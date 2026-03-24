# ELBO Derivation

> **Tags**: `elbo`, `variational-inference`, `kl-divergence`, `vae`

## Statement

推导 Evidence Lower BOund (ELBO) 及其在变分推断中的核心作用。从对数边际似然 $\log p(x)$ 出发，通过引入隐变量和Jensen不等式得到ELBO，分析其分解形式，并建立与VAE和扩散模型的联系。

## Prerequisites

- KL散度定义及非负性（Gibbs不等式）
- Jensen不等式：$f(\mathbb{E}[X]) \geq \mathbb{E}[f(X)]$（对凸函数取 $\leq$，$\log$ 是凹函数取 $\geq$）
- 贝叶斯定理：$p(z|x) = \frac{p(x|z)p(z)}{p(x)}$
- 期望的定义与线性性

---

## Part 1: Motivation — 边际似然与后验推断

### 1.1 生成模型的目标

给定观测数据 $x$ 和隐变量 $z$，生成模型定义联合分布 $p_\theta(x, z) = p_\theta(x|z)\, p(z)$。

**训练目标**：最大化边际似然（evidence）：

$$p_\theta(x) = \int p_\theta(x|z)\, p(z)\, dz$$

**问题**：这个积分通常是intractable的（维度高、被积函数复杂）。

### 1.2 后验推断的困难

真实后验：

$$p_\theta(z|x) = \frac{p_\theta(x|z)\, p(z)}{p_\theta(x)}$$

由于分母 $p_\theta(x)$ 就是那个intractable的积分，后验也无法精确计算。

**解决方案**：用一个简单的分布族 $q_\phi(z|x)$（变分分布）来近似真实后验 $p_\theta(z|x)$。

---

## Part 2: ELBO Derivation — Method 1 (Jensen's Inequality)

### 2.1 从对数边际似然出发

$$\log p_\theta(x) = \log \int p_\theta(x, z)\, dz$$

### 2.2 引入变分分布

$$= \log \int \frac{p_\theta(x, z)}{q_\phi(z|x)}\, q_\phi(z|x)\, dz$$

$$= \log \mathbb{E}_{q_\phi(z|x)}\left[\frac{p_\theta(x, z)}{q_\phi(z|x)}\right]$$

### 2.3 应用 Jensen 不等式

由于 $\log$ 是凹函数，Jensen不等式给出：

$$\log \mathbb{E}_{q_\phi(z|x)}\left[\frac{p_\theta(x, z)}{q_\phi(z|x)}\right] \geq \mathbb{E}_{q_\phi(z|x)}\left[\log \frac{p_\theta(x, z)}{q_\phi(z|x)}\right]$$

因此：

$$\boxed{\log p_\theta(x) \geq \mathbb{E}_{q_\phi(z|x)}\left[\log \frac{p_\theta(x, z)}{q_\phi(z|x)}\right] \triangleq \mathcal{L}_{\mathrm{ELBO}}(\theta, \phi; x)}$$

### 2.4 展开 ELBO

$$\mathcal{L}_{\mathrm{ELBO}} = \mathbb{E}_{q_\phi(z|x)}\left[\log p_\theta(x, z) - \log q_\phi(z|x)\right]$$

$$= \mathbb{E}_{q_\phi(z|x)}\left[\log p_\theta(x|z) + \log p(z) - \log q_\phi(z|x)\right]$$

$$\boxed{= \underbrace{\mathbb{E}_{q_\phi(z|x)}\left[\log p_\theta(x|z)\right]}_{\text{重构项 (reconstruction)}} - \underbrace{D_{\mathrm{KL}}\left(q_\phi(z|x) \| p(z)\right)}_{\text{正则化项 (regularization)}}}$$

**解释**：
- **重构项**：鼓励解码器从隐变量 $z$ 准确重建 $x$
- **KL项**：约束变分后验 $q_\phi(z|x)$ 不偏离先验 $p(z)$ 太远

---

## Part 3: ELBO Derivation — Method 2 (KL Divergence)

### 3.1 从 KL 散度出发

