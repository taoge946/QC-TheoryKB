# Decoding Problem and Main Approaches

> **Tags**: `decoder`, `qec`, `mwpm`, `belief-propagation`, `maximum-likelihood`

## Statement

解码问题是量子纠错的核心计算任务：给定 syndrome 测量结果 $\mathbf{s}$，找到一个恢复操作 $R$ 使得 $RE$（$E$ 是实际错误）不构成逻辑错误。理想情况下，解码器应当最大化纠错成功概率。本文推导最大似然解码（ML）、最小权重完美匹配（MWPM）、置信传播（BP）和 Union-Find 解码器的数学公式。

## Prerequisites

- **稳定子码**：[stabilizer_formalism.md]
- **表面码**：[surface_code_basics.md]
- **概率论**：条件概率、贝叶斯定理
- **图论**：图、匹配、最短路径

---

## Roffe's Practical Perspective on Decoding **[Roffe, §5.1]**

> **[Roffe, QEC Introductory Guide, §5.1]**: Measuring the stabilizers of an $[[n,k,d]]$ code will produce an $m$-bit syndrome where $m = n - k$. As a result, there are $2^m$ possible syndromes for each code. For small codes, lookup-tables can exhaustively list the best recovery operation for each syndrome. However, such a decoding strategy rapidly becomes impractical: the distance-five surface code $[[41,1,5]]$ produces syndromes of length $m = 40$, and would therefore need a lookup table of size $2^{40} \approx 10^{12}$.

> **[Roffe, §5.1]**: In place of lookup tables, large-scale quantum error correction codes use approximate inference techniques to determine the most likely error given a syndrome $S$. For surface codes, a technique known as **minimum weight perfect matching (MWPM)** can be used for decoding, which works by identifying error chains between positive syndrome measurements.

---

## Part 1: The Decoding Problem **[Gottesman, §3.2; Roffe, §5.1; Bacon, p.23-25]**

### 形式化定义

给定一个 $[[n, k, d]]$ 稳定子码，稳定子群 $\mathcal{S} = \langle g_1, \ldots, g_{n-k} \rangle$。

**输入**：syndrome 向量 $\mathbf{s} = (s_1, s_2, \ldots, s_{n-k}) \in \mathbb{F}_2^{n-k}$

**输出**：恢复算子 $R \in \mathcal{G}_n$，使得 $\mathbf{s}(R) = \mathbf{s}$

**成功条件**：$RE \in \mathcal{S}$（即 $RE$ 是一个稳定子，作用在码空间上等于恒等）

**失败条件**：$RE \in N(\mathcal{S}) \setminus \mathcal{S}$（即 $RE$ 是一个非平凡逻辑算子，会改变编码信息）

> **[Gottesman thesis, §3.2]**: The error syndrome $f(E) = (f_{M_1}(E), \ldots, f_{M_{n-k}}(E))$ where $f_M(E) = 0$ if $[M, E] = 0$ and $f_M(E) = 1$ if $\{M, E\} = 0$. Then $f(E)$ is some $(n-k)$-bit binary number which is $0$ iff $E \in N(S)$. For a nondegenerate code, $f(E)$ is different for each correctable error $E$.

> **[Roffe, §3.5]**: The decoding step fails if $\mathcal{R}E = L$ where $L$ is a logical operator of the code. The frequency with which the decoder fails in this way gives the logical error rate $p_L$. The logical error rate depends heavily on the decoder used, and can be determined by simulating stabilizer code cycles with errors sampled from a noise model.

**关键观察**：同一个 syndrome 对应的错误不唯一。所有满足 $\mathbf{s}(E) = \mathbf{s}$ 的错误 $E$ 构成一个**陪集** $E_0 \cdot \mathcal{S} \cdot N(\mathcal{S})$，其中 $E_0$ 是该陪集的任意代表元。解码器不需要找到精确的 $E$，只需要找到与 $E$ 在同一个**逻辑等价类**中的 $R$。

### 逻辑等价类

两个错误 $E$ 和 $E'$ 是逻辑等价的，当且仅当 $E'E^{-1} \in \mathcal{S}$（它们只差一个稳定子）。

对于 CSS 码（如表面码），由于 $X$ 和 $Z$ 错误独立处理，解码问题分解为两个独立的经典解码问题。

---

## Part 2: Maximum Likelihood Decoding (ML) **[Dennis et al. 2002, §3.3, Eq.(6); Bacon, p.24-25]**

### 数学公式

最大似然解码器（也称为最优解码器）选择使后验概率最大的**逻辑等价类**。

**给定**：噪声模型 $\Pr(E)$（每个 Pauli 错误 $E$ 的先验概率），syndrome $\mathbf{s}$。

**ML 解码器**选择逻辑类 $\bar{L}$ 使得：

$$\hat{L} = \arg\max_{\bar{L}} \Pr(\bar{L} \mid \mathbf{s}) = \arg\max_{\bar{L}} \sum_{E \in \bar{L}, \; \mathbf{s}(E) = \mathbf{s}} \Pr(E)$$

