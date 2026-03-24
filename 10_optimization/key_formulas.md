# Chapter 10: Combinatorial Optimization - Key Formulas

> 组合优化（Combinatorial Optimization）核心公式速查表。所有公式均使用 LaTeX 记号，解释使用中文。

---

## 基本形式与经典问题

### F10.1: Integer Linear Programming (ILP) General Form

$$\min \; \mathbf{c}^\top \mathbf{x}, \quad \text{s.t.} \; A\mathbf{x} \leq \mathbf{b}, \; \mathbf{x} \in \{0,1\}^n$$

整数线性规划的一般形式：在线性约束 $A\mathbf{x} \leq \mathbf{b}$ 下，最小化线性目标函数 $\mathbf{c}^\top \mathbf{x}$，决策变量限制为二进制整数。ILP 是 NP-hard 问题，是大量组合优化问题的统一建模框架。

**Source**: [references/boyd_convex_optimization.pdf] | Schrijver, *Combinatorial Optimization* (2003)

---

### F10.2: Maximum Independent Set (MIS) Formulation

$$\max \sum_{i \in V} x_i, \quad \text{s.t.} \; x_i + x_j \leq 1 \; \forall (i,j) \in E, \quad x_i \in \{0,1\}$$

最大独立集：在图 $G = (V, E)$ 中选取最多的互不相邻顶点。约束 $x_i + x_j \leq 1$ 保证相邻顶点不同时被选中。MIS 是 NP-hard 问题，且在一般图上不可被多项式时间内以 $n^{1-\varepsilon}$ 的比率近似（除非 P = NP）。

**Source**: [derivations/np_hard_problems.md] | Garey & Johnson, *Computers and Intractability* (1979)

---

### F10.3: Maximum Clique (MCl) Formulation

$$\max \sum_{i \in V} x_i, \quad \text{s.t.} \; x_i + x_j \leq 1 \; \forall (i,j) \notin E, \quad x_i \in \{0,1\}$$

最大团：在图 $G$ 中找最大的完全子图。等价于在补图 $\bar{G}$ 上求最大独立集，即 $\text{MCl}(G) = \text{MIS}(\bar{G})$。约束条件要求所有被选中的顶点在原图中两两相邻。

**Source**: [derivations/np_hard_problems.md] | Bomze et al., *Handbook of Combinatorial Optimization* (1999)

---

### F10.4: Minimum Vertex Cover (MVC) Formulation

$$\min \sum_{i \in V} x_i, \quad \text{s.t.} \; x_i + x_j \geq 1 \; \forall (i,j) \in E, \quad x_i \in \{0,1\}$$

最小顶点覆盖：选取最少的顶点使得每条边至少有一个端点被选中。与 MIS 的对偶关系：$\text{MVC}(G) + \text{MIS}(G) = |V|$，即 $S$ 是独立集当且仅当 $V \setminus S$ 是顶点覆盖。

**Source**: [derivations/np_hard_problems.md] | Garey & Johnson (1979)

---

### F10.5: Maximum Cut (MaxCut) — QUBO Form

$$\max \frac{1}{2} \sum_{(i,j) \in E} w_{ij}(1 - s_i s_j), \quad s_i \in \{-1, +1\}$$

等价的 QUBO 形式（令 $x_i = \frac{1-s_i}{2} \in \{0,1\}$）：

$$\max \sum_{(i,j) \in E} w_{ij}(x_i + x_j - 2x_i x_j)$$

最大割：将图的顶点分为两组，使得跨越两组的边权重之和最大。Ising 形式中，$s_i s_j = -1$ 当且仅当 $i, j$ 被分到不同组。MaxCut 是 NP-hard 的，Goemans-Williamson 的 SDP 松弛算法可达 $\approx 0.878$ 近似比。

**Source**: [derivations/qubo_ising_mapping.md] | Goemans & Williamson, JACM 42 (1995)

---

### F10.6: Traveling Salesman Problem (TSP) Formulation

