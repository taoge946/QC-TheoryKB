# Key Formulas: Linear Algebra for Quantum Computing

> 量子计算中最重要的15个线性代数公式。所有公式使用 Dirac 记号与标准矩阵记号混合表示。

---

### F1.1: Spectral Decomposition (谱分解)

$$A = \sum_{i} \lambda_i |e_i\rangle\langle e_i|$$

正规算符可以用其特征值 $\lambda_i$ 和对应的正交归一特征向量 $|e_i\rangle$ 完全分解，这是量子力学中可观测量理论的数学基础。

**Source**: [derivations/spectral_decomposition.md] | Nielsen & Chuang, Theorem 2.1

---

### F1.2: Singular Value Decomposition (奇异值分解)

$$A = U \Sigma V^\dagger = \sum_{i=1}^{r} \sigma_i |u_i\rangle\langle v_i|$$

其中 $U, V$ 是酉矩阵，$\Sigma = \mathrm{diag}(\sigma_1, \sigma_2, \ldots, \sigma_r)$，$\sigma_i > 0$ 为奇异值。任意矩阵都可以分解为酉变换和缩放的组合，在量子信息中用于保真度计算和信道分析。

**Source**: [derivations/svd_and_polar_decomposition.md] | Horn & Johnson, Theorem 7.3.5

---

### F1.3: Tensor Product (张量积)

$$|a\rangle \otimes |b\rangle = |a\rangle|b\rangle = |ab\rangle, \quad \text{dim}(V \otimes W) = \dim(V) \cdot \dim(W)$$

**基本性质**:

$$(\alpha|a_1\rangle + \beta|a_2\rangle) \otimes |b\rangle = \alpha|a_1\rangle \otimes |b\rangle + \beta|a_2\rangle \otimes |b\rangle$$

$$(A \otimes B)(C \otimes D) = (AC) \otimes (BD) \quad \text{(Mixed Product Property)}$$

张量积描述复合量子系统的状态空间，$n$ 个量子比特的状态空间为 $(\mathbb{C}^2)^{\otimes n}$，维数为 $2^n$。

**Source**: [derivations/tensor_product_properties.md] | Nielsen & Chuang, Section 2.1.7

---

### F1.4: Partial Trace (偏迹)

$$\mathrm{Tr}_B\big(|a\rangle\langle a'| \otimes |b\rangle\langle b'|\big) = |a\rangle\langle a'| \cdot \mathrm{Tr}(|b\rangle\langle b'|) = |a\rangle\langle a'| \cdot \langle b'|b\rangle$$

偏迹是从复合系统的密度矩阵中提取子系统约化密度矩阵的唯一物理合理操作，满足 $\rho_A = \mathrm{Tr}_B(\rho_{AB})$。

**Source**: [derivations/trace_and_partial_trace.md] | Nielsen & Chuang, Section 2.4.3

---

### F1.5: Matrix Exponential (矩阵指数)

$$e^A = \sum_{n=0}^{\infty} \frac{A^n}{n!} = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots$$

**对角化情况**: 若 $A = PDP^{-1}$，则 $e^A = P\, e^D\, P^{-1}$，其中 $e^D = \mathrm{diag}(e^{d_1}, e^{d_2}, \ldots)$。

矩阵指数是量子力学时间演化算符 $U(t) = e^{-iHt/\hbar}$ 的数学基础，将 Hermitian 的 Hamilton 量映射为酉演化。

**Source**: [derivations/matrix_exponential.md] | Sakurai, Chapter 2

---

### F1.6: Baker-Campbell-Hausdorff Formula (BCH 公式)

$$e^A e^B = e^{A + B + \frac{1}{2}[A,B] + \frac{1}{12}([A,[A,B]] - [B,[A,B]]) + \cdots}$$

**特殊情况**: 若 $[A, B]$ 与 $A, B$ 均对易，则:

$$e^A e^B = e^{A+B+\frac{1}{2}[A,B]}$$

BCH 公式描述了非对易算符指数乘积与指数之和的关系，在量子门分解和 Trotter-Suzuki 近似中至关重要。

**Source**: [derivations/matrix_exponential.md] | Hall, Lie Groups, Lie Algebras, Chapter 5

---

### F1.7: Trace Properties (迹的性质)

**线性性**: $\mathrm{Tr}(\alpha A + \beta B) = \alpha\,\mathrm{Tr}(A) + \beta\,\mathrm{Tr}(B)$

