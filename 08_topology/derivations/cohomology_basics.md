# Cohomology Basics for Quantum Codes

> **Tags**: `cohomology`, `cocycle`, `poincare-duality`, `topology`
>
> **Primary Source**: H. Bombin, *An Introduction to Topological Quantum Codes* **[Bombin, §3.2, §4.2--4.3]**

## Statement

上同调（Cohomology）是同调的对偶理论 **[Bombin, §4.2 (Dual lattice)]**。给定链复形 $C_n$ 和边界算子 $\partial_n$，通过取对偶空间 $C^n = \operatorname{Hom}(C_n, \mathbb{F}_2)$ 和转置映射 $\delta^n = \partial_{n+1}^T$，我们得到上链复形（cochain complex）。上同调群 $H^n = \ker \delta^n / \operatorname{im} \delta^{n-1}$ 度量上闭链（cocycles）模去上边界（coboundaries）。对于闭流形，Poincaré 对偶定理给出 $H_n \cong H^{d-n}$。在拓扑量子码中，$X$ 型和 $Z$ 型错误分别生活在对偶的链复形和上链复形中：$Z$ 型逻辑算子对应 $H_1$，$X$ 型逻辑算子对应 $H^1$ **[Bombin, §4.3 (Logical operators)]**。

## Prerequisites

- **同调基础**：链复形、边界算子、cycles、boundaries、同调群 → [homology_basics.md]
- **线性代数**：对偶空间、转置矩阵、核与像的关系 → [../01_linear_algebra/key_formulas.md]
- **$\mathbb{F}_2$ 算术**

---

## Derivation

### Step 1: Cochain Groups（上链群）

**定义**：给定链复形 $C_n$（$\mathbb{F}_2$-向量空间），$n$ 维上链群定义为其对偶空间：

$$C^n = \operatorname{Hom}(C_n, \mathbb{F}_2) = \{ \phi : C_n \to \mathbb{F}_2 \mid \phi \text{ 是线性映射} \}$$

一个 $n$-cochain $\phi \in C^n$ 是一个给每条 $n$-chain 赋值 0 或 1 的线性函数。

**$\mathbb{F}_2$ 上的简化**：在有限维 $\mathbb{F}_2$ 向量空间上，$C^n \cong C_n$（自然同构：每个上链可以用一条链来表示，通过内积 $\langle \phi, c \rangle = \phi(c)$）。

具体来说，如果 $C_n$ 有基 $\{\sigma_1, \ldots, \sigma_m\}$，则 $C^n$ 有对偶基 $\{\sigma_1^*, \ldots, \sigma_m^*\}$，其中 $\sigma_i^*(\sigma_j) = \delta_{ij}$。在 $\mathbb{F}_2$ 上，我们可以直接将 $\sigma_i^*$ 等同于 $\sigma_i$，将内积写成：

$$\langle \phi, c \rangle = \sum_i a_i b_i \pmod{2}$$

其中 $\phi = \sum_i a_i \sigma_i^*$，$c = \sum_i b_i \sigma_i$。

**物理意义**：在拓扑码中，
- 1-chain $c \in C_1$：边的子集 → $Z$ 型错误的支撑集（哪些量子比特上有 $Z$ 错误）
- 1-cochain $\gamma \in C^1$：也是边的子集 → $X$ 型错误的支撑集
- 内积 $\langle \gamma, c \rangle$：$\gamma$ 和 $c$ 的支撑集交集的奇偶性 → 判断 $X(\gamma)$ 和 $Z(c)$ 是否反对易

---

### Step 2: Coboundary Operator（上边界算子）

**定义**：上边界算子 $\delta^n: C^n \to C^{n+1}$ 定义为边界算子 $\partial_{n+1}$ 的伴随/转置：

$$(\delta^n \phi)(c) = \phi(\partial_{n+1}(c)) \quad \forall \phi \in C^n, \; c \in C_{n+1}$$

用矩阵表示（在 $\mathbb{F}_2$ 上利用 $C^n \cong C_n$ 的等同）：

$$\delta^n = \partial_{n+1}^T$$

上链复形的方向与链复形相反：

