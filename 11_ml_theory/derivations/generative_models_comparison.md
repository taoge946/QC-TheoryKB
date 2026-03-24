# Generative Models: Theoretical Comparison

> **Tags**: `vae`, `gan`, `diffusion`, `flow-matching`, `generative-models`, `comparison`

## Statement

系统比较四大深度生成模型范式（VAE、GAN、Diffusion、Flow Matching）的理论基础，包括目标函数、训练动力学、散度度量、失败模式及其数学联系。

## Prerequisites

- ELBO 推导（见 [elbo_derivation.md](elbo_derivation.md)）
- KL 散度及其性质
- Jensen-Shannon 散度
- 随机微分方程基础（见 [diffusion_models_math.md](diffusion_models_math.md)）
- ODE/连续归一化流基础

---

## Part 1: VAE — Variational Auto-Encoder **[Kingma & Welling 2014]**

### 1.1 目标函数：ELBO 最大化

$$\max_{\boldsymbol{\theta}, \boldsymbol{\phi}} \; \mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}) = \mathbb{E}_{q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x})}\left[\log p_{\boldsymbol{\theta}}(\mathbf{x}|\mathbf{z})\right] - D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}) \| p(\mathbf{z}))$$

**[Kingma & Welling 2014, Eq.(2)]**

### 1.2 散度度量

VAE 隐式最小化 $D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}) \| p_{\boldsymbol{\theta}}(\mathbf{z}|\mathbf{x}))$（forward KL），这是 **mode-covering** 行为：

- $q$ 倾向于覆盖 $p$ 的所有 modes
- 宁可在低密度区域有概率密度，也不漏掉 mode
- 导致生成样本偏模糊（blurriness）

### 1.3 关键定理：ELBO 与边际似然的关系

$$\log p_{\boldsymbol{\theta}}(\mathbf{x}) = \mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\phi}; \mathbf{x}) + D_{\mathrm{KL}}(q_{\boldsymbol{\phi}}(\mathbf{z}|\mathbf{x}) \| p_{\boldsymbol{\theta}}(\mathbf{z}|\mathbf{x}))$$

**[Kingma & Welling 2014, §2.2]**

Gap = $D_{\mathrm{KL}}(q \| p_{\text{true}}) \geq 0$，等号当且仅当 $q = p_{\text{true}}$。

### 1.4 重参数化技巧

$$\mathbf{z} = \boldsymbol{\mu}_{\boldsymbol{\phi}}(\mathbf{x}) + \boldsymbol{\sigma}_{\boldsymbol{\phi}}(\mathbf{x}) \odot \boldsymbol{\epsilon}, \quad \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$$

使得梯度可以通过采样操作反向传播 **[Kingma & Welling 2014, §2.4]**。

### 1.5 高斯 VAE 闭式 KL

$$-D_{\mathrm{KL}}(q \| p) = \frac{1}{2}\sum_{j=1}^J \left(1 + \log(\sigma_j^{(i)})^2 - (\mu_j^{(i)})^2 - (\sigma_j^{(i)})^2\right)$$

**[Kingma & Welling 2014, Appendix B]**

### 1.6 失败模式

- **后验坍缩（posterior collapse）**：编码器输出退化为先验 $q_\phi(z|x) \approx p(z)$，KL 项趋零但重构质量差
- **模糊生成**：mode-covering 导致的平均效应
- **amortization gap**：共享编码器的近似精度有限

---

## Part 2: GAN — Generative Adversarial Network **[Goodfellow et al. 2014]**

### 2.1 目标函数：Minimax Game

$$\min_G \max_D \; V(D, G) = \mathbb{E}_{\mathbf{x} \sim p_{\text{data}}(\mathbf{x})}[\log D(\mathbf{x})] + \mathbb{E}_{\mathbf{z} \sim p_{\mathbf{z}}(\mathbf{z})}[\log(1 - D(G(\mathbf{z})))]$$

**[Goodfellow et al. 2014, Eq.(1)]**

### 2.2 Proposition 1：最优判别器 **[Goodfellow et al. 2014, Proposition 1]**

**命题**：对于固定的生成器 $G$，最优判别器为：

$$D^*_G(\mathbf{x}) = \frac{p_{\text{data}}(\mathbf{x})}{p_{\text{data}}(\mathbf{x}) + p_g(\mathbf{x})}$$

**证明**：对 $D$ 的训练准则为最大化：

