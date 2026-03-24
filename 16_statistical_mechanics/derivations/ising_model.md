# Ising Model and Phase Transitions

> **Tags**: `ising`, `phase-transition`, `critical-phenomena`, `transfer-matrix`, `mean-field`

## Statement

Ising 模型是统计力学中最基本的格子模型，描述具有离散自旋自由度的系统。尽管定义简单（只有最近邻相互作用），它展现了丰富的物理：自发对称性破缺、二级相变、临界指数的普适性等。本文推导 1D 精确解（转移矩阵法）、2D 临界温度（Kramers-Wannier 对偶）、平均场理论、以及临界现象的一般理论。

## Prerequisites

- **线性代数**：矩阵本征值、迹 [01_linear_algebra/]
- **概率论**：概率分布、期望值
- **微积分**：偏导数、渐近分析

---

## Part 1: 1D Ising Model — Transfer Matrix Solution（1D Ising 精确解）

### Step 1: Setup（问题设置）

考虑一维链上 $N$ 个 Ising 自旋，$s_i \in \{+1, -1\}$，周期性边界条件 $s_{N+1} = s_1$。

$$H = -J \sum_{i=1}^{N} s_i s_{i+1} - h \sum_{i=1}^{N} s_i$$

配分函数：

$$Z = \sum_{s_1 = \pm 1} \cdots \sum_{s_N = \pm 1} \prod_{i=1}^{N} \exp\left[\beta J s_i s_{i+1} + \frac{\beta h}{2}(s_i + s_{i+1})\right]$$

注意我们将磁场项对称地分配到每对相邻自旋上（因为周期性边界条件，总贡献不变）。

### Step 2: Transfer matrix construction（转移矩阵构建）

定义 $2 \times 2$ 转移矩阵 $T$，矩阵元为：

$$T_{s_i, s_{i+1}} = \exp\left[\beta J s_i s_{i+1} + \frac{\beta h}{2}(s_i + s_{i+1})\right]$$

显式写出：

$$T = \begin{pmatrix} T_{++} & T_{+-} \\ T_{-+} & T_{--} \end{pmatrix} = \begin{pmatrix} e^{\beta J + \beta h} & e^{-\beta J} \\ e^{-\beta J} & e^{\beta J - \beta h} \end{pmatrix}$$

配分函数变为矩阵乘积的迹：

$$Z = \sum_{s_1} \cdots \sum_{s_N} T_{s_1 s_2} T_{s_2 s_3} \cdots T_{s_N s_1} = \text{Tr}(T^N)$$

### Step 3: Diagonalization（对角化）

$T$ 是实对称矩阵（在 $h = 0$ 时显然；$h \neq 0$ 时也可以通过相似变换化为对称形式）。本征值为：

$$\lambda_\pm = e^{\beta J} \cosh(\beta h) \pm \sqrt{e^{2\beta J} \sinh^2(\beta h) + e^{-2\beta J}}$$

因此：

$$\boxed{Z = \lambda_+^N + \lambda_-^N}$$

### Step 4: Thermodynamic limit（热力学极限）

由于 $\lambda_+ > \lambda_- > 0$（对所有有限 $T > 0$），在 $N \to \infty$ 时：

$$Z \approx \lambda_+^N \left[1 + \left(\frac{\lambda_-}{\lambda_+}\right)^N\right] \to \lambda_+^N$$

自由能密度（每自旋）：

$$f = -\frac{k_B T}{N} \ln Z \xrightarrow{N \to \infty} -k_B T \ln \lambda_+$$

**$h = 0$ 的特殊情况**：

$$\lambda_+ = 2\cosh(\beta J), \quad \lambda_- = 2\sinh(\beta J)$$

$$f = -k_B T \ln[2\cosh(\beta J)]$$

**1D Ising 无相变**：$\lambda_+$ 和 $\lambda_-$ 对所有 $T > 0$ 都是正的且 $\lambda_+ > \lambda_-$，所以自由能密度是 $T$ 的解析函数。**相变只能在 $T = 0$ 出现**（此时 $\lambda_+/\lambda_- \to \infty$，但热力学极限和 $T \to 0$ 极限不可交换）。

### Step 5: Correlation function（关联函数）

在 $h = 0$ 下，两点关联函数为：

$$\langle s_i s_j \rangle = \left(\frac{\lambda_-}{\lambda_+}\right)^{|i-j|} = [\tanh(\beta J)]^{|i-j|}$$

关联长度 $\xi$ 定义为 $\langle s_i s_j \rangle \sim e^{-|i-j|/\xi}$：

$$\xi = -\frac{1}{\ln[\tanh(\beta J)]}$$

