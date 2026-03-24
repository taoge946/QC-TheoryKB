# Surface Code Basics

> **Tags**: `surface-code`, `qec`, `stabilizer`, `topological`

## Statement

表面码（Surface Code）是一族定义在二维方格子上的拓扑稳定子码。量子比特放置在格子的边上，$X$ 型稳定子定义在顶点上，$Z$ 型稳定子定义在面上。表面码的关键特性包括：局部稳定子（每个稳定子只涉及相邻的少量量子比特）、码距与格子尺寸成正比、以及逻辑算子对应跨越格子的拓扑非平凡路径。

## Prerequisites

- **稳定子形式体系**：[stabilizer_formalism.md]
- **图论基础**：图、顶点、边、面、对偶图
- **Pauli 群**：$X, Z$ 算子的对易/反对易关系

---

## Derivation

### Step 1: Lattice Setup（格子构建） **[Dennis et al. 2002, §2; Bacon, p.20-22]**

考虑一个 $L \times L$ 的正方形格子。我们首先处理**环面码（toric code）**的情况（周期性边界条件），然后讨论**平面码（planar code）**的边界修改。

**格子元素**：
- **顶点（vertices）**：格子的交叉点，共 $L^2$ 个
- **边（edges）**：连接相邻顶点的线段，共 $2L^2$ 条（水平 $L^2$ 条 + 垂直 $L^2$ 条）
- **面（faces/plaquettes）**：由四条边围成的正方形区域，共 $L^2$ 个

**量子比特放置**：每条边上放一个物理量子比特。因此总共 $n = 2L^2$ 个物理量子比特。

**直观图示**（$3 \times 3$ 格子的一小部分）：

```
  v---q---v---q---v
  |       |       |
  q       q       q
  |       |       |
  v---q---v---q---v
  |       |       |
  q       q       q
  |       |       |
  v---q---v---q---v
```

其中 `v` 是顶点，`q` 是量子比特（在边上），四条边围成的方框是一个 plaquette（面）。

### The Surface Code Four-Cycle Building Block **[Roffe, §4.1]**

> **[Roffe, QEC Introductory Guide, §4.1]**: The fundamental building block of surface codes is the **four-cycle**: two data qubits ($D_1$, $D_2$) and two ancilla qubits ($A_1$, $A_2$). Ancilla $A_1$ measures the stabilizer $X_{D_1}X_{D_2}$ via controlled-$X$ gates; ancilla $A_2$ measures $Z_{D_1}Z_{D_2}$ via controlled-$Z$ gates. These two stabilizers commute as they intersect non-trivially on an even number of qubits. The four-cycle encodes $k = n - m = 2 - 2 = 0$ logical qubits, but working codes are formed by tiling multiple four-cycles into square lattices.

### Step 2: Define X and Z Stabilizers **[Dennis et al. 2002, §2, Eq. 2.1-2.2; Bombin, §3.2; Bacon, p.20-21]**

**顶点算子（Star operator / X-stabilizer）** **[Dennis et al. 2002, §2]**：对于每个顶点 $v$，定义：

$$A_v = \prod_{e \in \text{star}(v)} X_e$$

其中 $\text{star}(v)$ 是与顶点 $v$ 相连的所有边的集合。在方格子内部，每个顶点有4条边，所以 $A_v$ 是4个 $X$ 算子的张量积（其余位置为 $I$）。

**面算子（Plaquette operator / Z-stabilizer）** **[Dennis et al. 2002, §2]**：对于每个面 $f$，定义：

$$B_f = \prod_{e \in \partial f} Z_e$$

其中 $\partial f$ 是面 $f$ 的边界上所有边的集合。每个面有4条边，所以 $B_f$ 是4个 $Z$ 算子的张量积。

**具体例子**：考虑以下局部结构，标注边上的量子比特编号：

```
    |2|
  --1--v--3--
    |4|
```

顶点 $v$ 的 star 算子为：$A_v = X_1 X_2 X_3 X_4$

```
  --1--
  |    |
  4  f  2
  |    |
  --3--
```

面 $f$ 的 plaquette 算子为：$B_f = Z_1 Z_2 Z_3 Z_4$

### Step 3: Verify Stabilizer Properties **[Roffe, §4.1; Dennis et al. 2002, §2]**

要证明 $\{A_v, B_f\}$ 构成合法的稳定子群，需要验证：

**性质1：所有算子相互对易**

