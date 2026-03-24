# QAOA理论推导

> Quantum Approximate Optimization Algorithm: Complete Theory
> 涵盖问题编码、哈密顿量构造、电路设计、p=1解析解、性能保证与量子退火的联系。

---

## 1. 问题设置：组合优化的Ising/QUBO编码 (Problem Setup)

### 1.1 QUBO形式

二次无约束二元优化（Quadratic Unconstrained Binary Optimization）：

$$\min_{\mathbf{x} \in \{0,1\}^n} \mathbf{x}^T Q \mathbf{x} + \mathbf{c}^T \mathbf{x}$$

> 大量经典组合优化问题（MaxCut、Max-SAT、图着色等）可自然映射为QUBO形式。

### 1.2 Ising形式

通过变量替换 $x_i = \frac{1-z_i}{2}$（$z_i \in \{+1, -1\}$），QUBO等价于Ising模型：

$$\min_{\mathbf{z} \in \{-1,+1\}^n} \sum_{i<j} J_{ij} z_i z_j + \sum_i h_i z_i$$

量子化：$z_i \to Z_i$（Pauli-Z算符），得到对角哈密顿量：

$$H_C = \sum_{i<j} J_{ij} Z_i Z_j + \sum_i h_i Z_i$$

$H_C$ 在计算基 $|z_1 z_2 \cdots z_n\rangle$ 上是对角的，本征值即为目标函数值。

---

## 2. 代价哈密顿量的构造 (Cost Hamiltonian Construction)

### 2.1 一般规则

给定目标函数 $C(\mathbf{z}) = \sum_\alpha C_\alpha(\mathbf{z})$，其中每个子句 $C_\alpha$ 仅涉及少量变量：

$$H_C = \sum_\alpha \hat{C}_\alpha$$

> 代价哈密顿量将经典目标函数的每一项提升为对角量子算符。

其中 $\hat{C}_\alpha$ 是将 $C_\alpha$ 中 $z_i \to Z_i$ 后得到的算符。

### 2.2 MaxCut实例

**问题**: 给定图 $G = (V, E)$，找到顶点二分 $(S, \bar{S})$ 使割边数最大。

目标函数（对每条边 $(i,j) \in E$，当 $z_i \neq z_j$ 时贡献1）：

$$C(\mathbf{z}) = \sum_{(i,j) \in E} \frac{1 - z_i z_j}{2}$$

量子化：

$$H_C = \sum_{(i,j) \in E} \frac{1}{2}(I - Z_i Z_j)$$

> MaxCut代价哈密顿量的本征值等于对应比特串的割边数。

验证：对计算基态 $|z_1\cdots z_n\rangle$：

$$H_C |z_1\cdots z_n\rangle = \sum_{(i,j)\in E} \frac{1-z_iz_j}{2} |z_1\cdots z_n\rangle = C(\mathbf{z}) |z_1\cdots z_n\rangle \quad \checkmark$$

### 2.3 Max-SAT实例

对 $k$-SAT子句 $C_\alpha = (x_{i_1} \vee \bar{x}_{i_2} \vee x_{i_3})$，使用 $x_i = \frac{1-Z_i}{2}$：

$$\hat{C}_\alpha = 1 - \frac{(I + Z_{i_1})(I - Z_{i_2})(I + Z_{i_3})}{2^k}$$

当且仅当赋值不满足子句时 $\hat{C}_\alpha = 0$。

---

## 3. 混合哈密顿量与Trotter化动机 (Mixing Hamiltonian and Trotterization)

### 3.1 绝热量子计算的启示

绝热定理：系统从 $H_M$ 的基态 $|+\rangle^{\otimes n}$ 缓慢演化到 $H_C$ 的基态：

$$H(t) = \left(1 - \frac{t}{T}\right) H_M + \frac{t}{T} H_C, \quad t \in [0, T]$$

> QAOA可视为绝热演化的Trotter化近似，有限层数对应有限时间分辨率。

若 $T$ 足够大（满足绝热条件），最终态逼近 $H_C$ 的基态。

### 3.2 Trotter化

时间演化算符 $U = \mathcal{T}\exp(-i\int_0^T H(t)dt)$ 的 $P$ 步Trotter近似：

$$U \approx \prod_{p=1}^{P} e^{-i\Delta t_p H_M} e^{-i\Delta t_p H_C}$$

