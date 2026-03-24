# Chapter 13: Quantum Circuit Compilation & Routing - Key Formulas

> 量子线路编译与量子比特路由（Qubit Routing）核心公式速查表。所有公式均使用 LaTeX 记号，解释使用中文。

---

## 映射与路由

### F13.1: Qubit Mapping Problem Definition

给定量子线路 $C$ 作用于逻辑量子比特集合 $Q = \{q_0, q_1, \ldots, q_{n-1}\}$，以及硬件耦合图 $G = (V, E)$，其中 $|V| \geq |Q|$。**量子比特映射**（qubit mapping）是一个单射函数：

$$\pi: Q \to V, \quad \text{s.t.} \quad \pi(q_i) \neq \pi(q_j) \; \forall i \neq j$$

对于线路中的每个两量子比特门 $\text{CNOT}(q_i, q_j)$，需要满足**邻接约束**：

$$(\pi(q_i), \pi(q_j)) \in E$$

若不满足，则需插入 SWAP 操作使逻辑量子比特"移动"到相邻物理位置。

**优化目标**（多目标）：

$$\min_{\pi, \text{SWAPs}} \; \alpha \cdot |\text{SWAPs inserted}| + \beta \cdot \text{depth}(C') + \gamma \cdot \text{fidelity\_loss}(C')$$

其中 $C'$ 是插入 SWAP 后的物理线路。

**Source**: [derivations/qubit_routing_theory.md] | **[Siraichi et al., CGO 2018; Li et al., ASPLOS 2019; Cowtan et al., TCAD 2019]**

---

### F13.2: SWAP Gate Decomposition (3 CNOTs)

SWAP 门可分解为 3 个 CNOT 门：

$$\text{SWAP}(q_i, q_j) = \text{CNOT}(q_i, q_j) \cdot \text{CNOT}(q_j, q_i) \cdot \text{CNOT}(q_i, q_j)$$

矩阵表示：

$$\text{SWAP} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

SWAP 门的作用是交换两个量子比特的量子态：$\text{SWAP}|a, b\rangle = |b, a\rangle$。

由于每个 SWAP 需要 3 个 CNOT，插入 $k$ 个 SWAP 会增加 $3k$ 个 CNOT 门，这是路由开销（routing overhead）的主要来源。

在某些硬件上（如使用 $\sqrt{i\text{SWAP}}$ 原生门），SWAP 可分解为 2 个原生双量子比特门，降低开销。

**Source**: [derivations/qubit_routing_theory.md] | **[Nielsen & Chuang, Exercise 4.17, p.184]**

---

### F13.3: Routing Distance Lower Bound

对于耦合图 $G$ 上的两个物理量子比特 $u, v \in V$，设 $d_G(u, v)$ 为它们在 $G$ 上的**最短路径距离**（shortest path distance）。若当前映射下 $\pi(q_i) = u$, $\pi(q_j) = v$，则执行门 $\text{CNOT}(q_i, q_j)$ 至少需要：

$$\text{SWAPs}_{\min}(q_i, q_j) = d_G(\pi(q_i), \pi(q_j)) - 1$$

**证明**：每次 SWAP 操作将一个量子比特沿边移动一步。初始距离为 $d$，目标是使两个量子比特相邻（距离为 1）。因此至少需要 $d - 1$ 次 SWAP。

**注意**：这是**单对**量子比特的下界。当多对量子比特需要同时路由时，由于路径可能冲突，实际所需 SWAP 数通常大于各对下界之和。

**Source**: [derivations/qubit_routing_theory.md] | **[Cowtan et al., TCAD 2019; Childs et al., QIC 2019]**

---

### F13.4: Token Swapping Problem

**Token Swapping** 是路由问题的图论抽象。给定图 $G = (V, E)$，每个顶点上放置一个标记（token），初始排列为 $\sigma$，目标排列为 $\tau$（通常取 $\tau = \text{id}$）。每步操作选择一条边 $(u, v) \in E$，交换 $u$ 和 $v$ 上的标记。目标是：

$$\min \; |\text{swap sequence}| \quad \text{s.t.} \quad \text{final permutation} = \tau \circ \sigma^{-1}$$

等价地，需要将排列 $\pi = \tau \circ \sigma^{-1}$ 分解为图 $G$ 上的边对换（transpositions）的乘积，且总数最小。

**下界**：

$$\text{OPT}(G, \pi) \geq \frac{1}{2} \sum_{v \in V} d_G(v, \pi(v))$$

即每个标记到目标位置的距离之和的一半（因为每次 SWAP 同时移动两个标记）。

**NP-困难性**：Token Swapping 问题在一般图上是 NP-困难的 [Miltzow et al., ESA 2016]。在树上可以精确求解（多项式时间）。

