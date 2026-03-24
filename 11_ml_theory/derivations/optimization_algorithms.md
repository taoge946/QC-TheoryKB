# ML Optimization Algorithms

> **Tags**: `optimization`, `sgd`, `adam`, `learning-rate`, `gradient-clipping`

## Statement

推导机器学习中核心优化算法的数学基础，包括 SGD 收敛理论、Adam 算法及其偏差修正证明、学习率调度策略和梯度裁剪理论。

## Prerequisites

- 凸优化基础：凸函数、Lipschitz 连续梯度
- 概率论：期望、方差、矩
- 随机过程：鞅、随机逼近
- 矩阵分析：正定性、迹

---

## Part 1: SGD Convergence Theory

### 1.1 问题设定

$$\min_\theta f(\theta) = \mathbb{E}_{\xi}[F(\theta; \xi)]$$

其中 $\xi$ 是随机数据样本，$F(\theta; \xi)$ 是单样本损失。

**SGD 更新**：

$$\theta_{t+1} = \theta_t - \alpha_t \nabla F(\theta_t; \xi_t)$$

其中 $g_t = \nabla F(\theta_t; \xi_t)$ 是随机梯度，满足 $\mathbb{E}[g_t | \theta_t] = \nabla f(\theta_t)$。

### 1.2 凸函数的 SGD 收敛

**定理** (Robbins-Monro 条件下的 SGD 收敛)：

设 $f$ 是凸函数，$\nabla f$ 是 $L$-Lipschitz 连续的，随机梯度满足有界方差 $\mathbb{E}[\|g_t - \nabla f(\theta_t)\|^2] \leq \sigma^2$。若步长满足 Robbins-Monro 条件：

$$\sum_{t=1}^\infty \alpha_t = \infty, \quad \sum_{t=1}^\infty \alpha_t^2 < \infty$$

则 $\theta_t \to \theta^*$（a.s.）。

### 1.3 非凸情况的收敛速率

**定理**：设 $f$ 有 $L$-Lipschitz 梯度，$\mathbb{E}[\|g_t - \nabla f(\theta_t)\|^2] \leq \sigma^2$，固定步长 $\alpha = \frac{1}{L\sqrt{T}}$，则：

$$\frac{1}{T}\sum_{t=1}^T \mathbb{E}[\|\nabla f(\theta_t)\|^2] \leq \frac{2L(f(\theta_1) - f^*)}{\sqrt{T}} + \frac{\sigma}{\sqrt{T}}$$

即 $\min_{t \leq T} \mathbb{E}[\|\nabla f(\theta_t)\|^2] = O(1/\sqrt{T})$。

**推导要点**：

由 $L$-光滑性：$f(\theta_{t+1}) \leq f(\theta_t) + \langle \nabla f(\theta_t), \theta_{t+1} - \theta_t \rangle + \frac{L}{2}\|\theta_{t+1} - \theta_t\|^2$

代入 SGD 更新 $\theta_{t+1} - \theta_t = -\alpha g_t$：

$$f(\theta_{t+1}) \leq f(\theta_t) - \alpha \langle \nabla f(\theta_t), g_t \rangle + \frac{L\alpha^2}{2}\|g_t\|^2$$

取期望（利用 $\mathbb{E}[g_t] = \nabla f(\theta_t)$）：

$$\mathbb{E}[f(\theta_{t+1})] \leq \mathbb{E}[f(\theta_t)] - \alpha \|\nabla f(\theta_t)\|^2 + \frac{L\alpha^2}{2}(\|\nabla f(\theta_t)\|^2 + \sigma^2)$$

$$= \mathbb{E}[f(\theta_t)] - \alpha(1 - \frac{L\alpha}{2})\|\nabla f(\theta_t)\|^2 + \frac{L\alpha^2\sigma^2}{2}$$

对 $T$ 步求和并整理，即得收敛速率。

### 1.4 Mini-batch SGD

使用 mini-batch $\mathcal{B}$ 大小为 $B$：

$$g_t = \frac{1}{B}\sum_{i \in \mathcal{B}_t} \nabla F(\theta_t; \xi_i)$$

方差减少为 $\mathbb{E}[\|g_t - \nabla f(\theta_t)\|^2] \leq \frac{\sigma^2}{B}$。

