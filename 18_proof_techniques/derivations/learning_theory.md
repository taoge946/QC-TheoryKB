# Learning Theory: PAC, VC Dimension, Rademacher, PAC-Bayes

> 机器学习泛化理论的核心推导——从 PAC 框架到现代神经网络泛化界。
> 写论文 theory/generalization section 时的必备参考。
> 特别关注 GNN 泛化和扩散模型泛化（与用户研究方向相关）。

---

## 1. PAC Framework (PAC 学习框架) [F18.10]

### 1.1 Definition

**Probably Approximately Correct (PAC)**: 假设类 $\mathcal{H}$ 是 PAC learnable 的，如果存在算法 $A$ 和多项式函数 $m(\epsilon, \delta)$，使得对任意分布 $\mathcal{D}$、任意 $\epsilon, \delta > 0$，当样本量 $n \geq m(\epsilon, \delta)$ 时：

$$P_{S \sim \mathcal{D}^n}\left(R(A(S)) - \min_{h \in \mathcal{H}} R(h) \leq \epsilon\right) \geq 1 - \delta$$

其中 $R(h) = \mathbb{E}_{(x,y)\sim\mathcal{D}}[\ell(h(x), y)]$ 是真实风险，$A(S)$ 是算法在训练集 $S$ 上输出的假设。

> 一行解释：PAC = 用多项式样本达到近似正确、以高概率成功。

### 1.2 Finite Hypothesis Class

**Theorem**: 若 $|\mathcal{H}| < \infty$，$\ell \in [0, 1]$，则 ERM 是 PAC learnable 的，样本复杂度：

$$m(\epsilon, \delta) = \frac{\ln|\mathcal{H}| + \ln(1/\delta)}{2\epsilon^2}$$

**Proof**:

**Step 1**: 对单个假设 $h$，由 Hoeffding [F18.3]：

$$P(|R(h) - \hat{R}(h)| \geq \epsilon) \leq 2e^{-2n\epsilon^2}$$

**Step 2**: Union bound [F18.20] 对所有 $h \in \mathcal{H}$：

$$P(\exists h: |R(h) - \hat{R}(h)| \geq \epsilon) \leq 2|\mathcal{H}| \cdot e^{-2n\epsilon^2}$$

**Step 3**: 设 $\leq \delta$，解得 $n \geq \frac{\ln(2|\mathcal{H}|/\delta)}{2\epsilon^2}$。$\square$

**When to use**: 直觉建设——理解为什么更复杂的模型需要更多数据。实际中 $|\mathcal{H}|$ 通常无穷大，需要 VC dim 等工具。

---

## 2. VC Dimension [F18.10]

### 2.1 Definitions

**Shattering**: 假设类 $\mathcal{H}$ shatters 集合 $\{x_1,\ldots,x_m\}$，如果对所有 $2^m$ 种 $\{0,1\}^m$ 标签，都存在 $h \in \mathcal{H}$ 实现该标签。

**VC dimension**: $\mathrm{VCdim}(\mathcal{H}) = \max\{m : \exists S, |S|=m, \mathcal{H} \text{ shatters } S\}$。

### 2.2 Sauer's Lemma (Sauer-Shelah Lemma)

**Statement**: 设 $\mathrm{VCdim}(\mathcal{H}) = d$。则 growth function 满足：

$$\Pi_{\mathcal{H}}(m) = \max_{S:|S|=m} |\{(h(x_1),\ldots,h(x_m)) : h \in \mathcal{H}\}| \leq \sum_{i=0}^{d} \binom{m}{i} \leq \left(\frac{em}{d}\right)^d$$

**Proof sketch** (induction on $m$ and $d$):

Base cases: $\Pi(m) = 2^m$ when $d \geq m$; $\Pi(m) \leq 1$ when $d = 0$.

Inductive step: Fix a point $x_m$, partition hypotheses by behavior on $x_m$. Use double counting to show $\Pi(m) \leq \Pi(m-1, d) + \Pi(m-1, d-1)$. The inequality follows from the combinatorial identity. $\square$

