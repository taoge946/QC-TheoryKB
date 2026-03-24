#!/usr/bin/env python3
"""Download and extract arXiv LaTeX source packages.

Usage:
    python download_arxiv_source.py <arxiv_id> <output_dir>

Examples:
    python download_arxiv_source.py 2006.11239 ../11_ml_theory/references/ho_ddpm
    python download_arxiv_source.py quant-ph/9705052 ../04_quantum_error_correction/references/gottesman_thesis
"""

import os
import sys
import tarfile
import gzip
import io
import urllib.request
import urllib.error
import json
from pathlib import Path
from datetime import datetime


def normalize_arxiv_id(arxiv_id: str) -> str:
    """Normalize arXiv ID for URL construction."""
    arxiv_id = arxiv_id.strip()
    # Remove any arxiv: prefix or URL
    for prefix in ["arxiv:", "https://arxiv.org/abs/", "https://arxiv.org/pdf/", "http://arxiv.org/abs/"]:
        if arxiv_id.lower().startswith(prefix):
            arxiv_id = arxiv_id[len(prefix):]
    # Remove version suffix like v1, v2
    if arxiv_id[-2] == 'v' and arxiv_id[-1].isdigit():
        arxiv_id = arxiv_id[:-2]
    return arxiv_id


def download_source(arxiv_id: str, output_dir: str) -> dict:
    """Download and extract arXiv source. Returns metadata dict."""
    arxiv_id = normalize_arxiv_id(arxiv_id)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    url = f"https://arxiv.org/e-print/{arxiv_id}"
    print(f"Downloading: {url}")

    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (research tool; mailto:lijt@baqis.ac.cn)"
    })

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            data = response.read()
            content_type = response.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        print(f"Error downloading {arxiv_id}: HTTP {e.code}")
        return {"success": False, "error": f"HTTP {e.code}"}
    except Exception as e:
        print(f"Error downloading {arxiv_id}: {e}")
        return {"success": False, "error": str(e)}

    print(f"Downloaded {len(data)} bytes, Content-Type: {content_type}")

    # Try to extract as tar.gz first
    tex_files = []
    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
            tar.extractall(path=str(output_path))
            tex_files = [m.name for m in tar.getmembers() if m.name.endswith(".tex")]
            print(f"Extracted tar.gz: {len(tar.getmembers())} files")
    except tarfile.TarError:
        # Maybe it's a single gzipped file
        try:
            decompressed = gzip.decompress(data)
            # Check if it looks like LaTeX
            text = decompressed.decode("utf-8", errors="replace")
            if "\\begin" in text or "\\document" in text:
                tex_path = output_path / "main.tex"
                tex_path.write_bytes(decompressed)
                tex_files = ["main.tex"]
                print("Extracted single gzipped .tex file")
            else:
                # Maybe plain tar (not gzipped)
                try:
                    with tarfile.open(fileobj=io.BytesIO(data), mode="r:") as tar:
                        tar.extractall(path=str(output_path))
                        tex_files = [m.name for m in tar.getmembers() if m.name.endswith(".tex")]
                        print(f"Extracted plain tar: {len(tar.getmembers())} files")
                except tarfile.TarError:
                    # Save raw data
                    raw_path = output_path / "source_raw"
                    raw_path.write_bytes(data)
                    print("Could not extract, saved raw data")
        except Exception:
            # Try plain tar
            try:
                with tarfile.open(fileobj=io.BytesIO(data), mode="r:") as tar:
                    tar.extractall(path=str(output_path))
                    tex_files = [m.name for m in tar.getmembers() if m.name.endswith(".tex")]
            except Exception:
                raw_path = output_path / "source_raw"
                raw_path.write_bytes(data)
                print("Could not extract, saved raw data")

    # Find main tex file
    main_tex = None
    if tex_files:
        # Prefer files with \documentclass
        for tf in tex_files:
            fpath = output_path / tf
            if fpath.exists():
                content = fpath.read_text(encoding="utf-8", errors="replace")
                if "\\documentclass" in content:
                    main_tex = tf
                    break
        if not main_tex:
            # Prefer 'main.tex' or the largest .tex file
            for name in ["main.tex", "paper.tex", "article.tex"]:
                if name in tex_files:
                    main_tex = name
                    break
            if not main_tex:
                main_tex = tex_files[0]

    metadata = {
        "arxiv_id": arxiv_id,
        "download_url": url,
        "download_date": datetime.now().isoformat(),
        "output_dir": str(output_path),
        "tex_files": tex_files,
        "main_tex": main_tex,
        "success": True
    }

    # Save metadata
    meta_path = output_path / "metadata.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    if main_tex:
        print(f"Main .tex file: {main_tex}")
    print(f"Output directory: {output_path}")

    return metadata


def batch_download(papers: list[dict]):
    """Download multiple papers. Each dict has 'id' and 'output_dir'."""
    results = []
    for paper in papers:
        print(f"\n{'='*60}")
        result = download_source(paper["id"], paper["output_dir"])
        results.append(result)
    return results


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    arxiv_id = sys.argv[1]
    output_dir = sys.argv[2]
    download_source(arxiv_id, output_dir)
