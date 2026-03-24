# Discrete Score Matching and Continuous-Time Discrete Diffusion

> **Tags**: `discrete-score`, `concrete-score`, `ratio-matching`, `tau-leaping`, `continuous-time`

## Statement

推导离散数据上的得分函数（Concrete Score）及其匹配方法，建立离散扩散与连续得分模型之间的理论联系，并推导连续时间离散扩散（Campbell et al. 2022）的 tau-leaping 采样框架。

## Prerequisites

- 连续空间得分匹配（见 [score_matching.md](score_matching.md)）
- D3PM 离散扩散框架（见 [discrete_diffusion_d3pm.md](discrete_diffusion_d3pm.md)）
- 连续时间马尔可夫链（CTMC）基础
- 矩阵指数 $e^{tR}$ 的定义和性质
- 常微分方程（ODE）基础

---

## Part 1: Concrete Score — Discrete Analog of Score Function

### 1.1 连续得分的回顾

在连续空间中，得分函数定义为对数概率密度的梯度：

$$s(x) = \nabla_x \log p(x)$$

<!-- 连续得分指向概率密度增长最快的方向 -->

**问题**：对于离散变量 $x \in \{1, \ldots, K\}$，没有梯度算子，$\nabla_x$ 无意义。

### 1.2 Concrete Score 的定义

对于离散分布 $p(x)$，**concrete score**（Meng et al. 2022）定义为：

$$\boxed{s_\theta(x_t)_y \triangleq \log p_\theta(x_0 = y \,|\, x_t), \quad \forall y \in \{1, \ldots, K\}}$$

<!-- Concrete score 是条件对数概率，对每个可能的"干净值"给出一个分数 -->

即对于当前噪声状态 $x_t$，concrete score 是一个 $K$ 维向量，第 $y$ 个分量是网络估计的"$x_0$ 等于 $y$"的对数后验概率。

### 1.3 与连续得分的类比

| 连续得分 | Concrete Score（离散） |
|:---:|:---:|
| $s(x) = \nabla_x \log p(x) \in \mathbb{R}^d$ | $s(x_t)_y = \log p(x_0 = y \| x_t) \in \mathbb{R}^K$ |
| 指向高概率密度方向 | 指出哪些"干净值"最可能 |
| 用于 Langevin 动力学采样 | 用于离散去噪采样 |
| 满足 $\mathbb{E}[\nabla_x \log p] = 0$ | 满足 $\sum_y e^{s(x_t)_y} = 1$（归一化） |

### 1.4 Concrete Score 与 D3PM 的关系

在 D3PM 中，网络 $\tilde{p}_\theta(\tilde{x}_0 | x_t)$ 正是 concrete score 的指数形式：

$$\tilde{p}_\theta(\tilde{x}_0 = y | x_t) = \exp(s_\theta(x_t)_y) = \mathrm{softmax}(\ell_\theta(x_t))_y$$

<!-- 网络的logit输出就是concrete score -->

其中 $\ell_\theta(x_t) \in \mathbb{R}^K$ 是网络的 logit 输出。因此 D3PM 的网络本质上就是在学习 concrete score。

---

## Part 2: Ratio Matching — Discrete Denoising Score Matching

### 2.1 动机

在连续空间中，去噪得分匹配（Denoising Score Matching, DSM）的目标是：

$$L_{\mathrm{DSM}} = \mathbb{E}_{q(x_t, x_0)}\left[\|s_\theta(x_t) - \nabla_{x_t} \log q(x_t | x_0)\|^2\right]$$

<!-- 连续DSM：让网络得分匹配条件得分 -->

离散空间没有梯度，需要找到类比物。

### 2.2 离散得分的比率形式

定义离散条件"得分"为**概率比率**（ratio）：

$$r(x_t, y) \triangleq \frac{p(x_t^{(y)})}{p(x_t)}$$

<!-- 概率比率衡量"如果把 $x_t$ 换成 $y$，概率会变化多少" -->

其中 $x_t^{(y)}$ 表示将 $x_t$ 的值替换为 $y$（对于多维情形，替换某个特定位置）。

**直觉**：在连续空间中，$\nabla_x \log p(x)$ 可以理解为"沿某方向微扰 $x$，对数概率变化多少"。在离散空间中，将 $x$ 替换为 $y$ 是离散版本的"微扰"，概率的比率就是离散版本的"得分"。

### 2.3 Ratio Matching 目标

**Ratio Matching**（Hyvarinen, 2007）定义目标函数：

