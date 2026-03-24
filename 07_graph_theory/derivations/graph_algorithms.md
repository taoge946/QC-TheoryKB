# Graph Algorithms: Complexity and Correctness

> **Tags**: `graph-algorithms`, `bfs`, `dfs`, `dijkstra`, `mst`, `matching`, `coloring`, `mwpm`, `qec`
>
> **References**: Standard graph algorithms; GNN context from **[Wu et al. 2021, §2 (Background)]**

## Statement

推导经典图算法的复杂度和正确性：BFS/DFS、最短路径（Dijkstra）、最小生成树（Kruskal/Prim）、最大匹配（Edmonds' Blossom）、图着色界。这些算法在 QEC 解码（MWPM）和组合优化（GNN-based solver） **[Wu et al. 2021, §7 (Applications)]** 中至关重要。

## Prerequisites

- 图论基础：$G = (V, E)$，邻接表/矩阵表示
- 数据结构：堆、并查集
- 基本复杂度分析

---

## Part 1: Graph Traversal — BFS & DFS

### 1.1 BFS (Breadth-First Search)

**算法**：从源节点 $s$ 出发，按层遍历（使用队列）。

```
BFS(G, s):
    for each v in V: dist[v] = inf
    dist[s] = 0, enqueue(s)
    while queue not empty:
        u = dequeue()
        for each v in N(u):
            if dist[v] == inf:
                dist[v] = dist[u] + 1
                enqueue(v)
```

**复杂度**：$O(|V| + |E|)$

**证明**：每个节点最多入队一次（dist 从 inf 变为有限值后不再改变），每条边最多被检查两次（无向图）。

**正确性**：BFS 计算的 dist[v] 等于无权图中 $s$ 到 $v$ 的最短距离。

**证明**（归纳法，对距离 $d$）：
- $d = 0$：$\mathrm{dist}[s] = 0$ ✓
- 假设距离 $\leq d-1$ 的节点都正确计算。对距离为 $d$ 的节点 $v$，存在邻居 $u$ 使得 $\delta(s, u) = d-1$。由归纳假设 $\mathrm{dist}[u] = d-1$，且 $u$ 在 $v$ 之前被处理。当处理 $u$ 时，$v$ 会被发现并设置 $\mathrm{dist}[v] = d$。$\square$

### 1.2 DFS (Depth-First Search)

**算法**：从源节点出发，尽可能深入探索（使用栈/递归）。

```
DFS(G, s):
    mark s as visited
    for each v in N(s):
        if v not visited:
            DFS(G, v)
```

**复杂度**：$O(|V| + |E|)$（同 BFS）

**DFS 的关键性质**：
- 产生 DFS 树，将边分类为 tree edge, back edge, forward edge, cross edge
- **定理**：无向图中 DFS 只产生 tree edge 和 back edge（无 cross edge）
- **应用**：拓扑排序（DAG）、强连通分量（Tarjan/Kosaraju）、割点和桥检测

---

## Part 2: Shortest Path — Dijkstra's Algorithm

### 2.1 问题

给定加权图 $G = (V, E, w)$（$w: E \to \mathbb{R}_{\geq 0}$），求从源 $s$ 到所有节点的最短路径。

### 2.2 算法

```
Dijkstra(G, s):
    for each v in V: dist[v] = inf
    dist[s] = 0
    Q = min-priority-queue(V, key=dist)
    while Q not empty:
        u = extract-min(Q)
        for each v in N(u):
            if dist[u] + w(u,v) < dist[v]:
                dist[v] = dist[u] + w(u,v)
                decrease-key(Q, v, dist[v])
```

### 2.3 复杂度分析

| 数据结构 | extract-min | decrease-key | 总复杂度 |
|---------|------------|-------------|---------|
| 数组 | $O(|V|)$ | $O(1)$ | $O(|V|^2)$ |
| 二叉堆 | $O(\log|V|)$ | $O(\log|V|)$ | $O((|V|+|E|)\log|V|)$ |
| 斐波那契堆 | $O(\log|V|)$ amortized | $O(1)$ amortized | $O(|V|\log|V| + |E|)$ |

**稀疏图**（$|E| = O(|V|)$）：斐波那契堆给出 $O(|V|\log|V|)$。
**稠密图**（$|E| = O(|V|^2)$）：数组实现 $O(|V|^2)$ 最优。

### 2.4 正确性证明

**定理**：当 Dijkstra 从 $Q$ 中提取节点 $u$ 时，$\mathrm{dist}[u] = \delta(s, u)$（真实最短距离）。

