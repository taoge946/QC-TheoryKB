# Langevin Dynamics for Sampling

> **Tags**: `langevin`, `sampling`, `sde`, `score-function`

## Statement

推导Langevin动力学如何从目标分布中生成样本。从连续时间SDE出发，推导离散化更新规则，进而发展退火Langevin动力学（Annealed Langevin Dynamics），并建立与扩散模型采样过程的联系。

## Prerequisites

- 随机微分方程（SDE）基础
- Score function $\nabla_x \log p(x)$（见 [score_matching.md](score_matching.md)）
- 布朗运动 / Wiener过程
- Fokker-Planck方程（基本概念）
- 马尔可夫链蒙特卡洛（MCMC）基本思想

---

## Part 1: Overdamped Langevin SDE

### 1.1 物理背景

Langevin方程最初描述布朗粒子在势场中的运动。在机器学习中，我们使用其过阻尼（overdamped）版本，将"势能"对应为负对数概率密度。

### 1.2 连续时间SDE

给定目标分布 $p(x)$，overdamped Langevin SDE为：

$$dx_t = \frac{1}{2}\nabla_x \log p(x_t)\, dt + dw_t$$

其中：
- $\nabla_x \log p(x_t)$ 是score function，提供梯度信息
- $w_t$ 是标准Wiener过程（布朗运动），$dw_t \sim \mathcal{N}(0, dt\, I)$
- 系数 $\frac{1}{2}$ 保证平稳分布恰好是 $p(x)$

### 1.3 Fokker-Planck方程与平稳分布

SDE $dx = f(x)dt + g\, dw$ 对应的Fokker-Planck方程描述概率密度 $\rho(x, t)$ 的演化：

$$\frac{\partial \rho}{\partial t} = -\nabla \cdot (f \rho) + \frac{g^2}{2}\nabla^2 \rho$$

对于Langevin SDE，$f(x) = \frac{1}{2}\nabla \log p(x)$，$g = 1$：

$$\frac{\partial \rho}{\partial t} = -\nabla \cdot \left(\frac{1}{2}\nabla \log p(x) \cdot \rho\right) + \frac{1}{2}\nabla^2 \rho$$

### 1.4 验证平稳分布

设 $\rho^* = p(x)$，验证 $\frac{\partial \rho^*}{\partial t} = 0$：

$$-\nabla \cdot \left(\frac{1}{2}\nabla \log p \cdot p\right) + \frac{1}{2}\nabla^2 p$$

第一项：$\frac{1}{2}\nabla \log p \cdot p = \frac{1}{2}\frac{\nabla p}{p} \cdot p = \frac{1}{2}\nabla p$

所以：$-\nabla \cdot \left(\frac{1}{2}\nabla p\right) + \frac{1}{2}\nabla^2 p = -\frac{1}{2}\nabla^2 p + \frac{1}{2}\nabla^2 p = 0$ $\checkmark$

**结论**：$p(x)$ 是Langevin SDE的平稳分布。在一定正则条件下（如 $p(x)$ 满足log-Sobolev不等式），Langevin动力学从任意初始分布指数收敛到 $p(x)$。 $\blacksquare$

---

## Part 2: Discrete Langevin Dynamics (Euler-Maruyama Discretization)

### 2.1 Euler-Maruyama方法

对SDE $dx = f(x)dt + g\, dw$ 进行离散化，时间步长 $\eta$：

$$x_{k+1} = x_k + f(x_k)\, \eta + g\, \sqrt{\eta}\, z_k, \quad z_k \sim \mathcal{N}(0, I)$$

### 2.2 离散Langevin动力学

应用于Langevin SDE：

$$\boxed{x_{k+1} = x_k + \frac{\eta}{2}\, \nabla_x \log p(x_k) + \sqrt{\eta}\, z_k, \quad z_k \sim \mathcal{N}(0, I)}$$

**两项的作用**：
- **梯度项** $\frac{\eta}{2}\nabla_x \log p(x_k)$：将样本推向高概率区域（类似梯度上升）
- **噪声项** $\sqrt{\eta}\, z_k$：注入随机性，保证遍历性（exploration）

### 2.3 收敛性

**定理**：当 $\eta \to 0$，$K \to \infty$，$x_K$ 的分布收敛到 $p(x)$。