> 一行解释：VC 维有限 → 增长函数从指数变为多项式 → 可以用有限样本均匀收敛。

### 2.3 Fundamental Theorem of Statistical Learning

**Theorem** [Vapnik & Chervonenkis, 1971; Blumer et al., 1989]: 以下等价：
1. $\mathcal{H}$ 是 PAC learnable 的
2. $\mathcal{H}$ 有 uniform convergence 性质
3. $\mathrm{VCdim}(\mathcal{H}) < \infty$

**Sample complexity**: $\mathrm{VCdim}(\mathcal{H}) = d$ 时：

$$m(\epsilon, \delta) = O\left(\frac{d \log(d/\epsilon) + \log(1/\delta)}{\epsilon^2}\right)$$

**VC Generalization Bound**: 以概率 $\geq 1-\delta$，对所有 $h \in \mathcal{H}$：

$$R(h) \leq \hat{R}(h) + O\left(\sqrt{\frac{d \log(n/d) + \log(1/\delta)}{n}}\right)$$

**When to use**: 经典泛化分析的黄金标准。限制：对神经网络通常过于悲观（VC dim 随参数数增长，但实际泛化好得多）。

### 2.4 Key VC Dimension Examples

| 假设类 | VC Dimension |
|--------|-------------|
| 1D 阈值函数 | 1 |
| $\mathbb{R}^d$ 中的线性分类器 | $d+1$ |
| $\mathbb{R}^d$ 中的 $k$-NN | $\infty$ |
| 深度 $L$、宽度 $W$ 的 ReLU 网络 | $O(WL \log(WL))$ |
| 具有 $P$ 个参数的 ReLU 网络 | $O(P \log P)$ |

---

## 3. Rademacher Complexity [F18.11]

### 3.1 Definition

**Empirical Rademacher complexity**:

$$\hat{\mathcal{R}}_n(\mathcal{F}) = \mathbb{E}_\sigma\left[\sup_{f \in \mathcal{F}} \frac{1}{n}\sum_{i=1}^n \sigma_i f(x_i)\right]$$

其中 $\sigma_i \stackrel{\text{iid}}{\sim} \mathrm{Uniform}\{-1, +1\}$ 是 Rademacher 随机变量。

**Rademacher complexity** (averaged over data):

$$\mathcal{R}_n(\mathcal{F}) = \mathbb{E}_S\left[\hat{\mathcal{R}}_n(\mathcal{F})\right]$$

> 一行解释：Rademacher 复杂度衡量函数类拟合随机噪声的能力——能拟合噪声 → 容易过拟合。

### 3.2 Generalization Bound

**Theorem** [Bartlett & Mendelson, 2002]: 对任意 $\delta > 0$，以概率 $\geq 1-\delta$，对所有 $f \in \mathcal{F}$：

$$R(f) \leq \hat{R}(f) + 2\mathcal{R}_n(\mathcal{F}) + \sqrt{\frac{\ln(1/\delta)}{2n}}$$

**Proof**:

**Step 1 (Symmetrization)**: 引入 ghost sample $S' = \{x_1', \ldots, x_n'\}$：

$$\mathbb{E}_S\left[\sup_{f} (R(f) - \hat{R}(f))\right] = \mathbb{E}_S\left[\sup_f \mathbb{E}_{S'}[\hat{R}'(f)] - \hat{R}(f)\right]$$

$$\leq \mathbb{E}_{S,S'}\left[\sup_f (\hat{R}'(f) - \hat{R}(f))\right]$$

**Step 2 (Rademacher introduction)**: 因为 $x_i$ 和 $x_i'$ 可交换：

$$= \mathbb{E}_{S,S',\sigma}\left[\sup_f \frac{1}{n}\sum_i \sigma_i(f(x_i') - f(x_i))\right] \leq 2\mathbb{E}_{S,\sigma}\left[\sup_f \frac{1}{n}\sum_i \sigma_i f(x_i)\right] = 2\mathcal{R}_n(\mathcal{F})$$

**Step 3 (High probability)**: $\phi(S) = \sup_f(R(f) - \hat{R}(f))$ 满足有界差分条件（改变一个样本最多影响 $2/n$），由 McDiarmid [F18.6]：

