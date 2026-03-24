# Noise Models for Quantum Error Correction

> **Tags**: `noise`, `qec`, `depolarizing`, `circuit-level`, `erasure`, `phenomenological`

## Statement

量子纠错中使用的噪声模型从简单到复杂分为多个层次：code capacity（无测量噪声）、phenomenological（简化测量噪声）、circuit-level（完整电路噪声）。每种模型有不同的数学描述和对应的阈值。理解噪声模型对写 QEC 论文至关重要，因为阈值和性能声明总是相对于特定噪声模型而言。

## Prerequisites

- **量子信道**：CPTP 映射、Kraus 表示
- **Pauli 群**：$\{I, X, Y, Z\}$ 的性质
- **稳定子码**：[stabilizer_formalism.md]
- **表面码**：[surface_code_basics.md]

---

## Digitisation of Quantum Errors **[Roffe, §2.2; Gottesman thesis, §2.2]**

> **[Roffe, QEC Introductory Guide, §2.2]**: Any coherent error process can be decomposed into a sum from the Pauli set $\{I, X, Z, XZ\}$. The error correction process itself involves performing projective measurements that cause the superposition to collapse to a subset of its terms. As a result, a quantum error correction code with the ability to correct errors described by the $X$- and $Z$-Pauli matrices will be able to correct any coherent error. This effect is referred to as the **digitisation of the error**.

> **[Gottesman thesis, §2.2]**: The most general one-qubit error is some $2 \times 2$ matrix, which can always be written as a complex linear combination of $\sigma_x$, $\sigma_y$, $\sigma_z$, and $I$. The syndrome measurement process acts as a measurement of which Pauli error occurred, causing the state to collapse to a definite error branch that can then be corrected.

---

## Part 1: Single-Qubit Noise Channels **[Preskill Ch.7, §7.1-7.2; Steane, p.3-4; Bacon, p.3-6]**

### 1.1 Depolarizing Channel **[NordiQUEst, §2.1; Bacon, p.4-5; Preskill Ch.7, §7.1, p.3]**

**定义**：以概率 $p$ 将量子比特替换为最大混合态：

$$\mathcal{D}_p(\rho) = (1-p)\rho + \frac{p}{3}(X\rho X + Y\rho Y + Z\rho Z)$$

等价地（用 Kraus 算子表示）：

$$\mathcal{D}_p(\rho) = (1-p)\rho + \frac{p}{3}(X\rho X + Y\rho Y + Z\rho Z)$$

$$= \left(1-\frac{4p}{3}\right)\rho + \frac{p}{3}(I\rho I + X\rho X + Y\rho Y + Z\rho Z)$$

注：$I\rho I + X\rho X + Y\rho Y + Z\rho Z = 2I$（Pauli twirling identity），所以：

$$\mathcal{D}_p(\rho) = \left(1-\frac{4p}{3}\right)\rho + \frac{4p}{3}\frac{I}{2}$$

**Pauli 错误概率**：
- 无错误 ($I$): $1 - p$
- $X$ 错误: $p/3$
- $Y$ 错误: $p/3$
- $Z$ 错误: $p/3$

**Bloch 球收缩**：depolarizing channel 将 Bloch 矢量缩放为 $(1 - 4p/3)$ 倍。

### 1.2 Independent Bit-Flip / Phase-Flip Channel

**Bit-flip channel**（$X$ 噪声）：

$$\mathcal{E}_X(\rho) = (1-p)\rho + p\,X\rho X$$

**Phase-flip channel**（$Z$ 噪声）：

$$\mathcal{E}_Z(\rho) = (1-p)\rho + p\,Z\rho Z$$

**独立 $X/Z$ 噪声模型**：常用于分析 CSS 码（如表面码），因为 $X$ 和 $Z$ 错误可以独立解码。等效于 bit-flip 和 phase-flip 独立作用：

$$\mathcal{E}_{XZ}(\rho) = (1-p_X)(1-p_Z)\rho + p_X(1-p_Z)X\rho X + (1-p_X)p_Z Z\rho Z + p_X p_Z Y\rho Y$$

### 1.3 Biased Noise **[NordiQUEst, §2.3; Tuckett et al. 2018]**

在许多物理实现中，某种 Pauli 错误远多于其他类型。偏置比 (bias ratio) 定义为：

$$\eta = \frac{p_Z}{p_X + p_Y}$$