**线性加速**：在固定总计算量下，增大 batch size 等价于减小步长，收敛速率变为 $O(1/\sqrt{BT})$，直到到达梯度噪声下界。

---

## Part 2: Adam Algorithm **[Kingma & Ba 2015]**

### 2.1 动机

不同参数可能有非常不同的梯度尺度。Adam 结合了两种思想：

- **Momentum** (动量)：用梯度的一阶矩（均值）平滑更新方向
- **RMSProp**：用梯度的二阶矩（未中心化方差）自适应调整学习率

### 2.2 Algorithm 1: Adam **[Kingma & Ba 2015, Algorithm 1]**

```
Algorithm: Adam (Adaptive Moment Estimation)
Input: 步长 α = 0.001，衰减率 β₁ = 0.9, β₂ = 0.999，数值稳定 ε = 10⁻⁸
Input: 目标函数 f(θ)，初始参数 θ₀

m₀ ← 0  (一阶矩估计初始化)
v₀ ← 0  (二阶矩估计初始化)
t ← 0

Repeat:
    t ← t + 1
    g_t ← ∇_θ f_t(θ_{t-1})           (计算随机梯度)
    m_t ← β₁ · m_{t-1} + (1 - β₁) · g_t     (更新一阶矩的有偏估计)
    v_t ← β₂ · v_{t-1} + (1 - β₂) · g_t²    (更新二阶矩的有偏估计)
    m̂_t ← m_t / (1 - β₁ᵗ)            (偏差修正一阶矩)
    v̂_t ← v_t / (1 - β₂ᵗ)            (偏差修正二阶矩)
    θ_t ← θ_{t-1} - α · m̂_t / (√v̂_t + ε)   (参数更新)
Until 收敛
Return θ_t
```

**[Kingma & Ba 2015, Algorithm 1]**

### 2.3 偏差修正推导 **[Kingma & Ba 2015, §3]**

**问题**：$m_t$ 和 $v_t$ 的递推初始化为零，导致初期估计有偏。

**一阶矩的偏差分析**：

$$m_t = (1-\beta_1)\sum_{i=1}^t \beta_1^{t-i} g_i$$

取期望（假设 $g_i$ 的分布平稳，即 $\mathbb{E}[g_i] = \mathbb{E}[g_t]$ 对所有 $i$）：

$$\mathbb{E}[m_t] = \mathbb{E}[g_t] \cdot (1-\beta_1)\sum_{i=1}^t \beta_1^{t-i} = \mathbb{E}[g_t] \cdot (1 - \beta_1^t)$$

因此 $\mathbb{E}[m_t] \neq \mathbb{E}[g_t]$（有偏），偏差因子为 $(1-\beta_1^t)$。

**修正**：

$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t} \implies \mathbb{E}[\hat{m}_t] = \mathbb{E}[g_t]$$

**[Kingma & Ba 2015, §3]**

**二阶矩的偏差分析**（完全类似）：

$$v_t = (1-\beta_2)\sum_{i=1}^t \beta_2^{t-i} g_i^2$$

$$\mathbb{E}[v_t] = \mathbb{E}[g_t^2] \cdot (1 - \beta_2^t)$$

修正：$\hat{v}_t = v_t / (1 - \beta_2^t)$。

**偏差修正的重要性**：
- 在训练初期（$t$ 小时），$\beta_1^t \approx 0.9^t$ 和 $\beta_2^t \approx 0.999^t$ 显著偏离 0
- 例如 $t=1$：$\hat{m}_1 = m_1 / 0.1 = 10 m_1$（修正幅度很大）
- 随着 $t \to \infty$，$\beta^t \to 0$，修正因子趋向 1（修正消失）

### 2.4 Adam 更新的直觉

$$\theta_t = \theta_{t-1} - \alpha \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

- **分子** $\hat{m}_t$：动量方向（梯度的指数移动平均）
- **分母** $\sqrt{\hat{v}_t}$：自适应学习率（梯度幅度大的参数步长小，梯度幅度小的参数步长大）
- **效果**：信噪比 (SNR) 高的参数方向更新更大

### 2.5 收敛定理 **[Kingma & Ba 2015, Theorem 4.1]**

