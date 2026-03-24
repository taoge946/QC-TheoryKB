# Machine Scheduling: Taxonomy, Algorithms, and Approximation

> **Tags**: `scheduling`, `makespan`, `NP-hard`, `list-scheduling`, `LPT`, `precedence`, `Graham-notation`
>
> 机器调度问题的完整分类体系（Graham 三场记号）、经典算法及其近似比推导、优先级约束调度理论。
>
> **References**: **[Graham et al., 1979]** (scheduling survey); **[Garey & Johnson, 1979]** (NP-completeness); **[Brucker, 2007]** (scheduling algorithms textbook); **[Pinedo, 2016]** (scheduling theory and algorithms)

---

## 1. Graham's Three-Field Notation（Graham 三场记号）

### Definition 1.1 (Scheduling Taxonomy) **[Graham et al., 1979, §2]**

调度问题用三元组 $\alpha \mid \beta \mid \gamma$ 分类：

| 场 | 含义 | 典型取值 |
|----|------|---------|
| $\alpha$ (Machine environment) | 机器环境 | $1$（单机）, $P$（同型并行机）, $Q$（异速并行机）, $R$（不相关并行机）, $F$（流水车间）, $J$（作业车间） |
| $\beta$ (Job characteristics) | 作业约束 | $\text{prec}$（优先级约束）, $p_j=1$（单位处理时间）, $r_j$（释放时间）, $\text{pmtn}$（可抢占）, $\text{res}$（资源约束） |
| $\gamma$ (Objective function) | 优化目标 | $C_{\max}$（最大完工时间/makespan）, $\sum C_j$（总完工时间）, $\sum w_j T_j$（加权延迟） |

**关键实例**：

| 问题 | 含义 | 复杂度 |
|------|------|--------|
| $1 \| C_{\max}$ | 单机, 无约束, 最小化 makespan | $O(n)$（平凡） |
| $P \| C_{\max}$ | 同型并行机, 无约束, 最小化 makespan | NP-hard ($m \geq 3$) |
| $P2 \| C_{\max}$ | 2台同型并行机, 最小化 makespan | NP-hard (等价于 Partition) |
| $P \mid \text{prec} \mid C_{\max}$ | 同型并行机, 优先级约束 | NP-hard ($m \geq 2$) |
| $P \mid p_j=1, \text{prec} \mid C_{\max}$ | 单位时间, 优先级约束 | $m$ 固定时多项式 |

---

## 2. Makespan 问题 $P \| C_{\max}$

### Definition 2.1 ($P \| C_{\max}$)

给定 $n$ 个独立作业，处理时间为 $p_1, \ldots, p_n$，和 $m$ 台相同的并行机器。目标是找到分配 $\sigma: \{1,\ldots,n\} \to \{1,\ldots,m\}$，最小化 makespan：

$$C_{\max}(\sigma) = \max_{j=1,\ldots,m} \sum_{i: \sigma(i)=j} p_i$$

### Theorem 2.2 (NP-hardness) **[Garey & Johnson, 1979, Problem SS13]**

$P \| C_{\max}$ 当 $m \geq 3$ 时为强 NP-hard（strong NP-hard）。

**Proof sketch.** 当 $m = 2$ 时，$P2 \| C_{\max}$ 等价于 Partition 问题（弱 NP-hard，可由动态规划在伪多项式时间内求解）。当 $m = 3$ 时，归约自 3-Partition 问题，后者是强 NP-complete。$\square$

### Proposition 2.3 (Makespan Lower Bounds)

对任意可行调度，makespan 的下界为：

$$C_{\max}^* \geq \max\left\{ \frac{1}{m} \sum_{i=1}^n p_i, \; \max_{i=1,\ldots,n} p_i \right\}$$

**Proof.** 第一项：总工作量 $\sum p_i$ 在 $m$ 台机器上的平均负载是任何调度 makespan 的下界。第二项：最大作业必须在某台机器上完整执行。$\square$

---

## 3. List Scheduling（列表调度）