$$D_{\mathrm{KL}}\left(q_\phi(z|x) \| p_\theta(z|x)\right) = \mathbb{E}_{q_\phi(z|x)}\left[\log \frac{q_\phi(z|x)}{p_\theta(z|x)}\right]$$

### 3.2 展开真实后验

$$= \mathbb{E}_{q_\phi(z|x)}\left[\log \frac{q_\phi(z|x)}{p_\theta(x,z) / p_\theta(x)}\right]$$

$$= \mathbb{E}_{q_\phi(z|x)}\left[\log q_\phi(z|x) - \log p_\theta(x,z) + \log p_\theta(x)\right]$$

### 3.3 提出常数项

$\log p_\theta(x)$ 不依赖于 $z$，可以提出期望：

$$= \log p_\theta(x) + \mathbb{E}_{q_\phi(z|x)}\left[\log q_\phi(z|x) - \log p_\theta(x,z)\right]$$

$$= \log p_\theta(x) - \mathbb{E}_{q_\phi(z|x)}\left[\log \frac{p_\theta(x,z)}{q_\phi(z|x)}\right]$$

### 3.4 整理得到核心等式

$$\boxed{\log p_\theta(x) = \mathcal{L}_{\mathrm{ELBO}}(\theta, \phi; x) + D_{\mathrm{KL}}\left(q_\phi(z|x) \| p_\theta(z|x)\right)}$$

由于 $D_{\mathrm{KL}} \geq 0$（Gibbs不等式），立即得到：

$$\log p_\theta(x) \geq \mathcal{L}_{\mathrm{ELBO}}$$

### 3.5 Gap 分析

ELBO与真实对数似然之间的gap恰好是变分后验与真实后验的KL散度：

$$\mathrm{Gap} = D_{\mathrm{KL}}\left(q_\phi(z|x) \| p_\theta(z|x)\right) \geq 0$$

- 当 $q_\phi(z|x) = p_\theta(z|x)$ 时，gap = 0，ELBO变成等式
- 最大化ELBO等价于同时（1）最大化 $\log p_\theta(x)$ 和（2）最小化gap

---

## Part 4: KL Divergence Properties

### 4.1 非负性证明 (Gibbs' Inequality)

$$D_{\mathrm{KL}}(q \| p) = \mathbb{E}_q\left[\log \frac{q(x)}{p(x)}\right] = -\mathbb{E}_q\left[\log \frac{p(x)}{q(x)}\right]$$

由Jensen不等式（$-\log$ 是凸函数）：

$$\geq -\log \mathbb{E}_q\left[\frac{p(x)}{q(x)}\right] = -\log \int q(x) \frac{p(x)}{q(x)}\, dx = -\log \int p(x)\, dx = -\log 1 = 0$$

等号成立当且仅当 $p = q$ a.e.。 $\blacksquare$

### 4.2 高斯 KL 散度闭式解

对于 $q = \mathcal{N}(\mu_q, \Sigma_q)$ 和 $p = \mathcal{N}(\mu_p, \Sigma_p)$：

$$D_{\mathrm{KL}}(q \| p) = \frac{1}{2}\left[\log\frac{|\Sigma_p|}{|\Sigma_q|} - d + \mathrm{tr}(\Sigma_p^{-1}\Sigma_q) + (\mu_p - \mu_q)^T \Sigma_p^{-1} (\mu_p - \mu_q)\right]$$

**推导**：

$$D_{\mathrm{KL}} = \mathbb{E}_q[\log q - \log p]$$

对多元高斯，$\log \mathcal{N}(x; \mu, \Sigma) = -\frac{d}{2}\log(2\pi) - \frac{1}{2}\log|\Sigma| - \frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)$

$$\log q(x) - \log p(x) = -\frac{1}{2}\log|\Sigma_q| + \frac{1}{2}\log|\Sigma_p| - \frac{1}{2}(x-\mu_q)^T\Sigma_q^{-1}(x-\mu_q) + \frac{1}{2}(x-\mu_p)^T\Sigma_p^{-1}(x-\mu_p)$$

取期望（利用 $\mathbb{E}_q[(x-\mu_q)(x-\mu_q)^T] = \Sigma_q$）：

