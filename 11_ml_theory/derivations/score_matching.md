# Score Matching and Denoising Score Matching

> **Tags**: `score-matching`, `denoising`, `fisher-divergence`

## Statement

推导得分匹配（Score Matching）目标函数及其与去噪得分匹配（Denoising Score Matching, DSM）的等价性。建立从显式得分匹配到隐式得分匹配、再到去噪得分匹配的完整理论链条，最终说明DDPM损失函数是DSM的特例。

## Prerequisites

- 概率密度函数 $p(x)$ 及其性质
- Fisher divergence / Fisher information
- 分部积分（integration by parts）
- 高斯分布的导数
- DDPM 前向过程（见 [diffusion_models_math.md](diffusion_models_math.md)）

---

## Part 1: Score Function Basics

### 1.1 定义

给定概率密度 $p(x)$，**score function** 定义为：

$$s(x) \triangleq \nabla_x \log p(x) = \frac{\nabla_x p(x)}{p(x)}$$

**关键性质**：

1. Score function 不依赖于归一化常数。若 $p(x) = \frac{\tilde{p}(x)}{Z}$，则 $\nabla_x \log p(x) = \nabla_x \log \tilde{p}(x)$（因为 $\nabla_x \log Z = 0$）
2. 对于高斯 $p(x) = \mathcal{N}(x; \mu, \sigma^2 I)$：$\nabla_x \log p(x) = -\frac{x - \mu}{\sigma^2}$
3. Score 指向概率密度增大最快的方向

### 1.2 目标

我们希望训练一个神经网络 $s_\theta(x)$ 来近似真实得分 $\nabla_x \log p_{\mathrm{data}}(x)$。最自然的目标是最小化Fisher divergence：

$$J_{\mathrm{Fisher}}(\theta) = \frac{1}{2}\mathbb{E}_{p_{\mathrm{data}}(x)}\left[\|s_\theta(x) - \nabla_x \log p_{\mathrm{data}}(x)\|^2\right]$$

**问题**：真实得分 $\nabla_x \log p_{\mathrm{data}}(x)$ 未知！

---

## Part 2: Explicit Score Matching

### 2.1 展开 Fisher Divergence

$$J_{\mathrm{Fisher}}(\theta) = \frac{1}{2}\mathbb{E}_{p_{\mathrm{data}}}\left[\|s_\theta(x)\|^2 - 2\, s_\theta(x)^T \nabla_x \log p_{\mathrm{data}}(x) + \|\nabla_x \log p_{\mathrm{data}}(x)\|^2\right]$$

第三项与 $\theta$ 无关，优化时可忽略。第一项可直接计算。问题在于第二项（交叉项）包含未知的 $\nabla_x \log p_{\mathrm{data}}(x)$。

---

## Part 3: Implicit Score Matching (Hyvarinen, 2005)

### 3.1 核心思想

利用分部积分消除交叉项中对 $\nabla_x \log p_{\mathrm{data}}(x)$ 的依赖。

### 3.2 处理交叉项

考虑交叉项的第 $i$ 个分量：

$$\mathbb{E}_{p_{\mathrm{data}}}\left[s_{\theta,i}(x)\, \frac{\partial \log p_{\mathrm{data}}(x)}{\partial x_i}\right]$$

$$= \int p_{\mathrm{data}}(x)\, s_{\theta,i}(x)\, \frac{\partial \log p_{\mathrm{data}}(x)}{\partial x_i}\, dx$$

利用 $p(x) \cdot \partial_i \log p(x) = p(x) \cdot \frac{\partial_i p(x)}{p(x)} = \partial_i p(x)$：

$$= \int s_{\theta,i}(x)\, \frac{\partial p_{\mathrm{data}}(x)}{\partial x_i}\, dx$$

### 3.3 分部积分

$$\int s_{\theta,i}(x)\, \frac{\partial p_{\mathrm{data}}(x)}{\partial x_i}\, dx_i = \left[s_{\theta,i}(x)\, p_{\mathrm{data}}(x)\right]_{-\infty}^{\infty} - \int \frac{\partial s_{\theta,i}(x)}{\partial x_i}\, p_{\mathrm{data}}(x)\, dx_i$$

**边界条件**：假设 $p_{\mathrm{data}}(x) \to 0$ 当 $\|x\| \to \infty$（对实际数据分布合理），且 $s_\theta$ 增长不超过多项式，则边界项为零：