$$\cdots \xleftarrow{\delta^{n+1}} C^{n+1} \xleftarrow{\delta^n} C^n \xleftarrow{\delta^{n-1}} C^{n-1} \xleftarrow{\delta^{n-2}} \cdots$$

或者写成递增方向：

$$\cdots \xrightarrow{\delta^{n-1}} C^n \xrightarrow{\delta^n} C^{n+1} \xrightarrow{\delta^{n+1}} \cdots$$

**二维格子上的具体形式**：

$$C^0 \xrightarrow{\delta^0 = \partial_1^T} C^1 \xrightarrow{\delta^1 = \partial_2^T} C^2$$

- $\delta^0 = \partial_1^T$：将顶点映射到与之相连的边的集合（star operation）
- $\delta^1 = \partial_2^T$：将边映射到以它为边界的面的集合

**三角形例子**（续 [homology_basics.md] 的例子）：

```
    v0
   / \
  e2   e0
 /     \
v2--e1--v1
```

$$\partial_1 = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} \quad \Rightarrow \quad \delta^0 = \partial_1^T = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$$

计算 $\delta^0$ 的作用：

$$\delta^0(v_0) = e_0 + e_2 \quad \text{(与 } v_0 \text{ 相连的边)}$$

$$\delta^0(v_1) = e_0 + e_1 \quad \text{(与 } v_1 \text{ 相连的边)}$$

$$\delta^0(v_2) = e_1 + e_2 \quad \text{(与 } v_2 \text{ 相连的边)}$$

每个顶点的上边界 = 它的 star = 在拓扑码中对应 $X$-stabilizer 的支撑集。

---

### Step 3: Verify $\delta^2 = 0$（验证 $\delta^n \circ \delta^{n-1} = 0$）

**证明**：

$$\delta^n \circ \delta^{n-1} = \partial_{n+1}^T \circ \partial_n^T = (\partial_n \circ \partial_{n+1})^T = 0^T = 0$$

因为 $\partial_n \circ \partial_{n+1} = 0$（链复形的基本性质），其转置也为零。 $\square$

**三角形例子的验证**（假设有填充面 $f$）：

$$\delta^1 = \partial_2^T$$

$$\partial_2 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \quad \Rightarrow \quad \delta^1 = (1, 1, 1)$$

$$\delta^1 \circ \delta^0 = (1, 1, 1) \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} = (1+0+1, \; 1+1+0, \; 0+1+1) = (0, 0, 0) \quad \checkmark$$

直观理解：$\delta^0(v)$ 给出顶点 $v$ 的 star（相连的边），$\delta^1$ 将边映射到含该边的面。$\delta^1(\delta^0(v))$ 数的是包含顶点 $v$ 的面的集合——但每个面被计数了两次（$v$ 通过两条边连到每个相邻面），在 $\mathbb{F}_2$ 上为零。

---

### Step 4: Cocycles and Coboundaries（上闭链与上边界链）

**定义**：

$$Z^n = \ker \delta^n = \{ \gamma \in C^n : \delta^n(\gamma) = 0 \} \quad \text{(n-cocycles)}$$

$$B^n = \operatorname{im} \delta^{n-1} = \{ \delta^{n-1}(\alpha) : \alpha \in C^{n-1} \} \quad \text{(n-coboundaries)}$$

由 $\delta^2 = 0$，有 $B^n \subseteq Z^n$。

**二维格子上 $n = 1$ 的具体含义**：

$Z^1 = \ker \delta^1 = \ker \partial_2^T$：一条1-cochain $\gamma$ 是 cocycle 当且仅当它与每个面的边界的内积为零——即 $\gamma$ 穿过每个面的次数为偶数。

$B^1 = \operatorname{im} \delta^0 = \operatorname{im} \partial_1^T$：一条1-cochain $\gamma$ 是 coboundary 当且仅当它是某些顶点的 star 之和。

**与量子码的直接对应**：

$$Z^1 = \ker \partial_2^T = (\operatorname{im} \partial_2)^\perp = B_1^\perp$$

$X$ 型算子 $X(\gamma)$ 与所有 $Z$-stabilizer 对易 $\Leftrightarrow$ $\gamma \in B_1^\perp = Z^1$。

