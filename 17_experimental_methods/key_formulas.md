# Chapter 17: Experimental Methods - Key Formulas

> 实验方法学核心公式速查表。用于论文实验部分的统计检验、置信区间、效应量计算。
> 这些公式偏应用而非深层理论，但在论文审稿中经常被要求。

---

## 基本估计量

### F17.1: Statistical Fidelity Estimation (保真度的统计估计)

$$\hat{F} = \frac{n_{\text{success}}}{n_{\text{shots}}}, \qquad \text{Var}(\hat{F}) = \frac{\hat{F}(1-\hat{F})}{n_{\text{shots}}}$$

在量子实验中，保真度通常通过重复测量（shots）来估计。每次测量的结果是二值的（成功/失败），因此 $\hat{F}$ 服从二项分布 $B(n_{\text{shots}}, F_{\text{true}})$。标准误差为 $\text{SE} = \sqrt{\hat{F}(1-\hat{F})/n_{\text{shots}}}$。

**注意**: 这是最简单的频率估计。当 $\hat{F}$ 接近 0 或 1 时，正态近似不准确，应使用 Wilson 区间（F17.2）或 Bayesian 方法（F17.9）。

**常见错误**: 很多量子计算论文只报告 $\hat{F}$ 而不报告误差棒。审稿人越来越关注这个问题。

**Source**: 基础统计学 | 量子实验通用做法

---

### F17.2: Wilson Score Confidence Interval (Wilson 置信区间)

$$\hat{F}_{\text{Wilson}} = \frac{\hat{F} + \frac{z^2}{2n}}{1 + \frac{z^2}{n}}, \qquad w = \frac{z}{1 + z^2/n}\sqrt{\frac{\hat{F}(1-\hat{F})}{n} + \frac{z^2}{4n^2}}$$

$$\text{CI}_{\text{Wilson}} = \left[\hat{F}_{\text{Wilson}} - w, \;\hat{F}_{\text{Wilson}} + w\right]$$

其中 $z = z_{1-\alpha/2}$ 是标准正态分布的分位数（95% CI 时 $z = 1.96$），$n = n_{\text{shots}}$。

**为什么用 Wilson 而非 Wald**: Wald 区间（$\hat{F} \pm z\sqrt{\hat{F}(1-\hat{F})/n}$）在 $\hat{F}$ 接近 0 或 1 时表现很差（区间可能超出 $[0,1]$）。Wilson 区间在所有 $\hat{F}$ 值下都表现良好，是二项比例估计的推荐方法。

**Python**: `from statsmodels.stats.proportion import proportion_confint; proportion_confint(n_success, n_shots, method='wilson')`

**Source**: Wilson (1927), JASA | Brown, Cai & DasGupta (2001), Statistical Science

---

## 假设检验

### F17.3: Paired t-test (配对 t 检验)

$$t = \frac{\bar{d}}{s_d / \sqrt{n}}, \qquad \bar{d} = \frac{1}{n}\sum_{i=1}^n d_i, \qquad s_d = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (d_i - \bar{d})^2}$$

其中 $d_i = x_i^{(A)} - x_i^{(B)}$ 是第 $i$ 个测试实例上方法 A 和方法 B 的性能差异。$n$ 是测试实例数（不是 shots 数）。$t$ 服从自由度 $\nu = n-1$ 的 t 分布。

**使用条件**: (1) 差值 $d_i$ 近似正态分布（$n \geq 30$ 时由 CLT 保证）; (2) 配对数据（同一测试实例上的两个方法）。

**适用场景**: 比较两种编译方法在同一组电路上的门数/深度差异；比较两种解码器在同一组综合征上的逻辑错误率。

**Python**: `from scipy.stats import ttest_rel; t, p = ttest_rel(method_a, method_b)`

**Source**: Student (1908) | 基础统计学教材

---

### F17.4: Wilcoxon Signed-Rank Test (Wilcoxon 符号秩检验)

$$W = \sum_{i: d_i > 0} R_i, \qquad \text{or} \quad W^{-} = \sum_{i: d_i < 0} R_i$$

其中 $R_i$ 是 $|d_i|$ 在所有非零 $|d_j|$ 中的秩。检验统计量为 $W^{+}$ 和 $W^{-}$ 中较小者。当 $n$ 较大时，$W$ 近似正态：

$$z = \frac{W - n(n+1)/4}{\sqrt{n(n+1)(2n+1)/24}}$$

**使用条件**: 配对数据，不要求正态分布，但要求差值分布关于零对称。

