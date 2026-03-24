# Density Matrix Formalism (密度矩阵形式化)

> **Tags**: `density-matrix`, `mixed-state`, `quantum-state`, `partial-trace`

## Statement

任何量子态——无论是纯态还是混合态——都可以用一个密度矩阵（密度算子）$\rho$ 来描述。密度矩阵是定义在 Hilbert 空间上的正半定、迹为 1 的算子：

$$\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|, \qquad p_i \geq 0, \quad \sum_i p_i = 1$$

这是量子力学中对量子态的**最一般描述** **[N&C, Section 2.4, p.98]** **[Preskill, Ch.2, &sect;2.3, p.16]**，涵盖了态矢量描述（纯态）无法处理的统计混合情况。

## Prerequisites

- **线性代数**: 矩阵运算、特征值分解、迹运算、正半定矩阵
- **Dirac 记号**: $|a\rangle$（ket）、$\langle a|$（bra）、$|a\rangle\langle b|$（外积/投影算子）
- **Hilbert 空间**: 内积、标准正交基、完备性关系 $\sum_i |i\rangle\langle i| = I$

---

## Derivation

### Step 1: 从纯态出发

在最基本的量子力学中，系统的状态由 Hilbert 空间 $\mathcal{H}$ 中的一个归一化态矢量描述 **[N&C, Postulate 1, p.80]** **[Preskill, Ch.2, Axiom 1, p.3]**：

$$|\psi\rangle \in \mathcal{H}, \qquad \langle\psi|\psi\rangle = 1$$

对于纯态，任何可观测量 $A$ 的期望值为 **[Preskill, Ch.2, Eq.(2.9), p.5]**：

$$\langle A \rangle = \langle\psi|A|\psi\rangle$$

我们定义纯态的密度矩阵为外积：

$$\rho = |\psi\rangle\langle\psi|$$

**验证期望值公式等价**：我们来验证用密度矩阵也能得到同样的期望值。选一组标准正交基 $\{|n\rangle\}$，计算 $\text{Tr}(\rho A)$：

$$\text{Tr}(\rho A) = \sum_n \langle n|\rho A|n\rangle$$

代入 $\rho = |\psi\rangle\langle\psi|$：

$$= \sum_n \langle n|\psi\rangle\langle\psi|A|n\rangle$$

利用完备性关系 $\sum_n |n\rangle\langle n| = I$：

$$= \langle\psi|A\left(\sum_n |n\rangle\langle n|\right)|\psi\rangle = \langle\psi|A \cdot I|\psi\rangle = \langle\psi|A|\psi\rangle$$

所以：

$$\boxed{\langle A \rangle = \text{Tr}(\rho A) = \langle\psi|A|\psi\rangle}$$
**[N&C, Eq.(2.160), p.99]** **[Preskill, Ch.2, &sect;2.3.1, p.17]**

两种描述给出完全相同的物理预测。

### Step 2: 为什么需要混合态？

纯态描述有一个根本局限：**当我们对量子态的了解不完整时，纯态无法描述这种"经典不确定性"**。

**场景 1: 制备的不确定性**
假设一个量子态制备装置以概率 $p_1$ 制备 $|\psi_1\rangle$，以概率 $p_2$ 制备 $|\psi_2\rangle$。如果我们不知道实际制备了哪个态，系统的状态该如何描述？

**场景 2: 子系统**
一个纠缠态 $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ 中，如果我们只看其中一个量子比特，它的状态是什么？它既不是 $|0\rangle$ 也不是 $|1\rangle$，也不是它们的叠加。

这两种情况都需要混合态来描述。

### Step 3: 混合态的定义

假设系统以概率 $p_i$ 处于纯态 $|\psi_i\rangle$（$i = 1, 2, \ldots, k$），那么任何可观测量 $A$ 的期望值是**经典**加权平均：

$$\langle A \rangle = \sum_i p_i \langle\psi_i|A|\psi_i\rangle$$

用每个纯态的密度矩阵 $\rho_i = |\psi_i\rangle\langle\psi_i|$ 代入：

$$= \sum_i p_i \, \text{Tr}(\rho_i A) = \text{Tr}\left[\left(\sum_i p_i \rho_i\right) A\right]$$

因此，我们定义混合态的密度矩阵为：

$$\boxed{\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|}$$
**[N&C, Eq.(2.158), p.99]** **[Preskill, Ch.2, &sect;2.3.1, Eq.(2.37), p.17]**

