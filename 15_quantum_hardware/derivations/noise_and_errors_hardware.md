# Physical Noise Sources and Calibration in Quantum Hardware

> **Tags**: `noise`, `decoherence`, `T1`, `T2`, `crosstalk`, `calibration`, `drift`, `ZZ-coupling`, `leakage`, `readout-error`, `hardware-noise`

## Statement

量子硬件的噪声来源多样且相互耦合：从单量子比特的弛豫/退相干，到多量子比特的串扰、泄漏、以及校准漂移。理解这些物理噪声源对于有效使用量子处理器（尤其是 BAQIS Quafu 平台的超导芯片）至关重要。本文系统梳理物理噪声源的数学描述，以及如何在实验中识别和缓解它们。

## Prerequisites

- **量子信道** [02_quantum_mechanics/derivations/quantum_channels_kraus.md]
- **超导量子比特** [15_quantum_hardware/derivations/superconducting_qubits.md]
- **噪声模型（抽象）** [04_quantum_error_correction/derivations/noise_models.md]

---

## Part 1: 退相干过程（$T_1$ 和 $T_2$）

### Step 1: 能量弛豫（$T_1$）

量子比特从激发态 $|1\rangle$ 自发衰变到基态 $|0\rangle$ 的过程，对应振幅阻尼信道：

$$\rho(t) = \mathcal{E}_{T_1}(\rho) = \sum_{k=0,1} E_k \rho E_k^\dagger$$

Kraus 算子 [F15.3]：

$$E_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1 - \gamma} \end{pmatrix}, \quad E_1 = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix}$$

其中 $\gamma = 1 - e^{-t/T_1}$。

**$T_1$ 的物理来源**（超导系统）：
- 介电损耗（dielectric loss）：基底和界面处的两能级系统（TLS）缺陷
- Purcell 衰变：量子比特通过读出谐振腔的自发辐射
- 准粒子隧穿（quasiparticle tunneling）：Cooper 对被打断产生的准粒子
- 辐射到环境的光子泄漏

**典型值**（BAQIS Quafu ScQ-P136 等超导平台）：$T_1 \sim 20$--$100 \mu\mathrm{s}$

### Step 2: 纯退相干（$T_\phi$）和总退相干（$T_2$）

纯退相干描述相位信息的丢失（不涉及能量转移），对应相位阻尼信道：

$$E_0^{(\phi)} = \sqrt{1 - p_\phi/2} \cdot I, \quad E_1^{(\phi)} = \sqrt{p_\phi/2} \cdot Z$$

总退相干时间 $T_2$ 由两个过程共同决定 [F15.4]：

$$\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}$$

**$T_\phi$ 的物理来源**：
- 1/f 磁通噪声（flux noise）：来自磁性杂质和界面缺陷
- 电荷噪声（charge noise）：在 transmon 中已被大幅抑制（$E_J/E_C \gg 1$）
- 光子数涨落（photon shot noise）：读出腔中残余光子导致的 AC Stark 效应

**$T_2$ vs $T_2^*$**：
- $T_2^*$：Ramsey 实验测得，包含低频噪声的非均匀展宽（inhomogeneous dephasing）
- $T_2$：spin echo 实验测得，消除了部分低频噪声
- 一般 $T_2^* \leq T_2 \leq 2T_1$

### Step 3: 门执行期间的退相干效应

在门时间 $t_g$ 内积累的退相干导致的门错误率（门保真度下降）：

$$\epsilon_{\mathrm{decoherence}} \approx \frac{t_g}{3} \left( \frac{1}{T_1} + \frac{1}{T_\phi} \right)$$

对于单量子比特门（$t_g \sim 20$--$50\,\mathrm{ns}$），此贡献约 $10^{-4}$--$10^{-3}$。
对于双量子比特门（$t_g \sim 100$--$500\,\mathrm{ns}$），此贡献约 $10^{-3}$--$10^{-2}$。

---

## Part 2: 串扰（Crosstalk）

### Step 1: 频率碰撞和静态 ZZ 耦合

两个 transmon 之间的残余 ZZ 相互作用是超导系统中最主要的串扰源：

$$H_{\mathrm{ZZ}} = \frac{\zeta}{2} Z_i \otimes Z_j$$

