# Tensor Product Properties (张量积性质)

## Metadata
- **Topic**: Linear Algebra
- **Tags**: `tensor-product`, `kronecker`, `partial-trace`, `multi-qubit`
- **Prerequisites**: vector spaces, linear maps, inner product spaces
- **Related Formulas**: F1.3, F1.4, F1.11, F1.12
- **References**: Nielsen & Chuang Section 2.1.7-2.1.8; **[Watrous, Ch.1, §1.1]**; Preskill Lecture Notes Chapter 2; **[Slofstra, Ch.7--9]**

---

## Statement (定理陈述)

张量积 (tensor product) 提供了从两个（或多个）向量空间构造更大向量空间的标准方法。在量子计算中，复合量子系统的状态空间由子系统状态空间的张量积给出。

**核心定理** **[Slofstra, Ch.8, Thm.8.7]** **[Watrous, Ch.1, §1.1.1]**: 设 $V$ 和 $W$ 分别是维数为 $m$ 和 $n$ 的复向量空间，则:
1. 存在维数为 $mn$ 的向量空间 $V \otimes W$ 及双线性映射 $\otimes: V \times W \to V \otimes W$
2. 若 $\{|v_i\rangle\}_{i=1}^m$ 和 $\{|w_j\rangle\}_{j=1}^n$ 分别是 $V$ 和 $W$ 的基，则 $\{|v_i\rangle \otimes |w_j\rangle\}$ 是 $V \otimes W$ 的基
3. (Mixed Product Property) $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$

---

## Derivation (完整推导)

### Step 1: 张量积的定义

**代数定义**: 给定向量空间 $V$ 和 $W$，张量积 $V \otimes W$ 是由形式符号 $\{|v\rangle \otimes |w\rangle : |v\rangle \in V, |w\rangle \in W\}$ 生成的向量空间，模去以下等价关系（双线性性）：

$$(\alpha|v_1\rangle + \beta|v_2\rangle) \otimes |w\rangle = \alpha(|v_1\rangle \otimes |w\rangle) + \beta(|v_2\rangle \otimes |w\rangle)$$

$$|v\rangle \otimes (\alpha|w_1\rangle + \beta|w_2\rangle) = \alpha(|v\rangle \otimes |w_1\rangle) + \beta(|v\rangle \otimes |w_2\rangle)$$

形如 $|v\rangle \otimes |w\rangle$ 的元素称为**可分 (separable / product)** 向量。$V \otimes W$ 中的一般元素是可分向量的线性组合：

$$|\Psi\rangle = \sum_{k} c_k |v_k\rangle \otimes |w_k\rangle$$

不能写成单个张量积形式的向量称为**纠缠 (entangled)** 向量。

### Step 2: 基的构造与维数公式

**命题**: 若 $\{|v_i\rangle\}_{i=1}^m$ 是 $V$ 的基，$\{|w_j\rangle\}_{j=1}^n$ 是 $W$ 的基，则

$$\mathcal{B} = \{|v_i\rangle \otimes |w_j\rangle : 1 \leq i \leq m, \; 1 \leq j \leq n\}$$

是 $V \otimes W$ 的基。

*证明 (线性无关性)*: 假设 $\sum_{i,j} c_{ij} (|v_i\rangle \otimes |w_j\rangle) = 0$。

对任意 $|v_k^*\rangle \in V^*$ 和 $|w_l^*\rangle \in W^*$（对偶基），作用双线性泛函：

$$\sum_{i,j} c_{ij} \langle v_k^*|v_i\rangle \langle w_l^*|w_j\rangle = \sum_{i,j} c_{ij} \delta_{ki} \delta_{lj} = c_{kl} = 0$$

因此所有 $c_{kl} = 0$，$\mathcal{B}$ 线性无关。

*证明 (张成性)*: $V \otimes W$ 中任意元素 $\sum_k c_k |v^{(k)}\rangle \otimes |w^{(k)}\rangle$ 可以展开：

