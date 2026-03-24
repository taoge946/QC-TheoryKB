#!/usr/bin/env python3
"""Batch download all planned arXiv papers."""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from download_arxiv_source import download_source
import time

BASE = os.path.join(os.path.dirname(__file__), "..")

PAPERS = [
    # QEC papers
    {"id": "quant-ph/9705052", "dir": "04_quantum_error_correction/references/gottesman_thesis"},
    {"id": "1208.0928", "dir": "04_quantum_error_correction/references/fowler_surface_codes"},
    {"id": "quant-ph/0110143", "dir": "04_quantum_error_correction/references/dennis_topological_memory"},
    {"id": "quant-ph/9707021", "dir": "04_quantum_error_correction/references/kitaev_qec"},
    {"id": "2009.14794", "dir": "04_quantum_error_correction/references/roffe_qec_guide"},
    {"id": "1504.01444", "dir": "04_quantum_error_correction/references/terhal_qec_memories"},
    {"id": "2103.09347", "dir": "04_quantum_error_correction/references/breuckmann_qldpc"},
    {"id": "quant-ph/9604024", "dir": "04_quantum_error_correction/references/calderbank_css"},
    # Quantum info theory
    {"id": "1106.1445", "dir": "03_quantum_info_theory/references/wilde_shannon_theory"},
    # ML theory
    {"id": "2006.11239", "dir": "11_ml_theory/references/ho_ddpm"},
    {"id": "2011.13456", "dir": "11_ml_theory/references/song_score_sde"},
    # Graph theory
    {"id": "1901.00596", "dir": "07_graph_theory/references/gnn_survey"},
    # Topology
    {"id": "1311.0277", "dir": "08_topology/references/bombin_topological_codes"},
]

if __name__ == "__main__":
    success = 0
    failed = 0
    for paper in PAPERS:
        output_dir = os.path.normpath(os.path.join(BASE, paper["dir"]))
        print(f"\n{'='*60}")
        print(f"Downloading: {paper['id']} -> {paper['dir']}")
        try:
            result = download_source(paper["id"], output_dir)
            if result.get("success"):
                success += 1
            else:
                failed += 1
                print(f"  FAILED: {result.get('error')}")
        except Exception as e:
            failed += 1
            print(f"  ERROR: {e}")
        # Be polite to arXiv
        time.sleep(3)

    print(f"\n{'='*60}")
    print(f"Done: {success} succeeded, {failed} failed out of {len(PAPERS)}")
