# Quantum Experiment Design

> 量子计算论文的实验设计指南。涵盖仿真实验和真机实验的设计原则。
> 侧重实践操作，不涉及深层统计理论。

---

## 1. 实验对照 (Experimental Controls)

### 为什么需要对照？

没有对照的实验无法说明你的方法好不好。"我们的方法在 100-qubit 电路上达到了 0.85 的保真度"——这个数字本身没有意义，除非你告诉读者基线是多少。

### 对照层次

```
Level 0: 随机基线 (Random Baseline)
  └── 证明你的方法至少比随机好

Level 1: 经典/简单基线 (Simple Baseline)
  └── 证明问题确实需要你提出的复杂方法

Level 2: 已有方法 (Existing Methods / Previous SOTA)
  └── 证明你的方法比现有最好的方法更好

Level 3: 消融实验 (Ablation)
  └── 证明你方法的每个组件都有贡献
```

### 各类问题的推荐基线

| 问题类型 | Random Baseline | Simple Baseline | SOTA |
|---------|----------------|-----------------|------|
| 量子编译/路由 | 随机 SWAP 插入 | Qiskit default (stochastic) | SABRE, t\|ket\|, OLSQ |
| QEC 解码 | 随机翻转 | MWPM (最小权重完美匹配) | Union-Find, 神经网络解码器 |
| VQE/QAOA | 随机参数 | 经典精确解（小规模） | 之前最好的变分方法 |
| 量子电路生成 | 随机电路 | 规则化构造（如 QFT 模板） | 之前的生成方法 |
| 量子机器学习 | 随机猜测 | 经典 ML 方法 | 之前的 QML 方法 |

### 注意事项

- **Random baseline 必须有**: 如果你的方法连随机都不显著优于，说服力为零
- **经典基线很重要**: 量子 ML 论文经常被批评不和经典方法比较
- **SOTA 要用最新版本**: 不要和 5 年前的方法比（除非那仍是 SOTA），使用原始作者发布的代码或官方 benchmark
- **公平比较**: 给所有方法相同的计算预算（时间/迭代次数/参数量）

---

## 2. Scaling 实验 (泛化性测试)

### 为什么需要 Scaling 实验？

在小规模问题上表现好不一定能泛化到大规模。审稿人几乎一定会问"这个方法能 scale 吗？"

### 设计要点

**选择合适的规模范围**:
- 量子比特数: 小 (5-20) → 中 (20-50) → 大 (50-100+)
- 码距 (QEC): $d = 3, 5, 7, 9, 11, 13$ （奇数）
- 电路深度: 浅 (10-50 layers) → 中 (50-200) → 深 (200+)
- 问题规模 (CO): $n = 20, 50, 100, 200, 500, 1000$

**每个规模点需要足够多的实例**:
- 最少 10 个随机实例（最好 30-50 个）
- 报告均值和标准差，画误差棒

**检查 scaling behavior**:
```
理想结果: 性能随规模缓慢下降，但下降速度比基线慢
可接受: 性能在大规模时与基线相当，但在中等规模有优势
不理想: 性能在大规模时反而比基线差（可能方法不 scalable）
```

### 作图建议

```python
import matplotlib.pyplot as plt
import numpy as np

# Scaling 实验的标准图
sizes = [10, 20, 50, 100, 200]
ours_mean = [0.95, 0.92, 0.87, 0.81, 0.74]
ours_std = [0.02, 0.03, 0.04, 0.05, 0.06]
baseline_mean = [0.93, 0.88, 0.79, 0.68, 0.55]
baseline_std = [0.03, 0.04, 0.05, 0.07, 0.08]

fig, ax = plt.subplots(figsize=(6, 4))
ax.errorbar(sizes, ours_mean, yerr=ours_std, marker='o', label='Ours', capsize=3)
ax.errorbar(sizes, baseline_mean, yerr=baseline_std, marker='s', label='Baseline', capsize=3)
ax.set_xlabel('Number of qubits')
ax.set_ylabel('Fidelity')
ax.set_xscale('log')  # log scale 通常更清晰
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
```

---

## 3. 消融实验 (Ablation Study)

### 什么是消融实验？

