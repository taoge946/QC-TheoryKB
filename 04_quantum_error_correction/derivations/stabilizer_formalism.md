# Stabilizer Formalism

> **Tags**: `stabilizer`, `qec`, `pauli-group`, `codespace`

## Statement

稳定子形式体系（Stabilizer Formalism）提供了一种用 Pauli 群的阿贝尔子群来高效描述量子纠错码的数学框架。一个 $[[n, k]]$ 稳定子码用 $n$ 个物理量子比特编码 $k$ 个逻辑量子比特，码空间由稳定子群 $\mathcal{S}$ 的 $n-k$ 个独立生成元的共同 $+1$ 特征子空间定义。该形式体系将指数维的 Hilbert 空间问题简化为多项式规模的 Pauli 群运算。

## Prerequisites

- **Pauli 群**：单量子比特 Pauli 矩阵 $\{I, X, Y, Z\}$ 及其性质
- **张量积**：多量子比特算子的张量积结构
- **群论基础**：群、子群、生成元、陪集的概念
- **线性代数**：特征值、特征子空间、投影算子

---

## Derivation

### Step 1: Pauli Group on $n$ Qubits **[Gottesman, §2.3; Steane, p.10-11; Preskill Ch.7, §7.1, p.2]**

**单量子比特 Pauli 矩阵**定义为：

$$I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

它们满足以下基本关系：

$$X^2 = Y^2 = Z^2 = I$$

$$XY = iZ, \quad YZ = iX, \quad ZX = iY$$

$$YX = -iZ, \quad ZY = -iX, \quad XZ = -iY$$

关键性质：任意两个 Pauli 矩阵要么**对易**（commute），要么**反对易**（anticommute）。

**单量子比特 Pauli 群** $\mathcal{G}_1$ 包含所有 Pauli 矩阵乘以相位因子 $\pm 1, \pm i$：

$$\mathcal{G}_1 = \{ \pm I, \pm iI, \pm X, \pm iX, \pm Y, \pm iY, \pm Z, \pm iZ \}$$

这是一个阶为 16 的群（在矩阵乘法下封闭）。

**$n$ 量子比特 Pauli 群** $\mathcal{G}_n$ **[Gottesman, §2.3]** 定义为所有 $n$ 个单量子比特 Pauli 算子的张量积（含相位因子）：

$$\mathcal{G}_n = \{ i^\phi \cdot \sigma_1 \otimes \sigma_2 \otimes \cdots \otimes \sigma_n : \phi \in \{0,1,2,3\}, \; \sigma_j \in \{I, X, Y, Z\} \}$$

$\mathcal{G}_n$ 的重要性质：

1. **封闭性**：$\mathcal{G}_n$ 中任意两个元素的乘积仍在 $\mathcal{G}_n$ 中
2. **对易/反对易**：任意两个元素（忽略相位）要么对易要么反对易
3. **自逆性**：忽略相位后，每个元素的平方等于 $\pm I^{\otimes n}$
4. **阶**：$|\mathcal{G}_n| = 4 \cdot 4^n$（4 个相位选择 $\times$ $4^n$ 个 Pauli 串）

### Step 2: Define the Stabilizer Group **[Gottesman, §3.2; Nielsen & Chuang, §10.5.1, p.456; Bacon, p.17]**

**定义**：一个**稳定子群** $\mathcal{S}$ 是 $\mathcal{G}_n$ 的一个阿贝尔子群，满足以下条件：

1. $-I^{\otimes n} \notin \mathcal{S}$（即 $\mathcal{S}$ 不包含负单位元）
2. $\mathcal{S}$ 中所有元素相互对易
3. $\mathcal{S}$ 中每个元素的平方等于 $I^{\otimes n}$（即每个元素的特征值只能是 $\pm 1$）

为什么需要条件1？假设 $-I^{\otimes n} \in \mathcal{S}$，那么对码空间中的任意态 $|\psi\rangle$：

$$(-I^{\otimes n})|\psi\rangle = |\psi\rangle \implies -|\psi\rangle = |\psi\rangle \implies |\psi\rangle = 0$$

这意味着码空间只包含零向量，没有意义。所以必须排除 $-I^{\otimes n}$。

**生成元**：$\mathcal{S}$ 可以由一组**独立生成元** $g_1, g_2, \ldots, g_r$ 生成：

$$\mathcal{S} = \langle g_1, g_2, \ldots, g_r \rangle = \{ g_1^{a_1} g_2^{a_2} \cdots g_r^{a_r} : a_i \in \{0, 1\} \}$$

由于每个 $g_i^2 = I$，所以 $\mathcal{S}$ 有 $2^r$ 个元素。这里"独立"意味着没有任何一个生成元可以由其他生成元的乘积得到。

### Step 3: Stabilizer Group Defines the Codespace **[Gottesman, §3.2; Nielsen & Chuang, Theorem 10.3, p.457]**

**核心定理**：给定稳定子群 $\mathcal{S} = \langle g_1, \ldots, g_r \rangle \leq \mathcal{G}_n$，定义码空间为：

$$\mathcal{C}(\mathcal{S}) = \{ |\psi\rangle \in (\mathbb{C}^2)^{\otimes n} : g|\psi\rangle = |\psi\rangle, \; \forall g \in \mathcal{S} \}$$

即码空间是 $\mathcal{S}$ 中**所有**元素的共同 $+1$ 特征子空间。

**等价地**，只需要对所有生成元满足 $+1$ 特征值条件即可：

$$\mathcal{C}(\mathcal{S}) = \{ |\psi\rangle : g_i |\psi\rangle = |\psi\rangle, \; \forall i = 1, \ldots, r \}$$

**证明等价性**：如果 $g_i|\psi\rangle = |\psi\rangle$ 对所有 $i$ 成立，那么对于 $\mathcal{S}$ 中的任意元素 $g = g_1^{a_1} \cdots g_r^{a_r}$：

$$g|\psi\rangle = g_1^{a_1} \cdots g_r^{a_r} |\psi\rangle = |\psi\rangle$$

因为每次作用一个 $g_i$ 都不改变 $|\psi\rangle$。

**码空间的维度**：对于 $r$ 个独立生成元作用在 $n$ 个量子比特上：

$$\dim(\mathcal{C}) = 2^{n-r}$$

**推导维度公式**：

考虑向码空间的投影算子。对于单个稳定子元素 $g_i$（特征值为 $\pm 1$），向 $+1$ 特征子空间的投影算子为：

$$P_i = \frac{I + g_i}{2}$$

验证这确实是投影算子：
- **幂等性**：$P_i^2 = \frac{(I + g_i)^2}{4} = \frac{I + 2g_i + g_i^2}{4} = \frac{I + 2g_i + I}{4} = \frac{2(I + g_i)}{4} = \frac{I + g_i}{2} = P_i$（用了 $g_i^2 = I$）
- **Hermitian 性**：$P_i^\dagger = \frac{I + g_i^\dagger}{2} = \frac{I + g_i}{2} = P_i$（Pauli 算子都是 Hermitian 的）

向整个码空间的投影算子为所有 $P_i$ 的乘积（因为它们相互对易）：

$$P = \prod_{i=1}^{r} P_i = \prod_{i=1}^{r} \frac{I + g_i}{2}$$ **[Nielsen & Chuang, Eq. 10.72, p.457]**

展开这个乘积：

$$P = \frac{1}{2^r} \prod_{i=1}^{r} (I + g_i) = \frac{1}{2^r} \sum_{g \in \mathcal{S}} g$$ **[Gottesman, §4.2, Eq. 4.2; Nielsen & Chuang, Eq. 10.72, p.457]**

最后一步是因为展开乘积后，每一项恰好对应 $\mathcal{S}$ 中的一个元素（选择每个因子中的 $I$ 或 $g_i$）。

码空间的维度等于投影算子的迹：

$$\dim(\mathcal{C}) = \text{tr}(P) = \frac{1}{2^r} \sum_{g \in \mathcal{S}} \text{tr}(g)$$

对于 $g = I^{\otimes n}$，$\text{tr}(I^{\otimes n}) = 2^n$。对于 $g \neq I^{\otimes n}$（即至少有一个位置不是 $I$），$\text{tr}(g) = 0$，因为 $\text{tr}(X) = \text{tr}(Y) = \text{tr}(Z) = 0$，而张量积的迹是各分量迹的乘积。

因此：

$$\dim(\mathcal{C}) = \frac{1}{2^r} \cdot 2^n = 2^{n-r}$$

若设 $r = n - k$（即用 $n - k$ 个独立生成元），则码空间维度为 $2^k$，可以编码 $k$ 个逻辑量子比特。这就是 $[[n, k]]$ 稳定子码。

### Step 4: Syndrome Extraction **[Gottesman, §3.2; Roffe, §3.5; Steane, p.12-13; Preskill Ch.7, §7.5, p.20]**

现在来看当一个错误 $E \in \mathcal{G}_n$ 作用在码字 $|\psi\rangle \in \mathcal{C}$ 上时会发生什么。

**关键观察**：由于 $E$ 和 $g_i$ 都是 Pauli 群的元素，它们要么对易要么反对易：

$$g_i E = \pm E g_i$$