**定理** (Adam 在线凸优化的遗憾界)：

设 $f_1, \ldots, f_T$ 是凸函数序列，$\|\nabla f_t(\theta)\|_2 \leq G$，$\|\theta_n - \theta_m\|_2 \leq D$ 对所有 $n, m$。设 $\beta_1, \beta_2$ 满足 $\beta_1^2 / \sqrt{\beta_2} < 1$。则 Adam 的遗憾界为：

$$R_T = \sum_{t=1}^T [f_t(\theta_t) - f_t(\theta^*)] \leq \frac{D^2}{2\alpha(1-\beta_1)}\sum_{i=1}^d \sqrt{T \hat{v}_{T,i}} + \frac{\alpha(1+\beta_1)G_\infty}{(1-\beta_1)\sqrt{1-\beta_2}(1-\gamma)^2}\sum_{i=1}^d \|g_{1:T,i}\|_2$$

**[Kingma & Ba 2015, Theorem 4.1]**

其中 $\gamma = \beta_1^2 / \sqrt{\beta_2}$，$d$ 是参数维度。

**推论**：遗憾界为 $O(\sqrt{T})$，对应平均遗憾 $O(1/\sqrt{T})$，与 SGD 的最优收敛速率相同。

### 2.6 与其他优化器的比较 **[Kingma & Ba 2015, §5]**

| 优化器 | 一阶矩 | 二阶矩 | 偏差修正 | 特点 |
|---|---|---|---|---|
| SGD | 无 | 无 | N/A | 简单，需要仔细调参 |
| SGD + Momentum | $\beta m_{t-1} + g_t$ | 无 | 无 | 加速收敛 |
| AdaGrad | 无 | $\sum g_i^2$ (累积) | 无 | 稀疏数据好，后期步长趋零 |
| RMSProp | 无 | EMA of $g^2$ | 无 | 解决 AdaGrad 衰减问题 |
| **Adam** | EMA of $g$ | EMA of $g^2$ | **有** | 结合动量+自适应LR |
| AdamW | 同 Adam | 同 Adam | 有 | 解耦权重衰减 |

### 2.7 AdamW：解耦权重衰减 **[Loshchilov & Hutter 2019]**

标准 Adam 中 $L_2$ 正则化 $\lambda\|\theta\|^2$ 的梯度 $\lambda\theta$ 也会被自适应学习率缩放，导致正则化效果被削弱。

**AdamW 修正**：将权重衰减从梯度计算中解耦：

$$\theta_t = \theta_{t-1} - \alpha\left(\frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon} + \lambda \theta_{t-1}\right)$$

而非 $g_t = \nabla f_t(\theta) + \lambda\theta$（标准 $L_2$）。

---

## Part 3: Learning Rate Scheduling

### 3.1 为什么需要学习率调度？

- 训练初期：大步长快速下降
- 训练后期：小步长精细调整
- 理论保证：Robbins-Monro 条件要求 $\sum \alpha_t = \infty$, $\sum \alpha_t^2 < \infty$

### 3.2 常见调度策略

**Step Decay**：

$$\alpha_t = \alpha_0 \cdot \gamma^{\lfloor t / s \rfloor}$$

每 $s$ 步衰减为 $\gamma$ 倍（如 $\gamma = 0.1$, $s = 30$ epochs）。

**Cosine Annealing** (Loshchilov & Hutter, 2017)：

$$\alpha_t = \alpha_{\min} + \frac{1}{2}(\alpha_{\max} - \alpha_{\min})\left(1 + \cos\left(\frac{t}{T}\pi\right)\right)$$

平滑衰减，在训练末期接近 $\alpha_{\min}$。

**Linear Warmup + Decay**（Transformer 标准）：

$$\alpha_t = \begin{cases} \alpha_{\max} \cdot t / t_{\text{warmup}} & t \leq t_{\text{warmup}} \\ \alpha_{\max} \cdot \text{decay}(t - t_{\text{warmup}}) & t > t_{\text{warmup}} \end{cases}$$

Warmup 避免训练初期 Adam 的偏差修正不足导致的不稳定。

**Transformer 原始调度** (Vaswani et al., 2017)：

