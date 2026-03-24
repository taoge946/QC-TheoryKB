# Quantum Channels and Kraus Representation (量子信道与 Kraus 表示)

> **Tags**: `quantum-channel`, `kraus`, `cptp`, `noise-model`

## Statement (Kraus Representation Theorem)

任何从 $d_{\text{in}}$ 维系统到 $d_{\text{out}}$ 维系统的完全正迹守恒（CPTP）映射 $\mathcal{E}$，都可以表示为 Kraus 形式：

$$\mathcal{E}(\rho) = \sum_{k=1}^{r} E_k \, \rho \, E_k^\dagger$$
**[N&C, Theorem 8.1, p.368]** **[Preskill, Ch.3, &sect;3.2.1, pp.11-13]**

其中 Kraus 算子 $E_k$ 是 $d_{\text{out}} \times d_{\text{in}}$ 的矩阵，满足完备性关系：

$$\sum_{k=1}^{r} E_k^\dagger E_k = I_{d_{\text{in}}}$$
**[N&C, Eq.(8.8), p.360]**

反过来，任何满足上述完备性关系的 Kraus 算子集合都定义了一个 CPTP 映射。

## Prerequisites

- **密度矩阵**: 纯态、混合态、$\rho \geq 0$，$\text{Tr}(\rho) = 1$（参见 [density_matrix_formalism.md](density_matrix_formalism.md)）
- **张量积**: $\mathcal{H}_S \otimes \mathcal{H}_E$，分系统、偏迹
- **幺正演化**: $U\rho U^\dagger$，$UU^\dagger = U^\dagger U = I$

---

## Derivation

### Step 1: 物理图像 —— 系统-环境模型 **[N&C, Section 8.2.2, p.358]** **[Preskill, Ch.3, &sect;3.2, pp.11-12]**

量子信道的物理起源是：系统 $S$ 与环境 $E$ 发生相互作用后，我们只观察系统 $S$。

整个过程分三步：

1. **初始化环境**：环境处于某个纯态 $|0\rangle_E$
2. **联合幺正演化**：系统+环境一起经历幺正演化 $U_{SE}$
3. **丢弃环境**：对环境求偏迹

$$\mathcal{E}(\rho_S) = \text{Tr}_E\left[U_{SE}(\rho_S \otimes |0\rangle\langle 0|_E)U_{SE}^\dagger\right]$$
**[N&C, Eq.(8.4), p.358]** **[Preskill, Ch.3, &sect;3.2.1, Eq.(3.31), p.12]**

