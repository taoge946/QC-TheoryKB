# D3PM: Discrete Denoising Diffusion Probabilistic Models

> **Tags**: `d3pm`, `discrete-diffusion`, `combinatorial-optimization`, `categorical`, `DIFUSCO`

## Statement

推导离散去噪扩散概率模型（D3PM, Austin et al. 2021）的完整数学框架。从连续扩散模型在离散数据上的局限性出发，定义基于转移矩阵的前向过程，推导边际分布和后验分布的闭式解，推导变分下界（VLB），简化训练目标，并建立与组合优化（DIFUSCO）的联系。

## Prerequisites

- 连续扩散模型（DDPM）基础（见 [diffusion_models_math.md](diffusion_models_math.md)）
- ELBO 与变分推断（见 [elbo_derivation.md](elbo_derivation.md)）
- KL散度定义及性质
- 范畴分布（Categorical distribution）
- 马尔可夫链与转移矩阵
- 矩阵乘法与克罗内克积基础

---

## Part 1: Motivation — Why Discrete Diffusion?

### 1.1 连续扩散的局限

标准DDPM在**连续**空间 $\mathbb{R}^d$ 上定义前向过程：

$$q(x_t | x_{t-1}) = \mathcal{N}(x_t;\; \sqrt{1 - \beta_t}\, x_{t-1},\; \beta_t \mathbf{I})$$

<!-- 连续扩散通过加高斯噪声来破坏数据 -->

但许多实际问题的数据是**本质离散的**：

1. **组合优化**：最大独立集（MIS）中每个节点取值 $\{0, 1\}$，旅行商问题（TSP）中边的选取也是二值的
2. **图着色**：每个节点的颜色属于有限集 $\{1, 2, \ldots, K\}$
3. **排列调度**：机器调度问题中，作业顺序是离散排列
4. **分子设计**：原子类型属于离散集合
5. **文本生成**：每个token属于词表 $\{1, \ldots, V\}$

**核心矛盾**：对离散变量 $x \in \{1, \ldots, K\}$ 加高斯噪声 $x + \epsilon$ 会产生连续值，破坏离散结构。即使最终取整/argmax，梯度信号也会退化。

<!-- 离散数据不能直接加高斯噪声，需要定义离散噪声过程 -->

### 1.2 D3PM 的核心思想

D3PM 的关键洞察：用**范畴噪声**（categorical noise）替代高斯噪声。

- 前向过程：通过**转移矩阵** $Q_t$ 定义离散状态间的随机跳转
- 每一步的噪声过程是一个马尔可夫链在有限状态空间上的转移
- 极限分布是某种"纯噪声"的离散分布（如均匀分布或吸收态）

---

## Part 2: Forward Process — Categorical Noise

### 2.1 符号约定

设数据空间为 $\{1, 2, \ldots, K\}$，即每个变量有 $K$ 个可能取值。

<!-- $K$ 是类别数，如二值问题 $K=2$，图着色 $K$ 为颜色数 -->

用 **one-hot 行向量** 表示状态：若 $x = k$，则 $\mathbf{x} = (0, \ldots, 0, 1, 0, \ldots, 0) \in \mathbb{R}^{1 \times K}$，第 $k$ 个位置为1。

<!-- 使用 one-hot 行向量便于与转移矩阵相乘 -->

### 2.2 单步转移

定义**转移矩阵** $Q_t \in \mathbb{R}^{K \times K}$，其中 $[Q_t]_{ij} = q(x_t = j | x_{t-1} = i)$。

<!-- $Q_t$ 的第 $i$ 行第 $j$ 列表示从状态 $i$ 转移到状态 $j$ 的概率 -->

$Q_t$ 满足：
- $[Q_t]_{ij} \geq 0$ （概率非负）
- $\sum_{j=1}^K [Q_t]_{ij} = 1$ （每行之和为1，即行随机矩阵）

单步前向过程定义为 **[Austin et al. 2021, Eq.(1)]**：

$$\boxed{q(x_t | x_{t-1}) = \mathrm{Cat}(x_t;\; p = \mathbf{x}_{t-1} Q_t)}$$

<!-- 用范畴分布和转移矩阵定义单步噪声 -->

**展开含义**：若 $x_{t-1} = i$（即 $\mathbf{x}_{t-1}$ 是第 $i$ 个标准基向量），则：

$$q(x_t = j | x_{t-1} = i) = [\mathbf{x}_{t-1} Q_t]_j = [Q_t]_{ij}$$

<!-- 这就是标准的马尔可夫链转移 -->

### 2.3 联合前向过程

与连续情形类似，前向过程是马尔可夫链：

$$q(x_{1:T} | x_0) = \prod_{t=1}^{T} q(x_t | x_{t-1})$$

---

## Part 3: Marginal Distribution $q(x_t | x_0)$

### 3.1 推导

**目标**：直接从 $x_0$ 得到任意时刻 $t$ 的分布，跳过中间步。

<!-- 类比连续扩散中 $q(x_t|x_0)$ 的闭式解 -->

**第1步**：$t=1$ 的情形

$$q(x_1 | x_0) = \mathrm{Cat}(x_1;\; p = \mathbf{x}_0 Q_1)$$

**第2步**：$t=2$ 的情形，利用全概率公式

$$q(x_2 = j | x_0 = i) = \sum_{k=1}^K q(x_2 = j | x_1 = k)\, q(x_1 = k | x_0 = i) = \sum_{k=1}^K [Q_1]_{ik}\, [Q_2]_{kj}$$

<!-- 这正是矩阵乘法 $[Q_1 Q_2]_{ij}$ -->

这正是矩阵乘法的定义：

$$q(x_2 = j | x_0 = i) = [Q_1 Q_2]_{ij}$$

**第3步**：归纳法推广到一般 $t$

定义**累积转移矩阵**：

$$\boxed{\bar{Q}_t = Q_1 Q_2 \cdots Q_t = \prod_{s=1}^t Q_s}$$

<!-- 累积转移矩阵是所有单步转移矩阵之积 -->

则**边际分布**为 **[Austin et al. 2021, Eq.(2)]**：

$$\boxed{q(x_t | x_0) = \mathrm{Cat}(x_t;\; p = \mathbf{x}_0 \bar{Q}_t)}$$

**验证**：$q(x_t = j | x_0 = i) = [\bar{Q}_t]_{ij}$，这是 $t$ 步马尔可夫链的 Chapman-Kolmogorov 方程。

<!-- 这是 Chapman-Kolmogorov 方程的矩阵形式 -->

### 3.2 与连续情形的类比

