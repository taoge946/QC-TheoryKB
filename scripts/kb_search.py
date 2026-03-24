"""
Math Theory KB Search - TF-IDF based semantic search.
No GPU needed, no dependency issues.

Usage:
    python kb_search.py build                              # Build index
    python kb_search.py "Uhlmann fidelity theorem"         # Search
    python kb_search.py "DDPM reverse process" --top_k 10  # Top 10
    python kb_search.py "stabilizer code" --show_text      # Show matched text
"""
import os, sys, json, glob, pickle, re
from pathlib import Path

KB_ROOT = Path(r"F:\数学定理推导")
INDEX_PATH = KB_ROOT / "scripts" / ".tfidf_index.pkl"

def chunk_text(text, source, chunk_size=600, overlap=150):
    chunks = []
    lines = text.split("\n")
    cur, cur_len, sec = [], 0, ""
    for line in lines:
        if line.startswith("## ") or line.startswith("### "):
            sec = line.strip("# ").strip()
        cur.append(line)
        cur_len += len(line) + 1
        if cur_len >= chunk_size:
            t = "\n".join(cur)
            chunks.append({"text": t, "source": source, "section": sec})
            ov, ov_len = [], 0
            for l in reversed(cur):
                if ov_len + len(l) > overlap: break
                ov.insert(0, l)
                ov_len += len(l) + 1
            cur, cur_len = ov, ov_len
    if cur and len("\n".join(cur).strip()) > 30:
        chunks.append({"text": "\n".join(cur), "source": source, "section": sec})
    return chunks

def collect_chunks():
    all_chunks = []
    # Derivation files
    for md in sorted(glob.glob(str(KB_ROOT / "**/derivations/*.md"), recursive=True)):
        rel = os.path.relpath(md, KB_ROOT).replace("\\", "/")
        with open(md, "r", encoding="utf-8") as f: text = f.read()
        all_chunks.extend(chunk_text(text, rel))
    # Key formulas
    for md in sorted(glob.glob(str(KB_ROOT / "*/key_formulas.md"))):
        rel = os.path.relpath(md, KB_ROOT).replace("\\", "/")
        with open(md, "r", encoding="utf-8") as f: text = f.read()
        all_chunks.extend(chunk_text(text, rel))
    # Top-level
    for name in ["INDEX.md", "NOTATION.md", "SEARCH_TAGS.md"]:
        fp = KB_ROOT / name
        if fp.exists():
            with open(fp, "r", encoding="utf-8") as f: text = f.read()
            all_chunks.extend(chunk_text(text, name))
    # Extracted text (larger chunks)
    for txt in sorted(glob.glob(str(KB_ROOT / "_extracted_text/*.txt"))):
        rel = os.path.relpath(txt, KB_ROOT).replace("\\", "/")
        with open(txt, "r", encoding="utf-8") as f: text = f.read()
        all_chunks.extend(chunk_text(text, rel, chunk_size=1200, overlap=200))
    return all_chunks

def build():
    from sklearn.feature_extraction.text import TfidfVectorizer
    print("Collecting chunks...")
    chunks = collect_chunks()
    n_files = len(set(c["source"] for c in chunks))
    print(f"  {len(chunks)} chunks from {n_files} files")
    texts = [c["text"] for c in chunks]
    print("Building TF-IDF index...")
    vectorizer = TfidfVectorizer(
        max_features=50000,
        ngram_range=(1, 2),
        sublinear_tf=True,
        strip_accents="unicode",
        token_pattern=r"(?u)\b\w[\w\-\.]+\b",  # keep hyphens, dots (e.g., "Knill-Laflamme", "Eq.11")
    )
    tfidf_matrix = vectorizer.fit_transform(texts)
    meta = [{"source": c["source"], "section": c["section"], "preview": c["text"][:200]} for c in chunks]
    full_texts = [c["text"] for c in chunks]
    data = {"vectorizer": vectorizer, "matrix": tfidf_matrix, "meta": meta, "texts": full_texts}
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(INDEX_PATH, "wb") as f:
        pickle.dump(data, f)
    print(f"Index saved: {len(chunks)} chunks, {n_files} files, {tfidf_matrix.shape[1]} features")

def search(query, top_k=5, show_text=False):
    with open(INDEX_PATH, "rb") as f:
        data = pickle.load(f)
    vec = data["vectorizer"]
    mat = data["matrix"]
    meta = data["meta"]
    texts = data["texts"]
    q_vec = vec.transform([query])
    scores = (mat @ q_vec.T).toarray().flatten()
    top_idx = scores.argsort()[::-1]
    results, seen = [], set()
    for i in top_idx:
        if scores[i] <= 0: break
        src = meta[i]["source"]
        if src in seen: continue
        seen.add(src)
        r = {"score": float(scores[i]), "source": src, "section": meta[i]["section"], "preview": meta[i]["preview"]}
        if show_text:
            r["text"] = texts[i]
        results.append(r)
        if len(results) >= top_k: break
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python kb_search.py build | \"query\" [--top_k N] [--show_text]")
        sys.exit(1)
    if sys.argv[1] == "build":
        build()
    else:
        q = sys.argv[1]
        tk = int(sys.argv[sys.argv.index("--top_k")+1]) if "--top_k" in sys.argv else 5
        st = "--show_text" in sys.argv
        results = search(q, tk, st)
        print(f"\n=== KB Search: \"{q}\" ===\n")
        for i, r in enumerate(results):
            print(f"{i+1}. [{r['score']:.3f}] {r['source']}")
            if r["section"]: print(f"   Section: {r['section']}")
            print(f"   {r['preview'][:120]}...")
            if st and "text" in r:
                print(f"   ---\n   {r['text'][:500]}\n   ---")
            print()
