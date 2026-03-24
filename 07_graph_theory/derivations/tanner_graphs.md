# Tanner Graphs: From Classical Codes to Quantum Error Correction

> **Tags**: `tanner-graph`, `ldpc`, `qec`, `css-code`, `belief-propagation`, `factor-graph`, `surface-code`
>
> **References**: Tanner (1981); QEC context from **[Gottesman 1997, Ch.3, §3.4]** and **[Bombin, §2]**

## Statement

推导 Tanner 图的定义与性质：经典线性码的 Tanner 图表示、因子图与置信传播、量子 CSS 码的 Tanner 图 **[Gottesman 1997, Ch.3]**、LDPC 码的稀疏性条件 **[Bombin, §2]**、以及与 QEC 解码的联系。Tanner 图是连接图论和纠错码理论的核心桥梁。

## Prerequisites

- 线性代数（$\mathbb{F}_2$ 上的矩阵运算）
- 经典纠错码基础：线性码、校验矩阵、生成矩阵
- 二部图基本概念
- 概率推理基础（用于置信传播）

---

## Part 1: Tanner Graph for Classical Linear Codes

### 1.1 线性码回顾

**$[n, k, d]$ 线性码** $\mathcal{C}$：
- $n$ 个比特的码字空间
- $k$ 维码空间（$2^k$ 个码字）
- 最小距离 $d$（可纠正 $\lfloor(d-1)/2\rfloor$ 个错误）
- **校验矩阵** $H \in \mathbb{F}_2^{m \times n}$：$\mathcal{C} = \ker(H) = \{x \in \mathbb{F}_2^n : Hx = 0\}$
- **生成矩阵** $G \in \mathbb{F}_2^{k \times n}$：$\mathcal{C} = \mathrm{rowspace}(G)$
- 关系：$HG^T = 0$（所有码字满足校验条件）

### 1.2 Tanner 图定义

**定义 (Tanner, 1981)**：给定校验矩阵 $H \in \mathbb{F}_2^{m \times n}$，其 Tanner 图 $\mathcal{T}(H)$ 是**二部图** $G = (V_b \cup V_c, E)$：

- **比特节点** (variable nodes)：$V_b = \{b_1, b_2, \ldots, b_n\}$，对应 $n$ 个码比特
- **校验节点** (check nodes)：$V_c = \{c_1, c_2, \ldots, c_m\}$，对应 $m$ 个校验方程
- **边**：$(b_j, c_i) \in E \Leftrightarrow H_{ij} = 1$

**直觉**：校验节点 $c_i$ 连接参与第 $i$ 个校验方程的所有比特。

### 1.3 图的度与码的参数

- **比特节点 $b_j$ 的度** $d_{b_j} = \sum_{i=1}^m H_{ij}$（$b_j$ 参与多少个校验）
- **校验节点 $c_i$ 的度** $d_{c_i} = \sum_{j=1}^n H_{ij}$（第 $i$ 个校验涉及多少比特）
- **边总数**：$|E| = \sum_{ij} H_{ij}$

### 1.4 例子：[7,4,3] Hamming 码

$$H = \begin{pmatrix} 1 & 0 & 0 & 1 & 1 & 0 & 1 \\ 0 & 1 & 0 & 1 & 0 & 1 & 1 \\ 0 & 0 & 1 & 0 & 1 & 1 & 1 \end{pmatrix}$$

Tanner 图：3 个校验节点，7 个比特节点。每个校验节点连接 4 个比特节点（度 4），每个比特节点连接 1-3 个校验节点。

### 1.5 码距与图的 girth 的关系

**定理**：Tanner 图的 **girth**（最短环长度）$g$ 与码距 $d$ 的关系：

$$d \geq \left\lfloor \frac{g}{2} \right\rfloor + 1 \quad \text{（对某些特殊构造）}$$

更一般地：大 girth $\Rightarrow$ 局部树状结构 $\Rightarrow$ BP 解码效果好。

**直觉**：短环使 BP 传递的消息高度相关（违反独立假设），降低解码性能。

---

## Part 2: Factor Graphs and Belief Propagation

### 2.1 因子图 (Factor Graph)

Tanner 图是**因子图**的特例。因子图表示函数的因式分解：

