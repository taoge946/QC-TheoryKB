# Weisfeiler-Leman Test and GNN Expressiveness

> **Tags**: `wl-test`, `graph-isomorphism`, `gin`, `expressiveness`, `mpnn`, `higher-order-gnn`
>
> **Primary Source**: Z. Wu et al., *A Comprehensive Survey on Graph Neural Networks*, IEEE TNNLS (2021) **[Wu et al. 2021, §4.4 (Theoretical Aspects)]**; K. Xu et al., *How Powerful are Graph Neural Networks?*, ICLR 2019 **[Xu et al. 2019]**

## Statement

推导 Weisfeiler-Leman 图同构测试的层次结构（1-WL, $k$-WL），证明 MPNN 的表达力上界为 1-WL **[Xu et al. 2019, Thm.3]**，以及 GIN 达到该上界的条件 **[Xu et al. 2019, Thm.3, Lem.5]**。讨论超越 1-WL 的高阶方法和 MPNN 的固有局限性 **[Wu et al. 2021, §4.4]**。

## Prerequisites

- 图论基础：$G = (V, E)$，邻接矩阵，同构
- MPNN 框架（参见 `11_ml_theory/derivations/gnn_message_passing.md`）
- 集合与多重集（multiset）的概念
- 单射函数的定义

---

## Part 1: Graph Isomorphism Problem

### 1.1 定义

两个图 $G_1 = (V_1, E_1)$ 和 $G_2 = (V_2, E_2)$ **同构**（记为 $G_1 \cong G_2$）当且仅当存在双射 $\phi: V_1 \to V_2$ 使得：

$$(u, v) \in E_1 \Leftrightarrow (\phi(u), \phi(v)) \in E_2$$

### 1.2 计算复杂度

- 图同构问题不知道是否在 P 中（也不知道是否 NP-complete）
- Babai (2016)：图同构可在准多项式时间 $\exp((\log n)^{O(1)})$ 内判定
- 实践中 1-WL 测试已经能区分绝大多数图

---

## Part 2: 1-WL (Color Refinement) Test

### 2.1 算法

**输入**：图 $G = (V, E)$，初始颜色 $c_v^{(0)}$（可以是节点标签，或所有节点相同初始色）

**迭代**：

$$\boxed{c_v^{(l+1)} = \mathrm{HASH}\!\left(c_v^{(l)},\; \{\!\{ c_u^{(l)} : u \in \mathcal{N}(v) \}\!\}\right)}$$

其中：
- $\{\!\{ \cdot \}\!\}$ 是 **multiset**（多重集，允许重复元素）
- $\mathrm{HASH}$ 是任意**单射函数**，将 (颜色, 邻居颜色多重集) 映射到新颜色

**终止条件**：当颜色分区不再变化时停止（至多 $n$ 轮）。

**判定规则**：若两图 $G_1, G_2$ 在某轮的颜色 multiset $\{\!\{ c_v^{(l)} : v \in V \}\!\}$ 不同，则 $G_1 \not\cong G_2$。

### 2.2 性质

**定理**：1-WL 是图同构的**必要条件**检测：
- 若 1-WL 判定两图不同构 → 一定不同构（**sound**）
- 若 1-WL 判定两图"可能同构" → 不一定同构（**incomplete**）

### 2.3 1-WL 无法区分的例子

**正则图反例**：两个非同构的 3-正则图可能具有完全相同的 1-WL 颜色序列。

经典例子：Cai-Furer-Immerman (1992) 构造了需要 $k$-WL（$k \geq 3$）才能区分的图对。

**直觉**：1-WL 只能看到"树形"的局部邻域结构（$l$-hop 邻域的展开树），无法检测环结构的全局差异。

---

## Part 3: MPNN $\leq$ 1-WL

### 3.1 MPNN 回顾

第 $l$ 层更新：

$$h_v^{(l+1)} = U^{(l)}\!\left(h_v^{(l)},\; \bigoplus_{u \in \mathcal{N}(v)} M^{(l)}(h_v^{(l)}, h_u^{(l)})\right)$$

