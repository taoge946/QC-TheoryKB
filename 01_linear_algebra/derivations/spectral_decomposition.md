# Spectral Decomposition (谱分解定理)

## Metadata
- **Topic**: Linear Algebra
- **Tags**: `spectral`, `eigenvalue`, `diagonalization`, `normal-operator`
- **Prerequisites**: eigenvalues, eigenvectors, Hermitian matrices, unitary matrices
- **Related Formulas**: F1.1, F1.9, F1.15
- **References**: Nielsen & Chuang Section 2.1; Horn & Johnson Chapter 2; Sakurai Chapter 1; **[Slofstra, Ch.10--11]**; **[Watrous, Ch.1, §1.1.3]**

---

## Statement (定理陈述)

**Spectral Theorem for Normal Operators** **[Slofstra, Thm.10.11]** **[Watrous, Ch.1, Thm.1.3]**: 设 $A$ 是有限维复 Hilbert 空间 $\mathcal{H}$ 上的正规算符 (normal operator)，即满足 $A^\dagger A = A A^\dagger$，则 $A$ 可以写成谱分解的形式：

$$A = \sum_{i=1}^{d} \lambda_i |e_i\rangle\langle e_i|$$

其中 $\{\lambda_i\}$ 是 $A$ 的特征值，$\{|e_i\rangle\}$ 是对应的正交归一特征向量，构成 $\mathcal{H}$ 的一组正交归一基。

等价地，存在酉矩阵 $U$ 使得：

$$A = U \Lambda U^\dagger, \qquad \Lambda = \mathrm{diag}(\lambda_1, \lambda_2, \ldots, \lambda_d)$$

---

## Derivation (完整推导)

### Step 1: 正规算符的定义与基本性质

**定义**: 算符 $A$ 称为正规的 (normal)，若 $A^\dagger A = A A^\dagger$。

正规算符包含以下重要子类：
- **Hermitian (自伴)**: $A = A^\dagger$（特征值全为实数）
- **Unitary (酉)**: $A^\dagger A = A A^\dagger = I$（特征值模长为 1）
- **Skew-Hermitian (反自伴)**: $A = -A^\dagger$（特征值纯虚数）

**引理 1**: 若 $A$ 是正规的，则对任意向量 $|v\rangle$，有 $\|A|v\rangle\| = \|A^\dagger|v\rangle\|$。

*证明*:
$$\|A|v\rangle\|^2 = \langle v|A^\dagger A|v\rangle = \langle v|AA^\dagger|v\rangle = \|A^\dagger|v\rangle\|^2$$

其中第二个等号用到了 $A^\dagger A = AA^\dagger$（正规性条件）。$\square$

### Step 2: 正规算符的特征值与特征向量性质

**引理 2**: 正规算符 $A$ 的属于不同特征值的特征向量正交。

*证明*: 设 $A|e_i\rangle = \lambda_i|e_i\rangle$，$A|e_j\rangle = \lambda_j|e_j\rangle$，$\lambda_i \neq \lambda_j$。

首先注意，若 $A|e_i\rangle = \lambda_i|e_i\rangle$，则 $A^\dagger|e_i\rangle = \lambda_i^*|e_i\rangle$。

这是因为由引理 1：

$$\|(A - \lambda_i I)|e_i\rangle\| = \|(A - \lambda_i I)^\dagger|e_i\rangle\| = \|(A^\dagger - \lambda_i^* I)|e_i\rangle\|$$

左边等于 0，因此 $(A^\dagger - \lambda_i^* I)|e_i\rangle = 0$，即 $A^\dagger|e_i\rangle = \lambda_i^*|e_i\rangle$。

现在计算内积：

$$\lambda_i \langle e_j|e_i\rangle = \langle e_j|A|e_i\rangle = \langle A^\dagger e_j|e_i\rangle = (\lambda_j^*)^* \langle e_j|e_i\rangle = \lambda_j \langle e_j|e_i\rangle$$

因此 $(\lambda_i - \lambda_j)\langle e_j|e_i\rangle = 0$。由于 $\lambda_i \neq \lambda_j$，必有 $\langle e_j|e_i\rangle = 0$。$\square$

### Step 3: 正规算符可酉对角化

**定理 (Schur Decomposition)**: 任意方阵 $A$ 都可以写成 $A = UTU^\dagger$，其中 $U$ 为酉矩阵，$T$ 为上三角矩阵。

