# Domain Terminology Glossary

> **Purpose**: Quick-reference for paper writing and reviewer communication
> **Scope**: 120+ terms across 8 categories, mapped to KB derivation files
> **Last updated**: 2026-03-24

---

## How to Use

- **Paper writing**: Look up the standard English term and its common paper phrasing
- **Reviewer response**: Find precise definitions to cite in rebuttals
- **Cross-reference**: Each term links to the KB file with full derivations
- **Notation**: KB paths are relative to the repository root

---

## 1. Quantum Computing Basics (量子计算基础)

| Term | 中文 | Definition | KB Reference | Common Usage |
|------|------|------------|-------------|--------------|
| **Qubit** | 量子比特 | A two-level quantum system described by $\|\psi\rangle = \alpha\|0\rangle + \beta\|1\rangle$ with $\|\alpha\|^2 + \|\beta\|^2 = 1$. The fundamental unit of quantum information. | `02_quantum_mechanics/derivations/density_matrix_formalism.md` | "We use $n$ qubits to encode..." |
| **Superposition** | 叠加态 | A quantum state that is a linear combination of basis states, enabling parallelism in quantum computation. | `02_quantum_mechanics/key_formulas.md` (F2.1) | "The qubit is prepared in a superposition of computational basis states." |
| **Entanglement** | 纠缠 | A quantum correlation between subsystems that cannot be described by product states. Quantified by measures such as concurrence or entanglement entropy. | `03_quantum_info_theory/derivations/entanglement_theory.md` | "Entanglement is a key resource for quantum error correction." |
| **Decoherence** | 退相干 | The process by which a quantum system loses coherence through interaction with its environment, effectively turning quantum superpositions into classical mixtures. | `02_quantum_mechanics/derivations/quantum_channels_kraus.md` | "Decoherence limits the circuit depth achievable on NISQ devices." |
| **Quantum gate** | 量子门 | A unitary operation acting on qubits. Common single-qubit gates: X, Y, Z, H, S, T. Common two-qubit gate: CNOT. | `01_linear_algebra/derivations/matrix_exponential.md` | "We decompose the unitary into a sequence of native gates." |
| **Circuit depth** | 线路深度 | The number of time steps (layers of parallel gates) in a quantum circuit. A proxy for execution time and noise accumulation. | `13_quantum_compilation/key_formulas.md` | "Our method reduces circuit depth by 30%." |
| **Circuit width** | 线路宽度 | The number of qubits used in a quantum circuit. | `13_quantum_compilation/derivations/qubit_routing_theory.md` | "The circuit width is bounded by the number of physical qubits." |
| **Unitary** | 酉算子/酉矩阵 | A matrix $U$ satisfying $U^\dagger U = UU^\dagger = I$. All quantum gates are unitary; ensures norm preservation. | `01_linear_algebra/derivations/spectral_decomposition.md` | "The time evolution is governed by a unitary operator." |
| **Hermitian operator** | 厄米算子 | A matrix $A$ satisfying $A = A^\dagger$. Observables in quantum mechanics are Hermitian; eigenvalues are real. | `01_linear_algebra/derivations/spectral_decomposition.md` | "The Hamiltonian is a Hermitian operator on the Hilbert space." |
| **Observable** | 可观测量 | A Hermitian operator representing a measurable physical quantity. Its eigenvalues are the possible measurement outcomes. | `02_quantum_mechanics/derivations/measurement_theory.md` | "We measure the observable $Z \otimes Z$ to extract the syndrome." |
| **Measurement** | 测量 | The process of extracting classical information from a quantum state. Projective (von Neumann) or generalized (POVM). Collapses the state. | `02_quantum_mechanics/derivations/measurement_theory.md` | "Measurement in the computational basis yields..." |
| **Born rule** | 玻恩规则 | The probability of outcome $m$ is $p(m) = \langle\psi\|M_m^\dagger M_m\|\psi\rangle$. The fundamental link between quantum states and measurement probabilities. | `02_quantum_mechanics/key_formulas.md` (F2.4) | "By the Born rule, the probability of measuring $\|0\rangle$ is $\|\alpha\|^2$." |
| **No-cloning theorem** | 不可克隆定理 | It is impossible to create an identical copy of an arbitrary unknown quantum state. A fundamental constraint motivating QEC. | `02_quantum_mechanics/key_formulas.md` | "The no-cloning theorem prevents direct copying of quantum information." |
| **Quantum teleportation** | 量子隐形传态 | A protocol to transmit a qubit using a shared Bell pair and two classical bits. Foundational for quantum networks and lattice surgery. | `03_quantum_info_theory/derivations/entanglement_theory.md` | "Logical operations are implemented via gate teleportation." |
| **Superdense coding** | 超密编码 | A protocol to send two classical bits using one qubit and a shared Bell pair. The converse of teleportation. | `03_quantum_info_theory/derivations/entanglement_theory.md` | "Superdense coding demonstrates the information-theoretic power of entanglement." |
| **Bell state** | 贝尔态 | One of four maximally entangled two-qubit states: $\|\Phi^{\pm}\rangle = (\|00\rangle \pm \|11\rangle)/\sqrt{2}$, $\|\Psi^{\pm}\rangle = (\|01\rangle \pm \|10\rangle)/\sqrt{2}$. | `03_quantum_info_theory/derivations/entanglement_theory.md` | "The ancilla qubits are initialized in Bell states." |
| **GHZ state** | GHZ态 | The $n$-qubit state $(\|0\rangle^{\otimes n} + \|1\rangle^{\otimes n})/\sqrt{2}$. Maximally entangled multi-qubit state; useful for benchmarking. | `02_quantum_mechanics/key_formulas.md` | "We prepare a GHZ state to verify multi-qubit entanglement." |
| **W state** | W态 | The $n$-qubit state $(1/\sqrt{n})(\|100\ldots0\rangle + \|010\ldots0\rangle + \ldots + \|00\ldots01\rangle)$. Robust entanglement that persists under particle loss. | `03_quantum_info_theory/derivations/entanglement_theory.md` | "Unlike GHZ states, W states retain bipartite entanglement upon tracing out one qubit." |
| **Bloch sphere** | 布洛赫球 | Geometric representation of a single qubit state as a point on the unit sphere: $\|\psi\rangle = \cos(\theta/2)\|0\rangle + e^{i\phi}\sin(\theta/2)\|1\rangle$. | `02_quantum_mechanics/derivations/density_matrix_formalism.md` | "The rotation on the Bloch sphere corresponds to..." |
| **Pauli matrices** | 泡利矩阵 | The four single-qubit operators $\{I, X, Y, Z\}$ forming a basis for $2\times2$ Hermitian matrices. $X$ = bit-flip, $Z$ = phase-flip, $Y = iXZ$. | `06_group_theory/derivations/pauli_group.md` | "Errors are expressed in the Pauli basis $\{I, X, Y, Z\}^{\otimes n}$." |
| **Density matrix** | 密度矩阵 | A positive semidefinite, unit-trace matrix $\rho$ representing a (possibly mixed) quantum state. Generalizes the state vector formalism. | `02_quantum_mechanics/derivations/density_matrix_formalism.md` | "The system state is described by the density matrix $\rho$." |
| **Fidelity** | 保真度 | A measure of closeness between quantum states: $F(\rho,\sigma) = (\mathrm{tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}})^2$. Equals 1 for identical states. | `02_quantum_mechanics/derivations/fidelity_and_trace_distance.md` | "We achieve a state fidelity of 99.5%." |
| **Trace distance** | 迹距离 | Distinguishability metric: $T(\rho,\sigma) = \frac{1}{2}\|\rho - \sigma\|_1$. Operationally, the maximum distinguishing probability. | `02_quantum_mechanics/derivations/fidelity_and_trace_distance.md` | "The trace distance to the ideal state is bounded by..." |

