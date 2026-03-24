# Schmidt Decomposition (Schmidt 分解)

> **Tags**: `schmidt`, `entanglement`, `bipartite`, `svd`

## Statement

**定理（Schmidt Decomposition）** **[N&C, Theorem 2.7, p.109]** **[Preskill, Ch.2, &sect;2.4, pp.23-25]**: 任何双体（bipartite）纯态 $|\psi\rangle_{AB} \in \mathcal{H}_A \otimes \mathcal{H}_B$ 都可以写成如下形式：

$$|\psi\rangle_{AB} = \sum_{i=1}^{r} \lambda_i \, |a_i\rangle_A \otimes |b_i\rangle_B$$

其中：
- $\lambda_i > 0$，$\sum_i \lambda_i^2 = 1$（Schmidt 系数）
- $\{|a_i\rangle\}$ 是 $\mathcal{H}_A$ 中的标准正交集
- $\{|b_i\rangle\}$ 是 $\mathcal{H}_B$ 中的标准正交集
- $r \leq \min(d_A, d_B)$ 是 Schmidt 秩（Schmidt rank）

## Prerequisites

- **奇异值分解（SVD）**: 任意矩阵 $M = U\Sigma V^\dagger$
- **张量积**: $\mathcal{H}_A \otimes \mathcal{H}_B$，计算基的展开
- **Dirac 记号**: $|a\rangle \otimes |b\rangle$，或简写为 $|a\rangle|b\rangle$ 或 $|ab\rangle$

---

## Derivation

### Step 1: 一般双体纯态的展开

选 $\mathcal{H}_A$ 的标准正交基 $\{|i\rangle_A\}_{i=1}^{d_A}$ 和 $\mathcal{H}_B$ 的标准正交基 $\{|j\rangle_B\}_{j=1}^{d_B}$。

任何 $|\psi\rangle_{AB}$ 可以展开为：

$$|\psi\rangle_{AB} = \sum_{i=1}^{d_A}\sum_{j=1}^{d_B} c_{ij} \, |i\rangle_A \otimes |j\rangle_B$$

其中 $c_{ij} \in \mathbb{C}$ 是展开系数，满足归一化条件：

$$\langle\psi|\psi\rangle = \sum_{i,j}|c_{ij}|^2 = 1$$

系数 $c_{ij}$ 构成一个 $d_A \times d_B$ 的复矩阵 $C$，即 $(C)_{ij} = c_{ij}$。

### Step 2: 对系数矩阵做 SVD

**奇异值分解回顾** **[N&C, Corollary 2.4, p.79]**：任何 $m \times n$ 复矩阵 $C$ 都可以分解为：

$$C = U \Sigma V^\dagger$$

其中：
- $U$ 是 $m \times m$ 幺正矩阵（$U^\dagger U = I_m$）
- $V$ 是 $n \times n$ 幺正矩阵（$V^\dagger V = I_n$）
- $\Sigma$ 是 $m \times n$ "对角"矩阵，对角元 $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$（奇异值），$r = \text{rank}(C)$

写成分量形式：

$$c_{ij} = \sum_{k=1}^{r} U_{ik} \, \sigma_k \, (V^\dagger)_{kj} = \sum_{k=1}^{r} U_{ik} \, \sigma_k \, V_{jk}^*$$

### Step 3: 代入态矢量

将 $c_{ij}$ 的 SVD 代入 $|\psi\rangle$ 的展开：

$$|\psi\rangle_{AB} = \sum_{i,j} c_{ij} \, |i\rangle_A|j\rangle_B = \sum_{i,j}\sum_{k=1}^{r} U_{ik}\,\sigma_k\,V_{jk}^* \, |i\rangle_A|j\rangle_B$$

交换求和顺序（都是有限和，可以自由交换）：

$$= \sum_{k=1}^{r} \sigma_k \left(\sum_i U_{ik}|i\rangle_A\right) \otimes \left(\sum_j V_{jk}^*|j\rangle_B\right)$$

### Step 4: 定义 Schmidt 基

定义新的基矢量：

$$|a_k\rangle_A = \sum_{i=1}^{d_A} U_{ik} \, |i\rangle_A$$

$$|b_k\rangle_B = \sum_{j=1}^{d_B} V_{jk}^* \, |j\rangle_B$$

**验证正交归一性**：

对 $|a_k\rangle$ 的内积：

$$\langle a_k|a_l\rangle = \sum_{i,i'} U_{ik}^* \, U_{i'l} \, \langle i|i'\rangle = \sum_i U_{ik}^* U_{il} = (U^\dagger U)_{kl} = \delta_{kl}$$

