# 11. ML Theory: Key Formulas

> 聚焦扩散模型（Diffusion Models）和图神经网络（GNN）的核心数学公式。
> 所有公式使用 LaTeX 记法，解释用中文。

---

### F11.1: ELBO (Evidence Lower BOund)

$$\log p(x) \geq \mathbb{E}_{q(z|x)}\left[\log p(x|z)\right] - D_{\mathrm{KL}}\left(q(z|x) \| p(z)\right) = \mathcal{L}_{\mathrm{ELBO}}$$

对数边际似然的下界：重构项鼓励模型准确重建数据，KL项约束后验逼近先验。变分推断和VAE的理论基石。

**Source**: [derivations/elbo_derivation.md] | Kingma & Welling, 2014; Blei et al., 2017

---

### F11.2: Forward Diffusion Process $q(x_t | x_0)$

$$q(x_t | x_0) = \mathcal{N}\left(x_t; \sqrt{\bar{\alpha}_t}\, x_0,\; (1 - \bar{\alpha}_t)\, \mathbf{I}\right)$$

其中 $\bar{\alpha}_t = \prod_{s=1}^{t} \alpha_s = \prod_{s=1}^{t}(1 - \beta_s)$。前向过程的闭式解：可以从 $x_0$ 一步跳到任意时刻 $x_t$，无需逐步加噪。

**Source**: [derivations/diffusion_models_math.md] | Ho et al., DDPM, NeurIPS 2020

---

### F11.3: Reverse Process $p_\theta(x_{t-1} | x_t)$

$$p_\theta(x_{t-1} | x_t) = \mathcal{N}\left(x_{t-1};\; \mu_\theta(x_t, t),\; \sigma_t^2 \mathbf{I}\right)$$

$$\mu_\theta(x_t, t) = \frac{1}{\sqrt{\alpha_t}}\left(x_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}}\, \epsilon_\theta(x_t, t)\right)$$

反向去噪过程：神经网络 $\epsilon_\theta$ 预测噪声，通过学到的均值逐步还原干净数据。

**Source**: [derivations/diffusion_models_math.md] | Ho et al., DDPM, NeurIPS 2020

---

### F11.4: DDPM Training Loss (Simplified)

$$\mathcal{L}_{\text{simple}} = \mathbb{E}_{t, x_0, \epsilon}\left[\left\| \epsilon - \epsilon_\theta\left(\sqrt{\bar{\alpha}_t}\, x_0 + \sqrt{1 - \bar{\alpha}_t}\, \epsilon,\; t\right)\right\|^2\right]$$

其中 $\epsilon \sim \mathcal{N}(0, \mathbf{I})$，$t \sim \mathrm{Uniform}\{1, \ldots, T\}$。简化训练目标：让网络学会预测加入的噪声，等价于加权变分下界。

**Source**: [derivations/diffusion_models_math.md] | Ho et al., DDPM, NeurIPS 2020

---

### F11.5: Score Function

$$s(x) = \nabla_x \log p(x)$$

Score function（得分函数）是对数概率密度的梯度，指向概率密度增大最快的方向。无需知道归一化常数即可定义。

**Source**: [derivations/score_matching.md] | Hyvarinen, 2005; Song & Ermon, 2019

---

### F11.6: Denoising Score Matching Objective

$$\mathcal{L}_{\mathrm{DSM}} = \mathbb{E}_{t}\left[\lambda(t)\, \mathbb{E}_{x_0}\, \mathbb{E}_{x_t | x_0}\left[\left\| s_\theta(x_t, t) - \nabla_{x_t} \log q(x_t | x_0)\right\|^2\right]\right]$$

去噪得分匹配：用已知的条件得分 $\nabla_{x_t} \log q(x_t|x_0)$ 作为目标来训练得分网络，避免计算真实数据分布的得分。

**Source**: [derivations/score_matching.md] | Vincent, 2011; Song & Ermon, NeurIPS 2019

---

### F11.7: Langevin Dynamics Sampling

$$x_{k+1} = x_k + \frac{\eta}{2}\, \nabla_x \log p(x_k) + \sqrt{\eta}\, z_k, \quad z_k \sim \mathcal{N}(0, \mathbf{I})$$

Langevin 动力学采样：梯度项将样本推向高概率区域，噪声项保证遍历性。当 $\eta \to 0, K \to \infty$ 时收敛到目标分布。

**Source**: [derivations/langevin_dynamics.md] | Roberts & Tweedie, 1996; Song & Ermon, 2019

---

### F11.8: SDE Formulation (Forward & Reverse)

**Forward SDE:**

$$dx = f(x, t)\, dt + g(t)\, dw$$

**Reverse SDE (Anderson, 1982):**

$$dx = \left[f(x, t) - g(t)^2\, \nabla_x \log p_t(x)\right] dt + g(t)\, d\bar{w}$$

前向SDE逐步加噪，反向SDE通过得分函数逆转噪声过程。统一了DDPM、SMLD等不同扩散模型。

**Source**: [derivations/diffusion_models_math.md] | Song et al., Score-Based SDE, ICLR 2021

---

### F11.9: Probability Flow ODE

$$dx = \left[f(x, t) - \frac{1}{2}\, g(t)^2\, \nabla_x \log p_t(x)\right] dt$$

