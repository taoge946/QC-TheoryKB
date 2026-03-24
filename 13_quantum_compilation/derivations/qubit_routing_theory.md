# Qubit Routing Theory

> **Tags**: `qubit-routing`, `swap`, `token-swapping`, `np-hard`, `coupling-graph`, `compilation`

## Statement

量子比特路由（Qubit Routing）是量子线路编译中的核心子问题：给定一个逻辑量子线路和一个具有有限连通性的物理量子处理器，如何通过插入最少数量的 SWAP 门来使所有两量子比特门满足硬件邻接约束。这一问题在一般图上是 NP-困难的，等价于图上的 Token Swapping 问题。

## Prerequisites

- **图论基础**：图的连通性、最短路径、子图同构
- **群论基础**：对称群、对换（transposition）
- **计算复杂性**：NP-困难性、多项式归约
- **量子门基础**：CNOT 门、SWAP 门

---

## Derivation

### Step 1: Formal Problem Definition **[Siraichi et al., CGO 2018, Section 2; Li et al., ASPLOS 2019, Section 2]**

**输入**：
1. 量子线路 $C$：由一系列量子门 $g_1, g_2, \ldots, g_m$ 组成，作用于逻辑量子比特集合 $Q = \{q_0, \ldots, q_{n-1}\}$
2. 耦合图 $G_{\text{hw}} = (V, E)$：物理量子比特 $V$ 和可执行双量子比特门的连接 $E$

**映射**：单射函数 $\pi: Q \to V$，将逻辑量子比特映射到物理量子比特。

**邻接约束**：对于线路中的每个两量子比特门 $g = \text{CNOT}(q_i, q_j)$，必须满足：

$$(\pi(q_i), \pi(q_j)) \in E$$

**动态性**：映射 $\pi$ 在线路执行过程中会因 SWAP 操作而改变。设 $\pi_t$ 为第 $t$ 步时的映射，则：

$$\pi_{t+1} = \begin{cases} \pi_t \circ (u \; v) & \text{若在第 } t \text{ 步执行 SWAP}(u, v) \\ \pi_t & \text{否则} \end{cases}$$

其中 $(u \; v)$ 是交换物理量子比特 $u, v$ 的对换。

**优化目标**：找到初始映射 $\pi_0$ 和 SWAP 插入方案，使得：

$$\min \sum_{t} \mathbb{1}[\text{step } t \text{ is a SWAP}]$$

同时保证每个原始两量子比特门在执行时满足邻接约束。

### Step 2: SWAP Gate Properties **[Nielsen & Chuang, Section 4.3, p.184]**

SWAP 门交换两个量子比特的量子态。其作用为：

$$\text{SWAP}|a\rangle|b\rangle = |b\rangle|a\rangle, \quad \forall a, b \in \{0, 1\}$$

**SWAP 的 CNOT 分解**（标准分解）：

$$\text{SWAP}(q_1, q_2) = \text{CNOT}_{1 \to 2} \cdot \text{CNOT}_{2 \to 1} \cdot \text{CNOT}_{1 \to 2}$$

验证（计算基上）：

$$|00\rangle \xrightarrow{\text{CNOT}_{1\to2}} |00\rangle \xrightarrow{\text{CNOT}_{2\to1}} |00\rangle \xrightarrow{\text{CNOT}_{1\to2}} |00\rangle$$

$$|01\rangle \xrightarrow{\text{CNOT}_{1\to2}} |01\rangle \xrightarrow{\text{CNOT}_{2\to1}} |11\rangle \xrightarrow{\text{CNOT}_{1\to2}} |10\rangle$$

$$|10\rangle \xrightarrow{\text{CNOT}_{1\to2}} |11\rangle \xrightarrow{\text{CNOT}_{2\to1}} |11\rangle \xrightarrow{\text{CNOT}_{1\to2}} |01\rangle$$

$$|11\rangle \xrightarrow{\text{CNOT}_{1\to2}} |10\rangle \xrightarrow{\text{CNOT}_{2\to1}} |00\rangle \xrightarrow{\text{CNOT}_{1\to2}} |11\rangle$$

**SWAP 的门开销**：每个 SWAP 需要 3 个 CNOT 门。在 NISQ 时代，CNOT 的保真度通常为 99%--99.5%，因此一个 SWAP 的保真度约为 $(0.99)^3 \approx 0.97$，引入约 3% 的错误率。这使得最小化 SWAP 数目对于保持计算保真度至关重要。

**Bridge gate 替代方案** [Cowtan et al., TCAD 2019]：当两个量子比特距离为 2 时，可以用 **bridge CNOT** 代替 SWAP+CNOT+SWAP。Bridge gate 利用中间量子比特作为桥梁：

$$\text{Bridge-CNOT}(q_1, q_3; q_2) = \text{CNOT}_{1\to2} \cdot \text{CNOT}_{2\to3} \cdot \text{CNOT}_{1\to2} \cdot \text{CNOT}_{2\to3}$$

