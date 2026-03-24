# Variational Inference Basics

> **Tags**: `variational-inference`, `elbo`, `mean-field`, `approximate-inference`

## Statement

推导变分推断（Variational Inference, VI）的基本框架：将后验推断问题转化为优化问题。从intractable后验出发，定义变分族，推导ELBO最大化目标，给出均场近似的具体形式，并讨论与采样方法（MCMC）的对比。

## Prerequisites

- KL散度及其性质（见 [elbo_derivation.md](elbo_derivation.md)）
- 指数族分布
- 凸优化基础
- 条件独立与图模型（基本概念）
- 贝叶斯推断框架

---

## Part 1: The Posterior Inference Problem

### 1.1 贝叶斯推断框架

给定：
- 观测数据 $x = \{x_1, \ldots, x_n\}$
- 隐变量 $z = \{z_1, \ldots, z_m\}$（可包含模型参数）
- 联合分布 $p(x, z) = p(x|z)\, p(z)$

目标：计算后验分布

$$p(z|x) = \frac{p(x|z)\, p(z)}{p(x)} = \frac{p(x, z)}{\int p(x, z)\, dz}$$

### 1.2 为什么后验计算困难？

分母（evidence/边际似然）：

$$p(x) = \int p(x, z)\, dz$$

- 积分维度可能很高（$z$ 是高维的）
- 被积函数可能没有解析形式
- 即使有解析形式，积分也可能是intractable的

**例子**：
- 混合高斯模型：$z$ 是离散的聚类分配，$p(x) = \sum_z p(x|z)p(z)$ 有 $K^n$ 项
- 深度生成模型（VAE）：$p(x|z)$ 由神经网络参数化，积分无闭式
- 贝叶斯神经网络：$z$ 是所有网络权重，积分空间是超高维的

### 1.3 两类近似方法

| 方法 | 思想 | 优缺点 |
|---|---|---|
| **MCMC** | 构造马尔可夫链，平稳分布为 $p(z\|x)$ | 渐近精确，但慢 |
| **Variational Inference** | 在分布族中找最接近 $p(z\|x)$ 的 | 快，但有近似误差 |

---

## Part 2: Variational Inference Framework

### 2.1 核心思想

将推断问题转化为优化问题：

$$q^*(z) = \arg\min_{q \in \mathcal{Q}} D_{\mathrm{KL}}(q(z) \| p(z|x))$$

其中 $\mathcal{Q}$ 是变分族（variational family），一类tractable的分布。

### 2.2 KL散度方向的选择

**为什么用 $D_{\mathrm{KL}}(q \| p)$（forward KL）而不是 $D_{\mathrm{KL}}(p \| q)$（reverse KL）？**

两种KL有不同的行为：

- $D_{\mathrm{KL}}(q \| p)$（VI使用）：**mode-seeking**。$q$ 倾向于集中在 $p$ 的一个mode上，宁可漏掉mode也不在低概率区域有密度。
- $D_{\mathrm{KL}}(p \| q)$（期望传播等）：**mean-seeking/mass-covering**。$q$ 倾向覆盖 $p$ 的所有mode，可能在modes之间的低密度区域也有密度。

选择 $D_{\mathrm{KL}}(q \| p)$ 的实际原因：它可以转化为ELBO最大化，而 $D_{\mathrm{KL}}(p \| q)$ 需要从 $p(z|x)$ 采样，同样intractable。

### 2.3 ELBO推导（回顾）

$$D_{\mathrm{KL}}(q(z) \| p(z|x)) = \mathbb{E}_q\left[\log \frac{q(z)}{p(z|x)}\right]$$

$$= \mathbb{E}_q[\log q(z)] - \mathbb{E}_q[\log p(z|x)]$$

$$= \mathbb{E}_q[\log q(z)] - \mathbb{E}_q[\log p(x, z)] + \log p(x)$$

整理：

$$\log p(x) = D_{\mathrm{KL}}(q(z) \| p(z|x)) + \underbrace{\mathbb{E}_q[\log p(x, z)] - \mathbb{E}_q[\log q(z)]}_{\mathcal{L}_{\mathrm{ELBO}}(q)}$$

