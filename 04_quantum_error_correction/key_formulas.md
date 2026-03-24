# Chapter 4: Quantum Error Correction - Key Formulas

> 量子纠错（QEC）核心公式速查表。所有公式均使用 LaTeX 记号，解释使用中文。

---

## 基础条件与框架

### F4.1: Knill-Laflamme Quantum Error Correction Conditions

$$\langle \psi_i | E_a^\dagger E_b | \psi_j \rangle = C_{ab} \delta_{ij}$$

其中 $|\psi_i\rangle, |\psi_j\rangle$ 是码空间的正交基矢，$E_a, E_b$ 是错误算子，$C_{ab}$ 是仅依赖于错误而不依赖于码字的 Hermitian 矩阵元素。这是量子纠错码能纠正一组错误 $\{E_a\}$ 的充要条件。

等价的投影算子形式：

$$P E_a^\dagger E_b P = C_{ab} P$$

其中 $P = \sum_i |\psi_i\rangle\langle\psi_i|$ 是码空间的投影算子。

**Source**: [derivations/knill_laflamme_conditions.md] | **[Nielsen & Chuang, Theorem 10.1, p.436]**; Knill & Laflamme, PRA 55, 900 (1997)

---

### F4.2: Stabilizer State Definition

$$|\psi\rangle = \frac{1}{2^k} \prod_{i=1}^{n-k} (I + g_i) |\psi_0\rangle$$

其中 $g_1, g_2, \ldots, g_{n-k}$ 是稳定子群 $\mathcal{S}$ 的独立生成元，每个 $g_i$ 是 $n$ 量子比特 Pauli 群的元素且满足 $g_i^2 = I$。码空间定义为所有生成元的 $+1$ 特征值子空间：

$$\mathcal{C} = \{ |\psi\rangle : g_i |\psi\rangle = |\psi\rangle, \; \forall i = 1, \ldots, n-k \}$$

一个 $[[n, k]]$ 稳定子码用 $n$ 个物理量子比特编码 $k$ 个逻辑量子比特，稳定子群有 $n-k$ 个独立生成元。

**Source**: [derivations/stabilizer_formalism.md] | **[Nielsen & Chuang, Theorem 10.3, p.457; Section 10.5.1, p.456]**; Gottesman, PhD thesis (1997)

---

### F4.3: Syndrome Measurement

$$s_i = \begin{cases} 0 & \text{if } g_i E |\psi\rangle = + E|\psi\rangle \\ 1 & \text{if } g_i E |\psi\rangle = - E|\psi\rangle \end{cases}$$

等价地，对于错误 $E$ 和稳定子生成元 $g_i$：

$$s_i = \begin{cases} 0 & \text{if } [E, g_i] = 0 \quad \text{(对易)} \\ 1 & \text{if } \{E, g_i\} = 0 \quad \text{(反对易)} \end{cases}$$

syndrome 向量 $\mathbf{s} = (s_1, s_2, \ldots, s_{n-k})$ 唯一标识了错误的等价类，不会泄露任何关于编码态的信息。测量所有稳定子生成元后，可以根据 syndrome 确定需要施加的恢复操作。

**Source**: [derivations/stabilizer_formalism.md] | **[Nielsen & Chuang, Section 10.5.2, p.459]**

---

## 码构造

### F4.4: CSS Code Construction

给定两个经典线性码 $C_1$ 和 $C_2$，满足 $C_2 \subseteq C_1$（即 $C_2$ 是 $C_1$ 的子码），其中 $C_1$ 是 $[n, k_1, d_1]$ 码，$C_2$ 是 $[n, k_2, d_2]$ 码，则可以构造量子 CSS 码：

$$\text{CSS}(C_1, C_2) = [[n, \; k_1 - k_2, \; \min(d_1, d_2^\perp)]]$$

其中 $d_2^\perp$ 是 $C_2^\perp$（$C_2$ 的对偶码）的最小距离。CSS 码的码字为：

$$|x + C_2\rangle = \frac{1}{\sqrt{|C_2|}} \sum_{y \in C_2} |x + y\rangle, \quad x \in C_1$$

$X$ 型稳定子来自 $C_2$ 的码字，$Z$ 型稳定子来自 $C_1^\perp$ 的码字。

**Source**: [derivations/css_codes.md] | **[Nielsen & Chuang, Section 10.4.2, p.450]**; Calderbank & Shor (1996); Steane (1996)

---

### F4.5: Surface Code Parameters