$$V(G, D) = \int_{\mathbf{x}} p_{\text{data}}(\mathbf{x}) \log D(\mathbf{x}) + p_g(\mathbf{x}) \log(1 - D(\mathbf{x}))\,dx$$

对于任意 $(a, b) \in \mathbb{R}^2 \setminus \{0,0\}$，函数 $y \mapsto a\log(y) + b\log(1-y)$ 在 $[0,1]$ 上的最大值点为 $y = \frac{a}{a+b}$。 $\blacksquare$

### 2.3 Theorem 1：全局最优性 **[Goodfellow et al. 2014, Theorem 1]**

**定理**：虚拟训练准则 $C(G) = \max_D V(G, D)$ 的全局最小值当且仅当 $p_g = p_{\text{data}}$ 时达到。此时 $C(G) = -\log 4$。

**证明**：将最优判别器代入 $C(G)$：

$$C(G) = \mathbb{E}_{\mathbf{x} \sim p_{\text{data}}}\left[\log \frac{p_{\text{data}}(\mathbf{x})}{p_{\text{data}}(\mathbf{x}) + p_g(\mathbf{x})}\right] + \mathbb{E}_{\mathbf{x} \sim p_g}\left[\log \frac{p_g(\mathbf{x})}{p_{\text{data}}(\mathbf{x}) + p_g(\mathbf{x})}\right]$$

当 $p_g = p_{\text{data}}$ 时，$D^*(\mathbf{x}) = \frac{1}{2}$，故 $C(G) = \log\frac{1}{2} + \log\frac{1}{2} = -\log 4$。

为证明这是全局最小值，从 $C(G)$ 中减去 $-\log 4$：

$$C(G) = -\log 4 + D_{\mathrm{KL}}\left(p_{\text{data}} \left\| \frac{p_{\text{data}} + p_g}{2}\right.\right) + D_{\mathrm{KL}}\left(p_g \left\| \frac{p_{\text{data}} + p_g}{2}\right.\right)$$

$$\boxed{C(G) = -\log 4 + 2 \cdot \mathrm{JSD}(p_{\text{data}} \| p_g)}$$

**[Goodfellow et al. 2014, Theorem 1]**

由于 $\mathrm{JSD} \geq 0$，等号当且仅当 $p_g = p_{\text{data}}$。 $\blacksquare$

### 2.4 Jensen-Shannon Divergence

$$\mathrm{JSD}(P \| Q) = \frac{1}{2}D_{\mathrm{KL}}\left(P \left\| \frac{P+Q}{2}\right.\right) + \frac{1}{2}D_{\mathrm{KL}}\left(Q \left\| \frac{P+Q}{2}\right.\right)$$

**性质**：
- 对称：$\mathrm{JSD}(P\|Q) = \mathrm{JSD}(Q\|P)$
- 有界：$0 \leq \mathrm{JSD}(P\|Q) \leq \log 2$
- $\sqrt{\mathrm{JSD}}$ 是一个度量（满足三角不等式）

### 2.5 Proposition 2：收敛性 **[Goodfellow et al. 2014, Proposition 2]**

**命题**：如果 $G$ 和 $D$ 有足够容量，在算法每步中判别器达到其给定 $G$ 的最优值，且 $p_g$ 被更新以改进 $\mathbb{E}_{\mathbf{x} \sim p_{\text{data}}}[\log D^*_G(\mathbf{x})] + \mathbb{E}_{\mathbf{x} \sim p_g}[\log(1 - D^*_G(\mathbf{x}))]$，则 $p_g$ 收敛到 $p_{\text{data}}$。

**证明要点**：$U(p_g, D) = V(G, D)$ 关于 $p_g$ 是凸函数。凸函数上确界的次导数包含最大值点处的导数。$\sup_D U(p_g, D)$ 关于 $p_g$ 凸且有唯一全局最优（Theorem 1），因此足够小的 $p_g$ 更新保证收敛。 **[Goodfellow et al. 2014, Proposition 2]** $\blacksquare$

### 2.6 实际训练：非饱和目标

原始目标 $\min_G \log(1 - D(G(\mathbf{z})))$ 在训练初期梯度饱和。实践中使用：

$$\max_G \; \mathbb{E}_{\mathbf{z}}[\log D(G(\mathbf{z}))]$$

与原始目标有相同的不动点，但提供更强的梯度 **[Goodfellow et al. 2014, §3]**。

### 2.7 散度度量

GAN 隐式最小化 Jensen-Shannon 散度，这是 **mode-seeking** 行为：

