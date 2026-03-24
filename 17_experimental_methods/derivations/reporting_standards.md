# Reporting Standards for Quantum Computing & ML Papers

> 论文实验结果的报告规范。如何写出让审稿人满意的实验部分。
> 包含保真度、编译结果、ML结果的报告模板，以及提交前自查清单。

---

## 1. 保真度结果的报告 (Reporting Fidelity)

### 必须包含的信息

| 项目 | 说明 | 示例 |
|------|------|------|
| 保真度值 | 均值 | $F = 0.923$ |
| 误差棒 | 标准差或 CI | $\pm 0.015$ (std) 或 $[0.908, 0.938]$ (95% CI) |
| Shot 数量 | 每个电路的 shots | 1000 shots |
| 电路数量 | 测试集大小 | 50 random circuits |
| 保真度类型 | 什么保真度？ | process fidelity / state fidelity / gate fidelity |
| 读出缓解 | 是否做了？ | with/without readout error mitigation |

### 推荐写法

**仿真实验**:
```
"We evaluate on 100 random Clifford circuits with n = {10, 20, 50} qubits and
depth d = {10, 20, 50}. For each (n, d) configuration, we generate 100 random
instances. The process fidelity is estimated via 10,000 shots per circuit under
a depolarizing noise model with single-qubit error rate p1 = 0.001 and
two-qubit error rate p2 = 0.01. Results are reported as mean ± std over the
100 instances."
```

**硬件实验**:
```
"Hardware experiments are performed on the Quafu ScQ-P136 superconducting
processor (136 qubits, median T1 = 45 μs, median CX error = 0.8%, calibrated
on 2026-03-15). We use a linear chain of 20 qubits (q12-q31) with average
CX fidelity 99.1%. Each circuit is executed with 4,000 shots. Readout error
mitigation is applied using the M3 method. We report state fidelity estimated
from the output distribution."
```

### 保真度类型说明

| 类型 | 定义 | 适用场景 |
|------|------|---------|
| State fidelity | $F = \langle \psi_{\text{ideal}} | \rho_{\text{exp}} | \psi_{\text{ideal}} \rangle$ | 输出状态与理想态的比较 |
| Process fidelity | $F_{\text{proc}} = \text{Tr}[\chi_{\text{ideal}} \chi_{\text{exp}}]$ | 量子过程的比较 |
| Average gate fidelity | $\bar{F} = \frac{d \cdot F_{\text{proc}} + 1}{d + 1}$ | 单个门的质量 |
| Heavy output probability | $\Pr[\text{heavy output}]$ | Google quantum supremacy 风格 |

**务必说清楚你用的是哪种保真度！** 不同定义的数值差别可以很大。

---

## 2. 编译结果的报告 (Reporting Compilation Results)

### 关键指标

| 指标 | 含义 | 越小越好? |
|------|------|---------|
| CNOT count (或 CX count) | 双量子比特门数量 | 是 |
| Total gate count | 所有门的数量 | 是 |
| Circuit depth | 电路深度（并行层数） | 是 |
| SWAP count | 插入的 SWAP 门数量 | 是 |
| Compilation time | 编译耗时 | 通常是（但有权衡） |

### 表格模板

```latex
\begin{table*}[t]
\centering
\caption{Compilation results on QUEKO benchmark circuits (mean $\pm$ std over
100 instances). Best results in \textbf{bold}. ``Time'' is wall-clock compilation
time in seconds.}
\label{tab:compilation}
\begin{tabular}{l|ccc|ccc|c}
\toprule
\multirow{2}{*}{Method} & \multicolumn{3}{c|}{20 qubits} & \multicolumn{3}{c|}{50 qubits} & \multirow{2}{*}{Time (s)} \\
 & CX $\downarrow$ & Depth $\downarrow$ & SWAP $\downarrow$ & CX $\downarrow$ & Depth $\downarrow$ & SWAP $\downarrow$ & \\
\midrule
Qiskit L3  & $125 \pm 18$ & $67 \pm 12$ & $32 \pm 8$ & $410 \pm 52$ & $198 \pm 31$ & $105 \pm 24$ & 0.3 \\
SABRE      & $112 \pm 15$ & $58 \pm 10$ & $26 \pm 7$ & $378 \pm 48$ & $175 \pm 28$ & $89 \pm 21$ & 0.5 \\
t$|$ket$>$ & $108 \pm 14$ & $55 \pm 9$  & $24 \pm 6$ & $362 \pm 45$ & $168 \pm 26$ & $82 \pm 19$ & 1.2 \\
\midrule
Ours       & $\mathbf{98 \pm 12}$ & $\mathbf{48 \pm 8}$ & $\mathbf{19 \pm 5}$
           & $\mathbf{335 \pm 41}$ & $\mathbf{152 \pm 23}$ & $\mathbf{71 \pm 16}$ & 2.8 \\
\bottomrule
\end{tabular}
\end{table*}
```

