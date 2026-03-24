# QEC-Statistical Mechanics Mapping

> **Tags**: `stat-mech-mapping`, `RBIM`, `Nishimori-line`, `Dennis-mapping`, `Z2-gauge`, `toric-code`, `error-threshold`, `phase-transition`, `disorder`, `replica`

## Statement

Dennis, Kitaev, Landahl, Preskill (2002) 发现了量子纠错与统计力学之间的深刻映射：toric code 的解码问题等价于随机键 Ising 模型（Random-Bond Ising Model, RBIM）的相变问题。这个映射将 QEC 的纠错阈值精确对应到统计力学模型在 Nishimori 线上的有序-无序相变点。本文详细推导这一映射及其物理意义。

## Prerequisites

- **Stabilizer formalism** [04_quantum_error_correction/derivations/stabilizer_formalism.md]
- **Surface code** [04_quantum_error_correction/derivations/surface_code_basics.md]
- **Ising model** [16_statistical_mechanics/derivations/ising_model.md]
- **Percolation theory** [16_statistical_mechanics/derivations/percolation_theory.md]

---

## Part 1: Toric Code 复习

### Step 1: Toric code 定义

在 $L \times L$ 的环面（torus）上，量子比特位于边（edges）上 [Kitaev, arXiv:quant-ph/9707021]：

- **星算子（vertex/star operator）**：$A_v = \prod_{e \ni v} X_e$（作用在与顶点 $v$ 相连的4条边上）
- **面算子（plaquette operator）**：$B_p = \prod_{e \in \partial p} Z_e$（作用在面 $p$ 的4条边界边上）
- **码空间**：$A_v |\psi\rangle = +|\psi\rangle$, $B_p |\psi\rangle = +|\psi\rangle$ 对所有 $v, p$
- **逻辑算子**：环绕环面非平凡循环的 $X$-链和 $Z$-链

### Step 2: 错误和 Syndrome

假设独立的 $Z$ 错误（bit-flip channel），每条边以概率 $p$ 发生 $Z$ 错误。错误模式 $E \subseteq \mathrm{edges}$。

**Syndrome**（从 $A_v$ 测量得到）：

$$s_v = (-1)^{|\{e \ni v : e \in E\}| \bmod 2}$$

$s_v = -1$ 表示在顶点 $v$ 处检测到一个 defect（anyon）。Defect 总是成对出现。

### Step 3: 解码问题

给定 syndrome $s$，找到修正 $C$ 使得 $C + E$（mod 2）是平凡的（可收缩的）。关键：$C + E$ 不需要等于零，只需与零同调（homologous），即不缠绕环面。

---

## Part 2: Dennis 映射——从 QEC 到 RBIM

### Step 2.1: 配分函数构造 [Dennis et al., J. Math. Phys. 43, 4452 (2002)]

**核心想法**：将错误概率用 Boltzmann 权重表示。

对于独立去极化噪声，边 $e$ 发生 $Z$ 错误的概率为 $p$，不发生的概率为 $1-p$。定义：

$$e^{-2\beta_p J} = \frac{p}{1-p} \quad \Leftrightarrow \quad \beta_p J = -\frac{1}{2}\ln\frac{p}{1-p}$$

其中 $\beta_p$ 是 Nishimori 温度对应的逆温度。

错误模式 $E$ 的概率可写为：

$$P(E) = \prod_{e} \left[\frac{e^{\beta_p J \tau_e}}{2\cosh(\beta_p J)}\right]$$

其中 $\tau_e = +1$ 表示边 $e$ 无错误，$\tau_e = -1$ 表示有错误。

### Step 2.2: 映射到 RBIM

引入 Ising 自旋 $\sigma_v \in \{+1, -1\}$ 在每个顶点上。定义随机键 Ising 模型（RBIM）的 Hamiltonian：