$$\left[s_{\theta,i}(x)\, p_{\mathrm{data}}(x)\right]_{-\infty}^{\infty} = 0$$

因此：

$$\mathbb{E}_{p_{\mathrm{data}}}\left[s_{\theta,i}(x)\, \partial_i \log p_{\mathrm{data}}(x)\right] = -\mathbb{E}_{p_{\mathrm{data}}}\left[\frac{\partial s_{\theta,i}(x)}{\partial x_i}\right]$$

### 3.4 对所有维度求和

$$\mathbb{E}_{p_{\mathrm{data}}}\left[s_\theta(x)^T \nabla_x \log p_{\mathrm{data}}(x)\right] = -\mathbb{E}_{p_{\mathrm{data}}}\left[\mathrm{tr}\left(\nabla_x s_\theta(x)\right)\right]$$

其中 $\mathrm{tr}(\nabla_x s_\theta(x)) = \sum_i \frac{\partial s_{\theta,i}}{\partial x_i}$ 是 Jacobian 的迹。

### 3.5 隐式得分匹配目标

将交叉项的结果代回 $J_{\mathrm{Fisher}}$：

$$\boxed{J_{\mathrm{ISM}}(\theta) = \mathbb{E}_{p_{\mathrm{data}}}\left[\mathrm{tr}\left(\nabla_x s_\theta(x)\right) + \frac{1}{2}\|s_\theta(x)\|^2\right]}$$

**Hyvarinen定理**：$J_{\mathrm{ISM}}(\theta) = J_{\mathrm{Fisher}}(\theta) + C$（$C$ 与 $\theta$ 无关），因此两者有相同的最优解。

### 3.6 计算问题

$\mathrm{tr}(\nabla_x s_\theta(x))$ 需要计算 Jacobian 的迹，对高维数据代价很大。可用Hutchinson trace estimator缓解：

$$\mathrm{tr}(A) = \mathbb{E}_{v}\left[v^T A v\right], \quad v \sim \mathcal{N}(0, I) \text{ or } v \sim \mathrm{Rademacher}$$

但仍需反向传播计算Jacobian-vector product，计算量较大。

---

## Part 4: Denoising Score Matching (Vincent, 2011)

### 4.1 核心思想

不直接匹配数据分布的score，而是匹配加噪数据分布的score。加噪后的条件score是已知的闭式表达式。

### 4.2 定义加噪分布

给定噪声核 $q_\sigma(\tilde{x}|x)$（通常是高斯），加噪数据分布为：

$$q_\sigma(\tilde{x}) = \int q_\sigma(\tilde{x}|x)\, p_{\mathrm{data}}(x)\, dx$$

选择高斯噪声核：

$$q_\sigma(\tilde{x}|x) = \mathcal{N}(\tilde{x};\; x,\; \sigma^2 \mathbf{I})$$

### 4.3 条件 score 的闭式解

$$\nabla_{\tilde{x}} \log q_\sigma(\tilde{x}|x) = \nabla_{\tilde{x}}\left[-\frac{\|\tilde{x} - x\|^2}{2\sigma^2}\right] = -\frac{\tilde{x} - x}{\sigma^2}$$

这是已知量！不依赖于数据分布 $p_{\mathrm{data}}$。

### 4.4 DSM 目标函数

$$\boxed{J_{\mathrm{DSM}}(\theta) = \frac{1}{2}\mathbb{E}_{p_{\mathrm{data}}(x)}\, \mathbb{E}_{q_\sigma(\tilde{x}|x)}\left[\left\|s_\theta(\tilde{x}) - \nabla_{\tilde{x}} \log q_\sigma(\tilde{x}|x)\right\|^2\right]}$$

**[Song et al. 2021, Eq.(8)]** (continuous-time generalization)

代入高斯噪声核：

$$J_{\mathrm{DSM}}(\theta) = \frac{1}{2}\mathbb{E}_{p_{\mathrm{data}}(x)}\, \mathbb{E}_{\epsilon \sim \mathcal{N}(0,I)}\left[\left\|s_\theta(x + \sigma\epsilon) + \frac{\epsilon}{\sigma}\right\|^2\right]$$

### 4.5 DSM 与 ISM 等价性证明

**定理 (Vincent, 2011)**：$J_{\mathrm{DSM}}(\theta) = J_{\mathrm{ISM}}^{q_\sigma}(\theta) + C$，即DSM等价于对加噪分布 $q_\sigma(\tilde{x})$ 做隐式得分匹配。