$$\boxed{L_{\mathrm{RM}} = \mathbb{E}_{p(x)}\left[\sum_{y \neq x} \left(1 - \sqrt{\frac{r_\theta(x, y)}{r_{\mathrm{true}}(x, y)}}\right)^2\right]}$$

<!-- 让网络学习的概率比率匹配真实比率 -->

其中 $r_\theta(x, y) = \frac{p_\theta(y)}{p_\theta(x)}$ 是模型的概率比率，$r_{\mathrm{true}}(x, y) = \frac{p_{\mathrm{data}}(y)}{p_{\mathrm{data}}(x)}$ 是真实比率。

**关键性质**：类似于连续得分匹配可以消除对 $\nabla_x \log p_{\mathrm{data}}$ 的依赖，ratio matching 可以变换为不需要 $p_{\mathrm{data}}$ 的形式。

### 2.4 去噪版 Ratio Matching

类比连续 DSM，在噪声条件下定义：

$$L_{\mathrm{DRM}} = \mathbb{E}_{t,\, q(x_0),\, q(x_t|x_0)}\left[\sum_{y=1}^K w(x_t, y) \left(\log r_\theta(x_t, y) - \log \frac{q(x_t^{(y)} | x_0)}{q(x_t | x_0)}\right)^2\right]$$

<!-- 去噪ratio matching：在噪声条件下匹配条件概率比率 -->

其中 $w(x_t, y)$ 是权重函数，$q(x_t | x_0)$ 来自 D3PM 前向过程。

**代入 D3PM 前向过程**：

$$\frac{q(x_t^{(y)} | x_0)}{q(x_t | x_0)} = \frac{[\bar{Q}_t]_{x_0, y}}{[\bar{Q}_t]_{x_0, x_t}}$$

<!-- 条件概率比率可以从累积转移矩阵直接读出 -->

这个比率可以直接从累积转移矩阵 $\bar{Q}_t$ 中读出，完全已知。

---

## Part 3: Connection to Continuous Score-Based Methods

### 3.1 从离散到连续的极限

考虑离散状态空间 $\{0, \frac{1}{N}, \frac{2}{N}, \ldots, 1\}$，当 $N \to \infty$ 时：

**离散转移矩阵** $\to$ **连续转移核**：

$$[Q_t]_{ij} \to q(x_t | x_{t-1}) \, dx_t$$

<!-- 离散转移矩阵在连续极限下变为转移核 -->

**离散化高斯噪声矩阵**（Part 5.3 of D3PM）：

$$[Q_t^{\mathrm{gauss}}]_{ij} \propto \exp\left(-\frac{(i/N - j/N)^2}{2\sigma_t^2}\right)$$

当 $N \to \infty$，$\sigma_t \to 0$（适当缩放）时，这收敛到高斯转移核：

$$q(x_t | x_{t-1}) = \mathcal{N}(x_t; x_{t-1}, \sigma_t^2)$$

<!-- 离散化高斯噪声在连续极限下恢复连续高斯扩散 -->

即**连续高斯扩散是离散化高斯 D3PM 的连续极限**。

### 3.2 Concrete Score 与 Continuous Score 的关系

在上述连续极限下：

$$s_\theta(x_t)_y = \log p_\theta(x_0 = y | x_t) \longrightarrow \log p_\theta(x_0 | x_t)$$

而由 Tweedie's formula（连续情形）：

$$\mathbb{E}[x_0 | x_t] = x_t + \sigma_t^2 \nabla_{x_t} \log p(x_t)$$

因此 concrete score 中包含的信息（$x_0$ 的后验分布）在连续极限下退化为 $x_0$ 的后验均值，后者由连续得分函数唯一确定。

<!-- Concrete score 是比连续得分更丰富的对象：它给出完整后验，而非仅仅均值 -->

**关键区别**：

- **连续得分**：$\nabla_x \log p(x_t) \in \mathbb{R}^d$，给出一个方向（$x_0$ 的后验均值方向）
- **Concrete score**：$s(x_t) \in \mathbb{R}^K$，给出完整后验分布（每个类别的概率）
- Concrete score 严格地比连续得分信息更丰富

### 3.3 统一框架

| 概念 | 连续 | 离散 |
|:---|:---|:---|
| 状态空间 | $\mathbb{R}^d$ | $\{1, \ldots, K\}$ |
| 噪声 | 高斯 $\mathcal{N}(0, \sigma^2 I)$ | 转移矩阵 $Q_t$ |
| 得分 | $\nabla_x \log p(x)$ | $\log p(x_0 = \cdot \| x_t)$ |
| 得分匹配 | DSM（$L^2$ 损失） | Ratio Matching |
| 采样 | Langevin / SDE 求解器 | 祖先采样 / Tau-leaping |
| 先验 | $\mathcal{N}(0, I)$ | 均匀 / 吸收态 |