其中求和遍历逻辑类 $\bar{L}$ 中所有与 syndrome $\mathbf{s}$ 一致的错误。

**展开**：对于一个 $[[n, k, d]]$ 码，normalizer 中的元素 $N(\mathcal{S})$ 可以按逻辑类分组。对于 $k = 1$ 的码（如平面表面码），有 4 个逻辑类（对应 $\bar{I}, \bar{X}, \bar{Y}, \bar{Z}$）。对于 CSS 码，进一步简化为只需要区分 $\bar{I}$ 和 $\bar{X}$（对 $Z$ 错误），以及 $\bar{I}$ 和 $\bar{Z}$（对 $X$ 错误）。

**独立去极化噪声**：每个量子比特独立地以概率 $p$ 出错（$X, Y, Z$ 各 $p/3$），则：

$$\Pr(E) = \left(\frac{p}{3}\right)^{\text{wt}(E)} (1-p)^{n - \text{wt}(E)}$$

$$= (1-p)^n \left(\frac{p}{3(1-p)}\right)^{\text{wt}(E)}$$

取对数：

$$\log \Pr(E) = n \log(1-p) + \text{wt}(E) \log\frac{p}{3(1-p)}$$

因此 ML 解码变为：

$$\hat{L} = \arg\max_{\bar{L}} \sum_{E \in \bar{L}, \; \mathbf{s}(E) = \mathbf{s}} \left(\frac{p}{3(1-p)}\right)^{\text{wt}(E)}$$

### 计算复杂度

ML 解码是 **#P-hard** 问题（对于一般的稳定子码）。直观原因：需要对指数多的错误模式求和。但对于特定的码族（如表面码），存在高效的近似算法。

---

## Part 3: Minimum Weight Perfect Matching (MWPM) **[Dennis et al. 2002, §3.5; Roffe, §5.1]**

### 物理动机

对于表面码上的独立噪声，低权重错误比高权重错误更可能发生。MWPM 解码器寻找与 syndrome 一致的最小权重错误，作为 ML 解码的近似。

### 数学构造

**Step 1: Construct the syndrome graph**

对于表面码的 $Z$ 错误解码（检测 $X$ 型稳定子）：

给定 syndrome $\mathbf{s}$，令 $D = \{v : s_v = 1\}$ 为所有 syndrome 缺陷的集合（syndrome 非零的顶点/plaquette）。

syndrome 缺陷总是成对出现（因为每条错误链有两个端点），所以 $|D|$ 是偶数。

构造完全图 $G_D = (D, E_D)$：
- 顶点集：所有 syndrome 缺陷 $D$
- 对于每对缺陷 $(u, v)$，边权重为它们之间最短错误链的长度

**Step 2: Edge weights from noise model**

对于独立 bit-flip 噪声（每个量子比特以概率 $p$ 翻转），两个缺陷 $u, v$ 之间的边权重：

$$w(u, v) = \text{dist}(u, v) \cdot \log\frac{1-p}{p}$$

其中 $\text{dist}(u, v)$ 是 $u$ 和 $v$ 之间在格子上的曼哈顿距离（最短路径长度）。

更一般地，对于非均匀噪声，权重为：

$$w(u,v) = -\log \Pr(\text{most likely error chain from } u \text{ to } v)$$

$$= \sum_{e \in \text{path}(u,v)} \log\frac{1-p_e}{p_e}$$

其中 $p_e$ 是边 $e$ 上的错误概率。

**Step 3: Handle boundaries (planar code)**

在平面码中，syndrome 缺陷也可以与边界配对（一条错误链从缺陷延伸到边界）。为此，添加**虚拟节点**（boundary node）$b$，对每个缺陷 $v \in D$：

$$w(v, b) = \text{dist}(v, \text{nearest boundary})  \cdot \log\frac{1-p}{p}$$

**Step 4: Find minimum weight perfect matching**

在加权完全图 $G_D$（包含虚拟边界节点）上找最小权重完美匹配 $M^*$：

$$M^* = \arg\min_{M \in \text{PM}(G_D)} \sum_{(u,v) \in M} w(u,v)$$

其中 $\text{PM}(G_D)$ 是 $G_D$ 上所有完美匹配的集合。

**Step 5: Construct recovery**

对 $M^*$ 中的每一对 $(u, v)$，选择从 $u$ 到 $v$ 的最短路径上的所有边，在这些边上施加 $Z$（或 $X$）恢复操作。

### 复杂度

**Edmonds 的 Blossom 算法**：在 $|D|$ 个顶点的图上找最小权重完美匹配，时间复杂度 $O(|D|^3)$。

对于 $d \times d$ 表面码，当错误率 $p$ 时，平均缺陷数 $|D| \approx O(pd^2)$，所以平均复杂度 $O(p^3 d^6)$。

**预处理优化**：可以预计算所有顶点对之间的距离（$O(d^2)$ 次 BFS），然后在线阶段只做匹配。

### 阈值性能 **[Dennis et al. 2002, §3.4; Roffe, §5.2]**

