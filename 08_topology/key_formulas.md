# Chapter 8: Topology - Key Formulas

> 代数拓扑核心公式速查表，聚焦于拓扑量子纠错码相关的同调理论。所有公式均使用 LaTeX 记号，解释使用中文。

---

## 链复形与同调

### F8.1: Chain Complex (链复形)

$$\cdots \xrightarrow{\partial_{n+2}} C_{n+1} \xrightarrow{\partial_{n+1}} C_n \xrightarrow{\partial_n} C_{n-1} \xrightarrow{\partial_{n-1}} \cdots$$

其中边界算子满足：

$$\partial_n \circ \partial_{n+1} = 0 \quad \forall n$$

链复形是一系列 Abel 群（或向量空间）$C_n$ 和群同态 $\partial_n: C_n \to C_{n-1}$ 的序列，核心性质是"边界的边界为零"。在拓扑码中，链群 $C_n$ 对应 $n$ 维胞腔上的链（如 $C_0$ = 顶点链，$C_1$ = 边链，$C_2$ = 面链），$\partial_n$ 描述高维对象的边界。

**Source**: [derivations/homology_basics.md] | Hatcher, *Algebraic Topology*, Ch. 2

---

### F8.2: Homology Group (同调群)

$$H_n = \ker \partial_n \, / \, \operatorname{im} \partial_{n+1} = Z_n \, / \, B_n$$

其中 $Z_n = \ker \partial_n$ 是 $n$ 维闭链（cycles）的集合，$B_n = \operatorname{im} \partial_{n+1}$ 是 $n$ 维边界链（boundaries）的集合。由于 $\partial^2 = 0$，有 $B_n \subseteq Z_n$，因此商群有定义。同调群度量的是"有多少闭链不是边界"——即空间中拓扑非平凡的"洞"。在拓扑码中，非平凡同调类恰好对应逻辑算子。

**Source**: [derivations/homology_basics.md] | Hatcher, *Algebraic Topology*, Ch. 2

---

### F8.3: Betti Numbers (Betti 数)

$$\beta_n = \dim H_n = \dim(\ker \partial_n) - \dim(\operatorname{im} \partial_{n+1})$$

第 $n$ 个 Betti 数 $\beta_n$ 是第 $n$ 个同调群的维度（或秩），直观上度量 $n$ 维"洞"的数量。$\beta_0$ = 连通分量个数，$\beta_1$ = 独立环的个数（1维洞），$\beta_2$ = 封闭腔体的个数（2维洞）。对于环面 $T^2$，有 $\beta_0 = 1, \beta_1 = 2, \beta_2 = 1$，其中 $\beta_1 = 2$ 直接对应环面码编码 2 个逻辑量子比特。

**Source**: [derivations/euler_characteristic.md] | Hatcher, *Algebraic Topology*, Ch. 2

---

### F8.4: Euler Characteristic (Euler 示性数)

$$\chi = \sum_{n=0}^{d} (-1)^n \beta_n = \sum_{n=0}^{d} (-1)^n \dim C_n$$

两个等价表达：(1) Betti 数的交替和；(2) 链群维数的交替和。对于二维曲面：

$$\chi = V - E + F$$

其中 $V, E, F$ 分别是顶点数、边数、面数。亏格为 $g$ 的可定向闭曲面满足 $\chi = 2 - 2g$。Euler 示性数是拓扑不变量，不依赖于具体的 CW 分解或三角剖分。

**Source**: [derivations/euler_characteristic.md] | Euler (1752); Hatcher, Ch. 2

---

## 格子上的拓扑结构

### F8.5: Boundary Operator on a Lattice (格子上的边界算子)

对于二维方格子（$\mathbb{F}_2$ 系数），边界算子的矩阵形式为：

$$(\partial_1)_{v,e} = \begin{cases} 1 & \text{if vertex } v \text{ is an endpoint of edge } e \\ 0 & \text{otherwise} \end{cases}$$

