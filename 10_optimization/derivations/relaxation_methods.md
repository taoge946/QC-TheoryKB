# Relaxation Methods for Combinatorial Optimization

> 组合优化的松弛方法：LP 松弛、SDP 松弛（含 Goemans-Williamson 0.878 近似比推导）、拉格朗日松弛。
>
> **References**: **[Boyd & Vandenberghe, Ch.5, §5.7 (Lagrangian relaxation)]**; **[Boyd & Vandenberghe, Ch.11, §11.6 (SDP)]**; **[Cappart et al. 2023, §3]** (GNN+CO relaxation)

---

## 1. LP Relaxation

### 1.1 Formulation

将整数规划

$$\text{ILP:} \quad z^* = \min \; \mathbf{c}^\top \mathbf{x}, \quad \text{s.t.} \; A\mathbf{x} \leq \mathbf{b}, \; \mathbf{x} \in \{0,1\}^n$$

松弛为线性规划：

$$\text{LP:} \quad z_{\text{LP}} = \min \; \mathbf{c}^\top \mathbf{x}, \quad \text{s.t.} \; A\mathbf{x} \leq \mathbf{b}, \; 0 \leq x_i \leq 1$$

LP 松弛扩大了可行域（$\{0,1\}^n \subset [0,1]^n$），因此对最小化问题有

$$z_{\text{LP}} \leq z^*$$

LP 松弛的最优值是原问题最优值的一个下界。

### 1.2 Integrality Gap

**Definition.** 整数性间隙（integrality gap）是 LP 松弛在所有实例上的最坏松弛质量：

$$\text{IG} = \sup_{I} \frac{z^*(I)}{z_{\text{LP}}(I)} \quad (\text{最小化问题, } z_{\text{LP}} > 0)$$

对于最大化问题取 $\inf$。整数性间隙限制了任何基于 LP 松弛的舍入算法能达到的最佳近似比。

### 1.3 LP-based Rounding for MVC

**Theorem.** LP 松弛 + 阈值舍入给出 MVC 的 2-近似算法。

MVC 的 LP 松弛：

$$\min \sum_i x_i, \quad \text{s.t.} \; x_i + x_j \geq 1 \; \forall (i,j) \in E, \quad 0 \leq x_i \leq 1$$

**舍入规则**：令 $\mathbf{x}^*$ 为 LP 最优解，取 $S = \{i : x_i^* \geq 1/2\}$。

**Proof of 2-approximation.**

1. **可行性**：对任意边 $(i,j) \in E$，有 $x_i^* + x_j^* \geq 1$，因此 $x_i^*$ 和 $x_j^*$ 中至少一个 $\geq 1/2$，即 $S$ 覆盖所有边。

2. **近似比**：
$$|S| = |\{i : x_i^* \geq 1/2\}| \leq \sum_{i: x_i^* \geq 1/2} 2x_i^* \leq 2 \sum_i x_i^* = 2 \cdot z_{\text{LP}} \leq 2 \cdot z^*$$

因此 $|S| \leq 2 \cdot \text{OPT}_{\text{MVC}}$。$\square$

**Remark.** MVC 的 LP 松弛整数性间隙恰好为 2（考虑完全二部图 $K_{n,n}$），因此 LP 舍入无法给出优于 2 的近似比。在 Unique Games Conjecture 下，2-近似是最优的。

**Source**: Hochbaum (1982) | Vazirani (2001), Ch. 1

---

## 2. SDP Relaxation: Goemans-Williamson for MaxCut

### 2.1 MaxCut as Quadratic Program

MaxCut 可写为：

$$\text{MC:} \quad \max \frac{1}{2} \sum_{(i,j) \in E} w_{ij}(1 - y_i y_j), \quad y_i \in \{-1, +1\}$$

令 $Y_{ij} = y_i y_j$，则 $Y$ 是 $n \times n$ 矩阵且 $Y = \mathbf{y}\mathbf{y}^\top$，满足 $Y_{ii} = 1$，$Y \succeq 0$，$\text{rank}(Y) = 1$。

### 2.2 SDP Relaxation

去掉秩-1 约束，得到 SDP 松弛：

$$\text{SDP:} \quad \max \frac{1}{2} \sum_{(i,j) \in E} w_{ij} \frac{1 - X_{ij}}{2}, \quad \text{s.t.} \; X_{ii} = 1, \; X \succeq 0$$

等价地，令 $X = V^\top V$ 其中 $V = [\mathbf{v}_1, \ldots, \mathbf{v}_n]$，$\mathbf{v}_i \in \mathbb{R}^n$ 且 $\|\mathbf{v}_i\| = 1$：

