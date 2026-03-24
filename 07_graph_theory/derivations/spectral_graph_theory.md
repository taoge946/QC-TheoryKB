# Spectral Graph Theory

> **Tags**: `spectral-graph-theory`, `laplacian`, `graph-fourier-transform`, `chebyshev`, `gcn`, `cheeger`
>
> **Primary Source**: Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, P.S. Yu, *A Comprehensive Survey on Graph Neural Networks*, IEEE TNNLS (2021) **[Wu et al. 2021, §4 (Spectral-based ConvGNNs)]**

## Statement

推导谱图论的核心结果：图拉普拉斯的性质、图傅里叶变换、谱卷积到空间卷积的转换（ChebNet → GCN）、随机游走联系、Cheeger 不等式。这些构成图神经网络谱方法的数学基础 **[Wu et al. 2021, §4.1 (Spectral-based ConvGNNs)]**。

## Prerequisites

- 线性代数：实对称矩阵的谱分解、半正定性
- 基本图论：$G = (V, E)$, 邻接矩阵 $A$, 度矩阵 $D$
- 傅里叶分析的基本概念（经典卷积定理）
- 切比雪夫多项式基础

---

## Part 1: Graph Laplacian Properties

### 1.1 定义

给定无向图 $G = (V, E)$，$|V| = n$：

**Unnormalized Laplacian:**
$$L = D - A$$

**Normalized Laplacian:**
$$L_{\mathrm{sym}} = D^{-1/2} L D^{-1/2} = I - D^{-1/2} A D^{-1/2}$$

**Random Walk Laplacian:**
$$L_{\mathrm{rw}} = D^{-1} L = I - D^{-1} A = I - P$$

### 1.2 半正定性证明

**定理**：$L$ 是半正定的。

**证明**：对任意 $x \in \mathbb{R}^n$：

$$x^T L x = x^T (D - A) x = x^T D x - x^T A x$$

展开：

$$x^T D x = \sum_i d_i x_i^2, \quad x^T A x = \sum_{(i,j) \in E} 2 x_i x_j$$

（对无向图，每条边在 $x^T A x$ 中贡献 $x_i x_j + x_j x_i = 2x_i x_j$）

因此：

$$x^T L x = \sum_i d_i x_i^2 - \sum_{(i,j) \in E} 2 x_i x_j$$

由于 $d_i = \sum_{j: (i,j) \in E} 1$，将 $d_i x_i^2$ 按边展开：

$$\boxed{x^T L x = \sum_{(i,j) \in E} (x_i - x_j)^2 \geq 0}$$

**推论**：$L$ 的所有特征值 $\lambda_i \geq 0$。$\square$

### 1.3 零特征值

**定理**：$\lambda_1 = 0$，对应特征向量 $\mathbf{1} = (1, 1, \ldots, 1)^T$。

**证明**：$L \mathbf{1} = (D - A) \mathbf{1} = D \mathbf{1} - A \mathbf{1}$。由于 $A \mathbf{1}$ 的第 $i$ 分量为 $\sum_j A_{ij} = d_i = (D\mathbf{1})_i$，所以 $L \mathbf{1} = \mathbf{0}$。$\square$

### 1.4 连通分量与零特征值重数

**定理**：$L$ 的零特征值重数等于图 $G$ 的连通分量数 $k$。

**证明思路**：
- 若 $G$ 有 $k$ 个连通分量 $C_1, \ldots, C_k$，则 $L$ 可以排列为分块对角矩阵 $L = \mathrm{diag}(L_1, \ldots, L_k)$
- 每个 $L_i$ 有且仅有一个零特征值（其对应特征向量在 $C_i$ 上为常数，其他分量为 0）
- 因此总共 $k$ 个零特征值

### 1.5 Normalized Laplacian 的特征值范围

**定理**：$L_{\mathrm{sym}}$ 的特征值满足 $0 = \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n \leq 2$。

**证明**：

