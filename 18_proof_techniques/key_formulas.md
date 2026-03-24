# 18. Proof Techniques Arsenal: Key Formulas

> 论文写作中最常用的不等式、界和证明工具。
> 这些是"万金油"级别的工具——几乎所有理论分析都会用到其中几个。
> 所有公式使用 LaTeX 记法，解释用中文。

---

### F18.1: Markov Inequality (马尔可夫不等式)

$$P(X \geq a) \leq \frac{\mathbb{E}[X]}{a}, \quad \forall\, a > 0$$

要求 $X \geq 0$。最基本的概率尾界：非负随机变量超过 $a$ 的概率不超过均值除以 $a$。虽然松，但它是所有更强集中不等式的起点。

**When to use**: 当你只知道均值、无其他信息时的最后手段；或作为推导更强不等式的第一步。

**Source**: [derivations/concentration_inequalities.md] | 任何概率论教材

---

### F18.2: Chebyshev Inequality (切比雪夫不等式)

$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$$

等价形式：$P(|X - \mu| \geq t) \leq \frac{\mathrm{Var}(X)}{t^2}$。利用二阶矩（方差）给出比 Markov 更紧的尾界。

**When to use**: 当你知道均值和方差、但不知道分布形状时。常用于证明弱大数定律。

**Source**: [derivations/concentration_inequalities.md] | 由 Markov 不等式应用于 $(X-\mu)^2$ 得到

---

### F18.3: Hoeffding Inequality (Hoeffding 不等式)

$$P\left(\bar{X} - \mu \geq t\right) \leq \exp\left(-\frac{2nt^2}{(b-a)^2}\right)$$

其中 $X_1, \ldots, X_n$ 是独立随机变量，$X_i \in [a_i, b_i]$，$\bar{X} = \frac{1}{n}\sum X_i$。一般形式的指数为 $-2t^2/\sum(b_i - a_i)^2$。有界独立随机变量均值的指数级集中。

**When to use**: 经验均值偏离真实均值的概率界。量子计算中：从 $N$ 次测量估计期望值（如保真度）的置信区间。

**Source**: [derivations/concentration_inequalities.md] | Hoeffding, 1963

---

### F18.4: Chernoff Bound (Chernoff 界，乘法形式)

$$P\left(X \geq (1+\delta)\mu\right) \leq \left(\frac{e^\delta}{(1+\delta)^{(1+\delta)}}\right)^\mu$$

其中 $X = \sum X_i$，$X_i$ 独立 Bernoulli，$\mu = \mathbb{E}[X]$。简化形式：$P(X \geq (1+\delta)\mu) \leq \exp(-\mu\delta^2/3)$（当 $0 < \delta \leq 1$）。

**When to use**: 计数随机事件（如量子纠错中错误个数）超过阈值的概率。比 Hoeffding 对 Bernoulli 和更紧。

**Source**: [derivations/concentration_inequalities.md] | Chernoff, 1952; Mitzenmacher & Upfal

---

### F18.5: Bernstein Inequality (Bernstein 不等式)

$$P\left(\sum_{i=1}^n X_i \geq t\right) \leq \exp\left(-\frac{t^2/2}{\sum \mathbb{E}[X_i^2] + bt/3}\right)$$

其中 $X_i$ 独立、零均值、$|X_i| \leq b$。相比 Hoeffding，Bernstein 利用了方差信息：当方差远小于有界范围时，Bernstein 比 Hoeffding 紧得多。

**When to use**: 当随机变量的方差比范围小很多时（如稀疏随机变量）。对"方差自适应"的集中不等式非常有用。

**Source**: [derivations/concentration_inequalities.md] | Bernstein, 1924; Boucheron et al.

---

### F18.6: McDiarmid Inequality (有界差分不等式)

$$P\left(f(X_1, \ldots, X_n) - \mathbb{E}[f] \geq t\right) \leq \exp\left(-\frac{2t^2}{\sum_{i=1}^n c_i^2}\right)$$

其中 $c_i = \sup_{x_1,\ldots,x_n, x_i'} |f(x_1,\ldots,x_i,\ldots,x_n) - f(x_1,\ldots,x_i',\ldots,x_n)|$ 是改变第 $i$ 个变量对 $f$ 影响的最大值。Hoeffding 不等式在函数空间的推广。