实际使用中 $\eta > 0$ 引入离散化误差。可以用Metropolis-Hastings校正步（MALA算法）来修正，但在深度生成模型中通常省略校正步。

### 2.4 与梯度下降的对比

| | 梯度下降 | Langevin动力学 |
|---|---|---|
| 更新 | $x \leftarrow x + \eta \nabla \log p(x)$ | $x \leftarrow x + \frac{\eta}{2} \nabla \log p(x) + \sqrt{\eta}\, z$ |
| 目标 | 找到 mode $\arg\max p(x)$ | 从 $p(x)$ 中采样 |
| 行为 | 收敛到点 | 收敛到分布 |

---

## Part 3: Langevin Dynamics with Learned Score

### 3.1 替换真实 score 为学习的 score

在实际应用中，$\nabla_x \log p(x)$ 未知。用训练好的score网络 $s_\theta(x) \approx \nabla_x \log p(x)$ 替代：

$$x_{k+1} = x_k + \frac{\eta}{2}\, s_\theta(x_k) + \sqrt{\eta}\, z_k$$

这是 Song & Ermon (2019) 提出的基于score的生成模型的采样方法。

### 3.2 Score估计误差的影响

如果 $\|s_\theta(x) - \nabla_x \log p(x)\| \leq \delta$，则离散Langevin采样的分布 $\hat{p}$ 与目标 $p$ 之间的距离（TV或Wasserstein）可以被 $\delta$ 和 $\eta$ 控制。

形式地（简化版）：

$$W_2(\hat{p}_K, p) \leq C_1 \sqrt{\eta} + C_2 \delta + C_3 e^{-c K \eta}$$

- 第一项：离散化误差
- 第二项：score估计误差
- 第三项：mixing误差（指数衰减）

---

## Part 4: Annealed Langevin Dynamics

### 4.1 单一噪声水平的问题

低密度区域（$p(x)$ 很小的地方）score估计不准：训练数据稀少，梯度信号弱。

**后果**：Langevin采样可能困在局部模式中，无法有效探索整个支撑集。

### 4.2 退火策略 (Song & Ermon, 2019)

使用一系列噪声水平 $\sigma_1 > \sigma_2 > \cdots > \sigma_L$，对每个噪声水平，目标分布是加噪版本：

$$p_{\sigma_i}(x) = \int p_{\mathrm{data}}(y)\, \mathcal{N}(x; y, \sigma_i^2 I)\, dy$$

从高噪声（平滑分布，易于采样）逐步过渡到低噪声（接近真实分布）。

### 4.3 算法

**Algorithm: Annealed Langevin Dynamics**

输入：噪声水平 $\sigma_1 > \cdots > \sigma_L$，步长 $\{\eta_i\}$，每级步数 $K$，score网络 $s_\theta(x, \sigma)$

1. 初始化 $x_0 \sim \mathcal{N}(0, \sigma_1^2 I)$（或其他宽分布）
2. **For** $i = 1, \ldots, L$:
   - **For** $k = 1, \ldots, K$:
     - $z \sim \mathcal{N}(0, I)$
     - $x \leftarrow x + \frac{\eta_i}{2}\, s_\theta(x, \sigma_i) + \sqrt{\eta_i}\, z$
3. 返回 $x$

### 4.4 直觉

- $\sigma_1$ 大：$p_{\sigma_1}$ 近似高斯，modes之间有"桥"，Langevin容易跨模式
- $\sigma_L$ 小：$p_{\sigma_L} \approx p_{\mathrm{data}}$，精细刻画数据分布
- 逐级退火：从粗到细，兼顾exploration和exploitation

---

## Part 5: Connection to Diffusion Model Sampling

### 5.1 DDPM采样 = 离散化反向SDE **[Ho et al. 2020, Algorithm 2]**

DDPM的反向采样步 **[Ho et al. 2020, Algorithm 2]**：

$$x_{t-1} = \frac{1}{\sqrt{\alpha_t}}\left(x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\, \epsilon_\theta(x_t, t)\right) + \sqrt{\beta_t}\, z$$

利用 $s_\theta(x_t, t) = -\frac{\epsilon_\theta(x_t, t)}{\sqrt{1-\bar{\alpha}_t}}$，改写为：

$$x_{t-1} = \frac{1}{\sqrt{\alpha_t}}\left(x_t + \beta_t\, s_\theta(x_t, t)\right) + \sqrt{\beta_t}\, z$$

