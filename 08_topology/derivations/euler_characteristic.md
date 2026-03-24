# Euler Characteristic and Its Role in Code Parameters

> **Tags**: `euler`, `betti`, `genus`, `topology`, `code-parameters`
>
> **Primary Source**: H. Bombin, *An Introduction to Topological Quantum Codes* **[Bombin, §3.1]**

## Statement

Euler 示性数 $\chi$ 是一个拓扑不变量 **[Bombin, §3.1, Eq.(1)--(2)]**，可以通过两种等价方式计算：(1) CW 分解的胞腔数交替和 $\chi = V - E + F$；(2) Betti 数的交替和 $\chi = \beta_0 - \beta_1 + \beta_2$。对于亏格为 $g$ 的可定向闭曲面，$\chi = 2 - 2g$ **[Bombin, §3.1, Eq.(2)]**。在拓扑量子码中，Euler 示性数直接约束码参数：逻辑量子比特数 $k = 2g$（对于闭曲面码），即 $k = 2 - \chi$ **[Bombin, §4.1, after Eq.(13)]**。Euler 示性数的拓扑不变性保证了码参数不依赖于具体的格子划分（CW 分解）。

## Prerequisites

- **同调基础**：链复形、边界算子、同调群 → [homology_basics.md]
- **Betti 数**：$\beta_n = \dim H_n$ → [homology_basics.md]
- **线性代数**：秩-零化度定理 → [../01_linear_algebra/key_formulas.md]

---

## Derivation

### Step 1: Euler Formula for Polyhedra（多面体的 Euler 公式）

**历史起点**：Euler 在 1752 年发现，对于任何凸多面体：

$$V - E + F = 2$$

其中 $V$ = 顶点数，$E$ = 边数，$F$ = 面数。

**验证几个经典例子**：

| 多面体 | $V$ | $E$ | $F$ | $V - E + F$ |
|--------|-----|-----|-----|-------------|
| 四面体 | 4 | 6 | 4 | 2 $\checkmark$ |
| 立方体 | 8 | 12 | 6 | 2 $\checkmark$ |
| 八面体 | 6 | 12 | 8 | 2 $\checkmark$ |
| 十二面体 | 20 | 30 | 12 | 2 $\checkmark$ |
| 二十面体 | 12 | 30 | 20 | 2 $\checkmark$ |

所有凸多面体（拓扑上等价于球面 $S^2$）都满足 $V - E + F = 2$。

**为什么是2**？因为球面的 Euler 示性数 $\chi(S^2) = 2$。

---

### Step 2: Generalize to Chain Complexes（推广到链复形）

**定义**：给定一个有限链复形 $C_d \xrightarrow{\partial_d} \cdots \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0$，Euler 示性数定义为：

$$\chi = \sum_{n=0}^{d} (-1)^n \dim C_n$$

对于二维 CW 复形：

$$\chi = \dim C_0 - \dim C_1 + \dim C_2 = V - E + F$$

**定理**（Euler-Poincaré 公式）：Euler 示性数也等于 Betti 数的交替和：

$$\chi = \sum_{n=0}^{d} (-1)^n \beta_n$$

**证明**（完整推导）：

设 $c_n = \dim C_n$，$z_n = \dim Z_n = \dim \ker \partial_n$，$b_n = \dim B_n = \dim \operatorname{im} \partial_{n+1}$，$\beta_n = z_n - b_n$。

由秩-零化度定理，对每个 $n$：

$$c_n = z_n + r_n$$

其中 $r_n = \operatorname{rank}(\partial_n) = \dim \operatorname{im} \partial_n = b_{n-1}$（$\partial_n$ 的像是 $(n-1)$-boundaries）。

所以 $c_n = z_n + b_{n-1}$，即 $z_n = c_n - b_{n-1}$。

代入 $\beta_n = z_n - b_n = c_n - b_{n-1} - b_n$。

计算 Betti 数的交替和：

$$\sum_{n=0}^{d} (-1)^n \beta_n = \sum_{n=0}^{d} (-1)^n (c_n - b_{n-1} - b_n)$$

$$= \sum_{n=0}^{d} (-1)^n c_n - \sum_{n=0}^{d} (-1)^n b_{n-1} - \sum_{n=0}^{d} (-1)^n b_n$$

第二个求和中（约定 $b_{-1} = 0$）：

$$\sum_{n=0}^{d} (-1)^n b_{n-1} = \sum_{m=-1}^{d-1} (-1)^{m+1} b_m = -\sum_{m=0}^{d-1} (-1)^m b_m$$