$$\min \sum_{i=1}^{n} \sum_{j=1}^{n} d_{ij} \sum_{t=1}^{n} x_{i,t} x_{j,t+1}$$

$$\text{s.t.} \quad \sum_{i=1}^{n} x_{i,t} = 1 \; \forall t, \quad \sum_{t=1}^{n} x_{i,t} = 1 \; \forall i, \quad x_{i,t} \in \{0,1\}$$

旅行商问题：寻找经过所有城市恰好一次的最短哈密顿回路。$x_{i,t} = 1$ 表示城市 $i$ 在路径中第 $t$ 个位置。行约束和列约束分别保证每个时间步恰好访问一个城市、每个城市恰好被访问一次。下标 $t+1$ 理解为模 $n$。

**Source**: [derivations/qubo_ising_mapping.md] | Applegate et al., *The Traveling Salesman Problem* (2006)

---

### F10.7: Graph Coloring as Optimization

$$\min k, \quad \text{s.t.} \; \sum_{c=1}^{k} x_{i,c} = 1 \; \forall i \in V, \quad x_{i,c} + x_{j,c} \leq 1 \; \forall (i,j) \in E, \; \forall c$$

图着色问题：用最少的颜色对图的顶点染色，使得相邻顶点颜色不同。$x_{i,c} = 1$ 表示顶点 $i$ 被分配颜色 $c$。第一组约束保证每个顶点恰好一个颜色，第二组约束保证相邻顶点不同色。最小的 $k$ 称为色数 $\chi(G)$。

**Source**: Garey & Johnson (1979) | Jensen & Toft, *Graph Coloring Problems* (1995)

---

## 松弛方法

### F10.8: LP Relaxation

$$\min \; \mathbf{c}^\top \mathbf{x}, \quad \text{s.t.} \; A\mathbf{x} \leq \mathbf{b}, \; 0 \leq x_i \leq 1$$

线性规划松弛：将 ILP 中的整数约束 $x_i \in \{0,1\}$ 放松为连续约束 $0 \leq x_i \leq 1$。LP 松弛的最优值提供原 ILP 的一个下界（最小化问题）。整数性间隙（integrality gap）定义为最坏情况下 LP 松弛最优值与 ILP 最优值之比。

**Source**: [derivations/relaxation_methods.md] | [references/boyd_convex_optimization.pdf]

---

### F10.9: Lagrangian Relaxation

$$L(\boldsymbol{\lambda}) = \min_{\mathbf{x} \in \{0,1\}^n} \left\{ \mathbf{c}^\top \mathbf{x} + \boldsymbol{\lambda}^\top (A\mathbf{x} - \mathbf{b}) \right\}, \quad \boldsymbol{\lambda} \geq \mathbf{0}$$

$$\text{Lagrangian dual:} \quad \max_{\boldsymbol{\lambda} \geq \mathbf{0}} L(\boldsymbol{\lambda})$$

拉格朗日松弛：将困难约束 $A\mathbf{x} \leq \mathbf{b}$ 乘以非负乘子 $\boldsymbol{\lambda}$ 加入目标函数，使子问题更容易求解。对偶函数 $L(\boldsymbol{\lambda})$ 对于任意 $\boldsymbol{\lambda} \geq 0$ 给出原问题最优值的下界。拉格朗日对偶的最优值不差于 LP 松弛（通常严格更好）。

**Source**: [derivations/relaxation_methods.md] | Fisher, *Management Science* 27 (1981)

---

### F10.10: Approximation Ratio Definition

对于最小化问题，算法 $\mathcal{A}$ 的近似比 $\rho$ 定义为：

$$\rho = \sup_{I} \frac{\mathcal{A}(I)}{\text{OPT}(I)} \geq 1$$

对于最大化问题：

$$\rho = \inf_{I} \frac{\mathcal{A}(I)}{\text{OPT}(I)} \leq 1$$

近似比衡量多项式时间算法输出解与最优解的最坏情况比值。$\rho$-近似算法保证在所有实例上，算法解与最优解之比不超过 $\rho$（最小化）或不低于 $\rho$（最大化）。