---

## 2. Quantum Error Correction (量子纠错)

| Term | 中文 | Definition | KB Reference | Common Usage |
|------|------|------------|-------------|--------------|
| **Logical qubit** | 逻辑量子比特 | A qubit encoded redundantly across multiple physical qubits via a QEC code. Protected from noise up to the code distance. | `04_quantum_error_correction/derivations/stabilizer_formalism.md` | "Each logical qubit is encoded in $d^2$ physical qubits." |
| **Physical qubit** | 物理量子比特 | A single hardware-level qubit subject to noise. Multiple physical qubits compose a logical qubit. | `04_quantum_error_correction/key_formulas.md` | "The overhead is $n/k$ physical qubits per logical qubit." |
| **Code distance** | 码距 | The minimum weight of a nontrivial logical operator; a $[[n,k,d]]$ code can correct $\lfloor(d-1)/2\rfloor$ errors. | `04_quantum_error_correction/derivations/code_distance_bounds.md` | "We demonstrate improved performance at code distance $d = 5$." |
| **Code rate** | 码率 | The ratio $k/n$ of logical to physical qubits. Higher rate means less overhead but typically lower distance. | `04_quantum_error_correction/derivations/quantum_ldpc_codes.md` | "LDPC codes achieve constant rate $k/n = \Theta(1)$." |
| **Stabilizer** | 稳定子 | An element of the stabilizer group $\mathcal{S} \subset \mathcal{P}_n$ that fixes all codewords: $g\|\psi\rangle = \|\psi\rangle$ for all $g \in \mathcal{S}$. | `04_quantum_error_correction/derivations/stabilizer_formalism.md` | "The stabilizer generators are measured each round." |
| **Syndrome** | 校验子/综合征 | The binary vector $\mathbf{s} = (s_1,\ldots,s_{n-k})$ obtained from stabilizer measurements, identifying the error equivalence class without revealing the encoded state. | `04_quantum_error_correction/key_formulas.md` (F4.3) | "The decoder takes the syndrome as input." |
| **Decoder** | 译码器 | An algorithm that maps syndromes to recovery operations. Examples: MWPM, Union-Find, neural decoders. | `04_quantum_error_correction/derivations/decoder_theory.md` | "We propose a GNN-based decoder that achieves near-optimal accuracy." |
| **Threshold** | 阈值 | The physical error rate below which increasing code distance exponentially suppresses logical error rate. | `04_quantum_error_correction/derivations/threshold_theorem.md` | "The surface code has a threshold of approximately 1%." |
| **Surface code** | 表面码 | A topological stabilizer code on a 2D lattice with $[[d^2, 1, d]]$ parameters using only nearest-neighbor interactions. The leading candidate for FTQC. | `04_quantum_error_correction/derivations/surface_code_basics.md` | "We benchmark on the rotated surface code." |
| **Toric code** | 环面码 | Kitaev's topological code on a torus with $[[2d^2, 2, d]]$ parameters. The periodic-boundary version of the surface code. | `04_quantum_error_correction/derivations/surface_code_basics.md` | "The toric code is defined on a periodic lattice." |
| **Color code** | 色码 | A topological code on a trivalent, 3-colorable lattice supporting transversal Clifford gates. | `04_quantum_error_correction/derivations/css_codes.md` | "Color codes allow transversal implementation of the full Clifford group." |
| **CSS code** | CSS码 | Calderbank-Shor-Steane code: constructed from two classical codes $C_2 \subseteq C_1$, with X- and Z-stabilizers derived independently. | `04_quantum_error_correction/derivations/css_codes.md` | "The surface code is a CSS code with X and Z stabilizers on faces and vertices." |
| **LDPC code** | 低密度奇偶校验码 | A code whose parity-check matrix is sparse (each row/column has $O(1)$ nonzeros). Quantum LDPC codes promise constant-rate, growing-distance codes. | `04_quantum_error_correction/derivations/quantum_ldpc_codes.md` | "Recent qLDPC codes achieve $[[n, \Theta(n), \Theta(n)]]$ parameters." |
| **Steane code** | Steane码 | The $[[7,1,3]]$ CSS code based on the classical Hamming code. The smallest code supporting transversal CNOT. | `04_quantum_error_correction/derivations/css_codes.md` | "We use the Steane code as a pedagogical example." |
| **Repetition code** | 重复码 | The simplest QEC code: $[[n,1,n]]$ for bit-flip or phase-flip (but not both). Used for benchmarking. | `04_quantum_error_correction/derivations/stabilizer_formalism.md` | "Experiments on the repetition code demonstrate error suppression." |
| **Fault-tolerant** | 容错的 | A procedure where a single component failure causes at most one error in each encoded block, preventing error propagation. | `04_quantum_error_correction/derivations/fault_tolerant_gates.md` | "We implement fault-tolerant syndrome extraction." |
| **Transversal gate** | 横向门 | A logical gate applied by performing the same gate independently on each physical qubit. Inherently fault-tolerant. | `04_quantum_error_correction/derivations/fault_tolerant_gates.md` | "Transversal CNOT is available in CSS codes." |
| **Magic state** | 魔态 | A non-stabilizer state (e.g., $T\|+\rangle$) that, combined with Clifford gates and distillation, enables universal computation. | `04_quantum_error_correction/derivations/magic_state_distillation.md` | "Universal FTQC requires magic state distillation." |
| **Lattice surgery** | 晶格手术 | A method for performing logical operations on surface codes by merging and splitting code patches through boundary manipulation. | `10_optimization/derivations/lattice_surgery_compilation_bounds.md` | "Logical CNOT is implemented via lattice surgery." |
| **Code capacity noise** | 码容量噪声 | A noise model where errors occur only on data qubits; syndrome measurements are perfect. Provides an upper bound on threshold. | `04_quantum_error_correction/derivations/noise_models.md` | "Under code capacity noise, the threshold is $\sim$10.9%." |
| **Phenomenological noise** | 唯象噪声 | A noise model adding measurement errors to code capacity: data qubit errors plus syndrome bit-flip errors. | `04_quantum_error_correction/derivations/noise_models.md` | "The phenomenological threshold is approximately 3%." |
| **Circuit-level noise** | 电路级噪声 | The most realistic noise model: errors on all gate, preparation, measurement, and idle operations within the syndrome extraction circuit. | `04_quantum_error_correction/derivations/noise_models.md` | "We evaluate under circuit-level depolarizing noise at $p = 10^{-3}$." |
| **Detection event** | 探测事件 | A change in syndrome value between consecutive measurement rounds, indicating a possible error. Forms the input to space-time decoders. | `04_quantum_error_correction/derivations/decoder_theory.md` | "Detection events are mapped to edges in the matching graph." |
| **Hook error** | 钩形错误 | A single fault in a CNOT gate during syndrome extraction that propagates to a weight-2 data error, creating a correlated error pattern. | `04_quantum_error_correction/derivations/noise_models.md` | "Hook errors must be accounted for in the matching graph construction." |
| **Logical error rate** | 逻辑错误率 | The probability of a logical (undetectable) error per round or per shot. Should decrease exponentially with code distance below threshold. | `04_quantum_error_correction/derivations/threshold_theorem.md` | "$p_L \propto (p/p_{\mathrm{th}})^{\lfloor d/2 \rfloor}$." |