$$\max \frac{1}{2} \sum_{(i,j) \in E} w_{ij} \cdot \frac{1 - \mathbf{v}_i \cdot \mathbf{v}_j}{2}$$

注意 $\frac{1 - \mathbf{v}_i \cdot \mathbf{v}_j}{2} = \frac{\|\mathbf{v}_i - \mathbf{v}_j\|^2}{4}$，因此也可写为

$$\max \frac{1}{4} \sum_{(i,j) \in E} w_{ij} \|\mathbf{v}_i - \mathbf{v}_j\|^2, \quad \text{s.t.} \; \|\mathbf{v}_i\| = 1$$

SDP 松弛可在多项式时间内求解（椭球法或内点法），精度为 $\varepsilon$ 时复杂度为 $\tilde{O}(n^{3.5} \log(1/\varepsilon))$。

### 2.3 Hyperplane Rounding

**Algorithm (Goemans-Williamson Rounding):**
1. 求解 SDP 得到单位向量 $\{\mathbf{v}_1, \ldots, \mathbf{v}_n\} \subset \mathbb{R}^n$
2. 均匀随机选取单位向量 $\mathbf{r} \in S^{n-1}$
3. 划分 $S = \{i : \mathbf{v}_i \cdot \mathbf{r} \geq 0\}$，$\bar{S} = V \setminus S$

### 2.4 The 0.878 Approximation Ratio — Full Derivation

**Theorem (Goemans & Williamson, 1995).** 上述算法的近似比为 $\alpha_{\text{GW}} \approx 0.87856$。

**Step 1: Probability of an edge being cut.**

对于边 $(i,j)$，它被切割当且仅当 $\mathbf{v}_i$ 和 $\mathbf{v}_j$ 在随机超平面的两侧。设 $\theta_{ij} = \arccos(\mathbf{v}_i \cdot \mathbf{v}_j)$ 是两个单位向量的夹角，则

$$\Pr[(i,j) \text{ is cut}] = \frac{\theta_{ij}}{\pi}$$

这是因为均匀随机超平面分割两个向量的概率等于它们之间的"归一化角度"。直观理解：超平面法向量 $\mathbf{r}$ 均匀分布在 $S^{n-1}$ 上，$\mathbf{v}_i \cdot \mathbf{r}$ 和 $\mathbf{v}_j \cdot \mathbf{r}$ 异号当且仅当 $\mathbf{r}$ 落在 $\mathbf{v}_i$ 和 $\mathbf{v}_j$ 张成的二维平面中两个向量的"夹角区域"内。

**Step 2: Expected cut value.**

$$\mathbb{E}[\text{Cut}] = \sum_{(i,j) \in E} w_{ij} \cdot \frac{\theta_{ij}}{\pi}$$

**Step 3: Comparison with SDP optimum.**

SDP 对每条边 $(i,j)$ 的贡献为 $w_{ij} \cdot \frac{1 - \cos\theta_{ij}}{2}$。我们需要找到

$$\alpha_{\text{GW}} = \min_{\theta \in [0,\pi]} \frac{\theta/\pi}{(1-\cos\theta)/2}$$

即对所有 $\theta \in [0, \pi]$，

$$\frac{\theta/\pi}{(1-\cos\theta)/2} \geq \alpha_{\text{GW}}$$

**Step 4: Computing $\alpha_{\text{GW}}$.**

令 $g(\theta) = \frac{2\theta}{\pi(1 - \cos\theta)}$，求 $g$ 在 $(0, \pi]$ 上的最小值。

求导令 $g'(\theta) = 0$：

$$g'(\theta) = \frac{2}{\pi} \cdot \frac{(1 - \cos\theta) - \theta \sin\theta}{(1 - \cos\theta)^2} = 0$$

即 $1 - \cos\theta = \theta \sin\theta$。

数值求解此超越方程得 $\theta^* \approx 2.331$ 弧度（约 $133.6°$），代入得

$$\alpha_{\text{GW}} = g(\theta^*) = \frac{2 \times 2.331}{\pi \times (1 - \cos(2.331))} \approx 0.87856$$

**Step 5: Conclusion.**

对每条边 $(i,j)$，

$$\frac{\theta_{ij}}{\pi} \geq \alpha_{\text{GW}} \cdot \frac{1 - \cos\theta_{ij}}{2}$$

因此

$$\mathbb{E}[\text{Cut}] = \sum_{(i,j) \in E} w_{ij} \frac{\theta_{ij}}{\pi} \geq \alpha_{\text{GW}} \sum_{(i,j) \in E} w_{ij} \frac{1 - \cos\theta_{ij}}{2} = \alpha_{\text{GW}} \cdot z_{\text{SDP}} \geq \alpha_{\text{GW}} \cdot z^*$$

