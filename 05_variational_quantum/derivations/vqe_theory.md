# VQE理论推导

> Variational Quantum Eigensolver: Complete Theory
> 涵盖变分原理证明、拟设设计、测量方案、参数平移规则推导、梯度估计与优化景观分析。

---

## 1. 变分原理证明 (Proof of the Variational Principle)

**定理**: 对任意归一化态 $|\psi\rangle$ 和哈密顿量 $H$，有

$$\langle\psi|H|\psi\rangle \geq E_0$$

其中 $E_0$ 是 $H$ 的最小本征值（基态能量）。

> 任意试探态的能量期望值不低于基态能量。

**证明**:

设 $H$ 的本征值分解为 $H = \sum_k E_k |E_k\rangle\langle E_k|$，其中 $E_0 \leq E_1 \leq E_2 \leq \cdots$。

将任意归一化态展开为：

$$|\psi\rangle = \sum_k \alpha_k |E_k\rangle, \quad \sum_k |\alpha_k|^2 = 1$$

则：

$$\langle\psi|H|\psi\rangle = \sum_k |\alpha_k|^2 E_k$$

由于 $E_k \geq E_0$ 对所有 $k$ 成立：

$$\sum_k |\alpha_k|^2 E_k \geq \sum_k |\alpha_k|^2 E_0 = E_0 \sum_k |\alpha_k|^2 = E_0$$

等号成立当且仅当 $|\psi\rangle$ 完全位于基态子空间中，即 $\alpha_k = 0$ 对所有 $E_k > E_0$。$\blacksquare$

**VQE的核心思想**: 通过参数化量子电路 $U(\boldsymbol{\theta})$ 制备试探态 $|\psi(\boldsymbol{\theta})\rangle = U(\boldsymbol{\theta})|0\rangle^{\otimes n}$，经典优化器调整 $\boldsymbol{\theta}$ 以最小化：

$$C(\boldsymbol{\theta}) = \langle 0^n | U^\dagger(\boldsymbol{\theta}) H U(\boldsymbol{\theta}) | 0^n \rangle$$

变分原理保证 $\min_{\boldsymbol{\theta}} C(\boldsymbol{\theta}) \geq E_0$，当拟设具有足够表达能力时可以逼近等号。

---

## 2. 拟设设计 (Ansatz Design)

### 2.1 硬件高效拟设 (Hardware-Efficient Ansatz, HEA)

$$U_{\text{HEA}}(\boldsymbol{\theta}) = \prod_{l=1}^{L} \left[\bigotimes_{i=1}^{n} R_Y(\theta_{l,i}^{(1)}) R_Z(\theta_{l,i}^{(2)}) \right] \cdot V_{\text{ent}}$$

> 硬件高效拟设直接按照硬件拓扑设计，参数量 $2nL$，但可能遭遇贫瘠高原。

其中 $V_{\text{ent}}$ 为纠缠层，通常由最近邻CNOT门组成：

$$V_{\text{ent}} = \prod_{i=1}^{n-1} \text{CNOT}_{i, i+1}$$

**优点**: 适配硬件拓扑，电路深度可控。
**缺点**: 缺乏物理先验，在大量子比特数下可能出现贫瘠高原。

### 2.2 问题启发拟设 (Problem-Inspired Ansatz)

#### 酉耦合簇拟设 (Unitary Coupled Cluster, UCC)

$$|\psi_{\text{UCC}}\rangle = e^{T - T^\dagger} |\phi_{\text{ref}}\rangle$$

其中 $T = T_1 + T_2 + \cdots$ 是簇算符：

$$T_1 = \sum_{i \in \text{occ}, a \in \text{virt}} t_i^a \, a_a^\dagger a_i, \quad T_2 = \sum_{\substack{i<j \in \text{occ} \\ a<b \in \text{virt}}} t_{ij}^{ab} \, a_a^\dagger a_b^\dagger a_j a_i$$

> UCC拟设从量子化学的耦合簇理论出发，天然保持粒子数和自旋对称性。

通常截断到单激发和双激发（UCCSD），参数数量为 $O(n_{\text{occ}}^2 n_{\text{virt}}^2)$。

#### 对称性保持拟设

如果哈密顿量具有对称性群 $\mathcal{G}$（如粒子数守恒 $[H, N] = 0$），可设计拟设使得：

$$[U(\boldsymbol{\theta}), \hat{N}] = 0 \quad \forall \boldsymbol{\theta}$$

