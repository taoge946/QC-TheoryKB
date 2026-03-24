# Group Theory Key Formulas for Quantum Computing

> 群论是量子纠错的数学语言。Pauli群、Clifford群、辛表示构成了stabilizer formalism的核心框架。

---

### F6.1: Pauli Matrices

$$
I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

Pauli矩阵是所有$2\times 2$ Hermitian酉矩阵的基，满足 $P^2 = I$，$P^\dagger = P$，特征值为$\pm 1$，构成量子信息中最基本的算符集合。

**Source**: [derivations/pauli_group.md] | Nielsen & Chuang Ch. 4

---

### F6.2: Pauli Group on $n$ Qubits $\mathcal{P}_n$

$$
\mathcal{P}_n = \{ \alpha \, \sigma_1 \otimes \sigma_2 \otimes \cdots \otimes \sigma_n \mid \alpha \in \{\pm 1, \pm i\}, \; \sigma_k \in \{I, X, Y, Z\} \}
$$

$n$量子比特Pauli群由所有$n$重Pauli张量积（含相位$\pm 1, \pm i$）构成，是stabilizer码的基础代数结构。

**Source**: [derivations/pauli_group.md] | Gottesman, Ph.D. thesis (1997)

---

### F6.3: Commutation and Anti-commutation Relations

$$
[X, Y] = 2iZ, \quad [Y, Z] = 2iX, \quad [Z, X] = 2iY
$$

$$
\{X, Y\} = 0, \quad \{Y, Z\} = 0, \quad \{Z, X\} = 0
$$

$$
\sigma_j \sigma_k = \delta_{jk} I + i \epsilon_{jkl} \sigma_l \quad (j,k,l \in \{1,2,3\})
$$

不同Pauli矩阵之间严格反对易（$\{A,B\}=AB+BA=0$），同种Pauli矩阵对易。这一性质决定了stabilizer算符之间何时对易、何时不对易。

**Source**: [derivations/pauli_group.md] | Sakurai, Modern Quantum Mechanics

---

### F6.4: Clifford Group Definition

$$
\mathcal{C}_n = \{ U \in U(2^n) \mid U \mathcal{P}_n U^\dagger = \mathcal{P}_n \} / U(1)
$$

Clifford群是Pauli群的normalizer（正规化子）：Clifford门把Pauli算符共轭变换后仍为Pauli算符。这使得Clifford电路对stabilizer态的作用可以用Pauli的变换表高效追踪。

**Source**: [derivations/clifford_group.md] | Gottesman (1998)

---

### F6.5: Clifford Gates Action on Paulis

$$
H: \; X \mapsto Z, \quad Z \mapsto X, \quad Y \mapsto -Y
$$

$$
S: \; X \mapsto Y, \quad Z \mapsto Z, \quad Y \mapsto -X
$$

$$
\text{CNOT}: \; X \otimes I \mapsto X \otimes X, \quad I \otimes X \mapsto I \otimes X, \quad Z \otimes I \mapsto Z \otimes I, \quad I \otimes Z \mapsto Z \otimes Z
$$

三个Clifford生成元 $\{H, S, \text{CNOT}\}$ 对Pauli算符的共轭作用完全决定了它们在stabilizer formalism中的行为。

**Source**: [derivations/clifford_group.md] | Aaronson & Gottesman (2004)

---

### F6.6: Gottesman-Knill Theorem

$$
\text{Clifford circuit} + \text{computational basis input} + \text{Pauli measurement} \implies \text{classically simulable in } O(\text{poly}(n))
$$

Gottesman-Knill定理：仅使用Clifford门（$H, S, \text{CNOT}$）、计算基输入态和Pauli测量的量子电路可以在经典计算机上多项式时间模拟。需要非Clifford门（如$T$门）才能实现量子优越性。

**Source**: [derivations/clifford_group.md] | Gottesman (1998), Aaronson & Gottesman (2004)

---

### F6.7: Symplectic Representation of Pauli Operators

