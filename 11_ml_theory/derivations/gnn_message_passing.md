# GNN Message Passing Framework

> **Tags**: `gnn`, `message-passing`, `graph-neural-network`, `gcn`, `gat`

## Statement

推导消息传递神经网络（Message Passing Neural Networks, MPNN）的通用框架，并证明GCN、GAT、GraphSAGE等经典图神经网络都是该框架的特例。涵盖从谱方法到空间方法的联系。

## Prerequisites

- 图论基础：$G = (V, E)$，邻接矩阵 $A$，度矩阵 $D$，拉普拉斯矩阵 $L$
- 神经网络基础：线性变换、非线性激活
- 矩阵分析：特征值分解
- 注意力机制基本概念

---

## Part 1: Graph Notation

### 1.1 基本定义

给定图 $G = (V, E)$：

- 节点集 $V$，$|V| = n$
- 边集 $E \subseteq V \times V$
- 邻接矩阵 $A \in \{0, 1\}^{n \times n}$，$A_{ij} = 1$ iff $(i, j) \in E$
- 度矩阵 $D = \mathrm{diag}(d_1, \ldots, d_n)$，$d_i = \sum_j A_{ij}$
- 节点特征矩阵 $X \in \mathbb{R}^{n \times d}$，第 $i$ 行 $h_i^{(0)} = x_i \in \mathbb{R}^d$
- 边特征 $e_{ij} \in \mathbb{R}^{d_e}$（可选）
- 邻居集 $\mathcal{N}(v) = \{u : (u, v) \in E\}$

### 1.2 图拉普拉斯矩阵

**Unnormalized Laplacian:**

$$L = D - A$$

**Symmetric normalized Laplacian:**

$$L_{\mathrm{sym}} = D^{-1/2} L D^{-1/2} = I - D^{-1/2} A D^{-1/2}$$

**性质**：$L_{\mathrm{sym}}$ 是半正定的，特征值 $0 = \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n \leq 2$。

---

## Part 2: Spectral Approach — 从图傅里叶变换到GCN

### 2.1 图傅里叶变换

$L_{\mathrm{sym}}$ 的特征分解：$L_{\mathrm{sym}} = U \Lambda U^T$，其中 $U = [u_1, \ldots, u_n]$ 是正交特征向量矩阵。

信号 $x \in \mathbb{R}^n$ 的图傅里叶变换：

$$\hat{x} = U^T x$$

逆变换：$x = U \hat{x}$

### 2.2 谱图卷积 **[Kipf & Welling 2017, Eq.(3)]**

图上的卷积定义为频域的逐元素乘法（类比经典傅里叶卷积定理）**[Kipf & Welling 2017, §2]**：

$$g_\theta \star x = U g_\theta U^T x$$

其中 $g_\theta = \mathrm{diag}(\theta)$，$\theta \in \mathbb{R}^N$ 参数化滤波器。$U^T x$ 是图傅里叶变换。

**问题**：$N$ 个自由参数，且与 $U$ 的矩阵乘法复杂度 $O(N^2)$，计算特征分解需 $O(N^3)$，不实用。

### 2.3 ChebNet: 多项式近似 (Defferrard et al., 2016) **[Kipf & Welling 2017, Eq.(4)]**

用切比雪夫多项式 $T_k$ 近似滤波器 **[Kipf & Welling 2017, Eq.(4)]**：