静态 ZZ 耦合强度（对于 transmon，通过虚能级的交换相互作用产生）[F15.12]：

$$\zeta \approx \frac{2 g^2 \alpha}{\Delta(\Delta + \alpha)}$$

其中 $g$ 是耦合强度，$\Delta = \omega_i - \omega_j$ 是频率失谐，$\alpha$ 是非谐性。

**后果**：idle 量子比特的相位积累：$\phi_{\mathrm{ZZ}} = \zeta \cdot t$，在长电路中可能导致显著的相干错误。

### Step 2: 经典串扰（控制线间）

微波驱动脉冲通过控制线之间的电容/电感耦合泄漏到邻近量子比特：

$$\Omega_{\mathrm{leak}} = \eta \cdot \Omega_{\mathrm{drive}}$$

其中 $\eta$ 是串扰系数（典型值 $\eta \sim 10^{-3}$--$10^{-2}$）。

**缓解方法**：
- 脉冲整形（DRAG 脉冲）
- 串扰补偿矩阵
- 频率规划（避免频率碰撞）

### Step 3: 量化串扰

使用同时 RB（simultaneous randomized benchmarking）量化：

$$\epsilon_{\mathrm{crosstalk}} = \epsilon_{\mathrm{sim}} - \epsilon_{\mathrm{iso}}$$

其中 $\epsilon_{\mathrm{sim}}$ 和 $\epsilon_{\mathrm{iso}}$ 分别是同时执行和单独执行时的 RB 错误率。

---

## Part 3: 能级泄漏（Leakage）

### Step 1: 泄漏到非计算态

Transmon 是弱非谐振子，有高于 $|1\rangle$ 的能级 $|2\rangle, |3\rangle, \ldots$。门脉冲可能将布居数泄漏到这些非计算态：

$$\rho_{\mathrm{leak}} = \mathrm{Tr}_{\mathrm{comp}}(\rho) \neq 0$$

**泄漏率**与非谐性和门脉冲参数密切相关。对于 DRAG 修正的单量子比特门：

$$\epsilon_{\mathrm{leak}} \sim \left( \frac{\Omega}{\alpha} \right)^2$$

其中 $\Omega$ 是 Rabi 频率，$\alpha$ 是非谐性。

### Step 2: 泄漏在 QEC 中的问题

泄漏是非 Pauli 错误，不能被标准 stabilizer QEC 自然纠正：
- 泄漏态不在 codespace 内
- 可能"传播"到邻近量子比特（通过纠缠门）
- 需要专门的 leakage reduction units (LRU)

---

## Part 4: 读出错误

### Step 1: 读出保真度

量子比特读出通过色散测量实现。读出错误矩阵：

$$M = \begin{pmatrix} 1 - \epsilon_0 & \epsilon_1 \\ \epsilon_0 & 1 - \epsilon_1 \end{pmatrix}$$

其中 $\epsilon_0 = P(\text{measure } 1 | \text{prepared } 0)$，$\epsilon_1 = P(\text{measure } 0 | \text{prepared } 1)$。

平均读出保真度：

$$F_{\mathrm{readout}} = 1 - \frac{\epsilon_0 + \epsilon_1}{2}$$

**典型值**：$F_{\mathrm{readout}} \sim 95\%$--$99.5\%$。$\epsilon_1 > \epsilon_0$ 通常成立（$T_1$ 衰变在读出期间将 $|1\rangle$ 翻转为 $|0\rangle$）。

### Step 2: 读出错误缓解

对于 $n$ 量子比特系统，理想分布 $\vec{p}$ 和观测分布 $\vec{p}_{\mathrm{obs}}$ 的关系：

$$\vec{p}_{\mathrm{obs}} = A \vec{p}$$

其中 $A$ 是 $2^n \times 2^n$ 的赋值矩阵。通过求逆（或正则化求逆）可以缓解：

$$\vec{p}_{\mathrm{corrected}} = A^{-1} \vec{p}_{\mathrm{obs}}$$

> **实际限制**：$n$ 较大时 $A$ 的维度指数增长。常用的近似：张量积假设 $A \approx \bigotimes_{i=1}^n M_i$。

---

## Part 5: 校准漂移（Calibration Drift）

### Step 1: 频率漂移

量子比特频率随时间漂移，来源包括 TLS 缺陷的开关（TLS switching）、温度波动：