$$
i^c \, X^{a_1}Z^{b_1} \otimes X^{a_2}Z^{b_2} \otimes \cdots \otimes X^{a_n}Z^{b_n} \;\longleftrightarrow\; (\mathbf{a} \mid \mathbf{b}) \in \mathbb{F}_2^{2n}
$$

其中 $\mathbf{a} = (a_1, \ldots, a_n)$，$\mathbf{b} = (b_1, \ldots, b_n)$，$a_i, b_i \in \{0, 1\}$。

每个Pauli算符（忽略相位）映射为$\mathbb{F}_2^{2n}$上的二元向量，将量子纠错问题转化为$\text{GF}(2)$上的线性代数问题。

**Source**: [derivations/symplectic_representation.md] | Calderbank et al. (1997)

---

### F6.8: Symplectic Inner Product and Commutativity

$$
\langle (\mathbf{a} \mid \mathbf{b}), (\mathbf{a}' \mid \mathbf{b}') \rangle_s = \mathbf{a} \cdot \mathbf{b}' + \mathbf{a}' \cdot \mathbf{b} \pmod{2}
$$

$$
[P, Q] = 0 \iff \langle v_P, v_Q \rangle_s = 0
$$

辛内积为零当且仅当对应的Pauli算符对易。Stabilizer群对应辛空间中的各向同性（isotropic）子空间。

**Source**: [derivations/symplectic_representation.md] | Calderbank et al. (1997)

---

### F6.9: Weyl-Heisenberg Group

$$
W(a, b) = (-1)^{a \cdot b} X^{a_1}Z^{b_1} \otimes \cdots \otimes X^{a_n}Z^{b_n}, \quad a, b \in \mathbb{F}_2^n
$$

