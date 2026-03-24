# Essential Group Theory for Quantum Computing

> **Tags**: `group`, `subgroup`, `coset`, `normalizer`, `quotient`
>
> **Primary Source**: D. Gottesman, *Stabilizer Codes and Quantum Error Correction*, PhD thesis, Caltech (1997), Ch.3--5
> (`04_quantum_error_correction/references/gottesman_thesis/Thesis.tex`)

## Statement

本文介绍量子纠错论文中频繁出现的群论基本概念：群、子群、陪集、正规子群、商群、normalizer、centralizer等，并以Pauli群为主要例子。所有QEC相关群论结构的系统化处理参见 **[Gottesman 1997, Ch.3]**。

## Prerequisites

- 集合论基础（集合、映射、等价关系）

---

## Derivation

### Step 1: Group — 群的定义

**定义** **[Gottesman 1997, Ch.1, §1.2]**：一个**群** $(G, \cdot)$ 是一个集合 $G$ 配上一个二元运算 $\cdot: G \times G \to G$，满足：

1. **封闭性**（Closure）：$\forall a, b \in G$，$a \cdot b \in G$
2. **结合律**（Associativity）：$\forall a, b, c \in G$，$(a \cdot b) \cdot c = a \cdot (b \cdot c)$
3. **单位元**（Identity）：$\exists e \in G$ 使得 $\forall a \in G$，$e \cdot a = a \cdot e = a$
4. **逆元**（Inverse）：$\forall a \in G$，$\exists a^{-1} \in G$ 使得 $a \cdot a^{-1} = a^{-1} \cdot a = e$

若还满足 $a \cdot b = b \cdot a$（交换律），则称为**阿贝尔群**（Abelian group）。

**QEC中的例子**：

| 群 | 运算 | 是否阿贝尔 |
|---|------|-----------|
| $\mathcal{P}_n$（Pauli群） | 矩阵乘法 | 否（$XZ = -ZX$） |
| $\bar{\mathcal{P}}_n = \mathcal{P}_n/Z(\mathcal{P}_n)$ | 模相位乘法 | 是（$\cong \mathbb{Z}_2^{2n}$） |
| $\mathcal{C}_n$（Clifford群） | 矩阵乘法 | 否 |
| $\text{Sp}(2n, \mathbb{F}_2)$（辛群） | 矩阵乘法 | 否 |
| $(\mathbb{F}_2^{2n}, +)$ | 向量加法 | 是 |
| Stabilizer群 $\mathcal{S}$ | 矩阵乘法 | 是 |

### Step 2: Subgroup — 子群

**定义**：$H \subseteq G$ 是 $G$ 的**子群**（记 $H \leq G$），若 $H$ 在 $G$ 的运算下自身构成群。

**子群判定准则**（一步检验法）：$H \leq G$ 当且仅当 $H \neq \emptyset$ 且 $\forall a, b \in H$，$ab^{-1} \in H$。

**QEC例子**：
- $\mathcal{P}_n \leq \mathcal{C}_n \leq U(2^n)$：Pauli群是Clifford群的子群，Clifford群是酉群的子群
- Stabilizer群 $\mathcal{S} \leq \mathcal{P}_n$：stabilizer是Pauli群的阿贝尔子群
- $Z(\mathcal{P}_n) \leq \mathcal{P}_n$：中心是子群

### Step 3: Lagrange's Theorem — 拉格朗日定理

**定理** **[Gottesman 1997, Ch.3, §3.2 implicitly]**：设 $G$ 是有限群，$H \leq G$，则 $|H|$ 整除 $|G|$。

$$
|G| = [G : H] \cdot |H|
$$

其中 $[G:H] = |G|/|H|$ 称为 $H$ 在 $G$ 中的**指标**（index）。

**证明**：

定义左陪集 $aH = \{ah \mid h \in H\}$。

**Claim 1**：任意两个左陪集要么相等、要么不相交。