$$P(\phi(S) \geq \mathbb{E}[\phi(S)] + t) \leq e^{-nt^2/2}$$

设 $t = \sqrt{\ln(1/\delta)/(2n)}$ 并合并。$\square$

**When to use**: 比 VC 维更精细；可以利用损失函数的 Lipschitz 性质（通过 contraction lemma）缩减复杂度。

### 3.3 Relationship to VC Dimension

**Theorem** [Dudley, Haussler]: 对二值函数类 $\mathcal{F}: \mathcal{X} \to \{0, 1\}$：

$$\mathcal{R}_n(\mathcal{F}) \leq \sqrt{\frac{2d \ln(en/d)}{n}}$$

其中 $d = \mathrm{VCdim}(\mathcal{F})$。因此 Rademacher bound 可以recover VC bound（但通常更紧，因为它是数据依赖的）。

### 3.4 Contraction Lemma (Talagrand)

**Theorem**: 若 $\phi: \mathbb{R} \to \mathbb{R}$ 是 $L$-Lipschitz，$\phi(0) = 0$，则：

$$\mathcal{R}_n(\phi \circ \mathcal{F}) \leq L \cdot \mathcal{R}_n(\mathcal{F})$$

> 一行解释：Lipschitz 损失函数不会增加函数类的 Rademacher 复杂度（至多乘以 Lipschitz 常数）。

**When to use**: 将假设类的复杂度转化为关于损失函数的复杂度。

---

## 4. Neural Network Generalization Bounds

### 4.1 Norm-Based Bounds [Bartlett & Mendelson, 2002; Neyshabur et al., 2015]

**Theorem** (spectral norm bound): 对深度 $L$ 的 ReLU 网络 $f_W$，参数 $W = (W_1, \ldots, W_L)$：

$$\mathcal{R}_n(\mathcal{F}) \leq \frac{2^L \prod_{l=1}^L \|W_l\|_\sigma \cdot (\sum_{l=1}^L \|W_l\|_F^{2/3} / \|W_l\|_\sigma^{2/3})^{3/2}}{\sqrt{n}}$$

其中 $\|W_l\|_\sigma$ 是谱范数，$\|W_l\|_F$ 是 Frobenius 范数。

**Intuition**: 泛化不取决于参数数量 $P$，而取决于权重矩阵的范数（"有效复杂度"）。这解释了为什么过参数化网络仍能泛化。

**When to use**: 分析深度学习模型的泛化性；解释为什么正则化（weight decay）有效。

### 4.2 PAC-Bayes Bounds [F18.12]

**Theorem** [McAllester, 1999; Catoni, 2007]: 对任意先验 $P$（数据无关），以概率 $\geq 1-\delta$，对所有后验 $Q$：

$$\mathbb{E}_{h \sim Q}[R(h)] \leq \mathbb{E}_{h \sim Q}[\hat{R}(h)] + \sqrt{\frac{D_{\mathrm{KL}}(Q \| P) + \ln(n/\delta)}{2(n-1)}}$$

**Proof sketch**:

**Step 1 (Change of measure)**: 对任意随机变量 $Z$ 和分布 $P, Q$：

$$\mathbb{E}_Q[Z] \leq D_{\mathrm{KL}}(Q\|P) + \ln \mathbb{E}_P[e^Z]$$

（由 Donsker-Varadhan variational formula）。

**Step 2**: 取 $Z = \lambda(R(h) - \hat{R}(h))$，利用 $\mathbb{E}_P[e^Z]$ 的高概率控制（通过 Hoeffding + 积分技巧）。

**Step 3**: 对 $\lambda$ 优化得到最终形式。$\square$

**Practical use**: 近年来 PAC-Bayes 界已经可以给出非空洞（non-vacuous）的泛化证书，特别是对 SGD 训练的网络（视为近似后验采样）。

### 4.3 Compression-Based Bounds

**Theorem** [Arora et al., 2018]: 如果网络可以被压缩为 $q$ 个有效参数（通过量化、剪枝等），则泛化间隙为 $O(\sqrt{q \log n / n})$。

