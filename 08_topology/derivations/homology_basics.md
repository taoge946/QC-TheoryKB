# Homology Theory Basics for Topological Codes

> **Tags**: `homology`, `chain-complex`, `boundary`, `cycle`, `topology`
>
> **Primary Source**: H. Bombin, *An Introduction to Topological Quantum Codes*, Ch. in *Quantum Error Correction* (CUP, 2013) **[Bombin, §3]**

## Statement

同调理论提供了一套代数工具，将拓扑空间中的"洞"精确地形式化 **[Bombin, §3 (Surface Homology)]**。通过构造链复形——一系列由边界算子连接的向量空间——我们可以定义 cycles（闭链）、boundaries（边界链）和 homology groups（同调群） **[Bombin, §3, Eq.(5)--(6)]**。同调群 $H_n = Z_n / B_n$ 精确地度量了"不是边界的闭链"的等价类。这一框架直接对应拓扑量子纠错码的结构：稳定子是边界，逻辑算子是非平凡同调类 **[Bombin, §4]**。

## Prerequisites

- **线性代数**：向量空间、线性映射、核与像、秩-零化度定理、商空间 → [../01_linear_algebra/key_formulas.md]
- **基础拓扑概念**：图、格子、边界的直观概念
- **$\mathbb{F}_2$ 算术**：二元域上的加法（$1 + 1 = 0$），即模 2 算术

---

## Derivation

### Step 1: Simplicial Complex（单纯复形）

**概念引入**：我们从最具体的对象开始。单纯复形是构建链复形的几何基础。

**定义**：一个（抽象）单纯复形 $K$ 是顶点集 $V$ 的子集族，满足：
- 每个单点 $\{v\}$ 属于 $K$
- 如果 $\sigma \in K$ 且 $\tau \subseteq \sigma$，则 $\tau \in K$（对取子集封闭）

各维度的单纯形（simplex）：
- 0-simplex：顶点 $\{v\}$
- 1-simplex：边 $\{v_0, v_1\}$
- 2-simplex：三角形 $\{v_0, v_1, v_2\}$
- $n$-simplex：$\{v_0, v_1, \ldots, v_n\}$，共 $n+1$ 个顶点

**量子码中的对应**：在表面码/环面码中，我们使用的是 CW 复形（比单纯复形更一般），但基本思想相同：
- 0-cells = 顶点
- 1-cells = 边（放置量子比特）
- 2-cells = 面/plaquette

**例子**：考虑一个最小的三角剖分——三角形的边界：

```
    v0
   / \
  e2   e0
 /     \
v2--e1--v1
```

顶点：$\{v_0, v_1, v_2\}$，边：$\{e_0, e_1, e_2\}$，其中 $e_0 = \{v_0, v_1\}$，$e_1 = \{v_1, v_2\}$，$e_2 = \{v_2, v_0\}$。

---

### Step 2: Chain Groups（链群） **[Bombin, §3.2, Eq.(3)]**

**定义**：$n$ 维链群 $C_n(K; \mathbb{F}_2)$ 是以 $K$ 中所有 $n$-simplex 为基的 $\mathbb{F}_2$-向量空间。

换言之，一条 $n$-chain 是若干 $n$-simplex 的形式和（系数在 $\mathbb{F}_2$ 中）：

$$c = \sum_i a_i \sigma_i, \quad a_i \in \mathbb{F}_2$$

**为什么用 $\mathbb{F}_2$**：在量子纠错中，我们关心的是 Pauli 算子的支撑集，而 Pauli 群（模去相位）在每个量子比特上只有 $\{I, X, Y, Z\}$。对于 CSS 码，$X$ 型和 $Z$ 型错误可以分别处理，每种类型的错误要么在某个量子比特上存在（1），要么不存在（0），正好是 $\mathbb{F}_2$ 算术。

**三角形例子中的链群**：

$$C_0 = \operatorname{span}_{\mathbb{F}_2}\{v_0, v_1, v_2\} \cong \mathbb{F}_2^3, \quad \dim C_0 = 3$$

$$C_1 = \operatorname{span}_{\mathbb{F}_2}\{e_0, e_1, e_2\} \cong \mathbb{F}_2^3, \quad \dim C_1 = 3$$

$$C_2 = \{0\} \cong \mathbb{F}_2^0, \quad \dim C_2 = 0 \quad \text{(没有2-simplex，三角形没有被填充)}$$