证明：设 $aH \cap bH \neq \emptyset$，则存在 $h_1, h_2 \in H$ 使得 $ah_1 = bh_2$。于是 $a = bh_2h_1^{-1} \in bH$。对任意 $ah \in aH$，$ah = bh_2h_1^{-1}h \in bH$，故 $aH \subseteq bH$。对称地 $bH \subseteq aH$，所以 $aH = bH$。

**Claim 2**：$|aH| = |H|$（映射 $h \mapsto ah$ 是双射）。

由Claim 1和2，$G$ 被划分为若干大小相等（$= |H|$）的不相交陪集，因此 $|H|$ 整除 $|G|$。$\blacksquare$

**QEC应用**：

- $|\mathcal{P}_n| = 4^{n+1}$ 整除 $|\mathcal{C}_n|$ $\checkmark$
- stabilizer群 $|\mathcal{S}| = 2^{n-k}$ 整除 $|\mathcal{P}_n| = 4^{n+1}$ $\checkmark$
- Clifford群阶中的 $[\mathcal{C}_n : \mathcal{P}_n] = |\text{Sp}(2n, \mathbb{F}_2)|$

### Step 4: Cosets — 陪集 **[Gottesman 1997, Ch.3, §3.2]**

**定义**：设 $H \leq G$，$a \in G$。

- **左陪集**：$aH = \{ah \mid h \in H\}$
- **右陪集**：$Ha = \{ha \mid h \in H\}$

左陪集的全体记为 $G/H$（左陪集空间），其大小为 $[G:H]$。

**QEC中陪集的关键角色**：

对 $[[n,k,d]]$ stabilizer码，stabilizer群 $\mathcal{S}$ 在 normalizer $N(\mathcal{S})$ 中的陪集代表**逻辑算符**：

$$
N(\mathcal{S}) = \mathcal{S} \cup \bar{X}_1 \mathcal{S} \cup \bar{Z}_1 \mathcal{S} \cup \bar{X}_1\bar{Z}_1 \mathcal{S} \cup \cdots
$$

同一陪集中的元素在码空间上有相同的作用（相差一个stabilizer元素，在码空间上是恒等的）。

**错误的等价性**：两个错误 $E_1, E_2$ 属于 $\mathcal{S}$ 的同一陪集当且仅当 $E_1 E_2^{-1} \in \mathcal{S}$，即它们的差异是一个stabilizer元素——这意味着它们不可区分。decoder只需区分不同的陪集（即syndrome），而非具体错误。

### Step 5: Normal Subgroup — 正规子群 **[Gottesman 1997, Ch.3, §3.2]**

**定义**：$N \leq G$ 是**正规子群**（记 $N \trianglelefteq G$），若对所有 $g \in G$：

$$
gNg^{-1} = N
$$

即 $N$ 在共轭下不变。等价条件：

$$
gN = Ng, \quad \forall g \in G
$$

即左陪集等于右陪集。

**判定方法**：

1. 阿贝尔群的每个子群都是正规子群
2. 群的中心 $Z(G)$ 是正规子群
3. 指标为2的子群是正规子群（因为只有两个陪集，$G = N \cup gN = N \cup Ng$）

**QEC例子**：

- $\mathcal{P}_n \trianglelefteq \mathcal{C}_n$：Pauli群是Clifford群的正规子群（这正是Clifford群的定义——normalizer）
- $Z(\mathcal{P}_n) \trianglelefteq \mathcal{P}_n$：中心是正规子群
- $\mathcal{S} \trianglelefteq N(\mathcal{S})$：stabilizer是其normalizer的正规子群（由normalizer的定义直接得到）

### Step 6: Quotient Group — 商群

**定义**：设 $N \trianglelefteq G$。**商群** $G/N$ 定义为所有 $N$ 的陪集构成的集合，运算为：

$$
(aN)(bN) = (ab)N
$$

