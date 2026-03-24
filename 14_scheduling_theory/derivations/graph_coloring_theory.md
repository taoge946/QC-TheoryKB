# Graph Coloring Theory for Scheduling

> **Tags**: `graph-coloring`, `chromatic-number`, `Brooks-theorem`, `interval-graph`, `perfect-graph`, `circuit-depth`, `scheduling`
>
> 图着色理论及其与调度问题的等价关系。覆盖色数界、Brooks 定理证明、区间图的多项式可解性、以及量子线路深度优化中的着色应用。
>
> **References**: **[Diestel, *Graph Theory*, 2017, Ch.5]** (graph coloring); **[Golumbic, 1980]** (perfect graphs); **[Welsh & Powell, 1967]** (greedy coloring); **[Maslov et al., 2008]** (quantum circuit scheduling)

---

## 1. Chromatic Number: Definition and Basic Bounds（色数：定义与基本界）

### Definition 1.1 (Proper Coloring / 正常着色) **[Diestel, §5.1]**

图 $G = (V, E)$ 的一个**正常 $k$-着色**是映射 $c: V \to \{1, 2, \ldots, k\}$，满足

$$\forall (u,v) \in E: \quad c(u) \neq c(v)$$

图 $G$ 的**色数**（chromatic number）定义为使得 $G$ 可被正常着色的最小颜色数：

$$\chi(G) = \min\{k : G \text{ has a proper } k\text{-coloring}\}$$

### Theorem 1.2 (Basic Bounds) **[Diestel, §5.2]**

$$\omega(G) \leq \chi(G) \leq \Delta(G) + 1$$

其中 $\omega(G)$ 是最大团大小（clique number），$\Delta(G)$ 是最大度。

**Proof.**

**下界 $\chi(G) \geq \omega(G)$**：设 $K$ 是 $G$ 中大小为 $\omega(G)$ 的最大团。$K$ 中任意两个顶点相邻，因此在任何正常着色中需要 $\omega(G)$ 种不同颜色。整图的着色需要的颜色数不少于其子图所需的颜色数，所以 $\chi(G) \geq \omega(G)$。

**上界 $\chi(G) \leq \Delta(G) + 1$**：使用贪心着色。任取顶点的排列 $v_1, v_2, \ldots, v_n$，依次为每个顶点 $v_i$ 选择不与其已着色邻居冲突的最小颜色。由于 $v_i$ 最多有 $\Delta(G)$ 个邻居，因此最多有 $\Delta(G)$ 种颜色被禁用，颜色集 $\{1, \ldots, \Delta(G)+1\}$ 中总有可用颜色。$\square$

### Remark 1.3 (Gap between $\omega$ and $\chi$)

$\chi(G)$ 和 $\omega(G)$ 的差距可以任意大。Mycielski 构造给出了 $\omega(G) = 2$（无三角形）但 $\chi(G)$ 任意大的图。但在调度应用中，冲突图通常有特殊结构使差距可控。

---

## 2. Brooks' Theorem（Brooks 定理）

### Theorem 2.1 (Brooks' Theorem) **[Brooks, 1941; Diestel, Theorem 5.2.4]**

设 $G$ 是连通图。若 $G$ 既不是完全图 $K_n$ 也不是奇圈 $C_{2k+1}$，则

$$\chi(G) \leq \Delta(G)$$

**Proof sketch** (via BFS ordering). **[Diestel, §5.2]**

**Step 1 (选择根节点).** 取 $G$ 中任意顶点 $u$，进行 BFS 得到 BFS 树 $T$。取距 $u$ 最远的顶点 $v$ 作为着色的起始点。

**Step 2 (构造着色顺序).** 取 $v$ 的两个邻居 $v_1, v_2$（因为 $G$ 不是完全图且连通，$\Delta(G) \geq 3$ 的情况下可以找到不相邻的两个邻居）。构造顶点排列使 $v_1, v_2$ 排在最前面、$v$ 排在最后。