> 一行解释：模型的"可压缩性"决定泛化——可以被简洁描述的模型泛化好。

---

## 5. GNN Generalization (图神经网络泛化)

### 5.1 GNN Rademacher Complexity [Garg et al., 2020]

**Theorem**: 对 $L$ 层 GNN，消息传递 $h_v^{(l+1)} = \sigma(W_l \cdot \mathrm{AGG}(\{h_u^{(l)}: u \in N(v)\}))$：

$$\mathcal{R}_n(\mathcal{F}_{\text{GNN}}) \leq \frac{C \cdot \prod_{l=1}^L \|W_l\|_\sigma \cdot \sqrt{\sum_l \|W_l\|_F^2 / \|W_l\|_\sigma^2}}{\sqrt{n}}$$

类似于全连接网络的范数界，但 AGG 操作引入了图结构的影响。

### 5.2 Size Generalization [Yehudai et al., 2021]

**Problem**: GNN 在小图上训练，能否泛化到大图？

**Theorem (negative result)**: 存在图函数类，使得任何 GNN（有界 WL 深度）无法从 $n$ 节点图泛化到 $cn$ 节点图（$c > 1$ 常数）。

**Positive results** (sufficient conditions for size generalization):
1. 目标函数是"局部"的（仅依赖 $k$-hop 邻域统计量）
2. 图序列满足某种"图极限"收敛
3. GNN 层数 $\leq$ 图的直径

**Application to user's work**: GNN decoder (如 DIFUSCO 中的 GNN) 从小码距训练泛化到大码距：
- 如果解码器仅使用 local syndrome pattern → 有理论保证
- 如果依赖 global graph structure → 可能不泛化，需要额外技巧

### 5.3 DIFUSCO/GNN Decoder Generalization

**Practical analysis**: 对于 GNN-based QEC decoder：

1. **Input**: syndrome graph (nodes = stabilizers, edges = qubits)
2. **Training**: on code distance $d_{\text{train}}$
3. **Testing**: on code distance $d_{\text{test}} > d_{\text{train}}$

**Why it might work**:
- Surface code syndrome graph has local structure
- Error chains are local (under independent noise)
- GNN with $L$ layers sees $L$-hop neighborhood → local pattern

**Why it might fail**:
- Logical errors require global information (homology class)
- $d_{\text{test}} > d_{\text{train}}$ changes the graph topology

**Theoretical framework**: McDiarmid [F18.6] applied to graph perturbations can bound the sensitivity of GNN output to graph size changes.

---

## 6. Le Cam's Two-Point Method (Minimax Lower Bounds) [F18.18]

### 6.1 Statement

**Theorem** [Le Cam, 1973]: 对参数估计问题，损失 $\ell(\hat{\theta}, \theta)$：

$$\inf_{\hat{\theta}} \sup_{\theta \in \Theta} \mathbb{E}[\ell(\hat{\theta}, \theta)] \geq \frac{\ell(\theta_0, \theta_1)}{2} \left(1 - \|P_{\theta_0}^n - P_{\theta_1}^n\|_{\mathrm{TV}}\right)$$

其中 $\theta_0, \theta_1 \in \Theta$ 是两个"难以区分"的参数。

**Proof sketch**:

考虑 prior $\pi = \frac{1}{2}\delta_{\theta_0} + \frac{1}{2}\delta_{\theta_1}$。贝叶斯风险 $\leq$ minimax 风险。贝叶斯最优检验的误差率由 TV 距离控制。$\square$

### 6.2 Key Tool: TV Distance of Product Distributions

$$\|P_{\theta_0}^n - P_{\theta_1}^n\|_{\mathrm{TV}} \leq \sqrt{\frac{n}{2} D_{\mathrm{KL}}(P_{\theta_0} \| P_{\theta_1})}$$

（由 Pinsker 不等式 + tensorization）

### 6.3 Application: Quantum State Tomography Lower Bound

**Claim**: 估计 $d$-维密度矩阵需要 $\Omega(d^2/\epsilon^2)$ 个 copies。