$$B^1 = \operatorname{im} \partial_1^T$$

$X(\gamma)$ 是 $X$-stabilizer $\Leftrightarrow$ $\gamma \in B^1$。

---

### Step 5: Cohomology Groups（上同调群）

**定义**：

$$H^n = Z^n / B^n = \ker \delta^n \, / \, \operatorname{im} \delta^{n-1}$$

**三角形例子**（无填充面，$C_2 = 0$）：

$\delta^0 = \partial_1^T$（如 Step 2），$\delta^1 = 0$（因为 $C_2 = 0$，$\partial_2 = 0$）。

$Z^1 = \ker \delta^1 = \ker 0 = C^1 \cong \mathbb{F}_2^3$，$\dim Z^1 = 3$。

$B^1 = \operatorname{im} \delta^0 = \operatorname{im} \partial_1^T$。$\partial_1^T$ 的列：$(1,0,1), (1,1,0), (0,1,1)$。秩 = 2（任意两列独立，三列之和为零）。$\dim B^1 = 2$。

$$H^1 \cong \mathbb{F}_2^{3-2} = \mathbb{F}_2, \quad \dim H^1 = 1$$

对比：$H_1 \cong \mathbb{F}_2$（同调群，在 [homology_basics.md] 中计算）。$\dim H^1 = \dim H_1 = 1$。$\checkmark$

**$2 \times 2$ 环面例子**：

利用 [homology_basics.md] Step 8 中的矩阵：

$\delta^0 = \partial_1^T$ 是 $8 \times 4$ 矩阵（$\partial_1$ 的转置），$\operatorname{rank}(\delta^0) = \operatorname{rank}(\partial_1) = 3$。

$\delta^1 = \partial_2^T$ 是 $4 \times 8$ 矩阵，$\operatorname{rank}(\delta^1) = \operatorname{rank}(\partial_2) = 3$。

$$\dim Z^1 = \dim \ker \delta^1 = 8 - 3 = 5$$

$$\dim B^1 = \operatorname{rank}(\delta^0) = 3$$

$$\dim H^1 = 5 - 3 = 2$$

$$H^1(T^2; \mathbb{F}_2) \cong \mathbb{F}_2^2$$

与 $H_1(T^2; \mathbb{F}_2) \cong \mathbb{F}_2^2$ 吻合。$\checkmark$

---

### Step 6: Poincaré Duality for Closed Manifolds（闭流形的 Poincaré 对偶）

**定理**（Poincaré 对偶）：设 $M$ 是 $d$ 维可定向闭流形（紧致、无边界）。则：

$$H^n(M; \mathbb{F}_2) \cong H_{d-n}(M; \mathbb{F}_2)$$

在 $\mathbb{F}_2$ 系数下，可定向条件可以放宽——对所有闭流形都成立。

**直觉**：$d$ 维闭流形上，$n$ 维的"洞"与 $(d-n)$ 维的"洞"一一对应。具体机制：cap product 与流形的基本类 $[M] \in H_d(M)$，给出同构映射 $\cap [M]: H^n(M) \xrightarrow{\sim} H_{d-n}(M)$。

**二维闭曲面的对偶**（$d = 2$）：

$$H^0 \cong H_2, \quad H^1 \cong H_1, \quad H^2 \cong H_0$$

**逐一验证环面 $T^2$ 的情况**（$\mathbb{F}_2$ 系数）：

| $n$ | $H_n$ | $H^n$ | $H^n \cong H_{2-n}$? |
|-----|--------|--------|----------------------|
| 0 | $\mathbb{F}_2$ | $\mathbb{F}_2$ | $H^0 \cong H_2 = \mathbb{F}_2$ $\checkmark$ |
| 1 | $\mathbb{F}_2^2$ | $\mathbb{F}_2^2$ | $H^1 \cong H_1 = \mathbb{F}_2^2$ $\checkmark$ |
| 2 | $\mathbb{F}_2$ | $\mathbb{F}_2$ | $H^2 \cong H_0 = \mathbb{F}_2$ $\checkmark$ |

**更多曲面的对偶**：

