# Diffusion Models: Complete Mathematical Framework

> **Tags**: `diffusion`, `ddpm`, `generative-model`, `score-matching`

## Statement

推导扩散生成模型（Denoising Diffusion Probabilistic Models, DDPM）及基于得分的生成模型（Score-Based Generative Models）的完整数学框架。从变分自编码器（VAE）出发，定义前向扩散过程，推导闭式解，推导反向过程，简化训练目标，并建立与得分匹配的联系。

## Prerequisites

- 概率论基础：条件概率、贝叶斯定理、边际化
- 高斯分布及其性质（线性组合仍为高斯）
- KL散度及其高斯闭式解（见 [elbo_derivation.md](elbo_derivation.md)）
- 变分推断与ELBO（见 [elbo_derivation.md](elbo_derivation.md)）
- 随机微分方程基础（见 [langevin_dynamics.md](langevin_dynamics.md)）

---

## Part 1: From VAE to Diffusion — Hierarchical VAE Perspective

### 1.1 回顾 VAE

标准VAE有一层隐变量 $z$：

$$\log p(x) \geq \mathbb{E}_{q(z|x)}[\log p(x|z)] - D_{\mathrm{KL}}(q(z|x) \| p(z)) = \mathcal{L}_{\mathrm{ELBO}}$$

**扩散模型可以看成一个有 $T$ 层隐变量的层级VAE**，其中隐变量为 $x_1, x_2, \ldots, x_T$。

### 1.2 层级 VAE 的 ELBO

对于联合分布 $p(x_0, x_1, \ldots, x_T)$，ELBO为：

$$\log p(x_0) \geq \mathbb{E}_{q(x_{1:T}|x_0)}\left[\log \frac{p(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

---

## Part 2: Forward Diffusion Process

### 2.1 定义前向过程 **[Ho et al. 2020, Eq.(2)]**

前向过程是一个马尔可夫链，逐步向数据加入高斯噪声 **[Ho et al. 2020, Eq.(2)]**：

$$q(x_t | x_{t-1}) = \mathcal{N}(x_t;\; \sqrt{1 - \beta_t}\, x_{t-1},\; \beta_t \mathbf{I})$$

其中 $\beta_t \in (0, 1)$ 是噪声调度（noise schedule），$t = 1, \ldots, T$。

联合前向过程：

$$q(x_{1:T} | x_0) = \prod_{t=1}^{T} q(x_t | x_{t-1})$$

### 2.2 推导 $q(x_t | x_0)$ 的闭式解

**目标**：跳过中间步，直接从 $x_0$ 得到 $x_t$ 的分布。

定义 $\alpha_t = 1 - \beta_t$，$\bar{\alpha}_t = \prod_{s=1}^t \alpha_s$。

**第1步**：写出单步采样

$$x_t = \sqrt{\alpha_t}\, x_{t-1} + \sqrt{\beta_t}\, \epsilon_{t-1}, \quad \epsilon_{t-1} \sim \mathcal{N}(0, \mathbf{I})$$

**第2步**：递归展开

$$x_t = \sqrt{\alpha_t}\, x_{t-1} + \sqrt{1 - \alpha_t}\, \epsilon_{t-1}$$

代入 $x_{t-1} = \sqrt{\alpha_{t-1}}\, x_{t-2} + \sqrt{1 - \alpha_{t-1}}\, \epsilon_{t-2}$：

$$x_t = \sqrt{\alpha_t \alpha_{t-1}}\, x_{t-2} + \sqrt{\alpha_t(1 - \alpha_{t-1})}\, \epsilon_{t-2} + \sqrt{1 - \alpha_t}\, \epsilon_{t-1}$$

**第3步**：合并高斯噪声

两个独立高斯 $\mathcal{N}(0, \sigma_1^2 I)$ 和 $\mathcal{N}(0, \sigma_2^2 I)$ 之和服从 $\mathcal{N}(0, (\sigma_1^2 + \sigma_2^2) I)$。

后两项的方差之和：

$$\alpha_t(1 - \alpha_{t-1}) + (1 - \alpha_t) = \alpha_t - \alpha_t \alpha_{t-1} + 1 - \alpha_t = 1 - \alpha_t \alpha_{t-1}$$

所以：

$$x_t = \sqrt{\alpha_t \alpha_{t-1}}\, x_{t-2} + \sqrt{1 - \alpha_t \alpha_{t-1}}\, \bar{\epsilon}_{t-2}$$

**第4步**：归纳法得出一般结论

重复此过程直到 $x_0$：

$$\boxed{x_t = \sqrt{\bar{\alpha}_t}\, x_0 + \sqrt{1 - \bar{\alpha}_t}\, \epsilon, \quad \epsilon \sim \mathcal{N}(0, \mathbf{I})}$$

等价地写成分布形式：

$$\boxed{q(x_t | x_0) = \mathcal{N}\left(x_t;\; \sqrt{\bar{\alpha}_t}\, x_0,\; (1 - \bar{\alpha}_t)\mathbf{I}\right)}$$

**[Ho et al. 2020, Eq.(4)]**

### 2.3 性质分析

- 当 $t = 0$：$\bar{\alpha}_0 = 1$，$q(x_0|x_0) = \delta(x_0)$（确定性）
- 当 $t \to T$：$\bar{\alpha}_T \approx 0$，$q(x_T|x_0) \approx \mathcal{N}(0, \mathbf{I})$（纯噪声）
- 信噪比 (SNR)：$\mathrm{SNR}(t) = \bar{\alpha}_t / (1 - \bar{\alpha}_t)$，随 $t$ 单调递减

---

## Part 3: Reverse Process

### 3.1 反向过程定义

我们用参数化的高斯来近似真实后验 $q(x_{t-1}|x_t)$：

$$p_\theta(x_{t-1}|x_t) = \mathcal{N}(x_{t-1};\; \mu_\theta(x_t, t),\; \Sigma_\theta(x_t, t))$$

### 3.2 推导真实后验 $q(x_{t-1} | x_t, x_0)$

利用贝叶斯定理：

$$q(x_{t-1} | x_t, x_0) = \frac{q(x_t | x_{t-1}, x_0)\, q(x_{t-1} | x_0)}{q(x_t | x_0)}$$

由马尔可夫性 $q(x_t | x_{t-1}, x_0) = q(x_t | x_{t-1})$，三个分布都是已知的高斯：

$$q(x_t | x_{t-1}) = \mathcal{N}(x_t;\; \sqrt{\alpha_t}\, x_{t-1},\; (1-\alpha_t)\mathbf{I})$$

$$q(x_{t-1} | x_0) = \mathcal{N}(x_{t-1};\; \sqrt{\bar{\alpha}_{t-1}}\, x_0,\; (1-\bar{\alpha}_{t-1})\mathbf{I})$$

$$q(x_t | x_0) = \mathcal{N}(x_t;\; \sqrt{\bar{\alpha}_t}\, x_0,\; (1-\bar{\alpha}_t)\mathbf{I})$$

**第1步**：取对数并展开指数部分（只保留关于 $x_{t-1}$ 的项）

$$\log q(x_{t-1}|x_t, x_0) \propto -\frac{1}{2}\left[\frac{(x_t - \sqrt{\alpha_t} x_{t-1})^2}{1 - \alpha_t} + \frac{(x_{t-1} - \sqrt{\bar{\alpha}_{t-1}} x_0)^2}{1 - \bar{\alpha}_{t-1}}\right]$$

**第2步**：展开平方项，收集 $x_{t-1}$ 的二次项和一次项

$$= -\frac{1}{2}\left[\left(\frac{\alpha_t}{1-\alpha_t} + \frac{1}{1-\bar{\alpha}_{t-1}}\right)x_{t-1}^2 - 2\left(\frac{\sqrt{\alpha_t}\, x_t}{1-\alpha_t} + \frac{\sqrt{\bar{\alpha}_{t-1}}\, x_0}{1-\bar{\alpha}_{t-1}}\right)x_{t-1} + C\right]$$

**第3步**：配方得到后验方差

$$\tilde{\beta}_t = \frac{1}{\frac{\alpha_t}{1-\alpha_t} + \frac{1}{1-\bar{\alpha}_{t-1}}} = \frac{(1-\alpha_t)(1-\bar{\alpha}_{t-1})}{1 - \bar{\alpha}_t}$$

验证：分母 $\frac{\alpha_t(1-\bar{\alpha}_{t-1}) + (1-\alpha_t)}{(1-\alpha_t)(1-\bar{\alpha}_{t-1})} = \frac{1 - \bar{\alpha}_t}{(1-\alpha_t)(1-\bar{\alpha}_{t-1})}$，取倒数即得。

**第4步**：后验均值

$$\tilde{\mu}_t(x_t, x_0) = \tilde{\beta}_t \left(\frac{\sqrt{\alpha_t}}{1-\alpha_t}\, x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}}{1-\bar{\alpha}_{t-1}}\, x_0\right)$$

代入 $\tilde{\beta}_t$ 化简：

$$\boxed{\tilde{\mu}_t(x_t, x_0) = \frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}\, x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\, \beta_t}{1-\bar{\alpha}_t}\, x_0}$$