---

## 3. Quantum Hardware (量子硬件)

| Term | 中文 | Definition | KB Reference | Common Usage |
|------|------|------------|-------------|--------------|
| **Transmon** | 传输子量子比特 | A superconducting charge qubit with reduced charge noise sensitivity via a large $E_J/E_C$ ratio. The dominant qubit modality. | (hardware -- no dedicated KB file) | "Experiments are performed on a transmon-based processor." |
| **$T_1$ (relaxation time)** | 纵向弛豫时间 | The timescale for energy decay from $\|1\rangle$ to $\|0\rangle$. Limits the coherence of the excited state. | `02_quantum_mechanics/derivations/quantum_channels_kraus.md` | "$T_1$ times range from 50 to 200 $\mu$s." |
| **$T_2$ (dephasing time)** | 横向弛豫时间 | The timescale for loss of phase coherence. $T_2 \leq 2T_1$. Determines how long superpositions survive. | `02_quantum_mechanics/derivations/quantum_channels_kraus.md` | "The $T_2$ echo time exceeds 100 $\mu$s." |
| **Gate fidelity** | 门保真度 | The closeness of an implemented gate to the ideal unitary, typically measured via randomized benchmarking (RB). | `02_quantum_mechanics/derivations/fidelity_and_trace_distance.md` | "Two-qubit gate fidelities exceed 99.5%." |
| **Readout fidelity** | 读出保真度 | The probability of correctly assigning the measurement outcome $\|0\rangle$ or $\|1\rangle$. | (hardware -- no dedicated KB file) | "Readout fidelity is 98.7% for $\|0\rangle$ and 97.2% for $\|1\rangle$." |
| **Coupling map** | 耦合图/连接图 | The graph describing which pairs of physical qubits can directly interact via two-qubit gates. | `13_quantum_compilation/derivations/qubit_routing_theory.md` | "The coupling map of the 127-qubit processor is a heavy-hex lattice." |
| **Connectivity** | 连通性 | The degree or structure of the coupling map. Higher connectivity reduces routing overhead. | `13_quantum_compilation/derivations/qubit_routing_theory.md` | "Limited connectivity necessitates SWAP insertion." |
| **Crosstalk** | 串扰 | Unwanted interactions between qubits or control lines during gate operations, causing correlated errors. | `04_quantum_error_correction/derivations/noise_models.md` | "Crosstalk is mitigated by gate scheduling constraints." |
| **Leakage** | 泄漏 | Population escaping from the computational subspace $\{\|0\rangle, \|1\rangle\}$ to higher energy levels. | (hardware -- no dedicated KB file) | "Leakage reduction units are inserted every $d$ rounds." |
| **Calibration** | 标定/校准 | The process of tuning control parameters (frequencies, pulse shapes, amplitudes) to optimize gate performance. | (hardware -- no dedicated KB file) | "Calibration is performed daily to maintain gate fidelities." |
| **Quantum volume (QV)** | 量子体积 | A holistic benchmark: the largest $n$ such that a random $n$-qubit circuit of depth $n$ can be executed reliably. $QV = 2^n$. | (hardware -- no dedicated KB file) | "The device achieves a quantum volume of 128." |
| **CLOPS** | 电路层每秒操作数 | Circuit Layer Operations Per Second. Measures the speed of executing parameterized circuits. | (hardware -- no dedicated KB file) | "The system achieves 10K CLOPS." |
| **XEB** | 线性交叉熵基准 | Cross-entropy benchmarking: compares the output distribution of a random circuit to the ideal, used in quantum advantage claims. | (hardware -- no dedicated KB file) | "XEB fidelity is used to validate quantum computational advantage." |
| **NISQ** | 含噪中等规模量子 | Noisy Intermediate-Scale Quantum: current-era devices with 50--1000+ qubits but no full error correction. | `05_variational_quantum/key_formulas.md` | "Our algorithm is designed for the NISQ regime." |
| **FTQC** | 容错量子计算 | Fault-Tolerant Quantum Computing: the target regime where logical error rates are suppressed to arbitrary precision via QEC. | `04_quantum_error_correction/derivations/threshold_theorem.md` | "FTQC requires physical error rates below the threshold." |
| **Superconducting** | 超导（体系） | Qubit technology based on superconducting circuits (transmons, fluxoniums). Dominant platform (IBM, Google, BAQIS Quafu). | (hardware -- no dedicated KB file) | "We execute on a superconducting quantum processor." |
| **Trapped ion** | 离子阱 | Qubit technology using individual ions confined by electromagnetic fields. High fidelity, all-to-all connectivity, slower gates. | (hardware -- no dedicated KB file) | "Trapped-ion systems achieve two-qubit fidelities $>$99.9%." |
| **Neutral atom** | 中性原子 | Qubit technology using atoms held in optical tweezers. Supports reconfigurable connectivity and native multi-qubit gates. | (hardware -- no dedicated KB file) | "Neutral-atom platforms enable long-range entangling gates." |