$$D_{\mathrm{KL}} = \frac{1}{2}\left[\log\frac{|\Sigma_p|}{|\Sigma_q|} - d + \mathrm{tr}(\Sigma_p^{-1}\Sigma_q) + (\mu_p-\mu_q)^T\Sigma_p^{-1}(\mu_p-\mu_q)\right]$$

**对角情况**（VAE常用）：$\Sigma_q = \mathrm{diag}(\sigma_q^2)$，$\Sigma_p = I$，$\mu_p = 0$：

$$D_{\mathrm{KL}}(q \| p) = \frac{1}{2}\sum_{j=1}^{d}\left[-\log \sigma_{q,j}^2 - 1 + \sigma_{q,j}^2 + \mu_{q,j}^2\right]$$

---

## Part 5: VAE — ELBO in Practice

### 5.1 VAE 架构

- **编码器**（变分后验）：$q_\phi(z|x) = \mathcal{N}(z;\; \mu_\phi(x),\; \mathrm{diag}(\sigma_\phi^2(x)))$
- **解码器**（似然）：$p_\theta(x|z)$（高斯或Bernoulli）
- **先验**：$p(z) = \mathcal{N}(0, I)$

### 5.2 VAE 损失函数

$$\mathcal{L}_{\mathrm{VAE}} = -\mathcal{L}_{\mathrm{ELBO}} = -\mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] + D_{\mathrm{KL}}(q_\phi(z|x) \| p(z))$$

### 5.3 Reparameterization Trick

为了对 $\phi$ 求梯度，需要让采样操作可微分：

$$z = \mu_\phi(x) + \sigma_\phi(x) \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

这样 $\nabla_\phi \mathbb{E}_{q_\phi}[f(z)] = \mathbb{E}_{\epsilon}[\nabla_\phi f(\mu_\phi + \sigma_\phi \odot \epsilon)]$，可用蒙特卡洛估计。

---

## Part 6: Diffusion Model ELBO **[Ho et al. 2020, §2]**

### 6.1 层级 VAE 视角 **[Ho et al. 2020, §2]**

扩散模型是一个有 $T$ 层隐变量的 VAE，ELBO为 **[Ho et al. 2020, Eq.(3)]**：