概率流ODE：与反向SDE具有相同的边际分布，但是确定性轨迹。可用于精确的对数似然计算和更快的采样。

**Source**: [derivations/diffusion_models_math.md] | Song et al., Score-Based SDE, ICLR 2021

---

### F11.10: GNN Message Passing Framework

$$m_v^{(l+1)} = \bigoplus_{u \in \mathcal{N}(v)} M^{(l)}\left(h_v^{(l)}, h_u^{(l)}, e_{uv}\right)$$

$$h_v^{(l+1)} = U^{(l)}\left(h_v^{(l)}, m_v^{(l+1)}\right)$$

消息传递框架：每个节点从邻居收集消息（$M$: 消息函数，$\bigoplus$: 聚合算子），然后更新自身表示。GCN、GAT、GraphSAGE都是该框架的特例。

**Source**: [derivations/gnn_message_passing.md] | Gilmer et al., MPNN, ICML 2017

---

### F11.11: Graph Attention Mechanism

$$\alpha_{ij} = \frac{\exp\left(\mathrm{LeakyReLU}\left(a^T [W h_i \| W h_j]\right)\right)}{\sum_{k \in \mathcal{N}(i)} \exp\left(\mathrm{LeakyReLU}\left(a^T [W h_i \| W h_k]\right)\right)}$$

$$h_i' = \sigma\left(\sum_{j \in \mathcal{N}(i)} \alpha_{ij}\, W h_j\right)$$

图注意力机制：通过可学习的注意力系数 $\alpha_{ij}$ 加权邻居消息，使模型自适应地关注重要邻居。

**Source**: [derivations/gnn_message_passing.md] | Velickovic et al., GAT, ICLR 2018

---

### F11.12: KL Divergence

$$D_{\mathrm{KL}}(q \| p) = \mathbb{E}_{q(x)}\left[\log \frac{q(x)}{p(x)}\right] = \int q(x) \log \frac{q(x)}{p(x)}\, dx$$

**Gaussian 特例:**

$$D_{\mathrm{KL}}\left(\mathcal{N}(\mu_1, \sigma_1^2) \| \mathcal{N}(\mu_2, \sigma_2^2)\right) = \log\frac{\sigma_2}{\sigma_1} + \frac{\sigma_1^2 + (\mu_1 - \mu_2)^2}{2\sigma_2^2} - \frac{1}{2}$$

KL散度衡量两个分布之间的差异，非对称，非负（Gibbs不等式）。在ELBO和扩散模型损失中核心出现。

**Source**: [derivations/elbo_derivation.md] | Kullback & Leibler, 1951

---

### F11.13: Reparameterization Trick

$$z = \mu + \sigma \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, \mathbf{I})$$

重参数化技巧：将随机采样 $z \sim q_\phi(z|x)$ 转化为确定性变换加外部噪声，使梯度可以通过采样操作反向传播。VAE和扩散模型训练的关键。

**Source**: [derivations/elbo_derivation.md] | Kingma & Welling, VAE, ICLR 2014

---

### F11.14: Noise Schedule $\beta_t$

**Linear schedule:**

$$\beta_t = \beta_1 + \frac{t-1}{T-1}(\beta_T - \beta_1), \quad \beta_1 = 10^{-4},\; \beta_T = 0.02$$

**Cosine schedule:**

$$\bar{\alpha}_t = \frac{f(t)}{f(0)}, \quad f(t) = \cos^2\left(\frac{t/T + s}{1 + s} \cdot \frac{\pi}{2}\right)$$

噪声调度控制前向过程的加噪速率。线性调度简单但末端信噪比下降过快；余弦调度更均匀，适用于图像等高维数据。

**Source**: [derivations/diffusion_models_math.md] | Ho et al., 2020; Nichol & Dhariwal, 2021

---

### F11.15: Classifier-Free Guidance

$$\tilde{\epsilon}_\theta(x_t, t, c) = (1 + w)\, \epsilon_\theta(x_t, t, c) - w\, \epsilon_\theta(x_t, t, \varnothing)$$

等价的score形式：

$$\tilde{s}_\theta(x_t, t, c) = s_\theta(x_t, t, c) + w\left[s_\theta(x_t, t, c) - s_\theta(x_t, t, \varnothing)\right]$$

无分类器引导：通过放大条件预测与无条件预测之间的差异来增强生成质量。$w > 0$ 时牺牲多样性换取与条件更强的一致性。

**Source**: [derivations/diffusion_models_math.md] | Ho & Salimans, 2022

---

### F11.16: D3PM Forward Process (Discrete Diffusion)

$$q(x_t | x_{t-1}) = \mathrm{Cat}(x_t;\; p = \mathbf{x}_{t-1} Q_t), \quad q(x_t | x_0) = \mathrm{Cat}(x_t;\; p = \mathbf{x}_0 \bar{Q}_t)$$

其中 $\bar{Q}_t = Q_1 Q_2 \cdots Q_t$ 是累积转移矩阵。离散扩散的前向过程：通过转移矩阵在有限状态空间上加噪，类比连续DDPM的高斯加噪。

**Source**: [derivations/discrete_diffusion_d3pm.md] | Austin et al., D3PM, NeurIPS 2021

---

### F11.17: D3PM Posterior

