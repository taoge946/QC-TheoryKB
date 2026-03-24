# Matrix Concentration Inequalities

> 标量集中不等式到矩阵的推广——量子信息和高维统计中不可或缺的工具。
> 核心参考：Tropp, "An Introduction to Matrix Concentration Inequalities" (2015)
> 每个定理附带量子计算中的具体应用。

---

## 1. Matrix Bernstein Inequality [F18.9]

### 1.1 Statement

**Theorem** [Tropp, 2012]: 设 $X_1, \ldots, X_n$ 是独立的零均值随机矩阵（$d_1 \times d_2$），满足 $\|X_i\| \leq L$（算子范数）。定义矩阵方差统计量：

$$\sigma^2 = \max\left(\left\|\sum_{i=1}^n \mathbb{E}[X_i X_i^\dagger]\right\|,\; \left\|\sum_{i=1}^n \mathbb{E}[X_i^\dagger X_i]\right\|\right)$$

则：

$$P\left(\left\|\sum_{i=1}^n X_i\right\| \geq t\right) \leq (d_1 + d_2) \cdot \exp\left(-\frac{t^2/2}{\sigma^2 + Lt/3}\right)$$

> 一行解释：矩阵版 Bernstein——算子范数的集中，额外付出维度因子 $(d_1+d_2)$ 的代价。

### 1.2 Proof Sketch

**Key idea**: 利用 Lieb's concavity theorem 和矩阵 Laplace transform。

**Step 1 (Matrix Chernoff method)**: 对矩阵 MGF 应用 Golden-Thompson 不等式：

$$P\left(\lambda_{\max}\left(\sum X_i\right) \geq t\right) \leq \inf_{\theta > 0} e^{-\theta t} \cdot \mathbb{E}\left[\mathrm{tr}\, \exp\left(\theta \sum X_i\right)\right]$$

Golden-Thompson: $\mathrm{tr}\, e^{A+B} \leq \mathrm{tr}(e^A e^B)$ 对 Hermitian $A, B$。

**Step 2 (Iterative conditioning)**: 利用 Lieb's theorem 将乘积结构简化：

$$\mathbb{E}\left[\mathrm{tr}\, \exp\left(\theta \sum_{i=1}^n X_i\right)\right] \leq \mathrm{tr}\, \exp\left(\sum_{i=1}^n \log \mathbb{E}[e^{\theta X_i}]\right)$$

**Step 3 (Scalar bound per matrix)**: 对每个 $\mathbb{E}[e^{\theta X_i}]$，利用 $\|X_i\| \leq L$ 和零均值条件，得到：

$$\mathbb{E}[e^{\theta X_i}] \preceq \exp\left(g(\theta) \cdot \mathbb{E}[X_i^2]\right)$$

其中 $g(\theta)$ 类似标量 Bernstein 中的函数。

**Step 4**: 合并所有项，对 $\theta$ 优化，得到最终界。

**Step 5**: 通过 $\|A\| = \max(\lambda_{\max}(A), \lambda_{\max}(-A))$ 和 union bound 处理双侧。$\square$

### 1.3 Special Cases

**When $L \to 0$ (sub-Gaussian regime)**:

$$P\left(\left\|\sum X_i\right\| \geq t\right) \leq (d_1+d_2) \exp\left(-\frac{t^2}{2\sigma^2}\right)$$

**When $t$ large (sub-exponential regime)**:

$$P\left(\left\|\sum X_i\right\| \geq t\right) \leq (d_1+d_2) \exp\left(-\frac{3t}{2L}\right)$$

> 两个区间的行为与标量 Bernstein [F18.5] 完全对应。

---

## 2. Matrix Chernoff Inequality

### 2.1 Statement

**Theorem** [Tropp, 2012]: 设 $X_1, \ldots, X_n$ 是独立的 $d \times d$ 正半定随机矩阵，$\lambda_{\max}(X_i) \leq R$。设 $\mu_{\min} = \lambda_{\min}(\sum \mathbb{E}[X_i])$，$\mu_{\max} = \lambda_{\max}(\sum \mathbb{E}[X_i])$。则：

**上尾**:
$$P\left(\lambda_{\max}\left(\sum X_i\right) \geq (1+\delta)\mu_{\max}\right) \leq d \cdot \left(\frac{e^\delta}{(1+\delta)^{(1+\delta)}}\right)^{\mu_{\max}/R}$$

**下尾**:
$$P\left(\lambda_{\min}\left(\sum X_i\right) \leq (1-\delta)\mu_{\min}\right) \leq d \cdot \left(\frac{e^{-\delta}}{(1-\delta)^{(1-\delta)}}\right)^{\mu_{\min}/R}$$

> 一行解释：正半定矩阵和的特征值以类似 Chernoff 的速率集中——额外维度因子 $d$。

**When to use**: 随机投影矩阵、协方差估计、量子态估计中正算子求和的集中性。

---

## 3. Matrix Hoeffding Inequality

### 3.1 Statement

**Theorem** [Tropp, 2012]: 设 $X_1, \ldots, X_n$ 是独立的 $d \times d$ Hermitian 随机矩阵，$\mathbb{E}[X_i] = 0$，$X_i^2 \preceq A_i^2$（半正定序意义下）。则：

$$P\left(\lambda_{\max}\left(\sum X_i\right) \geq t\right) \leq d \cdot \exp\left(-\frac{t^2}{8\left\|\sum A_i^2\right\|}\right)$$

> 一行解释：矩阵版 Hoeffding——对 Hermitian 矩阵和的最大特征值的集中。