具体地：
- 如果 $g_i E = E g_i$（对易），则 $g_i (E|\psi\rangle) = E(g_i|\psi\rangle) = E|\psi\rangle$
  - 即 $E|\psi\rangle$ 仍是 $g_i$ 的 $+1$ 特征态

- 如果 $g_i E = -E g_i$（反对易），则 $g_i (E|\psi\rangle) = -E(g_i|\psi\rangle) = -E|\psi\rangle$
  - 即 $E|\psi\rangle$ 是 $g_i$ 的 $-1$ 特征态

**Syndrome 定义** **[Gottesman, §3.2; Nielsen & Chuang, §10.5.2, p.459]**：对于错误 $E$，定义 syndrome 位 $s_i \in \{0, 1\}$：

$$s_i(E) = \begin{cases} 0 & \text{if } g_i E = E g_i \\ 1 & \text{if } g_i E = -E g_i \end{cases}$$

syndrome 向量为 $\mathbf{s}(E) = (s_1, s_2, \ldots, s_{n-k}) \in \mathbb{F}_2^{n-k}$。

**Syndrome 测量不会破坏编码信息**：

测量 $g_i$ 得到结果 $(-1)^{s_i}$。这个测量将态 $E|\psi\rangle$ 投影到 $g_i$ 的 $(-1)^{s_i}$ 特征子空间。关键点是：
1. 不同的码字 $|\psi\rangle$ 在错误 $E$ 下给出**相同**的 syndrome
2. 因此测量 syndrome 不会泄露任何关于 $|\psi\rangle$ 的信息
3. 这与经典纠错中测量 syndrome 类似

**Syndrome 的可加性**（在 $\mathbb{F}_2$ 上）：

$$\mathbf{s}(E_1 E_2) = \mathbf{s}(E_1) \oplus \mathbf{s}(E_2)$$

这是因为对易/反对易关系在乘积下遵循 $\mathbb{F}_2$ 加法。

### Step 5: Error Correction Procedure **[Gottesman, §3.2; Roffe, §3.5; Preskill Ch.7, §7.5, pp.20-22]**

给定 syndrome $\mathbf{s}$，纠错过程如下：

**Step 5a**: 收到错误态 $E|\psi\rangle$。

**Step 5b**: 测量所有 syndrome 位 $s_1, s_2, \ldots, s_{n-k}$，得到 syndrome 向量 $\mathbf{s}$。

**Step 5c**: 根据 syndrome 查表（或使用解码算法），找到一个恢复算子 $R$ 满足 $\mathbf{s}(R) = \mathbf{s}(E)$。

**Step 5d**: 施加恢复算子 $R$，得到 $RE|\psi\rangle$。

**正确性分析**：$RE$ 与所有稳定子生成元对易（因为 $\mathbf{s}(RE) = \mathbf{s}(R) \oplus \mathbf{s}(E) = \mathbf{0}$），所以 $RE$ 要么：

1. $RE \in \mathcal{S}$：此时 $RE|\psi\rangle = |\psi\rangle$，**纠错成功**
2. $RE$ 在稳定子的 normalizer $N(\mathcal{S})$ 中但不在 $\mathcal{S}$ 中：$RE$ 是一个非平凡的逻辑算子，会改变编码信息，**纠错失败**（逻辑错误）

**Normalizer 的定义** **[Gottesman, §3.2; Nielsen & Chuang, Theorem 10.4, p.458]**：

$$N(\mathcal{S}) = \{ E \in \mathcal{G}_n : E g E^\dagger \in \mathcal{S}, \; \forall g \in \mathcal{S} \}$$

对于 Pauli 群，这等价于 **[Gottesman, §3.2]**：

$$N(\mathcal{S}) = \{ E \in \mathcal{G}_n : [E, g] = 0, \; \forall g \in \mathcal{S} \}$$

即 $N(\mathcal{S})$ 包含所有与 $\mathcal{S}$ 中每个元素对易的 Pauli 算子。$N(\mathcal{S})$ 包含 $4 \cdot 2^{n+k}$ 个元素 **[Gottesman, §3.2]**。

**逻辑算子**住在 $N(\mathcal{S}) \setminus \mathcal{S}$ 中（normalizer 减去 stabilizer）。对于 $k$ 个逻辑量子比特，有 $2k$ 个独立的逻辑算子 $\bar{X}_1, \bar{Z}_1, \ldots, \bar{X}_k, \bar{Z}_k$。

### Step 6: Code Distance **[Gottesman, §3.2; Nielsen & Chuang, p.467; Preskill Ch.7, §7.3.1, p.13, Eq. 7.34]**

**定义**：稳定子码的码距 $d$ 是不在 $\mathcal{S}$ 中的最小权重 normalizer 元素的权重：

$$d = \min_{E \in N(\mathcal{S}) \setminus \mathcal{S}} \text{wt}(E)$$

其中 $\text{wt}(E)$ 是 $E$ 的 Pauli 权重（非 $I$ 位置的数目）。

**物理含义**：码距 $d$ 的码可以：
- **检测**最多 $d - 1$ 个错误
- **纠正**最多 $t = \lfloor (d-1)/2 \rfloor$ 个错误

**码距与逻辑算子的关系**：$d$ 是最短逻辑算子的权重。要产生不可检测的逻辑错误，至少需要 $d$ 个物理量子比特同时出错。

---

## Gottesman Thesis: Key Theorems and Definitions

### The Pauli Group $\mathcal{G}_n$

> **[Gottesman thesis, §2.3]**: The set of all tensor products of $\sigma_x$, $\sigma_y$, $\sigma_z$, and $I$ with a possible overall factor of $-1$ or $\pm i$ forms a group $\mathcal{G}$ under multiplication. $\mathcal{G}_1$ is just the quaternionic group; $\mathcal{G}_n$ is the direct product of $n$ copies of the quaternions modulo all but a global phase factor.

> **[Gottesman thesis, §2.3]**: Key properties of $\mathcal{G}$: Since $\sigma_x^2 = \sigma_y^2 = \sigma_z^2 = +1$, every element in $\mathcal{G}$ squares to $\pm 1$. Also, $\sigma_x$, $\sigma_y$, and $\sigma_z$ on the same qubit anticommute, while they commute on different qubits. Therefore, any two elements of $\mathcal{G}$ either commute or they anticommute.

### General Stabilizer Code Definition

> **[Gottesman thesis, §3.2]**: In general, the stabilizer $S$ is some Abelian subgroup of $\mathcal{G}$ and the coding space $T$ is the space of vectors fixed by $S$:
> $$T = \{ |\psi\rangle \;\text{s.t.}\; M|\psi\rangle = |\psi\rangle \;\forall M \in S \}$$
> For a code to encode $k$ qubits in $n$, $T$ has $2^k$ dimensions and $S$ has $2^{n-k}$ elements. $S$ must be an Abelian group, since only commuting operators can have simultaneous eigenvectors, but provided it is Abelian and neither $i$ nor $-1$ is in $S$, the space $T$ does have dimension $2^k$.

### Error Detection and Correction Theorem

> **[Gottesman thesis, §3.2, Main Error Correction Result]**: A quantum code with stabilizer $S$ will detect all errors $E$ that are either in $S$ or anticommute with some element of $S$. In other words, $E \in S \cup (\mathcal{G} - N(S))$. This code will correct any set of errors $\{E_i\}$ iff $E_a E_b \in S \cup (\mathcal{G} - N(S))$ for all $E_a, E_b$.

**Proof sketch** [Gottesman thesis, §3.2]:

If $M \in S$, $|\psi_i\rangle \in T$, and $\{M, E\} = 0$, then:
$$ME|\psi_i\rangle = -EM|\psi_i\rangle = -E|\psi_i\rangle$$
so $E|\psi_i\rangle$ is an eigenvector of $M$ with eigenvalue $-1$ instead of $+1$. Therefore:
$$\langle\psi_i|E|\psi_j\rangle = \langle\psi_i|ME|\psi_j\rangle = -\langle\psi_i|E|\psi_j\rangle = 0$$

If $E \in S$, then $\langle\psi_i|E|\psi_j\rangle = \langle\psi_i|\psi_j\rangle = \delta_{ij}$, which also satisfies the Knill-Laflamme condition.

### Normalizer and Logical Operators

> **[Gottesman thesis, §3.2]**: The set of elements in $\mathcal{G}$ that commute with all of $S$ is defined as the centralizer $C(S)$ of $S$ in $\mathcal{G}$. Because of the properties of $S$ and $\mathcal{G}$, the centralizer is actually equal to the normalizer $N(S)$ of $S$ in $\mathcal{G}$. To see this, note that for any $A \in \mathcal{G}$, $M \in S$:
> $$A^\dagger M A = \pm A^\dagger A M = \pm M$$
> Since $-1 \notin S$, $A \in N(S)$ iff $A \in C(S)$, so $N(S) = C(S)$.

> **[Gottesman thesis, §3.2]**: $N(S)$ contains $4 \cdot 2^{n+k}$ elements. If $E \in N(S) - S$, then $E$ rearranges elements of $T$ but does not take them out of $T$: if $M \in S$ and $|\psi\rangle \in T$, then $ME|\psi\rangle = EM|\psi\rangle = E|\psi\rangle$, so $E|\psi\rangle \in T$ also.