实现方式：使用仅包含粒子数守恒门（如 $R_{XX+YY}$, SWAP类门）构建电路。

---

## 3. 测量方案：哈密顿量的Pauli分解 (Pauli Decomposition)

任意 $n$ 量子比特哈密顿量可精确展开为Pauli基：

$$H = \sum_{i=1}^{M} c_i P_i, \quad P_i \in \{I, X, Y, Z\}^{\otimes n}$$

> 将哈密顿量写成Pauli串的线性组合，每个Pauli串可直接在量子硬件上测量。

**分解方法**: 利用Pauli矩阵构成 $2^n \times 2^n$ Hermitian矩阵空间的正交基：

$$c_i = \frac{1}{2^n} \text{tr}(P_i H)$$

**测量协议**:

对每个Pauli项 $P_i = \sigma_{i_1} \otimes \sigma_{i_2} \otimes \cdots \otimes \sigma_{i_n}$：

1. 对每个量子比特 $j$，根据 $\sigma_{i_j}$ 选择测量基：
   - $Z$: 直接在计算基测量
   - $X$: 先施加 $H$ 门（Hadamard），再在计算基测量
   - $Y$: 先施加 $S^\dagger H$ 门，再在计算基测量
   - $I$: 无需测量该比特

2. 从 $N_{\text{shots}}$ 次重复测量中估计 $\langle P_i \rangle$

**分组优化**: 对易的Pauli项（$[P_i, P_j] = 0$）可以同时测量。常用分组策略：
- **Qubit-wise commutativity (QWC)**: $P_i, P_j$ 在每个比特位上对易
- **General commutativity (GC)**: 允许更一般的对易关系

分组后总代价函数为：

$$C(\boldsymbol{\theta}) = \sum_{g=1}^{G} \sum_{P_i \in \mathcal{G}_g} c_i \langle P_i \rangle_{\boldsymbol{\theta}}$$

其中 $G$ 为分组数，通常 $G \ll M$。

---

## 4. 参数平移规则：完整推导 (Parameter Shift Rule: Full Derivation)

### 4.1 设定

考虑参数化门 $U_k(\theta_k) = e^{-i\theta_k G_k / 2}$，其中生成元 $G_k$ 满足 $G_k^2 = I$（本征值 $\pm 1$）。

> 参数平移规则将解析梯度转化为两次电路求值之差，是VQE梯度计算的核心工具。

代价函数：

$$C(\theta_k) = \langle 0 | U_{\text{post}}^\dagger \, U_k^\dagger(\theta_k) \, U_{\text{pre}}^\dagger \, H \, U_{\text{pre}} \, U_k(\theta_k) \, U_{\text{post}} | 0 \rangle$$

简记为 $C(\theta_k) = \langle \phi | U_k^\dagger(\theta_k) \, A \, U_k(\theta_k) | \phi \rangle$，其中 $|\phi\rangle = U_{\text{post}}|0\rangle$，$A = U_{\text{pre}}^\dagger H U_{\text{pre}}$。

### 4.2 谱分解

由 $G_k^2 = I$，$G_k$ 的本征值为 $\pm 1$。设谱分解为：

$$G_k = \Pi_+ - \Pi_-, \quad \Pi_\pm = \frac{I \pm G_k}{2}$$

其中 $\Pi_+, \Pi_-$ 分别是 $+1, -1$ 本征空间的投影算符。

则：

$$U_k(\theta_k) = e^{-i\theta_k G_k / 2} = \cos\frac{\theta_k}{2} \, I - i\sin\frac{\theta_k}{2} \, G_k$$

### 4.3 展开代价函数

$$C(\theta_k) = \langle\phi| \left(\cos\frac{\theta_k}{2} I + i\sin\frac{\theta_k}{2} G_k\right) A \left(\cos\frac{\theta_k}{2} I - i\sin\frac{\theta_k}{2} G_k\right) |\phi\rangle$$

展开后：

$$C(\theta_k) = \cos^2\frac{\theta_k}{2} \langle\phi|A|\phi\rangle + \sin^2\frac{\theta_k}{2} \langle\phi|G_k A G_k|\phi\rangle + i\sin\frac{\theta_k}{2}\cos\frac{\theta_k}{2} \langle\phi|[G_k, A]|\phi\rangle$$

