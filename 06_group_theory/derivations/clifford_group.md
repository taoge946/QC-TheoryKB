# Clifford Group

> **Tags**: `clifford`, `group-theory`, `normalizer`, `gottesman-knill`
>
> **Primary Source**: D. Gottesman, *Stabilizer Codes and Quantum Error Correction*, PhD thesis, Caltech (1997), Ch.5 **[Gottesman 1997, Ch.5, §5.3]**

## Statement

Clifford群 $\mathcal{C}_n$ 是Pauli群 $\mathcal{P}_n$ 在酉群 $U(2^n)$ 中的normalizer（正规化子） **[Gottesman 1997, Ch.5, §5.3]**。Clifford群由 $\{H, S, \text{CNOT}\}$ 生成 **[Gottesman 1997, Ch.5, §5.3, Thm.10]**，其电路对stabilizer态的作用可以在经典计算机上高效模拟（Gottesman-Knill定理）。

$$
\mathcal{C}_n = \{ U \in U(2^n) \mid U \mathcal{P}_n U^\dagger = \mathcal{P}_n \} / U(1)
$$

## Prerequisites

- Pauli群 $\mathcal{P}_n$ 的结构 → [pauli_group.md]
- Normalizer的定义 → [group_theory_basics.md]
- 基本量子门操作

---

## Derivation

### Step 1: Clifford Group Definition **[Gottesman 1997, Ch.5, §5.3]**

**定义**：$n$量子比特Clifford群是所有将Pauli群映射到自身的酉算符（模全局相位）：

$$
\mathcal{C}_n = N_{U(2^n)}(\mathcal{P}_n) / U(1) = \{ U \in U(2^n) \mid U P U^\dagger \in \mathcal{P}_n, \; \forall P \in \mathcal{P}_n \} / U(1)
$$

即对任意Pauli算符 $P$，共轭 $UPU^\dagger$ 仍是Pauli算符（可能是不同的Pauli，且可能带不同相位）。

**注意**：模掉 $U(1)$ 是因为全局相位在量子力学中不可观测。如果不模全局相位，定义中的 $U(1)$ 因子会使群变得不必要地大。

**Pauli群是Clifford群的正规子群**：$\mathcal{P}_n \trianglelefteq \mathcal{C}_n$，因为对任意 $P \in \mathcal{P}_n$ 和 $Q \in \mathcal{P}_n$，$PQP^\dagger = PQP^{-1} \in \mathcal{P}_n$（Pauli群对自身共轭封闭）。

### Step 2: Generators of the Clifford Group **[Gottesman 1997, Ch.5, §5.3, Thm.10]**

**定理**：$\mathcal{C}_n$ 由以下三种门生成：

$$
H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad
S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}, \quad
\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
$$

下面逐一验证它们属于Clifford群，即它们对Pauli算符的共轭作用仍为Pauli算符。

### Step 3: Hadamard Gate $H$ — Conjugation Action

计算 $HPH^\dagger$ 对各Pauli矩阵的作用（注意 $H^\dagger = H$）：

**$H X H^\dagger$**:

$$
HXH = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix} \begin{pmatrix}0&1\\1&0\end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
$$

$$
= \frac{1}{2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}2&0\\0&-2\end{pmatrix} = Z
$$

$$
\boxed{HXH^\dagger = Z}
$$

**$H Z H^\dagger$**:

$$
HZH = \frac{1}{2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
$$

$$
= \frac{1}{2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}0&2\\2&0\end{pmatrix} = X
$$

$$
\boxed{HZH^\dagger = X}
$$

**$H Y H^\dagger$**:

$$
HYH = H(iXZ)H = i(HXH)(HZH) = iZX = i(-iY) = -Y \cdot (-1) \cdot \ldots
$$

更直接的计算：$Y = iXZ$，所以

$$
HYH^\dagger = H(iXZ)H^\dagger = i(HXH^\dagger)(HZH^\dagger) = i \cdot Z \cdot X = i(-iY) = -Y \cdot \ldots
$$

仔细算：$ZX = iY$（从乘法表），所以

$$
HYH^\dagger = i \cdot ZX = i \cdot iY = i^2 Y = -Y
$$

$$
\boxed{HYH^\dagger = -Y}
$$

总结 $H$ 的作用：$X \leftrightarrow Z$，$Y \mapsto -Y$。直观理解：$H$ 交换了$X$基和$Z$基。

### Step 4: Phase Gate $S$ — Conjugation Action

$S = \text{diag}(1, i)$，$S^\dagger = \text{diag}(1, -i)$。

**$S X S^\dagger$**:

$$
SXS^\dagger = \begin{pmatrix}1&0\\0&i\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&-i\end{pmatrix} = \begin{pmatrix}0&1\\i&0\end{pmatrix}\begin{pmatrix}1&0\\0&-i\end{pmatrix} = \begin{pmatrix}0&-i\\i&0\end{pmatrix} = Y
$$

$$
\boxed{SXS^\dagger = Y}
$$

**$S Z S^\dagger$**:

$$
SZS^\dagger = \begin{pmatrix}1&0\\0&i\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1&0\\0&-i\end{pmatrix} = \begin{pmatrix}1&0\\0&-i\end{pmatrix}\begin{pmatrix}1&0\\0&-i\end{pmatrix} = \begin{pmatrix}1&0\\0&-1\end{pmatrix} = Z
$$

$$
\boxed{SZS^\dagger = Z}
$$

**$S Y S^\dagger$**:

$$
SYS^\dagger = S(iXZ)S^\dagger = i(SXS^\dagger)(SZS^\dagger) = i \cdot Y \cdot Z = i \cdot iX = -X
$$

（其中 $YZ = iX$ 来自乘法表）

$$
\boxed{SYS^\dagger = -X}
$$

总结 $S$ 的作用：$X \mapsto Y$，$Y \mapsto -X$，$Z \mapsto Z$。直观理解：$S$ 在$XY$平面上做90度旋转（在Bloch球上绕$Z$轴旋转$\pi/2$）。

### Step 5: CNOT Gate — Conjugation Action

CNOT以第1个qubit为control、第2个为target。记 $P_1 \otimes P_2$ 为两qubit上的Pauli算符。

逐一计算 $\text{CNOT} \cdot (P_1 \otimes P_2) \cdot \text{CNOT}^\dagger$（注意 $\text{CNOT}^\dagger = \text{CNOT}$）：

$$
\boxed{X \otimes I \;\mapsto\; X \otimes X}
$$

推导：$\text{CNOT}|a, b\rangle = |a, a \oplus b\rangle$。

$$
\text{CNOT}(X \otimes I)\text{CNOT}|a, b\rangle = \text{CNOT}(X \otimes I)|a, a\oplus b\rangle = \text{CNOT}|a\oplus 1, a\oplus b\rangle
$$

$$
= |a\oplus 1, (a\oplus 1)\oplus(a\oplus b)\rangle = |a\oplus 1, 1 \oplus b\rangle = (X \otimes X)|a, b\rangle
$$

$$
\boxed{I \otimes X \;\mapsto\; I \otimes X}
$$

推导：

$$
\text{CNOT}(I \otimes X)\text{CNOT}|a,b\rangle = \text{CNOT}(I \otimes X)|a, a\oplus b\rangle = \text{CNOT}|a, a\oplus b\oplus 1\rangle
$$

$$
= |a, a\oplus(a\oplus b\oplus 1)\rangle = |a, b\oplus 1\rangle = (I\otimes X)|a,b\rangle
$$

$$
\boxed{Z \otimes I \;\mapsto\; Z \otimes I}
$$

推导：对计算基态 $|a,b\rangle$：

$$
\text{CNOT}(Z\otimes I)\text{CNOT}|a,b\rangle = \text{CNOT}(Z\otimes I)|a,a\oplus b\rangle = (-1)^a \text{CNOT}|a,a\oplus b\rangle
$$

$$
= (-1)^a|a,b\rangle = (Z\otimes I)|a,b\rangle
$$

$$
\boxed{I \otimes Z \;\mapsto\; Z \otimes Z}
$$

推导：

$$
\text{CNOT}(I\otimes Z)\text{CNOT}|a,b\rangle = \text{CNOT}(I\otimes Z)|a,a\oplus b\rangle = (-1)^{a\oplus b}\text{CNOT}|a,a\oplus b\rangle
$$

$$
= (-1)^{a\oplus b}|a,b\rangle = (-1)^a(-1)^b|a,b\rangle = (Z\otimes Z)|a,b\rangle
$$

**CNOT共轭作用完整表格**：

| Input | Output |
|-------|--------|
| $X \otimes I$ | $X \otimes X$ |
| $I \otimes X$ | $I \otimes X$ |
| $Z \otimes I$ | $Z \otimes I$ |
| $I \otimes Z$ | $Z \otimes Z$ |
| $Y \otimes I$ | $Y \otimes X$ |
| $I \otimes Y$ | $Z \otimes Y$ |

其中后两行由前四行推出：$Y = iXZ$，所以

$$
Y \otimes I \mapsto i(X\otimes X)(Z\otimes I) = i(XZ\otimes X) = Y\otimes X
$$

$$
I\otimes Y \mapsto i(I\otimes X)(Z\otimes Z) = i(Z\otimes XZ) = Z\otimes Y
$$

直观理解：CNOT将control的$X$错误传播到target，将target的$Z$错误传播回control。这就是量子纠错中"错误传播"分析的基础。

### Step 6: Why $\{H, S, \text{CNOT}\}$ Generate $\mathcal{C}_n$

**定理** (Gottesman, 1998)：任意$n$量子比特Clifford算符都可以分解为 $H$、$S$、$\text{CNOT}$ 门的有限序列。

**证明思路**：

Clifford算符 $U$ 完全由其对Pauli生成元 $\{X_1, Z_1, X_2, Z_2, \ldots, X_n, Z_n\}$ 的共轭作用确定（因为Pauli群由这些生成，知道生成元的像就知道所有元素的像）。

$U$ 的共轭作用可以表示为辛矩阵 $M \in \text{Sp}(2n, \mathbb{F}_2)$（见 Step 8）。而辛群 $\text{Sp}(2n, \mathbb{F}_2)$ 由以下变换生成：
- $H$ 对应交换 $(x_k, z_k)$ 的辛变换
- $S$ 对应 $z_k \mapsto z_k + x_k$ 的辛变换
- CNOT 对应行操作的辛变换

这三种变换生成了整个 $\text{Sp}(2n, \mathbb{F}_2)$，因此 $\{H, S, \text{CNOT}\}$ 生成整个Clifford群。

### Step 7: Clifford Group Order

**定理** (Nebe, Rains & Sloane, 2001)：

$$
|\mathcal{C}_n| = 2^{n^2 + 2n} \prod_{j=0}^{n-1} (4^{j+1} - 1)
$$

**推导**：

Clifford群模Pauli群同构于辛群：

$$
\mathcal{C}_n / \mathcal{P}_n \cong \text{Sp}(2n, \mathbb{F}_2)
$$

（严格地说是模去中心后同构。）

辛群的阶为：

$$
|\text{Sp}(2n, \mathbb{F}_2)| = 2^{n^2} \prod_{j=1}^{n} (4^j - 1)
$$

推导辛群阶的方法是计算辛基的选择方式数：
- 第1对辛基向量 $(e_1, f_1)$：$e_1$ 可以是 $\mathbb{F}_2^{2n} \setminus \{0\}$ 中任意非零向量（$4^n - 1$种），$f_1$ 必须满足 $\langle e_1, f_1 \rangle_s = 1$ 且不在 $\text{span}(e_1)$ 中（$2^{2n-1}$种，因为辛内积将空间分为一半满足$\langle e_1, \cdot\rangle_s = 0$和一半满足$\langle e_1, \cdot\rangle_s = 1$）。但 $f_1$ 的选择还需要精确计算...

更直接的计算：

$$
|\text{Sp}(2n, \mathbb{F}_2)| = 2^{n^2} \prod_{j=1}^{n}(4^j - 1)
$$

于是

$$
|\mathcal{C}_n| = |\mathcal{P}_n / Z(\mathcal{P}_n)| \cdot |\text{Sp}(2n, \mathbb{F}_2)| = 4^n \cdot 2^{n^2} \prod_{j=1}^{n}(4^j - 1) = 2^{n^2+2n} \prod_{j=0}^{n-1}(4^{j+1} - 1)
$$

**具体数值**：

| $n$ | $\|\mathcal{C}_n\|$ |
|-----|---------------------|
| 1 | $2^3 \cdot 3 = 24$ |
| 2 | $2^8 \cdot 3 \cdot 15 = 11520$ |
| 3 | $2^{15} \cdot 3 \cdot 15 \cdot 63 = 92{,}897{,}280$ |

$n=1$ 时 $\mathcal{C}_1$ 同构于 $S_4$（4元素置换群），作用于Bloch球的3个坐标轴（6个方向）的正八面体对称群。

### Step 8: Symplectic Representation of Clifford Operations

每个Pauli算符（忽略相位）对应二元向量 $v = (\mathbf{a} | \mathbf{b}) \in \mathbb{F}_2^{2n}$。

Clifford算符 $U$ 的共轭作用 $P \mapsto UPU^\dagger$ 在辛表示中变为线性映射：

$$
v \mapsto M v \pmod{2}
$$

其中 $M \in \text{Sp}(2n, \mathbb{F}_2)$ 是 $2n \times 2n$ 辛矩阵，满足：

$$
M \Omega M^T = \Omega \pmod{2}, \quad \text{where} \quad \Omega = \begin{pmatrix} 0 & I_n \\ I_n & 0 \end{pmatrix}
$$

**生成元的辛矩阵**（$n=1$的情况，$\Omega = \begin{pmatrix}0&1\\1&0\end{pmatrix}$）：

$H$ gate：交换 $X \leftrightarrow Z$，即 $(a|b) \mapsto (b|a)$：

$$
M_H = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

$S$ gate：$X \mapsto Y = iXZ$，即 $(1|0) \mapsto (1|1)$；$Z \mapsto Z$，即 $(0|1) \mapsto (0|1)$：

$$
M_S = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}
$$