- $G$ 倾向于集中在 $p_{\text{data}}$ 的某些 modes
- 可能完全忽略其他 modes
- 导致 mode collapse

### 2.8 失败模式

- **Mode collapse**：生成器只学到数据分布的部分 modes
- **训练不稳定**：判别器过强导致梯度消失，过弱导致无效指导
- **无法评估似然**：没有显式的 $p_g(\mathbf{x})$，难以定量评估

---

## Part 3: Diffusion Models — VLB Framework **[Ho et al. 2020]**

### 3.1 目标函数：变分下界 (VLB) **[Ho et al. 2020, Eq.(5)]**

$$-\mathcal{L}_{\mathrm{VLB}} = \underbrace{D_{\mathrm{KL}}(q(\mathbf{x}_T|\mathbf{x}_0) \| p(\mathbf{x}_T))}_{L_T} + \sum_{t=2}^{T} \underbrace{D_{\mathrm{KL}}(q(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{x}_0) \| p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t))}_{L_{t-1}} - \underbrace{\log p_\theta(\mathbf{x}_0|\mathbf{x}_1)}_{-L_0}$$

详细推导见 [elbo_derivation.md](elbo_derivation.md) Part 6-7。

### 3.2 简化训练目标 **[Ho et al. 2020, Eq.(14)]**

$$\mathcal{L}_{\text{simple}} = \mathbb{E}_{t, \mathbf{x}_0, \boldsymbol{\epsilon}}\left[\|\boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta(\sqrt{\bar{\alpha}_t}\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\boldsymbol{\epsilon}, t)\|^2\right]$$

### 3.3 散度度量

- 每一项 $L_{t-1}$ 是两个高斯之间的 KL 散度（forward KL）
- 总体上是 **mode-covering**（与 VAE 类似），但多层隐变量大大缓解了模糊问题

### 3.4 与 Score Matching 的联系

$$\boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t) \approx -\sqrt{1-\bar{\alpha}_t}\, \nabla_{\mathbf{x}_t} \log q(\mathbf{x}_t)$$

**[Ho et al. 2020, §3.2]** 噪声预测等价于在多个噪声水平上的去噪得分匹配 **[Song et al. 2021, §2]**。

### 3.5 失败模式

- **采样速度慢**：需要 $T$ 步（通常 $T = 1000$）
- **训练代价高**：需要在所有时间步上训练
- **无法精确计算似然**（除非使用 ODE 形式）

---

## Part 4: Flow Matching — Continuous Normalizing Flows (CFM)

### 4.1 目标函数：条件流匹配

$$\mathcal{L}_{\mathrm{CFM}} = \mathbb{E}_{t \sim \mathcal{U}(0,1)}\, \mathbb{E}_{q(\mathbf{x}_1)}\, \mathbb{E}_{p_t(\mathbf{x}|\mathbf{x}_1)}\left[\|v_\theta(\mathbf{x}, t) - u_t(\mathbf{x}|\mathbf{x}_1)\|^2\right]$$

其中 $u_t(\mathbf{x}|\mathbf{x}_1)$ 是条件向量场，$v_\theta$ 是神经网络参数化的速度场。

### 4.2 最优传输 (OT) 路径

最简单的选择是线性插值路径（OT 路径）：

$$\mathbf{x}_t = (1-t)\mathbf{x}_0 + t\mathbf{x}_1, \quad \mathbf{x}_0 \sim \mathcal{N}(\mathbf{0}, \mathbf{I}), \; \mathbf{x}_1 \sim q(\mathbf{x}_1)$$

对应的条件向量场：

$$u_t(\mathbf{x}|\mathbf{x}_1) = \mathbf{x}_1 - \mathbf{x}_0$$

### 4.3 与扩散模型的联系

Flow Matching 可以复现扩散模型的特定参数化：

| 路径选择 | 对应的扩散模型 |
|---|---|
| 高斯条件路径（$\sigma_t$ = VP 噪声调度） | VP-SDE (DDPM) |
| 最优传输路径（线性） | Rectified Flow |

### 4.4 ODE 采样

$$\frac{d\mathbf{x}}{dt} = v_\theta(\mathbf{x}, t), \quad \mathbf{x}(0) \sim \mathcal{N}(\mathbf{0}, \mathbf{I}), \quad \mathbf{x}(1) \approx \text{sample}$$

ODE 求解器（Euler、RK45 等）可实现精确似然计算（通过瞬时变量替换公式）。

### 4.5 散度度量

