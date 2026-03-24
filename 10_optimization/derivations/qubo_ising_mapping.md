# QUBO-Ising Mapping and Combinatorial Problem Encodings

> QUBO 与 Ising 模型的形式化定义、双射映射的完整推导，以及经典组合优化问题的 QUBO 编码。
>
> **References**: **[Farhi et al. 2014, §1]** (QUBO to quantum); **[Cappart et al. 2023, §2]** (CO problem encodings)

---

## 1. QUBO Definition and Properties

### 1.1 Definition

**Quadratic Unconstrained Binary Optimization (QUBO):**

$$\min_{\mathbf{x} \in \{0,1\}^n} H_{\text{QUBO}}(\mathbf{x}) = \mathbf{x}^\top Q \mathbf{x} = \sum_{i=1}^{n} \sum_{j=1}^{n} Q_{ij} x_i x_j$$

其中 $Q \in \mathbb{R}^{n \times n}$ 是上三角矩阵（或等价地，对称矩阵取上三角部分），$x_i \in \{0,1\}$。

### 1.2 Key Properties

**Property 1 (Idempotency).** 对于二进制变量 $x_i \in \{0,1\}$：$x_i^2 = x_i$。因此对角项 $Q_{ii} x_i^2 = Q_{ii} x_i$ 退化为线性项。

$$H_{\text{QUBO}}(\mathbf{x}) = \sum_{i} Q_{ii} x_i + \sum_{i < j} Q_{ij} x_i x_j$$

第一项是线性部分，第二项是二次交互部分。

**Property 2 (Universality).** 任何伪布尔函数 $f: \{0,1\}^n \to \mathbb{R}$ 都可以通过引入辅助变量，写成二次形式（quadratization），因此 QUBO 是通用的二进制优化框架。

**Property 3 (NP-hardness).** QUBO 是 NP-hard 的（包含 MaxCut 作为特例）。

**Source**: Kochenberger et al., *EJOR* 224 (2014) | Boros & Hammer, *Discrete Applied Mathematics* 123 (2002)

---

## 2. Ising Model

### 2.1 Definition

Ising 模型哈密顿量：

$$H_{\text{Ising}}(\mathbf{s}) = -\sum_{i < j} J_{ij} s_i s_j - \sum_{i} h_i s_i$$

其中 $s_i \in \{-1, +1\}$ 是自旋变量，$J_{ij}$ 是耦合强度（coupling），$h_i$ 是外场强度（local field）。

- $J_{ij} > 0$：铁磁耦合（倾向于 $s_i = s_j$，即自旋对齐）
- $J_{ij} < 0$：反铁磁耦合（倾向于 $s_i \neq s_j$，即自旋反对齐）
- 基态（ground state）是使 $H_{\text{Ising}}$ 最小化的自旋构型 $\mathbf{s}^*$

### 2.2 Physical Motivation

Ising 模型源自统计物理，描述晶格上自旋之间的相互作用。在组合优化中，寻找 Ising 基态等价于求解 QUBO，是量子退火器（D-Wave）和 QAOA 的原生问题格式。

---

## 3. QUBO ↔ Ising Bijection: Full Derivation

### 3.1 Variable Transformation

建立双射映射：

$$s_i = 2x_i - 1 \quad \iff \quad x_i = \frac{s_i + 1}{2}$$

其中 $x_i \in \{0,1\}$ 对应 $s_i \in \{-1, +1\}$：$x_i = 0 \mapsto s_i = -1$，$x_i = 1 \mapsto s_i = +1$。

### 3.2 Ising → QUBO 推导

将 $s_i = 2x_i - 1$ 代入 Ising 哈密顿量：

$$H_{\text{Ising}} = -\sum_{i<j} J_{ij} (2x_i - 1)(2x_j - 1) - \sum_i h_i (2x_i - 1)$$

展开乘积 $(2x_i - 1)(2x_j - 1) = 4x_i x_j - 2x_i - 2x_j + 1$：

$$H_{\text{Ising}} = -\sum_{i<j} J_{ij} (4x_i x_j - 2x_i - 2x_j + 1) - \sum_i h_i (2x_i - 1)$$

