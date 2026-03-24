# Syndrome Measurement Scheduling

> **Tags**: `syndrome-extraction`, `stabilizer-code`, `surface-code`, `scheduling`, `graph-coloring`, `hook-error`, `commutativity`
>
> 稳定子码 syndrome 提取线路的调度理论：冲突图构造、对易性约束、并行化策略、以及 hook error 回避。面向 asyndrome/DiffusionSynth 等 syndrome 调度项目。
>
> **References**: **[Dennis et al., 2002]** (topological quantum memory); **[Tomita et al., 2014]** (low-distance surface codes); **[Beverland et al., 2021]** (color codes overhead); **[Fowler et al., 2012]** (surface codes review); **[Gottesman, 1997]** (stabilizer formalism); **[Delfosse & Nickerson, 2021]** (almost-linear decoder)

---

## 1. Syndrome Extraction Circuit Structure（Syndrome 提取线路结构）

### Definition 1.1 (Syndrome Extraction) **[Gottesman, 1997, §3; Fowler et al., 2012, §II]**

给定 $[[n, k, d]]$ 稳定子码，其稳定子群 $\mathcal{S}$ 由 $n-k$ 个独立生成元 $\{s_1, s_2, \ldots, s_{n-k}\}$ 生成。**Syndrome 提取**是测量所有稳定子生成元 $s_i$ 的过程，每个测量结果（$\pm 1$）构成 syndrome 向量：

$$\mathbf{s} = (s_1, s_2, \ldots, s_{n-k}) \in \{0, 1\}^{n-k}$$

其中 $s_i = 0$ 表示测量结果 $+1$（无错误），$s_i = 1$ 表示 $-1$（检测到错误）。

### Definition 1.2 (Stabilizer Measurement Circuit) **[Fowler et al., 2012, §II.B]**

测量一个 weight-$w$ 的稳定子 $s = P_1 \otimes P_2 \otimes \cdots \otimes P_w$（$P_i \in \{X, Y, Z\}$）需要：

1. **一个辅助比特（ancilla）** $|0\rangle$ 用于间接测量
2. **$w$ 个 entangling gates**（CNOT 或 CZ）将数据比特的信息转移到辅助比特
3. **一次单比特测量**（测量辅助比特）

**Weight-4 X-stabilizer 测量线路**:

```
|0⟩_anc ---H---●---●---●---●---H---M
               |   |   |   |
|ψ⟩_d1 -------X   |   |   |
|ψ⟩_d2 -----------X   |   |
|ψ⟩_d3 ---------------X   |
|ψ⟩_d4 -------------------X
```

**Weight-4 Z-stabilizer 测量线路**:

```
|0⟩_anc ---●---●---●---●---M
           |   |   |   |
|ψ⟩_d1 ---X   |   |   |
|ψ⟩_d2 -------X   |   |
|ψ⟩_d3 -----------X   |
|ψ⟩_d4 ---------------X
```

每个 CNOT 门在辅助比特和一个数据比特之间操作。$w$ 个 CNOT 是顺序执行的（在单个稳定子内部不能并行化，因为它们共享同一个辅助比特）。

---

## 2. Measurement Scheduling as Graph Coloring（测量调度作为图着色问题）

### Definition 2.1 (Conflict Graph for Syndrome Scheduling) **[Tomita et al., 2014, §III]**

构造 syndrome 调度的冲突图 $G_S = (V_S, E_S)$：

**Vertex-level conflict (稳定子级冲突)**:
$$V_S = \{s_1, \ldots, s_{n-k}\}$$
$$(s_i, s_j) \in E_S \iff \mathrm{supp}(s_i) \cap \mathrm{supp}(s_j) \neq \emptyset$$

即两个稳定子共享至少一个数据比特时产生冲突。

**Gate-level conflict (门级冲突)**:
更精细地，可以在 CNOT 门级别定义冲突。设 $g_i^{(k)}$ 是稳定子 $s_i$ 的第 $k$ 个 CNOT 门：

$$(g_i^{(k)}, g_j^{(l)}) \in E \iff \mathrm{supp}(g_i^{(k)}) \cap \mathrm{supp}(g_j^{(l)}) \neq \emptyset$$

### Theorem 2.2 (Minimum Rounds Lower Bound)

最少的 syndrome 提取轮次（其中每轮中并行执行的稳定子测量互不冲突）满足：

$$\text{rounds}_{\min} \geq \chi(G_S)$$

对于表面码，$G_S$ 是平面图（plaquettes 和 stars 在格子上的冲突关系），由四色定理保证 $\chi(G_S) \leq 4$。

### Example 2.3 (Surface Code Conflict Structure) **[Dennis et al., 2002, §6; Fowler et al., 2012, §II]**

对于距离 $d$ 的表面码（rotated layout）：

