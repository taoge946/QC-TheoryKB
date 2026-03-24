# QC-TheoryKB

### Structured Mathematical Derivation Library for AI-Assisted Quantum Computing Research / 面向AI辅助量子计算研究的结构化数学推导库

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
![Files](https://img.shields.io/badge/derivation%20files-99-blue)
![Formulas](https://img.shields.io/badge/key%20formulas-323+-green)
![Search Tags](https://img.shields.io/badge/search%20tags-314-orange)

---

## What Is This?

A structured reference library of **mathematical derivations** covering quantum computing, machine learning, and their intersection. Every derivation is written as a self-contained Markdown note with:

- Step-by-step proofs with inline citations (`[Author, Theorem X.Y, p.Z]`)
- LaTeX formulas ready to copy into papers
- Cross-references to prerequisite derivations
- Tags for search and discovery

Designed to be used by **LLM coding assistants** (Claude Code, Cursor, Copilot, etc.) for rigorous paper writing --- but equally useful for humans browsing directly.

## Why This Exists

Researchers working at the intersection of quantum computing and machine learning frequently need to write theory sections that draw on results from multiple fields (quantum information, optimization, graph theory, ML theory, etc.). Tracking down the right theorem statement, understanding its proof, and formatting it correctly for a paper is time-consuming.

This KB provides **building blocks for constructing new proofs**, not just a lookup table of existing ones. The `BUILDING_BLOCKS.md` file maps proof goals to the specific formulas and derivation files you need.

## Key Statistics

| Metric | Count |
|--------|-------|
| Topic directories | 18 (+ 2 empty placeholders) |
| Derivation files | 99 |
| Key formula entries | 323+ |
| Inline citations | 1,400+ |
| Search tags | 314 |
| Reference source packages (LaTeX) | 36 directories, 187 .tex files |
| Extracted text files | 15 (from PDF textbooks) |

---

## Directory Structure

| # | Topic | Derivations | Formulas | Key References |
|---|-------|:-----------:|:--------:|----------------|
| 01 | Linear Algebra | 5 | 15 | Slofstra, Portugal, Nielsen & Chuang |
| 02 | Quantum Mechanics | 6 | 15 | Nielsen & Chuang, Preskill Ch.2--4 |
| 03 | Quantum Information Theory | 10 | 36 | Watrous, Wilde, Preskill Ch.5 |
| 04 | Quantum Error Correction | 13 | 20 | Gottesman, Fujii, Roffe, Dennis, Kitaev, Breuckmann, Steane, Preskill Ch.7 |
| 05 | Variational Quantum | 7 | 17 | Farhi (QAOA), Cerezo (VQA), Tilly (VQE) |
| 06 | Group Theory | 4 | 16 | Gottesman thesis |
| 07 | Graph Theory | 4 | 15 | GNN Survey (Wu et al.), GCN/GAT/GIN |
| 08 | Topology | 4 | 12 | Bombin, Dennis, Kitaev |
| 10 | Optimization | 8 | 34 | Boyd (Convex Optimization), Cappart (GNN+CO), Bengio (ML4CO) |
| 11 | ML Theory | 13 | 54 | DDPM, DDIM, D3PM, Score SDE, Flow Matching, DiGress, DIFUSCO, VAE, GAN, PPO, Adam, Transformer, Attention Mechanism |
| 12 | ZX-Calculus | 4 | 15 | Coecke & Duncan, van de Wetering, Kissinger |
| 13 | Quantum Compilation & Routing | 3 | 10 | SABRE, OLSQ, Solovay-Kitaev |
| 14 | Scheduling Theory | 3 | 10 | Graham, Tomita, Fowler |
| 15 | Quantum Hardware | 3 | 12 | Koch (transmon), Arute (XEB), Cross (QV) |
| 16 | Statistical Mechanics | 3 | 12 | Onsager, Dennis (RBIM), Nishimori |
| 17 | Experimental Methods | 3 | 10 | Fisher, Wilcoxon, bootstrap |
| 18 | Proof Techniques Arsenal | 6 | 20 | Concentration inequalities, matrix concentration, PAC/VC, coupling, probabilistic method, quantum proof toolkit |
| | **Total** | **99** | **323** | |

Placeholder directories (reserved, no content yet): `05_coding_theory/`, `09_probability_statistics/`

---

## How to Use

### For Humans

Browse the master index:

```
INDEX.md          -- Full table of contents with links to every derivation
SEARCH_TAGS.md    -- 314 tags mapped to derivation files (ctrl+F friendly)
NOTATION.md       -- Notation comparison table (N&C vs Watrous vs Preskill vs Gottesman)
GLOSSARY.md       -- 120+ terms with definitions, Chinese translations, and paper phrasings
BUILDING_BLOCKS.md -- "What can I prove with this?" Reverse index from proof goals to KB tools
```

### For LLMs / AI Coding Assistants

1. **Semantic search** (recommended):
   ```bash
   python scripts/kb_search.py "Uhlmann fidelity theorem"
   python scripts/kb_search.py "DDPM reverse process" --top_k 10
   python scripts/kb_search.py "stabilizer code syndrome" --show_text
   ```

2. **Index-based lookup**: Read `INDEX.md` to find the relevant topic, then read the specific derivation file.

3. **Tag search**: Search `SEARCH_TAGS.md` for a keyword to find all related files.

4. **Building blocks workflow**: Read `BUILDING_BLOCKS.md` to map your proof goal to the specific formulas (F-codes) and derivation files.

### For Paper Writing

Follow this workflow:

1. Identify your proof goal in `BUILDING_BLOCKS.md`
2. Read the referenced derivation files for the step-by-step proof
3. Copy LaTeX formulas from the derivation notes or from `references/*.tex`
4. Cite the original source using the inline citation provided (e.g., `[Watrous, Theorem 3.25]`)
5. Cross-check notation using `NOTATION.md`

---

## Key Files

| File | Purpose |
|------|---------|
| `INDEX.md` | Master table of contents -- every derivation file listed with links |
| `SEARCH_TAGS.md` | 314 search tags mapped to derivation files |
| `NOTATION.md` | Notation comparison across major textbooks |
| `GLOSSARY.md` | 120+ terms with definitions and standard paper phrasings |
| `BUILDING_BLOCKS.md` | Reverse index: proof goals to KB tools and formula codes |
| `scripts/kb_search.py` | TF-IDF semantic search over all derivation files |

---

## Sources

### Parsed LaTeX Sources (30+ papers)

All original LaTeX source files are in `references/` subdirectories within each topic. These can be read directly for exact formula verification.

**Quantum Error Correction**: Gottesman thesis (1997), Fujii book (9 chapters), Roffe QEC guide (2019), Dennis et al. topological memory (2002), Kitaev QEC (1997), Calderbank-Shor-Steane CSS codes (1996), Breuckmann QLDPC (2021), Terhal QEC memories (2015), Bombin topological codes (2013)

**Quantum Information**: Wilde, From Classical to Quantum Shannon Theory (44K lines of LaTeX)

**Machine Learning**: Ho et al. DDPM (2020), Song et al. Score SDE (2021), Austin et al. D3PM (2021), Song et al. DDIM (2021), Lipman et al. Flow Matching (2023), Vignac et al. DiGress (2023), Sun et al. DIFUSCO (2023), Kingma & Welling VAE (2014), Goodfellow et al. GAN (2014), Vaswani et al. Transformer (2017), Kool et al. Attention Model (2019)

**Variational Quantum**: Farhi et al. QAOA (2014), Cerezo et al. VQA review (2021), Tilly et al. VQE review (2022)

**Graph Theory**: Wu et al. GNN Survey (2020), Kipf & Welling GCN (2017), Velickovic et al. GAT (2018), Xu et al. GIN (2019)

**Optimization**: Cappart et al. GNN+CO (2023), Bengio et al. ML4CO (2021)

### Textbooks (extracted text in `_extracted_text/`)

| Textbook | Pages | Notes |
|----------|:-----:|-------|
| Nielsen & Chuang, *Quantum Computation and Quantum Information* | ~710 | The standard reference |
| Boyd & Vandenberghe, *Convex Optimization* | ~714 | Optimization theory |
| Watrous, *The Theory of Quantum Information* | full | Rigorous quantum info |
| Preskill, *Lecture Notes* Ch.2--5, 7 | ~500 | QM, entanglement, QIT, QEC |
| Slofstra, *Linear Algebra for Quantum Computing* | ~224 | Linear algebra foundations |
| Steane, *Quantum Error Correction* | -- | QEC lecture notes |
| Bacon, *Intro to Quantum Error Correcting Codes* | -- | QEC lecture notes |

> **Note**: The extracted text files (`_extracted_text/*.txt`) are derived from PDFs and are not included in this repository due to size and copyright considerations. See `_extracted_text/README.md` for details on what they contain and their limitations.

---

## Search

The built-in search uses TF-IDF (no GPU, no external API needed):

```bash
# First time: build the index
python scripts/kb_search.py build

# Search
python scripts/kb_search.py "quantum channel capacity"
python scripts/kb_search.py "surface code threshold" --top_k 10
python scripts/kb_search.py "barren plateau" --show_text
```

Requirements: Python 3.8+ with `scikit-learn` (for TF-IDF). No other dependencies.

---

## Contributing

### Adding a New Topic

1. Create a directory: `XX_topic_name/` with subdirectories `derivations/` and `references/`
2. Write `key_formulas.md` with numbered formula entries (e.g., `FXX.1`, `FXX.2`, ...)
3. Write derivation files in `derivations/` following the template:
   - YAML-style header with tags
   - Statement section
   - Prerequisites with links to other KB files
   - Step-by-step derivation with inline citations
   - Key references at the end
4. Add search tags to the top of each file: `> **Tags**: \`tag1\`, \`tag2\`, ...`
5. Run `python scripts/kb_search.py build` to rebuild the search index

### Adding a New Derivation to an Existing Topic

1. Create `XX_topic/derivations/your_derivation.md`
2. Add the formula entries to `XX_topic/key_formulas.md`
3. Rebuild the search index

---

## Citation

If you find this resource useful in your research, please cite:

```bibtex
@misc{qc-theorykb,
  title  = {QC-TheoryKB: Structured Mathematical Derivation Library for Quantum Computing Research},
  author = {Jintao Li},
  year   = {2026},
  url    = {https://github.com/your-username/QC-TheoryKB},
  note   = {A structured reference library of mathematical derivations covering quantum computing, machine learning, and optimization}
}
```

---

## License

This work is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

- **Derivation notes** (all `.md` files): Original educational content, CC BY-SA 4.0
- **Reference LaTeX sources** (`references/*.tex`): Downloaded from arXiv under arXiv's redistribution license. Original authors retain copyright.
- **Scripts** (`scripts/*.py`): CC BY-SA 4.0

You are free to share and adapt this material for any purpose, including commercial, as long as you give appropriate credit and distribute your contributions under the same license.