所以真实后验为：

$$\boxed{q(x_{t-1}|x_t, x_0) = \mathcal{N}\left(x_{t-1};\; \tilde{\mu}_t(x_t, x_0),\; \tilde{\beta}_t \mathbf{I}\right)}$$

**[Ho et al. 2020, Eq.(6)-(7)]**

### 3.3 用 $\epsilon$ 参数化均值

由 $x_0 = \frac{x_t - \sqrt{1-\bar{\alpha}_t}\,\epsilon}{\sqrt{\bar{\alpha}_t}}$ 代入 $\tilde{\mu}_t$：

$$\tilde{\mu}_t = \frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}\, x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\, \beta_t}{1-\bar{\alpha}_t} \cdot \frac{x_t - \sqrt{1-\bar{\alpha}_t}\,\epsilon}{\sqrt{\bar{\alpha}_t}}$$

整理 $x_t$ 的系数：

$$\frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t} + \frac{\beta_t}{(1-\bar{\alpha}_t)\sqrt{\alpha_t}} = \frac{\alpha_t(1-\bar{\alpha}_{t-1}) + \beta_t}{(1-\bar{\alpha}_t)\sqrt{\alpha_t}}$$

分子：$\alpha_t - \bar{\alpha}_t + 1 - \alpha_t = 1 - \bar{\alpha}_t$

所以 $x_t$ 系数 $= \frac{1}{\sqrt{\alpha_t}}$

整理 $\epsilon$ 的系数：$-\frac{\beta_t}{(1-\bar{\alpha}_t)\sqrt{\alpha_t}} \cdot \sqrt{1-\bar{\alpha}_t} = -\frac{\beta_t}{\sqrt{\alpha_t}\sqrt{1-\bar{\alpha}_t}}$

最终：

$$\boxed{\tilde{\mu}_t = \frac{1}{\sqrt{\alpha_t}}\left(x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\,\epsilon\right)}$$

因此，如果网络 $\epsilon_\theta(x_t, t)$ 预测噪声 $\epsilon$，则反向过程均值为 **[Ho et al. 2020, Eq.(11)]**：

$$\mu_\theta(x_t, t) = \frac{1}{\sqrt{\alpha_t}}\left(x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\,\epsilon_\theta(x_t, t)\right)$$

---

## Part 4: Deriving the Training Objective

### 4.1 扩散模型的变分下界 (VLB) **[Ho et al. 2020, Eq.(3)]**

