# Percolation Theory and Connection to QEC

> **Tags**: `percolation`, `threshold`, `qec`, `random-graph`, `critical-phenomena`

## Statement

渗流理论（Percolation Theory）研究随机介质中的连通性。在格子上，每条边（bond percolation）或每个顶点（site percolation）以概率 $p$ 被"占据"。当 $p$ 超过临界阈值 $p_c$ 时，出现跨越整个系统的无穷连通簇——这是最简单的几何相变。渗流与量子纠错有深刻联系：错误链的连通性直接决定解码的成败。

## Prerequisites

- **概率论**：独立事件、条件概率
- **图论基础**：连通分量、路径 [07_graph_theory/]
- **表面码基础**：[04_qec/surface_code_basics.md]

---

## Part 1: Basic Definitions（基本定义）

### Step 1: Bond percolation（键渗流）

给定一个无穷格子 $\mathcal{L}$（如 $\mathbb{Z}^d$ 上的超立方格子），每条边独立地以概率 $p$ 被"占据"（open），以概率 $1 - p$ 被"移除"（closed）。

**连通簇（cluster）**：通过占据边相互连通的顶点集合。

**关键问题**：是否存在无穷大的连通簇？

$$\theta(p) = P_p(\text{原点属于无穷簇}) = P_p(|C_0| = \infty)$$

其中 $C_0$ 是包含原点的连通簇。

### Step 2: Site percolation（点渗流）

每个顶点独立地以概率 $p$ 被占据。两个占据的相邻顶点属于同一簇。数学结构类似，但阈值不同。

### Step 3: Percolation threshold（渗流阈值）

$$\boxed{p_c = \inf\{p : \theta(p) > 0\}}$$

**基本性质**（严格结果）：
1. $0 < p_c < 1$（对任何有限配位数格子）
2. $\theta(p) = 0$ for $p < p_c$（subcritical phase）
3. $\theta(p) > 0$ for $p > p_c$（supercritical phase）
4. $\theta(p_c) = 0$（2D 中严格证明 [Kesten 1980; Harris 1960]）

**Refs**: Broadbent & Hammersley, Proc. Camb. Phil. Soc. 53, 629 (1957)

---

## Part 2: Critical Thresholds for Key Lattices（关键格子的临界阈值）

### Step 1: Exact results（精确结果）

**2D bond percolation**：利用自对偶性（类似 Kramers-Wannier），正方格子的 bond percolation 阈值可以精确求解：

$$p_c^{\text{bond}}(\text{square}) = \frac{1}{2}$$

**证明思路** [Kesten, Comm. Math. Phys. 74, 41 (1980)]：

正方格子是自对偶的。定义对偶格子上的边与原格子上的边一一对应：原格子上一条边 open 当且仅当对偶格子上对应边 closed。因此：

$$p_c(\text{original}) + p_c(\text{dual}) = 1$$

自对偶 $\Rightarrow$ $p_c = 1 - p_c$ $\Rightarrow$ $p_c = 1/2$。

**其他精确结果**：
- 三角格子 bond: $p_c = 2\sin(\pi/18) \approx 0.3473$
- 蜂窝格子 bond: $p_c = 1 - 2\sin(\pi/18) \approx 0.6527$

### Step 2: Numerical results（数值结果）

| 格子 | 类型 | $p_c$ | 配位数 $z$ |
|------|------|-------|-----------|
| Square | Bond | 0.5000 (exact) | 4 |
| Square | Site | 0.592746 | 4 |
| Triangular | Bond | 0.3473 (exact) | 6 |
| Triangular | Site | 0.5000 (exact) | 6 |
| Honeycomb | Bond | 0.6527 (exact) | 3 |
| Cubic (3D) | Bond | 0.2488 | 6 |
| Cubic (3D) | Site | 0.3116 | 6 |

### Step 3: Scaling near $p_c$（临界点附近的标度行为）

在 $p \to p_c$ 附近，渗流展现连续相变的典型行为：

**序参量**（无穷簇强度）：
$$\theta(p) \sim (p - p_c)^{\beta_{\text{perc}}}, \quad p \to p_c^+$$

**关联长度**（有限簇的典型大小）：
$$\xi_{\text{perc}} \sim |p - p_c|^{-\nu_{\text{perc}}}$$

**簇大小分布**（$p = p_c$ 时）：
$$n_s \sim s^{-\tau} \quad (\text{size-}s \text{ cluster 的数密度})$$

**临界指数**：

| 指数 | 2D (exact) | 3D (numerical) | Mean field ($d \geq 6$) |
|------|-----------|----------------|------------------------|
| $\beta_{\text{perc}}$ | 5/36 | 0.4181 | 1 |
| $\nu_{\text{perc}}$ | 4/3 | 0.8765 | 1/2 |
| $\gamma_{\text{perc}}$ | 43/18 | 1.795 | 1 |
| $\tau$ | 187/91 | 2.189 | 5/2 |

渗流的上临界维度是 $d_c = 6$（高于6维时平均场精确）。

**Refs**: Stauffer & Aharony, *Introduction to Percolation Theory* (1994); Smirnov, C. R. Acad. Sci. Paris 333, 239 (2001)（2D conformal invariance 的严格证明）

---

## Part 3: Connection to QEC — Error Chains as Percolation（与 QEC 的联系）

### Step 1: Error chains on the surface code（表面码上的错误链）

考虑 $L \times L$ 的表面码，独立 bit-flip 噪声（每个量子比特以概率 $p$ 发生 $X$ 错误）。