由于 $\log p(x)$ 是固定的：

$$\min_q D_{\mathrm{KL}}(q \| p(\cdot|x)) \iff \max_q \mathcal{L}_{\mathrm{ELBO}}(q)$$

### 2.4 ELBO的两种等价形式

**形式1：Energy + Entropy**

$$\mathcal{L}_{\mathrm{ELBO}} = \underbrace{\mathbb{E}_q[\log p(x, z)]}_{\text{energy (能量项)}} + \underbrace{H(q)}_{\text{entropy (熵)}}$$

其中 $H(q) = -\mathbb{E}_q[\log q(z)]$。

- Energy项鼓励 $q$ 把概率放在 $p(x,z)$ 大的地方
- Entropy项鼓励 $q$ 尽量"散开"（避免退化为点分布）

**形式2：Reconstruction - KL**

$$\mathcal{L}_{\mathrm{ELBO}} = \mathbb{E}_q[\log p(x|z)] - D_{\mathrm{KL}}(q(z) \| p(z))$$

这是VAE中使用的形式（见 [elbo_derivation.md](elbo_derivation.md)）。

---

## Part 3: Mean-Field Variational Inference

### 3.1 均场假设

最常见的变分族是完全分解的（mean-field）：

$$q(z) = \prod_{j=1}^{m} q_j(z_j)$$

即假设隐变量之间相互独立。这大大简化了优化问题。

### 3.2 坐标上升变分推断 (CAVI)

**目标**：在固定其他 $q_{-j} = \{q_i : i \neq j\}$ 的条件下，优化 $q_j(z_j)$。

**推导**：

$$\mathcal{L}_{\mathrm{ELBO}} = \mathbb{E}_q[\log p(x, z)] - \sum_{i=1}^m \mathbb{E}_{q_i}[\log q_i(z_i)]$$

只保留与 $q_j$ 有关的项：

$$\mathcal{L}[q_j] = \mathbb{E}_{q_j}\left[\mathbb{E}_{q_{-j}}[\log p(x, z)]\right] - \mathbb{E}_{q_j}[\log q_j(z_j)] + \text{const}$$

定义：

$$\log \tilde{p}(x, z_j) \triangleq \mathbb{E}_{q_{-j}}[\log p(x, z)]$$

则：

$$\mathcal{L}[q_j] = \mathbb{E}_{q_j}[\log \tilde{p}(x, z_j)] - \mathbb{E}_{q_j}[\log q_j(z_j)] + C$$

$$= -D_{\mathrm{KL}}(q_j(z_j) \| \tilde{p}(x, z_j)) + C'$$

（注意 $\tilde{p}$ 可能未归一化，但KL散度的最小值仍在 $q_j \propto \tilde{p}$ 时取到。）

**最优解**：

$$\boxed{q_j^*(z_j) \propto \exp\left(\mathbb{E}_{q_{-j}}[\log p(x, z)]\right)}$$

### 3.3 CAVI 算法

**Algorithm: Coordinate Ascent Variational Inference (CAVI)**

1. 初始化所有 $q_j(z_j)$
2. **Repeat** until convergence:
   - **For** $j = 1, \ldots, m$:
     - $q_j(z_j) \leftarrow \frac{1}{Z_j}\exp\left(\mathbb{E}_{q_{-j}}[\log p(x, z)]\right)$
3. 计算 $\mathcal{L}_{\mathrm{ELBO}}$ 监控收敛

**性质**：
- 每步保证ELBO不减（坐标上升）
- 收敛到局部最优（ELBO关于整个 $q$ 不是凸的，但关于每个 $q_j$ 是凸的）
- 在共轭指数族模型中，更新有闭式解

### 3.4 共轭指数族模型的CAVI

如果联合分布属于指数族：

$$p(x, z) = h(x, z)\, \exp(\eta^T t(x, z) - A(\eta))$$

且均场分解后每个 $q_j$ 也属于指数族，则CAVI更新简化为更新自然参数：

$$q_j^*(z_j) \propto \exp\left(\mathbb{E}_{q_{-j}}[\eta_j^T t_j(z_j)]\right)$$

