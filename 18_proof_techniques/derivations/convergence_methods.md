# Convergence Methods: Contraction, Coupling, Mixing

> 证明迭代过程收敛的三大方法：压缩映射、耦合、谱方法。
> 应用：扩散模型反向过程收敛、信念传播收敛、MCMC 收敛分析。

---

## 1. Contraction Mapping / Banach Fixed Point Theorem [F18.13]

### 1.1 Statement

**Theorem** [Banach, 1922]: 设 $(X, d)$ 是完备度量空间，$T: X \to X$ 是压缩映射，即存在 $0 \leq \gamma < 1$ 使得：

$$d(Tx, Ty) \leq \gamma \cdot d(x, y), \quad \forall\, x, y \in X$$

则：
1. $T$ 有唯一不动点 $x^* \in X$，$Tx^* = x^*$
2. 对任意 $x_0 \in X$，$x_n = T^n x_0 \to x^*$
3. **先验估计**: $d(x_n, x^*) \leq \frac{\gamma^n}{1 - \gamma} d(x_0, x_1)$
4. **后验估计**: $d(x_n, x^*) \leq \frac{\gamma}{1 - \gamma} d(x_{n-1}, x_n)$

### 1.2 Proof

**Existence (Cauchy sequence)**:

$$d(x_{n+1}, x_n) = d(Tx_n, Tx_{n-1}) \leq \gamma \cdot d(x_n, x_{n-1}) \leq \cdots \leq \gamma^n \cdot d(x_1, x_0)$$

对 $m > n$：

$$d(x_m, x_n) \leq \sum_{k=n}^{m-1} d(x_{k+1}, x_k) \leq d(x_1, x_0) \sum_{k=n}^{m-1} \gamma^k \leq \frac{\gamma^n}{1-\gamma} d(x_1, x_0)$$

因 $\gamma < 1$，右端 $\to 0$，故 $\{x_n\}$ 是 Cauchy 序列。由完备性，$x_n \to x^*$。

**$x^*$ is a fixed point**: $d(x^*, Tx^*) = \lim_n d(x_n, Tx^*) = \lim_n d(Tx_{n-1}, Tx^*) \leq \gamma \lim_n d(x_{n-1}, x^*) = 0$。

**Uniqueness**: 若 $Ty^* = y^*$，则 $d(x^*, y^*) = d(Tx^*, Ty^*) \leq \gamma \cdot d(x^*, y^*)$，由 $\gamma < 1$ 得 $d(x^*, y^*) = 0$。$\square$

> 一行解释：压缩映射必有唯一不动点，迭代以几何速率 $\gamma^n$ 收敛。

### 1.3 Application: Belief Propagation on Trees

**Setup**: 因子图上的 BP（sum-product 算法），消息更新 $m_{v \to f}^{(t+1)} = T(m^{(t)})$。

**On trees** (无环图): BP 消息更新是精确的 Bethe 自由能的不动点迭代。

**Contraction**: 在树上，消息空间中的 BP 更新满足（在合适的度量下）：