- $\eta = 1/2$：标准去极化噪声
- $\eta \gg 1$：$Z$-biased 噪声（如 cat qubits, Kerr parametric oscillators）
- $\eta \to \infty$：纯 dephasing 噪声

**对表面码的影响**：biased noise 下，表面码可以通过非对称码距（不同方向使用不同长度）或 XZZX 码（Bonilla Ataides et al. 2021）来显著提高阈值。XZZX 表面码在 $\eta = \infty$ 时阈值可达 $50\%$。

### 1.4 Amplitude Damping Channel **[Steane Tutorial, §2.5; Gottesman thesis, §2.4]**

> **[Gottesman thesis, §2.4]**: When qubits are ground or excited states of an ion, a likely source of errors is spontaneous emission. After some amount of time, the excited state will either decay to the ground state, producing the error $X + iY$ with probability $\epsilon$, or it will not, which changes the relative amplitudes of $|0\rangle$ and $|1\rangle$, resulting in the error $I - Z$ with probability $O(\epsilon^2)$. A channel that performs this sort of time evolution is known as an **amplitude damping** channel. Since the only $O(1)$ effect of time evolution is the identity, this sort of error can be protected against to lowest order by a code to correct an arbitrary single error.

描述能量弛豫（$T_1$ 过程）：

$$\mathcal{A}_\gamma(\rho) = E_0 \rho E_0^\dagger + E_1 \rho E_1^\dagger$$

$$E_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{pmatrix}, \quad E_1 = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix}$$

Amplitude damping 不是 Pauli 信道，但可以通过 Pauli twirling 近似为等效的去极化噪声。对于时间 $t$：

$$\gamma = 1 - e^{-t/T_1}$$

### 1.5 Erasure Channel **[Bacon, p.12; Preskill Ch.7, §7.3.2, p.14]**

**定义**：以概率 $p$ 量子比特被"擦除"（丢失），且已知哪些量子比特被擦除。

$$\mathcal{E}_{\text{erase}}(\rho) = (1-p)\rho + p\,|e\rangle\langle e|$$

其中 $|e\rangle$ 是正交于量子比特 Hilbert 空间的擦除标志态。

**关键性质**：擦除是 QEC 中最容易纠正的噪声类型，因为已知错误的位置。

**表面码在擦除噪声下的阈值**：$p_{\text{th}}^{\text{erasure}} = 50\%$（code capacity），远高于 Pauli 噪声的 $\sim 11\%$。

**与 Pauli 噪声的等效关系**：一个擦除等效于以 $1/2$ 概率施加 $I$，以 $1/6$ 概率施加 $X, Y, Z$ 中的每一个（擦除后的量子比特处于最大混合态）。因此 erasure rate $p_e$ 等效于 Pauli error rate $p \approx p_e/2$。

---

## Part 2: Multi-Qubit Noise Models

### 2.1 Independent Identically Distributed (IID) Noise

**定义**：每个量子比特独立经历相同的噪声信道 $\mathcal{E}$：

$$\mathcal{E}^{\otimes n}(\rho) = \bigotimes_{i=1}^{n} \mathcal{E}_i(\rho_i)$$

对于去极化噪声，$n$ 量子比特上发生 Pauli 错误 $E = P_1 \otimes P_2 \otimes \cdots \otimes P_n$ 的概率为：

$$\Pr(E) = \prod_{i=1}^{n} \Pr(P_i) = \left(\frac{p}{3}\right)^{\text{wt}(E)} (1-p)^{n-\text{wt}(E)}$$

其中 $\text{wt}(E)$ 是 $E$ 的 Pauli 权重（非 $I$ 位置数）。

### 2.2 Two-Qubit Gate Noise

**两比特去极化噪声**：在 CNOT 或 CZ 门之后，以概率 $p$ 施加 $4^2 - 1 = 15$ 种非平凡的两比特 Pauli 错误之一：

$$\mathcal{D}_p^{(2)}(\rho) = (1-p)\rho + \frac{p}{15}\sum_{(P,Q) \neq (I,I)} (P \otimes Q)\rho(P \otimes Q)$$

### 2.3 Correlated Noise

在实际量子硬件中，噪声往往是关联的。常见的关联噪声来源：

- **串扰 (crosstalk)**：对一个量子比特施加门时影响邻近量子比特
- **泄漏 (leakage)**：量子比特离开计算子空间 $\{|0\rangle, |1\rangle\}$
- **cosmic rays**：高能粒子导致多个量子比特同时出错