$$q(x_{t-1} | x_t, x_0) \propto \mathbf{x}_0 \bar{Q}_{t-1} \odot \mathbf{x}_t Q_t^\top$$

离散扩散的后验分布：由贝叶斯定理得到，是两个概率向量的逐元素乘积再归一化。类比连续DDPM的高斯后验。

**Source**: [derivations/discrete_diffusion_d3pm.md] | Austin et al., D3PM, NeurIPS 2021

---

### F11.18: Concrete Score (Discrete Score Function)

$$s_\theta(x_t)_y = \log p_\theta(x_0 = y \,|\, x_t)$$

Concrete score 是离散空间的得分函数类比：对每个可能的"干净值" $y$ 给出条件对数概率。网络的logit输出就是concrete score。

**Source**: [derivations/discrete_score_matching.md] | Meng et al., NeurIPS 2022

---

### F11.19: CTMC Reverse Rate (Continuous-Time Discrete Diffusion)

$$\overleftarrow{R}_t(x_t, y) = R_t(y, x_t) \frac{p_t(y)}{p_t(x_t)}$$

连续时间马尔可夫链的反向速率矩阵：离散版本的Anderson反向SDE。概率比率 $p_t(y)/p_t(x_t)$ 对应离散得分。

**Source**: [derivations/discrete_score_matching.md] | Campbell et al., NeurIPS 2022

---

---

### F11.20: VLB Weighted Loss Term **[Ho et al. 2020, Eq.(12)]**

$$L_{t-1} = \frac{\beta_t^2}{2\sigma_t^2\alpha_t(1-\bar{\alpha}_t)}\mathbb{E}_{\mathbf{x}_0, \boldsymbol{\epsilon}}\left[\|\boldsymbol{\epsilon} - \boldsymbol{\epsilon}_\theta(\sqrt{\bar{\alpha}_t}\mathbf{x}_0 + \sqrt{1-\bar{\alpha}_t}\boldsymbol{\epsilon}, t)\|^2\right]$$

VLB中每一项的精确形式（含权重因子）。$L_{\text{simple}}$ 将权重统一为1，下调小 $t$ 的损失，实验效果更好（FID 3.17 vs 13.51）。

**Source**: [derivations/diffusion_models_math.md] | Ho et al., DDPM, NeurIPS 2020, Eq.(12)

---

### F11.21: VE-SDE (Variance Exploding) **[Song et al. 2021, Eq.(6)]**

$$d\mathbf{x} = \sqrt{\frac{d[\sigma^2(t)]}{dt}}\,d\mathbf{w}$$

**具体实例化**（几何序列 $\sigma_i$）：$d\mathbf{x} = \sigma_{\min}(\sigma_{\max}/\sigma_{\min})^t\sqrt{2\log(\sigma_{\max}/\sigma_{\min})}\,d\mathbf{w}$

SMLD 的连续时间极限，方差随时间指数增长。

**Source**: [derivations/diffusion_models_math.md] | Song et al., Score SDE, ICLR 2021

---

### F11.22: sub-VP-SDE **[Song et al. 2021, Appendix B, Eq.(31)]**

$$d\mathbf{x} = -\frac{1}{2}\beta(t)\mathbf{x}\,dt + \sqrt{\beta(t)(1-e^{-2\int_0^t\beta(s)ds})}\,d\mathbf{w}$$

sub-VP-SDE 的方差始终被 VP-SDE 上界：$\boldsymbol{\sigma}_{\text{sub-VP}}(t) \preccurlyeq \boldsymbol{\sigma}_{\text{VP}}(t)$。在似然值上通常优于 VP-SDE（CIFAR10: 2.99 bits/dim）。

**Source**: [derivations/diffusion_models_math.md] | Song et al., Score SDE, ICLR 2021

---

### F11.23: Exact Log-Likelihood via Probability Flow ODE **[Song et al. 2021, Appendix C.2]**

$$\log p_0(\mathbf{x}(0)) = \log p_T(\mathbf{x}(T)) + \int_0^T \nabla\cdot\tilde{\mathbf{f}}_\theta(\mathbf{x}(t), t)\,dt$$

利用概率流 ODE 与 neural ODE 的联系，通过瞬时变量替换公式计算精确对数似然。散度项用 Hutchinson 迹估计器高效近似。

**Source**: [derivations/diffusion_models_math.md] | Song et al., Score SDE, ICLR 2021

---

### F11.24: Continuous-Time ELBO for Discrete Diffusion **[Campbell et al. 2022, Proposition 2]**

$$\mathcal{L}_{\text{CT}}(\theta) = T\,\mathbb{E}_{t,q_t(x),r_t(\tilde{x}|x)}\left[\sum_{x' \neq x}\hat{R}_t^\theta(x,x') - \mathcal{Z}^t(x)\log\hat{R}_t^\theta(\tilde{x},x)\right] + C$$

连续时间离散扩散模型的 ELBO，可通过随机梯度下降高效优化。

**Source**: [derivations/discrete_score_matching.md] | Campbell et al., NeurIPS 2022

---

### F11.25: Tau-Leaping Error Bound **[Campbell et al. 2022, Theorem 1]**

$$\|\mathcal{L}(y_0) - p_{\text{data}}\|_{\text{TV}} \leq 3MT + \{(|R|SDC_1)^2 + \tfrac{1}{2}C_2(M+C_1SD|R|)\}\tau T + 2\exp\left\{-\frac{T\log^2 2}{t_{\text{mix}}\log 4D}\right\}$$