$$\omega_q(t) = \omega_q^{(0)} + \delta\omega(t)$$

频率漂移导致：
- 门相位误差：$\delta\phi = \delta\omega \cdot t_g$
- 频率碰撞条件变化
- ZZ 耦合强度变化

**典型漂移幅度**：$\delta\omega/(2\pi) \sim 10$--$100\,\mathrm{kHz}$ 在数小时时间尺度内

### Step 2: $T_1$ 波动

$T_1$ 在时间尺度数分钟到数小时内可能出现显著波动（因 TLS 耦合/退耦合）。这使得基于固定 $T_1$ 的错误缓解不够准确。

### Step 3: 对实验的影响

**最佳实践**（BAQIS Quafu 平台建议）：
- 每次实验前检查 $T_1, T_2$ 和频率
- 对长时间实验，交错执行基准测试电路
- 报告校准时间戳和主要参数值
- 使用 interleaved 设计以自动补偿慢漂移

---

## Part 6: 相干错误 vs 非相干错误

### Step 1: 区分

| 类型 | 数学描述 | 物理来源 | QEC 影响 |
|------|---------|---------|---------|
| 非相干错误 | 混合态：$\rho \to \sum_k E_k \rho E_k^\dagger$ | $T_1, T_2$, 热噪声 | 可被 Pauli twirling 转化为随机 Pauli 错误 |
| 相干错误 | 过/欠旋转：$U_{\mathrm{actual}} = e^{-i(H + \delta H)t}$ | 脉冲校准不准、串扰 | 可导致 QEC 阈值显著降低 |

### Step 2: 相干错误的数学描述

门过旋转（over-rotation）：

$$U_{\mathrm{actual}} = e^{-i(\theta + \delta\theta)\hat{n}\cdot\vec{\sigma}/2}$$

门轴偏转：

$$U_{\mathrm{actual}} = e^{-i\theta(\hat{n} + \delta\hat{n})\cdot\vec{\sigma}/2}$$

**钻石范数（diamond norm）**是量化最坏情况门错误的标准度量，尤其对相干错误更敏感：

$$\|\mathcal{E} - \mathcal{U}\|_\diamond = \max_\rho \| (\mathcal{E} \otimes \mathcal{I})(\rho) - (\mathcal{U} \otimes \mathcal{I})(\rho) \|_1$$

---

## Summary Table

| 噪声源 | 时间尺度 | 典型量级 | 可缓解？ | 关键参数 |
|--------|---------|---------|---------|---------|
| $T_1$ 衰变 | $\mu$s | $10^{-4}$--$10^{-3}$/门 | 提高 $T_1$，限制电路深度 | $T_1$ |
| $T_2$ 退相干 | $\mu$s | $10^{-4}$--$10^{-3}$/门 | 动力学退耦，echo | $T_2, T_\phi$ |
| 静态 ZZ | 持续 | $10^{-4}$--$10^{-2}$ | echo, 频率调谐 | $\zeta$ |
| 控制线串扰 | 门执行期间 | $10^{-3}$--$10^{-2}$ | 串扰补偿矩阵 | $\eta$ |
| 泄漏 | 门执行期间 | $10^{-4}$--$10^{-3}$ | DRAG, LRU | $\alpha, \Omega$ |
| 读出错误 | 读出窗口 | $10^{-3}$--$5\times10^{-2}$ | 读出错误缓解矩阵 | $\epsilon_0, \epsilon_1$ |
| 校准漂移 | 分钟--小时 | $10$--$100$ kHz | 频繁重校准 | $\delta\omega(t)$ |
| 相干错误 | 门执行期间 | $10^{-4}$--$10^{-3}$ | 随机化编译 | $\delta\theta$ |

---

## Cross-References

- **抽象噪声模型** → [04_quantum_error_correction/derivations/noise_models.md]
- **Transmon 物理** → [15_quantum_hardware/derivations/superconducting_qubits.md]
- **基准测试** → [15_quantum_hardware/derivations/benchmarking_metrics.md]
- **错误缓解** → [05_variational_quantum/derivations/error_mitigation.md]
- **量子信道数学** → [02_quantum_mechanics/derivations/quantum_channels_kraus.md]
- **QEC 阈值** → [04_quantum_error_correction/derivations/threshold_theorem.md]