**Source**: [derivations/qubit_routing_theory.md] | **[Miltzow et al., ESA 2016; Alon et al., SICOMP 1994; Bonnet et al., SWAT 2018]**

---

### F13.5: Circuit Depth Under Routing Constraints

设原始线路深度为 $D_{\text{orig}}$，路由引入的额外深度取决于 SWAP 的并行化程度。设路由过程中插入的 SWAP 层数为 $L_{\text{swap}}$，每个 SWAP 需要 3 层 CNOT。则编译后线路的总深度：

$$D_{\text{total}} = D_{\text{orig}} + 3 \cdot L_{\text{swap}} + D_{\text{scheduling}}$$

其中 $D_{\text{scheduling}}$ 是由于门调度（gate scheduling）引起的额外延迟。

**深度下界**（对于线性连接架构 $P_n$）：

$$D_{\text{total}} \geq \Omega(n \cdot D_{\text{orig}})$$

在最坏情况下，线性链上的线路深度会被放大 $\Theta(n)$ 倍 [Cheung et al., QIC 2007]。

对于二维网格 $\sqrt{n} \times \sqrt{n}$：

$$D_{\text{total}} \geq \Omega(\sqrt{n} \cdot D_{\text{orig}})$$

**Source**: [derivations/circuit_compilation_complexity.md] | **[Cheung et al., QIC 2007; Beals et al., Proc. Royal Soc. A, 2013]**

---

## 硬件约束

### F13.6: Connectivity Graph / Coupling Map

量子处理器的**耦合图**（coupling graph / connectivity graph）$G_{\text{hw}} = (V, E)$ 定义为：

- $V = \{v_0, v_1, \ldots, v_{N-1}\}$：物理量子比特集合
- $E \subseteq V \times V$：可执行双量子比特门的量子比特对

常见拓扑结构及其图论性质：

| 拓扑 | 图 | 直径 | 平均距离 | 度 |
|------|------|------|---------|------|
| 线性链 | $P_n$ | $n-1$ | $\frac{n+1}{3}$ | 1--2 |
| 环 | $C_n$ | $\lfloor n/2 \rfloor$ | $\sim n/4$ | 2 |
| 二维网格 | $\sqrt{n}\times\sqrt{n}$ | $2(\sqrt{n}-1)$ | $\sim \frac{2\sqrt{n}}{3}$ | 2--4 |
| 重六角 (Heavy-hex) | IBM | $O(\sqrt{n})$ | $O(\sqrt{n})$ | 2--3 |
| 全连通 | $K_n$ | 1 | 1 | $n-1$ |

**耦合图的谱间隙**（spectral gap）$\lambda_2(G)$（Laplacian 第二小特征值）衡量图的"连通质量"。$\lambda_2$ 越大，路由效率越高：

$$\lambda_2(G) \leq \frac{n \cdot \delta_{\min}}{n - 1}$$

其中 $\delta_{\min}$ 是图的最小度。

**Source**: [derivations/qubit_routing_theory.md] | **[IBM Quantum hardware specs; Brierley, 2015; Siraichi et al., CGO 2018]**

---

## 启发式算法

### F13.7: SABRE Heuristic Cost Function

SABRE (SWAP-based Bidirectional heuristic search) 算法 [Li et al., ASPLOS 2019] 使用以下代价函数评估候选 SWAP 操作。

设**前沿层**（front layer）$F$ 为当前可执行但不满足邻接约束的门集合。对于候选 SWAP$(u, v)$，记执行该 SWAP 后的新映射为 $\pi'$。SABRE 代价函数：

$$H_{\text{basic}}(\text{SWAP}) = \frac{1}{|F|} \sum_{\text{gate}(q_i, q_j) \in F} d_G(\pi'(q_i), \pi'(q_j))$$

扩展版本（考虑后续层）：

$$H_{\text{SABRE}}(\text{SWAP}) = \frac{1}{|F|} \sum_{\text{gate} \in F} d_G(\pi'(q_i), \pi'(q_j)) + W \cdot \frac{1}{|E|} \sum_{\text{gate} \in E} d_G(\pi'(q_i), \pi'(q_j))$$

其中 $E$ 是**扩展集**（extended set），即前沿层之后的下一批待执行门，$W$ 是权重参数（通常 $W = 0.5$）。$d_G$ 是耦合图上的最短路径距离。

SABRE 的**双向搜索**策略：先从前向遍历得到映射，然后反向遍历优化，交替进行直到收敛。

**Source**: [derivations/routing_algorithms.md] | **[Li et al., ASPLOS 2019, Section 3]**

---

### F13.8: Initial Mapping as Subgraph Isomorphism