Tau-leaping 采样的全变差误差界：反向速率近似误差 + 离散化误差 + 混合误差。误差对维度 $D$ 至多二次增长。

**Source**: [derivations/discrete_diffusion_d3pm.md] | Campbell et al., NeurIPS 2022

---

### F11.26: D3PM Auxiliary Loss **[Austin et al. 2021, Eq.(6)]**

$$L_\lambda = L_{\text{vb}} + \lambda\,\mathbb{E}_{q(\mathbf{x}_0)}\mathbb{E}_{q(\mathbf{x}_t|\mathbf{x}_0)}[-\log\tilde{p}_\theta(\mathbf{x}_0|\mathbf{x}_t)]$$

D3PM 的混合训练目标：VLB + 交叉熵辅助损失。Austin et al. 使用 $\lambda = 0.001$。

**Source**: [derivations/discrete_diffusion_d3pm.md] | Austin et al., D3PM, NeurIPS 2021

---

### F11.27: Anderson Reverse SDE (General Form) **[Song et al. 2021, Theorem 1]**

$$d\mathbf{x} = \left\{\mathbf{f}(\mathbf{x},t) - \nabla\cdot[\mathbf{G}\mathbf{G}^\top] - \mathbf{G}\mathbf{G}^\top\nabla_\mathbf{x}\log p_t(\mathbf{x})\right\}dt + \mathbf{G}(\mathbf{x},t)d\bar{\mathbf{w}}$$

一般矩阵值扩散系数的反向 SDE，包含散度修正项 $\nabla\cdot[\mathbf{G}\mathbf{G}^\top]$。标量扩散系数时退化为简化形式。

**Source**: [derivations/diffusion_models_math.md] | Song et al., Score SDE, ICLR 2021

---

### F11.28: GCN Layer-wise Propagation Rule **[Kipf & Welling 2017, Eq.(2)]**

$$H^{(l+1)} = \sigma\!\left(\tilde{D}^{-\frac{1}{2}}\tilde{A}\tilde{D}^{-\frac{1}{2}} H^{(l)} W^{(l)}\right)$$

其中 $\tilde{A} = A + I_N$（加自环），$\tilde{D}_{ii} = \sum_j \tilde{A}_{ij}$。由谱图卷积的一阶切比雪夫近似 + renormalization trick 推导而来。计算复杂度 $O(|\mathcal{E}|FC)$，线性于边数。

**Source**: [derivations/gnn_message_passing.md] | Kipf & Welling, GCN, ICLR 2017, Eq.(2)

---

### F11.29: GCN Spectral Derivation Chain **[Kipf & Welling 2017, Eq.(3)→(7)]**

$$g_\theta \star x = Ug_\theta U^\top x \;\xrightarrow{K\text{-Cheb}}\; \sum_{k=0}^K \theta_k' T_k(\tilde{L})x \;\xrightarrow{K=1}\; \theta_0' x - \theta_1' D^{-1/2}AD^{-1/2}x \;\xrightarrow{\text{renorm}}\; \tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}X\Theta$$

从谱图卷积到 GCN 的完整推导链：图傅里叶变换 → 切比雪夫多项式近似 → 一阶近似（$K=1$, $\lambda_{\max} \approx 2$）→ 单参数约束（$\theta_0' = -\theta_1'$）→ Renormalization trick。

**Source**: [derivations/gnn_message_passing.md] | Kipf & Welling, GCN, ICLR 2017

---

### F11.30: GAT Attention Coefficient **[Veličković et al. 2018, Eq.(3)]**

$$\alpha_{ij} = \frac{\exp\!\left(\mathrm{LeakyReLU}\!\left(\vec{\mathbf{a}}^T[W\vec{h}_i \| W\vec{h}_j]\right)\right)}{\sum_{k \in \mathcal{N}_i} \exp\!\left(\mathrm{LeakyReLU}\!\left(\vec{\mathbf{a}}^T[W\vec{h}_i \| W\vec{h}_k]\right)\right)}$$

$$\vec{h}_i' = \sigma\!\left(\sum_{j \in \mathcal{N}_i} \alpha_{ij} W\vec{h}_j\right)$$

图注意力机制的完整形式：$W \in \mathbb{R}^{F' \times F}$ 共享线性变换，$\vec{\mathbf{a}} \in \mathbb{R}^{2F'}$ 注意力向量，$\|$ 拼接。Multi-head 版本拼接 $K$ 个头（中间层）或取均值（最后层）。

**Source**: [derivations/gnn_message_passing.md] | Veličković et al., GAT, ICLR 2018, Eq.(3)-(4)

---

### F11.31: GIN Update Rule **[Xu et al. 2019, Eq.(4.1)]**

$$h_v^{(k)} = \mathrm{MLP}^{(k)}\!\left((1 + \epsilon^{(k)}) \cdot h_v^{(k-1)} + \sum_{u \in \mathcal{N}(v)} h_u^{(k-1)}\right)$$

Graph Isomorphism Network 的节点更新规则。Sum 聚合保证 multiset 单射性（Lemma 5），MLP 为通用近似器（保证更新单射性），$(1+\epsilon)$ 分离中心节点与邻居。GIN 可证明与 1-WL test 同等强大。