$$= -4\sum_{i<j} J_{ij} x_i x_j + 2\sum_{i<j} J_{ij}(x_i + x_j) - \sum_{i<j} J_{ij} - 2\sum_i h_i x_i + \sum_i h_i$$

整理线性项：对于顶点 $i$，$x_i$ 出现在所有含 $i$ 的耦合项中：

$$\sum_{i<j} J_{ij}(x_i + x_j) = \sum_i x_i \sum_{j: j \neq i} J_{ij}$$

（其中 $J_{ij} = J_{ji}$）。因此：

$$H_{\text{Ising}} = -4\sum_{i<j} J_{ij} x_i x_j + 2\sum_i x_i \sum_{j \neq i} J_{ij} - 2\sum_i h_i x_i + C$$

其中常数 $C = -\sum_{i<j} J_{ij} + \sum_i h_i$。

合并，得到 QUBO 形式 $H = \sum_i Q_{ii} x_i + \sum_{i<j} Q_{ij} x_i x_j + C$：

$$\boxed{Q_{ij} = -4J_{ij} \quad (i < j), \qquad Q_{ii} = 2\sum_{j \neq i} J_{ij} - 2h_i}$$

### 3.3 QUBO → Ising 推导

反向推导，将 $x_i = \frac{s_i + 1}{2}$ 代入 QUBO：

$$H_{\text{QUBO}} = \sum_i Q_{ii} \frac{s_i + 1}{2} + \sum_{i<j} Q_{ij} \frac{s_i + 1}{2} \cdot \frac{s_j + 1}{2}$$

展开：

$$= \frac{1}{2}\sum_i Q_{ii} s_i + \frac{1}{2}\sum_i Q_{ii} + \frac{1}{4}\sum_{i<j} Q_{ij}(s_i s_j + s_i + s_j + 1)$$

$$= \frac{1}{4}\sum_{i<j} Q_{ij} s_i s_j + \frac{1}{2}\sum_i Q_{ii} s_i + \frac{1}{4}\sum_{i<j} Q_{ij}(s_i + s_j) + C'$$

整理 $s_i$ 的系数：

$$= \frac{1}{4}\sum_{i<j} Q_{ij} s_i s_j + \sum_i \left(\frac{Q_{ii}}{2} + \frac{1}{4}\sum_{j \neq i} Q_{ij}\right) s_i + C'$$

对比 $H_{\text{Ising}} = -\sum_{i<j} J_{ij} s_i s_j - \sum_i h_i s_i + \text{const}$，得到：

$$\boxed{J_{ij} = -\frac{Q_{ij}}{4}, \qquad h_i = -\frac{Q_{ii}}{2} - \frac{1}{4}\sum_{j \neq i} Q_{ij}}$$

### 3.4 Summary

| QUBO | Ising |
|------|-------|
| $x_i \in \{0,1\}$ | $s_i \in \{-1,+1\}$ |
| $Q_{ij}$ (off-diagonal) | $J_{ij} = -Q_{ij}/4$ |
| $Q_{ii}$ (diagonal/linear) | $h_i = -Q_{ii}/2 - \frac{1}{4}\sum_{j \neq i} Q_{ij}$ |
| 最小化 $\mathbf{x}^\top Q \mathbf{x}$ | 最小化 $H_{\text{Ising}}$ |

两种表述完全等价，最优解通过 $s_i = 2x_i - 1$ 一一对应。

**Source**: Lucas, *Frontiers in Physics* 2, 5 (2014) | Glover et al. (2019)

---

## 4. Encoding CO Problems as QUBO

### 4.1 Maximum Independent Set (MIS)

$$H_{\text{MIS}} = -A \sum_{i \in V} x_i + B \sum_{(i,j) \in E} x_i x_j$$

其中 $A > 0$ 鼓励选更多顶点，$B > A$ 是惩罚系数，惩罚相邻顶点同时被选中。

要求 $B > A$ 保证任何违反独立集约束的解都不会是最优解。典型选取 $B = 2A$。

### 4.2 Maximum Clique (MCl)

在补图 $\bar{G} = (V, \bar{E})$ 上的 MIS 即为原图的 MCl：