$$(\partial_2)_{e,f} = \begin{cases} 1 & \text{if edge } e \text{ is on the boundary of face } f \\ 0 & \text{otherwise} \end{cases}$$

在 $\mathbb{F}_2$（二元域）上工作时，所有运算取模 2，边的方向不重要。验证 $\partial_1 \circ \partial_2 = 0$：每条面的边界是一个闭合回路，其顶点各被访问偶数次（2次），在 $\mathbb{F}_2$ 上为 0。这正是表面码中稳定子对易性的拓扑来源。

**Source**: [derivations/homology_basics.md] | Kitaev, Ann. Phys. 303, 2 (2003)

---

### F8.6: Cycle Space and Boundary Space ($Z_n$ 和 $B_n$)

$$Z_n = \ker \partial_n = \{ c \in C_n : \partial_n(c) = 0 \}$$

$$B_n = \operatorname{im} \partial_{n+1} = \{ \partial_{n+1}(c') : c' \in C_{n+1} \}$$

**维数关系**（秩-零化度定理）：

$$\dim C_n = \dim Z_n + \dim(\operatorname{im} \partial_n) = \dim Z_n + \operatorname{rank}(\partial_n)$$

$$\dim Z_n = \dim B_n + \beta_n$$

$Z_1$（1-cycles）是无边界的边链集合——在格子上就是闭合回路。$B_1$（1-boundaries）是面的边界组成的回路。在表面码中，$Z_1$ 中的元素对应 $Z$ 型错误链必须形成闭环的约束，$B_1$ 中的元素对应可被稳定子纠正的平凡错误，$Z_1 / B_1$ 中的非平凡类对应逻辑 $Z$ 算子。

**Source**: [derivations/homology_basics.md] | Hatcher, Ch. 2

---

## 上同调与对偶

### F8.7: Cohomology Group and Cocycles (上同调群与上闭链)

上链群（cochain group）：

$$C^n = \operatorname{Hom}(C_n, \mathbb{F}_2)$$

上边界算子（coboundary operator）由边界算子的转置定义：

$$\delta^n = \partial_{n+1}^T : C^n \to C^{n+1}$$

上同调群：

$$H^n = \ker \delta^n \, / \, \operatorname{im} \delta^{n-1} = Z^n \, / \, B^n$$

其中 $Z^n = \ker \delta^n$ 是 $n$-cocycles，$B^n = \operatorname{im} \delta^{n-1}$ 是 $n$-coboundaries。在拓扑码中，上链复形对应对偶格子上的链复形：$Z$ 型稳定子是 boundaries，$X$ 型稳定子是 coboundaries；逻辑 $Z$ 是 homology class，逻辑 $X$ 是 cohomology class。

**Source**: [derivations/cohomology_basics.md] | Hatcher, Ch. 3

---

### F8.8: Poincaré Duality (Poincaré 对偶)

对于 $d$ 维可定向闭流形 $M$（$\mathbb{F}_2$ 系数下可推广到不可定向情形）：

$$H_n(M; \mathbb{F}_2) \cong H^{d-n}(M; \mathbb{F}_2) \cong H_{d-n}(M; \mathbb{F}_2)$$

特别地，对于二维环面 $T^2$（$d = 2$）：

$$H_0(T^2) \cong H^2(T^2) \cong \mathbb{F}_2, \quad H_1(T^2) \cong H^1(T^2) \cong \mathbb{F}_2^2, \quad H_2(T^2) \cong H^0(T^2) \cong \mathbb{F}_2$$

Poincaré 对偶的物理意义：环面码中 $X$ 型逻辑算子和 $Z$ 型逻辑算子之间存在天然对偶关系——一个对应 $H_1$，另一个对应 $H^1 \cong H_1$（在环面上同调与上同调同构）。这保证了逻辑 $X$ 和逻辑 $Z$ 的"对称地位"。

**Source**: [derivations/cohomology_basics.md] | Hatcher, Ch. 3; Poincaré (1895)

---

## 拓扑码联系

### F8.9: Homology and Code Distance (同调类与码距)

对于同调码（homological code），码距定义为：

$$d = \min\left( d_X, \, d_Z \right)$$

$$d_Z = \min_{[c] \neq 0 \in H_1} |c| = \min_{c \in Z_1 \setminus B_1} |c|$$

$$d_X = \min_{[\gamma] \neq 0 \in H^1} |\gamma| = \min_{\gamma \in Z^1 \setminus B^1} |\gamma|$$

其中 $|c|$ 表示链 $c$ 的 Hamming 重量（即涉及的边数/面数），最小化遍历所有非平凡同调类的代表元。$d_Z$ 是最短非平凡 1-cycle 的长度（在原格子上），$d_X$ 是最短非平凡 1-cocycle 的长度（等价于对偶格子上的最短非平凡 1-cycle）。对于 $L \times L$ 环面码，$d = L$，因为最短的非平凡环必须绕环面一周。

**Source**: [derivations/topological_codes_connection.md] | Kitaev, Ann. Phys. 303, 2 (2003)

---

### F8.10: Toric Code as Homological Code (环面码作为同调码)

在 $L \times L$ 环面上定义链复形 $C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0$，环面码的参数为：

$$[[n, k, d]] = [[2L^2, \; 2, \; L]]$$

各量的拓扑来源：

$$n = \dim C_1 = 2L^2 \quad \text{(边数 = 物理量子比特数)}$$

$$k = \dim H_1(T^2; \mathbb{F}_2) = \beta_1 = 2 \quad \text{(逻辑量子比特数 = 第一 Betti 数)}$$

$$d = \text{sys}(T^2) = L \quad \text{(码距 = 收缩距离/最短非平凡环)}$$

稳定子的拓扑定义：$Z$ 稳定子 = $\operatorname{im} \partial_2$（面的边界），$X$ 稳定子 = $\operatorname{im} \delta^0 = \operatorname{im} \partial_1^T$（顶点的上边界/对偶边界）。逻辑算子 $\bar{Z}$ = $H_1$ 的非平凡代表元，$\bar{X}$ = $H^1$ 的非平凡代表元。

**Source**: [derivations/topological_codes_connection.md] | Kitaev, Ann. Phys. 303, 2 (2003)

---

### F8.11: General Surface Code on Genus-$g$ Surface (亏格-$g$ 曲面上的一般表面码)

对于亏格为 $g$ 的可定向闭曲面 $\Sigma_g$：

$$k = \dim H_1(\Sigma_g; \mathbb{F}_2) = 2g$$

$$\chi(\Sigma_g) = 2 - 2g = V - E + F$$

更一般地，对于带边界的曲面（平面码）：

$$k = \dim H_1(\Sigma, \partial \Sigma; \mathbb{F}_2)$$

其中 $H_1(\Sigma, \partial \Sigma)$ 是相对同调群。对于标准平面码（一个正方形，交替的粗糙边界和光滑边界）：$k = 1$，因为只有一个拓扑非平凡的路径类——从一侧粗糙边界到另一侧。

**Source**: [derivations/topological_codes_connection.md] | Freedman & Meyer, Found. Comput. Math. 1, 325 (2001)

---

### F8.12: Rank-Nullity for Boundary Operators (边界算子的秩-零化度关系)

$$\dim C_n = \operatorname{rank}(\partial_n) + \dim(\ker \partial_n)$$

等价地：

$$\dim C_n = \dim B_{n-1} + \dim Z_n = \dim B_{n-1} + \dim B_n + \beta_n$$

对环面码的约束计数：物理量子比特数 $n = \dim C_1$，独立稳定子生成元数 $= \dim B_0 + \dim B_1 = \operatorname{rank}(\partial_1) + \operatorname{rank}(\partial_2)$，逻辑量子比特数 $k = \beta_1 = \dim C_1 - \operatorname{rank}(\partial_1) - \operatorname{rank}(\partial_2)$。这给出 $n - k = $ 独立稳定子数，与稳定子形式体系完全一致。

**Source**: [derivations/homology_basics.md] | 线性代数基本定理