利用三角恒等式 $\cos^2\frac{\theta}{2} = \frac{1+\cos\theta}{2}$，$\sin^2\frac{\theta}{2} = \frac{1-\cos\theta}{2}$，$\sin\frac{\theta}{2}\cos\frac{\theta}{2} = \frac{\sin\theta}{2}$：

$$C(\theta_k) = \underbrace{\frac{\langle A \rangle + \langle G_k A G_k \rangle}{2}}_{A_0} + \underbrace{\frac{\langle A \rangle - \langle G_k A G_k \rangle}{2}}_{A_1} \cos\theta_k + \underbrace{\frac{i\langle [G_k, A] \rangle}{2}}_{A_2} \sin\theta_k$$

这证明了 $C(\theta_k)$ 是 $\theta_k$ 的**正弦函数**（单频率）。

### 4.4 求导

$$\frac{\partial C}{\partial \theta_k} = -A_1 \sin\theta_k + A_2 \cos\theta_k$$

### 4.5 平移求值

$$C\!\left(\theta_k + \frac{\pi}{2}\right) = A_0 + A_1 \cos\!\left(\theta_k + \frac{\pi}{2}\right) + A_2 \sin\!\left(\theta_k + \frac{\pi}{2}\right) = A_0 - A_1\sin\theta_k + A_2\cos\theta_k$$

$$C\!\left(\theta_k - \frac{\pi}{2}\right) = A_0 + A_1 \cos\!\left(\theta_k - \frac{\pi}{2}\right) + A_2 \sin\!\left(\theta_k - \frac{\pi}{2}\right) = A_0 + A_1\sin\theta_k - A_2\cos\theta_k$$

### 4.6 最终结果

$$\frac{\partial C}{\partial \theta_k} = \frac{1}{2}\left[C\!\left(\theta_k + \frac{\pi}{2}\right) - C\!\left(\theta_k - \frac{\pi}{2}\right)\right] \quad \blacksquare$$

### 4.7 推广：一般生成元

若 $G_k$ 有本征值 $\{g_1, g_2\}$（不限于 $\pm 1$），则平移量变为 $s = \frac{\pi}{2(g_1 - g_2)}$，系数变为 $\frac{g_1 - g_2}{2}$：

$$\frac{\partial C}{\partial \theta_k} = \frac{g_1 - g_2}{2} \cdot \frac{C(\theta_k + s) - C(\theta_k - s)}{2\sin((g_1 - g_2)s)}$$

---

## 5. 梯度估计：有限采样与方差分析 (Gradient Estimation under Finite Shots)

### 5.1 单Pauli项的测量方差

对单个Pauli可观测量 $P$（本征值 $\pm 1$），$N_s$ 次测量的估计：

$$\hat{\langle P \rangle} = \frac{1}{N_s}\sum_{m=1}^{N_s} p_m, \quad p_m \in \{+1, -1\}$$

方差为：

$$\text{Var}[\hat{\langle P \rangle}] = \frac{1 - \langle P \rangle^2}{N_s}$$

> 有限采样引入的统计噪声以 $1/\sqrt{N_s}$ 衰减。

### 5.2 梯度估计的方差

由参数平移规则，梯度的方差为：

$$\text{Var}\left[\frac{\widehat{\partial C}}{\partial \theta_k}\right] = \frac{1}{4}\left(\text{Var}[\hat{C}_+] + \text{Var}[\hat{C}_-]\right) = \frac{1}{4}\left(\frac{\sigma_+^2}{N_s} + \frac{\sigma_-^2}{N_s}\right)$$

其中 $\sigma_\pm^2$ 为 $C(\theta_k \pm \pi/2)$ 处代价函数的方差。

### 5.3 总测量预算

对 $p$ 个参数，每个参数需两次电路求值，每个电路对 $M$ 个Pauli项分别测量 $N_s$ 次，总测量次数为：

$$N_{\text{total}} = 2p \cdot M \cdot N_s$$

使用Pauli分组可将 $M$ 降低到 $G$ 组。精度 $\epsilon$ 的梯度估计需要 $N_s = O(1/\epsilon^2)$。

---

## 6. 经典优化景观 (Classical Optimization Landscape)

### 6.1 代价函数结构

由第4节的推导，$C(\boldsymbol{\theta})$ 关于每个参数 $\theta_k$ 是正弦函数。整体代价函数是多个正弦函数的嵌套组合——一个**三角多项式**。

### 6.2 局部极小值