$$H_{\text{MCl}} = -A \sum_{i \in V} x_i + B \sum_{(i,j) \in \bar{E}} x_i x_j$$

惩罚原图中不相邻的顶点对同时被选入团。

### 4.3 Minimum Vertex Cover (MVC)

$$H_{\text{MVC}} = A \sum_{i \in V} x_i + B \sum_{(i,j) \in E} (1 - x_i)(1 - x_j)$$

展开惩罚项：$(1-x_i)(1-x_j) = 1 - x_i - x_j + x_i x_j$，代入得

$$H_{\text{MVC}} = A \sum_i x_i + B\sum_{(i,j) \in E}(1 - x_i - x_j + x_i x_j)$$

$$= (A - 2B \cdot \deg(i)/?) \ldots$$

更清晰的写法：

$$H_{\text{MVC}} = A \sum_i x_i + B \sum_{(i,j) \in E} x_i x_j - 2B \sum_{(i,j) \in E} (x_i + x_j)/2 + B|E|$$

整理后对角项 $Q_{ii} = A - B \cdot \deg(i)$，交叉项 $Q_{ij} = B$ 对 $(i,j) \in E$，加常数 $B|E|$。

要求 $B > A$ 以惩罚未覆盖的边。

### 4.4 Maximum Cut (MaxCut)

$$H_{\text{MaxCut}} = -\sum_{(i,j) \in E} w_{ij}(x_i + x_j - 2x_i x_j)$$

取负号因为我们要最小化（QUBO 惯例），而 MaxCut 是最大化问题。QUBO 矩阵：

$$Q_{ii} = -\sum_{j: (i,j) \in E} w_{ij}, \qquad Q_{ij} = 2w_{ij} \; \text{for } (i,j) \in E$$

MaxCut 天然是 QUBO 形式，无需额外惩罚项。

### 4.5 Traveling Salesman Problem (TSP)

使用 $n^2$ 个二进制变量 $x_{i,t}$（$x_{i,t} = 1$ 表示城市 $i$ 在路径第 $t$ 步）：

$$H_{\text{TSP}} = A \sum_i \left(\sum_t x_{i,t} - 1\right)^2 + A \sum_t \left(\sum_i x_{i,t} - 1\right)^2 + B \sum_{(i,j)} d_{ij} \sum_t x_{i,t} x_{j,t+1}$$

- 第一项（惩罚）：每个城市恰好出现一次（行约束）
- 第二项（惩罚）：每个时间步恰好一个城市（列约束）
- 第三项（目标）：路径长度

展开约束惩罚项 $\left(\sum_t x_{i,t} - 1\right)^2 = \sum_t x_{i,t}^2 - 2\sum_t x_{i,t} + 1 + 2\sum_{t<t'} x_{i,t} x_{i,t'}$，利用 $x_{i,t}^2 = x_{i,t}$：

$$= -\sum_t x_{i,t} + 1 + 2\sum_{t<t'} x_{i,t} x_{i,t'}$$

这给出二次形式，从而整体 $H_{\text{TSP}}$ 是 QUBO。

要求 $A \gg B \cdot \max_{ij} d_{ij}$ 以保证约束被满足。

**Source**: Lucas, *Frontiers in Physics* 2, 5 (2014) | Kochenberger et al. (2014)

---

## 5. Connection to Quantum Computing

### 5.1 Quantum Annealing

量子退火利用量子涨落寻找 Ising 基态。系统哈密顿量随时间演化：

$$H(t) = -A(t) \sum_i \sigma_i^x + B(t) H_{\text{Ising}}$$

其中 $A(t)$ 从大值衰减到 0，$B(t)$ 从 0 增加到大值。初态为 $\sum_i \sigma_i^x$ 的基态（所有自旋的均匀叠加），末态为 $H_{\text{Ising}}$ 的基态。

绝热定理保证：若演化足够慢（$T \propto 1/\Delta_{\min}^2$，$\Delta_{\min}$ 是最小能隙），系统将停留在瞬时基态。D-Wave 量子退火器即基于此原理。

### 5.2 QAOA (Quantum Approximate Optimization Algorithm)

QAOA 是变分量子算法，参数化量子电路由 $p$ 层组成：