我们不证明 Schur 分解（它需要用到代数基本定理和归纳法），而是用它来证明谱定理。

**命题**: 若 $A$ 是正规的，$A = UTU^\dagger$ 是其 Schur 分解，则 $T$ 必为对角矩阵。

*证明*: 由 $A = UTU^\dagger$，得 $A^\dagger = UT^\dagger U^\dagger$。

正规性 $AA^\dagger = A^\dagger A$ 意味着：

$$UTU^\dagger \cdot UT^\dagger U^\dagger = UT^\dagger U^\dagger \cdot UTU^\dagger$$

$$UTT^\dagger U^\dagger = UT^\dagger T U^\dagger$$

因此 $TT^\dagger = T^\dagger T$，即 $T$ 也是正规的。

现在证明正规的上三角矩阵必为对角矩阵。设 $T = (t_{ij})$，上三角意味着 $t_{ij} = 0$ 当 $i > j$。

比较 $TT^\dagger$ 和 $T^\dagger T$ 的对角元素：

$(TT^\dagger)_{11} = \sum_{k} |t_{1k}|^2 = |t_{11}|^2 + |t_{12}|^2 + \cdots + |t_{1d}|^2$

$(T^\dagger T)_{11} = \sum_{k} |t_{k1}|^2 = |t_{11}|^2$（因为 $T$ 上三角，$t_{k1} = 0$ 当 $k > 1$）

由 $TT^\dagger = T^\dagger T$，得 $(TT^\dagger)_{11} = (T^\dagger T)_{11}$，故：

$$|t_{12}|^2 + |t_{13}|^2 + \cdots + |t_{1d}|^2 = 0$$

因此 $t_{12} = t_{13} = \cdots = t_{1d} = 0$，即第一行除对角元外全为零。

类似地，对第二行，比较 $(TT^\dagger)_{22}$ 和 $(T^\dagger T)_{22}$：

$(TT^\dagger)_{22} = |t_{22}|^2 + |t_{23}|^2 + \cdots + |t_{2d}|^2$

$(T^\dagger T)_{22} = |t_{12}|^2 + |t_{22}|^2 = |t_{22}|^2$（已知 $t_{12} = 0$）

因此 $t_{23} = t_{24} = \cdots = t_{2d} = 0$。

逐行重复此过程，得到 $T$ 的所有非对角元素为零，即 $T$ 是对角矩阵。$\square$

### Step 4: 组装谱分解

由 Step 3，正规算符 $A$ 可以写成：

$$A = U \Lambda U^\dagger, \qquad \Lambda = \mathrm{diag}(\lambda_1, \lambda_2, \ldots, \lambda_d)$$

设 $U = [|e_1\rangle, |e_2\rangle, \ldots, |e_d\rangle]$，即 $U$ 的列向量为 $|e_i\rangle$。由于 $U$ 是酉矩阵，$\{|e_i\rangle\}$ 构成正交归一基。

展开 $U\Lambda U^\dagger$：

$$A = \sum_{i,j} |e_i\rangle \Lambda_{ij} \langle e_j| = \sum_{i} \lambda_i |e_i\rangle\langle e_i|$$

其中最后一步用到 $\Lambda_{ij} = \lambda_i \delta_{ij}$。这就是谱分解。

验证 $|e_i\rangle$ 确实是特征向量：

$$A|e_i\rangle = \left(\sum_j \lambda_j |e_j\rangle\langle e_j|\right)|e_i\rangle = \sum_j \lambda_j |e_j\rangle \delta_{ji} = \lambda_i |e_i\rangle \quad \checkmark$$

---

## Functional Calculus (函数演算)

谱分解的一个强大推论是函数演算：对任意函数 $f$，可以定义：

$$f(A) = \sum_{i} f(\lambda_i) |e_i\rangle\langle e_i|$$

### 重要特例

**矩阵多项式**: 若 $p(x) = \sum_k c_k x^k$，则

$$p(A) = \sum_i p(\lambda_i) |e_i\rangle\langle e_i|$$

**矩阵指数**:

$$e^A = \sum_i e^{\lambda_i} |e_i\rangle\langle e_i|$$

**矩阵平方根** (对 $A \geq 0$):

$$\sqrt{A} = \sum_i \sqrt{\lambda_i} |e_i\rangle\langle e_i|$$

