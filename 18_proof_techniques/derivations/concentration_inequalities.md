# Concentration Inequalities: Full Derivations

> 集中不等式完整推导链：Markov → Chebyshev → Chernoff/Hoeffding → Bernstein → McDiarmid → Azuma
> 这是论文理论分析中最常用的工具集——几乎所有"以高概率成立"的声明都源于此。
> 每个定理附带量子计算/ML相关的具体应用示例。

## Primary References

- **[BLM13]** Boucheron, Lugosi, Massart. *Concentration Inequalities: A Nonasymptotic Theory of Independence*. Oxford, 2013. — 综合性现代教材，覆盖本文所有内容
- **[Hoeffding63]** Hoeffding, W. "Probability Inequalities for Sums of Bounded Random Variables." *JASA* 58(301):13-30, 1963. — Hoeffding 不等式和引理的原始论文
- **[McDiarmid89]** McDiarmid, C. "On the Method of Bounded Differences." *Surveys in Combinatorics*, London Math. Soc. Lecture Notes 141:148-188, 1989. — 有界差分法的经典参考
- **[Azuma67]** Azuma, K. "Weighted Sums of Certain Dependent Random Variables." *Tôhoku Math. J.* 19(3):357-367, 1967.
- **[Bennett62]** Bennett, G. "Probability Inequalities for the Sum of Independent Random Variables." *JASA* 57(297):33-45, 1962.
- **[Bernstein46]** Bernstein, S. *The Theory of Probabilities*. 4th ed., Gastehizdat, Moscow, 1946. — 也见 [BLM13, §2.7-2.8]
- **[Chernoff52]** Chernoff, H. "A Measure of Asymptotic Efficiency for Tests of a Hypothesis Based on the Sum of Observations." *Ann. Math. Statist.* 23(4):493-507, 1952.

---

## 1. Markov → Chebyshev → Chernoff Chain

### 1.1 Markov Inequality (马尔可夫不等式) [F18.1] **[BLM13, Theorem 2.1, p.24]**

**Statement**: 若 $X \geq 0$ 且 $\mathbb{E}[X] < \infty$，则对任意 $a > 0$：

$$P(X \geq a) \leq \frac{\mathbb{E}[X]}{a}$$

**Proof**:

$$\mathbb{E}[X] = \int_0^\infty x\, dF(x) \geq \int_a^\infty x\, dF(x) \geq a \int_a^\infty dF(x) = a \cdot P(X \geq a)$$

除以 $a$ 即得。$\square$

> 一行解释：非负随机变量不可能"经常"远超均值——概率被均值/阈值压制。

**When to use**: 作为推导链的起点；当你只知道一阶矩时；证明某个非负量级 $O(1/a)$ 衰减。

---

### 1.2 Chebyshev Inequality (切比雪夫不等式) [F18.2] **[BLM13, §2.1, p.23]**

**Statement**: 若 $\mathbb{E}[X] = \mu$，$\mathrm{Var}(X) = \sigma^2 < \infty$，则：

$$P(|X - \mu| \geq t) \leq \frac{\sigma^2}{t^2}$$

**Proof**: 对非负随机变量 $(X - \mu)^2$ 应用 Markov 不等式：

$$P(|X - \mu| \geq t) = P((X-\mu)^2 \geq t^2) \leq \frac{\mathbb{E}[(X-\mu)^2]}{t^2} = \frac{\sigma^2}{t^2} \quad \square$$

> 一行解释：利用方差给出比 Markov 更紧的双侧尾界——方差小 → 分布更集中。

**When to use**: 证明弱大数定律；当只知道前两阶矩时。缺点：只有多项式衰减 $O(1/t^2)$，比指数衰减弱。

---

### 1.3 Exponential Markov Method / Chernoff Method

**Key idea**: 对 $e^{\lambda X}$（而非 $X$ 或 $X^2$）应用 Markov 不等式，获得指数级衰减。

