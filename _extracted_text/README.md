# Extracted Text Files -- Limitations and Usage Guide

## What These Files Are

Plain text files extracted from PDF textbooks and lecture notes using **PyMuPDF** (`fitz`).
Each file corresponds to one source PDF. Extraction was performed programmatically;
no manual correction has been applied.

## What They Are Good For

- **Keyword search**: Quickly locate where a topic, theorem name, or term appears.
- **Finding page numbers**: Every file contains `===== PAGE X =====` markers that correspond
  to the physical page numbers in the original PDF, making cross-referencing straightforward.
- **Locating theorem statements**: Identify which page/section a theorem, lemma, or definition
  lives on, then go to the original source for the precise statement.

## What They Are NOT Good For

**Do not copy mathematical formulas from these files.**

PyMuPDF text extraction does not understand LaTeX or MathML. Inline and display math is
garbled in extraction -- symbols are dropped, subscripts/superscripts are flattened,
summation/integral signs are lost or replaced, and multi-line equations collapse into
nonsensical character sequences. Any formula copied from these `.txt` files will almost
certainly be wrong.

## Where to Get Reliable Formulas

1. **`references/*.tex` files** (most reliable) -- LaTeX source from original papers.
   Formulas can be copied directly into your own `.tex` documents.
2. **Original PDFs** opened with a LaTeX-aware PDF reader -- read the typeset equations
   directly from the source.
3. **`derivations/*.md` files** -- curated derivation notes that cite the original sources
   with proper LaTeX formatting.

## Page Markers

Every extracted text file contains markers of the form:

```
===== PAGE 42 =====
```

These correspond to physical page numbers in the original PDF. Use them to jump to the
exact page when cross-referencing with the original document.

## File List

| File | Size | Source |
|------|------|--------|
| `nielsen_chuang.txt` | 798 KB | Nielsen & Chuang, *Quantum Computation and Quantum Information* (~710 pages) |
| `boyd.txt` | 361 KB | Boyd & Vandenberghe, *Convex Optimization* (~714 pages) |
| `watrous_tqi.txt` | 354 KB | Watrous, *The Theory of Quantum Information* (complete book) |
| `slofstra.txt` | 207 KB | Slofstra, *Linear Algebra for Quantum Computing* (~224 pages) |
| `preskill_ch7.txt` | 174 KB | Preskill, *Lecture Notes Ch.7* (Quantum Error Correction) |
| `preskill_ch3.txt` | 128 KB | Preskill, *Lecture Notes Ch.3* (Foundations of Quantum Theory II) |
| `preskill_ch4.txt` | 125 KB | Preskill, *Lecture Notes Ch.4* (Quantum Entanglement) |
| `preskill_ch5.txt` | 115 KB | Preskill, *Lecture Notes Ch.5* (Quantum Information Theory) |
| `preskill_ch2.txt` | 109 KB | Preskill, *Lecture Notes Ch.2* (Foundations of Quantum Theory) |
| `bacon.txt` | 92 KB | Bacon, *Quantum Error Correcting Codes* (lecture notes) |
| `steane.txt` | 81 KB | Steane, *Quantum Error Correction* |
| `surface_notes.txt` | 53 KB | Surface code lecture notes / tutorial |
| `linalg_qc.txt` | 51 KB | Linear algebra for quantum computing (supplementary notes) |
| `nordiquest.txt` | 17 KB | Nordiquest notes (short reference) |

## Known Extraction Issues

- **Nielsen & Chuang (`nielsen_chuang.txt`)**: Some formatting loss. The book uses
  extensive inline math and boxed equations; many of these are partially or fully garbled.
  Chapter/section headings are mostly intact but exercise numbering can be disrupted.
- **Boyd & Vandenberghe (`boyd.txt`)**: Formatting loss in optimization problem
  formulations (the "minimize ... subject to ..." blocks). Matrix expressions and
  constraint sets are frequently mangled. Figures and tables are lost entirely.
- **Preskill lecture notes**: Generally cleaner extraction since the originals are
  TeX-produced with simpler layouts, but complex bra-ket notation and tensor product
  expressions still suffer.
- **All files**: Figures, diagrams, and tables are not captured. Only raw text survives
  the extraction process.