- **$A_v$ 与 $A_{v'}$ 对易**：两个顶点算子都只含 $X$，而 $[X_i, X_j] = 0$，所以它们对易。

- **$B_f$ 与 $B_{f'}$ 对易**：类似地，都只含 $Z$，而 $[Z_i, Z_j] = 0$。

- **$A_v$ 与 $B_f$ 对易**（关键验证）：

  $A_v$ 含 $X$ 算子在 $\text{star}(v)$ 的边上，$B_f$ 含 $Z$ 算子在 $\partial f$ 的边上。由于 $\{X, Z\} = 0$（反对易），$A_v$ 和 $B_f$ 对易当且仅当它们共享**偶数**条边。

  考虑顶点 $v$ 和面 $f$ 的几何关系：
  - 如果 $v$ 不在 $f$ 的边界上：共享 0 条边 $\to$ 对易 $\checkmark$
  - 如果 $v$ 在 $f$ 的角上：共享 2 条边 $\to$ 两次反对易 $= $ 对易 $\checkmark$
  - 不可能出现共享 1 或 3 条边的情况（由格子几何保证）

  **详细计算**：设 $A_v$ 和 $B_f$ 共享 $m$ 条边。则：

  $$A_v B_f = (-1)^m B_f A_v$$

  因为每条共享边上 $X_e Z_e = -Z_e X_e$，贡献一个 $(-1)$ 因子。由格子几何，$m$ 总是偶数，所以 $(-1)^m = +1$，即 $[A_v, B_f] = 0$。

**性质2：每个算子的平方等于 $I$**

$$A_v^2 = \prod_{e \in \text{star}(v)} X_e^2 = \prod_{e \in \text{star}(v)} I = I$$

$$B_f^2 = \prod_{e \in \partial f} Z_e^2 = \prod_{e \in \partial f} I = I$$

**性质3：$-I^{\otimes n} \notin \mathcal{S}$**

由于所有稳定子都具有正号（没有全局 $-1$ 相位），它们的任意乘积也不会产生 $-I^{\otimes n}$。

### Step 4: Count Stabilizers and Determine Code Parameters **[Dennis et al. 2002, §2; Bombin, §3.2]**

**环面码（Toric Code）**：

顶点算子数：$L^2$ 个（每个顶点一个）

面算子数：$L^2$ 个（每个面一个）

但它们不是全部独立的。存在以下约束：

$$\prod_{\text{all } v} A_v = I^{\otimes n}$$

**证明**：每条边被恰好两个顶点共享，所以在乘积中每个 $X_e$ 出现偶数次（2次），即 $X_e^2 = I$。

$$\prod_{\text{all } f} B_f = I^{\otimes n}$$

**证明**：类似地，每条边是恰好两个面的边界，$Z_e$ 出现偶数次。

因此独立生成元数为：

$$r = L^2 + L^2 - 2 = 2L^2 - 2$$

编码的逻辑量子比特数：

$$k = n - r = 2L^2 - (2L^2 - 2) = 2$$

所以环面码编码 $k = 2$ 个逻辑量子比特 **[Bombin, §3.2; Bacon, p.22]**。由 Euler 特征 $\chi = V - E + F = 2 - 2g$，对亏格 $g$ 曲面 $k = 2g$ **[Bombin, §3.2]**。

**环面码参数**：$[[2L^2, 2, L]]$

**平面码（Planar Code）**：

在平面码中，格子有边界。一种标准构造（Bravyi-Kitaev）：
- 上下边界是"rough boundary"（粗糙边界）：边界上的顶点少一条边
- 左右边界是"smooth boundary"（光滑边界）：边界上的面少一条边

对于 $d \times d$ 的平面码：
- 数据量子比特数：$n = d^2 + (d-1)^2 = 2d^2 - 2d + 1$
- $X$ 型稳定子数（面）：$(d-1)^2$
- $Z$ 型稳定子数（顶点）：$(d-1)^2$ 或 $d(d-1)$ 取决于具体构造
- 总独立稳定子数：$n - 1 = 2d^2 - 2d$
- 逻辑量子比特数：$k = 1$

一种更常见的 rotated surface code 表述：用 $d \times d$ 的方格子（旋转 45 度），数据量子比特在格点上：

$$n = d^2, \quad k = 1, \quad \text{稳定子数} = d^2 - 1$$

但经典的 non-rotated 版本中 $n = 2d^2 - 2d + 1$。

**平面码参数**：$[[2d^2 - 2d + 1, 1, d]]$ 或 rotated 版本 $[[d^2, 1, d]]$

> **[Roffe, QEC Introductory Guide, §4.2]**: A surface code with distance $d = \lambda$ will encode a single logical qubit and have code parameters $[[n = \lambda^2 + (\lambda - 1)^2, k = 1, d = \lambda]]$. The smallest surface code capable of detecting and correcting errors is the $[[13, 1, 3]]$ code.

### Step 5: Code Distance **[Dennis et al. 2002, §2; Bombin, §3.3; Bacon, p.22-23]**

**码距的定义**：最短非平凡逻辑算子的权重。

**环面码的码距**：

在环面上，逻辑算子对应拓扑非平凡的环路（non-contractible loops）。环面有两个非平凡同伦类（沿水平和垂直方向绕环面一圈）。

- 逻辑 $\bar{Z}$ 算子：沿水平方向的 $Z$ 链，长度至少 $L$
- 逻辑 $\bar{X}$ 算子：沿垂直方向的 $X$ 链，长度至少 $L$

因此码距 $d = L$。

**为什么最短路径长度等于 $L$？**

考虑一个逻辑 $\bar{Z}$ 算子，它是一条从左到右穿越格子的 $Z$ 链。这条链必须穿过 $L$ 列，每列至少贡献一个 $Z$ 算子，所以最短长度为 $L$。

更严格地：逻辑算子在 $N(\mathcal{S}) \setminus \mathcal{S}$ 中，它必须与所有稳定子对易但不在稳定子群中。一条穿越格子的 $Z$ 链与所有 $B_f$ 对易（因为 $Z$ 与 $Z$ 对易），也与所有 $A_v$ 对易（因为链穿过每个顶点偶数次或零次——这要求链是闭合的或连接边界的）。

**平面码的码距**：

在平面码中，逻辑 $\bar{Z}$ 是连接上下两个 rough boundary 的 $Z$ 链，最短长度 $d$。逻辑 $\bar{X}$ 是连接左右两个 smooth boundary 的 $X$ 链，最短长度也是 $d$。

### Step 6: Logical Operators **[Bombin, §3.4; Dennis et al. 2002, §2]**

**环面码的逻辑算子**（编码 2 个逻辑量子比特，$\bar{X}_1, \bar{Z}_1, \bar{X}_2, \bar{Z}_2$）：

$$\bar{Z}_1 = \prod_{e \in \gamma_1^Z} Z_e, \qquad \bar{X}_1 = \prod_{e \in \gamma_1^X} X_e$$

$$\bar{Z}_2 = \prod_{e \in \gamma_2^Z} Z_e, \qquad \bar{X}_2 = \prod_{e \in \gamma_2^X} X_e$$

其中 $\gamma_1^Z$ 是沿水平方向绕环面的闭合路径，$\gamma_1^X$ 是沿垂直方向绕环面的闭合路径，等等。

关键性质验证：

**1. 与所有稳定子对易**：

$\bar{Z}_1$ 只含 $Z$ 算子，自动与所有 $B_f$（也只含 $Z$）对易。$\bar{Z}_1$ 是一条闭合的 $Z$ 链，穿过每个 $A_v$ 的 star 中偶数条边（0 或 2 条），所以与所有 $A_v$ 对易。

**2. 反对易关系**：$\bar{X}_1 \bar{Z}_1 = -\bar{Z}_1 \bar{X}_1$

$\gamma_1^X$ 和 $\gamma_1^Z$ 是两条在不同方向上绕环面的路径，它们恰好交叉一次。在交叉点处，$X_e Z_e = -Z_e X_e$，贡献一个 $(-1)$。其他所有边上要么只有 $X$ 或只有 $Z$（对易），要么什么都没有。所以总的符号是 $(-1)^1 = -1$，即反对易。

**3. 不同逻辑量子比特的算子相互对易**：$[\bar{X}_1, \bar{Z}_2] = 0$

$\gamma_1^X$（垂直 $X$ 链）和 $\gamma_2^Z$（垂直 $Z$ 链）不交叉（它们平行），所以对易。

**平面码的逻辑算子**（编码 1 个逻辑量子比特）：

$$\bar{Z} = \prod_{e \in \gamma_Z} Z_e \quad \text{（从 rough 边界到 rough 边界的路径）}$$

$$\bar{X} = \prod_{e \in \gamma_X} X_e \quad \text{（从 smooth 边界到 smooth 边界的路径）}$$

### Step 7: Planar vs Toric Boundary Conditions

**环面码（Toric Code）**：
- 周期性边界条件：上下粘合，左右粘合
- 拓扑：环面（torus），genus = 1
- 编码量子比特：$k = 2$（对应环面的两个非平凡同伦类）
- 参数：$[[2L^2, 2, L]]$

**平面码（Planar Code）**：
- 开放边界条件：有四个边界
- 两种边界类型交替出现：rough-smooth-rough-smooth
- 编码量子比特：$k = 1$
- 参数：$[[2d^2-2d+1, 1, d]]$

**为什么边界条件影响 $k$？**

在环面上，$\prod_v A_v = I$ 和 $\prod_f B_f = I$ 给出 2 个约束，减少 2 个独立生成元，增加 2 个逻辑量子比特。

在平面上，边界处的不完整稳定子（3-body 而非 4-body）破坏了上述全局约束的一个，只剩 1 个约束，所以 $k = 1$。

更直觉地：环面有两个"洞"（同伦类），每个"洞"对应一个逻辑量子比特。平面只有一个"通道"（从一种边界到另一种边界），对应一个逻辑量子比特。

### Step 8: Error Correction in the Surface Code **[Dennis et al. 2002, §3; Roffe, §5.1; Preskill Ch.7, §7.5]**

**错误模型**：假设每个物理量子比特独立地以概率 $p$ 发生 Pauli 错误。由于 $Y = iXZ$，可以分别处理 $X$ 错误和 $Z$ 错误。

**$X$ 错误检测**：$X$ 错误改变 $B_f$（plaquette）稳定子的测量结果：

如果 $X_e$ 发生在边 $e$ 上，则与 $e$ 相邻的两个 plaquette $f_1, f_2$ 的 syndrome 翻转：

$$B_{f_i} X_e = -X_e B_{f_i}, \quad i = 1, 2$$

所以 $X$ 错误在 plaquette 测量中产生一对相邻的 $-1$ 结果（syndrome 缺陷）。

**$Z$ 错误检测**：类似地，$Z$ 错误改变 $A_v$（star）稳定子的测量结果。$Z_e$ 在顶点测量中产生一对相邻的 syndrome 缺陷。

**错误链与 syndrome 缺陷**：

一连串相邻的 $X$ 错误形成一条"错误链"。这条链的 syndrome 只在链的**端点**产生缺陷（因为中间的 plaquette 被链穿过两次，符号抵消）。

这意味着 syndrome 缺陷总是成对出现。解码器的任务是找到一组配对方案，将缺陷配对后确定恢复操作。

**关键几何洞察**：解码器选择的恢复链 $R$ 和实际错误链 $E$ 可以不同，只要 $RE$ 不构成一个非平凡逻辑算子（不跨越格子）就行。只有当 $RE$ 形成一条拓扑非平凡的闭合路径时，才会发生逻辑错误。

---

## Summary Table

| 属性 | 环面码 (Toric) | 平面码 (Planar) | Rotated 平面码 |
|------|---------------|----------------|----------------|
| 参数 | $[[2L^2, 2, L]]$ | $[[2d^2-2d+1, 1, d]]$ | $[[d^2, 1, d]]$ |
| 物理比特数 | $2L^2$ | $2d^2-2d+1$ | $d^2$ |
| 逻辑比特数 | 2 | 1 | 1 |
| 码距 | $L$ | $d$ | $d$ |
| 边界条件 | 周期性 | 开放 | 开放(旋转) |
| 稳定子类型 | 全部 weight-4 | 边界 weight-3 | 边界 weight-2 |

---

## From Dennis et al. 2002: Topological Quantum Memory

### Homological Formulation **[Dennis et al. 2002, §2]**

Qubits in one-to-one correspondence with links of a square lattice on a torus ($2L^2$ qubits). Check operators:

$$X_s = \bigotimes_{\ell \ni s} X_\ell \quad \text{(site operators)}, \qquad Z_P = \bigotimes_{\ell \in P} Z_\ell \quad \text{(plaquette operators)}$$

A Pauli operator commuting with the stabilizer is a product of $Z$'s on a **cycle** of the lattice times $X$'s on a **cycle** of the dual lattice. The operator acts trivially on the code space iff these cycles are **homologically trivial** (boundaries). Non-trivial logical operators correspond to **homologically non-trivial cycles** **[Dennis et al. 2002, §2]**.

### Code Distance as Systole **[Dennis et al. 2002, §2]**

The distance of a toric code is the number of lattice links in the shortest homologically non-trivial cycle on the lattice or dual lattice. For an $L \times L$ square lattice on the torus: $d = L$.

### Planar Codes and Relative Homology **[Dennis et al. 2002, §2.2]**

For planar codes, the boundary has two types of edges: **rough edges** (plaquette edges, with 3-qubit $Z^{\otimes 3}$ operators) and **smooth edges** (site edges, with 3-qubit $X^{\otimes 3}$ operators). Logical $\bar{Z}$: chain from one rough edge to the other (non-trivial relative homology class). Logical $\bar{X}$: chain of the dual lattice from one smooth edge to the other.

For a square lattice: $n = L^2 + (L-1)^2$ links, $L(L-1)$ plaquettes, $L(L-1)$ sites, encoding $k = 1$ qubit with distance $d = L$ **[Dennis et al. 2002, §2.2]**.

### Defect Behaviour at Boundaries **[Dennis et al. 2002, §2.2]**

In planar codes, individual defects can appear (unlike toric codes where defects always appear in pairs). A site defect can reach a rough edge and disappear, but persists at a smooth edge. A plaquette defect can disappear at a smooth edge, but not at a rough edge.

### Statistical Mechanics Mapping **[Dennis et al. 2002, §3]**

Error recovery is mapped to a statistical mechanics model. In 2D (perfect syndrome): the random-bond Ising model with partition function:

$$Z[J, \eta] = \sum_{\{\sigma_i\}} \exp\left(J \sum_{\langle ij \rangle} \eta_{ij} \sigma_i \sigma_j\right)$$

where $e^{-2J} = p/(1-p)$ and $\eta_\ell = \pm 1$ marks the error chain. The accuracy threshold corresponds to the **Nishimori line** phase transition: $p_c \approx 10.9\%$ **[Dennis et al. 2002, §3.4]**.

In 3D (imperfect syndrome): a $\mathbb{Z}_2$ lattice gauge theory with quenched disorder. The third dimension is time (repeated syndrome measurements). Threshold: $p_c \geq 1.7 \times 10^{-4}$ per qubit per time step **[Dennis et al. 2002, §1]**.

### Generalizations **[Dennis et al. 2002, §2.2]**

- Any tessellation of a surface (not just square lattice) yields a surface code.
- A closed orientable genus-$g$ surface encodes $2g$ qubits (each handle adds two homology cycles).
- Planar surface with $e$ distinct rough edges encodes $e - 1$ qubits.
- Holes in the lattice: $h$ holes bounded by smooth edges encode $h$ qubits.
- Asymmetric codes: different distances for rough-to-rough and smooth-to-smooth paths.

---

## From Bombin: Topological Codes Chapter

### Surface Code Basis States **[Bombin, §3.1]**

The surface code has a basis with elements labelled by homology classes:

$$|\overline{z}\rangle = \sum_{b \in B_1} |z + b\rangle, \qquad \overline{z} \in H_1$$

These are uniform superpositions of all cycles within a given homology class. Number of encoded qubits: $k = 2g$ where $g$ is the genus of the surface **[Bombin, §3.1, Eq.(14)]**.

### Stabilizer Structure **[Bombin, §3.2]**

Face (plaquette) and vertex (star) operators commute and generate the stabilizer. Stabilizer constraints:

$$\prod_f X_f = 1, \qquad \prod_v Z_v = 1$$

Independent generators: $V + F - 2$, so $k = E - (V + F - 2) = 2 - \chi = 2g$ by the Euler characteristic **[Bombin, §3.2]**.

### Hadamard Duality **[Bombin, §3.3]**

Applying transversal Hadamard $W^{\otimes E}$ maps the surface code to the surface code on the **dual lattice**:

$$W^{\otimes E} X_f W^{\otimes E} = Z_{\hat{f}}, \qquad W^{\otimes E} Z_v W^{\otimes E} = X_{\hat{v}}$$

Therefore, the distance of a surface code is the length of the shortest non-trivial cycle in the original **or** the dual lattice **[Bombin, §3.3]**.

### String Operators and Logical Operations **[Bombin, §3.4]**

Any Pauli operator can be written as $A = i^\alpha X_c Z_{\hat{c}}$ with $(c, \hat{c}) \in C_1 \times \hat{C}_1$. Elements of the normalizer $N(S)$ are labelled by cycles: $(c, \hat{c}) \in Z_1 \times \hat{Z}_1$. Elements of the stabilizer are labelled by boundaries: $(b, \hat{b}) \in B_1 \times \hat{B}_1$. Therefore:

$$\frac{N(S)}{S'} \simeq H_1 \times \hat{H}_1 \simeq H_1^2$$

where $S' = \langle iI \rangle S$ **[Bombin, §3.4]**.

### Boundaries and Holes **[Bombin, §3.5]**

Removing face stabilizer generators creates holes. Removing two face generators $X_f, X_{f'}$ creates one new encoded qubit. Logical $\bar{Z}$: open dual string connecting the missing faces. Logical $\bar{X}$: direct closed string enclosing one hole. Two types of boundaries:
- **Rough (dual) boundary**: site defects can disappear here
- **Smooth (direct) boundary**: plaquette defects can disappear here

**[Bombin, §3.5]**

### 2D Locality Bound **[Bombin, §2]**

For any family of 2D local codes: $d = O(\sqrt{n})$. However, topological codes can correct **most** errors of weight $O(n)$, reflected in the existence of an error threshold **[Bombin, §2]**.

---

## From Steane Tutorial: Topological Code Motivation

### Why Topological Codes? **[Steane Tutorial, §7]**

Steane 在其 tutorial 中讨论了从通用稳定子码到拓扑码的动机：

1. **局部性**：通用稳定子码的稳定子可能涉及任意距离的量子比特对，而拓扑码的稳定子是**几何局部的**——只涉及相邻量子比特。这对二维量子芯片至关重要。

2. **可扩展性**：增大码距只需扩大格子尺寸，不改变稳定子的结构（始终是 weight-4 或 weight-3/2 边界算子）。

3. **高阈值**：局部性使得 syndrome 提取电路更短，减少了错误传播的机会，导致 circuit-level 阈值比级联码高出 2-3 个数量级。

### 经典纠错到拓扑码的类比 **[Steane Tutorial, §7.1]**

| 经典概念 | 量子/拓扑对应 |
|---------|-------------|
| 奇偶校验 | 稳定子测量 |
| 校验矩阵行 | 稳定子生成元 |
| Syndrome | Syndrome（缺陷位置） |
| 码字 | $+1$ 特征子空间 |
| 码距 | 最短非平凡逻辑算子权重 |
| 重复码 | 一维 repetition code（$ZZ$ 稳定子链） |
| 二维校验 | 表面码（二维稳定子格子） |

---

## From Bacon's Introduction: Surface Code and Homological QEC

### Homological Perspective on Surface Codes **[Bacon, §4.1]**

Bacon 从链复形（chain complex）出发，给出表面码的代数拓扑观点：

**链复形** $C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0$：
- $C_0$：0-chains（顶点的形式线性组合，over $\mathbb{F}_2$）
- $C_1$：1-chains（边的形式线性组合）
- $C_2$：2-chains（面的形式线性组合）
- $\partial_1$：边界算子，将边映射到其两个端点的异或
- $\partial_2$：边界算子，将面映射到其四条边的异或

**关键公式** **[Bacon, §4.1]**：$\partial_1 \circ \partial_2 = 0$（面的边界的边界为零），这正是 $X$ 型和 $Z$ 型稳定子对易的拓扑原因。

**码参数的同调公式** **[Bacon, §4.2]**：
- 逻辑量子比特数 $k = \dim H_1 = \dim(\ker\partial_1 / \operatorname{im}\partial_2)$（第一同调群的维度）
- 码距 $d$ = 最短非平凡同调类中最轻代表元的权重
- 对亏格 $g$ 曲面：$k = 2g$

### Stabilizer Code 到 Surface Code 的特化 **[Bacon, §4.3]**

Bacon 展示了表面码如何从一般稳定子码的 symplectic 框架自然产生：

一般稳定子码 check matrix $H = (H_X | H_Z)$，对于表面码：

$$H_X = \partial_1^T \quad (\text{顶点-边的关联矩阵转置}), \qquad H_Z = \partial_2 \quad (\text{面-边的关联矩阵})$$

对易条件 $H_X H_Z^T = \partial_1^T \partial_2^T = (\partial_2 \partial_1)^T = 0$ 自动满足。

---

## From Surface Code Notes: Practical Implementation Details

### Syndrome Extraction Circuits **[Surface Code Notes, §4]**

Syndrome 测量通过辅助量子比特（ancilla）间接实现，不直接测量数据量子比特。

**X-stabilizer 测量电路**（测量 $A_v = X_1 X_2 X_3 X_4$）：

```
|0⟩ ancilla ---H---●---●---●---●---H---M
                    |   |   |   |
data qubit 1 ------X---+---+---+--------
data qubit 2 ----------X---+---+--------
data qubit 3 --------------X---+--------
data qubit 4 ------------------X--------
```

1. Ancilla 准备在 $|+\rangle = H|0\rangle$
2. 对每个数据量子比特执行 CNOT（ancilla 为 control）
3. 再次施加 $H$ 并测量 ancilla

**Z-stabilizer 测量电路**（测量 $B_f = Z_1 Z_2 Z_3 Z_4$）：

```
|0⟩ ancilla ---●---●---●---●---M
               |   |   |   |
data qubit 1 --X---+---+---+----
data qubit 2 ------X---+---+----
data qubit 3 ----------X---+----
data qubit 4 --------------X----
```

1. Ancilla 准备在 $|0\rangle$
2. 对每个数据量子比特执行 CNOT（数据为 control，ancilla 为 target）
3. 测量 ancilla

**Hook Error（钩形错误）** **[Surface Code Notes, §4.2]**：CNOT 门序安排不当时，ancilla 上的单个错误可能传播为数据量子比特上 weight-2 的关联错误。标准做法是按照固定的 serpentine ordering（蛇形顺序）安排门操作，使 hook error 限制在同一行/列内。

### Rotated Surface Code **[Surface Code Notes, §5]**

旋转表面码将标准表面码的格子旋转 45 度，实现更高的量子比特利用率。

| 属性 | 标准平面码 | 旋转平面码 |
|------|-----------|-----------|
| 数据量子比特 ($d$) | $2d^2 - 2d + 1$ | $d^2$ |
| Syndrome 量子比特 | $2(d-1)^2$ | $d^2 - 1$ |
| 总量子比特 | $\approx 4d^2$ | $\approx 2d^2$ |
| 稳定子权重 | 边界: 3, 内部: 4 | 角: 2, 边界: 3, 内部: 4 |

**常用 rotated surface code 参数**：

| 码距 $d$ | 数据量子比特 | Ancilla | 总量子比特 |
|----------|------------|---------|-----------|
| 3 | 9 | 8 | 17 |
| 5 | 25 | 24 | 49 |
| 7 | 49 | 48 | 97 |
| 9 | 81 | 80 | 161 |
| 11 | 121 | 120 | 241 |
| 13 | 169 | 168 | 337 |

### Measurement Rounds and 3D Decoding **[Surface Code Notes, §6]**

在实际有噪声的 syndrome 提取中，需要多轮重复测量。对码距 $d$ 的表面码，需要至少 $d$ 轮 syndrome 测量。

这将解码问题从 2D 扩展为 3D：
- 2 个空间维度（格子平面）
- 1 个时间维度（测量轮次）

3D syndrome 图中，数据错误在空间中产生相邻缺陷对，测量错误在时间方向产生缺陷对。

### Logical Operations via Lattice Surgery **[Surface Code Notes, §7]**

Lattice surgery 是表面码上最实用的逻辑操作方法：

- **Rough merge ($\bar{XX}$ 测量)**：合并两个 patch 的 rough boundary，测量联合 $X$ 稳定子
- **Smooth merge ($\bar{ZZ}$ 测量)**：合并两个 patch 的 smooth boundary，测量联合 $Z$ 稳定子
- 通过 merge + split 序列实现逻辑 CNOT

**Magic State Distillation**：非 Clifford 门（如 $T$ 门）需要 magic state $|T\rangle = (|0\rangle + e^{i\pi/4}|1\rangle)/\sqrt{2}$ 的蒸馏 + gate teleportation。

---

## From Fowler (2025): Detectors, Hook Errors, and Memory Experiments

### Detector Definition **[Surface Notes, p.4]**

A **detector** is a set of measurements with predictable parity in the absence of errors [Surface Notes, p.4]. For the surface code:

- First-round $Z$ stabilizer measurements after $|0\rangle$ initialization: each forms an individual detector (predicted value matches initialization)
- Second and subsequent rounds: pairs of consecutive measurements of the same stabilizer form detectors (predicted parity 0)
- First-round $X$ stabilizer measurements are random (not detectors) when initialized in $Z$ basis

A **detection event** occurs when a detector's parity differs from prediction [Surface Notes, p.4].

### Error Propagation and Detection Events **[Surface Notes, p.4]**

A single $X$ error between rounds of stabilizer measurement on a qubit touching two $Z$ stabilizers generates two detection events [Surface Notes, p.4]. A $Y$ error anticommutes with all four neighboring stabilizers, leading to four detection events --- this is associated with a hyperedge in the detector hypergraph [Surface Notes, p.4].

Key insight: physical errors are not corrected; only the flipping of logical operators is tracked. After sufficient time, all stabilizer signs will be random, but the decoder tracks corrections to logical operators [Surface Notes, p.5].

### Hook Errors **[Surface Notes, p.5-6]**

Hook errors are multiple data qubit errors resulting from a single measure qubit error [Surface Notes, p.5]. They occur when a measure qubit touches $\geq 4$ data qubits, corrupting at most half of them. The CNOT ordering in Fig.3 of Fowler's notes arranges hook errors perpendicular to logical operators to avoid reducing the code distance.

With worst-case hook error arrangements, alternating the circuit time ordering limits the code distance reduction to just 1 [Surface Notes, p.6]. This is acceptable for large code distances but sub-optimal when qubit counts are limited.

### Logical Error Mechanism **[Surface Notes, p.5]**

Initialization to $|0_L\rangle$ fails when errors form a path connecting two boundaries of the same type [Surface Notes, p.5]. For a distance-$d$ code, at least approximately $(d+1)/2$ independent physical errors are needed to cause a logical error. The probability of such error clusters is exponentially suppressed as code distance increases.

### Memory Experiments **[Surface Notes, p.7]**

Fowler defines four surface code circuit variants: InitX$_k$, InitZ$_k$, MeasX$_k$, MeasZ$_k$, where $k$ parameterizes a $2k \times 2k$ grid of weight-4 stabilizers. Memory experiments consist of InitZ$_k$ followed by $2k-1$ rounds of stabilizer measurement followed by MeasZ$_k$ (and similarly for X basis) [Surface Notes, p.7].

### CNOT via Lattice Surgery **[Surface Notes, p.8]**

The CNOT stabilizer flows are [Surface Notes, p.8]:

$$X_a X_b \xrightarrow{\text{CNOT}_{ab}} X_a I_b, \quad Z_a I_b \xrightarrow{\text{CNOT}_{ab}} Z_a I_b$$
$$I_a X_b \xrightarrow{\text{CNOT}_{ab}} I_a X_b, \quad Z_a Z_b \xrightarrow{\text{CNOT}_{ab}} I_a Z_b$$

A structure with correlation surfaces matching these flows implements CNOT up to byproduct operators. The output byproduct operators depend on corrected parities $\lambda'_{X_a}, \lambda'_{Z_a}, \lambda'_{X_b}, \lambda'_{Z_b}$ of the correlation surfaces [Surface Notes, p.8].

---

## From NordiQUEst: Surface Code Practical Overview

### Surface Code Error Budget **[NordiQUEst, p.26]**

NordiQUEst presents an error budget for a distance-5 surface code on a 72-qubit processor (arXiv:2408.13687), showing the relative contributions of different error sources in a real experimental setting [NordiQUEst, p.26].

### Stim for Detector Hypergraph Construction **[Surface Notes, p.7]**

The detector hypergraph can be constructed using Stim [Surface Notes, p.7]. The process: start with a quantum circuit annotated with detectors, systematically consider every possible error on every gate, propagate until detection events are generated, and record these as hyperedges. If two different errors lead to the same detection events but flip different logical operators, this would imply they form a logical operator --- violating the assumption $d \geq 3$ [Surface Notes, p.7].

---

## References

- Kitaev, A. Yu. "Fault-tolerant quantum computation by anyons." Ann. Phys. 303, 2 (2003). arXiv:quant-ph/9707021
- Bravyi, S. & Kitaev, A. "Quantum codes on a lattice with boundary." arXiv:quant-ph/9811052 (1998).
- Dennis, E., Kitaev, A., Landahl, A. & Preskill, J. "Topological quantum memory." J. Math. Phys. 43, 4452 (2002).
- **[Preskill, Ch.7]** Preskill, J. *Lecture Notes for Ph219/CS219*, Ch.7: "Quantum Error Correction". Shor 9-qubit code (§7.1, pp.1-5), stabilizer codes (§7.9, pp.34-41), CSS construction underlying the toric/surface code structure.
- **[Surface Notes]** Fowler, A. G. "Surface code quantum computation." Google Quantum AI (2025).
- **[NordiQUEst]** Lenssen, Martres, Myneni, Fuchs. "Quantum Error Correction - Theory and Hands-on." NordiQUEst workshop (2024).
- Bombin, H. "An Introduction to Topological Quantum Codes." In: Quantum Error Correction, Cambridge UP (2013).
- Roffe, J. "Quantum Error Correction: An Introductory Guide." Contemp. Phys. 60, 226 (2019).
- Fowler, A. G. et al. "Surface codes: Towards practical large-scale quantum computation." PRA 86, 032324 (2012).
- Horsman, C. et al. "Surface code quantum computing by lattice surgery." New J. Phys. 14, 123011 (2012).
- Fujii, K. "Quantum Computation with Topological Codes." SpringerBriefs in Mathematical Physics (2015), Ch.3-4.

---

## Additions from Fujii's "Quantum Computation with Topological Codes" (2015)

### Chain Complex Formulation of Surface Code [Fujii, Ch.3, §3.1-3.3]

> **[Fujii, Ch.3, §3.1]**: 曲面 $G=(V,E,F)$ 上定义 $\mathbf{Z}_2$ 链复形 $C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0$，量子比特在边 $e_l \in E$ 上。Pauli 乘积由 1-chain $c_1 = \sum_l z_l e_l$ 定义：$W(c_1) = \prod_l W_l^{z_l}$。两算子 $X(c_1)$ 和 $Z(c'_1)$ 的对易性由内积决定：
>
> $$c_1 \cdot c'_1 = 0 \Leftrightarrow [X(c_1), Z(c'_1)] = 0; \quad c_1 \cdot c'_1 = 1 \Leftrightarrow \{X(c_1), Z(c'_1)\} = 0$$

> **[Fujii, Ch.3, §3.1, Eq.(3.8)]**: 对偶关系 $M(\partial_1) = M(\bar{\partial}_2)^T$ 保证 $\bar{\partial}\bar{c}_2 \cdot \partial c_2 = 0$，即 $X(\partial c_2)$ 和 $Z(\bar{\partial}\bar{c}_2)$ 总是对易——这是稳定子群合法性的拓扑根源。

### Toric Code: Formal Definition [Fujii, Ch.3, §3.3]

> **[Fujii, Ch.3, §3.3]**: 环面上 $n \times n$ 方格子的稳定子生成元：
>
> $$A_m = Z(\partial f_m) \quad \text{(plaquette)}, \qquad B_k = X(\delta v_k) = X(\partial \bar{f}_k) \quad \text{(star)}$$
>
> 独立稳定子数 $|F|+|V|-2 = 2n^2-2$（因 $\prod_m A_m = I$ 和 $\prod_k B_k = I$）。量子比特数 $|E|=2n^2$。码参数 $[[2n^2, 2, n]]$。

> **[Fujii, Ch.3, §3.3]**: 逻辑算子对应非平凡同调类。若 $c_1$ 和 $c'_1$ 同调等价，则 $Z(c'_1) = Z(c_1)\prod_{f_m\in c_2}A_m$，即作用在码空间上相同。逻辑基态的显式形式：
>
> $$|\Psi_Z(s_1,s_2)\rangle = \mathcal{N}\,Z(c_1^{(1)})^{s_1}Z(c_1^{(2)})^{s_2}\prod_{v_k\in V}\frac{I+B_k}{2}|0\rangle^{\otimes n^2}$$