这里用了 $\langle i|i'\rangle = \delta_{ii'}$（原始基的正交归一性）和 $U$ 的幺正性。

对 $|b_k\rangle$ 的内积：

$$\langle b_k|b_l\rangle = \sum_{j,j'} V_{jk} \, V_{j'l}^* \, \langle j|j'\rangle = \sum_j V_{jk} V_{jl}^* = (V^\dagger V)_{kl} = \delta_{kl}$$

两组基都是标准正交的。

### Step 5: 写出 Schmidt 分解

令 $\lambda_k = \sigma_k$（SVD 的奇异值），代入得：

$$\boxed{|\psi\rangle_{AB} = \sum_{k=1}^{r} \lambda_k \, |a_k\rangle_A \otimes |b_k\rangle_B}$$
**[N&C, Theorem 2.7, p.109]** **[Preskill, Ch.2, &sect;2.4, p.23]**

其中 $\lambda_k > 0$（奇异值为正），$r = \text{rank}(C) \leq \min(d_A, d_B)$。

**归一化验证**：

$$\langle\psi|\psi\rangle = \sum_{k,l}\lambda_k\lambda_l\langle a_k|a_l\rangle\langle b_k|b_l\rangle = \sum_{k,l}\lambda_k\lambda_l\delta_{kl}\delta_{kl} = \sum_k\lambda_k^2 = 1$$

最后一个等式成立是因为 SVD 奇异值满足 $\sum_k\sigma_k^2 = \|C\|_F^2 = \sum_{ij}|c_{ij}|^2 = 1$。

### Step 6: Schmidt 分解的唯一性

Schmidt 系数 $\{\lambda_k\}$（即奇异值）是**唯一的**（给定从大到小排序）。

但是，Schmidt 基 $\{|a_k\rangle\}$ 和 $\{|b_k\rangle\}$ 在某个 $\lambda_k$ 简并时（即多个奇异值相等时）**不唯一**——可以在简并子空间内做幺正旋转。

### Step 7: Schmidt 秩与纠缠判据

**定义** **[N&C, p.109]** **[Preskill, Ch.2, &sect;2.4.1, pp.25-26]**: Schmidt 秩 $r$ = 非零 Schmidt 系数的个数。

**纠缠判据**：

$$|\psi\rangle_{AB} \text{ 是可分态（product state）} \iff r = 1$$

$$|\psi\rangle_{AB} \text{ 是纠缠态} \iff r \geq 2$$

**证明（$\Rightarrow$）**: 如果 $|\psi\rangle = |\alpha\rangle_A \otimes |\beta\rangle_B$，则系数矩阵 $c_{ij} = \alpha_i\beta_j$（秩为 1 的矩阵），所以 $r = 1$。

**证明（$\Leftarrow$）**: 如果 $r = 1$，则 $|\psi\rangle = \lambda_1|a_1\rangle|b_1\rangle$，又 $\lambda_1 = 1$（归一化），所以 $|\psi\rangle = |a_1\rangle|b_1\rangle$ 是乘积态。

### Step 8: 约化密度矩阵与 Schmidt 系数

对 Schmidt 形式的态求偏迹，可以直接得到约化密度矩阵。

**子系统 $A$ 的约化密度矩阵**：

$$\rho_A = \text{Tr}_B(|\psi\rangle\langle\psi|) = \text{Tr}_B\left(\sum_{k,l}\lambda_k\lambda_l|a_k\rangle\langle a_l| \otimes |b_k\rangle\langle b_l|\right)$$

利用偏迹规则 $\text{Tr}_B(|b_k\rangle\langle b_l|) = \langle b_l|b_k\rangle = \delta_{kl}$：

$$= \sum_{k,l}\lambda_k\lambda_l|a_k\rangle\langle a_l|\,\delta_{kl} = \sum_k\lambda_k^2|a_k\rangle\langle a_k|$$

$$\boxed{\rho_A = \sum_{k=1}^r \lambda_k^2 \, |a_k\rangle\langle a_k|}$$

类似地：

$$\boxed{\rho_B = \sum_{k=1}^r \lambda_k^2 \, |b_k\rangle\langle b_k|}$$
**[N&C, p.109]** **[Preskill, Ch.2, &sect;2.4.1, pp.25-26]**

**极其重要的结论**：$\rho_A$ 和 $\rho_B$ 有**相同的非零特征值** $\{\lambda_k^2\}$！ **[N&C, Corollary, p.109]**