图级表示：

$$h_G = R\!\left(\{\!\{ h_v^{(L)} : v \in V \}\!\}\right)$$

### 3.2 主定理：GNN $\leq$ WL (Lemma 2)

**Lemma 2** **[Xu et al. 2019, Lemma 2]**：令 $G_1$, $G_2$ 为任意两个非同构图。如果 GNN $\mathcal{A}: \mathcal{G} \to \mathbb{R}^d$ 将 $G_1$ 和 $G_2$ 映射为不同嵌入，则 WL test 也判定 $G_1$ 和 $G_2$ 不同构。

即：**任何基于聚合的 GNN 的区分能力 $\leq$ 1-WL**。

### 3.3 证明 **[Xu et al. 2019, Appendix A]**

**证明策略**：反证法。假设 GNN $\mathcal{A}$ 在第 $k$ 轮得到 $\mathcal{A}(G_1) \neq \mathcal{A}(G_2)$，但 WL test 无法判定 $G_1, G_2$ 不同构。则从第 $0$ 到 $k$ 轮，$G_1, G_2$ 始终有相同的 WL 节点标签集合。

**关键引理**：在同一图 $G$ 上，若 WL 节点标签 $l_v^{(i)} = l_u^{(i)}$，则 GNN 节点特征 $h_v^{(i)} = h_u^{(i)}$，对任意 $i$ 成立。

**Base case** ($i = 0$)：WL 和 GNN 使用相同初始特征。

**Inductive step**：假设对第 $j$ 层成立。若 $l_v^{(j+1)} = l_u^{(j+1)}$，则必有：

$$\left(l_v^{(j)}, \{\!\{l_w^{(j)} : w \in \mathcal{N}(v)\}\!\}\right) = \left(l_u^{(j)}, \{\!\{l_w^{(j)} : w \in \mathcal{N}(u)\}\!\}\right)$$

由归纳假设：

$$\left(h_v^{(j)}, \{\!\{h_w^{(j)} : w \in \mathcal{N}(v)\}\!\}\right) = \left(h_u^{(j)}, \{\!\{h_w^{(j)} : w \in \mathcal{N}(u)\}\!\}\right)$$

GNN 的 AGGREGATE 和 COMBINE 对相同输入产生相同输出，故 $h_v^{(j+1)} = h_u^{(j+1)}$。

由归纳法，存在合法映射 $\phi$ 使得 $h_v^{(i)} = \phi(l_v^{(i)})$。由 $G_1, G_2$ 有相同 WL 邻域标签 multiset，推得两图有相同 GNN 邻域特征集合，进而 $\{h_v^{(k)}\}$ 相同。图级 readout 是置换不变的，因此 $\mathcal{A}(G_1) = \mathcal{A}(G_2)$，与假设矛盾。$\square$

**关键洞察**：MPNN 的更新是 1-WL 更新的"连续松弛"——HASH 被替换为可微函数 $U \circ \bigoplus \circ M$。

---

## Part 4: GIN = 1-WL **[Xu et al. 2019, §4]**

### 4.1 达到上界的条件：Theorem 3

**Theorem 3** **[Xu et al. 2019, Theorem 3]**：GNN $\mathcal{A}: \mathcal{G} \to \mathbb{R}^d$ 与 WL test 同样强大（即 WL test 判定为不同构的图，$\mathcal{A}$ 也映射为不同嵌入），只要以下条件成立：

- **(a)** $\mathcal{A}$ 的节点更新为 $h_v^{(k)} = \phi(h_v^{(k-1)}, f(\{h_u^{(k-1)} : u \in \mathcal{N}(v)\}))$，其中 $f$（操作于 multiset）和 $\phi$ 均为**单射函数**
- **(b)** $\mathcal{A}$ 的图级 readout（操作于节点特征 multiset $\{h_v^{(k)}\}$）是**单射的**

