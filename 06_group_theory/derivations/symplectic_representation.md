# Symplectic Representation of Stabilizer Codes

> **Tags**: `symplectic`, `binary`, `gf2`, `stabilizer`, `group-theory`
>
> **Primary Source**: D. Gottesman, *Stabilizer Codes and Quantum Error Correction*, PhD thesis, Caltech (1997), Ch.3, §3.4 **[Gottesman 1997, Ch.3, §3.4]**

## Statement

二元辛表示（binary symplectic representation）将$n$量子比特Pauli算符（忽略相位）映射为 $\mathbb{F}_2^{2n}$ 上的二元向量 **[Gottesman 1997, Ch.3, §3.4]**。在此表示下，Pauli算符的对易性由辛内积判定，stabilizer群对应各向同性子空间，量子纠错问题转化为 $\text{GF}(2)$ 上的线性代数问题。

$$
i^c \, X^{a_1}Z^{b_1} \otimes \cdots \otimes X^{a_n}Z^{b_n} \;\longleftrightarrow\; (\mathbf{a} \mid \mathbf{b}) \in \mathbb{F}_2^{2n}
$$

## Prerequisites

- Pauli群 $\mathcal{P}_n$ → [pauli_group.md]
- 线性代数基础（向量空间、内积、零空间）
- $\text{GF}(2)$（二元域）上的线性代数

---

## Derivation

### Step 1: Binary Encoding of Single-Qubit Paulis

每个单量子比特Pauli矩阵可以写成 $X^a Z^b$ 的形式（忽略相位 $\pm 1, \pm i$）：

$$
I = X^0 Z^0, \quad X = X^1 Z^0, \quad Z = X^0 Z^1, \quad Y = iX^1 Z^1
$$

因此用二元对 $(a, b) \in \mathbb{F}_2^2$ 编码：

| Pauli | $X^a Z^b$ | $(a \mid b)$ |
|-------|-----------|---------------|
| $I$ | $X^0 Z^0$ | $(0 \mid 0)$ |
| $X$ | $X^1 Z^0$ | $(1 \mid 0)$ |
| $Z$ | $X^0 Z^1$ | $(0 \mid 1)$ |
| $Y$ | $X^1 Z^1$ (up to phase) | $(1 \mid 1)$ |

**注意**：$Y = iXZ$，所以 $X^1Z^1 = XZ = -iY$。辛表示忽略了相位因子，只保留$X$和$Z$的指数。

### Step 2: $n$-Qubit Pauli to Binary Vector **[Gottesman 1997, Ch.3, §3.4]**

$n$量子比特Pauli算符：

$$
P = i^c \, X^{a_1}Z^{b_1} \otimes X^{a_2}Z^{b_2} \otimes \cdots \otimes X^{a_n}Z^{b_n}
$$

映射为 $2n$ 位二元向量：

$$
P \;\longleftrightarrow\; v_P = (a_1, a_2, \ldots, a_n \mid b_1, b_2, \ldots, b_n) = (\mathbf{a} \mid \mathbf{b}) \in \mathbb{F}_2^{2n}
$$

前$n$位编码$X$分量，后$n$位编码$Z$分量。

**例子**（$n = 5$）：

$$
X \otimes I \otimes Z \otimes Y \otimes Z \;\longleftrightarrow\; (1, 0, 0, 1, 0 \mid 0, 0, 1, 1, 1)
$$

验证：
- 第1位：$X = X^1Z^0$，得 $(a_1, b_1) = (1, 0)$
- 第2位：$I = X^0Z^0$，得 $(a_2, b_2) = (0, 0)$
- 第3位：$Z = X^0Z^1$，得 $(a_3, b_3) = (0, 1)$
- 第4位：$Y \sim X^1Z^1$，得 $(a_4, b_4) = (1, 1)$
- 第5位：$Z = X^0Z^1$，得 $(a_5, b_5) = (0, 1)$

### Step 3: Group Multiplication Becomes Vector Addition