球面 $S^2$（$g = 0$）：$H_0 = \mathbb{F}_2$，$H_1 = 0$，$H_2 = \mathbb{F}_2$。

$$H^0 \cong H_2 = \mathbb{F}_2, \quad H^1 \cong H_1 = 0, \quad H^2 \cong H_0 = \mathbb{F}_2 \quad \checkmark$$

亏格-2 曲面：$H_0 = \mathbb{F}_2$，$H_1 = \mathbb{F}_2^4$，$H_2 = \mathbb{F}_2$。

$$H^1 \cong H_1 = \mathbb{F}_2^4 \quad \checkmark$$

---

### Step 7: Poincaré Duality for Lattice Models（格子模型中的 Poincaré 对偶）

在格子/CW 复形层面，Poincaré 对偶有一个非常具体的几何实现——**对偶格子（dual lattice）**。

**构造**：给定二维流形 $M$ 上的 CW 分解 $\mathcal{K}$，其对偶分解 $\mathcal{K}^*$ 定义为：
- $\mathcal{K}$ 的每个面 $f$ → $\mathcal{K}^*$ 的一个顶点 $f^*$
- $\mathcal{K}$ 的每条边 $e$ → $\mathcal{K}^*$ 的一条对偶边 $e^*$（穿过 $e$）
- $\mathcal{K}$ 的每个顶点 $v$ → $\mathcal{K}^*$ 的一个面 $v^*$

维度对偶：$\mathcal{K}$ 的 $n$-cell $\leftrightarrow$ $\mathcal{K}^*$ 的 $(d-n)$-cell。

**对偶格子上的链复形**：

$$C_2^* \xrightarrow{\partial_2^*} C_1^* \xrightarrow{\partial_1^*} C_0^*$$

关键关系：

$$C_n^* \cong C^{d-n} \cong C_{d-n}$$

$$\partial_n^* \cong \delta^{d-n} = \partial_{d-n+1}^T$$

具体地（$d = 2$）：

$$C_0^* = \operatorname{span}\{f^* : f \in \mathcal{K}_2\} \cong C_2 \cong C^0$$

$$C_1^* = \operatorname{span}\{e^* : e \in \mathcal{K}_1\} \cong C_1 \cong C^1$$

$$C_2^* = \operatorname{span}\{v^* : v \in \mathcal{K}_0\} \cong C_0 \cong C^2$$

$$\partial_1^* = \partial_2^T = \delta^1, \quad \partial_2^* = \partial_1^T = \delta^0$$

所以**原格子上的上链复形 = 对偶格子上的链复形**。原格子上的上同调 = 对偶格子上的同调。

**方格子的对偶**：

```
原格子:                       对偶格子:
  v---e---v                   *---e*---*
  |   f   |          →        |   v*   |
  e       e                   e*       e*
  |       |                   |        |
  v---e---v                   *---e*---*
```

原格子的顶点 ↔ 对偶格子的面，原格子的面 ↔ 对偶格子的顶点，边 ↔ 对偶边（正交穿过）。

---

### Step 8: Practical Meaning for Quantum Codes（对量子码的实际意义）

**$X$ 型和 $Z$ 型错误生活在对偶的链复形中**：

| | $Z$ 型 | $X$ 型 |
|---|--------|--------|
| 错误空间 | $C_1$（原格子的边） | $C^1 \cong C_1^*$（对偶格子的边） |
| Syndrome 空间 | $C_0$（原格子的顶点） | $C^2 \cong C_0^*$（对偶格子的顶点 = 原格子的面） |
| Syndrome 映射 | $\partial_1$（边界：边→端点） | $\delta^1 = \partial_2^T$（上边界：边→相邻面） |
| 稳定子 | $B_1 = \operatorname{im} \partial_2$（面的边界） | $B^1 = \operatorname{im} \partial_1^T$（顶点的上边界 = star） |
| 逻辑算子 | $H_1 = Z_1 / B_1$ | $H^1 = Z^1 / B^1$ |

**syndrome 测量的对偶解释**：