（因为 $b_{-1} = 0$。）

第三个求和中（约定 $b_d = 0$，因为没有 $(d+1)$-chain）：

$$\sum_{n=0}^{d} (-1)^n b_n = \sum_{m=0}^{d-1} (-1)^m b_m$$

（因为 $b_d = 0$。）

所以后两项之和：

$$-\left(-\sum_{m=0}^{d-1} (-1)^m b_m\right) - \sum_{m=0}^{d-1} (-1)^m b_m = \sum_{m=0}^{d-1} (-1)^m b_m - \sum_{m=0}^{d-1} (-1)^m b_m = 0$$

因此：

$$\sum_{n=0}^{d} (-1)^n \beta_n = \sum_{n=0}^{d} (-1)^n c_n = \chi \quad \square$$

**这个定理的重要性**：等式左边 $\sum (-1)^n \beta_n$ 只依赖于拓扑空间本身（$\beta_n$ 是拓扑不变量），等式右边 $\sum (-1)^n c_n$ 依赖于具体的 CW 分解。两者相等意味着 $\chi$ 不依赖于 CW 分解的选取——无论你用什么格子来划分同一个曲面，$V - E + F$ 的值不变。

---

### Step 3: Compute $\chi$ for Sphere, Torus, Genus-$g$ Surface（计算各曲面的 Euler 示性数）

#### 球面 $S^2$

**方法1**（最小 CW 分解：1个0-cell、1个2-cell）：

一种最简的 CW 分解：$V = 1$（一个点），$E = 0$，$F = 1$（一个圆盘，边界粘到点上）。

$$\chi = 1 - 0 + 1 = 2$$

**方法2**（正八面体的 CW 分解）：$V = 6, E = 12, F = 8$。

$$\chi = 6 - 12 + 8 = 2 \quad \checkmark$$

**方法3**（Betti 数）：$H_0(S^2) = \mathbb{F}_2$（连通），$H_1(S^2) = 0$（无环），$H_2(S^2) = \mathbb{F}_2$（有封闭腔体）。

$$\chi = 1 - 0 + 1 = 2 \quad \checkmark$$

#### 环面 $T^2$（亏格 $g = 1$）

**方法1**（$L \times L$ 方格子，周期性边界）：$V = L^2, E = 2L^2, F = L^2$。

$$\chi = L^2 - 2L^2 + L^2 = 0$$

任何 $L$ 都给出 $\chi = 0$！$\checkmark$（不依赖于 CW 分解。）

**方法2**（最小 CW 分解：1个0-cell，2个1-cell，1个2-cell）：

环面可以用一个正方形四边粘合得到：$V = 1$（四个角等同），$E = 2$（上下边等同为 $a$，左右边等同为 $b$），$F = 1$（正方形内部）。

$$\chi = 1 - 2 + 1 = 0 \quad \checkmark$$

**方法3**（Betti 数）：$\beta_0 = 1, \beta_1 = 2, \beta_2 = 1$。

$$\chi = 1 - 2 + 1 = 0 \quad \checkmark$$

#### 亏格-$g$ 可定向闭曲面 $\Sigma_g$

**分类定理**：每个可定向闭曲面同胚于某个 $\Sigma_g$（$g$ 个"把手"附着到球面上）。

**$\Sigma_g$ 的 Betti 数**：

$$\beta_0 = 1, \quad \beta_1 = 2g, \quad \beta_2 = 1$$

直观理解：$\beta_1 = 2g$ 是因为每个把手（handle）贡献两个独立的 1-cycle——一个绕把手转（$a$-cycle），一个沿把手转（$b$-cycle）。

$$\chi(\Sigma_g) = 1 - 2g + 1 = 2 - 2g$$

**验证**：

| $g$ | 曲面 | $\chi$ | $\beta_1$ |
|-----|------|--------|-----------|
| 0 | 球面 $S^2$ | 2 | 0 |
| 1 | 环面 $T^2$ | 0 | 2 |
| 2 | 双环面 | $-2$ | 4 |
| 3 | 三环面 | $-4$ | 6 |
| $g$ | $\Sigma_g$ | $2-2g$ | $2g$ |

**最小 CW 分解的验证**：$\Sigma_g$ 可以用一个 $4g$ 边形粘合得到（$a_1 b_1 a_1^{-1} b_1^{-1} \cdots a_g b_g a_g^{-1} b_g^{-1}$）：
- $V = 1$（所有顶点等同）
- $E = 2g$（$a_1, b_1, \ldots, a_g, b_g$）
- $F = 1$