Surface code（表面码）是定义在二维方格子上的 $[[n, k, d]]$ 拓扑稳定子码：

**Toric code（环面码）**：在 $L \times L$ 的环面上，

$$[[n, k, d]] = [[2L^2, \; 2, \; L]]$$

**Planar code（平面码）**：在 $L \times L$ 的平面上（带边界），

$$[[n, k, d]] = [[2L^2 - 2L + 1, \; 1, \; L]]$$

或近似写为 $[[(2d-1)^2 + (2d-2)^2)/2, \; 1, \; d]]$。对于 $d \times d$ 的平面码，物理量子比特数为：

$$n = d^2 + (d-1)^2 = 2d^2 - 2d + 1$$

码距 $d$ 等于最短逻辑算子（连接两个相对边界的路径）的长度。

**Source**: [derivations/surface_code_basics.md] | Kitaev (1997); Bravyi & Kitaev (1998)

---

### F4.6: Threshold Theorem

对于码距为 $d$ 的拓扑码（如表面码），在物理错误率 $p$ 低于阈值 $p_{\text{th}}$ 时，逻辑错误率指数衰减：

$$p_L \sim A \left( \frac{p}{p_{\text{th}}} \right)^{\lfloor d/2 \rfloor + 1}$$

其中 $A$ 是常数前因子，$\lfloor d/2 \rfloor + 1$ 是导致逻辑错误所需的最少物理错误数。当 $p < p_{\text{th}}$ 时，增大 $d$ 可使 $p_L$ 指数级降低。对于表面码 + MWPM 解码器，$p_{\text{th}} \approx 1.1\%$（去极化噪声）或 $p_{\text{th}} \approx 10.3\%$（独立 $X/Z$ 噪声）。

对于级联码，阈值定理表述为：

$$p_L^{(l)} \leq \frac{1}{C} \left( C \cdot p \right)^{2^l}$$

其中 $l$ 是级联层数，$C$ 是与码有关的常数。

**Source**: [derivations/threshold_theorem.md] | **[Nielsen & Chuang, Theorem 10.6, p.480; Section 10.6, pp.470-499]**; Aharonov & Ben-Or (1997); Dennis et al. (2002)

---

### F4.7: Toric Code Hamiltonian

$$H = -J_s \sum_{s} A_s - J_p \sum_{p} B_p$$

其中 star 算子和 plaquette 算子定义为：

$$A_s = \prod_{i \in \text{star}(s)} X_i, \qquad B_p = \prod_{i \in \text{boundary}(p)} Z_i$$

$A_s$ 作用于顶点 $s$ 周围的4条边上的量子比特（施加 $X$ 算子），$B_p$ 作用于面 $p$ 周围的4条边上的量子比特（施加 $Z$ 算子）。所有 $A_s$ 和 $B_p$ 相互对易，基态是所有 $A_s = +1$ 且 $B_p = +1$ 的本征态。激发态对应于 anyonic excitation：$A_s = -1$ 产生 $e$ 粒子（电荷），$B_p = -1$ 产生 $m$ 粒子（磁通量）。

**Source**: [derivations/surface_code_basics.md] | Kitaev, Ann. Phys. 303, 2 (2003)

---

## 解码与逻辑操作

### F4.8: Minimum Weight Perfect Matching (MWPM) Decoder

给定 syndrome $\mathbf{s}$，MWPM 解码器的目标是在syndrome图上找到最小权重的完美匹配：

$$\hat{E} = \arg\min_{E: \sigma(E) = \mathbf{s}} \text{wt}(E)$$

等价地，构造 syndrome 图 $G = (V, E_G)$：
- 顶点 $V$：所有非平凡 syndrome 位（$s_i = 1$ 的稳定子）
- 边 $(u,v) \in E_G$：权重 $w(u,v) = -\log \frac{p_{uv}}{1-p_{uv}}$，其中 $p_{uv}$ 是连接 $u, v$ 的最短错误链的概率

MWPM 在此加权图上找到最小权重完美匹配，时间复杂度为 $O(n^3)$（Edmonds 算法），其中 $n$ 是 syndrome 缺陷数。

**Source**: [derivations/decoder_theory.md] | Dennis et al., J. Math. Phys. 43, 4452 (2002)

---

### F4.9: Logical Operators for Surface Code

在平面码中，逻辑 $\bar{X}$ 和 $\bar{Z}$ 算子是连接相对边界的 string operator：