**链的加法（$\mathbb{F}_2$）**：

$$e_0 + e_1 = \text{边 } e_0 \text{ 和 } e_1 \text{ 组成的链}$$

$$e_0 + e_0 = 0 \quad \text{(模 2 加法：同一条边出现两次等于没有)}$$

---

### Step 3: Boundary Operator（边界算子） **[Bombin, §3.2, Eq.(4)]**

**定义**：边界算子 $\partial_n: C_n \to C_{n-1}$ 是一个线性映射，将每个 $n$-simplex 映射到其边界。

在 $\mathbb{F}_2$ 系数下，$n$-simplex $\sigma = \{v_0, v_1, \ldots, v_n\}$ 的边界为：

$$\partial_n(\sigma) = \sum_{i=0}^{n} \{v_0, \ldots, \hat{v}_i, \ldots, v_n\}$$

其中 $\hat{v}_i$ 表示删去 $v_i$。在 $\mathbb{F}_2$ 上不需要 $(-1)^i$ 的符号因子（因为 $-1 = 1$ mod 2）。

**三角形例子**：

$$\partial_1: C_1 \to C_0$$

$$\partial_1(e_0) = \partial_1(\{v_0, v_1\}) = v_0 + v_1$$

$$\partial_1(e_1) = \partial_1(\{v_1, v_2\}) = v_1 + v_2$$

$$\partial_1(e_2) = \partial_1(\{v_2, v_0\}) = v_0 + v_2$$

用矩阵表示（行 = $C_0$ 的基 $\{v_0, v_1, v_2\}$，列 = $C_1$ 的基 $\{e_0, e_1, e_2\}$）：

$$\partial_1 = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

直观理解：每条边的边界是其两个端点（之和）。

---

### Step 4: Verify $\partial^2 = 0$（验证 $\partial_n \circ \partial_{n+1} = 0$） **[Bombin, §3.2, after Eq.(4)]**

这是链复形最关键的性质。

**一般证明**（$\mathbb{F}_2$ 系数）：

对于 $n$-simplex $\sigma = \{v_0, \ldots, v_n\}$：

$$\partial_n(\partial_{n+1}(\sigma)) = \partial_n\left(\sum_{i=0}^{n+1} \{v_0, \ldots, \hat{v}_i, \ldots, v_{n+1}\}\right)$$

$$= \sum_{i=0}^{n+1} \sum_{j \neq i} \{v_0, \ldots, \hat{v}_i, \ldots, \hat{v}_j, \ldots, v_{n+1}\}$$

每个 $(n-1)$-simplex $\{v_0, \ldots, \hat{v}_i, \ldots, \hat{v}_j, \ldots, v_{n+1}\}$ 在求和中恰好出现两次：一次对应先删 $v_i$ 再删 $v_j$（$i < j$），一次对应先删 $v_j$ 再删 $v_i$（$j < i$）。在 $\mathbb{F}_2$ 上，$1 + 1 = 0$，所以每项抵消。

$$\therefore \partial_n \circ \partial_{n+1} = 0 \quad \square$$

**三角形例子的具体验证**：

如果我们有一个填充的三角形 $f = \{v_0, v_1, v_2\}$（作为 2-simplex），则：

$$\partial_2(f) = \{v_1, v_2\} + \{v_0, v_2\} + \{v_0, v_1\} = e_1 + e_2 + e_0 = e_0 + e_1 + e_2$$

然后验证 $\partial_1(\partial_2(f))$：

$$\partial_1(e_0 + e_1 + e_2) = \partial_1(e_0) + \partial_1(e_1) + \partial_1(e_2)$$

$$= (v_0 + v_1) + (v_1 + v_2) + (v_0 + v_2)$$

$$= 2v_0 + 2v_1 + 2v_2 = 0 + 0 + 0 = 0 \quad \checkmark$$

**直观理解**：三角形的边界是三条边组成的闭合回路，而闭合回路没有端点（"边界"），所以"边界的边界为零"。

**格子上的验证**：考虑方格子上的一个 plaquette（面）$f$：

```
  v0---e0---v1
  |          |
  e3    f    e1
  |          |
  v3---e2---v2
```

$$\partial_2(f) = e_0 + e_1 + e_2 + e_3$$