- 测量 $A_v$（$X$-stabilizer，顶点 $v$）得到 syndrome bit $s_v$：这检测 $Z$ 型错误。$s_v = 1$ 意味着奇数条有 $Z$ 错误的边连到 $v$，即 $(\partial_1 e)_v = 1$。所以 $Z$ 型 syndrome = $\partial_1(e)$。
- 测量 $B_f$（$Z$-stabilizer，面 $f$）得到 syndrome bit $s_f$：这检测 $X$ 型错误。$s_f = 1$ 意味着奇数条有 $X$ 错误的边在面 $f$ 的边界上，即 $(\delta^1 \gamma)_f = (\partial_2^T \gamma)_f = 1$。所以 $X$ 型 syndrome = $\delta^1(\gamma) = \partial_2^T(\gamma)$。

**对偶性保证了对称处理**：在 Poincaré 对偶下（$H^1 \cong H_1$），$X$ 型码距和 $Z$ 型码距由相同的拓扑量（最短非平凡同调类的长度）决定。对于环面码（正方格子，自对偶），$d_X = d_Z$。对于非自对偶格子，$d_X$ 和 $d_Z$ 可能不同，但它们仍然由格子和对偶格子上的最短非平凡环分别确定。

---

### Step 9: Intersection Form and Logical Operator Commutation（交叉形式与逻辑算子对易关系）

**交叉形式**（Intersection form）提供了 $H_1$ 和 $H^1$ 之间的自然配对：

$$\langle \cdot, \cdot \rangle : H^1 \times H_1 \to \mathbb{F}_2$$

$$\langle [\gamma], [c] \rangle = \sum_{i} \gamma_i c_i \pmod{2} = |\text{supp}(\gamma) \cap \text{supp}(c)| \pmod{2}$$

这个配对与逻辑算子的对易性直接相关：

$$\langle [\gamma], [c] \rangle = 0 \quad \Leftrightarrow \quad [\bar{X}(\gamma), \bar{Z}(c)] = 0$$

$$\langle [\gamma], [c] \rangle = 1 \quad \Leftrightarrow \quad \{\bar{X}(\gamma), \bar{Z}(c)\} = 0$$

对于环面 $T^2$，$H_1 \cong H^1 \cong \mathbb{F}_2^2$，选取标准基 $[\gamma_h], [\gamma_v]$（水平环和垂直环），交叉矩阵为：

$$Q = \begin{pmatrix} \langle [\gamma_h], [\gamma_h] \rangle & \langle [\gamma_h], [\gamma_v] \rangle \\ \langle [\gamma_v], [\gamma_h] \rangle & \langle [\gamma_v], [\gamma_v] \rangle \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

（水平环和垂直环交叉一次，同一方向的环不交叉。）

这个辛结构（symplectic structure）正是两个逻辑量子比特的 Pauli 代数所需要的：$\bar{X}_1$ 与 $\bar{Z}_2$ 对易，$\bar{X}_1$ 与 $\bar{Z}_1$ 反对易，等等。

对于亏格-$g$ 曲面，交叉矩阵是 $2g \times 2g$ 的辛矩阵：

$$Q = \begin{pmatrix} 0 & 1 & & & \\ 1 & 0 & & & \\ & & 0 & 1 & \\ & & 1 & 0 & \\ & & & & \ddots \end{pmatrix} = \bigoplus_{i=1}^{g} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

$g$ 个配对的环（$a$-cycle 和 $b$-cycle），对应 $g$ 对逻辑量子比特。

---

### Step 10: Summary Table（总结表）

| 同调概念 | 上同调对偶概念 | 量子码意义 |
|----------|--------------|-----------|
| $C_n$（$n$-chains） | $C^n$（$n$-cochains） | $\mathbb{F}_2$ 上等同 |
| $\partial_n$（boundary） | $\delta^{n-1} = \partial_n^T$（coboundary） | 转置关系 |
| $Z_n = \ker \partial_n$ | $Z^n = \ker \delta^n$ | Cycle / Cocycle |
| $B_n = \operatorname{im} \partial_{n+1}$ | $B^n = \operatorname{im} \delta^{n-1}$ | $Z$-stab / $X$-stab |
| $H_n = Z_n / B_n$ | $H^n = Z^n / B^n$ | 逻辑 $Z$ / 逻辑 $X$ |
| $\partial^2 = 0$ | $\delta^2 = 0$ | 稳定子对易 |
| Poincaré 对偶 $H_n \cong H^{d-n}$ | | $X/Z$ 对称性 |
| 交叉形式 $H^1 \times H_1 \to \mathbb{F}_2$ | | 逻辑 Pauli 代数 |
| 对偶格子 | 原格子 | $X/Z$ 解码的对偶性 |