$$|\boldsymbol{\gamma}, \boldsymbol{\beta}\rangle = \prod_{l=1}^{p} e^{-i\beta_l H_M} e^{-i\gamma_l H_C} |+\rangle^{\otimes n}$$

其中 $H_C = H_{\text{Ising}}$ 是编码优化问题的代价哈密顿量，$H_M = \sum_i \sigma_i^x$ 是混合哈密顿量。

优化目标：

$$\max_{\boldsymbol{\gamma}, \boldsymbol{\beta}} \langle \boldsymbol{\gamma}, \boldsymbol{\beta} | H_C | \boldsymbol{\gamma}, \boldsymbol{\beta}\rangle$$

**QAOA 性质**：
- $p = 1$ 时，对 MaxCut 的近似比 $\geq 0.6924$（在 3-正则图上）
- $p \to \infty$ 时，理论上收敛到最优解
- QAOA 可视为量子退火的离散化（Trotterized）版本
- 实际中在 NISQ 设备上受限于噪声和量子比特连通性

### 5.3 From CO Problem to Quantum Circuit

完整的求解流程：
1. **建模**：将 CO 问题写成 ILP 形式
2. **QUBO 化**：用惩罚法将约束编码到目标函数
3. **Ising 映射**：通过 $s_i = 2x_i - 1$ 转为 Ising 哈密顿量
4. **量子电路**：将 $H_{\text{Ising}}$ 中的 $s_i s_j$ 项编译为 $ZZ$ 门（$e^{-i\gamma J_{ij} Z_i Z_j}$），$s_i$ 项编译为 $R_z$ 门
5. **测量**：在计算基下测量，采样得到候选解
6. **后处理**：对采样结果做经典后处理（如局部搜索）

**Source**: Farhi, Goldstone & Gutmann, arXiv:1411.4028 (2014) | Kadowaki & Nishimori, PRE 58 (1998)

---

---

## 6. Farhi原始论文中的MaxCut编码 (MaxCut Encoding from Farhi et al. 2014)

> 直接基于 **[Farhi et al. 2014, §1-§2]** 的原始表述。

### 6.1 一般子句形式 **[Farhi et al. 2014, §1]**

**[Farhi et al. 2014, Eq.(1)]** 将一般组合优化定义为：$n$ 比特、$m$ 子句，目标函数

$$C(z) = \sum_{\alpha=1}^m C_\alpha(z), \quad C_\alpha(z) \in \{0, 1\}$$

量子化后，$C$ 被视为计算基上的对角算符，本征值即为经典目标函数值。

### 6.2 MaxCut的具体编码 **[Farhi et al. 2014, §2, Eq.(12)-(13)]**

对图 $G$ 的MaxCut问题：

$$C = \sum_{\langle jk \rangle} C_{\langle jk \rangle}, \quad C_{\langle jk \rangle} = \frac{1}{2}(-\sigma_j^z \sigma_k^z + 1)$$

**[Farhi et al. 2014, Eq.(12)]**。这里每条边的贡献 $C_{\langle jk \rangle}$ 在量子比特 $j$ 和 $k$ 取不同值时为1（贡献到割），取相同值时为0。

期望值的边分解：

$$F_p(\boldsymbol{\gamma}, \boldsymbol{\beta}) = \sum_{\langle jk \rangle} \langle s| U^\dagger(C, \gamma_1) \cdots U^\dagger(B, \beta_p) \, C_{\langle jk \rangle} \, U(B, \beta_p) \cdots U(C, \gamma_1) |s\rangle$$

**[Farhi et al. 2014, Eq.(13)]**

### 6.3 独立集的受限编码 **[Farhi et al. 2014, §6]**

对独立集问题，QUBO编码为 $C(z) = \sum_j z_j$（汉明重量），但Hilbert空间被限制为仅包含独立集的合法字符串。混合算符 $B$ 定义为受限超立方体的邻接矩阵，$B$ 一般没有整数本征值。**[Farhi et al. 2014, §6, Eq.(37)]**

---

> **See also**: [../key_formulas.md] (F10.5, F10.13, F10.14, F10.15) | [np_hard_problems.md] | [neural_co_theory.md]
