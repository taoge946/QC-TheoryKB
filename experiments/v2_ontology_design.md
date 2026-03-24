# QC-TheoryKB v2.0 Ontology Design

> **Source**: GPT-5.4 review + Claude analysis, 2026-03-24
> **Status**: Design draft — not yet implemented

---

## Core Design: 3-Axis Indexing

Every KB entry is indexed along three independent axes:

### Axis A — Claim Type (what are you trying to prove?)
`BOUND.UPPER`, `BOUND.LOWER`, `CORRECTNESS`, `EQUIVALENCE`, `CONVERGENCE`, `APPROXIMATION`, `STABILITY`, `SAMPLE_COMPLEXITY`, `GENERALIZATION`, `FINITE_SIZE`, `STATISTICAL_VALIDATION`, `EXPRESSIVENESS`, `LIMITATION`, `DERIVATION`, `MONOTONICITY`

### Axis B — Domain (what subject area?)
- **QC**: `QC.QINFO`, `QC.QEC`, `QC.CHANNEL`, `QC.SIM`, `QC.COMPILATION`, `QC.OPT`, `QC.COMPLEXITY`, `QC.TN`, `QC.VQA`
- **ML**: `ML.DIFFUSION`, `ML.GNN`, `ML.RL`, `ML.OPT`, `ML.GEN`
- **MATH**: `MATH.MATRIX`, `MATH.CONCENTRATION`, `MATH.LINALG`, `MATH.OPT`, `MATH.PROB`
- **STATS**: `STATS.EXPERIMENT`

### Axis C — Artifact Type (what are you retrieving?)
`THEOREM`, `LEMMA`, `DERIVATION`, `IDENTITY`, `COUNTEREXAMPLE`, `PROOF_TEMPLATE`, `EXPERIMENTAL_PROTOCOL`, `STATISTICAL_TEST`, `CANONICAL_CHAIN`

---

## Semantic ID Scheme

Format: `<DOMAIN>.<SUBDOMAIN>.<OBJECT_NAME>.<VERSION>`

### Legacy Alias Mapping
```yaml
aliases:
  F4.1: QC.QEC.KNILL_LAFLAMME.01
  F3.13: QC.CHANNEL.FUCHS_VAN_DE_GRAAF.01
  F3.20: QC.CHANNEL.DATA_PROCESSING.01
  F10.13: QC.OPT.QUBO_ISING_EQUIV.01
  F11.4: ML.DIFFUSION.DDPM_SIMPLE_LOSS.01
  F11.31: ML.GNN.GIN_EQ_1WL.01
  F11.32: ML.GNN.MPNN_LEQ_1WL.01
  F11.49: ML.RL.REINFORCE_GRADIENT.01
  F17.3: STATS.EXPERIMENT.PAIRED_NONPARAMETRIC.01
```

---

## 10 Domain-Agnostic Proof Patterns (replacing current Part 2)

1. **PATTERN.REDUCTION_COMPLETENESS** — Reduce known hard problem → preserve structure → conclude hardness
2. **PATTERN.MONOTONICITY_INFORMATION** — Define quantity → apply DPI/contractivity → conclude bound
3. **PATTERN.VARIATIONAL_DECOMPOSITION** — Start from objective → decompose → isolate terms → optimize surrogate
4. **PATTERN.RELAXATION_ROUNDING** — Relax problem → solve surrogate → round/project → bound gap
5. **PATTERN.PERTURBATION_STABILITY** — Define ideal → inject perturbation → propagate via Lipschitz → conclude robustness
6. **PATTERN.CONCENTRATION_FINITE_SAMPLE** — Define estimator → concentration inequality → finite-sample bound
7. **PATTERN.ACHIEVABILITY_CONVERSE** — Construct scheme → prove achievability → prove converse → characterize gap
8. **PATTERN.CANONICAL_FORM_EQUIVALENCE** — Show transformation preserves semantics → map to normal form
9. **PATTERN.ASYMPTOTIC_TO_FINITE_SIZE** — Leading-order scaling → remainder bound → finite-size correction
10. **PATTERN.MECHANISM_ISOLATION** — Decompose method → controlled comparisons → quantify component effects

---

## Citation Verification Layer (prevent phantom citations)

### 3 Layers
1. **Source typing**: `primary_original`, `secondary_textbook`, `survey`, `unverified_memory`
2. **Locator granularity**: edition, chapter, section, theorem/eq number, page range, verified status
3. **Verification status**: `citation_checked`, `theorem_number_checked`, `page_checked`

### 6 Rules
1. Never cite theorem numbers from memory — only after checking exact edition
2. Store one original-source + one pedagogical-source citation per theorem
3. Add `citation_status` banner to every markdown file
4. Maintain centralized `citations.yaml` registry
5. Add CI lint pass (ID uniqueness, citation key existence, verified status)
6. Add citation confidence badge: VERIFIED / PARTIALLY VERIFIED / UNVERIFIED

---

## Proposed File Layout
```
kb/
  entries/           # YAML metadata per theorem
  derivations/       # Markdown derivation files
  patterns/          # Proof pattern templates
  sources/           # citations.yaml
  indexes/           # BUILDING_BLOCKS.md (auto-generated)
  scripts/           # lint_kb.py, build_index.py
```

---

## Implementation Priority

### Phase 1 (Mandatory for v2.0)
- [ ] Move from flat F-codes to semantic IDs with alias mapping
- [ ] Split indexing into claim type / domain / artifact type
- [ ] Replace Part 2 with 10 domain-agnostic proof patterns
- [ ] Add structured metadata files (YAML)
- [ ] Add citation verification status fields
- [ ] Add lint_kb.py

### Phase 2 (High Value)
- [ ] Add source registry (citations.yaml) with edition-aware textbook entries
- [ ] Separate theorem statements from derivation walkthroughs
- [ ] Add "don't use when" and "failure modes" to every important entry
- [ ] Add missing backbone modules: quantum complexity, simulation, tensor networks, security, concentration/matrix inequalities

### Phase 3 (Nice to Have)
- [ ] Auto-generate BUILDING_BLOCKS.md from metadata
- [ ] Prerequisite DAG with "shortest route" computation
- [ ] CI integration with GitHub Actions