**矩阵逆** (对可逆 $A$，即 $\lambda_i \neq 0$):

$$A^{-1} = \sum_i \lambda_i^{-1} |e_i\rangle\langle e_i|$$

**矩阵对数** (对 $A > 0$):

$$\ln A = \sum_i \ln(\lambda_i) |e_i\rangle\langle e_i|$$

---

## Applications in Quantum Computing (量子计算中的应用)

### 1. 量子可观测量

量子力学中的可观测量用 Hermitian 算符表示。Hermitian 算符是正规的 ($A = A^\dagger$ 意味着 $A^\dagger A = A^2 = AA^\dagger$)，因此有谱分解：

$$O = \sum_i o_i |o_i\rangle\langle o_i|$$

- 测量结果只能是特征值 $o_i$（实数）
- 在态 $|\psi\rangle$ 上测量得到 $o_i$ 的概率为 $p_i = |\langle o_i|\psi\rangle|^2$
- 期望值 $\langle O \rangle = \langle\psi|O|\psi\rangle = \sum_i o_i |\langle o_i|\psi\rangle|^2$

### 2. 密度矩阵

密度矩阵 $\rho$ 是半正定、Hermitian、迹为 1 的算符。其谱分解：

$$\rho = \sum_i p_i |\phi_i\rangle\langle\phi_i|, \qquad p_i \geq 0, \quad \sum_i p_i = 1$$

给出了混合态的本征分解（ensemble interpretation）。

- **纯态**: 恰好一个 $p_i = 1$，其余为 0，即 $\rho = |\phi\rangle\langle\phi|$
- **最大混合态**: $p_i = 1/d$ 对所有 $i$，即 $\rho = I/d$

纯度 (purity) 可以通过特征值计算：$\mathrm{Tr}(\rho^2) = \sum_i p_i^2$。

### 3. 酉门的谱分解

量子门 $U$ 是酉算符，其特征值 $e^{i\theta_i}$ 在单位圆上：

$$U = \sum_i e^{i\theta_i} |u_i\rangle\langle u_i|$$

这使得我们可以定义 $U$ 的分数幂：

$$U^{1/k} = \sum_i e^{i\theta_i/k} |u_i\rangle\langle u_i|$$

例如，$\sqrt{X}$ 门（$X$ 为 Pauli-X）的构造就用到了这个方法。

### 4. Projective Measurement (投影测量)

谱分解直接给出投影测量的数学结构。对可观测量 $O = \sum_m m\, P_m$（$P_m$ 为投影到特征值 $m$ 的特征空间上的投影算符），测量过程为：

- 概率: $p(m) = \mathrm{Tr}(P_m \rho)$
- 测后态: $\rho_m = P_m \rho P_m / p(m)$
- 完备性: $\sum_m P_m = I$

---

## Generalization: Degenerate Case (简并情况的推广)

当特征值有简并时（即 $\lambda_i$ 的几何重数 $g_i > 1$），谱分解写成投影算符形式：

$$A = \sum_{i=1}^{k} \lambda_i P_i$$

其中 $k$ 为不同特征值的个数，$P_i$ 是投影到特征值 $\lambda_i$ 对应特征空间 $V_i$ 上的正交投影算符：

$$P_i = \sum_{j=1}^{g_i} |e_i^{(j)}\rangle\langle e_i^{(j)}|$$

这里 $\{|e_i^{(j)}\rangle\}_{j=1}^{g_i}$ 是 $V_i$ 的一组正交归一基。

投影算符满足：
- $P_i^2 = P_i$（幂等性）
- $P_i^\dagger = P_i$（自伴性）
- $P_i P_j = \delta_{ij} P_i$（正交性）
- $\sum_i P_i = I$（完备性）

---

## Summary (总结)

谱定理的核心信息：

1. 正规算符 $\Longleftrightarrow$ 可酉对角化 $\Longleftrightarrow$ 有正交归一特征基
2. 谱分解 $A = \sum \lambda_i |e_i\rangle\langle e_i|$ 将算符完全编码为"特征值 + 特征向量"
3. 函数演算 $f(A) = \sum f(\lambda_i)|e_i\rangle\langle e_i|$ 允许对算符施加任意函数
4. Hermitian 算符（可观测量）和酉算符（量子门）都是正规算符的特例

---

## From Linear Algebra for QC Reference