$$|v^{(k)}\rangle = \sum_i \alpha_i^{(k)} |v_i\rangle, \qquad |w^{(k)}\rangle = \sum_j \beta_j^{(k)} |w_j\rangle$$

代入并利用双线性性：

$$\sum_k c_k |v^{(k)}\rangle \otimes |w^{(k)}\rangle = \sum_k c_k \sum_{i,j} \alpha_i^{(k)} \beta_j^{(k)} (|v_i\rangle \otimes |w_j\rangle) = \sum_{i,j} \left(\sum_k c_k \alpha_i^{(k)} \beta_j^{(k)}\right) |v_i\rangle \otimes |w_j\rangle$$

因此 $\mathcal{B}$ 张成 $V \otimes W$。

**推论**: $\dim(V \otimes W) = mn$。

对于量子比特：$\dim((\mathbb{C}^2)^{\otimes n}) = 2^n$。这解释了量子计算的指数复杂性来源。

### Step 3: 张量积上的内积

若 $V$ 和 $W$ 都是内积空间，则 $V \otimes W$ 上的内积由以下规则唯一确定：

$$\langle v_1 \otimes w_1 | v_2 \otimes w_2 \rangle = \langle v_1|v_2\rangle \cdot \langle w_1|w_2\rangle$$

然后通过线性扩展到一般元素：

$$\left\langle \sum_i a_i |v_i\rangle \otimes |w_i\rangle \;\middle|\; \sum_j b_j |v_j'\rangle \otimes |w_j'\rangle \right\rangle = \sum_{i,j} a_i^* b_j \langle v_i|v_j'\rangle \langle w_i|w_j'\rangle$$

**验证**: 若 $\{|v_i\rangle\}$ 和 $\{|w_j\rangle\}$ 分别是 $V$ 和 $W$ 的正交归一基，则 $\{|v_i\rangle \otimes |w_j\rangle\}$ 是 $V \otimes W$ 的正交归一基：

$$\langle v_i \otimes w_j | v_k \otimes w_l \rangle = \langle v_i|v_k\rangle \langle w_j|w_l\rangle = \delta_{ik}\delta_{jl} \quad \checkmark$$

### Step 4: 算符的张量积与 Mixed Product Property

**定义**: 给定线性算符 $A: V \to V'$ 和 $B: W \to W'$，定义 $A \otimes B: V \otimes W \to V' \otimes W'$ 为：

$$(A \otimes B)(|v\rangle \otimes |w\rangle) = (A|v\rangle) \otimes (B|w\rangle)$$

然后线性扩展到一般元素。

**Mixed Product Property (混合积性质)**:

$$(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$$

*证明*: 对任意 $|v\rangle \otimes |w\rangle$：

$$\big[(A \otimes B)(C \otimes D)\big](|v\rangle \otimes |w\rangle) = (A \otimes B)\big[(C|v\rangle) \otimes (D|w\rangle)\big]$$

$$= (AC|v\rangle) \otimes (BD|w\rangle) = \big[(AC) \otimes (BD)\big](|v\rangle \otimes |w\rangle)$$

由于对所有基向量 $|v\rangle \otimes |w\rangle$ 成立，对一般元素也成立。$\square$

**推论 1**: $(A \otimes B)^{-1} = A^{-1} \otimes B^{-1}$（若逆存在）

*证明*: $(A \otimes B)(A^{-1} \otimes B^{-1}) = (AA^{-1}) \otimes (BB^{-1}) = I_V \otimes I_W = I_{V \otimes W}$ $\square$

**推论 2**: $(A \otimes B)^\dagger = A^\dagger \otimes B^\dagger$

*证明*: 对任意 $|v_1\rangle \otimes |w_1\rangle$ 和 $|v_2\rangle \otimes |w_2\rangle$：

$$\langle v_1 \otimes w_1 | (A \otimes B) | v_2 \otimes w_2 \rangle = \langle v_1|A|v_2\rangle \langle w_1|B|w_2\rangle$$

$$= \langle A^\dagger v_1|v_2\rangle \langle B^\dagger w_1|w_2\rangle = \langle (A^\dagger \otimes B^\dagger)(v_1 \otimes w_1) | v_2 \otimes w_2\rangle$$

因此 $(A \otimes B)^\dagger = A^\dagger \otimes B^\dagger$。$\square$

### Step 5: Kronecker 积（矩阵表示）

在选定基下，张量积的矩阵表示就是 Kronecker 积。若 $A$ 是 $m \times m$ 矩阵，$B$ 是 $n \times n$ 矩阵：

$$A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B & \cdots & a_{1m}B \\ a_{21}B & a_{22}B & \cdots & a_{2m}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mm}B \end{pmatrix}$$

