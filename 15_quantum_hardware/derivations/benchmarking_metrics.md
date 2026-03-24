# Quantum Hardware Benchmarking Metrics

> **Tags**: `randomized-benchmarking`, `RB`, `XEB`, `quantum-volume`, `CLOPS`, `fidelity`, `gate-error`, `benchmarking`

## Statement

量子硬件基准测试（benchmarking）是评估量子处理器性能的标准化方法。不同于单纯报告门保真度，基准测试协议提供了可复现、可比较的系统级指标。本文推导四个核心基准测试方法的数学框架：Randomized Benchmarking (RB)、Cross-Entropy Benchmarking (XEB)、Quantum Volume (QV) 和 CLOPS（Circuit Layer Operations Per Second）。

## Prerequisites

- **量子门和量子信道** [02_quantum_mechanics/derivations/quantum_channels_kraus.md]
- **Clifford 群** [06_group_theory/derivations/clifford_group.md]
- **保真度和迹距离** [02_quantum_mechanics/derivations/fidelity_and_trace_distance.md]
- **噪声模型** [04_quantum_error_correction/derivations/noise_models.md]

---

## Part 1: Randomized Benchmarking (RB)（随机基准测试）

### Step 1: 基本原理

**核心思想**：利用 Clifford 群的结构来隔离门错误率，消除态制备和测量（SPAM）误差的影响。

**协议描述**：
1. 从 $n$-qubit Clifford 群 $\mathcal{C}_n$ 中均匀随机抽取 $m$ 个 Clifford 门 $C_1, C_2, \ldots, C_m$
2. 计算逆操作 $C_{m+1} = (C_m \cdots C_2 C_1)^{-1}$
3. 对初态 $|0\rangle^{\otimes n}$ 执行序列 $C_{m+1} C_m \cdots C_1$
4. 测量返回初态的概率（survival probability）

### Step 2: 数学模型 [F15.5]

每个实际 Clifford 门 $\tilde{C}_i$ 可以写成理想门加噪声信道：

$$\tilde{C}_i = \Lambda_i \circ C_i$$

其中 $\Lambda_i$ 是实现 $C_i$ 时引入的噪声信道。

**关键假设**：在 Clifford twirling 下，噪声信道被等效为去极化信道（depolarizing channel）：

$$\Lambda_{\mathrm{eff}}(\rho) = p \rho + (1 - p) \frac{I}{d}$$

其中 $d = 2^n$ 是 Hilbert 空间维数，$p$ 是去极化参数。

**Survival probability 的指数衰减**：

$$F_{\mathrm{seq}}(m) = A \cdot p^m + B$$

其中 $A$ 和 $B$ 吸收了 SPAM 误差。通过对不同 $m$ 拟合此指数衰减曲线，可提取 $p$。

### Step 3: 从 $p$ 到平均门保真度 [F15.6]

平均 Clifford 门保真度（average gate fidelity）与去极化参数的关系：

$$\bar{F} = \frac{p(d - 1) + 1}{d}$$

等价地，平均门错误率（error per Clifford, EPC）为：

$$r = (1 - p) \cdot \frac{d - 1}{d}$$

对于单量子比特（$d = 2$）：$r = (1 - p)/2$。

**从 EPC 到单门错误率**的估算：若每个 Clifford 门平均由 $n_g$ 个原生门（native gates）组成，则单门平均错误率约为：

$$\epsilon_{\mathrm{gate}} \approx \frac{r}{n_g}$$

> **注意**：此估算假设错误可加性，仅在错误率较小时近似成立。

### Step 4: Interleaved RB（交错 RB）[F15.7]

为测量特定门 $G$ 的保真度，使用交错协议：

1. **标准 RB**：$C_1, C_2, \ldots, C_m$ → 拟合得到 $p_{\mathrm{ref}}$
2. **交错 RB**：$C_1, G, C_2, G, \ldots, C_m, G$ → 拟合得到 $p_G$

特定门 $G$ 的错误率：