| 连续（DDPM） | 离散（D3PM） |
|:---:|:---:|
| $q(x_t \| x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t}\, x_0,\; (1 - \bar{\alpha}_t) I)$ | $q(x_t \| x_0) = \mathrm{Cat}(x_t; \mathbf{x}_0 \bar{Q}_t)$ |
| 噪声调度 $\beta_t$ 控制加噪速度 | 转移矩阵 $Q_t$ 控制加噪速度 |
| 极限 $q(x_T \| x_0) \to \mathcal{N}(0, I)$ | 极限 $q(x_T \| x_0) \to$ 均匀/吸收分布 |
| 累积参数 $\bar{\alpha}_t = \prod \alpha_s$ | 累积矩阵 $\bar{Q}_t = \prod Q_s$ |

---

## Part 4: Posterior $q(x_{t-1} | x_t, x_0)$

### 4.1 推导动机

反向过程需要 $q(x_{t-1} | x_t)$，但这依赖于未知的数据分布。与连续DDPM一样，当给定 $x_0$ 时，后验 $q(x_{t-1} | x_t, x_0)$ 可以精确计算。

<!-- 这是训练反向网络的"标签"，贝叶斯定理的核心应用 -->

### 4.2 完整贝叶斯推导

由贝叶斯定理：

$$q(x_{t-1} | x_t, x_0) = \frac{q(x_t | x_{t-1}, x_0)\, q(x_{t-1} | x_0)}{q(x_t | x_0)}$$

<!-- 利用马尔可夫性 $q(x_t|x_{t-1}, x_0) = q(x_t|x_{t-1})$ -->

**第1步**：由马尔可夫性，$q(x_t | x_{t-1}, x_0) = q(x_t | x_{t-1})$，因此：

$$q(x_{t-1} = j | x_t = k, x_0 = i) = \frac{q(x_t = k | x_{t-1} = j)\, q(x_{t-1} = j | x_0 = i)}{q(x_t = k | x_0 = i)}$$

**第2步**：代入已知量

- $q(x_t = k | x_{t-1} = j) = [Q_t]_{jk}$（单步转移矩阵）
- $q(x_{t-1} = j | x_0 = i) = [\bar{Q}_{t-1}]_{ij}$（累积转移矩阵）
- $q(x_t = k | x_0 = i) = [\bar{Q}_t]_{ik}$（$t$步累积转移矩阵）

$$q(x_{t-1} = j | x_t = k, x_0 = i) = \frac{[Q_t]_{jk}\, [\bar{Q}_{t-1}]_{ij}}{[\bar{Q}_t]_{ik}}$$

**第3步**：向量化表达

定义后验概率向量（对 $x_{t-1}$ 的所有可能取值）：

$$\boxed{q(x_{t-1} | x_t, x_0) \propto \mathbf{x}_0 \bar{Q}_{t-1} \odot \mathbf{x}_t Q_t^\top}$$

**[Austin et al. 2021, Eq.(2)]**

<!-- 逐元素乘（Hadamard积），然后归一化 -->

其中 $\odot$ 表示逐元素乘（Hadamard product），最终需要归一化使概率之和为1 **[Austin et al. 2021, Eq.(2)]**：

$$q(x_{t-1} | x_t, x_0) = \mathrm{Cat}\left(x_{t-1};\; p = \frac{\mathbf{x}_0 \bar{Q}_{t-1} \odot \mathbf{x}_t Q_t^\top}{\mathbf{x}_0 \bar{Q}_{t-1} (\mathbf{x}_t Q_t^\top)^\top}\right)$$

<!-- 分母是归一化常数，保证概率之和为1 -->

**第4步**：验证

分子中第 $j$ 个元素为：

$$[\mathbf{x}_0 \bar{Q}_{t-1}]_j \cdot [\mathbf{x}_t Q_t^\top]_j = [\bar{Q}_{t-1}]_{i,j} \cdot [Q_t]_{j,k}$$

这正是 $q(x_{t-1}=j|x_0=i) \cdot q(x_t=k|x_{t-1}=j)$，与第2步一致。

### 4.3 与连续后验的类比

| 连续 DDPM 后验 | 离散 D3PM 后验 |
|:---:|:---:|
| $q(x_{t-1} \| x_t, x_0) = \mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_t I)$ | $q(x_{t-1} \| x_t, x_0) = \mathrm{Cat}(x_{t-1}; \cdot)$ |
| 均值由 $x_0, x_t$ 线性组合 | 概率由 $\bar{Q}_{t-1}, Q_t$ 矩阵运算得到 |
| 高斯分布由均值方差完全确定 | 范畴分布由概率向量完全确定 |

---

## Part 5: Common Noise Schedules

### 5.1 均匀噪声（Uniform Transition）

**思想**：以概率 $\beta_t$ 随机跳到任意状态（均匀选取），以概率 $(1 - \beta_t)$ 保持不变。

<!-- 最简单的离散噪声：要么不变，要么随机跳 -->

$$\boxed{Q_t^{\mathrm{uniform}} = (1 - \beta_t) I + \frac{\beta_t}{K} \mathbf{1}\mathbf{1}^\top}$$

**[Austin et al. 2021, §3.1, Appendix A.1]**

其中 $\mathbf{1} \in \mathbb{R}^K$ 是全1列向量，$\mathbf{1}\mathbf{1}^\top$ 是全1矩阵。

**矩阵形式**（$K = 3$ 为例）：

$$Q_t = \begin{pmatrix} 1 - \beta_t + \frac{\beta_t}{3} & \frac{\beta_t}{3} & \frac{\beta_t}{3} \\ \frac{\beta_t}{3} & 1 - \beta_t + \frac{\beta_t}{3} & \frac{\beta_t}{3} \\ \frac{\beta_t}{3} & \frac{\beta_t}{3} & 1 - \beta_t + \frac{\beta_t}{3} \end{pmatrix}$$

**极限行为**：当 $t \to T$ 且 $\prod_t (1 - \beta_t) \to 0$ 时，$\bar{Q}_T \to \frac{1}{K}\mathbf{1}\mathbf{1}^\top$，即均匀分布。

<!-- 最终所有状态等概率，信息完全被破坏 -->

**累积矩阵**：由于 $Q_t^{\mathrm{uniform}}$ 的特殊结构（可对角化），可得：

$$\bar{Q}_t^{\mathrm{uniform}} = \bar{\alpha}_t I + (1 - \bar{\alpha}_t) \frac{1}{K}\mathbf{1}\mathbf{1}^\top, \quad \text{where } \bar{\alpha}_t = \prod_{s=1}^t (1 - \beta_s)$$

<!-- 累积矩阵保持相同结构，可以闭式计算 -->

