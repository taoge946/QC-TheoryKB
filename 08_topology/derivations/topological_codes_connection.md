# How Homology Connects to Quantum Error Correcting Codes

> **Tags**: `topological-code`, `homology`, `surface-code`, `toric-code`, `code-distance`
>
> **Primary Source**: H. Bombin, *An Introduction to Topological Quantum Codes* **[Bombin, §4 (Surface Codes)]**

## Statement

拓扑量子码（Topological Quantum Codes）本质上是同调码（Homological Codes） **[Bombin, §4]**。给定一个二维流形上的 CW 复形和对应的链复形 $C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0$，我们可以构造一个 CSS 码 **[Bombin, §4.1, Eq.(8)--(11)]**，其中：$Z$ 型稳定子对应边界（boundaries） **[Bombin, §4.2, Eq.(12)]**，$X$ 型稳定子对应上边界（coboundaries），逻辑 $Z$ 算子对应同调类（homology classes），逻辑 $X$ 算子对应上同调类（cohomology classes） **[Bombin, §4.3]**，码距等于最短非平凡同调/上同调类代表元的 Hamming 重量。拓扑保护的本质在于：局部变形（施加稳定子）不改变同调类，只有跨越整个系统的全局操作才能改变编码信息。

## Prerequisites

- **同调基础**：链复形、边界算子、cycles、boundaries、同调群 → [homology_basics.md]
- **上同调基础**：上链、上边界算子、上同调群 → [cohomology_basics.md]
- **稳定子形式体系**：稳定子群、syndrome、CSS 码 → [../04_quantum_error_correction/derivations/stabilizer_formalism.md]
- **$\mathbb{F}_2$ 线性代数**：向量空间、核、像

---

## Derivation

### Step 1: From Lattice to Chain Complex（从格子到链复形）

**设置**：取一个二维流形 $M$（如环面 $T^2$）上的 CW 分解（胞腔分解），得到：

- $V$ 个顶点（0-cells），$E$ 条边（1-cells），$F$ 个面（2-cells）

构造 $\mathbb{F}_2$ 上的链复形：

$$C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0$$

$$\mathbb{F}_2^F \xrightarrow{\partial_2} \mathbb{F}_2^E \xrightarrow{\partial_1} \mathbb{F}_2^V$$

其中 $\partial_2$ 是 $E \times F$ 矩阵，$\partial_1$ 是 $V \times E$ 矩阵（均在 $\mathbb{F}_2$ 上），满足 $\partial_1 \partial_2 = 0$。

**物理量子比特**：放置在 1-cells（边）上，共 $n = E$ 个。

这是拓扑码的标准约定。每个物理量子比特对应格子的一条边。

---

### Step 2: Z-Stabilizers as Boundaries（$Z$ 型稳定子 = 边界） **[Bombin, §4.2, Eq.(12)]**

**定义**：对每个面 $f_j$（$j = 1, \ldots, F$），定义 plaquette operator：

$$B_{f_j} = \prod_{e_i \in \partial f_j} Z_{e_i}$$

即在面 $f_j$ 的边界上所有边上施加 $Z$ 算子。**[Bombin, §4.2, Eq.(12)]**

**同调语言**：$B_{f_j}$ 的支撑集（support）恰好是 $\partial_2(f_j) \in C_1$，即面 $f_j$ 的边界链。$Z$ 型稳定子群的整体支撑是：

$$\mathcal{S}_Z = \operatorname{im} \partial_2 = B_1 \quad \text{(1-boundaries)}$$

更精确地说：任意 $Z$ 型稳定子 $\prod_j B_{f_j}^{a_j}$（$a_j \in \{0,1\}$）的支撑集为

$$\text{supp}(Z\text{-stabilizer}) = \partial_2\left(\sum_j a_j f_j\right) \in B_1$$

所以 $Z$ 型稳定子的支撑集集合 = $B_1$。

**为什么稳定子必须是 cycle**：不需要！$Z$ 型稳定子的支撑集是 boundary，boundary 是 cycle 的特例（$B_1 \subseteq Z_1$），但这里的关键是 $Z$ 型稳定子生成的空间是 $B_1$。