结果是 $mn \times mn$ 矩阵。

**Kronecker 积的额外性质**:

$$\mathrm{Tr}(A \otimes B) = \mathrm{Tr}(A) \cdot \mathrm{Tr}(B)$$

*证明*:

$$\mathrm{Tr}(A \otimes B) = \sum_{i,j} (A \otimes B)_{(i,j),(i,j)} = \sum_{i,j} a_{ii} b_{jj} = \left(\sum_i a_{ii}\right)\left(\sum_j b_{jj}\right) = \mathrm{Tr}(A) \cdot \mathrm{Tr}(B) \quad \square$$

$$\det(A \otimes B) = (\det A)^n \cdot (\det B)^m$$

$$\mathrm{eigenvalues}(A \otimes B) = \{\lambda_i(A) \cdot \mu_j(B) : \forall\, i, j\}$$

*证明*: 若 $A|v_i\rangle = \lambda_i|v_i\rangle$，$B|w_j\rangle = \mu_j|w_j\rangle$，则

$$(A \otimes B)(|v_i\rangle \otimes |w_j\rangle) = \lambda_i|v_i\rangle \otimes \mu_j|w_j\rangle = \lambda_i\mu_j (|v_i\rangle \otimes |w_j\rangle) \quad \square$$

### Step 6: 偏迹的推导

**定义**: 设 $\rho_{AB}$ 是复合系统 $\mathcal{H}_A \otimes \mathcal{H}_B$ 上的算符。系统 $A$ 的约化密度矩阵定义为对系统 $B$ 取偏迹：

$$\rho_A = \mathrm{Tr}_B(\rho_{AB})$$

偏迹 $\mathrm{Tr}_B$ 是唯一满足以下条件的线性映射 $\mathrm{Tr}_B: \mathcal{L}(\mathcal{H}_A \otimes \mathcal{H}_B) \to \mathcal{L}(\mathcal{H}_A)$：

$$\mathrm{Tr}_B(X \otimes Y) = X \cdot \mathrm{Tr}(Y)$$

**对可分算符的计算**:

$$\mathrm{Tr}_B(|a\rangle\langle a'| \otimes |b\rangle\langle b'|) = |a\rangle\langle a'| \cdot \mathrm{Tr}(|b\rangle\langle b'|) = |a\rangle\langle a'| \cdot \langle b'|b\rangle$$

**对一般算符的计算**: 选取 $\mathcal{H}_B$ 的正交归一基 $\{|b_k\rangle\}$：

$$\mathrm{Tr}_B(\rho_{AB}) = \sum_k (I_A \otimes \langle b_k|) \rho_{AB} (I_A \otimes |b_k\rangle)$$

*证明*: 设 $\rho_{AB} = \sum_{i,j,k,l} \rho_{ij,kl} |a_i\rangle\langle a_j| \otimes |b_k\rangle\langle b_l|$。