---

## Part 4: Continuous-Time Discrete Diffusion and Tau-Leaping

### 4.1 从离散时间到连续时间

D3PM 使用**离散时间步** $t \in \{1, \ldots, T\}$。Campbell et al. (2022) 将其推广到**连续时间** $t \in [0, 1]$。

<!-- 连续时间公式更优雅，且允许自适应步长 -->

**连续时间马尔可夫链（CTMC）**：状态空间 $\{1, \ldots, K\}$，由**速率矩阵**（rate matrix）$R_t \in \mathbb{R}^{K \times K}$ 控制：

$$\frac{d}{dt} q(x_t | x_0) = q(x_t | x_0)\, R_t$$

<!-- Kolmogorov 前向方程的矩阵形式 -->

$R_t$ 满足：
- $[R_t]_{ij} \geq 0$ for $i \neq j$（非对角元素非负，表示从 $i$ 跳到 $j$ 的速率）
- $[R_t]_{ii} = -\sum_{j \neq i} [R_t]_{ij}$（每行之和为0）

### 4.2 与离散时间的关系

离散时间的转移矩阵 $Q_t$ 与连续时间的速率矩阵 $R_t$ 的关系：

$$Q_{\Delta t} = I + R_t \Delta t + O((\Delta t)^2) \approx \exp(R_t \Delta t)$$

<!-- 转移矩阵是速率矩阵的矩阵指数 -->

**精确关系**：

$$\bar{Q}(t) = \mathcal{T}\exp\left(\int_0^t R_s\, ds\right)$$

其中 $\mathcal{T}\exp$ 是时序指数（time-ordered exponential）。当 $R_t$ 不随时间变化时简化为普通矩阵指数 $\bar{Q}(t) = e^{tR}$。

### 4.3 常见连续时间速率矩阵

**均匀速率**：

$$R^{\mathrm{uniform}} = \sigma(t)\left(\frac{1}{K}\mathbf{1}\mathbf{1}^\top - I\right)$$

<!-- 均匀速率：以相等概率跳到任何其他状态 -->

其中 $\sigma(t) > 0$ 是时间依赖的标量速率。

**吸收速率**（对应 D3PM 吸收噪声）：

$$[R^{\mathrm{absorb}}]_{ij} = \begin{cases} \sigma(t) & \text{if } j = \mathrm{MASK} \text{ and } i \neq \mathrm{MASK} \\ -\sigma(t) & \text{if } i = j \text{ and } i \neq \mathrm{MASK} \\ 0 & \text{otherwise} \end{cases}$$

### 4.4 连续时间 ELBO

连续时间的ELBO可以表示为积分形式：

$$\log p_\theta(x_0) \geq -\int_0^1 \mathbb{E}_{q(x_t|x_0)}\left[\sum_{y \neq x_t} R_t(x_t, y) \log \frac{R_t(x_t, y)}{R_t^\theta(x_t, y)}\right] dt - D_{\mathrm{KL}}(q(x_1 | x_0) \| p(x_1))$$

<!-- 连续时间ELBO自然地表示为对时间的积分 -->

其中 $R_t^\theta(x_t, y)$ 是反向过程的速率矩阵，由网络参数化。

### 4.5 反向 CTMC **[Campbell et al. 2022, Proposition 1]**

**前向 CTMC** 的反向过程也是 CTMC，其反向速率矩阵为 **[Campbell et al. 2022, Proposition 1]**：

$$\boxed{\overleftarrow{R}_t(x_t, y) = R_t(y, x_t) \frac{p_t(y)}{p_t(x_t)}, \quad y \neq x_t}$$

<!-- 这是离散版本的 Anderson 反向 SDE -->

这是**离散版的 Anderson 反向 SDE**。比率 $\frac{p_t(y)}{p_t(x_t)}$ 正是离散得分（ratio）。

**给定 $x_0$ 的条件反向速率**：

$$\overleftarrow{R}_t(x_t, y | x_0) = R_t(y, x_t) \frac{q(x_t = y | x_0)}{q(x_t | x_0)} = R_t(y, x_t) \frac{[\bar{Q}(t)]_{x_0, y}}{[\bar{Q}(t)]_{x_0, x_t}}$$

<!-- 条件反向速率可以从前向过程直接计算 -->

### 4.6 Tau-Leaping 采样