**Source**: [derivations/np_hard_problems.md] | Vazirani, *Approximation Algorithms* (2001)

---

### F10.11: Greedy Algorithm Approximation Bounds

**MVC 贪心 2-近似**：取 LP 松弛最优解 $\mathbf{x}^*$，令 $S = \{i : x_i^* \geq 1/2\}$，则

$$|S| \leq 2 \cdot \text{OPT}_{\text{MVC}}$$

**MaxCut 随机 0.5-近似**：随机将每个顶点独立等概率分配到两个集合之一，则期望割值

$$\mathbb{E}[\text{Cut}] = \frac{1}{2} \sum_{(i,j) \in E} w_{ij} = \frac{1}{2} W$$

贪心/随机算法为诸多 NP-hard 问题提供了简单的常数近似保证。MVC 的 2-近似是基于 LP 松弛的四舍五入；MaxCut 的 0.5-近似是随机基线，可被 SDP 松弛改进至 0.878。

**Source**: [derivations/relaxation_methods.md] | Vazirani (2001)

---

### F10.12: SDP Relaxation — Goemans-Williamson for MaxCut

$$\max \frac{1}{4} \sum_{(i,j) \in E} w_{ij} \|\mathbf{v}_i - \mathbf{v}_j\|^2, \quad \text{s.t.} \; \|\mathbf{v}_i\|^2 = 1, \; \mathbf{v}_i \in \mathbb{R}^n$$

等价 SDP 形式：$\max \frac{1}{4} \mathbf{w}^\top (\mathbf{1} - \text{diag}(X)) \cdot \ldots$ 简写为

$$\max \frac{1}{2} \sum_{(i,j) \in E} w_{ij} \frac{1 - X_{ij}}{2}, \quad \text{s.t.} \; X_{ii} = 1, \; X \succeq 0$$

随机超平面舍入后，近似比为 $\alpha_{\text{GW}} = \min_{\theta \in [0,\pi]} \frac{2}{\pi} \cdot \frac{\theta}{1 - \cos\theta} \approx 0.87856$。

Goemans-Williamson 算法：(1) 求解 SDP 得到向量 $\{\mathbf{v}_i\}$；(2) 取随机超平面 $\mathbf{r}$；(3) 按 $\text{sign}(\mathbf{v}_i \cdot \mathbf{r})$ 分割顶点。这是组合优化中 SDP 松弛最经典的成功案例。

**Source**: [derivations/relaxation_methods.md] | Goemans & Williamson, JACM 42 (1995)

---

## QUBO 与 Ising 模型

### F10.13: QUBO (Quadratic Unconstrained Binary Optimization)

$$\min_{\mathbf{x} \in \{0,1\}^n} \mathbf{x}^\top Q \mathbf{x} = \min_{\mathbf{x} \in \{0,1\}^n} \sum_{i} Q_{ii} x_i + \sum_{i < j} Q_{ij} x_i x_j$$

QUBO：在二进制变量上最小化二次目标函数，无任何约束。由于 $x_i \in \{0,1\}$ 意味着 $x_i^2 = x_i$，故对角项即线性项。$Q$ 是上三角（或对称）实矩阵。QUBO 是 NP-hard 的，是量子退火和 QAOA 的原生问题形式。

**Source**: [derivations/qubo_ising_mapping.md] | Kochenberger et al., *EJOR* 224 (2014)

---

### F10.14: Ising Model ↔ QUBO Mapping

Ising 哈密顿量：

$$H_{\text{Ising}} = -\sum_{i<j} J_{ij} s_i s_j - \sum_{i} h_i s_i, \quad s_i \in \{-1, +1\}$$

QUBO ↔ Ising 双射：令 $s_i = 2x_i - 1$（即 $x_i = \frac{s_i + 1}{2}$），则

$$H_{\text{Ising}} = 4 \sum_{i<j} Q_{ij} x_i x_j + 2\sum_i \left(Q_{ii} - \sum_{j \neq i} Q_{ij}\right) x_i + \text{const}$$