$$\mathrm{Tr}_B(\rho_{AB}) = \sum_{i,j,k,l} \rho_{ij,kl} |a_i\rangle\langle a_j| \cdot \mathrm{Tr}(|b_k\rangle\langle b_l|)$$

$$= \sum_{i,j,k,l} \rho_{ij,kl} |a_i\rangle\langle a_j| \cdot \langle b_l|b_k\rangle = \sum_{i,j,k} \rho_{ij,kk} |a_i\rangle\langle a_j|$$

另一方面：

$$\sum_m (I_A \otimes \langle b_m|) \rho_{AB} (I_A \otimes |b_m\rangle) = \sum_m \sum_{i,j,k,l} \rho_{ij,kl} |a_i\rangle\langle a_j| \cdot \langle b_m|b_k\rangle\langle b_l|b_m\rangle$$

$$= \sum_m \sum_{i,j} \rho_{ij,mm} |a_i\rangle\langle a_j| = \sum_{i,j,k} \rho_{ij,kk} |a_i\rangle\langle a_j| \quad \checkmark \quad \square$$

### Step 7: Schmidt 分解

**定理 (Schmidt Decomposition)**: 对于双体纯态 $|\Psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$，存在正交归一集 $\{|a_i\rangle\} \subset \mathcal{H}_A$，$\{|b_i\rangle\} \subset \mathcal{H}_B$，和非负实数 $\{\lambda_i\}$ 使得：

$$|\Psi\rangle = \sum_{i=1}^{r} \lambda_i |a_i\rangle \otimes |b_i\rangle, \qquad \sum_i \lambda_i^2 = 1$$

其中 $r \leq \min(\dim \mathcal{H}_A, \dim \mathcal{H}_B)$ 称为 Schmidt 秩。

*推导*: 将 $|\Psi\rangle$ 展开为：

$$|\Psi\rangle = \sum_{i,j} c_{ij} |v_i\rangle \otimes |w_j\rangle$$

系数 $c_{ij}$ 构成矩阵 $C$。对 $C$ 做 SVD：$C = U\Sigma V^\dagger$，即 $c_{ij} = \sum_k U_{ik} \sigma_k (V^\dagger)_{kj}$。

代入：

$$|\Psi\rangle = \sum_{i,j,k} U_{ik} \sigma_k V_{jk}^* |v_i\rangle \otimes |w_j\rangle = \sum_k \sigma_k \left(\sum_i U_{ik}|v_i\rangle\right) \otimes \left(\sum_j V_{jk}^*|w_j\rangle\right)$$

定义 $|a_k\rangle = \sum_i U_{ik}|v_i\rangle$ 和 $|b_k\rangle = \sum_j V_{jk}^*|w_j\rangle$。由于 $U$ 和 $V$ 是酉矩阵，$\{|a_k\rangle\}$ 和 $\{|b_k\rangle\}$ 分别是正交归一的。令 $\lambda_k = \sigma_k$，即得 Schmidt 分解。

**Schmidt 分解与纠缠的关系**:
- $r = 1$: 可分态 $|\Psi\rangle = |a\rangle \otimes |b\rangle$，无纠缠
- $r > 1$: 纠缠态，$r$ 越大纠缠越强
- $r = \min(d_A, d_B)$ 且 $\lambda_i$ 均相等: 最大纠缠态

**Schmidt 系数与约化密度矩阵**:

$$\rho_A = \mathrm{Tr}_B(|\Psi\rangle\langle\Psi|) = \sum_i \lambda_i^2 |a_i\rangle\langle a_i|$$

因此 Schmidt 系数的平方就是约化密度矩阵的特征值。

### Step 8: 计算基下的多量子比特系统

对于 $n$ 个量子比特系统，计算基为：

$$|x_1 x_2 \cdots x_n\rangle = |x_1\rangle \otimes |x_2\rangle \otimes \cdots \otimes |x_n\rangle, \qquad x_i \in \{0, 1\}$$

共 $2^n$ 个基态。一般态为：