**证明** **[Xu et al. 2019, Appendix B]**：对 $k$ 归纳，证明存在单射 $\varphi$ 使 $h_v^{(k)} = \varphi(l_v^{(k)})$。关键步骤：代入 $h_v^{(k-1)} = \varphi(l_v^{(k-1)})$ 后，利用 $\phi, f$ 的单射性得到 $h_v^{(k)} = \psi(l_v^{(k-1)}, \{l_u^{(k-1)}\})$，再由 WL hash $g$ 的单射性得 $h_v^{(k)} = \psi \circ g^{-1}(l_v^{(k)})$，单射函数的复合仍为单射。

**Lemma 4 (可数性传播)** **[Xu et al. 2019, Lemma 4]**：假设输入特征空间 $\mathcal{X}$ 可数。GNN 第 $k$ 层函数 $g^{(k)}$ 的值域（节点隐藏特征空间）对所有 $k = 1, \ldots, L$ 也是可数的。

### 4.2 Sum 聚合的单射性：Lemma 5

**Lemma 5** **[Xu et al. 2019, Lemma 5]**：假设 $\mathcal{X}$ 可数。存在函数 $f: \mathcal{X} \to \mathbb{R}^n$ 使得 $h(X) = \sum_{x \in X} f(x)$ 对有界大小的 multiset $X \subset \mathcal{X}$ 是**唯一的（单射的）**。更进一步，任何 multiset 函数 $g$ 可分解为 $g(X) = \phi(\sum_{x \in X} f(x))$。

**证明** **[Xu et al. 2019, Appendix D]**：构造映射 $Z: \mathcal{X} \to \mathbb{N}$，令 $N$ 为 multiset 大小上界，取 $f(x) = N^{-Z(x)}$。这等价于 $N$-进制表示，不同 multiset 的求和结果在 $N$-进制下不同。$h(X) = \sum_{x \in X} f(x)$ 的单射性保证 $\phi$ 是良定义的。

**反例说明 mean 和 max 不是单射** **[Xu et al. 2019, §5.2, Figure 3]**：
- **Mean**：$\{\!\{1, 1, 1\}\!\}$ 和 $\{\!\{1\}\!\}$ 的 mean 都是 1 → 无法区分
- **Max**：$\{\!\{1, 2, 3\}\!\}$ 和 $\{\!\{3\}\!\}$ 的 max 都是 3 → 无法区分
- **Sum**：$\{\!\{1, 1, 1\}\!\} \to 3$，$\{\!\{1\}\!\} \to 1$ → 可区分

**表达力排序** **[Xu et al. 2019, Figure 2]**：**sum > mean > max**。

### 4.3 GIN 更新规则：Corollary 6

**Corollary 6** **[Xu et al. 2019, Corollary 6]**：假设 $\mathcal{X}$ 可数。存在函数 $f: \mathcal{X} \to \mathbb{R}^n$，使得对无穷多个 $\epsilon$ 的选取（包括所有**无理数**），

$$h(c, X) = (1 + \epsilon) \cdot f(c) + \sum_{x \in X} f(x)$$

对每对 $(c, X)$（$c \in \mathcal{X}$, $X \subset \mathcal{X}$ 有界 multiset）是唯一的。且任何关于 $(c, X)$ 的函数 $g$ 可分解为 $g(c, X) = \varphi((1+\epsilon) \cdot f(c) + \sum_{x \in X} f(x))$。

**证明** **[Xu et al. 2019, Appendix E]**：反证法。若 $c' = c$ 但 $X' \neq X$，由 Lemma 5 直接矛盾。若 $c' \neq c$，则等式 $\epsilon(f(c) - f(c')) = \text{有理数}$，但左边是无理数乘非零有理数 = 无理数，矛盾。

由此得到 GIN 更新规则 **[Xu et al. 2019, Eq.(4.1)]**：

$$\boxed{h_v^{(k)} = \mathrm{MLP}^{(k)}\!\left((1 + \epsilon^{(k)})\, h_v^{(k-1)} + \sum_{u \in \mathcal{N}(v)} h_u^{(k-1)}\right)}$$