### 注意事项

- **指定目标芯片拓扑**: "compiled to IBM Eagle (heavy-hex, 127 qubits)" 或 "compiled to Quafu ScQ-P136 (grid-like, 136 qubits)"
- **指定优化级别**: 如使用 Qiskit，注明 `optimization_level`
- **编译时间**: 如果你的方法慢但质量好，必须讨论 time-quality tradeoff
- **统计检验**: 如果声称显著优于基线，在表格下方注明 p 值

---

## 3. ML 结果的报告 (Reporting ML Results)

### 标准格式

```
"We train each model with 5 random seeds {42, 123, 456, 789, 1024} and
report mean ± standard deviation. Training uses Adam optimizer with learning
rate 1e-3, batch size 64, for 200 epochs on a single NVIDIA RTX PRO 6000
(98 GB). Training takes approximately 4 hours per seed."
```

### 必须报告的超参数

**模型相关**:
- 架构细节（层数、隐藏维度、注意力头数等）
- 参数总量
- 特殊设计（如果有）

**训练相关**:
- 优化器及其参数（学习率、weight decay、momentum 等）
- 学习率调度（warmup、cosine decay 等）
- Batch size
- 训练 epochs/steps
- 早停策略（如果有）
- 正则化（dropout、label smoothing 等）

**数据相关**:
- 训练/验证/测试集划分
- 数据增强（如果有）
- 数据预处理

### 超参数表模板

```latex
\begin{table}[h]
\centering
\caption{Hyperparameters.}
\begin{tabular}{ll}
\toprule
Hyperparameter & Value \\
\midrule
Hidden dimension & 256 \\
Number of layers & 6 \\
Attention heads & 8 \\
Learning rate & $1 \times 10^{-3}$ \\
LR scheduler & Cosine decay \\
Weight decay & $1 \times 10^{-4}$ \\
Batch size & 64 \\
Epochs & 200 \\
Optimizer & Adam ($\beta_1=0.9$, $\beta_2=0.999$) \\
Dropout & 0.1 \\
Random seeds & $\{42, 123, 456, 789, 1024\}$ \\
\bottomrule
\end{tabular}
\end{table}
```

---

## 4. 表格 vs 图表：何时用哪种？

### 决策指南

| 用表格 | 用图表 |
|-------|-------|
| 精确数字很重要 | 趋势/模式更重要 |
| 比较 2-5 种方法在 2-5 个指标上 | Scaling behavior（连续变化） |
| 数据点少（$< 20$ 个数字） | 数据点多（$> 20$） |
| 消融实验 | 训练曲线 |
| 最终性能对比 | 性能 vs 参数/时间的权衡 |

### 图表最佳实践

**误差棒/误差带**:
```python
# 误差棒 (离散点)
ax.errorbar(x, y_mean, yerr=y_std, marker='o', capsize=3)

# 误差带 (连续曲线)
ax.plot(x, y_mean)
ax.fill_between(x, y_mean - y_std, y_mean + y_std, alpha=0.2)
```

**字体大小**: 确保图表中的文字在论文中印刷后仍然可读。建议：
- 坐标轴标签: 至少 12pt
- 刻度标签: 至少 10pt
- 图例: 至少 10pt
- 标题: 通常不需要（用 caption 代替）

**颜色**: 考虑色盲友好的配色方案。推荐 matplotlib 的 `tab10` 或 `Set2`。不要只用颜色区分——同时用不同的 marker 形状和线型。

**保存格式**: PDF（矢量图）用于线图，PNG（300+ dpi）用于热力图/密度图。

---

## 5. 统计显著性声明

### 什么时候可以说 "significantly better"？