$$\mathcal{L}_{\mathrm{VLB}} = \mathbb{E}_{q}\left[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

展开 **[Ho et al. 2020, Eq.(3)]**：

$$= \mathbb{E}_q\left[-\log p(x_T) - \sum_{t=1}^{T} \log \frac{p_\theta(x_{t-1}|x_t)}{q(x_t|x_{t-1})}\right]$$

**关键变换**：将 $q(x_t|x_{t-1})$ 改写为 $\frac{q(x_{t-1}|x_t, x_0)\, q(x_t|x_0)}{q(x_{t-1}|x_0)}$（贝叶斯定理）。

经过整理（telescoping），VLB可以分解为：

$$\mathcal{L}_{\mathrm{VLB}} = \underbrace{D_{\mathrm{KL}}(q(x_T|x_0) \| p(x_T))}_{L_T} + \sum_{t=2}^{T} \underbrace{D_{\mathrm{KL}}(q(x_{t-1}|x_t, x_0) \| p_\theta(x_{t-1}|x_t))}_{L_{t-1}} + \underbrace{(-\log p_\theta(x_0|x_1))}_{L_0}$$

**[Ho et al. 2020, Eq.(5)]**

### 4.2 分析各项

- **$L_T$**：不含可学习参数（前向过程是固定的），可忽略
- **$L_{t-1}$ ($t = 2, \ldots, T$)**：两个高斯之间的KL散度，有闭式解
- **$L_0$**：重构损失

### 4.3 计算 $L_{t-1}$

两个高斯 $q(x_{t-1}|x_t,x_0) = \mathcal{N}(\tilde{\mu}_t, \tilde{\beta}_t I)$ 和 $p_\theta(x_{t-1}|x_t) = \mathcal{N}(\mu_\theta, \sigma_t^2 I)$。

固定方差 $\sigma_t^2 = \tilde{\beta}_t$（Ho et al., 2020的选择），则：

$$L_{t-1} = D_{\mathrm{KL}}(q \| p_\theta) = \frac{1}{2\sigma_t^2} \|\tilde{\mu}_t(x_t, x_0) - \mu_\theta(x_t, t)\|^2 + C$$

**[Ho et al. 2020, Eq.(8)]**

### 4.4 代入 $\epsilon$ 参数化

$$\tilde{\mu}_t - \mu_\theta = \frac{\beta_t}{\sqrt{\alpha_t}\sqrt{1-\bar{\alpha}_t}}\left(\epsilon - \epsilon_\theta(x_t, t)\right)$$

所以：

$$L_{t-1} = \frac{\beta_t^2}{2\sigma_t^2 \alpha_t (1-\bar{\alpha}_t)} \|\epsilon - \epsilon_\theta(x_t, t)\|^2$$

**[Ho et al. 2020, Eq.(12)]**

### 4.5 简化训练目标

Ho et al. (2020) 发现去掉时间依赖的权重系数效果更好 **[Ho et al. 2020, Eq.(14)]**：

$$\boxed{\mathcal{L}_{\text{simple}} = \mathbb{E}_{t, x_0, \epsilon}\left[\|\epsilon - \epsilon_\theta(\underbrace{\sqrt{\bar{\alpha}_t}\, x_0 + \sqrt{1-\bar{\alpha}_t}\, \epsilon}_{x_t},\; t)\|^2\right]}$$

其中 $t \sim \mathrm{Uniform}\{1, \ldots, T\}$，$\epsilon \sim \mathcal{N}(0, \mathbf{I})$。

---

## Part 5: Connection to Score Matching

### 5.1 Score function 与噪声预测的关系

条件得分函数：

$$\nabla_{x_t} \log q(x_t|x_0) = \nabla_{x_t}\left[-\frac{\|x_t - \sqrt{\bar{\alpha}_t} x_0\|^2}{2(1-\bar{\alpha}_t)}\right] = -\frac{x_t - \sqrt{\bar{\alpha}_t} x_0}{1-\bar{\alpha}_t}$$

由 $x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t}\, \epsilon$，得 $x_t - \sqrt{\bar{\alpha}_t} x_0 = \sqrt{1-\bar{\alpha}_t}\, \epsilon$，所以：

$$\boxed{\nabla_{x_t} \log q(x_t|x_0) = -\frac{\epsilon}{\sqrt{1-\bar{\alpha}_t}}}$$

因此，预测噪声 $\epsilon_\theta$ 等价于估计得分函数（差一个缩放因子）：

$$s_\theta(x_t, t) = -\frac{\epsilon_\theta(x_t, t)}{\sqrt{1-\bar{\alpha}_t}}$$

DDPM损失 $\|\epsilon - \epsilon_\theta\|^2$ 与去噪得分匹配 $\|s_\theta - \nabla_{x_t}\log q(x_t|x_0)\|^2$ 仅差一个常数因子。

详细推导见 [score_matching.md](score_matching.md)。

---

## Part 6: SDE Formulation

### 6.1 连续时间极限

当 $T \to \infty$，DDPM的离散过程收敛为连续SDE。

**前向SDE (Variance Preserving, VP-SDE)** **[Song et al. 2021, Eq.(5)]**：

$$dx = -\frac{1}{2}\beta(t)\, x\, dt + \sqrt{\beta(t)}\, dw$$

其中 $\beta(t)$ 是连续噪声调度，$w$ 是标准Wiener过程。

**反向SDE (Anderson, 1982)** **[Song et al. 2021, Theorem 1]**：

$$dx = \left[-\frac{1}{2}\beta(t)\, x - \beta(t)\, \nabla_x \log p_t(x)\right] dt + \sqrt{\beta(t)}\, d\bar{w}$$

### 6.2 Probability Flow ODE

去掉噪声项，得到与反向SDE具有相同边际分布 $p_t(x)$ 的ODE：

$$\frac{dx}{dt} = -\frac{1}{2}\beta(t)\left[x + \nabla_x \log p_t(x)\right]$$

这是一个neural ODE，可用ODE solver（如RK45）求解。

**优势**：
- 确定性轨迹，适合精确似然计算
- 可用自适应步长solver加速采样
- 可用于编辑（DDIM的连续版本）

### 6.3 统一框架

Song et al. (2021) 提出的通用SDE框架：