**Well-definedness验证**：若 $aN = a'N$ 且 $bN = b'N$，即 $a' = an_1$，$b' = bn_2$，则

$$
a'b' = an_1 bn_2 = ab(b^{-1}n_1 b)n_2 \in abN
$$

最后一步用了 $N \trianglelefteq G$，所以 $b^{-1}n_1 b \in N$。因此 $(a'b')N = (ab)N$。$\checkmark$

**阶**：$|G/N| = [G:N] = |G|/|N|$

**QEC中的商群**：

1. **$\bar{\mathcal{P}}_n = \mathcal{P}_n / Z(\mathcal{P}_n)$**：模去相位的Pauli群，$\cong \mathbb{Z}_2^{2n}$，是辛表示的基础。

2. **$N(\mathcal{S})/\mathcal{S}$**：逻辑算符群。$|N(\mathcal{S})/\mathcal{S}| = 4^{k+1}/2^{n-k} \cdot 2^{n-k}$... 更直接地，$|N(\mathcal{S})/\mathcal{S}| = 2^{2k}$（辛空间中 $V^{\perp_s}/V$ 的大小），每个逻辑qubit贡献一对 $\bar{X}, \bar{Z}$。

3. **$\mathcal{C}_n / \mathcal{P}_n \cong \text{Sp}(2n, \mathbb{F}_2)$**：Clifford群模Pauli群同构于辛群。

### Step 7: Normalizer and Centralizer **[Gottesman 1997, Ch.3, §3.2; Ch.5, §5.3]**

**定义**：设 $H \leq G$。

**Normalizer**（正规化子）：

$$
N_G(H) = \{ g \in G \mid gHg^{-1} = H \}
$$

$N_G(H)$ 是包含 $H$ 的最大子群，使得 $H$ 在其中是正规子群。

**Centralizer**（中心化子）：

$$
C_G(H) = \{ g \in G \mid gh = hg, \; \forall h \in H \}
$$

$C_G(H)$ 是与 $H$ 的每一个元素都对易的元素集合。

**关系**：

$$
C_G(H) \leq N_G(H) \leq G
$$

第一个包含关系：若 $g \in C_G(H)$，则 $ghg^{-1} = h \in H$ 对所有 $h \in H$，故 $gHg^{-1} = H$，即 $g \in N_G(H)$。

**特殊情况**：对于Pauli群中的阿贝尔子群 $\mathcal{S}$，centralizer和normalizer一致：

$$
C_{\mathcal{P}_n}(\mathcal{S}) = N_{\mathcal{P}_n}(\mathcal{S})
$$

原因：对 Pauli 算符 $P$ 和 $g \in \mathcal{S}$，$PgP^{-1} = PgP^\dagger = \pm g$。若 $PgP^\dagger \in \mathcal{S}$，则 $PgP^\dagger = g$ 或 $PgP^\dagger = -g$。但 $-g \in \mathcal{S}$ 仅当 $-I \in \mathcal{S}$，而stabilizer群要求 $-I \notin \mathcal{S}$。所以 $PgP^\dagger = g$，即 $[P, g] = 0$。

**QEC应用**：

| 概念 | QEC中的实例 |
|------|-----------|
| $N_{U(2^n)}(\mathcal{P}_n)$ | Clifford群 $\mathcal{C}_n$ |
| $N_{\mathcal{P}_n}(\mathcal{S})$ | Stabilizer码的逻辑算符群（+stabilizer） |
| $C_{\mathcal{P}_n}(\mathcal{S})$ | 等于 $N_{\mathcal{P}_n}(\mathcal{S})$（对stabilizer码） |
| $Z(G) = C_G(G)$ | $Z(\mathcal{P}_n) = \{\pm 1, \pm i\} \cdot I$ |

### Step 8: First Isomorphism Theorem — 第一同构定理 **[Gottesman 1997, Ch.5, §5.3]**

**定理**：设 $\phi: G \to G'$ 是群同态，则：