忽略相位后，两个Pauli算符的乘积对应二元向量的加法：

$$
v_{PQ} = v_P + v_Q \pmod{2}
$$

**推导**：设 $P = X^{a_1}Z^{b_1} \otimes \cdots$ 和 $Q = X^{a'_1}Z^{b'_1} \otimes \cdots$。在第$k$位上：

$$
(X^{a_k}Z^{b_k})(X^{a'_k}Z^{b'_k}) = (\text{phase}) \cdot X^{a_k + a'_k}Z^{b_k + b'_k}
$$

其中指数的加法在 $\mathbb{F}_2$ 中进行（即 $\bmod 2$）。忽略相位后得到逐位的 $\mathbb{F}_2$ 加法。

因此，商群 $\bar{\mathcal{P}}_n = \mathcal{P}_n / Z(\mathcal{P}_n)$ 同构于加法群 $(\mathbb{F}_2^{2n}, +)$：

$$
\bar{\mathcal{P}}_n \cong (\mathbb{F}_2^{2n}, +) \cong \mathbb{Z}_2^{2n}
$$

### Step 4: Symplectic Inner Product **[Gottesman 1997, Ch.3, §3.4]**

定义辛内积（symplectic inner product）：

$$
\langle v, w \rangle_s = \langle (\mathbf{a} \mid \mathbf{b}), (\mathbf{a}' \mid \mathbf{b}') \rangle_s = \mathbf{a} \cdot \mathbf{b}' + \mathbf{a}' \cdot \mathbf{b} \pmod{2}
$$

$$
= \sum_{k=1}^n (a_k b'_k + a'_k b_k) \pmod{2}
$$

用矩阵形式写：

$$
\langle v, w \rangle_s = v^T \Omega w \pmod{2}, \quad \text{where} \quad \Omega = \begin{pmatrix} 0_n & I_n \\ I_n & 0_n \end{pmatrix}
$$

$\Omega$ 是 $2n \times 2n$ 辛形式矩阵。

**辛内积的性质**（所有运算在 $\mathbb{F}_2$ 中）：

1. **双线性性**：$\langle u + v, w \rangle_s = \langle u, w \rangle_s + \langle v, w \rangle_s$
2. **反对称性**：$\langle v, w \rangle_s = \langle w, v \rangle_s$（在 $\mathbb{F}_2$ 中，$-1 = 1$，所以反对称等于对称）
3. **非退化性**：若 $\langle v, w \rangle_s = 0$ 对所有 $w$，则 $v = 0$
4. **各向同性**：$\langle v, v \rangle_s = 2\sum_k a_k b_k = 0 \pmod{2}$（在 $\mathbb{F}_2$ 中恒为零）

### Step 5: Commutativity Criterion — The Central Theorem

**定理**：两个 $n$-qubit Pauli算符 $P, Q$（忽略相位后为 $v_P, v_Q$）的对易性完全由辛内积决定：

$$
\boxed{PQ = (-1)^{\langle v_P, v_Q \rangle_s} QP}
$$

因此：

$$
[P, Q] = 0 \iff \langle v_P, v_Q \rangle_s = 0
$$

**完整推导**：

考虑第$k$位上的贡献。设 $P$ 在第$k$位为 $X^{a_k}Z^{b_k}$，$Q$ 在第$k$位为 $X^{a'_k}Z^{b'_k}$。

利用 $ZX = -XZ$（反对易关系），我们需要将 $P_k Q_k$ 变换为 $Q_k P_k$ 时产生的符号。

$$
P_k Q_k = X^{a_k}Z^{b_k} \cdot X^{a'_k}Z^{b'_k}
$$