其中 $J_{ij} = -4Q_{ij}$，$h_i = -2Q_{ii} + 2\sum_{j \neq i} Q_{ij}$（具体系数取决于符号约定）。Ising 模型与 QUBO 在计算复杂性上完全等价，存在保持最优解的线性变换。这是量子计算（量子退火、QAOA）求解组合优化的理论基础。

**Source**: [derivations/qubo_ising_mapping.md] | Lucas, *Frontiers in Physics* 2, 5 (2014)

---

### F10.15: Penalty Method for Constraints

将约束优化转化为无约束 QUBO：

$$\min_{\mathbf{x} \in \{0,1\}^n} f(\mathbf{x}) + \lambda \sum_{k} \left( g_k(\mathbf{x}) \right)^2$$

其中 $g_k(\mathbf{x}) = 0$ 是等式约束，$\lambda > 0$ 是惩罚系数。

典型惩罚项示例（MIS 中相邻约束）：

$$H_{\text{penalty}} = \lambda \sum_{(i,j) \in E} x_i x_j$$

惩罚方法将约束违反转化为目标函数中的二次惩罚项。惩罚系数 $\lambda$ 必须足够大以保证约束被满足，但过大会导致数值问题。选择合适的 $\lambda$ 是实际应用中的关键问题，通常取 $\lambda > \max_i |c_i|$ 即可。

**Source**: [derivations/qubo_ising_mapping.md] | Lucas (2014) | Glover et al., *EJOR* 282 (2019)

---

## 凸优化基础 (Convex Optimization Foundations)

### F10.16: Convex Function — First-Order Condition **[Boyd & Vandenberghe, Ch.3, §3.1.3]**

$$f(y) \geq f(x) + \nabla f(x)^\top (y - x), \quad \forall x, y \in \text{dom}(f)$$

可微函数 $f$ 是凸函数当且仅当上式成立。几何含义：凸函数始终位于其切平面之上。这是梯度下降收敛的理论基础，也是 ELBO 推导中 Jensen 不等式的核心。

**Source**: [derivations/convex_optimization_basics.md] | [references/boyd_convex_optimization.pdf]

---

### F10.17: Second-Order Condition for Convexity **[Boyd & Vandenberghe, Ch.3, §3.1.4]**

$$f \text{ convex} \iff \nabla^2 f(x) \succeq 0, \quad \forall x \in \text{dom}(f)$$

Hessian 矩阵处处半正定等价于函数凸性。若 $\nabla^2 f \succ 0$（正定），则 $f$ 严格凸。用于验证优化问题的凸性。

**Source**: [derivations/convex_optimization_basics.md] | [references/boyd_convex_optimization.pdf]

---

### F10.18: KKT Conditions (Karush-Kuhn-Tucker) **[Boyd & Vandenberghe, Ch.5, §5.5.3]**

$$\boxed{\begin{aligned}
& f_i(x^*) \leq 0, \quad h_i(x^*) = 0 \quad \text{(primal feasibility)} \\
& \lambda_i^* \geq 0 \quad \text{(dual feasibility)} \\
& \lambda_i^* f_i(x^*) = 0 \quad \text{(complementary slackness)} \\
& \nabla f_0(x^*) + \sum_i \lambda_i^* \nabla f_i(x^*) + \sum_i \nu_i^* \nabla h_i(x^*) = 0 \quad \text{(stationarity)}
\end{aligned}}$$

KKT 条件：凸优化 + 强对偶性下的最优性充要条件。互补松弛 $\lambda_i^* f_i(x^*) = 0$ 说明非活跃约束的乘子为零。KKT 是 SVM 对偶推导、SDP 对偶分析、水位填充算法的基础。

**Source**: [derivations/duality_kkt.md] | [references/boyd_convex_optimization.pdf]

---

### F10.19: Lagrangian Dual Function **[Boyd & Vandenberghe, Ch.5, §5.1.2]**