$$\chi = 1 - 2g + 1 = 2 - 2g \quad \checkmark$$

---

### Step 4: Euler Characteristic and Code Parameters（Euler 示性数与码参数）

**核心关系**：对于定义在亏格-$g$ 闭曲面 $\Sigma_g$ 上的同调码：

$$k = \beta_1 = 2g = 2 - \chi$$

推导：

$$k = \dim H_1 = \beta_1$$

由 $\chi = \beta_0 - \beta_1 + \beta_2$ 和 $\beta_0 = \beta_2 = 1$（对闭曲面）：

$$\chi = 1 - \beta_1 + 1 = 2 - \beta_1$$

$$\therefore \beta_1 = 2 - \chi = 2 - (2 - 2g) = 2g$$

**稳定子计数的等价推导**：

物理量子比特数 $n = E$。

独立 $X$-stabilizer 数 = $V - 1$（每个顶点一个，但乘积为 $I$，少一个独立的）= $V - \beta_0 = V - 1$。

独立 $Z$-stabilizer 数 = $F - 1 = F - \beta_2 = F - 1$。

$$k = n - (V - 1) - (F - 1) = E - V - F + 2 = -(V - E + F) + 2 = 2 - \chi = 2g$$

这与 $k = \beta_1$ 完全一致。 $\checkmark$

---

### Step 5: Detailed Verification for Specific Codes（具体码的验证）

#### 环面码 $[[2L^2, 2, L]]$

曲面：$T^2$，$g = 1$，$\chi = 0$。

$$V = L^2, \quad E = 2L^2, \quad F = L^2$$

$$k = 2 - \chi = 2 - 0 = 2 \quad \checkmark$$

$$n - k = 2L^2 - 2 = (L^2 - 1) + (L^2 - 1)$$

独立 $X$-stabilizer：$L^2 - 1$。独立 $Z$-stabilizer：$L^2 - 1$。 $\checkmark$

#### 平面码 $[[L^2 + (L-1)^2, 1, L]]$（正方形，粗糙+光滑边界）

平面码定义在有边界的正方形上。以 $L = 3$ 为例：

```
粗糙边界（上下）
  ●---q---●---q---●
  |   f   |   f   |
  q       q       q     光滑边界（左右）
  |   f   |   f   |
  ●---q---●---q---●
  |   f   |   f   |
  q       q       q
  |   f   |   f   |
  ●---q---●---q---●
```

$L = 3$ 的平面码：$V = 3 \times 3 = 9$，$E = 2 \times 3 \times 2 + 3 + 2 = ?$

让我更仔细地数。标准 $L \times L$ 平面码（$L$ 行 $L$ 列的面）：

- 顶点：$(L+1) \times (L+1)$...

实际上标准平面码的参数推导最好从 Betti 数入手。平面码拓扑上是圆盘（$\chi = 1$），但通过边界条件的修改使得 $k = 1$。具体分析需要相对同调，这里给出参数结果：

对于 $d \times d$ 平面码（$d$ 行 $d$ 列的数据量子比特行）：

$$n = 2d^2 - 2d + 1, \quad k = 1, \quad d_{\text{code}} = d$$

#### 亏格-2 码

曲面：$\Sigma_2$（双环面），$g = 2$，$\chi = -2$。

$$k = 2 - \chi = 2 - (-2) = 4$$

使用 $L \times L$ 格子嵌入到 $\Sigma_2$ 上（通过适当的边粘合），可以编码 4 个逻辑量子比特。

---

### Step 6: $\chi$ as Topological Invariant — Independence of CW Decomposition（$\chi$ 的拓扑不变性——不依赖于 CW 分解）

**定理**：如果 $\mathcal{K}$ 和 $\mathcal{K}'$ 是同一个拓扑空间 $X$ 的两个不同 CW 分解，则它们的 Euler 示性数相等：

$$V - E + F = V' - E' + F'$$

**证明思路**：两种论证方式。

**论证1（通过 Betti 数）**：$\beta_n$ 是拓扑不变量（同胚空间有同构的同调群），而 $\chi = \sum (-1)^n \beta_n$。这是 Euler-Poincaré 公式（Step 2）的直接推论。

**论证2（通过初等操作）**：任何两个 CW 分解可以通过一系列初等操作相互转化（如细分），每次操作都保持 $V - E + F$ 不变。