- 直接回归目标向量场（$L_2$ 损失）
- 不显式最小化某种散度，但在最优解处等价于最小化 KL 散度
- 比扩散模型的路径更直，采样更快

---

## Part 5: Comprehensive Comparison

### 5.1 理论对比表

| 维度 | VAE | GAN | Diffusion | Flow Matching |
|---|---|---|---|---|
| **目标函数** | ELBO 最大化 | Minimax game | VLB / $\mathcal{L}_{\text{simple}}$ | CFM (向量场回归) |
| **散度** | $D_{\mathrm{KL}}(q\|p)$ (forward) | $\mathrm{JSD}(p_{\text{data}}\|p_g)$ | $\sum D_{\mathrm{KL}}(q_{t-1\|t,0} \| p_\theta)$ | $L_2$ loss on vector field |
| **KL 方向** | Mode-covering | Mode-seeking (JSD) | Mode-covering | N/A (回归) |
| **显式密度** | 有（ELBO 下界） | 无 | 有（VLB 或 ODE） | 有（ODE） |
| **训练稳定性** | 稳定 | 不稳定 | 稳定 | 稳定 |
| **样本质量** | 偏模糊 | 锐利 | 高质量 | 高质量 |
| **采样速度** | 快（一步） | 快（一步） | 慢（$T$ 步） | 中等（ODE 步） |
| **模型类型** | 编码器+解码器 | 生成器+判别器 | 去噪网络 | 速度场网络 |
| **隐变量** | 低维 $\mathbf{z}$ | 噪声 $\mathbf{z}$ | 同维 $\mathbf{x}_{1:T}$ | 无显式隐变量 |

### 5.2 散度关系

$$\text{TV}(P, Q) \leq \sqrt{\frac{1}{2} D_{\mathrm{KL}}(P\|Q)} \leq \sqrt{2 \cdot \mathrm{JSD}(P\|Q)} / \sqrt{\log 2}$$

Pinsker 不等式将 KL 与 Total Variation 联系起来。

### 5.3 Mode Covering vs Mode Seeking

**Forward KL** $D_{\mathrm{KL}}(q\|p)$（VAE 使用）：
- 当 $p(\mathbf{x}) > 0$ 时要求 $q(\mathbf{x}) > 0$（否则 KL 趋于 $\infty$）
- 结果：$q$ 覆盖 $p$ 的所有 modes，但可能在 modes 之间有不必要的密度
- 生成效果：样本偏模糊

**Reverse KL** $D_{\mathrm{KL}}(p\|q)$：
- 当 $q(\mathbf{x}) > 0$ 时要求 $p(\mathbf{x}) > 0$
- 结果：$q$ 集中在 $p$ 的少数 modes，但每个 mode 内精确
- 生成效果：样本锐利但多样性差

**JSD**（GAN 使用）：
- 对称，介于 forward KL 和 reverse KL 之间
- 兼具 mode-seeking 和 mode-covering 特性，但实际训练中常表现为 mode-seeking
- 生成效果：锐利但可能 mode collapse

### 5.4 统一视角：生成模型作为分布匹配

所有四种方法都在解决同一个问题：将模型分布 $p_\theta$ 匹配到数据分布 $p_{\text{data}}$。

$$\min_\theta \; d(p_{\text{data}}, p_\theta)$$

不同之处在于：
1. **散度 $d$ 的选择**：KL、JSD、Wasserstein、$L_2$ 等
2. **模型 $p_\theta$ 的参数化**：隐变量模型、隐式模型、马尔可夫链
3. **优化策略**：单目标优化 vs 对抗训练

---

## Summary

四种生成模型从不同角度逼近数据分布：

- **VAE**：通过 ELBO 最大化，以 forward KL 为桥梁，训练稳定但样本偏模糊
- **GAN**：通过对抗训练隐式最小化 JSD，样本锐利但训练不稳定且有 mode collapse
- **Diffusion**：通过多步 VLB，综合了 mode-covering 和高质量生成，但采样慢
- **Flow Matching**：通过向量场回归，结合了扩散模型的质量和更快的采样

---

## References

1. Kingma, D.P. & Welling, M. (2014). Auto-Encoding Variational Bayes. ICLR.
2. Goodfellow, I.J. et al. (2014). Generative Adversarial Nets. NeurIPS.
3. Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. NeurIPS.
4. Song, Y. et al. (2021). Score-Based Generative Modeling through SDEs. ICLR.
5. Lipman, Y. et al. (2023). Flow Matching for Generative Modeling. ICLR.
6. Tong, A. et al. (2024). Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal Transport. TMLR.