$$g(\lambda, \nu) = \inf_x \left\{ f_0(x) + \sum_i \lambda_i f_i(x) + \sum_i \nu_i h_i(x) \right\} \leq p^*, \quad \forall \lambda \geq 0$$

Lagrange 对偶函数：总是凹函数，对任意 $\lambda \geq 0$ 给出原问题最优值的下界（弱对偶性）。在 Slater 条件下，对偶最优值等于原最优值（强对偶性 $d^* = p^*$）。

**Source**: [derivations/duality_kkt.md] | [references/boyd_convex_optimization.pdf]

---

### F10.20: Gradient Descent Convergence — Strongly Convex Case **[Boyd & Vandenberghe, Ch.9, §9.3]**

$$f(x^{(k)}) - f^* \leq \left(1 - \frac{m}{L}\right)^k \cdot (f(x^{(0)}) - f^*), \quad \kappa = L/m$$

$m$-强凸 + $L$-Lipschitz 梯度的函数，固定步长 $t = 1/L$ 的梯度下降线性收敛。迭代复杂度 $O(\kappa \log(1/\varepsilon))$，条件数 $\kappa$ 越大收敛越慢。

**Source**: [derivations/gradient_methods.md] | [references/boyd_convex_optimization.pdf]

---

### F10.21: Newton's Method — Quadratic Convergence **[Boyd & Vandenberghe, Ch.9, §9.5]**

$$\Delta x_{\text{nt}} = -[\nabla^2 f(x)]^{-1} \nabla f(x)$$

Newton 步：在当前点用二阶 Taylor 近似的最小化方向。近最优点处二次收敛（有效数字每步翻倍），仿射不变，但每步需要 $O(n^3)$ 求解线性系统。

**Source**: [derivations/gradient_methods.md] | [references/boyd_convex_optimization.pdf]

---

### F10.22: Interior Point Method — Central Path **[Boyd & Vandenberghe, Ch.11, §11.2]**

$$x^*(t) = \arg\min_x \left\{ t \cdot f_0(x) - \sum_{i=1}^{m} \log(-f_i(x)) \right\}, \quad t \to \infty \implies x^*(t) \to x^*$$

内点法中心路径：对数障碍函数将约束编码为势垒，参数 $t$ 控制逼近精度。对偶间隙上界 $m/t$。LP/SOCP/SDP 的总复杂度为 $O(\sqrt{m} \log(m/\varepsilon))$ 次 Newton 步。

**Source**: [derivations/gradient_methods.md] | [references/boyd_convex_optimization.pdf]

---

### F10.23: Jensen's Inequality **[Boyd & Vandenberghe, Ch.3, §3.1.8]**

$$f(\mathbb{E}[X]) \leq \mathbb{E}[f(X)] \quad (f \text{ convex})$$

Jensen 不等式：凸函数的期望不小于期望的凸函数值。ML 中 ELBO 推导 $\log p(x) \geq \mathbb{E}_q[\log(p(x,z)/q(z))]$、KL 散度非负性、EM 算法的核心工具。

**Source**: [derivations/convex_optimization_basics.md] | [references/boyd_convex_optimization.pdf]

---

### F10.24: SDP Standard Form **[Boyd & Vandenberghe, Ch.4, §4.6]**

$$\min \; \text{tr}(CX), \quad \text{s.t.} \; \text{tr}(A_i X) = b_i, \; X \succeq 0$$

半定规划标准形式：推广了 LP, QP, SOCP。SDP 松弛是 MaxCut (0.878), MAX-2SAT (0.940) 等 NP-hard 问题最佳近似算法的基础。内点法 $O(n^{3.5} \log(1/\varepsilon))$ 求解。

**Source**: [derivations/convex_optimization_basics.md] | [derivations/relaxation_methods.md] | [references/boyd_convex_optimization.pdf]

---

### F10.25: Fenchel Conjugate **[Boyd & Vandenberghe, Ch.3, §3.3]**

$$f^*(y) = \sup_x \left( y^\top x - f(x) \right), \qquad f(x) + f^*(y) \geq x^\top y \; \text{(Fenchel inequality)}$$