$$
G / \ker(\phi) \cong \text{Im}(\phi)
$$

其中 $\ker(\phi) = \{g \in G \mid \phi(g) = e'\}$ 是核，$\text{Im}(\phi) = \{\phi(g) \mid g \in G\}$ 是像。

**证明概要**：

定义映射 $\bar{\phi}: G/\ker(\phi) \to \text{Im}(\phi)$，$\bar{\phi}(g\ker\phi) = \phi(g)$。

1. **Well-defined**：若 $g\ker\phi = g'\ker\phi$，则 $g' = gn$（$n \in \ker\phi$），$\phi(g') = \phi(g)\phi(n) = \phi(g)$。$\checkmark$
2. **同态**：$\bar{\phi}(gN \cdot g'N) = \bar{\phi}(gg'N) = \phi(gg') = \phi(g)\phi(g') = \bar{\phi}(gN)\bar{\phi}(g'N)$。$\checkmark$
3. **单射**：$\bar{\phi}(gN) = e'$ $\Rightarrow$ $\phi(g) = e'$ $\Rightarrow$ $g \in \ker\phi$ $\Rightarrow$ $gN = N$。$\checkmark$
4. **满射**：由 $\text{Im}(\phi)$ 定义显然。$\checkmark$

$\blacksquare$

**QEC应用**：

考虑同态 $\phi: \mathcal{C}_n \to \text{Aut}(\mathcal{P}_n)$，$\phi(U)(P) = UPU^\dagger$。

- $\ker(\phi) = \{U \mid UPU^\dagger = P, \forall P \in \mathcal{P}_n\}$：与所有Pauli对易的酉算符，即 $\mathcal{P}_n$（的中心扩展）
- $\text{Im}(\phi) \cong \text{Sp}(2n, \mathbb{F}_2)$

由第一同构定理：

$$
\mathcal{C}_n / \mathcal{P}_n \cong \text{Sp}(2n, \mathbb{F}_2)
$$

### Step 9: Direct Product — 直积

**定义**：群 $G$ 和 $H$ 的**直积** $G \times H$ 是集合 $\{(g, h) \mid g \in G, h \in H\}$ 上定义运算：

$$
(g_1, h_1)(g_2, h_2) = (g_1 g_2, h_1 h_2)
$$

**性质**：$|G \times H| = |G| \cdot |H|$

**QEC例子**：

非纠缠的stabilizer码可以写成直积形式。例如，$n$个独立量子比特的stabilizer群：

$$
\mathcal{S} = \langle Z_1 \rangle \times \langle Z_2 \rangle \times \cdots \times \langle Z_n \rangle \cong \mathbb{Z}_2^n
$$

商群的直积分解：

$$
\bar{\mathcal{P}}_n \cong \mathbb{Z}_2^{2n} = \mathbb{Z}_2^2 \times \mathbb{Z}_2^2 \times \cdots \times \mathbb{Z}_2^2
$$

每个 $\mathbb{Z}_2^2$ 因子对应一个量子比特的$X, Z$自由度。

### Step 10: Semi-direct Product — 半直积

**定义**：设 $N \trianglelefteq G$，$H \leq G$，$N \cap H = \{e\}$，$NH = G$。则 $G$ 是 $N$ 和 $H$ 的（内部）**半直积**：

$$
G = N \rtimes H
$$

等价地，存在同态 $\phi: H \to \text{Aut}(N)$，使得 $G$ 中的乘法为：

$$
(n_1, h_1)(n_2, h_2) = (n_1 \phi(h_1)(n_2), h_1 h_2)
$$

与直积的区别：直积中 $N$ 和 $H$ 互相对易（$\phi$ 是平凡同态），半直积中 $H$ 通过 $\phi$ 对 $N$ 有非平凡的作用。

**QEC中的半直积结构**：

Clifford群可以（非精确地）理解为Pauli群和辛群的半直积：

$$
\mathcal{C}_n \sim \mathcal{P}_n \rtimes \text{Sp}(2n, \mathbb{F}_2)
$$

其中辛群通过共轭作用（即辛变换）对Pauli群产生非平凡的自同构。

（严格来说，由于相位问题，这里有中心扩张的微妙之处，但作为直觉理解是正确的。）

### Step 11: Group Actions — 群作用

**定义**：群 $G$ 对集合 $X$ 的（左）**作用**是映射 $G \times X \to X$，$(g, x) \mapsto g \cdot x$，满足：

1. $e \cdot x = x$
2. $(gh) \cdot x = g \cdot (h \cdot x)$

**轨道**：$\text{Orb}(x) = \{g \cdot x \mid g \in G\}$

**稳定子群**：$\text{Stab}(x) = \{g \in G \mid g \cdot x = x\}$

**轨道-稳定子定理**：$|G| = |\text{Orb}(x)| \cdot |\text{Stab}(x)|$

**QEC中的群作用**：

1. **Clifford群对Pauli群的共轭作用**：$\mathcal{C}_n$ 作用在 $\mathcal{P}_n$ 上，$U \cdot P = UPU^\dagger$。

2. **Pauli群对码空间的作用**：stabilizer $\mathcal{S}$ 中的每个元素把码空间映射到自身（$g|\psi\rangle = |\psi\rangle$ 对码字 $|\psi\rangle$）。

3. **对称群对物理qubit的排列作用**：码的自同构群（automorphism group）是保持码不变的qubit排列。

---

## Key Insight

量子纠错论文中反复出现的群论模式可以归纳为一个核心链条：

$$
\mathcal{S} \;\trianglelefteq\; N(\mathcal{S}) \;\subseteq\; \mathcal{P}_n \;\trianglelefteq\; \mathcal{C}_n
$$

- **Stabilizer $\mathcal{S}$**：定义码空间的阿贝尔子群
- **Normalizer $N(\mathcal{S})$**：stabilizer + 逻辑算符
- **陪集 $N(\mathcal{S})/\mathcal{S}$**：逻辑算符群（码的逻辑自由度）
- **Pauli $\mathcal{P}_n$**：所有可能的错误
- **Clifford $\mathcal{C}_n$**：所有保Pauli的变换（纠错操作、编码电路）

理解了这条链和相关的商群、陪集结构，就掌握了阅读QEC论文所需的绝大部分群论工具。

---

## Summary

| 概念 | 定义 | QEC实例 |
|------|------|---------|
| 群 | 封闭+结合+单位元+逆元 | $\mathcal{P}_n, \mathcal{C}_n$ |
| 子群 | 对运算封闭的子集 | $\mathcal{S} \leq \mathcal{P}_n$ |
| 正规子群 | 对共轭不变 | $\mathcal{P}_n \trianglelefteq \mathcal{C}_n$ |
| 陪集 | $aH = \{ah \mid h \in H\}$ | 逻辑算符 = normalizer的陪集 |
| 商群 | $G/N$，陪集上的群 | $\mathcal{C}_n/\mathcal{P}_n \cong \text{Sp}(2n,\mathbb{F}_2)$ |
| Normalizer | $\{g \mid gHg^{-1}=H\}$ | Clifford群, 逻辑算符 |
| Centralizer | $\{g \mid [g,h]=0, \forall h\}$ | 对Pauli子群=Normalizer |
| Lagrange | $\|H\|$ 整除 $\|G\|$ | 码参数约束 |
| 第一同构定理 | $G/\ker\phi \cong \text{Im}\phi$ | $\mathcal{C}_n/\mathcal{P}_n\cong\text{Sp}$ |
| 直积 | $G \times H$ | 独立码的组合 |
| 半直积 | $N \rtimes H$ | $\mathcal{C}_n \sim \mathcal{P}_n \rtimes \text{Sp}$ |