CNOT gate（$n=2$，$4\times 4$ 矩阵）：
从共轭作用表格：

$$
(1,0|0,0) \mapsto (1,0|0,0) \quad \text{(Z_1 不变)}
$$

等等...... 写成标准形式（$(x_1,x_2|z_1,z_2)$排列）：

$$
M_{\text{CNOT}} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{pmatrix}
$$

验证辛条件 $M\Omega M^T = \Omega$：

$$
\Omega_{4\times 4} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}
$$

$$
M_{\text{CNOT}} \Omega M_{\text{CNOT}}^T = \begin{pmatrix}1&0&0&0\\1&1&0&0\\0&0&1&1\\0&0&0&1\end{pmatrix}\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix}\begin{pmatrix}1&1&0&0\\0&1&0&0\\0&0&1&0\\0&0&1&1\end{pmatrix} = \Omega \quad \checkmark
$$

### Gottesman Thesis: Clifford Group as Normalizer of Pauli Group

> **[Gottesman thesis, §5.3]**: The set of $U$ such that $UAU^\dagger \in \mathcal{G}$ for all $A \in \mathcal{G}$ is the normalizer $N(\mathcal{G})$ of $\mathcal{G}$ in $U(n)$. It turns out that $N(\mathcal{G})$ is generated by the single qubit operations $R$ (the Hadamard transform) and $P = \text{diag}(1, i)$, and the controlled NOT.

