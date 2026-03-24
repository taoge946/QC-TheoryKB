# Key Formulas: Scheduling Theory

> **Tags**: `scheduling`, `graph-coloring`, `chromatic-number`, `circuit-depth`, `syndrome-measurement`, `precedence-constraints`, `interval-scheduling`, `NP-hard`

本文件汇集调度理论中 10 个核心公式，涵盖经典机器调度、图着色与调度的等价关系、量子线路调度和 syndrome 测量调度。每个公式标注与量子计算调度问题的关联。

---

### F14.1: Job Scheduling Problem $P \| C_{\max}$（并行机调度最大完工时间）

$$P \| C_{\max}: \quad \min \; C_{\max} = \min_{\sigma} \; \max_{j=1,\ldots,m} \; \sum_{i: \sigma(i)=j} p_i$$

> 将 $n$ 个独立作业（处理时间 $p_1, \ldots, p_n$）分配到 $m$ 台相同并行机上，最小化最大完工时间（makespan）。此问题是量子门并行调度的经典抽象：门是作业，量子比特是资源约束。当 $m \geq 3$ 时为强 NP-hard [Garey & Johnson, 1979]。

**Source**: [Graham et al., 1979, §4] — `derivations/scheduling_basics.md`

---

### F14.2: Graph Coloring as Scheduling（图着色作为调度）

$$\text{Scheduling} \leftrightarrow \text{Coloring}: \quad \sigma: V \to \{1, \ldots, k\} \;\text{ s.t. } (u,v) \in E \Rightarrow \sigma(u) \neq \sigma(v)$$

> 将相互冲突（不能同时执行）的任务建模为图的顶点，冲突关系为边，则调度问题等价于图着色问题。颜色数 $k$ 对应时间步数（电路深度）。这是量子线路调度和 syndrome 测量调度的核心建模手段。

**Source**: [Welsh & Powell, 1967] — `derivations/graph_coloring_theory.md`

---

### F14.3: Chromatic Number Bounds — Brooks' Theorem（色数界 — Brooks 定理）

$$\omega(G) \leq \chi(G) \leq \Delta(G) + 1$$

**Brooks' Theorem**: 若连通图 $G$ 既不是完全图也不是奇圈，则 $\chi(G) \leq \Delta(G)$。

> 色数 $\chi(G)$ 的下界为最大团 $\omega(G)$，上界为最大度加一。Brooks 定理将上界改进一步。在量子调度中，冲突图的最大度对应单个量子比特参与的最大门/测量数目，色数给出最优调度深度。

**Source**: [Brooks, 1941; Diestel, *Graph Theory*, Theorem 5.2.4] — `derivations/graph_coloring_theory.md`

---

### F14.4: Interval Scheduling / Interval Graph（区间调度 / 区间图）

$$G \text{ 是区间图 (interval graph)} \iff \chi(G) = \omega(G)$$

> 区间图是完美图的特例。若任务的冲突结构可以表示为实数轴上区间的相交关系，则最优着色（调度）可在多项式时间内通过贪心算法求解，时间步数恰好等于最大同时冲突数。区间图着色算法复杂度 $O(n \log n)$。

**Source**: [Golumbic, *Algorithmic Graph Theory and Perfect Graphs*, 1980, Ch.4] — `derivations/graph_coloring_theory.md`

---

### F14.5: List Scheduling Approximation Ratio（列表调度近似比）

$$\frac{C_{\max}^{\text{LS}}}{C_{\max}^{*}} \leq \frac{4}{3} - \frac{1}{3m}$$

> Graham 的列表调度算法（List Scheduling）：按任意顺序将作业分配到当前负载最小的机器上。对 $P \| C_{\max}$ 问题，此贪心策略的近似比为 $2 - 1/m$。若使用 LPT（Longest Processing Time First）规则预排序，近似比改进为 $4/3 - 1/(3m)$。

**Source**: [Graham, 1969, Theorem 1] — `derivations/scheduling_basics.md`

---

### F14.6: Syndrome Measurement Scheduling（Syndrome 测量调度）

$$\text{Construct conflict graph } G_S = (V_S, E_S): \quad (s_i, s_j) \in E_S \iff \mathrm{supp}(s_i) \cap \mathrm{supp}(s_j) \neq \emptyset$$

> 稳定子码中，syndrome 测量的调度问题：每个稳定子生成元 $s_i$ 需要一个辅助比特和一系列 CNOT 门来测量。两个稳定子 $s_i, s_j$ 若共享数据比特（$\mathrm{supp}(s_i) \cap \mathrm{supp}(s_j) \neq \emptyset$），则不能完全并行执行。冲突图 $G_S$ 的色数 $\chi(G_S)$ 给出最小测量轮次数的下界。

**Source**: [Tomita et al., 2014; Beverland et al., 2021] — `derivations/syndrome_scheduling.md`

---

### F14.7: Parallel Gate Scheduling — Commutativity Constraint（并行门调度 — 对易约束）

$$[U_i, U_j] = 0 \;\text{ and } \;\mathrm{supp}(U_i) \cap \mathrm{supp}(U_j) = \emptyset \implies U_i, U_j \text{ can be parallelized}$$

> 量子线路中两个门可以在同一时间步执行的充分条件：(1) 它们作用在不相交的量子比特上，或 (2) 它们对易且共享比特上的操作兼容。条件 (1) 是实际硬件调度的标准约束；条件 (2) 在理论分析中使用但硬件上一般仍要求不相交支撑。