$$
W(a,b) \, W(a',b') = (-1)^{a' \cdot b} \, W(a \oplus a', b \oplus b')
$$

Weyl-Heisenberg群是Pauli群的另一种参数化形式，使得群乘法直接对应辛内积。在量子信息的许多理论分析中更为方便。

**Source**: [derivations/pauli_group.md] | Appleby (2005)

---

### F6.10: Group Order Formulas

$$
|\mathcal{P}_n| = 4^{n+1}
$$

$$
|\mathcal{C}_n| = 2^{n^2+2n} \prod_{j=0}^{n-1}(4^{j+1} - 1)
$$

$n$量子比特Pauli群有$4^{n+1}$个元素（含相位），Clifford群的阶随$n$指数增长。例如 $|\mathcal{C}_1| = 24$，$|\mathcal{C}_2| = 11520$。

**Source**: [derivations/clifford_group.md] | Nebe, Rains & Sloane (2001)

---

### F6.11: Normalizer and Centralizer

$$
N_G(H) = \{ g \in G \mid gHg^{-1} = H \} \quad \text{(normalizer)}
$$

$$
C_G(H) = \{ g \in G \mid gh = hg, \; \forall h \in H \} \quad \text{(centralizer)}
$$

$$
C_G(H) \subseteq N_G(H) \subseteq G
$$

Normalizer保持子群整体不变（共轭下封闭），centralizer与子群每个元素都对易。Clifford群就是Pauli群在酉群中的normalizer；stabilizer码的logical operators属于stabilizer群的normalizer但不属于stabilizer群本身。

**Source**: [derivations/group_theory_basics.md] | Hungerford, Algebra

---

### F6.12: Coset Decomposition for Logical Operators

$$
N(\mathcal{S}) / \mathcal{S} \cong \text{Logical operator group}
$$

对于 $[[n, k, d]]$ stabilizer码，设 $\mathcal{S}$ 为stabilizer群，$N(\mathcal{S})$ 为 $\mathcal{S}$ 在 $\mathcal{P}_n$ 中的normalizer：

$$
|N(\mathcal{S})| = 4 \cdot 4^{n}, \quad |\mathcal{S}| = 2^{n-k}, \quad |N(\mathcal{S})/\mathcal{S}| = 4^{k+1}
$$

逻辑算符恰好是normalizer中不属于stabilizer的陪集代表元。每个逻辑量子比特对应一对逻辑 $\bar{X}_i, \bar{Z}_i$，它们与stabilizer对易但自身不在stabilizer中。

**Source**: [derivations/symplectic_representation.md] | Gottesman, Ph.D. thesis (1997)

---

### F6.13: Normalizer equals Centralizer for Pauli Group [Gottesman thesis, §3.2]

$$N_{\mathcal{G}}(S) = C_{\mathcal{G}}(S)$$

For any stabilizer subgroup $S$ of the Pauli group $\mathcal{G}$: the normalizer equals the centralizer. This is because for $A \in \mathcal{G}$, $M \in S$: $A^\dagger M A = \pm M$, and since $-1 \notin S$, fixing $S$ under conjugation is equivalent to commuting with every element.

**Source**: [Gottesman thesis, §3.2] | Gottesman (1997)

---

### F6.14: Normalizer Size [Gottesman thesis, §3.2]

$$|N(S)| = 4 \cdot 2^{n+k}$$

For an $[[n,k]]$ stabilizer code with stabilizer $S$ (having $2^{n-k}$ elements), the normalizer $N(S)$ in $\mathcal{G}_n$ contains $4 \cdot 2^{n+k}$ elements. The factor of 4 accounts for global phase.

**Source**: [Gottesman thesis, §3.2] | Gottesman (1997)

---

### F6.15: GF(4) Representation of Stabilizer Codes [Gottesman thesis, §3.4]

$$I \to 0, \quad X \to 1, \quad Z \to \omega, \quad Y \to \omega^2$$

where $\omega^3 = 1$, $1 + \omega = \omega^2$ in GF(4). Two operators commute iff $\text{Tr}\;u \cdot \bar{v} = 0$. A code whose stabilizer is closed under multiplication by $\omega$ is a linear code over GF(4); the most general stabilizer code is an additive code.

**Source**: [Gottesman thesis, §3.4] | Calderbank et al. (1997)

---

### F6.16: Orthogonal Group Condition for Universal Transversal Gates [Gottesman thesis, §5.4]

For an $n$-qubit transversal operation that works for any stabilizer code, the binary matrix describing the automorphism must be in $O(n, \mathbb{Z}_2)$: dot product of any row with itself is 1, dot product of different rows is 0. The smallest $n$ with a non-permutation element is $n = 4$.

**Source**: [Gottesman thesis, §5.4] | Rains (1997)

---

## Quick Reference Table

| Formula | Key Result | 应用 |
|---------|-----------|------|
| F6.1 | Pauli matrices | 基本构建块 |
| F6.2 | $\mathcal{P}_n$ definition | Stabilizer formalism |
| F6.3 | $\{X,Y\}=0$ | 对易性判断 |
| F6.4 | $\mathcal{C}_n = N_{U(2^n)}(\mathcal{P}_n)$ | Clifford门定义 |
| F6.5 | $H,S,\text{CNOT}$ actions | 电路编译 |
| F6.6 | Gottesman-Knill | 经典可模拟性 |
| F6.7 | Pauli $\to (\mathbf{a}\mid\mathbf{b})$ | 辛表示 |
| F6.8 | Symplectic inner product | 对易性$\leftrightarrow$辛正交 |
| F6.9 | Weyl-Heisenberg | 理论分析工具 |
| F6.10 | $\|\mathcal{P}_n\|, \|\mathcal{C}_n\|$ | 群阶计算 |
| F6.11 | $N_G(H), C_G(H)$ | 逻辑算符 |
| F6.12 | $N(\mathcal{S})/\mathcal{S}$ | 码的逻辑空间 |
| F6.13 | $N(S) = C(S)$ for Pauli | Normalizer = Centralizer |
| F6.14 | $|N(S)| = 4 \cdot 2^{n+k}$ | Normalizer大小 |
| F6.15 | GF(4) representation | 经典码联系 |
| F6.16 | $O(n, \mathbb{Z}_2)$ condition | 通用transversal门 |
