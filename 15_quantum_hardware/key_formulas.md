# Chapter 15: Quantum Hardware Fundamentals — Key Formulas

> 超导量子硬件核心公式速查表。涵盖 transmon 物理、退相干、门保真度、基准测试指标。所有公式均使用 LaTeX 记号，解释使用中文。

---

## 超导量子比特物理

### F15.1: Transmon Qubit Hamiltonian

$$H = 4E_C(\hat{n} - n_g)^2 - E_J \cos\hat{\phi}$$

其中 $E_C = e^2/(2C_\Sigma)$ 是充电能（charging energy），$C_\Sigma$ 是总电容；$E_J$ 是 Josephson 耦合能；$\hat{n}$ 是 Cooper pair number 算子，$\hat{\phi}$ 是超导相位算子，满足 $[\hat{\phi}, \hat{n}] = i$；$n_g$ 是 offset charge（由栅极电压控制）。

Transmon 工作在 $E_J/E_C \gg 1$ 的极限（典型值 $E_J/E_C \sim 50$--$80$），此时能级对 $n_g$ 的依赖指数衰减，从而大幅抑制电荷噪声：

$$\epsilon_m(n_g) \propto e^{-\sqrt{8E_J/E_C}}$$

在 transmon 极限下，低能谱近似为弱非谐振子：

$$E_m \approx -E_J + \sqrt{8 E_J E_C}\left(m + \frac{1}{2}\right) - \frac{E_C}{12}(6m^2 + 6m + 3)$$

非谐性（anharmonicity）：

$$\alpha \equiv E_{12} - E_{01} \approx -E_C$$

典型参数：$\omega_{01}/(2\pi) \sim 4$--$6$ GHz，$\alpha/(2\pi) \sim -200$--$-300$ MHz。负非谐性意味着 transmon 是弱非谐振子。

**Source**: [derivations/superconducting_qubits.md] | **[Koch et al., PRA 76, 042319 (2007), Eqs. (2.2), (2.11), (2.18)]**

---

### F15.2: $T_1$ Energy Relaxation

$$\rho_{01}(t) = \rho_{01}(0)\,e^{-t/T_1}$$

更完整地，$|1\rangle$ 态的布居数（population）随时间指数衰减：

$$P_1(t) = P_1(0)\,e^{-t/T_1}$$

$$P_0(t) = 1 - P_1(t) = 1 - P_1(0)\,e^{-t/T_1}$$

$T_1$ 表征量子比特从 $|1\rangle$ 到 $|0\rangle$ 的能量弛豫时间（纵向弛豫）。对应量子信道为振幅阻尼（amplitude damping）信道，阻尼参数 $\gamma = 1 - e^{-t/T_1}$。

对于 transmon，主要的 $T_1$ 限制来源包括：
- Purcell 效应（通过读出腔的辐射衰减）
- 介质损耗（表面和界面处的两能级系统，TLS）
- 准粒子隧穿

典型值（2024 超导平台）：$T_1 \sim 50$--$300\;\mu\text{s}$。

**Source**: [derivations/superconducting_qubits.md] | **[Krantz et al., Applied Physics Reviews 6, 021318 (2019), §IV.A]**

---

### F15.3: $T_2$ Dephasing (Ramsey Decay)

$$\langle X \rangle(t) = e^{-t/T_2}\cos(\Delta\omega\, t)$$

其中 $\Delta\omega = \omega_{\text{qubit}} - \omega_{\text{drive}}$ 是量子比特频率与驱动频率之差。

$T_2$ 表征横向弛豫时间（相位退相干），包含两个贡献：

$$\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}$$

其中 $T_\phi$ 是纯 dephasing 时间。由此可得：

$$T_2 \le 2T_1$$

实验中区分两种测量：

- **$T_2^*$（Ramsey）**：自由衰减，受低频噪声（$1/f$ 噪声）影响大，通常 $T_2^* < T_2$
- **$T_2^{\text{echo}}$（Hahn echo）**：在中间插入 $\pi$ 脉冲，折射低频噪声，$T_2^{\text{echo}} \ge T_2^*$

$$\text{Hahn echo: } \langle X \rangle(t) = e^{-(t/T_2^{\text{echo}})^\beta}$$