MWPM 解码器在表面码上的阈值：
- 独立 $X/Z$ 噪声：$p_{\text{th}} \approx 10.3\%$ **[Dennis et al. 2002, §3.4]**
- 去极化噪声：$p_{\text{th}} \approx 1.1\%$（因为 $Y$ 错误同时触发 $X$ 和 $Z$ syndrome，MWPM 无法利用这种关联）

MWPM 不是最优解码器（它不等于 ML），因为：
1. 它只找最小权重错误，不考虑错误的简并性（同一 syndrome 对应的多种等价错误链）
2. 对于 CSS 码，它独立处理 $X$ 和 $Z$，忽略了 $Y$ 错误的关联

---

## Part 4: Belief Propagation (BP) Decoder **[Roffe, §5.1]**

### 数学框架

置信传播是一种基于概率图模型的近似推断算法，在 factor graph（因子图）上传递消息。

**Step 1: Factor graph construction**

构造二部图 $G = (V \cup F, E)$：
- **变量节点** $V = \{e_1, e_2, \ldots, e_n\}$：每个物理量子比特对应一个变量，取值 $e_i \in \{I, X, Y, Z\}$（或简化为 $\{0, 1\}$ 对单一类型错误）
- **因子节点** $F = \{f_1, f_2, \ldots, f_{n-k}\}$：每个稳定子对应一个因子
- 边：变量 $e_i$ 与因子 $f_j$ 相连当且仅当稳定子 $g_j$ 作用在量子比特 $i$ 上（即 $g_j$ 在第 $i$ 位不是 $I$）

**Step 2: Message passing**

对于 bit-flip 噪声（只考虑 $X$ 错误），每个变量 $e_i \in \{0, 1\}$（0: no error, 1: error）。

**变量到因子的消息**（第 $t$ 次迭代）：

$$m_{i \to j}^{(t)}(e_i) \propto p_i(e_i) \prod_{j' \in N(i) \setminus j} \hat{m}_{j' \to i}^{(t-1)}(e_i)$$

其中 $p_i(e_i)$ 是先验概率（$p_i(0) = 1-p$，$p_i(1) = p$），$N(i)$ 是变量 $i$ 的邻居因子集。

**因子到变量的消息**：

$$\hat{m}_{j \to i}^{(t)}(e_i) = \sum_{\{e_{i'} : i' \in N(j) \setminus i\}} f_j(e_i, \{e_{i'}\}) \prod_{i' \in N(j) \setminus i} m_{i' \to j}^{(t)}(e_{i'})$$

其中因子函数 $f_j$ 强制 syndrome 约束：

$$f_j(e_{N(j)}) = \begin{cases} 1 & \text{if } \bigoplus_{i \in N(j)} e_i = s_j \\ 0 & \text{otherwise} \end{cases}$$

即变量 $e_i$ 在因子 $f_j$ 的邻域内的 XOR 必须等于 syndrome 位 $s_j$。

**Step 3: Log-likelihood ratio (LLR) formulation**

为了数值稳定，用对数似然比（LLR）表示消息：

$$\lambda_i = \log \frac{p_i(0)}{p_i(1)} = \log \frac{1-p}{p}$$

$$\mu_{i \to j}^{(t)} = \lambda_i + \sum_{j' \in N(i) \setminus j} \nu_{j' \to i}^{(t-1)}$$

因子到变量的 LLR 消息：

$$\nu_{j \to i}^{(t)} = (-1)^{s_j} \cdot 2 \tanh^{-1} \left( \prod_{i' \in N(j) \setminus i} \tanh\left(\frac{\mu_{i' \to j}^{(t)}}{2}\right) \right)$$

这是标准的 sum-product BP 在 $\mathbb{F}_2$ 上的公式（Gallager 解码）。

**Step 4: Decision**

收敛后（或达到最大迭代次数），计算每个变量的后验 LLR：

$$L_i^{(t)} = \lambda_i + \sum_{j \in N(i)} \nu_{j \to i}^{(t)}$$

决策：$\hat{e}_i = \begin{cases} 1 & \text{if } L_i^{(t)} < 0 \\ 0 & \text{if } L_i^{(t)} \geq 0 \end{cases}$

### BP 在量子码上的问题

1. **短环问题**：表面码的 factor graph 有很多长度为 4 的短环（两个相邻的稳定子共享两条边），BP 在有短环的图上不保证收敛或正确
2. **简并性处理**：BP 难以处理量子码的简并性（多个不同错误导致相同逻辑效果）
3. **性能**：在表面码上，纯 BP 的阈值远低于 MWPM（约 $3\%$  vs $10.3\%$），但可以通过改进（如 BP+OSD, BP+UF）提升

### 复杂度

每次迭代 $O(n)$（线性于物理量子比特数，因为表面码是 LDPC 码），总复杂度 $O(n \cdot T)$，其中 $T$ 是迭代次数。

---

## Part 5: Union-Find Decoder

### 数学框架

Union-Find 解码器是 Delfosse 和 Nickerson 提出的近线性时间解码器，基于不相交集合（disjoint set）数据结构。