**Conjugation actions from thesis** [Gottesman thesis, §5.3]:

> **[Gottesman thesis, §5.3]**: $R$ switches $X$ and $Z$:
> $$RXR^\dagger = Z, \quad RZR^\dagger = X, \quad RYR^\dagger = -Y$$

> **[Gottesman thesis, §5.3]**: $P$ switches $X$ and $Y$:
> $$PXP^\dagger = Y, \quad PZP^\dagger = Z$$
> These two operations generate all possible permutations of $X$, $Y$, and $Z$.

> **[Gottesman thesis, §5.3]**: The CNOT acts as:
> $$X \otimes I \to X \otimes X, \quad I \otimes X \to I \otimes X$$
> $$Z \otimes I \to Z \otimes I, \quad I \otimes Z \to Z \otimes Z$$
> Amplitudes are copied forwards and phases are copied backwards.

### Automorphism Correspondence

> **[Gottesman thesis, §5.3]**: Given an automorphism of $\mathcal{G}$, we can always find an element of $N(\mathcal{G})$ that produces that automorphism, modulo the automorphism $iI \to -iI$. We can find the matrix of a given transformation $U$ corresponding to some automorphism by determining the action of $U$ on basis states. $|0\rangle$ is an eigenvector of $Z$, so it is mapped to an eigenvector of $UZU^\dagger$. $|1\rangle = X|0\rangle$, so it becomes $(UXU^\dagger)U|0\rangle$.

### The Four-Qubit Gate for Universal Stabilizer Operations

> **[Gottesman thesis, §5.4, Eq. 5.6-5.7]**: Consider the four-qubit transformation where $X_i \to X_i \otimes X_{i+1} \otimes X_{i+2}$ (cyclic, omitting one) and similarly for $Z$. Given an element $M$ of an arbitrary stabilizer, this operation applied bitwise maps:
> $$M \otimes I \otimes I \otimes I \to M \otimes M \otimes M \otimes I$$
> Each image is in the group $S \times S \times S \times S$, so this is a valid transversal operation for any stabilizer code. Using this with ancilla preparation and measurement, we can perform any operation in $N(\mathcal{G})$ for any stabilizer code encoding a single qubit.

### Step 9: Gottesman-Knill Theorem

**定理** (Gottesman, 1998; Knill, 1996)：