| 模型 | $f(x,t)$ | $g(t)$ |
|---|---|---|
| VP-SDE (DDPM) | $-\frac{1}{2}\beta(t)x$ | $\sqrt{\beta(t)}$ |
| VE-SDE (SMLD) | $0$ | $\sqrt{\frac{d[\sigma^2(t)]}{dt}}$ |
| sub-VP-SDE | $-\frac{1}{2}\beta(t)x$ | $\sqrt{\beta(t)(1-e^{-2\int_0^t \beta(s)ds})}$ |

---

## Part 7: Classifier-Free Guidance

### 7.1 条件生成

训练条件模型 $\epsilon_\theta(x_t, t, c)$ 时，以概率 $p_{\text{uncond}}$（通常10%-20%）将条件 $c$ 替换为空标记 $\varnothing$。

### 7.2 推导

条件得分可以分解为：

$$\nabla_x \log p(x|c) = \nabla_x \log p(x) + \nabla_x \log p(c|x)$$

Classifier-free guidance放大条件信号：

$$\tilde{s}(x,t,c) = s(x,t,\varnothing) + (1+w)[s(x,t,c) - s(x,t,\varnothing)]$$

$$= (1+w)\, s(x,t,c) - w\, s(x,t,\varnothing)$$

等价地，用噪声预测：

$$\boxed{\tilde{\epsilon}_\theta(x_t, t, c) = (1+w)\,\epsilon_\theta(x_t, t, c) - w\,\epsilon_\theta(x_t, t, \varnothing)}$$

$w = 0$ 时退化为普通条件生成，$w > 0$ 时增强条件一致性但降低多样性。

---

## Part 8: Sampling Algorithms

### 8.1 DDPM Sampling **[Ho et al. 2020, Algorithm 2]**

$$x_{t-1} = \frac{1}{\sqrt{\alpha_t}}\left(x_t - \frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}}\,\epsilon_\theta(x_t, t)\right) + \sigma_t z, \quad z \sim \mathcal{N}(0, \mathbf{I})$$

需要 $T$ 步（通常1000步），较慢。

### 8.2 DDIM Sampling (Song et al., 2021)

$$x_{t-1} = \sqrt{\bar{\alpha}_{t-1}}\underbrace{\left(\frac{x_t - \sqrt{1-\bar{\alpha}_t}\,\epsilon_\theta(x_t,t)}{\sqrt{\bar{\alpha}_t}}\right)}_{\text{predicted } x_0} + \sqrt{1-\bar{\alpha}_{t-1}-\sigma_t^2}\,\epsilon_\theta(x_t,t) + \sigma_t\,\epsilon_t$$

当 $\sigma_t = 0$ 时，采样是确定性的。可以跳步（sub-sequence），大幅减少步数。

---

## Part 9: Rigorous Derivations from Original Papers

### 9.1 VLB 展开的严格推导 **[Ho et al. 2020, Eq.(3)-(5)]**

Ho et al. 从负对数似然的变分界出发：

$$L = \mathbb{E}_q\left[-\log p(\mathbf{x}_T) - \sum_{t \geq 1} \log \frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)}{q(\mathbf{x}_t|\mathbf{x}_{t-1})}\right]$$

通过将 $q(\mathbf{x}_t|\mathbf{x}_{t-1})$ 用贝叶斯定理改写为 $\frac{q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0) q(\mathbf{x}_t|\mathbf{x}_0)}{q(\mathbf{x}_{t-1}|\mathbf{x}_0)}$ 并利用 telescoping cancellation，最终得到 **[Ho et al. 2020, Eq.(5)]**：

$$L = \mathbb{E}_q\left[D_{\mathrm{KL}}(q(\mathbf{x}_T|\mathbf{x}_0) \| p(\mathbf{x}_T)) + \sum_{t>1} D_{\mathrm{KL}}(q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0) \| p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)) - \log p_\theta(\mathbf{x}_0|\mathbf{x}_1)\right]$$

### 9.2 $\epsilon$-参数化的严格推导 **[Ho et al. 2020, Eq.(8)-(12)]**

当 $p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t) = \mathcal{N}(\mathbf{x}_{t-1}; \boldsymbol{\mu}_\theta(\mathbf{x}_t, t), \sigma_t^2 \mathbf{I})$，VLB 的每一项化为 **[Ho et al. 2020, Eq.(8)]**：

$$L_{t-1} = \mathbb{E}_q\left[\frac{1}{2\sigma_t^2}\|\tilde{\boldsymbol{\mu}}_t(\mathbf{x}_t, \mathbf{x}_0) - \boldsymbol{\mu}_\theta(\mathbf{x}_t, t)\|^2\right] + C$$

将 $\mathbf{x}_t = \sqrt{\bar{\alpha}_t}\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\boldsymbol{\epsilon}$ 代入后验均值公式，得到 $\epsilon$-参数化 **[Ho et al. 2020, Eq.(11)]**：

$$\boldsymbol{\mu}_\theta(\mathbf{x}_t, t) = \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)\right)$$

代回 $L_{t-1}$ 得到 **[Ho et al. 2020, Eq.(12)]**：

$$L_{t-1} = \mathbb{E}_{\mathbf{x}_0, \boldsymbol{\epsilon}}\left[\frac{\beta_t^2}{2\sigma_t^2 \alpha_t(1-\bar{\alpha}_t)}\|\boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta(\sqrt{\bar{\alpha}_t}\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\boldsymbol{\epsilon}, t)\|^2\right]$$

### 9.3 方差选择 **[Ho et al. 2020, Section 3.2]**

Ho et al. 考虑两种固定方差选择：

- $\sigma_t^2 = \beta_t$：当 $\mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ 时最优（对应反向过程熵的上界）
- $\sigma_t^2 = \tilde{\beta}_t = \frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}\beta_t$：当 $\mathbf{x}_0$ 为确定性时最优（对应反向过程熵的下界）

实验发现两者性能相似。

### 9.4 离散解码器 $L_0$ **[Ho et al. 2020, Eq.(13)]**