$$p(x_1, \ldots, x_n) = \frac{1}{Z} \prod_{a} f_a(x_{\partial a})$$

其中 $f_a$ 是因子函数，$x_{\partial a}$ 是与因子 $a$ 相关的变量子集。

**对于线性码**：
- 变量 $x_j \in \{0, 1\}$：码比特
- 因子 $f_i(x_{\partial i})$：校验约束，$f_i = \mathbb{1}[\bigoplus_{j: H_{ij}=1} x_j = 0]$
- 目标：给定噪声观测 $y$，求后验 $p(x | y)$

### 2.2 Belief Propagation (BP) / Sum-Product Algorithm

BP 在因子图上传递消息，近似计算边际概率。

**比特节点 $b_j$ → 校验节点 $c_i$ 的消息**：

$$\mu_{b_j \to c_i}(x_j) = p(y_j | x_j) \prod_{i' \in \mathcal{N}(b_j) \setminus \{c_i\}} \hat{\mu}_{c_{i'} \to b_j}(x_j)$$

**校验节点 $c_i$ → 比特节点 $b_j$ 的消息**：

$$\hat{\mu}_{c_i \to b_j}(x_j) = \sum_{x_{\partial i \setminus j}} f_i(x_{\partial i}) \prod_{j' \in \mathcal{N}(c_i) \setminus \{b_j\}} \mu_{b_{j'} \to c_i}(x_{j'})$$

**边际估计**：

$$\hat{p}(x_j | y) \propto p(y_j | x_j) \prod_{i \in \mathcal{N}(b_j)} \hat{\mu}_{c_i \to b_j}(x_j)$$

### 2.3 对数似然比 (LLR) 形式

定义 LLR：$\ell_j = \log \frac{p(x_j = 0 | y_j)}{p(x_j = 1 | y_j)}$

BP 更新（BSC 信道上的简化）：

**比特 → 校验**：
$$\lambda_{b_j \to c_i} = \ell_j + \sum_{i' \in \mathcal{N}(b_j) \setminus \{c_i\}} \Lambda_{c_{i'} \to b_j}$$

**校验 → 比特**（使用 $\tanh$ 规则）：
$$\tanh\!\left(\frac{\Lambda_{c_i \to b_j}}{2}\right) = \prod_{j' \in \mathcal{N}(c_i) \setminus \{b_j\}} \tanh\!\left(\frac{\lambda_{b_{j'} \to c_i}}{2}\right)$$

### 2.4 BP 的收敛条件

**定理**：若 Tanner 图是**树**（无环），则 BP 在有限步后精确收敛到真实边际概率。

**证明**：在树上，从叶节点向根传递的消息互相独立（不存在信息循环），因此 BP 等价于精确推理。

**含环图上**：BP 是近似算法。短环导致消息相关性，降低近似质量。LDPC 码的大 girth 设计正是为了缓解此问题。

---

## Part 3: LDPC Codes as Sparse Tanner Graphs

### 3.1 LDPC 码定义

**Low-Density Parity-Check (LDPC) 码** (Gallager, 1962)：校验矩阵 $H$ 是稀疏的。

**$(d_v, d_c)$-正则 LDPC 码**：
- 每个比特节点度恰好为 $d_v$（参与 $d_v$ 个校验）
- 每个校验节点度恰好为 $d_c$（每个校验涉及 $d_c$ 个比特）
- $d_v, d_c = O(1)$（不随 $n$ 增长）

**码率**：$R = k/n \geq 1 - d_v/d_c$（对正则码）

### 3.2 LDPC 码的优势

**信息论性能**：
- LDPC + BP 解码可以**逼近 Shannon 极限**（容量达到码）
- 在各种信道模型下性能优异

**计算优势**（来自 Tanner 图的稀疏性）：
- BP 每次迭代复杂度 $O(|E|) = O(n \cdot d_v)$（线性于码长）
- 不需要矩阵求逆或高次运算
- 可高度并行化

### 3.3 度分布优化

**非正则 LDPC 码**：通过优化度分布 $(\lambda(x), \rho(x))$ 来逼近信道容量。

$$\lambda(x) = \sum_i \lambda_i x^{i-1}, \quad \rho(x) = \sum_i \rho_i x^{i-1}$$