---

### Step 3: X-Stabilizers as Coboundaries（$X$ 型稳定子 = 上边界） **[Bombin, §4.2, Eq.(12)]**

**定义**：对每个顶点 $v_j$（$j = 1, \ldots, V$），定义 star operator：

$$A_{v_j} = \prod_{e_i \in \text{star}(v_j)} X_{e_i}$$

即在与顶点 $v_j$ 相连的所有边上施加 $X$ 算子。

**同调语言**：$\text{star}(v_j)$ 作为 $C_1$ 中的一条链，等于什么？

引入上边界算子 $\delta^0 = \partial_1^T: C^0 \to C^1$。将 $C^0$ 和 $C_0$ 等同（$\mathbb{F}_2$ 上自对偶），$C^1$ 和 $C_1$ 等同，则：

$$\delta^0(v_j) = \partial_1^T(v_j) = \sum_{i: v_j \in \partial_1(e_i)} e_i = \sum_{e_i \in \text{star}(v_j)} e_i$$

所以 star 算子的支撑集恰好是顶点的上边界（coboundary）！

$$\text{supp}(X\text{-stabilizer from } v_j) = \delta^0(v_j) \in B^1 \quad \text{(1-coboundaries)}$$

$X$ 型稳定子群的整体支撑是：

$$\mathcal{S}_X = \operatorname{im} \delta^0 = \operatorname{im} \partial_1^T = B^1$$

---

### Step 4: Commutativity from $\partial^2 = 0$（对易性来自 $\partial^2 = 0$） **[Bombin, §4.2]**

**命题**：所有 $A_v$ 和 $B_f$ 彼此对易。

**证明**：$A_v$ 在顶点 $v$ 的 star 上施加 $X$，$B_f$ 在面 $f$ 的 boundary 上施加 $Z$。$X$ 和 $Z$ 在同一量子比特上反对易。因此 $A_v$ 和 $B_f$ 对易当且仅当它们的支撑集的交集大小为偶数：

$$[A_v, B_f] = 0 \quad \Leftrightarrow \quad |\text{star}(v) \cap \partial f| \equiv 0 \pmod{2}$$

用代数语言：$|\text{star}(v) \cap \partial f| = \langle \delta^0(v), \partial_2(f) \rangle$，其中 $\langle \cdot, \cdot \rangle$ 是 $C_1$ 上的标准内积（$\mathbb{F}_2$ 上的点积）。

$$\langle \delta^0(v), \partial_2(f) \rangle = \langle \partial_1^T(v), \partial_2(f) \rangle = v^T \partial_1 \partial_2 f = 0$$

最后一步用了 $\partial_1 \partial_2 = 0$！

所以 **$\partial^2 = 0$ 直接保证了 $X$ 型和 $Z$ 型稳定子的对易性**。这是 CSS 码结构的拓扑核心。 $\square$

更一般地：
- $A_v$ 之间都对易（因为纯 $X$ 算子总是对易的）
- $B_f$ 之间都对易（因为纯 $Z$ 算子总是对易的）
- $A_v$ 和 $B_f$ 对易（因为 $\partial^2 = 0$）

---

### Step 5: Logical Operators from Homology and Cohomology（逻辑算子来自同调和上同调）

**$Z$ 型错误和逻辑 $Z$**：

一个 $Z$ 型错误链 $c \in C_1$ 对应在链 $c$ 的支撑集上施加 $Z$ 算子：$\bar{Z}(c) = \prod_{e_i \in \text{supp}(c)} Z_{e_i}$。

- $\bar{Z}(c)$ 与所有 $B_f$ 对易（因为 $Z$ 与 $Z$ 对易）— 总是成立
- $\bar{Z}(c)$ 与 $A_v$ 的对易性：$[A_v, \bar{Z}(c)] = 0 \Leftrightarrow \langle \delta^0(v), c \rangle = 0$

$\bar{Z}(c)$ 与**所有** $A_v$ 对易当且仅当 $c \in (\operatorname{im} \delta^0)^\perp = (\operatorname{im} \partial_1^T)^\perp = \ker \partial_1 = Z_1$。