---

## From Bombin: Cohomology in Surface Codes

### Dual Lattice and Hadamard Duality **[Bombin, §3.3]**

Given a lattice, its dual lattice maps: faces $\to$ dual vertices $\hat{f}$, edges $\to$ dual edges $\hat{e}$, vertices $\to$ dual faces $\hat{v}$. The dual boundary operators satisfy:

$$\hat{e} \in \hat{\partial}_1 \hat{v} \iff v \in \partial_1 e, \qquad \hat{f} \in \hat{\partial}_2 \hat{e} \iff e \in \partial_2 f$$

Transversal Hadamard $W^{\otimes E}$ maps the surface code on the original lattice to the surface code on the dual lattice:

$$W^{\otimes E} X_f W^{\otimes E} = Z_{\hat{f}}, \qquad W^{\otimes E} Z_v W^{\otimes E} = X_{\hat{v}}$$

This is the physical manifestation of Poincare duality **[Bombin, §3.3]**.

### Cocycles as X-type Operators **[Bombin, §3.4]**

Phase-flip errors are related to 1-chains on the dual lattice (cocycles on the original). The stabilizer structure becomes:

- $A \in N(S) \iff (c, \hat{c}) \in Z_1 \times \hat{Z}_1$
- $B \in S \iff (c, \hat{c}) \in B_1 \times \hat{B}_1$

Therefore $N(S)/S' \simeq H_1 \times \hat{H}_1 \simeq H_1 \times H^1$. The cohomological and homological perspectives are connected through the dual lattice **[Bombin, §3.4]**.

### String Operators and Crossing **[Bombin, §3.4]**

Direct strings (lattice 1-chains, $X$-type) and dual strings (dual lattice 1-chains, $Z$-type) anticommute iff they cross an odd number of times. The oddness is preserved under homology/cohomology equivalence, providing a geometric interpretation of the symplectic structure of logical operators **[Bombin, §3.4]**.

---

## From Dennis et al.: Cohomological Interpretation

### Cycle Condition as Cocycle **[Dennis et al. 2002, §3.4]**

Dennis et al. solve the cycle constraint $du = 0$ (where $u$ is a discrete 1-form and $d$ the exterior derivative) by writing $u = d\sigma$ for a 0-form $\sigma$. This solution generates all and only homologically trivial cycles. In 2D this gives the random-bond Ising model; in 3D (for gauge theory with imperfect syndrome), $u$ is a 2-form and $\sigma$ a 1-form, yielding the $\mathbb{Z}_2$ gauge model **[Dennis et al. 2002, §3.4]**.

### Cohomological Non-trivial Contributions **[Dennis et al. 2002, §3.4]**

The solution $u = d\sigma$ misses the cohomologically non-trivial closed forms (closed but not exact). These correspond precisely to the homologically non-trivial cycles that produce logical errors. The error recovery threshold is the point at which these non-trivial contributions become statistically negligible **[Dennis et al. 2002, §3.4]**.

---

## References

1. Hatcher, A. *Algebraic Topology*. Cambridge University Press, 2002. Chapter 3.
2. Munkres, J. R. *Elements of Algebraic Topology*. Addison-Wesley, 1984.
3. Kitaev, A. Y. "Fault-tolerant quantum computation by anyons." *Ann. Phys.* 303, 2-30 (2003).
4. Bombin, H. "An Introduction to Topological Quantum Codes." In: *Quantum Error Correction*, Cambridge UP (2013).
5. Dennis, E., Kitaev, A., Landahl, A. & Preskill, J. "Topological quantum memory." *J. Math. Phys.* 43, 4452 (2002).
6. Bredon, G. E. *Topology and Geometry*. Springer, 1993. Chapter VI (Poincare duality).
