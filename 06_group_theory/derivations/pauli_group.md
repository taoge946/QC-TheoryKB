# Pauli Group Structure

> **Tags**: `pauli`, `group-theory`, `qec`
>
> **Primary Source**: D. Gottesman, *Stabilizer Codes and Quantum Error Correction*, PhD thesis, Caltech (1997), Ch.3 **[Gottesman 1997, Ch.3, §3.1--3.2]**

## Statement

$n$量子比特Pauli群 $\mathcal{P}_n$ 是量子纠错理论的核心代数结构 **[Gottesman 1997, Ch.3, §3.1]**。本文从单量子比特Pauli矩阵出发，推导其完整群结构、乘法规则、中心、商群等性质。

$$
\mathcal{P}_n = \{ \alpha \, \sigma_1 \otimes \sigma_2 \otimes \cdots \otimes \sigma_n \mid \alpha \in \{\pm 1, \pm i\}, \; \sigma_k \in \{I, X, Y, Z\} \}
$$

## Prerequisites

- 基本群论：群的定义、子群、中心
- 矩阵乘法与张量积
- 量子力学基本符号

---

## Derivation

### Step 1: Single-Qubit Pauli Matrices **[Gottesman 1997, Ch.1, §1.2]**

定义四个$2\times 2$矩阵：

$$
I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

物理意义：
- $X$：比特翻转 (bit flip)，$X|0\rangle = |1\rangle$，$X|1\rangle = |0\rangle$
- $Z$：相位翻转 (phase flip)，$Z|0\rangle = |0\rangle$，$Z|1\rangle = -|1\rangle$
- $Y = iXZ$：同时比特和相位翻转

### Step 2: Fundamental Properties

**性质1: Hermitian性（自伴）**

$$
X^\dagger = X, \quad Y^\dagger = Y, \quad Z^\dagger = Z
$$

验证 $Y$：$(Y^\dagger)_{ij} = \overline{Y_{ji}}$，

$$
Y^\dagger = \begin{pmatrix} 0 & \overline{i} \\ \overline{-i} & 0 \end{pmatrix} = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = Y \quad \checkmark
$$

**性质2: 酉性**

$$
XX^\dagger = X^2 = I, \quad YY^\dagger = Y^2 = I, \quad ZZ^\dagger = Z^2 = I
$$

直接计算 $X^2$：

$$
X^2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark
$$

因此每个Pauli矩阵既Hermitian又酉，即 $P^\dagger = P$ 且 $P^{-1} = P^\dagger = P$。

**性质3: 特征值**

Hermitian + 酉 $\Rightarrow$ 特征值满足 $\lambda = \bar{\lambda}$（实数）且 $|\lambda| = 1$，因此 $\lambda \in \{+1, -1\}$。

具体地：
- $X$ 的特征值 $\pm 1$，特征向量 $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$，$|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$
- $Z$ 的特征值 $\pm 1$，特征向量 $|0\rangle$，$|1\rangle$
- $Y$ 的特征值 $\pm 1$，特征向量 $|+i\rangle = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$，$|-i\rangle = \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$

**性质4: Traceless**

$$
\text{tr}(X) = 0 + 0 = 0, \quad \text{tr}(Y) = 0 + 0 = 0, \quad \text{tr}(Z) = 1 + (-1) = 0
$$

**性质5: 正交完备性**

$$
\text{tr}(\sigma_j^\dagger \sigma_k) = 2\delta_{jk}, \quad j, k \in \{0, 1, 2, 3\}
$$

其中 $\sigma_0 = I, \sigma_1 = X, \sigma_2 = Y, \sigma_3 = Z$。这意味着 $\{I, X, Y, Z\}$ 构成 $2\times 2$ 矩阵空间的正交基。

### Step 3: Multiplication Table **[Gottesman 1997, Ch.3, §3.1]**

通过直接矩阵乘法计算完整乘法表：

$$
XY = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} = iZ
$$

$$
YX = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = -iZ
$$

类似地计算所有乘积：

| $\times$ | $I$ | $X$ | $Y$ | $Z$ |
|----------|-----|-----|-----|-----|
| $I$ | $I$ | $X$ | $Y$ | $Z$ |
| $X$ | $X$ | $I$ | $iZ$ | $-iY$ |
| $Y$ | $Y$ | $-iZ$ | $I$ | $iX$ |
| $Z$ | $Z$ | $iY$ | $-iX$ | $I$ |

**统一公式**：

$$
\sigma_j \sigma_k = \delta_{jk} I + i \sum_l \epsilon_{jkl} \sigma_l
$$