**证明**：注意到 $I$ 和 $\frac{1}{K}\mathbf{1}\mathbf{1}^\top$ 是两个正交投影算子，且 $\frac{1}{K}\mathbf{1}\mathbf{1}^\top \cdot \frac{1}{K}\mathbf{1}\mathbf{1}^\top = \frac{1}{K}\mathbf{1}\mathbf{1}^\top$，因此矩阵乘法可以按两个分量分别累积。

### 5.2 吸收噪声（Absorbing State）

**思想**：引入一个特殊的吸收态 $[\mathrm{MASK}]$（编号为 $K+1$ 或 $K$），每步以概率 $\beta_t$ 被"遮蔽"，一旦被遮蔽就永远留在该状态。

<!-- 类似BERT的[MASK]机制 -->

设状态空间为 $\{1, \ldots, K-1, \mathrm{MASK}\}$（$K$ 个状态，最后一个是吸收态），则：

$$\boxed{Q_t^{\mathrm{absorb}} = \begin{pmatrix} (1-\beta_t) I_{(K-1)\times(K-1)} & \beta_t \mathbf{1}_{K-1} \\ \mathbf{0}_{1\times(K-1)} & 1 \end{pmatrix}}$$

**[Austin et al. 2021, §3.1, Appendix A.2]**

<!-- 非吸收状态以 $\beta_t$ 概率跳到 MASK，MASK 永远停留 -->

**$K=3$ 时的例子**（状态1,2,MASK）：

$$Q_t = \begin{pmatrix} 1 - \beta_t & 0 & \beta_t \\ 0 & 1 - \beta_t & \beta_t \\ 0 & 0 & 1 \end{pmatrix}$$

**累积矩阵**：

$$[\bar{Q}_t^{\mathrm{absorb}}]_{ij} = \begin{cases} \bar{\alpha}_t & \text{if } i = j \text{ and } i \neq \mathrm{MASK} \\ 1 - \bar{\alpha}_t & \text{if } j = \mathrm{MASK} \text{ and } i \neq \mathrm{MASK} \\ 1 & \text{if } i = j = \mathrm{MASK} \\ 0 & \text{otherwise} \end{cases}$$

其中 $\bar{\alpha}_t = \prod_{s=1}^t (1 - \beta_s)$。

**极限行为**：$\bar{Q}_T \to$ 所有非MASK状态全部变为MASK。

<!-- 最终所有token都被mask，类似masked language model的完全遮蔽 -->

### 5.3 离散化高斯噪声（Discretized Gaussian）

**思想**：模仿连续高斯扩散，在离散有序状态上定义"局部"噪声——状态倾向于跳到邻近状态。

<!-- 适用于有自然序关系的离散变量（如量化像素值） -->

$$\boxed{[Q_t^{\mathrm{gauss}}]_{ij} \propto \exp\left(-\frac{(i - j)^2}{2\sigma_t^2}\right), \quad \text{每行归一化}}$$

**[Austin et al. 2021, §3.1, Appendix A.3]**

其中 $\sigma_t$ 随 $t$ 增大，控制跳转范围。

**性质**：
- 对角线附近元素较大（倾向保持或跳到邻近状态）
- $\sigma_t$ 小时近似单位矩阵，$\sigma_t$ 大时趋近均匀分布
- 适用于有序离散变量（如灰度像素值 $\{0, 1, \ldots, 255\}$）

---

## Part 6: Variational Lower Bound (VLB)

### 6.1 离散 ELBO 推导

**目标**：推导 $\log p_\theta(x_0)$ 的变分下界。

<!-- 与连续DDPM的ELBO推导平行，但所有分布换成范畴分布 -->

**第1步**：写出对数似然的下界

$$\log p_\theta(x_0) = \log \sum_{x_{1:T}} p_\theta(x_{0:T})$$

引入变分分布 $q(x_{1:T} | x_0)$：

$$\log p_\theta(x_0) = \log \sum_{x_{1:T}} q(x_{1:T} | x_0) \frac{p_\theta(x_{0:T})}{q(x_{1:T} | x_0)} \geq \sum_{x_{1:T}} q(x_{1:T} | x_0) \log \frac{p_\theta(x_{0:T})}{q(x_{1:T} | x_0)}$$

<!-- 由 Jensen 不等式（离散版本），凸函数取负号方向 -->

最后一步用了 Jensen 不等式（$\log$ 是凹函数）。

**第2步**：展开联合分布

$$p_\theta(x_{0:T}) = p(x_T) \prod_{t=1}^T p_\theta(x_{t-1} | x_t)$$

$$q(x_{1:T} | x_0) = \prod_{t=1}^T q(x_t | x_{t-1})$$

**第3步**：代入并整理 ELBO

$$\mathcal{L}_{\mathrm{VLB}} = \sum_{x_{1:T}} q(x_{1:T} | x_0) \left[\log p(x_T) + \sum_{t=1}^T \log \frac{p_\theta(x_{t-1} | x_t)}{q(x_t | x_{t-1})}\right]$$

**第4步**：重写条件概率比

利用贝叶斯规则 $q(x_t | x_{t-1}) = \frac{q(x_{t-1} | x_t, x_0) q(x_t | x_0)}{q(x_{t-1} | x_0)}$，代入并重新分组：

$$\mathcal{L}_{\mathrm{VLB}} = \underbrace{\mathbb{E}_q[\log p_\theta(x_0 | x_1)]}_{L_0} - \underbrace{D_{\mathrm{KL}}(q(x_T | x_0) \| p(x_T))}_{L_T} - \sum_{t=2}^{T} \underbrace{\mathbb{E}_q\left[D_{\mathrm{KL}}(q(x_{t-1} | x_t, x_0) \| p_\theta(x_{t-1} | x_t))\right]}_{L_{t-1}}$$

<!-- ELBO 分解为重建项 $L_0$、先验匹配项 $L_T$、去噪匹配项 $L_{t-1}$ -->

### 6.2 各项含义

$$\boxed{L_{\mathrm{VLB}} = L_0 + L_T + \sum_{t=2}^T L_{t-1}}$$

其中：

- **$L_0 = -\mathbb{E}_q[\log p_\theta(x_0 | x_1)]$**：重建损失。给定略带噪声的 $x_1$，重建原始数据 $x_0$ 的交叉熵。

<!-- 从第一步噪声数据恢复原始数据的能力 -->

- **$L_T = D_{\mathrm{KL}}(q(x_T | x_0) \| p(x_T))$**：先验匹配项。前向过程终点与先验分布的KL散度。**无可训练参数**（由噪声调度决定），训练时可忽略。

<!-- 确保最终分布接近先验，与连续DDPM相同 -->