$$\log p(x_0) \geq \mathbb{E}_{q(x_{1:T}|x_0)}\left[\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$

### 6.2 展开与分组

$$-\mathcal{L}_{\mathrm{VLB}} = \mathbb{E}_q\left[\log \frac{q(x_{1:T}|x_0)}{p_\theta(x_{0:T})}\right]$$

分子展开（马尔可夫链）：

$$q(x_{1:T}|x_0) = \prod_{t=1}^T q(x_t|x_{t-1})$$

分母展开：

$$p_\theta(x_{0:T}) = p(x_T) \prod_{t=1}^T p_\theta(x_{t-1}|x_t)$$

### 6.3 利用贝叶斯定理重写

对 $t \geq 2$，$q(x_t|x_{t-1}) = \frac{q(x_{t-1}|x_t, x_0)\, q(x_t|x_0)}{q(x_{t-1}|x_0)}$

代入后，telescoping cancellation给出：

**[Ho et al. 2020, Eq.(5)]**:

$$-\mathcal{L}_{\mathrm{VLB}} = \underbrace{D_{\mathrm{KL}}(q(x_T|x_0) \| p(x_T))}_{L_T}$$

$$+ \sum_{t=2}^{T} \underbrace{\mathbb{E}_{q(x_t|x_0)}\left[D_{\mathrm{KL}}(q(x_{t-1}|x_t, x_0) \| p_\theta(x_{t-1}|x_t))\right]}_{L_{t-1}}$$

$$+ \underbrace{\mathbb{E}_{q(x_1|x_0)}[-\log p_\theta(x_0|x_1)]}_{L_0}$$

### 6.4 Telescoping 推导细节

写出对数比：

$$\log \frac{q(x_{1:T}|x_0)}{p_\theta(x_{0:T})} = \log \frac{q(x_1|x_0) \prod_{t=2}^T q(x_t|x_{t-1})}{p(x_T) p_\theta(x_0|x_1) \prod_{t=2}^T p_\theta(x_{t-1}|x_t)}$$

对 $t \geq 2$，将 $q(x_t|x_{t-1})$ 替换为 $\frac{q(x_{t-1}|x_t, x_0) q(x_t|x_0)}{q(x_{t-1}|x_0)}$：

$$= \log \frac{q(x_1|x_0)}{p_\theta(x_0|x_1)} + \log \frac{1}{p(x_T)} + \sum_{t=2}^T \log \frac{q(x_{t-1}|x_t,x_0)\, q(x_t|x_0)}{q(x_{t-1}|x_0)\, p_\theta(x_{t-1}|x_t)}$$

$q(x_t|x_0)/q(x_{t-1}|x_0)$ 形成telescoping product：

$$\prod_{t=2}^T \frac{q(x_t|x_0)}{q(x_{t-1}|x_0)} = \frac{q(x_T|x_0)}{q(x_1|x_0)}$$

所以：

$$= -\log p_\theta(x_0|x_1) + \log \frac{q(x_T|x_0)}{p(x_T)} + \sum_{t=2}^T \log \frac{q(x_{t-1}|x_t,x_0)}{p_\theta(x_{t-1}|x_t)}$$

取期望即得 $L_T + \sum L_{t-1} + L_0$ 的分解。 $\blacksquare$

### 6.5 各项的含义

| 项 | 含义 | 可学习？ |
|---|---|---|
| $L_T$ | 前向过程终态与先验的匹配 | 否（固定） |
| $L_{t-1}$ | 反向过程每步的去噪质量 | 是（核心项） |
| $L_0$ | 重构质量 | 是 |

每个 $L_{t-1}$ 是两个高斯之间的KL散度，有闭式解。简化后就得到DDPM的noise prediction loss。

详细推导见 [diffusion_models_math.md](diffusion_models_math.md)。

---

## Summary

ELBO推导的核心路径：

$$\log p(x) = \mathcal{L}_{\mathrm{ELBO}} + D_{\mathrm{KL}}(q \| p_{\text{true posterior}})$$

- Method 1 (Jensen): $\log \mathbb{E}[\cdot] \geq \mathbb{E}[\log(\cdot)]$
- Method 2 (KL): 从 $D_{\mathrm{KL}} \geq 0$ 直接得到

ELBO的分解：重构 + 正则化，在VAE和扩散模型中分别有不同的具体形式，但数学本质一致。

---

## Part 7: Detailed VLB Derivation from Ho et al. **[Ho et al. 2020]**

### 7.1 从原始 VLB 到 KL 分解的严格推导 **[Ho et al. 2020, Eq.(3)→(5)]**

原始变分界 **[Ho et al. 2020, Eq.(3)]**：

$$L = \mathbb{E}_q\left[-\log p(\mathbf{x}_T) - \sum_{t \geq 1} \log\frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)}{q(\mathbf{x}_t|\mathbf{x}_{t-1})}\right]$$

**关键步骤**：将 $q(\mathbf{x}_t|\mathbf{x}_{t-1})$ 用贝叶斯定理改写。对 $t \geq 2$：

$$q(\mathbf{x}_t|\mathbf{x}_{t-1}) = \frac{q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0)\,q(\mathbf{x}_t|\mathbf{x}_0)}{q(\mathbf{x}_{t-1}|\mathbf{x}_0)}$$

代入原式中 $\sum_{t>1}$ 的部分，对数比值变为：

$$\sum_{t>1}\log\frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)}{q(\mathbf{x}_t|\mathbf{x}_{t-1})} = \sum_{t>1}\log\frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)\,q(\mathbf{x}_{t-1}|\mathbf{x}_0)}{q(\mathbf{x}_{t-1}|\mathbf{x}_t,\mathbf{x}_0)\,q(\mathbf{x}_t|\mathbf{x}_0)}$$

$q(\mathbf{x}_t|\mathbf{x}_0)/q(\mathbf{x}_{t-1}|\mathbf{x}_0)$ 形成 telescoping 乘积：