**循环性**: $\mathrm{Tr}(ABC) = \mathrm{Tr}(BCA) = \mathrm{Tr}(CAB)$

**张量积**: $\mathrm{Tr}(A \otimes B) = \mathrm{Tr}(A) \cdot \mathrm{Tr}(B)$

**内积**: $\mathrm{Tr}(A^\dagger B) = \sum_{i,j} A_{ij}^* B_{ij}$ (Hilbert-Schmidt 内积)

迹运算是量子力学中计算期望值 $\langle O \rangle = \mathrm{Tr}(\rho\, O)$ 和概率 $p_i = \mathrm{Tr}(P_i \rho)$ 的核心工具。

**Source**: [derivations/trace_and_partial_trace.md] | Nielsen & Chuang, Section 2.1.9

---

### F1.8: Commutator and Anti-commutator (对易子与反对易子)

$$[A, B] = AB - BA, \qquad \{A, B\} = AB + BA$$

**关键恒等式**:

$$[A, BC] = [A,B]C + B[A,C]$$

$$e^A B e^{-A} = B + [A,B] + \frac{1}{2!}[A,[A,B]] + \cdots \quad \text{(Hadamard Lemma)}$$

对易子刻画量子力学中可观测量的相容性：$[A,B]=0$ 意味着 $A,B$ 可同时对角化（同时精确测量）；$[A,B] \neq 0$ 则导致不确定性关系。

**Source**: [derivations/matrix_exponential.md] | Sakurai, Section 1.4

---

### F1.9: Positive Semidefinite Matrices (半正定矩阵)

$$A \geq 0 \quad \Longleftrightarrow \quad \langle\psi|A|\psi\rangle \geq 0 \quad \forall\, |\psi\rangle$$

**等价条件**:
- $A$ 的所有特征值 $\lambda_i \geq 0$
- 存在矩阵 $B$ 使得 $A = B^\dagger B$
- $A = \sum_i \lambda_i |e_i\rangle\langle e_i|$，$\lambda_i \geq 0$

量子态的密度矩阵必须满足半正定 ($\rho \geq 0$)、Hermitian ($\rho = \rho^\dagger$) 和归一化 ($\mathrm{Tr}(\rho) = 1$) 三个条件。

**Source**: [derivations/spectral_decomposition.md] | Horn & Johnson, Chapter 7

---

### F1.10: Polar Decomposition (极分解)

$$A = U|A|, \qquad |A| = \sqrt{A^\dagger A}$$

其中 $U$ 为酉矩阵（或部分等距），$|A|$ 为半正定矩阵。类比复数 $z = e^{i\theta}|z|$，极分解将任意算符拆为"旋转"和"缩放"两部分。在量子信息中用于 Uhlmann 保真度定理。

**Source**: [derivations/svd_and_polar_decomposition.md] | Nielsen & Chuang, Theorem 2.3

---

### F1.11: Kronecker Product Properties (Kronecker 积性质)

$$(A \otimes B)^{-1} = A^{-1} \otimes B^{-1}$$

$$(A \otimes B)^\dagger = A^\dagger \otimes B^\dagger$$

$$\det(A \otimes B) = (\det A)^n (\det B)^m, \quad A \in \mathbb{C}^{m \times m},\; B \in \mathbb{C}^{n \times n}$$

$$\mathrm{eigenvalues}(A \otimes B) = \{\lambda_i \mu_j\}, \quad \text{where } \lambda_i \in \mathrm{spec}(A),\; \mu_j \in \mathrm{spec}(B)$$

Kronecker 积是张量积在选定基下的矩阵表示，在多比特量子门 (如 CNOT = $|0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes X$) 的构造中不可或缺。

**Source**: [derivations/tensor_product_properties.md] | Horn & Johnson, Section 4.2

---

### F1.12: Vectorization and Operator-State Duality (向量化与算符-态对偶)

$$\mathrm{vec}(|a\rangle\langle b|) = |a\rangle \otimes |b^*\rangle$$

$$\mathrm{vec}(ABC) = (C^T \otimes A)\,\mathrm{vec}(B)$$

**Choi-Jamiolkowski 同构**: 量子信道 $\mathcal{E}$ 与 Choi 矩阵 $J(\mathcal{E}) = \sum_{i,j} |i\rangle\langle j| \otimes \mathcal{E}(|i\rangle\langle j|)$ 一一对应。