**核心思想**：从每个 syndrome 缺陷出发，逐步"生长"cluster，直到 cluster 变成"中性的"（可以被局部纠正）。

**Step 1: 初始化**

- 对每个 syndrome 缺陷 $v$（$s_v = 1$），创建一个单元素 cluster $C_v = \{v\}$
- 每个 cluster 有一个"边界"（与 cluster 相邻但不在 cluster 内的边）

**Step 2: Growth phase（生长阶段）**

重复以下步骤直到所有 cluster 都是"中性的"（even）：

1. 将每个"奇"cluster（包含奇数个 syndrome 缺陷）的边界扩展半步
2. 如果两个 cluster 的边界相遇，用 Union-Find 合并它们
3. 检查合并后的 cluster 是否变成"偶"的（包含偶数个缺陷）

**"中性" cluster 的定义**：一个 cluster 包含偶数个 syndrome 缺陷（包括边界缺陷），此时 cluster 内部的错误可以被局部纠正，不会导致逻辑错误。

**Step 3: Peeling phase（剥离阶段）**

对每个"中性"的 cluster，用 spanning tree 上的剥离算法找到连接所有缺陷的错误链：

1. 构造 cluster 的 spanning tree $T$
2. 从叶节点开始"剥离"：如果叶节点是缺陷，标记叶节点到父节点的边为"错误"；否则不标记
3. 删除叶节点，重复直到树为空

**形式化**：设 spanning tree $T = (V_T, E_T)$，对每个叶节点 $v$，设其父节点为 $u$：

$$\hat{e}_{(v,u)} = \begin{cases} 1 & \text{if } v \text{ has odd number of defects in its subtree} \\ 0 & \text{otherwise} \end{cases}$$

### 复杂度

- Union-Find 数据结构：$O(\alpha(n))$ 每次操作（$\alpha$ 是反 Ackermann 函数，实际近似为常数）
- 总复杂度：$O(n \cdot \alpha(n))$，近线性

### 性能

Union-Find 解码器的阈值低于 MWPM（约 $9.9\%$ vs $10.3\%$ 对独立 $X/Z$ 噪声），但速度快得多，适合实时解码。

---

## Comparison Table

| 解码器 | 时间复杂度 | 阈值 ($X/Z$ 噪声) | 阈值 (去极化) | 是否最优 | 适用场景 |
|-------|-----------|-------------------|-------------|---------|---------|
| ML | $O(2^n)$ | $\sim 11\%$ | $\sim 18.9\%$ (理论极限) | 是 | 理论参考 |
| MWPM | $O(n^3)$ | $\sim 10.3\%$ | $\sim 1.1\%$ | 否 | 标准基准 |
| BP | $O(n \cdot T)$ | $\sim 3\%$ (纯 BP) | 较低 | 否 | LDPC 码 |
| BP + OSD | $O(n^3)$ | $\sim 10\%$ | $\sim 15\%$ | 近似 | 高精度需求 |
| Union-Find | $O(n \cdot \alpha(n))$ | $\sim 9.9\%$ | — | 否 | 实时解码 |

---

## From Steane Tutorial: Decoding in the Stabilizer Framework

### Syndrome-Based Recovery **[Steane Tutorial, §3.3]**

Steane 从稳定子框架出发，给出解码问题的基本结构：

**错误恢复三步骤** **[Steane Tutorial, §3.3]**：

1. **Syndrome 提取**：测量所有稳定子生成元 $g_1, \ldots, g_{n-k}$，得到 syndrome $\mathbf{s} \in \mathbb{F}_2^{n-k}$
2. **Syndrome 解码**：根据 $\mathbf{s}$ 确定恢复操作 $R$（这是解码器的核心任务）
3. **恢复操作**：施加 $R$，将态恢复到码空间

**查找表 vs 算法解码** **[Steane Tutorial, §3.4]**：

对小码（如 $[[5,1,3]]$、$[[7,1,3]]$），可以预计算所有 $2^{n-k}$ 个 syndrome 对应的恢复操作。但对大码（如表面码），syndrome 空间指数增长，必须使用算法解码。

### 简并性对解码的影响 **[Steane Tutorial, §3.5]**

**定义** **[Steane Tutorial, §3.5]**：如果存在两个不同的可纠正错误 $E_1 \neq E_2$ 但 $E_1^\dagger E_2 \in \mathcal{S}$（相差一个稳定子），则码是**简并的**。

**简并性对解码的关键影响**：

1. **正面**：简并码可以纠正超过 Hamming bound 允许的错误数——例如表面码就是高度简并的
2. **解码挑战**：简并意味着不能简单地选"最可能的单个错误"，而应选"最可能的逻辑等价类"
3. **MWPM 的局限**：MWPM 找最可能的单个错误（最小权重），不利用简并性。理论上可以通过考虑等价类概率来改进

---

## From Bacon's Introduction: Decoding as Inference Problem

### 贝叶斯推断视角 **[Bacon, §4.4]**

Bacon 将解码问题定位为贝叶斯推断：