其中 $p_i \geq 0$，$\sum_i p_i = 1$。

### Step 4: 密度矩阵的基本性质

**性质 1: Hermitian（厄米性）**

$$\rho^\dagger = \left(\sum_i p_i |\psi_i\rangle\langle\psi_i|\right)^\dagger = \sum_i p_i^* \left(|\psi_i\rangle\langle\psi_i|\right)^\dagger$$

因为 $(|a\rangle\langle b|)^\dagger = |b\rangle\langle a|$，所以 $(|\psi_i\rangle\langle\psi_i|)^\dagger = |\psi_i\rangle\langle\psi_i|$。

又因为 $p_i$ 是实数（概率），所以 $p_i^* = p_i$，因此：

$$\rho^\dagger = \sum_i p_i |\psi_i\rangle\langle\psi_i| = \rho \qquad \checkmark$$

**性质 2: Trace one（迹为 1）**

$$\text{Tr}(\rho) = \sum_i p_i \, \text{Tr}(|\psi_i\rangle\langle\psi_i|) = \sum_i p_i \langle\psi_i|\psi_i\rangle = \sum_i p_i \cdot 1 = 1 \qquad \checkmark$$

这里用了 $\text{Tr}(|a\rangle\langle b|) = \langle b|a\rangle$ 以及态的归一化。

**性质 3: Positive semi-definite（正半定）**

对任意 $|\phi\rangle$：

$$\langle\phi|\rho|\phi\rangle = \sum_i p_i \langle\phi|\psi_i\rangle\langle\psi_i|\phi\rangle = \sum_i p_i |\langle\phi|\psi_i\rangle|^2 \geq 0 \qquad \checkmark$$

每一项 $p_i \geq 0$，$|\langle\phi|\psi_i\rangle|^2 \geq 0$，所以和一定非负。

**汇总**：合法的密度矩阵当且仅当满足 **[N&C, Theorem 2.5, p.101]**：
$$\rho \geq 0 \quad \text{(正半定)}, \qquad \text{Tr}(\rho) = 1$$

### Step 5: 区分纯态和混合态

**判据** **[N&C, Eq.(2.140), p.100]** **[Preskill, Ch.2, &sect;2.3.2, p.21]**: $\rho$ 描述纯态当且仅当 $\text{Tr}(\rho^2) = 1$；描述混合态当且仅当 $\text{Tr}(\rho^2) < 1$。

**证明**：设 $\rho$ 的特征值为 $\lambda_1, \lambda_2, \ldots, \lambda_d$（$d$ 是 Hilbert 空间维数），则：

$$\text{Tr}(\rho) = \sum_i \lambda_i = 1, \qquad \lambda_i \geq 0$$

$$\text{Tr}(\rho^2) = \sum_i \lambda_i^2$$

由柯西-施瓦茨不等式（或直接由概率论），对于满足 $\sum_i \lambda_i = 1$，$\lambda_i \geq 0$ 的数集：

$$\sum_i \lambda_i^2 \leq \left(\sum_i \lambda_i\right)^2 = 1$$

等号成立当且仅当只有一个 $\lambda_i = 1$，其余为零，即 $\rho = |k\rangle\langle k|$ 为某个纯态。

这也可以这样理解：对纯态 $\rho = |\psi\rangle\langle\psi|$，

$$\rho^2 = |\psi\rangle\langle\psi|\psi\rangle\langle\psi| = |\psi\rangle \cdot 1 \cdot \langle\psi| = \rho$$

所以 $\rho^2 = \rho$（幂等性），从而 $\text{Tr}(\rho^2) = \text{Tr}(\rho) = 1$。

### Step 6: 密度矩阵中的期望值计算

给定可观测量 $A$（Hermitian 算子），在态 $\rho$ 下：

$$\langle A \rangle = \text{Tr}(\rho A)$$

**具体计算方法**：选标准正交基 $\{|n\rangle\}$，

$$\text{Tr}(\rho A) = \sum_n \langle n|\rho A|n\rangle$$

**例子**：单比特态 $\rho = \frac{1}{2}(I + \vec{r}\cdot\vec{\sigma})$ **[N&C, p.15, Eq.(1.15)]** **[Preskill, Ch.2, &sect;2.3.2, p.21]**，求 $\langle\sigma_z\rangle$：