- **$L_{t-1} = \mathbb{E}_q[D_{\mathrm{KL}}(q(x_{t-1} | x_t, x_0) \| p_\theta(x_{t-1} | x_t))]$**：去噪匹配项。要求模型的反向过程 $p_\theta$ 拟合真实后验 $q(x_{t-1}|x_t, x_0)$。

<!-- 这是主要的训练目标，让网络学会去噪 -->

### 6.3 范畴分布之间的 KL 散度

对于两个范畴分布 $p = (p_1, \ldots, p_K)$ 和 $r = (r_1, \ldots, r_K)$：

$$\boxed{D_{\mathrm{KL}}(p \| r) = \sum_{k=1}^K p_k \log \frac{p_k}{r_k}}$$

<!-- 离散 KL 散度，可以精确计算，无需蒙特卡洛估计 -->

**关键优势**：与连续情形不同，离散 KL 散度可以**精确计算**（有限求和），无需蒙特卡洛估计或高斯闭式解。

因此每一项 $L_{t-1}$ 都可以精确写出：

$$L_{t-1} = \mathbb{E}_{q(x_t | x_0)}\left[\sum_{k=1}^K q(x_{t-1} = k | x_t, x_0) \log \frac{q(x_{t-1} = k | x_t, x_0)}{p_\theta(x_{t-1} = k | x_t)}\right]$$

---

## Part 7: Training Objective

### 7.1 反向参数化

网络 $\mu_\theta(x_t, t)$ 需要输出 $p_\theta(x_{t-1} | x_t)$ 的参数。D3PM 提出两种参数化：

**方法 A：直接预测反向转移概率**

$$p_\theta(x_{t-1} | x_t) = \mathrm{Cat}(x_{t-1};\; p = f_\theta(x_t, t))$$

其中 $f_\theta(x_t, t) \in \Delta^{K-1}$（概率单纯形上的向量）。

<!-- 直接输出一个概率向量，最简单但未充分利用结构 -->

**方法 B：预测 $\tilde{p}_\theta(x_0 | x_t)$，然后代入后验公式（推荐）**

让网络预测 "干净数据" 的分布 $\tilde{p}_\theta(\tilde{x}_0 | x_t)$，然后利用后验公式 (Part 4) 计算：

$$p_\theta(x_{t-1} | x_t) = \sum_{\tilde{x}_0} q(x_{t-1} | x_t, \tilde{x}_0)\, \tilde{p}_\theta(\tilde{x}_0 | x_t)$$

**[Austin et al. 2021, Eq.(3)]**

<!-- 类似连续DDPM中预测 $x_0$ 然后代入后验均值公式 -->

展开为概率向量形式：

$$\boxed{p_\theta(x_{t-1} | x_t) = \sum_{\tilde{x}_0=1}^K \tilde{p}_\theta(\tilde{x}_0 | x_t) \cdot \frac{\mathbf{e}_{\tilde{x}_0} \bar{Q}_{t-1} \odot \mathbf{x}_t Q_t^\top}{(\mathbf{e}_{\tilde{x}_0} \bar{Q}_{t-1})(\mathbf{x}_t Q_t^\top)^\top}}$$

其中 $\mathbf{e}_k$ 是第 $k$ 个标准基行向量。

### 7.2 简化训练损失

**完整VLB**训练通常方差较大。Austin et al. 提出辅助损失来稳定训练。

定义**交叉熵辅助损失**：

$$\boxed{L_{\mathrm{CE}} = -\mathbb{E}_{t \sim \mathrm{Uniform}\{1,\ldots,T\},\; q(x_t|x_0)}\left[\log \tilde{p}_\theta(x_0 | x_t)\right]}$$

<!-- 直接用交叉熵衡量网络预测 $x_0$ 的准确度，类似DDPM的简化目标 -->

这等价于对网络预测的 "干净数据分布" 做标准分类交叉熵。

**混合目标**（D3PM 实际使用）**[Austin et al. 2021, Eq.(4)]**：

$$L_{\mathrm{hybrid}} = L_{\mathrm{VLB}} + \lambda \cdot L_{\mathrm{CE}}$$

其中 $\lambda > 0$ 是超参数（Austin et al. 使用 $\lambda = 0.001$）。

<!-- 混合损失兼顾理论完备性和训练稳定性 -->

### 7.3 训练算法

```
Input: 数据集, 网络 f_θ, 噪声调度 {Q_t}
Repeat:
  1. 采样 x_0 ~ 数据集
  2. 采样 t ~ Uniform{1, ..., T}
  3. 采样 x_t ~ Cat(x_t; x_0 @ Q̄_t)     // 用累积矩阵直接采样
  4. 计算网络输出 p̃_θ(x̃_0 | x_t)
  5. 计算 L_VLB(t) + λ · L_CE(t)
  6. 梯度下降更新 θ
```

---

## Part 8: Connection to DIFUSCO

### 8.1 DIFUSCO 概述

DIFUSCO (Sun & Yang, 2023) 将 D3PM 应用于**组合优化**（NP-hard问题），特别是最大独立集（MIS）和旅行商问题（TSP）。

<!-- DIFUSCO: Diffusion for Combinatorial Optimization -->

### 8.2 二值 D3PM 特化（$K = 2$）

对于 MIS 等二值问题，$x_i \in \{0, 1\}$，此时 $K = 2$。

**伯努利噪声**：转移矩阵简化为 $2 \times 2$：

$$Q_t = \begin{pmatrix} 1 - \beta_t & \beta_t \\ \beta_t & 1 - \beta_t \end{pmatrix}$$

<!-- 对称噪声：以 $\beta_t$ 概率翻转比特 -->

累积矩阵：

$$\bar{Q}_t = \begin{pmatrix} \frac{1 + \bar{\alpha}_t}{2} & \frac{1 - \bar{\alpha}_t}{2} \\ \frac{1 - \bar{\alpha}_t}{2} & \frac{1 + \bar{\alpha}_t}{2} \end{pmatrix}, \quad \bar{\alpha}_t = \prod_{s=1}^t (1 - 2\beta_s)$$

<!-- 二值情形下累积矩阵有简洁闭式 -->

边际分布：

$$q(x_t = 1 | x_0) = x_0 \cdot \frac{1 + \bar{\alpha}_t}{2} + (1 - x_0) \cdot \frac{1 - \bar{\alpha}_t}{2}$$

### 8.3 图结构整合

DIFUSCO 的关键创新是在图上定义扩散：