直接模拟 CTMC 的反向过程（精确的 Gillespie 算法）效率低。**Tau-leaping** 是一种加速方法：

<!-- Tau-leaping 是化学模拟中的经典加速方法，此处用于离散扩散采样 -->

**算法**：

```
1. 采样 x_1 ~ p(x_1)                    // 从先验采样
2. 设定时间步 τ = 1/N
3. For t = 1, 1-τ, 1-2τ, ..., τ:
   a. 计算反向速率 R̃_t^θ(x_t, y) for all y ≠ x_t
   b. 计算跳转概率:
      P(x_t → y) = R̃_t^θ(x_t, y) · τ,  y ≠ x_t
      P(x_t → x_t) = 1 - Σ_{y≠x_t} R̃_t^θ(x_t, y) · τ
   c. 采样 x_{t-τ} ~ Cat(x_{t-τ}; P(x_t → ·))
4. 返回 x_0
```

**关键近似**：在时间步 $\tau$ 内，假设速率恒定，则跳转概率近似为速率乘以时间步：

$$p(x_{t-\tau} = y | x_t) \approx \begin{cases} \overleftarrow{R}_t^\theta(x_t, y) \cdot \tau & y \neq x_t \\ 1 - \sum_{y \neq x_t} \overleftarrow{R}_t^\theta(x_t, y) \cdot \tau & y = x_t \end{cases}$$

<!-- 线性近似：$e^{R\tau} \approx I + R\tau$，当 $\tau$ 足够小时精确 -->

**要求**：$\tau$ 足够小使得所有概率非负，即 $\tau < \frac{1}{\max_{x_t} \sum_{y} \overleftarrow{R}_t(x_t, y)}$。

### 4.7 Tau-Leaping 与 D3PM 祖先采样的等价性

当选择特定的时间离散化，tau-leaping 退化为 D3PM 的祖先采样：

设连续时间 $[0, 1]$ 被等分为 $T$ 步，$\tau = 1/T$，且速率矩阵在每个区间内恒定 $R_t = R_{k/T}$ for $t \in [k/T, (k+1)/T)$，则：

$$Q_{k} = I + R_{k/T} \cdot \frac{1}{T} \approx \exp\left(\frac{R_{k/T}}{T}\right)$$

<!-- 离散时间D3PM是连续时间tau-leaping的特例 -->

这正是 D3PM 的转移矩阵。因此 **D3PM 是连续时间离散扩散 + tau-leaping 采样的特例**。

### 4.8 自适应步长的优势

连续时间公式的核心优势：**可以使用自适应步长**。

- 在噪声变化剧烈的区间（通常是 $t$ 接近 0 或 1 时）用小步长
- 在噪声变化平缓的区间用大步长
- 这类似于连续扩散中 ODE/SDE 求解器的自适应步长控制

<!-- 自适应步长允许用更少的函数评估达到相同精度 -->

**误差控制**：tau-leaping 的局部截断误差为 $O(\tau^2)$，全局误差为 $O(\tau)$。通过选择合适的 $\tau(t)$，可以在采样质量和速度之间灵活权衡。

---

## Part 5: Advanced Topics

### 5.1 Predictor-Corrector 采样

类比连续扩散中的 predictor-corrector 方法：

1. **Predictor 步**：用 tau-leaping 向前推进一步
2. **Corrector 步**：在当前时刻做几步 MCMC（如 Gibbs 采样），利用网络输出的 concrete score 作为目标分布

$$x_t^{(\text{corrected})} \sim p_\theta^{(\text{Gibbs})}(x_t | \text{neighbors of } x_t)$$

<!-- Corrector 步提高每个时间步的采样质量 -->

### 5.2 离散扩散的模式坍缩问题

与连续扩散不同，离散扩散存在特有的挑战：

1. **零概率陷阱**：如果 $q(x_{t-1} = j | x_t, x_0)$ 对某些 $j$ 精确为零，而网络给出非零概率，KL散度无穷大
2. **缓解方法**：在后验中加入微小的平滑项 $\epsilon$，或使用截断（clamping）

$$\tilde{q}(x_{t-1} | x_t, x_0) = (1 - \epsilon) \cdot q(x_{t-1} | x_t, x_0) + \frac{\epsilon}{K}$$

<!-- 平滑后验避免数值不稳定 -->

---

## Part 6: Rigorous Results from Campbell et al. (2022)

### 6.1 CTMC 反向速率的参数化 **[Campbell et al. 2022, Eq.(5)]**

将 $q_{0|t}(x_0|x)$ 用参数化去噪模型 $p_{0|t}^\theta(x_0|x)$ 近似：