$$\bar{X} = \prod_{i \in \gamma_X} X_i, \qquad \bar{Z} = \prod_{j \in \gamma_Z} Z_j$$

其中 $\gamma_X$ 是从上边界到下边界的一条路径（穿过面），$\gamma_Z$ 是从左边界到右边界的一条路径（穿过顶点）。关键性质：

1. **与所有稳定子对易**：$[\bar{X}, g_i] = 0$ 且 $[\bar{Z}, g_i] = 0$，$\forall g_i \in \mathcal{S}$
2. **彼此反对易**：$\bar{X}\bar{Z} = -\bar{Z}\bar{X}$
3. **不在稳定子群中**：$\bar{X} \notin \mathcal{S}$，$\bar{Z} \notin \mathcal{S}$
4. **最短路径长度等于码距**：$d = \min(|\gamma_X|, |\gamma_Z|) = L$

**Source**: [derivations/surface_code_basics.md] | Fowler et al., PRA 86, 032324 (2012)

---

## 编码理论界限

### F4.10: Code Rate

$$R = \frac{k}{n}$$

其中 $k$ 是编码的逻辑量子比特数，$n$ 是使用的物理量子比特数。对于表面码 $R = 1/n \to 0$（当 $d \to \infty$），这是拓扑码的固有代价。对于好的量子 LDPC 码，存在 $R = \Theta(1)$ 且 $d = \Theta(n^{1/2})$ 甚至更好的码族。

量子 encoding rate 与经典类似，但受到更严格的量子界限限制。

**Source**: 基本定义 | Gottesman (1997)

---

### F4.11: Quantum Singleton Bound

$$k \leq n - 2(d - 1)$$

等价形式：

$$d \leq \frac{n - k}{2} + 1$$

对于一个 $[[n, k, d]]$ 量子纠错码（无论是否退化），码距 $d$、逻辑量子比特数 $k$、物理量子比特数 $n$ 必须满足此界限。达到此界限的码称为 quantum MDS (Maximum Distance Separable) 码。

注意：这个界限对退化码和非退化码都成立，这与经典情况不同——经典 Singleton bound 只需要 $d \leq n - k + 1$，量子版本多了一个因子2，反映了量子信息需要同时纠正 $X$ 和 $Z$ 错误。

**Source**: [derivations/code_distance_bounds.md] | **[Nielsen & Chuang, Theorem 10.2, p.444]**; Knill & Laflamme (1997); Rains (1999)

---

### F4.12: Quantum Hamming Bound

对于一个非退化的 $[[n, k, d]]$ 量子码，能纠正 $t = \lfloor(d-1)/2\rfloor$ 个错误，必须满足：

$$\sum_{j=0}^{t} \binom{n}{j} 3^j \leq 2^{n-k}$$

左边计数了作用在 $n$ 个量子比特上、权重不超过 $t$ 的所有非平凡 Pauli 错误模式数（每个位置有 $X, Y, Z$ 三种非平凡 Pauli 算子，故因子 $3^j$）。右边是 syndrome 空间的大小 $2^{n-k}$。达到此界限的码称为 quantum perfect code。

注意：退化码可以违反此界限，因为不同错误可以有相同的效果（degeneracy），这是量子纠错码独有的现象。

**Source**: [derivations/code_distance_bounds.md] | **[Nielsen & Chuang, Eq. 10.57, p.444]**; Gottesman (1997)

---

## 具体码与噪声模型

### F4.13: Steane Code [[7, 1, 3]]

Steane 码是基于经典 $[7, 4, 3]$ Hamming 码的 CSS 码。取 $C_1 = [7, 4, 3]$ Hamming 码，$C_2 = C_1^\perp = [7, 3, 4]$（其对偶码），由于 $C_2 \subseteq C_1$，构造 CSS 码：

$$\text{CSS}(C_1, C_1^\perp) = [[7, \; 4 - 3, \; 3]] = [[7, 1, 3]]$$

稳定子生成元（6个，对应 $n - k = 6$）：

| 生成元 | $q_1$ | $q_2$ | $q_3$ | $q_4$ | $q_5$ | $q_6$ | $q_7$ |
|--------|--------|--------|--------|--------|--------|--------|--------|
| $g_1$ | $I$ | $I$ | $I$ | $X$ | $X$ | $X$ | $X$ |
| $g_2$ | $I$ | $X$ | $X$ | $I$ | $I$ | $X$ | $X$ |
| $g_3$ | $X$ | $I$ | $X$ | $I$ | $X$ | $I$ | $X$ |
| $g_4$ | $I$ | $I$ | $I$ | $Z$ | $Z$ | $Z$ | $Z$ |
| $g_5$ | $I$ | $Z$ | $Z$ | $I$ | $I$ | $Z$ | $Z$ |
| $g_6$ | $Z$ | $I$ | $Z$ | $I$ | $Z$ | $I$ | $Z$ |