令 $\beta_p = \Delta t_p (1 - t_p/T)$，$\gamma_p = \Delta t_p \cdot t_p/T$，得到QAOA形式。但QAOA中 $\{\gamma_p, \beta_p\}$ 是**自由变分参数**，不受Trotter分解约束。

### 3.3 标准混合哈密顿量

$$H_M = \sum_{i=1}^{n} X_i$$

其基态为 $|+\rangle^{\otimes n} = \frac{1}{\sqrt{2^n}}\sum_{\mathbf{z}} |\mathbf{z}\rangle$——所有计算基态的均匀叠加。

演化算符分解为单比特旋转：

$$e^{-i\beta H_M} = \prod_{i=1}^{n} e^{-i\beta X_i} = \prod_{i=1}^{n} R_X(2\beta)$$

---

## 4. QAOA电路构造 (QAOA Circuit Construction)

### 4.1 初始态

$$|\psi_0\rangle = |+\rangle^{\otimes n} = H^{\otimes n} |0\rangle^{\otimes n}$$

> QAOA从均匀叠加态出发，这是混合哈密顿量的基态。

### 4.2 参数化演化

第 $p$ 层（$p = 1, \dots, P$）包含：

**相位分离算符** (Phase Separation):

$$U_C(\gamma_p) = e^{-i\gamma_p H_C} = \prod_{(i,j)\in E} e^{-i\gamma_p (I - Z_iZ_j)/2}$$

对MaxCut，每条边对应一个 $R_{ZZ}$ 门：

$$e^{-i\gamma_p Z_iZ_j/2} = \text{CNOT}_{ij} \cdot R_Z(\gamma_p)_j \cdot \text{CNOT}_{ij}$$

（忽略全局相位）

**混合算符** (Mixing):

$$U_M(\beta_p) = e^{-i\beta_p H_M} = \prod_{i=1}^{n} R_X(2\beta_p)$$

### 4.3 完整电路

$$|\boldsymbol{\gamma}, \boldsymbol{\beta}\rangle = U_M(\beta_P) U_C(\gamma_P) \cdots U_M(\beta_1) U_C(\gamma_1) |+\rangle^{\otimes n}$$

电路深度为 $O(P \cdot |E|)$（MaxCut），参数数目为 $2P$。

---

## 5. p=1 QAOA for MaxCut: 解析解 (Analytical Solution)

### 5.1 期望值计算

对 $P=1$，目标：

$$F_1(\gamma, \beta) = \langle +^n | U_C^\dagger(\gamma) U_M^\dagger(\beta) \, H_C \, U_M(\beta) U_C(\gamma) | +^n \rangle$$

> Farhi等人(2014)给出了 $p=1$ MaxCut的完全解析表达式，仅依赖图的局部结构。

由于 $H_C = \sum_{(i,j)\in E} \frac{1}{2}(I - Z_iZ_j)$，可逐边计算：

$$F_1(\gamma, \beta) = \sum_{(i,j)\in E} f_{ij}(\gamma, \beta)$$

### 5.2 单边贡献

对边 $(i,j)$，设 $d_i, d_j$ 为顶点度数（不含边 $(i,j)$ 本身），$f_{ij}$ 的解析表达式为：

$$f_{ij}(\gamma, \beta) = \frac{1}{2} + \frac{1}{4}\sin(4\beta)\sin(\gamma)\left[\cos^{d_i-1}(\gamma) + \cos^{d_j-1}(\gamma)\right] - \frac{1}{4}\sin^2(2\beta)\sin^2(\gamma)\cos^{d_i+d_j-2}(\gamma)$$

（此处 $d_i, d_j$ 包含边 $(i,j)$ 自身，具体指数视文献约定可能有 $\pm 1$ 的差异。）

### 5.3 对 $d$-正则图的简化

对 $d$-正则图，所有边的贡献相同：

$$F_1(\gamma, \beta) = \frac{|E|}{2} + \frac{|E|}{2}\sin(4\beta)\sin(\gamma)\cos^{d-2}(\gamma) - \frac{|E|}{4}\sin^2(2\beta)\sin^2(\gamma)\cos^{2(d-2)}(\gamma)$$

---

## 6. 性能保证 (Performance Guarantees)

### 6.1 Farhi et al. 2014 主要结果

**定理**: 对任意图 $G$，QAOA在 $P=1$ 时的MaxCut近似比满足：