为获得离散对数似然，Ho et al. 将最后一步的反向过程设为从高斯 $\mathcal{N}(\mathbf{x}_0; \boldsymbol{\mu}_\theta(\mathbf{x}_1, 1), \sigma_1^2 \mathbf{I})$ 导出的独立离散解码器：

$$p_\theta(\mathbf{x}_0|\mathbf{x}_1) = \prod_{i=1}^D \int_{\delta_-(x_0^i)}^{\delta_+(x_0^i)} \mathcal{N}(x; \mu_\theta^i(\mathbf{x}_1, 1), \sigma_1^2) dx$$

其中 $\delta_+(x) = x + \frac{1}{255}$（$x < 1$ 时），$\delta_-(x) = x - \frac{1}{255}$（$x > -1$ 时），边界处取 $\pm\infty$。

### 9.5 渐进有损压缩解释 **[Ho et al. 2020, Section 4.2]**

Ho et al. 发现 VLB 的分解自然对应一个渐进有损编码方案：

- **速率**：$L_1 + \cdots + L_T$（传输隐变量所需的比特数）
- **失真**：$L_0$（最终重建误差）

CIFAR10 实验显示：速率 = 1.78 bits/dim，失真 = 1.97 bits/dim，即超过一半的无损编码长度用于描述人眼不可感知的细节。

### 9.6 与自回归解码的联系 **[Ho et al. 2020, Section 4.2]**

VLB 可以重写为 **[Ho et al. 2020]**：

$$L = D_{\mathrm{KL}}(q(\mathbf{x}_T) \| p(\mathbf{x}_T)) + \mathbb{E}_q\left[\sum_{t \geq 1} D_{\mathrm{KL}}(q(\mathbf{x}_{t-1}|\mathbf{x}_t) \| p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t))\right] + H(\mathbf{x}_0)$$

如果将扩散长度 $T$ 设为数据维度，前向过程定义为逐坐标 masking，则训练 $p_\theta$ 等价于训练自回归模型。因此高斯扩散可以理解为一种广义的"比特排序"自回归模型。

---

## Part 10: SDE Framework — Rigorous Formulation **[Song et al. 2021]**

### 10.1 从离散到连续的严格推导 **[Song et al. 2021, Section 3]**

**VE-SDE 推导**：SMLD 的离散马尔可夫链 $\mathbf{x}_i = \mathbf{x}_{i-1} + \sqrt{\sigma_i^2 - \sigma_{i-1}^2}\mathbf{z}_{i-1}$ 在 $N \to \infty$ 极限下收敛为 **[Song et al. 2021, Eq.(6)]**：

$$d\mathbf{x} = \sqrt{\frac{d[\sigma^2(t)]}{dt}} d\mathbf{w}$$

具体地，对几何序列 $\sigma_i = \sigma_{\min}(\sigma_{\max}/\sigma_{\min})^{(i-1)/(N-1)}$：

$$d\mathbf{x} = \sigma_{\min}\left(\frac{\sigma_{\max}}{\sigma_{\min}}\right)^t \sqrt{2\log\frac{\sigma_{\max}}{\sigma_{\min}}} d\mathbf{w}$$

**VP-SDE 推导**：DDPM 的离散链 $\mathbf{x}_i = \sqrt{1-\beta_i}\mathbf{x}_{i-1} + \sqrt{\beta_i}\mathbf{z}_{i-1}$，定义 $\bar{\beta}_i = N\beta_i$，在 $N \to \infty$ 下 **[Song et al. 2021, Appendix]**：

$$\mathbf{x}(t+\Delta t) \approx \mathbf{x}(t) - \frac{1}{2}\beta(t)\Delta t \cdot \mathbf{x}(t) + \sqrt{\beta(t)\Delta t}\mathbf{z}(t)$$

收敛到 VP-SDE：

$$d\mathbf{x} = -\frac{1}{2}\beta(t)\mathbf{x}\,dt + \sqrt{\beta(t)}\,d\mathbf{w}$$

### 10.2 Anderson 反向 SDE 定理 **[Song et al. 2021, Theorem 1]**

**定理（Anderson, 1982; Song et al. 2021 的严格表述）**：对于一般 SDE $d\mathbf{x} = \mathbf{f}(\mathbf{x},t)dt + \mathbf{G}(\mathbf{x},t)d\mathbf{w}$，其反向过程为：

$$d\mathbf{x} = \left\{\mathbf{f}(\mathbf{x},t) - \nabla\cdot[\mathbf{G}(\mathbf{x},t)\mathbf{G}(\mathbf{x},t)^\top] - \mathbf{G}(\mathbf{x},t)\mathbf{G}(\mathbf{x},t)^\top\nabla_\mathbf{x}\log p_t(\mathbf{x})\right\}dt + \mathbf{G}(\mathbf{x},t)d\bar{\mathbf{w}}$$

其中 $\bar{\mathbf{w}}$ 是时间反向的标准 Wiener 过程，$\nabla\cdot\mathbf{F}(\mathbf{x}) := (\nabla\cdot\mathbf{f}^1(\mathbf{x}), \ldots, \nabla\cdot\mathbf{f}^d(\mathbf{x}))^\top$。

对标量扩散系数 $g(t)$ 的简化情形，散度项消失，退化为本文 Part 6 中的形式。

### 10.3 线性 SDE 的精确解 **[Song et al. 2021, Proposition 1]**

**命题（Sarkka & Solin, 2019）**：当 $\mathbf{f}(\mathbf{x}_t, t) = \mathbf{F}(t)\mathbf{x}_t + \mathbf{u}(t)$ 且 $\mathbf{G}(\mathbf{x}_t, t) = \mathbf{L}(t)$ 时，转移核为高斯 $p_{0t}(\mathbf{x}_t|\mathbf{x}_0) = \mathcal{N}(\mathbf{x}_t|\mathbf{m}(t), \boldsymbol{\sigma}(t))$，其中均值和协方差满足线性 ODE：