**给定**：
- 先验分布 $\Pr(E)$（由噪声模型决定）
- 似然函数 $\Pr(\mathbf{s}|E) = \delta_{\mathbf{s}, \sigma(E)}$（syndrome 是确定性函数）
- 逻辑等价类 $[E] = \{E' : E'E^{-1} \in \mathcal{S}\}$

**最优解码** **[Bacon, §4.4]**：

$$\hat{L} = \arg\max_{L} \Pr(L | \mathbf{s}) = \arg\max_{L} \sum_{\substack{E : \sigma(E)=\mathbf{s} \\ E \in L}} \Pr(E)$$

Bacon 强调这是 **marginal inference**（对等价类内所有错误求和），而非 **MAP inference**（找单个最可能的错误）。对简并码（如表面码），两者差异显著。

### 解码复杂度层级 **[Bacon, §4.5]**

| 解码目标 | 复杂度 | 对简并码最优? |
|---------|--------|-------------|
| 找最可能的单个错误 (MAP) | NP-hard | 否 |
| 找最可能的等价类 (ML) | #P-hard | 是 |
| 近似 ML | 多项式 | 接近最优 |

---

## From Surface Code Notes: Decoder Implementation Details

### Detection Event Graph **[Surface Code Notes, §6.2]**

在 circuit-level noise 下，解码器不直接使用 raw syndrome，而是使用 **detection events**（syndrome 位在相邻轮次之间的翻转）：

$$d_i^{(t)} = s_i^{(t)} \oplus s_i^{(t-1)}$$

**优势**：detection events 只在错误发生时为 1，消除了 syndrome 累积效应。在 3D 解码图中，detection events 对应时空格点上的节点。

### 边权重的精确计算 **[Surface Code Notes, §6.3]**

对于 circuit-level noise 模型，detection graph 的边权重不再是简单的 $\log\frac{1-p}{p}$，而需要考虑：

1. **数据错误**的传播路径（通过 CNOT 门）
2. **测量错误**的时间位置
3. **Hook errors**的关联效应

精确权重需要追踪 syndrome 提取电路中每个故障位置的 detector 响应，然后计算每条 detector graph 边被单个故障触发的概率。

### 实时解码约束 **[Surface Code Notes, §8]**

超导量子计算机上的实时解码面临严格时间约束：

- Syndrome 测量周期：$\sim 1\,\mu$s
- 需要在下一个周期前完成解码
- 若解码跟不上，syndrome 数据积压（backlog），最终导致失败

**解决方案**：
- Union-Find：$O(n\alpha(n))$，实际 $\sim 0.1\,\mu$s/round
- Sparse Blossom MWPM：平均 $O(1)$ per detection event（利用稀疏性）
- Sliding window：只解码最近 $w$ 轮的数据

---

## From Dennis et al. 2002: Optimal Decoding and Statistical Mechanics

### Optimal Recovery Criterion **[Dennis et al. 2002, §3.3, Eq.(6)]**

Given measured syndrome $S$, the probability that it was caused by an error chain $E' = S + C'$ where $C'$ belongs to homology class $h$:

$$\text{prob}(h|S) = \frac{\sum_{C' \in h} \text{prob}(S + C')}{\sum_{C'} \text{prob}(S + C')}$$

The optimal recovery guesses the homology class $h$ that maximizes this expression. Recovery succeeds if the actual cycle $C$ belongs to this class.

### Accuracy Threshold Criterion **[Dennis et al. 2002, §3.3, Eq.(8)]**

The error probability per qubit lies below the accuracy threshold iff, in the limit $L \to \infty$:

$$\sum_E \text{prob}(E) \cdot \sum_{D \text{ nontrivial}} \text{prob}[(E+D)|E] = 0$$

This means error chains differing from the actual error by a homologically non-trivial cycle have probability zero in the thermodynamic limit.

### Random-Bond Ising Model (2D, Perfect Syndrome) **[Dennis et al. 2002, §3.4]**

The fluctuations of error chains are described by:

$$Z[J, \eta] = \sum_{\{\sigma_i\}} \exp\left(J \sum_{\langle ij \rangle} \eta_{ij} \sigma_i \sigma_j\right)$$

where $e^{-2J} = p/(1-p)$, $\eta_\ell = \pm 1$ with probability $1-p$ and $p$. The relation between coupling and bond probability defines the **Nishimori line** in the phase diagram, with enhanced symmetry. The phase transition on this line gives the accuracy threshold $p_c \approx 10.9\%$ **[Dennis et al. 2002, §3.4]**.

### $\mathbb{Z}_2$ Gauge Theory (3D, Imperfect Syndrome) **[Dennis et al. 2002, §3.4]**

With faulty syndrome measurements (probability $q$), the third dimension is time. The model becomes:

$$Z[J, \eta] = \sum_{\{\sigma_\ell\}} \exp\left(J \sum_P \eta_P u_P\right)$$

where $u_P = \prod_{\ell \in P} \sigma_\ell$ and $\eta_P = \pm 1$ marks the error chain. This is a 3D $\mathbb{Z}_2$ lattice gauge theory with quenched disorder. The order-disorder phase transition gives the accuracy threshold for quantum storage with imperfect measurements **[Dennis et al. 2002, §3.4]**.