令 $y = D^{1/2} x$，则：

$$\frac{y^T L_{\mathrm{sym}} y}{y^T y} = \frac{x^T D^{1/2} L_{\mathrm{sym}} D^{1/2} x}{x^T D x} = \frac{x^T L x}{x^T D x} = \frac{\sum_{(i,j) \in E} (x_i - x_j)^2}{\sum_i d_i x_i^2}$$

**下界**：Rayleigh 商 $\geq 0$，由半正定性。

**上界**：对任意边 $(i,j)$：$(x_i - x_j)^2 \leq 2(x_i^2 + x_j^2)$（均值不等式）。

$$\sum_{(i,j) \in E} (x_i - x_j)^2 \leq 2\sum_{(i,j) \in E} (x_i^2 + x_j^2) = 2\sum_i d_i x_i^2$$

因此所有特征值 $\lambda_i \leq 2$。

**等号条件**：$\lambda_n = 2$ 当且仅当 $G$ 包含二部分量。$\square$

**[Wu et al. GNN Survey, §4.1]**：上述性质在 survey 的 "Background" 部分有简要叙述。

---

## Part 2: Graph Fourier Transform

### 2.1 从经典傅里叶到图傅里叶

**经典傅里叶变换**的特征函数是拉普拉斯算子 $\Delta = -\frac{d^2}{dx^2}$ 的特征函数：

$$-\frac{d^2}{dx^2} e^{i \omega x} = \omega^2 e^{i \omega x}$$

**类比**：图拉普拉斯 $L$ 的特征向量 $\{u_k\}$ 扮演 $e^{i\omega x}$ 的角色，特征值 $\lambda_k$ 扮演频率 $\omega^2$。

### 2.2 定义

$L_{\mathrm{sym}}$ 的谱分解：$L_{\mathrm{sym}} = U \Lambda U^T$

**图傅里叶变换**：

$$\hat{x} = U^T x$$

**逆变换**：

$$x = U \hat{x} = \sum_{k=1}^n \hat{x}_k u_k$$

**直觉**：
- $\hat{x}_k = u_k^T x$ 是信号 $x$ 在第 $k$ 个"频率"方向上的分量
- 小 $\lambda_k$ → 低频（对应图上平滑变化的信号）
- 大 $\lambda_k$ → 高频（对应图上剧烈变化的信号）

### 2.3 频率的物理意义

特征向量 $u_k$ 对应特征值 $\lambda_k$ 的 "振荡程度"：

$$\lambda_k = u_k^T L u_k = \sum_{(i,j) \in E} (u_{k,i} - u_{k,j})^2$$

$\lambda_k$ 越大，$u_k$ 在相邻节点间变化越剧烈 → 高频。

**[Wu et al. GNN Survey, §4.1]**：survey 定义了图傅里叶变换 $\mathscr{F}(x) = U^T x$ 并以此为基础定义谱卷积。

---

## Part 3: Spectral Convolution → Spatial Convolution

### 3.1 谱图卷积定义

类比经典卷积定理（频域乘法 = 时域卷积）：

$$x *_G g = \mathscr{F}^{-1}(\mathscr{F}(x) \odot \mathscr{F}(g)) = U(U^T x \odot U^T g)$$

令 $g_\theta = \mathrm{diag}(U^T g)$，简化为：

$$\boxed{x *_G g_\theta = U \, g_\theta(\Lambda) \, U^T x}$$

**[Wu et al. GNN Survey, §4.1, Eq. (2)]**

### 3.2 ChebNet: 多项式滤波器 (Defferrard et al., 2016)

**动机**：学习 $n$ 个频域参数不实际，且需要 $O(n^3)$ 特征分解。

用 $K$ 阶切比雪夫多项式近似滤波器：

$$g_\theta(\Lambda) \approx \sum_{k=0}^{K} \theta_k \, T_k(\tilde{\Lambda}), \quad \tilde{\Lambda} = \frac{2}{\lambda_{\max}} \Lambda - I$$