### Operator Inequalities and Positive Semidefiniteness **[LinAlg for QC, §2]**

**Loewner partial order**: 对 Hermitian 算符 $A, B$，定义 $A \geq B$ 当且仅当 $A - B \geq 0$（半正定）。

**性质**：
- $A \geq 0$ 等价于所有特征值 $\lambda_i \geq 0$
- $A \geq 0$ 等价于 $A = B^\dagger B$ 对某个 $B$
- 若 $A \geq B \geq 0$，则 $\text{Tr}(A) \geq \text{Tr}(B) \geq 0$
- 若 $A \geq B \geq 0$ 且 $C \geq 0$，**不一定**有 $AC \geq BC$（矩阵乘法不保持序）
- 但 $A \geq B \geq 0$ 意味着 $C^\dagger AC \geq C^\dagger BC$ 对任意 $C$

**平方根唯一性**：若 $A \geq 0$，存在唯一的 $B \geq 0$ 使得 $B^2 = A$，记为 $B = \sqrt{A} = A^{1/2}$。

$$\sqrt{A} = U\,\text{diag}(\sqrt{\lambda_1}, \ldots, \sqrt{\lambda_n})\,U^\dagger$$

### Spectral Decomposition in Quantum Information Theory **[Slofstra, §3]**

**密度矩阵的谱分解**：任何密度矩阵 $\rho$ 可以唯一地写为其本征分解（特征值可以重复）：

$$\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|, \quad p_i > 0, \quad \sum p_i = 1$$

**不同的系综可以产生相同的密度矩阵**（Hughston-Jozsa-Wootters 定理）：$\{q_j, |\phi_j\rangle\}$ 与 $\{p_i, |\psi_i\rangle\}$ 给出相同 $\rho$ 当且仅当存在酉矩阵 $U_{ji}$ 使得 $\sqrt{q_j}|\phi_j\rangle = \sum_i U_{ji}\sqrt{p_i}|\psi_i\rangle$。

### Operator Norms via Spectral Theory **[LinAlg for QC, §3; Slofstra, §4]**

**Schatten $p$-norms**：对算符 $A$ 的奇异值 $\sigma_1 \geq \sigma_2 \geq \cdots$：

$$\|A\|_p = \left(\sum_i \sigma_i^p\right)^{1/p}$$

- $p = 1$: 迹范数 $\|A\|_1 = \text{Tr}(\sqrt{A^\dagger A}) = \sum_i \sigma_i$
- $p = 2$: Frobenius/Hilbert-Schmidt 范数 $\|A\|_2 = \sqrt{\text{Tr}(A^\dagger A)}$
- $p = \infty$: 算符范数 $\|A\|_\infty = \sigma_{\max}$

**Diamond norm**（量子信道距离的标准度量）：

$$\|\mathcal{E}\|_\diamond = \max_{\rho} \|(\mathcal{E} \otimes \text{id})(\rho)\|_1$$

其中最大化遍历所有二体态 $\rho$。Diamond norm 是比较量子信道的标准度量。

---

---

## Inner Product Spaces and Hilbert Spaces (from Slofstra Ch.3)

### Definition (Sesquilinear and Hermitian Forms) **[Slofstra, Ch.3, Def.3.1.1]**

> Slofstra 原文 (p.30): "A function $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{F}$ is called a sesquilinear form if $\langle su + v, w \rangle = \bar{s}\langle u, w \rangle + \langle v, w \rangle$ and $\langle u, sv + w \rangle = s\langle u, v \rangle + \langle u, w \rangle$."

- **Hermitian form**: $\langle u, v \rangle = \overline{\langle v, u \rangle}$
- **Positive semidefinite form**: $\langle u, u \rangle \geq 0$ for all $u$
- **Inner product (positive definite)**: $\langle u, u \rangle = 0$ iff $u = 0$

### Theorem (Sesquilinear Form ↔ Matrix) **[Slofstra, Ch.3, Thm.3.1.11]**

设 $M$ 是 $n \times n$ 矩阵，$B$ 是 $n$ 维向量空间 $V$ 的基。则 $\langle x, y \rangle := [x]_B^* M [y]_B$ 是 $V$ 上的半线性形式。$M$ 是该形式关于 $B$ 的矩阵，且 $\langle \cdot, \cdot \rangle$ 是 Hermitian / 半正定 / 正定当且仅当 $M$ 是 Hermitian / 半正定 / 正定。