$$r_G = \frac{(d - 1)(1 - p_G / p_{\mathrm{ref}})}{d}$$

---

## Part 2: Cross-Entropy Benchmarking (XEB)（交叉熵基准测试）

### Step 1: 定义与动机

XEB 由 Google 在量子霸权实验中提出 [Arute et al., Nature 574, 505 (2019)]，用于验证量子电路的输出分布是否符合理论预期。

**核心量度**：线性交叉熵保真度（Linear Cross-Entropy Benchmarking fidelity, $\mathcal{F}_{\mathrm{XEB}}$）。

### Step 2: 数学定义 [F15.8]

设量子电路 $U$ 作用于 $|0\rangle^{\otimes n}$，理想输出态为 $|\psi\rangle = U|0\rangle^{\otimes n}$。对计算基 $|x\rangle$，理想概率为：

$$p(x) = |\langle x | \psi \rangle|^2$$

线性 XEB 保真度定义为：

$$\mathcal{F}_{\mathrm{XEB}} = 2^n \langle p(x) \rangle_{\mathrm{exp}} - 1$$

其中 $\langle \cdot \rangle_{\mathrm{exp}}$ 表示对实验采样得到的比特串 $x$ 取平均。

**直觉解释**：
- 若实验完美实现了 $U$，则 $\langle p(x) \rangle_{\mathrm{exp}} = \sum_x p(x)^2 \approx 2/2^n$（Porter-Thomas 分布的二阶矩），所以 $\mathcal{F}_{\mathrm{XEB}} \approx 1$
- 若实验输出是均匀随机噪声，$\langle p(x) \rangle_{\mathrm{exp}} = 1/2^n$，所以 $\mathcal{F}_{\mathrm{XEB}} = 0$

### Step 3: 噪声模型下的 XEB

在全局去极化噪声模型下，若噪声强度为 $\lambda$：

$$\tilde{p}(x) = \lambda \cdot p(x) + (1 - \lambda) / 2^n$$

则：

$$\mathcal{F}_{\mathrm{XEB}} = \lambda$$

在门错误率模型下，若电路包含 $n_g$ 个双量子比特门，每个门错误率为 $\epsilon$：

$$\mathcal{F}_{\mathrm{XEB}} \approx (1 - \epsilon)^{n_g} \approx e^{-n_g \epsilon}$$

### Step 4: XEB 的统计估计

实际估计 $\mathcal{F}_{\mathrm{XEB}}$ 需要 $N_s$ 个样本。统计误差（标准差）约为：

$$\sigma(\mathcal{F}_{\mathrm{XEB}}) \approx \frac{1}{\sqrt{N_s}} \cdot 2^n \cdot \mathrm{std}[p(x)]$$

> **与 RB 的对比**：RB 隔离 SPAM 误差，XEB 测量全局电路保真度。RB 只用 Clifford 门（可经典模拟），XEB 使用通用门集。

---

## Part 3: Quantum Volume (QV)（量子体积）

### Step 1: 定义与动机

Quantum Volume 是 IBM 提出的整体性能指标 [Cross et al., Phys. Rev. A 100, 032328 (2019)]，综合考虑量子比特数、连通性、门保真度和编译效率。

### Step 2: 协议 [F15.9]

1. 选择宽度 $m \leq n$（$n$ 为系统量子比特数），深度也为 $m$
2. 构造随机 SU(4) 电路：$m$ 层，每层对 $m$ 个量子比特做随机两两 Haar 随机酉操作
3. 将电路编译到硬件原生门集
4. 执行并采样，计算重输出概率（heavy output probability）

**Heavy Output Generation (HOG)** 测试：

$$h_m = \Pr[\text{output } x \text{ has } p(x) > \text{median}(p)]$$

### Step 3: Quantum Volume 定义 [F15.10]

$$\log_2 \mathrm{QV} = \max \{ m : h_m > 2/3 \text{ with confidence} > 97.7\% \}$$