> **[Gottesman thesis, §3.2]**: The logical operators satisfy:
> $$[\bar{X}_i, \bar{X}_j] = 0, \quad [\bar{Z}_i, \bar{Z}_j] = 0, \quad [\bar{X}_i, \bar{Z}_j] = 0 \;(i \neq j), \quad \{\bar{X}_i, \bar{Z}_i\} = 0$$

### Code Distance

> **[Gottesman thesis, §3.2]**: The code will have distance $d$ iff $N(S) - S$ contains no elements of weight less than $d$. If $S$ has elements of weight less than $d$ (except the identity), it is a degenerate code; otherwise it is a nondegenerate code. A nondegenerate stabilizer code satisfies:
> $$\langle\psi_i|E_a^\dagger E_b|\psi_j\rangle = \delta_{ab}\delta_{ij}$$

### Error Syndrome

> **[Gottesman thesis, §3.2]**: Let $f_M : \mathcal{G} \to \mathbb{Z}_2$,
> $$f_M(E) = \begin{cases} 0 & \text{if } [M, E] = 0 \\ 1 & \text{if } \{M, E\} = 0 \end{cases}$$
> and $f(E) = (f_{M_1}(E), \ldots, f_{M_{n-k}}(E))$, where $M_1, \ldots, M_{n-k}$ are the generators of $S$. Then $f(E)$ is some $(n-k)$-bit binary number which is $0$ iff $E \in N(S)$. For a nondegenerate code, $f(E)$ is different for each correctable error $E$.

### Example: Five-Qubit Code $[[5,1,3]]$

> **[Gottesman thesis, §3.3, Table 3.2]**: The five-qubit code stabilizer generators:
> $$M_1 = XZZXI, \quad M_2 = IXZZX, \quad M_3 = XIXZZ, \quad M_4 = ZXIXZ$$
> with $\bar{X} = XXXXX$ and $\bar{Z} = ZZZZZ$.

> **[Gottesman thesis, §3.3]**: The basis codewords are:
> $$|\bar{0}\rangle = \sum_{M \in S} M\;|00000\rangle$$
> $$|\bar{1}\rangle = \bar{X}|\bar{0}\rangle$$
> This code is cyclic, has distance three, and is nondegenerate. It is also a perfect code (every possible error syndrome is used by the single-qubit errors).

### Example: Shor's Nine-Qubit Code

> **[Gottesman thesis, §3.1]**: The stabilizer for Shor's nine-qubit code has 8 generators: $M_1 = Z_1Z_2$, $M_2 = Z_1Z_3$, $M_3 = Z_4Z_5$, $M_4 = Z_4Z_6$, $M_5 = Z_7Z_8$, $M_6 = Z_7Z_9$, $M_7 = X_1X_2X_3X_4X_5X_6$, $M_8 = X_1X_2X_3X_7X_8X_9$.

> **[Gottesman thesis, §3.1]**: The codewords are:
> $$|\bar{0}\rangle = (|000\rangle + |111\rangle)(|000\rangle + |111\rangle)(|000\rangle + |111\rangle)$$
> $$|\bar{1}\rangle = (|000\rangle - |111\rangle)(|000\rangle - |111\rangle)(|000\rangle - |111\rangle)$$
> This code is degenerate (distance 3, but $Z_1Z_2 \in S$).

### Encoding Codewords

> **[Gottesman thesis, §4.2, Eq. 4.1-4.2]**: The operation of encoding a stabilizer code can be written as:
> $$|c_1 \ldots c_k\rangle \to \left(\sum_{M \in S} M\right) \bar{X}_1^{c_1} \cdots \bar{X}_k^{c_k} |0\ldots 0\rangle$$
> $$= (I + M_1) \cdots (I + M_{n-k}) \bar{X}_1^{c_1} \cdots \bar{X}_k^{c_k} |0\ldots 0\rangle$$

### Code Constructions: Making New Codes from Old

> **[Gottesman thesis, §3.5]**: **Concatenation**: Suppose we have an $[n_1, k, d_1]$ code (stabilizer $S_1$) and encode each of its $n_1$ qubits using an $[n_2, 1, d_2]$ code (stabilizer $S_2$). The result is an $[n_1 n_2, k, d_1 d_2]$ code. The concatenated code has distance $d_1 d_2$ because operators in $N(S) - S$ must have distance at least $d_2$ on at least $d_1$ blocks of $n_2$ qubits.

> **[Gottesman thesis, §3.5]**: **Removing a qubit**: An $[n, k, d]$ code can be converted into an $[n-1, k+1, d-1]$ code by choosing generators appropriately and dropping two of them.

> **[Gottesman thesis, §3.5]**: **Adding a qubit**: Adding a new qubit and a new generator which is $X$ for the new qubit makes an $[n, k, d]$ code into an $[n+1, k, d]$ degenerate code.

---

## From Roffe's QEC Guide: Digitisation and Stabilizer Measurement

### Theorem: Digitisation of Quantum Errors **[Roffe, §2.2]**

Any coherent error process on a single qubit can be decomposed as:

$$U(\delta\theta, \delta\phi)|\psi\rangle = \alpha_I \mathbb{1}|\psi\rangle + \alpha_X X|\psi\rangle + \alpha_Z Z|\psi\rangle + \alpha_{XZ} XZ|\psi\rangle$$

**Significance**: The stabilizer measurement process involves projective measurements that cause the above superposition to collapse to a subset of its terms. Therefore, a quantum error correction code with the ability to correct $X$ and $Z$ errors can correct *any* coherent error. This is the **digitisation of the error** **[Roffe, §2.2]**.

### General Encoding via Stabilizer Projection **[Roffe, §3.3]**

The $|0\rangle_L$ codeword of any $[[n,k,d]]$ stabilizer code can be obtained via projection onto the $(+1)$ eigenspace of all stabilizers:

$$|0\rangle_L = \frac{1}{N} \prod_{P_i \in \langle \mathcal{S} \rangle} (\mathbb{1}^{\otimes n} + P_i) |0^{\otimes n}\rangle$$

where $\langle \mathcal{S} \rangle$ is the minimal generating set and $1/N$ ensures normalisation. This is implemented by the syndrome extraction circuit applied to $|0\rangle^{\otimes n}$.

### Theorem: Error Correction Success/Failure Conditions **[Roffe, §3.5]**

For a stabilizer code with recovery operation $\mathcal{R}$ applied after error $E$:

- **Success**: $\mathcal{R}E|\psi\rangle_L = (+1)|\psi\rangle_L$, which is satisfied if $\mathcal{R}E \in \mathcal{S}$ (trivially) or $\mathcal{R} = E^\dagger$.
- **Failure**: $\mathcal{R}E|\psi\rangle_L = L|\psi\rangle_L$, where $L$ is a logical operator. The state is returned to the codespace but the encoded information is changed.

### Degenerate Codes **[Roffe, §3.6]**

In degenerate codes, multiple distinct errors can map to the same syndrome. This does not reduce the code distance. For the Shor $[[9,1,3]]$ code, $Z_1$ and $Z_2$ both map to syndrome `00000010`, but the recovery $\mathcal{R} = Z_1$ succeeds for either: if $E = Z_1$, $\mathcal{R}E = I$; if $E = Z_2$, $\mathcal{R}E = Z_1Z_2 \in \mathcal{S}$ **[Roffe, §3.6]**.

### The $[[4,2,2]]$ Detection Code **[Roffe, §3.4]**

The smallest stabilizer code protecting against both $X$ and $Z$ errors. Stabilizers: $\mathcal{S}_{[[4,2,2]]} = \langle X_1X_2X_3X_4, Z_1Z_2Z_3Z_4 \rangle$. Codespace:

$$|00\rangle_L = \frac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle), \quad |01\rangle_L = \frac{1}{\sqrt{2}}(|0110\rangle + |1001\rangle)$$
$$|10\rangle_L = \frac{1}{\sqrt{2}}(|1010\rangle + |0101\rangle), \quad |11\rangle_L = \frac{1}{\sqrt{2}}(|1100\rangle + |0011\rangle)$$

Logical operators: $\bar{X}_1 = X_1X_3$, $\bar{Z}_1 = Z_1Z_4$, $\bar{X}_2 = X_2X_3$, $\bar{Z}_2 = Z_2Z_4$. Minimum-weight logical operator has weight 2, so $d = 2$ (detection code) **[Roffe, §3.4]**.

### Threshold Theorem **[Roffe, §5.2]**

The threshold theorem for stabilizer codes states that increasing the distance of a code will result in a corresponding reduction in the logical error rate $p_L$, provided the physical error rate $p$ satisfies $p < p_\text{th}$. For the surface code:

- Upper bound (statistical mechanics): $p_\text{th} \approx 10.9\%$ **[Dennis et al. 2002]**
- Practical MWPM decoder: $p_\text{th} \approx 10.3\%$ **[Roffe, §5.2]**
- With noisy syndrome measurement: $p_\text{th} \approx 1\%$ **[Roffe, §5.3]**

### Fault Tolerance **[Roffe, §5.3]**

A quantum error correction code is **fault tolerant** if it accounts for errors up to the code distance occurring at *any* location in the circuit. Key result: for a fault-tolerant syndrome extraction using Shor's method, $\lambda$ ancilla qubits are required to measure each stabilizer, where $\lambda$ is the number of non-identity elements **[Roffe, §5.3]**.