```
检查清单:
□ 做了适当的统计检验？
□ p < 0.05（或更严格的阈值）？
□ 报告了具体的 p 值（不只是 "p < 0.05"）？
□ 多重比较时做了校正 [F17.10]？
□ 效应量 [F17.5] 有实际意义？
□ 样本量足够？

全部满足 → 可以说 "significantly"
任一不满足 → 改用 "substantially", "notably", "consistently" 等
```

### 报告模板

**有统计检验时**:
```
"Our method significantly outperforms SABRE on CNOT count reduction
(paired t-test, t(99) = 5.23, p < 0.001, Cohen's d = 1.12)."
```

**没有统计检验时**:
```
"Our method consistently reduces CNOT count compared to SABRE across all
tested circuit sizes (average reduction: 12.3%)."
```

---

## 6. 负面结果和诚实报告

### 什么时候你的方法不是最好的？

在某些设置下你的方法可能不如基线，这是正常的。诚实报告这些情况会：
1. **增加可信度**: 审稿人更信任坦诚的论文
2. **帮助读者**: 他们知道什么时候不该用你的方法
3. **避免后续打脸**: 如果你隐瞒了，别人复现时发现会更糟糕

### 如何报告

```
"We note that our method underperforms SABRE on circuits with very low depth
(d < 5), where the overhead of our neural network inference outweighs the
routing improvement. For practical circuits (d > 20), our method consistently
achieves lower CNOT counts."
```

### Limitations Section

每篇论文都应该有一个 limitations 讨论（可以在 conclusion 或单独一节）：

```latex
\paragraph{Limitations.}
Our approach has several limitations: (1) The inference time of our neural
network model ($\sim$2s per circuit) is higher than heuristic methods
($\sim$0.1s), making it less suitable for compilation pipelines requiring
sub-second latency. (2) Our method is trained on random circuits and may
not generalize well to highly structured circuits (e.g., QFT, Grover).
(3) We have only tested on grid-like topologies; performance on heavy-hex
or other irregular topologies requires further investigation.
```

---

## 7. 量子计算论文提交前自查清单 (Pre-submission Checklist)

### 实验设计

- [ ] 有随机基线 (random baseline)
- [ ] 有经典/简单基线 (simple baseline)
- [ ] 有当前最优方法 (state-of-the-art) 比较
- [ ] 所有方法在相同条件下测试（相同电路、相同噪声、相同芯片）
- [ ] 测试集足够大（每个配置 $\geq 30$ 个实例，最低 $\geq 10$）
- [ ] 有 scaling 实验（至少 3 个不同规模）
- [ ] 有消融实验

### 统计报告

- [ ] 所有数值结果有误差棒（$\pm$ std 或 CI）
- [ ] 报告了样本量（$n$ = 多少个实例/种子）
- [ ] 使用了适当的统计检验（配对 t / Wilcoxon）
- [ ] 报告了 p 值和效应量
- [ ] 多重比较有校正
- [ ] 没有伪重复（样本单位是电路/实例，不是 shot）

### ML 实验

- [ ] 多个随机种子（$\geq 3$，推荐 $\geq 5$）
- [ ] 报告了所有超参数
- [ ] 有训练曲线（至少附录）
- [ ] 报告了训练时间和硬件
- [ ] 验证集和测试集严格分离
- [ ] 没有在测试集上调参

### 硬件实验

- [ ] 报告了芯片型号和校准信息
- [ ] 报告了 shot 数量
- [ ] 说明了读出错误缓解方法（或说明未使用）
- [ ] 讨论了 simulation-hardware gap
- [ ] 校准漂移已被控制（交叉运行或同一窗口）
- [ ] 报告了 qubit layout

### 可复现性

- [ ] 代码将会开源（或提供匿名链接给审稿人）
- [ ] 随机种子已固定并记录
- [ ] 软件环境已记录
- [ ] 数据集可用或可生成
- [ ] 实验可以用提供的脚本一键复现

### 图表质量

- [ ] 所有图表有误差棒/误差带
- [ ] 文字在打印时可读（$\geq 10$pt）
- [ ] 考虑了色盲友好配色
- [ ] 矢量格式（PDF）用于线图
- [ ] 坐标轴有标签和单位
- [ ] 图例清晰且不遮挡数据

### 论文写作

- [ ] "significantly" 只在有统计检验支持时使用
- [ ] 诚实报告了方法不如基线的情况
- [ ] 有 Limitations 讨论
- [ ] 保真度类型已说明（state/process/gate）
- [ ] 噪声模型已说明
- [ ] 引用了所有基线方法的原始论文