其中 $\lambda_i$ ($\rho_i$) 是度为 $i$ 的比特（校验）节点在边中的比例。

**密度进化 (Density Evolution)**：在 $n \to \infty$ 时追踪 BP 消息的分布演化，用于分析阈值和优化度分布。

---

## Part 4: Tanner Graphs for Quantum CSS Codes

### 4.1 CSS 码回顾

**Calderbank-Shor-Steane (CSS) 码** $[[n, k, d]]$：

由两个经典线性码 $\mathcal{C}_X$ 和 $\mathcal{C}_Z$ 构造：
- $H_X \in \mathbb{F}_2^{m_X \times n}$：$X$-stabilizer 的校验矩阵
- $H_Z \in \mathbb{F}_2^{m_Z \times n}$：$Z$-stabilizer 的校验矩阵

**CSS 条件**（stabilizer 对易）：

$$\boxed{H_X H_Z^T = 0}$$

即 $\mathcal{C}_Z^\perp \subseteq \mathcal{C}_X$（或等价地 $\mathcal{C}_X^\perp \subseteq \mathcal{C}_Z$）。

**逻辑量子比特数**：$k = n - \mathrm{rank}(H_X) - \mathrm{rank}(H_Z)$

### 4.2 量子 Tanner 图

CSS 码对应**两个** Tanner 图：

1. **$X$-Tanner 图** $\mathcal{T}(H_X)$：检测 $Z$-错误
   - 比特节点：$n$ 个物理量子比特
   - 校验节点：$m_X$ 个 $X$-stabilizer

2. **$Z$-Tanner 图** $\mathcal{T}(H_Z)$：检测 $X$-错误
   - 比特节点：$n$ 个物理量子比特
   - 校验节点：$m_Z$ 个 $Z$-stabilizer

**CSS 条件的图论意义**：$H_X H_Z^T = 0$ 意味着 $\mathcal{T}(H_X)$ 的每个校验节点的邻域与 $\mathcal{T}(H_Z)$ 的每个校验节点的邻域有**偶数个**公共比特节点。

### 4.3 表面码的 Tanner 图

**Toric code** $[[2n^2, 2, n]]$ 在 $n \times n$ 环面上：

- 物理量子比特在边上（$2n^2$ 条边）
- $X$-stabilizer 在面上（面周围 4 条边的乘积）
- $Z$-stabilizer 在顶点上（顶点周围 4 条边的乘积）

Tanner 图是一个**平面**二部图（局部结构简单），这使得 MWPM 解码高效。

**Planar code**（有边界的表面码）：
- 边界处 stabilizer 度为 2 或 3
- 其他地方度为 4
- 正是这种规则的局部结构使表面码成为最实用的量子纠错码之一

### 4.4 量子 LDPC 码的 Tanner 图

**Quantum LDPC 码**：$H_X$ 和 $H_Z$ 都是稀疏矩阵。

$$\max_i \sum_j (H_X)_{ij} \leq w_X, \quad \max_j \sum_i (H_X)_{ij} \leq w_X'$$

（对 $H_Z$ 类似）其中 $w_X, w_X'$ 是常数。

**关键挑战**：在满足 $H_X H_Z^T = 0$ 的约束下构造好的 LDPC 码比经典情形困难得多。

**近期突破**：
- **Good quantum LDPC codes** (Panteleev & Kalachev, 2022; Leverrier & Zemor, 2022)：$[[n, \Theta(n), \Theta(n)]]$（线性码率和距离）
- 这些码的 Tanner 图具有**expander 性质**，保证码距线性增长

---

## Part 5: Connection to QEC Decoding

### 5.1 Syndrome 和解码问题

物理错误 $e \in \mathbb{F}_2^n$ 产生 syndrome：

$$s_X = H_X e \pmod{2}, \quad s_Z = H_Z e \pmod{2}$$

（$s_X$ 检测 $Z$-错误，$s_Z$ 检测 $X$-错误）

**解码问题**：给定 syndrome $s$，找到错误估计 $\hat{e}$ 使得 $H\hat{e} = s$ 且 $\hat{e}$ 与真实错误 $e$ 等价（差一个 stabilizer）。

### 5.2 BP 解码