---

## Key Insight: Why the Stabilizer Formalism is Powerful

稳定子形式体系的核心威力在于**指数级压缩**：

1. **描述压缩**：一个 $n$ 量子比特的量子态需要 $2^n$ 个复振幅来描述。但一个稳定子态只需要 $n - k$ 个生成元（每个是 $n$ 个 Pauli 矩阵的张量积），即 $O(n^2)$ 个比特就能完全描述。

2. **运算压缩**：Clifford 运算（Hadamard, CNOT, Phase gate 等）在稳定子表示下只需要更新生成元的 Pauli 标签，每步 $O(n)$ 时间，而非在 $2^n$ 维 Hilbert 空间中做矩阵乘法。

3. **错误分析压缩**：错误 $E$ 对码空间的影响完全由 syndrome $\mathbf{s}(E) \in \mathbb{F}_2^{n-k}$ 描述，这是一个简单的二元向量运算。

4. **与经典编码理论的桥梁**：通过 $\mathbb{F}_2$ 上的 symplectic 表示，稳定子码可以映射到经典线性码的问题，利用成熟的经典编码理论工具。

| 表示方法 | 描述复杂度 | 运算复杂度 |
|---------|-----------|-----------|
| 态向量 | $O(2^n)$ | $O(4^n)$ |
| 密度矩阵 | $O(4^n)$ | $O(8^n)$ |
| 稳定子 | $O(n^2)$ | $O(n^2)$ per Clifford gate |

---

## Usage in Research

1. **量子纠错码设计**：几乎所有实用的 QEC 码（表面码、色码、量子 LDPC 码）都是稳定子码
2. **量子电路模拟**：Gottesman-Knill 定理——稳定子态 + Clifford 门 + Pauli 测量可以在 $O(n^2)$ 时间内经典模拟
3. **量子噪声分析**：Pauli twirling 将一般噪声简化为 Pauli 信道，与稳定子框架完美配合
4. **解码器设计**：syndrome 的线性结构使得可以用图论、匹配、置信传播等经典算法进行高效解码
5. **容错量子计算**：magic state distillation 和 transversal gates 的理论基础建立在稳定子框架上

---

## Nielsen & Chuang: Theorems and Formal Results (Chapter 10)

### Chapter 10 Overview **[Nielsen & Chuang, Ch. 10, pp.425-499]**
Chapter 10 "Quantum error-correction" covers the stabilizer formalism in depth in Sections 10.5 (pp.453-470). The treatment builds from the theory of classical linear codes through CSS codes to the general stabilizer framework.

### Definition (Stabilizer Code) **[Nielsen & Chuang, Section 10.5.1, p.456]**
Let $S$ be an Abelian subgroup of the Pauli group $G_n$ such that $-I \notin S$. The stabilizer code $C(S)$ is the subspace of the $n$-qubit Hilbert space fixed by all elements of $S$:
$$C(S) = \{|\psi\rangle : g|\psi\rangle = |\psi\rangle \text{ for all } g \in S\}$$

### Theorem 10.3 (Stabilizer Codes Exist) **[Nielsen & Chuang, Theorem 10.3, p.457]**
Let $S$ be an Abelian subgroup of $G_n$ not containing $-I$, with $n-k$ independent generators. Then $C(S)$ is a $2^k$-dimensional subspace encoding $k$ logical qubits into $n$ physical qubits.

### Theorem 10.4 (Normalizer and Logical Operators) **[Nielsen & Chuang, Theorem 10.4, p.458]**
The normalizer $N(S)$ of $S$ in $G_n$ consists of all elements of $G_n$ that commute with every element of $S$:
$$N(S) = \{g \in G_n : gsg^\dagger \in S \text{ for all } s \in S\}$$
For the Pauli group, this equals the centralizer. Elements in $N(S) \setminus S$ are logical operators that act non-trivially on the codespace.

### Theorem 10.8 (Error-Correction Conditions for Stabilizer Codes) **[Nielsen & Chuang, Theorem 10.8, p.465]**
Let $S$ be the stabilizer for a stabilizer code $C(S)$. Suppose $\{E_j\}$ is a set of operators in $G_n$ such that $E_j^\dagger E_k \notin N(S) - S$ for all $j$ and $k$. Then $\{E_j\}$ is a correctable set of errors for the code $C(S)$. Without loss of generality we can restrict to $E_j$ with $E_j^\dagger = E_j$, reducing the condition to $E_j E_k \notin N(S) - S$.

**Proof** **[Nielsen & Chuang, pp.465-466]**: Let $P$ be the projector onto $C(S)$. Two cases: (1) If $E_j^\dagger E_k \in S$, then $PE_j^\dagger E_k P = P$. (2) If $E_j^\dagger E_k \in G_n - N(S)$, it anticommutes with some generator $g_1$. Using $P = \prod_l(I+g_l)/2^{n-k}$ and anticommutativity: $PE_j^\dagger E_k P = 0$ since $P(I-g_1) = 0$. Both cases satisfy the quantum error-correction conditions (Theorem 10.1).

### Theorem 10.6 (Normalizer Generated by Clifford Gates) **[Nielsen & Chuang, Theorem 10.6, p.461]**
Suppose $U$ is any unitary on $n$ qubits such that $UgU^\dagger \in G_n$ for all $g \in G_n$. Then up to a global phase, $U$ can be composed from $O(n^2)$ Hadamard, phase, and controlled-NOT gates.

### Corollary (Code Distance) **[Nielsen & Chuang, p.467]**
The distance $d$ of a stabilizer code $C(S)$ is the minimum weight of an element of $N(S) - S$. Denoted $[[n,k,d]]$. By Theorem 10.8, distance $\geq 2t+1$ corrects arbitrary errors on $t$ qubits.

### Definition (Syndrome) **[Nielsen & Chuang, Section 10.5.2, p.459]**
For each generator $g_i$ of $S$ and error $E \in G_n$, the syndrome bit is $s_i = 0$ if $[g_i, E] = 0$ and $s_i = 1$ if $\{g_i, E\} = 0$. The syndrome vector $\mathbf{s} = (s_1, \ldots, s_{n-k})$ identifies the error equivalence class without revealing the encoded information.

### Codespace Projector **[Nielsen & Chuang, Eq. 10.72, p.457]**
$$P = \frac{1}{|S|}\sum_{g \in S} g = \prod_{i=1}^{n-k}\frac{I + g_i}{2}$$

### Gottesman-Knill Theorem **[Nielsen & Chuang, Theorem 10.7, p.464]**
A quantum circuit using only the following elements can be efficiently simulated on a classical computer:
1. State preparation in the computational basis
2. Hadamard gates, Phase gates ($S$), CNOT gates (i.e., Clifford group gates)
3. Measurements in the computational basis
4. Classical feed-forward of measurement results

The simulation runs in $O(n^2)$ time per gate, where $n$ is the number of qubits.

### CSS Code Construction **[Nielsen & Chuang, Section 10.4.2, p.450]**
Given classical codes $C_1$ and $C_2$ with $C_2^\perp \subseteq C_1$ (equivalently $C_2 \subseteq C_1^\perp$), the CSS code has parameters:
$$\text{CSS}(C_1, C_2) = [[n, k_1 + k_2 - n, d]]$$
where $d \geq \min(\text{wt}(C_1 \setminus C_2^\perp), \text{wt}(C_2 \setminus C_1^\perp))$.

### Quantum Hamming Bound **[Nielsen & Chuang, Eq. 10.57, p.444]**
For a non-degenerate $[[n, k, 2t+1]]$ code:
$$\sum_{j=0}^{t}\binom{n}{j}3^j \leq 2^{n-k}$$

### Quantum Singleton Bound **[Nielsen & Chuang, Theorem 10.2, p.444]**
$$k + 2d \leq n + 2$$
or equivalently $d \leq \lfloor(n-k)/2\rfloor + 1$.

### Table 10.1: Important Stabilizer Codes **[Nielsen & Chuang, Table 10.1, p.470]**

| Code | $[[n,k,d]]$ | Generators |
|------|-------------|------------|
| Bit-flip | $[[3,1,1]]$ | $Z_1Z_2, Z_2Z_3$ |
| Phase-flip | $[[3,1,1]]$ | $X_1X_2, X_2X_3$ |
| Shor | $[[9,1,3]]$ | 8 generators (see text) |
| Steane | $[[7,1,3]]$ | 6 generators from Hamming code |
| Five-qubit | $[[5,1,3]]$ | $XZZXI, IXZZX, XIXZZ, ZXIXZ$ |

### Fault-Tolerant Quantum Computation **[Nielsen & Chuang, Section 10.6, pp.470-499]**

**Threshold Theorem** **[Nielsen & Chuang, Theorem 10.6, p.480]**: There exists a threshold error rate $p_{\text{th}} > 0$ such that if the error rate per gate $p < p_{\text{th}}$, then an arbitrary long quantum computation can be performed reliably using concatenated coding with polylogarithmic overhead.

**Transversal Gates** **[Nielsen & Chuang, p.474]**: A gate is transversal if it acts independently on corresponding qubits in each code block. Transversal gates are automatically fault-tolerant because they do not propagate errors within a block.

---

## From Steane's Tutorial: Error Operators and Symplectic Structure

### Binary Vector Notation for Pauli Products **[Steane, p.10-11]**