自然参数的更新只涉及其他因子的充分统计量的期望——这正是共轭先验的优势。

---

## Part 4: Example — Gaussian Mixture Model

### 4.1 模型

$$\mu_k \sim \mathcal{N}(0, \sigma^2 I), \quad k = 1, \ldots, K$$

$$c_i \sim \mathrm{Categorical}(1/K, \ldots, 1/K), \quad i = 1, \ldots, n$$

$$x_i | c_i, \mu \sim \mathcal{N}(\mu_{c_i}, I)$$

隐变量 $z = \{\mu_1, \ldots, \mu_K, c_1, \ldots, c_n\}$。

### 4.2 均场假设

$$q(z) = \prod_{k=1}^K q(\mu_k) \prod_{i=1}^n q(c_i)$$

### 4.3 CAVI更新

**更新 $q(c_i)$**：

$$\log q^*(c_i = k) = \mathbb{E}_{q(\mu_k)}[\log \mathcal{N}(x_i; \mu_k, I)] + \text{const}$$

$$= -\frac{1}{2}\mathbb{E}_q[\|x_i - \mu_k\|^2] + \text{const}$$

$$= -\frac{1}{2}\|x_i - m_k\|^2 - \frac{1}{2}\mathrm{tr}(S_k) + \text{const}$$

其中 $m_k = \mathbb{E}_q[\mu_k]$，$S_k = \mathrm{Cov}_q(\mu_k)$。

归一化后得到 $q(c_i = k) = r_{ik}$（类似EM中的responsibility）。

**更新 $q(\mu_k)$**：

$$q^*(\mu_k) = \mathcal{N}(\mu_k;\; m_k, S_k)$$

其中：

$$S_k = \left(\frac{1}{\sigma^2}I + n_k I\right)^{-1}, \quad m_k = S_k \sum_{i=1}^n r_{ik}\, x_i$$

这里 $n_k = \sum_i r_{ik}$。

**类比EM**：CAVI的均场VI与EM算法非常相似，但VI给出的是后验的近似分布（不仅仅是点估计）。

---

## Part 5: Stochastic Variational Inference (SVI)

### 5.1 Motivation

CAVI需要遍历所有数据点来更新全局参数，对大数据集不可扩展。

### 5.2 随机优化

ELBO可以写成数据点的期望：

$$\mathcal{L} = \mathbb{E}_{q}\left[\sum_{i=1}^n \log p(x_i | z_i, \theta) + \log p(\theta) - \log q(\theta) - \sum_i \log q(z_i)\right]$$

用mini-batch $\mathcal{B} \subset \{1, \ldots, n\}$ 做无偏估计：

$$\hat{\mathcal{L}} = \frac{n}{|\mathcal{B}|}\sum_{i \in \mathcal{B}} \mathbb{E}_q[\log p(x_i | z_i, \theta) - \log q(z_i)] + \mathbb{E}_q[\log p(\theta) - \log q(\theta)]$$

### 5.3 SVI算法 (Hoffman et al., 2013)

1. 采样 mini-batch
2. 对局部隐变量做CAVI更新（只涉及mini-batch中的数据点）
3. 计算全局参数的自然梯度
4. 用步长 $\rho_t$ 做随机梯度更新

$$\lambda_{t+1} = (1 - \rho_t)\lambda_t + \rho_t \hat{\lambda}_t$$

其中 $\lambda$ 是全局变分参数，$\hat{\lambda}$ 是基于mini-batch的"局部最优"。

**步长条件**（Robbins-Monro）：$\sum_t \rho_t = \infty$，$\sum_t \rho_t^2 < \infty$。

---

## Part 6: Amortized Variational Inference

### 6.1 从SVI到摊销推断

传统VI为每个数据点 $x_i$ 维护独立的变分参数 $\phi_i$。**摊销推断**用一个共享的inference network $q_\phi(z|x)$：

$$\phi_i \text{ (per-data-point)} \longrightarrow q_\phi(z|x) \text{ (shared encoder)}$$

### 6.2 VAE作为摊销VI