$$|\Psi\rangle = \sum_{x \in \{0,1\}^n} c_x |x\rangle, \qquad \sum_x |c_x|^2 = 1$$

**The Pauli Group as a Tensor Product Structure** **[Gottesman thesis, §1.2, §2.3]**:

> **[Gottesman thesis, §2.3]**: The set of all tensor products of $\sigma_x$, $\sigma_y$, $\sigma_z$, and $I$ (with a possible overall factor of $\pm 1$ or $\pm i$) forms a group $\mathcal{G}_n$ under multiplication. $\mathcal{G}_1$ is the quaternionic group; $\mathcal{G}_n$ is the direct product of $n$ copies of the quaternions modulo all but a global phase factor. Every element in $\mathcal{G}$ squares to $\pm 1$. Any two elements of $\mathcal{G}$ either commute or anticommute.

This tensor product structure is the mathematical foundation of the stabilizer formalism for quantum error correction. The mixed product property $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$ is what makes Pauli group multiplication efficient: each tensor factor is multiplied independently.

**多比特量子门的张量积表示**:

局部门 $U_i$ 作用在第 $i$ 个比特上：

$$U_i^{(\text{full})} = I^{\otimes(i-1)} \otimes U_i \otimes I^{\otimes(n-i)}$$

两比特门的例子——CNOT 门 (control: qubit 1, target: qubit 2)：

$$\mathrm{CNOT} = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes X = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

### Step 9: Vectorization 与算符-态对偶

**Vectorization (向量化)**: 将 $m \times n$ 矩阵 $A$ 映射为 $mn$ 维向量：

$$\mathrm{vec}(A) = \sum_{i,j} A_{ij} |i\rangle \otimes |j\rangle$$

等价地，对外积 $|a\rangle\langle b|$：

$$\mathrm{vec}(|a\rangle\langle b|) = |a\rangle \otimes |b^*\rangle$$

其中 $|b^*\rangle$ 是 $|b\rangle$ 的复共轭（在计算基下取复共轭）。

**关键性质**:

$$\mathrm{vec}(ABC) = (C^T \otimes A)\,\mathrm{vec}(B)$$

*证明*: 设 $B = \sum_{k,l} B_{kl} |k\rangle\langle l|$，则 $\mathrm{vec}(B) = \sum_{k,l} B_{kl} |k\rangle \otimes |l\rangle$。

$$ABC = \sum_{k,l} B_{kl} A|k\rangle\langle l|C^\dagger{}^\dagger = \sum_{k,l} B_{kl} (A|k\rangle)(\langle l|C^\dagger)^\dagger$$

$$\mathrm{vec}(ABC) = \sum_{k,l} B_{kl} (A|k\rangle) \otimes (C^T|l^*\rangle)^* $$

更直接地，利用分量计算：

$$(ABC)_{ij} = \sum_{k,l} A_{ik} B_{kl} C_{lj}^{\phantom{\dagger}} = \sum_{k,l} A_{ik} C_{jl}^T B_{kl}$$

$$\mathrm{vec}(ABC)_{(i,j)} = \sum_{k,l} (C^T)_{jl} A_{ik} \cdot B_{kl} = \sum_{k,l} (C^T \otimes A)_{(i,j),(k,l)} \cdot \mathrm{vec}(B)_{(k,l)} \quad \square$$

**Choi-Jamiolkowski 同构**: 量子信道 $\mathcal{E}: \mathcal{L}(\mathcal{H}_A) \to \mathcal{L}(\mathcal{H}_B)$ 与 Choi 矩阵 $J(\mathcal{E}) \in \mathcal{L}(\mathcal{H}_B \otimes \mathcal{H}_A)$ 一一对应：

$$J(\mathcal{E}) = \sum_{i,j} |i\rangle\langle j| \otimes \mathcal{E}(|i\rangle\langle j|) = (I \otimes \mathcal{E})(|\Omega\rangle\langle\Omega|)$$