其中 $\epsilon_{jkl}$ 是Levi-Civita符号（$\epsilon_{123} = 1$，奇排列为$-1$，其余为$0$）。

### Step 4: Commutation and Anti-commutation Relations

从乘法表立即得到：

**对易关系**（commutators）：

$$
[\sigma_j, \sigma_k] = \sigma_j \sigma_k - \sigma_k \sigma_j = 2i \sum_l \epsilon_{jkl} \sigma_l
$$

具体地：

$$
[X, Y] = XY - YX = iZ - (-iZ) = 2iZ
$$

$$
[Y, Z] = YZ - ZY = iX - (-iX) = 2iX
$$

$$
[Z, X] = ZX - XZ = iY - (-iY) = 2iY
$$

**反对易关系**（anti-commutators）：

$$
\{\sigma_j, \sigma_k\} = \sigma_j \sigma_k + \sigma_k \sigma_j = 2\delta_{jk} I
$$

即不同Pauli矩阵严格反对易：

$$
\{X, Y\} = XY + YX = iZ + (-iZ) = 0
$$

$$
\{Y, Z\} = 0, \quad \{Z, X\} = 0
$$

关键结论：**不同的Pauli矩阵反对易，相同的Pauli矩阵对易**。

### Step 5: The Single-Qubit Pauli Group $\mathcal{P}_1$ **[Gottesman 1997, Ch.3, §3.1]**

乘法表中出现了因子 $\pm 1, \pm i$。为了使集合对乘法封闭，必须包含这些相位因子。

定义单量子比特Pauli群 **[Gottesman 1997, Ch.3, §3.1]**：

$$
\mathcal{P}_1 = \{ \pm I, \pm iI, \pm X, \pm iX, \pm Y, \pm iY, \pm Z, \pm iZ \}
$$

**验证群公理**：

1. **封闭性**：从乘法表可见，任意两个元素之积仍在集合中。例如 $(iX)(iY) = i^2 XY = -iZ \in \mathcal{P}_1$。

2. **结合律**：矩阵乘法天然满足结合律。

3. **单位元**：$I \in \mathcal{P}_1$。

4. **逆元**：对任意 $\alpha P \in \mathcal{P}_1$，其逆为 $\alpha^{-1} P$（因为 $P^2 = I$）。
   - $(\pm P)^{-1} = \pm P$
   - $(\pm iP)^{-1} = \mp iP$

**群阶**：$|\mathcal{P}_1| = 4 \times 4 = 16$。（4个相位 $\times$ 4个Pauli矩阵）

### Step 6: Tensor Product Structure

对于两个量子比特，Pauli算符的张量积定义为：

$$
(\alpha P) \otimes (\beta Q) = \alpha\beta (P \otimes Q)
$$

其中 $P \otimes Q$ 作用在 $\mathbb{C}^2 \otimes \mathbb{C}^2 = \mathbb{C}^4$ 上：

$$
(P \otimes Q)(|a\rangle \otimes |b\rangle) = P|a\rangle \otimes Q|b\rangle
$$

关键乘法规则：

$$
(P_1 \otimes P_2)(Q_1 \otimes Q_2) = (P_1 Q_1) \otimes (P_2 Q_2)
$$

这意味着张量积逐位相乘。

例如：

$$
(X \otimes Z)(Y \otimes X) = (XY) \otimes (ZX) = (iZ) \otimes (iY) = -Z \otimes Y
$$

### Step 7: The $n$-Qubit Pauli Group $\mathcal{P}_n$

推广到 $n$ 量子比特：

$$
\mathcal{P}_n = \{ \alpha \, \sigma_1 \otimes \sigma_2 \otimes \cdots \otimes \sigma_n \mid \alpha \in \{\pm 1, \pm i\}, \; \sigma_k \in \{I, X, Y, Z\} \}
$$

**乘法规则**：

$$
(\alpha \, P_1 \otimes \cdots \otimes P_n)(\beta \, Q_1 \otimes \cdots \otimes Q_n) = \alpha\beta \prod_{k=1}^n c_k \, (R_1 \otimes \cdots \otimes R_n)
$$

其中 $P_k Q_k = c_k R_k$，$c_k \in \{\pm 1, \pm i\}$，$R_k \in \{I, X, Y, Z\}$。

**对易性判断**：两个$n$-qubit Pauli算符 $P = P_1 \otimes \cdots \otimes P_n$ 和 $Q = Q_1 \otimes \cdots \otimes Q_n$ 的对易性为：

$$
PQ = (-1)^{s(P,Q)} QP
$$

其中

$$
s(P, Q) = \#\{k \mid P_k \neq I, \, Q_k \neq I, \, P_k \neq Q_k\} \pmod{2}
$$