---

## 4. Quantum Algorithms (量子算法)

| Term | 中文 | Definition | KB Reference | Common Usage |
|------|------|------------|-------------|--------------|
| **VQE** | 变分量子本征求解器 | Variational Quantum Eigensolver: a hybrid algorithm that minimizes $\langle\psi(\theta)\|H\|\psi(\theta)\rangle$ to find ground state energies. | `05_variational_quantum/derivations/vqe_theory.md` | "VQE is applied to find the ground state of the molecular Hamiltonian." |
| **QAOA** | 量子近似优化算法 | Quantum Approximate Optimization Algorithm: alternates cost ($e^{-i\gamma C}$) and mixer ($e^{-i\beta B}$) unitaries to solve combinatorial optimization. | `05_variational_quantum/derivations/qaoa_theory.md` | "We benchmark QAOA at depth $p = 3$ on MaxCut." |
| **Grover's algorithm** | Grover搜索算法 | Provides quadratic speedup for unstructured search: finds a marked item in $O(\sqrt{N})$ queries. | `02_quantum_mechanics/key_formulas.md` | "Grover's algorithm achieves a provable quadratic speedup." |
| **Shor's algorithm** | Shor分解算法 | Factors integers in polynomial time using quantum Fourier transform. The canonical example of exponential quantum speedup. | `02_quantum_mechanics/key_formulas.md` | "Shor's algorithm demonstrates exponential quantum advantage for factoring." |
| **HHL algorithm** | HHL算法 | Solves linear systems $Ax = b$ with exponential speedup in system size (under certain conditions). | `02_quantum_mechanics/key_formulas.md` | "The HHL algorithm solves sparse linear systems exponentially faster." |
| **Variational** | 变分的 | A hybrid quantum-classical paradigm where a parameterized quantum circuit is optimized by a classical optimizer. | `05_variational_quantum/key_formulas.md` | "We adopt a variational approach to mitigate noise." |
| **Ansatz** | 拟设/变分电路结构 | The parameterized quantum circuit used in variational algorithms. Choice of ansatz critically affects expressibility and trainability. | `05_variational_quantum/derivations/vqe_theory.md` | "We use a hardware-efficient ansatz with $L$ layers." |
| **Parameter shift rule** | 参数位移规则 | A method to compute exact gradients of expectation values on quantum hardware: $\partial_\theta f = [f(\theta+\pi/2) - f(\theta-\pi/2)]/2$. | `05_variational_quantum/key_formulas.md` (F5.5) | "Gradients are estimated via the parameter shift rule." |
| **Barren plateau** | 贫瘠高原 | A phenomenon where the gradient variance vanishes exponentially with system size, making optimization intractable. | `05_variational_quantum/derivations/barren_plateaus.md` | "Random ansatze suffer from barren plateaus." |
| **Quantum advantage** | 量子优势 | A rigorous demonstration that a quantum device solves a specific task faster than any known classical method. | (general -- no dedicated KB file) | "We provide evidence of quantum advantage for this sampling task." |
| **Quantum supremacy** | 量子霸权/量子优越性 | The milestone of performing a computation infeasible for classical computers, regardless of practical utility. Coined by Preskill. | (general -- no dedicated KB file) | "Quantum supremacy was first claimed by Google in 2019." |
| **Quantum speedup** | 量子加速 | The ratio of classical to quantum computational complexity for a given problem. Can be polynomial or exponential. | (general -- no dedicated KB file) | "The algorithm provides a quadratic quantum speedup." |
| **BQP** | 有界量子多项式时间 | Bounded-error Quantum Polynomial time: the class of decision problems solvable by a quantum computer in polynomial time. | (complexity -- no dedicated KB file) | "Factoring is in BQP but believed not in BPP." |
| **QMA** | 量子梅林-亚瑟 | Quantum Merlin-Arthur: the quantum analogue of NP. A complexity class where a quantum verifier checks a quantum proof. | (complexity -- no dedicated KB file) | "The local Hamiltonian problem is QMA-complete." |
| **Error mitigation** | 错误缓解 | Techniques to reduce the effect of noise in NISQ computations without full QEC (e.g., ZNE, PEC, Clifford data regression). | `05_variational_quantum/derivations/error_mitigation.md` | "We apply zero-noise extrapolation to mitigate errors." |