- **$X$-稳定子**定义在面（plaquettes）上，每个涉及 4 个数据比特
- **$Z$-稳定子**定义在顶点（stars）上，每个涉及 4 个数据比特
- 相邻的同类型稳定子（如两个相邻 $X$-plaquettes）共享 2 个数据比特
- 不同类型的相邻稳定子（一个 $X$-plaquette 和一个 $Z$-star）共享 1 或 2 个数据比特

**冲突图性质**：
- 同类型稳定子的冲突图是格子的对偶图（也是格子），$\chi = 2$（二部图，棋盘着色）
- 加上跨类型冲突后，$\chi \leq 4$

---

## 3. Commutativity Constraints（对易性约束）

### Theorem 3.1 (Stabilizer Commutativity) **[Gottesman, 1997, §3.2]**

稳定子群 $\mathcal{S}$ 的所有元素两两对易：

$$\forall s_i, s_j \in \mathcal{S}: \quad [s_i, s_j] = 0$$

这是稳定子码的定义性质。然而，**对易性不意味着可以同时测量**，因为测量线路涉及辅助比特和 CNOT 门，这些额外操作引入了新的约束。

### Proposition 3.2 (When Can Two Stabilizers Be Measured Simultaneously?)

两个稳定子 $s_i$ 和 $s_j$ 可以在同一时间步开始测量的**充分条件**：

$$\mathrm{supp}(s_i) \cap \mathrm{supp}(s_j) = \emptyset$$

即它们的支撑（所涉及的数据比特集合）完全不相交。

若 $\mathrm{supp}(s_i) \cap \mathrm{supp}(s_j) \neq \emptyset$，两个稳定子的 CNOT 门序列可能在某些时间步作用于同一个数据比特。此时，虽然 $s_i$ 和 $s_j$ 作为 Pauli 算符对易，但它们的测量线路中的**个别 CNOT 门可能冲突**。

### Definition 3.3 (CNOT Ordering within a Stabilizer)

对于一个 weight-$w$ 稳定子 $s = P_{q_1} \otimes P_{q_2} \otimes \cdots \otimes P_{q_w}$，CNOT 门的执行顺序定义了一个排列 $\pi: \{1,\ldots,w\} \to \{q_1,\ldots,q_w\}$，其中 $\pi(t)$ 是第 $t$ 步与辅助比特做 CNOT 的数据比特。

**标准顺序**（对表面码）：通常采用固定的 CNOT 顺序使得不同稳定子在同一时间步不会竞争同一数据比特。

### Proposition 3.4 (Fine-grained Parallelism)

即使两个稳定子共享数据比特，通过精心安排各自 CNOT 的时间步，可以实现**交错并行**（interleaved parallelism）：

$$\exists \; \text{orderings } \pi_i, \pi_j \text{ such that } \pi_i(t) \neq \pi_j(t) \;\;\forall t$$

即在每个时间步中，两个稳定子的 CNOT 门作用于不同的数据比特。这允许在不增加测量轮次的情况下并行化更多的稳定子测量。

---

## 4. Parallelism Constraints from Qubit Sharing（量子比特共享的并行约束）

### Definition 4.1 (Qubit Occupation Constraint)

在任意时间步 $t$，每个量子比特（数据比特或辅助比特）只能参与至多一个门操作：

$$\forall q, \forall t: \quad |\{g : q \in \mathrm{supp}(g), \; g \text{ scheduled at time } t\}| \leq 1$$

### Theorem 4.2 (Surface Code Syndrome Depth) **[Fowler et al., 2012, §II.C; Tomita et al., 2014]**

对于旋转表面码（rotated surface code），存在 CNOT 排序使得完整的 syndrome 提取（所有 $X$ 和 $Z$ 稳定子）可以在 **$d_{\text{syn}} = 4$ 个时间步** 内完成所有 CNOT 门，加上 2 个步骤用于辅助比特的初始化和测量，总深度 $\leq 6$。

**标准 CNOT 顺序（"Z-shape" / "N-shape"）**:

对于每个 weight-4 稳定子，4 个 CNOT 门在 4 个时间步中依次执行，采用如下空间顺序（以 plaquette 内的 4 个数据比特为例）：

```
Step 1: NW    Step 2: NE    Step 3: SW    Step 4: SE
```

或其旋转/反射变体。关键是**所有同类型稳定子使用相同的顺序**，加上**不同类型的稳定子使用互补的顺序**，确保在每个时间步中不发生冲突。

### Proof Sketch (4-step schedule existence)

**Claim**: 对旋转表面码，存在一种 CNOT 顺序使得在每个时间步 $t \in \{1,2,3,4\}$ 中，所有 CNOT 门两两不冲突（不共享量子比特）。

考虑旋转表面码中数据比特和稳定子的几何排列。每个数据比特恰好被 2 个 $X$-稳定子和 2 个 $Z$-稳定子共享。采用如下策略：