即：统计两个算符在同一位上"不同且都非$I$"的位数。偶数个则对易，奇数个则反对易。

推导：在每一位上，$P_k$ 和 $Q_k$ 的对易性为：
- $P_k = I$ 或 $Q_k = I$：对易（贡献因子 $+1$）
- $P_k = Q_k \neq I$：$P_k^2 = I$，对易（贡献因子 $+1$）
- $P_k \neq Q_k$，两者都不是$I$：反对易（贡献因子 $-1$）

总对易因子为各位贡献之积，即 $(-1)^{s(P,Q)}$。

### Step 8: Group Order

$$
|\mathcal{P}_n| = 4 \times 4^n = 4^{n+1}
$$

- 相位因子：4种（$\pm 1, \pm i$）
- 每一位上的Pauli矩阵选择：4种（$I, X, Y, Z$）
- $n$位的选择：$4^n$种

### Step 9: Center of the Pauli Group

群的中心 $Z(\mathcal{P}_n)$ 是与所有元素都对易的元素集合：

$$
Z(\mathcal{P}_n) = \{ g \in \mathcal{P}_n \mid gp = pg, \; \forall p \in \mathcal{P}_n \}
$$

**Claim**: $Z(\mathcal{P}_n) = \{\pm I^{\otimes n}, \pm i I^{\otimes n}\} = \{\pm 1, \pm i\} \cdot I^{\otimes n}$

**Proof**:

($\supseteq$) 显然 $\alpha I^{\otimes n}$ 与所有Pauli算符对易，因为 $I$ 与一切矩阵对易。

($\subseteq$) 设 $g = \alpha \, P_1 \otimes \cdots \otimes P_n \in Z(\mathcal{P}_n)$。对任意位$k$，考虑仅在第$k$位放$X$、其余放$I$的Pauli算符 $Q^{(k)}$。要使 $g$ 与 $Q^{(k)}$ 对易，需要 $P_k$ 与 $X$ 对易。同理需与 $Z$ 对易。

在第$k$位上，$P_k$ 必须同时与 $X$ 和 $Z$ 对易。
- $I$ 与一切对易 $\checkmark$
- $X$ 与 $Z$ 反对易 $\times$
- $Y$ 与 $X$ 反对易 $\times$
- $Z$ 与 $X$ 反对易 $\times$

因此 $P_k = I$ 对所有 $k$，得 $g = \alpha I^{\otimes n}$。

所以 $|Z(\mathcal{P}_n)| = 4$。

### Step 10: Quotient Group $\mathcal{P}_n / Z(\mathcal{P}_n)$

商群消除了相位信息：

$$
\bar{\mathcal{P}}_n = \mathcal{P}_n / Z(\mathcal{P}_n)
$$

$$
|\bar{\mathcal{P}}_n| = \frac{|\mathcal{P}_n|}{|Z(\mathcal{P}_n)|} = \frac{4^{n+1}}{4} = 4^n
$$

$\bar{\mathcal{P}}_n$ 中的元素可以用不含相位的Pauli string表示：

$$
\bar{\mathcal{P}}_n = \{ \sigma_1 \otimes \cdots \otimes \sigma_n \mid \sigma_k \in \{I, X, Y, Z\} \}
$$

这是一个阶为 $4^n$ 的阿贝尔群（Abel群），同构于 $\mathbb{Z}_2^{2n}$：

$$
\bar{\mathcal{P}}_n \cong \mathbb{Z}_2^{2n}
$$

同构映射就是辛表示：每一位的 $\{I, X, Y, Z\}$ 映射到 $\{(0,0), (1,0), (1,1), (0,1)\} \in \mathbb{F}_2^2$。

注意：$\mathcal{P}_n$ 本身不是阿贝尔群（因为存在反对易的元素），但商群 $\bar{\mathcal{P}}_n$ 是阿贝尔群。

### Step 11: $\mathcal{P}_n$ 的群结构

$\mathcal{P}_n$ 可以写成中心扩张（central extension）：

$$
1 \to Z(\mathcal{P}_n) \to \mathcal{P}_n \to \bar{\mathcal{P}}_n \to 1
$$

即短正合列：

$$
1 \to \mathbb{Z}_4 \to \mathcal{P}_n \to \mathbb{Z}_2^{2n} \to 1
$$

这个扩张不是直积（因为 $\mathcal{P}_n$ 非阿贝尔），而是由辛内积决定的2-cocycle定义的非平凡扩张。

---

## Gottesman Thesis: Pauli Group Properties

### Definition and Structure from Thesis