$$H[\sigma; \tau] = -J \sum_{\langle v, v' \rangle} \tau_{vv'} \sigma_v \sigma_{v'}$$

其中 $\tau_{vv'} = \tau_e$ 是边 $e = (v, v')$ 上的随机键（quenched disorder），由错误模式决定。

**RBIM 配分函数**：

$$Z[\tau] = \sum_{\{\sigma\}} \exp\left(\beta J \sum_{\langle v, v' \rangle} \tau_{vv'} \sigma_v \sigma_{v'}\right)$$

### Step 2.3: 核心映射定理

**定理** [Dennis et al., 2002]：toric code 在独立 $Z$-错误模型下的最大似然解码成功概率，等价于 2D RBIM 在 Nishimori 温度 $\beta = \beta_p$ 处的有序相概率。

具体地：
- **解码成功** ↔ RBIM 铁磁有序相（自旋对齐）
- **解码失败** ↔ RBIM 顺磁无序相（自旋随机）
- **纠错阈值 $p_c$** ↔ Nishimori 线上的有序-无序相变点

---

## Part 3: Nishimori 线和相图

### Step 3.1: Nishimori 条件

Nishimori 线定义为逆温度 $\beta$ 等于 disorder 的 Nishimori 温度 $\beta_p$ [Nishimori, Prog. Theor. Phys. 66, 1169 (1981)]：

$$\beta = \beta_p \quad \Leftrightarrow \quad e^{-2\beta J} = \frac{p}{1-p}$$

**物理含义**：在 Nishimori 线上，热涨落和淬火无序（quenched disorder）的强度完全匹配。

### Step 3.2: Nishimori 线的特殊性质

在 Nishimori 线上，以下恒等式成立：

1. **Gauge 对称性**：

$$[\langle \sigma_v \sigma_{v'} \rangle^{2n}]_{\mathrm{dis}} = [\langle \sigma_v \sigma_{v'} \rangle^{n}]_{\mathrm{dis}}$$

其中 $[\cdot]_{\mathrm{dis}}$ 表示对 disorder 取平均，$\langle \cdot \rangle$ 表示热力学平均。

2. **内能恒等式**：

$$[E]_{\mathrm{dis}} = -NJ(1-2p)$$

3. **相变的特殊性质**：在 Nishimori 线上的相变点 $p_c$，有：
   - 自发磁化连续消失
   - 不可能存在自旋玻璃相（spin glass phase）

### Step 3.3: RBIM 相图

2D RBIM 的相图（$p$-$T$ 平面）包含三个区域：

```
T (温度)
|
|    顺磁 (PM)
|   /
|  / Nishimori 线
| /
|/______ 铁磁 (FM)
|       \
|  自旋  \
|  玻璃   \
|  (SG)   \
+----------→ p (disorder)
0    p_c    0.5
```

**关键点**：
- 铁磁相 ↔ 解码成功
- 顺磁/自旋玻璃相 ↔ 解码失败
- Nishimori 线上的相变点 $p_c$ = QEC 阈值

---

## Part 4: 阈值的精确计算

### Step 4.1: $\mathbb{Z}_2$ Gauge Theory 映射

Dennis 映射可以进一步等价为 $\mathbb{Z}_2$ 格规理论。引入 gauge 变量 $u_{vv'} \in \{+1, -1\}$ 在每条边上：

$$Z = \sum_{\{u\}} \prod_{\langle v, v' \rangle} e^{\beta_p J u_{vv'}} \prod_p \left(\sum_{\sigma_p = \pm 1} e^{\beta J \sigma_p \prod_{e \in \partial p} u_e}\right)$$

**Wilson loop** $W(\Gamma) = \prod_{e \in \Gamma} u_e$ 的行为决定了相：
- 铁磁相：Wilson loop 满足 perimeter law → 解码成功
- 顺磁相：Wilson loop 满足 area law → 解码失败

### Step 4.2: 数值结果

通过 Monte Carlo 模拟 RBIM 在 Nishimori 线上的相变：

| 码类型 | 噪声模型 | 阈值 $p_c$ | 方法 |
|--------|---------|-----------|------|
| Toric code | 独立 $X$/$Z$ | $10.917(3)\%$ | MC [Dennis 2002; Merz & Chalker 2002] |
| Toric code | 去极化 | $\approx 18.9\%$ | MC [Bombin et al.] |
| Planar surface code | 独立 $X$/$Z$ | $10.31(1)\%$ | MC |
| Toric code (MWPM) | 独立 $X$/$Z$ | $10.31\%$ | MWPM decoder |

> **重要**：$10.917\%$ 是**最优解码**阈值（最大似然解码），对应 RBIM 相变点。实际解码器（如 MWPM 的 $10.31\%$）的阈值总是更低。

### Step 4.3: 阈值的意义

在 $p < p_c$ 时，逻辑错误率随码距 $d$ 指数衰减：

$$P_L \sim \exp\left(-\alpha(p) \cdot d\right), \quad \alpha(p) > 0 \text{ for } p < p_c$$

在 $p > p_c$ 时，增大码距无法降低逻辑错误率。

---

## Part 5: 推广到更一般的情况

### Step 5.1: 推广到有相关错误

当错误不独立时（如 crosstalk 导致的相关错误），映射变为更复杂的 disorder 模型。但 Dennis 框架仍然适用，disorder 的结构对应错误的相关性。

### Step 5.2: 推广到其他拓扑码

| 码 | 统计力学模型 | 阈值（ML） |
|----|------------|-----------|
| Toric code | 2D RBIM | 10.917% |
| Color code | 2D 3-body RBIM | ~10.9% |
| 3D toric code (string-like errors) | 3D RBIM | ~3.3% |
| Hyperbolic surface codes | RBIM on hyperbolic lattice | 依赖几何 |

### Step 5.3: 推广到测量错误（phenomenological noise）

当 syndrome 测量本身有错误（概率 $q$）时，需要在时间方向上堆叠 syndrome：

$$p_c \text{ (phenomenological)} < p_c \text{ (code capacity)}$$

对 toric code：$p_c \approx 2.93\%$（phenomenological, $p = q$），对应 3D RBIM 在 Nishimori 线上的相变。

---

## Part 6: Replica Method 和解析方法

### Step 6.1: Replica 技巧

计算 quenched 自由能需要 replica method：

$$[F]_{\mathrm{dis}} = -\frac{1}{\beta}[\ln Z]_{\mathrm{dis}} = -\frac{1}{\beta}\lim_{n \to 0} \frac{[Z^n]_{\mathrm{dis}} - 1}{n}$$

**$[Z^n]$** 可以通过引入 $n$ 个 replica 系统来计算：

$$[Z^n]_{\mathrm{dis}} = \sum_{\{\sigma^{(1)}\}} \cdots \sum_{\{\sigma^{(n)}\}} \prod_e \left[(1-p)e^{\beta J \sum_a \sigma_v^{(a)}\sigma_{v'}^{(a)}} + p \cdot e^{-\beta J \sum_a \sigma_v^{(a)}\sigma_{v'}^{(a)}}\right]$$

### Step 6.2: 与量子信息的联系

- **Replica 对称性**（RS）假设对应 Nishimori 线以上
- **Replica 对称性破缺**（RSB）可能出现在 Nishimori 线以下的自旋玻璃相
- Nishimori 线上不存在 RSB（这与 Nishimori 线的 gauge 对称性直接相关）

---

## Summary

Dennis 映射的核心对应关系：

| QEC 概念 | 统计力学概念 |
|---------|------------|
| 量子比特（边上） | Ising 键 |
| Stabilizer (vertex/plaquette) | 局部约束 |
| 错误模式 | Quenched disorder 配置 |
| 错误概率 $p$ | Nishimori 温度 $\beta_p$ |
| Syndrome | Frustrated plaquettes |
| 解码成功 | 铁磁有序相 |
| 解码失败 | 无序相 |
| 纠错阈值 $p_c$ | Nishimori 线上的相变点 |
| 最大似然解码 | 自由能最小化 |
| 码距 → ∞ | 热力学极限 $L \to \infty$ |

**关键公式**：$e^{-2\beta_p J} = p/(1-p)$，连接错误概率和 Nishimori 温度。

---

## Cross-References

- **Toric code** → [04_quantum_error_correction/derivations/surface_code_basics.md]
- **Stabilizer formalism** → [04_quantum_error_correction/derivations/stabilizer_formalism.md]
- **Ising model** → [16_statistical_mechanics/derivations/ising_model.md]
- **Percolation** → [16_statistical_mechanics/derivations/percolation_theory.md]
- **Decoder theory** → [04_quantum_error_correction/derivations/decoder_theory.md]
- **阈值定理** → [04_quantum_error_correction/derivations/threshold_theorem.md]
- **拓扑码** → [08_topology/derivations/topological_codes_connection.md]
- **噪声模型** → [04_quantum_error_correction/derivations/noise_models.md]