逐个移除方法中的组件，观察性能变化。证明每个组件都有贡献。

### 设计原则

**完整消融表**:

```
Full model (所有组件)             → 最好的结果
  - 去掉组件 A (w/o Component A)  → 性能下降 X%
  - 去掉组件 B (w/o Component B)  → 性能下降 Y%
  - 去掉组件 C (w/o Component C)  → 性能下降 Z%
  - 只保留骨架 (Backbone only)    → 基线水平
```

**注意事项**:
- 每行都需要误差棒（多种子/多实例）
- 如果某个组件移除后性能不下降，要诚实报告——这可能意味着该组件不必要
- 消融实验通常在一个有代表性的中等规模上做即可，不需要在所有规模上做

### LaTeX 表格模板

```latex
\begin{table}[h]
\centering
\caption{Ablation study on 50-qubit random circuits ($n=100$, mean $\pm$ std).}
\begin{tabular}{lcc}
\toprule
Variant & CNOT Count $\downarrow$ & Fidelity $\uparrow$ \\
\midrule
Full model & $\mathbf{172.1 \pm 25.3}$ & $\mathbf{0.891 \pm 0.031}$ \\
\quad w/o graph attention & $189.3 \pm 27.8$ & $0.862 \pm 0.035$ \\
\quad w/o noise-aware loss & $178.5 \pm 26.1$ & $0.871 \pm 0.033$ \\
\quad w/o iterative refinement & $195.7 \pm 30.2$ & $0.845 \pm 0.039$ \\
\midrule
Random baseline & $245.3 \pm 32.1$ & $0.712 \pm 0.045$ \\
\bottomrule
\end{tabular}
\end{table}
```

---

## 4. 真机实验注意事项 (Hardware Experiments)

### 4.1 校准漂移 (Calibration Drift)

**问题**: 超导量子芯片的参数（$T_1$, $T_2$, 门保真度）会随时间变化。如果方法 A 在上午跑，方法 B 在下午跑，比较是不公平的。

**解决方案**:
```
方案 1: 交叉运行 (Interleaved Execution)
  A-B-A-B-A-B... 交替运行两种方法
  优点: 消除了线性漂移
  缺点: 增加了总运行时间

方案 2: 随机化顺序 (Randomized Order)
  打乱所有实验的运行顺序
  优点: 漂移效应在两种方法间均匀分布
  缺点: 不能消除漂移，只能使其成为噪声

方案 3: 同一校准窗口 (Same Calibration Window)
  在一次校准后尽快跑完所有实验
  优点: 简单
  缺点: 受限于校准窗口长度（通常几小时）
```

**Quafu 平台建议**: 使用 ScQ-P136 等芯片时，建议在提交任务前检查当日校准数据。可以通过 Quafu API 获取最新的门保真度和退相干时间。尽量在同一个校准周期内完成所有对比实验。

### 4.2 公平的跨芯片/跨时间比较

**原则**: 如果必须在不同芯片或不同时间段比较：
1. 报告每次运行时的芯片校准指标（平均单量子比特门保真度、平均双量子比特门保真度、平均 $T_1$, $T_2$）
2. 使用相同的量子比特子集（layout）
3. 考虑使用 **模拟噪声模型** 作为"归一化"基准——如果方法 A 在好的校准下跑，方法 B 在差的校准下跑，可以用噪声模型来估计校准差异的影响

### 4.3 Shot 预算分配 (Shot Budget Allocation)

**固定总 shot 预算时的分配策略**:

假设总 shot 预算为 $S$，有 $m$ 种方法，$n$ 个测试电路：
- 均匀分配: 每个 (方法, 电路) 组合分 $S / (m \times n)$ shots
- 自适应分配: 对不确定性大的组合分更多 shots

**实践建议**:
- 单个电路的保真度估计: 1000 shots 通常足够（精度 $\sim \pm 0.01$--$0.03$）
- QEC 逻辑错误率估计: 可能需要 10000--100000 shots（因为错误率很低）
- 如果 shot 预算有限: 减少电路种类，不要减少每个电路的 shots

### 4.4 读出错误缓解 (Readout Error Mitigation)

**是否需要做读出错误缓解？**