$$r = \frac{F_1(\gamma^*, \beta^*)}{C_{\max}} \geq \frac{1}{2} + \frac{1}{4\sqrt{d-1}} \quad \text{(对 $d$-正则图)}$$

> 即使仅一层QAOA，MaxCut也能保证超越随机猜测的性能。

对3-正则图：$r \geq 0.6924$。

**对比**: 经典Goemans-Williamson SDP松弛算法达到 $r \geq 0.878$。

### 6.2 证明思路

1. 对3-正则图，代入 $d=3$ 到 $F_1$ 的解析式
2. 优化 $(\gamma^*, \beta^*)$：取 $\gamma^* \approx 0.6155$，$\beta^* \approx 0.3927$
3. 由Farhi等人的图论分析，对任意3-正则图的最大割 $C_{\max} \leq \frac{3n}{2}$（边数 $|E| = \frac{3n}{2}$），计算比值下界

### 6.3 层数增加的改进

- $P \to \infty$: QAOA可精确求解（等价于完整绝热演化）
- 对有界度图，$P = O(\text{poly}(n))$ 足以达到近似最优
- 数值证据表明 $P$ 的增加带来稳定改进，但具体收敛速率依赖于图结构

---

## 7. 集中现象与参数迁移 (Concentration and Parameter Transfer)

### 7.1 参数集中

**定理** (Brandao et al., 2018): 对 $d$-正则图，当 $P$ 固定时，QAOA的最优参数 $(\boldsymbol{\gamma}^*, \boldsymbol{\beta}^*)$ 对不同图实例**集中**——最优参数几乎不依赖于具体图。

> 参数集中现象使得可以在小规模图上优化参数，然后迁移到大规模实例。

更精确地，对两个 $d$-正则图 $G_1, G_2$，以高概率：

$$\left|\frac{F_P^{G_1}(\boldsymbol{\gamma}^*, \boldsymbol{\beta}^*)}{|E_1|} - \frac{F_P^{G_2}(\boldsymbol{\gamma}^*, \boldsymbol{\beta}^*)}{|E_2|}\right| \leq \epsilon$$

### 7.2 参数迁移策略

**训练迁移** (Transfer Learning):
1. 在小图 $G_{\text{small}}$ 上优化得到 $(\boldsymbol{\gamma}^*, \boldsymbol{\beta}^*)$
2. 将参数直接用于大图 $G_{\text{large}}$
3. 可选：在大图上进一步微调

**层间迁移** (Layer Interpolation):
从 $P$ 层参数 $\{(\gamma_p, \beta_p)\}_{p=1}^P$ 生成 $P+1$ 层初始参数，通过线性插值：

$$\gamma_p^{(P+1)} = \frac{p}{P+1}\gamma_P^{(P)} + \frac{P+1-p}{P+1}\gamma_1^{(P)}$$

（类似地对 $\beta$）

---

## 8. QAOA与量子退火的联系 (QAOA vs Quantum Annealing)

### 8.1 Trotter化绝热演化

量子退火的含时哈密顿量：

$$H(s) = (1-s)H_M + s H_C, \quad s = t/T \in [0,1]$$

> QAOA是绝热量子计算的数字化（门型）版本，$P \to \infty$ 时两者等价。

一阶Trotter分解：

$$U(T) = \mathcal{T}\exp\left(-i\int_0^T H(t)dt\right) \approx \prod_{p=1}^{P} e^{-i\beta_p^{\text{ad}} H_M} e^{-i\gamma_p^{\text{ad}} H_C}$$

其中 $\beta_p^{\text{ad}} = (1 - p/P)\Delta t$，$\gamma_p^{\text{ad}} = (p/P)\Delta t$，$\Delta t = T/P$。

### 8.2 关键差异

| 特征 | QAOA | 量子退火 (QA) |
|------|------|--------------|
| 参数 | 自由变分参数 $(\boldsymbol{\gamma}, \boldsymbol{\beta})$ | 退火路径 $s(t)$ 固定或启发式 |
| 硬件 | 门型量子计算机 | 专用退火机（如D-Wave） |
| 理论保证 | 已知近似比下界 | 依赖绝热定理（间隙假设） |
| 灵活性 | 可超越绝热路径 | 受限于连续演化 |
| 纠错兼容 | 是（数字化电路） | 困难 |

### 8.3 超越绝热的优势