其中 $|\Omega\rangle = \sum_i |i\rangle \otimes |i\rangle$ 是非归一化最大纠缠态。

$\mathcal{E}$ 是 CPTP (completely positive, trace-preserving) 当且仅当 $J(\mathcal{E}) \geq 0$ 且 $\mathrm{Tr}_B(J(\mathcal{E})) = I_A$。

---

## Summary (总结)

1. 张量积是复合量子系统的数学基础，$\dim(V \otimes W) = \dim V \cdot \dim W$
2. Mixed product property $(A \otimes B)(C \otimes D) = AC \otimes BD$ 是多比特计算的关键
3. 偏迹 $\mathrm{Tr}_B(X \otimes Y) = X \cdot \mathrm{Tr}(Y)$ 用于提取子系统信息
4. Schmidt 分解连接了 SVD、偏迹和纠缠度量
5. 向量化 $\mathrm{vec}(ABC) = (C^T \otimes A)\mathrm{vec}(B)$ 建立了算符与态的对偶
6. Choi-Jamiolkowski 同构将量子信道理论转化为半正定矩阵理论

---

## From Linear Algebra References

### Entanglement Detection via Partial Transpose **[Slofstra, §5]**

**PPT (Positive Partial Transpose) 准则**：定义对系统 $B$ 的部分转置：

$$(|i\rangle\langle j| \otimes |k\rangle\langle l|)^{T_B} = |i\rangle\langle j| \otimes |l\rangle\langle k|$$

若 $\rho_{AB}$ 是可分态（$\rho = \sum_i p_i \rho_A^i \otimes \rho_B^i$），则 $\rho^{T_B} \geq 0$（半正定）。

因此 $\rho^{T_B}$ 有负特征值意味着 $\rho$ 是纠缠态。对 $2 \times 2$ 和 $2 \times 3$ 系统，PPT 是充要条件（Peres-Horodecki 判据）。

### Operator-Sum Representation and Kraus Theorem **[LinAlg for QC, §4; Slofstra, §6]**

**定理**：$\mathcal{E}: \mathcal{L}(\mathcal{H}_A) \to \mathcal{L}(\mathcal{H}_B)$ 是 CPTP 映射当且仅当存在一组 Kraus 算子 $\{K_i\}$ 使得：

$$\mathcal{E}(\rho) = \sum_i K_i \rho K_i^\dagger, \qquad \sum_i K_i^\dagger K_i = I_A$$