**何时用这个而非 t 检验**: (1) 样本量小（$n < 30$）且差值非正态; (2) 数据含异常值; (3) 数据是有序的但非连续的。在量子实验中，当测试电路数量少（如只有5-10种电路规模）时推荐使用。

**Python**: `from scipy.stats import wilcoxon; stat, p = wilcoxon(method_a, method_b)`

**Source**: Wilcoxon (1945) | Biometrics Bulletin

---

### F17.5: Effect Size - Cohen's d (效应量)

$$d = \frac{\bar{x}_A - \bar{x}_B}{s_p}, \qquad s_p = \sqrt{\frac{(n_A-1)s_A^2 + (n_B-1)s_B^2}{n_A + n_B - 2}}$$

对于配对设计：$d = \bar{d} / s_d$。

| $|d|$ 范围 | 解释 |
|-----------|------|
| $< 0.2$ | 极小效应 (negligible) |
| $0.2$--$0.5$ | 小效应 (small) |
| $0.5$--$0.8$ | 中等效应 (medium) |
| $> 0.8$ | 大效应 (large) |

**为什么要报告效应量**: p 值只告诉你"差异是否统计显著"，不告诉你"差异有多大"。当 $n$ 很大时，即使微不足道的差异也能达到统计显著。APA (American Psychological Association) 要求同时报告 p 值和效应量。

**Source**: Cohen (1988), Statistical Power Analysis for the Behavioral Sciences

---

## 误差分析

### F17.6: Monte Carlo Sampling Error (蒙特卡洛采样误差)

$$\text{SE}(\hat{\mu}) = \frac{\sigma}{\sqrt{N}}, \qquad \text{CI}_{95\%} = \hat{\mu} \pm 1.96 \cdot \frac{\sigma}{\sqrt{N}}$$

其中 $\hat{\mu} = \frac{1}{N}\sum_{i=1}^N x_i$ 是 $N$ 次独立采样的均值，$\sigma$ 是总体标准差（通常用样本标准差 $s$ 估计）。

**实际意义**: 如果跑了 $N=10$ 个随机种子，每个种子得到一个最终性能值 $x_i$，则报告 $\hat{\mu} \pm s/\sqrt{N}$。要将误差棒缩小一半，需要 $4\times$ 的种子数。

**常见问题**: 很多 ML 论文只跑 3 个种子，误差棒很大。审稿人可能要求更多种子。推荐最少 5 个，最好 10 个。

**Source**: 基础概率论 (大数定律 + 中心极限定理)

---

### F17.7: Bootstrap Confidence Interval (Bootstrap 置信区间)

算法步骤：
1. 从原始数据 $\{x_1, \ldots, x_n\}$ 有放回抽样 $n$ 个点，计算统计量 $\hat{\theta}^*_b$
2. 重复 $B$ 次（通常 $B = 10000$）
3. Percentile 方法：$\text{CI}_{95\%} = [\hat{\theta}^*_{(0.025)}, \hat{\theta}^*_{(0.975)}]$

BCa (bias-corrected and accelerated) 修正版：

$$\text{CI}_{\text{BCa}} = \left[\hat{\theta}^*_{(\alpha_1)}, \hat{\theta}^*_{(\alpha_2)}\right], \qquad \alpha_{1,2} = \Phi\left(\hat{z}_0 + \frac{\hat{z}_0 + z_{\alpha/2}}{1 - \hat{a}(\hat{z}_0 + z_{\alpha/2})}\right)$$

其中 $\hat{z}_0$ 是偏差修正项，$\hat{a}$ 是加速项。

**何时使用**: (1) 不知道统计量的理论分布时; (2) 统计量比较复杂（如两个保真度的差值的中位数）; (3) 样本量小时。Bootstrap 几乎没有使用限制，是万能的置信区间方法。

**Python**: `from scipy.stats import bootstrap; res = bootstrap((data,), np.mean, confidence_level=0.95, method='BCa')`

**Source**: Efron (1979), Annals of Statistics | Efron & Tibshirani (1993), An Introduction to the Bootstrap

---

### F17.8: Hypergeometric Test (超几何检验)

$$P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$$

其中 $N$ 是总体大小，$K$ 是总体中的成功数，$n$ 是抽样大小，$k$ 是样本中的成功数。

**适用场景**: 比较两种方法在有限测试集上的成功率，特别是当测试集较小且不能独立采样时。例如：在 $N = 100$ 个测试电路中，方法 A 成功了 $K = 70$ 个，从中随机选 $n = 20$ 个看方法 B 的表现。

**与二项检验的区别**: 二项检验假设独立采样（有放回），超几何检验适用于无放回采样（有限总体）。当 $N \gg n$ 时两者近似相等。