### 5.2 与Langevin的比较

Langevin更新：$x' = x + \frac{\eta}{2} s(x) + \sqrt{\eta}\, z$

DDPM更新（简化）：$x' = \frac{1}{\sqrt{\alpha_t}}(x + \beta_t\, s_\theta(x, t)) + \sqrt{\beta_t}\, z$

**相似之处**：
- 都有score引导的梯度项
- 都有噪声注入项
- 都从高噪声到低噪声

**不同之处**：
- DDPM有额外的缩放因子 $\frac{1}{\sqrt{\alpha_t}}$
- DDPM的"步长"和"噪声水平"由noise schedule精确控制
- DDPM有严格的变分下界保证

### 5.3 连续时间统一 (Song et al., 2021)

反向SDE：

$$dx = \left[f(x,t) - g(t)^2\, \nabla_x \log p_t(x)\right] dt + g(t)\, d\bar{w}$$

这是一个时间非齐次的Langevin SDE：
- 漂移项包含score $\nabla_x \log p_t(x)$
- 扩散系数 $g(t)$ 随时间变化

**DDPM采样**是这个反向SDE的Euler-Maruyama离散化。

### 5.4 Predictor-Corrector采样

Song et al. (2021) 提出混合方案：

1. **Predictor**：用反向SDE的一步离散化（DDPM/DDIM风格）
2. **Corrector**：在当前噪声水平做几步Langevin MCMC

这结合了两者的优势：predictor跨时间步移动，corrector在当前时间步精细调整。

算法：

$$\text{For } t = T, T-1, \ldots, 1:$$

$$\quad \text{Predictor: } x \leftarrow \text{reverse-SDE-step}(x, t)$$

$$\quad \text{For } j = 1, \ldots, M:$$

$$\quad\quad \text{Corrector: } x \leftarrow x + \eta_t\, s_\theta(x, t) + \sqrt{2\eta_t}\, z$$

---

## Part 6: Convergence Theory

### 6.1 Log-Sobolev不等式

如果 $p(x) \propto e^{-U(x)}$ 满足 log-Sobolev 不等式（常数 $\alpha > 0$）：

$$D_{\mathrm{KL}}(\rho \| p) \leq \frac{1}{2\alpha}\, \mathbb{E}_\rho\left[\|\nabla \log \frac{\rho}{p}\|^2\right]$$

则连续Langevin动力学的KL散度指数衰减：

$$D_{\mathrm{KL}}(\rho_t \| p) \leq e^{-2\alpha t}\, D_{\mathrm{KL}}(\rho_0 \| p)$$

### 6.2 强对数凹分布

如果 $U(x)$ 是 $m$-strongly convex（即 $\nabla^2 U \succeq mI$），则 log-Sobolev常数 $\alpha = m$。

此时离散Langevin的收敛速率为：

$$W_2^2(\rho_K, p) \leq (1 - m\eta)^K W_2^2(\rho_0, p) + O\left(\frac{d\eta}{m}\right)$$

其中 $d$ 是维度。收敛需要 $K = O\left(\frac{1}{m\eta}\log\frac{1}{\epsilon}\right)$ 步。

### 6.3 非对数凹情况

实际数据分布通常是多模态的（非对数凹）。此时：
- 连续Langevin仍然收敛，但可能需要指数长时间来跨越能量壁垒
- 退火策略（Annealed LD）通过逐步降低噪声来缓解这个问题
- 目前对扩散模型的采样质量尚无完整的非渐近理论

---

## Summary

Langevin动力学在扩散模型中的角色：

$$\underbrace{\text{连续 Langevin SDE}}_{\text{理论基础}} \xrightarrow{\text{Euler-Maruyama}} \underbrace{\text{离散 Langevin}}_{\text{基本采样器}} \xrightarrow{\text{多尺度}} \underbrace{\text{退火 Langevin}}_{\text{NCSN}} \xrightarrow{\text{精确化}} \underbrace{\text{DDPM/SDE采样}}_{\text{现代扩散模型}}$$

核心思想始终一致：**梯度（score）引导 + 噪声注入 = 从目标分布采样**。

---

## Part 7: Reverse Diffusion Sampler **[Song et al. 2021]**

### 7.1 反向扩散采样器的推导 **[Song et al. 2021, Section 4.1, Appendix D]**