**证明**（反证法）：

假设 $u$ 是第一个被提取时 $\mathrm{dist}[u] > \delta(s, u)$ 的节点。

考虑 $s \to u$ 的真实最短路径 $P$。令 $y$ 为 $P$ 上第一个尚在 $Q$ 中的节点，$x$ 为 $y$ 的前驱（$x$ 已被提取）。

- 由于 $x$ 在 $u$ 之前被提取，且 $x$ 不是反例（$u$ 是第一个），$\mathrm{dist}[x] = \delta(s, x)$
- 当 $x$ 被提取时，边 $(x, y)$ 被松弛，所以 $\mathrm{dist}[y] \leq \delta(s, y)$
- 由于 $y$ 在 $s \to u$ 的路径上，$\delta(s, y) \leq \delta(s, u)$
- 由非负权：$\mathrm{dist}[y] \leq \delta(s, y) \leq \delta(s, u) < \mathrm{dist}[u]$
- 但 $u$ 在 $y$ 之前被提取 $\Rightarrow$ $\mathrm{dist}[u] \leq \mathrm{dist}[y]$，矛盾！$\square$

**注意**：Dijkstra 要求 $w \geq 0$。负权边需使用 Bellman-Ford ($O(|V| \cdot |E|)$)。

### 2.5 与 QEC/GNN 的关联

- **[Wu et al. GNN Survey, §4.2]**：PGC-DGCNN 使用最短路径距离定义邻接矩阵 $S^{(j)}$，时间复杂度为 $O(n^3)$（所有对最短路径）
- QEC 中 MWPM 解码器需要在 syndrome 图上计算节点间距离

---

## Part 3: Minimum Spanning Tree

### 3.1 问题

给定连通加权无向图 $G = (V, E, w)$，找权最小的生成树。

### 3.2 Cut Property（割性质）

**定理**：对于图的任意割 $(S, V \setminus S)$，穿越该割的最小权边一定在某个 MST 中。

**证明**：设 $e = (u, v)$ 是穿越割的最小权边，$T$ 是一个不包含 $e$ 的 MST。将 $e$ 加入 $T$ 会形成环，环中必有另一条穿越割的边 $e'$。由于 $w(e) \leq w(e')$，用 $e$ 替换 $e'$ 得到权 $\leq w(T)$ 的生成树。$\square$

### 3.3 Kruskal 算法

按权排序所有边，依次加入不形成环的边（使用并查集）。

**复杂度**：$O(|E| \log |E|)$（排序主导）

### 3.4 Prim 算法

类似 Dijkstra，从一个节点开始，每次加入连接已选集合和未选集合的最小权边。

**复杂度**：与 Dijkstra 相同，$O(|V| \log |V| + |E|)$（斐波那契堆）。

---

## Part 4: Maximum Matching & Edmonds' Blossom Algorithm

### 4.1 定义

**匹配** $M \subseteq E$：没有两条边共享端点。

**最大匹配**：$|M|$ 最大的匹配。

**完美匹配**：$|M| = |V|/2$（覆盖所有节点）。

### 4.2 增广路径定理 (Berge's Theorem)

**定理 (Berge, 1957)**：匹配 $M$ 是最大匹配 $\Leftrightarrow$ 不存在关于 $M$ 的增广路径。

**增广路径**：一条从非匹配节点到非匹配节点的路径，且路径上的边交替属于 $E \setminus M$ 和 $M$。

**证明必要性**（$\Leftarrow$）：若存在增广路径 $P$，则 $M \oplus P$（对称差）是更大的匹配。

**证明充分性**（$\Rightarrow$）：若 $M$ 不是最大匹配，设 $M^*$ 是更大的匹配。考虑 $M \oplus M^*$，其每个连通分量是路径或偶环。由于 $|M^*| > |M|$，必存在 $M^*$ 边多于 $M$ 边的路径分量，这就是增广路径。$\square$

### 4.3 二部图匹配

**Hopcroft-Karp 算法**：在二部图中找最大匹配。

**复杂度**：$O(|E| \sqrt{|V|})$

**思路**：每轮用 BFS 找最短增广路径集合，再用 DFS 同时沿多条增广。

### 4.4 一般图匹配：Edmonds' Blossom 算法

**难点**：一般图中可能存在奇环（"花"），使增广路径搜索复杂化。

**Blossom（花）**：长度为 $2k+1$ 的交替环，其中 $k$ 条边在匹配中。