> Slofstra 原文 (p.34): "Going the other way, $\langle v, w \rangle' = \langle c_B^{-1}(v), c_B^{-1}(w) \rangle$, so $\langle \cdot, \cdot \rangle'$ is the pullback of $\langle \cdot, \cdot \rangle$ through $c_B^{-1}$."

### Definition (Hilbert Space) **[Slofstra, Ch.3, Def.3.2.1]**

> Slofstra 原文 (p.36): "A (finite-dimensional) inner product space is a pair $(H, \langle \cdot, \cdot \rangle)$ where $H$ is a (finite-dimensional) $\mathbb{F}$-vector space, $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$, and $\langle \cdot, \cdot \rangle$ is an inner product on $H$. A Hilbert space is another name for an inner product space over $\mathbb{C}$."

**正交归一基的关键性质** (Slofstra, Lemma 3.2.3):

$$x = \sum_{i=1}^n \langle v_i, x \rangle v_i \quad \text{for all } x \in H$$

即坐标向量 $[x]_B$ 的第 $i$ 个分量就是 $\langle v_i, x \rangle$。

### Proposition (Orthonormal Basis ↔ Identity Matrix) **[Slofstra, Ch.3, Prop.3.2.6]**

基 $B$ 是正交归一基 $\iff$ 内积关于 $B$ 的矩阵是 $\mathbb{1}_n$。

---

## Free Vector Spaces and Dirac Notation (from Slofstra Ch.2)

### Definition (Free Vector Space) **[Slofstra, Ch.2, Def.2.2.1]**

> Slofstra 原文 (p.24): "The free vector space spanned by $X$ over $\mathbb{F}$ is the vector space of formal sums $\mathbb{F}X := \{\sum_{x \in X} c_x |x\rangle : c_x \in \mathbb{F}\}$."

$\{|x\rangle : x \in X\}$ 构成 $\mathbb{F}X$ 的基。若 $|X| = n$，则 $\mathbb{F}X \cong \mathbb{F}^n$。

**线性化函数** (Slofstra, Prop.2.2.7): 若 $f: X \to W$ 是任意函数，则存在唯一线性映射 $T: \mathbb{F}X \to W$ 使得 $T|x\rangle = f(x)$。

### Dual Spaces **[Slofstra, Ch.2, §2.3]**

对偶空间 $V^* = \text{Lin}(V, \mathbb{F})$。$\dim V^* = \dim V$。

**Kronecker 对偶基**: 给定 $V$ 的基 $B = \{x_1, \ldots, x_n\}$，存在唯一的 $V^*$ 的基 $\{x^1, \ldots, x^n\}$ 满足 $x^i(x_j) = \delta_{ij}$。

> Slofstra 原文 (p.27): "elements $f \in \mathrm{Lin}(V, \mathbb{F})$ send vectors $v \in V$ to scalars $f(v) \in \mathbb{F}$."

选取基后，$V$ 对应列向量空间 $\mathbb{F}^n$，$V^*$ 对应行向量空间 $M_{1n}\mathbb{F}$，对偶配对 $(f, v) \mapsto f(v)$ 对应矩阵乘法。

---

## Quantum Axioms from Linear Algebra (from Slofstra Ch.1)

### The Six Axioms of Quantum Probability **[Slofstra, Ch.1, §1.4]**

> Slofstra 原文 (p.13): The key axioms needed for quantum information are:

1. **物理系统 ↔ Hilbert 空间**: A physical system corresponds to a Hilbert space $H$.
2. **态 ↔ 单位向量**: The state of a physical system is given by a unit vector $v \in H$.
3. **测量 ↔ 正交归一基**: For every orthonormal basis, there is an associated measurement.
4. **时间演化是线性的**: Time evolution is linear.
5. **投影测量**: For every complete family of orthogonal projections, there is an associated measurement.
6. **复合系统 ↔ 张量积**: The Hilbert space of a joint system is the tensor product $H_1 \otimes H_2$.

---

## Dirac Notation and Computational Basis (from LinAlg for QC)

### Dirac Notation **[Portugal, *Quantum Walks*, Appendix A, §A.3]**

> LinAlg for QC 原文 (p.197): "The Dirac notation uses $v \equiv |v\rangle$... The key to the Dirac notation is to always view kets as column matrices, bras as row matrices, and recognize that a sequence of bras and kets is a matrix product."