逻辑算子：$\bar{X} = X^{\otimes 7}$，$\bar{Z} = Z^{\otimes 7}$。此码能纠正任意单量子比特错误（$t = \lfloor(3-1)/2\rfloor = 1$）。

**Source**: [derivations/css_codes.md] | **[Nielsen & Chuang, Section 10.4.2, p.450-453]**; Steane, PRL 77, 793 (1996)

---

### F4.14: Depolarizing Channel Kraus Operators

去极化信道 $\mathcal{E}_{\text{dep}}$ 对单个量子比特的作用：

$$\mathcal{E}_{\text{dep}}(\rho) = (1-p)\rho + \frac{p}{3}(X\rho X + Y\rho Y + Z\rho Z)$$

等价的 Kraus 表示：

$$\mathcal{E}_{\text{dep}}(\rho) = \sum_{i=0}^{3} K_i \rho K_i^\dagger$$

其中 Kraus 算子为：

$$K_0 = \sqrt{1 - p} \; I, \quad K_1 = \sqrt{\frac{p}{3}} \; X, \quad K_2 = \sqrt{\frac{p}{3}} \; Y, \quad K_3 = \sqrt{\frac{p}{3}} \; Z$$

完备性关系 $\sum_i K_i^\dagger K_i = I$ 自动满足。物理含义：以概率 $(1-p)$ 什么都不发生，以概率 $p/3$ 分别发生 $X$、$Y$、$Z$ 翻转。去极化信道是 QEC 理论中最常用的噪声模型。

**Source**: **[Nielsen & Chuang, Eq. 8.101, p.378; Section 8.3.4, p.378]** | Preskill Lecture Notes

---

### F4.15: Logical Error Rate under Repetition / Code Distance Scaling

对于码距为 $d$ 的量子纠错码，在独立去极化噪声模型下，逻辑错误率的 leading order 行为：

$$p_L \approx A \binom{d}{\lfloor d/2 \rfloor + 1} p^{\lfloor d/2 \rfloor + 1} (1-p)^{d - \lfloor d/2 \rfloor - 1}$$

当 $p \ll 1$ 时简化为：

$$p_L \approx A \binom{d}{\lfloor d/2 \rfloor + 1} p^{\lfloor d/2 \rfloor + 1}$$

对于重复码（repetition code），纠正 $t = \lfloor(d-1)/2\rfloor$ 个比特翻转错误：

$$p_L = \sum_{j=t+1}^{d} \binom{d}{j} p^j (1-p)^{d-j}$$

这是二项分布的尾概率。当 $p < 1/2$ 时，$p_L$ 随 $d$ 指数衰减，体现了纠错的指数级优势。

**Source**: [derivations/threshold_theorem.md] | Fowler et al. (2012); Dennis et al. (2002)

---

## Bounds from Gottesman Thesis

### F4.16: Quantum Hamming Bound (Asymptotic) [Gottesman thesis, §7.1]

$$\frac{k}{n} \leq 1 - p\log_2 3 - H(p)$$

where $H(x) = -x\log_2 x - (1-x)\log_2(1-x)$ is the binary entropy and $p = t/n$ is the error fraction. This applies to nondegenerate codes on the depolarizing channel.

**Source**: [Gottesman thesis, §7.1, Eq. 7.2] | Ekert & Macchiavello (1996)

---

### F4.17: Quantum Gilbert-Varshamov Bound [Gottesman thesis, §7.1]

$$\sum_{j=0}^{d-1} 3^j \binom{n}{j} 2^k \geq 2^n$$

Asymptotically: $k/n \geq 1 - 2p\log_2 3 - H(2p)$ where $d = 2t+1$ and $p = t/n$.

This is a lower bound: codes with these parameters are guaranteed to exist.

**Source**: [Gottesman thesis, §7.1, Eq. 7.5] | Calderbank et al. (1997)

---

### F4.18: Knill-Laflamme / Quantum Singleton Bound [Gottesman thesis, §7.1]

$$n \geq 2(d-1) + k$$