**Source**: [Aaronson & Gottesman, 2004; Nielsen & Chuang, §4.5] — `derivations/syndrome_scheduling.md`

---

### F14.8: Circuit Depth = Chromatic Number of Dependency Graph（线路深度 = 依赖图色数）

$$\text{depth}(\mathcal{C}) = \chi(G_{\text{conflict}}(\mathcal{C}))$$

> 给定量子线路 $\mathcal{C}$ 中的门集合 $\{g_1, \ldots, g_n\}$，构造冲突图 $G_{\text{conflict}}$：两个门若共享量子比特则连边。线路的最小深度等于 $G_{\text{conflict}}$ 的色数。对于有拓扑约束（如最近邻连通性）的硬件，还需考虑 SWAP 门插入后的扩展冲突图。

**Source**: [Maslov et al., 2008; Childs et al., 2019] — `derivations/graph_coloring_theory.md`

---

### F14.9: Resource-Constrained Scheduling（资源约束调度）

$$P \mid \text{res} \mid C_{\max}: \quad \sum_{i \in S_t} r_{ik} \leq R_k, \;\; \forall k, \forall t$$

> 资源约束调度问题：每个作业 $i$ 在执行时消耗 $r_{ik}$ 单位的第 $k$ 种资源，系统中第 $k$ 种资源总量为 $R_k$。同一时间步执行的作业集 $S_t$ 的总资源消耗不能超过资源上限。量子线路调度中，"资源"可以是量子比特、辅助比特、经典控制线等。

**Source**: [Brucker, *Scheduling Algorithms*, 2007, Ch.8] — `derivations/scheduling_basics.md`

---

### F14.10: Scheduling with Precedence Constraints（带优先级约束的调度）

$$P \mid \text{prec} \mid C_{\max}: \quad i \prec j \implies C_i \leq S_j$$

**Hu's Algorithm** (for unit tasks, $P \mid \text{tree, } p_j=1 \mid C_{\max}$): 按 level（到叶节点的最长路径长度）降序分配，最优解深度为 $\lceil n/m \rceil$ 或关键路径长度，取较大者。

**一般情况**: $P \mid \text{prec} \mid C_{\max}$ 是 NP-hard 的（即使 $m = 2$ 时也是 NP-hard [Ullman, 1975]）。

> 偏序关系 $\prec$ 表示任务间的依赖。量子线路中的因果依赖（如测量后经典反馈、T 门后纠错）构成优先级约束。关键路径（Critical Path）长度是 $C_{\max}$ 的下界。

**Source**: [Hu, 1961; Coffman & Graham, 1972; Ullman, 1975] — `derivations/scheduling_basics.md`

---

## Cross-Reference

| 公式 | 关联领域 | 详细推导 |
|------|---------|---------|
| F14.1, F14.5, F14.9, F14.10 (经典调度) | 组合优化 | `derivations/scheduling_basics.md`, `10_optimization/derivations/np_hard_problems.md` |
| F14.2, F14.3, F14.4, F14.8 (图着色) | 图论 | `derivations/graph_coloring_theory.md`, `07_graph_theory/key_formulas.md` (F7.15) |
| F14.6, F14.7 (syndrome/门调度) | QEC | `derivations/syndrome_scheduling.md`, `04_quantum_error_correction/derivations/surface_code_basics.md` |
| F14.8 (线路深度) | 量子编译 | `derivations/graph_coloring_theory.md` |

---

## References

1. Graham, R.L., Lawler, E.L., Lenstra, J.K., & Rinnooy Kan, A.H.G. (1979). Optimization and approximation in deterministic sequencing and scheduling: a survey. Annals of Discrete Mathematics, 5, 287-326.
2. Graham, R.L. (1969). Bounds on Multiprocessing Timing Anomalies. SIAM J. Appl. Math., 17(2), 416-429.
3. Brooks, R.L. (1941). On colouring the nodes of a network. Mathematical Proceedings of the Cambridge Philosophical Society, 37(2), 194-197.
4. Welsh, D.J.A. & Powell, M.B. (1967). An upper bound for the chromatic number of a graph and its application to timetabling problems. The Computer Journal, 10(1), 85-86.
5. Golumbic, M.C. (1980). Algorithmic Graph Theory and Perfect Graphs. Academic Press.
6. Garey, M.R. & Johnson, D.S. (1979). Computers and Intractability: A Guide to the Theory of NP-Completeness. W.H. Freeman.
7. Hu, T.C. (1961). Parallel sequencing and assembly line problems. Operations Research, 9(6), 841-848.
8. Coffman, E.G. & Graham, R.L. (1972). Optimal scheduling for two-processor systems. Acta Informatica, 1(3), 200-213.
9. Ullman, J.D. (1975). NP-complete scheduling problems. JCSS, 10(3), 384-393.
10. Brucker, P. (2007). Scheduling Algorithms. 5th ed. Springer.
11. Tomita, Y., Svore, K.M., & Bravyi, S. (2014). Low-distance surface codes under realistic quantum noise. PRA, 90(6), 062320.
12. Beverland, M.E., Kubica, A., & Svore, K.M. (2021). Cost of universality: A comparative study of the overhead of state distillation and code switching with color codes. PRX Quantum, 2(2), 020341.
13. Maslov, D., Falconer, S.M., & Mosca, M. (2008). Quantum circuit placement. IEEE TCAD, 27(4), 752-763.
14. Childs, A.M., Schoute, E., & Unsal, C.M. (2019). Circuit transformations for quantum architectures. TQC 2019.
15. Diestel, R. (2017). Graph Theory. 5th ed. Springer.