Steane introduces compact notation for tensor products of Pauli matrices using binary vectors $u, v \in \mathbb{F}_2^n$:

$$X_u Z_v \equiv X_1^{u_1} Z_1^{v_1} \otimes X_2^{u_2} Z_2^{v_2} \otimes \cdots \otimes X_n^{u_n} Z_n^{v_n}$$

**Example** [Steane, p.11]: $X \otimes I \otimes Z \otimes Y \otimes X \equiv X_{10011} Z_{00110}$ (since $Y = -iXZ$, up to phase).

The weight of an error operator is the number of terms not equal to $I$. For instance, $X_{10011}Z_{00110}$ has length 5, weight 4 [Steane, p.11].

### Commutation via Symplectic Inner Product **[Steane, p.15]**

Two error operators $M = X_u Z_v$ and $M' = X_{u'} Z_{v'}$ satisfy:

$$X_u Z_v = (-1)^{u \cdot v} Z_v X_u$$

and commute if and only if the **symplectic inner product** vanishes [Steane, p.15]:

$$u \cdot v' + v \cdot u' = 0 \pmod{2}$$

### Stabilizer as Binary Matrix **[Steane, p.15]**

The stabilizer is uniquely specified by an $(n-k) \times 2n$ binary matrix [Steane, p.15]:

$$H = (H_x \mid H_z)$$

where rows encode the $X$ and $Z$ parts of each generator. The Abelian (commutativity) condition becomes:

$$H_x H_z^T + H_z H_x^T = 0 \pmod{2}$$

The dual matrix $G = (G_x \mid G_z)$ satisfies $H_x G_z^T + H_z G_x^T = 0$, and has $n+k$ rows. All error operators not in $G$ anticommute with at least one member of $H$ and are thus detectable [Steane, p.15].

### Syndrome Extraction via Ancilla **[Steane, p.12-13]**

Steane describes syndrome extraction by attaching an $(n-k)$-qubit ancilla and using the standard eigenvalue measurement method [Steane, p.12]:

> Prepare ancilla in $(|0\rangle + |1\rangle)/\sqrt{2}$. Operate controlled-$M$ with ancilla as control, system as target, then Hadamard-rotate the ancilla. The final state is $[(1+\lambda)|0\rangle + (1-\lambda)|1\rangle]/2$ where $\lambda = \pm 1$ is the eigenvalue.

The full process on a noisy encoded state $\sum_i (E_i|\phi\rangle_L)|\psi_i\rangle_e$ yields [Steane, p.12]:

$$|0\rangle_a \sum_i (E_i|\phi\rangle_L)|\psi_i\rangle_e \;\to\; \sum_i |s_i\rangle_a (E_i|\phi\rangle_L)|\psi_i\rangle_e$$

Measuring the ancilla collapses the sum to a single error term, yielding the syndrome $s_i$.

### Degenerate Codes **[Steane, p.13]**

When two errors $E_1, E_2$ have the same syndrome but $E_1 E_2 \in \mathcal{S}$, both are correctable because applying $E_1$ as recovery after $E_2$ occurred gives $E_1 E_2|\phi\rangle_L = |\phi\rangle_L$ [Steane, p.13]. Steane notes this phenomenon has no classical analogue, and degenerate codes are not constrained by the quantum Hamming bound.

---

## From Bacon's Introduction: Stabilizer Error Correction Criterion

### Anticommutation as Detection Mechanism **[Bacon, p.65-66]**

Bacon provides a clean derivation of why anticommutation enables error detection. Given stabilizer generators $S_i$ with $S_i|\psi\rangle = |\psi\rangle$ for code states, if error product $E_k^\dagger E_l$ anticommutes with some $S_i$ [Bacon, p.66]:

$$\langle\psi_i|E_k^\dagger E_l|\psi_j\rangle = \langle\psi_i|E_k^\dagger E_l S_i|\psi_j\rangle = -\langle\psi_i|S_i E_k^\dagger E_l|\psi_j\rangle = -\langle\psi_i|E_k^\dagger E_l|\psi_j\rangle$$

Therefore $\langle\psi_i|E_k^\dagger E_l|\psi_j\rangle = 0$, satisfying the quantum error-correcting criterion [Bacon, p.66].

### Stabilizer Subspace Measurement **[Bacon, p.52]**

The operators $S_1 = Z \otimes Z \otimes I$ and $S_2 = Z \otimes I \otimes Z$ for the 3-qubit bit-flip code yield syndrome eigenvalues that identify error subspaces without disturbing encoded information [Bacon, p.52]:

| Basis states of subspace | $S_1$ | $S_2$ | Error |
|--------------------------|-------|-------|-------|
| $\{|000\rangle, |111\rangle\}$ | $+1$ | $+1$ | $I \otimes I \otimes I$ |
| $\{|100\rangle, |011\rangle\}$ | $-1$ | $-1$ | $X \otimes I \otimes I$ |
| $\{|010\rangle, |101\rangle\}$ | $-1$ | $+1$ | $I \otimes X \otimes I$ |
| $\{|001\rangle, |110\rangle\}$ | $+1$ | $-1$ | $I \otimes I \otimes X$ |

### Digitization of Quantum Errors **[Bacon, p.54; NordiQUEst, p.34-35]**

Bacon shows that a code designed for discrete Pauli errors also corrects continuous errors. If correctable errors $\{F_k\}$ satisfy the diagonal error-correcting criterion, and actual errors $G_l = \sum_p f_{lp} F_p$ are linear combinations, then recovery still works [Bacon, p.61]:

$$\sum_k R_k \left(\sum_l G_l \rho_C G_l^\dagger\right) R_k^\dagger = \left(\sum_{k,l} d_k |f_{lk}|^2\right) \rho_C$$

NordiQUEst states this principle concisely [NordiQUEst, p.35]: measurement turns continuous errors into discrete errors. After syndrome measurement, $E|\psi\rangle = (e_0 I + e_1 X + e_2 Y + e_3 Z)|\psi\rangle$ collapses to $\eta_i \sigma_i|\psi\rangle$ where $\sigma_i \in \{I,X,Y,Z\}$ and $\eta_i$ is an irrelevant global phase.

---

## From Surface Code Notes (Fowler 2025): Stabilizer Sign Tracking

### Stabilizer Sign Detection Circuit **[Surface Notes, p.2]**

Fowler provides the stabilizer measurement circuit and its analysis [Surface Notes, p.2]:

Given operator $A$ with $A^2 = I$, the circuit $|0\rangle \xrightarrow{H} |+\rangle \xrightarrow{\text{ctrl-}A} \xrightarrow{H} \xrightarrow{M}$ produces:

$$|0\rangle|\Psi\rangle \xrightarrow{H} |+\rangle|\Psi\rangle \xrightarrow{\text{ctrl-}A} \frac{1}{\sqrt{2}}(|0\rangle|\Psi\rangle + |1\rangle A|\Psi\rangle) \xrightarrow{H,M} |\Psi_M\rangle$$

where $A|\Psi_M\rangle = (-1)^M|\Psi_M\rangle$. The output is the $+1$ eigenstate of $A$ if $M=0$, or the $-1$ eigenstate if $M=1$ [Surface Notes, p.2].

Crucially, this circuit not only detects the stabilizer sign but also **projects** errors: an arbitrary error $E$ that neither commutes nor anticommutes with stabilizer $A$ gets projected to either a commuting or anticommuting component [Surface Notes, p.2].

---

## References

- **[Nielsen & Chuang]** Nielsen, M. A. & Chuang, I. L. *Quantum Computation and Quantum Information* (Cambridge, 10th anniversary ed., 2010), Ch. 10 (pp.425-499)
- **[Steane]** Steane, A. M. "A Tutorial on Quantum Error Correction." Proc. Int. School of Physics "Enrico Fermi", course CLXII (IOS Press, 2006), pp. 1-32.
- **[Bacon]** Bacon, D. "Introduction to quantum error correction." Ch. 2 in *Quantum Error Correction*, ed. Lidar & Brun (Cambridge, 2013), pp. 46-106.
- **[Surface Notes]** Fowler, A. G. "Surface code quantum computation." Google Quantum AI (2025).
- **[NordiQUEst]** Lenssen, Martres, Myneni, Fuchs. "Quantum Error Correction - Theory and Hands-on." NordiQUEst workshop (2024).
- Gottesman, D. "Stabilizer Codes and Quantum Error Correction." PhD thesis, Caltech (1997). arXiv:quant-ph/9705052
- Aaronson, S. & Gottesman, D. "Improved simulation of stabilizer circuits." PRA 70, 052328 (2004).
- Fujii, K. "Quantum Computation with Topological Codes." SpringerBriefs in Mathematical Physics (2015), Ch.2.

---

## Additions from Fujii's "Quantum Computation with Topological Codes" (2015)

### Clifford Operations on Stabilizer States [Fujii, Ch.2, §2.2]

> **[Fujii, Ch.2, §2.2]**: Clifford 操作 $U$ 在共轭下将 Pauli 乘积映射为另一个 Pauli 乘积。对于稳定子态 $|\psi\rangle$（稳定子群 $\mathcal{S} = \langle \{S_i\} \rangle$），作用表示为稳定子群的变换：
>
> $$U|\psi\rangle = US_i|\psi\rangle = (US_iU^\dagger)U|\psi\rangle = S'_i U|\psi\rangle, \quad S'_i \equiv US_iU^\dagger$$
>
> 这对应量子计算的 Heisenberg 图像——追踪算子的演化而非态的演化。

**CNOT 门变换规则** [Fujii, Ch.2, Eqs.(2.33)-(2.36)]：

$$\Lambda_{c,t}(X)\,X_c\,\Lambda_{c,t}(X) = X_cX_t, \quad \Lambda_{c,t}(X)\,Z_t\,\Lambda_{c,t}(X) = Z_cZ_t$$

$$\Lambda_{c,t}(X)\,X_t\,\Lambda_{c,t}(X) = X_t, \quad \Lambda_{c,t}(X)\,Z_c\,\Lambda_{c,t}(X) = Z_c$$

### Gottesman-Knill Theorem [Fujii, Ch.2, §2.4]

> **[Fujii, Ch.2, Theorem 2.1]**: 任何 Clifford 操作作用在 $|0\rangle^{\otimes n}$ 上后进行 $Z$ 基测量，可在**强意义**下经典多项式时间模拟（即可计算任意边际分布 $P_C(x)$）。

> **[Fujii, Ch.2, Theorem 2.2]**: 扩展至 Pauli 基态凸混合的乘积态输入——可**弱意义**模拟（采样输出分布）。凸混合位于 Bloch 球八面体内部；八面体外的态（如 magic state $e^{-i(\pi/8)Z}|+\rangle$）可通过 gate teleportation 实现非 Clifford 门。

### Graph States [Fujii, Ch.2, §2.5]

> **[Fujii, Ch.2, §2.5]**: 图态由图 $G=(V,E)$ 定义，稳定子生成元 $K_i = X_i\prod_{j\in V_i}Z_j$，生成方式：$|G\rangle = \prod_{(i,j)\in E}\Lambda(Z)_{i,j}|+\rangle^{\otimes|V|}$。

Pauli 基测量变换图态：$Z$ 基删除顶点及关联边；$X$ 基收缩；$Y$ 基改变链长奇偶性。任何稳定子态在局部 Clifford 下等价于某个图态（局部互补性）。

### MBQC Operator Formulation [Fujii, Ch.2, §2.6]

> **[Fujii, Ch.2, §2.6]**: 一维 cluster state 上第 $i$ 步的逻辑算子：$L_X^{(i)} = X_iZ_{i+1}$，$L_Y^{(i)} = Y_iZ_{i+1}$，$L_Z^{(i)} = Z_i$。$Z$ 旋转 $e^{-i(\theta/2)Z_i}$ 后 $X$ 基测量将逻辑算子变换为 $U\equiv X^{m_i}He^{-i(\theta/2)Z}$。Byproduct 传播：
>
> $$U = X^{m_{i+2}\oplus m_i}Z^{m_{i+1}}He^{i(-1)^{m_{i+1}}\phi'Z}He^{i(-1)^{m_i}\theta'Z}He^{i\xi Z}$$

### QEC 纠错过程 [Fujii, Ch.2, §2.7]

> **[Fujii, Ch.2, §2.7, Eq.(2.100)]**: 三量子比特翻转码恢复后：$\mathcal{R}\circ\mathcal{E}_1\circ\mathcal{E}_2\circ\mathcal{E}_3|\psi_L\rangle\langle\psi_L| = [(1-p)^3+3p(1-p)^2]|\psi_L\rangle\langle\psi_L|+O(p^2)$。

任何单量子比特噪声 Kraus 算子可 Pauli 分解 $K_j=\sum_l c_{jl}\sigma_l$。若码纠正 $X$ 和 $Z$，则自动纠正任意单量子比特噪声——syndrome 测量将连续噪声坍缩为离散 Pauli 错误。

### 7-Qubit Steane Code Transversality [Fujii, Ch.2, §2.7]

> **[Fujii, Ch.2, §2.7]**: 7-qubit Steane 码横截操作：$\bar{H}=H^{\otimes7}$（逻辑 Hadamard），$\bar{S}=(ZS)^{\otimes7}$（逻辑 Phase），$\bar{\Lambda}(X)=\Lambda(X)^{\otimes7}$（逻辑 CNOT）。整个 Clifford 群可横截实现，天然容错。非 Clifford 门需 magic state distillation。

---

## From Steane's QEC Tutorial

### Classical-to-Quantum Error Correction Bridge **[Steane Tutorial, §2]**

Steane 强调量子纠错与经典纠错的深层联系。经典线性码 $C[n, k, d]$ 由奇偶校验矩阵 $H$ 定义：$C = \{x \in \mathbb{F}_2^n : Hx = 0\}$。Syndrome: $s = He$。

**量子纠错的三个障碍及其解决** **[Steane Tutorial, §2.1-2.3]**：

1. **No-cloning 定理**：不能复制未知量子态，但可以通过**纠缠**建立冗余——将逻辑信息编码在多体纠缠态中
2. **测量坍缩**：直接测量会破坏叠加态，但**间接测量**（syndrome extraction 通过 ancilla）只提取错误信息而不坍缩编码内容
3. **连续错误**：量子错误是连续的（如小角旋转 $e^{i\epsilon Z}$），但 syndrome 测量将其**离散化**为 Pauli 错误——这是量子纠错最深刻的洞察之一

**错误离散化的详细推导** **[Steane Tutorial, §2.3]**：

设连续错误 $\mathcal{E}(\rho) = E\rho E^\dagger$，其中 $E = \alpha I + \beta X + \gamma Z + \delta Y$。测量稳定子 $g_i$ 后，态被投影到 $g_i$ 的 $\pm 1$ 特征子空间。由于 Pauli 算子 $\{I, X, Y, Z\}$ 分别位于不同的 syndrome sector（不同的对易/反对易模式），测量过程将连续叠加坍缩为离散的 Pauli 错误分支，每个分支的概率为 $|\alpha|^2, |\beta|^2, |\gamma|^2, |\delta|^2$。

### 量子纠错的基本条件 **[Steane Tutorial, §3]**

#### Knill-Laflamme 定理 **[Steane Tutorial, §3.1]**

**定理（Knill-Laflamme, 1997; Bennett et al., 1996）**：量子码 $\mathcal{C}$ 能纠正错误集 $\{E_a\}$ 当且仅当：

$$\langle i|E_a^\dagger E_b|j\rangle = C_{ab} \delta_{ij}$$

对所有码字 $|i\rangle, |j\rangle \in \mathcal{C}$ 和所有 $E_a, E_b$ 成立，其中 $C_{ab}$ 是一个与码字无关的 Hermitian 矩阵。

**物理含义**：

- $\delta_{ij}$ 条件：不同码字在错误后保持正交，保证可区分
- $C_{ab}$ 与 $i,j$ 无关：错误对所有码字的影响是"均匀的"，编码信息不泄露

**对稳定子码的简化** **[Steane Tutorial, §3.2]**：

对稳定子码，Knill-Laflamme 条件简化为：$E_a^\dagger E_b \in \mathcal{S} \cup (\mathcal{G}_n \setminus N(\mathcal{S}))$。

即 $E_a^\dagger E_b$ 要么是稳定子（两个错误等价——简并情况），要么与某个稳定子反对易（可被检测）。

#### 推论：非简并码的纯正交条件 **[Steane Tutorial, §3.2]**

对非简并码：$\langle i|E_a^\dagger E_b|j\rangle = \delta_{ab}\delta_{ij}$。这意味着不同的可纠正错误将码空间映射到完全正交的子空间——每个 syndrome 唯一对应一个错误。

### CSS Code Construction **[Steane Tutorial, §4]**

给定两个经典线性码 $C_1[n, k_1, d_1]$ 和 $C_2[n, k_2, d_2]$，满足 $C_2^\perp \subseteq C_1$，构造量子码：

$$\text{CSS}(C_1, C_2) = [[n, k_1 + k_2 - n, d \geq \min(d_1, d_2)]]$$

码字：$|x + C_2^\perp\rangle = \frac{1}{\sqrt{|C_2^\perp|}} \sum_{y \in C_2^\perp} |x + y\rangle$，其中 $x \in C_1$。

$X$ 错误由 $C_1$ 的校验矩阵检测，$Z$ 错误由 $C_2$ 的校验矩阵检测。

### Steane Code Detail **[Steane Tutorial, §4.2]**

由 $[7, 4, 3]$ Hamming 码自对偶构造（$C^\perp \subset C$）。校验矩阵：

$$H = \begin{pmatrix} 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 0 & 0 & 1 & 1 \\ 1 & 0 & 1 & 0 & 1 & 0 & 1 \end{pmatrix}$$

稳定子生成元由 $H$ 矩阵的行确定（$X$ 型和 $Z$ 型各 3 个）：

$$g_1^X = X_4 X_5 X_6 X_7, \quad g_2^X = X_2 X_3 X_6 X_7, \quad g_3^X = X_1 X_3 X_5 X_7$$
$$g_1^Z = Z_4 Z_5 Z_6 Z_7, \quad g_2^Z = Z_2 Z_3 Z_6 Z_7, \quad g_3^Z = Z_1 Z_3 Z_5 Z_7$$

逻辑算子：$\bar{X} = X^{\otimes 7}$，$\bar{Z} = Z^{\otimes 7}$。

### Steane Syndrome Extraction **[Steane Tutorial, §5]**

不需要逐个测量稳定子。而是准备编码的 ancilla 态，通过 transversal CNOT 一步提取所有 syndrome 位：

1. 准备 ancilla 在 $|\bar{0}\rangle_{anc}$
2. Transversal CNOT（data $\to$ ancilla）
3. 测量 ancilla 所有 7 个量子比特，从中提取 $Z$ syndrome

优势：transversal CNOT 不传播错误，天然容错。

**Steane extraction 与 Shor extraction 的比较** **[Steane Tutorial, §5.2]**：

| 方法 | Ancilla 准备 | 容错机制 | 适用码 |
|------|-------------|---------|--------|
| Shor | Cat state $\frac{1}{\sqrt{2}}(\|00...0\rangle + \|11...1\rangle)$ + 验证 | 每个数据比特连接不同 ancilla 比特 | 一般稳定子码 |
| Steane | 编码的 $\|\bar{0}\rangle$ 或 $\|\bar{+}\rangle$ | Transversal CNOT 天然不传播错误 | CSS 码 |
| Knill | 编码的 Bell 对 | 隐形传态自动纠错 | 一般稳定子码 |

**Steane extraction 数学公式** **[Steane Tutorial, §5.1]**：

初始态 $|\psi\rangle_{\text{data}} \otimes |\bar{0}\rangle_{\text{anc}}$。Transversal CNOT 后：

$$\text{CNOT}^{\otimes n}: |x\rangle_D |\bar{0}\rangle_A \to |x\rangle_D |x \oplus \bar{0}\rangle_A$$

对码字 $|\bar{0}\rangle = \sum_{c \in C_2^\perp} |c\rangle$，作用后测量 ancilla 得到 $x \oplus c$（某个 $c \in C_2^\perp$），其 syndrome $H(x \oplus c) = Hx$（因为 $Hc = 0$）。

### Transversal Gates for QEC Codes **[Steane Tutorial, §6]**

**定义** **[Steane Tutorial, §6.1]**：Transversal gate 是在码块内逐比特独立操作的门，形如 $U^{\otimes n}$ 或 $U_1 \otimes U_2 \otimes \cdots \otimes U_n$（不同比特可用不同单比特门）。

**容错性**：Transversal gate 天然容错，因为码块内第 $i$ 个量子比特上的错误不会传播到第 $j$ 个量子比特（$i \neq j$）。

**Eastin-Knill 定理** **[Steane Tutorial, §6.3]**：不存在能横截实现所有逻辑门的量子码。这意味着至少一个逻辑门需要非横截方法（如 magic state distillation）。

### Noise Models Overview **[Steane Tutorial, §2.5]**

**Amplitude damping channel**（描述能量弛豫 $T_1$ 过程）：

$$\mathcal{A}_\gamma(\rho) = E_0 \rho E_0^\dagger + E_1 \rho E_1^\dagger, \quad E_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{pmatrix}, \quad E_1 = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix}$$