$$\langle\sigma_z\rangle = \text{Tr}\left[\frac{1}{2}(I + r_x\sigma_x + r_y\sigma_y + r_z\sigma_z)\sigma_z\right]$$

利用 $\text{Tr}(\sigma_i) = 0$，$\text{Tr}(\sigma_i\sigma_j) = 2\delta_{ij}$：

$$= \frac{1}{2}\left[\text{Tr}(\sigma_z) + r_x\text{Tr}(\sigma_x\sigma_z) + r_y\text{Tr}(\sigma_y\sigma_z) + r_z\text{Tr}(\sigma_z^2)\right]$$

$$= \frac{1}{2}\left[0 + 0 + 0 + r_z \cdot 2\right] = r_z$$

所以 Bloch 向量的 $z$ 分量就是 $\sigma_z$ 的期望值，直观而优美。

### Step 7: 复合系统与约化密度矩阵

考虑两个子系统 $A$（维数 $d_A$）和 $B$（维数 $d_B$）构成的复合系统，其 Hilbert 空间为：

$$\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B$$

全局密度矩阵为 $\rho_{AB}$。如果我们只关心子系统 $A$，则需要对 $B$ 进行**偏迹**操作 **[N&C, Theorem 2.7, p.105]** **[Preskill, Ch.2, &sect;2.3.1, p.16]**：

$$\rho_A = \text{Tr}_B(\rho_{AB})$$

### Step 8: 偏迹的定义与计算

**定义** **[N&C, Eq.(2.178), p.105]**：令 $\{|j\rangle_B\}$ 为子系统 $B$ 的标准正交基，则：

$$\rho_A = \text{Tr}_B(\rho_{AB}) \equiv \sum_j \left(I_A \otimes \langle j|_B\right) \rho_{AB} \left(I_A \otimes |j\rangle_B\right)$$

**对张量积形式的简化**：若 $\rho_{AB} = \rho_A \otimes \rho_B$（无关联的态），则：

$$\text{Tr}_B(\rho_A \otimes \rho_B) = \rho_A \cdot \text{Tr}(\rho_B) = \rho_A \cdot 1 = \rho_A$$

**一般规则** **[N&C, Eq.(2.178), p.105]**：对外积张量积形式 $|a_1\rangle\langle a_2| \otimes |b_1\rangle\langle b_2|$，

$$\text{Tr}_B\left(|a_1\rangle\langle a_2| \otimes |b_1\rangle\langle b_2|\right) = |a_1\rangle\langle a_2| \cdot \text{Tr}(|b_1\rangle\langle b_2|) = |a_1\rangle\langle a_2| \cdot \langle b_2|b_1\rangle$$

**推导**：

$$\sum_j (I_A \otimes \langle j|)(|a_1\rangle\langle a_2| \otimes |b_1\rangle\langle b_2|)(I_A \otimes |j\rangle)$$

$$= \sum_j |a_1\rangle\langle a_2| \otimes \langle j|b_1\rangle\langle b_2|j\rangle$$

$$= |a_1\rangle\langle a_2| \otimes \sum_j \langle j|b_1\rangle\langle b_2|j\rangle$$

$$= |a_1\rangle\langle a_2| \cdot \sum_j \langle b_2|j\rangle\langle j|b_1\rangle$$

$$= |a_1\rangle\langle a_2| \cdot \langle b_2|b_1\rangle$$

最后一步用了完备性 $\sum_j |j\rangle\langle j| = I_B$。

### Step 9: 偏迹的完整例子 —— Bell 态

考虑 Bell 态：

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

其密度矩阵为：

$$\rho_{AB} = |\Phi^+\rangle\langle\Phi^+| = \frac{1}{2}(|00\rangle + |11\rangle)(\langle 00| + \langle 11|)$$

展开：

$$= \frac{1}{2}\left(|00\rangle\langle 00| + |00\rangle\langle 11| + |11\rangle\langle 00| + |11\rangle\langle 11|\right)$$

写成张量积形式：

$$= \frac{1}{2}\left(|0\rangle\langle 0| \otimes |0\rangle\langle 0| + |0\rangle\langle 1| \otimes |0\rangle\langle 1| + |1\rangle\langle 0| \otimes |1\rangle\langle 0| + |1\rangle\langle 1| \otimes |1\rangle\langle 1|\right)$$