Kraus 表示不唯一：$\{K_i\}$ 和 $\{K_j'\}$ 给出同一个信道当且仅当存在酉矩阵 $U_{ij}$ 使得 $K_j' = \sum_i U_{ji} K_i$。

**Stinespring dilation**：任何 CPTP 映射可以写成酉演化 + 偏迹：

$$\mathcal{E}(\rho) = \text{Tr}_E(V\rho V^\dagger)$$

其中 $V: \mathcal{H}_A \to \mathcal{H}_B \otimes \mathcal{H}_E$ 是等距映射（$V^\dagger V = I_A$）。

**Choi 矩阵与 Kraus 算子的关系**：若 $J(\mathcal{E}) = \sum_i \sigma_i |u_i\rangle\langle u_i|$ 是 Choi 矩阵的谱分解，则 $K_i = \sqrt{\sigma_i} \cdot \text{unvec}(|u_i\rangle)$ 是一组 Kraus 算子。

### Tensor Network Notation **[LinAlg for QC, §5]**

张量积的图形化表示（tensor network diagrams）：

- **张量**：用节点（方块或圆）表示
- **指标（index）**：用从节点伸出的线段（leg）表示
- **收缩（contraction）**：连接两个节点的线段表示对该指标求和

常用张量网络：
- **MPS (Matrix Product State)**：一维链状结构，$|\psi\rangle = \sum_{i_1\ldots i_n} \text{Tr}(A^{[1]}_{i_1} \cdots A^{[n]}_{i_n}) |i_1\ldots i_n\rangle$
- **PEPS (Projected Entangled Pair State)**：二维网格结构
- **MERA (Multiscale Entanglement Renormalization Ansatz)**：层次树状结构

在 QEC 中，tensor network 解码器利用这种表示来近似计算 syndrome 的后验概率分布。

---

## Abstract Tensor Products (from Slofstra Ch.7-8)

### Concrete vs Abstract Tensor Products **[Slofstra, Ch.7-8]**

> Slofstra 原文 (Ch.7, p.65): "Putting two quantum systems together" motivates the tensor product construction.

**Concrete (Kronecker) product**: 给定向量 $u \in \mathbb{F}^m$, $v \in \mathbb{F}^n$，定义 $u \otimes v \in \mathbb{F}^{mn}$ 为分量 $(u \otimes v)(i,j) = u(i) v(j)$。

**Abstract construction** (Slofstra, Ch.8, §8.2): 构造 $V \otimes W$ 为 $\mathbb{F}(V \times W)$（自由向量空间）模以双线性关系的商空间。

### Universal Property of Tensor Products **[Slofstra, Ch.8, Prop.8.2.4]**

对于任何双线性映射 $\phi: V \times W \to Y$，存在唯一线性映射 $A: V \otimes W \to Y$ 使得 $\phi(v, w) = A(v \otimes w)$。

> 这正是 Watrous (Prop.1.1) 中多线性函数定理的抽象版本。

### Tensor Products of Linear Maps **[Slofstra, Ch.8, §8.3]**

> Slofstra 原文 (Ch.8, p.78): 给定 $S: V \to V'$, $T: W \to W'$，$S \otimes T: V \otimes W \to V' \otimes W'$ 定义为 $(S \otimes T)(v \otimes w) = S(v) \otimes T(w)$，然后线性扩展。

### Natural Properties **[Slofstra, Ch.9]**

- **结合律**: $(U \otimes V) \otimes W \cong U \otimes (V \otimes W) \cong U \otimes V \otimes W$
- **$\text{Lin}(V, W) \cong V^* \otimes W$**: 线性映射空间与张量积的对偶关系
- **收缩与迹**: 迹是 $V^* \otimes V \to \mathbb{F}$ 的收缩，$\text{Tr}(|v^*\rangle \otimes |w\rangle) = v^*(w)$

### Tensor Product of Hilbert Spaces **[Slofstra, Ch.10]**

> Slofstra 原文 (Ch.10, p.101): 张量积 Hilbert 空间继承内积 $\langle u_1 \otimes u_2, v_1 \otimes v_2 \rangle = \langle u_1, v_1 \rangle \cdot \langle u_2, v_2 \rangle$。

**Frobenius 内积**: $\langle S, T \rangle = \text{Tr}(S^* T)$ 给出 $\text{Lin}(V, W)$ 上的内积。

### No-Cloning Theorem **[Slofstra, Ch.10, §10.2]**

> Slofstra 原文 (Ch.10, p.105): 不存在酉算符 $U$ 使得 $U(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle$ 对所有 $|\psi\rangle$ 成立。

**Proof**: 设 $U(|a\rangle|0\rangle) = |a\rangle|a\rangle$, $U(|b\rangle|0\rangle) = |b\rangle|b\rangle$。取内积（$U$ 保持内积）：$\langle a|b\rangle = \langle a|b\rangle^2$，因此 $\langle a|b\rangle \in \{0, 1\}$。$\square$

---

## Projective Measurements, Observables, Uncertainty (from Slofstra Ch.11-12)

### Direct Sums and Projections **[Slofstra, Ch.11, §11.1]**

$V = W \oplus W'$ 时投影 $P: V \to V$ 满足 $P^2 = P$。正交直和时 $P^* = P$。

### Projective Measurement **[Slofstra, Ch.11, §11.3]**

> Slofstra: 投影测量由正交投影族 $\{P_m\}$ 定义，$\sum_m P_m = \mathbb{1}$, $P_m P_{m'} = \delta_{mm'} P_m$。

概率 $\text{Prob}(m) = \langle v|P_m|v\rangle$。

### Uncertainty Principle **[Slofstra, Ch.12, §12.3]**

$$\Delta A \cdot \Delta B \geq \frac{1}{2}|\langle v|[A, B]|v\rangle|$$

### Compatible Measurements **[Slofstra, Ch.12, §12.4]**

$A, B$ 可同时测量 $\iff [A, B] = 0$（同时对角化）。

---

## Tensor Products in Watrous's Framework (from Watrous Ch.1)

### Tensor Product of Complex Euclidean Spaces **[Watrous, Ch.1, §1.1.1]**

> Watrous 原文 (p.6): "$\mathcal{X}_1 \otimes \cdots \otimes \mathcal{X}_n = \mathbb{C}^{\Sigma_1 \times \cdots \times \Sigma_n}$."

$(u_1 \otimes \cdots \otimes u_n)(a_1, \ldots, a_n) = u_1(a_1) \cdots u_n(a_n)$

**多线性性**: $u_1 \otimes \cdots \otimes (\alpha u_k + \beta v_k) \otimes \cdots \otimes u_n = \alpha(u_1 \otimes \cdots \otimes u_k \otimes \cdots) + \beta(u_1 \otimes \cdots \otimes v_k \otimes \cdots)$

### Proposition (Universal Property) **[Watrous, Ch.1, Prop.1.1]**

> Watrous 原文 (p.6): "There exists a unique linear mapping $A: \mathcal{X}_1 \otimes \cdots \otimes \mathcal{X}_n \to \mathcal{Y}$ such that $\phi(u_1, \ldots, u_n) = A(u_1 \otimes \cdots \otimes u_n)$" for any multilinear $\phi$.

### Operators on Direct Sums **[Watrous, Ch.1, §1.1.2]**

> Watrous 原文 (p.12): 算符 $A \in L(\mathcal{X}_1 \oplus \cdots \oplus \mathcal{X}_n, \mathcal{Y}_1 \oplus \cdots \oplus \mathcal{Y}_m)$ 对应分块矩阵 $\{A_{j,k}\}$，其中 $A_{j,k} \in L(\mathcal{X}_k, \mathcal{Y}_j)$，作用规则 $v_j = \sum_k A_{j,k} u_k$。

### Adjoint and Transpose **[Watrous, Ch.1, §1.1.2]**

> Watrous 原文 (p.10-11): 伴随 $A^*$ 是唯一满足 $\langle v, Au \rangle = \langle A^* v, u \rangle$ 的算符。$A^* = \overline{A}^T$。

向量 $u \in \mathcal{X}$ 可以视为 $L(\mathbb{C}, \mathcal{X})$ 中的算符。则 $u^* \in L(\mathcal{X}, \mathbb{C})$ 满足 $u^* v = \langle u, v \rangle$。

秩-1 算符：$(vu^*)w = \langle u, w \rangle v$，rank $(vu^*) = 1$（当 $u, v \neq 0$）。

---

## References

- **[LinAlg for QC]** — Portugal, R. *Quantum Walks and Search Algorithms*, Springer (2013), Appendix A.
- **[Slofstra]** — Slofstra, W. *Linear algebra and quantum probability* (v0.8, 2022), Ch. 7-12: Tensor products, projective measurements, observables, uncertainty principle, no-cloning theorem.
- **[Watrous]** — Watrous, J. *The Theory of Quantum Information*, Cambridge University Press (2018), Ch. 1-2: Tensor products, direct sums, operators.
- Nielsen & Chuang Section 2.1.7-2.1.8; Preskill Lecture Notes Chapter 2.