---

## 5. Machine Learning for Quantum (机器学习与量子)

| Term | 中文 | Definition | KB Reference | Common Usage |
|------|------|------------|-------------|--------------|
| **GNN** | 图神经网络 | Graph Neural Network: a neural architecture that operates on graph-structured data via message passing between nodes. | `11_ml_theory/derivations/gnn_message_passing.md` | "We use a GNN to process the syndrome graph." |
| **Diffusion model** | 扩散模型 | A generative model that learns to reverse a gradual noising process. Produces samples by iterative denoising. | `11_ml_theory/derivations/diffusion_models_math.md` | "We train a diffusion model to generate solutions to the CO problem." |
| **DDPM** | 去噪扩散概率模型 | Denoising Diffusion Probabilistic Model: the foundational continuous diffusion framework by Ho et al. (2020). | `11_ml_theory/derivations/diffusion_models_math.md` | "Our model builds on the DDPM framework." |
| **Score matching** | 得分匹配 | A method to estimate the score function $\nabla_x \log p(x)$ without computing the normalization constant. | `11_ml_theory/derivations/score_matching.md` | "The network is trained via denoising score matching." |
| **D3PM** | 离散去噪扩散概率模型 | Discrete Denoising Diffusion Probabilistic Model: extends diffusion to discrete state spaces using transition matrices. | `11_ml_theory/derivations/discrete_diffusion_d3pm.md` | "D3PM is used for graph generation with discrete node/edge types." |
| **Flow matching** | 流匹配 | A simulation-free framework for training continuous normalizing flows by regressing on conditional vector fields. | `11_ml_theory/derivations/flow_matching.md` | "Flow matching provides a simpler training objective than score-based methods." |
| **Score SDE** | 得分SDE | A unified framework (Song et al., 2021) casting diffusion as stochastic differential equations with score-based reverse processes. | `11_ml_theory/key_formulas.md` (F11.8) | "We adopt the VP-SDE formulation from Song et al." |
| **Reinforcement learning (RL)** | 强化学习 | A learning paradigm where an agent learns to maximize cumulative reward through interaction with an environment. | `11_ml_theory/derivations/reinforcement_learning_basics.md` | "The decoder policy is trained via reinforcement learning." |
| **MCTS** | 蒙特卡洛树搜索 | Monte Carlo Tree Search: a search algorithm combining tree exploration with random sampling. Used in AlphaGo and circuit optimization. | `11_ml_theory/derivations/reinforcement_learning_basics.md` | "MCTS is used to guide the circuit compilation search." |
| **Attention mechanism** | 注意力机制 | A mechanism that computes weighted aggregation of values based on query-key compatibility: $\mathrm{Attn}(Q,K,V) = \mathrm{softmax}(QK^T/\sqrt{d_k})V$. | `11_ml_theory/derivations/attention_mechanism.md` | "We use multi-head attention to capture long-range dependencies." |
| **Neural decoder** | 神经网络译码器 | A decoder for QEC that uses neural networks (GNN, CNN, Transformer) to map syndromes to corrections. | `04_quantum_error_correction/derivations/decoder_theory.md` | "The neural decoder achieves near-MWPM accuracy with lower latency." |
| **Neural compiler** | 神经网络编译器 | A neural network that learns to compile/optimize quantum circuits, e.g., via RL or diffusion. | `13_quantum_compilation/derivations/routing_algorithms.md` | "Our neural compiler reduces SWAP count by 15%." |
| **Heatmap decoding** | 热力图解码 | A decoding paradigm where a neural network outputs per-qubit error probabilities, then a classical algorithm (e.g., MWPM) uses them as edge weights. | `04_quantum_error_correction/derivations/decoder_theory.md` | "Heatmap decoding combines neural networks with MWPM." |
| **Guided diffusion** | 引导扩散 | Conditioning the diffusion sampling process using external signals (classifier guidance or classifier-free guidance). | `11_ml_theory/derivations/diffusion_models_math.md` | "We apply guided diffusion to enforce hardware constraints." |
| **ELBO** | 证据下界 | Evidence Lower Bound: $\log p(x) \geq \mathbb{E}_{q(z|x)}[\log p(x|z)] - D_{KL}(q\|p)$. The training objective for VAEs and foundation of diffusion model losses. | `11_ml_theory/derivations/elbo_derivation.md` | "The training loss is derived from the ELBO." |