当 $T \to 0$：$\tanh(\beta J) \to 1$，$\xi \to \infty$（准长程序）。
当 $T \to \infty$：$\tanh(\beta J) \to 0$，$\xi \to 0$（无关联）。

**Refs**: Kramers & Wannier, Phys. Rev. 60, 252 (1941); Baxter, *Exactly Solved Models in Statistical Mechanics*, Ch.2

---

## Part 2: 2D Ising Model — Critical Temperature（2D Ising 临界温度）

### Step 1: Kramers-Wannier Duality（KW 对偶）

**核心思想**：2D Ising 模型的高温展开和低温展开具有相同的数学结构，两者之间存在精确的对偶映射。

**低温展开**（$T \ll T_c$）：以全部自旋向上的基态 $\{s_i = +1\}$ 为参考态。翻转一组自旋对应在格子上画出 domain wall（翻转自旋区域的边界），每条 domain wall 边贡献因子 $e^{-2\beta J}$：

$$Z_{\text{low}} = 2 e^{-2NJ\beta} \sum_{n=0}^{\infty} g_n \, (e^{-2\beta J})^n$$

其中 $g_n$ 是长度为 $n$ 的闭合 domain wall 的数目，因子 2 来自全局翻转对称性。

**高温展开**（$T \gg T_c$）：将 $e^{\beta J s_i s_j}$ 展开为 $\cosh(\beta J)(1 + s_i s_j \tanh(\beta J))$：

$$Z_{\text{high}} = 2^N [\cosh(\beta J)]^{2N} \sum_{n=0}^{\infty} g_n^* \, [\tanh(\beta J)]^n$$

其中 $g_n^*$ 是对偶格子上长度为 $n$ 的闭合回路数目。

**对偶映射**：在正方格子上，格子与其对偶格子同构，因此 $g_n = g_n^*$。定义对偶关系：

$$e^{-2\beta^* J} = \tanh(\beta J) \quad \Longleftrightarrow \quad \sinh(2\beta^* J) \sinh(2\beta J) = 1$$

### Step 2: Self-duality and critical point（自对偶与临界点）

如果只有**一个**相变点，那么它必须在自对偶点上（因为对偶映射将高温映射到低温，相变点必须映射到自身）：

$$\beta_c = \beta_c^* \quad \Longrightarrow \quad \sinh(2\beta_c J) = 1$$

$$\boxed{\frac{k_B T_c}{J} = \frac{2}{\ln(1+\sqrt{2})} \approx 2.269}$$

**严格性说明**：Kramers-Wannier 的论证假设只有一个相变点。Onsager (1944) 的精确解证实了这个假设，并给出了完整的自由能表达式。

### Step 3: Onsager Solution — statement（Onsager 精确解）

Onsager (1944) 给出 2D Ising 模型在 $h = 0$ 时的精确自由能：

$$-\beta f = \ln 2 + \frac{1}{2\pi^2} \int_0^\pi d\theta_1 \int_0^\pi d\theta_2 \, \ln\left[\cosh^2(2\beta J) - \sinh(2\beta J)(\cos\theta_1 + \cos\theta_2)\right]$$

**临界行为**：在 $T = T_c$ 附近，比热发散为：

$$C \sim -\ln|T - T_c| \quad (\alpha = 0, \text{ logarithmic divergence})$$

**自发磁化**（Yang, 1952）：

$$m = \begin{cases} [1 - \sinh^{-4}(2\beta J)]^{1/8} & T < T_c \\ 0 & T \geq T_c \end{cases}$$

临界指数 $\beta_{\text{mag}} = 1/8$。

**Refs**: Onsager, Phys. Rev. 65, 117 (1944); Yang, Phys. Rev. 85, 808 (1952)

---

## Part 3: Mean Field Theory（平均场理论）

### Step 1: Mean field approximation（平均场近似）

用平均磁化替代每个自旋的邻居：$s_j \approx m = \langle s_j \rangle$。每个自旋感受到的有效场为：

$$h_{\text{eff}} = zJm + h$$

其中 $z$ 是配位数（正方格子 $z = 4$，三角格子 $z = 6$）。

### Step 2: Self-consistency equation（自洽方程）

$$m = \langle s_i \rangle = \tanh(\beta h_{\text{eff}}) = \tanh[\beta(zJm + h)]$$

在 $h = 0$ 时：

$$\boxed{m = \tanh(\beta z J m)}$$

### Step 3: Critical temperature（临界温度）

在 $m = 0$ 附近展开 $\tanh$ 到三阶：$m \approx \beta z J m - \frac{1}{3}(\beta z J m)^3 + \cdots$

非零解存在的条件：$\beta z J > 1$，即：