**证明思路**：

展开DSM：

$$J_{\mathrm{DSM}} = \frac{1}{2}\mathbb{E}_{q_\sigma(\tilde{x},x)}\left[\|s_\theta(\tilde{x})\|^2 - 2 s_\theta(\tilde{x})^T \nabla_{\tilde{x}} \log q_\sigma(\tilde{x}|x) + \|\nabla_{\tilde{x}} \log q_\sigma(\tilde{x}|x)\|^2\right]$$

第三项与 $\theta$ 无关。关键是证明交叉项等价：

$$\mathbb{E}_{q_\sigma(\tilde{x},x)}\left[s_\theta(\tilde{x})^T \nabla_{\tilde{x}} \log q_\sigma(\tilde{x}|x)\right] = \mathbb{E}_{q_\sigma(\tilde{x})}\left[s_\theta(\tilde{x})^T \nabla_{\tilde{x}} \log q_\sigma(\tilde{x})\right]$$

**证明**：

左边 = $\int \int q_\sigma(\tilde{x}|x) p_{\mathrm{data}}(x)\, s_\theta(\tilde{x})^T \nabla_{\tilde{x}} \log q_\sigma(\tilde{x}|x)\, dx\, d\tilde{x}$

利用 $q_\sigma(\tilde{x}|x) \cdot \nabla_{\tilde{x}} \log q_\sigma(\tilde{x}|x) = \nabla_{\tilde{x}} q_\sigma(\tilde{x}|x)$：

$$= \int s_\theta(\tilde{x})^T \int p_{\mathrm{data}}(x)\, \nabla_{\tilde{x}} q_\sigma(\tilde{x}|x)\, dx\, d\tilde{x}$$

$$= \int s_\theta(\tilde{x})^T \nabla_{\tilde{x}} \underbrace{\int p_{\mathrm{data}}(x)\, q_\sigma(\tilde{x}|x)\, dx}_{q_\sigma(\tilde{x})}\, d\tilde{x}$$

$$= \int s_\theta(\tilde{x})^T \nabla_{\tilde{x}} q_\sigma(\tilde{x})\, d\tilde{x}$$

$$= \int q_\sigma(\tilde{x})\, s_\theta(\tilde{x})^T \nabla_{\tilde{x}} \log q_\sigma(\tilde{x})\, d\tilde{x} = \text{右边}$$

因此DSM目标等价于对加噪分布做Fisher divergence匹配（差一个常数），但完全避免了Jacobian迹的计算和未知得分函数的问题。 $\blacksquare$

---

## Part 5: Multi-Scale Denoising Score Matching

### 5.1 问题：单一噪声水平不够

单一小 $\sigma$ 下，低密度区域的score估计不准（因为缺少数据点）。

### 5.2 解决方案 (Song & Ermon, 2019)

使用一系列递增的噪声水平 $\sigma_1 < \sigma_2 < \cdots < \sigma_L$：

$$\mathcal{L}_{\mathrm{NCSN}} = \frac{1}{L}\sum_{i=1}^{L} \lambda(\sigma_i)\, \mathbb{E}_{p_{\mathrm{data}}(x)}\, \mathbb{E}_{q_{\sigma_i}(\tilde{x}|x)}\left[\left\|s_\theta(\tilde{x}, \sigma_i) + \frac{\tilde{x} - x}{\sigma_i^2}\right\|^2\right]$$

其中 $\lambda(\sigma_i) = \sigma_i^2$ 是经验选择的权重。

---

## Part 6: Connection to DDPM Loss

### 6.1 DDPM 前向过程作为噪声核

DDPM的前向过程 $q(x_t|x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1-\bar{\alpha}_t)I)$ 可以看作：

$$x_t = \sqrt{\bar{\alpha}_t}\, x_0 + \sqrt{1-\bar{\alpha}_t}\, \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

条件score：

$$\nabla_{x_t} \log q(x_t|x_0) = -\frac{x_t - \sqrt{\bar{\alpha}_t} x_0}{1-\bar{\alpha}_t} = -\frac{\epsilon}{\sqrt{1-\bar{\alpha}_t}}$$

### 6.2 DSM 应用于 DDPM

令 $s_\theta(x_t, t)$ 为score网络。DSM目标为：