代入谱卷积：

$$x *_G g_\theta = U \left(\sum_{k=0}^{K} \theta_k \, T_k(\tilde{\Lambda})\right) U^T x = \sum_{k=0}^{K} \theta_k \, U T_k(\tilde{\Lambda}) U^T x$$

**关键引理**：$T_k(\tilde{L}_{\mathrm{sym}}) = U T_k(\tilde{\Lambda}) U^T$

**证明**（归纳法）：
- $k=0$：$T_0(\tilde{L}) = I = U I U^T = U T_0(\tilde{\Lambda}) U^T$ ✓
- $k=1$：$T_1(\tilde{L}) = \tilde{L} = U \tilde{\Lambda} U^T = U T_1(\tilde{\Lambda}) U^T$ ✓
- 归纳步：假设 $T_{k-1}(\tilde{L}) = U T_{k-1}(\tilde{\Lambda}) U^T$ 和 $T_{k-2}(\tilde{L}) = U T_{k-2}(\tilde{\Lambda}) U^T$

  $$T_k(\tilde{L}) = 2\tilde{L} T_{k-1}(\tilde{L}) - T_{k-2}(\tilde{L})$$
  $$= 2 U\tilde{\Lambda}U^T \cdot U T_{k-1}(\tilde{\Lambda}) U^T - U T_{k-2}(\tilde{\Lambda}) U^T$$
  $$= U (2\tilde{\Lambda} T_{k-1}(\tilde{\Lambda}) - T_{k-2}(\tilde{\Lambda})) U^T = U T_k(\tilde{\Lambda}) U^T \quad \square$$

因此 ChebNet 卷积为：

$$\boxed{x *_G g_\theta = \sum_{k=0}^{K} \theta_k \, T_k(\tilde{L}_{\mathrm{sym}}) \, x}$$

**[Wu et al. GNN Survey, §4.1, Eq. (5)]**

**空间局部性**：$T_k(\tilde{L})$ 是 $\tilde{L}$ 的 $k$ 次多项式。由于 $L$ 的非零模式与 $A$ 一致（加上对角），$L^k$ 的 $(i,j)$ 元素只在 $i, j$ 之间距离 $\leq k$ 时非零。因此 $K$ 阶 ChebNet 只聚合 $K$-hop 邻居的信息。

### 3.3 GCN: 一阶近似 (Kipf & Welling, 2017)

取 $K = 1$，$\lambda_{\max} \approx 2$：

$$\tilde{L} = L - I, \quad T_0(\tilde{L}) = I, \quad T_1(\tilde{L}) = L - I$$

$$x *_G g_\theta = \theta_0 x + \theta_1 (L_{\mathrm{sym}} - I) x = \theta_0 x - \theta_1 D^{-1/2} A D^{-1/2} x$$

令 $\theta = \theta_0 = -\theta_1$（减少参数）：

$$x *_G g_\theta = \theta (I + D^{-1/2} A D^{-1/2}) x$$

**Renormalization trick**：$I + D^{-1/2} A D^{-1/2}$ 的特征值在 $[0, 2]$，多层堆叠会导致数值不稳定（梯度爆炸/消失）。

**解决方案**：令 $\tilde{A} = A + I$，$\tilde{D}_{ii} = \sum_j \tilde{A}_{ij} = d_i + 1$：

$$\tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2} = \tilde{D}^{-1/2}(A + I)\tilde{D}^{-1/2}$$

这等价于将 $I + D^{-1/2}AD^{-1/2}$ 重新归一化，使特征值限制在 $[-1, 1]$ 附近。

多通道版本（GCN layer）：

$$\boxed{H^{(l+1)} = \sigma\!\left(\tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2} H^{(l)} W^{(l)}\right)}$$

**[Wu et al. GNN Survey, §4.1, Eq. (6)-(8)]**

### 3.4 谱 → 空间的桥梁