**Step 3 (贪心着色).** 给 $v_1$ 和 $v_2$ 赋相同的颜色（它们不相邻）。然后按排列顺序贪心着色。关键观察：除 $v$ 外，每个顶点在被着色时至少有一个邻居尚未着色（因为排列是 BFS 逆序），因此最多有 $\Delta(G) - 1$ 种颜色被禁用，$\Delta(G)$ 种颜色足够。

**Step 4 (处理 $v$).** $v$ 是最后着色的。$v$ 有 $\Delta(G)$ 个邻居（最坏情况），但 $v_1$ 和 $v_2$ 使用了同一颜色，所以至多 $\Delta(G) - 1$ 种颜色被 $v$ 的邻居占用，$\Delta(G)$ 种颜色中至少有一种可用。

因此 $\Delta(G)$ 种颜色足以完成正常着色。$\square$

**例外情况**：
- $K_n$：$\chi(K_n) = n = \Delta(K_n) + 1$
- $C_{2k+1}$（奇圈）：$\chi = 3 = \Delta + 1 = 2 + 1$

### Corollary 2.2 (Scheduling Implication)

在量子线路调度中，若冲突图 $G$ 满足：(1) 不是完全图（即并非所有门两两冲突），(2) 不是奇圈，则调度深度严格小于 $\Delta(G) + 1$，即至少可以比"最繁忙量子比特参与的门数加一"少一层。

---

## 3. Greedy Coloring（贪心着色）

### Algorithm 3.1 (Greedy Coloring) **[Welsh & Powell, 1967]**

1. 选择顶点排列 $v_1, v_2, \ldots, v_n$
2. 对 $i = 1, 2, \ldots, n$：将 $v_i$ 着色为不与其已着色邻居冲突的最小正整数

### Theorem 3.2 (Greedy Upper Bound)

贪心着色使用的颜色数满足：

$$\chi_{\text{greedy}} \leq \max_{i=1,\ldots,n} \min\{d_{\text{back}}(v_i) + 1, \; i\}$$

其中 $d_{\text{back}}(v_i) = |\{v_j : j < i, (v_i, v_j) \in E\}|$ 是 $v_i$ 在排列中的"回溯度"（已着色邻居数）。

**特别地**，若顶点按度降序排列（Welsh-Powell ordering），贪心着色满足 $\chi_{\text{greedy}} \leq \Delta(G) + 1$。

### Theorem 3.3 (Degeneracy Bound)

图 $G$ 的**退化度**（degeneracy）$\delta^*(G) = \max_{H \subseteq G} \delta(H)$（所有子图的最小度的最大值）。存在顶点排列使贪心着色使用至多 $\delta^*(G) + 1$ 种颜色：

$$\chi(G) \leq \delta^*(G) + 1 \leq \Delta(G) + 1$$

**Proof.** 按退化序排列：反复删除度最小的顶点，逆序即为退化序。在此排列中，每个顶点 $v_i$ 至多有 $\delta^*(G)$ 个已着色邻居。$\square$

---

## 4. Interval Graphs and Perfect Graphs（区间图与完美图）

### Definition 4.1 (Interval Graph)

图 $G$ 是**区间图**（interval graph）如果存在实数轴上的闭区间集合 $\{I_v : v \in V\}$，使得

$$(u, v) \in E \iff I_u \cap I_v \neq \emptyset$$

### Theorem 4.2 (Interval Graphs are Perfect) **[Golumbic, 1980, Ch.4]**

区间图是完美图的一个子类。对区间图 $G$：

$$\chi(G) = \omega(G)$$

**Proof.**

显然 $\chi(G) \geq \omega(G)$（定理 1.2）。需证 $\chi(G) \leq \omega(G)$。

考虑贪心着色：将区间按左端点排序 $l_1 \leq l_2 \leq \cdots \leq l_n$。按此顺序为每个区间分配最小可用颜色。