$$d(T(m), T(m')) \leq \tanh(\beta J) \cdot d(m, m')$$

当 $\tanh(\beta J) < 1$（即温度足够高或耦合足够弱），BP 是压缩映射 → 唯一不动点 → BP 收敛。

**On graphs with cycles**: BP 不再保证是压缩映射。收敛依赖于图的结构（girth, degree 等）。这是 BP 解码在 LDPC 码上的理论基础。

> **与 QEC 的关联**: BP 解码 surface code / LDPC code 时，在树状区域快速收敛，在有环区域可能振荡。

### 1.4 Application: Bellman Equation

$$V^*(s) = \max_a \left[r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s')\right]$$

Bellman 最优算子 $T$ 在 $\|\cdot\|_\infty$ 下是 $\gamma$-压缩（$\gamma$ 是折扣因子）。因此值迭代（value iteration）以 $\gamma^n$ 速率收敛。

---

## 2. Coupling Method [F18.15]

### 2.1 Definition of Coupling

给定两个概率分布 $P, Q$ on $\mathcal{X}$，一个 **coupling** 是联合分布 $\gamma$ on $\mathcal{X} \times \mathcal{X}$ 使得：
- 边际分布：$\gamma(A \times \mathcal{X}) = P(A)$，$\gamma(\mathcal{X} \times A) = Q(A)$

> 一行解释：耦合 = 在同一概率空间上同时实现两个分布，使得可以"逐点比较"。

### 2.2 Coupling Inequality

**Theorem**:

$$\|P - Q\|_{\mathrm{TV}} = \inf_{\gamma \in \Gamma(P,Q)} P_{(X,Y) \sim \gamma}[X \neq Y]$$

**Proof (sketch)**:

**Upper bound** ($\leq$): 对任何耦合 $\gamma$ 和事件 $A$：

$$P(A) - Q(A) = P_\gamma(X \in A) - P_\gamma(Y \in A)$$
$$= P_\gamma(X \in A, X \neq Y) + P_\gamma(X \in A, X = Y) - P_\gamma(Y \in A, X \neq Y) - P_\gamma(Y \in A, X = Y)$$
$$\leq P_\gamma(X \neq Y)$$

取 $\sup_A$ 和 $\inf_\gamma$ 得 $\|P-Q\|_{\mathrm{TV}} \leq \inf_\gamma P_\gamma(X \neq Y)$。

**Lower bound** ($\geq$): 构造最优耦合（maximal coupling）使等式成立。$\square$

### 2.3 Maximal Coupling Construction

**Construction**: 对离散分布，定义：

$$\gamma(x, x) = \min(P(x), Q(x)), \quad \text{(agree part)}$$

剩余概率质量按条件分布独立采样（disagree part）。

此耦合下 $P(X = Y) = \sum_x \min(P(x), Q(x)) = 1 - \|P-Q\|_{\mathrm{TV}}$。

### 2.4 Application to Markov Chain Convergence

**Setup**: 马尔可夫链 $(X_t)$ 和 $(Y_t)$，$X_0 \sim \mu$（任意初始分布），$Y_0 \sim \pi$（平稳分布）。

**Coupling construction**: 构造联合过程 $(X_t, Y_t)$：
- 当 $X_t \neq Y_t$：各自按转移核独立演化
- 当 $X_t = Y_t$：之后永远 $X_s = Y_s$（coupling time $\tau$）

**Coupling bound**:

$$\|P^t\mu - \pi\|_{\mathrm{TV}} \leq P(\tau > t)$$

如果 coupling time $\tau$ 有指数尾 $P(\tau > t) \leq C\rho^t$，则混合时间为 $O(\log(1/\epsilon)/\log(1/\rho))$。

---

## 3. Markov Chain Mixing [F18.14]

### 3.1 Spectral Gap Method

**Setup**: 可逆马尔可夫链，转移矩阵 $P$（关于 $\pi$ 可逆），特征值 $1 = \lambda_1 > \lambda_2 \geq \cdots \geq \lambda_n \geq -1$。

**Spectral gap**: $\lambda_{\mathrm{gap}} = 1 - \max(|\lambda_2|, |\lambda_n|) = 1 - \lambda^*$。

**Mixing time bound**:

$$t_{\mathrm{mix}}(\epsilon) \leq \frac{1}{\lambda_{\mathrm{gap}}} \ln\left(\frac{1}{\epsilon \cdot \pi_{\min}}\right)$$

**Proof sketch**: 用谱分解 $P^t = \sum_i \lambda_i^t v_i v_i^\top$，因此：

$$\left\|P^t(x, \cdot) - \pi\right\|_2^2 = \sum_{i \geq 2} \lambda_i^{2t} v_i(x)^2 \leq (\lambda^*)^{2t} \cdot \frac{1}{\pi(x)}$$

由 Cauchy-Schwarz 转化为 TV 距离。$\square$

### 3.2 Conductance / Cheeger Inequality

**Conductance** (Cheeger 常数):

$$\Phi = \min_{S: 0 < \pi(S) \leq 1/2} \frac{\sum_{x \in S, y \notin S} \pi(x) P(x,y)}{\pi(S)}$$

**Cheeger Inequality for Markov Chains**:

$$\frac{\Phi^2}{2} \leq \lambda_{\mathrm{gap}} \leq 2\Phi$$

> 一行解释：谱间隙 ≈ conductance² — 链的"瓶颈"越窄，混合越慢。

**When to use**: 当直接计算特征值困难时，通过几何方法（分析"瓶颈"）来bound mixing time。

### 3.3 Path Coupling [Bubley & Dyer, 1997]

**Theorem**: 设 $d$ 是图度量（定义在状态空间的图上），$U$ 是相邻状态对的集合。如果对所有 $(x, y) \in U$（$d(x,y) = 1$），存在耦合使得：

$$\mathbb{E}[d(X', Y') | X=x, Y=y] \leq (1-\alpha) \cdot d(x, y) = 1-\alpha$$

则对任意初始分布 $\mu$：

$$\|P^t\mu - \pi\|_{\mathrm{TV}} \leq \mathrm{diam}(G) \cdot (1-\alpha)^t$$

> 一行解释：只需检查相邻状态的耦合收缩性——大大简化了证明。

**When to use**: 当状态空间大但相邻状态间的转移容易分析时（如 Glauber dynamics, Metropolis algorithm）。

### 3.4 Mixing Time Examples

| Chain | Spectral Gap | Mixing Time |
|-------|-------------|-------------|
| Random walk on $\mathbb{Z}_n$ | $\Theta(1/n^2)$ | $\Theta(n^2)$ |
| Random walk on expander graph | $\Theta(1)$ | $\Theta(\log n)$ |
| Glauber dynamics (Ising, high-T) | $\Theta(1/n)$ | $\Theta(n \log n)$ |
| MCMC for uniform sampling from convex body | $\Theta(1/(n \cdot R^2))$ | $\Theta(n \cdot R^2 \log(1/\epsilon))$ |

---

## 4. Application to Diffusion Models (扩散模型收敛)

### 4.1 DDPM Reverse Process Convergence

**Setup**: 前向过程 $q(x_t|x_0) = \mathcal{N}(\sqrt{\bar\alpha_t} x_0, (1-\bar\alpha_t)I)$。反向过程学习 $p_\theta(x_{t-1}|x_t)$。

**Convergence via coupling**: 定义 $p_\theta$ 和真实反向过程 $p^*$ 的耦合。

**Key result** [Chen et al., 2023]: 在 score estimation error $\epsilon_{\mathrm{score}} = \mathbb{E}\left[\|s_\theta(x_t, t) - \nabla \log q_t(x_t)\|^2\right]$ 下：

$$\mathrm{TV}(p_\theta(x_0), q(x_0)) \leq O\left(\sqrt{T \cdot \epsilon_{\mathrm{score}}} + \sqrt{d/T}\right)$$

**Proof structure**:
1. 将 $T$ 步反向过程分解为 $T$ 个单步
2. 每步的 TV 误差由 score error 和 discretization error 控制
3. 用 **data processing inequality** 将误差累积（不是简单相加，因为 Markov 性质）
4. 总误差 $\leq \sum_t \epsilon_t$，其中 $\epsilon_t$ 是第 $t$ 步的 TV 误差

**Connection to mixing**: DDPM 反向过程可以看作一种"退火 Langevin dynamics"——从高温（$t=T$，近似高斯）逐步退火到低温（$t=0$，目标分布）。mixing time 分析给出 $T$ 的选择。

### 4.2 Discrete Diffusion (D3PM) Convergence

**Setup**: 离散状态空间上的扩散。前向：$q(x_t|x_{t-1}) = x_{t-1} Q_t$。

**Mixing of forward process**: $Q_t$ 的特征值决定前向过程的混合速率。对 uniform noise: $Q_t = (1-\beta_t)I + \beta_t \mathbf{1}\mathbf{1}^\top/K$，谱间隙 = $\beta_t$。

**Reverse convergence**: 类似连续情况，但用离散 coupling（耦合不等式 [F18.15]）。

> **与用户研究的关联**: D3PM/DiGress 用于组合优化问题的采样。理论收敛速率决定了所需的扩散步数 $T$。

---

## 5. Application to Decoders (解码器收敛)

### 5.1 BP Convergence on Trees (精确)

在树状因子图上，BP 消息在 $O(\mathrm{diameter})$ 步后精确收敛（无近似误差）。

**Proof**: 用 contraction mapping [F18.13]。消息从叶到根传播，每步传播一层。

### 5.2 BP on Loopy Graphs (近似)

在有环图上，BP 不保证收敛。但当图的 girth（最短环长）$\geq 2L+1$（$L$ 是 BP 迭代次数）时，BP 消息与树上相同——"局部树状"近似。

**For LDPC codes**: random LDPC code 的 Tanner 图 girth = $\Omega(\log n)$，所以 BP 在 $O(\log n)$ 步内近似正确。

**For surface code**: Tanner 图有短环（长度 4），BP 收敛性更差。这解释了为什么 BP 解码 surface code 效果不如 MWPM。

### 5.3 Neural Decoder Convergence

GNN-based decoder（如 DIFUSCO 的 GNN 部分）：
- 可以视为"学到的消息传递"
- 收敛性不再由 contraction mapping 保证
- 但可以通过 Lipschitz 约束（spectral normalization）强制压缩性

---

## Cross-References (交叉引用)

- **Concentration inequalities** → [concentration_inequalities.md]: Azuma [F18.7] for martingale convergence
- **Coupling inequality** → [concentration_inequalities.md]: Sub-Gaussian framework
- **Diffusion models** → [../11_ml_theory/derivations/diffusion_models_math.md]: DDPM forward/reverse
- **BP decoding** → [../04_quantum_error_correction/derivations/]: Decoder analysis
- **Spectral methods** → [../01_linear_algebra/derivations/spectral_decomposition.md]: Eigenvalue theory
- **TV distance** → [../02_quantum_mechanics/derivations/fidelity_and_trace_distance.md]: Quantum generalization
- **Original references**:
  - Levin, Peres & Wilmer, "Markov Chains and Mixing Times", 2009
  - Bubley & Dyer, "Path coupling: A technique for proving rapid mixing", 1997
  - Lindvall, "Lectures on the Coupling Method", 2002
  - Chen et al., "Sampling is as easy as learning the score", 2023