所以：**$Z$ 型算子与所有稳定子对易 $\Leftrightarrow$ 其支撑集是一条 1-cycle**。

进一步分类：
- 如果 $c \in B_1$：$\bar{Z}(c)$ 本身就是稳定子（或稳定子的乘积），作用于码空间为恒等——**平凡错误，可被稳定子纠正**
- 如果 $c \in Z_1 \setminus B_1$：$\bar{Z}(c)$ 与所有稳定子对易但不属于稳定子群——这是**逻辑算子**
- 如果 $c \notin Z_1$：$\bar{Z}(c)$ 与某些 $A_v$ 反对易——**可检测错误**（有非零 syndrome）

$$\text{逻辑 } Z \text{ 算子} \longleftrightarrow H_1 = Z_1 / B_1 \text{ 中的非平凡类}$$

**$X$ 型错误和逻辑 $X$**（完全对偶的分析）：

一个 $X$ 型错误链 $\gamma \in C^1 \cong C_1$ 对应 $\bar{X}(\gamma) = \prod_{e_i \in \text{supp}(\gamma)} X_{e_i}$。

$\bar{X}(\gamma)$ 与所有稳定子对易 $\Leftrightarrow$ $\gamma \in Z^1 = \ker \delta^1 = \ker \partial_2^T$。

- $\gamma \in B^1$：平凡（稳定子本身）
- $\gamma \in Z^1 \setminus B^1$：逻辑 $X$ 算子

$$\text{逻辑 } X \text{ 算子} \longleftrightarrow H^1 = Z^1 / B^1 \text{ 中的非平凡类}$$

---

### Step 6: Code Distance = Minimum Weight of Non-trivial Homology Class（码距 = 最小非平凡同调类重量）

**定义**（同调码的码距）：