其中：
- **Sum 聚合**：保证对 multiset 的单射性（Lemma 5）
- **MLP**：通用函数近似器（Hornik 1991），建模 $f^{(k+1)} \circ \varphi^{(k)}$ 的复合
- **$(1 + \epsilon)$**：分离中心节点和邻居聚合，$\epsilon$ 可学习或固定

### 4.4 GIN 的图级别 readout **[Xu et al. 2019, Eq.(4.2)]**

$$h_G = \mathrm{CONCAT}\!\left(\mathrm{READOUT}\!\left(\{\!\{ h_v^{(k)} : v \in V \}\!\}\right) \;:\; k = 0, 1, \ldots, K\right)$$

使用所有层的信息（类似 JK-Net），因为不同层捕获不同尺度的结构信息。当 READOUT 为 sum 时，GIN 可证明地推广了 WL test 和 WL 子树核 **[Xu et al. 2019, §4.2]**。

### 4.5 辅助定理：1-layer perceptron 不足

**Lemma 7** **[Xu et al. 2019, Lemma 7]**：存在有限 multiset $X_1 \neq X_2$ 使得对任意线性映射 $W$，$\sum_{x \in X_1} \mathrm{ReLU}(Wx) = \sum_{x \in X_2} \mathrm{ReLU}(Wx)$。

**证明** **[Xu et al. 2019, Appendix F]**：取 $X_1 = \{1,1,1,1,1\}$，$X_2 = \{2,3\}$（和相同）。利用 ReLU 的齐次性：对所有正数 $x$，$\mathrm{ReLU}(Wx) = Wx$，因此 $\sum_{x \in X} \mathrm{ReLU}(Wx) = \mathrm{ReLU}(W \sum_{x \in X} x)$。两个 multiset 和相同，故不可区分。

**意义**：这说明 GCN（使用 1-layer perceptron $\sigma \circ W$）的表达力严格弱于 GIN（使用 MLP）。

### 4.6 Mean 和 Max 聚合的精确刻画

**Corollary 7 (Mean captures distributions)** **[Xu et al. 2019, Corollary 7]**：假设 $\mathcal{X}$ 可数，存在 $f$ 使得 $h(X) = \frac{1}{|X|}\sum_{x \in X} f(x)$ 满足 $h(X_1) = h(X_2)$ 当且仅当 $X_1, X_2$ 有相同分布，即 $X_1 = (S, m)$, $X_2 = (S, k \cdot m)$。

**Corollary 8 (Max captures sets)** **[Xu et al. 2019, Corollary 8]**：假设 $\mathcal{X}$ 可数，存在 $f: \mathcal{X} \to \mathbb{R}^\infty$ 使得 $h(X) = \max_{x \in X} f(x)$ 满足 $h(X_1) = h(X_2)$ 当且仅当 $X_1, X_2$ 有相同底层集合。

---

## Part 5: Higher-Order WL and Beyond MPNN

### 5.1 $k$-WL 层次

**$k$-WL test**：对 $k$-元组 $(v_1, \ldots, v_k)$ 进行颜色细化。

$$c_{(v_1,\ldots,v_k)}^{(l+1)} = \mathrm{HASH}\!\left(c_{(v_1,\ldots,v_k)}^{(l)},\; \left(\{\!\{ c_{(v_1,\ldots,v_{i-1},w,v_{i+1},\ldots,v_k)}^{(l)} : w \in V \}\!\}\right)_{i=1}^k\right)$$

即：对每个位置 $i$，将第 $i$ 个元素替换为所有可能的节点 $w$，得到一个 multiset。

**层次关系**（Cai-Furer-Immerman, 1992）：

$$1\text{-WL} < 3\text{-WL} \leq 4\text{-WL} \leq \cdots$$

注意：1-WL = 2-WL（folklore result），所以跳跃是从 1-WL 到 3-WL。

### 5.2 $k$-WL 对应的 GNN

**$k$-GNN (Morris et al., 2019)**：将 MPNN 推广到 $k$-元组上的消息传递。