此信道不是 Pauli 信道，但可通过 Pauli twirling 近似为等效去极化噪声。Steane 指出这种近似在分析稳定子码性能时通常是合理的，因为 Pauli twirling 保留了一阶错误率行为。

---

## From Bacon's Introduction to QEC

### Quantum No-Cloning and Error Discretization **[Bacon, §1]**

Bacon 从三个困难出发：(1) no-cloning 禁止直接冗余; (2) 测量坍缩叠加; (3) 连续错误（小角度旋转）。

**关键洞察**：syndrome 测量将连续错误"离散化"为 Pauli 错误。测量 syndrome 坍缩错误的"类型"，但不坍缩编码信息。

**三量子比特翻转码的完整分析** **[Bacon, §1.2]**：

编码：$|0\rangle \to |000\rangle$，$|1\rangle \to |111\rangle$。稳定子 $\{Z_1Z_2, Z_2Z_3\}$。对一般单比特错误 $E = aI + bX$（作用于第 1 个比特），syndrome 测量后：

- Syndrome $(0,0)$：态坍缩为 $aI|\psi_L\rangle$，概率 $|a|^2$ —— 无错误
- Syndrome $(1,0)$：态坍缩为 $bX_1|\psi_L\rangle$，概率 $|b|^2$ —— 已知第 1 比特翻转