最后一个不等式因为 SDP 是 MaxCut 的松弛，$z_{\text{SDP}} \geq z^*$。

综上，$\mathbb{E}[\text{Cut}] \geq 0.87856 \cdot \text{OPT}_{\text{MaxCut}}$。$\square$

**Remark.** 在 Unique Games Conjecture (Khot 2002) 下，$\alpha_{\text{GW}}$ 是 MaxCut 最优近似比：不存在多项式时间算法能超过 $0.87856$。

**Source**: Goemans & Williamson, JACM 42 (1995) | Khot et al., FOCS (2007)

---

## 3. Lagrangian Relaxation

### 3.1 Formulation

考虑带约束的整数规划：

$$z^* = \min \; \mathbf{c}^\top \mathbf{x}, \quad \text{s.t.} \; A\mathbf{x} \leq \mathbf{b}, \; D\mathbf{x} \leq \mathbf{d}, \; \mathbf{x} \in \{0,1\}^n$$

假设约束 $A\mathbf{x} \leq \mathbf{b}$ 是"复杂约束"（使问题困难），而 $D\mathbf{x} \leq \mathbf{d}$ 加上整数约束后的子问题容易求解。将复杂约束松弛：

$$L(\boldsymbol{\lambda}) = \min_{\mathbf{x} \in \{0,1\}^n, \; D\mathbf{x} \leq \mathbf{d}} \left\{ \mathbf{c}^\top \mathbf{x} + \boldsymbol{\lambda}^\top (A\mathbf{x} - \mathbf{b}) \right\}, \quad \boldsymbol{\lambda} \geq \mathbf{0}$$

### 3.2 Weak Duality

**Theorem.** 对任意 $\boldsymbol{\lambda} \geq \mathbf{0}$，$L(\boldsymbol{\lambda}) \leq z^*$。

**Proof.** 设 $\mathbf{x}^*$ 是原问题最优解。则 $A\mathbf{x}^* \leq \mathbf{b}$，即 $A\mathbf{x}^* - \mathbf{b} \leq \mathbf{0}$。因 $\boldsymbol{\lambda} \geq \mathbf{0}$：

$$L(\boldsymbol{\lambda}) \leq \mathbf{c}^\top \mathbf{x}^* + \boldsymbol{\lambda}^\top (A\mathbf{x}^* - \mathbf{b}) \leq \mathbf{c}^\top \mathbf{x}^* = z^* \quad \square$$

### 3.3 Lagrangian Dual

最紧的下界由拉格朗日对偶问题给出：

$$z_{\text{LD}} = \max_{\boldsymbol{\lambda} \geq \mathbf{0}} L(\boldsymbol{\lambda})$$

$L(\boldsymbol{\lambda})$ 是 $\boldsymbol{\lambda}$ 的凹函数（取最小值函数的逐点下确界），但一般不可微（分段线性）。

### 3.4 Relationship with LP Relaxation

**Theorem.** 拉格朗日对偶下界不弱于 LP 松弛下界：

$$z_{\text{LP}} \leq z_{\text{LD}} \leq z^*$$

当约束矩阵 $D$ 满足完全单模性（total unimodularity）时等号成立。一般情况下，拉格朗日对偶严格优于 LP 松弛。

### 3.5 Subgradient Method

由于 $L(\boldsymbol{\lambda})$ 不可微，使用次梯度法求解对偶问题：

$$\boldsymbol{\lambda}^{(t+1)} = \max\left\{\mathbf{0}, \; \boldsymbol{\lambda}^{(t)} + \alpha_t \left(A\mathbf{x}^{(t)} - \mathbf{b}\right)\right\}$$

其中 $\mathbf{x}^{(t)} = \arg\min_{\mathbf{x} \in \mathcal{X}} \{\mathbf{c}^\top \mathbf{x} + (\boldsymbol{\lambda}^{(t)})^\top A\mathbf{x}\}$ 是给定 $\boldsymbol{\lambda}^{(t)}$ 时的拉格朗日子问题最优解，$\alpha_t > 0$ 是步长。

**常用步长规则（Polyak）**：

$$\alpha_t = \frac{z_{\text{UB}} - L(\boldsymbol{\lambda}^{(t)})}{\|A\mathbf{x}^{(t)} - \mathbf{b}\|^2}$$

其中 $z_{\text{UB}}$ 是原问题已知的上界（来自启发式解）。