$$P(X \geq t) = P(e^{\lambda X} \geq e^{\lambda t}) \leq \frac{\mathbb{E}[e^{\lambda X}]}{e^{\lambda t}}, \quad \forall\, \lambda > 0$$

然后对 $\lambda$ 取 $\inf$：

$$P(X \geq t) \leq \inf_{\lambda > 0} e^{-\lambda t} \mathbb{E}[e^{\lambda X}] = \inf_{\lambda > 0} e^{-\lambda t} M_X(\lambda)$$

> 一行解释：所有指数级集中不等式的统一框架——不同的分布假设导致不同的 MGF 上界。

---

### 1.4 Chernoff Bound (Chernoff 界) [F18.4] **[Chernoff52; BLM13, §2.4, p.28-30]**

**Statement (乘法形式)**: 设 $X = \sum_{i=1}^n X_i$，$X_i$ 独立取 $\{0, 1\}$（Bernoulli），$\mu = \mathbb{E}[X]$。则：

**上尾**: $P(X \geq (1+\delta)\mu) \leq \left(\frac{e^\delta}{(1+\delta)^{(1+\delta)}}\right)^\mu$

**下尾**: $P(X \leq (1-\delta)\mu) \leq \left(\frac{e^{-\delta}}{(1-\delta)^{(1-\delta)}}\right)^\mu$

**Proof (上尾)**:

**Step 1**: 对单个 Bernoulli 变量 $X_i$（$P(X_i=1)=p_i$），计算 MGF：

$$\mathbb{E}[e^{\lambda X_i}] = 1 - p_i + p_i e^\lambda = 1 + p_i(e^\lambda - 1) \leq e^{p_i(e^\lambda - 1)}$$

最后一步用了 $1 + x \leq e^x$。

**Step 2**: 由独立性：

$$\mathbb{E}[e^{\lambda X}] = \prod_{i=1}^n \mathbb{E}[e^{\lambda X_i}] \leq \prod_{i=1}^n e^{p_i(e^\lambda - 1)} = e^{\mu(e^\lambda - 1)}$$

**Step 3**: 应用 Chernoff method，设 $t = (1+\delta)\mu$：

$$P(X \geq (1+\delta)\mu) \leq \inf_{\lambda > 0} e^{-\lambda(1+\delta)\mu} \cdot e^{\mu(e^\lambda - 1)}$$

**Step 4**: 对 $\lambda$ 求导令其为零，得 $\lambda^* = \ln(1+\delta)$，代入：

$$P(X \geq (1+\delta)\mu) \leq e^{-\mu[(1+\delta)\ln(1+\delta) - \delta]} = \left(\frac{e^\delta}{(1+\delta)^{(1+\delta)}}\right)^\mu \quad \square$$

**Simplified forms** (实用近似):
- $P(X \geq (1+\delta)\mu) \leq e^{-\mu\delta^2/3}$，当 $0 < \delta \leq 1$
- $P(X \geq (1+\delta)\mu) \leq e^{-\mu\delta/3}$，当 $\delta > 1$ (此时 $\ln(1+\delta) > \delta/3$ 仍成立但更宽松)

> 一行解释：独立 Bernoulli 和的最紧指数尾界——通过优化 MGF 中的 $\lambda$ 得到。

**When to use**: 随机比特/事件计数的精确尾界。量子纠错中：$n$ 个物理比特各独立以概率 $p$ 出错，总错误数超过 $t$ 的概率。

---

## 2. Hoeffding Inequality [F18.3] **[Hoeffding63, Theorem 1-2]**

### 2.1 Hoeffding's Lemma (Hoeffding 引理) **[Hoeffding63, Lemma 1; BLM13, Lemma 2.2, p.25]**

**Statement**: 若 $\mathbb{E}[X] = 0$，$a \leq X \leq b$，则：

$$\mathbb{E}[e^{\lambda X}] \leq \exp\left(\frac{\lambda^2 (b-a)^2}{8}\right)$$