1. 为所有 $X$-稳定子固定 CNOT 顺序为 $(\text{NW}, \text{NE}, \text{SW}, \text{SE})$
2. 为所有 $Z$-稳定子固定 CNOT 顺序为 $(\text{NW}, \text{SW}, \text{NE}, \text{SE})$ —— 与 $X$ 的顺序不同

通过逐时间步检查，可以验证在每个时间步 $t$，每个数据比特只被一个 CNOT 使用。这本质上是因为相邻同类型稳定子在棋盘着色下交错排列，而不同类型稳定子采用互补顺序避免了冲突。$\square$

---

## 5. Connection to Surface Code Syndrome Extraction Ordering（与表面码 Syndrome 提取顺序的联系）

### Definition 5.1 (Syndrome Extraction Round)

一个**完整的 syndrome 提取轮次**包括：

1. 辅助比特初始化（$|0\rangle$ 或 $|+\rangle$）
2. $d_{\text{syn}}$ 个 CNOT 时间步
3. 辅助比特测量（$Z$ 基或 $X$ 基）

总深度为 $d_{\text{syn}} + 2$。对于容错计算，每轮 syndrome 提取需要重复 $O(d)$ 次以抑制测量错误。

### Definition 5.2 (Repeated Syndrome Measurement) **[Dennis et al., 2002, §4]**

为了可靠地提取 syndrome，需要在 $T = O(d)$ 轮中重复测量。这产生了一个 $(d-1) \times (d-1) \times T$ 的三维 syndrome 数据块，其中前两个维度是空间（格子上的稳定子位置），第三个维度是时间。

解码器在此三维 syndrome 体上工作，同时纠正空间错误和时间错误（测量错误）。

### Remark 5.3 (Scheduling Affects Decoder Performance)

CNOT 的调度顺序直接影响错误传播模式：
- 不同的 CNOT 顺序导致不同的**错误传播图**
- 错误传播图决定了哪些错误组合会产生相同的 syndrome（影响 decoder 的有效距离）
- 次优的调度可能导致**hook errors**（见下节），降低码的有效距离

---

## 6. Hook Error Avoidance Through Scheduling（通过调度避免 Hook Error）

### Definition 6.1 (Hook Error) **[Dennis et al., 2002, §6.1; Fowler et al., 2012, §V]**

**Hook error**（钩形错误）是指在 syndrome 提取过程中，辅助比特上的单比特错误通过后续 CNOT 门传播到多个数据比特上，产生一个有效 weight $> 1$ 的数据比特错误。

具体地，若辅助比特在第 $k$ 个 CNOT 之后（第 $k+1$ 个 CNOT 之前）发生 $X$ 错误，此错误会通过第 $k+1, k+2, \ldots, w$ 个 CNOT 传播到 $w-k$ 个数据比特上（对 $X$-stabilizer 测量线路）。

**Worst case**: 辅助比特在第 1 个 CNOT 之后发生错误，传播到 $w-1$ 个数据比特。对 weight-4 稳定子，一个单比特错误可以变成 weight-3 的数据错误。

### Theorem 6.2 (Hook Error Weight Bound)

对 weight-$w$ 稳定子的 syndrome 测量线路，辅助比特上的单比特错误导致的 hook error 的最大 weight 为：

$$w_{\text{hook}} \leq w - 1$$

**Proof.** 辅助比特错误最早在第 1 个 CNOT 之后发生（第 0 个时间步的错误等价于准备错误，不传播到更多比特）。此后还有 $w - 1$ 个 CNOT 可以传播此错误，每个 CNOT 最多影响一个额外的数据比特。$\square$

### Definition 6.3 (Hook Error Direction)

hook error 影响的数据比特集合取决于 CNOT 的**执行顺序**。对于表面码中的 weight-4 稳定子，hook error 的"方向"（哪些数据比特被影响）由 CNOT 顺序决定：

- **"好的"方向**：hook error 沿稳定子的一条边传播，不增加有效码距的退化
- **"坏的"方向**：hook error 横跨稳定子，可能与其他错误组合形成低 weight 的逻辑错误

### Theorem 6.4 (Scheduling to Minimize Hook Error Impact) **[Tomita et al., 2014, §III; Beverland et al., 2021]**

通过选择合适的 CNOT 顺序，可以使所有 hook error 沿着不降低有效码距的方向传播。对于旋转表面码，**标准的 Z-shape 顺序**保证：

**(a)** 所有 weight-2 hook error 与现有的 weight-2 错误等价（同一 syndrome），不产生新的退化

**(b)** 有效码距保持为 $d$（不因 hook error 降低）

**原理**: 选择 CNOT 顺序使得 hook error 影响的数据比特集合沿着格子的行或列排列（而非对角线），这样 hook error 不会"跨越"逻辑算子的路径，保持了码距。