其中 $\beta$ 取决于噪声谱：$1/f$ 噪声对应 $\beta \approx 1$--$2$，白噪声对应 $\beta = 1$。

**Source**: [derivations/superconducting_qubits.md] | **[Krantz et al., §IV.B; Ithier et al., PRB 72, 134519 (2005)]**

---

## 门保真度与表征

### F15.4: Gate Fidelity (Process Fidelity)

$$F_{\text{pro}} = \frac{\text{tr}(U_{\text{ideal}}^\dagger\, U_{\text{actual}})}{d}$$

更一般地，对于量子过程（CPTP 映射 $\mathcal{E}$，目标酉算子 $U$）的 process fidelity 用 $\chi$-矩阵定义：

$$F_{\text{pro}} = \text{tr}(\chi_{\text{ideal}}\, \chi_{\text{actual}})$$

其中 $\chi$ 是过程在 Pauli 基下的矩阵表示。对于理想酉门 $U$，$\chi_{\text{ideal}}$ 只在 $U$ 对应的 Pauli 分量上为 $1$。

对于 $d$ 维系统（$n$ 量子比特时 $d = 2^n$），process fidelity 与 average gate fidelity（见 F15.5）的关系见下一条。

**Source**: [derivations/benchmarking_metrics.md] | **[Nielsen, PLA 303, 249 (2002)]**

---

### F15.5: Average Gate Fidelity from Process Fidelity

$$F_{\text{avg}} = \frac{d\, F_{\text{pro}} + 1}{d + 1}$$

其中 $d = 2^n$ 是 Hilbert 空间维度。Average gate fidelity 定义为：

$$F_{\text{avg}}(\mathcal{E}, U) = \int d\psi\, \langle\psi| U^\dagger \mathcal{E}(|\psi\rangle\langle\psi|) U |\psi\rangle$$

其中积分遍历 Haar 均匀分布的纯态。$F_{\text{avg}}$ 是实验中最常报告的门保真度。

对于单量子比特门（$d = 2$）：

$$F_{\text{avg}} = \frac{2F_{\text{pro}} + 1}{3}$$

对于两量子比特门（$d = 4$）：

$$F_{\text{avg}} = \frac{4F_{\text{pro}} + 1}{5}$$

平均门不保真度（average gate infidelity）：

$$r = 1 - F_{\text{avg}} = \frac{d(1 - F_{\text{pro}})}{d + 1}$$

**Source**: [derivations/benchmarking_metrics.md] | **[Horodecki et al., PRA 60, 1888 (1999); Nielsen, PLA 303, 249 (2002)]**

---

### F15.6: Randomized Benchmarking (RB) Decay

$$F_m = A\, p^m + B$$

其中 $m$ 是 Clifford 门序列的长度，$p$ 是 depolarizing parameter（衰减率），$A, B$ 是 SPAM（state preparation and measurement）误差相关的拟合参数。

每个 Clifford 门的平均错误率（error per Clifford, EPC）：

$$r_{\text{Clifford}} = \frac{(d-1)(1-p)}{d}$$

对于单量子比特（$d = 2$）：

$$r_{\text{Clifford}} = \frac{1-p}{2}$$

**Interleaved RB**：在每对随机 Clifford 之间插入目标门 $G$，拟合新的 depolarizing parameter $p_G$。目标门的错误率：

$$r_G = \frac{(d-1)(1 - p_G/p)}{d}$$

RB 的优势：
- 对 SPAM 误差不敏感（被吸收到 $A, B$ 中）
- 可扩展到多量子比特
- 给出平均错误率而非最坏情况

典型值（2024 超导平台）：单量子比特门 $r \sim 10^{-4}$--$10^{-3}$，两量子比特门 $r \sim 10^{-3}$--$10^{-2}$。

**Source**: [derivations/benchmarking_metrics.md] | **[Magesan et al., PRL 106, 180504 (2011); PRA 85, 042311 (2012)]**

---

### F15.7: Cross-Resonance (CR) Gate Hamiltonian

$$H_{\text{CR}} = \frac{\Omega}{2}\left(Z_c \otimes I_t + \frac{J}{\Delta}\, Z_c \otimes X_t\right) + \text{higher order terms}$$