对 $B$ 求偏迹，逐项应用规则 $\text{Tr}_B(|a_1\rangle\langle a_2| \otimes |b_1\rangle\langle b_2|) = \langle b_2|b_1\rangle \cdot |a_1\rangle\langle a_2|$：

- 第一项：$\langle 0|0\rangle \cdot |0\rangle\langle 0| = 1 \cdot |0\rangle\langle 0|$
- 第二项：$\langle 1|0\rangle \cdot |0\rangle\langle 1| = 0$
- 第三项：$\langle 0|1\rangle \cdot |1\rangle\langle 0| = 0$
- 第四项：$\langle 1|1\rangle \cdot |1\rangle\langle 1| = 1 \cdot |1\rangle\langle 1|$

所以：

$$\rho_A = \frac{1}{2}\left(|0\rangle\langle 0| + |1\rangle\langle 1|\right) = \frac{I}{2}$$

这是最大混合态！说明 Bell 态中每个子系统看起来完全是随机的，所有信息都存储在关联中——这正是纠缠的本质特征。

**验证**：$\text{Tr}(\rho_A^2) = \text{Tr}(I/4) = 1/2 < 1$，确认这是混合态。

### Step 10: 密度矩阵的谱分解

由于 $\rho$ 是 Hermitian 且正半定的，由谱定理 **[N&C, Theorem 2.1, p.72]** 它可以对角化：

$$\rho = \sum_{i=1}^d \lambda_i |e_i\rangle\langle e_i|$$

其中 $\{|e_i\rangle\}$ 是标准正交特征向量，$\lambda_i \geq 0$ 是特征值，$\sum_i \lambda_i = 1$。

这个分解是**唯一的**（当特征值不简并时），它告诉我们 $\rho$ "本质上"是以概率 $\lambda_i$ 处于正交纯态 $|e_i\rangle$ 的混合。

**注意**：密度矩阵的系综分解（$\rho = \sum_i p_i|\psi_i\rangle\langle\psi_i|$ 中 $|\psi_i\rangle$ 不一定正交）**不是唯一的** **[N&C, Theorem 2.6, p.103]** **[Preskill, Ch.2, &sect;2.5.5, pp.34-36]**。不同的系综可以给出同一个 $\rho$。只有谱分解（正交分解）是唯一的。

---

## Summary

| 概念 | 数学表达 | 物理意义 |
|------|---------|---------|
| 纯态密度矩阵 | $\rho = \|\psi\rangle\langle\psi\|$ | 完全已知的量子态 |
| 混合态密度矩阵 | $\rho = \sum_i p_i \|\psi_i\rangle\langle\psi_i\|$ | 统计混合/部分信息 |
| 正半定 + 迹为 1 | $\rho \geq 0$, $\text{Tr}(\rho)=1$ | 合法量子态的充要条件 |
| 纯度 | $\text{Tr}(\rho^2) \leq 1$ | 等于 1 ↔ 纯态；小于 1 ↔ 混合 |
| 偏迹 | $\rho_A = \text{Tr}_B(\rho_{AB})$ | 子系统的量子态 |
| 期望值 | $\langle A\rangle = \text{Tr}(\rho A)$ | 统一的测量预测公式 |

---

## Nielsen & Chuang: Theorems and Formal Results

### Theorem 2.1 (Spectral Decomposition) **[Nielsen & Chuang, Theorem 2.1, p.72]**
Any normal operator $M$ on a vector space $V$ is diagonal with respect to some orthonormal basis for $V$. Conversely, any diagonalizable operator is normal.

In outer product representation: $M = \sum_i \lambda_i |i\rangle\langle i|$, where $\lambda_i$ are eigenvalues, $|i\rangle$ is an orthonormal basis. In projector form: $M = \sum_i \lambda_i P_i$, with $\sum_i P_i = I$ and $P_i P_j = \delta_{ij} P_i$.

**Proof** **[Nielsen & Chuang, p.72]**: By induction on dimension $d$. Let $\lambda$ be an eigenvalue of $M$, $P$ the projector onto the $\lambda$ eigenspace, $Q = I - P$. Then $M = PMP + QMQ$ (cross terms vanish by normality: $QMP = 0$ and $PMQ = 0$ since $M^\dagger$ preserves the $\lambda$ eigenspace). $QMQ$ is normal on the subspace $Q$, and by induction is diagonal there.

