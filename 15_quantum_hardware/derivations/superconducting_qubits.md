# Superconducting Qubits: Physics, Gates, and Platform Specifics

> **Tags**: `transmon`, `superconducting`, `josephson`, `quafu`, `decoherence`, `gates`, `hardware`

## Statement

超导量子比特（特别是 transmon）是当前最成熟的量子计算物理实现之一。本文从 Josephson 结出发，推导 transmon 的能级结构、退相干机制、单/双量子比特门的物理原理，并介绍 BAQIS Quafu 平台的硬件特性。

## Prerequisites

- **量子力学基础**：谐振子、二次量子化 → [02_quantum_mechanics/]
- **量子信道**：Kraus 表示、振幅阻尼 → [02_quantum_mechanics/derivations/quantum_channels_kraus.md]
- **密度矩阵**：→ [02_quantum_mechanics/derivations/density_matrix_formalism.md]

---

## Part 1: From Josephson Junction to Transmon **[Koch et al., PRA 76, 042319 (2007)]**

### 1.1 Josephson Junction Physics

超导约瑟夫森结（Josephson junction）由两块超导体夹一层薄绝缘体构成。其核心关系为 Josephson 方程：

**DC Josephson 关系**：

$$I = I_c \sin\phi$$

其中 $I_c$ 是临界电流，$\phi = \phi_1 - \phi_2$ 是两侧超导体的超导相位差。

**AC Josephson 关系**：

$$\frac{d\phi}{dt} = \frac{2eV}{\hbar}$$

其中 $V$ 是结两端的电压。约瑟夫森结提供了一个非线性、无耗散的电感元件，这是构建非谐振子（量子比特）的关键。

**约瑟夫森能量**：

$$U(\phi) = -E_J \cos\phi, \quad E_J = \frac{\hbar I_c}{2e} = \frac{\Phi_0 I_c}{2\pi}$$

其中 $\Phi_0 = h/(2e)$ 是超导磁通量子。

### 1.2 Cooper Pair Box (CPB) Hamiltonian

考虑一个由约瑟夫森结和电容构成的电路（Cooper pair box），其 Hamiltonian 为：

$$H_{\text{CPB}} = 4E_C(\hat{n} - n_g)^2 - E_J \cos\hat{\phi}$$

**[Koch et al., Eq. (2.2)]**

其中：
- $E_C = e^2/(2C_\Sigma)$ — 充电能，$C_\Sigma = C_J + C_g$ 是总电容
- $\hat{n}$ — Cooper pair number 算子（离散，本征值为整数）
- $n_g = C_g V_g/(2e)$ — 由栅极电压控制的 offset charge
- $\hat{\phi}$ — 超导相位算子
- 对易关系：$[\hat{\phi}, \hat{n}] = i$

在 charge basis $\{|n\rangle\}$ 下：

$$H = 4E_C \sum_n (n - n_g)^2 |n\rangle\langle n| - \frac{E_J}{2}\sum_n (|n\rangle\langle n+1| + |n+1\rangle\langle n|)$$

这是 Mathieu 方程的量子版本，精确本征值可以用 Mathieu 函数表示。

### 1.3 Charge Qubit → Transmon Limit

不同 $E_J/E_C$ 比值对应不同的工作机制：

| 参数区间 | 名称 | 特点 |
|---------|------|------|
| $E_J/E_C \ll 1$ | Charge qubit (CPB) | 能级强烈依赖 $n_g$，对电荷噪声极敏感 |
| $E_J/E_C \sim 1$ | Quantronium | 在最优工作点 $n_g = 1/2$ 对噪声一阶不敏感 |
| $E_J/E_C \gg 1$ | **Transmon** | 对 $n_g$ 指数不敏感，牺牲少量非谐性换取超强噪声免疫 |

**[Koch et al., §III]**: Transmon 的关键洞察是，当 $E_J/E_C \gg 1$ 时，能级对 offset charge $n_g$ 的灵敏度指数衰减：

$$\frac{\partial E_m}{\partial n_g} \propto e^{-\sqrt{8E_J/E_C}}$$

代价是非谐性减小。在 transmon 极限下展开余弦势（类似谐振子 + 微扰），得到能级：

$$E_m \approx -E_J + \sqrt{8E_J E_C}\left(m + \frac{1}{2}\right) - \frac{E_C}{12}(6m^2 + 6m + 3)$$

**[Koch et al., Eq. (2.11)]**

### 1.4 Energy Levels and Anharmonicity

量子比特跃迁频率：