1. **输入表示**：图 $G = (V, E)$，每个节点 $v \in V$ 有二值决策变量 $x_v \in \{0, 1\}$
2. **GNN 去噪网络**：$\tilde{p}_\theta(\tilde{x}_0 | x_t, G) = \mathrm{GNN}_\theta(x_t, G, t)$
3. **前向过程**：对所有节点独立加噪 $q(x_t | x_0) = \prod_{v \in V} q(x_{t,v} | x_{0,v})$
4. **训练目标**：节点级二值交叉熵

<!-- 每个节点独立加噪，GNN利用图结构进行联合去噪 -->

$$L_{\mathrm{DIFUSCO}} = -\mathbb{E}_{t, q(x_t|x_0)}\left[\sum_{v \in V} x_{0,v} \log \tilde{p}_\theta^{(v)} + (1 - x_{0,v}) \log(1 - \tilde{p}_\theta^{(v)})\right]$$

### 8.4 连续松弛与离散扩散

DIFUSCO 实际上同时探索了两种方案：

- **连续扩散**：将 $\{0, 1\}$ 松弛到 $[0, 1]$，用标准高斯扩散，最后阈值化
- **离散扩散**（D3PM）：直接在 $\{0, 1\}$ 上做伯努利扩散

<!-- 实验表明离散扩散在MIS上更好，连续扩散在TSP上更好 -->

---

## Part 9: Sampling Algorithms

### 9.1 祖先采样（Ancestral Sampling）

反向逐步采样：

```
1. 采样 x_T ~ p(x_T)       // 从先验采样（均匀/全MASK）
2. For t = T, T-1, ..., 1:
   a. 计算 p̃_θ(x̃_0 | x_t)   // 网络预测"干净数据"
   b. 计算 p_θ(x_{t-1} | x_t) // 由后验公式得到
   c. 采样 x_{t-1} ~ Cat(x_{t-1}; p_θ(x_{t-1} | x_t))
3. 返回 x_0
```

<!-- 标准的自回归式逆扩散采样 -->

### 9.2 温度调节采样

在采样时引入温度参数 $\tau > 0$ 来控制多样性：

$$p_\theta^{(\tau)}(x_{t-1} = k | x_t) = \frac{p_\theta(x_{t-1} = k | x_t)^{1/\tau}}{\sum_{j} p_\theta(x_{t-1} = j | x_t)^{1/\tau}}$$

<!-- $\tau < 1$ 更确定性（贪心），$\tau > 1$ 更随机（探索） -->

- $\tau \to 0$：贪心采样（argmax），最确定
- $\tau = 1$：标准采样
- $\tau > 1$：增加随机性/探索性

在组合优化中，通常用 $\tau < 1$ 来提高解的质量。

### 9.3 并行解码（Non-autoregressive）

D3PM 的一个重要优势：**所有位置可以并行去噪**。

$$p_\theta(x_{t-1} | x_t) = \prod_{i=1}^N p_\theta(x_{t-1}^{(i)} | x_t)$$

<!-- 各位置条件独立去噪（给定全局信息），允许并行计算 -->

每一步的去噪操作可以同时作用于所有节点/位置，这使得扩散模型在序列/图问题上比自回归模型更高效。

---

## Part 10: Rigorous Results from Austin et al. (2021)

### 10.1 $\mathbf{x}_0$-参数化的推导 **[Austin et al. 2021, Eq.(5)]**

网络预测 $\tilde{p}_\theta(\tilde{\mathbf{x}}_0|\mathbf{x}_t)$，反向过程通过求和得到 **[Austin et al. 2021, Eq.(5)]**：

$$p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t) \propto \sum_{\tilde{\mathbf{x}}_0} q(\mathbf{x}_{t-1}, \mathbf{x}_t|\tilde{\mathbf{x}}_0)\,\tilde{p}_\theta(\tilde{\mathbf{x}}_0|\mathbf{x}_t)$$

**关键性质**：在此参数化下，$D_{\mathrm{KL}}(q(\mathbf{x}_{t-1}|\mathbf{x}_t,\mathbf{x}_0)\|p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)) = 0$ 当且仅当 $\tilde{p}_\theta(\tilde{\mathbf{x}}_0|\mathbf{x}_t)$ 将所有概率集中在真实 $\mathbf{x}_0$ 上。此外，$\mathbf{x}_0$-参数化自动保证反向转移概率 $p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)$ 具有正确的稀疏模式（由 $Q_t$ 决定）。

### 10.2 辅助损失的严格形式 **[Austin et al. 2021, Eq.(6)]**

$$L_\lambda = L_{\mathrm{vb}} + \lambda\,\mathbb{E}_{q(\mathbf{x}_0)}\mathbb{E}_{q(\mathbf{x}_t|\mathbf{x}_0)}[-\log\tilde{p}_\theta(\mathbf{x}_0|\mathbf{x}_t)]$$

辅助项在 $t=1$ 时与 $L_0$（交叉熵重建项）一致。由于 $\mathbf{x}_0$-参数化，$L_{\mathrm{vb}}$ 和辅助项具有**相同的最优解**：$\tilde{p}_\theta(\tilde{\mathbf{x}}_0|\mathbf{x}_t)$ 集中在 $\mathbf{x}_0$ 上。

### 10.3 与 BERT/Masked Language Model 的联系 **[Austin et al. 2021, Appendix E]**

对于吸收态 D3PM（[MASK] 为吸收态），使用 $\beta(t) = 1/(T-t+1)$ 的调度时，VLB 的每一项化为：

$$D_{\mathrm{KL}}(q(\mathbf{x}_{t-1}|\mathbf{x}_t,\mathbf{x}_0)\|p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)) = -\frac{1}{t}\sum_{i: [\mathbf{x}_t]_i = \text{MASK}} \log\tilde{p}_\theta([\mathbf{x}_0]_i|\mathbf{x}_t) + C$$

完整目标退化为：

$$-\mathbb{E}_{q(\mathbf{x}_0)}\left[\sum_{t=1}^T \frac{1}{t}\mathbb{E}_{q(\mathbf{x}_t|\mathbf{x}_0)}\left[\sum_{i: [\mathbf{x}_t]_i = \text{MASK}} \log p_\theta([\mathbf{x}_0]_i|\mathbf{x}_t)\right]\right]$$

这与条件 Masked Language Model (CMLM) 的训练目标几乎一致（差异仅在于 masking 是独立逐位置 vs. 精确选 $k$ 个）。因此 **BERT/MLM 是吸收态 D3PM 的重新加权特例**。

### 10.4 双随机矩阵的收敛定理 **[Austin et al. 2021, Appendix A]**

**定理**：若 $Q_t$ 是具有严格正元素的双随机矩阵（行和与列和均为 1），则 $Q_t$ 是不可约且非周期的，累积矩阵 $\bar{Q}_t = \prod Q_s$ 在 $t \to \infty$ 时收敛到均匀分布 $\frac{1}{K}\mathbf{1}\mathbf{1}^\top$。