$$\hat{R}_t^\theta(x, \tilde{x}) = R_t(\tilde{x}, x)\sum_{x_0}\frac{q_{t|0}(\tilde{x}|x_0)}{q_{t|0}(x|x_0)}p_{0|t}^\theta(x_0|x), \quad x \neq \tilde{x}$$

**关键观察**：这与离散时间参数化反向核 $p_{k|k+1}^\theta$ 形式相同（参见 Austin et al. 的 $\mathbf{x}_0$-参数化），只是将前向核 $q_{k+1|k}$ 替换为前向速率 $R_t$。

### 6.2 前向过程的特征分解 **[Campbell et al. 2022, Section 4.1]**

当 $R_t = \beta(t)R_b$（$R_b$ 为时间无关的基速率矩阵），Kolmogorov 微分方程可解析求解：

$$q_{t|0}(x=j|x_0=i) = \left(Q\exp\left[\Lambda\int_0^t\beta(s)ds\right]Q^{-1}\right)_{ij}$$

其中 $R_b = Q\Lambda Q^{-1}$ 是特征分解，$\exp[\cdot]$ 是逐元素指数。

具体的 $R_b$ 选择：
- **均匀速率**：$R_b = \mathbf{1}\mathbf{1}^\top - S\,\mathrm{Id}$（所有非对角元素相等）
- **吸收速率**：仅 $R_b(i, \text{MASK}) > 0$（$i \neq \text{MASK}$）

### 6.3 连续时间 ELBO 的直观解释 **[Campbell et al. 2022, Proposition 2, Eq.(6)]**

$\mathcal{L}_{\text{CT}}$ 中的两项有清晰的直觉：

- **第二项** $-\mathcal{Z}^t(x)\log\hat{R}_t^\theta(\tilde{x}, x)$：最大化从 $\tilde{x}$ 到 $x$ 的反向速率（即学习反转噪声过程）
- **第一项** $\sum_{x' \neq x}\hat{R}_t^\theta(x, x')$：正则化项，防止所有反向速率都变得过大

训练时只需对 $\tilde{x}$ 做一次网络前向传播（通过近似 $x \approx \tilde{x}$，因为 $\tilde{x}$ 近似服从 $q_{t+\delta t}$）。

### 6.4 Tau-Leaping 的具体更新规则 **[Campbell et al. 2022, §4.3, Proposition 3]**

给定当前状态 $\mathbf{x}_t^{1:D}$，tau-leaping 步骤 $t \to t-\tau$：

1. 对每个维度 $d$ 和每个可能的目标状态 $s \neq x_t^d$，采样 $P_{ds} \sim \mathrm{Poisson}(\tau\,\hat{R}_t^{\theta,1:D}(\mathbf{x}_t, \mathbf{x}_t + (s-x_t^d)\mathbf{e}^d))$
2. 同时应用所有转移：$\mathbf{x}_{t-\tau}^{1:D} = \mathbf{x}_t^{1:D} + \sum_d\sum_{s \neq x_t^d} P_{ds}(s - x_t^d)\mathbf{e}^d$

**对非有序数据**：若某维度 $d$ 的总跳转次数 $\sum_s P_{ds} > 1$，则拒绝该维度的更新（回退到 $x_t^d$）。

与 D3PM 祖先采样的关系：当 $\tau = 1/T$ 且速率矩阵在每个区间内恒定时，tau-leaping 退化为 D3PM 的祖先采样。

---

## References

1. Meng, C., He, Y., Song, Y., Song, J., Wu, J., Zhu, J.-Y., & Ermon, S. (2022). *Concrete Score Matching: Generalized Score Matching for Discrete Data*. NeurIPS 2022.
2. Campbell, A., Benton, J., De Bortoli, V., Rainforth, T., Deligiannidis, G., & Doucet, A. (2022). *A Continuous Time Framework for Discrete Denoising Models*. NeurIPS 2022.
3. Hyvarinen, A. (2007). *Some Extensions of Score Matching*. Computational Statistics & Data Analysis.
4. Austin, J., Johnson, D.D., Ho, J., Tarlow, D., & van den Berg, R. (2021). *Structured Denoising Diffusion Models in Discrete State-Spaces*. NeurIPS 2021.
5. Lou, A., Meng, C., & Ermon, S. (2024). *Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution*. ICML 2024.
6. Sun, H. & Yang, L. (2023). *DIFUSCO: Graph-based Diffusion Solvers for Combinatorial Optimization*. NeurIPS 2023.