$$\omega_{01} = (E_1 - E_0)/\hbar \approx \sqrt{8E_J E_C}/\hbar - E_C/\hbar$$

非谐性：

$$\alpha \equiv (E_2 - E_1) - (E_1 - E_0) = E_{12} - E_{01} \approx -E_C$$

**[Koch et al., Eq. (2.18)]**

非谐性是负的（$\alpha < 0$），意味着更高能级间距更小。这使得 $|0\rangle \leftrightarrow |1\rangle$ 跃迁与 $|1\rangle \leftrightarrow |2\rangle$ 跃迁在频率上可区分，从而可以用微波脉冲选择性地驱动计算子空间内的跃迁。

典型参数（包括 Quafu 平台等超导平台）：
- $\omega_{01}/(2\pi) \sim 4$--$6$ GHz
- $\alpha/(2\pi) \sim -200$--$-300$ MHz
- $E_J/E_C \sim 50$--$80$

---

## Part 2: Decoherence **[Krantz et al., Applied Physics Reviews 6, 021318 (2019), §IV]**

### 2.1 $T_1$: Energy Relaxation

$T_1$ 过程描述量子比特从激发态 $|1\rangle$ 到基态 $|0\rangle$ 的不可逆衰变，类似于原子自发辐射。

Bloch-Redfield 框架下，$T_1$ 由量子比特频率处的噪声谱密度决定：

$$\frac{1}{T_1} = \frac{1}{\hbar^2} |\langle 0|\hat{\lambda}|1\rangle|^2 S(\omega_{01})$$

其中 $\hat{\lambda}$ 是耦合算子，$S(\omega)$ 是噪声功率谱密度。

密度矩阵演化：

$$\rho_{11}(t) = \rho_{11}(0)\, e^{-t/T_1}$$
$$\rho_{01}(t) = \rho_{01}(0)\, e^{-t/(2T_1)} \quad \text{(仅含 } T_1 \text{ 贡献)}$$

对应的 Kraus 算子（amplitude damping channel, $\gamma = 1 - e^{-t/T_1}$）：

$$K_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{pmatrix}, \quad K_1 = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix}$$

**主要 $T_1$ 限制机制**：

1. **Purcell 效应**：量子比特通过读出谐振腔发生辐射衰变
   $$\frac{1}{T_1^{\text{Purcell}}} = \frac{\kappa g^2}{\Delta^2}$$
   其中 $\kappa$ 是腔的衰减率，$g$ 是量子比特-腔耦合强度，$\Delta = \omega_q - \omega_r$ 是失谐量。可通过 Purcell filter 抑制。

2. **两能级系统（TLS）缺陷**：界面和衬底表面的杂散 TLS 与量子比特共振耦合
3. **准粒子隧穿（quasiparticle tunneling）**：破缺的 Cooper 对产生准粒子
4. **红外/杂散辐射**：非热光子激发

### 2.2 $T_2$: Dephasing

$T_2$ 描述量子比特的相位信息丢失（Bloch 球上 $xy$ 平面内的弛豫）：

$$\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}$$

其中 $T_\phi$ 是纯 dephasing 时间。$T_\phi$ 由量子比特频率的低频涨落引起：

$$\frac{1}{T_\phi} = \frac{1}{2}\left|\frac{\partial \omega_{01}}{\partial \lambda}\right|^2 S_\lambda(0)$$

**Ramsey 实验**（测量 $T_2^*$）：
1. $\pi/2$ 脉冲 → 自由演化时间 $\tau$ → $\pi/2$ 脉冲 → 测量
2. 信号：$\langle X \rangle(\tau) = e^{-\tau/T_2^*}\cos(\Delta\omega\, \tau)$

**Hahn Echo**（测量 $T_2^{\text{echo}}$）：
1. $\pi/2$ → $\tau/2$ → $\pi$ → $\tau/2$ → $\pi/2$ → 测量
2. 中间的 $\pi$ 脉冲折射（refocus）静态和低频噪声
3. $T_2^{\text{echo}} \ge T_2^*$，通常 $T_2^{\text{echo}} \le 2T_1$

**$1/f$ 噪声**对 transmon 的影响：

超导量子比特中普遍存在 $1/f$ 磁通噪声，功率谱密度：

$$S_\Phi(\omega) = \frac{A_\Phi^2}{|\omega|}$$

对于工作在磁通敏感点的量子比特（如 flux-tunable transmon），$T_\phi$ 与噪声振幅和灵敏度有关。在 sweet spot（$\partial\omega/\partial\Phi = 0$）处，对磁通噪声一阶不敏感。