其中 $q_2$ 是 $q_1$ 和 $q_3$ 之间的中间量子比特。Bridge gate 只需 4 个 CNOT，而 SWAP+CNOT+SWAP 需要 7 个 CNOT。

### Step 3: Per-Pair SWAP Lower Bound **[Cowtan et al., TCAD 2019, Section III]**

**定理**：在耦合图 $G$ 上，若当前映射下逻辑量子比特 $q_i, q_j$ 分别位于物理位置 $u = \pi(q_i), v = \pi(q_j)$，则使它们相邻至少需要 $d_G(u, v) - 1$ 次 SWAP。

**证明**：

设 $d = d_G(u, v)$ 为 $u$ 到 $v$ 的最短路径距离。

**引理**：每次 SWAP$(a, b)$ 操作（其中 $(a,b) \in E$）至多将一个量子比特沿一条边移动一步。更精确地，若 SWAP 涉及携带 $q_i$ 的量子比特，则 $q_i$ 到 $q_j$ 的距离变化量 $\Delta d$ 满足 $|\Delta d| \leq 1$。

**证明引理**：设 SWAP$(a, b)$ 将 $q_i$ 从 $a$ 移到 $b$。由三角不等式：

$$d_G(b, \pi(q_j)) \geq d_G(a, \pi(q_j)) - d_G(a, b) = d_G(a, \pi(q_j)) - 1$$

因此距离至多减少 1。同理距离也可能增加 1 或不变。$\square$

**回到主定理**：初始距离为 $d$，目标距离为 $\leq 1$（相邻）。每次 SWAP 至多减少距离 1。因此至少需要 $d - 1$ 次 SWAP。$\square$

**注意**：此下界在路径图 $P_n$ 上对单对量子比特是紧的（可以精确达到）。但对于一般图和多对量子比特同时路由的情况，下界可能不紧。

### Step 4: Token Swapping and NP-Hardness **[Miltzow et al., ESA 2016; Alon et al., SICOMP 1994]**

量子比特路由与经典的 **Token Swapping** 问题密切相关。

**Token Swapping 问题**：
- **输入**：图 $G = (V, E)$，初始排列 $\sigma: V \to V$（每个顶点上有一个带标签的 token）
- **目标**：通过最少次数的边上 token 交换，将 $\sigma$ 变换为恒等排列 $\text{id}$
- **操作**：每步选择一条边 $(u, v) \in E$，交换 $u$ 和 $v$ 上的 token

**量子比特路由 $\leq_P$ Token Swapping**：给定一个路由问题实例（当前映射 $\pi_t$，需要在下一层执行的门集合），确定最优 SWAP 序列等价于一个 Token Swapping 实例。

**定理** [Miltzow et al., ESA 2016]：Token Swapping 在一般图上是 NP-困难的。

**证明思路**：通过从 **排列群上的 Sorting by Transpositions**（一般图上的推广）进行归约。在一般图上，允许的对换被限制为图的边，使得寻找最短对换序列变为 NP-困难问题。

具体归约链：

$$\text{Set Cover} \leq_P \text{Colored Token Swapping} \leq_P \text{Token Swapping on general graphs}$$

**特殊图上的结果**：

| 图类 | 复杂度 | 算法 | 近似比 |
|------|--------|------|--------|
| 树 | $O(n^2)$ | 精确（贪心） | 最优 |
| 路径 $P_n$ | $O(n \log n)$ | 冒泡排序 | 最优 |
| 环 $C_n$ | $O(n^2)$ | 旋转+冒泡 | 最优 |
| 完全图 $K_n$ | $O(n)$ | 任意对换 | 最优 |
| 星图 $S_n$ | $O(n)$ | 中心旋转 | 最优 |
| 一般图 | NP-hard | 近似算法 | 4 [Miltzow] |
| 二分图 | NP-hard | -- | -- |

**近似算法** [Miltzow et al., ESA 2016]：存在 4-近似算法——对每对 token，沿最短路径移动，总步数不超过 $2 \sum_v d_G(v, \sigma(v))$，而下界为 $\frac{1}{2}\sum_v d_G(v, \sigma(v))$。

### Step 5: Multi-Pair Routing and Vertex-Disjoint Paths **[Cowtan et al., TCAD 2019; Childs et al., QIC 2019]**

当多对量子比特需要同时路由时，问题更加复杂。

**Vertex-Disjoint Paths Problem**：给定图 $G$ 和 $k$ 对源-汇对 $(s_1, t_1), \ldots, (s_k, t_k)$，找到 $k$ 条顶点不相交的路径连接每对源-汇。

**与路由的关系**：若能找到顶点不相交的路径，则可以沿各路径并行执行 SWAP，总 SWAP 层数等于最长路径的长度。

**定理** [Robertson & Seymour, JCTB 1995]：对于固定 $k$，Vertex-Disjoint Paths 在一般图上可以在 $O(n^3)$ 时间内求解。但若 $k$ 是输入的一部分，则问题是 NP-完全的。