VAE的编码器 $q_\phi(z|x) = \mathcal{N}(\mu_\phi(x), \sigma_\phi^2(x) I)$ 就是摊销推断：

- **优势**：新数据点无需重新优化，一次前向传播即得近似后验
- **代价**：amortization gap — 共享网络的近似能力有限，可能不如per-point优化精确

### 6.3 与扩散模型的联系

扩散模型可以看作一种特殊的摊销VI：

- **"编码器"**（前向过程）：$q(x_{1:T}|x_0) = \prod_t q(x_t|x_{t-1})$，是固定的（不可学习）
- **"解码器"**（反向过程）：$p_\theta(x_{0:T}) = p(x_T)\prod_t p_\theta(x_{t-1}|x_t)$，是可学习的
- **ELBO**：就是diffusion VLB（见 [elbo_derivation.md](elbo_derivation.md) Part 6）

与标准VAE的区别：
- VAE同时学习编码器和解码器
- 扩散模型固定编码器（前向加噪），只学习解码器（反向去噪）
- 扩散模型有 $T$ 层隐变量，比VAE的单层表达力更强

---

## Part 7: Beyond Mean-Field

### 7.1 Structured Variational Inference

放松均场假设，允许部分依赖：

$$q(z) = \prod_{g \in \text{groups}} q_g(z_g)$$

组内变量可以有依赖。例如，在时间序列中保留时间方向的依赖。

### 7.2 Normalizing Flows

用一系列可逆变换将简单分布变成复杂分布：

$$z_K = f_K \circ \cdots \circ f_1(z_0), \quad z_0 \sim q_0(z_0)$$

$$\log q_K(z_K) = \log q_0(z_0) - \sum_{k=1}^K \log\left|\det \frac{\partial f_k}{\partial z_{k-1}}\right|$$

可以与VI结合，增强变分族的表达力。

### 7.3 Variational Inference与MCMC的混合

- **MCMC within VI**：用MCMC步来改进变分近似
- **VI within MCMC**：用变分近似作为MCMC的proposal

---

## Summary

变分推断的核心思路：

$$\underbrace{p(z|x) \text{ intractable}}_{\text{问题}} \xrightarrow{\text{选择变分族 }\mathcal{Q}} \underbrace{\min_{q \in \mathcal{Q}} D_{\mathrm{KL}}(q \| p(z|x))}_{\text{优化问题}} \xlongequal{\text{等价}} \underbrace{\max_{q \in \mathcal{Q}} \mathcal{L}_{\mathrm{ELBO}}(q)}_{\text{可计算}}$$

发展脉络：

| 方法 | 变分族 | 优化 | 应用 |
|---|---|---|---|
| Mean-field CAVI | 全分解 | 坐标上升 | 传统贝叶斯模型 |
| SVI | 全分解 | 随机梯度 | 大规模数据 |
| Amortized VI (VAE) | 参数化网络 | SGD | 深度生成模型 |
| Diffusion VI | 固定编码器 | SGD on decoder | 扩散模型 |

---

## Part 8: Diffusion Models as Hierarchical VI **[Ho et al. 2020]**

### 8.1 扩散模型的变分推断视角 **[Ho et al. 2020, Section 2]**

Ho et al. 将扩散模型严格定义为隐变量模型：

$$p_\theta(\mathbf{x}_0) = \int p_\theta(\mathbf{x}_{0:T})d\mathbf{x}_{1:T}$$

其中 $\mathbf{x}_1, \ldots, \mathbf{x}_T$ 是与数据同维度的隐变量。关键区别在于：

**与标准 VAE 的对比**：

| 特性 | VAE | 扩散模型 |
|---|---|---|
| 近似后验 $q$ | 可学习 $q_\phi(z\|x)$ | 固定 $q(\mathbf{x}_{1:T}\|\mathbf{x}_0) = \prod q(\mathbf{x}_t\|\mathbf{x}_{t-1})$ |
| 先验 $p$ | 简单 $p(z) = \mathcal{N}(0,I)$ | $p(\mathbf{x}_T) = \mathcal{N}(0,I)$ |
| 解码器 | $p_\theta(x\|z)$ 任意 | $p_\theta(\mathbf{x}_{t-1}\|\mathbf{x}_t)$ 高斯 |
| 隐变量层数 | 1 | $T$（通常 1000） |
| KL gap | 由 $q_\phi$ 的表达力决定 | 由 $p_\theta$ 的去噪能力决定 |