$$\frac{d\mathbf{m}(t)}{dt} = \mathbf{F}(t)\mathbf{m}(t) + \mathbf{u}(t), \quad \mathbf{m}(0) = \mathbf{x}_0$$

$$\frac{d\boldsymbol{\sigma}(t)}{dt} = \mathbf{F}(t)\boldsymbol{\sigma}(t) + \boldsymbol{\sigma}(t)\mathbf{F}(t)^\top + \mathbf{L}(t)\mathbf{L}(t)^\top, \quad \boldsymbol{\sigma}(0) = \mathbf{0}$$

### 10.4 三种 SDE 的转移核 **[Song et al. 2021, Appendix B, Eq.(79)]**

$$p_{0t}(\mathbf{x}(t)|\mathbf{x}(0)) = \begin{cases}
\mathcal{N}\big(\mathbf{x}(t); \mathbf{x}(0), [\sigma^2(t) - \sigma^2(0)]\mathbf{I}\big) & \text{(VE-SDE)} \\
\mathcal{N}\big(\mathbf{x}(t); \mathbf{x}(0)e^{-\frac{1}{2}\int_0^t\beta(s)ds}, \mathbf{I} - \mathbf{I}e^{-\int_0^t\beta(s)ds}\big) & \text{(VP-SDE)} \\
\mathcal{N}\big(\mathbf{x}(t); \mathbf{x}(0)e^{-\frac{1}{2}\int_0^t\beta(s)ds}, [1-e^{-\int_0^t\beta(s)ds}]^2\mathbf{I}\big) & \text{(sub-VP-SDE)}
\end{cases}$$

### 10.5 sub-VP-SDE **[Song et al. 2021, Appendix B, Eq.(31)]**

Song et al. 还提出 sub-VP-SDE：

$$d\mathbf{x} = -\frac{1}{2}\beta(t)\mathbf{x}\,dt + \sqrt{\beta(t)(1 - e^{-2\int_0^t\beta(s)ds})}\,d\mathbf{w}$$

其方差满足 $\boldsymbol{\sigma}_{\text{sub-VP}}(t) \preccurlyeq \boldsymbol{\sigma}_{\text{VP}}(t)$（始终被 VP-SDE 方差上界），但在 $t \to \infty$ 时两者收敛到相同极限 $\mathbf{I}$。sub-VP-SDE 在似然值上通常优于 VP-SDE。

### 10.6 概率流 ODE 的 Fokker-Planck 推导 **[Song et al. 2021, Appendix C]**

**推导思路**：从一般 SDE 的 Fokker-Planck 方程出发：

$$\frac{\partial p_t(\mathbf{x})}{\partial t} = -\sum_i \frac{\partial}{\partial x_i}[f_i p_t] + \frac{1}{2}\sum_{i,j}\frac{\partial^2}{\partial x_i \partial x_j}\left[\sum_k G_{ik}G_{jk}\,p_t\right]$$

利用乘积法则将二阶项改写为一阶散度形式：

$$\sum_j \frac{\partial}{\partial x_j}\left[\sum_k G_{ik}G_{jk}\,p_t\right] = p_t\,\nabla\cdot[\mathbf{G}\mathbf{G}^\top] + p_t\,\mathbf{G}\mathbf{G}^\top\nabla_\mathbf{x}\log p_t$$

由此可以将整个 Fokker-Planck 方程改写为一个无扩散项的连续性方程（Liouville 方程），其等效漂移为：

$$\tilde{\mathbf{f}}(\mathbf{x},t) = \mathbf{f}(\mathbf{x},t) - \frac{1}{2}\nabla\cdot[\mathbf{G}\mathbf{G}^\top] - \frac{1}{2}\mathbf{G}\mathbf{G}^\top\nabla_\mathbf{x}\log p_t(\mathbf{x})$$

这就证明了概率流 ODE $d\mathbf{x} = \tilde{\mathbf{f}}(\mathbf{x},t)dt$ 与原 SDE 具有相同的边际分布 $p_t(\mathbf{x})$。

### 10.7 VP-SDE 方差保持性的证明 **[Song et al. 2021, Appendix B]**

VP-SDE 的方差演化 ODE 为：

$$\frac{d\boldsymbol{\sigma}_{\text{VP}}(t)}{dt} = \beta(t)(\mathbf{I} - \boldsymbol{\sigma}_{\text{VP}}(t))$$

解为 $\boldsymbol{\sigma}_{\text{VP}}(t) = \mathbf{I} + e^{-\int_0^t\beta(s)ds}(\boldsymbol{\sigma}_{\text{VP}}(0) - \mathbf{I})$。当 $\boldsymbol{\sigma}_{\text{VP}}(0) = \mathbf{I}$ 时，$\boldsymbol{\sigma}_{\text{VP}}(t) \equiv \mathbf{I}$，方差恒定。

### 10.8 精确似然计算 **[Song et al. 2021, Appendix C.2]**

利用概率流 ODE 与 neural ODE 的联系，通过瞬时变量替换公式计算精确对数似然：

$$\log p_0(\mathbf{x}(0)) = \log p_T(\mathbf{x}(T)) + \int_0^T \nabla\cdot\tilde{\mathbf{f}}_\theta(\mathbf{x}(t), t)\,dt$$

其中 $\nabla\cdot\tilde{\mathbf{f}}_\theta$ 可用 Skilling-Hutchinson 迹估计器高效计算：

$$\nabla\cdot\tilde{\mathbf{f}}_\theta(\mathbf{x},t) = \mathbb{E}_{p(\mathbf{e})}[\mathbf{e}^\top\nabla\tilde{\mathbf{f}}_\theta(\mathbf{x},t)\mathbf{e}]$$

---

## Part 11: DDIM — Non-Markovian Forward Process and Deterministic Sampling **[Song et al. DDIM 2021]**

### 11.1 核心思想：训练目标只依赖边际分布

**关键观察 [Song et al. DDIM 2021, §3]**：DDPM 的训练目标 $L_\gamma$ 只依赖边际分布 $q(x_t|x_0)$，而不依赖联合分布 $q(x_{1:T}|x_0)$。因此，可以选择与DDPM具有相同边际但不同联合的**非马尔可夫**推断过程。