$$\mathcal{L}_{\mathrm{DSM}} = \mathbb{E}_t \mathbb{E}_{x_0} \mathbb{E}_{\epsilon}\left[\left\|s_\theta(x_t, t) + \frac{\epsilon}{\sqrt{1-\bar{\alpha}_t}}\right\|^2\right]$$

### 6.3 与 DDPM 噪声预测的等价

定义 $\epsilon_\theta(x_t, t) = -\sqrt{1-\bar{\alpha}_t}\, s_\theta(x_t, t)$，代入：

$$\mathcal{L}_{\mathrm{DSM}} = \mathbb{E}_t \mathbb{E}_{x_0} \mathbb{E}_{\epsilon}\left[\left\|-\frac{\epsilon_\theta(x_t,t)}{\sqrt{1-\bar{\alpha}_t}} + \frac{\epsilon}{\sqrt{1-\bar{\alpha}_t}}\right\|^2\right]$$

$$= \mathbb{E}_t \frac{1}{1-\bar{\alpha}_t} \mathbb{E}_{x_0, \epsilon}\left[\|\epsilon - \epsilon_\theta(x_t, t)\|^2\right]$$

去掉与 $\theta$ 无关的权重（简化版），就得到 DDPM 的简化损失：

$$\boxed{\mathcal{L}_{\text{simple}} = \mathbb{E}_{t, x_0, \epsilon}\left[\|\epsilon - \epsilon_\theta(x_t, t)\|^2\right]}$$

**[Ho et al. 2020, Eq.(14)]**

**结论**：DDPM的噪声预测训练等价于在各时间步做去噪得分匹配。

---

## Part 7: Summary of Equivalences

$$\underbrace{J_{\mathrm{Fisher}}(\theta)}_{\text{Fisher divergence}} \xlongequal{\text{分部积分}} \underbrace{J_{\mathrm{ISM}}(\theta)}_{\text{隐式得分匹配}} + C_1$$

$$\underbrace{J_{\mathrm{DSM}}(\theta)}_{\text{去噪得分匹配}} \xlongequal{\text{Vincent定理}} \underbrace{J_{\mathrm{ISM}}^{q_\sigma}(\theta)}_{\text{加噪分布的ISM}} + C_2$$

$$\underbrace{\mathcal{L}_{\text{DDPM}}}_{\text{噪声预测}} \xlongequal{\epsilon = -\sqrt{1-\bar{\alpha}_t}\, s} \underbrace{\mathcal{L}_{\text{DSM}}}_{\text{多尺度DSM}} \times (1-\bar{\alpha}_t)$$

这一链条说明：DDPM训练的本质是多尺度的去噪得分匹配，而去噪得分匹配是Fisher divergence最小化的实用近似。

---

## Part 8: Continuous-Time Score Matching **[Song et al. 2021]**

### 8.1 统一训练目标 **[Song et al. 2021, Eq.(7)]**

Song et al. 提出连续时间的统一训练目标，将离散噪声水平推广到无穷多个：

$$\min_\theta \mathbb{E}_{\mathbf{x}_0 \sim p_0}\mathbb{E}_{t \sim \mathcal{U}(0,T)}\mathbb{E}_{\mathbf{x}_t \sim p_{0t}(\mathbf{x}|\mathbf{x}_0)}\left[\lambda(t)\|\mathbf{s}_\theta(\mathbf{x}_t, t) - \nabla_{\mathbf{x}_t}\log p_{0t}(\mathbf{x}_t|\mathbf{x}_0)\|^2\right]$$

其中 $\lambda: [0,T] \to \mathbb{R}_{>0}$ 是正权重函数，$\mathcal{U}(0,T)$ 是 $[0,T]$ 上的均匀分布。

NCSN 和 DDPM 的训练目标分别是这个连续目标在离散时间步上的近似。

### 8.2 NCSN 与 DDPM 目标函数的统一形式

**NCSN 目标** **[Song et al. 2021, Eq.(1)]**：

$$\theta^* = \arg\min_\theta \sum_{i=1}^N \sigma_i^2 \mathbb{E}_{p_{\text{data}}(\mathbf{x})}\mathbb{E}_{p_{\sigma_i}(\tilde{\mathbf{x}}|\mathbf{x})}\left[\|\mathbf{s}_\theta(\tilde{\mathbf{x}}, \sigma_i) - \nabla_{\tilde{\mathbf{x}}}\log p_{\sigma_i}(\tilde{\mathbf{x}}|\mathbf{x})\|^2\right]$$

