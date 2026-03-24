# Math Theory Derivation Library — Master Index

> **Purpose**: Formula derivations and cross-references for paper writing
> **Format**: Derivation notes (Markdown) + original papers/textbooks (tex/PDF)
> **Last updated**: 2026-03-24
> **Auto-generated**: Rebuilt from filesystem scan

---

## Statistics

| Metric | Count |
|--------|-------|
| Topic directories | 17 (+ 2 empty placeholders) |
| Derivation files | 99 |
| Key formula entries | 323 |
| Reference source packages (tex) | 36 directories |
| Reference PDFs (standalone textbooks) | 13 |
| Extracted text files | 15 |
| Total tex files | 187 |

---

## Quick Navigation

| # | Topic | Derivations | Formulas | Key References |
|---|-------|-------------|----------|----------------|
| [01](#01-linear-algebra) | Linear Algebra | 5 | 15 | Slofstra, Portugal, N&C |
| [02](#02-quantum-mechanics) | Quantum Mechanics | 6 | 15 | N&C, Preskill ch2-4 |
| [03](#03-quantum-information-theory) | Quantum Information Theory | 10 | 36 | Watrous, Wilde, Preskill ch5 |
| [04](#04-quantum-error-correction) | Quantum Error Correction | 13 | 20 | Gottesman, Fujii, Roffe, Dennis, Kitaev, Breuckmann, Terhal, Steane, Bacon, Preskill ch7 |
| [05](#05-variational-quantum) | Variational Quantum | 7 | 17 | Farhi QAOA, Cerezo VQA, Tilly VQE |
| [06](#06-group-theory) | Group Theory | 4 | 16 | Gottesman thesis |
| [07](#07-graph-theory) | Graph Theory | 4 | 15 | GNN Survey (Wu et al.), GCN/GAT/GIN |
| [08](#08-topology) | Topology | 4 | 12 | Bombin, Dennis, Kitaev |
| [10](#10-optimization) | Optimization | 8 | 34 | Boyd Convex Opt, Cappart GNN+CO, Bengio ML4CO |
| [11](#11-ml-theory) | ML Theory | 13 | 54 | DDPM/DDIM/D3PM/ScoreSDE/FlowMatching/DiGress/DIFUSCO/VAE/GAN/PPO/Adam/Transformer/AM |
| [12](#12-zx-calculus) | ZX-Calculus | 4 | 15 | Coecke & Duncan, van de Wetering, Kissinger, Backens, Duncan et al. |
| [13](#13-quantum-compilation) | Quantum Compilation & Routing | 3 | 10 | SABRE, OLSQ, Siraichi, Cowtan, Miltzow, Solovay-Kitaev |
| [14](#14-scheduling-theory) | Scheduling Theory | 3 | 10 | Graham, Brooks, Tomita, Fowler, Maslov |
| [15](#15-quantum-hardware) | Quantum Hardware | 3 | 12 | Koch transmon, Arute XEB, Cross QV, IBM CLOPS |
| [16](#16-statistical-mechanics) | Statistical Mechanics | 3 | 12 | Onsager, Dennis RBIM, Nishimori, Grimmett percolation |
| [17](#17-experimental-methods) | Experimental Methods | 3 | 10 | Fisher/Wilcoxon/bootstrap, experiment design, reporting |
| [18](#18-proof-techniques-arsenal) | Proof Techniques Arsenal | 6 | 20 | Concentration ineq., Matrix conc., PAC/VC/Rademacher, Coupling, Probabilistic method, Quantum toolkit |
| | **TOTAL** | **99** | **323** | |

---

## 01 Linear Algebra

**Key Formulas**: [key_formulas.md](01_linear_algebra/key_formulas.md) -- 15 formulas (F1.1--F1.15)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [matrix_exponential.md](01_linear_algebra/derivations/matrix_exponential.md) | Matrix Exponential and Applications |
| 2 | [spectral_decomposition.md](01_linear_algebra/derivations/spectral_decomposition.md) | Spectral Decomposition |
| 3 | [svd_and_polar_decomposition.md](01_linear_algebra/derivations/svd_and_polar_decomposition.md) | SVD and Polar Decomposition |
| 4 | [tensor_product_properties.md](01_linear_algebra/derivations/tensor_product_properties.md) | Tensor Product Properties |
| 5 | [trace_and_partial_trace.md](01_linear_algebra/derivations/trace_and_partial_trace.md) | Trace and Partial Trace |

**References (PDF)**:
- `references/slofstra_linalg_quantum.pdf` -- Slofstra, Linear Algebra for Quantum Computing (224p)
- `references/linear_algebra_for_qc.pdf` -- Portugal, Linear Algebra for QC

**Extracted text**: `_extracted_text/slofstra.txt`, `_extracted_text/linalg_qc.txt`

---

## 02 Quantum Mechanics

**Key Formulas**: [key_formulas.md](02_quantum_mechanics/key_formulas.md) -- 15 formulas (F2.1--F2.15)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [density_matrix_formalism.md](02_quantum_mechanics/derivations/density_matrix_formalism.md) | Density Matrix Formalism |
| 2 | [fidelity_and_trace_distance.md](02_quantum_mechanics/derivations/fidelity_and_trace_distance.md) | Fidelity and Trace Distance |
| 3 | [measurement_theory.md](02_quantum_mechanics/derivations/measurement_theory.md) | Quantum Measurement Theory (POVM) |
| 4 | [quantum_channels_kraus.md](02_quantum_mechanics/derivations/quantum_channels_kraus.md) | Quantum Channels and Kraus Representation |
| 5 | [schmidt_decomposition.md](02_quantum_mechanics/derivations/schmidt_decomposition.md) | Schmidt Decomposition |
| 6 | [von_neumann_entropy.md](02_quantum_mechanics/derivations/von_neumann_entropy.md) | Von Neumann Entropy and Related Quantities |

**References (PDF)**:
- `references/nielsen_chuang.pdf` -- Nielsen & Chuang (710p)
- `references/preskill_ch2.pdf` -- Preskill Ch.2
- `references/preskill_ch3.pdf` -- Preskill Ch.3
- `references/preskill_ch4.pdf` -- Preskill Ch.4

**Extracted text**: `_extracted_text/nielsen_chuang.txt`, `_extracted_text/preskill_ch2.txt`, `_extracted_text/preskill_ch3.txt`, `_extracted_text/preskill_ch4.txt`

---

## 03 Quantum Information Theory

**Key Formulas**: [key_formulas.md](03_quantum_info_theory/key_formulas.md) -- 36 formulas (Watrous Ch.1--7 + Wilde W1--W8)

| # | Derivation | Title | Source |
|---|-----------|-------|--------|
| 1 | [classical_information_theory.md](03_quantum_info_theory/derivations/classical_information_theory.md) | Classical Information Theory | Wilde |
| 2 | [entanglement_theory.md](03_quantum_info_theory/derivations/entanglement_theory.md) | Entanglement Theory | Watrous Ch.7 |
| 3 | [entropy_inequalities.md](03_quantum_info_theory/derivations/entropy_inequalities.md) | Quantum Entropy Inequalities | Wilde |
| 4 | [holevo_bound.md](03_quantum_info_theory/derivations/holevo_bound.md) | Holevo Bound and Classical Capacity | Wilde |
| 5 | [quantum_capacity.md](03_quantum_info_theory/derivations/quantum_capacity.md) | Quantum Capacity and Coherent Information | Wilde |
| 6 | [quantum_channel_capacity.md](03_quantum_info_theory/derivations/quantum_channel_capacity.md) | Quantum Channel Capacities | Watrous Ch.6 |
| 7 | [quantum_data_processing.md](03_quantum_info_theory/derivations/quantum_data_processing.md) | Quantum Data Processing Inequalities | Wilde Ch.11--12 |
| 8 | [quantum_discrimination.md](03_quantum_info_theory/derivations/quantum_discrimination.md) | Quantum State Discrimination | Watrous Ch.4 |
| 9 | [quantum_entropy_advanced.md](03_quantum_info_theory/derivations/quantum_entropy_advanced.md) | Quantum Entropy: Advanced Theory | Watrous Ch.5 |
| 10 | [sdp_quantum_info.md](03_quantum_info_theory/derivations/sdp_quantum_info.md) | Semidefinite Programming in QI | Watrous Ch.3 |

**References (tex + PDF)**:
- `references/watrous_tqi/` -- Watrous, *Theory of Quantum Information* (PDF)
- `references/wilde_shannon_theory/` -- Wilde, *From Classical to Quantum Shannon Theory* (tex: `qit-notes.tex`)
- `references/preskill_ch5.pdf` -- Preskill Ch.5

**Extracted text**: `_extracted_text/watrous_tqi.txt`, `_extracted_text/preskill_ch5.txt`

---

## 04 Quantum Error Correction

**Key Formulas**: [key_formulas.md](04_quantum_error_correction/key_formulas.md) -- 20 formulas (F4.1--F4.20)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [anyonic_models.md](04_quantum_error_correction/derivations/anyonic_models.md) | Anyonic Models and Topological QC |
| 2 | [code_distance_bounds.md](04_quantum_error_correction/derivations/code_distance_bounds.md) | Quantum Code Distance Bounds |
| 3 | [css_codes.md](04_quantum_error_correction/derivations/css_codes.md) | CSS Code Construction |
| 4 | [decoder_theory.md](04_quantum_error_correction/derivations/decoder_theory.md) | Decoding Problem and Main Approaches |
| 5 | [fault_tolerant_gates.md](04_quantum_error_correction/derivations/fault_tolerant_gates.md) | Fault-Tolerant Gate Operations |
| 6 | [knill_laflamme_conditions.md](04_quantum_error_correction/derivations/knill_laflamme_conditions.md) | Knill-Laflamme QEC Conditions |
| 7 | [magic_state_distillation.md](04_quantum_error_correction/derivations/magic_state_distillation.md) | Magic State Distillation |
| 8 | [noise_models.md](04_quantum_error_correction/derivations/noise_models.md) | Noise Models for QEC |
| 9 | [quantum_ldpc_codes.md](04_quantum_error_correction/derivations/quantum_ldpc_codes.md) | Quantum LDPC Codes |
| 10 | [stabilizer_formalism.md](04_quantum_error_correction/derivations/stabilizer_formalism.md) | Stabilizer Formalism |
| 11 | [surface_code_basics.md](04_quantum_error_correction/derivations/surface_code_basics.md) | Surface Code Basics |
| 12 | [threshold_theorem.md](04_quantum_error_correction/derivations/threshold_theorem.md) | Threshold Theorem |
| 13 | [topological_mbqc.md](04_quantum_error_correction/derivations/topological_mbqc.md) | Topological Measurement-Based QC |

**References (tex)**:
- `references/gottesman_thesis/` -- Gottesman PhD thesis (`Thesis.tex`)
- `references/breuckmann_qldpc/` -- Breuckmann, LDPC Quantum Codes (`main.tex` + 12 tikz files)
- `references/calderbank_css/` -- Calderbank & Shor, CSS codes (`EPP30.tex`)
- `references/dennis_topological_memory/` -- Dennis et al., Topological quantum memory (`toric.tex`)
- `references/kitaev_qec/` -- Kitaev, Fault-tolerant QC by anyons (`anyons.tex`)
- `references/roffe_qec_guide/` -- Roffe, QEC guide (`cp_review_arxiv.tex`)
- `references/terhal_qec_memories/` -- Terhal, QEC for quantum memories (`book.tex` + 8 chapter files)
- `references/fowler_surface_codes/` -- Fowler et al., Surface codes (metadata + raw source)

**References (PDF)**:
- `references/bacon_intro_qec.pdf` -- Bacon, Intro to QEC
- `references/nordiquest_qec_practical.pdf` -- Nordiquest, Practical QEC
- `references/preskill_ch7.pdf` -- Preskill Ch.7
- `references/steane_qec_tutorial.pdf` -- Steane, QEC tutorial
- `references/surface_code_notes.pdf` -- Surface code lecture notes

**Extracted text**: `_extracted_text/bacon.txt`, `_extracted_text/nordiquest.txt`, `_extracted_text/preskill_ch7.txt`, `_extracted_text/steane.txt`, `_extracted_text/surface_notes.txt`

---

## 05 Variational Quantum

**Key Formulas**: [key_formulas.md](05_variational_quantum/key_formulas.md) -- 17 formulas (F5.1--F5.17)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [adapt_vqe.md](05_variational_quantum/derivations/adapt_vqe.md) | ADAPT-VQE and Adaptive Ansatz |
| 2 | [barren_plateaus.md](05_variational_quantum/derivations/barren_plateaus.md) | Barren Plateaus Theory |
| 3 | [error_mitigation.md](05_variational_quantum/derivations/error_mitigation.md) | Quantum Error Mitigation |
| 4 | [qaoa_theory.md](05_variational_quantum/derivations/qaoa_theory.md) | QAOA Theory |
| 5 | [quantum_natural_gradient.md](05_variational_quantum/derivations/quantum_natural_gradient.md) | Quantum Natural Gradient |
| 6 | [vqe_theory.md](05_variational_quantum/derivations/vqe_theory.md) | VQE Theory |
| 7 | [warm_starting_strategies.md](05_variational_quantum/derivations/warm_starting_strategies.md) | Warm-Starting Strategies |

**References (tex)**:
- `references/cerezo_vqa_review/` -- Cerezo et al., VQA review (`main.tex`)
- `references/farhi_qaoa/` -- Farhi et al., QAOA (`QuantAlgor.tex`)
- `references/tilly_vqe/` -- Tilly et al., VQE review (`main.tex` + 10 section files)

---

## 06 Group Theory

**Key Formulas**: [key_formulas.md](06_group_theory/key_formulas.md) -- 16 formulas (F6.1--F6.16)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [clifford_group.md](06_group_theory/derivations/clifford_group.md) | Clifford Group |
| 2 | [group_theory_basics.md](06_group_theory/derivations/group_theory_basics.md) | Essential Group Theory for QC |
| 3 | [pauli_group.md](06_group_theory/derivations/pauli_group.md) | Pauli Group Structure |
| 4 | [symplectic_representation.md](06_group_theory/derivations/symplectic_representation.md) | Symplectic Representation of Stabilizer Codes |

**References**: Uses Gottesman thesis from `04_quantum_error_correction/references/gottesman_thesis/`

---

## 07 Graph Theory

**Key Formulas**: [key_formulas.md](07_graph_theory/key_formulas.md) -- 15 formulas

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [graph_algorithms.md](07_graph_theory/derivations/graph_algorithms.md) | Graph Algorithms: Complexity and Correctness |
| 2 | [spectral_graph_theory.md](07_graph_theory/derivations/spectral_graph_theory.md) | Spectral Graph Theory |
| 3 | [tanner_graphs.md](07_graph_theory/derivations/tanner_graphs.md) | Tanner Graphs: Classical to QEC |
| 4 | [wl_test_expressiveness.md](07_graph_theory/derivations/wl_test_expressiveness.md) | Weisfeiler-Leman Test and GNN Expressiveness |

**References (tex)**:
- `references/gnn_survey/` -- Wu et al., GNN Survey (`content.tex`, `sup_full.tex`, `supplemental.tex`)

---

## 08 Topology

**Key Formulas**: [key_formulas.md](08_topology/key_formulas.md) -- 12 formulas (F8.1--F8.12)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [cohomology_basics.md](08_topology/derivations/cohomology_basics.md) | Cohomology Basics for Quantum Codes |
| 2 | [euler_characteristic.md](08_topology/derivations/euler_characteristic.md) | Euler Characteristic and Code Parameters |
| 3 | [homology_basics.md](08_topology/derivations/homology_basics.md) | Homology Theory for Topological Codes |
| 4 | [topological_codes_connection.md](08_topology/derivations/topological_codes_connection.md) | How Homology Connects to QEC Codes |

**References (tex)**:
- `references/bombin_topological_codes/` -- Bombin, Topological Codes (`QEC_Book-Topological_Codes.tex`)

---

## 10 Optimization

**Key Formulas**: [key_formulas.md](10_optimization/key_formulas.md) -- 34 formulas

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [convex_optimization_basics.md](10_optimization/derivations/convex_optimization_basics.md) | Convex Optimization: Sets, Functions, Problems |
| 2 | [duality_kkt.md](10_optimization/derivations/duality_kkt.md) | Lagrangian Duality and KKT Conditions |
| 3 | [gradient_methods.md](10_optimization/derivations/gradient_methods.md) | Gradient Methods, Newton, Interior Point |
| 4 | [lattice_surgery_compilation_bounds.md](10_optimization/derivations/lattice_surgery_compilation_bounds.md) | Lattice Surgery Compilation: Volume Lower Bounds |
| 5 | [neural_co_theory.md](10_optimization/derivations/neural_co_theory.md) | Neural Combinatorial Optimization Theory |
| 6 | [np_hard_problems.md](10_optimization/derivations/np_hard_problems.md) | NP-Hard Problems: Definitions and Reductions |
| 7 | [qubo_ising_mapping.md](10_optimization/derivations/qubo_ising_mapping.md) | QUBO-Ising Mapping and CO Encodings |
| 8 | [relaxation_methods.md](10_optimization/derivations/relaxation_methods.md) | Relaxation Methods for CO |

**References (tex + PDF)**:
- `references/boyd_convex_optimization.pdf` -- Boyd & Vandenberghe, Convex Optimization (714p)
- `references/bengio_ml4co/` -- Bengio et al., ML for CO (`ml4or.tex`, `glossary.tex`)
- `references/cappart_gnn_co/` -- Cappart et al., GNN for CO (`main_jmlr.tex`)

**Extracted text**: `_extracted_text/boyd.txt`

---

## 11 ML Theory

**Key Formulas**: [key_formulas.md](11_ml_theory/key_formulas.md) -- 54 formulas

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [attention_mechanism.md](11_ml_theory/derivations/attention_mechanism.md) | Attention Mechanism: Complete Theory |
| 2 | [diffusion_models_math.md](11_ml_theory/derivations/diffusion_models_math.md) | Diffusion Models: Complete Math Framework |
| 3 | [discrete_diffusion_d3pm.md](11_ml_theory/derivations/discrete_diffusion_d3pm.md) | D3PM: Discrete Denoising Diffusion |
| 4 | [discrete_score_matching.md](11_ml_theory/derivations/discrete_score_matching.md) | Discrete Score Matching and CTMC Diffusion |
| 5 | [elbo_derivation.md](11_ml_theory/derivations/elbo_derivation.md) | ELBO Derivation |
| 6 | [flow_matching.md](11_ml_theory/derivations/flow_matching.md) | Flow Matching: Complete Math Framework |
| 7 | [generative_models_comparison.md](11_ml_theory/derivations/generative_models_comparison.md) | Generative Models: Theoretical Comparison |
| 8 | [gnn_message_passing.md](11_ml_theory/derivations/gnn_message_passing.md) | GNN Message Passing Framework |
| 9 | [langevin_dynamics.md](11_ml_theory/derivations/langevin_dynamics.md) | Langevin Dynamics for Sampling |
| 10 | [optimization_algorithms.md](11_ml_theory/derivations/optimization_algorithms.md) | ML Optimization Algorithms (SGD/Adam) |
| 11 | [reinforcement_learning_basics.md](11_ml_theory/derivations/reinforcement_learning_basics.md) | RL Theory for Combinatorial Optimization |
| 12 | [score_matching.md](11_ml_theory/derivations/score_matching.md) | Score Matching and Denoising Score Matching |
| 13 | [variational_inference.md](11_ml_theory/derivations/variational_inference.md) | Variational Inference Basics |

**References (tex)** -- 19 source packages:

| Reference | Main file | Paper |
|-----------|-----------|-------|
| `austin_d3pm/` | `root.tex` | Austin et al., D3PM (NeurIPS 2021) |
| `campbell_ctmc/` | `neurips_2022.tex` | Campbell et al., CTMC diffusion |
| `diffuco/` | `Part_I_2025-01-26.tex` | DiffuCO |
| `goodfellow_gan/` | `adversarial.tex` | Goodfellow et al., GAN |
| `ho_ddpm/` | `main.tex` | Ho et al., DDPM |
| `kingma_adam/` | `arxiv.tex` | Kingma & Ba, Adam |
| `kingma_vae/` | `main.tex` | Kingma & Welling, VAE |
| `kipf_gcn/` | `main.tex` | Kipf & Welling, GCN |
| `kool_attention_model/` | `iclr2019_conference.tex` | Kool et al., Attention Model for VRP |
| `lipman_flow_matching/` | `fm_arxiv_v2.tex` | Lipman et al., Flow Matching |
| `schulman_ppo/` | `ppo-arxiv.tex` | Schulman et al., PPO |
| `song_ddim/` | `main.tex` | Song et al., DDIM |
| `song_score_sde/` | `main.tex` | Song et al., Score SDE |
| `sun_difusco/` | `main.tex` | Sun et al., DIFUSCO |
| `vaswani_transformer/` | `ms.tex` | Vaswani et al., Transformer |
| `velickovic_gat/` | `iclr2018_conference.tex` | Velickovic et al., GAT |
| `vignac_digress/` | `diffusion_main.tex` | Vignac et al., DiGress |
| `williams_reinforce/` | (metadata only) | Williams, REINFORCE |
| `xu_gin/` | `main.tex` | Xu et al., GIN |

---

## 12 ZX-Calculus

**Key Formulas**: [key_formulas.md](12_zx_calculus/key_formulas.md) -- 15 formulas (F12.1--F12.15)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [zx_basics.md](12_zx_calculus/derivations/zx_basics.md) | ZX-Calculus Basics: Generators, Composition, Gate Decomposition |
| 2 | [zx_rewrite_rules.md](12_zx_calculus/derivations/zx_rewrite_rules.md) | ZX Rewrite Rules and Completeness |
| 3 | [zx_circuit_optimization.md](12_zx_calculus/derivations/zx_circuit_optimization.md) | ZX-Calculus for Circuit Optimization (PyZX, T-count) |
| 4 | [zx_graph_states.md](12_zx_calculus/derivations/zx_graph_states.md) | ZX-Calculus and Graph States (LC, Pivot, MBQC) |

**Key references** (no local tex/PDF yet -- cite from arXiv):
- Coecke & Duncan, New J. Phys. 13, 043016 (2011) -- Interacting Quantum Observables (arXiv:0906.4725)
- van de Wetering, arXiv:2012.13966 (2020) -- ZX-calculus for the working quantum computer scientist (THE standard reference)
- Kissinger & van de Wetering, EPTCS 318, pp.229-241 (2020) -- PyZX (arXiv:1904.04735)
- Backens, New J. Phys. 16, 093021 (2014) -- ZX is complete for stabilizer QM (arXiv:1307.7025)
- Duncan, Kissinger, Perdrix & van de Wetering, Quantum 4, 279 (2020) -- Graph-theoretic simplification (arXiv:1902.03178)

**Cross-references**: `04_quantum_error_correction/` (stabilizer formalism), `06_group_theory/` (Clifford group, Pauli group), `13_quantum_compilation/` (circuit compilation)

---

## 13 Quantum Compilation & Routing

**Key Formulas**: [key_formulas.md](13_quantum_compilation/key_formulas.md) -- 10 formulas (F13.1--F13.10)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [qubit_routing_theory.md](13_quantum_compilation/derivations/qubit_routing_theory.md) | Qubit Routing: Formal Theory and NP-Hardness |
| 2 | [circuit_compilation_complexity.md](13_quantum_compilation/derivations/circuit_compilation_complexity.md) | Circuit Compilation Complexity and Gate Synthesis |
| 3 | [routing_algorithms.md](13_quantum_compilation/derivations/routing_algorithms.md) | Routing Algorithms: SABRE, OLSQ, A*, Token Swapping |

**Key references** (no local tex/PDF yet -- cite from papers):
- Siraichi et al., CGO 2018 -- Qubit allocation formalization
- Li et al., ASPLOS 2019 -- SABRE algorithm
- Cowtan et al., TCAD 2019 -- t|ket> routing, bridge gate
- Tan & Cong, ICCAD 2020 / DAC 2021 -- OLSQ / OLSQ-TB
- Miltzow et al., ESA 2016 -- Token Swapping NP-hardness
- Dawson & Nielsen, QIC 2006 -- Solovay-Kitaev theorem

---

## 14 Scheduling Theory

**Key Formulas**: [key_formulas.md](14_scheduling_theory/key_formulas.md) -- 10 formulas (F14.1--F14.10)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [scheduling_basics.md](14_scheduling_theory/derivations/scheduling_basics.md) | Machine Scheduling: Taxonomy, Algorithms, and Approximation |
| 2 | [graph_coloring_theory.md](14_scheduling_theory/derivations/graph_coloring_theory.md) | Graph Coloring Theory for Scheduling |
| 3 | [syndrome_scheduling.md](14_scheduling_theory/derivations/syndrome_scheduling.md) | Syndrome Measurement Scheduling |

**Key references** (no local tex/PDF yet -- cite from papers):
- Graham et al., 1979 -- Scheduling survey (three-field notation)
- Graham, 1969 -- LPT algorithm, approximation ratio
- Brooks, 1941 -- Chromatic number upper bound
- Golumbic, 1980 -- Algorithmic Graph Theory and Perfect Graphs
- Tomita et al., 2014 -- Low-distance surface codes, CNOT scheduling
- Fowler et al., 2012 -- Surface codes review, syndrome extraction
- Maslov et al., 2008 -- Quantum circuit scheduling

**Cross-references**: `07_graph_theory/` (F7.15 graph coloring), `04_quantum_error_correction/` (surface code, stabilizer formalism), `10_optimization/` (NP-hard problems), `13_quantum_compilation/` (circuit depth optimization)

---

## 15 Quantum Hardware

**Key Formulas**: [key_formulas.md](15_quantum_hardware/key_formulas.md) -- 12 formulas (F15.1--F15.12)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [superconducting_qubits.md](15_quantum_hardware/derivations/superconducting_qubits.md) | Superconducting Qubits: Transmon Physics, Gates, Quafu Platform |
| 2 | [benchmarking_metrics.md](15_quantum_hardware/derivations/benchmarking_metrics.md) | Benchmarking Metrics: RB, XEB, QV, CLOPS |
| 3 | [noise_and_errors_hardware.md](15_quantum_hardware/derivations/noise_and_errors_hardware.md) | Physical Noise Sources, Calibration Drift, Crosstalk |

**Key references** (cite from papers):
- Koch et al., Phys. Rev. A 76, 042319 (2007) -- Transmon qubit
- Arute et al., Nature 574, 505 (2019) -- Google quantum supremacy, XEB
- Cross et al., Phys. Rev. A 100, 032328 (2019) -- Quantum Volume
- Wack et al., arXiv:2110.14108 (2021) -- CLOPS
- Magesan et al., Phys. Rev. Lett. 106, 180504 (2011) -- Randomized Benchmarking
- Krantz et al., Appl. Phys. Rev. 6, 021318 (2019) -- Superconducting qubit guide

**Cross-references**: `02_quantum_mechanics/` (channels, fidelity), `04_quantum_error_correction/` (noise models, threshold), `05_variational_quantum/` (error mitigation), `06_group_theory/` (Clifford group for RB)

---

## 16 Statistical Mechanics

**Key Formulas**: [key_formulas.md](16_statistical_mechanics/key_formulas.md) -- 12 formulas (F16.1--F16.12)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [ising_model.md](16_statistical_mechanics/derivations/ising_model.md) | Ising Model: 1D/2D, Transfer Matrix, Onsager, Critical Exponents |
| 2 | [percolation_theory.md](16_statistical_mechanics/derivations/percolation_theory.md) | Percolation Theory: Bond/Site, Threshold, QEC Connection |
| 3 | [qec_stat_mech_mapping.md](16_statistical_mechanics/derivations/qec_stat_mech_mapping.md) | QEC-Stat Mech Mapping: Dennis 2002, RBIM, Nishimori Line, Z2 Gauge |

**Key references** (cite from papers):
- Onsager, Phys. Rev. 65, 117 (1944) -- 2D Ising exact solution
- Dennis et al., J. Math. Phys. 43, 4452 (2002) -- Topological quantum memory, RBIM mapping
- Nishimori, Prog. Theor. Phys. 66, 1169 (1981) -- Nishimori line
- Grimmett, Percolation (Springer, 1999) -- Percolation theory
- Merz & Chalker, Phys. Rev. B 65, 054425 (2002) -- RBIM phase diagram

**Cross-references**: `04_quantum_error_correction/` (surface code, threshold, decoder), `08_topology/` (topological codes), `10_optimization/` (QUBO-Ising mapping)

---

## 17 Experimental Methods

**Key Formulas**: [key_formulas.md](17_experimental_methods/key_formulas.md) -- 10 formulas (F17.1--F17.10)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [statistical_testing.md](17_experimental_methods/derivations/statistical_testing.md) | Statistical Testing: t-test, Wilcoxon, Bootstrap, Multiple Comparison |
| 2 | [quantum_experiment_design.md](17_experimental_methods/derivations/quantum_experiment_design.md) | Quantum Experiment Design: Controls, Baselines, Scaling, Ablation |
| 3 | [reporting_standards.md](17_experimental_methods/derivations/reporting_standards.md) | Reporting Standards: Fidelity, Compilation, ML Results, Paper Checklist |

**Key references** (cite from papers/textbooks):
- Fisher, Statistical Methods for Research Workers (1925) -- t-test foundations
- Wilcoxon, Biometrics 1, 80 (1945) -- Signed-rank test
- Efron & Tibshirani, An Introduction to the Bootstrap (1993) -- Bootstrap methods
- Holm, Scandinavian J. Statistics 6, 65 (1979) -- Multiple comparison correction

**Cross-references**: `15_quantum_hardware/` (benchmarking metrics), `05_variational_quantum/` (error mitigation), `11_ml_theory/` (optimization algorithms)

---

## 18 Proof Techniques Arsenal

**Key Formulas**: [key_formulas.md](18_proof_techniques/key_formulas.md) -- 20 formulas (F18.1--F18.20)

| # | Derivation | Title |
|---|-----------|-------|
| 1 | [concentration_inequalities.md](18_proof_techniques/derivations/concentration_inequalities.md) | Concentration Inequalities: Markov→Chebyshev→Chernoff→Hoeffding→Bernstein→McDiarmid→Azuma, Sub-Gaussian Framework |
| 2 | [matrix_concentration.md](18_proof_techniques/derivations/matrix_concentration.md) | Matrix Concentration: Matrix Bernstein/Chernoff/Hoeffding, Classical Shadows, Tomography |
| 3 | [learning_theory.md](18_proof_techniques/derivations/learning_theory.md) | Learning Theory: PAC, VC Dimension, Rademacher, PAC-Bayes, GNN Generalization |
| 4 | [convergence_methods.md](18_proof_techniques/derivations/convergence_methods.md) | Convergence Methods: Contraction Mapping, Coupling, Markov Chain Mixing, Diffusion Model Convergence |
| 5 | [probabilistic_method.md](18_proof_techniques/derivations/probabilistic_method.md) | Probabilistic Method: First/Second Moment, LLL, Alteration, Gilbert-Varshamov, Random LDPC |
| 6 | [quantum_proof_toolkit.md](18_proof_techniques/derivations/quantum_proof_toolkit.md) | Quantum Proof Toolkit: Decoupling, Post-selection, Quantum Union Bound, Gentle Measurement, de Finetti |

**Key references** (cite from papers/textbooks):
- Boucheron, Lugosi & Massart, Concentration Inequalities (2013) -- Comprehensive reference
- Tropp, User-Friendly Tail Bounds for Sums of Random Matrices, Found. Comput. Math. (2012) -- Matrix concentration
- Vershynin, High-Dimensional Probability (2018) -- Sub-Gaussian framework
- Shalev-Shwartz & Ben-David, Understanding Machine Learning (2014) -- PAC/VC theory
- Alon & Spencer, The Probabilistic Method, 4th ed. (2016) -- Probabilistic existence proofs
- Levin, Peres & Wilmer, Markov Chains and Mixing Times (2009) -- Coupling and mixing
- Watrous, Theory of Quantum Information (2018) -- Quantum proof techniques

**Cross-references**: `03_quantum_info_theory/` (entropy inequalities, quantum channels), `04_quantum_error_correction/` (threshold proofs, BP decoding), `11_ml_theory/` (diffusion model convergence, GNN), `07_graph_theory/` (GNN architecture), `02_quantum_mechanics/` (fidelity, trace distance)

---

## Placeholder Directories (empty, reserved)

- `05_coding_theory/` -- Classical coding theory (has `derivations/` and `references/` dirs, no content yet)
- `09_probability_statistics/` -- Probability and statistics (has `derivations/` and `references/` dirs, no content yet)

---

## Extracted Text Files

Full-text extractions from PDF textbooks/lecture notes, stored in `_extracted_text/`. Each file contains page markers `===== PAGE X =====`.

| File | Source | Size |
|------|--------|------|
| `bacon.txt` | Bacon, Intro to QEC | 92 KB |
| `boyd.txt` | Boyd & Vandenberghe, Convex Optimization | 361 KB |
| `linalg_qc.txt` | Portugal, Linear Algebra for QC | 51 KB |
| `nielsen_chuang.txt` | Nielsen & Chuang, Quantum Computation and QI | 798 KB |
| `nordiquest.txt` | Nordiquest, Practical QEC | 17 KB |
| `preskill_ch2.txt` | Preskill Lecture Notes Ch.2 | 108 KB |
| `preskill_ch3.txt` | Preskill Lecture Notes Ch.3 | 128 KB |
| `preskill_ch4.txt` | Preskill Lecture Notes Ch.4 | 125 KB |
| `preskill_ch5.txt` | Preskill Lecture Notes Ch.5 | 115 KB |
| `preskill_ch7.txt` | Preskill Lecture Notes Ch.7 | 174 KB |
| `slofstra.txt` | Slofstra, Linear Algebra for QC | 207 KB |
| `steane.txt` | Steane, QEC Tutorial | 81 KB |
| `surface_notes.txt` | Surface Code Lecture Notes | 53 KB |
| `watrous_tqi.txt` | Watrous, Theory of Quantum Information | 354 KB |

**Total extracted text**: ~2.66 MB across 14 files (15 listed, `linalg_qc.txt` = Portugal extraction)

---

## Utility Files

- `scripts/download_arxiv_source.py` -- Download arXiv source packages
- `scripts/tex_to_md.py` -- Convert tex to markdown derivations
- `scripts/batch_download.py` -- Batch download references
- `scripts/build_index.py` -- Auto-build this index
- `SEARCH_TAGS.md` -- Tag-based search index
- `GLOSSARY.md` -- 129 terms across 8 categories with Chinese translations and KB links

---

## Usage Rules (for Claude Code instances)

1. **Read this INDEX first** to find the relevant topic and derivation file
2. **Read the derivation .md** for the structured proof/derivation with source citations
3. **Read `references/*.tex`** to cross-verify formulas from original LaTeX
4. **Read `_extracted_text/*.txt`** for additional textbook context (page markers included)
5. **Cite sources**: every formula must reference `[Author, Theorem X.Y, p.Z]`
6. **Never fabricate formulas**: if the KB lacks a derivation, say so explicitly