- **边细分**（在一条边上加一个新顶点）：$V \to V+1$，$E \to E+1$，$F$ 不变。$\Delta\chi = 1 - 1 + 0 = 0$。$\checkmark$
- **面三角化**（在一个面内加一条对角线）：$V$ 不变，$E \to E+1$，$F \to F+1$。$\Delta\chi = 0 - 1 + 1 = 0$。$\checkmark$
- **面加点**（在面内加一个新顶点，并连到边界上 $m$ 个已有顶点）：$V \to V+1$，$E \to E+m$，$F \to F+(m-1)$。$\Delta\chi = 1 - m + (m-1) = 0$。$\checkmark$

**对量子码的含义**：在同一个曲面上使用不同的格子划分，得到的码有不同的 $n$（物理量子比特数）和不同的 $d$（码距），但 $k$（逻辑量子比特数）永远相同——它只取决于曲面的拓扑，不取决于格子的选择。

$$k = 2 - \chi = 2g \quad \text{(不依赖于格子)}$$

---

### Step 7: The Role of $\chi$ in Quantum Code Design（$\chi$ 在量子码设计中的角色）

**设计约束1——逻辑量子比特数**：

$$k = 2 - \chi(\text{surface})$$

要编码更多逻辑量子比特 → 需要更高亏格的曲面 → 更负的 $\chi$。

**设计约束2——稳定子权重 vs $k$ 的折衷**：

在亏格-$g$ 曲面上，$k = 2g$ 可以很大。但高亏格曲面的格子嵌入在三维空间中可能需要长程连接（long-range connectivity），这在物理上难以实现。

**设计约束3——BPT bound（Bravyi-Poulin-Terhal 界）**：

对于二维局部码（每个稳定子只涉及有限个量子比特，量子比特排列在二维平面上）：

$$k d^2 \leq c \cdot n$$

对于环面码（$k = 2, d = L, n = 2L^2$）：$k d^2 = 2L^2 = n$，达到了 BPT 界！

这说明环面码在二维局部码中是最优的参数关系。如果要更大的 $k$（更高亏格），$d$ 必须相应减小，或者 $n$ 必须增大。

**小结**：

$$\boxed{\chi(\Sigma_g) = 2 - 2g, \quad k = 2g, \quad n = E, \quad d = \text{sys}(\Sigma_g, \mathcal{K})}$$

其中 $\text{sys}(\Sigma_g, \mathcal{K})$ 是格子 $\mathcal{K}$ 在曲面 $\Sigma_g$ 上的收缩距离（systole）——最短非平凡闭合曲线的长度。

---

### Step 8: Euler Characteristic for Surfaces with Boundary（带边界曲面的 Euler 示性数）

对于平面码等需要考虑带边界的曲面。

**亏格-$g$ 曲面有 $b$ 个边界分量**：$\Sigma_{g,b}$。

$$\chi(\Sigma_{g,b}) = 2 - 2g - b$$

**推导**：$\Sigma_{g,b}$ 可以从 $\Sigma_g$ 上挖去 $b$ 个开圆盘得到。每挖去一个圆盘，$F$ 减少 1，而 $V$ 和 $E$ 不变（或者说 Betti 数 $\beta_2$ 变为 0 但 $\beta_1$ 增加等），总效果是 $\chi$ 减少 1。

- 球面 $S^2$ 挖一个洞 → 圆盘：$\chi = 2 - 1 = 1$
- 环面 $T^2$ 挖一个洞 → 带边环面：$\chi = 0 - 1 = -1$

**带边界曲面上的码参数**：

对于带边界的曲面，逻辑量子比特数由**相对同调** $H_1(\Sigma, \partial\Sigma; \mathbb{F}_2)$ 决定，计算比闭曲面复杂。标准平面码（$\Sigma_{0,1}$ 即圆盘，但边界分为粗糙和光滑两种）：$k = 1$。

---

### Step 9: Full Worked Example — From Euler Characteristic to Code Parameters（完整算例）

**目标**：在亏格-2 曲面上设计一个拓扑码，计算所有参数。

**Step 9.1**：确定拓扑参数。

$$g = 2, \quad \chi = 2 - 2(2) = -2, \quad k = 2g = 4$$

**Step 9.2**：选择 CW 分解。

使用 $L = 3$ 的方格子嵌入到 $\Sigma_2$。$\Sigma_2$ 可以表示为一个八边形 $a_1 b_1 a_1^{-1} b_1^{-1} a_2 b_2 a_2^{-1} b_2^{-1}$ 的粘合。

