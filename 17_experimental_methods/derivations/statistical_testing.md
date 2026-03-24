# Statistical Testing for Quantum Computing & ML Papers

> 统计检验实用指南：写论文实验部分时如何选择和报告统计检验。
> 本文不追求数学深度，而是给出可操作的决策流程。

---

## 1. 参数检验 vs 非参数检验

### 决策树

```
你的数据满足正态假设吗？
├── 是（或 n >= 30，由 CLT 保证） → 参数检验
│   ├── 两组配对数据 → 配对 t 检验 [F17.3]
│   ├── 两组独立数据 → 独立 t 检验
│   └── 多组数据 → 单因素 ANOVA + post-hoc (Tukey HSD)
│
└── 否（小样本、有异常值、明显偏态） → 非参数检验
    ├── 两组配对数据 → Wilcoxon signed-rank [F17.4]
    ├── 两组独立数据 → Mann-Whitney U
    └── 多组数据 → Friedman test + post-hoc (Nemenyi)
```

### 量子计算论文中的典型情况

| 场景 | 数据特点 | 推荐检验 |
|------|---------|---------|
| 比较两种编译器在 100 个随机电路上的 CNOT 数 | 配对、大样本、近似正态 | 配对 t 检验 |
| 比较两种解码器在 5 种码距上的逻辑错误率 | 配对、极小样本 | Wilcoxon signed-rank |
| 比较 10 个种子的 ML 训练结果 | 配对（同种子同数据）、中等样本 | 配对 t 检验（如正态）或 Wilcoxon |
| 比较 3 种路由方法在 50 个电路上的 SWAP 数 | 配对、多组 | 重复测量 ANOVA 或 Friedman |

---

## 2. 配对 vs 非配对比较

### 配对设计（Paired Design）

**定义**: 同一测试实例上比较两种方法。

**举例**:
- 同一个量子电路分别用方法 A 和方法 B 编译，比较门数
- 同一组 syndrome 数据分别用解码器 A 和解码器 B 解码，比较成功率
- 同一个随机种子分别训练模型 A 和模型 B，比较最终 loss

**优势**: 消除了实例间差异的干扰。如果电路 1 本身就比电路 2 难编译，配对设计自动控制了这个变量。

**统计效力**: 配对设计通常比非配对设计有更高的统计效力（更容易检测到真实差异），因为方差更小。

### 非配对设计（Unpaired Design）

**定义**: 两组数据来自不同的实例。

**举例**:
- 方法 A 在芯片 X 上跑了 100 个电路，方法 B 在芯片 Y 上跑了 100 个电路（注意：这通常是不好的实验设计）
- 方法 A 和 B 用不同的随机电路集测试

**建议**: 在量子计算论文中，几乎总是应该使用配对设计。如果你发现自己在用非配对检验，请反思实验设计是否有问题。

---

## 3. 多重比较校正 (Multiple Comparison Correction)

### 什么时候需要校正？

**需要校正的情况**:
- 比较 $m \geq 3$ 种方法的所有配对（共 $\binom{m}{2}$ 次比较）
- 在多个数据集上分别检验同一假设
- 超参数搜索后声称最优

**不需要校正的情况**:
- 只比较两种方法（只有一次检验）
- 在同一数据集上测试同一方法在不同规模下的表现（这是一个趋势，不是多次独立检验）
- 预先指定的比较（而非事后挑选）

### 校正方法选择

| 方法 | 控制目标 | 严格程度 | 适用场景 |
|------|---------|---------|---------|
| Bonferroni | FWER | 最严格 | 比较次数少（$m \leq 5$），要求强控制 |
| Holm-Bonferroni | FWER | 中等 | **推荐默认使用**，比 Bonferroni 强且同样简单 |
| Benjamini-Hochberg | FDR | 较宽松 | 大量比较（$m > 10$），允许少量假阳性 |

### Python 实现

```python
from statsmodels.stats.multitest import multipletests
import numpy as np

# 假设你做了 6 次配对 t 检验，得到 6 个 p 值
p_values = np.array([0.003, 0.012, 0.045, 0.067, 0.23, 0.89])

# Holm-Bonferroni 校正
reject, p_adj, _, _ = multipletests(p_values, alpha=0.05, method='holm')
print("Holm-adjusted p-values:", p_adj)
print("Reject H0:", reject)
# 输出示例: reject = [True, True, False, False, False, False]
```

---

## 4. 报告标准

### 必须报告的内容

每个实验结果都应包含：

1. **中心趋势**: 均值（mean）或中位数（median）
2. **变异度**: 标准差（std）或四分位距（IQR）
3. **置信区间**: 95% CI（最好用 bootstrap 或 Wilson）
4. **样本量**: $n$（测试实例数）和种子数
5. **如果做了假设检验**: p 值、检验方法、效应量

### 正确格式