### Remark 6.5 (Hook Errors in Non-Surface Codes)

对于其他拓扑码（如 color code, hyperbolic code）或 qLDPC 码：
- Hook error 问题更严重，因为稳定子权重可能更高（$w > 4$）
- CNOT 顺序的选择空间更大（$w!$ 种排列 per stabilizer）
- 找到最优的 hook error 避免调度是一个组合优化问题
- **这正是 asyndrome/DiffusionSynth 等项目要解决的核心问题之一**

---

## 7. Formal Optimization Problem（形式化优化问题）

### Problem 7.1 (Syndrome Scheduling Optimization)

**Input**:
- 稳定子码的校验矩阵 $H$（或稳定子生成元集合 $\{s_1, \ldots, s_{n-k}\}$）
- 硬件连通性图 $G_{\text{hw}}$

**Output**:
- 每个稳定子的 CNOT 顺序 $\pi_i$
- 全局时间步分配 $\sigma: \text{CNOTs} \to \{1, \ldots, T\}$

**Objectives**（可能冲突的多目标）:
1. **最小化深度** $T$
2. **最小化 hook error 影响**（最大化有效码距）
3. **满足硬件连通性约束**

**Constraints**:
1. 每个量子比特每个时间步至多参与一个 CNOT
2. CNOT 必须遵守硬件连通性（或通过 SWAP 门实现）
3. 每个稳定子内部的 CNOT 顺序是该稳定子涉及比特的一个排列

### Theorem 7.2 (Complexity)

Syndrome scheduling optimization 在一般稳定子码上是 NP-hard 的。

**Proof sketch.** 将图着色问题归约到 syndrome 调度的深度最小化子问题：给定图 $G$，构造稳定子码使得冲突图恰好为 $G$，则深度最小化等价于 $G$ 的色数计算。$\square$

---

## 8. Algorithmic Approaches（算法方法综述）

### 8.1 Heuristic Methods（启发式方法）

| 方法 | 复杂度 | 适用场景 |
|------|--------|---------|
| 贪心着色 | $O(n \cdot w_{\max})$ | 快速获得可行调度 |
| DSATUR（饱和度优先） | $O(n^2)$ | 利用度信息的改进贪心 |
| 模拟退火 / 遗传算法 | 可控 | 大规模实例 |

### 8.2 ML-based Methods（基于机器学习的方法）

- **DiffusionSynth**: 用扩散模型生成 syndrome 测量调度
- **asyndrome**: 基于 GNN + RL 的自动 syndrome 调度优化
- 这些方法可以探索比启发式更大的解空间，并学习到好的调度结构

### 8.3 Exact Methods（精确方法）

| 方法 | 适用范围 |
|------|---------|
| Integer Programming (IP) | 小规模实例 |
| Constraint Satisfaction (CSP) | 中等规模，丰富约束 |
| Branch and Bound | 有良好上下界时 |

---

## Summary of Key Results

| 结果 | ID | 内容 |
|------|-----|------|
| Syndrome 冲突图 | F14.6 | $(s_i, s_j) \in E \iff \mathrm{supp}(s_i) \cap \mathrm{supp}(s_j) \neq \emptyset$ |
| 并行门约束 | F14.7 | 不相交支撑 $\implies$ 可并行 |
| Surface code depth = 4 | — | 标准 CNOT 顺序实现 4-step syndrome |
| Hook error weight | — | $w_{\text{hook}} \leq w - 1$ |
| 调度优化 NP-hard | — | 一般稳定子码的最优调度 |

---

## References

1. Gottesman, D. (1997). Stabilizer Codes and Quantum Error Correction. PhD thesis, Caltech. arXiv:quant-ph/9705052.
2. Dennis, E., Kitaev, A., Landahl, A., & Preskill, J. (2002). Topological quantum memory. J. Math. Phys., 43(9), 4452-4505.
3. Fowler, A.G., Mariantoni, M., Martinis, J.M., & Cleland, A.N. (2012). Surface codes: Towards practical large-scale quantum computation. PRA, 86(3), 032324.
4. Tomita, Y., Svore, K.M., & Bravyi, S. (2014). Low-distance surface codes under realistic quantum noise. PRA, 90(6), 062320.
5. Beverland, M.E., Kubica, A., & Svore, K.M. (2021). Cost of universality. PRX Quantum, 2(2), 020341.
6. Delfosse, N. & Nickerson, N.H. (2021). Almost-linear time decoding algorithm for topological codes. Quantum, 5, 595.
7. Aaronson, S. & Gottesman, D. (2004). Improved simulation of stabilizer circuits. PRA, 70(5), 052328.
8. Nielsen, M.A. & Chuang, I.L. (2010). Quantum Computation and Quantum Information. 10th Anniversary Edition. Cambridge University Press.