**Source**: [derivations/gnn_message_passing.md], [07_graph_theory/derivations/wl_test_expressiveness.md] | Xu et al., GIN, ICLR 2019, Eq.(4.1)

---

### F11.32: GNN $\leq$ WL Upper Bound **[Xu et al. 2019, Lemma 2]**

$$\text{If } \mathcal{A}(G_1) \neq \mathcal{A}(G_2), \text{ then WL test decides } G_1 \not\cong G_2$$

任何基于邻域聚合的 GNN $\mathcal{A}$ 的区分能力至多等于 1-WL test。若 WL 无法区分两图，则任何 GNN 也无法区分。GIN（sum + MLP）紧达此上界（Theorem 3）。

**Source**: [07_graph_theory/derivations/wl_test_expressiveness.md] | Xu et al., GIN, ICLR 2019, Lemma 2 & Theorem 3

---

### F11.33: Sum Aggregation Injectivity on Multisets **[Xu et al. 2019, Lemma 5]**

$$\exists f: \mathcal{X} \to \mathbb{R}^n \text{ s.t. } h(X) = \sum_{x \in X} f(x) \text{ is injective on bounded-size multisets}$$

且任何 multiset 函数可分解为 $g(X) = \phi(\sum_{x \in X} f(x))$。构造性证明：取 $f(x) = N^{-Z(x)}$（$N$-进制编码）。这是 GIN 使用 sum 而非 mean/max 的理论基础。

**Source**: [07_graph_theory/derivations/wl_test_expressiveness.md] | Xu et al., GIN, ICLR 2019, Lemma 5

---

### F11.34: DDIM Update Rule **[Song et al. DDIM 2021, Eq.(12)]**

$$x_{t-1} = \sqrt{\alpha_{t-1}}\left(\frac{x_t - \sqrt{1-\alpha_t}\,\epsilon_\theta^{(t)}(x_t)}{\sqrt{\alpha_t}}\right) + \sqrt{1-\alpha_{t-1}-\sigma_t^2}\cdot\epsilon_\theta^{(t)}(x_t) + \sigma_t\,\epsilon_t$$

非马尔可夫推断过程的通用采样公式。三项分别为：predicted $x_0$ 的缩放、指向 $x_t$ 的方向项、随机噪声。$\sigma_t=0$ 时为确定性 DDIM，$\sigma_t = \sqrt{(1-\alpha_{t-1})/(1-\alpha_t)}\sqrt{1-\alpha_t/\alpha_{t-1}}$ 时退化为 DDPM。

**Source**: [derivations/diffusion_models_math.md] | Song et al., DDIM, ICLR 2021, Eq.(12)

---

### F11.35: DDIM as Neural ODE **[Song et al. DDIM 2021, Eq.(14)]**

$$d\bar{x}(t) = \epsilon_\theta^{(t)}\!\left(\frac{\bar{x}(t)}{\sqrt{\sigma^2+1}}\right) d\sigma(t), \quad \bar{x} = x/\sqrt{\alpha},\; \sigma = \sqrt{(1-\alpha)/\alpha}$$

DDIM 确定性采样的连续极限 ODE。等价于 VE-SDE 的概率流 ODE（Proposition 1），支持确定性编码-解码和隐空间插值。

**Source**: [derivations/diffusion_models_math.md] | Song et al., DDIM, ICLR 2021, Eq.(14)

---

### F11.36: Flow Matching Objective **[Lipman et al. 2023, Eq.(4)]**

$$\mathcal{L}_{\mathrm{FM}}(\theta) = \mathbb{E}_{t \sim \mathcal{U}[0,1],\, x \sim p_t(x)} \|v_t(x;\theta) - u_t(x)\|^2$$

流匹配目标：回归生成目标概率路径 $p_t$ 的向量场 $u_t$。本身不可行（$u_t$ 不可解析），需要通过条件流匹配实现。

**Source**: [derivations/flow_matching.md] | Lipman et al., Flow Matching, ICLR 2023, Eq.(4)

---

### F11.37: Conditional Flow Matching **[Lipman et al. 2023, Theorem 2]**

$$\mathcal{L}_{\mathrm{CFM}}(\theta) = \mathbb{E}_{t,\, q(x_1),\, p_t(x|x_1)} \|v_t(x;\theta) - u_t(x|x_1)\|^2, \quad \nabla_\theta\mathcal{L}_{\mathrm{FM}} = \nabla_\theta\mathcal{L}_{\mathrm{CFM}}$$

条件流匹配与流匹配梯度相同（Theorem 2）。从条件路径 $p_t(x|x_1)$ 采样并回归条件向量场 $u_t(x|x_1)$，完全可行且无偏。

**Source**: [derivations/flow_matching.md] | Lipman et al., Flow Matching, ICLR 2023, Theorem 2

---

### F11.38: Gaussian Conditional Vector Field **[Lipman et al. 2023, Theorem 3]**