### Algorithm 3.1 (List Scheduling, LS) **[Graham, 1966]**

1. 给定作业列表 $L = (j_1, j_2, \ldots, j_n)$（任意顺序）
2. 按列表顺序依次取作业 $j_k$
3. 将 $j_k$ 分配到当前负载最小的机器上

### Theorem 3.2 (LS Approximation Ratio) **[Graham, 1966, Theorem 1]**

对 $P \| C_{\max}$ 问题，列表调度的近似比为：

$$\frac{C_{\max}^{\text{LS}}}{C_{\max}^*} \leq 2 - \frac{1}{m}$$

**Proof.**

设 $C_{\max}^{\text{LS}}$ 由机器 $j^*$ 上最后完成的作业 $i^*$ 决定。设 $S_{i^*}$ 为作业 $i^*$ 的开始时间。

在 $i^*$ 被分配到机器 $j^*$ 时，$j^*$ 是负载最小的机器，因此

$$S_{i^*} \leq \frac{1}{m} \sum_{i \neq i^*} p_i$$

（若所有其他机器的负载都 $\geq S_{i^*}$，则总负载 $\geq m \cdot S_{i^*}$，但总负载 $= \sum_{i \neq i^*} p_i$）

因此

$$C_{\max}^{\text{LS}} = S_{i^*} + p_{i^*} \leq \frac{1}{m} \sum_{i \neq i^*} p_i + p_{i^*} = \frac{1}{m} \sum_{i=1}^n p_i + \left(1 - \frac{1}{m}\right) p_{i^*}$$

利用下界 $C_{\max}^* \geq \frac{1}{m}\sum p_i$ 和 $C_{\max}^* \geq p_{i^*}$：

$$C_{\max}^{\text{LS}} \leq C_{\max}^* + \left(1 - \frac{1}{m}\right) C_{\max}^* = \left(2 - \frac{1}{m}\right) C_{\max}^*$$

$\square$

---

## 4. LPT Algorithm（最长处理时间优先）

### Algorithm 4.1 (Longest Processing Time First) **[Graham, 1969]**

1. 将作业按处理时间降序排列：$p_1 \geq p_2 \geq \cdots \geq p_n$
2. 按此顺序执行列表调度

### Theorem 4.2 (LPT Approximation Ratio) **[Graham, 1969, Theorem 1]**

$$\frac{C_{\max}^{\text{LPT}}}{C_{\max}^*} \leq \frac{4}{3} - \frac{1}{3m}$$

**Proof.**

设 $C_{\max}^{\text{LPT}}$ 由作业 $i^*$（最后完成的作业）确定。由 LPT 排序，$p_{i^*} \leq p_i$ 对所有 $i < i^*$。

**Case 1**: $i^* \leq m$。此时每个作业分配到不同机器，$C_{\max}^{\text{LPT}} = p_1 = C_{\max}^*$，比率为 1。

**Case 2**: $i^* > m$。此时至少有一台机器执行了两个或更多作业，且 $p_{i^*} \leq p_m$。

由于最优解中至少有一台机器执行了 $\lceil n/m \rceil \geq 2$ 个作业，且最短的两个作业处理时间之和 $\geq 2p_{i^*}$，所以

$$C_{\max}^* \geq 2p_{i^*} \implies p_{i^*} \leq \frac{C_{\max}^*}{2}$$

更精确地，由于 $n \geq m+1$ 且 LPT 排序，可以证明 $p_{i^*} \leq p_{\lfloor n/2 \rfloor + 1} \leq C_{\max}^*/3$（利用最优解中某台机器至少处理了 3 个长度 $\geq p_{i^*}$ 的作业的论证）。

代入列表调度的基本不等式：

$$C_{\max}^{\text{LPT}} \leq \frac{1}{m}\sum p_i + \left(1 - \frac{1}{m}\right) p_{i^*} \leq C_{\max}^* + \left(1 - \frac{1}{m}\right) \frac{C_{\max}^*}{3} = \left(\frac{4}{3} - \frac{1}{3m}\right) C_{\max}^*$$