$$\partial_1(e_0 + e_1 + e_2 + e_3) = (v_0 + v_1) + (v_1 + v_2) + (v_2 + v_3) + (v_3 + v_0)$$

$$= 2v_0 + 2v_1 + 2v_2 + 2v_3 = 0 \quad \checkmark$$

每个顶点出现两次（被两条边共享），在 $\mathbb{F}_2$ 上抵消为零。这正是表面码中 $A_v$ 和 $B_f$ 稳定子对易的拓扑根源。

---

### Step 5: Cycles and Boundaries（闭链与边界链）

**定义**：

$$Z_n = \ker \partial_n = \{ c \in C_n : \partial_n(c) = 0 \}$$

$Z_n$ 的元素称为 $n$-cycles（$n$维闭链）。一条链是闭链当且仅当它没有边界。

$$B_n = \operatorname{im} \partial_{n+1} = \{ \partial_{n+1}(c') : c' \in C_{n+1} \}$$

$B_n$ 的元素称为 $n$-boundaries（$n$维边界链）。一条链是边界链当且仅当它是某个高维链的边界。

**关键包含关系**：由 $\partial^2 = 0$，有

$$B_n \subseteq Z_n$$

证明：若 $c \in B_n$，则存在 $c' \in C_{n+1}$ 使得 $c = \partial_{n+1}(c')$，于是

$$\partial_n(c) = \partial_n(\partial_{n+1}(c')) = 0$$

所以 $c \in Z_n$。 $\square$

**三角形例子**（只有边界，没有填充的 2-simplex，即 $C_2 = 0$）：

计算 $Z_1 = \ker \partial_1$：

我们需要找所有满足 $\partial_1(a_0 e_0 + a_1 e_1 + a_2 e_2) = 0$ 的链。

$$\partial_1(a_0 e_0 + a_1 e_1 + a_2 e_2) = a_0(v_0 + v_1) + a_1(v_1 + v_2) + a_2(v_0 + v_2)$$

$$= (a_0 + a_2)v_0 + (a_0 + a_1)v_1 + (a_1 + a_2)v_2 = 0$$

这要求：

$$a_0 + a_2 = 0, \quad a_0 + a_1 = 0, \quad a_1 + a_2 = 0 \quad \text{(mod 2)}$$

解为 $a_0 = a_1 = a_2$，即 $Z_1 = \operatorname{span}\{e_0 + e_1 + e_2\}$。这就是三角形的完整边界回路。

$$\dim Z_1 = 1$$

计算 $B_1 = \operatorname{im} \partial_2$：

由于 $C_2 = 0$（没有填充的三角形），所以 $B_1 = \{0\}$，$\dim B_1 = 0$。

---

### Step 6: Homology Definition（同调群的定义）

**定义**：第 $n$ 个同调群是 cycles 模去 boundaries 的商群：

$$H_n(K; \mathbb{F}_2) = Z_n / B_n = \ker \partial_n \, / \, \operatorname{im} \partial_{n+1}$$

商群中的元素称为同调类（homology class）。两条 cycle $c_1$ 和 $c_2$ 是同调的（homologous），记作 $c_1 \sim c_2$，当且仅当：

$$c_1 - c_2 \in B_n \quad \Leftrightarrow \quad c_1 + c_2 \in B_n \quad \text{(在 } \mathbb{F}_2 \text{ 上)}$$

即它们的差是一条边界链。

**直观理解**：
- $H_n = 0$ 意味着所有闭链都是边界——没有 $n$ 维的"洞"
- $H_n \neq 0$ 意味着存在不是边界的闭链——空间中有 $n$ 维的"洞"
- 同调类 $[c]$ 中的所有代表元可以通过"添加/删除边界"相互转化——对应拓扑码中通过施加稳定子来变形错误链

**三角形例子**（$K$ = 三角形的边界，无填充）：

$$H_0 = Z_0 / B_0$$

$Z_0 = \ker \partial_0 = C_0$（因为 $\partial_0 = 0$，所有 0-chain 都是 0-cycle），$\dim Z_0 = 3$。

$B_0 = \operatorname{im} \partial_1$：$\partial_1$ 的列向量 $(1,1,0)^T, (0,1,1)^T, (1,0,1)^T$ 在 $\mathbb{F}_2$ 上张成一个 2 维空间（任意两列线性无关，三列之和为零），所以 $\dim B_0 = 2$。

$$H_0 \cong \mathbb{F}_2^{3-2} = \mathbb{F}_2$$

$\dim H_0 = 1$，即 $\beta_0 = 1$，表示三角形边界是连通的（只有1个连通分量）。

$$H_1 = Z_1 / B_1 = \operatorname{span}\{e_0 + e_1 + e_2\} / \{0\} \cong \mathbb{F}_2$$

$\dim H_1 = 1$，即 $\beta_1 = 1$，表示三角形边界有1个"洞"（三角形内部未被填充，形成一个环）。

如果三角形被填充（加入 2-simplex $f = \{v_0, v_1, v_2\}$），则 $B_1 = \operatorname{im}\partial_2 = \operatorname{span}\{e_0 + e_1 + e_2\} = Z_1$，于是 $H_1 = 0$——洞被填上了。

---

### Step 7: Small Lattice Example（小格子上的完整计算）

考虑一个 $2 \times 2$ 的方格子（无周期性边界，4个顶点，4条边，1个面）：

```
  v0---e0---v1
  |          |
  e2    f    e1
  |          |
  v2---e3---v3
```

**链群**：

$$C_0 = \operatorname{span}\{v_0, v_1, v_2, v_3\} \cong \mathbb{F}_2^4$$

$$C_1 = \operatorname{span}\{e_0, e_1, e_2, e_3\} \cong \mathbb{F}_2^4$$

$$C_2 = \operatorname{span}\{f\} \cong \mathbb{F}_2^1$$

**边界算子矩阵**：

$$\partial_1 = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 1 \end{pmatrix}$$

行对应 $v_0, v_1, v_2, v_3$；列对应 $e_0, e_1, e_2, e_3$。

例如：$\partial_1(e_0) = v_0 + v_1$（$e_0$ 连接 $v_0$ 和 $v_1$）。

$$\partial_2 = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}$$

行对应 $e_0, e_1, e_2, e_3$；列对应 $f$。

$\partial_2(f) = e_0 + e_1 + e_2 + e_3$（面的边界是其四条边）。

**验证 $\partial_1 \circ \partial_2 = 0$**：

$$\partial_1 \partial_2 = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1+1 \\ 1+1 \\ 1+1 \\ 1+1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} \quad \checkmark$$