$$u_t(x|x_1) = \frac{\sigma_t'(x_1)}{\sigma_t(x_1)}(x - \mu_t(x_1)) + \mu_t'(x_1)$$

一般高斯条件路径 $p_t(x|x_1) = \mathcal{N}(\mu_t(x_1), \sigma_t(x_1)^2 I)$ 的唯一生成向量场。扩散路径（VP/VE）和 OT 路径都是 $\mu_t, \sigma_t$ 的不同选择。

**Source**: [derivations/flow_matching.md] | Lipman et al., Flow Matching, ICLR 2023, Theorem 3

---

### F11.39: OT Conditional Flow and CFM Loss **[Lipman et al. 2023, Eq.(12)-(14)]**

$$\psi_t(x) = (1-(1-\sigma_{\min})t)\,x + t\,x_1, \quad \mathcal{L}_{\mathrm{CFM}}^{\mathrm{OT}} = \mathbb{E}_{t,q(x_1),p(x_0)}\|v_t(\psi_t(x_0)) - (x_1-(1-\sigma_{\min})x_0)\|^2$$

最优传输条件流：线性插值 noise→data，产生直线轨迹和时间恒定方向的向量场。比扩散路径训练更快、采样更高效。

**Source**: [derivations/flow_matching.md] | Lipman et al., Flow Matching, ICLR 2023, Eq.(12)-(14)

---

### F11.40: DiGress Graph Forward Process **[Vignac et al. 2023, §3.1]**

$$q(G^t|G) = (\mathbf{X}\bar{\mathbf{Q}}^t_X,\; \mathbf{E}\bar{\mathbf{Q}}^t_E), \quad \bar{\mathbf{Q}}^t = \mathbf{Q}^1\cdots\mathbf{Q}^t$$

图上的离散扩散前向过程：对节点特征矩阵和边特征张量分别独立施加转移矩阵噪声。保持图的离散结构和稀疏性。

**Source**: [derivations/discrete_diffusion_d3pm.md] | Vignac et al., DiGress, ICLR 2023, §3.1

---

### F11.41: DiGress Marginal Transition Matrices **[Vignac et al. 2023, Theorem 4.1]**

$$\mathbf{Q}^t_X = \alpha^t\mathbf{I} + \beta^t\,\mathbf{1}_a\,\mathbf{m}_X^\top, \quad \mathbf{Q}^t_E = \alpha^t\mathbf{I} + \beta^t\,\mathbf{1}_b\,\mathbf{m}_E^\top$$

边际分布保持的转移矩阵：极限分布为训练数据的边际分布 $\mathbf{m}_X, \mathbf{m}_E$（而非均匀分布），是数据分布在因子化分布类上的 $L_2$ 最优投影。

**Source**: [derivations/discrete_diffusion_d3pm.md] | Vignac et al., DiGress, ICLR 2023, Theorem 4.1

---

### F11.42: DiGress ELBO **[Vignac et al. 2023, Appendix D]**

$$\log p_\theta(G) \geq \log p(n_G) + D_{\mathrm{KL}}[q(G^T|G) \| q_X \times q_E] + \sum_{t=2}^T \mathbb{E}_{q(G^t|G)}[D_{\mathrm{KL}}[q(G^{t-1}|G^t,G) \| p_\theta(G^{t-1}|G^t)]] + \mathbb{E}_{q(G^1|G)}[\log p_\theta(G|G^1)]$$

图生成的变分下界：先验损失（噪声分布匹配）+ 扩散损失（反向过程匹配）+ 重构损失。所有项都是范畴分布间的 KL 散度，可以精确计算。

**Source**: [derivations/discrete_diffusion_d3pm.md] | Vignac et al., DiGress, ICLR 2023, Appendix D

---

### F11.43: Scaled Dot-Product Attention **[Vaswani et al. 2017, §3.2.1]**

$$\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

缩放点积注意力。缩放因子 $\sqrt{d_k}$：若 $q, k$ 各分量独立均值0方差1，则 $\mathrm{Var}(q \cdot k) = d_k$，除以 $\sqrt{d_k}$ 归一化至方差1，防止 softmax 饱和。

**Source**: [derivations/attention_mechanism.md] | Vaswani et al., NeurIPS 2017

---

### F11.44: Multi-Head Attention **[Vaswani et al. 2017, §3.2.2]**

$$\mathrm{MultiHead}(Q, K, V) = \mathrm{Concat}(\mathrm{head}_1, \ldots, \mathrm{head}_h)W^O, \quad \mathrm{head}_i = \mathrm{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

$h$ 个并行注意力头投影到 $d_k = d_{\mathrm{model}}/h$ 维子空间。总计算量 $O(n^2 d)$ 与单头相当。

**Source**: [derivations/attention_mechanism.md] | Vaswani et al., NeurIPS 2017

---

### F11.45: Sinusoidal Positional Encoding **[Vaswani et al. 2017, §3.5]**

$$PE_{(pos, 2i)} = \sin(pos/10000^{2i/d}), \quad PE_{(pos, 2i+1)} = \cos(pos/10000^{2i/d})$$

波长几何级数 $2\pi$ 到 $10000 \cdot 2\pi$。$PE_{pos+k}$ 是 $PE_{pos}$ 的线性函数（三角恒等式），便于学习相对位置。

**Source**: [derivations/attention_mechanism.md] | Vaswani et al., NeurIPS 2017

---

### F11.46: Self-Attention = MPNN on Complete Graph

$$h_v' = \sum_{u} \mathrm{softmax}\left(\frac{(h_v W^Q)(h_u W^K)^\top}{\sqrt{d_k}}\right) \cdot h_u W^V$$

Transformer self-attention 等价于完全图 $K_n$ 上的消息传递。通过 mask（设非邻接 logit 为 $-\infty$）可适配稀疏图。

**Source**: [derivations/attention_mechanism.md] | [derivations/gnn_message_passing.md]

---

### F11.47: GAN Minimax Objective **[Goodfellow et al. 2014, Eq.(1)]**

$$\min_G \max_D \; V(D, G) = \mathbb{E}_{\mathbf{x} \sim p_{\text{data}}}[\log D(\mathbf{x})] + \mathbb{E}_{\mathbf{z} \sim p_{\mathbf{z}}}[\log(1 - D(G(\mathbf{z})))]$$

GAN 的核心目标函数：在最优解处 $p_g = p_{\text{data}}$，$D^*(\mathbf{x}) = 1/2$。训练准则等价于最小化 JSD。

**Source**: [derivations/generative_models_comparison.md] | Goodfellow et al., GAN, NeurIPS 2014

---

### F11.48: GAN Optimal Discriminator **[Goodfellow et al. 2014, Proposition 1]**

$$D^*_G(\mathbf{x}) = \frac{p_{\text{data}}(\mathbf{x})}{p_{\text{data}}(\mathbf{x}) + p_g(\mathbf{x})}$$

对固定 $G$，最优判别器是数据来源的贝叶斯后验。代入后 $C(G) = -\log 4 + 2\,\mathrm{JSD}(p_{\text{data}} \| p_g)$。

**Source**: [derivations/generative_models_comparison.md] | Goodfellow et al., GAN, NeurIPS 2014

---

### F11.49: REINFORCE Policy Gradient

$$\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}\left[\sum_{t=0}^{T}(G_t - b(s_t))\nabla_\theta \log \pi_\theta(a_t|s_t)\right]$$

策略梯度定理 + 基线减法。通过对数导数技巧将期望回报梯度转化为可采样形式。在组合优化中用于训练 attention model。

**Source**: [derivations/reinforcement_learning_basics.md] | Williams, 1992; Sutton et al., 2000

---

### F11.50: PPO Clipped Surrogate Objective **[Schulman et al. 2017, Eq.(7)]**

$$L^{\mathrm{CLIP}}(\theta) = \hat{\mathbb{E}}_t\left[\min\left(r_t(\theta)\hat{A}_t, \; \operatorname{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t\right)\right]$$

Clipping 限制概率比 $r_t = \pi_\theta/\pi_{\theta_{\text{old}}}$ 在 $[1-\epsilon, 1+\epsilon]$ 内，创建信赖域一阶近似。

**Source**: [derivations/reinforcement_learning_basics.md] | Schulman et al., PPO, 2017

---

### F11.51: Adam Update Rule **[Kingma & Ba 2015, Algorithm 1]**

$$\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1-\beta_2^t}, \quad \theta_t = \theta_{t-1} - \alpha\frac{\hat{m}_t}{\sqrt{\hat{v}_t}+\epsilon}$$

Adam：动量 + 自适应学习率 + 偏差修正。默认 $\beta_1=0.9$, $\beta_2=0.999$, $\epsilon=10^{-8}$。

**Source**: [derivations/optimization_algorithms.md] | Kingma & Ba, Adam, ICLR 2015

---

### F11.52: Gaussian VAE Complete Estimator **[Kingma & Welling 2014, §3]**

$$\mathcal{L} \simeq \frac{1}{2}\sum_{j=1}^J\left(1+\log(\sigma_j^{(i)})^2 - (\mu_j^{(i)})^2 - (\sigma_j^{(i)})^2\right) + \frac{1}{L}\sum_{l=1}^L \log p_\theta(\mathbf{x}^{(i)}|\mathbf{z}^{(i,l)})$$

高斯 VAE 的完整训练目标：闭式 KL + MC 重构项。$\mathbf{z}^{(i,l)} = \boldsymbol{\mu}^{(i)} + \boldsymbol{\sigma}^{(i)} \odot \boldsymbol{\epsilon}^{(l)}$。

**Source**: [derivations/elbo_derivation.md] | Kingma & Welling, VAE, ICLR 2014

---

### F11.53: Gradient Norm Clipping

$$\tilde{g} = g \cdot \min\left(1, \frac{c}{\|g\|}\right)$$

梯度范数裁剪：保持方向不变，仅缩放范数。在 Transformer/RNN 训练中防止梯度爆炸。典型阈值 $c = 1.0$。

**Source**: [derivations/optimization_algorithms.md] | Pascanu et al., 2013

---

### F11.54: GAE (Generalized Advantage Estimation)

$$\hat{A}_t^{\mathrm{GAE}(\gamma,\lambda)} = \sum_{l=0}^{\infty}(\gamma\lambda)^l \delta_{t+l}^V, \quad \delta_t^V = r_t + \gamma V(s_{t+1}) - V(s_t)$$

$\lambda$ 在偏差（$\lambda=0$, TD 误差）与方差（$\lambda=1$, MC 回报）之间平衡。PPO 中标配。

**Source**: [derivations/reinforcement_learning_basics.md] | Schulman et al., 2016

---

## Quick Reference Table

| ID | Formula | 核心用途 |
|---|---|---|
| F11.1 | ELBO | 变分推断目标函数 |
| F11.2 | $q(x_t\|x_0)$ | 前向加噪闭式解 |
| F11.3 | $p_\theta(x_{t-1}\|x_t)$ | 反向去噪过程 |
| F11.4 | $\mathcal{L}_{\text{simple}}$ | DDPM训练损失 |
| F11.5 | $\nabla_x \log p(x)$ | Score function |
| F11.6 | DSM objective | 去噪得分匹配 |
| F11.7 | Langevin dynamics | 基于score的采样 |
| F11.8 | Forward/Reverse SDE | 连续时间扩散 |
| F11.9 | Probability flow ODE | 确定性采样 |
| F11.10 | MPNN | GNN消息传递 |
| F11.11 | GAT attention | 图注意力 |
| F11.12 | KL divergence | 分布距离度量 |
| F11.13 | Reparameterization | 可微分采样 |
| F11.14 | Noise schedule $\beta_t$ | 加噪速率控制 |
| F11.15 | Classifier-free guidance | 条件生成增强 |
| F11.16 | D3PM $q(x_t\|x_0) = \mathrm{Cat}(\mathbf{x}_0 \bar{Q}_t)$ | 离散扩散前向过程 |
| F11.17 | D3PM posterior $\propto \bar{Q}_{t-1} \odot Q_t^\top$ | 离散扩散后验 |
| F11.18 | Concrete score $\log p(x_0=y\|x_t)$ | 离散得分函数 |
| F11.19 | CTMC reverse rate | 连续时间离散扩散 |
| F11.20 | VLB weighted $L_{t-1}$ | 精确变分界每项 |
| F11.21 | VE-SDE | 方差爆炸SDE |
| F11.22 | sub-VP-SDE | 次方差保持SDE |
| F11.23 | Exact log-likelihood (ODE) | 精确似然计算 |
| F11.24 | CT-ELBO (discrete) | 连续时间离散ELBO |
| F11.25 | Tau-leaping error bound | 采样误差理论界 |
| F11.26 | D3PM auxiliary loss | 离散扩散混合损失 |
| F11.27 | Anderson reverse SDE (general) | 一般反向SDE |
| F11.28 | GCN propagation $\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}HW$ | GCN 层传播规则 |
| F11.29 | GCN spectral derivation chain | 谱卷积→GCN推导链 |
| F11.30 | GAT attention $\alpha_{ij}$ (LeakyReLU + softmax) | 图注意力系数 |
| F11.31 | GIN update: $\mathrm{MLP}((1+\epsilon)h_v + \sum h_u)$ | GIN 更新规则 |
| F11.32 | GNN $\leq$ WL upper bound | GNN表达力上界 |
| F11.33 | Sum aggregation injectivity on multisets | Sum聚合单射性 |
| F11.34 | DDIM update rule | 非马尔可夫确定性采样 |
| F11.35 | DDIM Neural ODE | DDIM连续极限ODE |
| F11.36 | FM objective $\mathbb{E}\|v_t - u_t\|^2$ | 流匹配目标 |
| F11.37 | CFM = FM gradients (Theorem 2) | 条件流匹配等价性 |
| F11.38 | Gaussian conditional VF $\frac{\sigma'}{\sigma}(x-\mu)+\mu'$ | 高斯路径向量场 |
| F11.39 | OT conditional flow $\psi_t = (1-t)x + tx_1$ | 最优传输直线路径 |
| F11.40 | DiGress graph forward $q(G^t\|G) = (\mathbf{X}\bar{Q}_X, \mathbf{E}\bar{Q}_E)$ | 图上离散扩散 |
| F11.41 | DiGress marginal transition $Q = \alpha I + \beta\mathbf{1}\mathbf{m}^\top$ | 边际分布保持噪声 |
| F11.42 | DiGress ELBO for graphs | 图生成似然界 |
| F11.43 | $\mathrm{softmax}(QK^\top/\sqrt{d_k})V$ | 缩放点积注意力 |
| F11.44 | $\mathrm{Concat}(\mathrm{head}_1,\ldots,\mathrm{head}_h)W^O$ | 多头注意力 |
| F11.45 | $\sin(pos/10000^{2i/d})$, $\cos(\cdots)$ | 正弦位置编码 |
| F11.46 | Self-Attn = MPNN on $K_n$ | Transformer-GNN统一 |
| F11.47 | GAN minimax $\min_G\max_D V(D,G)$ | GAN目标函数 |
| F11.48 | $D^*_G = p_{\text{data}}/(p_{\text{data}}+p_g)$ | GAN最优判别器 |
| F11.49 | REINFORCE $\nabla J = \mathbb{E}[(G_t-b)\nabla\log\pi]$ | 策略梯度 |
| F11.50 | PPO clipped surrogate | 近端策略优化 |
| F11.51 | Adam $\theta \leftarrow \theta - \alpha\hat{m}/(\sqrt{\hat{v}}+\epsilon)$ | 自适应优化器 |
| F11.52 | Gaussian VAE estimator (KL+recon) | VAE训练目标 |
| F11.53 | Gradient norm clipping $g\cdot\min(1, c/\|g\|)$ | 梯度裁剪 |
| F11.54 | GAE $\sum(\gamma\lambda)^l\delta_t$ | 广义优势估计 |