$\square$

**紧性示例**: 取 $n = 2m+1$, $p_1 = \cdots = p_m = 2$, $p_{m+1} = \cdots = p_{2m+1} = 1$。LPT 产生 makespan 4（某机器得到一个 2 和两个 1），最优 makespan 3（每台机器得到一个 2 和 $\lfloor (m+1)/m \rfloor$ 个 1）。当 $m \to \infty$，比率 $\to 4/3$。

---

## 5. Scheduling with Precedence Constraints（带优先级约束的调度）

### Definition 5.1 (Precedence-Constrained Scheduling)

给定有向无环图（DAG）$G = (V, E)$，其中 $V = \{1, \ldots, n\}$ 是任务集合，$(i,j) \in E$ 表示任务 $i$ 必须在任务 $j$ 开始之前完成（$i \prec j$）。

$$P \mid \text{prec} \mid C_{\max}: \quad \text{minimize } C_{\max} \text{ subject to } C_i \leq S_j \;\forall (i,j) \in E$$

### Definition 5.2 (Critical Path)

DAG 中从源节点到汇节点的最长路径称为**关键路径（critical path）**，其长度为：

$$L_{\text{CP}} = \max_{\text{path } P} \sum_{i \in P} p_i$$

关键路径长度是 $C_{\max}^*$ 的下界，与 $\frac{1}{m}\sum p_i$ 一起构成两个基本下界：

$$C_{\max}^* \geq \max\left\{L_{\text{CP}}, \; \frac{1}{m}\sum_{i=1}^n p_i\right\}$$

### Theorem 5.3 (Hu's Algorithm) **[Hu, 1961]**

对于 $P \mid \text{tree}, p_j=1 \mid C_{\max}$（单位处理时间、树形优先级约束），Hu 的算法是最优的：

**Algorithm**: 定义每个任务的**level** = 从该任务到任何叶子的最长路径中的任务数。在每个时间步，优先调度 level 最大的就绪任务。

**Optimality**: 此算法产生的 makespan 为

$$C_{\max}^* = \max\left\{\lceil n/m \rceil, \; L_{\text{CP}}\right\}$$

### Theorem 5.4 (General Precedence is NP-hard) **[Ullman, 1975]**

$P \mid \text{prec}, p_j=1 \mid C_{\max}$ 当 $m$ 不固定时为 NP-hard。即使是单位处理时间和一般 DAG 约束，找到最优 makespan 也是 NP-hard 的。

**Proof sketch.** 归约自 Clique 问题。给定图 $G = (V, E)$，构造 DAG 使得 $G$ 有大小为 $k$ 的 clique 当且仅当调度问题的最优 makespan $\leq$ 某个阈值。$\square$

### Theorem 5.5 (Coffman-Graham Algorithm) **[Coffman & Graham, 1972]**

对 $P2 \mid \text{prec}, p_j=1 \mid C_{\max}$（2台机器、单位处理时间），Coffman-Graham 算法给出最优解。

对 $m$ 台机器，Coffman-Graham 算法的近似比为：

$$\frac{C_{\max}^{\text{CG}}}{C_{\max}^*} \leq 2 - \frac{2}{m}$$

---

## 6. NP-Hardness of General Scheduling（调度问题的 NP-hardness 全景）

### Theorem 6.1 (NP-hardness Summary) **[Garey & Johnson, 1979]**

| 问题 | 复杂度 | 归约来源 |
|------|--------|---------|
| $P2 \| C_{\max}$ | NP-hard (弱) | Partition |
| $P \| C_{\max}$ ($m \geq 3$) | NP-hard (强) | 3-Partition |
| $P \mid \text{prec} \mid C_{\max}$ | NP-hard | Clique |
| $1 \mid r_j \mid \sum C_j$ | NP-hard | - |
| $P \mid \text{prec}, p_j=1 \mid C_{\max}$ ($m$ 变量) | NP-hard | Clique |
| Graph Coloring | NP-hard | 3-SAT |