测量过程将连续的 $a, b$ 系数坍缩为离散的两种情况，同时不暴露 $\alpha, \beta$（逻辑信息）。

### Symplectic Representation **[Bacon, §3]**

$n$ 量子比特 Pauli 群元素用 $2n$ 位二进制向量表示：$P \mapsto (\mathbf{a} | \mathbf{b}) \in \mathbb{F}_2^{2n}$。

其中 $\mathbf{a} = (a_1, \ldots, a_n)$ 记录 $X$ 分量，$\mathbf{b} = (b_1, \ldots, b_n)$ 记录 $Z$ 分量：

$$P = i^{\phi} \prod_{j=1}^n X_j^{a_j} Z_j^{b_j}$$

对易性由 symplectic 内积决定：

$$\lambda(P, Q) = \mathbf{a}_P \cdot \mathbf{b}_Q + \mathbf{a}_Q \cdot \mathbf{b}_P \pmod{2}$$

- 0：对易; 1：反对易

稳定子码的 check matrix $H = (H_X \;|\; H_Z)$，对易条件：$H_X H_Z^T + H_Z H_X^T = 0 \pmod{2}$。

**Symplectic 表示的优势** **[Bacon, §3.2]**：

1. 码设计问题简化为 $\mathbb{F}_2$ 上的线性代数
2. Syndrome 计算变为矩阵-向量乘法：$\mathbf{s} = H_X \mathbf{b}_E + H_Z \mathbf{a}_E \pmod{2}$
3. 码距 $d = \min\{\text{wt}(v) : v \in N(S) \setminus S\}$ 变为在 $\mathbb{F}_2^{2n}$ 中寻找满足 symplectic 约束的最小权重向量

### Erasure Channel and Its Properties **[Bacon, §2.5]**

**定义**：以概率 $p$ 量子比特被"擦除"（丢失），且已知哪些量子比特被擦除。

$$\mathcal{E}_{\text{erase}}(\rho) = (1-p)\rho + p\,|e\rangle\langle e|$$

**Bacon 的关键论述** **[Bacon, §2.5]**：

- 擦除错误是最容易纠正的噪声类型——因为已知错误位置
- 一个 $[[n, k, d]]$ 码可以纠正最多 $d-1$ 个擦除错误（而非 $\lfloor(d-1)/2\rfloor$ 个 Pauli 错误）
- 擦除阈值总是高于 Pauli 阈值（表面码: $50\%$ vs $\sim 11\%$）
- 近年来许多量子架构（如双轨光子、cat qubits）利用可检测泄漏将 Pauli 噪声转化为擦除噪声

### Subsystem Codes (Operator QEC) **[Bacon, §5]**

Hilbert 空间分解为 $\mathcal{H} = (\mathcal{H}_A \otimes \mathcal{H}_B) \oplus \mathcal{H}_C$：$\mathcal{H}_A$ 是逻辑子系统，$\mathcal{H}_B$ 是 gauge 子系统，$\mathcal{H}_C$ 是错误子空间。

Gauge group $\mathcal{G}$ 不要求对易，其中心 $Z(\mathcal{G}) = \mathcal{S}$ 是稳定子群。

**Operator QEC 条件** **[Bacon, §5.1]**：

$$\Pi_A E_a^\dagger E_b \Pi_A = C_{ab} \Pi_A$$

其中 $\Pi_A$ 是逻辑子系统 $\mathcal{H}_A$ 上的投影。关键区别：$C_{ab}$ 可以是 $\mathcal{H}_B$ 上的非平凡算子（作用在 gauge 自由度上），而不仅仅是标量。

### Bacon-Shor Code **[Bacon, §5.2]**

$d \times d$ 排列的 $[[d^2, 1, d]]$ 码：
- Gauge 算子：同行相邻 $XX$，同列相邻 $ZZ$（均为 weight-2）
- 稳定子：整行 $X^{\otimes d}$ 对，整列 $Z^{\otimes d}$ 对
- 所有测量均为 weight-2，极其简单
- 缺点：码率 $1/d^2$ 低

**Gauge fixing** **[Bacon, §5.3]**：通过测量 gauge 算子，可以将 Bacon-Shor 码"固定"为标准的 Shor 码或 Surface code 的变体。Gauge fixing 是连接 subsystem codes 和 subspace codes 的桥梁。

### Quantum Bounds **[Bacon, §2.3-2.4]**

**Singleton bound**: $n - k \geq 2(d - 1)$，即 $k \leq n - 2d + 2$。

**Hamming bound**（非简并码）: $\sum_{j=0}^{t} \binom{n}{j} 3^j \leq 2^{n-k}$。

注：简并码可以违反 Hamming bound。

**Gilbert-Varshamov bound（量子版）** **[Bacon, §2.4]**：

存在 $[[n, k, d]]$ 稳定子码当：

$$\frac{2^n}{\sum_{j=0}^{d-1} \binom{n}{j} 3^j} \geq 2^{n-k}$$

即 $k \geq n - (d-1)\log_2 3 - h_2(\cdot)$（渐近形式）。