要把这重排为 $Q_k P_k = X^{a'_k}Z^{b'_k} \cdot X^{a_k}Z^{b_k}$，需要交换 $Z^{b_k}$ 和 $X^{a'_k}$。每次交换 $Z$ 和 $X$ 产生一个 $-1$ 因子（因为 $ZX = -XZ$），所以：

$$
P_k Q_k = (-1)^{a'_k b_k} X^{a_k} X^{a'_k} Z^{b_k} Z^{b'_k}
$$

而

$$
Q_k P_k = (-1)^{a_k b'_k} X^{a'_k} X^{a_k} Z^{b'_k} Z^{b_k}
$$

由于 $X^{a_k}X^{a'_k} = X^{a'_k}X^{a_k}$ 且 $Z^{b_k}Z^{b'_k} = Z^{b'_k}Z^{b_k}$（同种Pauli对易），所以

$$
P_k Q_k = (-1)^{a'_k b_k - a_k b'_k} Q_k P_k = (-1)^{a_k b'_k + a'_k b_k} Q_k P_k
$$

（最后一步用了 $\mathbb{F}_2$ 中 $-1 = 1$。）

$n$-qubit的情况下，取各位贡献之积：

$$
PQ = \prod_{k=1}^n (-1)^{a_k b'_k + a'_k b_k} \cdot QP = (-1)^{\sum_k(a_k b'_k + a'_k b_k)} QP = (-1)^{\langle v_P, v_Q \rangle_s} QP
$$

$\blacksquare$

### Step 6: Stabilizer Group as Isotropic Subspace

**定义**：$[[n, k, d]]$ stabilizer码的stabilizer群 $\mathcal{S}$ 是 $\mathcal{P}_n$ 的一个阿贝尔子群，满足 $-I \notin \mathcal{S}$，且 $|\mathcal{S}| = 2^{n-k}$。

**辛表示中的条件**：

1. **阿贝尔（所有元素两两对易）** $\iff$ 对应向量集 $V_\mathcal{S} \subset \mathbb{F}_2^{2n}$ 满足：

$$
\langle v, w \rangle_s = 0, \quad \forall v, w \in V_\mathcal{S}
$$

即 $V_\mathcal{S}$ 是辛空间中的**各向同性子空间**（isotropic subspace）。

2. **$-I \notin \mathcal{S}$** 的条件在辛表示中自动满足（因为 $-I$ 的辛向量是零向量 $(0\mid 0)$，属于任何子空间，但相位 $-1$ 需要额外追踪——辛表示忽略了相位）。

3. **维数**：$V_\mathcal{S}$ 是 $\mathbb{F}_2^{2n}$ 的一个 $(n-k)$ 维子空间。

**Stabilizer群的辛矩阵表示**：选择 $\mathcal{S}$ 的 $n-k$ 个独立生成元 $g_1, \ldots, g_{n-k}$，对应辛向量 $v_1, \ldots, v_{n-k}$，排成 $(n-k) \times 2n$ 矩阵：

$$
H_{\text{stab}} = \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_{n-k} \end{pmatrix} = \begin{pmatrix} \mathbf{a}_1 \mid \mathbf{b}_1 \\ \mathbf{a}_2 \mid \mathbf{b}_2 \\ \vdots \\ \mathbf{a}_{n-k} \mid \mathbf{b}_{n-k} \end{pmatrix} \in \mathbb{F}_2^{(n-k) \times 2n}
$$

各向同性条件写为：

$$
H_{\text{stab}} \, \Omega \, H_{\text{stab}}^T = 0 \pmod{2}
$$

### Gottesman Thesis: Binary Vector Space Formalism

> **[Gottesman thesis, §3.4]**: We can write the stabilizer using binary vector spaces, which emphasizes connections with the classical theory of error-correcting codes. We write the stabilizer as a pair of $(n-k) \times n$ binary matrices (or often one $(n-k) \times 2n$ matrix with a line separating the two halves). The rows correspond to the different generators of the stabilizer and the columns correspond to different qubits. One matrix has a $1$ whenever the generator has a $X$ or a $Y$ in the appropriate place, the other has a $1$ whenever the generator has a $Y$ or $Z$.

> **[Gottesman thesis, §3.4, Eq. 3.6]**: In the binary formalism, the condition that two operators commute with each other becomes:
> $$Q(a|b, c|d) = \sum_{i=1}^n (a_i d_i + b_i c_i) = 0$$
> using binary arithmetic. Therefore the condition that the stabilizer be Abelian converts to the condition that the stabilizer matrix $(A|B)$ satisfy:
> $$\sum_{l=1}^n (A_{il}B_{jl} + B_{il}A_{jl}) = 0$$

> **[Gottesman thesis, §3.4]**: To get a real code (with an even number of $Y$'s), the code should also satisfy:
> $$\sum_{l=1}^n A_{il}B_{il} = 0$$

### Standard Form for Stabilizer Codes

> **[Gottesman thesis, §4.1, Eq. 4.5]**: Any stabilizer code can be put into the standard form:
> $$\begin{pmatrix} I_r & A_1 & A_2 & B & C_1 & C_2 \\ 0 & 0 & 0 & D & I_{n-k-r} & E \end{pmatrix}$$
> where $r$ is the rank of the $X$ portion of the stabilizer generator matrix. The $\bar{X}$ and $\bar{Z}$ operators can be chosen in standard form as well, with $\bar{X}$ having $U_3 = I_k$ and $\bar{Z}$ having $V_3' = I_k$.

### GF(4) Formalism

> **[Gottesman thesis, §3.4]**: Another formalism highlights connections with the classical theory of codes over the field GF(4). This field contains four elements $\{0, 1, \omega, \omega^2\}$ with $\omega^3 = 1$ and $1 + \omega = \omega^2$. We rewrite the generators as an $n$-dimensional vector over GF(4) by substituting $1$ for $X$, $\omega$ for $Z$, and $\omega^2$ for $Y$. If the stabilizer is closed under multiplication by $\omega$, the code is a linear code (essentially a classical code over GF(4)). The most general quantum code is sometimes called an additive code.

> **[Gottesman thesis, §3.4]**: Two operators in $\mathcal{G}$ commute iff their images, the vectors $u$ and $v$ over GF(4), satisfy:
> $$\text{Tr}\; u \cdot \bar{v} = \text{Tr}\left(\sum_{j=1}^n u_j \bar{v}_j\right) = 0$$
> where $\bar{v}_j$ is conjugation on the $j$th component, switching $\omega$ and $\omega^2$.

### Step 7: CSS Codes in the Symplectic Picture

**CSS码**（Calderbank-Shor-Steane码）是stabilizer码的特殊子类，其stabilizer生成元分为纯$X$型和纯$Z$型：

$$
H_{\text{stab}} = \begin{pmatrix} H_X & 0 \\ 0 & H_Z \end{pmatrix}
$$

其中 $H_X \in \mathbb{F}_2^{r_X \times n}$（$X$型生成元）和 $H_Z \in \mathbb{F}_2^{r_Z \times n}$（$Z$型生成元），$r_X + r_Z = n - k$。

**各向同性条件简化**：

$$
H_{\text{stab}} \, \Omega \, H_{\text{stab}}^T = \begin{pmatrix} H_X & 0 \\ 0 & H_Z \end{pmatrix} \begin{pmatrix} 0 & I \\ I & 0 \end{pmatrix} \begin{pmatrix} H_X^T & 0 \\ 0 & H_Z^T \end{pmatrix} = \begin{pmatrix} 0 & H_X H_Z^T \\ H_Z H_X^T & 0 \end{pmatrix} = 0
$$

因此CSS码的条件为：

$$
\boxed{H_X H_Z^T = 0 \pmod{2}}
$$

即：$H_X$ 的每一行与 $H_Z$ 的每一行正交（在 $\mathbb{F}_2$ 中）。等价地，$H_Z$ 的行空间包含在 $H_X$ 的零空间（dual space）中：

$$
\text{rowspace}(H_Z) \subseteq \ker(H_X) = C_X^\perp
$$

其中 $C_X$ 是以 $H_X$ 为校验矩阵的经典码。

**CSS码的经典码解释**：CSS码 $\text{CSS}(C_1, C_2)$ 由两个经典码构成：
- $C_1$：以 $H_X$ 为校验矩阵（纠正$Z$错误）
- $C_2$：以 $H_Z$ 为校验矩阵（纠正$X$错误）
- 约束：$C_2^\perp \subseteq C_1$（等价于 $H_X H_Z^T = 0$）

### Step 8: Normalizer and Logical Operators

stabilizer码的逻辑算符来自 $\mathcal{S}$ 在 $\mathcal{P}_n$ 中的normalizer：

$$
N(\mathcal{S}) = \{ P \in \mathcal{P}_n \mid PgP^\dagger \in \mathcal{S}, \; \forall g \in \mathcal{S} \}
$$

由于 $\mathcal{S}$ 是阿贝尔群，$PgP^\dagger = \pm g$（Pauli算符要么对易要么反对易）。要使 $PgP^\dagger \in \mathcal{S}$，需要 $P$ 与 $\mathcal{S}$ 的所有元素对易：

$$
N(\mathcal{S}) = C_{\mathcal{P}_n}(\mathcal{S}) = \{ P \in \mathcal{P}_n \mid [P, g] = 0, \; \forall g \in \mathcal{S} \}
$$

（对Pauli群，normalizer等于centralizer。）

**辛表示**：$N(\mathcal{S})$ 对应 $V_\mathcal{S}$ 的**辛补**（symplectic complement）：

$$
V_{N(\mathcal{S})} = V_\mathcal{S}^{\perp_s} = \{ w \in \mathbb{F}_2^{2n} \mid \langle v, w \rangle_s = 0, \; \forall v \in V_\mathcal{S} \}
$$

由于 $V_\mathcal{S}$ 是 $(n-k)$ 维的各向同性子空间：

$$
\dim(V_\mathcal{S}^{\perp_s}) = 2n - (n-k) = n+k
$$

因为 $V_\mathcal{S} \subseteq V_\mathcal{S}^{\perp_s}$（各向同性条件），逻辑算符的空间为商空间：

$$
V_{\text{logical}} = V_\mathcal{S}^{\perp_s} / V_\mathcal{S}
$$

$$
\dim(V_{\text{logical}}) = (n+k) - (n-k) = 2k
$$

这 $2k$ 维空间对应 $k$ 个逻辑量子比特的 $k$ 对逻辑 $\bar{X}_i, \bar{Z}_i$ 算符。

**逻辑算符的选取**：选 $2k$ 个向量 $\bar{x}_1, \bar{z}_1, \ldots, \bar{x}_k, \bar{z}_k \in V_\mathcal{S}^{\perp_s} \setminus V_\mathcal{S}$，满足：

$$
\langle \bar{x}_i, \bar{z}_j \rangle_s = \delta_{ij}, \quad \langle \bar{x}_i, \bar{x}_j \rangle_s = 0, \quad \langle \bar{z}_i, \bar{z}_j \rangle_s = 0
$$

即逻辑算符之间满足与物理Pauli相同的辛关系。

### Step 9: Complete Symplectic Structure

对 $[[n, k, d]]$ 码，$\mathbb{F}_2^{2n}$ 分解为：

$$
\mathbb{F}_2^{2n} = V_\mathcal{S} \oplus V_{\text{logical}} \oplus V_{\text{gauge}}
$$

（严格来说这不是直和分解，而是选取代表元后的分层。）

更精确地，可以选一组辛基：

$$
\{s_1, \ldots, s_{n-k}, \; \bar{x}_1, \bar{z}_1, \ldots, \bar{x}_k, \bar{z}_k, \; t_1, \ldots, t_{n-k}\}
$$

其中：
- $s_1, \ldots, s_{n-k}$：stabilizer生成元
- $\bar{x}_i, \bar{z}_i$：逻辑算符对
- $t_1, \ldots, t_{n-k}$：$s_i$ 的辛伙伴（$\langle s_i, t_j \rangle_s = \delta_{ij}$），即"pure error"算符

这构成了 $\mathbb{F}_2^{2n}$ 的一组辛基，辛内积矩阵为标准形式。

### Step 10: Syndrome Computation

对于错误 $E$ 对应辛向量 $v_E$，其syndrome向量为：

$$
\text{syn}(E) = H_{\text{stab}} \, \Omega \, v_E^T \in \mathbb{F}_2^{n-k}
$$

第$i$个分量：

$$
\text{syn}(E)_i = \langle v_{g_i}, v_E \rangle_s = \begin{cases} 0 & \text{if } [g_i, E] = 0 \\ 1 & \text{if } \{g_i, E\} = 0 \end{cases}
$$

syndrome为零的错误恰好是 $N(\mathcal{S})$ 中的元素，即stabilizer或逻辑算符。这就是为什么码距的定义是：

$$
d = \min \{ \text{wt}(P) \mid P \in N(\mathcal{S}) \setminus \mathcal{S} \}
$$

即最小权重逻辑算符的权重。

### Step 11: Example — $[[5,1,3]]$ Code

$[[5,1,3]]$五量子比特码的stabilizer生成元：

$$
g_1 = XZZXI, \quad g_2 = IXZZX, \quad g_3 = XIXZZ, \quad g_4 = ZXIXZ
$$

辛矩阵（$4 \times 10$，前5列为$X$分量，后5列为$Z$分量）：

$$
H_{\text{stab}} = \begin{pmatrix}
1 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 0 \\
1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1
\end{pmatrix}
$$

验证各向同性：$H_{\text{stab}} \Omega H_{\text{stab}}^T = 0 \pmod{2}$。

逻辑算符：$\bar{X} = XXXXX$，$\bar{Z} = ZZZZZ$。

$$
v_{\bar{X}} = (1,1,1,1,1 \mid 0,0,0,0,0), \quad v_{\bar{Z}} = (0,0,0,0,0 \mid 1,1,1,1,1)
$$

验证：$\langle v_{\bar{X}}, v_{\bar{Z}} \rangle_s = 1\cdot1+1\cdot1+1\cdot1+1\cdot1+1\cdot1 = 5 = 1 \pmod{2}$，所以 $\bar{X}$ 和 $\bar{Z}$ 反对易（正确）。

---

## Key Insight

辛表示的核心价值在于**将量子问题转化为经典线性代数问题**：

1. **对易性判断**：从矩阵乘法简化为二元内积
2. **Stabilizer群**：从矩阵群简化为 $\mathbb{F}_2$ 上的线性子空间
3. **逻辑算符**：从群论的normalizer简化为线性代数的零空间
4. **Syndrome计算**：从量子测量简化为矩阵-向量乘法
5. **码距计算**：从搜索Pauli算符简化为搜索二元向量

这使得所有stabilizer码的分析（surface code, color code, LDPC code等）都可以用成熟的 $\text{GF}(2)$ 线性代数工具高效处理。

---

## Summary

| 概念 | 辛表示 |
|------|--------|
| Pauli算符 | $(\mathbf{a}\mid\mathbf{b}) \in \mathbb{F}_2^{2n}$ |
| 乘法 | 向量加法 $\pmod{2}$ |
| 对易性 | $\langle v_P, v_Q\rangle_s = 0$ |
| Stabilizer群 | 各向同性子空间，维度 $n-k$ |
| Normalizer | 辛补 $V_\mathcal{S}^{\perp_s}$，维度 $n+k$ |
| 逻辑算符 | $V_\mathcal{S}^{\perp_s}/V_\mathcal{S}$，维度 $2k$ |
| Syndrome | $H_{\text{stab}}\Omega v_E^T$ |
| CSS码条件 | $H_X H_Z^T = 0$ |