GCN 的逐节点写法：

$$h_v^{(l+1)} = \sigma\!\left(\sum_{u \in \mathcal{N}(v) \cup \{v\}} \frac{1}{\sqrt{\tilde{d}_v \tilde{d}_u}} W^{(l)} h_u^{(l)}\right)$$

这正是一个消息传递操作：
- **Message**: $m_{u \to v} = \frac{1}{\sqrt{\tilde{d}_v \tilde{d}_u}} W h_u$
- **Aggregate**: sum
- **Update**: $\sigma(\cdot)$

因此 GCN（从谱方法推导）等价于空间聚合方法。这是 **[Wu et al. GNN Survey, §4.1]** 的核心观察。

---

## Part 4: Connection to Random Walks

### 4.1 转移概率矩阵

$$P = D^{-1} A$$

$P_{ij} = A_{ij} / d_i$ 表示从节点 $i$ 随机游走到邻居 $j$ 的概率。

### 4.2 拉普拉斯与随机游走

$$L_{\mathrm{rw}} = I - P = D^{-1}L$$

$L_{\mathrm{rw}}$ 和 $L_{\mathrm{sym}}$ 有相同的特征值（因为 $D^{-1/2} L_{\mathrm{sym}} D^{1/2} = D^{-1}L = L_{\mathrm{rw}}$，相似变换保持特征值）。

### 4.3 扩散与低通滤波

多层 GCN（去掉非线性）相当于：

$$H^{(L)} = \hat{A}^L X W^{(0)} \cdots W^{(L-1)}$$

其中 $\hat{A} = \tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}$。

$\hat{A}$ 的特征值 $\hat{\lambda}_i = 1 - \lambda_i$（$\lambda_i$ 是 $L_{\mathrm{sym}}$ 的特征值）。

$\hat{A}^L$ 的特征值为 $(1 - \lambda_i)^L$：
- $\lambda_i = 0$（最低频）：$(1-0)^L = 1$，完全保留
- $\lambda_i$ 大（高频）：$(1-\lambda_i)^L \to 0$，被抑制

**结论**：多层 GCN 是低通滤波器。这解释了 over-smoothing：当 $L$ 足够大，只有 $\lambda = 0$ 对应的常数特征向量存活，所有节点表示趋同。

**[Wu et al. GNN Survey, §7]** 讨论了 GNN 的深度问题。

### 4.4 DCNN: 扩散卷积

DCNN (Atwood & Towsley, 2016) 直接使用转移矩阵的幂：

$$H^{(k)} = f(W^{(k)} \odot P^k X)$$

$P^k$ 的 $(i,j)$ 元素是从 $i$ 经 $k$ 步游走到 $j$ 的概率。

DGC 取所有步的和：$H = \sum_{k=0}^{K} f(P^k X W^{(k)})$，近似扩散核的幂级数。

**[Wu et al. GNN Survey, §4.2]**

---

## Part 5: Cheeger Inequality and Graph Connectivity

### 5.1 Cheeger 常数

$$h(G) = \min_{\substack{S \subset V \\ 0 < |S| \leq n/2}} \frac{|\partial S|}{|S|}$$

其中 $|\partial S| = |\{(u,v) \in E : u \in S, v \notin S\}|$ 是 $S$ 的边界大小。

（另一种定义使用 $\mathrm{vol}(S)$ 代替 $|S|$，对应 normalized Cheeger 常数。）

### 5.2 Cheeger 不等式

**定理 (Cheeger, 1970; Alon & Milman, 1985)**：对 $d$-正则图：

$$\frac{\lambda_2}{2} \leq h(G) \leq \sqrt{2\lambda_2}$$

**对一般图** (normalized version)：令 $\phi(G) = \min_{S} \frac{|\partial S|}{\min(\mathrm{vol}(S), \mathrm{vol}(\bar{S}))}$，则：

$$\frac{\lambda_2}{2} \leq \phi(G) \leq \sqrt{2\lambda_2}$$