**When to use**: 当矩阵有已知的半正定上界但不是正半定时。

---

## 4. Applications to Quantum Information

### 4.1 Classical Shadows Sample Complexity (经典阴影样本复杂度)

**Setup** [Huang, Kueng, Preskill, 2020]: 要估计 $M$ 个可观测量 $O_1, \ldots, O_M$ 的期望值 $\mathrm{tr}(O_i \rho)$，精度 $\epsilon$，成功概率 $1-\delta$。

**Random Clifford measurements**: 每次测量产生一个无偏估计 $\hat{o}_i$ of $\mathrm{tr}(O_i \rho)$。

**Sample complexity**: 由 **Matrix Bernstein** [F18.9]，加上对 $M$ 个可观测量的 **union bound** [F18.20]：

$$N = O\left(\frac{\log M}{\epsilon^2} \cdot \max_i \|O_i\|_{\mathrm{shadow}}^2\right)$$

其中 shadow norm $\|O\|_{\mathrm{shadow}}$ 取决于测量方案。

**Proof sketch**:
1. 单个可观测量：$N$ 个独立 shadow 给出估计 $\hat{o}_i = \frac{1}{N}\sum_k \hat{o}_i^{(k)}$
2. 每个 $\hat{o}_i^{(k)}$ 有界（由 shadow norm 控制），零均值
3. 由 Hoeffding [F18.3]: $P(|\hat{o}_i - \mathrm{tr}(O_i\rho)| \geq \epsilon) \leq 2e^{-2N\epsilon^2/\|O_i\|^2}$
4. Union bound [F18.20]: $P(\exists i: |\hat{o}_i - \mathrm{tr}(O_i\rho)| \geq \epsilon) \leq 2M \cdot e^{-2N\epsilon^2/\max\|O_i\|^2}$
5. 设 $\leq \delta$，解 $N$ 得到 $N = O(\log(M/\delta)/\epsilon^2)$

**Median-of-means improvement**: 用 Matrix Bernstein 代替 Hoeffding 可以利用方差信息得到更紧的界。

### 4.2 Quantum State Tomography Bounds (量子态层析界)

**Full tomography**: 估计 $d \times d$ 密度矩阵 $\rho$，在 trace norm 意义下精度 $\epsilon$。

**Sample complexity lower bound** [Haah et al., 2017]: $N = \Omega(d^2/\epsilon^2)$（由 Le Cam [F18.18] 得到）。

**Upper bound**: 压缩感知方法 + **Matrix Bernstein**:
- 随机 Pauli 测量，每次测量产生随机矩阵 $X_k$
- $\rho$ 的估计 $\hat{\rho}$ 通过 $\min \|\hat{\rho}\|_1$ s.t. 测量数据一致
- Matrix Bernstein 给出 RIP 条件成立的概率，需要 $N = O(d \cdot \mathrm{polylog}(d)/\epsilon^2)$

### 4.3 Random Circuit Fidelity Estimation (随机电路保真度估计)

**Setup**: XEB (cross-entropy benchmarking) 中，估计线性 XEB 保真度：

$$F_{\mathrm{XEB}} = 2^n \mathbb{E}_{x \sim p_{\text{ideal}}}[p_{\text{noisy}}(x)] - 1$$

**From samples**: 用 $N$ 个样本 $x_1, \ldots, x_N$ 从噪声电路抽取：

$$\hat{F}_{\mathrm{XEB}} = \frac{2^n}{N} \sum_{k=1}^N p_{\text{ideal}}(x_k) - 1$$

**By Hoeffding**: 因为 $p_{\text{ideal}}(x) \in [0, 1]$（重归一化后），需要 $N = O(4^n/\epsilon^2)$ 个样本。

**Better bound via Bernstein**: 利用 Porter-Thomas 分布的方差 $\mathrm{Var} \approx 1$（而非有界范围 $2^n$），Bernstein 给出 $N = O(1/\epsilon^2)$ 在 $F_{\mathrm{XEB}}$ 尺度上。

---

## 5. Practical Guidelines (使用指南)

### How to Choose the Right Matrix Inequality

```
你的随机矩阵是什么类型？
├── 正半定 → Matrix Chernoff
├── Hermitian、有界 → Matrix Hoeffding
├── 一般矩阵、有界 + 已知方差 → Matrix Bernstein (最常用)
└── 需要最大特征值的精确控制 → 考虑 Matrix Freedman (鞅版)
```

### Dimension Factor

所有矩阵集中不等式都有一个维度因子 $d$（或 $d_1 + d_2$）。这是标量不等式没有的。

**Why**: 本质上是对 $d$ 个特征值方向做了 union bound。

**Can it be improved?**: 有时可以。如果矩阵有特殊结构（如低秩），可以用更精细的工具（如 intrinsic dimension）替代 $d$。

---

## Cross-References (交叉引用)

- **Scalar versions** → [concentration_inequalities.md]: Bernstein, Hoeffding, Chernoff
- **Classical shadows** → [../03_quantum_info_theory/]: Shadow norm definitions
- **State tomography** → [../02_quantum_mechanics/derivations/fidelity_and_trace_distance.md]: Fidelity definition
- **Le Cam lower bound** → [learning_theory.md]: Minimax lower bounds
- **Sub-Gaussian framework** → [concentration_inequalities.md] Section 6: Underlies matrix results
- **Original reference**: Tropp, "User-Friendly Tail Bounds for Sums of Random Matrices", Found. Comput. Math., 2012