即使 $d_A \neq d_B$，两个约化密度矩阵的非零特征值完全一致。

### Step 9: 与纠缠熵的联系

双体纯态的纠缠熵定义为任一约化密度矩阵的 von Neumann 熵 **[N&C, Theorem 11.8(3), p.513]** **[Preskill, Ch.2, &sect;2.4.1, pp.25-26]**：

$$E(|\psi\rangle_{AB}) = S(\rho_A) = S(\rho_B) = -\sum_{k=1}^r \lambda_k^2 \log \lambda_k^2$$

由 Step 8，$S(\rho_A) = S(\rho_B)$——双体纯态中两个子系统的熵总是相同的 **[N&C, Section 2.5.1, p.109]**。

**纠缠的度量**：

- $E = 0$：$r = 1$，可分态，无纠缠
- $E = \log r$（最大值）：所有 $\lambda_k = 1/\sqrt{r}$ 相等，最大纠缠
- $E = \log d$（$d = \min(d_A,d_B)$，$r = d$）：最大纠缠态

**例子 —— Bell 态**：

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle$$

这已经是 Schmidt 形式！Schmidt 系数为 $\lambda_1 = \lambda_2 = \frac{1}{\sqrt{2}}$，$r = 2$。

$$E = -2 \cdot \frac{1}{2}\log\frac{1}{2} = \log 2$$

这是两量子比特系统的最大纠缠。

### Step 10: 完整计算示例

考虑态：

$$|\psi\rangle = \frac{1}{2}|00\rangle + \frac{1}{2}|01\rangle + \frac{1}{2}|10\rangle + \frac{1}{2}|11\rangle$$

**Step 10a**: 写出系数矩阵。

$$C = \begin{pmatrix}c_{00} & c_{01} \\ c_{10} & c_{11}\end{pmatrix} = \begin{pmatrix}1/2 & 1/2 \\ 1/2 & 1/2\end{pmatrix}$$

**Step 10b**: 做 SVD。

$C = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}$。这个矩阵的秩为 1。

特征值：$C^\dagger C = \frac{1}{4}\begin{pmatrix}2&2\\2&2\end{pmatrix}$，特征值为 $1$ 和 $0$。

奇异值：$\sigma_1 = 1$，$\sigma_2 = 0$。

右奇异向量：$V_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}$。

左奇异向量：$U_1 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}$。

**Step 10c**: Schmidt 分解。

$$|a_1\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$$

$$|b_1\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$$

$$|\psi\rangle = 1 \cdot |+\rangle_A \otimes |+\rangle_B = |+\rangle|+\rangle$$

Schmidt 秩 $r = 1$，这是一个可分态（没有纠缠），只是写在计算基下"看起来"复杂。

### Step 11: 另一个例子 —— 真正的纠缠态

考虑：

$$|\psi\rangle = \frac{\sqrt{3}}{2}|00\rangle + \frac{1}{2}|11\rangle$$

系数矩阵：

$$C = \begin{pmatrix}\sqrt{3}/2 & 0 \\ 0 & 1/2\end{pmatrix}$$

这已经是对角矩阵，所以 SVD 就是它自己。奇异值 $\sigma_1 = \sqrt{3}/2$，$\sigma_2 = 1/2$。

Schmidt 分解（恰好就是原始形式）：

$$|\psi\rangle = \frac{\sqrt{3}}{2}|0\rangle|0\rangle + \frac{1}{2}|1\rangle|1\rangle$$

$r = 2$，这是纠缠态。约化密度矩阵：

$$\rho_A = \frac{3}{4}|0\rangle\langle 0| + \frac{1}{4}|1\rangle\langle 1|$$

纠缠熵：

$$E = -\frac{3}{4}\log\frac{3}{4} - \frac{1}{4}\log\frac{1}{4} \approx 0.811 \text{ bits}$$

小于 $\log 2 = 1$ bit（Bell 态的纠缠量），说明这不是最大纠缠态。

---

## Summary

| 概念 | 数学表达 | 意义 |
|------|---------|------|
| Schmidt 分解 | $\|\psi\rangle = \sum_k\lambda_k\|a_k\rangle\|b_k\rangle$ | 双体纯态的标准形式 |
| 来自 SVD | $C = U\Sigma V^\dagger$ → $\lambda_k = \sigma_k$ | 系数矩阵的奇异值 = Schmidt 系数 |
| Schmidt 秩 | $r = $ 非零 $\lambda_k$ 的个数 | $r=1$: 可分态; $r>1$: 纠缠态 |
| 约化密度矩阵 | $\rho_A = \sum_k\lambda_k^2\|a_k\rangle\langle a_k\|$ | 两个子系统有相同的非零特征值 |
| 纠缠熵 | $E = -\sum_k\lambda_k^2\log\lambda_k^2$ | $S(\rho_A) = S(\rho_B)$ |