### Theorem 2.2 (Simultaneous Diagonalization) **[Nielsen & Chuang, Theorem 2.2, p.77]**
Suppose $A$ and $B$ are Hermitian operators. Then $[A, B] = 0$ if and only if there exists an orthonormal basis such that both $A$ and $B$ are diagonal with respect to that basis.

### Theorem 2.3 (Polar Decomposition) **[Nielsen & Chuang, Theorem 2.3, p.78]**
Let $A$ be a linear operator on a vector space $V$. Then there exists unitary $U$ and positive operators $J$ and $K$ such that $A = UJ = KU$, where $J \equiv \sqrt{A^\dagger A}$ and $K \equiv \sqrt{AA^\dagger}$. If $A$ is invertible then $U$ is unique.

### Corollary 2.4 (Singular Value Decomposition) **[Nielsen & Chuang, Corollary 2.4, p.79]**
Let $A$ be a square matrix. Then there exist unitary matrices $U$ and $V$, and a diagonal matrix $D$ with non-negative entries such that $A = UDV$. The diagonal elements of $D$ are the singular values of $A$.

### Postulate 1 (State Space) **[Nielsen & Chuang, Postulate 1, p.80]**
Associated to any isolated physical system is a complex vector space with inner product (that is, a Hilbert space) known as the state space of the system. The system is completely described by its state vector, which is a unit vector in the system's state space.

### Postulate 2 (Evolution) **[Nielsen & Chuang, Postulate 2, p.81]**
The evolution of a closed quantum system is described by a unitary transformation. That is, the state $|\psi\rangle$ of the system at time $t_1$ is related to the state $|\psi'\rangle$ of the system at time $t_2$ by a unitary operator $U$ which depends only on the times $t_1$ and $t_2$: $|\psi'\rangle = U|\psi\rangle$.

### Postulate 2' (Schrodinger Equation) **[Nielsen & Chuang, Postulate 2', p.82]**
The time evolution of the state of a closed quantum system is described by the Schrodinger equation: $i\hbar \frac{d|\psi\rangle}{dt} = H|\psi\rangle$, where $H$ is the Hamiltonian. The connection to Postulate 2 is $U(t_1,t_2) = \exp(-iH(t_2-t_1)/\hbar)$.

### Postulate 3 (Measurement) **[Nielsen & Chuang, Postulate 3, p.84]**
Quantum measurements are described by a collection $\{M_m\}$ of measurement operators acting on the state space of the system being measured. The probability that result $m$ occurs is $p(m) = \langle\psi|M_m^\dagger M_m|\psi\rangle$, and the state after measurement is $M_m|\psi\rangle / \sqrt{p(m)}$. The measurement operators satisfy the completeness equation $\sum_m M_m^\dagger M_m = I$.

### Postulate 4 (Composite Systems) **[Nielsen & Chuang, Postulate 4, p.94]**
The state space of a composite physical system is the tensor product of the state spaces of the component physical systems: $\mathcal{H}_{12} = \mathcal{H}_1 \otimes \mathcal{H}_2$.

### Theorem 2.5 (Characterization of Density Operators) **[Nielsen & Chuang, Theorem 2.5, p.101]**
An operator $\rho$ is the density operator associated to some ensemble $\{p_i, |\psi_i\rangle\}$ if and only if: (i) $\rho$ has trace equal to one ($\text{Tr}(\rho) = 1$), and (ii) $\rho$ is a positive operator ($\rho \geq 0$).

### Theorem 2.6 (Unitary Freedom in Ensembles) **[Nielsen & Chuang, Theorem 2.6, p.103]**
The sets $\{|\tilde{\psi}_i\rangle\}$ and $\{|\tilde{\phi}_j\rangle\}$ (unnormalized, $|\tilde{\psi}_i\rangle = \sqrt{p_i}|\psi_i\rangle$) generate the same density matrix if and only if $|\tilde{\psi}_i\rangle = \sum_j u_{ij}|\tilde{\phi}_j\rangle$ where $u_{ij}$ is a unitary matrix (with zero-padding if necessary).

This theorem explains why the ensemble decomposition of a density matrix is **not unique** -- different ensembles can give the same $\rho$. Only the spectral decomposition (orthogonal decomposition) is unique.

