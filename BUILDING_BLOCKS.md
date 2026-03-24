# BUILDING_BLOCKS.md — "What Can I Prove With This?"

> **Reverse index for the Math Theory KB.**
> Given a proof goal, this file tells you which KB tools (formulas, derivation files, extracted texts) to use.
>
> **How to use**: Find your proof goal below, then follow the pointers to the specific formulas (F-codes) and derivation files.
> For full formula details, see the corresponding `key_formulas.md` in each topic directory.

---

## Part 1: Proof Goals → Tools

### 1.1 "证明某个算法有理论上界/下界"

| Sub-goal | KB Tools | Key Formulas |
|----------|----------|-------------|
| **NP-hardness reduction** | `10_optimization/derivations/np_hard_problems.md` | F10.2--F10.7 (ILP, MIS, MaxCut, TSP formulations) |
| **Approximation ratio** | `10_optimization/derivations/relaxation_methods.md` | F10.10 (ratio definition), F10.11 (greedy bounds), F10.12 (GW 0.878) |
| **LP/SDP relaxation gap** | `10_optimization/derivations/relaxation_methods.md`, `convex_optimization_basics.md` | F10.8, F10.9 (LP/Lagrangian relaxation), F10.24 (SDP standard form) |
| **Gradient convergence** | `10_optimization/derivations/gradient_methods.md` | F10.20 (strongly convex: linear rate $O(\kappa \log 1/\varepsilon)$), F10.21 (Newton: quadratic) |
| **Sample complexity / CI** | `17_experimental_methods/derivations/statistical_testing.md` | F17.1 (binomial estimation), F17.2 (Wilson CI) |
| **Error suppression (QEC)** | `04_qec/derivations/threshold_theorem.md` | F4.6 ($p_L \sim (p/p_{th})^{d/2}$), F4.20 (concatenation recursion) |
| **Code distance bounds** | `04_qec/derivations/code_distance_bounds.md` | F4.11 (Singleton), F4.12 (Hamming), F4.16--F4.18 (asymptotic bounds) |
| **GNN expressiveness ceiling** | `07_graph_theory/derivations/wl_test_expressiveness.md` | F11.32 (GNN $\leq$ 1-WL), F10.29 (GNN MVC ratio = 2) |
| **Submodularity / greedy** | `10_optimization/derivations/relaxation_methods.md` | $(1-1/e)$ approximation for submodular maximization |
| **Statistical significance** | `17_experimental_methods/derivations/statistical_testing.md` | F17.3 (paired t-test), F17.4 (Wilcoxon), F17.5 (Cohen's d) |

---

### 1.2 "证明某个量子方法的正确性"

| Sub-goal | KB Tools | Key Formulas |
|----------|----------|-------------|
| **Fidelity bound** | `02_qm/derivations/fidelity_and_trace_distance.md` | F2.4 (Uhlmann fidelity), F3.12 (SDP form) |
| **Fidelity ↔ trace distance** | `03_qit/derivations/sdp_quantum_info.md` | F3.13 (Fuchs-van de Graaf: $1-\sqrt{F} \leq D \leq \sqrt{1-F}$) |
| **Channel distance** | `03_qit/derivations/sdp_quantum_info.md` | F3.10 (diamond norm, SDP computable) |
| **Error correction validity** | `04_qec/derivations/knill_laflamme_conditions.md` | F4.1 ($PE_a^\dagger E_b P = C_{ab}P$) |
| **Stabilizer code correctness** | `04_qec/derivations/stabilizer_formalism.md` | F4.2 (stabilizer state), F4.3 (syndrome measurement) |
| **CSS code construction** | `04_qec/derivations/css_codes.md` | F4.4 ($C_2 \subseteq C_1 \Rightarrow [[n, k_1-k_2, d]]$) |
| **Threshold existence** | `04_qec/derivations/threshold_theorem.md` | F4.6 (topological threshold), F4.20 (concatenation recursion) |
| **Channel capacity** | `03_qit/derivations/quantum_channel_capacity.md` | F3.23 (Holevo), F3.24 (LSD), F3.25 (EA capacity) |
| **Data processing** | `03_qit/derivations/quantum_data_processing.md` | F3.20 ($D(\Phi(\rho)\|\Phi(\sigma)) \leq D(\rho\|\sigma)$) |
| **State discrimination** | `03_qit/derivations/quantum_discrimination.md` | F3.14 (Helstrom bound), F3.15 (unambiguous discrimination) |
| **Entanglement verification** | `03_qit/derivations/entanglement_theory.md` | F3.30 (PPT criterion), F3.29 (log negativity) |
| **Variational upper bound** | `05_vq/derivations/vqe_theory.md` | F5.1 (variational principle: $E_0 \leq \langle H \rangle$) |
| **QAOA correctness** | `05_vq/derivations/qaoa_theory.md` | F5.4 (ansatz), F5.13 (monotonicity + limit convergence) |
| **Gate fault tolerance** | `04_qec/derivations/fault_tolerant_gates.md`, `magic_state_distillation.md` | Transversal gate theorems, magic state overhead |

---

### 1.3 "证明某个 ML 方法的收敛性 / 正确性"

| Sub-goal | KB Tools | Key Formulas |
|----------|----------|-------------|
| **ELBO derivation** | `11_ml/derivations/elbo_derivation.md` | F11.1 ($\log p(x) \geq \text{ELBO}$) |
| **DDPM loss equivalence** | `11_ml/derivations/diffusion_models_math.md` | F11.4 ($L_{\text{simple}}$), F11.20 (VLB weighted loss) |
| **Score matching equivalence** | `11_ml/derivations/score_matching.md` | F11.6 (DSM objective = implicit score matching) |
| **SDE ↔ DDPM unification** | `11_ml/derivations/diffusion_models_math.md` | F11.8 (forward/reverse SDE), F11.27 (Anderson general) |
| **Flow matching validity** | `11_ml/derivations/flow_matching.md` | F11.37 (CFM gradient = FM gradient, Theorem 2) |
| **GNN expressiveness** | `07_graph_theory/derivations/wl_test_expressiveness.md` | F11.32 (GNN $\leq$ WL), F11.33 (sum injectivity) |
| **GIN = 1-WL** | `11_ml/derivations/gnn_message_passing.md` | F11.31 (GIN update), F11.32 (Theorem 3) |
| **Policy gradient unbiased** | `11_ml/derivations/reinforcement_learning_basics.md` | F11.49 (REINFORCE), F10.30 (REINFORCE for CO) |
| **PPO trust region** | `11_ml/derivations/reinforcement_learning_basics.md` | F11.50 (clipped surrogate) |
| **GAN equilibrium** | `11_ml/derivations/generative_models_comparison.md` | F11.47 (minimax), F11.48 (optimal discriminator → JSD) |
| **VAE training** | `11_ml/derivations/elbo_derivation.md` | F11.52 (Gaussian VAE estimator), F11.13 (reparam trick) |
| **Discrete diffusion** | `11_ml/derivations/discrete_diffusion_d3pm.md` | F11.16--F11.17 (D3PM forward/posterior), F11.24 (CT-ELBO) |
| **Langevin convergence** | `11_ml/derivations/langevin_dynamics.md` | F11.7 (Langevin dynamics, $\eta \to 0$ convergence) |
| **ODE likelihood** | `11_ml/derivations/diffusion_models_math.md` | F11.23 (exact log-likelihood via probability flow ODE) |

---

### 1.4 "证明某个优化方法的保证"

| Sub-goal | KB Tools | Key Formulas |
|----------|----------|-------------|
| **Convexity verification** | `10_optimization/derivations/convex_optimization_basics.md` | F10.16 (first-order), F10.17 (Hessian PSD) |
| **Jensen's inequality** | `10_optimization/derivations/convex_optimization_basics.md` | F10.23 ($f(E[X]) \leq E[f(X)]$) |
| **KKT optimality** | `10_optimization/derivations/duality_kkt.md` | F10.18 (KKT conditions) |
| **Lagrangian duality** | `10_optimization/derivations/duality_kkt.md` | F10.19 (weak/strong duality) |
| **SDP relaxation quality** | `10_optimization/derivations/relaxation_methods.md` | F10.12 (GW: $\alpha \geq 0.878$), F10.24 (SDP form) |
| **Interior point complexity** | `10_optimization/derivations/gradient_methods.md` | F10.22 ($O(\sqrt{m}\log(m/\varepsilon))$ Newton steps) |
| **Adam convergence** | `10_optimization/derivations/gradient_methods.md` | F10.26 / F11.51 (Adam update rule) |
| **Greedy approximation** | `10_optimization/derivations/relaxation_methods.md` | F10.11 (MVC 2-approx, MaxCut 0.5-approx) |
| **QUBO ↔ Ising equivalence** | `10_optimization/derivations/qubo_ising_mapping.md` | F10.13--F10.14 (bijection), F10.15 (penalty method) |
| **Penalty method soundness** | `10_optimization/derivations/qubo_ising_mapping.md` | F10.15 (sufficiently large $\lambda$) |
| **Fenchel duality** | `10_optimization/derivations/convex_optimization_basics.md` | F10.25 (conjugate function) |

---

### 1.5 "推导一个新公式"

| Sub-goal | KB Tools | Key Formulas |
|----------|----------|-------------|
| **DDPM forward/reverse chain** | `11_ml/derivations/diffusion_models_math.md` | F11.2 → F11.3 → F11.4 (full derivation) |
| **Discrete diffusion (D3PM)** | `11_ml/derivations/discrete_diffusion_d3pm.md` | F11.16 → F11.17 → F11.26 |
| **DDIM from DDPM** | `11_ml/derivations/diffusion_models_math.md` | F11.34 (DDIM update), F11.35 (neural ODE limit) |
| **Flow matching from scratch** | `11_ml/derivations/flow_matching.md` | F11.36 → F11.37 → F11.38 → F11.39 |
| **GCN from spectral theory** | `11_ml/derivations/gnn_message_passing.md` | F11.29 (full chain: spectral → Chebyshev → GCN) |
| **Fidelity ↔ trace distance** | `02_qm/derivations/fidelity_and_trace_distance.md` | F2.4, F2.5, F3.13 (Fuchs-van de Graaf) |
| **Entropy chain rules** | `03_qit/derivations/entropy_inequalities.md` | F3.16 → F3.17 → F3.18 → F3.19 (SSA) → F3.22 |
| **Kraus → Choi → Stinespring** | `02_qm/derivations/quantum_channels_kraus.md` | F2.6 → F2.7 → F3.7 → F3.8 |
| **Stabilizer → syndrome → decoder** | `04_qec/derivations/stabilizer_formalism.md` → `decoder_theory.md` | F4.2 → F4.3 → F4.8 |
| **QUBO → Ising → QAOA** | `10_optimization/derivations/qubo_ising_mapping.md` → `05_vq/derivations/qaoa_theory.md` | F10.13 → F10.14 → F5.4 → F5.6 |
| **VQE gradient computation** | `05_vq/derivations/vqe_theory.md` | F5.2 → F5.3 (parameter shift rule) |
| **Quantum natural gradient** | `05_vq/derivations/quantum_natural_gradient.md` | F5.10, F5.11 (QFI matrix) |
| **ZX simplification** | `12_zx_calculus/derivations/zx_rewrite_rules.md` | F12.3 (spider fusion), F12.4 (color change) |
| **Toric code from homology** | `08_topology/derivations/homology_basics.md` → `topological_codes_connection.md` | F8.1 → F8.2 → F4.7 |

---

### 1.6 "证明某个硬件/实验结果的有效性"

| Sub-goal | KB Tools | Key Formulas |
|----------|----------|-------------|
| **Error bar / confidence** | `17_experimental_methods/derivations/statistical_testing.md` | F17.1 (binomial SE), F17.2 (Wilson CI) |
| **Method comparison** | `17_experimental_methods/derivations/statistical_testing.md` | F17.3 (paired t), F17.4 (Wilcoxon), F17.5 (effect size) |
| **Noise model justification** | `04_qec/derivations/noise_models.md` | F4.14 (depolarizing Kraus), F3.9 |
| **Gate fidelity metrics** | `15_quantum_hardware/derivations/superconducting_qubits.md` | F15.1 (transmon Hamiltonian), F15.2 ($T_1$) |
| **Logical error rate scaling** | `04_qec/derivations/threshold_theorem.md` | F4.15 ($p_L \sim p^{d/2+1}$), F4.6 (threshold) |
| **Classical shadow efficiency** | `05_vq/derivations/vqe_theory.md` | F5.12 ($T = O(\log M / \varepsilon^2)$) |
| **Statistical mechanics mapping** | `16_stat_mech/derivations/ising_model.md`, `percolation_theory.md` | F16.1--F16.3 (Ising, partition fn, free energy) |

---

### 1.7 "证明某个编译/路由方法的开销"

| Sub-goal | KB Tools | Key Formulas |
|----------|----------|-------------|
| **Routing overhead** | `13_quantum_compilation/derivations/qubit_routing_theory.md` | F13.1 (mapping problem), F13.2 (SWAP = 3 CNOTs) |
| **Circuit compilation NP-hardness** | `13_quantum_compilation/derivations/circuit_compilation_complexity.md` | Complexity results for optimal routing |
| **Scheduling = graph coloring** | `14_scheduling_theory/derivations/graph_coloring_theory.md` | F14.2 (equivalence), F14.3 (Brooks' theorem) |
| **Optimal schedule depth** | `14_scheduling_theory/derivations/scheduling_basics.md` | F14.1 ($P\|C_{\max}$), F14.4 (interval graph: $\chi = \omega$) |
| **ZX-based optimization** | `12_zx_calculus/derivations/zx_circuit_optimization.md` | F12.3 (fusion), ZX rewrite rules |
| **Lattice surgery bounds** | `10_optimization/derivations/lattice_surgery_compilation_bounds.md` | Compilation complexity for surface code |

---

## Part 2: Common Proof Patterns

### Pattern A: "我的方法超过了某个理论上界"

1. **Establish the bound**: Identify the theoretical limit
   - Selection ceiling / binomial: F17.1 + `statistical_testing.md`
   - NP-hard inapproximability: F10.2 + `np_hard_problems.md`
   - Quantum Singleton/Hamming bound: F4.11, F4.12 + `code_distance_bounds.md`
   - GNN $\leq$ WL: F11.32 + `wl_test_expressiveness.md`
2. **Show your method breaks the assumption**
   - i.i.d. → correlated (resampling, diffusion guidance)
   - Fixed architecture → adaptive (ADAPT-VQE: `adapt_vqe.md`)
   - Single-shot → iterative (multi-round decoding)
   - Degenerate codes can violate Hamming bound: F4.12 note
3. **Quantify the improvement**: Use F17.3--F17.5 for statistical significance
4. **Explain the mechanism**: Point to the specific KB derivation that covers the technique

### Pattern B: "我的解码器比 baseline 好"

1. **Define the metric**: Logical error rate $p_L$ under specific noise → `noise_models.md`, F4.14
2. **Establish baseline**: MWPM threshold ($\approx 1.1\%$ depolarizing) → `decoder_theory.md`, F4.8
3. **Prove better scaling or threshold**:
   - Show $p_L^{\text{yours}} < p_L^{\text{MWPM}}$ for same $d$ → F4.15, F4.6
   - Or show higher threshold $p_{th}^{\text{yours}} > p_{th}^{\text{MWPM}}$
4. **Connect to statistical mechanics** (if applicable):
   - RBIM mapping → `16_stat_mech/derivations/ising_model.md`, F16.1--F16.4
   - Nishimori line → `percolation_theory.md`
   - Maximum likelihood decoding = partition function → F16.2
5. **Statistical validation**: F17.3 (paired t-test across code distances), F17.5 (effect size)

### Pattern C: "GNN 能泛化到更大的图"

1. **Characterize GNN expressiveness**: F11.32 (GNN $\leq$ WL), F11.31 (GIN = WL)
2. **Show domain has size-independent local structure**:
   - Tanner graphs of LDPC codes → `07_graph_theory/derivations/tanner_graphs.md`
   - ZX diagrams → `12_zx_calculus/derivations/zx_basics.md`
   - CO problem structure (fixed-degree graphs) → `np_hard_problems.md`
3. **Use WL test** to characterize what GNN can/cannot distinguish → `wl_test_expressiveness.md`
4. **Message passing analysis**: F11.10 (MPNN framework), receptive field argument
5. **Empirical scaling law**: Train on size $N$, test on $2N, 4N, 8N$, report with error bars (F17.1--F17.2)

### Pattern D: "扩散模型能求解 CO 问题"

1. **Problem formulation**: QUBO/Ising → `qubo_ising_mapping.md`, F10.13--F10.14
2. **D3PM as discrete sampler**: `discrete_diffusion_d3pm.md`, F11.16--F11.17
3. **GNN as denoiser**: `gnn_message_passing.md`, F11.10
4. **Training objective**:
   - Supervised: F10.28 (ML4CO learning)
   - Unsupervised: F10.34 (DiffUCO energy loss)
   - RL: F10.30, F11.49 (REINFORCE)
5. **Approximation quality**: `neural_co_theory.md`, F10.10 (approximation ratio)
6. **Constraint satisfaction**: F10.15 (penalty method)

### Pattern E: "扩散模型生成量子纠错码/线路"

1. **Code structure**: Stabilizer formalism → F4.2, `stabilizer_formalism.md`
2. **Graph representation**: Tanner graph → `tanner_graphs.md`, or ZX diagram → `zx_basics.md`
3. **Discrete diffusion on graphs**: DiGress → F11.40--F11.42
4. **Quality metric**: Code distance (F4.11 bounds), logical error rate (F4.15)
5. **Validity check**: Knill-Laflamme conditions → F4.1

### Pattern F: "QAOA/VQE 在真机上的性能"

1. **Ansatz**: F5.4 (QAOA) or F5.9 (hardware-efficient)
2. **Gradient computation**: F5.3 (parameter shift rule)
3. **Barren plateau analysis**: F5.8 → `barren_plateaus.md`
4. **Noise effects**: F4.14 (depolarizing), `noise_models.md`, `error_mitigation.md`
5. **Hardware constraints**: F15.1 (transmon), `superconducting_qubits.md`
6. **Comparison metric**: F5.7 (approximation ratio), F17.1--F17.3 (statistical tests)

### Pattern G: "量子信道的容量/性能分析"

1. **Channel definition**: F2.6 (Kraus), F2.7 (Choi), F3.8 (Stinespring)
2. **Capacity bounds**: F3.23 (Holevo), F3.24 (quantum capacity), F3.25 (EA capacity)
3. **Hierarchy**: F3.26 ($Q \leq C \leq C_{EA}$)
4. **Key tools**: F3.19 (SSA), F3.20 (DPI), F3.37 (recoverability)
5. **Special channels**: F3.9 (depolarizing), F3.46 (erasure: $Q = \max(1-2\varepsilon, 0)$)

---

## Part 3: Quick Reference — "我需要证 X，去读哪个文件？"

| # | 要证的东西 | 去读 | 关键公式 |
|---|-----------|------|---------|
| 1 | 上界/下界（组合优化） | `np_hard_problems.md` + `relaxation_methods.md` | F10.10--F10.12 |
| 2 | 收敛性（梯度法） | `gradient_methods.md` | F10.20 (linear), F10.21 (quadratic) |
| 3 | 收敛性（Langevin） | `langevin_dynamics.md` | F11.7 |
| 4 | 收敛性（QAOA 层数） | `qaoa_theory.md` | F5.13 ($M_p \to \max C(z)$) |
| 5 | 正确性（量子码） | `knill_laflamme_conditions.md` | F4.1 |
| 6 | 正确性（CSS 码） | `css_codes.md` | F4.4 |
| 7 | 正确性（稳定子码） | `stabilizer_formalism.md` | F4.2, F4.3 |
| 8 | 态区分度 | `fidelity_and_trace_distance.md` | F2.4, F2.5 |
| 9 | 保真度↔迹距离 | `sdp_quantum_info.md` | F3.13 (Fuchs-van de Graaf) |
| 10 | 信道距离 | `sdp_quantum_info.md` | F3.10 (diamond norm) |
| 11 | 量子容量 | `quantum_capacity.md` | F3.24 (LSD theorem) |
| 12 | 经典容量 | `holevo_bound.md` | F3.23 (Holevo) |
| 13 | 纠缠辅助容量 | `quantum_channel_capacity.md` | F3.25 (BSST) |
| 14 | 纠缠度量 | `entanglement_theory.md` | F3.27--F3.31 |
| 15 | 可分性判据 | `entanglement_theory.md` | F3.30 (PPT) |
| 16 | 熵不等式 | `entropy_inequalities.md` | F3.19 (SSA), F3.22 (subadditivity) |
| 17 | 熵连续性 | `entropy_inequalities.md` | F3.42 (Fannes-Audenaert), F3.43 (AFW) |
| 18 | 数据处理不等式 | `quantum_data_processing.md` | F3.20 |
| 19 | 可恢复性 | `quantum_data_processing.md` | F3.37 |
| 20 | SDP 对偶性 | `sdp_quantum_info.md` | F3.11 |
| 21 | 最优判别 | `quantum_discrimination.md` | F3.14 (Helstrom) |
| 22 | 凸性验证 | `convex_optimization_basics.md` | F10.16, F10.17 |
| 23 | Jensen 不等式 | `convex_optimization_basics.md` | F10.23 |
| 24 | KKT 最优性 | `duality_kkt.md` | F10.18 |
| 25 | Lagrangian 对偶 | `duality_kkt.md` | F10.19 |
| 26 | SDP 松弛 | `relaxation_methods.md` | F10.12 (GW), F10.24 |
| 27 | QUBO↔Ising | `qubo_ising_mapping.md` | F10.13, F10.14 |
| 28 | 阈值定理 | `threshold_theorem.md` | F4.6, F4.20 |
| 29 | 码距界 | `code_distance_bounds.md` | F4.11 (Singleton), F4.12 (Hamming) |
| 30 | 码存在性 | `code_distance_bounds.md` | F4.17 (Gilbert-Varshamov) |
| 31 | 权重枚举器 | `code_distance_bounds.md` | F4.19 (MacWilliams) |
| 32 | 表面码参数 | `surface_code_basics.md` | F4.5, F4.7, F4.9 |
| 33 | 逻辑错误率 | `threshold_theorem.md` | F4.15 ($p_L \sim p^{d/2+1}$) |
| 34 | MWPM 解码 | `decoder_theory.md` | F4.8 |
| 35 | 噪声模型 | `noise_models.md` | F4.14 (depolarizing), F3.9 |
| 36 | ELBO 推导 | `elbo_derivation.md` | F11.1, F11.12 (KL) |
| 37 | DDPM 损失 | `diffusion_models_math.md` | F11.4, F11.20 |
| 38 | Score matching | `score_matching.md` | F11.5, F11.6 |
| 39 | SDE 框架 | `diffusion_models_math.md` | F11.8, F11.27 |
| 40 | 概率流 ODE | `diffusion_models_math.md` | F11.9, F11.23 |
| 41 | DDIM 推导 | `diffusion_models_math.md` | F11.34, F11.35 |
| 42 | Flow matching | `flow_matching.md` | F11.36--F11.39 |
| 43 | 离散扩散 (D3PM) | `discrete_diffusion_d3pm.md` | F11.16--F11.19, F11.24--F11.26 |
| 44 | 离散 score | `discrete_score_matching.md` | F11.18, F11.19 |
| 45 | 图上扩散 (DiGress) | `discrete_diffusion_d3pm.md` | F11.40--F11.42 |
| 46 | GNN 消息传递 | `gnn_message_passing.md` | F11.10, F11.28 (GCN), F11.30 (GAT) |
| 47 | GCN 谱推导 | `gnn_message_passing.md` | F11.29 (full chain) |
| 48 | GIN/WL 等价 | `wl_test_expressiveness.md` | F11.31, F11.32, F11.33 |
| 49 | Attention 机制 | `attention_mechanism.md` | F11.43 (scaled dot-product), F11.44 (multi-head) |
| 50 | Self-Attn = MPNN | `attention_mechanism.md` | F11.46 |
| 51 | GAN 最优性 | `generative_models_comparison.md` | F11.47, F11.48 |
| 52 | REINFORCE 梯度 | `reinforcement_learning_basics.md` | F11.49, F10.30 |
| 53 | PPO 优化 | `reinforcement_learning_basics.md` | F11.50, F11.54 (GAE) |
| 54 | Adam 更新 | `optimization_algorithms.md` | F11.51 / F10.26 |
| 55 | VAE 完整目标 | `elbo_derivation.md` | F11.52, F11.13 |
| 56 | 变分原理 | `vqe_theory.md` | F5.1 |
| 57 | 参数平移规则 | `vqe_theory.md` | F5.3 |
| 58 | 贫瘠高原 | `barren_plateaus.md` | F5.8, F5.16 |
| 59 | 量子自然梯度 | `quantum_natural_gradient.md` | F5.10, F5.11 |
| 60 | 经典影子 | `vqe_theory.md` | F5.12 |
| 61 | QAOA 近似比 | `qaoa_theory.md` | F5.7 ($\geq 0.6924$ for MaxCut at $P=1$) |
| 62 | QAOA 方差集中 | `qaoa_theory.md` | F5.14 |
| 63 | 密度矩阵 | `density_matrix_formalism.md` | F2.1, F2.2 |
| 64 | Schmidt 分解 | `schmidt_decomposition.md` | F2.12, F2.13 |
| 65 | 量子测量 (POVM) | `measurement_theory.md` | F2.14 |
| 66 | von Neumann 熵 | `von_neumann_entropy.md` | F2.3, F3.16 |
| 67 | 相对熵非负 | `entropy_inequalities.md` | F3.21 (Klein), F3.39 |
| 68 | Pinsker 不等式 | `entropy_inequalities.md` | F3.41 |
| 69 | Fano 不等式 | `classical_information_theory.md` | F3.40 |
| 70 | 谱分解 | `spectral_decomposition.md` | F1.1 |
| 71 | SVD/极分解 | `svd_and_polar_decomposition.md` | F1.2, F1.10 |
| 72 | 张量积性质 | `tensor_product_properties.md` | F1.3, F1.11 |
| 73 | 偏迹 | `trace_and_partial_trace.md` | F1.4, F1.7 |
| 74 | 矩阵指数/BCH | `matrix_exponential.md` | F1.5, F1.6 |
| 75 | Choi-Jamiolkowski | `quantum_channels_kraus.md` | F2.7, F3.7 |
| 76 | Stinespring 膨胀 | `quantum_channel_capacity.md` | F3.8 |
| 77 | Pauli 群 | `pauli_group.md` | F6.1, F6.2, F6.3 |
| 78 | Clifford 群 | `clifford_group.md` | Clifford generators, tableau |
| 79 | 辛表示 | `symplectic_representation.md` | Symplectic inner product |
| 80 | ZX 蜘蛛定义 | `zx_basics.md` | F12.1, F12.2 |
| 81 | ZX 重写规则 | `zx_rewrite_rules.md` | F12.3, F12.4 |
| 82 | ZX 电路优化 | `zx_circuit_optimization.md` | T-count reduction |
| 83 | 同调群/Betti数 | `homology_basics.md` | F8.1, F8.2, F8.3 |
| 84 | Euler 示性数 | `euler_characteristic.md` | F8.4 |
| 85 | 拓扑码↔同调 | `topological_codes_connection.md` | Chain complex ↔ stabilizers |
| 86 | 图拉普拉斯 | `spectral_graph_theory.md` | F7.3, F7.4 |
| 87 | 谱图卷积 | `spectral_graph_theory.md` | F7.5 |
| 88 | Tanner 图 | `tanner_graphs.md` | LDPC code ↔ bipartite graph |
| 89 | Qubit routing | `qubit_routing_theory.md` | F13.1, F13.2 |
| 90 | 调度=着色 | `graph_coloring_theory.md` | F14.2, F14.3 |
| 91 | Ising 模型 | `ising_model.md` | F16.1--F16.3 |
| 92 | 渗流阈值 | `percolation_theory.md` | Percolation ↔ QEC threshold |
| 93 | 保真度统计估计 | `statistical_testing.md` | F17.1, F17.2 |
| 94 | 配对检验 | `statistical_testing.md` | F17.3, F17.4 |
| 95 | 效应量 | `statistical_testing.md` | F17.5 |
| 96 | Transmon 物理 | `superconducting_qubits.md` | F15.1, F15.2 |
| 97 | 神经 CO 求解器 | `neural_co_theory.md` | F10.30--F10.34 |
| 98 | AM (Attention Model) | `neural_co_theory.md` | F10.31, F10.32, F10.33 |
| 99 | 条件生成引导 | `diffusion_models_math.md` | F11.15 (classifier-free guidance) |
| 100 | Noise schedule 设计 | `diffusion_models_math.md` | F11.14 (linear/cosine) |
| 101 | Warm-starting VQA | `warm_starting_strategies.md` | Initial parameter strategies |
| 102 | 错误缓解 | `error_mitigation.md` | ZNE, PEC techniques |
| 103 | Magic state 蒸馏 | `magic_state_distillation.md` | Distillation overhead |
| 104 | 容错门 | `fault_tolerant_gates.md` | Transversal + magic state |
| 105 | LDPC 码 | `quantum_ldpc_codes.md` | Good LDPC: $R=\Theta(1), d=\Theta(n^{1/2})$ |
| 106 | Anyon 模型 | `anyonic_models.md` | $e$/$m$ particles, braiding |
| 107 | 上同调 | `cohomology_basics.md` | Dual to homology |
| 108 | 梯度裁剪 | `optimization_algorithms.md` | F11.53 |
| 109 | Syndrome 调度 | `syndrome_scheduling.md` | Measurement scheduling optimization |
| 110 | 线路编译复杂度 | `circuit_compilation_complexity.md` | NP-hardness of optimal compilation |

---

## Part 4: Cross-Domain Proof Chains

These are multi-step proofs that span multiple KB topics. Each chain shows the logical flow and which files to read in order.

### Chain 1: "扩散模型做 QEC 解码" (Diffusion for QEC Decoding)

```
noise_models.md (F4.14) → stabilizer_formalism.md (F4.2-F4.3)
   → tanner_graphs.md (graph representation)
   → discrete_diffusion_d3pm.md (F11.16-F11.17) or diffusion_models_math.md (F11.2-F11.4)
   → gnn_message_passing.md (F11.10, denoiser architecture)
   → threshold_theorem.md (F4.6, evaluate threshold)
   → statistical_testing.md (F17.1-F17.3, report results)
```

### Chain 2: "GNN 做量子线路编译" (GNN for Circuit Compilation)

```
qubit_routing_theory.md (F13.1-F13.2) → circuit_compilation_complexity.md (NP-hard)
   → gnn_message_passing.md (F11.10) → wl_test_expressiveness.md (F11.32)
   → reinforcement_learning_basics.md (F11.49, training) or elbo_derivation.md (F11.1, if VAE)
   → statistical_testing.md (F17.3, compare with SABRE/etc.)
```

### Chain 3: "QAOA 在真机上做 MaxCut" (QAOA for MaxCut on Real Hardware)

```
qubo_ising_mapping.md (F10.5) → qaoa_theory.md (F5.4-F5.7)
   → superconducting_qubits.md (F15.1-F15.2, hardware constraints)
   → noise_models.md (F4.14) → error_mitigation.md (ZNE/PEC)
   → barren_plateaus.md (F5.8, trainability)
   → statistical_testing.md (F17.1-F17.5, benchmarking)
```

### Chain 4: "拓扑码的同调论证明" (Homological Proof of Topological Codes)

```
homology_basics.md (F8.1-F8.3) → topological_codes_connection.md
   → surface_code_basics.md (F4.5, F4.7, F4.9)
   → stabilizer_formalism.md (F4.2) → knill_laflamme_conditions.md (F4.1)
   → threshold_theorem.md (F4.6) → ising_model.md (F16.1, Dennis mapping)
```

### Chain 5: "Flow Matching 生成量子态/图" (Flow Matching for Quantum/Graph Generation)

```
flow_matching.md (F11.36-F11.39) → gnn_message_passing.md (F11.10, graph encoder)
   → convex_optimization_basics.md (F10.23, Jensen for ELBO if needed)
   → neural_co_theory.md (F10.28, if CO application)
   → statistical_testing.md (F17.1-F17.5, evaluation)
```

---

## Appendix: Formula ID Quick Lookup

| Range | Topic | File |
|-------|-------|------|
| F1.1--F1.15 | Linear Algebra | `01_linear_algebra/key_formulas.md` |
| F2.1--F2.15 | Quantum Mechanics | `02_quantum_mechanics/key_formulas.md` |
| F3.1--F3.47 | Quantum Information Theory | `03_quantum_info_theory/key_formulas.md` |
| F4.1--F4.20 | Quantum Error Correction | `04_quantum_error_correction/key_formulas.md` |
| F5.1--F5.17 | Variational Quantum | `05_variational_quantum/key_formulas.md` |
| F6.1--F6.x | Group Theory | `06_group_theory/key_formulas.md` |
| F7.1--F7.x | Graph Theory | `07_graph_theory/key_formulas.md` |
| F8.1--F8.x | Topology | `08_topology/key_formulas.md` |
| F10.1--F10.34 | Optimization | `10_optimization/key_formulas.md` |
| F11.1--F11.54 | ML Theory | `11_ml_theory/key_formulas.md` |
| F12.1--F12.x | ZX-Calculus | `12_zx_calculus/key_formulas.md` |
| F13.1--F13.x | Quantum Compilation | `13_quantum_compilation/key_formulas.md` |
| F14.1--F14.x | Scheduling Theory | `14_scheduling_theory/key_formulas.md` |
| F15.1--F15.x | Quantum Hardware | `15_quantum_hardware/key_formulas.md` |
| F16.1--F16.x | Statistical Mechanics | `16_statistical_mechanics/key_formulas.md` |
| F17.1--F17.x | Experimental Methods | `17_experimental_methods/key_formulas.md` |