关联噪声使得 IID 假设失效，可能显著降低有效阈值。

> **[Gottesman thesis, §2.4]**: While correlated errors can in principle be a severe problem, they can be handled without a change in formalism as long as the chance of a correlated error drops rapidly enough with the size of the blocks of errors. Since a $t$-qubit error will occur with probability $O(\epsilon^t)$ when the probability of uncorrelated single-qubit errors is $\epsilon$, as long as the probability of a $t$-qubit correlated error is $O(\epsilon^t)$, the correlated errors cause no additional problems.

---

## Part 3: QEC-Specific Noise Models

### 3.1 Code Capacity Noise Model **[NordiQUEst, §3.1; Dennis et al. 2002, §3.4; Roffe, §5.2]**

**假设**：
- 数据量子比特有噪声（IID Pauli 错误）
- Syndrome 测量完美（无测量错误）
- 只需一轮 syndrome 测量

**数学描述**：对 $[[n, k, d]]$ 稳定子码，错误 $E$ 以概率 $\Pr(E) \propto (p/3)^{\text{wt}(E)}$ 发生，syndrome $\mathbf{s} = \sigma(E)$ 精确已知。

**阈值**（表面码）：
- 独立 $X/Z$: $p_{\text{th}} \approx 10.94\%$（ML 解码）
- 去极化: $p_{\text{th}} \approx 18.9\%$（hashing bound）

**用途**：理论基准，用于比较解码器的最优性能。

### 3.2 Phenomenological Noise Model **[NordiQUEst, §3.2; Dennis et al. 2002, §3; Roffe, §5.3]**

**假设**：
- 数据量子比特有噪声（IID，每轮错误率 $p$）
- Syndrome 测量有噪声（每个 syndrome 位以概率 $q$ 翻转）
- 需要 $d$ 轮 syndrome 测量
- **不**建模 syndrome 提取电路的具体细节

**数学描述**：3D 解码问题。Syndrome 在时空中是 $(x, y, t)$ 格点。

数据错误：在空间方向产生相邻缺陷对
测量错误：在时间方向产生缺陷对

$$\Pr(\text{数据错误在位置 } e) = p$$
$$\Pr(\text{syndrome 翻转在时刻 } t, \text{位置 } s) = q$$

通常取 $p = q$（同等错误率）。

**阈值**（表面码，$p = q$）：
- MWPM: $p_{\text{th}} \approx 2.93\%$
- ML: $p_{\text{th}} \approx 3.3\%$

### 3.3 Circuit-Level Noise Model **[NordiQUEst, §3.3; Surface Code Notes, §6]**

**定义**：最现实的噪声模型，建模 syndrome 提取电路中每个组件的噪声。

**Standard circuit-level depolarizing noise** 在以下位置注入错误：

| 位置 | 错误模型 | 参数 |
|------|---------|------|
| 单比特门后 | 单比特去极化 $\mathcal{D}_p^{(1)}$ | $p$ |
| 两比特门后 | 两比特去极化 $\mathcal{D}_p^{(2)}$ | $p$ |
| 量子比特初始化 | 以概率 $p$ 翻转 | $p$ |
| 量子比特测量 | 以概率 $p$ 翻转结果 | $p$ |
| 空闲量子比特（每时间步） | 单比特去极化 $\mathcal{D}_p^{(1)}$ | $p$ |

**Circuit-level noise 的关键特征**：

1. **Hook errors**：CNOT 门在 syndrome 提取中将 ancilla 错误传播为关联数据错误。单个 CNOT 故障可以产生 weight-2 的数据错误。

2. **时间关联**：多轮 syndrome 提取中，同一数据量子比特在不同轮次可能累积错误。

3. **Space-time defect graph**：syndrome 缺陷在 3D 时空中的图结构比 phenomenological 模型更复杂（因为 hook errors 产生的非局部关联）。

**阈值**（rotated surface code）：
- MWPM: $p_{\text{th}} \approx 0.57\%$
- Correlated MWPM: $p_{\text{th}} \approx 0.8\%$

### 3.4 SI1000 Noise Model **[NordiQUEst, §3.4]**

Google 提出的超导量子比特噪声模型，基于 Sycamore 处理器的实验数据：