**计算同调群**：

$Z_1 = \ker \partial_1$：由秩-零化度定理，$\dim Z_1 = \dim C_1 - \operatorname{rank}(\partial_1) = 4 - 3 = 1$。

（$\partial_1$ 的秩为 3：前三列线性无关。）

$Z_1$ 的基：$e_0 + e_1 + e_2 + e_3$（唯一的非零闭链——绕面 $f$ 一圈的回路）。

$B_1 = \operatorname{im} \partial_2 = \operatorname{span}\{e_0 + e_1 + e_2 + e_3\}$，$\dim B_1 = 1$。

$$H_1 = Z_1 / B_1 = \mathbb{F}_2 / \mathbb{F}_2 = 0, \quad \beta_1 = 0$$

结论：这个格子（拓扑上等价于圆盘）没有非平凡的 1 维洞，$H_1 = 0$。

$H_0$：$Z_0 = C_0 \cong \mathbb{F}_2^4$，$B_0 = \operatorname{im} \partial_1$，$\dim B_0 = \operatorname{rank}(\partial_1) = 3$。

$$H_0 \cong \mathbb{F}_2^{4-3} = \mathbb{F}_2, \quad \beta_0 = 1$$

一个连通分量。

$H_2$：$Z_2 = \ker \partial_2$。因为 $\partial_2(f) = e_0 + e_1 + e_2 + e_3 \neq 0$，所以 $Z_2 = 0$。

$$H_2 = 0, \quad \beta_2 = 0$$

**总结**：$(\beta_0, \beta_1, \beta_2) = (1, 0, 0)$，对应于圆盘的拓扑——连通且无洞。

---

### Step 8: Torus Example（环面——环面码的关键）

环面 $T^2$ 可以用 $L \times L$ 的周期性方格子表示。以最小的 $2 \times 2$ 环面为例：

```
对顶点编号（周期性边界条件：右边=左边，上面=下面）：

  v0---e0---v1---e1---[v0]
  |          |          |
  e4    f0   e5    f1   [e4]
  |          |          |
  v2---e2---v3---e3---[v2]
  |          |          |
  e6    f2   e7    f3   [e6]
  |          |          |
 [v0]--[e0]-[v1]--[e1]-[v0]
```