$$\alpha_t = d_{\text{model}}^{-0.5} \cdot \min(t^{-0.5}, t \cdot t_{\text{warmup}}^{-1.5})$$

先线性增长再 $t^{-0.5}$ 衰减。

### 3.3 Warmup 的理论直觉

**问题**：Adam 初期 $\hat{v}_t$ 估计不准确（样本太少），导致：
- 某些参数的 $\sqrt{\hat{v}_t}$ 偏小 $\to$ 有效学习率偏大 $\to$ 参数跳跃

**Warmup 方案**：用小学习率开始，让 $\hat{v}_t$ 先积累足够统计量，再提高学习率。

---

## Part 4: Gradient Clipping Theory

### 4.1 动机

深度网络中的梯度爆炸（gradient explosion）：

$$\|\nabla_\theta \mathcal{L}\| \gg 1$$

可能导致参数更新过大，训练发散。

### 4.2 Gradient Norm Clipping

$$\tilde{g} = \begin{cases} g & \text{if } \|g\| \leq c \\ c \cdot \frac{g}{\|g\|} & \text{if } \|g\| > c \end{cases}$$

等价于：$\tilde{g} = g \cdot \min\left(1, \frac{c}{\|g\|}\right)$

**性质**：
- 保持梯度方向不变（仅缩放范数）
- 阈值 $c$ 通常设为 1.0 或 5.0

### 4.3 Gradient Value Clipping

$$\tilde{g}_i = \operatorname{clip}(g_i, -c, c)$$

逐元素裁剪。注意：这会改变梯度方向。

### 4.4 收敛理论 **[Zhang et al. 2020]**

**定理** (Gradient Clipping SGD 收敛)：设 $f$ 有 $L$-Lipschitz 梯度但梯度方差可能无界（重尾噪声）。使用 gradient clipping SGD，步长 $\alpha = O(T^{-1/4})$，clip 阈值 $c = O(T^{1/4})$：

$$\frac{1}{T}\sum_{t=1}^T \mathbb{E}[\|\nabla f(\theta_t)\|^2] = O\left(\frac{1}{T^{1/4}}\right)$$

**关键洞察**：gradient clipping 使得 SGD 在重尾噪声（非有界方差）下也能收敛，标准 SGD 在这种情况下可能发散。

### 4.5 实践中的 Gradient Clipping

| 应用场景 | Clipping 方式 | 典型阈值 |
|---|---|---|
| RNN/LSTM | Norm clipping | $c = 5.0$ |
| Transformer | Norm clipping | $c = 1.0$ |
| GAN 训练 | Value clipping (WGAN) | $c = 0.01$ |
| 扩散模型 | Norm clipping | $c = 1.0$ |

---

## Summary

ML 优化的核心理论：

$$\underbrace{\text{SGD}}_{\text{基础}} \xrightarrow{\text{动量}} \underbrace{\text{Momentum SGD}}_{\text{加速}} \xrightarrow{\text{自适应LR}} \underbrace{\text{Adam}}_{\text{鲁棒}} \xrightarrow{\text{解耦衰减}} \underbrace{\text{AdamW}}_{\text{当前标准}}$$

辅助技术：
- **学习率调度**：warmup + cosine annealing 是当前最佳实践
- **梯度裁剪**：防止梯度爆炸，在 Transformer/RNN 中必不可少
- **偏差修正**：Adam 的关键创新，确保初期估计无偏

---

## References

1. Robbins, H. & Monro, S. (1951). A Stochastic Approximation Method. Annals of Mathematical Statistics.
2. Kingma, D.P. & Ba, J. (2015). Adam: A Method for Stochastic Optimization. ICLR.
3. Loshchilov, I. & Hutter, F. (2017). SGDR: Stochastic Gradient Descent with Warm Restarts. ICLR.
4. Loshchilov, I. & Hutter, F. (2019). Decoupled Weight Decay Regularization. ICLR.
5. Vaswani, A. et al. (2017). Attention Is All You Need. NeurIPS.
6. Zhang, J. et al. (2020). Why Gradient Clipping Accelerates Training. ICLR.
7. Bottou, L. et al. (2018). Optimization Methods for Large-Scale Machine Learning. SIAM Review.