**证明要点**：均匀分布 $\pi_i = 1/K$ 是双随机矩阵的特征向量（特征值为1）。由 Perron-Frobenius 定理，对正方阵，这是唯一的平稳分布。

### 10.5 低秩加速的累积矩阵计算 **[Austin et al. 2021, Appendix A.6]**

当 $Q_t = \beta_t A_t + (1-\beta_t)I$ 且 $A_t$ 是低秩矩阵时，$\bar{Q}_t$ 可以高效计算。

对**均匀噪声**：$A^{\text{uniform}} = \frac{1}{K}\mathbf{1}\mathbf{1}^\top$（秩1），$\bar{Q}_t = \bar{\alpha}_t I + (1-\bar{\alpha}_t)\frac{1}{K}\mathbf{1}\mathbf{1}^\top$。

对**吸收噪声**：$A^{\text{absorb}} = \mathbf{1}\mathbf{e}_m^\top$（秩1），$\bar{Q}_t = \bar{\alpha}_t I + (1-\bar{\alpha}_t)\mathbf{1}\mathbf{e}_m^\top$。

存储复杂度从 $O(K^2 T)$ 降至 $O(r^2 T)$（$r$ 为秩）。

---

## Part 11: Continuous-Time Extension **[Campbell et al. 2022]**

### 11.1 CTMC 反向速率的严格推导 **[Campbell et al. 2022, Proposition 1]**

**命题**：对于前向 CTMC（速率矩阵 $R_t$，初始分布 $p_{\text{data}}$），存在一个反向 CTMC（速率矩阵 $\hat{R}_t$），其反向速率为：

$$\hat{R}_t(x, \tilde{x}) = R_t(\tilde{x}, x)\sum_{x_0} \frac{q_{t|0}(\tilde{x}|x_0)}{q_{t|0}(x|x_0)} q_{0|t}(x_0|x), \quad x \neq \tilde{x}$$

其中 $q_{0|t}(x_0|x) = q_{t|0}(x|x_0)p_{\text{data}}(x_0)/q_t(x)$。

### 11.2 连续时间 ELBO **[Campbell et al. 2022, Proposition 2]**

**命题**：负模型对数似然的上界为：

$$\mathcal{L}_{\text{CT}}(\theta) = T\,\mathbb{E}_{t \sim \mathcal{U}(0,T),\,q_t(x),\,r_t(\tilde{x}|x)}\left[\sum_{x' \neq x}\hat{R}_t^\theta(x,x') - \mathcal{Z}^t(x)\log\hat{R}_t^\theta(\tilde{x},x)\right] + C$$

其中 $\mathcal{Z}^t(x) = \sum_{x' \neq x} R_t(x,x')$ 是总转移速率，$r_t(\tilde{x}|x) = (1-\delta_{\tilde{x},x})R_t(x,\tilde{x})/\mathcal{Z}^t(x)$ 是条件转移概率。

### 11.3 维度分解 **[Campbell et al. 2022, Proposition 3]**

**命题**：若前向过程按维度分解 $q_{t|s}(\mathbf{x}_t^{1:D}|\mathbf{x}_s^{1:D}) = \prod_d q_{t|s}(x_t^d|x_s^d)$，则前向和反向速率为：

$$R_t^{1:D}(\tilde{\mathbf{x}}^{1:D}, \mathbf{x}^{1:D}) = \sum_{d=1}^D R_t^d(\tilde{x}^d, x^d)\delta_{\mathbf{x}^{\backslash d}, \tilde{\mathbf{x}}^{\backslash d}}$$

$$\hat{R}_t^{1:D}(\mathbf{x}^{1:D}, \tilde{\mathbf{x}}^{1:D}) = \sum_{d=1}^D R_t^d(\tilde{x}^d, x^d)\delta_{\mathbf{x}^{\backslash d}, \tilde{\mathbf{x}}^{\backslash d}}\sum_{x_0^d} q_{0|t}(x_0^d|\mathbf{x}^{1:D})\frac{q_{t|0}(\tilde{x}^d|x_0^d)}{q_{t|0}(x^d|x_0^d)}$$

关键结果：连续时间过程中，每次转移仅改变**恰好一个维度**（概率为1），这使得 $S^D$ 个速率值中只有 $D \times (S-1) + 1$ 个非零。

### 11.4 Corrector 速率的构造 **[Campbell et al. 2022, Proposition 4]**

**命题**：对于前向速率 $R_t$ 和对应反向速率 $\hat{R}_t$，混合速率 $R_t^c = R_t + \hat{R}_t$ 以 $q_t(x_t)$ 为平稳分布。

这直接类比了连续空间中的 predictor-corrector 方法：predictor 通过反向 SDE 推进时间，corrector 通过基于 score 的 MCMC 修正当前分布。

### 11.5 Tau-Leaping 误差界 **[Campbell et al. 2022, Theorem 1]**

**定理**：对于 $D$ 维数据，每维取 $S$ 个值，前向 CTMC 速率矩阵 $R_t^{1:D}$，反向速率近似 $\hat{R}_t^{\theta,1:D}$ 满足

$$\sum_{y \neq x}|\hat{R}_t^{1:D}(x,y) - \hat{R}_t^{\theta,1:D}(x,y)| \leq M$$

则 tau-leaping 近似 $y_0$ 的分布满足全变差界：

$$\boxed{\|\mathcal{L}(y_0) - p_{\text{data}}\|_{\text{TV}} \leq 3MT + \left\{(|R|SDC_1)^2 + \frac{1}{2}C_2(M + C_1 SD|R|)\right\}\tau T + 2\exp\left\{-\frac{T\log^2 2}{t_{\text{mix}}\log 4D}\right\}}$$

其中 $|R| = \sup_{t,x}|R_t(x,x)|$，$t_{\text{mix}}$ 是前向链的 $(1/4)$-混合时间，$C_1, C_2$ 是不依赖于 $D$ 的常数。

**三项含义**：
1. **第一项 $3MT$**：反向速率近似误差
2. **第二项 $\sim \tau T$**：tau-leaping 离散化误差（$\tau \to 0$ 时消失）
3. **第三项**：前向链混合误差（$q_T \neq p_{\text{ref}}$ 的代价）

误差对维度 $D$ 至多二次增长（而非指数增长），说明 tau-leaping 在高维中仍然可行。

---

## Part 12: DIFUSCO 的数学细节 **[Sun & Yang 2023]**

### 12.1 二值离散扩散的完整后验 **[Sun & Yang 2023, Eq.(5)]**