- 单比特门错误率: $\sim 10^{-3}$
- 两比特门错误率: $\sim 5 \times 10^{-3}$ (主导噪声源)
- 测量错误率: $\sim 2 \times 10^{-2}$
- 初始化错误率: $\sim 10^{-3}$
- 空闲错误率: $\sim 3 \times 10^{-4}$ / $\mu$s
- 泄漏率: $\sim 10^{-3}$ / gate

**与标准去极化模型的区别**：
- 非均匀错误率（两比特门和测量主导）
- 包含泄漏
- 包含 T1/T2 弛豫
- CZ 门后的 correlated $ZZ$ 错误

### 3.5 Pauli Twirling Approximation **[Steane Tutorial, §2.5; Bacon, §2]**

任何噪声信道都可以通过 Pauli twirling 近似为 Pauli 信道：

$$\tilde{\mathcal{E}}(\rho) = \frac{1}{4^n}\sum_{P \in \mathcal{G}_n} P \mathcal{E}(P\rho P) P$$

结果 $\tilde{\mathcal{E}}$ 是对角的 Pauli 信道：

$$\tilde{\mathcal{E}}(\rho) = \sum_{P \in \{I,X,Y,Z\}^{\otimes n}} p_P \cdot P\rho P$$

其中 $p_P = \frac{1}{4^n}\text{Tr}(P \cdot \mathcal{E}(P))$。

**适用条件**：Pauli twirling 保留错误的一阶行为，但丢失了相干噪声的信息。对于 stabilizer 码的 threshold 分析，Pauli twirling 通常是一个合理的近似。

---

## Part 4: Error Rate Conversion Formulas

### 物理噪声参数与 QEC 错误率的关系

**从 $T_1, T_2$ 到 Pauli 错误率** **[NordiQUEst, §2.4]**：

对于持续时间 $\tau$ 的操作：

$$p_X = p_Y \approx \frac{1}{4}\left(1 - e^{-\tau/T_1}\right)$$

$$p_Z \approx \frac{1}{2}\left(1 - e^{-\tau/T_\phi}\right), \quad \frac{1}{T_\phi} = \frac{1}{T_2} - \frac{1}{2T_1}$$

总 Pauli 错误率：$p = p_X + p_Y + p_Z$

**从实验保真度到 Pauli 错误率**：

单比特门保真度 $F_1$ 到错误率：$p_1 = 1 - F_1$

两比特门保真度 $F_2$ 到错误率：$p_2 = 1 - F_2$

**等效去极化错误率**：

$$p_{\text{dep}} = \frac{4^n - 1}{4^n}(1 - F)$$

（$n$ 是量子比特数，$F$ 是平均门保真度）

---

## Part 5: Noise Model Hierarchy Summary

| 噪声模型 | syndrome 噪声 | 电路细节 | 阈值 (surface code, MWPM) | 解码维度 |
|---------|-------------|---------|--------------------------|---------|
| Code capacity | 无 | 无 | $\sim 10.3\%$ | 2D |
| Phenomenological | 有（简化） | 无 | $\sim 2.9\%$ | 3D |
| Circuit-level (uniform depol.) | 有（完整） | 有 | $\sim 0.57\%$ | 3D |
| Circuit-level (SI1000) | 有（完整） | 有（非均匀） | $\sim 0.3-0.5\%$ | 3D |
| Circuit-level (biased, $\eta=100$) | 有（完整） | 有 | $\sim 3\%$ (tailored) | 3D |

**写论文时的注意事项**：

1. 永远明确说明使用的噪声模型
2. 不同噪声模型的阈值不可直接比较
3. Code capacity 阈值是上界；circuit-level 阈值是实际相关的
4. 对于新解码器的性能声明，至少应该测试 phenomenological 和 circuit-level 两种模型
5. 如果声称"实用性"，应该使用 SI1000 或类似的实验校准噪声模型

---

## Part 6: From Steane Tutorial — Physical Noise and QEC

### Amplitude Damping and Dephasing **[Steane Tutorial, §2.5]**

Steane 详细讨论了实际物理量子比特的两种主要噪声过程：

**$T_1$ 弛豫（amplitude damping）** **[Steane Tutorial, §2.5.1]**：
- 物理过程：激发态 $|1\rangle$ 自发衰变到基态 $|0\rangle$
- Kraus 算子：$E_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{pmatrix}$，$E_1 = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix}$
- 衰变参数：$\gamma = 1 - e^{-t/T_1}$
- **非 Pauli 性质**：$E_0$ 不是 Pauli 算子（$E_0 \neq aI + bZ$），所以 amplitude damping 不是 Pauli 信道