QAOA的变分参数空间包含但不限于绝热路径的Trotter化。优化后的QAOA参数可以：
- "走捷径"穿越能级反交叉区域
- 在量子相变点附近采取非单调路径
- 利用量子干涉效应抵消不良振幅

Wurtz & Love (2021) 的数值研究表明，优化后的QAOA参数轨迹通常**偏离**线性退火路径，特别是在相变点附近出现非平凡的参数结构。

---

## 9. Farhi原始论文的严格构造 (Rigorous Construction from Farhi et al. 2014)

> 以下内容直接基于 **[Farhi et al. 2014, §1-§5]** 的原始数学表述。

### 9.1 一般组合优化设定

组合优化问题由 $n$ 比特和 $m$ 子句指定。目标函数：

$$C(z) = \sum_{\alpha=1}^{m} C_\alpha(z)$$

其中 $z = z_1 z_2 \cdots z_n$ 是比特串，$C_\alpha(z) \in \{0, 1\}$ 表示赋值 $z$ 是否满足子句 $\alpha$。**[Farhi et al. 2014, Eq.(1)]**

### 9.2 算子定义

**代价酉算符**：

$$U(C, \gamma) = e^{-i\gamma C} = \prod_{\alpha=1}^{m} e^{-i\gamma C_\alpha}$$

所有因子对易（因为它们在计算基上对角）。由于 $C$ 有整数本征值，$\gamma \in [0, 2\pi]$。**[Farhi et al. 2014, Eq.(3)]**

**混合算符** $B = \sum_{j=1}^n \sigma_j^x$，其对应的酉算符：

$$U(B, \beta) = e^{-i\beta B} = \prod_{j=1}^n e^{-i\beta \sigma_j^x}, \quad \beta \in [0, \pi]$$

**[Farhi et al. 2014, Eq.(4)-(5)]**

**QAOA态**：

$$|\boldsymbol{\gamma}, \boldsymbol{\beta}\rangle = U(B, \beta_p) U(C, \gamma_p) \cdots U(B, \beta_1) U(C, \gamma_1) |s\rangle$$

其中 $|s\rangle = \frac{1}{\sqrt{2^n}} \sum_z |z\rangle$ 是均匀叠加态。**[Farhi et al. 2014, Eq.(7)]**

**期望值与最大化**：

$$F_p(\boldsymbol{\gamma}, \boldsymbol{\beta}) = \langle \boldsymbol{\gamma}, \boldsymbol{\beta} | C | \boldsymbol{\gamma}, \boldsymbol{\beta} \rangle, \quad M_p = \max_{\boldsymbol{\gamma}, \boldsymbol{\beta}} F_p(\boldsymbol{\gamma}, \boldsymbol{\beta})$$

**[Farhi et al. 2014, Eq.(8)-(9)]**

### 9.3 单调性与极限定理

**定理 (单调性)** **[Farhi et al. 2014, Eq.(10)]**：

$$M_p \geq M_{p-1}$$

*证明*：$p-1$ 的最大化可视为 $p$ 处令 $\gamma_p = \beta_p = 0$ 的约束最大化。$\square$

**定理 (极限收敛)** **[Farhi et al. 2014, Eq.(11)]**：

$$\lim_{p \to \infty} M_p = \max_z C(z)$$

*证明思路*：通过绝热演化的Trotter化。考虑含时哈密顿量 $H(t) = (1 - t/T)B + (t/T)C$。态 $|s\rangle$ 是 $B$ 的最高能量本征态。由Perron-Frobenius定理，最高能量态与次高能量态之间的间隙对所有 $t < T$ 严格为正。绝热定理保证当 $T$ 足够大时，系统将追踪到 $C$ 的最高能量本征态。Trotter化这一绝热演化给出交替的 $U(C,\gamma)$ 和 $U(B,\beta)$ 算符，每个角度需小以确保好的近似，总运行时间需长以确保成功，这要求 $p$ 足够大。**[Farhi et al. 2014, §5]** $\square$

---

## 10. 固定 $p$ 的经典预处理 (Fixed-$p$ Classical Preprocessing)

> **[Farhi et al. 2014, §2]**

### 10.1 局部性定理

**定理 (子图局部性)** **[Farhi et al. 2014, §2]**：对于MaxCut问题，考虑与边 $\langle jk \rangle$ 相关的算符

$$U^\dagger(C, \gamma_1) \cdots U^\dagger(B, \beta_p) \, C_{\langle jk \rangle} \, U(B, \beta_p) \cdots U(C, \gamma_1)$$