### Proved Lower Bound **[Dennis et al. 2002, §4]**

Error recovery succeeds in the large code block limit if qubit phase errors, bit-flip errors, and syndrome bit errors all occur with probability below $1.14\%$ **[Dennis et al. 2002, §4]**.

### From Roffe: Efficient Decoding **[Roffe, §5.1]**

For the distance-five surface code $[[41,1,5]]$, the syndrome has length $m = 40$, requiring a lookup table of size $2^{40} \approx 10^{12}$ -- impractical. Instead, approximate inference techniques (MWPM) identify error chains between positive syndrome measurements. The logical error rate depends heavily on the decoder used **[Roffe, §5.1]**.

---

## From NordiQUEst Practical Guide: Practical Decoding

### Practical MWPM Implementation **[NordiQUEst, §4.1]**

MWPM 解码器在实际实现中的关键步骤：

1. **Syndrome extraction**：执行 $d$ 轮 syndrome 测量，构建 3D detection graph
2. **Detection graph construction**：在 3D 中，节点是 detection events（syndrome 位翻转），空间边和时间边分别对应数据错误和测量错误
3. **Edge weighting**：对于非均匀噪声（如不同量子比特有不同错误率），边权重设为 $w_e = \log\frac{1-p_e}{p_e}$，其中 $p_e$ 是该边对应的错误概率
4. **Matching**：使用 PyMatching 或 Sparse Blossom 算法找最小权重完美匹配
5. **Correction inference**：从匹配结果反推恢复操作

**Sparse Blossom 算法** **[NordiQUEst, §4.1.2]**：Higgott & Gidney (2023) 提出的优化 MWPM 算法，在 surface code 上的平均时间复杂度为 $O(1)$ per detection event（在低错误率下），通过利用 syndrome 的稀疏性实现了接近实时的解码。

### Correlated MWPM **[NordiQUEst, §4.2]**

标准 MWPM 独立处理 $X$ 和 $Z$ 错误，忽略了 $Y$ 错误同时激发两种 syndrome 的关联性。改进方法：

**Correlated MWPM (也称 Möbius decoder)**：
- 构造联合 detection graph，包含 $X$-syndrome 节点、$Z$-syndrome 节点、以及连接两者的 hyperedge
- 通过加权图的方式近似处理 $Y$ 错误的关联
- 阈值从 $\sim 1.1\%$ 提升到 $\sim 1.5\%$（去极化噪声下）

### Tensor Network Decoder **[NordiQUEst, §4.3]**

基于张量网络收缩的近最优解码器：

$$\Pr(\bar{L} | \mathbf{s}) = \frac{1}{Z} \text{trc}\left(\prod_{\text{tensors}} T_i\right)$$

其中 $T_i$ 是由 syndrome 和错误概率构造的局部张量。通过近似收缩（如 boundary MPS 方法），可以在 $O(d^3 \chi^3)$ 时间内计算，其中 $\chi$ 是 bond dimension。

- $\chi = 1$: 退化为独立解码
- $\chi \to \infty$: 趋近 ML 解码
- 实用选择 $\chi \sim 8-64$：接近 ML 性能

### Sliding Window Decoder **[NordiQUEst, §4.4]**

实时解码的关键技术：不等待所有 $d$ 轮测量完成，而是使用滑动窗口：

1. 窗口包含最近 $w$ 轮测量（$w \ll d$ 轮的总数）
2. 在窗口内执行匹配/解码
3. 提交窗口前半部分的纠正决策
4. 窗口向前滑动

窗口大小 $w$ 需要平衡解码质量和延迟。典型选择 $w \approx d$。

### Neural Network Decoder **[NordiQUEst, §4.5]**

基于机器学习的解码方法：

- **输入**：syndrome 向量 $\mathbf{s} \in \{0,1\}^{n-k}$
- **输出**：恢复操作的逻辑等价类
- **架构**：CNN、GNN、Transformer 等
- **训练**：在模拟噪声数据上监督学习

优点：推理速度快（固定计算图，可并行化），可处理关联噪声。
缺点：需要针对每种码距和噪声模型重新训练，泛化能力有限。

### Practical Performance Comparison **[NordiQUEst, §4.6]**

对 rotated surface code 在 circuit-level depolarizing noise 下的实际性能：

| 解码器 | 阈值 | $d=5$ 逻辑错误率 ($p=10^{-3}$) | 解码速度 |
|-------|------|-------------------------------|---------|
| MWPM (PyMatching) | $\sim 0.6\%$ | $\sim 3 \times 10^{-4}$ | $\sim 1\,\mu$s/round |
| Correlated MWPM | $\sim 0.8\%$ | $\sim 1 \times 10^{-4}$ | $\sim 2\,\mu$s/round |
| Union-Find | $\sim 0.5\%$ | $\sim 5 \times 10^{-4}$ | $\sim 0.1\,\mu$s/round |
| Tensor Network ($\chi=8$) | $\sim 0.9\%$ | $\sim 5 \times 10^{-5}$ | $\sim 10$ms/round |
| ML (exact) | $\sim 1.0\%$ | $\sim 2 \times 10^{-5}$ | 不实际 |