时间复杂度：$O(n^k)$ 存储 $k$-元组，$O(n^{k+1})$ 的消息传递 → 对大图不实际。

### 5.3 MPNN 的固有局限性

1-WL（和 MPNN）**无法**：

- **数三角形**：无法计算节点所属三角形数量
- **区分某些正则图**：如 Petersen graph vs. 其他 3-正则图
- **检测子图结构**：如判断是否包含特定子图

**具体例子**：

考虑两个 3-正则图 $G_1$（6个节点的棱柱图）和 $G_2$（6个节点的Mobius-Kantor子图）。两者的 1-WL 颜色序列完全相同（所有节点始终同色），但它们不同构。

### 5.4 超越 MPNN 的方法

| 方法 | 原理 | 表达力 | 复杂度 |
|------|------|--------|--------|
| $k$-GNN | $k$-元组消息传递 | $\leq k$-WL | $O(n^{k+1})$ |
| Subgraph GNN | 对每个节点提取子图 | $> 1$-WL | $O(n \cdot \text{subgraph cost})$ |
| Random features | 添加随机节点特征打破对称 | 概率上 $>$ 1-WL | $O(n)$ 额外开销 |
| Positional encoding | 加入 Laplacian 特征向量位置编码 | $> 1$-WL | $O(n^2)$ (eigendecomposition) |
| Graph Transformer | 全局注意力 + 位置编码 | $>$ 1-WL | $O(n^2)$ |

### 5.5 与 QEC 的关联

QEC 解码需要理解**全局拓扑结构**（如同调类、逻辑算符），这超越了局部邻域聚合能力。这解释了为什么简单的 MPNN decoder 在大码距时性能下降——它们在表达力上受限于 1-WL，无法捕获某些全局特征。

---

## Summary

| 概念 | 关键结果 |
|------|---------|
| 1-WL test | $c_v^{(l+1)} = \mathrm{HASH}(c_v^{(l)}, \{\!\{c_u^{(l)}\}\!\})$，必要非充分 |
| MPNN $\leq$ 1-WL | WL 颜色相同 → MPNN 表示相同（归纳证明） |
| GIN = 1-WL | sum 聚合 + MLP 更新 → 达到上界 |
| $k$-WL 层次 | 1-WL $<$ 3-WL $\leq$ 4-WL $\leq \cdots$ |
| MPNN 局限 | 无法数三角形、区分正则图 |

**核心洞察**：
1. 所有 MPNN 的表达力都不超过 1-WL，这是一个**基本理论限制**
2. GIN 通过 sum + MLP 紧达此界
3. 超越 1-WL 需要高阶方法（$k$-GNN）或结构增强（随机特征、位置编码）
4. 这一理论框架为理解 GNN 的能力和局限提供了精确的数学工具

---

## References

1. Xu, K., Hu, W., Leskovec, J., & Jegelka, S. (2019). How Powerful are Graph Neural Networks? ICLR.
2. Morris, C., Ritzert, M., Fey, M., Hamilton, W.L., Lenssen, J.E., Rattan, G., & Grohe, M. (2019). Weisfeiler and Leman Go Neural: Higher-Order Graph Neural Networks. AAAI.
3. Weisfeiler, B. & Leman, A. (1968). The reduction of a graph to canonical form and the algebra which appears therein. NTI, Series 2.
4. Cai, J., Furer, M., & Immerman, N. (1992). An optimal lower bound on the number of variables for graph identification. Combinatorica.
5. Wu, Z., Pan, S., Chen, F., Long, G., Zhang, C., & Yu, P.S. (2020). A Comprehensive Survey on Graph Neural Networks. IEEE TNNLS.
6. Babai, L. (2016). Graph Isomorphism in Quasipolynomial Time. STOC.
7. Frasca, F., Bevilacqua, B., Bronstein, M.M., & Maron, H. (2022). Understanding and Extending Subgraph GNNs by Rethinking Their Symmetries. NeurIPS.