### Noise Discretization Theorem **[Bacon, §2.1]**

**定理（Bacon 的表述）**：设量子码 $\mathcal{C}$ 能纠正 Pauli 错误集 $\{E_a\}$。则 $\mathcal{C}$ 能纠正任何量子信道 $\mathcal{E}$，只要 $\mathcal{E}$ 的 Kraus 算子可以展开为 $\{E_a\}$ 的线性组合。

**证明思路** **[Bacon, §2.1]**：设 $\mathcal{E}(\rho) = \sum_j K_j \rho K_j^\dagger$，每个 $K_j = \sum_a c_{ja} E_a$。syndrome 测量将 $K_j|\psi\rangle$ 投影到 $E_a|\psi\rangle$（某个特定的 $a$），概率为 $|c_{ja}|^2$。之后施加 $E_a^\dagger$ 恢复。这表明纠正离散 Pauli 错误自动纠正连续错误。

---

## Updated References

- Gottesman, D. "Stabilizer Codes and Quantum Error Correction." PhD thesis, Caltech (1997). arXiv:quant-ph/9705052
- Nielsen, M. A. & Chuang, I. L. "Quantum Computation and Quantum Information." Cambridge (2000/2010), Ch. 10.
- Aaronson, S. & Gottesman, D. "Improved simulation of stabilizer circuits." PRA 70, 052328 (2004).
- Fujii, K. "Quantum Computation with Topological Codes." SpringerBriefs (2015), Ch.2.
- **[Preskill, Ch.7]** Preskill, J. *Lecture Notes for Ph219/CS219: Quantum Information*, Ch.7: "Quantum Error Correction". Stabilizer codes (§7.9, pp.34-41), Pauli group structure (§7.9.1, pp.34-38), symplectic notation (§7.9.2, pp.39-41), examples (§7.9.3, pp.41+). PDF: `references/preskill_ch7.pdf`

---

## Preskill: Theorems and Formal Results (Chapter 7)

### Pauli Group $G_n$ **[Preskill, Ch.7, §7.9.1, pp.34-35]**
The $n$-qubit Pauli group (using the convention $Y = ZX$, real matrices) is (Eq. 7.116):
$$G_n = \pm\{I, X, Y, Z\}^{\otimes n}$$
of order $|G_n| = 2^{2n+1}$ (Eq. 7.116). Key properties [Preskill, Ch.7, p.35]:
1. Each $M \in G_n$ is unitary, $M^{-1} = M^\dagger$
2. $M^2 = \pm I$: $M^2 = I$ if number of $Y$'s is even; $M^2 = -I$ if odd
3. $M^2 = I \Rightarrow M$ is Hermitian; $M^2 = -I \Rightarrow M$ is anti-Hermitian
4. Any two elements either commute or anticommute: $MN = \pm NM$

### Stabilizer Code Definition **[Preskill, Ch.7, §7.9.1, pp.35-36]**
**Definition** (Eq. 7.117): Let $S$ be an abelian subgroup of $G_n$. The stabilizer code $\mathcal{H}_S$ is the simultaneous $+1$ eigenspace:
$$|\psi\rangle \in \mathcal{H}_S \iff M|\psi\rangle = |\psi\rangle \;\; \forall M \in S$$

### Code Dimension **[Preskill, Ch.7, §7.9.1, pp.35-37]**
**Theorem** [Preskill, Ch.7, pp.35-37]: If $S$ has $n-k$ independent generators, the code space has dimension $2^k$ (encodes $k$ logical qubits).

**Proof** [Preskill, Ch.7, pp.35-37]: Each stabilizer generator $M_i$ with $M_i^2 = I$ and $M_i \neq \pm I$ has equally many $+1$ and $-1$ eigenstates (since there exists $N \in G_n$ anticommuting with $M_i$, establishing a 1-1 correspondence). So $M_1 = +1$ selects $2^{n-1}$ states (Eq. 7.119). Adding $M_2$ (commuting with $M_1$, independent) halves the space again to $2^{n-2}$ (Eq. 7.120). After $n-k$ generators: dimension $= 2^n \cdot (1/2)^{n-k} = 2^k$.

### Error Correction with Stabilizers **[Preskill, Ch.7, §7.9.1, pp.37-38]**
The syndrome of error $E_a$ with respect to generator $M_i$ is (Eq. 7.123):
$$M_i E_a = (-1)^{s_{ia}} E_a M_i$$

**Error correction criterion** [Preskill, Ch.7, pp.37-38]: A stabilizer code corrects error set $\{E_a\}$ if for each pair $E_a, E_b \in \mathcal{E}$, one of:
1. $E_a^\dagger E_b \in S$ (degenerate errors), or
2. $\exists M \in S$ that anticommutes with $E_a^\dagger E_b$ (different syndromes)

**Proof** [Preskill, Ch.7, p.37] (Eq. 7.125): In case (2), for $|\psi\rangle \in \mathcal{H}_S$:
$$\langle\psi|E_a^\dagger E_b|\psi\rangle = \langle\psi|E_a^\dagger E_b M|\psi\rangle = -\langle\psi|ME_a^\dagger E_b|\psi\rangle = -\langle\psi|E_a^\dagger E_b|\psi\rangle$$
so $\langle\psi|E_a^\dagger E_b|\psi\rangle = 0$, satisfying Knill-Laflamme with $C_{ab} = 0$.

### Distance of Stabilizer Codes **[Preskill, Ch.7, §7.9.1, p.38]**
A stabilizer code has distance $d$ if each Pauli operator of weight $< d$ either lies in $S$ or anticommutes with some element of $S$. Nondegenerate if $S$ contains no elements of weight $< d$. A distance $d = 2t+1$ code corrects $t$ errors; distance $s+1$ detects $s$ errors.

### Normalizer (Centralizer) **[Preskill, Ch.7, §7.9.1, p.38]**
Recovery fails if $E_a^\dagger E_b$ commutes with all of $S$ but is not in $S$. Such operators lie in the **normalizer** $N(S) = S^\perp$ (the set of Pauli operators commuting with all of $S$) but not in $S$ itself. These are the **logical operators** that act nontrivially on the encoded qubits.

### Symplectic Notation **[Preskill, Ch.7, §7.9.2, pp.39-41]**
The quotient group $\bar{G}_n = G_n/\mathbb{Z}_2$ is isomorphic to the binary vector space $\mathbb{F}_2^{2n}$. A Pauli operator is represented as (Eq. 7.127):
$$(\alpha|\beta) \equiv Z(\alpha)X(\beta) = \bigotimes_{i=1}^n Z_i^{\alpha_i} \cdot \bigotimes_{i=1}^n X_i^{\beta_i}$$

**Multiplication** (Eq. 7.128): $(\alpha|\beta)(\alpha'|\beta') = (-1)^{\alpha'\cdot\beta}(\alpha+\alpha'|\beta+\beta')$

**Commutation** (Eq. 7.129): Two operators commute iff their **symplectic inner product** vanishes:
$$\alpha \cdot \beta' + \alpha' \cdot \beta = 0 \pmod{2}$$

**Squaring** (Eq. 7.131): $(\alpha|\beta)^2 = (-1)^{\alpha\cdot\beta}I$ (squares to $I$ iff even number of $Y$'s)

**Self-orthogonality** (Eq. 7.133): A closed subspace where each element squares to $I$ is automatically self-orthogonal (symplectic), hence the corresponding group is automatically abelian.

**Stabilizer matrix** (Eq. 7.134): The $n-k$ generators form an $(n-k) \times 2n$ matrix $H = (H_Z|H_X)$. The syndrome of error $E_a = (\alpha_a|\beta_a)$ is (Eq. 7.135):
$$s_{ia} = \alpha_a \cdot \beta'_i + \alpha'_i \cdot \beta_a$$

### Nine-Qubit Code (Shor Code) **[Preskill, Ch.7, §7.9.3(a), pp.41]**
The $[[9,1,3]]$ code has 8 stabilizer generators (Eq. 7.136):
$$Z_1Z_2, \; Z_2Z_3, \; Z_4Z_5, \; Z_5Z_6, \; Z_7Z_8, \; Z_8Z_9, \; X_1X_2X_3X_4X_5X_6, \; X_4X_5X_6X_7X_8X_9$$

Codewords (Eq. 7.1): $|\bar{0}\rangle = [\frac{1}{\sqrt{2}}(|000\rangle+|111\rangle)]^{\otimes 3}$, $|\bar{1}\rangle = [\frac{1}{\sqrt{2}}(|000\rangle-|111\rangle)]^{\otimes 3}$
- **[Steane tutorial]** Steane, A. M. Tutorial on QEC: CSS codes, Knill-Laflamme conditions, Steane syndrome extraction. PDF: `references/steane_qec_tutorial.pdf` (encrypted)
- **[Bacon intro]** Bacon, D. Introduction to QEC: symplectic representation, subsystem codes, Bacon-Shor code, quantum bounds. PDF: `references/bacon_intro_qec.pdf` (encrypted)
- Calderbank, A. R. & Shor, P. W. "Good quantum error-correcting codes exist." PRA 54, 1098 (1996).
- Roffe, J. "Quantum Error Correction: An Introductory Guide." Contemp. Phys. 60, 226 (2019).