**收敛性**：当 $\alpha_t \to 0$ 且 $\sum_t \alpha_t = \infty$ 时，$L(\boldsymbol{\lambda}^{(t)}) \to z_{\text{LD}}$。Polyak 步长在 $z_{\text{UB}} = z^*$ 时保证有限步收敛。

**Source**: Fisher, *Management Science* 27 (1981) | Held & Karp, *Math. Programming* 1 (1971)

---

## 4. Semidefinite Programming Basics for CO

### 4.1 SDP Standard Form

$$\min \; \langle C, X \rangle, \quad \text{s.t.} \; \langle A_i, X \rangle = b_i \; (i = 1, \ldots, m), \quad X \succeq 0$$

其中 $X \in \mathbb{S}^n$（$n \times n$ 对称矩阵），$\langle A, B \rangle = \text{tr}(A^\top B)$ 是矩阵内积，$X \succeq 0$ 表示 $X$ 半正定。

SDP 推广了 LP：令 $X = \text{diag}(\mathbf{x})$ 可回到 LP。SDP 可在多项式时间内求解到任意精度。

### 4.2 SDP Dual

$$\max \; \mathbf{b}^\top \mathbf{y}, \quad \text{s.t.} \; \sum_{i=1}^{m} y_i A_i + S = C, \quad S \succeq 0$$

强对偶性在 Slater 条件下成立：若存在严格可行的原始和对偶解，则原始和对偶最优值相等。

### 4.3 Why SDP is Powerful for CO

SDP 松弛比 LP 松弛更紧，因为它可以捕获变量间的二次关系。关键思想：

1. 对二次目标 $\mathbf{x}^\top Q \mathbf{x}$，通过"提升"$X = \mathbf{x}\mathbf{x}^\top$ 转化为线性目标 $\langle Q, X \rangle$
2. 约束 $X = \mathbf{x}\mathbf{x}^\top$（秩-1 + 非负性）松弛为 $X \succeq 0$
3. 松弛后变成 SDP，可高效求解
4. 舍入（如随机超平面）将 SDP 解转化为整数解

SDP 松弛已在以下问题上给出最佳已知近似比：MaxCut（0.878）、MAX-2SAT（0.940）、图着色、以及各类 CSP 问题。

### 4.4 Lovász Theta Function

图 $G$ 的 Lovász theta 函数 $\vartheta(G)$ 是一个 SDP 可计算的值，满足

$$\alpha(G) \leq \vartheta(\bar{G}) \leq \chi(G)$$

其中 $\alpha(G)$ 是独立数，$\chi(G)$ 是色数。$\vartheta$ 可以"夹逼"这两个 NP-hard 量，是 SDP 在图论中最优美的应用之一。

对完美图（perfect graph），$\alpha(G) = \vartheta(\bar{G}) = \chi(G)$ 三者相等。

**Source**: Lovász, *IEEE Trans. Info. Theory* 25 (1979) | Vandenberghe & Boyd, *SIAM Review* 38 (1996)

---

---

## 5. LP/SDP Formalism from Convex Optimization Theory **[Boyd & Vandenberghe, Ch.4-5]**

### 5.1 LP as Convex Optimization

LP 是凸优化的最简单形式。Boyd & Vandenberghe (2004) 将 LP 置于凸优化层级的底层：

$$\text{LP} \subset \text{QCQP} \subset \text{SOCP} \subset \text{SDP} \subset \text{Conic Programming}$$

**LP 对偶性**的完整形式 **[Boyd & Vandenberghe, Ch.5, §5.2]**：

Primal: $\min c^\top x$, s.t. $Ax \leq b$

Dual: $\max b^\top \lambda$, s.t. $A^\top \lambda = c$, $\lambda \leq 0$

LP 的强对偶性**无条件成立**（只要原问题可行）。这比一般凸优化更强——一般凸优化需要 Slater 条件。

**互补松弛**：$\lambda_i^*(a_i^\top x^* - b_i) = 0$，即每个约束要么紧（取等），要么对应乘子为零。

**LP 求解方法**：
- **单纯形法**：沿多面体的边从顶点移动到顶点，最坏 $O(2^n)$ 但实际极快
- **内点法** **[Boyd & Vandenberghe, Ch.11]**：$O(\sqrt{m} \log(m/\varepsilon))$ 次 Newton 步，每步 $O(n^2 m)$

### 5.2 SDP Standard Form and Duality **[Boyd & Vandenberghe, Ch.4, §4.6; Ch.5, §5.9]**

SDP primal:

$$\min \; \langle C, X \rangle, \quad \text{s.t.} \; \langle A_i, X \rangle = b_i \; (i = 1, \ldots, m), \quad X \succeq 0$$