方括号表示由周期性边界条件等同的元素。

**胞腔计数**：
- 顶点：$v_0, v_1, v_2, v_3$，共 $V = 4$
- 边：$e_0, \ldots, e_7$，共 $E = 8$（每个顶点向右一条、向下一条）
- 面：$f_0, f_1, f_2, f_3$，共 $F = 4$

Euler 示性数验证：$\chi = V - E + F = 4 - 8 + 4 = 0 = 2 - 2g$，所以 $g = 1$（亏格为1的环面）。$\checkmark$

**链群**：$C_0 \cong \mathbb{F}_2^4$，$C_1 \cong \mathbb{F}_2^8$，$C_2 \cong \mathbb{F}_2^4$。

**边界算子 $\partial_1$**（$4 \times 8$ 矩阵，行=顶点，列=边）：

边的端点（在周期性边界条件下）：
- $e_0: v_0 \leftrightarrow v_1$
- $e_1: v_1 \leftrightarrow v_0$（周期性！从 $v_1$ 到右边 = 回到 $v_0$）
- $e_2: v_2 \leftrightarrow v_3$
- $e_3: v_3 \leftrightarrow v_2$
- $e_4: v_0 \leftrightarrow v_2$
- $e_5: v_1 \leftrightarrow v_3$
- $e_6: v_2 \leftrightarrow v_0$（周期性！从 $v_2$ 向下 = 回到 $v_0$）
- $e_7: v_3 \leftrightarrow v_1$

$$\partial_1 = \begin{pmatrix} 1 & 1 & 0 & 0 & 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 & 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 1 & 0 & 1 \end{pmatrix}$$

**$\partial_1$ 的秩**：通过行化简，$\operatorname{rank}(\partial_1) = 3$。

（第1行+第2行+第3行+第4行 = 0 向量，所以秩至多为 3；前3行线性无关，所以秩恰为 3。）

**边界算子 $\partial_2$**（$8 \times 4$ 矩阵，行=边，列=面）：

每个面的边界（四条边）：
- $\partial_2(f_0) = e_0 + e_5 + e_2 + e_4$
- $\partial_2(f_1) = e_1 + e_4 + e_3 + e_5$（注意周期性边界使得 $f_1$ 右边和下面连回去）
- $\partial_2(f_2) = e_2 + e_7 + e_0 + e_6$（$f_2$ 下面连回顶部）
- $\partial_2(f_3) = e_3 + e_6 + e_1 + e_7$

$$\partial_2 = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{pmatrix}$$

**$\partial_2$ 的秩**：列1+列2+列3+列4 = 0，列1+列3 = 0（即列1=列3），列2+列4 = 0（即列2=列4），所以秩为 2。

$$\operatorname{rank}(\partial_2) = 2$$

**验证 $\partial_1 \partial_2 = 0$**：可以直接矩阵乘法验证，每列都是零向量。$\checkmark$

**计算同调群**：

$$\dim Z_1 = \dim C_1 - \operatorname{rank}(\partial_1) = 8 - 3 = 5$$

$$\dim B_1 = \operatorname{rank}(\partial_2) = 2$$

$$\boxed{\beta_1 = \dim H_1 = \dim Z_1 - \dim B_1 = 5 - 2 - ??? }$$

等等，这里需要更仔细。$\dim H_1 = \dim Z_1 - \dim B_1 = 5 - 2 = 3$？让我们用 Euler 示性数交叉验证。

$$\chi = \beta_0 - \beta_1 + \beta_2 = 0$$

$\beta_0$：$\dim Z_0 = 4$（所有 0-chain 都是 cycle），$\dim B_0 = \operatorname{rank}(\partial_1) = 3$，所以 $\beta_0 = 4 - 3 = 1$。$\checkmark$（连通）

$\beta_2$：$\dim Z_2 = \dim C_2 - \operatorname{rank}(\partial_2) = 4 - 2 = 2$。但 $B_2 = \operatorname{im} \partial_3 = 0$（没有 3-chain），所以 $\beta_2 = 2$？

这也不对。让我们重新检查 $\partial_2$ 的核。

$\ker \partial_2$：我们需要 $\partial_2 c = 0$。设 $c = a_0 f_0 + a_1 f_1 + a_2 f_2 + a_3 f_3$。