其中 $\Omega$ 是驱动强度，$J$ 是量子比特间耦合强度，$\Delta = \omega_c - \omega_t$ 是控制量子比特（control）和目标量子比特（target）的频率差。

有效的 $ZX$ 相互作用率：

$$\omega_{ZX} = \frac{J\Omega}{\Delta}$$

CR 门是 IBM 超导量子处理器的标准两量子比特门。其工作原理是：在控制量子比特频率上对目标量子比特施加微波驱动，通过色散耦合产生条件旋转。

要产生 CNOT 门，需要在 $ZX$ 交互下演化时间 $t = \pi/(2\omega_{ZX})$，再加上单量子比特旋转修正。

实际实现中，通过 echo 方案（回波 CR）消除不需要的 $ZI$ 项，并通过 active cancellation tone 抑制直接驱动泄漏。

**Source**: [derivations/superconducting_qubits.md] | **[Rigetti & Devoret, PRB 81, 134507 (2010); Chow et al., PRL 107, 080502 (2011)]**

---

## 读出与 SPAM

### F15.8: Readout Assignment Fidelity

$$F_{\text{assign}} = 1 - \frac{P(1|0) + P(0|1)}{2}$$

其中 $P(j|i)$ 是准备态 $|i\rangle$ 但测量结果为 $j$ 的概率（误判率）。

完整的读出错误矩阵（confusion matrix）：

$$M = \begin{pmatrix} 1 - P(1|0) & P(0|1) \\ P(1|0) & 1 - P(0|1) \end{pmatrix}$$

其中 $M_{ji} = P(j|i)$。可以通过矩阵求逆进行读出纠错（readout error mitigation）：

$$\vec{p}_{\text{corrected}} = M^{-1} \vec{p}_{\text{raw}}$$

对于多量子比特系统（$n$ 个量子比特），完整 confusion matrix 为 $2^n \times 2^n$。在假设读出误差独立的近似下，可以用 $n$ 个 $2 \times 2$ 矩阵的张量积：

$$M_{\text{total}} \approx M_1 \otimes M_2 \otimes \cdots \otimes M_n$$

主要读出误差来源：
- $T_1$ 衰减（在读出过程中 $|1\rangle \to |0\rangle$）
- Discriminator 误差（信号重叠导致误分类）
- QND 违背（量子非破坏性测量条件不满足）

典型值：$F_{\text{assign}} \sim 95\%$--$99.5\%$。

**Source**: [derivations/benchmarking_metrics.md] | **[Krantz et al., §V; Gambetta et al., PRA 76, 012325 (2007)]**

---

## 系统级基准指标

### F15.9: Quantum Volume

$$\text{QV} = 2^n$$

其中 $n$ 是满足以下条件的最大电路宽度：对于深度 $n$ 宽度 $n$ 的随机 SU(4) 电路，heavy output 概率超过 $2/3$。

Heavy output generation 协议：
1. 生成 $n$ 量子比特、深度 $n$ 的随机模型电路（每层由随机 SU(4) 两量子比特门组成）
2. 经典模拟计算理想输出概率分布 $\{p_x\}$
3. 定义 heavy output 集合 $H = \{x : p_x > \text{median}(\{p_x\})\}$
4. 在量子硬件上运行电路，计算 heavy output 比例：

$$h_{\text{exp}} = \frac{|\{x_i \in H\}|}{N_{\text{shots}}}$$

5. 如果 $h_{\text{exp}} > 2/3$（并通过统计显著性检验），则 QV $\ge 2^n$

理想情况下 heavy output 概率为 $(1 + \ln 2)/2 \approx 0.8466$。

QV 同时衡量了量子比特数量和门质量，但因为需要经典模拟限制在 $\sim 30$--$40$ 量子比特。

**Source**: [derivations/benchmarking_metrics.md] | **[Cross et al., PRA 100, 032328 (2019)]**

---

### F15.10: CLOPS (Circuit Layer Operations Per Second)

$$\text{CLOPS} = \frac{M \times K \times S \times D}{t_{\text{wall}}}$$