### Remark 6.2 (Relation to Quantum Circuit Scheduling)

量子线路的调度问题本质上是带资源约束和优先级约束的并行机调度：
- **Machine** = 时间步（time slot）
- **Job** = 量子门（gate）
- **Resource constraint** = 量子比特不能同时被两个门使用
- **Precedence constraint** = 线路中的因果依赖（门的输出作为后续门的输入）

因此量子线路深度优化问题在一般情况下也是 NP-hard 的，但对于特定结构（如 stabilizer 测量线路、表面码 syndrome 提取线路）可以利用问题的特殊结构设计高效算法。

---

## 7. Resource-Constrained Scheduling（资源约束调度）

### Definition 7.1 (RCPSP) **[Brucker, 2007, Ch.8]**

资源约束项目调度问题（Resource-Constrained Project Scheduling Problem, RCPSP）：

$$\min \; C_{\max} \quad \text{s.t.} \quad \sum_{i \in S_t} r_{ik} \leq R_k \;\; \forall k \in \{1,\ldots,K\}, \;\forall t$$

其中 $S_t$ 是时刻 $t$ 正在执行的作业集合，$r_{ik}$ 是作业 $i$ 对资源 $k$ 的需求量，$R_k$ 是资源 $k$ 的总容量。

**RCPSP 是 NP-hard 的**，因为 $P \| C_{\max}$ 是其特例（$K=1$, $r_{i1}=1$, $R_1=m$）。

### Remark 7.2 (Quantum Context)

在量子线路调度中的资源约束：
- **量子比特**：每个量子比特同一时刻只能参与一个门（$R_{\text{qubit}} = 1$ per qubit）
- **辅助比特**：syndrome 测量需要辅助比特，数量有限
- **经典控制信号**：控制电子学的通道数有限
- **连通性**：物理硬件的量子比特连接拓扑限制了可并行的门

---

## Summary of Key Results

| 公式/定理 | ID | 结论 |
|----------|-----|------|
| LS 近似比 | F14.5 | $C_{\max}^{\text{LS}}/C_{\max}^* \leq 2 - 1/m$ |
| LPT 近似比 | F14.5 | $C_{\max}^{\text{LPT}}/C_{\max}^* \leq 4/3 - 1/(3m)$ |
| Makespan 下界 | F14.1 | $C_{\max}^* \geq \max\{(\sum p_i)/m, \max p_i\}$ |
| 关键路径下界 | F14.10 | $C_{\max}^* \geq L_{\text{CP}}$ |
| Hu 算法 | F14.10 | Tree + unit time: 最优 |
| RCPSP | F14.9 | NP-hard (一般化的 $P\|C_{\max}$) |

---

## References

1. Graham, R.L. (1966). Bounds for certain multiprocessing anomalies. Bell System Technical Journal, 45(9), 1563-1581.
2. Graham, R.L. (1969). Bounds on Multiprocessing Timing Anomalies. SIAM J. Appl. Math., 17(2), 416-429.
3. Graham, R.L., Lawler, E.L., Lenstra, J.K., & Rinnooy Kan, A.H.G. (1979). Optimization and approximation in deterministic sequencing and scheduling: a survey. Annals of Discrete Mathematics, 5, 287-326.
4. Garey, M.R. & Johnson, D.S. (1979). Computers and Intractability. W.H. Freeman.
5. Hu, T.C. (1961). Parallel sequencing and assembly line problems. Operations Research, 9(6), 841-848.
6. Coffman, E.G. & Graham, R.L. (1972). Optimal scheduling for two-processor systems. Acta Informatica, 1(3), 200-213.
7. Ullman, J.D. (1975). NP-complete scheduling problems. JCSS, 10(3), 384-393.
8. Brucker, P. (2007). Scheduling Algorithms. 5th ed. Springer.
9. Pinedo, M.L. (2016). Scheduling: Theory, Algorithms, and Systems. 5th ed. Springer.