即找最大的 $m$ 使得 heavy output probability 以足够高的置信度超过 $2/3$。

$$\mathrm{QV} = 2^{m^*}$$

**物理含义**：QV 回答了"你的处理器能可靠执行多大的'方形电路'？"。它同时受限于：
- 量子比特数量
- 门保真度（噪声积累）
- 连通性（SWAP 开销）
- 编译器效率

### Step 4: 置信度与统计

使用 $N$ 次重复实验估计 $h_m$，利用单侧假设检验：

$$H_0: h_m \leq 2/3 \quad \text{vs} \quad H_1: h_m > 2/3$$

需要 $\hat{h}_m - 2\sigma > 2/3$，其中 $\sigma = \sqrt{\hat{h}_m(1 - \hat{h}_m)/N}$。

---

## Part 4: CLOPS（电路层每秒操作数）

### Step 1: 定义 [F15.11]

CLOPS（Circuit Layer Operations Per Second）衡量量子系统的端到端吞吐量：

$$\mathrm{CLOPS} = \frac{M \cdot K \cdot S \cdot D}{t_{\mathrm{wall}}}$$

其中：
- $M$ = 模板电路数量（templates）
- $K$ = 每个模板的参数更新次数
- $S$ = 每次参数更新的采样次数（shots）
- $D$ = QV 电路的层数
- $t_{\mathrm{wall}}$ = 总挂钟时间

### Step 2: 瓶颈分析

端到端时间分解：

$$t_{\mathrm{wall}} = t_{\mathrm{compile}} + t_{\mathrm{upload}} + t_{\mathrm{queue}} + t_{\mathrm{execute}} + t_{\mathrm{readout}} + t_{\mathrm{download}}$$

**硬件与软件共同影响 CLOPS**：即使门保真度相同，经典控制软件的延迟也会显著影响实用性能。

---

## Part 5: 其他重要指标

### 5.1 层保真度（Layer Fidelity）

IBM 在 2023 年引入的更细粒度指标，衡量单层含 CNOT 门的保真度 [Kim et al., Nature 618, 500 (2023)]。

### 5.2 Algorithmic Qubits

$\mathrm{AQ} = \log_2(\text{最大可靠执行的电路规模})$，考虑了错误缓解的效果。

### 5.3 Application-Oriented Benchmarks

- **QAOA/VQE 收敛性**：在特定问题上的近似比
- **QPE 精度**：相位估计的有效位数
- **采样质量**：总变差距离、KL 散度

---

## Summary Table

| 指标 | 测量对象 | SPAM 独立？ | 可扩展？ | 关键公式 |
|------|---------|------------|---------|---------|
| RB | 平均 Clifford 门保真度 | 是 | 门数限制 | $F(m) = Ap^m + B$ [F15.5] |
| Interleaved RB | 特定门保真度 | 是 | 门数限制 | $r_G = (d-1)(1 - p_G/p_{\mathrm{ref}})/d$ [F15.7] |
| XEB | 全局电路保真度 | 否 | 至数百量子比特 | $\mathcal{F}_{\mathrm{XEB}} = 2^n\langle p(x)\rangle - 1$ [F15.8] |
| QV | 系统综合性能 | 否 | 受编译限制 | $\mathrm{QV} = 2^{m^*}$ [F15.10] |
| CLOPS | 端到端吞吐量 | N/A | 是 | $\mathrm{CLOPS} = MKSD/t$ [F15.11] |

---

## Cross-References

- **噪声信道理论** → [02_quantum_mechanics/derivations/quantum_channels_kraus.md]
- **Clifford 群** → [06_group_theory/derivations/clifford_group.md]
- **去极化信道** → [04_quantum_error_correction/derivations/noise_models.md]
- **保真度** → [02_quantum_mechanics/derivations/fidelity_and_trace_distance.md]
- **超导量子比特** → [15_quantum_hardware/derivations/superconducting_qubits.md]
- **硬件噪声源** → [15_quantum_hardware/derivations/noise_and_errors_hardware.md]