**syndrome 缺陷**：$Z$ 型稳定子测量值为 $-1$ 的面（plaquette），对应 $X$ 错误链的端点。参见 [04_qec/surface_code_basics.md, Step 2]。

**解码成功条件**：解码器找到的恢复链 $R$ 与实际错误链 $E$ 的组合 $R + E$（mod 2）不跨越系统（即在同一同调类中）。

**逻辑错误条件**：$R + E$ 包含跨越格子的非平凡环。

### Step 2: Percolation argument for threshold upper bound（渗流论证给出阈值上界）

**最简单的阈值上界**来自渗流：如果错误的占据概率 $p$ 低于 bond percolation threshold $p_c = 1/2$（在正方格子上），则几乎不可能形成跨越系统的错误链。

但这个界太粗糙了（$50\%$ 太高）。更精细的分析考虑到解码器只需要找到与 $E$ **同调等价**的链，而不是 $E$ 本身。

### Step 3: Optimal threshold from RBIM（最优阈值来自 RBIM 分析）

Dennis et al. (2002) 的统计力学映射给出更紧的阈值。将 surface code QEC 问题映射到 random-bond Ising model 后（详见 [qec_stat_mech_mapping.md]）：

**ML 解码器的阈值**（理论最优）= RBIM 在 Nishimori 线上的临界点：

$$p_c^{\text{ML}} \approx 10.9\% \quad \text{(2D, perfect syndrome)} \quad \text{[Dennis et al. 2002]}$$

**与纯 bond percolation 的关系**：

纯 bond percolation 给出了一个不同的、更简单的阈值概念——错误链本身是否渗流。RBIM 分析考虑了更多：不仅错误链的几何，还有解码器利用 syndrome 信息的能力。因此 RBIM 阈值（10.9%）远低于纯渗流阈值（50%），但远高于 naive 计算。

### Step 4: Surface code threshold from percolation — 10.3%

**MWPM 解码器**的阈值（约 $10.3\%$ 对独立 $X/Z$ 噪声）非常接近最优的 $10.9\%$。这个数值来自对 random-bond Ising model 的 Monte Carlo 模拟 [Honecker, Picco & Pujol, 2000]。

**注意**：$10.3\%$ 和 $10.9\%$ 的区别：
- $10.9\%$：Nishimori 线上 RBIM 的精确临界点（ML 解码器的极限）
- $10.3\%$：MWPM 解码器的实际阈值（略低于最优，因为 MWPM 不是 ML）

### Step 5: Phenomenological noise → 3D percolation（3D 渗流）

当 syndrome 测量本身也有噪声时（phenomenological noise model），需要重复测量 syndrome $d$ 轮。这将问题从 2D 提升到 **3D**：

- 2D 空间维度（格子）+ 1D 时间维度（syndrome 轮次）
- 错误链生活在 3D 时空格子上
- 解码问题映射到 **3D random-plaquette $Z_2$ gauge theory**（而非 2D RBIM）

**3D 模型的阈值**更低：
- $p = q$（代码错误率 = 测量错误率）时：$p_c \approx 3.3\%$（3D gauge theory）
- 实际 circuit-level noise 下：$p_c \approx 1\%$（MWPM 解码器）

**物理直觉**：3D 中渗流更容易（$p_c^{\text{3D}} < p_c^{\text{2D}}$），意味着更低的噪声就能导致跨越系统的错误，因此阈值降低。

**Refs**: Dennis et al. 2002, §4-5; Wang, Harrington & Preskill, Ann. Phys. 303, 31 (2003)

---

## Part 4: Rigorous Bounds from Percolation（渗流给出的严格界）

### Step 1: Dennis et al. lower bound on threshold

Dennis et al. (2002, §6) 通过分析 3D 模型中最小能量链（minimal chains）给出了阈值的严格下界。

对于 $p = q$ 的 phenomenological noise model：

$$p_c \geq 1.14\%$$

这是通过证明在 $p < 1.14\%$ 时，能量最小化（zero-temperature）解码器的失败概率在 $L \to \infty$ 时趋于零。

**证明思路**：在 3D 模型中，逻辑错误对应跨越系统的 surface（而非 2D 中的 path）。这个 surface 的面积至少为 $L^2$。利用 self-avoiding polygon/surface 的计数引理，当 $p$ 足够小时，大 surface 的概率被指数压制。

### Step 2: Hashing bound

另一个阈值上界来自量子信息论的 hashing bound [Bennett et al., 1996]：

$$p_c \leq p^* \quad \text{where} \quad 1 - H_2(p^*) - p^* \log_2 3 = 0$$

对于去极化噪声，$p^* \approx 18.9\%$（这是所有 stabilizer codes 的理论极限）。对于独立 $X/Z$ 噪声，hashing bound 给出 $H_2(p) = 1/2$，即 $p^* \approx 11.0\%$。

**Refs**: Dennis et al. 2002, §6; Bennett et al., PRA 54, 3824 (1996)

---

## Cross-references

- **[04_qec/threshold_theorem.md]**: 阈值定理的完整推导，包含渗流论证（Step 5）
- **[04_qec/decoder_theory.md]**: MWPM 和 ML 解码器的形式化
- **[04_qec/surface_code_basics.md]**: 表面码的格子结构和稳定子
- **[16_statistical_mechanics/ising_model.md]**: Ising 模型基础
- **[16_statistical_mechanics/qec_stat_mech_mapping.md]**: Dennis et al. 的完整映射
- **[08_topology/homology_basics.md]**: 同调理论（错误链的同调分类）