- **Ket**: $|v\rangle$ — 列向量
- **Bra**: $\langle v| = |v\rangle^\dagger$ — 行向量（共轭转置）
- **Bra-ket**: $\langle v|w\rangle = v^\dagger w$ — 内积（标量）
- **Ket-bra**: $|v\rangle\langle w|$ — 外积（$n \times n$ 矩阵）

### Computational Basis **[Portugal, Appendix A, §A.4]**

$\{|0\rangle, |1\rangle, \ldots, |n-1\rangle\}$ 是 $\mathbb{C}^n$ 的标准正交基，满足 $\langle i|j\rangle = \delta_{ij}$。

### Qubit and Bloch Sphere **[Portugal, Appendix A, §A.5]**

量子比特：$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$，$|\alpha|^2 + |\beta|^2 = 1$。

消除全局相位后：$|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle$，参数 $0 \leq \theta \leq \pi$，$0 \leq \phi < 2\pi$。

> LinAlg for QC 原文 (p.200): "When we disregard global phase factors, there is a one-to-one correspondence between the quantum states of a qubit and the points on the Bloch sphere."

Bloch 球的特殊点：
- 北极：$|0\rangle$（$\theta = 0$）
- 南极：$|1\rangle$（$\theta = \pi$）
- $x$ 轴交点：$|+\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$, $|-\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$
- $y$ 轴交点：$(|0\rangle \pm i|1\rangle)/\sqrt{2}$

### Rank-Nullity Theorem **[Portugal, Appendix A, §A.6]**

> LinAlg for QC 原文 (p.201): "The rank-nullity theorem states that rank $A$ + nullity $A$ = dim $V$."

---

## Linear Operators and Matrix Representation (from LinAlg for QC)

### Diagonal Representation (Spectral Decomposition) **[Portugal, Appendix A, §A.8]**

> LinAlg for QC 原文 (p.203): "Let $O$ be an operator in $V$. If there exists an orthonormal basis $\{|v_1\rangle, \ldots, |v_n\rangle\}$ of $V$ such that $O = \sum_{i=1}^n \lambda_i |v_i\rangle\langle v_i|$, we say that $O$ admits a diagonal representation."

### Outer Product Representation **[Portugal, Appendix A, §A.7]**

$$A = \sum_{i=1}^m \sum_{j=1}^n a_{ij} |w_i\rangle\langle v_j|$$

> LinAlg for QC 原文 (p.202): "Using the outer product notation, we have $A = \sum_{i,j} a_{ij} |w_i\rangle\langle v_j|$."

---

## Gottesman Thesis: Spectral Theory in QEC Context

> **[Gottesman thesis, §1.2]**: A matrix $A$ has real eigenvalues iff it is Hermitian: $A^\dagger = A$. All Pauli spin matrices are Hermitian. Eigenvectors of a Hermitian operator with different eigenvalues are automatically orthogonal. Two commuting matrices can be simultaneously diagonalized -- this means we can measure the eigenvalue of one without disturbing the eigenvectors of the other. This is the mathematical foundation of the stabilizer measurement framework in quantum error correction.

> **[Roffe, QEC Introductory Guide, §2.2]**: Coherent noise processes are described by matrices that can be expanded in terms of a Pauli basis $\{I, X, Y, Z\}$. The spectral decomposition of unitary error operators into Pauli components is the mathematical mechanism behind the digitisation of quantum errors.

---

## References

- **[LinAlg for QC]** -- Portugal, R. *Quantum Walks and Search Algorithms*, Springer (2013), Appendix A: Linear Algebra for Quantum Computation.
- **[Slofstra]** -- Slofstra, W. *Linear algebra and quantum probability* (v0.8, 2022): Hilbert spaces, inner product spaces, dual spaces, free vector spaces.
- **[Watrous]** -- Watrous, J. *The Theory of Quantum Information*, Cambridge University Press (2018), Chapter 1: Mathematical preliminaries.
- **[Gottesman thesis]** -- Gottesman, D. "Stabilizer Codes and Quantum Error Correction" (1997): spectral theory applied to QEC.
- **[Roffe]** -- Roffe, J. "Quantum Error Correction: An Introductory Guide" (2019): Pauli basis expansion of errors.
- Nielsen & Chuang Section 2.1; Horn & Johnson Chapter 2; Sakurai Chapter 1.