> **[Gottesman thesis, §1.2]**: A nice set of operators to consider for a single qubit is the set of Pauli spin matrices:
> $$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\; \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\; \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

> **[Gottesman thesis, §2.3]**: The set of all tensor products of $\sigma_x$, $\sigma_y$, $\sigma_z$, and $I$ with a possible overall factor of $-1$ or $\pm i$ forms a group $\mathcal{G}$ under multiplication. $\mathcal{G}_1$ is just the quaternionic group; $\mathcal{G}_n$ is the direct product of $n$ copies of the quaternions modulo all but a global phase factor.

### Key Algebraic Properties

> **[Gottesman thesis, §3.2]**: Since $\sigma_x^2 = \sigma_y^2 = \sigma_z^2 = +1$, every element in $\mathcal{G}$ squares to $\pm 1$. Also, $\sigma_x$, $\sigma_y$, and $\sigma_z$ on the same qubit anticommute, while they commute on different qubits. Therefore, any two elements of $\mathcal{G}$ either commute or they anticommute.

> **[Gottesman thesis, §3.2]**: Elements of $\mathcal{G}$ can be either Hermitian or anti-Hermitian. In either case, if $A \in \mathcal{G}$, $A^\dagger \in \mathcal{G}$ also. Similarly, $\sigma_x$, $\sigma_y$, and $\sigma_z$ are all unitary, so every element of $\mathcal{G}$ is unitary.

### Error Basis Property

> **[Gottesman thesis, §2.2]**: The most general one-qubit error that can occur is some $2 \times 2$ matrix; but such a matrix can always be written as the (complex) linear combination of $\sigma_x$, $\sigma_y$, $\sigma_z$, and the identity $I$. When the error correction process measures which error has occurred, the state collapses to one of the basis errors $\sigma_x$, $\sigma_y$, $\sigma_z$, or $I$, each with a corresponding probability.

### Nice Error Bases (Generalization to Qudits)

> **[Gottesman thesis, §3.6]**: Knill has codified the properties necessary for the stabilizer construction to generalize to $d$-dimensional spaces. Suppose we have a set of $d^2$ unitary operators $E_1, \ldots, E_{d^2}$ (including the identity) acting on a single qudit such that the $E_i$'s form a basis for all possible $d \times d$ complex matrices. If $E_i E_j = w_{ij} E_{i*j}$ for all $i, j$ (where $*$ is some binary group operation), then the $E_i$'s are said to form a nice error basis.

> **[Gottesman thesis, §3.6]**: One particularly convenient error basis for any $d$ is generated by $D_\omega$ and $C_n$, where $(D_\omega)_{ij} = \delta_{ij}\omega^i$ and $(C_n)_{ij} = \delta_{j,(i+1 \bmod n)}$. For $d = 2$, this reduces to the usual Pauli basis ($C_2 = X$, $D_{-1} = Z$). These satisfy:
> $$C_n D_\omega = \omega D_\omega C_n$$

---

## Key Insight

**为什么Pauli群是量子纠错的基础？**

1. **错误分解**：任意单量子比特错误 $E$ 可以展开为Pauli基：$E = c_0 I + c_1 X + c_2 Y + c_3 Z$。因此只需纠正Pauli错误就够了。

2. **离散化**：虽然量子错误是连续的（任意酉算符），但量子纠错码只需对付离散的Pauli错误集合——这是量子纠错的"离散化"奇迹。

3. **Stabilizer formalism**：Pauli群的阿贝尔子群定义了stabilizer码。$[[n,k,d]]$码的stabilizer群 $\mathcal{S}$ 是 $\mathcal{P}_n$ 的一个阶为 $2^{n-k}$ 的阿贝尔子群（不含$-I$），码空间是 $\mathcal{S}$ 的公共$+1$特征空间。

4. **辛结构**：商群 $\bar{\mathcal{P}}_n \cong \mathbb{F}_2^{2n}$ 上的辛内积完美编码了对易关系，使得量子码理论可以用$\text{GF}(2)$线性代数高效处理。

---

## Summary

| 性质 | 表达式 |
|------|--------|
| 群阶 | $\|\mathcal{P}_n\| = 4^{n+1}$ |
| 中心 | $Z(\mathcal{P}_n) = \{\pm 1, \pm i\} \cdot I^{\otimes n}$ |
| 中心阶 | $\|Z(\mathcal{P}_n)\| = 4$ |
| 商群 | $\bar{\mathcal{P}}_n \cong \mathbb{Z}_2^{2n}$ |
| 对易性 | $PQ = (-1)^{s(P,Q)} QP$ |
| 每个元素阶 | 整除4 |