### Euler Characteristic and Logical Qubits [Fujii, Ch.3, §3.3]

> **[Fujii, Ch.3, §3.3]**: 对一般 tiling $G=(V,E,F)$，码空间维度由 Euler 特征公式决定：
>
> $$|F|+|V|-|E| = 2-2g \quad \Rightarrow \quad \dim(\text{code space}) = 2^{|E|-(|F|+|V|-2)} = 2^{2g}$$
>
> 亏格 $g$ 曲面编码 $2g$ 个逻辑量子比特。

### Planar Code with Boundaries [Fujii, Ch.3, §3.3.2]

> **[Fujii, Ch.3, §3.3.2]**: 平面码在 $n\times(n-1)$ 方格子上定义。上下为光滑边界（smooth，完整 plaquette），左右为粗糙边界（rough，三量子比特 plaquette）。使用**相对同调**：两链 $c_i$ 和 $c'_i$ 相对同调等价当 $c'_i = c_i + \partial c_{i+1} + \gamma_i$（$\gamma_i \in \Gamma_i$，边界链）。码参数：$|E|=2n^2-2n+1$，$|V|=|F|=n^2-n$，码空间 2 维。

### Defect Pair Qubits [Fujii, Ch.4, §4.1]

> **[Fujii, Ch.4, §4.1]**: 通过在平面码上打洞（移除缺陷区域 $D$ 内的 plaquette 算子）引入逻辑量子比特。一对缺陷定义一个**缺陷对量子比特**（defect pair qubit）：
> - 逻辑 $Z$：围绕缺陷的非平凡 cycle $Z(\partial D)$
> - 逻辑 $X$：连接两缺陷的对偶 1-chain $X(\bar{c}_1)$
> - 码距 = min(缺陷周长, 缺陷间距离)
>
> 分为 primal defect（移除 plaquette）和 dual defect（移除 star）两类。