从 $\partial_2$ 矩阵的列结构（列1=列3，列2=列4），$\ker \partial_2$ 的基为 $\{f_0 + f_2, \, f_1 + f_3\}$？不对，让我重新检查。

$a_0 \partial_2(f_0) + a_1 \partial_2(f_1) + a_2 \partial_2(f_2) + a_3 \partial_2(f_3) = 0$

利用 $\partial_2$ 矩阵，对每行列出方程（$\mathbb{F}_2$ 上）：

- $e_0$行：$a_0 + a_2 = 0$
- $e_1$行：$a_1 + a_3 = 0$
- $e_2$行：$a_0 + a_2 = 0$（与 $e_0$ 相同）
- $e_3$行：$a_1 + a_3 = 0$（与 $e_1$ 相同）
- $e_4$行：$a_0 + a_1 = 0$
- $e_5$行：$a_0 + a_1 = 0$（与 $e_4$ 相同）
- $e_6$行：$a_2 + a_3 = 0$
- $e_7$行：$a_2 + a_3 = 0$（与 $e_6$ 相同）

独立方程：$a_0 = a_2$，$a_1 = a_3$，$a_0 = a_1$。

所以 $a_0 = a_1 = a_2 = a_3$，$\ker \partial_2 = \operatorname{span}\{f_0 + f_1 + f_2 + f_3\}$。

$$\dim Z_2 = \dim \ker \partial_2 = 1$$

$$\beta_2 = \dim Z_2 - \dim B_2 = 1 - 0 = 1$$

现在重新计算 $\operatorname{rank}(\partial_2)$：$\dim C_2 - \dim \ker \partial_2 = 4 - 1 = 3$。

等一下，让我再验证。$\operatorname{im} \partial_2$ 的维数 = $\operatorname{rank}(\partial_2) = 4 - 1 = 3$。

那么 $\beta_1 = \dim Z_1 - \dim B_1 = (8 - 3) - 3 = 5 - 3 = 2$。

验证 Euler：$\chi = 1 - 2 + 1 = 0$。$\checkmark$ 完美！

$$\boxed{H_0(T^2) \cong \mathbb{F}_2, \quad H_1(T^2) \cong \mathbb{F}_2^2, \quad H_2(T^2) \cong \mathbb{F}_2}$$

$$(\beta_0, \beta_1, \beta_2) = (1, 2, 1)$$

**$H_1(T^2) \cong \mathbb{F}_2^2$ 的代表元**：

$Z_1$ 是5维的，$B_1$ 是3维的。$H_1 = Z_1 / B_1$ 是2维的。我们需要找到两个 1-cycle，它们不是边界，且彼此不同调。

- **水平环** $\gamma_h = e_0 + e_1$：这是沿水平方向绕环面一圈的路径。$\partial_1(\gamma_h) = (v_0 + v_1) + (v_1 + v_0) = 0$，确实是 cycle。
- **垂直环** $\gamma_v = e_4 + e_6$：这是沿垂直方向绕环面一圈的路径。$\partial_1(\gamma_v) = (v_0 + v_2) + (v_2 + v_0) = 0$，确实是 cycle。

这两个环都不是任何面集合的边界（不能通过合并面来得到），而且它们对应环面上两个独立的"洞"。$\gamma_h$ 和 $\gamma_v$ 的同调类 $[\gamma_h], [\gamma_v]$ 构成 $H_1(T^2; \mathbb{F}_2)$ 的一组基。

**与环面码的联系**：
- 物理量子比特数 $n = \dim C_1 = 8 = 2 \times 2^2 = 2L^2$
- 逻辑量子比特数 $k = \beta_1 = 2$
- 逻辑 $\bar{Z}$ 算子对应 $[\gamma_h]$ 和 $[\gamma_v]$
- 码距 $d = L = 2$（最短非平凡环的长度）

---

### Step 9: Summary of Key Results（关键结果总结）