在 Tanner 图上运行 BP：
- 初始化：根据物理错误模型设定先验 LLR
- 迭代：比特节点和校验节点交替传递消息
- 判决：根据后验 LLR 判断每个比特是否有错误

**优势**：$O(n)$ 复杂度（稀疏 Tanner 图），可并行
**劣势**：短环导致 BP 在量子码上表现不佳（量子码的 Tanner 图通常环更短，因为 CSS 约束增加了结构关联）

### 5.3 MWPM 解码（表面码）

表面码的特殊结构允许使用 MWPM：

1. Syndrome 标记的校验节点构成**匹配图**的节点
2. 两个 syndrome 节点之间的边权 = 对数似然比路径权重
3. MWPM 找到最优配对
4. 沿匹配路径翻转比特

**复杂度**：$O(n^3)$，Sparse Blossom (Higgott & Gidney, 2023) 实际中接近线性。

### 5.4 GNN-based 解码

GNN 解码器的思路：将 Tanner 图作为 GNN 的输入图，syndrome 作为节点特征，学习解码映射。

**架构**：
- 节点 = 比特节点 + 校验节点
- 初始特征 = syndrome 值 + 先验错误概率
- 消息传递 = 在 Tanner 图的边上进行
- 输出 = 每个比特节点的错误概率

**本质联系**：BP 解码就是一种固定参数的消息传递；GNN 解码器是参数可学习的消息传递 → GNN 是 BP 的推广。

**局限性**（参见 `wl_test_expressiveness.md`）：
- MPNN 的表达力受限于 1-WL
- 量子码的 degenerate 错误需要全局推理
- 短环（尤其在量子码中）对 MPNN 的影响尚不完全理解

---

## Summary

| 概念 | 关键公式/结构 | 应用 |
|------|-------------|------|
| Tanner 图 | $H_{ij}=1 \Leftrightarrow (b_j, c_i) \in E$ | 码的图形表示 |
| BP 解码 | $\mu_{b \to c}, \hat{\mu}_{c \to b}$ 交替更新 | 经典/量子 LDPC 解码 |
| LDPC 稀疏性 | $d_v, d_c = O(1)$ | $O(n)$ 解码复杂度 |
| CSS Tanner 图 | $H_X H_Z^T = 0$, 两个 Tanner 图 | 量子 CSS 码 |
| 表面码 | 平面 Tanner 图, 度 $\leq 4$ | 最实用的 QEC 码 |
| GNN 解码 | 在 Tanner 图上学习消息传递 | BP 的可学习推广 |

**核心洞察**：
1. Tanner 图将代数编码理论（校验矩阵）转化为图论问题
2. 稀疏 Tanner 图（LDPC）$\Leftrightarrow$ 高效解码（BP 线性复杂度）
3. 量子码的 CSS 条件对 Tanner 图施加了额外的结构约束
4. GNN 解码器本质上是在 Tanner 图上的可学习消息传递，是 BP 的自然推广
5. 好的量子 LDPC 码需要 Tanner 图具有 expander 性质

---

## References

1. Tanner, R.M. (1981). A recursive approach to low complexity codes. IEEE Trans. Inform. Theory.
2. Gallager, R.G. (1962). Low-Density Parity-Check Codes. MIT Press.
3. Calderbank, A.R. & Shor, P.W. (1996). Good quantum error-correcting codes exist. Phys. Rev. A.
4. Steane, A.M. (1996). Error correcting codes in quantum theory. Phys. Rev. Lett.
5. Dennis, E., Kitaev, A., Landahl, A., & Preskill, J. (2002). Topological quantum memory. J. Math. Phys.
6. Panteleev, P. & Kalachev, G. (2022). Asymptotically good quantum and locally testable classical LDPC codes. STOC.
7. Leverrier, A. & Zemor, G. (2022). Quantum Tanner codes. FOCS.
8. Higgott, O. & Gidney, C. (2023). Sparse Blossom: correcting a million errors per core second. arXiv:2303.15933.
9. Richardson, T.J. & Urbanke, R.L. (2001). The capacity of low-density parity-check codes under message-passing decoding. IEEE Trans. Inform. Theory.
10. Kschischang, F.R., Frey, B.J., & Loeliger, H.A. (2001). Factor graphs and the sum-product algorithm. IEEE Trans. Inform. Theory.