This is the quantum analog of the classical Singleton bound. It holds for both degenerate and nondegenerate codes. A code correcting $t$ errors must satisfy $n \geq 4t + k$.

**Source**: [Gottesman thesis, §7.1] | Knill & Laflamme (1997)

---

### F4.19: Quantum MacWilliams Identity [Gottesman thesis, §7.2]

$$B(z) = \frac{1}{2^{n-k}} (1 + 3z)^n A\left(\frac{1-z}{1+3z}\right)$$

where $A(z) = \sum_{d=0}^n A_d z^d$ and $B(z) = \sum_{d=0}^n B_d z^d$ are the weight enumerators of the stabilizer $S$ and normalizer $N(S)$ respectively. $A_d$ is the number of elements of $S$ with weight $d$, $B_d$ is the number of elements of $N(S)$ with weight $d$. For a code of distance $d$: $B_{d'} = A_{d'}$ for all $d' < d$.

**Source**: [Gottesman thesis, §7.2, Eq. 7.8] | Shor & Laflamme (1997)

---

### F4.20: Concatenated Code Threshold Recursion [Gottesman thesis, §6.2]

For the $[7,1,3]$ code with cat-state error correction:

$$p_g^{(j)} = 21\left[(p_g^{(j-1)})^2 + 4\,p_g^{(j-1)}\,p_{EC} + 8\,p_{EC}^2\right]$$

Leading to the threshold scaling: $p_g^{(l)} \sim p_g^{(0)}(p_g^{(0)}/p_{thresh})^{2^l}$.

- No storage errors: $p_{thresh} \approx 4.0 \times 10^{-5}$
- Equal gate/storage errors: $p_{thresh} \approx 2.2 \times 10^{-6}$
- Optimized error correction frequency: $p_{thresh} \approx 4.1 \times 10^{-4}$

**Source**: [Gottesman thesis, §6.2, Eq. 6.1-6.2] | Gottesman (1997)

---

## 快速参考表

| 公式编号 | 名称 | 核心表达式 | 应用场景 |
|---------|------|-----------|---------|
| F4.1 | Knill-Laflamme | $PE_a^\dagger E_b P = C_{ab}P$ | 判断码能否纠正给定错误集 |
| F4.2 | Stabilizer state | $g_i\|\psi\rangle = \|\psi\rangle$ | 定义码空间 |
| F4.3 | Syndrome | $s_i \in \{0,1\}$ | 错误检测 |
| F4.4 | CSS construction | $C_2 \subseteq C_1 \Rightarrow [[n, k_1-k_2]]$ | 从经典码构造量子码 |
| F4.5 | Surface code | $[[2d^2-2d+1, 1, d]]$ | 拓扑码参数 |
| F4.6 | Threshold | $p_L \sim (p/p_{\text{th}})^{d/2}$ | 容错计算 |
| F4.7 | Toric Hamiltonian | $H = -\sum A_s - \sum B_p$ | 拓扑序 |
| F4.8 | MWPM | $\min$ wt matching | 解码 |
| F4.9 | Logical operators | $\bar{X}, \bar{Z}$ string ops | 逻辑门操作 |
| F4.10 | Code rate | $R = k/n$ | 编码效率 |
| F4.11 | Singleton bound | $d \leq (n-k)/2 + 1$ | 码极限 |
| F4.12 | Hamming bound | $\sum \binom{n}{j}3^j \leq 2^{n-k}$ | 非退化码极限 |
| F4.13 | Steane code | $[[7,1,3]]$ | 最小CSS码 |
| F4.14 | Depolarizing channel | $(1-p)\rho + \frac{p}{3}\sum P\rho P$ | 噪声建模 |
| F4.15 | Logical error rate | $p_L \sim p^{\lfloor d/2\rfloor+1}$ | 性能评估 |
| F4.16 | Q. Hamming bound (asymp.) | $k/n \leq 1 - p\log_2 3 - H(p)$ | 非退化码极限 |
| F4.17 | Q. Gilbert-Varshamov | $k/n \geq 1 - 2p\log_2 3 - H(2p)$ | 码存在性下界 |
| F4.18 | Q. Singleton bound | $n \geq 2(d-1) + k$ | 通用码极限 |
| F4.19 | Q. MacWilliams identity | $B(z) = 2^{-(n-k)}(1+3z)^n A(\cdot)$ | 权重枚举器关系 |
| F4.20 | Concat. threshold | $p_g^{(j)} = 21[(p_g^{(j-1)})^2 + \cdots]$ | 级联码阈值递推 |