**为什么环境初态可以取纯态**？如果环境初态是混合态 $\sigma_E = \sum_j q_j|\phi_j\rangle\langle\phi_j|$，我们总可以引入一个更大的"超级环境" $E'$，使得 $\sigma_E = \text{Tr}_{E'}(|\Psi\rangle\langle\Psi|_{EE'})$，然后把 $E$ 和 $E'$ 合并看作新的环境，其初态又是纯态。所以取纯态不失一般性。

### Step 2: 从幺正演化推导 Kraus 形式

设环境 $E$ 的 Hilbert 空间维数为 $d_E$，选一组标准正交基 $\{|e_k\rangle_E\}_{k=0}^{d_E-1}$。

将偏迹展开：

$$\mathcal{E}(\rho_S) = \text{Tr}_E\left[U_{SE}(\rho_S \otimes |0\rangle\langle 0|_E)U_{SE}^\dagger\right]$$

$$= \sum_{k=0}^{d_E-1} \langle e_k|_E \, U_{SE} \, (\rho_S \otimes |0\rangle\langle 0|_E) \, U_{SE}^\dagger \, |e_k\rangle_E$$

**关键步骤**：定义 Kraus 算子

$$E_k \equiv \langle e_k|_E \, U_{SE} \, |0\rangle_E$$
**[N&C, Eq.(8.5), p.359]** **[Preskill, Ch.3, &sect;3.2.1, Eq.(3.33), p.12]**

这个 $E_k$ 是一个**作用在系统 $S$ 上的算子**。更明确地说，对系统 $S$ 的任意态 $|\psi\rangle_S$：

$$E_k|\psi\rangle_S = \langle e_k|_E \, U_{SE} \, (|\psi\rangle_S \otimes |0\rangle_E)$$

这是从 $\mathcal{H}_S$ 到 $\mathcal{H}_S$ 的线性映射（我们取了环境基矢的"矩阵元"）。

### Step 3: 代入得到 Kraus 形式

将 $E_k$ 的定义代回：

$$\mathcal{E}(\rho_S) = \sum_k \langle e_k|_E \, U_{SE} \, |0\rangle_E \;\; \rho_S \;\; \langle 0|_E \, U_{SE}^\dagger \, |e_k\rangle_E$$

注意这里要仔细处理张量积结构。对 $\rho_S \otimes |0\rangle\langle 0|_E$ 的偏迹：

$$\sum_k \langle e_k|_E \left[U_{SE}(\rho_S \otimes |0\rangle\langle 0|_E)U_{SE}^\dagger\right] |e_k\rangle_E$$

$$= \sum_k \left(\langle e_k|_E U_{SE} |0\rangle_E\right) \rho_S \left(\langle 0|_E U_{SE}^\dagger |e_k\rangle_E\right)$$

$$= \sum_k E_k \, \rho_S \, E_k^\dagger$$

所以：

$$\boxed{\mathcal{E}(\rho_S) = \sum_k E_k \, \rho_S \, E_k^\dagger}$$
**[N&C, Theorem 8.1, p.368]** **[Preskill, Ch.3, &sect;3.2.1, Eq.(3.34), p.12]**

### Step 4: 完备性条件的推导

信道必须保迹（概率守恒），即 $\text{Tr}[\mathcal{E}(\rho)] = \text{Tr}(\rho)$ 对所有 $\rho$ 成立。

$$\text{Tr}\left[\sum_k E_k \rho E_k^\dagger\right] = \sum_k \text{Tr}(E_k \rho E_k^\dagger)$$

利用迹的循环性 $\text{Tr}(ABC) = \text{Tr}(CAB)$：

$$= \sum_k \text{Tr}(E_k^\dagger E_k \rho) = \text{Tr}\left[\left(\sum_k E_k^\dagger E_k\right)\rho\right]$$

要让这对所有 $\rho$ 等于 $\text{Tr}(\rho) = \text{Tr}(I\rho)$，必须有：

$$\boxed{\sum_k E_k^\dagger E_k = I}$$
**[N&C, Eq.(8.8), p.360]** **[Preskill, Ch.3, &sect;3.2.1, p.13]**

**从物理推导验证**：也可以从 $U_{SE}$ 的幺正性直接验证：

$$\sum_k E_k^\dagger E_k = \sum_k \langle 0|_E U_{SE}^\dagger |e_k\rangle_E \langle e_k|_E U_{SE} |0\rangle_E$$

$$= \langle 0|_E U_{SE}^\dagger \left(\sum_k |e_k\rangle_E\langle e_k|_E\right) U_{SE} |0\rangle_E$$

$$= \langle 0|_E U_{SE}^\dagger \cdot I_E \cdot U_{SE} |0\rangle_E = \langle 0|_E I_{SE} |0\rangle_E = I_S \qquad \checkmark$$

### Step 5: 完全正性（CP）的含义 **[N&C, Box 8.2, p.368]** **[Preskill, Ch.3, &sect;3.2.6, pp.18-19]**

**正性（Positivity）**：如果 $\rho \geq 0$，则 $\mathcal{E}(\rho) \geq 0$。

这对 Kraus 形式显然成立：对任意 $|\phi\rangle$，

$$\langle\phi|\mathcal{E}(\rho)|\phi\rangle = \sum_k \langle\phi|E_k\rho E_k^\dagger|\phi\rangle = \sum_k \langle\phi_k|\rho|\phi_k\rangle \geq 0$$

其中 $|\phi_k\rangle = E_k^\dagger|\phi\rangle$，而 $\langle\phi_k|\rho|\phi_k\rangle \geq 0$ 因为 $\rho \geq 0$。

**完全正性（Complete Positivity）**：不仅 $\mathcal{E}$ 本身是正的，而且 $\mathcal{E}$ 与任意恒等映射的张量积 $I_R \otimes \mathcal{E}$ 也是正的。

$$\rho_{RS} \geq 0 \implies (I_R \otimes \mathcal{E})(\rho_{RS}) \geq 0$$

**为什么需要"完全"正性**？因为系统可能与参考系统 $R$ 纠缠。如果 $\mathcal{E}$ 仅是正但不是完全正，那么当系统与参考纠缠时，映射可能把合法的密度矩阵变成非法的（含负特征值的）。转置映射 $T(\rho) = \rho^T$ 就是一个正但不完全正的例子。

Kraus 形式自动保证完全正性：

$$(I_R \otimes \mathcal{E})(\rho_{RS}) = \sum_k (I_R \otimes E_k) \rho_{RS} (I_R \otimes E_k)^\dagger$$

这仍然是 Kraus 形式，所以自动正半定。

### Step 6: Choi-Jamiołkowski 同构

信道 $\mathcal{E}$ 与一个矩阵（Choi 矩阵）之间存在一一对应。定义最大纠缠态：

$$|\Phi^+\rangle = \frac{1}{\sqrt{d}}\sum_{i=0}^{d-1}|i\rangle|i\rangle$$

**Choi 矩阵**：

$$J(\mathcal{E}) = d \cdot (I \otimes \mathcal{E})(|\Phi^+\rangle\langle\Phi^+|) = \sum_{i,j=0}^{d-1} |i\rangle\langle j| \otimes \mathcal{E}(|i\rangle\langle j|)$$

**推导第二个等号**：

$$d \cdot (I \otimes \mathcal{E})(|\Phi^+\rangle\langle\Phi^+|) = d \cdot (I \otimes \mathcal{E})\left(\frac{1}{d}\sum_{i,j}|i\rangle\langle j| \otimes |i\rangle\langle j|\right)$$

$$= \sum_{i,j} |i\rangle\langle j| \otimes \mathcal{E}(|i\rangle\langle j|)$$

**Choi 定理** **[N&C, pp.369-370]** **[Preskill, Ch.3, &sect;3.3.1, pp.20-22]**：$\mathcal{E}$ 是完全正的当且仅当 $J(\mathcal{E}) \geq 0$（正半定）。

**与 Kraus 算子的关系**：对 $J(\mathcal{E})$ 进行特征值分解：

$$J(\mathcal{E}) = \sum_k \lambda_k |v_k\rangle\langle v_k|$$

其中 $\lambda_k \geq 0$（因为 $J \geq 0$）。将每个 $|v_k\rangle$（一个 $d^2$ 维向量）重塑为 $d \times d$ 矩阵，得到的 $\sqrt{\lambda_k}$ 乘以该矩阵就是 Kraus 算子 $E_k$。

### Step 7: 示例 —— 去极化信道（Depolarizing Channel） **[N&C, Eq.(8.101), p.378]** **[Preskill, Ch.3, &sect;3.4.2, pp.27-31]**

去极化信道以概率 $p$ 将态替换为最大混合态：

$$\mathcal{E}_{\text{dep}}(\rho) = (1-p)\rho + p\frac{I}{2}$$

**找 Kraus 算子**：利用恒等式 $\frac{I}{2} = \frac{1}{4}(\rho + \sigma_x\rho\sigma_x + \sigma_y\rho\sigma_y + \sigma_z\rho\sigma_z)$。

这个恒等式可以直接验证：对任意单比特密度矩阵 $\rho = \frac{1}{2}(I + \vec{r}\cdot\vec{\sigma})$，

$$\sigma_i \rho \sigma_i = \frac{1}{2}(\sigma_i I \sigma_i + r_x\sigma_i\sigma_x\sigma_i + r_y\sigma_i\sigma_y\sigma_i + r_z\sigma_i\sigma_z\sigma_i)$$

利用 $\sigma_i\sigma_j\sigma_i = -\sigma_j$（$i\neq j$）和 $\sigma_i^2 = I$：

当 $i = x$：$\sigma_x\rho\sigma_x = \frac{1}{2}(I + r_x\sigma_x - r_y\sigma_y - r_z\sigma_z)$

当 $i = y$：$\sigma_y\rho\sigma_y = \frac{1}{2}(I - r_x\sigma_x + r_y\sigma_y - r_z\sigma_z)$

当 $i = z$：$\sigma_z\rho\sigma_z = \frac{1}{2}(I - r_x\sigma_x - r_y\sigma_y + r_z\sigma_z)$

把 $\rho$ 加上这三项，所有 $\sigma_i$ 项都抵消了：

$$\rho + \sigma_x\rho\sigma_x + \sigma_y\rho\sigma_y + \sigma_z\rho\sigma_z = 4 \cdot \frac{I}{2} = 2I$$

所以 $\frac{I}{2} = \frac{1}{4}(\rho + \sigma_x\rho\sigma_x + \sigma_y\rho\sigma_y + \sigma_z\rho\sigma_z)$。

代入去极化信道：

$$\mathcal{E}_{\text{dep}}(\rho) = (1-p)\rho + \frac{p}{4}(\rho + \sigma_x\rho\sigma_x + \sigma_y\rho\sigma_y + \sigma_z\rho\sigma_z)$$

$$= \left(1-\frac{3p}{4}\right)\rho + \frac{p}{4}(\sigma_x\rho\sigma_x + \sigma_y\rho\sigma_y + \sigma_z\rho\sigma_z)$$

所以 Kraus 算子为：

$$E_0 = \sqrt{1-\frac{3p}{4}}\; I, \quad E_1 = \frac{\sqrt{p}}{2}\;\sigma_x, \quad E_2 = \frac{\sqrt{p}}{2}\;\sigma_y, \quad E_3 = \frac{\sqrt{p}}{2}\;\sigma_z$$

**验证完备性**：

$$E_0^\dagger E_0 + E_1^\dagger E_1 + E_2^\dagger E_2 + E_3^\dagger E_3 = \left(1-\frac{3p}{4}\right)I + 3\cdot\frac{p}{4}I = I \quad \checkmark$$

### Step 8: 示例 —— 退相干信道（Dephasing Channel） **[N&C, Eq.(8.92-8.93), p.377]** **[Preskill, Ch.3, &sect;3.4.1, pp.24-27]**

退相干信道以概率 $p$ 发生 $Z$ 错误：

$$\mathcal{E}_{\text{deph}}(\rho) = (1-p)\rho + p\,\sigma_z\rho\sigma_z$$

Kraus 算子：

$$E_0 = \sqrt{1-p}\;I, \qquad E_1 = \sqrt{p}\;\sigma_z$$

**效果**：写成矩阵形式，如果 $\rho = \begin{pmatrix}a & b \\ b^* & d\end{pmatrix}$，则

$$\mathcal{E}_{\text{deph}}(\rho) = \begin{pmatrix}a & (1-2p)b \\ (1-2p)b^* & d\end{pmatrix}$$

对角元（population）不变，非对角元（coherence）衰减了 $(1-2p)$ 倍。这就是"退相干"的含义——相干性逐渐消失。

### Step 9: 示例 —— 振幅阻尼信道（Amplitude Damping Channel） **[N&C, Eq.(8.87-8.88), p.376]** **[Preskill, Ch.3, &sect;3.4.3, pp.31-33]**

振幅阻尼描述自发辐射过程（$|1\rangle \to |0\rangle$ 的衰变，概率为 $\gamma$）：

$$E_0 = \begin{pmatrix}1 & 0 \\ 0 & \sqrt{1-\gamma}\end{pmatrix}, \qquad E_1 = \begin{pmatrix}0 & \sqrt{\gamma} \\ 0 & 0\end{pmatrix}$$

**验证完备性**：

$$E_0^\dagger E_0 + E_1^\dagger E_1 = \begin{pmatrix}1&0\\0&1-\gamma\end{pmatrix} + \begin{pmatrix}0&0\\0&\gamma\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I \quad \checkmark$$

**效果**：

$$\mathcal{E}_{\text{AD}}\begin{pmatrix}a & b \\ b^* & d\end{pmatrix} = \begin{pmatrix}a + \gamma d & \sqrt{1-\gamma}\;b \\ \sqrt{1-\gamma}\;b^* & (1-\gamma)d\end{pmatrix}$$

$|1\rangle$ 态的概率（$d$）以速率 $\gamma$ 流向 $|0\rangle$ 态的概率（$a$），同时相干性衰减。当 $\gamma = 1$ 时，所有态都变成 $|0\rangle\langle 0|$——系统完全弛豫到基态。

### Step 10: Kraus 表示的非唯一性

**重要事实**：同一个信道可以有不同的 Kraus 表示。

如果 $\{E_k\}$ 和 $\{F_j\}$ 都是同一个信道 $\mathcal{E}$ 的 Kraus 算子，则它们之间通过一个幺正矩阵 $u_{jk}$ 联系 **[N&C, Theorem 8.2, p.373]** **[Preskill, Ch.3, &sect;3.2.1, pp.12-13]**：

$$F_j = \sum_k u_{jk} E_k$$

其中 $(u_{jk})$ 是幺正矩阵（可能需要补零使两组算子个数相同）。

**物理意义**：不同的 Kraus 表示对应于对环境进行不同基矢下的"测量"（不同的偏迹分解方式），但最终的信道效果相同。

---

## Summary

| 概念 | 表达式 | 物理意义 |
|------|--------|---------|
| 系统-环境模型 | $\mathcal{E}(\rho) = \text{Tr}_E[U(\rho \otimes \|0\rangle\langle 0\|)U^\dagger]$ | 噪声的物理起源 |
| Kraus 表示 | $\mathcal{E}(\rho) = \sum_k E_k\rho E_k^\dagger$ | CPTP 映射的算子和形式 |
| 完备性条件 | $\sum_k E_k^\dagger E_k = I$ | 迹守恒（概率守恒） |
| Choi 矩阵 | $J(\mathcal{E}) \geq 0$ | 判断完全正性 |
| 去极化 | 态 → 最大混合态 | 各向同性噪声 |
| 退相干 | 非对角元衰减 | 相干性丧失 |
| 振幅阻尼 | $\|1\rangle \to \|0\rangle$ 衰变 | 能量弛豫 |

---

## Nielsen & Chuang: Theorems and Formal Results

### Postulate (Quantum Operations) **[Nielsen & Chuang, Postulate, p.358]**
The general dynamics of a quantum system (including open systems interacting with an environment) is described by a quantum operation: a completely positive, trace-preserving (CPTP) linear map $\mathcal{E}$ acting on density operators.

### Theorem 8.1 (Operator-Sum Representation / Kraus Representation) **[Nielsen & Chuang, Theorem 8.1, p.368]**
The map $\mathcal{E}$ satisfies axioms A1 (trace condition), A2 (convex-linearity), and A3 (complete positivity) if and only if $\mathcal{E}(\rho) = \sum_i E_i \rho E_i^\dagger$ for some set of operators $\{E_i\}$ which map the input Hilbert space to the output Hilbert space, and $\sum_i E_i^\dagger E_i \leq I$.

**Proof (forward direction)** **[Nielsen & Chuang, p.368]**: Suppose $\mathcal{E}(\rho) = \sum_i E_i \rho E_i^\dagger$. Complete positivity follows because for any positive operator $A$ on extended system $RQ$: $\langle\psi|(I_R \otimes E_i)A(I_R \otimes E_i^\dagger)|\psi\rangle = \langle\phi_i|A|\phi_i\rangle \geq 0$ where $|\phi_i\rangle \equiv (I_R \otimes E_i^\dagger)|\psi\rangle$.

**Proof (reverse direction)** **[Nielsen & Chuang, pp.369-370]**: Introduce system $R$ with same dimension as $Q$. Define $|a\rangle \equiv \sum_i |i_R\rangle|i_Q\rangle$ (unnormalized maximally entangled state) and $\sigma \equiv (I_R \otimes \mathcal{E})(|a\rangle\langle a|)$. The operator $\sigma$ completely specifies $\mathcal{E}$: for any $|\psi\rangle = \sum_j \psi_j |j_Q\rangle$, defining $|\tilde{\psi}\rangle \equiv \sum_j \psi_j^* |j_R\rangle$, one obtains $\langle\tilde{\psi}|\sigma|\tilde{\psi}\rangle = \mathcal{E}(|\psi\rangle\langle\psi|)$. Decomposing $\sigma = \sum_i |s_i\rangle\langle s_i|$ and defining $E_i(|\psi\rangle) \equiv \langle\tilde{\psi}|s_i\rangle$ yields the operator-sum form.

### Completeness Relation **[Nielsen & Chuang, Eq. 8.8, p.360]**
The trace-preserving condition $\text{Tr}[\mathcal{E}(\rho)] = 1$ for all $\rho$ is equivalent to:
$$\sum_k E_k^\dagger E_k = I$$

### Theorem 8.2 (Unitary Freedom in Operator-Sum Representation) **[Nielsen & Chuang, Theorem 8.2, p.373]**
The sets $\{E_i\}$ and $\{F_j\}$ generate the same quantum operation $\mathcal{E}$ if and only if $E_i = \sum_j u_{ij} F_j$ where $u_{ij}$ is a unitary matrix (with zero-padding if necessary). This is the channel analogue of Theorem 2.6 for ensemble freedom.

### Theorem 8.3 (Maximum Number of Operation Elements) **[Nielsen & Chuang, Theorem 8.3, p.374]**
All quantum operations $\mathcal{E}$ on a system of Hilbert space dimension $d$ can be generated by an operator-sum representation containing at most $d^2$ elements: $\mathcal{E}(\rho) = \sum_{k=1}^M E_k \rho E_k^\dagger$, where $1 \leq M \leq d^2$.

**Proof sketch** **[Nielsen & Chuang, Exercise 8.10, p.374]**: Define $W_{jk} \equiv \text{Tr}(E_j^\dagger E_k)$. This matrix is Hermitian and of rank at most $d^2$ (since operators on a $d$-dimensional space form a $d^2$-dimensional vector space). Diagonalizing $W$ via a unitary $u$ gives a new set of at most $d^2$ non-zero operation elements.

### Choi-Jamiolkowski Isomorphism **[Nielsen & Chuang, pp.369-370]**
The Choi matrix $\sigma = (I_R \otimes \mathcal{E})(|a\rangle\langle a|)$ completely specifies the quantum operation $\mathcal{E}$. A map $\mathcal{E}$ is completely positive if and only if $\sigma \geq 0$.

### Definition: Complete Positivity **[Nielsen & Chuang, Box 8.2, p.368]**
A map $\mathcal{E}$ is *completely positive* if $(I_R \otimes \mathcal{E})(\rho_{RQ}) \geq 0$ for every positive operator $\rho_{RQ}$ on any extended system $RQ$. This is strictly stronger than mere positivity. The transpose map $T(\rho) = \rho^T$ is an example of a positive but not completely positive map.

### Common Noise Channels **[Nielsen & Chuang, Section 8.3.3-8.3.5, pp.376-382]**

**Depolarizing Channel** **[Nielsen & Chuang, Eq. 8.101, p.378]**:
$$\mathcal{E}(\rho) = \frac{p}{2}I + (1-p)\rho = (1-p)\rho + \frac{p}{3}(X\rho X + Y\rho Y + Z\rho Z)$$
(Note: N&C use a slightly different parametrization; the second form uses $p' = 3p/4$.)

**Phase Damping Channel** **[Nielsen & Chuang, Eq. 8.92-8.93, p.377]**:
$$E_0 = \begin{pmatrix}1 & 0 \\ 0 & \sqrt{1-\lambda}\end{pmatrix}, \quad E_1 = \begin{pmatrix}0 & 0 \\ 0 & \sqrt{\lambda}\end{pmatrix}$$

**Amplitude Damping Channel** **[Nielsen & Chuang, Eq. 8.87-8.88, p.376]**:
$$E_0 = \begin{pmatrix}1 & 0 \\ 0 & \sqrt{1-\gamma}\end{pmatrix}, \quad E_1 = \begin{pmatrix}0 & \sqrt{\gamma} \\ 0 & 0\end{pmatrix}$$
Models the process of energy dissipation (spontaneous emission from $|1\rangle$ to $|0\rangle$).

### Axiomatic Approach **[Nielsen & Chuang, Section 8.2.4, p.363]**
N&C present three equivalent descriptions of quantum operations:
1. **System-environment model** (unitary dilation + partial trace)
2. **Operator-sum representation** (Kraus form)
3. **Axiomatic approach**: $\mathcal{E}$ is a valid quantum operation iff (A1) $\text{Tr}[\mathcal{E}(\rho)]$ is a probability, (A2) $\mathcal{E}$ is convex-linear, (A3) $\mathcal{E}$ is completely positive.

The equivalence of these three descriptions is one of the central results of Chapter 8.

### Master Equation **[Nielsen & Chuang, Section 8.4, p.383]**
For Markovian open quantum systems, the Lindblad master equation gives the continuous-time evolution:
$$\frac{d\rho}{dt} = -i[H, \rho] + \sum_k \left(L_k \rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\}\right)$$
where $H$ is the system Hamiltonian and $L_k$ are Lindblad (jump) operators. This is the infinitesimal generator of a quantum dynamical semigroup.

---

## Preskill: Theorems and Formal Results (Chapter 3)

### Definition: Quantum Channel as TPCP Map **[Preskill, Ch.3, §3.2, pp.11-12]**
Preskill defines a quantum channel (superoperator) $\mathcal{E}$ as a **trace-preserving completely positive** (TPCP) map. The three properties are derived from physical requirements:
1. **Linearity**: $\mathcal{E}$ is linear on the space of operators (follows from the linearity of quantum mechanics)
2. **Complete positivity**: $(I_R \otimes \mathcal{E})(\rho_{RA}) \geq 0$ for any reference system $R$ (ensures physical states remain physical even when system is entangled)
3. **Trace preservation**: $\text{Tr}(\mathcal{E}(\rho)) = \text{Tr}(\rho)$ (probability conservation)

### Operator-Sum (Kraus) Representation **[Preskill, Ch.3, §3.2.1, pp.11-13]**
**Theorem**: Every TPCP map $\mathcal{E}$ admits an operator-sum representation:
$$\mathcal{E}(\rho) = \sum_\mu M_\mu \rho M_\mu^\dagger, \qquad \sum_\mu M_\mu^\dagger M_\mu = I$$

**Derivation** [Preskill, Ch.3, §3.2]: The system $A$ interacts unitarily with environment $E$ (initially in state $|0\rangle_E$):
$$\mathcal{E}(\rho_A) = \text{Tr}_E[U_{AE}(\rho_A \otimes |0\rangle\langle 0|_E)U_{AE}^\dagger]$$

Introducing an orthonormal basis $\{|\mu\rangle_E\}$ for the environment:
$$= \sum_\mu \langle\mu|_E U_{AE}|0\rangle_E \;\rho_A\; \langle 0|_E U_{AE}^\dagger|\mu\rangle_E = \sum_\mu M_\mu \rho_A M_\mu^\dagger$$

where $M_\mu \equiv \langle\mu|_E U_{AE}|0\rangle_E$ are the Kraus operators.

The completeness relation $\sum_\mu M_\mu^\dagger M_\mu = I$ follows from unitarity of $U_{AE}$ and completeness of $\{|\mu\rangle_E\}$.

### Unitary Freedom in Kraus Representation **[Preskill, Ch.3, §3.2.1, pp.12-13]**
**Theorem**: Two sets of Kraus operators $\{M_\mu\}$ and $\{N_\nu\}$ represent the same channel iff:
$$M_\mu = \sum_\nu V_{\mu\nu} N_\nu$$
where $V$ is an isometry ($V^\dagger V = I$, rectangular unitary). This is the channel analogue of the HJW theorem for ensembles.

**Physical interpretation**: Different Kraus decompositions correspond to different orthonormal bases chosen for the environment after the unitary interaction. Changing the environment basis $|\mu\rangle_E \to |\nu'\rangle_E = \sum_\mu V_{\mu\nu}|\mu\rangle_E$ transforms the Kraus operators accordingly.

### Reversibility of Quantum Channels **[Preskill, Ch.3, §3.2.2, pp.13-14]**
**Theorem** [Preskill, Ch.3, p.13] (Eq. 3.36-3.41): A quantum channel $\mathcal{E}$ can be inverted by another channel only if $\mathcal{E}$ is unitary. If $\mathcal{E}_2 \circ \mathcal{E}_1 = \text{id}$, then each Kraus operator $M_a$ of $\mathcal{E}_1$ must satisfy $M_a = \sqrt{\beta_{aa}}U_a$ for the same unitary $U$ (Eq. 3.39-3.41). Decoherence is irreversible: once $A$ becomes entangled with $B$, the damage to $A$ cannot be undone without access to $B$.

**Exception** [Preskill, Ch.3, p.14]: The conclusion can be evaded if the output space has larger dimension than the input (rectangular Kraus operators). This is exploited in quantum error correction (Ch. 7).

### Heisenberg Picture for Channels **[Preskill, Ch.3, §3.2.3, pp.14-15]**
The dual (adjoint) channel $\mathcal{E}^*$ acts on operators (Eq. 3.47):
$$A' = \mathcal{E}^*(A) = \sum_a M_a^\dagger A M_a$$
satisfying $\text{Tr}(A\mathcal{E}(\rho)) = \text{Tr}(\mathcal{E}^*(A)\rho)$ (Eq. 3.48). A channel is **unital** ($\mathcal{E}(I) = I$) iff its dual is trace-preserving and vice versa (Eq. 3.49-3.50). Unital channels preserve the maximally mixed state.

### Complete Positivity vs. Positivity **[Preskill, Ch.3, §3.2.6, pp.18-19]**
Complete positivity ($\mathcal{E} \otimes I$ is positive for any extension) is strictly stronger than positivity. The **transpose map** $T: \rho \mapsto \rho^T$ is positive but not CP (Eq. 3.64-3.67). Proof: $T \otimes I$ applied to $|\tilde{\Phi}\rangle\langle\tilde{\Phi}|$ yields the SWAP operator, which has negative eigenvalues. This underlies the PPT entanglement criterion.

### Stinespring Dilation Theorem **[Preskill, Ch.3, §3.3, pp.20-23]**
**Theorem (Stinespring)**: Any TPCP map $\mathcal{E}$ on system $A$ can be realized as:
$$\mathcal{E}(\rho_A) = \text{Tr}_E(V\rho_A V^\dagger)$$
where $V: \mathcal{H}_A \to \mathcal{H}_A \otimes \mathcal{H}_E$ is an isometry ($V^\dagger V = I_A$).

The isometry $V$ is called the **Stinespring dilation** of the channel. It is related to the Kraus operators by:
$$V|\psi\rangle_A = \sum_\mu (M_\mu|\psi\rangle_A) \otimes |\mu\rangle_E$$

**Key insight** [Preskill, Ch.3, §3.3]: The Stinespring dilation is unique up to a unitary on the environment. If $V$ and $V'$ are two dilations of the same channel, then $V' = (I_A \otimes U_E)V$ for some unitary $U_E$.

### Choi-Jamiolkowski Isomorphism (Channel-State Duality) **[Preskill, Ch.3, §3.3.1, pp.20-22]**
**Theorem**: There is a one-to-one correspondence between TPCP maps $\mathcal{E}$ on $d$-dimensional systems and density operators $\rho_\mathcal{E}$ on $\mathcal{H} \otimes \mathcal{H}$:

$$\rho_\mathcal{E} = (I \otimes \mathcal{E})(|\Phi^+\rangle\langle\Phi^+|)$$

where $|\Phi^+\rangle = \frac{1}{\sqrt{d}}\sum_{i=0}^{d-1}|i\rangle|i\rangle$ is the maximally entangled state.

**Properties of the Choi state** [Preskill, Ch.3, §3.3]:
- $\mathcal{E}$ is completely positive $\iff$ $\rho_\mathcal{E} \geq 0$
- $\mathcal{E}$ is trace-preserving $\iff$ $\text{Tr}_{\text{out}}(\rho_\mathcal{E}) = I/d$
- The channel can be recovered from the Choi state: $\mathcal{E}(\rho) = d \cdot \text{Tr}_{\text{in}}[({\rho^T} \otimes I)\rho_\mathcal{E}]$
- The rank of $\rho_\mathcal{E}$ equals the minimum number of Kraus operators needed

### Positive but Not Completely Positive: The Transpose Map **[Preskill, Ch.3, §3.2.6, pp.18-19]**
Preskill gives a detailed proof that the transpose map $T(\rho) = \rho^T$ is positive but not completely positive:

**Positivity**: If $\rho \geq 0$, then $\rho^T \geq 0$ (transposing preserves eigenvalues).

**Not CP**: Apply $I \otimes T$ to $|\Phi^+\rangle\langle\Phi^+| = \frac{1}{d}\sum_{ij}|i\rangle\langle j| \otimes |i\rangle\langle j|$:
$$(I \otimes T)(|\Phi^+\rangle\langle\Phi^+|) = \frac{1}{d}\sum_{ij}|i\rangle\langle j| \otimes |j\rangle\langle i| = \frac{1}{d}\text{SWAP}$$

The SWAP operator has eigenvalue $-1$ on antisymmetric states, so $(I \otimes T)(|\Phi^+\rangle\langle\Phi^+|) \not\geq 0$.

This is the basis of the **Peres-Horodecki (PPT) criterion** for entanglement detection.

### Three Quantum Channels **[Preskill, Ch.3, §3.4, pp.24-33]**
Preskill analyzes three important channels in detail:

**1. Depolarizing Channel** [Preskill, Ch.3, §3.4.1, pp.24-27]:
$$\mathcal{E}_{\text{deph}}(\rho) = (1-p)\rho + p Z\rho Z$$
Kraus operators: $M_0 = \sqrt{1-p}\,I$, $M_1 = \sqrt{p}\,Z$.
Effect on Bloch vector: $\vec{r} \to ((1-2p)r_x, (1-2p)r_y, r_z)$ — the $x$ and $y$ components shrink while $z$ is preserved. Geometrically, the Bloch sphere is compressed into an oblate ellipsoid.

**2. Dephasing Channel** [Preskill, Ch.3, §3.4.2, pp.27-31]:
$$\mathcal{E}_{\text{dep}}(\rho) = (1-p)\rho + p\frac{I}{2}$$
Kraus operators: $M_0 = \sqrt{1-3p/4}\,I$, $M_k = \sqrt{p/4}\,\sigma_k$ for $k = x,y,z$.
Effect on Bloch vector: $\vec{r} \to (1-p)\vec{r}$ — uniform contraction. The Bloch sphere shrinks uniformly.

**3. Amplitude Damping Channel** [Preskill, Ch.3, §3.4.3, pp.31-33]:
$$M_0 = \begin{pmatrix}1 & 0 \\ 0 & \sqrt{1-\gamma}\end{pmatrix}, \quad M_1 = \begin{pmatrix}0 & \sqrt{\gamma} \\ 0 & 0\end{pmatrix}$$
Effect on Bloch vector: $(r_x, r_y, r_z) \to (\sqrt{1-\gamma}\,r_x, \sqrt{1-\gamma}\,r_y, \gamma + (1-\gamma)r_z)$.
The Bloch sphere is compressed vertically and shifted upward toward the north pole $|0\rangle$. As $\gamma \to 1$, all states converge to $|0\rangle\langle 0|$.

### Quantum Operations **[Preskill, Ch.3, §3.2.4, pp.16-17]**
Quantum operations generalize both channels and measurements. A quantum operation $\mathcal{E}_a$ with Kraus operators $\{M_{a\mu}\}$ satisfying $\sum_\mu M_{a\mu}^\dagger M_{a\mu} \leq I$ (Eq. 3.54) describes the state transformation conditioned on measurement outcome $a$ (Eq. 3.52):
$$\mathcal{E}_a(\rho) = \sum_\mu M_{a\mu}\rho M_{a\mu}^\dagger, \qquad \text{Prob}(a) = \text{Tr}(\mathcal{E}_a(\rho))$$
A generalized measurement retains all information (one $\mu$ value), a channel discards all (one $a$ value), and an operation is the general case where some information is retained and some discarded.

### Linearity from Ensemble Consistency **[Preskill, Ch.3, §3.2.5, pp.17-18]**
The linearity of quantum channels follows from the ensemble interpretation of density operators (Eq. 3.57-3.59): if $\rho_i$ is prepared with probability $p_i$, then $\mathcal{E}(\sum_i p_i\rho_i) = \sum_i p_i\mathcal{E}(\rho_i)$ must hold, otherwise different ensemble decompositions of the same density operator would give different predictions.

### Master Equation (Lindblad Form) **[Preskill, Ch.3, §3.5, pp.34-38]**
For continuous-time Markovian evolution, the most general trace-preserving CP-divisible dynamics is governed by the **Lindblad master equation**:
$$\frac{d\rho}{dt} = -i[H, \rho] + \sum_k \left(L_k\rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\}\right)$$

**Derivation sketch** [Preskill, Ch.3, §3.5]: Starting from $\rho(t + dt) = \mathcal{E}_{dt}(\rho(t))$ with Kraus operators expanded to first order in $dt$:
- $M_0 = I - (iH + \frac{1}{2}K)dt$ where $K = \sum_k L_k^\dagger L_k$
- $M_k = \sqrt{dt}\,L_k$ for $k \geq 1$

Substituting into the Kraus form and keeping terms to $O(dt)$ yields the Lindblad equation.

**Key properties**:
- The first term $-i[H,\rho]$ generates unitary (Hamiltonian) evolution
- The $L_k$ terms (Lindblad/jump operators) generate dissipation and decoherence
- The equation preserves $\rho \geq 0$ and $\text{Tr}(\rho) = 1$ at all times
- The most general Markovian quantum dynamics is of this form (Gorini-Kossakowski-Sudarshan-Lindblad theorem)

---

## References

- **[Nielsen & Chuang]** Nielsen, M. A. & Chuang, I. L. *Quantum Computation and Quantum Information* (Cambridge, 10th anniversary ed., 2010), Ch. 8 (pp.353-398)
- **[Preskill, Ch.3]** Preskill, J. *Lecture Notes for Ph219/CS219: Quantum Information and Computation*, Ch.3: "Foundations II: Measurement and Evolution" (July 2015), §3.2 (quantum channels, Kraus representation, complete positivity), §3.3 (Stinespring dilation, Choi-Jamiolkowski isomorphism), §3.4 (dephasing, depolarizing, amplitude damping channels), §3.5 (Lindblad master equation). PDF: `references/preskill_ch3.pdf`
- Wilde, *Quantum Information Theory*, Ch. 4
- Choi, *Linear Algebra and its Applications* 10, 285 (1975)