### 11.2 非马尔可夫前向过程族 **[Song et al. DDIM 2021, Eq.(7)]**

定义推断分布族 $\mathcal{Q}$，由参数 $\sigma \in \mathbb{R}_{\geq 0}^T$ 索引：

$$q_\sigma(x_{1:T}|x_0) := q_\sigma(x_T|x_0) \prod_{t=2}^T q_\sigma(x_{t-1}|x_t, x_0)$$

其中 $q_\sigma(x_T|x_0) = \mathcal{N}(\sqrt{\alpha_T}\, x_0, (1-\alpha_T)\mathbf{I})$，对所有 $t > 1$：

$$\boxed{q_\sigma(x_{t-1}|x_t, x_0) = \mathcal{N}\left(\sqrt{\alpha_{t-1}}\, x_0 + \sqrt{1 - \alpha_{t-1} - \sigma_t^2} \cdot \frac{x_t - \sqrt{\alpha_t}\, x_0}{\sqrt{1-\alpha_t}},\; \sigma_t^2 \mathbf{I}\right)}$$

这里 $\alpha_t$ 对应 DDPM 中的 $\bar{\alpha}_t$（Song et al. DDIM 使用了不同的符号约定）。

**关键引理 [Song et al. DDIM 2021, Lemma 1]**：上述定义确保 $q_\sigma(x_t|x_0) = \mathcal{N}(\sqrt{\alpha_t}\, x_0, (1-\alpha_t)\mathbf{I})$ 对所有 $t$ 成立，即边际分布与DDPM相同。

**证明思路**：由归纳法。设 $q_\sigma(x_t|x_0) = \mathcal{N}(\sqrt{\alpha_t}\, x_0, (1-\alpha_t)\mathbf{I})$，则 $q_\sigma(x_{t-1}|x_0) = \int q_\sigma(x_t|x_0)\, q_\sigma(x_{t-1}|x_t, x_0)\, dx_t$。利用高斯卷积公式，均值为 $\sqrt{\alpha_{t-1}}\, x_0$（交叉项恰好消去），方差为 $\sigma_t^2 + \frac{1-\alpha_{t-1}-\sigma_t^2}{1-\alpha_t}(1-\alpha_t) = 1-\alpha_{t-1}$。

### 11.3 统一变分目标 **[Song et al. DDIM 2021, Theorem 1]**

**定理**：对所有 $\sigma > \mathbf{0}$，存在 $\gamma \in \mathbb{R}_{>0}^T$ 和常数 $C$，使得 $J_\sigma = L_\gamma + C$。

其中 $J_\sigma(\epsilon_\theta) = \mathbb{E}_{x_{0:T} \sim q_\sigma}[\log q_\sigma(x_{1:T}|x_0) - \log p_\theta(x_{0:T})]$ 是非马尔可夫过程的变分目标。

**推论**：当 $\epsilon_\theta^{(t)}$ 各时间步不共享参数时，$J_\sigma$ 的最优解与 $L_1$（DDPM目标）的最优解相同。因此可以直接使用DDPM预训练模型，无需重新训练。

### 11.4 DDIM 采样公式 **[Song et al. DDIM 2021, Eq.(12)]**

从生成过程 $p_\theta$ 中采样 $x_{t-1}$：

$$\boxed{x_{t-1} = \sqrt{\alpha_{t-1}}\underbrace{\left(\frac{x_t - \sqrt{1-\alpha_t}\,\epsilon_\theta^{(t)}(x_t)}{\sqrt{\alpha_t}}\right)}_{\text{"predicted } x_0\text{"}} + \underbrace{\sqrt{1-\alpha_{t-1}-\sigma_t^2}\cdot\epsilon_\theta^{(t)}(x_t)}_{\text{"direction pointing to } x_t\text{"}} + \underbrace{\sigma_t\,\epsilon_t}_{\text{random noise}}}$$

其中 $\epsilon_t \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$。

**推导**：将 $x_0$ 的预测 $f_\theta^{(t)}(x_t) = (x_t - \sqrt{1-\alpha_t}\,\epsilon_\theta^{(t)}(x_t))/\sqrt{\alpha_t}$ 代入 $q_\sigma(x_{t-1}|x_t, x_0)$ 的均值公式，重参数化后直接得到。

### 11.5 特殊情形

| $\sigma_t$ 的选择 | 对应模型 |
|---|---|
| $\sigma_t = \sqrt{(1-\alpha_{t-1})/(1-\alpha_t)}\sqrt{1-\alpha_t/\alpha_{t-1}}$ | DDPM（马尔可夫前向过程） |
| $\sigma_t = 0$ | **DDIM**（确定性采样，隐式模型） |
| 其他 $\sigma_t \in (0, \sigma_{\text{DDPM}})$ | 插值，可调节随机性 |

### 11.6 加速采样 **[Song et al. DDIM 2021, §4.2]**

由于训练目标仅依赖边际 $q(x_t|x_0)$，可以在任意子序列 $\tau = [\tau_1, \ldots, \tau_S]$（$S \ll T$）上定义前向过程。采样时只需按 $\mathrm{reversed}(\tau)$ 迭代，步数从 $T=1000$ 减少到 $S \sim 10\text{-}50$。

### 11.7 与 Neural ODE 的联系 **[Song et al. DDIM 2021, Eq.(14)]**

DDIM 更新可以改写为类 Euler 积分形式：

$$\frac{x_{t-\Delta t}}{\sqrt{\alpha_{t-\Delta t}}} = \frac{x_t}{\sqrt{\alpha_t}} + \left(\sqrt{\frac{1-\alpha_{t-\Delta t}}{\alpha_{t-\Delta t}}} - \sqrt{\frac{1-\alpha_t}{\alpha_t}}\right)\epsilon_\theta^{(t)}(x_t)$$