**初始映射问题**可形式化为**子图同构**（subgraph isomorphism）问题。

定义线路的**交互图**（interaction graph）$G_C = (Q, E_C)$，其中：

$$E_C = \{(q_i, q_j) : \exists \text{ a two-qubit gate on } q_i, q_j \text{ in circuit } C\}$$

**最优初始映射**要求找到一个单射 $\pi: Q \to V$ 使得 $G_C$ 同构于 $G_{\text{hw}}$ 的一个子图：

$$\forall (q_i, q_j) \in E_C: \; (\pi(q_i), \pi(q_j)) \in E_{\text{hw}}$$

这是经典的**子图同构问题**，已知是 NP-完全的 [Cook, 1971]。

**实际放松**：在大多数情况下，完美的子图同构映射不存在（$G_C$ 的边数多于 $G_{\text{hw}}$ 中任何同大小子图），因此实际目标是**最小化不满足的边数**或**最小化总路由距离**：

$$\pi^* = \arg\min_{\pi} \sum_{(q_i, q_j) \in E_C} d_G(\pi(q_i), \pi(q_j))$$

**Source**: [derivations/routing_algorithms.md] | **[Siraichi et al., CGO 2018; Zulehner et al., DATE 2018]**

---

### F13.9: Gate Scheduling Constraints

线路中的门调度需满足以下约束。设 $t(g)$ 为门 $g$ 的执行时间步。

**依赖约束**（data dependency）：如果门 $g_2$ 作用的量子比特之一是门 $g_1$ 的输出，则：

$$t(g_2) \geq t(g_1) + \text{duration}(g_1)$$

**资源约束**（resource constraint）：同一物理量子比特在同一时刻只能执行一个门：

$$\forall v \in V, \forall t: \; |\{g : v \in \text{qubits}(g), \; t(g) \leq t < t(g) + \text{duration}(g)\}| \leq 1$$

**串扰约束**（crosstalk constraint）[Murali et al., MICRO 2020]：某些同时执行的门对会产生串扰错误：

$$\text{if } \text{crosstalk}(g_1, g_2) > \epsilon_{\text{threshold}}: \quad |t(g_1) - t(g_2)| \geq \max(\text{duration}(g_1), \text{duration}(g_2))$$

门调度问题可建模为**带资源约束的作业调度**（job-shop scheduling），也是 NP-困难问题。

**Source**: [derivations/circuit_compilation_complexity.md] | **[Murali et al., MICRO 2020; Niu & Todri-Sanial, DATE 2020]**

---

### F13.10: Routing as Permutation Group Problem

量子比特路由可以从**置换群**（permutation group）的角度理解。

$n$ 个量子比特的映射是对称群 $S_n$ 中的一个元素 $\pi \in S_n$。每个 SWAP$(i,j)$ 对应一个对换（transposition）$(i \; j) \in S_n$。路由过程是将初始映射 $\pi_0$ 变换为目标映射 $\pi_{\text{target}}$ 的过程：

$$\pi_{\text{target}} = \tau_k \cdot \tau_{k-1} \cdots \tau_2 \cdot \tau_1 \cdot \pi_0$$

其中 $\tau_i = (u_i \; v_i)$ 是第 $i$ 步执行的 SWAP 对应的对换，且必须满足 $(u_i, v_i) \in E$（耦合图上的边）。

**Cayley 图**观点：以 $S_n$ 为顶点集，以耦合图 $G$ 的边集对应的对换为生成元集，构造 Cayley 图 $\text{Cay}(S_n, T_G)$。路由问题等价于在此 Cayley 图上寻找从 $\pi_0$ 到 $\pi_{\text{target}}$ 的最短路径。

对于**完全图** $K_n$，$T_G$ 包含所有对换，任意排列最多需要 $n-1$ 步：

$$\text{diam}(\text{Cay}(S_n, T_{K_n})) = n - 1$$

对于**路径图** $P_n$（线性链），直径为 $\binom{n}{2}$（冒泡排序的最坏情况）：

$$\text{diam}(\text{Cay}(S_n, T_{P_n})) = \binom{n}{2}$$

**Source**: [derivations/qubit_routing_theory.md] | **[Banerjee et al., IEEE QCE 2020; Alon et al., SICOMP 1994]**

---

## Cross-References

- **F4.x**: 量子纠错码与稳定子形式体系 → [04_quantum_error_correction/key_formulas.md]
- **F1.x**: 线性代数、置换矩阵、图的邻接矩阵 → [01_linear_algebra/key_formulas.md]
- **F7.x**: 图论基础、图同构、最短路径 → [07_graph_theory/key_formulas.md]
- **F10.x**: 组合优化、NP-困难性、近似算法 → [10_optimization/key_formulas.md]