**When to use**: 证明一个关于独立随机变量的函数（如图上的某个统计量）集中在均值附近。QAOA 中分析目标函数随图结构的集中性。

**Source**: [derivations/concentration_inequalities.md] | McDiarmid, 1989

---

### F18.7: Azuma-Hoeffding Inequality (鞅集中不等式)

$$P\left(|M_n - M_0| \geq t\right) \leq 2\exp\left(-\frac{t^2}{2\sum_{i=1}^n c_i^2}\right)$$

其中 $\{M_k\}$ 是鞅（martingale），$|M_k - M_{k-1}| \leq c_k$。将集中不等式从独立随机变量推广到鞅差序列。

**When to use**: 当随机变量有依赖关系但可以构造鞅时。McDiarmid 不等式的证明就是通过 Doob 鞅 + Azuma。

**Source**: [derivations/concentration_inequalities.md] | Azuma, 1967; Hoeffding, 1963

---

### F18.8: Sub-Gaussian Definition (亚高斯随机变量)

$$\mathbb{E}\left[e^{\lambda X}\right] \leq \exp\left(\frac{\lambda^2 \sigma^2}{2}\right), \quad \forall\, \lambda \in \mathbb{R}$$

零均值随机变量 $X$ 是 $\sigma$-sub-Gaussian 的，当且仅当其矩母函数被高斯的矩母函数控制。等价刻画：尾概率 $P(|X| \geq t) \leq 2e^{-t^2/(2\sigma^2)}$。

**When to use**: 统一框架处理有界随机变量、高斯随机变量等的集中性质。现代高维统计学的基本语言。

**Source**: [derivations/concentration_inequalities.md] | Vershynin, "High-Dimensional Probability"

---

### F18.9: Matrix Bernstein Inequality (矩阵 Bernstein 不等式)

$$P\left(\left\|\sum_{i=1}^n X_i\right\| \geq t\right) \leq (d_1 + d_2) \cdot \exp\left(-\frac{t^2/2}{\sigma^2 + Lt/3}\right)$$

其中 $X_i$ 是独立的零均值 $d_1 \times d_2$ 随机矩阵，$\|X_i\| \leq L$，$\sigma^2 = \max\left(\left\|\sum \mathbb{E}[X_i X_i^\dagger]\right\|, \left\|\sum \mathbb{E}[X_i^\dagger X_i]\right\|\right)$。标量 Bernstein 到矩阵的推广。

**When to use**: 量子态层析（tomography）的样本复杂度分析；经典阴影（classical shadows）的样本复杂度；随机矩阵理论。

**Source**: [derivations/matrix_concentration.md] | Tropp, 2012, "User-Friendly Tail Bounds for Sums of Random Matrices"

---

### F18.10: VC Dimension Bound (VC 维泛化界)

$$P\left(\sup_{f \in \mathcal{F}} |R(f) - \hat{R}(f)| > \epsilon\right) \leq 8 \cdot S(\mathcal{F}, n) \cdot e^{-n\epsilon^2/32}$$

因此样本复杂度为 $m = O\left(\frac{d}{\epsilon^2} \log \frac{d}{\epsilon} + \frac{1}{\epsilon^2}\log\frac{1}{\delta}\right)$，其中 $d = \mathrm{VCdim}(\mathcal{F})$。假设类的复杂度决定了泛化所需的样本数。

**When to use**: 经典泛化理论分析。证明某个假设类可以从有限样本学习。

**Source**: [derivations/learning_theory.md] | Vapnik & Chervonenkis, 1971; Shalev-Shwartz & Ben-David

---

### F18.11: Rademacher Complexity Bound (Rademacher 复杂度泛化界)

$$|R(f) - \hat{R}(f)| \leq 2\mathcal{R}_n(\mathcal{F}) + \sqrt{\frac{\log(1/\delta)}{2n}}$$

以至少 $1-\delta$ 的概率成立。$\mathcal{R}_n(\mathcal{F}) = \mathbb{E}\left[\sup_{f \in \mathcal{F}} \frac{1}{n}\sum_{i=1}^n \sigma_i f(x_i)\right]$，$\sigma_i$ 是 Rademacher 随机变量（等概率取 $\pm 1$）。比 VC 维更精细，可以捕捉函数类的"数据依赖"复杂度。