> **[Gottesman thesis, §5.6]**: Knill has shown that a quantum computer using only elements from $N(\mathcal{G})$ and measurements can be simulated efficiently on a classical computer. The argument follows easily: If we begin with a state initialized to $|0\cdots 0\rangle$, the stabilizer is $Z_1, Z_2, \ldots$. Each operation in $N(\mathcal{G})$ produces a well-defined transformation of the stabilizer, which can be classically tracked efficiently. Any measurement will also transform the stabilizer in a well-defined way.

以下量子计算模型可以在经典计算机上用 $O(\text{poly}(n))$ 时间和空间模拟：

1. 输入态为计算基态 $|0\rangle^{\otimes n}$
2. 门为Clifford门（$H, S, \text{CNOT}$ 的任意组合）
3. 测量为计算基测量（等价于Pauli $Z$测量）
4. 允许经典前馈（根据测量结果选择后续门）

**证明思路**：

**核心思想**：不追踪量子态向量（$2^n$维），而是追踪stabilizer群的生成元（$n$个Pauli算符，每个用$O(n)$位描述）。

1. **初始态**：$|0\rangle^{\otimes n}$ 的stabilizer群由 $\{Z_1, Z_2, \ldots, Z_n\}$ 生成（$Z_k|0\rangle^{\otimes n} = |0\rangle^{\otimes n}$）。

2. **Clifford门的更新**：施加Clifford门 $U$ 时，新的stabilizer生成元为 $\{Ug_1U^\dagger, Ug_2U^\dagger, \ldots, Ug_nU^\dagger\}$。由于 $U$ 是Clifford门，$Ug_kU^\dagger$ 仍是Pauli算符，可以用 $O(n)$ 位表示。更新$n$个生成元需要 $O(n^2)$ 时间。

3. **测量模拟**：测量Pauli算符 $P$ 时：
   - 若 $P$ 与所有stabilizer生成元对易：结果确定性（$+1$或$-1$），$O(n^2)$时间计算
   - 若 $P$ 与某个生成元 $g_j$ 反对易：结果等概率$\pm 1$，更新stabilizer（用$g_j$替换为$\pm P$），$O(n^2)$时间

4. **总复杂度**：$m$个门+$n$次测量需要 $O(mn^2 + n^3)$ 经典时间。

**意义**：Clifford电路不具有量子计算优越性。要实现通用量子计算和潜在的指数加速，需要添加非Clifford门（如 $T$ gate）。$T$ gate定义为：

$$
T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
$$

$T$ 不是Clifford门，因为 $TXT^\dagger = \frac{1}{\sqrt{2}}(X + Y) \notin \mathcal{P}_1$。$\{H, S, T, \text{CNOT}\}$ 构成通用门集。

### Step 10: Clifford Hierarchy

Clifford层级是对"非Clifford程度"的分层：

$$
\mathcal{C}^{(1)}_n = \mathcal{P}_n, \quad \mathcal{C}^{(k+1)}_n = \{ U \mid U\mathcal{P}_n U^\dagger \subseteq \mathcal{C}^{(k)}_n \}
$$

- 第1层：Pauli群
- 第2层：Clifford群（$U$把Pauli映射到Pauli）
- 第3层：$U$把Pauli映射到Clifford算符（$T$ gate在第3层）
- 更高层：类推

Clifford层级在容错量子计算中很重要：第$k$层的门可以用magic state distillation和第$(k-1)$层的门容错地实现。

---

## Key Insight

Clifford群是"经典可模拟"与"量子优越性"的分界线。Clifford电路虽然能产生高度纠缠的量子态，但其结构被stabilizer formalism完美捕捉，使得经典模拟成为可能。从实用角度看：

1. **量子纠错**完全在Clifford群框架内运作（stabilizer码、syndrome测量、Pauli恢复操作都是Clifford运算）
2. **Magic state distillation**是将非Clifford资源注入的桥梁
3. **Clifford + $T$** 门集是容错量子计算的标准范式

---

## Summary

| 概念 | 结果 |
|------|------|
| 定义 | $\mathcal{C}_n = N_{U(2^n)}(\mathcal{P}_n)/U(1)$ |
| 生成元 | $\{H, S, \text{CNOT}\}$ |
| 群阶 | $2^{n^2+2n}\prod_{j=0}^{n-1}(4^{j+1}-1)$ |
| 辛表示 | $\mathcal{C}_n/\mathcal{P}_n \cong \text{Sp}(2n,\mathbb{F}_2)$ |
| Gottesman-Knill | Clifford电路经典可模拟 |
| 通用性 | 需添加非Clifford门（如$T$）|