$$\boxed{k_B T_c^{\text{MF}} = z J}$$

对于正方格子（$z = 4$）：$k_B T_c^{\text{MF}} = 4J$，而精确值 $k_B T_c \approx 2.269 J$。平均场**高估**了临界温度（因为忽略了涨落）。

### Step 4: Mean field critical exponents（平均场临界指数）

在 $T \to T_c^-$ 附近，$m$ 小：

$$m \approx \beta zJ m - \frac{1}{3}(\beta zJ)^3 m^3$$

$$m^2 \approx 3\frac{\beta zJ - 1}{(\beta zJ)^3} \approx 3\frac{T_c - T}{T_c} \cdot \frac{1}{(\beta zJ)^2}$$

$$m \sim (T_c - T)^{1/2}$$

平均场临界指数：$\beta_{\text{mag}} = 1/2$, $\gamma = 1$, $\delta = 3$, $\nu = 1/2$, $\eta = 0$, $\alpha = 0$。

**适用条件**：平均场理论在维度 $d > d_c = 4$（上临界维度）时精确。

---

## Part 4: Phase Transitions — General Theory（相变一般理论）

### First order vs second order（一级相变 vs 二级相变）

| 特征 | 一级相变 | 二级相变（连续相变） |
|------|---------|-------------------|
| 序参量 | 在 $T_c$ 处不连续跳变 | 在 $T_c$ 处连续趋于零 |
| 潜热 | 有（$\Delta S \neq 0$） | 无（$\Delta S = 0$） |
| 关联长度 | 有限 | 发散（$\xi \to \infty$） |
| 自由能 | 一阶导不连续 | 二阶或更高阶导不连续/发散 |
| 例子 | 冰-水，liquid crystal | 铁磁转变，超导转变 |

Ising 模型在 $h = 0$ 时经历**二级相变**。在 $T < T_c$ 的一阶线 $h = 0$ 上（$m$ 从正跳到负），有**一级相变**。

### Critical exponents and universality（临界指数与普适性）

在 $T \to T_c$ 附近，热力学量呈现幂律行为：

| 指数 | 定义 | 2D Ising | 3D Ising | Mean Field |
|------|------|----------|----------|------------|
| $\alpha$ | $C \sim \|t\|^{-\alpha}$ | 0 (log) | 0.110 | 0 |
| $\beta_{\text{mag}}$ | $m \sim \|t\|^{\beta}$ | 1/8 | 0.3265 | 1/2 |
| $\gamma$ | $\chi \sim \|t\|^{-\gamma}$ | 7/4 | 1.237 | 1 |
| $\delta$ | $m \sim h^{1/\delta}$ ($T=T_c$) | 15 | 4.789 | 3 |
| $\nu$ | $\xi \sim \|t\|^{-\nu}$ | 1 | 0.6300 | 1/2 |
| $\eta$ | $G(r) \sim r^{-(d-2+\eta)}$ ($T=T_c$) | 1/4 | 0.0363 | 0 |

其中 $t = (T - T_c)/T_c$ 是约化温度。

**Scaling relations**（只有2个独立指数）：

$$\alpha + 2\beta + \gamma = 2 \quad \text{(Rushbrooke)}$$
$$\gamma = \beta(\delta - 1) \quad \text{(Widom)}$$
$$\gamma = (2 - \eta)\nu \quad \text{(Fisher)}$$
$$d\nu = 2 - \alpha \quad \text{(hyperscaling, } d \leq d_c \text{)}$$

**普适性**：临界指数只依赖于空间维度 $d$、序参量的对称性（$Z_2$ for Ising）和相互作用的力程，而不依赖于格子结构、$J$ 的具体值等微观细节。这就是为什么 Ising model 的临界行为可以描述如此多不同的物理系统。

**与 QEC 的联系**：QEC 阈值作为相变，其临界指数属于 random-bond Ising model 的普适类（与纯 Ising 不同）。Nishimori 线上的多临界点有自己的普适性。

**Refs**: Fisher, Rev. Mod. Phys. 46, 597 (1974); Kadanoff, Physics 2, 263 (1966); Wilson, Rev. Mod. Phys. 47, 773 (1975)

---

## Cross-references

- **[04_qec/threshold_theorem.md]**: 阈值定理的渗流/Ising 模型解释
- **[04_qec/surface_code_basics.md]**: 表面码格子结构（Ising 模型定义在其上）
- **[10_optimization/qubo_ising_mapping.md]**: QUBO 问题到 Ising 模型的映射
- **[16_statistical_mechanics/percolation_theory.md]**: 渗流理论
- **[16_statistical_mechanics/qec_stat_mech_mapping.md]**: Dennis et al. 的核心映射