**关键实际约束**：解码器必须在一个 syndrome 测量周期（$\sim 1\,\mu$s for superconducting qubits）内完成，否则 syndrome 数据积压，导致 backlog problem。这严格限制了可用的解码算法。

---

## From NordiQUEst: Formal MAP Decoding Derivation

### Bayesian Decoding Framework **[NordiQUEst, p.17-19]**

NordiQUEst provides a clean derivation of the optimal decoding problem [NordiQUEst, p.17-18]:

Given parity-check matrix $H$, received syndrome $s = He$, and error distribution $P(e)$, the MAP decoder solves:

$$\hat{e} = \arg\max_{e \in \{0,1\}^n} P(e \mid s) = \arg\max_{e : He = s} P(e)$$

using Bayes' rule $P(e|s) = P(s|e)P(e)/P(s)$, where $P(s|e) = 1$ if $He = s$ and $0$ otherwise [NordiQUEst, p.18].

### Independent Error Simplification **[NordiQUEst, p.19]**

For IID errors with $P(e_i = 1) = p$ and $p < 0.5$, the probability $P(e) = p^{|e|}(1-p)^{n-|e|}$ decreases with weight $|e|$. The MAP problem reduces to minimum-weight decoding [NordiQUEst, p.19]:

$$\min_{e \in \{0,1\}^n} |e| \quad \text{subject to} \quad He = s$$

### MAP Decoding Complexity **[NordiQUEst, p.20]**

MAP decoding is NP-complete in general: a naive approach requires searching all $2^n$ possible error vectors [NordiQUEst, p.20]. However, structured codes (Hamming codes, repetition codes) allow polynomial-time decoding.

### Belief Propagation for Approximate MAP **[NordiQUEst, p.21]**

Belief Propagation is an iterative, linear-time heuristic that exploits the factorization of $P(e|s)$ over a Tanner graph [NordiQUEst, p.21]. It is widely used in both classical and quantum error correction.

---

## From Steane Tutorial: Classical Error Correction Foundations

### Error Syndrome and Cosets **[Steane, p.9-10]**

Steane derives the fundamental syndrome property for linear codes [Steane, p.9]: for parity check matrix $H$ and received word $w = u + e$:

$$s = Hw^T = H(u+e)^T = Hu^T + He^T = He^T$$

The syndrome depends only on the error vector, not the transmitted word [Steane, p.9]. All errors with the same syndrome form a coset of the code, and exactly one error per coset is chosen as correctable.

### Shannon's Theorem for Binary Symmetric Channel **[Steane, p.9]**

If the rate $k/n$ is less than the channel capacity $1 - H(p)$, and $n$ is sufficiently large, there exists a binary code allowing transmission with arbitrarily low failure probability [Steane, p.9]. The capacity of the binary symmetric channel is $1 - H(p)$ where $H(p) = -p\log_2 p - (1-p)\log_2(1-p)$.

---

## From Surface Notes: Decoding as Hyperedge Matching

### Detector Hypergraph Decoding **[Surface Notes, p.4]**

Fowler frames decoding in terms of the detector hypergraph [Surface Notes, p.4]: given a sufficiently sparse pattern of detection events, decoders find a high-probability set of hyperedges that matches the detection events. This set determines how many times the signs of logical operators need to be flipped.

A $Y$ error leads to four detection events (anticommuting with all four neighboring stabilizers), forming a **hyperedge** rather than a simple edge. The surface code therefore has a detector hypergraph, not just a detector graph [Surface Notes, p.4].

### Minimum Path Logical Error **[Surface Notes, p.5]**

Given any path of detector graph edges connecting a boundary of one type to another disconnected boundary of the same type, if at least half the edges are associated with errors, there is potential for a logical error [Surface Notes, p.5]. The probability of such error clusters is exponentially suppressed as code distance increases.

---

## References

- Dennis, E., Kitaev, A., Landahl, A. & Preskill, J. "Topological quantum memory." J. Math. Phys. 43, 4452 (2002).
- Edmonds, J. "Paths, trees, and flowers." Canadian J. Math. 17, 449 (1965).
- Roffe, J. "Quantum Error Correction: An Introductory Guide." Contemp. Phys. 60, 226 (2019).
- **[Steane]** Steane, A. M. "A Tutorial on Quantum Error Correction." Proc. Int. School of Physics "Enrico Fermi" (2006).
- **[Bacon]** Bacon, D. "Introduction to quantum error correction." Ch. 2 in *Quantum Error Correction* (Cambridge, 2013).
- **[Surface Notes]** Fowler, A. G. "Surface code quantum computation." Google Quantum AI (2025).
- **[NordiQUEst]** Lenssen, Martres, Myneni, Fuchs. "Quantum Error Correction - Theory and Hands-on." NordiQUEst (2024).
- Delfosse, N. & Nickerson, N. H. "Almost-linear time decoding algorithm for topological codes." Quantum 5, 595 (2021).
- Panteleev, P. & Kalachev, G. "Degenerate quantum LDPC codes with good finite length performance." Quantum 5, 585 (2021).
- Higgott, O. & Gidney, C. "Sparse Blossom: correcting a million errors per core second with minimum-weight matching." arXiv:2303.15933 (2023).
- Bravyi, S. et al. "Maximum likelihood decoding and tensor networks." PRA 90, 032326 (2014).
- Fujii, K. "Quantum Computation with Topological Codes." SpringerBriefs (2015), Ch.3 §3.4, Appendix B.