VQE的代价函数景观一般是**非凸**的。存在：
- 全局最小值：对应基态（或其近似）
- 局部极小值：可能大量存在，数目随参数数指数增长
- 鞍点：高维空间中常见

### 6.3 常用优化器

| 优化器 | 类型 | 梯度需求 | 特点 |
|--------|------|----------|------|
| COBYLA | 无梯度 | 无 | 鲁棒，适合噪声环境 |
| Nelder-Mead | 无梯度 | 无 | 简单但维度扩展性差 |
| SPSA | 随机梯度 | 2次求值/步 | 适合有噪声 |
| L-BFGS-B | 拟牛顿 | 精确梯度 | 收敛快，对噪声敏感 |
| Adam | 自适应 | 梯度 | 广泛使用，动量加速 |
| QNG | 自然梯度 | 梯度+QFI | 几何感知，参数化不变 |

### 6.4 噪声对优化的影响

在NISQ设备上，测量噪声和门噪声将代价函数景观"平坦化"：

$$C_{\text{noisy}}(\boldsymbol{\theta}) \approx (1-\lambda) C_{\text{ideal}}(\boldsymbol{\theta}) + \lambda \cdot \text{tr}(H)/2^n$$

其中 $\lambda$ 与噪声强度和电路深度有关，有效地将代价函数推向平凡值 $\text{tr}(H)/2^n$。

---

## 7. 与量子化学的联系 (Connection to Quantum Chemistry)

### 7.1 分子哈密顿量

在Born-Oppenheimer近似下，电子哈密顿量为：

$$H_{\text{mol}} = \sum_{p,q} h_{pq} \, a_p^\dagger a_q + \frac{1}{2}\sum_{p,q,r,s} h_{pqrs} \, a_p^\dagger a_q^\dagger a_r a_s$$

> 分子哈密顿量由单体和双体积分构成，通过费米子-量子比特映射转化为量子电路可处理的形式。

其中 $h_{pq}, h_{pqrs}$ 为单电子和双电子积分，$a_p^\dagger, a_q$ 为费米子产生/湮灭算符。

### 7.2 费米子到量子比特映射

**Jordan-Wigner变换**:

$$a_j^\dagger \to \frac{1}{2}(X_j - iY_j) \otimes Z_{j-1} \otimes \cdots \otimes Z_0$$

**Bravyi-Kitaev变换**: 提供 $O(\log n)$ 的Pauli权重，改善Jordan-Wigner的 $O(n)$ 局域性。

映射后得到量子比特哈密顿量 $H = \sum_i c_i P_i$，Pauli项数 $M = O(n^4)$，可直接用VQE求解。

### 7.3 VQE在量子化学中的里程碑

- **H$_2$** (2比特): 首次实验演示，Peruzzo et al. (2014)
- **LiH, BeH$_2$** (6-12比特): Kandala et al., *Nature* (2017)
- **H$_2$O**: 多种拟设比较研究
- **强关联体系**: 如过渡金属化合物，经典方法困难，VQE展现潜力

---

## 8. VQA通用框架 (General VQA Framework)

> 以下内容基于 **[Cerezo et al. 2021, §2]** 的VQA综述。

### 8.1 通用代价函数 **[Cerezo et al. 2021, Eq.(1)-(2)]**

VQA的代价函数具有一般形式：

$$C(\vec{\theta}) = f\left(\{\rho_k\}, \{O_k\}, U(\vec{\theta})\right)$$

通常可表示为：

$$C(\vec{\theta}) = \sum_k f_k\left(\text{tr}[O_k U(\vec{\theta}) \rho_k U^\dagger(\vec{\theta})]\right)$$

其中 $\{\rho_k\}$ 是训练数据集的输入态，$\{O_k\}$ 是可观测量集合，$U(\vec{\theta})$ 是参数化酉算符。

### 8.2 通用拟设结构 **[Cerezo et al. 2021, Eq.(3)-(4)]**

参数化酉可表示为 $L$ 个顺序作用的酉乘积：

$$U(\vec{\theta}) = U_L(\vec{\theta}_L) \cdots U_2(\vec{\theta}_2) U_1(\vec{\theta}_1)$$

其中每层：

$$U_l(\theta_l) = \prod_m e^{-i\theta_m H_m} W_m$$

$W_m$ 是非参数化酉，$H_m$ 是Hermitian生成元。

### 8.3 代价函数设计准则 **[Cerezo et al. 2021, §2.1]**