```
场景判断:
├── 你的论文关注的是读出本身 → 不做缓解（否则循环论证）
├── 你的论文关注的是其他方面（编译、解码等）
│   ├── 读出错误显著影响结论 → 做缓解，并报告缓解前后的结果
│   └── 读出错误影响较小 → 可以不做，但在论文中讨论
└── 你要和仿真结果比较 → 做缓解（使硬件结果更接近理想值）
```

**常用方法**:
- Confusion matrix / tensor product mitigation: 最简单，假设各 qubit 独立
- M3 (Matrix-free measurement mitigation): Qiskit 内置，scalable
- 报告时注明: "with/without readout error mitigation"

### 4.5 仿真 vs 真机的 Gap

**论文中如何讨论 sim-hardware gap**:

1. 在仿真中验证方法正确性（理想仿真 + 噪声仿真）
2. 在真机上展示实际可行性
3. 量化 gap: $\Delta F = F_{\text{sim}} - F_{\text{hw}}$
4. 分析 gap 来源: 串扰、校准误差、非马尔可夫噪声等

**写法示例**:
> "In noise-free simulation, our method achieves a fidelity of 0.99. Under a
> depolarizing noise model (error rate 0.1%), the fidelity drops to 0.94. On the
> Quafu ScQ-P136 device, we observe a fidelity of 0.87 (with readout error
> mitigation), with the remaining gap attributed to coherent errors and crosstalk
> not captured by the noise model."

---

## 5. 可复现性 (Reproducibility)

### Checklist

- [ ] **代码开源**: GitHub/GitLab 链接，附 README
- [ ] **随机种子固定并报告**: 在代码和论文中都记录
- [ ] **环境记录**: Python 版本、PyTorch 版本、CUDA 版本、关键依赖版本
- [ ] **数据可用**: 测试数据集公开或有生成脚本
- [ ] **超参数完整**: 所有超参数在论文中列出（附录也行）
- [ ] **硬件实验**: 报告芯片型号、校准日期、qubit layout
- [ ] **训练曲线**: 提供训练过程的 loss 曲线（至少在附录中）
- [ ] **计算资源**: 报告训练时间、GPU 型号、内存使用

### 种子管理

```python
import random
import numpy as np
import torch

def set_seed(seed: int):
    """设置所有随机种子，确保可复现。"""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    # 注意: 以下设置会降低性能，但保证完全确定性
    # torch.backends.cudnn.deterministic = True
    # torch.backends.cudnn.benchmark = False

# 推荐: 使用多个不相关的种子
SEEDS = [42, 123, 456, 789, 1024, 2048, 3407, 4096, 5555, 9999]
```

### 数据归档建议

```
project/
├── code/              # 源代码
├── configs/           # 实验配置文件
├── data/              # 输入数据或生成脚本
├── results/           # 原始实验结果
│   ├── raw/           # 未处理的输出
│   └── processed/     # 处理后的表格/图表数据
├── figures/           # 论文图表
├── scripts/           # 运行实验的脚本
│   ├── run_all.sh     # 一键复现
│   └── plot_results.py
└── README.md          # 如何复现
```

---

## 6. 仿真实验 vs 硬件实验

### 角色分工

| 方面 | 仿真实验 | 硬件实验 |
|------|---------|---------|
| **目的** | 验证方法正确性、测试 scalability | 证明实际可行性 |
| **规模** | 可以很大（100+ qubits 仿真） | 受限于芯片（当前 ~100 qubits） |
| **噪声** | 可控（理想 / 可调噪声模型） | 真实但不完全已知 |
| **可复现** | 完全可复现 | 受校准漂移影响 |
| **在论文中** | 主要结果（尤其是 scaling） | 补充验证（但很有说服力） |

### 论文结构建议

```
Section 4: Experiments
  4.1 Experimental Setup (通用设置)
  4.2 Simulation Results
    4.2.1 Main comparison (vs baselines, on standard benchmarks)
    4.2.2 Scaling experiment (不同规模)
    4.2.3 Ablation study
  4.3 Hardware Results (如果有)
    4.3.1 Setup (芯片、校准、layout)
    4.3.2 Results (与仿真对比)
    4.3.3 Discussion (sim-hw gap 分析)
```