向量化将算符映射为向量，建立了量子信道与量子态之间的数学对偶，是研究量子信道性质的重要工具。

**Source**: [derivations/tensor_product_properties.md] | Watrous, *Theory of Quantum Information*, Chapter 2

---

### F1.13: Operator Norm and Trace Norm (算符范数与迹范数)

**算符范数 (Spectral Norm)**:

$$\|A\|_\infty = \max_i \sigma_i(A) = \max_{|\psi\rangle \neq 0} \frac{\|A|\psi\rangle\|}{\||\psi\rangle\|}$$

**迹范数 (Trace Norm / Nuclear Norm)**:

$$\|A\|_1 = \mathrm{Tr}\sqrt{A^\dagger A} = \sum_i \sigma_i(A)$$

**Frobenius 范数**:

$$\|A\|_F = \sqrt{\mathrm{Tr}(A^\dagger A)} = \sqrt{\sum_i \sigma_i^2(A)}$$

迹距离 $D(\rho, \sigma) = \frac{1}{2}\|\rho - \sigma\|_1$ 是量子态区分度的基本度量，保真度 $F(\rho,\sigma)$ 也与之密切相关。

**Source**: [derivations/svd_and_polar_decomposition.md] | Watrous, Chapter 1

---

### F1.14: Direct Sum Decomposition (直和分解)

$$V = V_1 \oplus V_2 \oplus \cdots \oplus V_k, \qquad \dim V = \sum_i \dim V_i$$

**分块对角矩阵**: $A = A_1 \oplus A_2 \oplus \cdots \oplus A_k = \mathrm{diag}(A_1, A_2, \ldots, A_k)$

**性质**: $f(A_1 \oplus A_2) = f(A_1) \oplus f(A_2)$，$\det(A_1 \oplus A_2) = \det(A_1)\det(A_2)$

直和分解描述 Hilbert 空间按不可约子空间的拆分，在量子纠错码的码空间 $\mathcal{H} = \mathcal{H}_{\text{code}} \oplus \mathcal{H}_{\text{code}}^\perp$ 定义中有直接应用。

**Source**: Horn & Johnson, Section 0.9

---

### F1.15: Projection Operators and Completeness (投影算符与完备性)

**投影算符**: $P^2 = P = P^\dagger$

**正交分解**:

$$I = \sum_{i} P_i, \qquad P_i P_j = \delta_{ij} P_i$$

**秩-1 投影**: $P_\psi = |\psi\rangle\langle\psi|$

**完备性关系 (Resolution of Identity)**:

$$\sum_{i=1}^{d} |i\rangle\langle i| = I$$

投影算符是量子测量 (projective measurement) 的数学表示：测量结果 $i$ 对应投影 $P_i$，概率为 $p_i = \mathrm{Tr}(P_i \rho)$，测后态为 $P_i \rho P_i / p_i$。

**Source**: [derivations/spectral_decomposition.md] | Nielsen & Chuang, Section 2.2.5

---

## Quick Reference Table

| # | Formula | 核心用途 |
|---|---------|----------|
| F1.1 | $A = \sum \lambda_i \|e_i\rangle\langle e_i\|$ | 量子可观测量、态的表示 |
| F1.2 | $A = U\Sigma V^\dagger$ | 保真度、信道分析 |
| F1.3 | $\|a\rangle \otimes \|b\rangle$ | 多比特系统 |
| F1.4 | $\mathrm{Tr}_B(\rho_{AB})$ | 约化密度矩阵 |
| F1.5 | $e^A = \sum A^n/n!$ | 时间演化 |
| F1.6 | BCH | 门分解、Trotter 近似 |
| F1.7 | $\mathrm{Tr}(ABC) = \mathrm{Tr}(CAB)$ | 期望值计算 |
| F1.8 | $[A,B]$, $\{A,B\}$ | 相容性、不确定性 |
| F1.9 | $A \geq 0$ | 密度矩阵条件 |
| F1.10 | $A = U\|A\|$ | Uhlmann 定理 |
| F1.11 | $(A \otimes B)(C \otimes D) = AC \otimes BD$ | 多比特门构造 |
| F1.12 | $\mathrm{vec}(ABC)$ | 信道-态对偶 |
| F1.13 | $\\|A\\|_1$, $\\|A\\|_\infty$ | 态区分度 |
| F1.14 | $V = V_1 \oplus V_2$ | 纠错码空间 |
| F1.15 | $\sum P_i = I$ | 量子测量 |