良好的VQA代价函数应满足：
1. **忠实性 (Faithfulness)**：$C(\vec{\theta})$ 的最小值对应问题的解
2. **可高效估计 (Efficient estimation)**：通过量子计算机测量可高效估计
3. **操作意义 (Operational meaning)**：较小的代价值指示更好的解质量
4. **可训练性 (Trainability)**：参数 $\vec{\theta}$ 可以被高效优化

---

## 9. 拟设的表达能力理论 (Ansatz Expressibility Theory)

> 基于 **[Tilly et al. 2022, §6]** 和 **[Cerezo et al. 2021, §2.2]**。

### 9.1 表达能力的严格量化 **[Tilly et al. 2022, §6, Eq.]**

设 $\mathbb{U}$ 为拟设可达到的酉集合，$\mathcal{U}(N)$ 为完整酉群。表达能力通过以下超算符量化 **[Tilly et al. 2022, §6, Eq.(expressibility)]**：

$$\mathcal{A}_{\mathbb{U}}(\cdot) := \int_{\mathcal{U}(N)} d\mu(V) V^{\otimes 2}(\cdot)(V^\dagger)^{\otimes 2} - \int_{\mathbb{U}} dU \, U^{\otimes 2}(\cdot)(U^\dagger)^{\otimes 2}$$

表达能力度量：

$$\varepsilon_{\mathbb{U}}^{\rho} := \|\mathcal{A}_{\mathbb{U}}(\rho^{\otimes 2})\|_2, \quad \varepsilon_{\mathbb{U}}^{\hat{P}} := \|\mathcal{A}_{\mathbb{U}}(\hat{P}^{\otimes 2})\|_2$$

若 $\varepsilon = 0$，拟设是最大表达的（2-设计）。

### 9.2 表达能力与可训练性的逆关系 **[Tilly et al. 2022, §6, Holmes et al.]**

**定理** (Holmes et al. 2022, 经由 **[Tilly et al. 2022, §6]**): 梯度方差的上界：

$$\text{Var}[\partial_{\theta_i} E] \leq \frac{g(\rho, \hat{P}, U)}{2^{2N} - 1} + f(\varepsilon_L^{\hat{P}}, \varepsilon_R^{\rho})$$

其中：

$$f(\varepsilon_x, \varepsilon_y) := 4\varepsilon_x \varepsilon_y + \frac{2^{N+2}(\varepsilon_x \|\hat{P}\|_2^2 + \varepsilon_y \|\rho\|_2^2)}{2^{2N} - 1}$$

当 $N \to \infty$ 时，上界趋向 $O(\varepsilon_L^{\hat{P}} \varepsilon_R^{\rho})$。高表达能力（低 $\varepsilon$）意味着低梯度方差上界，即可训练性受限。

### 9.3 拟设深度-参数-纠缠门的缩放比较 **[Tilly et al. 2022, §6, Table]**

| 拟设 | 深度 | 参数数 | 纠缠门数 |
|------|------|--------|---------|
| HEA | $O(L)$ | $O(NL)$ | $O((N-1)L)$ |
| UCCSD | $O((N-m)^2 m \tau)$ | $O((N-m)^2 m^2 \tau)$ | $O(\tilde{q} N^4 \tau)$ |
| k-UpCCGSD | $O(kN\tau)$ | $O(k\tau N^2/4)$ | $O(k\tau \tilde{q} N^2/2)$ |
| HVA | $O(\tilde{C}L)$ | $O(\tilde{C}L)$ | $O(\tilde{q}CL)$ |

其中 $N$ 为量子比特数，$m$ 为电子数，$\tau$ 为Trotter步数，$\tilde{q}$ 为平均Pauli权重，$C$ 为哈密顿量项数。**[Tilly et al. 2022, §6, Table 1]**

---

## 10. 求解激发态的VQE变体 (VQE Variants for Excited States)

> 基于 **[Cerezo et al. 2021, §3.1]**。

### 10.1 正交约束VQE **[Cerezo et al. 2021, §3.1]**

获得近似基态 $|\tilde{\psi}_G\rangle$ 后，构造修正哈密顿量：

$$H' = H + a |\tilde{\psi}_G\rangle\langle\tilde{\psi}_G|$$

其中 $a$ 远大于基态-第一激发态能隙。$H'$ 的基态即为 $H$ 的第一激发态。迭代此过程可获得更高激发态。