---

## 6. Combinatorial Optimization (组合优化)

| Term | 中文 | Definition | KB Reference | Common Usage |
|------|------|------------|-------------|--------------|
| **MIS** | 最大独立集 | Maximum Independent Set: find the largest set of pairwise non-adjacent vertices in a graph. NP-hard. | `10_optimization/derivations/np_hard_problems.md` | "We solve MIS on Erdos-Renyi graphs with $n = 500$." |
| **MCl** | 最大团 | Maximum Clique: find the largest complete subgraph. Equivalent to MIS on the complement graph. | `10_optimization/derivations/np_hard_problems.md` | "MCl can be reduced from MIS on the complement graph." |
| **MVC** | 最小顶点覆盖 | Minimum Vertex Cover: find the smallest set of vertices covering all edges. Complement of MIS. | `10_optimization/derivations/np_hard_problems.md` | "MVC admits a 2-approximation via matching." |
| **MCut / MaxCut** | 最大割 | Maximum Cut: partition vertices into two sets to maximize the number of cut edges. Classic QAOA benchmark. | `10_optimization/derivations/np_hard_problems.md` | "We evaluate on MaxCut instances with edge weights." |
| **TSP** | 旅行商问题 | Travelling Salesman Problem: find the shortest Hamiltonian cycle visiting all cities. The canonical NP-hard routing problem. | `10_optimization/derivations/np_hard_problems.md` | "We benchmark on TSP instances with $n = 100$ cities." |
| **QUBO** | 二次无约束二值优化 | Quadratic Unconstrained Binary Optimization: $\min_{x \in \{0,1\}^n} x^T Q x$. The standard formulation for quantum annealers and QAOA. | `10_optimization/derivations/qubo_ising_mapping.md` | "The problem is cast as a QUBO for quantum optimization." |
| **Ising model** | 伊辛模型 | A model of interacting spins: $H = -\sum_{ij} J_{ij} s_i s_j - \sum_i h_i s_i$ with $s_i \in \{-1, +1\}$. Equivalent to QUBO under variable substitution. | `10_optimization/derivations/qubo_ising_mapping.md` | "The cost function is mapped to an Ising Hamiltonian." |
| **Approximation ratio** | 近似比 | The worst-case ratio of the solution quality to the optimal: $\alpha = \mathrm{ALG}/\mathrm{OPT}$. Measures algorithm performance guarantees. | `10_optimization/derivations/np_hard_problems.md` | "Our method achieves an approximation ratio of 0.95." |
| **NP-hard** | NP困难 | A problem class at least as hard as any problem in NP. No known polynomial-time algorithm exists (assuming $P \neq NP$). | `10_optimization/derivations/np_hard_problems.md` | "Qubit routing is NP-hard in general." |
| **Heuristic** | 启发式算法 | An algorithm that finds good (but not provably optimal) solutions efficiently. Includes greedy, local search, metaheuristics. | `10_optimization/derivations/neural_co_theory.md` | "We compare against classical heuristics including simulated annealing." |