---

## Nielsen & Chuang: Theorems and Formal Results

### Theorem 2.7 (Schmidt Decomposition) **[Nielsen & Chuang, Theorem 2.7, p.109]**
Suppose $|\psi\rangle$ is a pure state of a composite system $AB$. Then there exist orthonormal states $|i_A\rangle$ for system $A$ and orthonormal states $|i_B\rangle$ for system $B$ such that:
$$|\psi\rangle = \sum_i \lambda_i |i_A\rangle|i_B\rangle$$
where $\lambda_i$ are non-negative real numbers satisfying $\sum_i \lambda_i^2 = 1$ known as *Schmidt coefficients*.

**Proof** **[Nielsen & Chuang, p.109]**: Write $|\psi\rangle = \sum_{jk} a_{jk}|j\rangle|k\rangle$. By the singular value decomposition (Corollary 2.4, p.79), $a = udv$ where $u, v$ are unitary and $d$ is diagonal with non-negative entries. Define $|i_A\rangle \equiv \sum_j u_{ji}|j\rangle$ and $|i_B\rangle \equiv \sum_k v_{ik}^*|k\rangle$. The orthonormality of these bases follows from the unitarity of $u$ and $v$: $\langle i_A|j_A\rangle = (u^\dagger u)_{ij} = \delta_{ij}$. Then $|\psi\rangle = \sum_i d_{ii}|i_A\rangle|i_B\rangle$.

### Schmidt Number **[Nielsen & Chuang, p.109]**
The number of non-zero values $\lambda_i$ is called the *Schmidt number* (or Schmidt rank). A state is a product state iff the Schmidt number is 1.

### Corollary: Equal Eigenvalues of Reduced Density Matrices **[Nielsen & Chuang, p.109]**
From the Schmidt decomposition:
$$\rho_A = \sum_i \lambda_i^2 |i_A\rangle\langle i_A|, \qquad \rho_B = \sum_i \lambda_i^2 |i_B\rangle\langle i_B|$$
Therefore $\rho_A$ and $\rho_B$ have the same non-zero eigenvalues $\{\lambda_i^2\}$, even when $\dim(\mathcal{H}_A) \neq \dim(\mathcal{H}_B)$.

### Theorem 2.8 (Purification) **[Nielsen & Chuang, Theorem 2.8, p.110]**
For any state $\rho^A$ of system $A$ there exists a *purification*: a pure state $|AR\rangle$ of a composite system $AR$ such that $\rho^A = \text{Tr}_R(|AR\rangle\langle AR|)$.

**Construction** **[Nielsen & Chuang, p.110]**: If $\rho^A = \sum_i p_i|i^A\rangle\langle i^A|$ (spectral decomposition), then $|AR\rangle = \sum_i \sqrt{p_i}|i^A\rangle|i^R\rangle$ is a purification, where $\{|i^R\rangle\}$ is any orthonormal basis for $R$ with $\dim(R) \geq \text{rank}(\rho^A)$.

### Freedom in Purifications **[Nielsen & Chuang, p.110]**
Different purifications of the same state are related by unitary operations on the reference system: if $|AR\rangle$ and $|AR'\rangle$ are both purifications of $\rho^A$, then $|AR'\rangle = (I_A \otimes U_R)|AR\rangle$ for some unitary $U_R$.

### Entanglement Detection **[Nielsen & Chuang, Section 2.5.1, p.109]**
A bipartite pure state $|\psi\rangle_{AB}$ is entangled if and only if its Schmidt number is greater than 1, equivalently if and only if $S(\rho_A) > 0$.

---

## Preskill: Theorems and Formal Results (Chapter 2)

### Schmidt Decomposition **[Preskill, Ch.2, §2.4, pp.23-25]**
**Theorem**: Any bipartite pure state $|\psi\rangle_{AB} \in \mathcal{H}_A \otimes \mathcal{H}_B$ can be expressed as:
$$|\psi\rangle_{AB} = \sum_{i=1}^r \sqrt{p_i}\,|i_A\rangle|i_B\rangle$$
where $p_i > 0$, $\sum_i p_i = 1$, $\{|i_A\rangle\}$ and $\{|i_B\rangle\}$ are orthonormal sets in $\mathcal{H}_A$ and $\mathcal{H}_B$ respectively, and $r \leq \min(\dim\mathcal{H}_A, \dim\mathcal{H}_B)$.