$$\prod_{t=2}^T \frac{q(\mathbf{x}_t|\mathbf{x}_0)}{q(\mathbf{x}_{t-1}|\mathbf{x}_0)} = \frac{q(\mathbf{x}_T|\mathbf{x}_0)}{q(\mathbf{x}_1|\mathbf{x}_0)}$$

最终得到 **[Ho et al. 2020, Eq.(5)]**：

$$\boxed{L = \underbrace{D_{\mathrm{KL}}(q(\mathbf{x}_T|\mathbf{x}_0)\|p(\mathbf{x}_T))}_{L_T} + \sum_{t>1}\underbrace{D_{\mathrm{KL}}(q(\mathbf{x}_{t-1}|\mathbf{x}_t,\mathbf{x}_0)\|p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t))}_{L_{t-1}} - \underbrace{\log p_\theta(\mathbf{x}_0|\mathbf{x}_1)}_{-L_0}}$$

### 7.2 简化目标的权重分析 **[Ho et al. 2020, Section 3.4]**

完整 VLB 中每一项 $L_{t-1}$ 的权重因子为 $\frac{\beta_t^2}{2\sigma_t^2\alpha_t(1-\bar{\alpha}_t)}$，而简化目标 $L_{\text{simple}}$ 将其统一为 1。

Ho et al. 的分析表明：这种重新加权**下调了小 $t$（低噪声）处的损失权重**，使网络能专注于更困难的大 $t$（高噪声）去噪任务。实验证实 $L_{\text{simple}}$ 虽然不是 VLB 的严格上界，但给出更好的样本质量（FID 3.17 vs. 13.51）。

### 7.3 VLB 的另一种等价形式 **[Ho et al. 2020, Section 4.2]**

$$L = D_{\mathrm{KL}}(q(\mathbf{x}_T)\|p(\mathbf{x}_T)) + \mathbb{E}_q\left[\sum_{t \geq 1} D_{\mathrm{KL}}(q(\mathbf{x}_{t-1}|\mathbf{x}_t)\|p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t))\right] + H(\mathbf{x}_0)$$

注意这里使用的是**无条件**后验 $q(\mathbf{x}_{t-1}|\mathbf{x}_t)$（而非 $q(\mathbf{x}_{t-1}|\mathbf{x}_t,\mathbf{x}_0)$），因此 KL 散度度量的是反向过程每步的真实误差。

---

## Part 8: Original VAE ELBO — Kingma & Welling (2014)

> 本节直接基于 **[Kingma & Welling 2014]** 原文推导，保留原始记号。

### 8.1 问题设定 **[Kingma & Welling 2014, §2.1]**

数据集 $\mathbf{X} = \{\mathbf{x}^{(i)}\}_{i=1}^N$，由 i.i.d. 样本组成。假设数据生成过程涉及不可观测的连续随机变量 $\mathbf{z}$：

1. $\mathbf{z}^{(i)} \sim p_{\boldsymbol{\theta}^*}(\mathbf{z})$（先验）
2. $\mathbf{x}^{(i)} \sim p_{\boldsymbol{\theta}^*}(\mathbf{x}|\mathbf{z})$（条件似然）

**核心困难**：
- 边际似然 $p_{\boldsymbol{\theta}}(\mathbf{x}) = \int p_{\boldsymbol{\theta}}(\mathbf{z}) p_{\boldsymbol{\theta}}(\mathbf{x}|\mathbf{z})\,d\mathbf{z}$ 不可积
- 真实后验 $p_{\boldsymbol{\theta}}(\mathbf{z}|\mathbf{x})$ 不可求
- 均场 VB 中的期望也不可解析

### 8.2 变分界 **[Kingma & Welling 2014, §2.2]**

引入识别模型（recognition model）$q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x})$ 近似不可解的后验。对单个数据点 $\mathbf{x}^{(i)}$ 的对数边际似然：

$$\log p_{\boldsymbol{\theta}}(\mathbf{x}^{(i)}) = D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}^{(i)}) \| p_{\boldsymbol{\theta}}(\mathbf{z}|\mathbf{x}^{(i)})) + \mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}^{(i)})$$

**ELBO 的两种等价形式**：