当着色区间 $I_i$ 时，与 $I_i$ 冲突的已着色区间是那些满足 $l_j < l_i$ 且 $r_j \geq l_i$ 的区间 $I_j$（$r_j$ 是右端点）。这些区间两两相交（因为它们都包含点 $l_i$），构成一个团。因此与 $I_i$ 冲突的已着色区间数 $< \omega(G)$，颜色 $\{1, \ldots, \omega(G)\}$ 中至少有一种可用。

所以 $\omega(G)$ 种颜色足够，$\chi(G) \leq \omega(G)$。$\square$

### Algorithm 4.3 (Optimal Interval Graph Coloring)

1. 按左端点排序所有区间：$O(n \log n)$
2. 贪心分配最小可用颜色（用优先队列维护）：$O(n \log n)$

总复杂度 $O(n \log n)$，最优（颜色数 $= \omega(G)$）。

### Remark 4.4 (Scheduling Interpretation)

在调度中，若每个任务有固定的开始和结束时间（区间），则冲突图是区间图。此时最优调度（使用最少的并行资源/时间步）可在 $O(n \log n)$ 时间内找到。这在经典调度中对应于**区间着色问题**（interval coloring / interval scheduling maximization）。

---

## 5. Graph Coloring ↔ Scheduling Equivalence（图着色与调度的等价性）

### Theorem 5.1 (Coloring-Scheduling Equivalence) **[Welsh & Powell, 1967; de Werra, 1970]**

给定一组任务 $\{t_1, \ldots, t_n\}$ 和冲突关系（不能同时执行的任务对），构造冲突图 $G = (V, E)$：

$$V = \{t_1, \ldots, t_n\}, \quad (t_i, t_j) \in E \iff t_i \text{ and } t_j \text{ conflict}$$

则：

**(a)** 合法调度（无冲突）↔ $G$ 的正常着色，颜色 $=$ 时间步

**(b)** 最小时间步数 $=$ 色数 $\chi(G)$

**(c)** 每个颜色类（independent set）$=$ 一个时间步中并行执行的任务集

### Corollary 5.2 (NP-hardness of Optimal Scheduling)

由于图着色问题（$k$-coloring for $k \geq 3$）是 NP-complete [Karp, 1972]，基于冲突图的最优调度在一般情况下也是 NP-hard 的。

---

## 6. Application: Quantum Circuit Depth Optimization（应用：量子线路深度优化）

### Definition 6.1 (Conflict Graph of a Quantum Circuit) **[Maslov et al., 2008]**

给定量子线路 $\mathcal{C}$ 中的门集合 $\mathcal{G} = \{g_1, \ldots, g_n\}$，构造冲突图 $G_{\text{conflict}} = (V, E)$：

$$V = \mathcal{G}, \quad (g_i, g_j) \in E \iff \mathrm{supp}(g_i) \cap \mathrm{supp}(g_j) \neq \emptyset$$

其中 $\mathrm{supp}(g)$ 是门 $g$ 作用的量子比特集合。

### Theorem 6.2 (Depth = Chromatic Number, without precedence) **[Maslov et al., 2008]**

若线路中的门没有强制的先后顺序（即可以自由重排），则

$$\text{depth}(\mathcal{C}) = \chi(G_{\text{conflict}})$$

**Proof.** 一个深度为 $d$ 的线路安排等价于将门分配到 $d$ 个时间步，每个时间步中的门两两不冲突。这恰好是 $G_{\text{conflict}}$ 的一个正常 $d$-着色。因此最小深度等于色数。$\square$

### Remark 6.3 (With Precedence Constraints)

实际量子线路中通常有门的因果依赖（precedence constraints），此时需要解决的是**带拓扑排序约束的着色问题**：

$$\text{depth}(\mathcal{C}) = \chi_{\text{prec}}(G_{\text{conflict}}, \prec) \geq \chi(G_{\text{conflict}})$$