SDP dual:

$$\max \; b^\top y, \quad \text{s.t.} \; \sum_{i=1}^{m} y_i A_i + S = C, \quad S \succeq 0$$

**KKT 条件 for SDP**：
- Primal feasibility: $\langle A_i, X \rangle = b_i$, $X \succeq 0$
- Dual feasibility: $C - \sum y_i A_i = S \succeq 0$
- Complementary slackness: $\text{tr}(SX) = 0$，即 $SX = 0$

由 $S, X \succeq 0$ 且 $SX = 0$，得 $\text{rank}(X) + \text{rank}(S) \leq n$。这个秩约束是 SDP 舍入方案的理论基础。

**Strong duality for SDP**：在 Slater 条件下（存在 $X \succ 0$ 满足约束，即严格可行），强对偶性成立。MaxCut 的 GW 松弛中 Slater 条件自动满足（取 $X = I$）。

### 5.3 SDP 在 CO 松弛中的优势 **[Boyd & Vandenberghe, Ch.4; Vandenberghe & Boyd, SIAM Review 1996]**

SDP 松弛比 LP 松弛更紧，核心机制：

1. **提升（Lifting）**：二次目标 $x^\top Q x$ 通过 $X = xx^\top$ 变为线性目标 $\langle Q, X \rangle$
2. **松弛**：非凸约束 $X = xx^\top$（秩-1 + 正性）松弛为 $X \succeq 0$（凸约束）
3. **求解**：松弛后是 SDP，内点法多项式时间求解
4. **舍入**：SDP 解通过随机方案（如超平面舍入）转回整数解

**定量比较**：

| 问题 | LP 松弛近似比 | SDP 松弛近似比 |
|------|-------------|---------------|
| MaxCut | 0.5 (随机) | 0.878 (GW) |
| MAX-2SAT | 0.75 (LP) | 0.940 (SDP) |
| MVC | 2 (LP rounding) | 2 (SDP 不改善) |

**SDP 求解工具**：
- CVXPY + MOSEK / SCS：Python 接口
- SDPA：C++ 高性能 SDP 求解器
- 内点法复杂度：$O(n^{3.5} \log(1/\varepsilon))$，限制可处理规模 $n \lesssim 10^3$

### 5.4 Lagrangian Relaxation vs LP Relaxation **[Boyd & Vandenberghe, Ch.5, §5.7]**

**Theorem (Boyd & Vandenberghe).** 对于 ILP 松弛：

$$z_{\text{LP}} \leq z_{\text{LD}} \leq z^*$$

Lagrangian 对偶界至少和 LP 松弛一样紧。当 LP 的可行域恰好是整数可行域凸包时，$z_{\text{LP}} = z_{\text{LD}} = z^*$（完全单模性情况）。

这为选择松弛方法提供了理论指导：Lagrangian 松弛更紧但更难求解（需要次梯度法），LP 松弛更简单但可能更松。

---

---

## 6. Cappart/Bengio综述的松弛相关内容 (Relaxation Content from Surveys)

> 基于 **[Cappart et al. 2023, §2.1]** 和 **[Bengio et al. 2021, §2.1]**。

### 6.1 连续松弛与GNN的联系 **[Cappart et al. 2023, §2.1]**

**[Cappart et al. 2023, §2.1]** 指出：许多CO问题可以重新表述为图上的非凸连续优化问题。早期在ML与CO交叉领域的工作将这些连续优化问题重新诠释为Hopfield网络或自组织映射的基于能量的训练 (Hopfield 1985, Durbin & Willshaw 1987)。这些方法可视为后来基于GNN的可微代理损失方法的先驱。

### 6.2 分支定界中LP松弛的ML增强 **[Bengio et al. 2021, §2.1]**

**[Bengio et al. 2021, §2.1]** 详细描述了LP松弛在分支定界中的核心角色：

分支定界在搜索树的每个节点处计算LP松弛。若松弛不可行或松弛解恰为整数，则节点无需扩展。否则，选择分数变量进行分支，创建两个子节点。LP松弛提供下界 $\underline{z}$，与incumbent解的上界 $\overline{z}$ 比较进行剪枝。

所有MILP求解器进一步通过**切割平面**（有效线性不等式）加强LP松弛，产生分支-切割（branch-and-cut）框架。**[Bengio et al. 2021, §2.1]**

---

> **See also**: [../key_formulas.md] (F10.8, F10.9, F10.12) | [np_hard_problems.md] | [qubo_ising_mapping.md] | [convex_optimization_basics.md] | [duality_kkt.md]