此算符仅涉及图上距边 $\langle jk \rangle$ 不超过 $p$ 步的量子比特。

*证明思路*：对 $p=1$，$U(B, \beta_1)$ 中不涉及量子比特 $j$ 或 $k$ 的因子与 $C_{\langle jk \rangle}$ 对易并消去。$U(C, \gamma_1)$ 中不涉及量子比特 $j, k$ 或其邻居的因子同样对易并消去。对一般 $p$，此论证递归应用。**[Farhi et al. 2014, Eq.(14)-(16)]** $\square$

### 10.2 子图分解定理

**定理** **[Farhi et al. 2014, Eq.(25)]**：期望值 $F_p$ 可分解为子图类型的加权和：

$$F_p(\boldsymbol{\gamma}, \boldsymbol{\beta}) = \sum_g w_g f_g(\boldsymbol{\gamma}, \boldsymbol{\beta})$$

其中 $w_g$ 是子图类型 $g$ 在原图中的出现次数，$f_g$ 是对应的子图贡献函数，**不依赖于** $n$ 和 $m$。

**推论 (经典高效求值)** **[Farhi et al. 2014, §2]**：对有界度 $v$ 的图，子图类型数有限，每个子图涉及的量子比特数至多为

$$q_{\text{tree}} = 2 \left[\frac{(v-1)^{p+1} - 1}{(v-1) - 1}\right]$$

**[Farhi et al. 2014, Eq.(26)]**。因此 $F_p$ 可在**不随 $n$ 增长**的经典计算资源上精确求值。

---

## 11. 集中现象的严格界 (Concentration Bound)

> **[Farhi et al. 2014, §3]**

**定理 (方差界)** **[Farhi et al. 2014, Eq.(31)]**：对度为 $v$ 的正则图，QAOA态下 $C$ 的方差满足：

$$\langle \boldsymbol{\gamma}, \boldsymbol{\beta} | C^2 | \boldsymbol{\gamma}, \boldsymbol{\beta} \rangle - \langle \boldsymbol{\gamma}, \boldsymbol{\beta} | C | \boldsymbol{\gamma}, \boldsymbol{\beta} \rangle^2 \leq 2 \left[\frac{(v-1)^{2p+2} - 1}{(v-1) - 1}\right] \cdot m$$

*证明*：将 $\text{Var}[C]$ 展开为边对 $\langle jk \rangle, \langle j'k' \rangle$ 的双求和。当两条边的 $p$-邻域不共享量子比特时（即图距离 $> 2p+1$），对应的协方差为零。每条边至多有 $2[(v-1)^{2p+2} - 1]/[(v-1) - 1]$ 条边与其邻域重叠，且每个被求和项的范数至多为1。**[Farhi et al. 2014, Eq.(27)-(31)]** $\square$

**推论**：对固定 $v$ 和 $p$，$C(z)$ 的标准差至多为 $O(\sqrt{m})$，即测量结果集中在均值 $F_p$ 附近。通过 $O(m^2)$ 次重复测量，可以概率 $1 - 1/m$ 将样本均值控制在 $F_p \pm 1$ 以内。

---

## 12. 环形分歧图的精确结果 (Ring of Disagrees)

> **[Farhi et al. 2014, §4]**

**定理** **[Farhi et al. 2014, §4]**：对2-正则图（环），QAOA在层数 $p$ 时的最大期望值为：

$$M_p = n \cdot \frac{2p+1}{2p+2}$$

*数值验证*：$p=1$ 时 $M_1 = 3n/4$，$p=2$ 时 $M_2 = 5n/6$，$p=3$ 时 $M_3 = 7n/8$，...

由于最佳割为 $n$（偶数 $n$），近似比为 $(2p+1)/(2p+2)$，通过增大 $p$ 可任意接近1，且电路深度仅为 $3p$（与 $n$ 无关）。

---

## 13. 3-正则图 $p=1$ 的完整分析 (Complete $p=1$ Analysis on 3-Regular Graphs)

> **[Farhi et al. 2014, §5]**

### 13.1 子图分类

对3-正则图，$p=1$ 时只有三种子图类型：$g_4$（4顶点）、$g_5$（5顶点）、$g_6$（6顶点）。设图中有 $S$ 个交叉方形（crossed squares）和 $T$ 个孤立三角形（isolated triangles），则：