**When to use**: 需要比 VC 维更紧的泛化界；GNN/神经网络泛化分析；与具体损失函数相关的复杂度。

**Source**: [derivations/learning_theory.md] | Bartlett & Mendelson, 2002

---

### F18.12: PAC-Bayes Bound (PAC-Bayes 界)

$$\mathbb{E}_{h \sim Q}\left[R(h)\right] \leq \mathbb{E}_{h \sim Q}\left[\hat{R}(h)\right] + \sqrt{\frac{D_{\mathrm{KL}}(Q \| P) + \log(n/\delta)}{2(n-1)}}$$

以至少 $1-\delta$ 的概率对所有后验 $Q$ 同时成立。$P$ 是先验，$Q$ 是（数据依赖的）后验。将贝叶斯思想融入频率学派的泛化界。

**When to use**: 分析随机化预测器（如贝叶斯神经网络、扰动模型）的泛化性；对比不同先验的影响。近年来在解释深度学习泛化方面很活跃。

**Source**: [derivations/learning_theory.md] | McAllester, 1999; Catoni, 2007

---

### F18.13: Contraction Mapping Theorem (压缩映射/Banach 不动点定理)

设 $(X, d)$ 是完备度量空间，$T: X \to X$ 满足 $d(Tx, Ty) \leq \gamma \cdot d(x, y)$，$0 \leq \gamma < 1$。则：
1. $T$ 有唯一不动点 $x^* = Tx^*$；
2. 对任意 $x_0$，$x_n = T^n x_0 \to x^*$；
3. 收敛速率：$d(x_n, x^*) \leq \frac{\gamma^n}{1-\gamma} d(x_0, x_1)$。

**When to use**: 证明迭代算法收敛（如 Bellman 方程、信念传播在树上）；证明不动点存在且唯一。

**Source**: [derivations/convergence_methods.md] | Banach, 1922; Rudin, Functional Analysis

---

### F18.14: Markov Chain Mixing Time (马尔可夫链混合时间)

$$\left\|P^t \mu - \pi\right\|_{\mathrm{TV}} \leq C \rho^t$$

其中 $\rho = 1 - \lambda_{\mathrm{gap}}$，$\lambda_{\mathrm{gap}} = 1 - \lambda_2$ 是谱间隙（$\lambda_2$ 是转移矩阵第二大特征值）。混合时间 $t_{\mathrm{mix}}(\epsilon) = O\left(\frac{1}{\lambda_{\mathrm{gap}}} \log \frac{1}{\epsilon}\right)$。

**When to use**: 分析 MCMC 采样器收敛速度；扩散模型反向过程的收敛分析；随机行走算法分析。

**Source**: [derivations/convergence_methods.md] | Levin, Peres & Wilmer, "Markov Chains and Mixing Times"

---

### F18.15: Coupling Inequality (耦合不等式)

$$\|P - Q\|_{\mathrm{TV}} = \inf_{\gamma \in \Gamma(P,Q)} P_{(X,Y) \sim \gamma}\left[X \neq Y\right]$$

全变差距离等于最优耦合下 $X \neq Y$ 的概率。这是 TV 距离的对偶刻画，将分布间的距离转化为构造具体耦合的问题。

**When to use**: 证明两个分布接近（构造一个好的耦合使 $X \neq Y$ 概率小）；马尔可夫链收敛分析；扩散模型的收敛证明。

**Source**: [derivations/convergence_methods.md] | Lindvall, "Lectures on the Coupling Method"

---

### F18.16: Lovász Local Lemma (Lovász 局部引理)

**对称版**: 设 $A_1, \ldots, A_n$ 是事件，每个 $P(A_i) \leq p$，每个事件至多与 $d$ 个其他事件相关。若 $ep(d+1) \leq 1$，则

$$P\left(\bigcap_{i=1}^n \overline{A_i}\right) > 0$$

**When to use**: 证明存在性——当你想避免很多"坏事件"同时发生时。经典应用：图着色、Ramsey 理论、随机码的存在性。

**Source**: [derivations/probabilistic_method.md] | Erdős & Lovász, 1975; Alon & Spencer, "The Probabilistic Method"

---