**DDPM 目标** **[Song et al. 2021, Eq.(3)]**：

$$\theta^* = \arg\min_\theta \sum_{i=1}^N (1-\alpha_i)\mathbb{E}_{p_{\text{data}}(\mathbf{x})}\mathbb{E}_{p_{\alpha_i}(\tilde{\mathbf{x}}|\mathbf{x})}\left[\|\mathbf{s}_\theta(\tilde{\mathbf{x}}, i) - \nabla_{\tilde{\mathbf{x}}}\log p_{\alpha_i}(\tilde{\mathbf{x}}|\mathbf{x})\|^2\right]$$

关键观察 **[Song et al. 2021, Section 2.2]**：两个目标中第 $i$ 项的权重（$\sigma_i^2$ 和 $1-\alpha_i$）与对应扰动核的条件得分范数的倒数成正比：

$$\sigma_i^2 \propto 1/\mathbb{E}\left[\|\nabla_\mathbf{x}\log p_{\sigma_i}(\tilde{\mathbf{x}}|\mathbf{x})\|^2\right], \quad (1-\alpha_i) \propto 1/\mathbb{E}\left[\|\nabla_\mathbf{x}\log p_{\alpha_i}(\tilde{\mathbf{x}}|\mathbf{x})\|^2\right]$$

### 8.3 VE-SDE 和 VP-SDE 的条件得分

**VE-SDE** 的转移核 **[Song et al. 2021, Eq.(29)]** 为 $p_{0t}(\mathbf{x}(t)|\mathbf{x}(0)) = \mathcal{N}(\mathbf{x}(t); \mathbf{x}(0), [\sigma^2(t) - \sigma^2(0)]\mathbf{I})$，条件得分为：

$$\nabla_{\mathbf{x}_t}\log p_{0t}(\mathbf{x}_t|\mathbf{x}_0) = -\frac{\mathbf{x}_t - \mathbf{x}_0}{\sigma^2(t) - \sigma^2(0)}$$

**VP-SDE** 的转移核 **[Song et al. 2021, Eq.(33)]** 为 $p_{0t}(\mathbf{x}(t)|\mathbf{x}(0)) = \mathcal{N}(\mathbf{x}(t); e^{-\frac{1}{2}\int_0^t\beta(s)ds}\mathbf{x}(0), (1-e^{-\int_0^t\beta(s)ds})\mathbf{I})$，条件得分为：

$$\nabla_{\mathbf{x}_t}\log p_{0t}(\mathbf{x}_t|\mathbf{x}_0) = -\frac{\mathbf{x}_t - e^{-\frac{1}{2}\int_0^t\beta(s)ds}\mathbf{x}_0}{1 - e^{-\int_0^t\beta(s)ds}}$$

### 8.4 Sliced Score Matching 替代方案 **[Song et al. 2021, Appendix A, Eq.(35)]**

当 SDE 不是线性的（转移核无闭式解）时，可用 sliced score matching 替代 DSM：

$$\theta^* = \arg\min_\theta \mathbb{E}_t\left\{\lambda(t)\mathbb{E}_{\mathbf{x}(0)}\mathbb{E}_{\mathbf{x}(t)}\mathbb{E}_{\mathbf{v}\sim p_\mathbf{v}}\left[\frac{1}{2}\|\mathbf{s}_\theta(\mathbf{x}(t), t)\|^2 + \mathbf{v}^\top\nabla_\mathbf{x}\mathbf{s}_\theta(\mathbf{x}(t), t)\mathbf{v}\right]\right\}$$

其中 $\mathbb{E}[\mathbf{v}] = \mathbf{0}$，$\operatorname{Cov}[\mathbf{v}] = \mathbf{I}$。

---

## References

1. Hyvarinen, A. (2005). Estimation of Non-Normalized Statistical Models by Score Matching. JMLR.
2. Vincent, P. (2011). A Connection Between Score Matching and Denoising Autoencoders. Neural Computation.
3. Song, Y. & Ermon, S. (2019). Generative Modeling by Estimating Gradients of the Data Distribution. NeurIPS.
4. Song, Y. & Ermon, S. (2020). Improved Techniques for Training Score-Based Generative Models. NeurIPS.
5. Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. NeurIPS.
6. Song, Y., Sohl-Dickstein, J., Kingma, D.P., Kumar, A., Ermon, S., & Poole, B. (2021). Score-Based Generative Modeling through Stochastic Differential Equations. ICLR.