**核心思想**：
1. 用 BFS 搜索增广路径
2. 遇到奇环（blossom）时，将整个花缩为一个"超级节点"
3. 在缩后的图中继续搜索
4. 找到增广路径后，"展开"花并沿路径增广

**复杂度**：
- 原始 Edmonds (1965)：$O(|V|^3)$
- Micali-Vazirani (1980)：$O(|E| \sqrt{|V|})$

### 4.5 最小权完美匹配 (MWPM)

**问题**：在加权图中找权最小的完美匹配。

**Blossom V 算法** (Kolmogorov, 2009)：基于 Edmonds 的原始对偶方法的高效实现。

**复杂度**：$O(|V|^3)$（理论），实际中对稀疏图远快于此。

### 4.6 MWPM 在 QEC 中的应用

**表面码解码**：
1. 测量 stabilizer，得到 syndrome（检测到错误的位置）
2. 在 syndrome 节点之间构建完全图，边权为物理距离（或对数似然比）
3. 求 MWPM，将 syndrome 配对
4. 沿配对路径纠正错误

**关键**：MWPM 解码的阈值接近最优（对独立噪声模型约 $10.3\%$），但复杂度为 $O(n^3)$（$n$ 为 syndrome 数），限制了实时解码。

**这正是 GNN/ML 解码器试图替代或辅助 MWPM 的动机**。

---

## Part 5: Graph Coloring Bounds

### 5.1 基本定义

**色数** $\chi(G)$：使相邻节点不同色的最小颜色数。

**团数** $\omega(G)$：最大完全子图的大小。

### 5.2 基本界

**下界**：$\chi(G) \geq \omega(G)$

**证明**：团中的 $\omega(G)$ 个节点两两相邻，必须用不同颜色。$\square$

**上界（贪心）**：$\chi(G) \leq \Delta(G) + 1$

**证明**：按任意顺序给节点着色。每个节点最多有 $\Delta(G)$ 个已着色邻居，因此 $\Delta(G) + 1$ 种颜色中至少有一种可用。$\square$

### 5.3 Brooks 定理

**定理 (Brooks, 1941)**：若 $G$ 连通，既不是完全图也不是奇环，则 $\chi(G) \leq \Delta(G)$。

### 5.4 与 QEC/GNN 的关联

- **图着色** 是 NP-hard 的组合优化问题，是 GNN-based CO solver 的常见 benchmark
- QEC 中的 syndrome 解码可以建模为约束满足问题，与图着色问题结构类似
- CO 问题（着色、最大割、TSP 等）的 GNN 求解器正在快速发展

---

## Summary Table

| 算法 | 问题 | 最佳复杂度 | QEC/GNN 关联 |
|------|------|-----------|-------------|
| BFS | 无权最短路 | $O(|V|+|E|)$ | 图遍历基础 |
| DFS | 图遍历/拓扑排序 | $O(|V|+|E|)$ | 连通性分析 |
| Dijkstra | 非负权最短路 | $O(|V|\log|V|+|E|)$ | PGC-DGCNN 距离矩阵 |
| Kruskal/Prim | MST | $O(|E|\log|E|)$ | 图稀疏化 |
| Edmonds' Blossom | 最大匹配 | $O(|E|\sqrt{|V|})$ | - |
| MWPM | 最小权完美匹配 | $O(|V|^3)$ | **QEC 表面码解码** |
| 贪心着色 | 图着色 | $O(|V|+|E|)$ | GNN-CO benchmark |

---

## References

1. Cormen, T.H., Leiserson, C.E., Rivest, R.L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.
2. Edmonds, J. (1965). Paths, trees, and flowers. Canadian Journal of Mathematics.
3. Kolmogorov, V. (2009). Blossom V: A new implementation of a minimum cost perfect matching algorithm. Mathematical Programming Computation.
4. Hopcroft, J.E. & Karp, R.M. (1973). An $n^{5/2}$ algorithm for maximum matchings in bipartite graphs. SIAM J. Comput.
5. Berge, C. (1957). Two theorems in graph theory. PNAS.
6. Wu, Z., Pan, S., Chen, F., Long, G., Zhang, C., & Yu, P.S. (2020). A Comprehensive Survey on Graph Neural Networks. IEEE TNNLS.
7. Dennis, E., Kitaev, A., Landahl, A., & Preskill, J. (2002). Topological quantum memory. J. Math. Phys.
8. Higgott, O. & Gidney, C. (2023). Sparse Blossom: correcting a million errors per core second. arXiv:2303.15933.