令 $\bar{x} = x/\sqrt{\alpha}$，$\sigma = \sqrt{(1-\alpha)/\alpha}$，连续极限下对应 ODE：

$$d\bar{x}(t) = \epsilon_\theta^{(t)}\left(\frac{\bar{x}(t)}{\sqrt{\sigma^2+1}}\right) d\sigma(t)$$

**命题 [Song et al. DDIM 2021, Proposition 1]**：此 ODE 等价于 Song et al. (2021) 提出的 Variance-Exploding SDE 的概率流 ODE（在最优模型下）。

这意味着 DDIM 可以将 $x_0$ 编码为 $x_T$（通过正向求解 ODE），实现确定性的编码-解码，支持隐空间插值。

### 11.8 非马尔可夫前向过程的离散版本 **[Song et al. DDIM 2021, Appendix B]**

DDIM 的非马尔可夫思想也可推广到离散变量。对 $K$ 类范畴变量 $x_0$，定义：

$$q(x_t|x_0) = \mathrm{Cat}(\alpha_t\, \mathbf{x}_0 + (1-\alpha_t)\, \mathbf{1}_K)$$

非马尔可夫反向为混合分布：以概率 $\sigma_t$ 选 $x_t$，以概率 $\alpha_{t-1}-\sigma_t\alpha_t$ 选 $x_0$，以概率 $(1-\alpha_{t-1})-(1-\alpha_t)\sigma_t$ 选均匀。当 $\sigma_t \to 0$ 时，采样趋于确定性。

---

## Part 12: Flow Matching 与扩散模型的联系 **[Lipman et al. 2023]**

### 12.1 扩散路径作为 Flow Matching 的特例

Flow Matching 框架（详见 [flow_matching.md](flow_matching.md)）表明，扩散模型的概率路径可以直接用条件向量场生成，无需通过随机过程推导。

对于 VP 扩散路径（时间反转为 noise→data）**[Lipman et al. 2023, §4.1]**：

$$p_t(x|x_1) = \mathcal{N}(x\,|\,\alpha_{1-t}\, x_1,\; (1-\alpha_{1-t}^2)\mathbf{I})$$

其中 $\alpha_t = e^{-\frac{1}{2}T(t)}$，$T(t) = \int_0^t \beta(s)\,ds$。

利用 Theorem 3（条件向量场公式），得到条件 VF **[Lipman et al. 2023, Eq.(11)]**：

$$u_t(x|x_1) = \frac{\alpha'_{1-t}}{1-\alpha_{1-t}^2}\left(\alpha_{1-t}\, x - x_1\right)$$

### 12.2 CFM vs DSM：梯度等价但训练更稳定

条件 Flow Matching (CFM) 直接回归向量场，去噪得分匹配 (DSM) 回归得分函数。对于同一条扩散路径：

- **DSM 目标**：$\|s_\theta(x_t, t) - \nabla_{x_t}\log p_t(x_t|x_1)\|^2$
- **CFM 目标**：$\|v_\theta(x_t, t) - u_t(x_t|x_1)\|^2$

两者在最优解处等价（向量场与得分函数差一个与 $x$ 无关的项），但 CFM 经验上更稳定：不需要损失加权（可以直接用均匀 $L_2$ 损失），且 OT 路径比扩散路径更简单。

### 12.3 从扩散到 OT 路径

传统扩散路径导致弯曲轨迹，而 OT 条件路径 $\psi_t(x) = (1-(1-\sigma_{\min})t)x + tx_1$ 产生直线轨迹。Flow Matching 框架使得这种切换成为可能，因为训练目标不依赖于特定的随机过程构造。

详细的 Flow Matching 理论见 [flow_matching.md](flow_matching.md)。

---

## Summary

扩散模型的数学核心可以总结为一个闭环：

1. **前向过程** $q(x_t|x_0)$：加噪，有闭式解
2. **反向后验** $q(x_{t-1}|x_t,x_0)$：贝叶斯定理推导，高斯闭式
3. **训练目标**：VLB → KL散度 → MSE噪声预测
4. **Score matching等价**：$\epsilon$-预测 $\Leftrightarrow$ score estimation
5. **SDE统一**：离散 $\to$ 连续 $\to$ 概率流ODE
6. **DDIM加速**：非马尔可夫推断 → 确定性采样 → 跳步加速 → Neural ODE联系
7. **Flow Matching联系**：扩散路径 $\subset$ 一般高斯路径 $\supset$ OT路径

---

## References

1. Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. NeurIPS.
2. Song, Y., & Ermon, S. (2019). Generative Modeling by Estimating Gradients of the Data Distribution. NeurIPS.
3. Song, Y., Sohl-Dickstein, J., Kingma, D.P., Kumar, A., Ermon, S., & Poole, B. (2021). Score-Based Generative Modeling through Stochastic Differential Equations. ICLR.
4. Song, J., Meng, C., & Ermon, S. (2021). Denoising Diffusion Implicit Models. ICLR.
5. Nichol, A. & Dhariwal, P. (2021). Improved Denoising Diffusion Probabilistic Models. ICML.
6. Ho, J. & Salimans, T. (2022). Classifier-Free Diffusion Guidance.
7. Lipman, Y., Chen, R.T.Q., Ben-Hamu, H., Nickel, M., & Le, M. (2023). Flow Matching for Generative Modeling. ICLR.

1. Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. NeurIPS.
2. Song, Y., & Ermon, S. (2019). Generative Modeling by Estimating Gradients of the Data Distribution. NeurIPS.
3. Song, Y., Sohl-Dickstein, J., Kingma, D.P., Kumar, A., Ermon, S., & Poole, B. (2021). Score-Based Generative Modeling through Stochastic Differential Equations. ICLR.
4. Song, J., Meng, C., & Ermon, S. (2021). Denoising Diffusion Implicit Models. ICLR.
5. Nichol, A. & Dhariwal, P. (2021). Improved Denoising Diffusion Probabilistic Models. ICML.
6. Ho, J. & Salimans, T. (2022). Classifier-Free Diffusion Guidance.