**Python**: `from scipy.stats import hypergeom; p = hypergeom.sf(k-1, N, K, n)`

**Source**: Fisher (1935) | 基础组合概率

---

### F17.9: Bayesian Fidelity Estimation (贝叶斯保真度估计)

先验：$F \sim \text{Beta}(\alpha_0, \beta_0)$（通常取无信息先验 $\alpha_0 = \beta_0 = 1$，即均匀分布）

后验（给定 $k$ 次成功，$n$ 次总尝试）：

$$F \mid k, n \sim \text{Beta}(\alpha_0 + k, \;\beta_0 + n - k)$$

$$\hat{F}_{\text{Bayes}} = \frac{\alpha_0 + k}{\alpha_0 + \beta_0 + n}, \qquad \text{Var}(F \mid k,n) = \frac{(\alpha_0+k)(\beta_0+n-k)}{(\alpha_0+\beta_0+n)^2(\alpha_0+\beta_0+n+1)}$$

95% 可信区间（credible interval）：取 Beta 分布的 2.5% 和 97.5% 分位数。

**优势**: (1) 当 shots 很少时（如 $n = 100$），贝叶斯方法比频率方法更稳健; (2) 可以自然地融合先验信息（如校准数据）; (3) 可信区间的解释比置信区间更直观（"F 有 95% 的概率落在此区间内"）。

**Python**: `from scipy.stats import beta; lo, hi = beta.ppf([0.025, 0.975], alpha0+k, beta0+n-k)`

**Source**: Blume-Kohout (2010), New J. Phys. | Granade et al. (2016), New J. Phys.

---

## 多重比较

### F17.10: Multiple Hypothesis Correction (多重假设检验校正)

**Bonferroni 校正**（最保守）：

$$\alpha_{\text{adj}} = \frac{\alpha}{m}, \qquad \text{拒绝 } H_i \text{ 当 } p_i < \frac{\alpha}{m}$$

其中 $m$ 是检验次数。

**Holm-Bonferroni 校正**（逐步法，比 Bonferroni 更强）：

1. 将 $p$ 值从小到大排序：$p_{(1)} \leq p_{(2)} \leq \cdots \leq p_{(m)}$
2. 找到最小的 $k$ 使得 $p_{(k)} > \frac{\alpha}{m - k + 1}$
3. 拒绝 $H_{(1)}, \ldots, H_{(k-1)}$，不拒绝 $H_{(k)}, \ldots, H_{(m)}$

**Benjamini-Hochberg (BH) FDR 控制**（控制假发现率而非族错误率）：

1. 将 $p$ 值从小到大排序
2. 找到最大的 $k$ 使得 $p_{(k)} \leq \frac{k}{m} \alpha$
3. 拒绝 $H_{(1)}, \ldots, H_{(k)}$

**选择指南**:
- 比较 2-3 种方法：可能不需要校正，但应说明
- 比较 4-10 种方法：用 Holm-Bonferroni
- 大规模筛选（如超参数搜索）：用 BH-FDR
- 比较大量电路实例上的单个方法对：通常不需要多重校正（这不是多重假设检验）

**Python**: `from statsmodels.stats.multitest import multipletests; reject, pvals_adj, _, _ = multipletests(pvals, method='holm')`

**Source**: Bonferroni (1936) | Holm (1979), Scandinavian J. Statistics | Benjamini & Hochberg (1995), JRSS-B

---

## 公式速查表

| ID | 公式名称 | 适用场景 | Python 函数 |
|----|---------|---------|-------------|
| F17.1 | 保真度统计估计 | 量子实验基本报告 | 手动计算 |
| F17.2 | Wilson 置信区间 | 二项比例的 CI | `proportion_confint(..., method='wilson')` |
| F17.3 | 配对 t 检验 | 两方法配对比较 | `scipy.stats.ttest_rel` |
| F17.4 | Wilcoxon 符号秩 | 小样本/非正态配对比较 | `scipy.stats.wilcoxon` |
| F17.5 | Cohen's d | 效应量报告 | 手动计算 |
| F17.6 | MC 采样误差 | 多种子实验误差棒 | 手动计算 |
| F17.7 | Bootstrap CI | 万能 CI 方法 | `scipy.stats.bootstrap` |
| F17.8 | 超几何检验 | 有限总体成功率比较 | `scipy.stats.hypergeom` |
| F17.9 | 贝叶斯保真度估计 | 少量 shots 时的保真度 | `scipy.stats.beta` |
| F17.10 | 多重比较校正 | 比较多种方法 | `statsmodels.stats.multitest.multipletests` |