### Partial Trace Definition **[Nielsen & Chuang, Eq. 2.178, p.105]**
The partial trace over system $B$ is defined by:
$$\text{Tr}_B(|a_1\rangle\langle a_2| \otimes |b_1\rangle\langle b_2|) = |a_1\rangle\langle a_2| \cdot \text{Tr}(|b_1\rangle\langle b_2|) = |a_1\rangle\langle a_2| \cdot \langle b_2|b_1\rangle$$

### Theorem 2.7 (Reduced Density Operator) **[Nielsen & Chuang, Theorem 2.7, p.105]**
For a composite system $AB$ in state $\rho^{AB}$, the reduced density operator for system $A$ is $\rho^A = \text{Tr}_B(\rho^{AB})$. The correct description of a subsystem is provided uniquely by the reduced density operator: it gives the correct measurement statistics for measurements on system $A$ alone.

### Bloch Sphere Representation **[Nielsen & Chuang, p.15, Eq. 1.15-1.16]**
Any single-qubit density matrix can be written as $\rho = \frac{I + \vec{r}\cdot\vec{\sigma}}{2}$, where $\vec{r}$ is the Bloch vector with $|\vec{r}| \leq 1$. Pure states correspond to $|\vec{r}| = 1$, mixed states to $|\vec{r}| < 1$.

### Purity Test **[Nielsen & Chuang, Eq. 2.140, p.100]**
A density operator $\rho$ describes a pure state if and only if $\text{Tr}(\rho^2) = 1$. For mixed states, $\text{Tr}(\rho^2) < 1$.

---

## Preskill: Theorems and Formal Results (Chapter 2)

### Five Axioms of Quantum Mechanics **[Preskill, Ch.2, §2.1, pp.3-6]**
Preskill formulates five axioms for closed quantum systems:

1. **Axiom 1 (States)** [Preskill, Ch.2, p.3]: A state is a ray in Hilbert space. Normalized: $\langle\psi|\psi\rangle = 1$ (Eq. 2.1).
2. **Axiom 2 (Observables)** [Preskill, Ch.2, p.4]: Observable = self-adjoint operator. Spectral decomposition: $A = \sum_n a_n E_n$ where $E_n E_m = \delta_{nm}E_n$ (Eqs. 2.4-2.6).
3. **Axiom 3 (Measurement)** [Preskill, Ch.2, p.5]: $\text{Prob}(a_n) = \langle\psi|E_n|\psi\rangle$ (Eq. 2.7). Post-measurement state: $E_n|\psi\rangle/\|E_n|\psi\rangle\|$ (Eq. 2.8). Expectation value: $\langle A\rangle = \langle\psi|A|\psi\rangle$ (Eq. 2.9).
4. **Axiom 4 (Dynamics)** [Preskill, Ch.2, p.6]: Unitary evolution $|\psi(t')\rangle = U(t',t)|\psi(t)\rangle$ (Eq. 2.10). Schrodinger equation: $\frac{d}{dt}|\psi\rangle = -iH|\psi\rangle$ (Eq. 2.11).
5. **Axiom 5 (Composite Systems)** [Preskill, Ch.2, p.6]: $\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B$ (Eq. 2.13).

**Key observation** [Preskill, Ch.2, p.17]: For open systems, axioms 1-3 are all violated: (1) states are not rays but density operators, (2) measurements are not orthogonal projections but POVMs, (3) evolution is not unitary but described by quantum channels.

### The Density Operator from Bipartite Systems **[Preskill, Ch.2, §2.3.1, pp.16-20]**
Preskill motivates the density operator through bipartite systems. Given a composite system $AB$ in state $\rho_{AB}$, the reduced density operator is:
$$\rho_A = \text{Tr}_B(\rho_{AB})$$
This is the **unique** operator on $A$ that reproduces all measurement statistics for observables on $A$ alone:
$$\text{Tr}(O_A \rho_A) = \text{Tr}((O_A \otimes I_B)\rho_{AB})$$
for all $O_A$. The proof follows from the definition of partial trace and the cyclic property of trace.

### Bloch Sphere for Qubits **[Preskill, Ch.2, §2.3.2, pp.21-22]**
Any single-qubit density matrix can be expanded in the Pauli basis:
$$\rho = \frac{1}{2}(I + \vec{r} \cdot \vec{\sigma}) = \frac{1}{2}\begin{pmatrix}1 + r_z & r_x - ir_y \\ r_x + ir_y & 1 - r_z\end{pmatrix}$$
where $\vec{r} = (r_x, r_y, r_z)$ is the **Bloch vector** with $|\vec{r}| \leq 1$.