**$T_2$ 退相干（dephasing）** **[Steane Tutorial, §2.5.2]**：
- 物理过程：$|0\rangle$ 和 $|1\rangle$ 之间的相对相位随机漂移
- 信道：$\mathcal{E}(\rho) = (1-p_\phi)\rho + p_\phi Z\rho Z$
- 退相干率：$p_\phi = \frac{1}{2}(1 - e^{-t/T_\phi})$，$1/T_\phi = 1/T_2 - 1/(2T_1)$
- 纯 dephasing 是 Pauli 信道（只有 $Z$ 错误）

**Steane 的重要警告** **[Steane Tutorial, §2.5.3]**：在超导量子比特中，amplitude damping 和 dephasing 通常同时存在，且 $T_2 \leq 2T_1$（equality 对应纯 $T_1$ 限制的退相干）。实验中典型值 $T_2/T_1 \approx 0.5 - 1.5$。

### Pauli Twirling 的严格表述 **[Steane Tutorial, §2.5.4]**

**定理（Pauli Twirling）** **[Steane Tutorial, §2.5]**：

对任意量子信道 $\mathcal{E}$，Pauli twirled 版本定义为：

$$\tilde{\mathcal{E}}(\rho) = \frac{1}{4^n} \sum_{P \in \mathcal{G}_n} P \mathcal{E}(P\rho P) P$$

则 $\tilde{\mathcal{E}}$ 是对角 Pauli 信道：$\tilde{\mathcal{E}}(\rho) = \sum_P p_P P\rho P$。

**Steane 的适用性讨论**：
- Pauli twirling 保留了错误的一阶行为（保真度不变）
- 丢失了相干噪声的信息（非对角 $\chi$-matrix 元素被消除）
- 对稳定子码的阈值分析通常足够准确
- 对实际超导量子比特，Pauli twirling 可通过随机化 Pauli 门在实验上实现（randomized compiling）

---

## Part 7: From Bacon's Introduction — Noise Discretization and Erasure

### 噪声离散化的严格证明 **[Bacon, §2.1-2.2]**

**定理（Noise Discretization）** **[Bacon, §2.1]**：

设 $\mathcal{C}$ 是一个能纠正 Pauli 错误集 $\mathcal{E} = \{E_a : a \in A\}$ 的量子码，$\mathcal{R}$ 是对应的恢复操作。则对任意量子信道 $\mathcal{N}(\rho) = \sum_j K_j \rho K_j^\dagger$，只要每个 $K_j$ 可以写成 $\{E_a\}$ 的线性组合，$\mathcal{R}$ 也能纠正 $\mathcal{N}$。

**证明** **[Bacon, §2.2]**：

设 $K_j = \sum_a c_{ja} E_a$。对码空间中的态 $|\psi\rangle$，错误后的态为：

$$\mathcal{N}(|\psi\rangle\langle\psi|) = \sum_j \left(\sum_a c_{ja} E_a\right) |\psi\rangle\langle\psi| \left(\sum_b c_{jb}^* E_b^\dagger\right)$$

恢复操作 $\mathcal{R}$ 首先测量 syndrome。由 Knill-Laflamme 条件，$\langle\psi|E_a^\dagger E_b|\psi'\rangle = C_{ab}\delta_{\psi\psi'}$。syndrome 测量将 $E_a|\psi\rangle$ 投影到特定 syndrome sector，之后施加恢复算子。

关键步骤：syndrome 测量坍缩了 $\{E_a\}$ 之间的叠加，但保留了逻辑信息 $|\psi\rangle$ 的叠加。

### 擦除噪声的详细分析 **[Bacon, §2.5]**

**擦除与 Pauli 噪声的等效关系** **[Bacon, §2.5]**：

一个被擦除的量子比特处于最大混合态 $I/2$。可以将其理解为以等概率 $1/4$ 施加 $\{I, X, Y, Z\}$ 中的每一个。因此：

- 擦除率 $p_e$ 对应有效 Pauli 错误率 $p_{\text{eff}} = 3p_e/4$（因为 $I$ 不算错误）
- 但由于擦除是**已知位置**的错误，纠正能力为 $d-1$（而非 $\lfloor(d-1)/2\rfloor$）

**擦除阈值推导** **[Bacon, §2.5.2]**：