**形式 A**（联合概率形式）**[Kingma & Welling 2014, Eq.(1)]**：

$$\mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}^{(i)}) = \mathbb{E}_{q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x})}\left[-\log q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}) + \log p_{\boldsymbol{\theta}}(\mathbf{x}, \mathbf{z})\right]$$

**形式 B**（KL + 重构）**[Kingma & Welling 2014, Eq.(2)]**：

$$\boxed{\mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}^{(i)}) = -D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}^{(i)}) \| p_{\boldsymbol{\theta}}(\mathbf{z})) + \mathbb{E}_{q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}^{(i)})}\left[\log p_{\boldsymbol{\theta}}(\mathbf{x}^{(i)}|\mathbf{z})\right]}$$

- 第一项：KL 正则化，约束近似后验逼近先验
- 第二项：期望重构误差

### 8.3 重参数化技巧 **[Kingma & Welling 2014, §2.4]**

**问题**：朴素的 Monte Carlo 梯度估计器 $\nabla_{\boldsymbol{\phi}} \mathbb{E}_{q_{\boldsymbol{\phi}}}[f(\mathbf{z})]$ 方差极高，不实用。

**解决方案**：将随机变量 $\tilde{\mathbf{z}} \sim q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x})$ 重参数化为：

$$\tilde{\mathbf{z}} = g_{\boldsymbol{\phi}}(\boldsymbol{\epsilon}, \mathbf{x}), \quad \boldsymbol{\epsilon} \sim p(\boldsymbol{\epsilon})$$

**证明** **[Kingma & Welling 2014, §2.4]**：给定确定性映射 $\mathbf{z} = g_{\boldsymbol{\phi}}(\boldsymbol{\epsilon}, \mathbf{x})$，由变量替换：

$$q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}) \prod_i dz_i = p(\boldsymbol{\epsilon}) \prod_i d\epsilon_i$$

因此：

$$\int q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}) f(\mathbf{z})\,d\mathbf{z} = \int p(\boldsymbol{\epsilon}) f(g_{\boldsymbol{\phi}}(\boldsymbol{\epsilon}, \mathbf{x}))\,d\boldsymbol{\epsilon} \simeq \frac{1}{L}\sum_{l=1}^L f(g_{\boldsymbol{\phi}}(\boldsymbol{\epsilon}^{(l)}, \mathbf{x}))$$

此估计器关于 $\boldsymbol{\phi}$ 可微分。

**三类适用分布** **[Kingma & Welling 2014, §2.4]**：

1. **可逆 CDF**：$\boldsymbol{\epsilon} \sim \mathcal{U}(\mathbf{0}, \mathbf{I})$，$g$ 为逆 CDF（适用于指数、柯西、Logistic 等分布）
2. **位置-尺度族**：$g(.) = \text{location} + \text{scale} \cdot \boldsymbol{\epsilon}$（适用于高斯、拉普拉斯、Student-t 等）
3. **复合法**：变换的组合（适用于对数正态、Gamma、Dirichlet、Beta 等）

### 8.4 SGVB 估计器 **[Kingma & Welling 2014, §2.3]**

**估计器 A**（通用形式）：

$$\widetilde{\mathcal{L}}^A(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}^{(i)}) = \frac{1}{L}\sum_{l=1}^L \left[\log p_{\boldsymbol{\theta}}(\mathbf{x}^{(i)}, \mathbf{z}^{(i,l)}) - \log q_{\boldsymbol{\phi}}(\mathbf{z}^{(i,l)}|\mathbf{x}^{(i)})\right]$$

其中 $\mathbf{z}^{(i,l)} = g_{\boldsymbol{\phi}}(\boldsymbol{\epsilon}^{(i,l)}, \mathbf{x}^{(i)})$，$\boldsymbol{\epsilon}^{(l)} \sim p(\boldsymbol{\epsilon})$。

**估计器 B**（低方差版本，KL 可解析时）：

$$\boxed{\widetilde{\mathcal{L}}^B(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}^{(i)}) = -D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}^{(i)}) \| p_{\boldsymbol{\theta}}(\mathbf{z})) + \frac{1}{L}\sum_{l=1}^L \log p_{\boldsymbol{\theta}}(\mathbf{x}^{(i)}|\mathbf{z}^{(i,l)})}$$