### 8.2 $L_T$ 几乎为零的验证 **[Ho et al. 2020, Section 4]**

实验参数设置 $T=1000$，$\beta_1 = 10^{-4}$，$\beta_T = 0.02$（线性调度），使得：

$$L_T = D_{\mathrm{KL}}(q(\mathbf{x}_T|\mathbf{x}_0)\|p(\mathbf{x}_T)) \approx 10^{-5} \text{ bits/dim}$$

这验证了前向过程在 $T$ 步后确实将数据分布变换为近似标准高斯。

### 8.3 等价于去噪得分匹配的变分推断解释 **[Ho et al. 2020, Section 3.2]**

Ho et al. 的核心贡献之一是揭示：优化类似去噪得分匹配的目标**等价于**对类似 Langevin 动力学的采样链做变分推断。

具体地，VLB 中每一项 $L_{t-1}$ 在 $\epsilon$-参数化下变为 **[Ho et al. 2020, Eq.(12)]**：

$$\frac{\beta_t^2}{2\sigma_t^2\alpha_t(1-\bar{\alpha}_t)}\|\boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta(\sqrt{\bar{\alpha}_t}\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\boldsymbol{\epsilon}, t)\|^2$$

这同时是：
1. **变分推断**：最小化反向过程与真实后验之间的 KL 散度
2. **去噪得分匹配**：在多个噪声水平上匹配得分函数
3. **Langevin 采样训练**：训练一个类似 Langevin 动力学的采样器

---

## Part 9: VAE as Amortized Variational Inference — Detailed Analysis **[Kingma & Welling 2014]**

### 9.1 从传统 VI 到 VAE 的范式转变

传统 VI（如 CAVI）和 VAE 都在最大化 ELBO，但在推断策略上有根本不同：

| 维度 | 传统 Mean-field VI | SVI | **VAE (Amortized VI)** |
|---|---|---|---|
| 变分参数 | 每个数据点 $\phi_i$ | 全局 $\lambda$ + 局部 $\phi_i$ | **共享网络** $q_{\boldsymbol{\phi}}(\mathbf{z}\|\mathbf{x})$ |
| 新数据推断 | 重新优化 | 局部优化 | **一次前向传播** |
| 优化方法 | 坐标上升 | 随机自然梯度 | SGD + 重参数化 |
| 变分族 | 指数族 | 指数族 | **神经网络参数化** |
| 计算代价/数据点 | $O(\text{iterations})$ | $O(1)$ amortized | $O(1)$ |

### 9.2 VAE 的摊销推断机制 **[Kingma & Welling 2014, §1-2]**

**核心创新**：Kingma & Welling 提出用参数化的 recognition model（识别模型）$q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x})$ 替代 per-datapoint 的变分参数。

**具体地**，VAE 的编码器输出近似后验的参数：

$$q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}) = \mathcal{N}(\mathbf{z};\; \boldsymbol{\mu}_{\boldsymbol{\phi}}(\mathbf{x}),\; \boldsymbol{\sigma}_{\boldsymbol{\phi}}^2(\mathbf{x})\mathbf{I})$$

其中 $\boldsymbol{\mu}_{\boldsymbol{\phi}}(\mathbf{x})$ 和 $\log \boldsymbol{\sigma}_{\boldsymbol{\phi}}^2(\mathbf{x})$ 是编码器网络（MLP）的输出 **[Kingma & Welling 2014, §3]**。

**摊销的含义**：
- 训练时：$\boldsymbol{\phi}$ 在所有数据点上共享，通过 minibatch SGD 联合优化
- 推断时：新数据点 $\mathbf{x}_{\text{new}}$ 只需一次前向传播即得近似后验
- 代价：amortization gap —— 共享网络的表达力可能不如逐点优化精确