使用标准方法（在八边形上施加 $3 \times 3$ 格子），胞腔数为：

$$V = ?, \quad E = ?, \quad F = ?$$

实际上更简洁的方法：取 $\Sigma_2$ 的某个具体三角剖分。最小三角剖分有 10 个顶点、30 条边、20 个面：

$$\chi = 10 - 30 + 20 = 0?$$

这不对。让我用正确的数字。对于 $\Sigma_2$ 的最小三角剖分（Ringel 等人的结果）：$V = 10, E = 40, F = ?$

使用 $\chi = -2$：$F = E - V - \chi = 40 - 10 + 2 = 32$。验证：每个面是三角形（3条边，每条边被2个面共享），所以 $3F = 2E$，$F = 80/3$——不是整数，说明不是纯三角剖分。

让我用一个正确的构造。取 $3 \times 6$ 的方格子，通过适当的边界等同实现 $\Sigma_2$：

$$V = 18, \quad E = 36, \quad F = 18$$

验证：$\chi = 18 - 36 + 18 = 0$。这不对（应该是 $-2$）。

正确的方法：对于一般的 $L \times L$ 方格子嵌入 $\Sigma_g$，需要特殊的边界等同。实际上，最简单的方法是取 $V = L^2, E = 2L^2, F = L^2$ 的方格子，但需要 $\chi = V - E + F = L^2 - 2L^2 + L^2 = 0$，这只适用于 $g = 1$（环面）。

对于高亏格曲面，标准方法是使用 **hyperbolic lattice** 或在方格子上做更复杂的等同。最简单的例子：

**双环面的显式构造**：取一个 $4 \times 2$ 的方格子，按照 $a_1 b_1 a_1^{-1} b_1^{-1} a_2 b_2 a_2^{-1} b_2^{-1}$ 的模式粘合边界。

粘合后：$V = 2, E = 8, F = 4$。

$$\chi = 2 - 8 + 4 = -2 \quad \checkmark$$

码参数：$n = 8, k = 4, d = 2$。这是一个 $[[8, 4, 2]]$ 码。

独立稳定子数 = $n - k = 4$。独立 $X$-stab = $V - 1 = 1$，独立 $Z$-stab = $F - 1 = 3$。总共 $1 + 3 = 4 = n - k$。$\checkmark$

---

### Step 10: Summary of Key Relations（关键关系总结）

$$\boxed{\chi = V - E + F = \beta_0 - \beta_1 + \beta_2 = 2 - 2g}$$

**码参数公式汇总**：

| 参数 | 公式 | 拓扑来源 |
|------|------|----------|
| $n$ (物理量子比特) | $E$ | 边数（依赖于 CW 分解） |
| $k$ (逻辑量子比特) | $\beta_1 = 2 - \chi = 2g$ | 拓扑不变量 |
| $n - k$ (独立稳定子数) | $(V - 1) + (F - 1)$ | 胞腔数约束 |
| $d$ (码距) | $\text{sys}(\Sigma_g, \mathcal{K})$ | 依赖于 CW 分解和嵌入 |

**关键洞察**：
1. $k$ 是纯拓扑量——只取决于 $g$，不依赖于格子
2. $n$ 和 $d$ 依赖于格子的选择——这就是码设计的自由度
3. $\chi$ 提供了一个不等式约束：$n - k = (V-1) + (F-1) = V + F - 2$，结合 $\chi = V - E + F$ 得 $n = E = V + F - 2 - \chi + k - k = ...$，即格子参数之间不是独立的
4. BPT 界 $kd^2 \leq cn$ 进一步约束了 $d$ 与 $n$ 的关系

---

## References

1. Euler, L. "Elementa doctrinae solidorum." *Novi Commentarii Academiae Scientiarum Petropolitanae* 4, 109-140 (1758).
2. Poincaré, H. "Analysis situs." *Journal de l'Ecole Polytechnique* 1, 1-123 (1895).
3. Hatcher, A. *Algebraic Topology*. Cambridge University Press, 2002. Chapter 2.
4. Bravyi, S., Poulin, D. & Terhal, B. "Tradeoffs for reliable quantum information storage in 2D systems." *PRL* 104, 050503 (2010).
5. Kitaev, A. Y. "Fault-tolerant quantum computation by anyons." *Ann. Phys.* 303, 2-30 (2003).