| 空间 | $\beta_0$ | $\beta_1$ | $\beta_2$ | $\chi$ | 含义 |
|------|-----------|-----------|-----------|--------|------|
| 圆盘（平面格子） | 1 | 0 | 0 | 1 | 无洞，不能编码逻辑比特 |
| 圆 $S^1$ | 1 | 1 | 0 | 0 | 1个环（经典重复码） |
| 球面 $S^2$ | 1 | 0 | 1 | 2 | 无1维洞 |
| 环面 $T^2$ | 1 | 2 | 1 | 0 | **2个独立环 → 编码2个逻辑量子比特** |
| 亏格-$g$ 曲面 | 1 | $2g$ | 1 | $2-2g$ | **$2g$ 个独立环 → 编码 $2g$ 个逻辑量子比特** |

核心结论：拓扑量子码的编码能力完全由底层流形的同调决定：

$$k = \dim H_1(M; \mathbb{F}_2) = \beta_1$$

---

## Connection to Topological Codes（与拓扑码的联系预览）

详见 [topological_codes_connection.md]。

简要对应：
- 链群 $C_1$ → 物理量子比特的集合
- $B_1 = \operatorname{im} \partial_2$ → $Z$-stabilizer 的生成空间
- $B^1 = \operatorname{im} \delta^0 = \operatorname{im} \partial_1^T$ → $X$-stabilizer 的生成空间
- $Z_1 \setminus B_1$ → 非平凡逻辑 $Z$ 算子
- $Z^1 \setminus B^1$ → 非平凡逻辑 $X$ 算子
- $H_1 = Z_1 / B_1$ → 逻辑 $Z$ 算子的等价类
- 码距 $d$ = 最短非平凡同调类代表元的重量

---

## From Bombin: Formal Homology for Surface Codes

### $\mathbb{Z}_2$-Chain Groups **[Bombin, §3]**

Given a lattice on a surface with vertices $V$, edges $E$, faces $F$:
- $C_i \simeq \mathbb{Z}_2^{|i\text{-cells}|}$ ($i = 0, 1, 2$)
- A 1-chain $c = \sum_i c_i e_i$ with $c_i \in \{0,1\}$ represents a set of edges
- Addition: $e_i + e_i = 0$ (edges cancel in pairs)

### Boundary Operators **[Bombin, §3]**

$\partial_2: C_2 \to C_1$ maps faces to their boundary edges. $\partial_1: C_1 \to C_0$ maps edge sets to their boundary vertices (vertices where an odd number of edges meet). The fundamental property:

$$\partial^2 := \partial_1 \circ \partial_2 = 0$$

### First Homology Group **[Bombin, §3, Eq.(10)]**

$$H_1 := Z_1 / B_1 = \ker(\partial_1) / \operatorname{im}(\partial_2)$$

For a closed orientable surface of genus $g$: $H_1 \simeq \mathbb{Z}_2^{2g}$ **[Bombin, §3, Eq.(11)]**.

### Euler Characteristic **[Bombin, §3, Eq.(1-2)]**

$$\chi = V - E + F = 2(1 - g)$$

This is a topological invariant independent of the particular lattice. For the surface code, the number of encoded qubits is:

$$k = E - (V + F - 2) = 2 - \chi = 2g$$

---

## From Dennis et al.: Homology in Error Recovery

### 1-Chains as Error Patterns **[Dennis et al. 2002, §3.1]**

An error chain $E$ is a $\mathbb{Z}_2$-valued 1-chain where $n_E(\ell) = 1$ for each occupied link. The syndrome $S$ reveals the boundary $\partial E$. Recovery succeeds if the hypothesized chain $E'$ satisfies $E + E' \in B_1$ (homologically trivial). Recovery fails if $E + E'$ is homologically non-trivial **[Dennis et al. 2002, §3.3]**.

### Relative Homology for Planar Codes **[Dennis et al. 2002, §2.2]**

For planar codes, cycles relative to rough edges come in two types: trivial (boundaries relative to the rough edge) and non-trivial (chains stretching between rough edges). The relative first homology group captures the logical operators of the planar code.

---

## References

1. Hatcher, A. *Algebraic Topology*. Cambridge University Press, 2002. Chapter 2.
2. Kitaev, A. Y. "Fault-tolerant quantum computation by anyons." *Ann. Phys.* 303, 2-30 (2003).
3. Bombin, H. "An Introduction to Topological Quantum Codes." In: *Quantum Error Correction*, Cambridge UP (2013).
4. Dennis, E., Kitaev, A., Landahl, A. & Preskill, J. "Topological quantum memory." *J. Math. Phys.* 43, 4452 (2002).
5. Bredon, G. E. *Topology and Geometry*. Springer, 1993.
6. Fujii, K. "Quantum Computation with Topological Codes." SpringerBriefs (2015), Ch.3 §3.1.