共轭函数/Legendre-Fenchel 变换：$f^*$ 总是凸函数。闭凸函数的双共轭 $f^{**} = f$。对偶理论的代数基础，变分推断中 $f$-divergence 的变分表示依赖于此。

**Source**: [derivations/convex_optimization_basics.md] | [references/boyd_convex_optimization.pdf]

---

### F10.26: Adam Optimizer Update Rule **[Kingma & Ba, ICLR 2015]**

$$\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1-\beta_2^t}, \quad x_{t+1} = x_t - \alpha \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \varepsilon}$$

Adam 优化器：结合一阶矩估计（动量）和二阶矩估计（自适应学习率），带偏差校正。默认 $\alpha=0.001$, $\beta_1=0.9$, $\beta_2=0.999$。当前 LLM/扩散模型训练的标准优化器。

**Source**: [derivations/gradient_methods.md] | Kingma & Ba, ICLR (2015)

---

---

## GNN与ML4CO理论公式 (GNN & ML4CO Formulas)

### F10.27: GNN邻域聚合公式 (GNN Neighborhood Aggregation) **[Cappart et al. 2023, §2.3]**

$$f^{(t)}(v) = \sigma\left(f^{(t-1)}(v) \cdot W_1^{(t)} + \sum_{w \in N(v)} f^{(t-1)}(w) \cdot W_2^{(t)}\right)$$

GNN的核心操作：每层迭代聚合邻居特征并与自身特征合并。GNN对置换不变，天然利用稀疏性。

**Source**: **[Cappart et al. 2023, §2.3, Eq.(1)]** | Morris et al. (2019)

---

### F10.28: ML4CO监督学习目标 (ML4CO Supervised Learning) **[Bengio et al. 2021, §2.2]**

$$\min_{\theta \in \mathbb{R}^p} \mathbb{E}_{X, Y \sim P} \, \ell(Y, f_\theta(X)) \quad \approx \quad \min_\theta \sum_{(x,y) \in D_{\text{train}}} \frac{1}{|D_{\text{train}}|} \ell(y, f_\theta(x))$$

将CO问题实例视为来自未知分布 $P$ 的数据点，通过经验分布近似学习从实例到解的映射。

**Source**: **[Bengio et al. 2021, §2.2, Eq.(2)-(3)]**

---

### F10.29: GNN近似比上界 (GNN Approximation Bound) **[Cappart et al. 2023, §5.1]**

一大类GNN对MVC问题可达到的最佳近似比为**2**（次最优），类推到其他CO问题。此结果通过分布式局部算法的理论迁移得到。

**Source**: **[Cappart et al. 2023, §5.1]**, Sato et al. (2019)

---

### F10.30: RL中的策略梯度 (REINFORCE for CO) **[Bengio et al. 2021, §2.3]**

$$\nabla_\theta \mathcal{L} = \mathbb{E}_{\pi \sim p_\theta}\left[(L(\pi) - b(\mathcal{G})) \nabla_\theta \log p_\theta(\pi | \mathcal{G})\right]$$

策略梯度方法用于训练神经CO求解器：$L(\pi)$ 为解的代价，$b(\mathcal{G})$ 为基线（减方差）。

**Source**: [derivations/neural_co_theory.md] | Williams (1992), Kool et al. (2019)

---

---

### F10.31: AM Encoder (Transformer for CO) **[Kool et al. 2019, §3.1]**

$$\hat{\mathbf{h}}_i = \mathrm{BN}(\mathbf{h}_i^{(l-1)} + \mathrm{MHA}_i^l(\mathbf{h}_1^{(l-1)}, \ldots, \mathbf{h}_n^{(l-1)})), \quad \mathbf{h}_i^{(l)} = \mathrm{BN}(\hat{\mathbf{h}}_i + \mathrm{FF}^l(\hat{\mathbf{h}}_i))$$