对于 $K=2$ 的 D3PM，转移矩阵 $Q_t = \begin{pmatrix} 1-\beta_t & \beta_t \\ \beta_t & 1-\beta_t \end{pmatrix}$，后验为：

$$q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0) = \mathrm{Cat}\left(\mathbf{x}_{t-1}; \mathbf{p} = \frac{\tilde{\mathbf{x}}_t Q_t^\top \odot \tilde{\mathbf{x}}_0 \bar{Q}_{t-1}}{\tilde{\mathbf{x}}_0 \bar{Q}_t \tilde{\mathbf{x}}_t^\top}\right)$$

### 12.2 连续扩散用于离散数据 **[Sun & Yang 2023, Section 3.2]**

将 $\{0,1\}$ 变量重缩放到 $\{-1,1\}$，然后应用标准高斯扩散。去噪网络预测未缩放的噪声 $\tilde{\boldsymbol{\epsilon}}_t = f_\theta(\hat{\mathbf{x}}_t, t)$，反向过程使用 $\hat{\mathbf{x}}_0$ 的点估计：

$$p_\theta(\hat{\mathbf{x}}_{t-1}|\hat{\mathbf{x}}_t) = q\left(\hat{\mathbf{x}}_{t-1}\Big|\hat{\mathbf{x}}_t, \frac{\hat{\mathbf{x}}_t - \sqrt{1-\bar{\alpha}_t}f_\theta(\hat{\mathbf{x}}_t, t)}{\sqrt{\bar{\alpha}_t}}\right)$$

最终通过阈值化将连续输出转回 $\{0,1\}$。

### 12.3 实验关键发现

**[Sun & Yang 2023, Section 4]** 的核心实验结论：
- **离散扩散在 MIS 上显著优于连续扩散**（因为 MIS 的决策变量本质离散）
- **连续扩散在 TSP 上可与离散扩散竞争**（因为边缘概率的连续性较好）
- **余弦去噪调度优于线性调度**（在低噪声区间分配更多步数）

---

## Part 13: DiGress — 图上的离散扩散 **[Vignac et al. 2023]**

### 13.1 动机：为什么图需要离散扩散

连续扩散（如 GDSS）对图的邻接矩阵加高斯噪声，会**破坏稀疏性**：原本稀疏的图变成完全图，使得连通性、环计数等结构信息无法定义。离散扩散保持图的离散结构，使噪声图仍有意义的图论性质 **[Vignac et al. 2023, §1]**。

### 13.2 图的表示

图 $G = (\mathbf{X}, \mathbf{E})$ 由两部分组成 **[Vignac et al. 2023, §3]**：

- **节点特征矩阵** $\mathbf{X} \in \mathbb{R}^{n \times a}$：每行 $\mathbf{x}_i \in \mathbb{R}^a$ 是节点 $i$ 类型的 one-hot 编码（$a$ 种节点类型）
- **边特征张量** $\mathbf{E} \in \mathbb{R}^{n \times n \times b}$：$\mathbf{e}_{ij} \in \mathbb{R}^b$ 是边 $(i,j)$ 类型的 one-hot 编码（$b$ 种边类型，含"无边"类型）

### 13.3 图上的前向扩散过程 **[Vignac et al. 2023, §3.1]**

对每个节点和每条边**独立**施加离散噪声。状态空间是节点类型 $\mathcal{X}$（大小 $a$）和边类型 $\mathcal{E}$（大小 $b$），而非整个图空间。

转移概率由矩阵定义：
- $[\mathbf{Q}^t_X]_{ij} = q(x^t = j | x^{t-1} = i)$（节点类型转移）
- $[\mathbf{Q}^t_E]_{ij} = q(e^t = j | e^{t-1} = i)$（边类型转移）

$$\boxed{q(G^t | G^{t-1}) = (\mathbf{X}^{t-1}\mathbf{Q}^t_X,\; \mathbf{E}^{t-1}\mathbf{Q}^t_E)}$$

边际分布（跳过中间步）：

$$\boxed{q(G^t | G) = (\mathbf{X}\bar{\mathbf{Q}}^t_X,\; \mathbf{E}\bar{\mathbf{Q}}^t_E), \quad \bar{\mathbf{Q}}^t_X = \mathbf{Q}^1_X \cdots \mathbf{Q}^t_X}$$

这与 D3PM 的结构完全一致（Part 2-3），只是同时作用于节点和边两个通道。

### 13.4 后验分布与反向采样 **[Vignac et al. 2023, §3.1]**

真实后验（贝叶斯定理）：

$$q(z^{t-1}|z^t, x) \propto \mathbf{z}^t\,(\mathbf{Q}^t)^\top \odot \mathbf{x}\,\bar{\mathbf{Q}}^{t-1}$$

这对节点和边分别适用。

反向采样时，去噪网络 $\phi_\theta$ 预测干净图 $\hat{p}^G = (\hat{p}^X, \hat{p}^E)$，然后对每个节点和边构造反向分布 **[Vignac et al. 2023, Eq.(4)-(5)]**：

$$p_\theta(G^{t-1}|G^t) = \prod_{i} p_\theta(x_i^{t-1}|G^t) \prod_{i,j} p_\theta(e_{ij}^{t-1}|G^t)$$

$$p_\theta(x_i^{t-1}|G^t) = \sum_{x \in \mathcal{X}} q(x_i^{t-1}|x_i=x,\, x_i^t)\;\hat{p}^X_i(x)$$

即对所有可能的干净类型 $x$ 做边际化：用网络预测的概率 $\hat{p}^X_i(x)$ 加权后验。

### 13.5 训练损失 **[Vignac et al. 2023, Eq.(2)]**

DiGress 使用交叉熵损失（而非 VLB）：

$$\boxed{l(\hat{p}^G, G) = \sum_{1 \leq i \leq n} \mathrm{CE}(x_i, \hat{p}^X_i) + \lambda \sum_{1 \leq i,j \leq n} \mathrm{CE}(e_{ij}, \hat{p}^E_{ij})}$$

其中 $\lambda \in \mathbb{R}^+$ 控制节点和边的相对权重。**优势**：将复杂的分布学习问题简化为节点和边的分类任务。

### 13.6 ELBO（似然界）**[Vignac et al. 2023, Appendix D]**

$$\log p_\theta(G) \geq \log p(n_G) + \underbrace{D_{\mathrm{KL}}[q(G^T|G) \| q_X(n_G) \times q_E(n_G)]}_{\text{Prior loss}} + \underbrace{\sum_{t=2}^T L_t(G)}_{\text{Diffusion loss}} + \underbrace{\mathbb{E}_{q(G^1|G)}[\log p_\theta(G|G^1)]}_{\text{Reconstruction loss}}$$