### 5.3 意义

**下界** $h(G) \geq \lambda_2 / 2$：若 $\lambda_2$ 大（代数连通度高），则图难以被小割分开 → 信息流通好 → GNN 传播高效。

**上界** $h(G) \leq \sqrt{2\lambda_2}$：若 $\lambda_2$ 小，则存在"瓶颈"，图几乎分裂 → over-squashing 问题（信息经过瓶颈时被压缩）。

### 5.4 证明下界（$h(G) \geq \lambda_2/2$, $d$-正则图）

对任意 $S \subset V$，$|S| \leq n/2$，定义指示向量：

$$x_i = \begin{cases} 1 & i \in S \\ 0 & i \notin S \end{cases}$$

由 Rayleigh 商：

$$\lambda_2 \leq \frac{x^T L x}{x^T x} = \frac{\sum_{(i,j) \in E} (x_i - x_j)^2}{\sum_i x_i^2} = \frac{|\partial S|}{|S|}$$

（对 $d$-正则图需调整为 $\lambda_2 d$ 的 Rayleigh 商，此处给出定性论证。）

精确证明需要使用最优的测试向量并仔细处理归一化，参见 Chung (1997)。

### 5.5 与 GNN 的关联

- **Spectral gap** ($\lambda_2$) 决定了 GNN 信息传播的效率
- 图的 Cheeger 常数越大，消息传递越不容易出现 over-squashing
- 近期研究（Topping et al., 2022, "Understanding over-squashing and bottlenecks on graphs via curvature"）利用 Cheeger 不等式分析 GNN 的几何瓶颈

---

## Summary

| 概念 | 核心公式 | GNN 中的角色 |
|------|---------|-------------|
| Graph Laplacian $L$ | $L = D - A$, $x^T L x = \sum_{(i,j)}(x_i-x_j)^2$ | 谱方法的数学基础 |
| 图傅里叶变换 | $\hat{x} = U^T x$ | 定义频域滤波 |
| ChebNet | $\sum_k \theta_k T_k(\tilde{L}) x$ | $K$-hop 局部化滤波器 |
| GCN | $\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2} H W$ | 一阶近似 = 空间聚合 |
| 随机游走 | $P = D^{-1}A$ | 扩散卷积 (DCNN) |
| Cheeger 不等式 | $\lambda_2/2 \leq h(G) \leq \sqrt{2\lambda_2}$ | 连通性 & over-squashing |

**关键洞察**：谱方法（频域滤波）与空间方法（邻居聚合）在 GCN 中统一。切比雪夫近似使谱卷积具有空间局部性，一阶近似直接等价于加权邻居求和。

---

## References

1. Chung, F.R.K. (1997). Spectral Graph Theory. AMS.
2. Shuman, D.I., Narang, S.K., Frossard, P., Ortega, A., & Vandergheynst, P. (2013). The Emerging Field of Signal Processing on Graphs. IEEE Signal Processing Magazine.
3. Defferrard, M., Bresson, X., & Vandergheynst, P. (2016). Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering. NeurIPS.
4. Kipf, T.N. & Welling, M. (2017). Semi-Supervised Classification with Graph Convolutional Networks. ICLR.
5. Wu, Z., Pan, S., Chen, F., Long, G., Zhang, C., & Yu, P.S. (2020). A Comprehensive Survey on Graph Neural Networks. IEEE TNNLS.
6. Bruna, J., Zaremba, W., Szlam, A., & LeCun, Y. (2014). Spectral Networks and Locally Connected Networks on Graphs. ICLR.
7. Cheeger, J. (1970). A lower bound for the smallest eigenvalue of the Laplacian. Problems in Analysis.
8. Topping, J., Di Giovanni, F., Chamberlain, B.P., Dong, X., & Bronstein, M.M. (2022). Understanding over-squashing and bottlenecks on graphs via curvature. ICLR.