---

## 7. Graph Theory (图论)

| Term | 中文 | Definition | KB Reference | Common Usage |
|------|------|------------|-------------|--------------|
| **Adjacency matrix** | 邻接矩阵 | A matrix $A \in \{0,1\}^{n \times n}$ where $A_{ij} = 1$ iff vertices $i$ and $j$ are connected. The standard graph representation. | `07_graph_theory/derivations/spectral_graph_theory.md` | "The graph is represented by its adjacency matrix." |
| **Laplacian matrix** | 拉普拉斯矩阵 | $L = D - A$ where $D$ is the degree matrix. Eigenvalues encode connectivity properties (e.g., algebraic connectivity = second smallest eigenvalue). | `07_graph_theory/derivations/spectral_graph_theory.md` | "We use the normalized Laplacian as positional encoding." |
| **Spectral decomposition** | 谱分解 | Decomposing a symmetric matrix into eigenvalue-eigenvector pairs: $A = \sum_i \lambda_i v_i v_i^T$. Basis of spectral graph theory. | `01_linear_algebra/derivations/spectral_decomposition.md` | "Spectral features are extracted from the graph Laplacian." |
| **Chromatic number** | 色数 | The minimum number of colors needed to color vertices such that no adjacent vertices share a color: $\chi(G)$. | `14_scheduling_theory/derivations/graph_coloring_theory.md` | "The chromatic number determines the minimum schedule length." |
| **Tanner graph** | Tanner图 | A bipartite graph representing a parity-check code: variable nodes (qubits) and check nodes (stabilizers) connected by edges. | `07_graph_theory/derivations/tanner_graphs.md` | "The quantum code is described by its Tanner graph." |
| **WL test** | WL测试 | Weisfeiler-Leman graph isomorphism test: iteratively refines node labels by aggregating neighbor information. Defines the expressiveness ceiling for GNNs. | `07_graph_theory/derivations/wl_test_expressiveness.md` | "GIN is provably as expressive as the 1-WL test." |
| **Message passing** | 消息传递 | The GNN computation paradigm: each node aggregates messages from neighbors, then updates its representation. Equivalent to 1-WL in expressiveness. | `11_ml_theory/derivations/gnn_message_passing.md` | "The decoder uses $L$ rounds of message passing." |
| **Graph isomorphism** | 图同构 | Two graphs are isomorphic if there exists a bijection preserving adjacency. Testing isomorphism is in NP but not known to be NP-complete or in P. | `07_graph_theory/derivations/wl_test_expressiveness.md` | "The WL test provides a necessary condition for graph isomorphism." |
| **GCN** | 图卷积网络 | Graph Convolutional Network (Kipf & Welling, 2017): spectral-based GNN using first-order Chebyshev approximation of graph convolutions. | `11_ml_theory/derivations/gnn_message_passing.md` | "We use a 3-layer GCN as the encoder." |
| **GAT** | 图注意力网络 | Graph Attention Network (Velickovic et al., 2018): GNN using attention weights for neighbor aggregation. | `11_ml_theory/derivations/gnn_message_passing.md` | "GAT learns adaptive aggregation weights." |
| **GIN** | 图同构网络 | Graph Isomorphism Network (Xu et al., 2019): maximally expressive GNN matching the 1-WL test. Uses sum aggregation + MLP. | `07_graph_theory/derivations/wl_test_expressiveness.md` | "GIN provides the most expressive message passing framework." |

---

## 8. ZX-Calculus (ZX演算)

