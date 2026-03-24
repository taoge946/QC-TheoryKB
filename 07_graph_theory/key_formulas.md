# Key Formulas: Graph Theory

> **Tags**: `graph-theory`, `spectral`, `laplacian`, `fourier`, `isomorphism`, `random-walk`, `tanner-graph`, `qec`

本文件汇集图论中 15 个核心公式，涵盖代数图论、谱图论、图算法、图同构和纠错码相关结构。每个公式标注与 GNN/QEC 的关联。

---

### F7.1: Adjacency Matrix (邻接矩阵)

$$A_{ij} = \begin{cases} 1 & \text{if } (i,j) \in E \\ 0 & \text{otherwise} \end{cases}$$

> 图的基本矩阵表示，无向图时对称，$A^k_{ij}$ 给出长度为 $k$ 的路径数，是 GNN 邻居聚合的核心输入。

**Source**: [Wu et al. GNN Survey, §2] — `derivations/spectral_graph_theory.md`

---

### F7.2: Degree Matrix (度矩阵)

$$D = \mathrm{diag}(d_1, d_2, \ldots, d_n), \quad d_i = \sum_{j=1}^{n} A_{ij}$$

> 对角矩阵记录各节点度数，$\mathrm{tr}(D) = 2|E|$（无向图），是构造 Laplacian 的基本组件。

**Source**: [Wu et al. GNN Survey, §2] — `derivations/spectral_graph_theory.md`

---

### F7.3: Graph Laplacian (图拉普拉斯矩阵)

$$L = D - A, \quad L_{\mathrm{sym}} = I - D^{-1/2} A D^{-1/2}, \quad L_{\mathrm{rw}} = I - D^{-1} A$$

> Laplacian 实对称半正定，满足 $x^T L x = \frac{1}{2}\sum_{(i,j)\in E}(x_i - x_j)^2 \geq 0$，零特征值重数等于连通分量数，是谱方法 GNN 的数学基础。

**Source**: [Wu et al. GNN Survey, §4.1] — `derivations/spectral_graph_theory.md`

---

### F7.4: Spectral Decomposition & Graph Fourier Transform (谱分解与图傅里叶变换)

$$L_{\mathrm{sym}} = U \Lambda U^T, \quad \hat{x} = U^T x \;\text{(正变换)}, \quad x = U \hat{x} \;\text{(逆变换)}$$

> 图信号的频域表示，特征向量 $U$ 构成图傅里叶基，所有谱方法 ConvGNN 的出发点。

**Source**: [Wu et al. GNN Survey, §4.1] — `derivations/spectral_graph_theory.md`

---

### F7.5: Spectral Graph Convolution (谱图卷积)

$$x *_G g_\theta = U \, g_\theta(\Lambda) \, U^T x$$

> 在频域定义图卷积，$g_\theta(\Lambda)$ 是可学习滤波器，但有 $n$ 个参数且需 $O(n^3)$ 特征分解，不可扩展。

**Source**: [Wu et al. GNN Survey, §4.1] — `derivations/spectral_graph_theory.md`

---

### F7.6: Chebyshev Polynomial Approximation (切比雪夫多项式近似)

$$x *_G g_\theta = \sum_{k=0}^{K} \theta_k \, T_k(\tilde{L}_{\mathrm{sym}}) \, x, \quad T_k(x) = 2x\,T_{k-1}(x) - T_{k-2}(x)$$

> 用 $K$ 阶切比雪夫多项式近似谱滤波器，复杂度 $O(K|E|)$，仅需 $K+1$ 个参数，是 ChebNet 的核心。

**Source**: [Defferrard et al. (ChebNet), 2016; Wu et al. GNN Survey, §4.1] — `derivations/spectral_graph_theory.md`

---

### F7.7: GCN First-Order Approximation (GCN 一阶近似)

$$H^{(l+1)} = \sigma\!\left(\tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2} H^{(l)} W^{(l)}\right)$$

> 取 $K=1$ 的切比雪夫近似并加自环 $\tilde{A}=A+I$，桥接谱方法与空间方法，是 Kipf & Welling (2017) 经典 GCN。

**Source**: [Kipf & Welling, 2017; Wu et al. GNN Survey, §4.1] — `derivations/spectral_graph_theory.md`

---

### F7.8: Cheeger Inequality (Cheeger 不等式)

$$\frac{\lambda_2}{2} \leq h(G) \leq \sqrt{2 \lambda_2}, \quad h(G) = \min_{S \subset V, |S| \leq n/2} \frac{|\partial S|}{\min(|S|, |V \setminus S|)}$$

> $\lambda_2$（Fiedler 值/代数连通度）刻画图的连通强度，$\lambda_2 > 0$ 等价于图连通。

**Source**: [Chung, Spectral Graph Theory, 1997] — `derivations/spectral_graph_theory.md`

---

### F7.9: Weisfeiler-Leman Test & GIN Theorem (WL 测试与 GIN 定理)

$$c_v^{(l+1)} = \mathrm{HASH}\!\left(c_v^{(l)}, \{\!\{ c_u^{(l)} : u \in \mathcal{N}(v) \}\!\}\right)$$

> 1-WL 颜色迭代判定图同构上界，GIN 定理证明任何 MPNN 区分能力 $\leq$ 1-WL，GIN（sum + MLP）达到该上界。