即在满足优先级约束的前提下的最小着色数。这比无约束着色更难，但在实践中（如表面码 syndrome 提取），线路结构通常使得 $\chi_{\text{prec}} = \chi$。

### Example 6.4 (Surface Code Syndrome Circuit)

考虑距离 $d$ 的表面码。每个 $X$-型稳定子和 $Z$-型稳定子需要 4 个 CNOT 门来测量（体内部的 weight-4 稳定子）。相邻稳定子共享数据比特，构成冲突。

对于标准的表面码 syndrome 提取线路：
- 冲突图的最大度 $\Delta \leq 6$（每个稳定子最多与 6 个相邻稳定子冲突）
- 通过精心安排 CNOT 顺序，可以实现 depth = 4（每轮 syndrome 提取）
- 这对应于在冲突图上找到一个 4-着色

---

## 7. Computational Complexity of Graph Coloring（图着色的计算复杂度）

### Theorem 7.1 (NP-completeness) **[Karp, 1972; Garey & Johnson, 1979]**

| 问题 | 复杂度 |
|------|--------|
| 2-coloring | $O(n + m)$（BFS/DFS 判二部图） |
| 3-coloring | NP-complete |
| $k$-coloring ($k \geq 3$) | NP-complete |
| Chromatic number $\chi(G)$ | NP-hard |
| Interval graph coloring | $O(n \log n)$ |
| Planar graph 4-coloring | Always possible (Four Color Theorem) |

### Theorem 7.2 (Inapproximability) **[Zuckerman, 2007]**

除非 P = NP，不存在多项式时间算法可以在 $n^{1-\varepsilon}$ 倍内近似一般图的色数（对任意 $\varepsilon > 0$）。

**意义**: 这说明对一般冲突图，最优调度深度在最坏情况下几乎不可近似。但量子线路的冲突图通常有特殊结构（如有界度、接近区间图等），使得实际问题远比最坏情况容易。

---

## Summary

| 结果 | ID | 内容 |
|------|-----|------|
| 基本色数界 | F14.3 | $\omega(G) \leq \chi(G) \leq \Delta(G) + 1$ |
| Brooks 定理 | F14.3 | 非完全图非奇圈: $\chi(G) \leq \Delta(G)$ |
| 区间图最优性 | F14.4 | $\chi(G) = \omega(G)$, $O(n\log n)$ 可解 |
| 着色-调度等价 | F14.2 | 颜色 = 时间步, 独立集 = 并行任务 |
| 线路深度 | F14.8 | $\text{depth} = \chi(G_{\text{conflict}})$ |

---

## References

1. Brooks, R.L. (1941). On colouring the nodes of a network. Math. Proc. Cambridge Phil. Soc., 37(2), 194-197.
2. Welsh, D.J.A. & Powell, M.B. (1967). An upper bound for the chromatic number of a graph and its application to timetabling problems. The Computer Journal, 10(1), 85-86.
3. de Werra, D. (1970). On some combinatorial problems arising in scheduling. Canadian Operational Research Society Journal, 8(3), 165-175.
4. Karp, R.M. (1972). Reducibility among combinatorial problems. In Complexity of Computer Computations, 85-103. Plenum.
5. Golumbic, M.C. (1980). Algorithmic Graph Theory and Perfect Graphs. Academic Press.
6. Diestel, R. (2017). Graph Theory. 5th ed. Springer. Chapter 5.
7. Garey, M.R. & Johnson, D.S. (1979). Computers and Intractability. W.H. Freeman.
8. Zuckerman, D. (2007). Linear degree extractors and the inapproximability of max clique and chromatic number. Theory of Computing, 3(1), 103-128.
9. Maslov, D., Falconer, S.M., & Mosca, M. (2008). Quantum circuit placement. IEEE TCAD, 27(4), 752-763.
10. Childs, A.M., Schoute, E., & Unsal, C.M. (2019). Circuit transformations for quantum architectures. TQC 2019.