其中：
- $M$ = 参数化更新次数（parameter updates）= 100
- $K$ = 每次更新的电路数（circuits per update）= 10
- $S$ = 每个电路的采样次数（shots per circuit）= 100
- $D$ = QV 电路层数（等于 QV 量子比特数）
- $t_{\text{wall}}$ = 总墙钟时间（wall clock time），包含编译、通信、执行、后处理

CLOPS 衡量量子计算系统的吞吐量（throughput），反映了硬件速度、软件栈效率和经典-量子接口延迟的综合性能。

**Source**: [derivations/benchmarking_metrics.md] | **[Wack et al., arXiv:2110.14108 (2021)]**

---

### F15.11: Cross-Entropy Benchmarking (XEB) Fidelity

$$F_{\text{XEB}} = 2^n \langle p(x_i) \rangle_{\text{samples}} - 1$$

其中 $p(x_i)$ 是理想电路输出位串 $x_i$ 的概率（由经典模拟计算），$\langle \cdot \rangle_{\text{samples}}$ 表示对实际硬件采样的位串取平均。

等价形式（linear XEB fidelity）：

$$F_{\text{XEB}} = \frac{\langle p(x_i) \rangle_{\text{samples}} - 1/2^n}{1/2^n} = 2^n \langle p(x_i) \rangle - 1$$

物理意义：
- $F_{\text{XEB}} = 1$：硬件完美复现理想电路
- $F_{\text{XEB}} = 0$：输出与均匀随机无法区分
- 与全局电路保真度的近似关系：$F_{\text{XEB}} \approx F_{\text{circuit}}$（在去极化噪声模型下精确成立）

Google 量子霸权实验中使用的核心验证指标。对于 $n$ 量子比特、深度 $d$ 的随机电路，在去极化噪声下：

$$F_{\text{XEB}} \approx \prod_{g} (1 - e_g) \approx (1 - e)^{n_g}$$

其中 $e_g$ 是第 $g$ 个门的错误率，$n_g$ 是总门数。

**Source**: [derivations/benchmarking_metrics.md] | **[Arute et al., Nature 574, 505 (2019), Supplementary §IV; Boixo et al., Nat. Phys. 14, 595 (2018)]**

---

### F15.12: ZZ Crosstalk Coupling

$$H_{ZZ} = \frac{\zeta}{2}\, Z_i Z_j$$

残余 $ZZ$ 耦合强度（对于 transmon 在色散耦合下）：

$$\zeta \approx \frac{2g^2 \alpha_i \alpha_j}{(\Delta_{ij})(\Delta_{ij} + \alpha_i)(\Delta_{ij} + \alpha_j)}$$

其中 $g$ 是耦合强度，$\alpha_i, \alpha_j$ 是两个 transmon 的非谐性，$\Delta_{ij} = \omega_i - \omega_j$ 是频率差。

$ZZ$ 耦合的物理效果：
- 产生条件相移：$|11\rangle$ 态相对于 $|01\rangle$ 和 $|10\rangle$ 态获得额外相位 $\phi_{ZZ} = \zeta \cdot t$
- 在空闲时间（idle）中积累相位误差
- 限制两量子比特门的保真度和并行门操作

空闲时 $ZZ$ 导致的不保真度估计：

$$1 - F \approx \frac{(\zeta \cdot t_{\text{gate}})^2}{4}$$

典型值：$|\zeta|/(2\pi) \sim 50$--$500$ kHz（取决于耦合方案和频率配置）。

抑制 $ZZ$ 的方法：
- 可调耦合器（tunable coupler）
- 回波/动态解耦序列
- 频率优化（frequency collision avoidance）

**Source**: [derivations/noise_and_errors_hardware.md] | **[Ku et al., PRL 125, 200504 (2020); Mundada et al., PRA 100, 012331 (2019)]**

---

## Cross-References

- **退相干模型与量子信道**：→ [02_quantum_mechanics/derivations/quantum_channels_kraus.md]
- **量子纠错中的噪声模型**：→ [04_quantum_error_correction/derivations/noise_models.md]
- **稳定子码与 syndrome**：→ [04_quantum_error_correction/derivations/stabilizer_formalism.md]
- **表面码**：→ [04_quantum_error_correction/derivations/surface_code_basics.md]
- **变分量子中的误差缓解**：→ [05_variational_quantum/derivations/error_mitigation.md]