---

## Additions from Fujii's "Quantum Computation with Topological Codes" (2015)

### $\mathbf{Z}_2$ Chain Complex Formalism [Fujii, Ch.3, §3.1]

> **[Fujii, Ch.3, §3.1]**: 曲面 $G=(V,E,F)$ 上的 $\mathbf{Z}_2$ 链复形。$C_i$ 是以 $i$ 维元素为基的 $\mathbf{Z}_2$ 向量空间。边界算子 $\partial_i: C_i \to C_{i-1}$ 满足 $\partial_i \circ \partial_{i-1} = 0$。cycle 定义为 $\ker(\partial_i)$，trivial cycle 为 $\mathrm{Img}(\partial_{i+1})$。同调群：
>
> $$h_i = \ker(\partial_i) / \mathrm{Img}(\partial_{i+1})$$
>
> 同调等价：$c_i$ 和 $c'_i$ 属于同一同调类当存在 $(i+1)$-chain $c_{i+1}$ 使得 $c_i = c'_i + \partial c_{i+1}$。

### Dual Lattice and Adjoint Relation [Fujii, Ch.3, §3.1]

> **[Fujii, Ch.3, §3.1]**: 对偶曲面 $\bar{G} = (\bar{V}, \bar{E}, \bar{F})$，其中 $\bar{V}=F$, $\bar{E}=E$, $\bar{F}=V$。对偶关系的矩阵表示：
>
> $$M(\partial_1) = M(\bar{\partial}_2)^T, \quad M(\partial_2) = M(\bar{\partial}_1)^T$$
>
> **伴随关系** [Fujii, Ch.3, Eq.(3.7)]：$(M(\partial_i)c_i)\cdot c_{i-1} = c_i \cdot (M(\partial_i)^T c_{i-1})$

> **[Fujii, Ch.3, Eq.(3.8)]**: 由 $\partial_1\circ\partial_2 = 0$ 得到核心对易性结论：对任何原始和对偶 2-chain，$\bar{\partial}\bar{c}_2 \cdot \partial c_2 = 0$，即 $X(\partial c_2)$ 和 $Z(\bar{\partial}\bar{c}_2)$ 总是对易。这是表面码稳定子对易性的拓扑根源。

### Inner Product and Commutation [Fujii, Ch.3, §3.1]

> **[Fujii, Ch.3, §3.1]**: 两个 1-chain $c_1$, $c'_1$ 定义的算子 $X(c_1)$ 和 $Z(c'_1)$ 的对易性由内积 $c_1 \cdot c'_1 \equiv \sum_l z_l z'_l \pmod{2}$ 决定。此外：
>
> $$c_1 \cdot \bar{\partial}_2\bar{c}_2 = \partial c_1 \cdot \bar{c}_2$$
>
> 这给出判断任意 1-chain 算子与稳定子对易性的便捷公式。

### Relative Homology for Planar Codes [Fujii, Ch.3, §3.3.2]

> **[Fujii, Ch.3, §3.3.2]**: 平面码使用**相对同调**处理边界。在边界处定义 1-chain 集合 $\Gamma_1 \subset C_1$（对应边界稳定子），两链 $c_i$ 和 $c'_i$ 相对同调等价当：
>
> $$c'_i = c_i + \partial c_{i+1} + \gamma_i, \quad \gamma_i \in \Gamma_i$$
>
> 光滑边界（smooth boundary）处 $X$ 算子可终止，粗糙边界（rough boundary）处 $Z$ 算子可终止。逻辑算子对应连接不同类型边界的相对非平凡 cycle。

### Euler Characteristic and Code Parameters [Fujii, Ch.3, §3.3]

> **[Fujii, Ch.3, §3.3]**: 对一般 tiling $G=(V,E,F)$ 定义在亏格 $g$ 曲面上：
>
> $$|F|+|V|-|E| = 2-2g \quad \Rightarrow \quad k = |E|-(|F|+|V|-2) = 2g$$
>
> 逻辑量子比特数等于曲面同调群 $h_1$ 的维度 $2g$。环面（$g=1$）编码 2 个逻辑量子比特，平面（$g=0$，带边界）通过缺陷引入逻辑量子比特。