```
# 好的写法
"Method A achieves a fidelity of 0.923 ± 0.015 (mean ± std, n=50 circuits,
1000 shots each), compared to 0.891 ± 0.021 for Method B. The difference is
statistically significant (paired t-test, t=4.32, p=0.0001, Cohen's d=1.68)."

# 差的写法
"Method A achieves 92.3% fidelity, outperforming Method B's 89.1%."
# 问题: 没有误差棒、没有样本量、没有统计检验
```

### 表格模板

```latex
\begin{table}[h]
\centering
\caption{Comparison of compilation methods on random circuits.}
\begin{tabular}{lccc}
\toprule
Method & CNOT count & Depth & Fidelity \\
\midrule
Random   & $245.3 \pm 32.1$ & $89.7 \pm 12.3$ & $0.712 \pm 0.045$ \\
SABRE    & $198.5 \pm 28.7$ & $72.4 \pm 10.8$ & $0.834 \pm 0.038$ \\
Ours     & $\mathbf{172.1 \pm 25.3}$ & $\mathbf{63.2 \pm 9.5}$ & $\mathbf{0.891 \pm 0.031}$ \\
\midrule
$p$-value (Ours vs SABRE) & $< 0.001$ & $< 0.001$ & $< 0.001$ \\
Cohen's $d$ & $0.97$ & $0.91$ & $1.65$ \\
\bottomrule
\end{tabular}
\end{table}
```

---

## 5. 量子计算论文中的常见统计错误

### 错误 1: 伪重复 (Pseudo-replication)

**问题**: 把 1000 shots 当作 1000 个独立样本来做统计检验。

**为什么错**: 1000 shots 只是对单个电路的单次实验的重复测量。它们给出了该电路在该时刻该芯片上的保真度估计的精度——但这不是你想比较的。你想比较的是方法在不同电路上的表现。

**正确做法**: 样本单位是电路（或测试实例），不是 shot。如果你在 50 个电路上测试了两种方法，$n = 50$，不是 $50 \times 1000 = 50000$。

### 错误 2: 没有置信区间

**问题**: 只报告均值，不报告任何变异度指标。

**为什么错**: 没有误差棒的数字没有意义。$92.3\%$ 可能意味着所有电路都在 $91\%$--$93\%$ 之间，也可能意味着一半在 $100\%$ 一半在 $85\%$。

### 错误 3: Cherry-picking 种子

**问题**: 跑了 20 个种子，只报告最好的 5 个。

**为什么错**: 这是 p-hacking 的一种形式。如果你跑了 20 个种子，就报告 20 个种子的结果。

**灰色地带**: 如果有个别种子明显训练失败（如 loss 爆炸），可以排除，但必须在论文中说明排除了多少个以及排除标准。

### 错误 4: 不恰当的显著性声明

**问题**: "Our method significantly outperforms the baseline"——但没有统计检验。

**为什么错**: "significant" 在科学论文中有特定含义（$p < 0.05$）。如果没有做检验，用 "substantially" 或 "notably" 等非统计术语。

### 错误 5: 混淆统计显著性和实际显著性

**问题**: $p < 0.001$，所以我们的方法好很多。

**为什么错**: 当 $n$ 很大时，即使 0.1% 的差异也可以达到 $p < 0.001$。必须同时报告效应量 [F17.5]。

---

## 6. 需要多少 Shots/Seeds？

### Shot 数量估计

对于保真度估计，给定目标精度 $\epsilon$ 和置信水平 $1-\alpha$：

$$n_{\text{shots}} \geq \frac{z_{1-\alpha/2}^2 \cdot F(1-F)}{\epsilon^2}$$

| 目标精度 $\epsilon$ | $F \approx 0.9$ | $F \approx 0.5$ |
|--------------------|-----------------|-----------------|
| $\pm 0.01$ | 3,458 shots | 9,604 shots |
| $\pm 0.02$ | 865 shots | 2,401 shots |
| $\pm 0.05$ | 139 shots | 385 shots |

**实践建议**: 大多数量子实验用 1000--10000 shots。如果保真度接近 1（如 QEC 逻辑错误率 $< 0.01$），需要更多 shots。

### 种子数量估计

对于 ML 实验，想要检测效应量 $d$ 的差异，配对 t 检验所需种子数：

$$n_{\text{seeds}} \geq \left(\frac{z_{1-\alpha/2} + z_{1-\beta}}{d}\right)^2$$

| 效应量 $d$ | Power = 0.8 | Power = 0.9 |
|-----------|-------------|-------------|
| 大 ($d = 0.8$) | 13 seeds | 17 seeds |
| 中 ($d = 0.5$) | 34 seeds | 44 seeds |
| 小 ($d = 0.2$) | 199 seeds | 264 seeds |

**实践建议**:
- 如果你的方法改进很大（大效应量）：5--10 个种子足够
- 如果改进中等：至少 10--20 个种子
- 如果改进微小但重要：可能需要 30+ 个种子（考虑是否值得声称）
- **最低标准**: 至少 3 个种子（但审稿人可能要求更多）
- **推荐标准**: 5--10 个种子，是发表质量的合理选择
