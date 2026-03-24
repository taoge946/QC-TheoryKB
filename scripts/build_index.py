"""
Build FAISS vector index for the Math Theory KB.
Usage:
    python build_index.py          # Build/rebuild index
    python build_index.py search "Uhlmann fidelity theorem"
    python build_index.py search "DDPM reverse process" --top_k 5
"""
import os, sys, json, glob
import numpy as np
from pathlib import Path

KB_ROOT = Path(r"F:\数学定理推导")
INDEX_DIR = KB_ROOT / "scripts" / ".rag_index"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 200
MODEL_NAME = "all-MiniLM-L6-v2"

def chunk_text(text, source, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    lines = text.split("\n")
    cur, cur_len, sec = [], 0, ""
    for line in lines:
        if line.startswith("## ") or line.startswith("### "):
            sec = line.strip("# ").strip()
        cur.append(line)
        cur_len += len(line) + 1
        if cur_len >= chunk_size:
            chunks.append({"text": "\n".join(cur), "source": source, "section": sec})
            ov, ov_len = [], 0
            for l in reversed(cur):
                if ov_len + len(l) > overlap: break
                ov.insert(0, l)
                ov_len += len(l) + 1
            cur, cur_len = ov, ov_len
    if cur:
        t = "\n".join(cur)
        if len(t.strip()) > 50:
            chunks.append({"text": t, "source": source, "section": sec})
    return chunks

def collect_all_chunks():
    all_chunks = []
    for md in sorted(glob.glob(str(KB_ROOT / "**/derivations/*.md"), recursive=True)):
        rel = os.path.relpath(md, KB_ROOT)
        with open(md, "r", encoding="utf-8") as f: text = f.read()
        all_chunks.extend(chunk_text(text, rel))
    for md in sorted(glob.glob(str(KB_ROOT / "*/key_formulas.md"))):
        rel = os.path.relpath(md, KB_ROOT)
        with open(md, "r", encoding="utf-8") as f: text = f.read()
        all_chunks.extend(chunk_text(text, rel))
    for name in ["INDEX.md", "NOTATION.md", "SEARCH_TAGS.md"]:
        fp = KB_ROOT / name
        if fp.exists():
            with open(fp, "r", encoding="utf-8") as f: text = f.read()
            all_chunks.extend(chunk_text(text, name))
    for txt in sorted(glob.glob(str(KB_ROOT / "_extracted_text/*.txt"))):
        rel = os.path.relpath(txt, KB_ROOT)
        with open(txt, "r", encoding="utf-8") as f: text = f.read()
        all_chunks.extend(chunk_text(text, rel, chunk_size=1500, overlap=300))
    return all_chunks

def build_index():
    from sentence_transformers import SentenceTransformer
    import faiss
    print("Collecting chunks...")
    chunks = collect_all_chunks()
    print(f"  {len(chunks)} chunks from {len(set(c['source'] for c in chunks))} files")
    print(f"Loading model: {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    print("Encoding...")
    texts = [c["text"] for c in chunks]
    emb = model.encode(texts, show_progress_bar=True, batch_size=64).astype("float32")
    print(f"Building FAISS index (dim={emb.shape[1]})...")
    idx = faiss.IndexFlatIP(emb.shape[1])
    faiss.normalize_L2(emb)
    idx.add(emb)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    faiss.write_index(idx, str(INDEX_DIR / "kb.index"))
    meta = [{"source": c["source"], "section": c["section"], "preview": c["text"][:200], "full": c["text"]} for c in chunks]
    with open(INDEX_DIR / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False)
    print(f"Done: {len(chunks)} chunks, {len(set(c['source'] for c in chunks))} files")

def search(query, top_k=5):
    from sentence_transformers import SentenceTransformer
    import faiss
    idx = faiss.read_index(str(INDEX_DIR / "kb.index"))
    with open(INDEX_DIR / "metadata.json", "r", encoding="utf-8") as f: meta = json.load(f)
    model = SentenceTransformer(MODEL_NAME)
    qe = model.encode([query], convert_to_numpy=True).astype("float32")
    faiss.normalize_L2(qe)
    scores, indices = idx.search(qe, min(top_k * 3, len(meta)))
    results, seen = [], set()
    for s, i in zip(scores[0], indices[0]):
        if i < 0: continue
        m = meta[i]
        if m["source"] in seen: continue
        seen.add(m["source"])
        results.append({"score": float(s), "source": m["source"], "section": m["section"], "preview": m["preview"]})
        if len(results) >= top_k: break
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "build":
        build_index()
    elif sys.argv[1] == "search":
        q = sys.argv[2] if len(sys.argv) > 2 else ""
        tk = int(sys.argv[sys.argv.index("--top_k")+1]) if "--top_k" in sys.argv else 5
        for r in search(q, tk):
            print(f"[{r['score']:.3f}] {r['source']} | {r['section']}")
            print(f"  {r['preview'][:120]}...\n")