**并行路由的深度优化**：若 $k$ 对量子比特需要路由，且找到了 $k$ 条最短的顶点不相交路径，设最长路径长度为 $\ell_{\max}$，则并行路由的 SWAP 层数为：

$$L_{\text{swap}} = \ell_{\max} - 1$$

这比串行路由（$\sum_i (\ell_i - 1)$ 层）高效得多。

### Step 6: Routing on Specific Topologies

**线性链 $P_n$** [Cheung et al., QIC 2007]：

在 $n$ 量子比特的线性链上，最坏情况下一个 CNOT 门需要 $O(n)$ 个 SWAP。整个线路的路由开销为 $O(n)$ 倍的深度放大。

**最优排序**：线性链上的 Token Swapping 等价于冒泡排序，最坏情况需要 $\binom{n}{2}$ 次 SWAP。

**二维网格 $\sqrt{n} \times \sqrt{n}$**：

直径为 $2(\sqrt{n} - 1)$，任意一对量子比特最多需要 $2\sqrt{n} - 3$ 次 SWAP。Token Swapping 的最坏情况为 $O(n)$ 次 SWAP [Alon et al., SICOMP 1994]。

**Heavy-hex 拓扑**（IBM 量子处理器）[Chamberland et al., PRX 2020]：

IBM 的 heavy-hex 结构是六角形格子的变体，degree 为 2--3。其路由特性介于线性链和二维网格之间。优势在于减少了频率碰撞（frequency collision），但增加了平均路由距离。

### Step 7: Routing as Permutation Group Problem **[Banerjee et al., IEEE QCE 2020]**

从代数角度看，路由过程是在**受限生成元集**下的排列分解问题。

设 $S_n$ 是 $n$ 个元素的对称群。耦合图 $G = (V, E)$ 定义了一组**允许的对换**：

$$T_G = \{(u \; v) : (u, v) \in E\} \subset S_n$$

路由问题等价于：给定排列 $\pi \in S_n$，将其分解为 $T_G$ 中对换的乘积，且乘积长度最小：

$$\pi = \tau_k \cdot \tau_{k-1} \cdots \tau_1, \quad \tau_i \in T_G, \quad k \text{ minimal}$$

**Cayley 图** $\Gamma = \text{Cay}(S_n, T_G)$ 的顶点是 $S_n$ 中的所有排列，两个排列 $\sigma_1, \sigma_2$ 之间有边当且仅当 $\sigma_2 = \tau \cdot \sigma_1$ 对某个 $\tau \in T_G$。路由问题等价于在 $\Gamma$ 中求最短路径。

Cayley 图的直径 $\text{diam}(\Gamma)$ 给出了最坏情况下的路由步数：

- $G = K_n$：$\text{diam} = n - 1$
- $G = P_n$：$\text{diam} = \binom{n}{2}$
- $G = C_n$：$\text{diam} = \lfloor n^2/4 \rfloor$

---

## Summary

| 结果 | 公式/结论 | 来源 |
|------|----------|------|
| SWAP 分解 | $\text{SWAP} = 3$ CNOTs | Nielsen & Chuang |
| 单对下界 | $\text{SWAPs} \geq d_G(u,v) - 1$ | Cowtan et al. 2019 |
| Token Swapping 下界 | $\text{OPT} \geq \frac{1}{2}\sum_v d(v, \sigma(v))$ | Alon et al. 1994 |
| 一般图 NP-hard | Token Swapping on general graph | Miltzow et al. 2016 |
| 4-近似 | 贪心沿最短路径 | Miltzow et al. 2016 |
| 树上精确 | $O(n^2)$ 贪心 | Vaughan 2015 |

---

## References

1. Siraichi, M. Y., et al. "Qubit allocation." *CGO 2018*. -- 首次系统形式化量子比特映射问题
2. Li, G., Ding, Y., & Xie, Y. "Tackling the qubit mapping problem for NISQ-era quantum devices." *ASPLOS 2019*. -- SABRE 算法
3. Cowtan, A., et al. "On the qubit routing problem." *TCAD 2019*. -- Bridge gate, 路由理论分析
4. Miltzow, T., et al. "Approximation and hardness for Token Swapping." *ESA 2016*. -- NP-hard 证明, 4-近似
5. Alon, N., et al. "Routing permutations on graphs via matchings." *SICOMP 1994*. -- 经典排列路由理论
6. Childs, A. M., Schoute, E., & Unsal, C. M. "Circuit transformations for quantum architectures." *QIC 2019*. -- 路由距离理论
7. Cheung, D., Maslov, D., & Severini, S. "Translation techniques between quantum circuit architectures." *QIC 2007*. -- 线性链路由
8. Nielsen, M. A. & Chuang, I. L. *Quantum Computation and Quantum Information*. Cambridge, 2000.
9. Robertson, N. & Seymour, P. D. "Graph minors. XIII." *JCTB 1995*. -- Vertex-disjoint paths
10. Banerjee, S., et al. "Algebraic techniques for qubit routing." *IEEE QCE 2020*.