### Defect Operations [Fujii, Ch.4, §4.2]

> **[Fujii, Ch.4, §4.2]**: 缺陷的基本操作（均通过局部量子操作实现）：
> - **创建**：在缺陷区域 $D$ 内测量 $X$ 基，准备逻辑 $Z$ 基态
> - **扩展**：创建更大缺陷 $D' \supset D$，逻辑信息保持不变
> - **收缩**：测量 plaquette 算子恢复缺陷内部，$(-1)^m Z(\partial D'')$ 成为新逻辑算子
> - **湮灭**：完全测量缺陷区域的 plaquette 算子，实现逻辑 $Z$ 基测量（$Z(\partial D) = \prod_{f_m\in D}A_m$）
> - **移动**：扩展 + 收缩的组合

### CNOT Gate by Braiding [Fujii, Ch.4, §4.3]

> **[Fujii, Ch.4, §4.3]**: 将一个 primal 缺陷绕另一个 dual 缺陷编织（braiding）实现逻辑 CNOT 门。所有操作仅用最近邻两量子比特门和单量子比特测量。

### Topological Error Correction [Fujii, Ch.3, §3.4]

> **[Fujii, Ch.3, §3.4]**: 错误链 $Z(c_1^e)$ 的 syndrome 为 $\partial c_1^e$。纠错任务：找恢复链 $c_1^r$ 使 $\partial(c_1^e + c_1^r) = 0$。若 $c_1^e + c_1^r$ 是平凡 cycle 则成功，非平凡 cycle 则逻辑错误。
>
> **最小权重解码**等价于找最小 Manhattan 距离匹配——Edmonds 的 MWPM 算法 $O(n^6)$。MWPM 阈值 $\sim 10.3\%$。

> **[Fujii, Ch.3, §3.4]**: 最优解码应最大化同调类的后验概率 $p_k = \sum_{c_1^{r'}} P(c_1^{r'}|c_0^s)$（对同一同调类求和），而非单个错误的后验概率。这利用码的简并性（degeneracy）。Pfaffian 方法可多项式时间计算最优解码。

### Renormalization Decoder [Fujii, Ch.3, §3.4]

> **[Fujii, Ch.3, §3.4]**: Duclos-Cianci & Poulin 提出重正化解码器：用 12 量子比特单元格定义层级结构，在每层进行 belief propagation。并行化后时间 $O(\log_2 n)$。阈值：独立 $X/Z$ 错误 $\sim 9\%$，去极化错误 $\sim 15.2\%$。