对表面码（code capacity）：

$$p_{\text{th}}^{\text{erasure}} = 50\%$$

这可以用渗流理论理解：当擦除率超过 $50\%$ 时，被擦除的量子比特形成渗透路径（跨越格子），使逻辑信息不可恢复。$50\%$ 恰好是二维方格子的 bond percolation 阈值。

### 关联噪声的影响 **[Bacon, §2.6]**

Bacon 讨论了 IID 假设失效时的情况：

**空间关联** **[Bacon, §2.6.1]**：
- 串扰导致相邻量子比特的错误关联
- 对 weight-$w$ 的关联错误，有效码距可能从 $d$ 降低到 $\lfloor d/w \rfloor$

**时间关联** **[Bacon, §2.6.2]**：
- 泄漏（leakage）是持续性错误——量子比特离开计算子空间后不会自动恢复
- 需要 leakage reduction circuits（如 SWAP 到新鲜量子比特）

---

## Part 8: From Surface Code Notes — Circuit-Level Noise Details

### Hook Error 的详细分析 **[Surface Code Notes, §4.2]**

**定义** **[Surface Code Notes, §4.2]**：Hook error 是指 syndrome 提取电路中单个 CNOT 故障产生的 weight-2 关联数据错误。

**产生机制**：考虑 $Z$-stabilizer $B_f = Z_1Z_2Z_3Z_4$ 的测量电路。Ancilla 通过 4 个 CNOT 依次与 data qubits 1,2,3,4 交互。如果第 1 个 CNOT 之前 ancilla 发生 $X$ 错误，该错误通过后续 CNOT 传播到 data qubits 2,3,4 上的关联 $Z$ 错误。

**影响** **[Surface Code Notes, §4.2]**：
- Hook error 使 circuit-level 的有效码距可能比 code capacity 的码距低
- 例如，距离-3 的 non-rotated surface code 在 circuit-level 下有效码距降为 2（单个 CNOT 故障可造成 weight-2 错误跨越逻辑路径）
- **解决方案**：(1) 使用 rotated surface code（hook error 被对角排列吸收）；(2) 精心安排 CNOT 顺序（serpentine ordering）

### Time-like Errors 和 3D 解码 **[Surface Code Notes, §6.1]**

在 $d$ 轮重复 syndrome 测量中，存在两种类型的错误事件：

1. **Space-like errors**（数据错误）：产生空间方向的缺陷对
2. **Time-like errors**（测量错误）：同一位置在相邻轮次给出不同结果，产生时间方向的缺陷对

**3D 解码图** **[Surface Code Notes, §6.1]**：

将 syndrome 组织为 3D 格点 $(x, y, t)$：
- 空间边（水平/垂直）：权重 $\sim \log\frac{1-p_{\text{data}}}{p_{\text{data}}}$
- 时间边：权重 $\sim \log\frac{1-p_{\text{meas}}}{p_{\text{meas}}}$
- 对角边（hook errors）：权重由 CNOT 故障率决定

### 最终轮处理 **[Surface Code Notes, §6.4]**

在 $d$ 轮 syndrome 测量后，需要一个"完美"的最终轮来确定最终 syndrome。在实际中这通过测量所有数据量子比特实现（destructive measurement），从测量结果可以推断最终轮的 syndrome。

---

## From Steane Tutorial: Noise Decomposition and Fidelity

### Phase Decoherence as Z-Error **[Steane, p.19]**

Phase decoherence applies a random $z$-rotation to each qubit [Steane, p.19]:

$$P(\epsilon\phi) = \cos(\epsilon\phi)I + i\sin(\epsilon\phi)Z$$

This is a combination of no error ($I$) and a phase flip ($Z$). For the 3-bit phase-error-correcting code, the codewords are the Hadamard transforms of the bit-flip code: $R|000\rangle$ and $R|111\rangle$ [Steane, p.19]. The fidelity of the corrected state is $f \simeq 1 - 3p^2$ for small $p$, where $p = \langle\sin^2\epsilon\phi\rangle \simeq (\pi\epsilon)^2/3$ for $\epsilon \ll 1$ [Steane, p.20].

### Digitization of Noise **[Steane, p.10]**

Steane states the fundamental digitization principle [Steane, p.10]: any interaction between qubits and environment can be expressed as:

$$|\phi\rangle|\psi_0\rangle_e \to \sum_i (E_i|\phi\rangle)|\psi_i\rangle_e$$