**Proof sketch**:

**Step 1**: 由凸性，对 $X \in [a, b]$：

$$e^{\lambda X} \leq \frac{b - X}{b - a} e^{\lambda a} + \frac{X - a}{b - a} e^{\lambda b}$$

**Step 2**: 取期望（用 $\mathbb{E}[X] = 0$）：

$$\mathbb{E}[e^{\lambda X}] \leq \frac{b}{b-a} e^{\lambda a} - \frac{a}{b-a} e^{\lambda b}$$

**Step 3**: 设 $p = -a/(b-a)$，$u = \lambda(b-a)$，则右边 $= e^{g(u)}$，其中 $g(u) = -pu + \ln(1 - p + pe^u)$。

**Step 4**: 验证 $g(0) = g'(0) = 0$，$g''(u) \leq 1/4$（因为 $g''(u) = \frac{pe^u(1-p+pe^u) - p^2 e^{2u}}{(1-p+pe^u)^2} \leq 1/4$）。

**Step 5**: 由 Taylor 展开 $g(u) \leq u^2/8$，因此 $\mathbb{E}[e^{\lambda X}] \leq e^{\lambda^2(b-a)^2/8}$。$\square$

### 2.2 Hoeffding Inequality

**Statement**: 设 $X_1, \ldots, X_n$ 独立，$X_i \in [a_i, b_i]$，$S_n = \sum X_i$。则：

$$P(S_n - \mathbb{E}[S_n] \geq t) \leq \exp\left(-\frac{2t^2}{\sum_{i=1}^n (b_i - a_i)^2}\right)$$

**Proof**:

$$P(S_n - \mathbb{E}[S_n] \geq t) \leq e^{-\lambda t} \prod_{i=1}^n \mathbb{E}[e^{\lambda(X_i - \mathbb{E}[X_i])}] \leq e^{-\lambda t} \prod_{i=1}^n e^{\lambda^2(b_i-a_i)^2/8}$$

第一步用 Chernoff method + 独立性，第二步用 Hoeffding's Lemma（对中心化变量 $X_i - \mathbb{E}[X_i]$）。

$$= \exp\left(-\lambda t + \frac{\lambda^2}{8}\sum(b_i-a_i)^2\right)$$

对 $\lambda$ 最优化：$\lambda^* = \frac{4t}{\sum(b_i-a_i)^2}$，代入得：

$$P(S_n - \mathbb{E}[S_n] \geq t) \leq \exp\left(-\frac{2t^2}{\sum(b_i-a_i)^2}\right) \quad \square$$

> 一行解释：有界独立随机变量之和以指数速度集中在均值附近——界只依赖区间宽度，不依赖分布细节。

**When to use**: 最常用的集中不等式。当你有独立有界观测（如量子测量二值结果）时，直接给出均值估计的置信区间。

---

## 3. Bernstein Inequality [F18.5] **[Bernstein46; BLM13, §2.7-2.8, pp.35-39]**

### 3.1 Bennett's Inequality **[Bennett62; BLM13, Theorem 2.9, p.35]**

**Statement**: 设 $X_1, \ldots, X_n$ 独立、零均值，$X_i \leq b$，$\sigma^2 = \frac{1}{n}\sum \mathbb{E}[X_i^2]$。则：

$$P\left(\sum X_i \geq t\right) \leq \exp\left(-\frac{n\sigma^2}{b^2} h\left(\frac{bt}{n\sigma^2}\right)\right)$$

其中 $h(u) = (1+u)\ln(1+u) - u$。

### 3.2 Bernstein Inequality (Bennett 的简化)

**Statement**: 在 Bennett 的条件下（$|X_i| \leq b$，$\sum \mathrm{Var}(X_i) = V$）：

$$P\left(\sum X_i \geq t\right) \leq \exp\left(-\frac{t^2/2}{V + bt/3}\right)$$

**Proof sketch**:

**Step 1**: 验证对 $|x| \leq b$：$e^{\lambda x} \leq 1 + \lambda x + \frac{\lambda^2 x^2}{2} \cdot \frac{e^{\lambda b}}{1 + \lambda b}$（这需要一些分析技巧）。

更直接的方法是利用 $h(u) \geq u^2/(2+2u/3)$（对 $u \geq 0$），将 Bennett 不等式简化为 Bernstein。$\square$

**Two regimes** (两个区间的行为):

| 条件 | 主导项 | 行为 | 类比 |
|------|--------|------|------|
| $t \ll V/b$ | $t^2/(2V)$ | Sub-Gaussian（高斯尾） | 类似 Hoeffding |
| $t \gg V/b$ | $3t/(2b)$ | Sub-exponential（指数尾） | 尾部更重 |

> 一行解释：方差自适应的集中不等式——当方差远小于有界范围时，比 Hoeffding 紧得多。

**When to use**: 当随机变量有小方差但大范围时（如稀疏估计器、偶尔有大偏差的测量）。

**Comparison with Hoeffding**:
- Hoeffding: $\exp(-2t^2/\sum(b_i-a_i)^2)$ — 只用区间宽度
- Bernstein: $\exp(-t^2/(2V+2bt/3))$ — 利用方差 $V$
- 当 $V \ll \sum(b_i-a_i)^2$ 时，Bernstein 显著优于 Hoeffding

---

## 4. McDiarmid Inequality [F18.6] **[McDiarmid89, Theorem 3.1; BLM13, Theorem 6.2, p.164]**

**Statement**: 设 $X_1, \ldots, X_n$ 独立，$f: \mathcal{X}^n \to \mathbb{R}$ 满足有界差分条件：

$$\sup_{x_1,\ldots,x_n,x_i'} |f(x_1,\ldots,x_i,\ldots,x_n) - f(x_1,\ldots,x_i',\ldots,x_n)| \leq c_i$$

则：
$$P(f(X_1,\ldots,X_n) - \mathbb{E}[f] \geq t) \leq \exp\left(-\frac{2t^2}{\sum_{i=1}^n c_i^2}\right)$$

**Proof (via Doob martingale + Azuma)**:

**Step 1**: 定义 Doob 鞅：$Z_k = \mathbb{E}[f(X) | X_1, \ldots, X_k]$，$k = 0, 1, \ldots, n$。

- $Z_0 = \mathbb{E}[f]$（常数）
- $Z_n = f(X_1, \ldots, X_n)$
- $\{Z_k\}$ 是关于滤波 $\{\sigma(X_1,\ldots,X_k)\}$ 的鞅

**Step 2**: 验证鞅差有界：$|Z_k - Z_{k-1}| \leq c_k$。

这是因为：
$$Z_k - Z_{k-1} = \mathbb{E}[f | X_1,\ldots,X_k] - \mathbb{E}[f | X_1,\ldots,X_{k-1}]$$

$Z_k$ 只依赖于 $X_k$ 的实现值（其他都已固定或积分掉），而改变 $X_k$ 最多改变 $f$ 的值 $c_k$。

**Step 3**: 关键：Doob 鞅差 $D_k = Z_k - Z_{k-1}$ 的**区间长度**（range）$\leq c_k$（不是 $|D_k| \leq c_k$）。对 Hoeffding 引理，区间长度 $c_k$ 给出 MGF 上界 $e^{\lambda^2 c_k^2/8}$（而非 $e^{\lambda^2 c_k^2/2}$）。

> **Convention Note**: Azuma-Hoeffding（§5）用 $|D_k| \leq c_k$ 即对称界（区间长度 $2c_k$），得到 $\exp(-t^2/(2\sum c_k^2))$。McDiarmid 用区间长度 $\leq c_k$，得到 $\exp(-2t^2/\sum c_k^2)$。两者相差 4 倍不是错误，是假设强度不同 **[BLM13, Remark 6.1, p.165]**。