$$d_Z = \min_{c \in Z_1 \setminus B_1} |c| = \min_{[c] \neq 0 \in H_1} \min_{c' \in [c]} |c'|$$

$$d_X = \min_{\gamma \in Z^1 \setminus B^1} |\gamma| = \min_{[\gamma] \neq 0 \in H^1} \min_{\gamma' \in [\gamma]} |\gamma'|$$

$$d = \min(d_X, d_Z)$$

其中 $|c|$ 是链 $c$ 的 Hamming 重量（支撑集中边的数量）。

**直觉解释**：
- $d_Z$ 是最短的 $Z$ 型逻辑算子的重量。要造成不可检测的逻辑错误，$Z$ 型错误链必须形成闭环（cycle），且这个闭环不能是任何面集合的边界（否则它是稳定子，不改变逻辑信息）。码距就是这样的"非平凡环"的最短长度。
- 同理 $d_X$ 来自上同调。
- 在环面码中，由 Poincaré 对偶，$d_X = d_Z$。

**为什么"拓扑"提供保护**：局部错误只能产生小的错误链。小的闭链一定是某些面的边界（在格子足够大时）。只有跨越整个系统的全局错误链才可能是非平凡的同调类。所以码距随系统尺寸增长，提供了天然的错误保护。

---

### Step 7: Code Parameters from Topology（码参数的拓扑来源）

综合以上分析，同调码 $[[n, k, d]]$ 的参数为：

$$n = \dim C_1 = E \quad \text{(物理量子比特数 = 边数)}$$

$$k = \dim H_1 = \beta_1 \quad \text{(逻辑量子比特数 = 第一 Betti 数)}$$

独立稳定子数的验证：

$$n - k = \dim C_1 - \dim H_1 = \dim C_1 - (\dim Z_1 - \dim B_1)$$

$$= (\dim C_1 - \dim Z_1) + \dim B_1 = \operatorname{rank}(\partial_1) + \operatorname{rank}(\partial_2)$$

$$= \dim B_0 + \dim B_1 = \text{独立 } X \text{-稳定子数} + \text{独立 } Z \text{-稳定子数}$$

这与稳定子形式体系完全一致：一个 $[[n, k]]$ 稳定子码有 $n - k$ 个独立稳定子生成元。

**注意**：$X$ 型稳定子（star operators）的独立生成元数 = $\operatorname{rank}(\partial_1^T) = \operatorname{rank}(\partial_1) = \dim B_0 = V - \beta_0$。$Z$ 型稳定子（plaquette operators）的独立生成元数 = $\operatorname{rank}(\partial_2) = \dim B_1 = F - \beta_2$。它们之和：

$$(V - \beta_0) + (F - \beta_2) = V + F - \beta_0 - \beta_2$$

应该等于 $n - k = E - \beta_1$。验证：

$$V + F - \beta_0 - \beta_2 = E - \beta_1 \quad \Leftrightarrow \quad \beta_0 - \beta_1 + \beta_2 = V - E + F = \chi$$

这正是 Euler 示性数的定义！所以一切自洽。 $\checkmark$

---

### Step 8: Why Topological Protection Works — Deformability of Errors（拓扑保护的原因——错误的可变形性）

**关键原理**：同一个同调类中的不同代表元通过添加边界来相互转化：

$$c' = c + \partial_2(s) \quad \text{for some } s \in C_2$$

这意味着 $\bar{Z}(c)$ 和 $\bar{Z}(c')$ 在码空间上的作用完全相同：

$$\bar{Z}(c') = \bar{Z}(c) \cdot \bar{Z}(\partial_2(s)) = \bar{Z}(c) \cdot \text{(stabilizer)} = \bar{Z}(c) \quad \text{on code space}$$

**物理含义**：
1. **错误等价性**：两条错误链如果差一个 boundary，它们造成的逻辑效果完全一样。这就是解码问题——只需要判断错误链的同调类，不需要知道具体的错误位置。
2. **可变形性**：逻辑算子可以沿流形"滑动"而不改变其逻辑效果。例如在环面上，绕水平方向的非平凡环可以上下平移而保持同一同调类。
3. **局部不可区分性**：局部操作（小面积上的变形）不能改变同调类。要实现逻辑操作或造成逻辑错误，必须进行全局操作。

**错误纠正流程的同调描述**：

1. 错误 $e \in C_1$ 发生
2. 测量 syndrome：$\text{synd}(e) = \partial_1(e) \in C_0$（哪些顶点的稳定子被翻转）
3. 解码器找到恢复操作 $r \in C_1$ 使得 $\partial_1(r) = \partial_1(e)$，即 $\partial_1(e + r) = 0$
4. 纠正成功当且仅当 $e + r \in B_1$（残留错误是边界 = 稳定子），即 $[e] = [r]$（同调类相同）
5. 纠正失败当且仅当 $e + r \in Z_1 \setminus B_1$（残留错误是非平凡 cycle = 逻辑错误）

---

### Step 9: Worked Example — Toric Code on $2 \times 2$ Lattice（完整例子：$2 \times 2$ 环面码）

使用 [homology_basics.md] Step 8 中的 $2 \times 2$ 环面格子。

```
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

**码参数**：$n = 8$ 边 = 物理量子比特，$k = \beta_1 = 2$，$d = L = 2$。

所以这是一个 $[[8, 2, 2]]$ 环面码。

**$Z$ 型稳定子**（plaquette operators）：

$$B_{f_0} = Z_{e_0} Z_{e_5} Z_{e_2} Z_{e_4}, \quad B_{f_1} = Z_{e_1} Z_{e_4} Z_{e_3} Z_{e_5}$$

$$B_{f_2} = Z_{e_2} Z_{e_7} Z_{e_0} Z_{e_6}, \quad B_{f_3} = Z_{e_3} Z_{e_6} Z_{e_1} Z_{e_7}$$

注意 $B_{f_0} B_{f_1} B_{f_2} B_{f_3} = I$（所有面的乘积是恒等，因为每条边被两个面共享，$Z^2 = I$），所以只有 3 个独立的 $Z$-stabilizer。

**$X$ 型稳定子**（star operators）：

$$A_{v_0} = X_{e_0} X_{e_1} X_{e_4} X_{e_6}, \quad A_{v_1} = X_{e_0} X_{e_1} X_{e_5} X_{e_7}$$

$$A_{v_2} = X_{e_2} X_{e_3} X_{e_4} X_{e_6}, \quad A_{v_3} = X_{e_2} X_{e_3} X_{e_5} X_{e_7}$$

同样 $A_{v_0} A_{v_1} A_{v_2} A_{v_3} = I$，只有 3 个独立的 $X$-stabilizer。

独立稳定子总数：$3 + 3 = 6 = n - k = 8 - 2$。$\checkmark$

**逻辑 $Z$ 算子**：

来自 $H_1$ 的非平凡代表元：

$$\bar{Z}_1 = Z_{e_0} Z_{e_1} \quad \text{(水平环 } \gamma_h = e_0 + e_1 \text{)}$$

$$\bar{Z}_2 = Z_{e_4} Z_{e_6} \quad \text{(垂直环 } \gamma_v = e_4 + e_6 \text{)}$$

验证 $\gamma_h$ 是 cycle：$\partial_1(\gamma_h) = \partial_1(e_0 + e_1) = (v_0 + v_1) + (v_1 + v_0) = 0$。$\checkmark$

验证 $\gamma_h$ 不是 boundary：$B_1 = \operatorname{im} \partial_2$。如果 $\gamma_h = \partial_2(\sum a_j f_j)$，需要 $e_0 + e_1 = a_0 \partial_2(f_0) + \cdots$。检查 $\partial_2$ 的像空间——$\gamma_h$ 不在其中（因为 $\partial_2$ 的任何非零像在 $e_4, e_5, e_6, e_7$ 上也有非零分量）。

**逻辑 $X$ 算子**：

来自 $H^1$ 的非平凡代表元。利用 Poincaré 对偶和对偶格子的直觉：

$$\bar{X}_1 = X_{e_4} X_{e_5} \quad \text{(穿过水平环的对偶路径)}$$

$$\bar{X}_2 = X_{e_0} X_{e_2} \quad \text{(穿过垂直环的对偶路径)}$$

**验证对易/反对易关系**：

逻辑算子必须满足：$[\bar{X}_i, \bar{Z}_j] = 0$ 当 $i \neq j$，$\{\bar{X}_i, \bar{Z}_i\} = 0$。

- $\bar{X}_1 = X_{e_4} X_{e_5}$ 和 $\bar{Z}_1 = Z_{e_0} Z_{e_1}$：支撑集交集 $\{e_4, e_5\} \cap \{e_0, e_1\} = \emptyset$，对易。$\checkmark$
- $\bar{X}_1 = X_{e_4} X_{e_5}$ 和 $\bar{Z}_2 = Z_{e_4} Z_{e_6}$：交集 $\{e_4\}$，大小为1（奇数），反对易。$\checkmark$
- $\bar{X}_2 = X_{e_0} X_{e_2}$ 和 $\bar{Z}_1 = Z_{e_0} Z_{e_1}$：交集 $\{e_0\}$，大小为1，反对易。$\checkmark$
- $\bar{X}_2 = X_{e_0} X_{e_2}$ 和 $\bar{Z}_2 = Z_{e_4} Z_{e_6}$：交集 $\emptyset$，对易。$\checkmark$

**码距验证**：

$d_Z = \min_{[c] \neq 0 \in H_1} |c|$。非平凡同调类的最短代表元有：$\gamma_h = e_0 + e_1$（重量2），$\gamma_v = e_4 + e_6$（重量2），$\gamma_h + \gamma_v$（重量4）。同一类中可以加 boundary 变形：例如 $\gamma_h + \partial_2(f_0) = e_1 + e_5 + e_2 + e_4$（重量4，更长了）。

所以 $d_Z = 2 = L$。同理 $d_X = 2 = L$。

$$\boxed{d = \min(d_X, d_Z) = L = 2}$$

---

### Step 10: General Picture and Summary（一般框架总结）

**同调码的统一视角**：

给定链复形 $C_2 \xrightarrow{\partial_2} C_1 \xrightarrow{\partial_1} C_0$，定义 CSS 码：

| 代数概念 | 量子码概念 |
|----------|-----------|
| $C_1$（1-chains） | 物理量子比特空间 |
| $\operatorname{im} \partial_2 = B_1$ | $Z$ 型稳定子群的支撑集 |
| $\operatorname{im} \partial_1^T = B^1$ | $X$ 型稳定子群的支撑集 |
| $\ker \partial_1 = Z_1$ | $Z$ 型逻辑+稳定子+逻辑的联合空间 |
| $\ker \partial_2^T = Z^1$ | $X$ 型逻辑+稳定子+逻辑的联合空间 |
| $H_1 = Z_1 / B_1$ | 逻辑 $Z$ 算子的等价类 |
| $H^1 = Z^1 / B^1$ | 逻辑 $X$ 算子的等价类 |
| $\partial_1 \partial_2 = 0$ | $X$-stabilizer 与 $Z$-stabilizer 对易 |
| $\beta_1 = \dim H_1$ | 逻辑量子比特数 $k$ |
| 最短非平凡同调类重量 | 码距 $d$ |

**标准表面码变体**：

| 码类型 | 流形 | 边界条件 | $k$ | $d$ |
|--------|------|----------|-----|-----|
| Toric code | 环面 $T^2$ | 周期性 | 2 | $L$ |
| Planar surface code | 正方形（带边界） | 粗糙+光滑 | 1 | $L$ |
| Genus-$g$ code | 亏格-$g$ 曲面 | 周期性 | $2g$ | $\Theta(L)$ |
| Color code | 三着色格子 | 依情况 | 依拓扑 | 依拓扑 |

**拓扑保护的本质**：错误链的同调类只能被全局操作（跨越系统的路径）改变。局部错误产生的链要么有非零 syndrome（可检测），要么是边界（可纠正）。只有当局部错误积累到跨越整个系统时，才会造成逻辑错误——这需要 $O(d)$ 个错误，提供了随系统尺寸增长的保护。

---

## From Kitaev 2003: Toric Code and Anyonic Excitations

### Toric Code Hamiltonian **[Kitaev 2003, §1, Eq.(2)]**

$$H_0 = -\sum_s A_s - \sum_p B_p$$

where $A_s = \prod_{j \in \text{star}(s)} \sigma_j^x$ and $B_p = \prod_{j \in \text{boundary}(p)} \sigma_j^z$. The ground state is the protected subspace of $\text{TOR}(k)$ with 4-fold degeneracy (genus 1). Energy gap: $\Delta E \geq 2$.

### Error Detection Capacity **[Kitaev 2003, §1]**

The code $\text{TOR}(k)$ detects $k-1$ errors and corrects $\lfloor(k-1)/2\rfloor$ errors. An undetectable error $E$ must have support containing a non-contractible loop or cut, requiring $|\text{Supp}(E)| \geq k$. At constant error rate below threshold, unrecoverable error probability decays as $\exp(-ak)$.

### Protected Subspace Algebra **[Kitaev 2003, §1]**

The algebra $\mathcal{L}(\mathcal{L})$ of operators on the protected subspace is generated by 4 operators $Z_1, Z_2, X_1, X_2$ corresponding to non-contractible loops/cuts on the torus. They satisfy the same commutation relations as $\sigma_1^z, \sigma_2^z, \sigma_1^x, \sigma_2^x$. In homological language: $\mathcal{F}$ (stabilizer algebra) corresponds to 2-boundaries and 0-coboundaries, $\mathcal{G}$ (normalizer) to 1-cycles and 1-cocycles, $\mathcal{L}(\mathcal{L})$ to 1-homologies and 1-cohomologies **[Kitaev 2003, §1]**.

### Abelian Anyons and String Operators **[Kitaev 2003, §2]**

String operators create pairs of excitations:

$$S^z(t) = \prod_{j \in t} \sigma_j^z, \qquad S^x(t') = \prod_{j \in t'} \sigma_j^x$$

$z$-type particles (electric charges) live on vertices; $x$-type particles (magnetic vortices) live on faces. When an $x$-type particle moves around a $z$-type particle, the wavefunction acquires phase $-1$ (Aharonov-Bohm effect). This is the hallmark of **abelian anyons** **[Kitaev 2003, §2]**.

### Ground State Degeneracy from Anyons **[Kitaev 2003, §2]**

The ground state degeneracy on the torus follows from the anyonic nature of excitations (Einarsson's proof). The operator $W = X_1^{-1} Z_1^{-1} X_1 Z_1$, realized by winding one particle around the other, gives $W = -1$. Since $X_1$ and $Z_1$ anticommute, the ground state must be degenerate. For genus-$g$ surfaces: $4^g$-fold degeneracy **[Kitaev 2003, §2]**.

### Stability Under Perturbation **[Kitaev 2003, §1]**

Under local perturbation $V$, the ground state splitting appears only in the $\lceil k/2 \rceil$-th or higher order of perturbation theory. The splitting vanishes as $\exp(-ak)$ in the thermodynamic limit. Physical interpretation: virtual particle tunneling around the torus requires traversing a non-contractible loop **[Kitaev 2003, §1]**.

---

## From Dennis et al.: Aharonov-Bohm Interaction and Degeneracy

### Defect Interactions **[Dennis et al. 2002, §2.3]**

The interaction between site defects and plaquette defects is analogous to the Aharonov-Bohm interaction. When a site defect is transported around a plaquette defect, the wavefunction is modified by phase $-1$, independent of separation. This leads to the commutation relation:

$$U_{P,2}^{-1} U_{S,1}^{-1} U_{P,2} U_{S,1} = -1$$

### Generic Degeneracy **[Dennis et al. 2002, §2.3]**

For a genus-$g$ Riemann surface: generic degeneracy is $2^{2g}$. For anyons with Aharonov-Bohm phase $\exp(2\pi i p/q)$: degeneracy is $q^{2g}$. For a disc with $h$ holes: degeneracy is $2^h$ (or $q^h$). Perturbations lift the degeneracy by an amount $A \sim C \exp(-\sqrt{2}(m^* \Delta)^{1/2} L/\hbar)$, negligible for large systems **[Dennis et al. 2002, §2.3]**.

---

## From Bombin: Normalizer-Homology Correspondence

### $N(S)/S \simeq H_1 \times \hat{H}_1$ **[Bombin, §3.4]**

For surface codes, the normalizer elements are labelled (up to phase) by $(z, \hat{z}) \in Z_1 \times \hat{Z}_1$ (cycles). Stabilizer elements are labelled by $(b, \hat{b}) \in B_1 \times \hat{B}_1$ (boundaries). Therefore:

$$\frac{N(S)}{S'} \simeq H_1 \times \hat{H}_1 \simeq H_1^2$$

This makes the connection between the stabilizer quotient and homology completely explicit **[Bombin, §3.4]**.

### Crossing Number and Commutation **[Bombin, §3.4]**

A direct string (1-chain on lattice) and a dual string (1-chain on dual lattice) anticommute iff they cross an odd number of times. The oddness of crossings is preserved under homology equivalence. This geometrically determines the commutation relations between logical operators **[Bombin, §3.4]**.

---

## References

1. Kitaev, A. Y. "Fault-tolerant quantum computation by anyons." *Ann. Phys.* 303, 2-30 (2003). arXiv:quant-ph/9707021.
2. Dennis, E., Kitaev, A., Landahl, A. & Preskill, J. "Topological quantum memory." *J. Math. Phys.* 43, 4452 (2002).
3. Bombin, H. "An Introduction to Topological Quantum Codes." In: *Quantum Error Correction*, Cambridge UP (2013).
4. Freedman, M. H. & Meyer, D. A. "Projective plane and planar quantum codes." *Found. Comput. Math.* 1, 325-332 (2001).
5. Bravyi, S. & Kitaev, A. "Quantum codes on a lattice with boundary." arXiv:quant-ph/9811052 (1998).
6. Breuckmann, N. P. & Eberhardt, J. N. "Quantum LDPC Codes." PRX Quantum 2, 040101 (2021).
7. Fujii, K. "Quantum Computation with Topological Codes." SpringerBriefs (2015), Ch.3-5.

---

## Additions from Fujii's "Quantum Computation with Topological Codes" (2015)

### Chain Complex ↔ Stabilizer Code Correspondence Table [Fujii, Ch.3, Table 3.1]

> **[Fujii, Ch.3, Table 3.1]**: 完整对应关系：

| 稳定子码 | 链复形 |
|---------|--------|
| $Z$ 型稳定子生成元 | 面 $f_m$ |
| $X$ 型稳定子生成元 | 顶点 $v_k$（对偶面 $\bar{f}_k$） |
| $Z/X$ 型稳定子算子 | 2-chain 的边界 $\mathrm{Img}(\partial_2)$, $\mathrm{Img}(\bar{\partial}_2)$ |
| 与稳定子对易的算子 | $\ker(\partial_1)$, $\ker(\bar{\partial}_1)$ |
| 逻辑 $Z/X$ 算子 | 非平凡 cycle（同调类 $\ker(\partial_1)/\mathrm{Img}(\partial_2)$） |
| $Z/X$ 错误 | 1-chain $c_1$, $\bar{c}_1$ |
| $Z/X$ syndrome | $\partial c_1$, $\partial\bar{c}_1$ |

### RBIM ↔ Surface Code Correspondence [Fujii, Ch.3, Table 3.2]

> **[Fujii, Ch.3, Table 3.2]**: 随机键 Ising 模型与表面码纠错的对应：

| RBIM | 稳定子码 | 链复形 |
|------|---------|--------|
| 对偶格子 | $Z$ 错误纠正 | 原始格子 |
| 原始格子 | $X$ 错误纠正 | 对偶格子 |
| Ising 交互 | 量子比特 | 边 $e_l$ |
| 规范自旋 | $Z$ 型稳定子 | 面 $f_m$ |
| 畴壁 | 逻辑 $X/Z$ 算子 | 非平凡 cycle |
| 反铁磁交互 | $X/Z$ 错误 | 1-chain |
| 阻挫 | syndrome | $\partial c_1$ |

### Topological Color Code [Fujii, Ch.3, §3.6]

> **[Fujii, Ch.3, §3.6]**: 拓扑色码（Bombin-Martin-Delgado）定义在三着色格子上，每个顶点恰好连接三种颜色的面。与表面码的关键区别：色码可以横截实现**整个 Clifford 群**（包括 Hadamard、Phase、CNOT），无需 lattice surgery。这是因为色码的 $X/Z$ 稳定子结构在 Hadamard 变换下不变。

### Topological Order Connection [Fujii, Ch.3, §3.7]

> **[Fujii, Ch.3, §3.7]**: 拓扑稳定子码（局部、平移不变的稳定子生成元）提供了凝聚态物理中拓扑序的玩具模型。关键问题：三维或更低维度是否存在热力学稳定的拓扑序？Bravyi-Terhal 结果表明二维不存在自纠正量子存储器。

### Correlation Surface and Topological Calculus [Fujii, Ch.4, §4.4]

> **[Fujii, Ch.4, §4.4]**: 拓扑图（topological diagram）中，逻辑算子的时空轨迹形成**关联面**（correlation surface）。拓扑演算（topological calculus）是一组保持逻辑作用不变的变换规则。例如：
> - 缺陷的创建/湮灭对应拓扑图中管道的开始/结束
> - 编织（braiding）对应两条世界线的交叉
> - 相同类型缺陷的融合对应管道的合并

### 3D Topological MBQC [Fujii, Ch.5]

> **[Fujii, Ch.5]**: 拓扑容错量子计算可在三维 cluster state 上用 MBQC 重新表述。三维中两个空间维度对应表面码，一个维度对应时间演化。稳定子生成元定义在原始和对偶面上：$K_{f_m} = X_{f_m}Z(\partial f_m)$。关联面 $K(c_2) = X(c_2)Z(\partial c_2)$ 连接不同时间步的逻辑算子：
>
> $$L_Z^{(t)} \sim L_Z^{(t+1)}, \quad L_X^{(t)} \sim L_X^{(t+1)}$$
>
> 编织操作在 3D 中对应缺陷世界线的空间交叉。三维纠错简化为：若无错误，每个原始立方体上六次 $X$ 基测量结果的奇偶性总为偶。