where each $E_i$ is a tensor product of Pauli operators. This is completely general because the Pauli matrices form a complete set. To correct the most general noise, it suffices to correct just $X$ and $Z$ errors [Steane, p.11].

### Correlated vs Uncorrelated Noise **[Steane, p.22-23]**

Steane distinguishes two noise regimes [Steane, p.22]:

1. **Coherent errors** (shared environment): $P(t+1) \simeq (3^{t+1}\binom{n}{t+1}\epsilon^{t+1})^2$ --- the amplitudes add coherently before squaring
2. **Incoherent errors** (independent environments): $P(t+1) \simeq 3^{t+1}\binom{n}{t+1}\epsilon^{2(t+1)}$ --- probabilities add directly

For correlated (burst) errors that happen to be in the stabilizer, Steane notes one can use error-avoiding codes where the code subspace is decoupled from the environment [Steane, p.23].

---

## From Bacon: Kraus Operator Formalism for Noise Channels

### Bit-Flip Channel **[Bacon, p.49]**

The quantum bit-flip channel with Kraus operators [Bacon, p.49]:

$$E_0 = \sqrt{1-p}\;I, \quad E_1 = \sqrt{p}\;X$$

### Phase-Flip Channel **[Bacon, p.53]**

The phase-flip channel [Bacon, p.53]:

$$A_0 = \sqrt{1-p}\;I, \quad A_1 = \sqrt{p}\;Z$$

Bacon shows this is equivalent (same superoperator) to the phase damping channel with Kraus operators [Bacon, p.53-54]:

$$B_0 = \sqrt{1-q}\;I, \quad B_1 = \frac{\sqrt{q}}{2}(I+Z), \quad B_2 = \frac{\sqrt{q}}{2}(I-Z)$$

when $p/2 = q$. A code designed to correct single $Z$ errors works on this channel because syndrome measurement projects sums of errors onto individual error subspaces [Bacon, p.54].

### Quantum Error Types from Superconducting Hardware **[NordiQUEst, p.25]**

NordiQUEst catalogs the noise sources in superconducting hardware [NordiQUEst, p.25]:

| Error Source | Physical Mechanism |
|-------------|-------------------|
| $T_1$ relaxation | Energy decay $|1\rangle \to |0\rangle$ |
| $T_2$ dephasing | Loss of phase coherence |
| Gate errors | Imperfect unitary implementation |
| Measurement errors | Incorrect readout |
| Cross-talk | Interference between neighboring qubits |
| Leakage | Transition outside $\{|0\rangle, |1\rangle\}$ |
| Stray interactions | Unintended couplings during gates |
| Idle errors | Environmental decoherence while waiting |
| External noise | Electromagnetic interference, cosmic rays |

---

## From Surface Notes: Leakage and Non-Computational Errors

### Leakage Handling **[Surface Notes, p.2]**

Fowler states that errors taking the computer out of the computational basis (leakage to $|2+\rangle$ states) must be handled in hardware, as must widespread bursts of errors [Surface Notes, p.2]. For the remainder of surface code analysis, one assumes these have been addressed, allowing focus on local, random, independent computational-basis (Pauli) errors.

---

## References

- Dennis, E. et al. "Topological quantum memory." J. Math. Phys. 43, 4452 (2002).
- **[Steane]** Steane, A. M. "A Tutorial on Quantum Error Correction." Proc. Int. School of Physics "Enrico Fermi" (2006).
- **[Bacon]** Bacon, D. "Introduction to quantum error correction." Ch. 2 in *Quantum Error Correction* (Cambridge, 2013).
- **[Surface Notes]** Fowler, A. G. "Surface code quantum computation." Google Quantum AI (2025).
- **[NordiQUEst]** Lenssen, Martres, Myneni, Fuchs. "Quantum Error Correction - Theory and Hands-on." NordiQUEst (2024).
- Tuckett, D. K. et al. "Ultrahigh error threshold for surface codes with biased noise." PRL 120, 050505 (2018).
- Bonilla Ataides, J. P. et al. "The XZZX surface code." Nature Commun. 12, 2172 (2021).
- Gidney, C. et al. "Stability experiments with the surface code on a superconducting quantum processor." Nature 638, 920 (2025).
- Google Quantum AI. "Suppressing quantum errors by scaling a surface code logical qubit." Nature 614, 676 (2023).