$$P(f - \mathbb{E}[f] \geq t) = P(Z_n - Z_0 \geq t) \leq \exp\left(-\frac{2t^2}{\sum c_k^2}\right) \quad \square$$

> 一行解释：Hoeffding 不等式从"变量的和"推广到"变量的任意有界影响函数"。

**When to use**: 证明一个复杂统计量（如图上的某个优化目标、解码成功率）集中在均值附近。

### 量子计算应用: QAOA 集中性

考虑 MaxCut QAOA 的目标函数 $C(\gamma, \beta) = \sum_{(i,j) \in E} \frac{1}{2}(1 - \langle Z_i Z_j \rangle)$。

在随机 $d$-正则图上，改变一条边（一个随机选择）最多影响 $C$ 的值 $O(1)$。由 McDiarmid：

$$P(|C - \mathbb{E}[C]| \geq t) \leq 2\exp\left(-\frac{2t^2}{|E| \cdot O(1)}\right) = 2\exp\left(-\Omega(t^2/n)\right)$$

即 QAOA 的期望目标值以 $O(\sqrt{n})$ 的尺度集中。

---

## 5. Azuma-Hoeffding Inequality [F18.7] **[Azuma67; BLM13, Theorem 6.3, p.165]**

**Statement**: 设 $\{M_k\}_{k=0}^n$ 是鞅（或超鞅），$|M_k - M_{k-1}| \leq c_k$。则：

$$P(M_n - M_0 \geq t) \leq \exp\left(-\frac{t^2}{2\sum_{k=1}^n c_k^2}\right)$$

$$P(|M_n - M_0| \geq t) \leq 2\exp\left(-\frac{t^2}{2\sum_{k=1}^n c_k^2}\right)$$

**Proof**:

**Step 1**: 对鞅差 $D_k = M_k - M_{k-1}$ 应用 Chernoff method：

$$P(M_n - M_0 \geq t) = P\left(\sum_{k=1}^n D_k \geq t\right) \leq e^{-\lambda t} \cdot \mathbb{E}\left[\exp\left(\lambda \sum_{k=1}^n D_k\right)\right]$$

**Step 2**: 关键步骤——用条件期望拆解（tower property）：

$$\mathbb{E}\left[e^{\lambda \sum D_k}\right] = \mathbb{E}\left[e^{\lambda \sum_{k=1}^{n-1} D_k} \cdot \mathbb{E}\left[e^{\lambda D_n} \mid \mathcal{F}_{n-1}\right]\right]$$

**Step 3**: 因为 $\mathbb{E}[D_n | \mathcal{F}_{n-1}] = 0$（鞅性）且 $|D_n| \leq c_n$（有界差），由 Hoeffding's Lemma：

$$\mathbb{E}[e^{\lambda D_n} | \mathcal{F}_{n-1}] \leq e^{\lambda^2 c_n^2 / 2}$$

（注意：这里用的是"条件版 Hoeffding's Lemma"，$D_n \in [-c_n, c_n]$，区间宽度 $2c_n$，指数为 $(2c_n)^2/8 = c_n^2/2$。）

**Step 4**: 递归：

$$\mathbb{E}\left[e^{\lambda \sum D_k}\right] \leq e^{\lambda^2 c_n^2/2} \cdot \mathbb{E}\left[e^{\lambda \sum_{k=1}^{n-1} D_k}\right] \leq \cdots \leq \prod_{k=1}^n e^{\lambda^2 c_k^2/2} = e^{\lambda^2 \sum c_k^2 / 2}$$

**Step 5**: 合并并优化 $\lambda$：

$$P(M_n - M_0 \geq t) \leq e^{-\lambda t + \lambda^2 \sum c_k^2/2}$$

取 $\lambda^* = t / \sum c_k^2$：

$$P(M_n - M_0 \geq t) \leq e^{-t^2 / (2\sum c_k^2)} \quad \square$$