---

## Additions from Fujii's "Quantum Computation with Topological Codes" (2015)

### Formal Decoding Framework [Fujii, Appendix B]

> **[Fujii, Appendix B]**: 对 $n$ 量子比特稳定子码（稳定子群 $\mathcal{G}=\{G_i\}$，逻辑算子群 $\mathcal{L}=\{L_i\}$），Pauli 错误 $E$ 唯一分解为：
>
> $$E = L_i G_j R[\mathcal{S}(E)]$$
>
> 其中 $R(S)$ 是给定 syndrome $S$ 的纯错误算子（pure error operator）。解码映射 $\mathcal{D}$ 计算 $L_i = \mathcal{D}(E)$。

> **[Fujii, Appendix B]**: 最优解码选择最大化后验概率的逻辑算子：
>
> $$\hat{L} = \arg\max_{L_i \in \mathcal{L}} P(L_i|S) = \arg\max_{L_i} \frac{1}{\mathcal{N}} \sum_{G_j \in \mathcal{G}} P[L_i G_j R(S)]$$
>
> 一般情况下计算 $P(L|S)$ 是困难的（需要对所有稳定子算子求和，指数时间）。

### Concatenated Code Decoding via Belief Propagation [Fujii, Appendix B]

> **[Fujii, Appendix B]**: 对级联码，利用层级结构可高效解码。第 $k$ 层错误 $E^{(k)}$ 递归分解：
>
> $$E^{(k)} = G_j^{(k+1)} L_i^{(k+1)} R^{(k+1)}(S^{(k+1)})$$
>
> 后验概率通过因子图上的 belief propagation（消息传递）高效计算：
> - 圆节点到方节点消息：$\mu_{c\to b}(x_c) = \prod_{b'\in\delta c\setminus b}\nu_{b'\to c}(x_c)$
> - 方节点到圆节点消息：$\nu_{b\to c}(x_c) = \sum_{\delta b\setminus x_c} f_b(\delta b)\prod_{c'\in\delta b\setminus c}\mu_{c'\to b}(x_{c'})$
>
> 由于级联码的因子图是树图，belief propagation 给出精确的边际分布。

### Surface Code Decoding: Posterior Probability and RBIM [Fujii, Ch.3, §3.4-3.5]

> **[Fujii, Ch.3, §3.4]**: 对表面码独立 $Z$ 错误（概率 $p$），给定 syndrome $c_0^s = \partial c_1^e$，同调类 $h_k$ 的后验概率为：
>
> $$p_k = \sum_{c_1^{r'}} P(c_1^{r'}|c_0^s) = \mathcal{N}'\,\mathcal{Z}(\{J_{ij}^{(k)}\})$$
>
> 其中 $\mathcal{Z}$ 是 $\pm J$ 随机键 Ising 模型（RBIM）的配分函数，$e^{-J} = \sqrt{p/(1-p)}$。

> **[Fujii, Ch.3, §3.5]**: RBIM 的相图决定解码性能。最优解码对应 Nishimori 线 $p = p'$。多临界点（optimal threshold）数值计算为 $10.94 \pm 0.02\%$。MWPM 对应零温极限 $J\to\infty$（抑制熵效应），阈值 $10.4 \pm 0.1\%$。

### Renormalization Group Decoder [Fujii, Ch.3, §3.4]

> **[Fujii, Ch.3, §3.4]**: Duclos-Cianci & Poulin 的重正化解码器用 12 量子比特单元格定义层级结构。每个单元格包含 2 对逻辑算子、6 个稳定子生成元、6 个纯错误算子、4 对边算子。任意 Pauli 算子分解为 $A = L^{(1)}G^{(1)}\bar{G}^{(1)}E^{(1)}$。
>
> 后验概率 $P(L^{(k)}|S^{(k)})$ 从底层向顶层传播。并行化时间 $O(\log_2 n)$。阈值：独立 $X/Z$ 错误 $\sim 9\%$，去极化 $\sim 15.2\%$。

### Efficient MWPM Implementation [Fujii, Ch.3, §3.4]

> **[Fujii, Ch.3, §3.4]**: Fowler 等人的高效 MWPM：因长错误链指数抑制，可按 Manhattan 距离分配权重并截断远距离匹配（$O(n^4) \to O(n^2)$ 边数）。匹配过程几乎完全使用局部信息，可并行化到 $O(1)$ 平均时间每轮。