**Key results**:
- $\rho$ is pure iff $|\vec{r}| = 1$ (surface of Bloch sphere)
- $\rho$ is maximally mixed iff $\vec{r} = 0$ (center of Bloch sphere)
- $\text{Tr}(\rho^2) = \frac{1}{2}(1 + |\vec{r}|^2)$, so purity is directly related to Bloch vector length
- Eigenvalues of $\rho$ are $\frac{1}{2}(1 \pm |\vec{r}|)$

### Ensemble Ambiguity and the HJW Theorem **[Preskill, Ch.2, §2.5, pp.26-36]**
Different ensembles can give rise to the same density operator. Preskill proves the **HJW theorem** (Hughston-Jozsa-Wootters), also known as the **unitary freedom theorem**:

**Theorem (HJW / Unitary Freedom in Ensembles)** **[Preskill, Ch.2, §2.5.5, pp.34-36]**: Two ensembles $\{p_i, |\psi_i\rangle\}$ and $\{q_j, |\phi_j\rangle\}$ give the same density operator $\rho$ if and only if
$$\sqrt{p_i}|\psi_i\rangle = \sum_j U_{ij}\sqrt{q_j}|\phi_j\rangle$$
where $U$ is a unitary matrix (padded with zeros if the ensemble sizes differ).

**Proof sketch** [Preskill, Ch.2, §2.5.5]: Consider a purification $|\Psi\rangle_{AR}$ of $\rho_A$. Different measurements on $R$ yield different ensembles for $A$, all producing the same $\rho_A$. Since all purifications are related by unitary operations on $R$, and different orthogonal measurements on $R$ are also related by unitaries, the ensembles are connected by a unitary matrix.

**Corollary (No signaling via ensemble ambiguity)** **[Preskill, Ch.2, §2.5.3, pp.30-31]**: Since different ensemble preparations of the same $\rho$ are operationally indistinguishable by local measurements, shared entanglement cannot be used for superluminal communication. Bob's local density operator $\rho_B = \text{Tr}_A(\rho_{AB})$ is independent of what measurement Alice performs on her subsystem.

### Purification Theorem **[Preskill, Ch.2, §2.5.5, pp.34-35]**
**Theorem**: For any mixed state $\rho_A$ on system $A$ with spectral decomposition $\rho_A = \sum_i \lambda_i |i\rangle\langle i|$, there exists a pure state $|\Psi\rangle_{AR}$ on an enlarged system $AR$ such that $\rho_A = \text{Tr}_R(|\Psi\rangle\langle\Psi|_{AR})$.

**Construction**: Choose reference system $R$ with $\dim(R) = \text{rank}(\rho_A)$ and define:
$$|\Psi\rangle_{AR} = \sum_i \sqrt{\lambda_i}|i\rangle_A|i\rangle_R$$

**Uniqueness up to unitary**: If $|\Psi\rangle_{AR}$ and $|\Psi'\rangle_{AR}$ are both purifications of $\rho_A$, then $|\Psi'\rangle_{AR} = (I_A \otimes U_R)|\Psi\rangle_{AR}$ for some unitary $U_R$ on $R$.

### Quantum Erasure **[Preskill, Ch.2, §2.5.4, pp.31-34]**
Preskill discusses quantum erasure as an application of ensemble ambiguity: by choosing different measurements on the environment, one can "erase" which-path information and restore interference fringes. This illustrates that decoherence is a property of the subsystem, not an irreversible process at the fundamental level.

---

## References

- **[Nielsen & Chuang]** Nielsen, M. A. & Chuang, I. L. *Quantum Computation and Quantum Information* (Cambridge, 10th anniversary ed., 2010), Ch. 2.4 (pp.98-109)
- **[Preskill, Ch.2]** Preskill, J. *Lecture Notes for Ph219/CS219: Quantum Information and Computation*, Ch.2: "Foundations I: States and Ensembles" (July 2015), §2.1 (axioms), §2.3 (density operator, bipartite systems, Bloch sphere), §2.4 (Schmidt decomposition, purification), §2.5 (ensemble ambiguity, HJW theorem, no-signaling, quantum erasure). PDF: `references/preskill_ch2.pdf`
- Sakurai & Napolitano, *Modern Quantum Mechanics*, Ch. 3
- Wilde, *Quantum Information Theory*, Ch. 4