> 一行解释：鞅差有界 → 鞅的终值以指数速度集中在初值附近。

**When to use**: 当随机变量有依赖但可构造鞅时（最常见：Doob 鞅用于证明 McDiarmid）。

---

## 6. Sub-Gaussian Framework [F18.8] **[BLM13, §2.5, pp.31-34]**

### 6.1 Definition and Equivalent Characterizations

零均值随机变量 $X$ 是 $\sigma$-sub-Gaussian 的，以下等价（常数不同）：

1. **MGF 条件**: $\mathbb{E}[e^{\lambda X}] \leq e^{\lambda^2 \sigma^2/2}$ for all $\lambda \in \mathbb{R}$
2. **尾概率**: $P(|X| \geq t) \leq 2e^{-t^2/(2\sigma^2)}$ for all $t \geq 0$
3. **矩条件**: $\mathbb{E}[|X|^p]^{1/p} \leq C\sigma\sqrt{p}$ for all $p \geq 1$
4. **Laplace transform 条件**: $\mathbb{E}[e^{\lambda X}] < \infty$ for all $\lambda$ in a neighborhood of 0, with specific growth control

### 6.2 Key Examples

| 分布 | Sub-Gaussian 参数 $\sigma$ |
|------|--------------------------|
| $X \in [a, b]$ 确定性有界 | $\sigma = (b-a)/2$ |
| $X \sim \mathcal{N}(0, \sigma^2)$ | $\sigma = \sigma$ (精确) |
| Rademacher $X \in \{-1, +1\}$ | $\sigma = 1$ |
| 有界鞅差 $|D_i| \leq c_i$ | 每步 $\sigma_i = c_i$ |

### 6.3 Closure Properties

**Property 1 (Sums/独立和)**: 若 $X_1, \ldots, X_n$ 独立，$X_i$ 是 $\sigma_i$-sub-Gaussian，则 $\sum X_i$ 是 $\sqrt{\sum \sigma_i^2}$-sub-Gaussian。

*Proof*: $\mathbb{E}[e^{\lambda \sum X_i}] = \prod \mathbb{E}[e^{\lambda X_i}] \leq \prod e^{\lambda^2 \sigma_i^2/2} = e^{\lambda^2 \sum \sigma_i^2 / 2}$。

**Property 2 (Maximum/最大值)**: 若 $X_1, \ldots, X_n$ 是 $\sigma$-sub-Gaussian（不需要独立），则：

$$\mathbb{E}\left[\max_{1 \leq i \leq n} X_i\right] \leq \sigma\sqrt{2\ln n}$$

*Proof*: 对任意 $\lambda > 0$：
$$e^{\lambda \mathbb{E}[\max X_i]} \leq \mathbb{E}[e^{\lambda \max X_i}] = \mathbb{E}\left[\max_i e^{\lambda X_i}\right] \leq \sum_i \mathbb{E}[e^{\lambda X_i}] \leq n e^{\lambda^2 \sigma^2/2}$$

取对数除以 $\lambda$，再优化 $\lambda = \sqrt{2\ln n}/\sigma$，得 $\mathbb{E}[\max X_i] \leq \sigma\sqrt{2\ln n}$。$\square$

> 一行解释：sub-Gaussian 提供了统一处理"类高斯尾行为"的框架——有界、高斯、Rademacher 都是特例。

**When to use**: 现代高维统计和机器学习理论的基本语言。当你需要把不同来源的随机性（测量噪声、算法随机性）统一处理时。

---

## 7. Sub-Exponential Variables

### 7.1 Definition

零均值 $X$ 是 $(\nu, \alpha)$-sub-exponential 的，如果：

$$\mathbb{E}[e^{\lambda X}] \leq e^{\nu^2 \lambda^2/2}, \quad \forall\, |\lambda| < 1/\alpha$$

**Key relationship**: $X$ sub-Gaussian $\Rightarrow$ $X$ sub-exponential，但反之不成立。