Attention Model 编码器：Transformer 编码器的变体（BN 代替 LN，无位置编码以保持置换不变性）。$N=3$ 层，$M=8$ 头，$d_h=128$。

**Source**: [derivations/neural_co_theory.md] | Kool et al., ICLR 2019

---

### F10.32: AM Decoder — Clipped Attention Logits **[Kool et al. 2019, §3.2]**

$$u_{(c)j} = \begin{cases} C \cdot \tanh\left(\frac{\mathbf{q}_{(c)}^\top \mathbf{k}_j}{\sqrt{d_k}}\right) & j \notin \pi_{1:t-1} \\ -\infty & \text{otherwise} \end{cases}$$

AM 解码器的输出 logits：tanh 裁剪（$C=10$）防止 softmax 饱和，mask 已访问节点。Context = [图嵌入, 首节点嵌入, 末节点嵌入]。

**Source**: [derivations/neural_co_theory.md] | Kool et al., ICLR 2019

---

### F10.33: Greedy Rollout Baseline **[Kool et al. 2019, §4]**

$$\nabla \mathcal{L}(\theta|s) = \mathbb{E}_{p_\theta(\pi|s)}\left[(L(\pi) - L(\pi^{\mathrm{greedy}}_{\theta^{\mathrm{BL}}})) \nabla \log p_\theta(\pi|s)\right]$$

基线 $b(s) = L(\pi^{\mathrm{greedy}}_{\theta^{\mathrm{BL}}})$ 为冻结参数的贪心解代价。每 epoch 通过 paired t-test ($\alpha=5\%$) 决定是否更新基线。

**Source**: [derivations/neural_co_theory.md] | Kool et al., ICLR 2019

---

### F10.34: DiffUCO Unsupervised Energy Loss **[DiffUCO, §3]**

$$\mathcal{L}_{\text{DiffUCO}} = \mathbb{E}_{\mathcal{G}, t, \mathbf{x}_t}\left[H(\hat{\mathbf{x}}_0^{(t)}) + \lambda \cdot \mathcal{P}(\hat{\mathbf{x}}_0^{(t)})\right]$$

无监督扩散CO：直接优化目标函数 $H$ + 约束惩罚 $\mathcal{P}$，无需最优解标签。消除了监督学习对精确求解器的依赖。

**Source**: [derivations/neural_co_theory.md] | Sanokowski et al., NeurIPS 2024

---

## 公式速查表（续）

| 编号 | 名称 | 核心表达式 | 应用 |
|------|------|-----------|------|
| F10.27 | GNN聚合 | $f^{(t)}(v) = \sigma(f^{(t-1)} W_1 + \sum_{N} f^{(t-1)} W_2)$ | 图表示学习 |
| F10.28 | ML4CO学习 | $\min_\theta \mathbb{E}_{P}[\ell(Y, f_\theta(X))]$ | 问题分布学习 |
| F10.29 | GNN近似界 | MVC最佳近似比 = 2（次最优） | GNN理论限制 |
| F10.30 | REINFORCE | $\nabla_\theta \mathcal{L} = \mathbb{E}[(L-b)\nabla\log p_\theta]$ | RL训练CO |
| F10.31 | AM Encoder | BN(h + MHA) → BN(h + FF) | Transformer for CO |
| F10.32 | AM Decoder | $C \cdot \tanh(q^\top k / \sqrt{d_k})$ + mask | 自回归CO解码 |
| F10.33 | Greedy Rollout Baseline | $b(s) = L(\pi^{\mathrm{greedy}}_{\theta^{BL}})$ | REINFORCE方差减小 |
| F10.34 | DiffUCO Loss | $\mathbb{E}[H(\hat{x}_0) + \lambda\mathcal{P}]$ | 无监督扩散CO |

---

> **Navigation**: [derivations/np_hard_problems.md] | [derivations/relaxation_methods.md] | [derivations/qubo_ising_mapping.md] | [derivations/neural_co_theory.md] | [derivations/convex_optimization_basics.md] | [derivations/duality_kkt.md] | [derivations/gradient_methods.md]