| Term | 中文 | Definition | KB Reference | Common Usage |
|------|------|------------|-------------|--------------|
| **Z-spider** | Z-蜘蛛 | Green node in ZX diagrams: $\|0\rangle^{\otimes m}\langle 0\|^{\otimes n} + e^{i\alpha}\|1\rangle^{\otimes m}\langle 1\|^{\otimes n}$. Copies Z-basis information. | `12_zx_calculus/derivations/zx_basics.md`, F12.1 | "Each CNOT is decomposed into Z- and X-spiders." |
| **X-spider** | X-蜘蛛 | Red node in ZX diagrams: the Hadamard-conjugate of Z-spider. Copies X-basis information. | `12_zx_calculus/derivations/zx_basics.md`, F12.2 | "X-spiders represent operations diagonal in the Hadamard basis." |
| **Phase** | 相位 | The parameter $\alpha \in [0, 2\pi)$ of a spider. Phase $0$ = Clifford (copy), $\pi/2$ = S gate, $\pi/4$ = T gate. | `12_zx_calculus/derivations/zx_basics.md` | "Non-Clifford phases correspond to T gates." |
| **Fusion rule** | 融合规则 | Two connected same-color spiders merge into one with summed phases: $Z_\alpha \circ Z_\beta = Z_{\alpha+\beta}$. The most-used simplification. | `12_zx_calculus/derivations/zx_rewrite_rules.md`, F12.3 | "Spider fusion reduces the number of nodes." |
| **Color change rule** | 颜色变换规则 | Hadamard gates on all legs convert $Z \leftrightarrow X$: $H^{\otimes m} Z_\alpha H^{\otimes n} = X_\alpha$. | `12_zx_calculus/derivations/zx_rewrite_rules.md`, F12.4 | "Color change is applied to commute through Hadamards." |
| **Bialgebra rule** | 双代数规则 | Describes how Z- and X-spiders interact when they have no phases: different-color spiders "slide through" each other. | `12_zx_calculus/derivations/zx_rewrite_rules.md`, F12.5 | "The bialgebra law governs Z-X interaction." |
| **Graph-like form** | 图状形式 | A ZX diagram where all spiders are Z-type, all connections pass through Hadamard boxes, and there are no parallel edges or self-loops. Every diagram can be reduced to this form. | `12_zx_calculus/derivations/zx_circuit_optimization.md` | "The circuit is first converted to graph-like form for optimization." |
| **Gflow** | 广义流 | Generalized flow: a combinatorial condition on an open graph ensuring deterministic computation in measurement-based QC. Generalizes causal flow. | `12_zx_calculus/derivations/zx_graph_states.md` | "The graph state has gflow, ensuring it implements a unitary." |
| **T-count** | T门计数 | The number of T gates ($\pi/4$ rotations) in a circuit. The dominant cost metric for fault-tolerant circuits since each T requires magic state distillation. | `12_zx_calculus/derivations/zx_circuit_optimization.md` | "ZX optimization reduces the T-count from 28 to 17." |
| **PyZX** | PyZX工具 | An open-source Python library for ZX-calculus manipulation: circuit-to-ZX conversion, automated simplification, extraction. | `12_zx_calculus/derivations/zx_circuit_optimization.md` | "We use PyZX for T-count optimization." |
| **Local complementation** | 局部互补 | A graph operation that complements the neighborhood of a vertex. Preserves the entanglement class of graph states. | `12_zx_calculus/derivations/zx_graph_states.md` | "LC equivalence classes partition graph states." |
| **Pivot** | 枢轴操作 | A graph operation equivalent to two local complementations. Used in ZX simplification to eliminate interior Clifford spiders. | `12_zx_calculus/derivations/zx_graph_states.md` | "Pivoting simplifies the ZX diagram by removing nodes." |

---

## Cross-Reference Index

For multi-topic lookups, use these mappings:

| If you need... | Start with... |
|----------------|---------------|
| QEC code parameters ($n, k, d$) | Section 2 + `04_quantum_error_correction/key_formulas.md` |
| Noise model definitions | Section 2 (noise terms) + `04.../derivations/noise_models.md` |
| Diffusion model math | Section 5 (DDPM, D3PM, etc.) + `11_ml_theory/key_formulas.md` |
| GNN architectures | Section 7 (GCN, GAT, GIN) + `11.../derivations/gnn_message_passing.md` |
| Circuit compilation | Section 3 (coupling map) + Section 8 (T-count) + `13_quantum_compilation/` |
| CO problem definitions | Section 6 + `10_optimization/derivations/np_hard_problems.md` |
| Group-theoretic QEC | Section 2 (stabilizer) + `06_group_theory/` (Pauli group, Clifford group) |
| Topological codes | Section 2 (surface/toric/color) + `08_topology/` (homology, Euler) |
| Scheduling | `14_scheduling_theory/` + Section 7 (chromatic number) |
| ZX for FTQC | Section 8 + `12_zx_calculus/` + Section 2 (magic state, transversal gate) |

---

## Abbreviation Quick-Lookup

| Abbrev. | Full Name | Section |
|---------|-----------|---------|
| BQP | Bounded-error Quantum Polynomial time | 4 |
| CLOPS | Circuit Layer Operations Per Second | 3 |
| CSS | Calderbank-Shor-Steane | 2 |
| D3PM | Discrete Denoising Diffusion Probabilistic Model | 5 |
| DDPM | Denoising Diffusion Probabilistic Model | 5 |
| ELBO | Evidence Lower Bound | 5 |
| FTQC | Fault-Tolerant Quantum Computing | 3 |
| GAT | Graph Attention Network | 7 |
| GCN | Graph Convolutional Network | 7 |
| GIN | Graph Isomorphism Network | 7 |
| GNN | Graph Neural Network | 5, 7 |
| HHL | Harrow-Hassidim-Lloyd | 4 |
| LDPC | Low-Density Parity-Check | 2 |
| MCl | Maximum Clique | 6 |
| MCut | Maximum Cut | 6 |
| MCTS | Monte Carlo Tree Search | 5 |
| MIS | Maximum Independent Set | 6 |
| MVC | Minimum Vertex Cover | 6 |
| MWPM | Minimum Weight Perfect Matching | 2 |
| NISQ | Noisy Intermediate-Scale Quantum | 3 |
| QAOA | Quantum Approximate Optimization Algorithm | 4 |
| QEC | Quantum Error Correction | 2 |
| QMA | Quantum Merlin-Arthur | 4 |
| QUBO | Quadratic Unconstrained Binary Optimization | 6 |
| QV | Quantum Volume | 3 |
| RB | Randomized Benchmarking | 3 |
| RL | Reinforcement Learning | 5 |
| SDE | Stochastic Differential Equation | 5 |
| TSP | Travelling Salesman Problem | 6 |
| VQE | Variational Quantum Eigensolver | 4 |
| WL | Weisfeiler-Leman | 7 |
| XEB | Cross-Entropy Benchmarking | 3 |
| ZNE | Zero-Noise Extrapolation | 4 |