### 10.2 子空间展开方法 **[Cerezo et al. 2021, §3.1]**

从基态 $|\tilde{\psi}_G\rangle$ 生成子空间 $\{|\psi_k\rangle = \sigma_k |\tilde{\psi}_G\rangle\}$，将候选本征态展开为 $|E\rangle = \sum_k \alpha_k |\psi_k\rangle$。系数 $\vec{\alpha}$ 通过广义本征值问题求解：

$$H_{\text{sub}} \vec{\alpha} = E \, S \vec{\alpha}$$

其中 $H_{k,j} = \langle\psi_k|H|\psi_j\rangle$，$S_{k,j} = \langle\psi_k|\psi_j\rangle$。

### 10.3 子空间VQE **[Cerezo et al. 2021, §3.1]**

加权子空间VQE的代价函数：

$$C(\vec{\theta}) = \sum_{i=0}^m w_i \langle\varphi_i| U^\dagger(\vec{\theta}) H U(\vec{\theta}) |\varphi_i\rangle$$

其中权重 $w_0 > w_1 > \cdots > w_m$，$\{|\varphi_i\rangle\}$ 为正交初始态。优化后，$U(\vec{\theta}^*)|\varphi_i\rangle$ 按能量递增排列近似对应 $H$ 的本征态。

---

## 11. 测量效率优化 (Measurement Efficiency)

> 基于 **[Cerezo et al. 2021, §4.2]** 和 **[Tilly et al. 2022, §7]**。

### 11.1 对易集分组 **[Cerezo et al. 2021, §4.2]**

将Pauli项分为对易子集以同时测量。QWC（qubit-wise commuting）分组：两个Pauli串在每个比特位上对易。一般对易分组可将测量次数从 $O(N^4)$ 降至 $O(N^3)$。**[Cerezo et al. 2021, §4.2]**

对费米子系统，利用双电子积分张量的分解，缩放可进一步降至 $O(N^2)$ 甚至线性。**[Cerezo et al. 2021, §4.2, Huggins et al.]**

### 11.2 最优采样分配 **[Cerezo et al. 2021, §4.2]**

对哈密顿量 $H = \sum_i c_i \sigma_i$，最优shot分配为给每个Pauli算符分配正比于 $|c_i|\sqrt{\text{Var}(\sigma_i)}$ 的测量次数。**[Cerezo et al. 2021, §4.2, Rubin et al.]**

### 11.3 经典阴影 (Classical Shadows) **[Cerezo et al. 2021, §4.2]**

通过随机Pauli测量构建量子态的经典近似表示，可使测量次数与Pauli项数呈**对数**关系缩放。**[Cerezo et al. 2021, §4.2, Huang et al. 2020]**

---

## 12. VQE优化的NP-硬性 (NP-hardness of VQE Optimization)

> **[Tilly et al. 2022, §7]** 与 **[Cerezo et al. 2021, §2.4]**

**定理** (Bittel & Kliesch 2021, 引自 **[Tilly et al. 2022, §7]**): 变分量子拟设的优化问题是NP-hard的——至少存在某些问题实例使得找到精确最优解不可行。

这意味着高效的优化策略（量子感知优化器）对VQE的实用性至关重要，而非期望找到全局最优。

---

## 13. 噪声对VQE的影响 (Impact of Noise on VQE)

> 基于 **[Cerezo et al. 2021, §4.3]**。

### 13.1 噪声对训练的影响

在非相干噪声下，代价函数景观围绕最大混合态的值指数集中 **[Cerezo et al. 2021, §4.3]**：

$$C_{\text{noisy}}(\vec{\theta}) \approx (1 - \lambda)^{nL} C_{\text{ideal}}(\vec{\theta}) + [1 - (1-\lambda)^{nL}] \cdot \frac{\text{tr}(H)}{2^n}$$

### 13.2 VQE的天然噪声鲁棒性

**相干噪声鲁棒性** **[Cerezo et al. 2021, §4.3]**：VQA对相干参数化误差天然具有弹性——若物理实现导致 $U(\vec{\theta})$ 变为 $U(\vec{\theta} + \vec{\delta})$，优化器可在训练中自动校准。

**最优参数鲁棒性 (OPR)** **[Cerezo et al. 2021, §4.3, Sharma et al.]**：某些VQA（如量子编译）展现出噪声代价函数的全局最小值仍对应无噪声代价函数的全局最小值。