**Proof sketch via Le Cam**:
1. Choose $\theta_0 = I/d$（最大混合态），$\theta_1 = I/d + \epsilon \cdot \Delta$，$\Delta$ 是 traceless Hermitian
2. $\|\theta_0 - \theta_1\|_1 = \Theta(\epsilon)$ → $\ell(\theta_0, \theta_1) = \Theta(\epsilon)$
3. Single-copy KL: $D_{\mathrm{KL}}(P_{\theta_0} \| P_{\theta_1}) = O(\epsilon^2/d)$（对最优测量）
4. TV distance: $\|P^n_{\theta_0} - P^n_{\theta_1}\|_{\mathrm{TV}} \leq \sqrt{n\epsilon^2/(2d)}$
5. For Le Cam bound to be nontrivial: $n \leq O(d/\epsilon^2)$
6. 但 density matrix 有 $O(d^2)$ 个自由度 → 需要对 $O(d^2)$ 个方向取 worst case → $n = \Omega(d^2/\epsilon^2)$

（完整证明需要 Fano/Assouad 方法处理多参数，见 Haah et al. 2017。）

---

## 7. Online Learning Regret [F18.19]

### 7.1 Online Gradient Descent (OGD)

**Setup**: 在线凸优化——每轮 $t$，选择 $x_t \in \mathcal{K}$，观察凸损失 $f_t$，承受损失 $f_t(x_t)$。

**Algorithm**: $x_{t+1} = \Pi_{\mathcal{K}}(x_t - \eta g_t)$，其中 $g_t \in \partial f_t(x_t)$。

**Theorem**: 设 $\|g_t\| \leq G$，$\mathrm{diam}(\mathcal{K}) \leq D$。取 $\eta = D/(G\sqrt{T})$：

$$R_T = \sum_{t=1}^T f_t(x_t) - \min_{x \in \mathcal{K}} \sum_{t=1}^T f_t(x) \leq DG\sqrt{T}$$

**Proof**:

$$f_t(x_t) - f_t(x^*) \leq \langle g_t, x_t - x^* \rangle = \frac{1}{\eta}\langle x_t - x_{t+1} + \eta g_t - x_t + x_{t+1}, x_t - x^*\rangle$$

$$\leq \frac{1}{2\eta}(\|x_t - x^*\|^2 - \|x_{t+1} - x^*\|^2) + \frac{\eta}{2}\|g_t\|^2$$

（用了投影的非扩张性和 $2\langle a, b\rangle = \|a\|^2 + \|b\|^2 - \|a-b\|^2$。）

对 $t$ 求和（telescoping）：

$$R_T \leq \frac{\|x_1 - x^*\|^2}{2\eta} + \frac{\eta}{2}\sum_t \|g_t\|^2 \leq \frac{D^2}{2\eta} + \frac{\eta G^2 T}{2}$$

取 $\eta = D/(G\sqrt{T})$：$R_T \leq DG\sqrt{T}$。$\square$

> 一行解释：在线凸优化的遗憾界 $O(\sqrt{T})$——与最优固定策略相比，平均每轮多付 $O(1/\sqrt{T})$。

**When to use**: 分析 SGD 的收敛性（可以视为在线学习）；变分量子算法中参数优化的遗憾分析；对抗性环境下的学习保证。

---

## Cross-References (交叉引用)

- **Concentration inequalities used** → [concentration_inequalities.md]: Hoeffding [F18.3], McDiarmid [F18.6] in proofs
- **Union bound** → [concentration_inequalities.md]: Used in finite hypothesis class proof
- **GNN theory** → [../07_graph_theory/]: GNN architecture definitions
- **DIFUSCO** → [../11_ml_theory/derivations/difusco_theory.md]: Diffusion model for combinatorial optimization
- **Quantum tomography** → [../02_quantum_mechanics/derivations/]: State estimation
- **Matrix concentration** → [matrix_concentration.md]: Matrix Bernstein for shadow tomography
- **PAC-Bayes** references: McAllester 1999, Catoni 2007, Dziugaite & Roy 2017
- **GNN generalization** references: Garg et al. 2020, Yehudai et al. 2021, Liao et al. 2021