**Minibatch 估计器**：

$$\mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{X}) \simeq \widetilde{\mathcal{L}}^M(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{X}^M) = \frac{N}{M}\sum_{i=1}^M \widetilde{\mathcal{L}}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}^{(i)})$$

实验中 $L=1$（每数据点一个样本），$M=100$（minibatch大小）即可。

### 8.5 高斯 VAE 闭式 KL **[Kingma & Welling 2014, Appendix B]**

设先验 $p_{\boldsymbol{\theta}}(\mathbf{z}) = \mathcal{N}(\mathbf{0}, \mathbf{I})$，近似后验 $q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}^{(i)}) = \mathcal{N}(\boldsymbol{\mu}^{(i)}, \boldsymbol{\sigma}^{2(i)}\mathbf{I})$，$J$ 维隐空间。

**推导**：

$$\int q(\mathbf{z}) \log p(\mathbf{z})\,d\mathbf{z} = \int \mathcal{N}(\mathbf{z}; \boldsymbol{\mu}, \boldsymbol{\sigma}^2) \log \mathcal{N}(\mathbf{z}; \mathbf{0}, \mathbf{I})\,d\mathbf{z} = -\frac{J}{2}\log(2\pi) - \frac{1}{2}\sum_{j=1}^J (\mu_j^2 + \sigma_j^2)$$

$$\int q(\mathbf{z}) \log q(\mathbf{z})\,d\mathbf{z} = -\frac{J}{2}\log(2\pi) - \frac{1}{2}\sum_{j=1}^J (1 + \log \sigma_j^2)$$

因此：

$$\boxed{-D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}^{(i)}) \| p(\mathbf{z})) = \frac{1}{2}\sum_{j=1}^J \left(1 + \log(\sigma_j^{(i)})^2 - (\mu_j^{(i)})^2 - (\sigma_j^{(i)})^2\right)}$$

### 8.6 完整高斯 VAE 估计器 **[Kingma & Welling 2014, §3]**

将闭式 KL 与蒙特卡洛重构项结合：

$$\boxed{\mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}^{(i)}) \simeq \frac{1}{2}\sum_{j=1}^J \left(1 + \log(\sigma_j^{(i)})^2 - (\mu_j^{(i)})^2 - (\sigma_j^{(i)})^2\right) + \frac{1}{L}\sum_{l=1}^L \log p_{\boldsymbol{\theta}}(\mathbf{x}^{(i)}|\mathbf{z}^{(i,l)})}$$

其中 $\mathbf{z}^{(i,l)} = \boldsymbol{\mu}^{(i)} + \boldsymbol{\sigma}^{(i)} \odot \boldsymbol{\epsilon}^{(l)}$，$\boldsymbol{\epsilon}^{(l)} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$。

### 8.7 AEVB 算法 **[Kingma & Welling 2014, Algorithm 1]**

```
Algorithm: Auto-Encoding Variational Bayes (AEVB)
Input: θ, φ ← 初始化参数
Repeat:
    X^M ← 从完整数据集随机抽取 M 个数据点
    ε ← 从噪声分布 p(ε) 采样
    g ← ∇_{θ,φ} L̃^M(θ, φ; X^M, ε)  (minibatch 估计器梯度)
    θ, φ ← 用梯度 g 更新参数 (SGD 或 Adagrad)
Until 参数 (θ, φ) 收敛
Return θ, φ
```

**关键设计选择**：编码器和解码器均使用单隐层 MLP，实验设置 $M=100$, $L=1$。

---

## References

1. Kingma, D.P. & Welling, M. (2014). Auto-Encoding Variational Bayes. ICLR.
2. Blei, D.M., Kucukelbir, A., & McAuliffe, J.D. (2017). Variational Inference: A Review for Statisticians. JASA.
3. Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. NeurIPS.
4. Jordan, M.I., Ghahramani, Z., Jaakkola, T.S., & Saul, L.K. (1999). An Introduction to Variational Methods for Graphical Models. Machine Learning.