Song et al. 提出一种更自然的反向 SDE 离散化方法。给定前向离散化 **[Song et al. 2021, Eq.(10)]**：

$$\mathbf{x}_{i+1} - \mathbf{x}_i = \mathbf{a}_i(\mathbf{x}_i) + \mathbf{A}_i(\mathbf{x}_i)\mathbf{z}_i$$

对应的反向离散化为 **[Song et al. 2021, Eq.(11)]**：

$$\mathbf{x}_i - \mathbf{x}_{i+1} = -\mathbf{a}_{i+1}(\mathbf{x}_{i+1}) + \mathbf{A}_{i+1}(\mathbf{x}_{i+1})\mathbf{A}_{i+1}(\mathbf{x}_{i+1})^\top\nabla_\mathbf{x}\log p(\mathbf{x}_{i+1}, t_{i+1}) + \mathbf{A}_i(\mathbf{x}_i)\mathbf{z}_i$$

**对 DDPM 的具体形式** **[Song et al. 2021, Eq.(13)]**：

$$\mathbf{x}_i = (2-\sqrt{1-\beta_{i+1}})\mathbf{x}_{i+1} + \beta_{i+1}\mathbf{s}_\theta(\mathbf{x}_{i+1}, t_{i+1}) + \sqrt{\beta_{i+1}}\mathbf{z}_i$$

当 $\beta_i \to 0$ 时，这与 DDPM 的原始采样规则（祖先采样）等价：

$$\frac{1}{\sqrt{1-\beta_{i+1}}}(\mathbf{x}_i + \beta_{i+1}\mathbf{s}_\theta) \approx (2-\sqrt{1-\beta_{i+1}})\mathbf{x}_i + \beta_{i+1}\mathbf{s}_\theta$$

### 7.2 Predictor-Corrector 采样的严格表述 **[Song et al. 2021, Section 4.2]**

Song et al. 将 PC 采样形式化为：
1. **Predictor**：数值 SDE 求解器的一步（反向扩散或祖先采样）
2. **Corrector**：在当前噪声水平做 $M$ 步 Langevin MCMC

现有方法都是 PC 的特例：
- **SMLD**：恒等 predictor + 退火 Langevin corrector
- **DDPM**：祖先采样 predictor + 恒等 corrector

实验结果 **[Song et al. 2021, Table 1]** 表明：
- 反向扩散采样器始终优于祖先采样（DDPM: FID 3.21 vs 3.24）
- 每个 predictor 步后加一个 corrector 步（PC1000）优于将计算量翻倍给 predictor（P2000）
- 最佳组合：概率流 predictor + Langevin corrector（VP-SDE 上 FID 3.06）

### 7.3 条件生成的反向 SDE **[Song et al. 2021, Appendix A, Eq.(26)]**

对于条件生成 $p_t(\mathbf{x}|\mathbf{y})$，条件反向 SDE 为：

$$d\mathbf{x} = \left\{\mathbf{f}(\mathbf{x},t) - \nabla\cdot[\mathbf{G}\mathbf{G}^\top] - \mathbf{G}\mathbf{G}^\top\nabla_\mathbf{x}\log p_t(\mathbf{x}) - \mathbf{G}\mathbf{G}^\top\nabla_\mathbf{x}\log p_t(\mathbf{y}|\mathbf{x})\right\}dt + \mathbf{G}(\mathbf{x},t)d\bar{\mathbf{w}}$$

其中额外的 $\nabla_\mathbf{x}\log p_t(\mathbf{y}|\mathbf{x})$ 项引导生成过程满足条件约束。

---

## References

1. Roberts, G.O. & Tweedie, R.L. (1996). Exponential Convergence of Langevin Distributions and Their Discrete Approximations. Bernoulli.
2. Song, Y. & Ermon, S. (2019). Generative Modeling by Estimating Gradients of the Data Distribution. NeurIPS.
3. Song, Y., Sohl-Dickstein, J., Kingma, D.P., Kumar, A., Ermon, S., & Poole, B. (2021). Score-Based Generative Modeling through Stochastic Differential Equations. ICLR.
4. Welling, M. & Teh, Y.W. (2011). Bayesian Learning via Stochastic Gradient Langevin Dynamics. ICML.
5. Vempala, S. & Wibisono, A. (2019). Rapid Convergence of the Unadjusted Langevin Algorithm: Isoperimetry Suffices. NeurIPS.