**Source**: [Xu et al. (GIN), 2019; Wu et al. GNN Survey, §4.2] — `derivations/wl_test_expressiveness.md`

---

### F7.10: Random Walk on Graphs (图上随机游走)

$$P = D^{-1} A, \quad p^{(t)} = P^t p^{(0)}, \quad \pi_i = \frac{d_i}{2|E|}$$

> 转移概率矩阵 $P$ 定义随机游走，连通非二部图有唯一稳态分布 $\pi$，与 Laplacian 关系为 $L_{\mathrm{rw}}=I-P$。

**Source**: [Wu et al. GNN Survey, §4.2] — `derivations/graph_algorithms.md`

---

### F7.11: Graph Cuts & Max-Flow/Min-Cut (图割与最大流最小割)

$$\mathrm{NCut}(S, \bar{S}) = \frac{\mathrm{cut}(S, \bar{S})}{\mathrm{vol}(S)} + \frac{\mathrm{cut}(S, \bar{S})}{\mathrm{vol}(\bar{S})}$$

> 归一化割的谱松弛解由 $L_{\mathrm{sym}}$ 第二小特征向量给出（谱聚类），最大流-最小割定理保证网络最大流等于最小割。

**Source**: [Ford-Fulkerson; Wu et al. GNN Survey] — `derivations/graph_algorithms.md`

---

### F7.12: Expander Graphs (扩展图)

$$\max(|\lambda_2|, |\lambda_n|) \leq \lambda, \quad \lambda_2 \geq 2\sqrt{d-1} - o(1) \;\text{(Alon-Boppana)}$$

> $d$-正则 $(n,d,\lambda)$-expander 的谱间隙条件，Ramanujan 图达到最优 $\lambda \leq 2\sqrt{d-1}$，与 quantum LDPC 码的距离增长密切相关。

**Source**: [Sipser & Spielman, 1996] — `derivations/graph_algorithms.md`

---

### F7.13: Tanner Graphs (Tanner 图)

$$G = (V_{\mathrm{bit}} \cup V_{\mathrm{check}}, E), \quad (i,j) \in E \Leftrightarrow H_{ji} = 1$$

> 线性码校验矩阵 $H$ 对应的二部图，量子 CSS 码由满足 $H_X H_Z^T=0$ 的两个 Tanner 图定义，LDPC 码的稀疏性保证高效 BP 解码。

**Source**: [Tanner, 1981] — `derivations/tanner_graphs.md`

---

### F7.14: Bipartite Matching & Hall's Theorem (二部图匹配与 Hall 定理)

$$\text{Hall: } |N(S)| \geq |S| \;\forall S\subseteq U \iff \text{存在 } U\text{-完美匹配}$$

> Hall 定理给出二部图完美匹配的充要条件，Konig 定理保证最大匹配数等于最小顶点覆盖数，MWPM 是表面码最常用解码算法。

**Source**: [Edmonds, 1965] — `derivations/tanner_graphs.md`

---

### F7.15: Graph Coloring & Chromatic Number (图着色与色数)

$$\omega(G) \leq \chi(G) \leq \Delta(G) + 1$$

> 色数夹在最大团 $\omega(G)$ 与最大度 $\Delta(G)+1$ 之间，Brooks 定理进一步改进上界，图着色是 GNN-based CO solver 的重要测试用例。

**Source**: [Brooks' Theorem] — `derivations/graph_algorithms.md`

---

## Cross-Reference

| 公式 | 关联领域 | 详细推导 |
|------|---------|---------|
| F7.3-F7.7 (Laplacian, Fourier, ChebNet, GCN) | GNN | `derivations/spectral_graph_theory.md`, `11_ml_theory/derivations/gnn_message_passing.md` |
| F7.8 (Cheeger) | 谱图论 | `derivations/spectral_graph_theory.md` |
| F7.9 (WL test) | GNN 表达力 | `derivations/wl_test_expressiveness.md` |
| F7.10-F7.11 (Random walk, Graph cuts) | 图算法 | `derivations/graph_algorithms.md` |
| F7.13-F7.14 (Tanner, Matching) | QEC | `derivations/tanner_graphs.md` |
| F7.15 (Coloring) | 组合优化 | `derivations/graph_algorithms.md` |

---

## References

1. Wu, Z., Pan, S., Chen, F., Long, G., Zhang, C., & Yu, P.S. (2020). A Comprehensive Survey on Graph Neural Networks. IEEE TNNLS.
2. Chung, F.R.K. (1997). Spectral Graph Theory. AMS.
3. Kipf, T.N. & Welling, M. (2017). Semi-Supervised Classification with Graph Convolutional Networks. ICLR.
4. Defferrard, M., Bresson, X., & Vandergheynst, P. (2016). Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering. NeurIPS.
5. Xu, K., Hu, W., Leskovec, J., & Jegelka, S. (2019). How Powerful are Graph Neural Networks? ICLR.
6. Sipser, M. & Spielman, D.A. (1996). Expander codes. IEEE Trans. Inform. Theory.
7. Tanner, R.M. (1981). A recursive approach to low complexity codes. IEEE Trans. Inform. Theory.
8. Edmonds, J. (1965). Paths, trees, and flowers. Canadian Journal of Mathematics.