$$g_{\theta'}(\Lambda) \approx \sum_{k=0}^{K} \theta_k'\, T_k(\tilde{\Lambda})$$

其中 $\tilde{\Lambda} = \frac{2}{\lambda_{\max}}\Lambda - I_N$ 将特征值缩放到 $[-1, 1]$，$\theta' \in \mathbb{R}^K$ 是切比雪夫系数向量。

切比雪夫多项式的递推关系：

$$T_0(x) = 1, \quad T_1(x) = x, \quad T_k(x) = 2x\, T_{k-1}(x) - T_{k-2}(x)$$

**关键**：$(U\Lambda U^T)^k = U\Lambda^k U^T$，因此 $T_k(\tilde{L})$ 只涉及 $L$ 的 $k$ 次幂，即 $k$-hop 邻居。避免了特征分解！

卷积变为 **[Kipf & Welling 2017, Eq.(5)]**：

$$g_{\theta'} \star x \approx \sum_{k=0}^{K} \theta_k'\, T_k(\tilde{L})\, x$$

其中 $\tilde{L} = \frac{2}{\lambda_{\max}}L - I_N$。只有 $K+1$ 个参数，计算复杂度 $O(K|\mathcal{E}|)$（$K$-localized）。

### 2.4 GCN: 一阶近似 **[Kipf & Welling 2017, §2.1]**

取 $K = 1$，$\lambda_{\max} \approx 2$ **[Kipf & Welling 2017, Eq.(5)]**：

$$g_{\theta'} \star x \approx \theta_0'\, x + \theta_1' (L - I_N) x = \theta_0'\, x - \theta_1'\, D^{-1/2} A D^{-1/2} x$$

进一步简化：令 $\theta_0' = -\theta_1' = \theta$ **[Kipf & Welling 2017, Eq.(6)]**：

$$g_\theta \star x \approx \theta (I_N + D^{-1/2} A D^{-1/2}) x$$

**Renormalization trick** **[Kipf & Welling 2017, §2.1]**：$I_N + D^{-1/2} A D^{-1/2}$ 的特征值在 $[0, 2]$，反复使用会数值不稳定。引入重整化：$I_N + D^{-1/2}AD^{-1/2} \rightarrow \tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$。

令 $\tilde{A} = A + I_N$（加自环），$\tilde{D}_{ii} = \sum_j \tilde{A}_{ij}$。推广到多通道信号 $X \in \mathbb{R}^{N \times C}$ 和 $F$ 个滤波器 **[Kipf & Welling 2017, Eq.(7)]**：

$$Z = \tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}X\Theta$$

其中 $\Theta \in \mathbb{R}^{C \times F}$ 是滤波器参数矩阵。加上非线性激活得到层传播规则 **[Kipf & Welling 2017, Eq.(2)]**：

$$\boxed{H^{(l+1)} = \sigma\left(\tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2} H^{(l)} W^{(l)}\right)}$$

这就是 GCN 层的矩阵形式。计算复杂度 $O(|\mathcal{E}|FC)$，线性于边数。

**两层 GCN 实例** **[Kipf & Welling 2017, Eq.(8)]**：

$$Z = f(X, A) = \mathrm{softmax}\!\left(\hat{A}\, \mathrm{ReLU}\!\left(\hat{A} X W^{(0)}\right) W^{(1)}\right)$$

其中 $\hat{A} = \tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$ 在预处理阶段计算。

### 2.5 GCN 的逐节点形式

$$h_v^{(l+1)} = \sigma\left(W^{(l)} \sum_{u \in \mathcal{N}(v) \cup \{v\}} \frac{1}{\sqrt{\tilde{d}_v \tilde{d}_u}}\, h_u^{(l)}\right)$$

其中 $\tilde{d}_v = d_v + 1$。这清楚地展示了消息传递结构。

---

## Part 3: General Message Passing Framework (Gilmer et al., 2017)

### 3.1 MPNN 通用公式

第 $l$ 层的更新分三步：

**Step 1: Message（消息计算）**

$$m_{u \to v}^{(l)} = M^{(l)}\left(h_v^{(l)}, h_u^{(l)}, e_{uv}\right)$$

**Step 2: Aggregate（消息聚合）**

$$m_v^{(l)} = \bigoplus_{u \in \mathcal{N}(v)} m_{u \to v}^{(l)}$$

其中 $\bigoplus$ 是置换不变的聚合算子（sum, mean, max等）。

**Step 3: Update（节点更新）**

$$h_v^{(l+1)} = U^{(l)}\left(h_v^{(l)}, m_v^{(l)}\right)$$

### 3.2 Readout（图级别输出）

对于图级别任务，需要将所有节点表示聚合为图表示：

$$h_G = R\left(\{h_v^{(L)} : v \in V\}\right)$$

常见选择：$R = \sum$、$R = \mathrm{mean}$、或 attention-based pooling。

### 3.3 置换不变性与等变性

**定理**：如果 $M, \bigoplus, U, R$ 都与节点排序无关（permutation invariant/equivariant），则MPNN对图同构具有不变性。

具体地：
- 节点表示 $h_v^{(l)}$ 是置换等变的（permutation equivariant）
- 图表示 $h_G$ 是置换不变的（permutation invariant）

---

## Part 4: Classical GNNs as MPNN Special Cases

### 4.1 GCN **[Kipf & Welling 2017, Eq.(2)]**

| 组件 | 具体形式 |
|---|---|
| Message | $m_{u \to v} = \frac{1}{\sqrt{\tilde{d}_v \tilde{d}_u}} W h_u$ |
| Aggregate | $\bigoplus = \sum$ |
| Update | $h_v' = \sigma(m_v)$（无残差） |

$$h_v^{(l+1)} = \sigma\left(\sum_{u \in \mathcal{N}(v) \cup \{v\}} \frac{1}{\sqrt{\tilde{d}_v \tilde{d}_u}}\, W^{(l)} h_u^{(l)}\right)$$

**特点**：归一化系数 $\frac{1}{\sqrt{\tilde{d}_v \tilde{d}_u}}$ 是固定的，由图结构决定。

注意 **[Xu et al. 2019, §2, Eq.(3)]** 将 GCN 等价地表示为 AGGREGATE 和 COMBINE 合并的形式：

$$h_v^{(k)} = \mathrm{ReLU}\!\left(W \cdot \mathrm{MEAN}\left\{h_u^{(k-1)},\; \forall u \in \mathcal{N}(v) \cup \{v\}\right\}\right)$$

这是 mean 聚合的形式，使用 mean 而非 sum 限制了 GCN 的表达力（见 Part 5）。

### 4.2 GraphSAGE (Hamilton et al., 2017)

| 组件 | 具体形式 |
|---|---|
| Message | $m_{u \to v} = h_u$ |
| Aggregate | $\bigoplus \in \{\mathrm{mean}, \mathrm{LSTM}, \mathrm{max\text{-}pool}\}$ |
| Update | $h_v' = \sigma(W \cdot [h_v \| \mathrm{AGG}(\{h_u\})])$ |

$$h_v^{(l+1)} = \sigma\left(W^{(l)} \cdot \mathrm{CONCAT}\left(h_v^{(l)},\; \mathrm{AGG}\left(\{h_u^{(l)} : u \in \mathcal{N}(v)\}\right)\right)\right)$$

**特点**：显式分离自身表示和邻居聚合，支持采样邻居（mini-batch训练）。

### 4.3 GAT **[Veličković et al. 2018, §2.1]**

| 组件 | 具体形式 |
|---|---|
| Message | $m_{u \to v} = \alpha_{vu}\, W h_u$ |
| Aggregate | $\bigoplus = \sum$ |
| Update | $h_v' = \sigma(m_v)$ |

注意力系数的完整计算（原文 graph attentional layer 定义）：

**输入** **[Veličković et al. 2018, §2.1]**：节点特征 $\mathbf{h} = \{\vec{h}_1, \ldots, \vec{h}_N\}$，$\vec{h}_i \in \mathbb{R}^F$。输出新特征 $\mathbf{h}' = \{\vec{h}_1', \ldots, \vec{h}_N'\}$，$\vec{h}_i' \in \mathbb{R}^{F'}$。

**Step 1**：共享线性变换 **[Veličković et al. 2018, §2.1]**

$$z_i = W \vec{h}_i, \quad W \in \mathbb{R}^{F' \times F}$$

**Step 2**：注意力系数（general form） **[Veličković et al. 2018, Eq.(1)]**

$$e_{ij} = a(W\vec{h}_i, W\vec{h}_j)$$

其中 $a : \mathbb{R}^{F'} \times \mathbb{R}^{F'} \to \mathbb{R}$ 是共享的注意力机制。仅对 $j \in \mathcal{N}_i$（一阶邻居+自身）计算（masked attention）。

**Step 3**：Softmax归一化 **[Veličković et al. 2018, Eq.(2)]**

$$\alpha_{ij} = \mathrm{softmax}_j(e_{ij}) = \frac{\exp(e_{ij})}{\sum_{k \in \mathcal{N}_i} \exp(e_{ik})}$$

具体实现中，$a$ 是单层前馈网络 **[Veličković et al. 2018, Eq.(3)]**：

$$\alpha_{ij} = \frac{\exp\left(\mathrm{LeakyReLU}\left(\vec{\mathbf{a}}^T [W\vec{h}_i \| W\vec{h}_j]\right)\right)}{\sum_{k \in \mathcal{N}_i} \exp\left(\mathrm{LeakyReLU}\left(\vec{\mathbf{a}}^T [W\vec{h}_i \| W\vec{h}_k]\right)\right)}$$

其中 $\vec{\mathbf{a}} \in \mathbb{R}^{2F'}$ 是可学习的注意力向量，$\|$ 表示拼接，LeakyReLU 负斜率 $\alpha = 0.2$。

**Step 4**：加权聚合 **[Veličković et al. 2018, Eq.(4)]**

$$\vec{h}_i' = \sigma\left(\sum_{j \in \mathcal{N}_i} \alpha_{ij}\, W\vec{h}_j\right)$$

**Multi-head attention** **[Veličković et al. 2018, Eq.(5)]**：$K$ 个独立注意力头拼接：

$$\vec{h}_i' = \big\|_{k=1}^{K} \sigma\left(\sum_{j \in \mathcal{N}_i} \alpha_{ij}^k\, W^k \vec{h}_j\right)$$

输出维度为 $KF'$。最后一层用均值代替拼接 **[Veličković et al. 2018, Eq.(6)]**：

$$\vec{h}_i' = \sigma\left(\frac{1}{K}\sum_{k=1}^{K}\sum_{j \in \mathcal{N}_i} \alpha_{ij}^k\, W^k \vec{h}_j\right)$$

**特点** **[Veličković et al. 2018, §2.2]**：
- 计算高效：单头复杂度 $O(|V|FF' + |E|F')$，与 GCN 同阶
- 注意力系数是数据依赖的（learnable），不同邻居获得不同权重
- 不依赖全局图结构，直接适用于归纳学习（inductive learning）
- 支持有向图（只需不计算缺失边的 $\alpha_{ij}$）

### 4.4 GIN **[Xu et al. 2019, §4.1, Eq.(4.1)]**

| 组件 | 具体形式 |
|---|---|
| Message | $m_{u \to v} = h_u$ |
| Aggregate | $\bigoplus = \sum$ |
| Update | $h_v' = \mathrm{MLP}((1 + \epsilon) h_v + \sum_{u} h_u)$ |

$$h_v^{(k)} = \mathrm{MLP}^{(k)}\!\left((1 + \epsilon^{(k)})\, h_v^{(k-1)} + \sum_{u \in \mathcal{N}(v)} h_u^{(k-1)}\right)$$

**理论依据**：

- **Lemma 5 (sum 聚合的单射性)** **[Xu et al. 2019, Lemma 5]**：假设 $\mathcal{X}$ 可数，存在函数 $f: \mathcal{X} \to \mathbb{R}^n$ 使得 $h(X) = \sum_{x \in X} f(x)$ 对有界大小的 multiset $X$ 是单射的。且任何 multiset 函数 $g$ 可分解为 $g(X) = \phi(\sum_{x \in X} f(x))$。

- **Corollary 6 (GIN 更新规则)** **[Xu et al. 2019, Corollary 6]**：假设 $\mathcal{X}$ 可数，存在函数 $f: \mathcal{X} \to \mathbb{R}^n$ 使得对无穷多个 $\epsilon$ 的选取（包括所有无理数），$h(c, X) = (1 + \epsilon) \cdot f(c) + \sum_{x \in X} f(x)$ 对每对 $(c, X)$ 唯一。

- **MLP 的使用**：由通用近似定理，MLP 可以学习 $f$ 和 $\varphi$，实践中将 $f^{(k+1)} \circ \varphi^{(k)}$ 建模为一个 MLP。

**图级 readout** **[Xu et al. 2019, Eq.(4.2)]**：

$$h_G = \mathrm{CONCAT}\!\left(\mathrm{READOUT}\!\left(\{h_v^{(k)} : v \in G\}\right) \;:\; k = 0, 1, \ldots, K\right)$$

使用所有层信息（类似 JK-Net），readout 为 sum 聚合时，GIN 可证明地推广了 WL test 和 WL 子树核。

**理论保证** **[Xu et al. 2019, Theorem 3]**：GIN 在可数特征空间上与 1-WL test 同等强大，是 MPNN 中表达力最强的。

---

## Part 5: Expressiveness — Weisfeiler-Leman Hierarchy **[Xu et al. 2019, §3–4]**

### 5.1 1-WL Test

1-WL（Weisfeiler-Leman）图同构测试的迭代过程：

$$c_v^{(l+1)} = \mathrm{HASH}\left(c_v^{(l)},\; \{\!\{ c_u^{(l)} : u \in \mathcal{N}(v) \}\!\}\right)$$

其中 $\{\!\{\cdot\}\!\}$ 是 multiset（允许重复的集合）。HASH 是将不同 multiset 映射为唯一新标签的单射函数。

### 5.2 MPNN $\leq$ 1-WL

**Lemma 2** **[Xu et al. 2019, Lemma 2]**：令 $G_1$, $G_2$ 为任意两个非同构图。如果 GNN $\mathcal{A}: \mathcal{G} \to \mathbb{R}^d$ 将 $G_1$ 和 $G_2$ 映射为不同嵌入，则 WL test 也判定 $G_1$ 和 $G_2$ 不同构。

即：**任何基于聚合的 GNN 的区分能力 $\leq$ 1-WL test**。

**Theorem 3 (达到上界的条件)** **[Xu et al. 2019, Theorem 3]**：GNN $\mathcal{A}$ 与 WL test 同样强大，若：

- (a) 节点更新 $h_v^{(k)} = \phi(h_v^{(k-1)}, f(\{h_u^{(k-1)} : u \in \mathcal{N}(v)\}))$，其中 $f$（操作于 multiset）和 $\phi$ 均为**单射函数**
- (b) 图级 readout（操作于节点特征 multiset）是**单射的**

**证明核心** **[Xu et al. 2019, Appendix A]**：对层数 $k$ 归纳证明存在单射映射 $\varphi$ 使得 $h_v^{(k)} = \varphi(l_v^{(k)})$。Base case ($k=0$)：WL 和 GNN 使用相同初始特征。归纳步：利用 $\phi, f$ 的单射性及 $g$（WL 的 HASH）的单射性，得到 $h_v^{(k)} = \psi \circ g^{-1}(l_v^{(k)})$，其中 $\psi \circ g^{-1}$ 是单射的复合。

### 5.3 聚合函数的表达力层次 **[Xu et al. 2019, §5]**

**排序** **[Xu et al. 2019, Figure 2]**：sum > mean > max

- **Sum**：捕获完整 multiset（单射）
- **Mean**：捕获分布/比例（Corollary 7 **[Xu et al. 2019, Corollary 7]**：mean 区分能力等价于分布等价类）
- **Max**：将 multiset 退化为集合（Corollary 8 **[Xu et al. 2019, Corollary 8]**：max 区分能力等价于底层集合）

**Lemma 7** **[Xu et al. 2019, Lemma 7]**：1-layer perceptron $\sigma \circ W$ 不足以区分某些 multiset，因为 ReLU 的齐次性使其退化为线性求和。MLP（非通用近似器中的 1-layer perceptron）是必要的。

### 5.4 局限性

1-WL 无法区分的图结构（MPNN 同样无法区分）**[Xu et al. 2019, §3]**：
- 某些正则图（如 Petersen graph vs. 其它 3-正则图）
- 需要"数三角形"等 higher-order structure 的任务

解决方案：higher-order GNN（$k$-WL）、subgraph GNN、random features 等。

---

## Part 6: Edge Features and Edge Updates

### 6.1 带边特征的消息传递

$$m_{u \to v}^{(l)} = M^{(l)}(h_v^{(l)}, h_u^{(l)}, e_{uv})$$

常见实现：

- **拼接**：$m_{u \to v} = W [h_u \| e_{uv}]$
- **乘法**：$m_{u \to v} = W h_u \odot W_e e_{uv}$
- **注意力**：将 $e_{uv}$ 纳入注意力计算

### 6.2 边更新（用于图transformer等）

$$e_{uv}^{(l+1)} = E^{(l)}(h_u^{(l)}, h_v^{(l)}, e_{uv}^{(l)})$$

同时更新节点和边表示，常用于需要边级别预测的任务（如分子性质预测中的键类型）。

---

## Part 6.5: Transformer Self-Attention as MPNN on Complete Graph

> **See also**: [attention_mechanism.md] for complete attention theory.

### 6.5.1 Transformer Self-Attention 的消息传递形式

Transformer 的 self-attention 层（**[Vaswani et al. 2017, §3.2]**）可以精确地表示为在完全图 $K_n$ 上的消息传递。在完全图上，$\mathcal{N}(v) = V$（所有节点），每个节点与所有其他节点交换信息。

| 组件 | 具体形式 |
|---|---|
| Graph | 完全图 $K_n$，$\mathcal{N}(v) = V$ |
| Message | $m_{u \to v} = \alpha_{vu} \cdot h_u W^V$ |
| Aggregate | $\bigoplus = \sum$（softmax 归一化的加权和） |
| Update | $h_v' = \mathrm{LN}(h_v + \mathrm{MHA}(h_v)) \to \mathrm{LN}(h_v' + \mathrm{FFN}(h_v'))$ |

其中注意力权重（scaled dot-product）：

$$\alpha_{vu} = \frac{\exp\left(\frac{(h_v W^Q)(h_u W^K)^\top}{\sqrt{d_k}}\right)}{\sum_{u'=1}^{n} \exp\left(\frac{(h_v W^Q)(h_{u'} W^K)^\top}{\sqrt{d_k}}\right)}$$

### 6.5.2 与 GAT 的关键对比

GAT 和 Transformer self-attention 都使用数据依赖的注意力权重，但机制不同：

| 特征 | GAT **[Velickovic et al. 2018]** | Transformer **[Vaswani et al. 2017]** |
|---|---|---|
| 兼容性函数 | $\mathrm{LeakyReLU}(a^\top [Wh_i \| Wh_j])$（加性） | $\frac{(h_i W^Q)(h_j W^K)^\top}{\sqrt{d_k}}$（乘性） |
| 图结构 | 给定稀疏图 | 完全图（或通过 mask 限制） |
| 复杂度 | $O(|E| \cdot d)$ | $O(n^2 \cdot d)$ |
| 位置信息 | 无（图同构不变） | 可选（sinusoidal 或 learned） |

### 6.5.3 通过 Mask 恢复稀疏图结构

对于非完全图，可以通过将非邻接节点的注意力 logit 设为 $-\infty$ 来恢复稀疏消息传递 **[Kool et al. 2019, Appendix A]**：

$$u_{ij} = \begin{cases} \frac{(h_i W^Q)(h_j W^K)^\top}{\sqrt{d_k}} & \text{if } (i,j) \in E \\ -\infty & \text{otherwise} \end{cases}$$

softmax 后，$\alpha_{ij} = 0$ 对所有 $(i,j) \notin E$，从而在 Transformer 框架中实现图感知的消息传递。

### 6.5.4 统一视角

$$\boxed{\text{Transformer} = \text{GNN on } K_n + \text{Positional Encoding} + \text{FFN} + \text{Residual/LayerNorm}}$$

所有空间 GNN（GCN, GAT, GraphSAGE, GIN）和 Transformer 都是 MPNN 框架的特例。差异在于：
- **图结构**：稀疏图 vs 完全图
- **注意力机制**：固定权重 vs 可学习权重 vs Q-K 点积
- **更新方式**：简单非线性 vs 残差+归一化+FFN

---

## Part 7: Over-Smoothing and Depth

### 7.1 Over-smoothing 问题

随着层数 $L$ 增加，MPNN中所有节点的表示趋向相同（over-smoothing）。

**直觉**：$L$ 层MPNN的感受野是 $L$-hop邻居。当 $L$ 大于图的直径时，所有节点"看到"整个图，表示趋同。

**数学分析**（以GCN为例）：

令 $\hat{A} = \tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$，则 $L$ 层GCN（去掉非线性）相当于：

$$H^{(L)} = \hat{A}^L X W^{(0)} \cdots W^{(L-1)}$$

$\hat{A}^L$ 的特征值为 $\hat{\lambda}_i^L$。由于 $|\hat{\lambda}_i| \leq 1$，当 $L \to \infty$，只有与 $\hat{\lambda} = 1$ 对应的特征向量（常数向量）存活，导致所有节点表示相同。

### 7.2 缓解方法

- **残差连接**：$h_v^{(l+1)} = h_v^{(l)} + \text{GNN-layer}(h_v^{(l)}, \ldots)$
- **JK-Net**：$h_v^{\text{final}} = \mathrm{AGG}(h_v^{(1)}, h_v^{(2)}, \ldots, h_v^{(L)})$
- **DropEdge**：训练时随机删除边
- **PairNorm / NodeNorm**：归一化节点表示

---

## Summary

| 方法 | Message $M$ | Aggregate $\bigoplus$ | Update $U$ | 特点 |
|---|---|---|---|---|
| GCN | $\frac{1}{\sqrt{d_v d_u}} W h_u$ | sum | $\sigma(\cdot)$ | 谱方法一阶近似 |
| GraphSAGE | $h_u$ | mean/max/LSTM | $\sigma(W[h_v \| m_v])$ | 采样+聚合 |
| GAT | $\alpha_{vu} W h_u$ | sum | $\sigma(\cdot)$ | 可学习注意力 |
| GIN | $h_u$ | sum | $\mathrm{MLP}((1+\epsilon)h_v + m_v)$ | 最大表达力 |
| **Transformer** | $\alpha_{vu}^{\mathrm{attn}} h_u W^V$ | sum | LN(res) + FFN | **完全图上的注意力** |

所有空间GNN都是MPNN的特例，表达力上界为1-WL test。谱方法通过图傅里叶变换定义卷积，空间方法直接在邻居上聚合，两者在GCN中建立了桥梁。Transformer self-attention 是完全图 $K_n$ 上的 MPNN，通过 mask 可适配任意图结构 **[Vaswani et al. 2017]** **[Kool et al. 2019]**。

---

## References

1. Gilmer, J., Schoenholz, S.S., Riley, P.F., Vinyals, O., & Dahl, G.E. (2017). Neural Message Passing for Quantum Chemistry. ICML.
2. Kipf, T.N. & Welling, M. (2017). Semi-Supervised Classification with Graph Convolutional Networks. ICLR.
3. Velickovic, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., & Bengio, Y. (2018). Graph Attention Networks. ICLR.
4. Hamilton, W.L., Ying, R., & Leskovec, J. (2017). Inductive Representation Learning on Large Graphs. NeurIPS.
5. Xu, K., Hu, W., Leskovec, J., & Jegelka, S. (2019). How Powerful are Graph Neural Networks? ICLR.
6. Defferrard, M., Bresson, X., & Vandergheynst, P. (2016). Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering. NeurIPS.
7. Vaswani, A., Shazeer, N., Parmar, N., et al. (2017). Attention Is All You Need. NeurIPS.
8. Kool, W., van Hoof, H., & Welling, M. (2019). Attention, Learn to Solve Routing Problems! ICLR.