### 2.3 $T_2^*$ vs $T_2^{\text{echo}}$ vs $T_2$

| 量 | 测量方法 | 物理意义 | 典型关系 |
|---|---------|---------|---------|
| $T_2^*$ | Ramsey | 包含低频噪声的总退相干 | $T_2^* \le T_2^{\text{echo}}$ |
| $T_2^{\text{echo}}$ | Hahn echo | 折射低频噪声后的退相干 | $T_2^{\text{echo}} \le 2T_1$ |
| $T_2$ | 完美 DD | 理论上限（仅含 $T_1$ 贡献和白噪声） | $T_2 \le 2T_1$ |

---

## Part 3: Single-Qubit Gates **[Krantz et al., §III]**

### 3.1 Microwave Drive and Rabi Oscillations

对 transmon 施加共振微波驱动（$\omega_d \approx \omega_{01}$），在旋转坐标系下的 Hamiltonian 为：

$$H_{\text{drive}} = \frac{\Omega}{2}(\cos\phi \cdot X + \sin\phi \cdot Y)$$

其中 $\Omega$ 是 Rabi 频率（正比于驱动振幅），$\phi$ 是驱动相位。

- $\phi = 0$：绕 $X$ 轴旋转 → $R_X(\theta)$ 门
- $\phi = \pi/2$：绕 $Y$ 轴旋转 → $R_Y(\theta)$ 门
- 旋转角度 $\theta = \Omega \cdot t_g$，其中 $t_g$ 是脉冲时间

**$\pi$ 脉冲**实现 $|0\rangle \leftrightarrow |1\rangle$ 翻转，对应 NOT 门。$\pi/2$ 脉冲创建叠加态。

### 3.2 Derivative Removal by Adiabatic Gate (DRAG)

直接方波脉冲会泄漏到 $|2\rangle$ 态。DRAG 方法通过在正交分量中加入脉冲的导数来抑制泄漏 **[Motzoi et al., PRL 103, 110501 (2009)]**：

$$\Omega_X(t) = \Omega_0(t), \quad \Omega_Y(t) = -\frac{\dot{\Omega}_0(t)}{\alpha}$$

其中 $\alpha$ 是非谐性。DRAG 脉冲是现代超导平台上单量子比特门的标准实现方法。

### 3.3 Virtual-Z Gate

$Z$ 旋转可以通过改变后续脉冲的参考相位来实现，不需要物理脉冲，因此门时间为零且不引入误差 **[McKay et al., PRA 96, 022330 (2017)]**：

$$R_Z(\theta): \phi_{\text{ref}} \to \phi_{\text{ref}} + \theta$$

结合 Virtual-Z 和物理的 $\sqrt{X}$ 门，可以实现任意单量子比特旋转：

$$U(\theta, \phi, \lambda) = R_Z(\phi) \sqrt{X}\, R_Z(\theta) \sqrt{X}\, R_Z(\lambda)$$

---

## Part 4: Two-Qubit Gates

### 4.1 Cross-Resonance (CR) Gate **[Rigetti & Devoret, PRB 81, 134507 (2010); Chow et al., PRL 107, 080502 (2011)]**

CR 门是 IBM（以及类似架构如 Quafu）的标准两量子比特门方案。

**原理**：以控制量子比特 $c$ 的频率 $\omega_c$ 驱动目标量子比特 $t$。在色散耦合（$\Delta = \omega_c - \omega_t$ 远大于耦合 $g$）下，有效 Hamiltonian 为：

$$H_{\text{eff}} = \frac{\Omega}{2}I_c X_t + \frac{J\Omega}{2\Delta} Z_c X_t + \cdots$$

第一项（$IX$）是不需要的直接驱动，第二项（$ZX$）是条件旋转——当控制量子比特在 $|0\rangle$ 和 $|1\rangle$ 时，目标量子比特绕 $X$ 轴以相反方向旋转。

通过 echo 方案消除 $IX$ 项：施加 CR 脉冲 → 对控制比特做 $X$ 门 → 施加 CR 脉冲 → 对控制比特做 $X$ 门。纯 $ZX$ 交互在 $t = \pi/(2\omega_{ZX})$ 时产生 CNOT（加单比特修正）。

### 4.2 CZ Gate (Tunable Coupler)

适用于频率可调量子比特或可调耦合器架构：

$$\text{CZ} = \text{diag}(1, 1, 1, -1)$$

实现方式：将 $|11\rangle$ 态快速调谐到与 $|02\rangle$（或 $|20\rangle$）态共振附近，通过避免交叉（avoided crossing）积累相对相位 $\pi$。