**Proof** [Preskill, Ch.2, §2.4, p.18]: Write $|\psi\rangle = \sum_{i,j}C_{ij}|i\rangle_A|j\rangle_B$ and apply SVD to the coefficient matrix: $C = U\Sigma V^\dagger$. Define Schmidt bases $|k_A\rangle = \sum_i U_{ik}|i\rangle$ and $|k_B\rangle = \sum_j V_{jk}^*|j\rangle$. The orthonormality of these bases follows from the unitarity of $U$ and $V$.

### Schmidt Number and Entanglement **[Preskill, Ch.2, §2.4.1, pp.25-26]**
**Definition**: The Schmidt number (Schmidt rank) $r$ is the number of nonzero Schmidt coefficients.

**Entanglement criterion**:
- $r = 1$: the state is a product state $|\psi\rangle = |\alpha\rangle_A|\beta\rangle_B$ (no entanglement)
- $r \geq 2$: the state is entangled

**Key consequence**: From the Schmidt decomposition, the reduced density matrices are:
$$\rho_A = \sum_i p_i|i_A\rangle\langle i_A|, \qquad \rho_B = \sum_i p_i|i_B\rangle\langle i_B|$$

Therefore $\rho_A$ and $\rho_B$ have **identical nonzero eigenvalues** $\{p_i\}$, even when $\dim\mathcal{H}_A \neq \dim\mathcal{H}_B$. This implies $S(\rho_A) = S(\rho_B)$ for any bipartite pure state.

### Purification as Generalized Schmidt Decomposition **[Preskill, Ch.2, §2.4, pp.23-24]**
Preskill presents purification as the converse of the Schmidt decomposition:

**Theorem (Purification)**: For any mixed state $\rho_A = \sum_i p_i|i_A\rangle\langle i_A|$, the state
$$|\Psi\rangle_{AR} = \sum_i \sqrt{p_i}|i_A\rangle|i_R\rangle$$
is a purification satisfying $\text{Tr}_R(|\Psi\rangle\langle\Psi|) = \rho_A$, where $\{|i_R\rangle\}$ is any orthonormal set in a reference system $R$ with $\dim R \geq \text{rank}(\rho_A)$.

**Freedom in purification** [Preskill, Ch.2, §2.4, p.19]: All purifications of $\rho_A$ are related by unitaries on the reference system: if $|\Psi\rangle$ and $|\Psi'\rangle$ are both purifications of $\rho_A$, then $|\Psi'\rangle = (I_A \otimes U_R)|\Psi\rangle$.

### Entanglement Quantification via Schmidt Coefficients **[Preskill, Ch.2, §2.4.1, pp.25-26]**
The Schmidt coefficients provide a complete characterization of entanglement for bipartite pure states:

**Entanglement entropy**:
$$E(|\psi\rangle_{AB}) = S(\rho_A) = -\sum_i p_i \log p_i$$

**Maximally entangled state**: When all Schmidt coefficients are equal, $p_i = 1/d$ for $d = \min(\dim\mathcal{H}_A, \dim\mathcal{H}_B)$:
$$|\Phi^+\rangle = \frac{1}{\sqrt{d}}\sum_{i=1}^d |i_A\rangle|i_B\rangle, \qquad E = \log d$$

**Entanglement ordering by majorization** [Preskill, Ch.2, §2.4.1]: State $|\psi\rangle$ is "more entangled" than $|\phi\rangle$ (in the sense of LOCC convertibility) iff the Schmidt coefficient vector of $|\phi\rangle$ majorizes that of $|\psi\rangle$. This is connected to Nielsen's theorem on LOCC transformations.

---

## References

- **[Nielsen & Chuang]** Nielsen, M. A. & Chuang, I. L. *Quantum Computation and Quantum Information* (Cambridge, 10th anniversary ed., 2010), Ch. 2.5 (pp.109-111)
- Schmidt, *Math. Ann.* 63, 433 (1907)
- **[Preskill, Ch.2]** Preskill, J. *Lecture Notes for Ph219/CS219: Quantum Information and Computation*, Ch.2: "Foundations I: States and Ensembles" (July 2015), §2.4 (Schmidt decomposition, purification, entanglement quantification). PDF: `references/preskill_ch2.pdf`
- Peres, *Quantum Theory: Concepts and Methods*, Ch. 5