**Key example**: $X \sim \chi^2(1)$ 是 sub-exponential 但不是 sub-Gaussian。

### 7.2 Bernstein Condition

$X$ 满足 Bernstein 条件（参数 $(b, \sigma^2)$）：

$$|\mathbb{E}[X^k]| \leq \frac{k!}{2} \sigma^2 b^{k-2}, \quad k = 2, 3, \ldots$$

这等价于 sub-exponential 性（参数不同但等阶）。Bernstein 不等式 [F18.5] 就是在这个条件下得到的。

---

## 8. Quantum Computing Applications (量子计算中的应用)

### 8.1 Estimating Fidelity from $N$ Shots (从 $N$ 次测量估计保真度)

**Setup**: 量子电路输出态 $\rho$，目标态 $|\psi\rangle$。测量 $N$ 次，每次得到 "correct" (概率 $F$) 或 "wrong" (概率 $1-F$)。

**Goal**: 估计 $F = \langle\psi|\rho|\psi\rangle$。

设 $X_i \in \{0, 1\}$ 为第 $i$ 次测量结果，$\hat{F} = \frac{1}{N}\sum X_i$。

**By Hoeffding** [F18.3]（$X_i \in [0, 1]$，$b-a=1$）：

$$P(|\hat{F} - F| \geq \epsilon) \leq 2\exp(-2N\epsilon^2)$$

要使误差 $|\hat{F} - F| \leq \epsilon$ 以概率 $\geq 1-\delta$ 成立，需要：

$$N \geq \frac{\ln(2/\delta)}{2\epsilon^2}$$

**Example**: $\epsilon = 0.01$，$\delta = 0.05$ → $N \geq 18,445$ shots。

**By Bernstein** [F18.5]（利用 $\mathrm{Var}(X_i) = F(1-F) \leq 1/4$，若已知 $F$ 近似值则方差更小）：

当 $F \approx 0.99$ 时，$\mathrm{Var} \approx 0.0099$，Bernstein 给出更少的所需 shots。

### 8.2 Counting Errors in QEC (量子纠错中的错误计数)

**Setup**: $n$ 个物理量子比特，每个独立以概率 $p$ 出错。总错误数 $X = \sum X_i$，$\mu = np$。

纠错码能纠正 $\leq t$ 个错误。问：$P(X > t) = ?$

**By Chernoff** [F18.4]（$\delta = t/\mu - 1$）：

$$P(X > t) \leq \exp\left(-\frac{np \cdot (t/(np) - 1)^2}{3}\right) \quad (\text{when } t/np - 1 \leq 1)$$

**Example**: $n = 1000$，$p = 0.001$，$t = 5$（码距 $d=11$ 的 surface code 可纠 5 个错误）：
$\mu = 1$，$P(X > 5) \leq$ Chernoff bound gives exponentially small probability。

### 8.3 QAOA Concentration on Random Graphs

见上面 McDiarmid 应用小节。核心结论：QAOA 在随机正则图上的目标函数以 $O(\sqrt{n})$ 尺度集中。这意味着 QAOA 的"典型"性能接近平均性能。

---

## Cross-References (交叉引用)

- **Matrix versions** → [matrix_concentration.md]: Matrix Bernstein, Matrix Chernoff
- **Application to learning** → [learning_theory.md]: VC dim, Rademacher bounds use Hoeffding/McDiarmid
- **Convergence analysis** → [convergence_methods.md]: Coupling + concentration
- **Quantum-specific** → [quantum_proof_toolkit.md]: Quantum union bound uses similar techniques
- **Classical shadows** → [../03_quantum_info_theory/derivations/]: Sample complexity via matrix concentration
- **Diffusion model convergence** → [../11_ml_theory/derivations/diffusion_models_math.md]: Uses sub-Gaussian framework
- **QEC threshold** → [../04_quantum_error_correction/derivations/]: Error counting uses Chernoff bounds