### F18.17: Second Moment Method (二阶矩方法)

$$P(X > 0) \geq \frac{(\mathbb{E}[X])^2}{\mathbb{E}[X^2]}$$

也称 Paley-Zygmund 不等式（一般形式）。如果 $\mathbb{E}[X^2] = O((\mathbb{E}[X])^2)$，则 $X > 0$ 以常数概率发生。

**When to use**: 证明随机对象存在的概率不可忽略（第一矩方法只给 $P(X>0) > 0$ 的可能性，二阶矩给定量下界）。随机图理论、随机码分析。

**Source**: [derivations/probabilistic_method.md] | Alon & Spencer, "The Probabilistic Method"

---

### F18.18: Le Cam's Two-Point Method (Le Cam 两点方法)

$$\inf_{\hat{\theta}} \sup_{\theta} \mathbb{E}\left[\ell(\hat{\theta}, \theta)\right] \geq \frac{\ell(\theta_0, \theta_1)}{2} \left(1 - \|P_{\theta_0}^n - P_{\theta_1}^n\|_{\mathrm{TV}}\right)$$

将 minimax 下界归结为区分两个具体假设的问题。如果两个参数产生的分布难以区分（TV 距离小），那么估计误差有下界。

**When to use**: 证明估计问题的 minimax 最优性（如量子态层析的最优样本复杂度下界）。

**Source**: [derivations/learning_theory.md] | Le Cam, 1973; Yu, "Assouad, Fano, and Le Cam"

---

### F18.19: Online Gradient Descent Regret Bound (在线梯度下降遗憾界)

$$R_T = \sum_{t=1}^T f_t(x_t) - \min_{x \in \mathcal{K}} \sum_{t=1}^T f_t(x) \leq \frac{\|x_1 - x^*\|^2}{2\eta} + \frac{\eta}{2}\sum_{t=1}^T \|g_t\|^2 = O\left(\sqrt{T}\right)$$

取 $\eta = O(1/\sqrt{T})$ 时最优。在线凸优化的基本遗憾界——任何在线算法能做到的最好也就是 $O(\sqrt{T})$（对一般凸函数）。

**When to use**: 分析在线学习算法的性能保证；证明优化算法的遗憾界；与变分量子算法的参数更新分析相关。

**Source**: [derivations/learning_theory.md] | Zinkevich, 2003; Hazan, "Introduction to Online Convex Optimization"

---

### F18.20: Union Bound (联合界/Boole 不等式)

$$P\left(\bigcup_{i=1}^n A_i\right) \leq \sum_{i=1}^n P(A_i)$$

最简单但最常用的概率工具之一。几乎所有概率分析的第一步——将复杂事件拆解为简单事件的并。

**When to use**: 几乎无处不在。典型用法：先用集中不等式控制单个"坏事件"的概率，再用 union bound 把所有坏事件合并。VC 维证明、量子纠错阈值证明、采样复杂度分析都以此为起点。

**Source**: [derivations/concentration_inequalities.md] | Boole, 1847

---

## 公式依赖图 (Formula Dependency Map)

```
F18.20 Union Bound ─────────────────────────────┐
                                                  │
F18.1 Markov ──→ F18.2 Chebyshev                 │ (几乎所有分析的最后一步)
      │                                           │
      └──→ Exponential Markov ──→ F18.4 Chernoff  │
                │                                  │
                └──→ F18.3 Hoeffding ──→ F18.6 McDiarmid
                │                            │
                └──→ F18.5 Bernstein         F18.7 Azuma (鞅推广)
                │
                └──→ F18.8 Sub-Gaussian Framework
                            │
                            └──→ F18.9 Matrix Bernstein

F18.8 Sub-Gaussian ──→ F18.10 VC Dimension Bound
                    ──→ F18.11 Rademacher Bound
                    ──→ F18.12 PAC-Bayes Bound

F18.13 Contraction ──→ F18.14 Mixing Time (谱方法)
F18.15 Coupling    ──→ F18.14 Mixing Time (耦合方法)

F18.16 LLL ──→ 存在性证明
F18.17 Second Moment ──→ 存在性证明

F18.18 Le Cam ──→ Minimax 下界（用 F18.15 耦合/TV距离）
F18.19 OGD Regret ──→ 在线学习保证
```