其中 $L_t(G) = \mathbb{E}_{q(G^t|G)}[D_{\mathrm{KL}}[q(G^{t-1}|G^t, G) \| p_\theta(G^{t-1}|G^t)]]$。

所有项均可计算：先验损失和扩散损失是范畴分布间的 KL 散度，重构损失由网络预测概率直接计算。

### 13.7 等变性与可交换性 **[Vignac et al. 2023, §3.3]**

**Lemma 1（等变性）[Vignac et al. 2023, Lemma 3.1]**：DiGress 是置换等变的。

**Lemma 2（不变损失）[Vignac et al. 2023, Lemma 3.2]**：形如 $\sum_i l_X(\hat{p}^X_i, x_i) + \sum_{i,j} l_E(\hat{p}^E_{ij}, e_{ij})$ 的损失是置换不变的。

**Lemma 3（可交换性）[Vignac et al. 2023, Lemma 3.3]**：DiGress 生成可交换分布，即 $\mathbb{P}(\mathbf{X}, \mathbf{A}) = \mathbb{P}(\pi^\top\mathbf{X}, \pi^\top\mathbf{A}\pi)$ 对任意置换 $\pi$。

可交换性是似然计算的必要条件，避免了对 $n!$ 个置换求和。

### 13.8 边际分布保持的噪声模型 **[Vignac et al. 2023, §4.1]**

**问题**：均匀转移噪声 $\mathbf{Q}^t = \alpha^t \mathbf{I} + (1-\alpha^t)\frac{\mathbf{1}\mathbf{1}^\top}{d}$ 的极限分布是均匀分布。但图通常是稀疏的，"无边"类型的概率远大于有边类型，均匀先验与数据分布差距大。

**Theorem（最优先验分布）[Vignac et al. 2023, Theorem 4.1]**：

在因子化分布类 $\mathcal{C} = \{\prod_i u \times \prod_{i,j} v\}$ 中，训练数据分布 $P$ 的最佳近似（$L_2$ 意义下的正交投影）为：

$$\pi^G = \prod_i m_X \times \prod_{i,j} m_E$$

其中 $m_X, m_E$ 分别是节点类型和边类型的**边际分布**。

由此定义边际转移矩阵：

$$\boxed{\mathbf{Q}^t_X = \alpha^t \mathbf{I} + \beta^t\, \mathbf{1}_a\, \mathbf{m}_X^\top, \quad \mathbf{Q}^t_E = \alpha^t \mathbf{I} + \beta^t\, \mathbf{1}_b\, \mathbf{m}_E^\top}$$

性质：$(\mathbf{1}\mathbf{m}^\top)^2 = \mathbf{1}\mathbf{m}^\top$，因此 $\bar{\mathbf{Q}}^t = \bar{\alpha}^t\mathbf{I} + \bar{\beta}^t\mathbf{1}\mathbf{m}^\top$，其中 $\bar{\alpha}^t = \prod_{\tau=1}^t \alpha^\tau$，$\bar{\beta}^t = 1 - \bar{\alpha}^t$。极限分布为边际分布 $m_X$（或 $m_E$），更接近真实数据分布。

### 13.9 结构特征增强 **[Vignac et al. 2023, §4.2]**

离散噪声保持图的稀疏性，使得可以在每个扩散步骤计算**图论描述符**并输入网络，弥补 GNN 的表达能力限制（如无法检测环）。包括：
- 度数特征
- 连通分量信息
- 谱特征（Laplacian 特征向量）
- 环计数等子结构信息

这是离散扩散相比连续扩散的重要优势。

### 13.10 离散 Classifier Guidance **[Vignac et al. 2023, §5]**

**Lemma（条件反向过程）[Vignac et al. 2023, Lemma 5.1]**：

$$\dot{q}(G^{t-1}|G^t, \mathbf{y}_G) \propto q(G^{t-1}|G^t)\;\dot{q}(\mathbf{y}_G|G^{t-1})$$

用回归器 $g_\eta(G^t) = \hat{\mathbf{y}}$ 估计 $\dot{q}(\mathbf{y}_G|G^{t-1})$，假设为高斯 $\mathcal{N}(g(G^t), \sigma_y\mathbf{I})$，通过一阶近似得到对每个节点和边的引导因子：

$$p_\eta(\hat{\mathbf{y}}|G^{t-1}) \propto \exp\left(-\lambda\,\langle \nabla_{G^t}\|\hat{\mathbf{y}} - \mathbf{y}\|^2,\; G^{t-1}\rangle\right)$$

采样时将引导因子乘入反向分布：$G^{t-1} \sim p_\theta(G^{t-1}|G^t)\; p_\eta(\hat{\mathbf{y}}|G^{t-1})$。

### 13.11 与 D3PM 的关系总结

| 方面 | D3PM (Austin et al. 2021) | DiGress (Vignac et al. 2023) |
|---|---|---|
| 数据类型 | 一般离散序列 | 图（节点+边） |
| 状态空间 | 每维 $K$ 类 | 节点 $a$ 类 + 边 $b$ 类 |
| 噪声 | 统一转移矩阵 | 分别对节点/边施加，支持边际分布保持 |
| 训练目标 | VLB（KL散度） | 交叉熵（分类损失） |
| 网络架构 | 通用 | Graph Transformer（等变） |
| 先验分布 | 均匀/吸收态 | 数据边际分布（Theorem 4.1） |
| 结构特征 | 无 | 利用离散稀疏性计算图论特征 |

---

## References

1. Austin, J., Johnson, D.D., Ho, J., Tarlow, D., & van den Berg, R. (2021). *Structured Denoising Diffusion Models in Discrete State-Spaces*. NeurIPS 2021.
2. Ho, J., Jain, A., & Abbeel, P. (2020). *Denoising Diffusion Probabilistic Models*. NeurIPS 2020.
3. Sun, H. & Yang, L. (2023). *DIFUSCO: Graph-based Diffusion Solvers for Combinatorial Optimization*. NeurIPS 2023.
4. Sohl-Dickstein, J., Weiss, E.A., Maheswaranathan, N., & Ganguli, S. (2015). *Deep Unsupervised Learning using Nonequilibrium Thermodynamics*. ICML 2015.
5. Campbell, A., Benton, J., De Bortoli, V., Rainforth, T., Deligiannidis, G., & Doucet, A. (2022). *A Continuous Time Framework for Discrete Denoising Models*. NeurIPS 2022.
6. Vignac, C., Krawczuk, I., Siraudin, A., Wang, B., Cevher, V., & Frossard, P. (2023). *DiGress: Discrete Denoising Diffusion for Graph Generation*. ICLR 2023.