### 9.3 编码器-解码器架构的 VI 解释 **[Kingma & Welling 2014, §2.1, §3]**

从编码理论视角（coding theory perspective），Kingma & Welling 将 VAE 框架解释为：

- **编码器**（概率性）：$q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x})$ — 给定数据 $\mathbf{x}$，产生编码 $\mathbf{z}$ 的分布
- **解码器**（概率性）：$p_{\boldsymbol{\theta}}(\mathbf{x}|\mathbf{z})$ — 给定编码 $\mathbf{z}$，产生数据 $\mathbf{x}$ 的分布
- **ELBO**：自编码器损失的概率论版本 —— 重构项 + 正则化项

**与确定性自编码器的联系**：
- 确定性 AE 的重构损失 $\|x - \hat{x}\|^2$ 对应高斯解码器的期望对数似然
- VAE 的 KL 正则项替代了传统 AE 中的启发式正则（如去噪、稀疏、收缩）
- KL 项由变分界自然产生，不需要超参数调节 **[Kingma & Welling 2014, §2.3]**

### 9.4 SGVB + AEVB 与传统 VI 的统一 **[Kingma & Welling 2014, §2.3]**

SGVB（随机梯度变分贝叶斯）是一种通用的 ELBO 梯度估计方法，AEVB 是将其与摊销推断结合的完整算法：

$$\nabla_{\boldsymbol{\theta}, \boldsymbol{\phi}} \mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{X}) \simeq \nabla_{\boldsymbol{\theta}, \boldsymbol{\phi}} \left[\frac{N}{M}\sum_{i=1}^M \widetilde{\mathcal{L}}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}^{(i)}, \boldsymbol{\epsilon}^{(i)})\right]$$

**统一视角**：

| VI 发展阶段 | 估计器 | 关键技术 |
|---|---|---|
| Classical VI (CAVI) | 精确坐标更新 | 共轭指数族 |
| Black-box VI | REINFORCE 梯度 | 控制变量降方差 |
| **SGVB/AEVB** | **重参数化梯度** | **$\mathbf{z} = g_\phi(\boldsymbol{\epsilon}, \mathbf{x})$** |
| Normalizing Flows | 可逆变换 | 对数行列式 Jacobian |

### 9.5 Full VB 扩展 **[Kingma & Welling 2014, Appendix C]**

Kingma & Welling 还展示了 SGVB 可用于参数 $\boldsymbol{\theta}$ 上的完全贝叶斯推断（不仅限于隐变量 $\mathbf{z}$）：

$$\log p_{\boldsymbol{\alpha}}(\mathbf{X}) = D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\boldsymbol{\theta}) \| p_{\boldsymbol{\alpha}}(\boldsymbol{\theta}|\mathbf{X})) + \mathcal{L}(\boldsymbol{\phi}; \mathbf{X})$$

其中 $\boldsymbol{\alpha}$ 是超先验参数。对 $\boldsymbol{\theta}$ 同样使用重参数化：$\tilde{\boldsymbol{\theta}} = h_{\boldsymbol{\phi}}(\boldsymbol{\zeta})$，$\boldsymbol{\zeta} \sim p(\boldsymbol{\zeta})$。

这展示了 SGVB 作为通用变分推断工具的灵活性，不局限于特定的模型结构。

---

## References

1. Blei, D.M., Kucukelbir, A., & McAuliffe, J.D. (2017). Variational Inference: A Review for Statisticians. JASA.
2. Jordan, M.I., Ghahramani, Z., Jaakkola, T.S., & Saul, L.K. (1999). An Introduction to Variational Methods for Graphical Models. Machine Learning.
3. Hoffman, M.D., Blei, D.M., Wang, C., & Paisley, J. (2013). Stochastic Variational Inference. JMLR.
4. Kingma, D.P. & Welling, M. (2014). Auto-Encoding Variational Bayes. ICLR.
5. Rezende, D.J. & Mohamed, S. (2015). Variational Inference with Normalizing Flows. ICML.
6. Zhang, C., Butepage, J., Kjellstrom, H., & Mandt, S. (2019). Advances in Variational Inference. IEEE TPAMI.
7. Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. NeurIPS.