优点：门速度快（$\sim 30$--$50$ ns），但需要磁通控制线，增加了硬件复杂度和噪声通道。

### 4.3 iSWAP Gate

$$\text{iSWAP} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

当两个量子比特频率相同时，交换耦合 $g(XX + YY)$ 在 $t = \pi/(2g)$ 产生 iSWAP。Google Sycamore 处理器使用 $\sqrt{\text{iSWAP}}$ 作为原生两量子比特门。

---

## Part 5: Quafu Platform Specifics

### 5.1 BAQIS Quafu 超导量子计算平台

Quafu（夸父）是北京量子信息科学研究院（BAQIS）开发的云量子计算平台，提供多个超导量子芯片的远程访问。

**芯片列表**（截至 2024-2025）：

| 芯片名称 | 量子比特数 | 拓扑 | 备注 |
|---------|----------|------|------|
| ScQ-P136 | 136 | 重六角格子 | 百比特级芯片 |
| ScQ-P66 | 66 | 格子型 | 中等规模 |
| ScQ-P18 | 18 | 格子型 | 小规模，高保真度 |
| ScQ-P10 | 10 | 链式/环式 | 教学/测试用 |

### 5.2 Typical Parameters

超导平台的典型硬件参数（以 Quafu 等平台为例，具体数值因芯片和校准状态而异）：

| 参数 | 典型范围 | 说明 |
|------|---------|------|
| $\omega_{01}/(2\pi)$ | 4--6 GHz | 量子比特频率 |
| $\alpha/(2\pi)$ | $-200$ to $-300$ MHz | 非谐性 |
| $T_1$ | 30--200 $\mu$s | 能量弛豫时间 |
| $T_2^*$ | 10--100 $\mu$s | Ramsey 退相干时间 |
| 单量子比特门时间 | 20--40 ns | DRAG 脉冲 |
| 两量子比特门时间 | 200--500 ns | CR 门（fixed-frequency），30--80 ns（CZ 门） |
| 单量子比特门保真度 | 99.5--99.9% | Randomized benchmarking |
| 两量子比特门保真度 | 95--99.5% | Interleaved RB |
| 读出保真度 | 95--99% | Assignment fidelity |

### 5.3 Chip Topology and Connectivity

超导量子处理器的量子比特排列在二维芯片上，通过超导谐振腔（bus resonator）或直接电容耦合连接近邻量子比特。

**常见拓扑**：
- **方格子（square lattice）**：每个量子比特最多 4 个近邻，适合表面码
- **重六角格子（heavy-hex lattice）**：IBM 使用，每个量子比特最多 2--3 个近邻，减少频率碰撞和串扰
- **其他**：链式、环式（小规模芯片）

连接性（connectivity）直接影响：
- 量子电路编译的 SWAP 开销 → [13_quantum_compilation/derivations/qubit_routing_theory.md]
- 可实现的量子纠错码 → [04_quantum_error_correction/derivations/surface_code_basics.md]
- 串扰和频率碰撞约束 → [noise_and_errors_hardware.md]

### 5.4 在论文中报告硬件参数

在使用 Quafu 平台进行实验的论文中，通常需要报告：

1. **芯片信息**：名称、量子比特数、制造工艺
2. **使用的量子比特子集**：编号、连接图
3. **校准参数**（表格形式）：
   - 每个量子比特的 $\omega_{01}$, $T_1$, $T_2^*$
   - 每个量子比特的单量子比特门保真度
   - 每对耦合量子比特的两量子比特门保真度
   - 读出保真度
4. **实验时间窗口**：校准参数随时间漂移，需标注
5. **使用的原生门集**：如 $\{\sqrt{X}, R_Z, \text{CNOT}\}$

---

## Key References

| 引用 | 内容 |
|------|------|
| Koch et al., PRA 76, 042319 (2007) | Transmon 量子比特的原始论文 |
| Krantz et al., Appl. Phys. Rev. 6, 021318 (2019) | 超导量子计算全面综述 |
| Rigetti & Devoret, PRB 81, 134507 (2010) | Cross-resonance 门理论 |
| Chow et al., PRL 107, 080502 (2011) | CR 门实验实现 |
| Motzoi et al., PRL 103, 110501 (2009) | DRAG 脉冲 |
| McKay et al., PRA 96, 022330 (2017) | Virtual-Z 门 |
| Ithier et al., PRB 72, 134519 (2005) | 超导量子比特退相干机制 |
| Blais et al., PRA 69, 062320 (2004) | 电路 QED 原始论文 |