$$F_1(\gamma, \beta) = S \, f_{g_4}(\gamma, \beta) + (4S + 3T) f_{g_5}(\gamma, \beta) + \left(\frac{3n}{2} - 5S - 3T\right) f_{g_6}(\gamma, \beta)$$

**[Farhi et al. 2014, Eq.(34)]**

### 13.2 近似比下界

**定理** **[Farhi et al. 2014, §5]**：对任意3-正则图，QAOA在 $p=1$ 时的近似比至少为

$$\frac{M_1(1, s, t)}{3/2 - s - t} \geq 0.6924$$

其中 $s = S/n$，$t = T/n$，最小值在 $s = t = 0$（无三角形和交叉方形的图）处取到。

### 13.3 $p=2$ 的部分结果

对 $p=2$，最大子图类型是14顶点的树。对没有五边形、四边形、三角形的3-正则图，数值优化得到单边贡献为 $0.7559$。**[Farhi et al. 2014, §5]**

---

## 14. 独立集的QAOA变体 (QAOA Variant for Maximum Independent Set)

> **[Farhi et al. 2014, §6]**

### 14.1 受限Hilbert空间

对独立集问题，Hilbert空间的正交基 $|z\rangle$ 仅包含对应独立集的比特串（而非全部 $2^n$ 个）。目标函数为汉明重量 $C(z) = \sum_j z_j$。

### 14.2 修改的混合算符

$$\langle z | B | z' \rangle = \begin{cases} 1 & z \text{ 和 } z' \text{ 仅在一个比特上不同} \\ 0 & \text{其他} \end{cases}$$

即 $B$ 是受限于合法字符串（独立集）的超立方体邻接矩阵。**[Farhi et al. 2014, Eq.(37)]**

### 14.3 演化与收敛

初始态为空独立集 $|z = 0\rangle$（$C$ 的最小值态），QAOA态为：

$$|\mathbf{b}, \boldsymbol{\gamma}\rangle = U(B, b_p) U(C, \gamma_{p-1}) \cdots U(B, b_1) |z = 0\rangle$$

**[Farhi et al. 2014, Eq.(42)]**。收敛性 $\lim_{p \to \infty} M_p = \max_{z \text{ legal}} C(z)$ 通过两段绝热路径证明：先从 $-C$ 的基态绝热演化到 $B$ 的顶态，再从 $B$ 的顶态绝热到 $+C$ 的顶态。**[Farhi et al. 2014, Eq.(50)]**

---

## 15. Cerezo等人综述中关于QAOA的理论补充 (QAOA Theory from Cerezo et al. 2021)

> 以下内容来自 **[Cerezo et al. 2021, §5.3]** VQA综述。

### 15.1 QAOA的理论性质总结

**[Cerezo et al. 2021, §5.3 (Optimization)]** 给出以下关键结论：

1. **可证明的性能保证**：$p=1$ QAOA对MaxCut有可证明的性能保证 **[Farhi et al. 2014]**。
2. **经典不可模拟性**：即使 $p=1$ 的QAOA拟设也无法被经典设备高效模拟 (Farhi & Harrow, 2016)。
3. **单调改进**：增大 $p$ 只能改善QAOA性能（$M_p \geq M_{p-1}$）。
4. **最优bang-bang控制**：QAOA的交替施加结构在固定量子计算时间下是最优的 (Yang et al., 2017)。
5. **浅层QAOA的局限**：存在某些问题使得浅层QAOA不能很好近似 (Hastings 2019, Bravyi et al. 2019)，暗示 $p$ 可能需要随问题规模增长。

### 15.2 QAOA与贫瘠高原

**[Cerezo et al. 2021, §4.1]** 指出，QAOA型拟设由于仅有 $2P$ 个参数（远少于HEA的 $O(nL)$），天然**不易陷入贫瘠高原**。然而，在NISQ设备上，噪声可以诱导QAOA代价景观的集中现象，使有效训练受限。

---

## 16. 高级主题：Quantum Alternating Operator Ansatz

> **[Cerezo et al. 2021, §2.2]**

QAOA的推广——量子交替算符拟设（Quantum Alternating Operator Ansatz, QAOAnsatz, Hadfield et al. 2019）——允许问题特定的混合算符 $U_M$ 来保持约束可行性。例如，对带约束的优化问题（如TSP），可以设计保持排列对称性的混合算符，使QAOA搜索限制在可行解空间内。
