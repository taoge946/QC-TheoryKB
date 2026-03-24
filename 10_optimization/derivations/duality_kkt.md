# Lagrangian Duality, KKT Conditions, and Strong Duality

> 拉格朗日对偶理论完整推导：Lagrangian、对偶函数、弱/强对偶性、KKT 条件、互补松弛。基于 Boyd & Vandenberghe, *Convex Optimization* (2004), Ch. 5。

---

## 1. The Lagrangian

### Setup: General Optimization Problem **[Boyd & Vandenberghe, Ch.5, §5.1]**

考虑（不一定凸的）优化问题：

$$\begin{aligned}
\min \quad & f_0(x) \\
\text{s.t.} \quad & f_i(x) \leq 0, \quad i = 1, \ldots, m \\
& h_i(x) = 0, \quad i = 1, \ldots, p
\end{aligned}$$

记最优值为 $p^*$，定义域 $\mathcal{D} = \bigcap_{i=0}^{m} \text{dom}(f_i) \cap \bigcap_{i=1}^{p} \text{dom}(h_i)$。

### Definition 1.1 (Lagrangian) **[Boyd & Vandenberghe, Ch.5, §5.1.1]**

**Lagrangian** $L: \mathbb{R}^n \times \mathbb{R}^m \times \mathbb{R}^p \to \mathbb{R}$：

$$L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^{m} \lambda_i f_i(x) + \sum_{i=1}^{p} \nu_i h_i(x)$$

其中：
- $\lambda_i \geq 0$ 是不等式约束 $f_i(x) \leq 0$ 的 **Lagrange 乘子**（对偶变量）
- $\nu_i$ 是等式约束 $h_i(x) = 0$ 的 Lagrange 乘子（无符号限制）
- $\lambda = (\lambda_1, \ldots, \lambda_m)$ 和 $\nu = (\nu_1, \ldots, \nu_p)$ 统称为**对偶变量**

**直觉**：Lagrangian 将约束"软化"到目标函数中。违反约束时（$f_i(x) > 0$），惩罚项 $\lambda_i f_i(x) > 0$ 增大目标值；满足约束时（$f_i(x) \leq 0$），惩罚项 $\leq 0$ 不会增大目标值。

---

## 2. Lagrange Dual Function

### Definition 2.1 (Dual Function) **[Boyd & Vandenberghe, Ch.5, §5.1.2]**

**Lagrange 对偶函数** $g: \mathbb{R}^m \times \mathbb{R}^p \to \mathbb{R}$：

$$g(\lambda, \nu) = \inf_{x \in \mathcal{D}} L(x, \lambda, \nu) = \inf_{x} \left\{ f_0(x) + \sum_{i=1}^{m} \lambda_i f_i(x) + \sum_{i=1}^{p} \nu_i h_i(x) \right\}$$

对偶函数是仿射函数（关于 $(\lambda, \nu)$）的逐点下确界，因此**无论原问题是否凸，$g(\lambda, \nu)$ 一定是凹函数**。

### Theorem 2.2 (Lower Bound Property / Weak Duality) **[Boyd & Vandenberghe, Ch.5, §5.1.3]**

对任意 $\lambda \succeq 0$ 和任意 $\nu$：

$$g(\lambda, \nu) \leq p^*$$

**Proof.** 设 $\tilde{x}$ 是原问题的任意可行点，即 $f_i(\tilde{x}) \leq 0$，$h_i(\tilde{x}) = 0$。则：

$$L(\tilde{x}, \lambda, \nu) = f_0(\tilde{x}) + \underbrace{\sum_{i=1}^{m} \lambda_i f_i(\tilde{x})}_{\leq 0 \text{ (since } \lambda_i \geq 0, f_i \leq 0)} + \underbrace{\sum_{i=1}^{p} \nu_i h_i(\tilde{x})}_{= 0} \leq f_0(\tilde{x})$$

因此 $g(\lambda, \nu) = \inf_x L(x, \lambda, \nu) \leq L(\tilde{x}, \lambda, \nu) \leq f_0(\tilde{x})$。

由于这对所有可行 $\tilde{x}$ 成立，$g(\lambda, \nu) \leq \inf_{\tilde{x} \text{ feasible}} f_0(\tilde{x}) = p^*$。$\square$

**关键意义**：对偶函数给出原问题最优值的下界族。每选取一组 $(\lambda, \nu)$（$\lambda \geq 0$），就得到一个下界。

### 2.3 Examples of Dual Functions

**Example 1: LP Dual** **[Boyd & Vandenberghe, Ch.5, §5.2.1]**

Primal: $\min \; c^\top x$, s.t. $Ax \leq b$

Lagrangian: $L(x, \lambda) = c^\top x + \lambda^\top (Ax - b) = (c + A^\top \lambda)^\top x - b^\top \lambda$

$$g(\lambda) = \inf_x \left[ (c + A^\top \lambda)^\top x - b^\top \lambda \right] = \begin{cases} -b^\top \lambda & \text{if } A^\top \lambda + c = 0 \\ -\infty & \text{otherwise} \end{cases}$$

因此有限的对偶函数值要求 $A^\top \lambda = -c$，即对偶问题是：

$$\max \; -b^\top \lambda, \quad \text{s.t.} \; A^\top \lambda + c = 0, \; \lambda \geq 0$$

等价写为 $\max \; b^\top \mu$，s.t. $A^\top \mu = c$, $\mu \leq 0$（令 $\mu = -\lambda$），这正是标准 LP 对偶。

**Example 2: Quadratic Minimization with Equality Constraints** **[Boyd & Vandenberghe, Ch.5, §5.2.2]**

Primal: $\min \; \frac{1}{2} x^\top P x + q^\top x + r$, s.t. $Ax = b$, $P \succ 0$

Lagrangian: $L(x, \nu) = \frac{1}{2} x^\top P x + q^\top x + r + \nu^\top (Ax - b)$

令 $\nabla_x L = Px + q + A^\top \nu = 0$，解得 $x^* = -P^{-1}(q + A^\top \nu)$，代入：

$$g(\nu) = -\frac{1}{2}(q + A^\top \nu)^\top P^{-1} (q + A^\top \nu) + r - b^\top \nu$$

这是关于 $\nu$ 的凹二次函数（无约束对偶），对偶最优 $\nu^*$ 通过 $\nabla_\nu g = 0$ 求解。

---

## 3. Lagrange Dual Problem

### Definition 3.1 (Dual Problem) **[Boyd & Vandenberghe, Ch.5, §5.2]**

**Lagrange 对偶问题**：

$$\begin{aligned}
\max \quad & g(\lambda, \nu) \\
\text{s.t.} \quad & \lambda \succeq 0
\end{aligned}$$

即在所有下界中找最紧的一个。对偶问题**总是凸优化问题**（最大化凹函数，线性约束），无论原问题是否凸。

记对偶最优值为 $d^*$。

### Theorem 3.2 (Weak Duality) **[Boyd & Vandenberghe, Ch.5, §5.2.3]**

$$d^* \leq p^*$$

对所有优化问题（凸或非凸）成立。差 $p^* - d^* \geq 0$ 称为**对偶间隙**（duality gap）。

**Proof.** 由 Theorem 2.2，$g(\lambda, \nu) \leq p^*$ 对所有可行 $(\lambda, \nu)$。取上确界：$d^* = \sup_{\lambda \geq 0, \nu} g(\lambda, \nu) \leq p^*$。$\square$

---

## 4. Strong Duality and Slater's Condition

### Definition 4.1 (Strong Duality) **[Boyd & Vandenberghe, Ch.5, §5.2.3]**

当 $d^* = p^*$ 时，称**强对偶性**成立。此时对偶间隙为零。

### Theorem 4.2 (Slater's Constraint Qualification) **[Boyd & Vandenberghe, Ch.5, §5.2.3]**

对于**凸优化问题**（$f_0, f_1, \ldots, f_m$ 凸，$h_i$ 仿射），如果存在**严格可行点** $\tilde{x}$：

$$f_i(\tilde{x}) < 0, \quad i = 1, \ldots, m; \qquad h_i(\tilde{x}) = 0, \quad i = 1, \ldots, p$$

则**强对偶性成立**：$d^* = p^*$。

**注意**：如果部分不等式约束 $f_i$ 是仿射的，则只需对非仿射约束要求严格不等式。特别地，对 LP（所有约束都是仿射的），只要原问题可行，强对偶性就成立。

**Proof sketch (geometric argument).** 考虑集合：

$$\mathcal{G} = \{(u, v, t) \mid \exists x: f_i(x) \leq u_i, h_i(x) = v_i, f_0(x) \leq t\}$$

$p^*$ 是使 $(0, 0, t) \in \mathcal{G}$ 的最小 $t$。对偶函数的几何解释是：$g(\lambda, \nu)$ 对应在 $\mathcal{G}$ 上方的某个支撑超平面。Slater 条件（严格可行点存在）保证 $\mathcal{G}$ 在 $(0, 0, p^*)$ 处有支撑超平面，从而 $d^* = p^*$。正式证明用分离超平面定理。$\square$

**意义**：Slater 条件是实践中最常用的强对偶性充分条件。对于 LP、QP（可行域非空）、SDP（存在严格正定可行解），强对偶性几乎总是成立。

### 4.3 When Does Strong Duality Fail?

强对偶性可能失败的情况：
1. **非凸问题**：一般非凸问题可能有正的对偶间隙
2. **不满足约束资格**：即使是凸问题，如果没有严格可行点（如约束不相容或只有边界可行），强对偶性可能失败
3. **Integer Programming**：ILP 到 LP 松弛的"对偶间隙"（整数性间隙）本质上是因为整数约束的非凸性

---

## 5. KKT Conditions — Full Derivation

### Theorem 5.1 (KKT Conditions) **[Boyd & Vandenberghe, Ch.5, §5.5.3]**

设原问题是凸优化，$f_0, f_1, \ldots, f_m$ 可微，强对偶性成立。则 $x^*$ 是原问题最优解，$(\lambda^*, \nu^*)$ 是对偶最优解，**当且仅当**以下 KKT 条件全部成立：

$$\boxed{\begin{aligned}
\text{(1) Primal feasibility:} \quad & f_i(x^*) \leq 0, \quad i = 1, \ldots, m \\
& h_i(x^*) = 0, \quad i = 1, \ldots, p \\[6pt]
\text{(2) Dual feasibility:} \quad & \lambda_i^* \geq 0, \quad i = 1, \ldots, m \\[6pt]
\text{(3) Complementary slackness:} \quad & \lambda_i^* f_i(x^*) = 0, \quad i = 1, \ldots, m \\[6pt]
\text{(4) Stationarity:} \quad & \nabla f_0(x^*) + \sum_{i=1}^{m} \lambda_i^* \nabla f_i(x^*) + \sum_{i=1}^{p} \nu_i^* \nabla h_i(x^*) = 0
\end{aligned}}$$

### 5.2 Full Derivation of KKT Conditions **[Boyd & Vandenberghe, Ch.5, §5.5]**

**Step 1: From Strong Duality to Complementary Slackness.**

假设强对偶性成立，$x^*$ 原最优，$(\lambda^*, \nu^*)$ 对偶最优。则：

$$f_0(x^*) = p^* = d^* = g(\lambda^*, \nu^*)$$

展开：

$$f_0(x^*) = g(\lambda^*, \nu^*) = \inf_x L(x, \lambda^*, \nu^*)$$

$$\leq L(x^*, \lambda^*, \nu^*) = f_0(x^*) + \sum_{i=1}^{m} \lambda_i^* f_i(x^*) + \sum_{i=1}^{p} \nu_i^* h_i(x^*)$$

$$= f_0(x^*) + \sum_{i=1}^{m} \underbrace{\lambda_i^*}_{\geq 0} \underbrace{f_i(x^*)}_{\leq 0} + 0 \leq f_0(x^*)$$

所有不等式取等，因此：

$$\sum_{i=1}^{m} \lambda_i^* f_i(x^*) = 0$$

由于每一项 $\lambda_i^* f_i(x^*) \leq 0$，而总和为零，所以每一项都必须为零：

$$\lambda_i^* f_i(x^*) = 0, \quad \forall i = 1, \ldots, m \quad \text{(Complementary Slackness)}$$

**解读**：对每个约束 $i$，要么约束是"紧的"（$f_i(x^*) = 0$，约束活跃），要么对应的乘子 $\lambda_i^* = 0$（约束"不起作用"）。直觉上，只有活跃约束才"值得"分配正的乘子。

**Step 2: Stationarity from Minimization.**

从上面的推导，$f_0(x^*) = \inf_x L(x, \lambda^*, \nu^*)$ 意味着 $x^*$ 是 $L(x, \lambda^*, \nu^*)$ 关于 $x$ 的最小化点。

若 $L$ 关于 $x$ 可微，必要条件是：

$$\nabla_x L(x^*, \lambda^*, \nu^*) = \nabla f_0(x^*) + \sum_{i=1}^{m} \lambda_i^* \nabla f_i(x^*) + \sum_{i=1}^{p} \nu_i^* \nabla h_i(x^*) = 0$$

这就是**驻点条件**（stationarity condition）。

**Step 3: KKT Sufficiency for Convex Problems.**

反方向：设 $\tilde{x}, \tilde{\lambda}, \tilde{\nu}$ 满足所有 KKT 条件。

由驻点条件，$\tilde{x}$ 是 $L(x, \tilde{\lambda}, \tilde{\nu})$ 关于 $x$ 的最小化点（因为 $L$ 关于 $x$ 是凸函数，驻点即全局最小）。因此：

$$g(\tilde{\lambda}, \tilde{\nu}) = L(\tilde{x}, \tilde{\lambda}, \tilde{\nu}) = f_0(\tilde{x}) + \sum_i \tilde{\lambda}_i f_i(\tilde{x}) + \sum_i \tilde{\nu}_i h_i(\tilde{x})$$

$$= f_0(\tilde{x}) + 0 + 0 = f_0(\tilde{x})$$

（其中用了互补松弛 $\tilde{\lambda}_i f_i(\tilde{x}) = 0$ 和原始可行性 $h_i(\tilde{x}) = 0$。）

所以 $g(\tilde{\lambda}, \tilde{\nu}) = f_0(\tilde{x})$，即对偶间隙为零。由弱对偶性 $g(\tilde{\lambda}, \tilde{\nu}) \leq p^* \leq f_0(\tilde{x})$，夹逼得 $p^* = f_0(\tilde{x}) = d^*$。

因此 $\tilde{x}$ 是原最优，$(\tilde{\lambda}, \tilde{\nu})$ 是对偶最优。$\square$

### 5.3 KKT for Nonconvex Problems **[Boyd & Vandenberghe, Ch.5, §5.5.1]**

对于**非凸问题**，KKT 条件在适当的约束资格（如 LICQ: Linear Independence Constraint Qualification）下仍是**必要条件**，但不再是充分条件。

LICQ 要求：在最优点处，所有活跃不等式约束的梯度 $\{\nabla f_i(x^*) \mid f_i(x^*) = 0\}$ 和等式约束的梯度 $\{\nabla h_i(x^*)\}$ 线性无关。

---

## 6. Applications of KKT

### 6.1 Water-Filling (Optimal Power Allocation) **[Boyd & Vandenberghe, Ch.5, §5.5.3]**

$$\max \sum_{i=1}^{n} \log(\alpha_i + x_i), \quad \text{s.t.} \; x \succeq 0, \; \mathbf{1}^\top x = 1$$

KKT 条件给出：

$$x_i^* = \max\left\{0, \; \frac{1}{\nu^*} - \alpha_i\right\}$$

其中 $\nu^*$ 是"水位"，由约束 $\sum x_i = 1$ 确定。这就是经典的"注水"（water-filling）解。

**应用**：MIMO 通信中的功率分配、并行高斯信道的容量达到。

### 6.2 SVM Dual via KKT **[Boyd & Vandenberghe, Ch.5; related to ML]**

Primal SVM（soft margin）：

$$\min_{w, b, \xi} \frac{1}{2}\|w\|^2 + C \sum_i \xi_i, \quad \text{s.t.} \; y_i(w^\top x_i + b) \geq 1 - \xi_i, \; \xi_i \geq 0$$

写成标准形式（$f_i \leq 0$）并应用 KKT：

Lagrangian:
$$L = \frac{1}{2}\|w\|^2 + C\sum_i \xi_i - \sum_i \alpha_i [y_i(w^\top x_i + b) - 1 + \xi_i] - \sum_i \mu_i \xi_i$$

**Stationarity:**

$$\frac{\partial L}{\partial w} = 0 \implies w = \sum_i \alpha_i y_i x_i$$

$$\frac{\partial L}{\partial b} = 0 \implies \sum_i \alpha_i y_i = 0$$

$$\frac{\partial L}{\partial \xi_i} = 0 \implies C - \alpha_i - \mu_i = 0 \implies 0 \leq \alpha_i \leq C$$

代入 Lagrangian 得 **SVM 对偶问题**：

$$\max_\alpha \sum_i \alpha_i - \frac{1}{2} \sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^\top x_j$$

$$\text{s.t.} \; 0 \leq \alpha_i \leq C, \quad \sum_i \alpha_i y_i = 0$$

**Complementary slackness** 给出支持向量的特征：$\alpha_i > 0$ 仅当 $y_i(w^\top x_i + b) = 1 - \xi_i$（约束活跃），这些点就是**支持向量**。

### 6.3 KKT for SDP **[Boyd & Vandenberghe, Ch.5, §5.9]**

SDP primal: $\min \langle C, X \rangle$, s.t. $\langle A_i, X \rangle = b_i$, $X \succeq 0$

SDP dual: $\max \; b^\top y$, s.t. $\sum y_i A_i + S = C$, $S \succeq 0$

KKT 条件：
- **Primal feasibility**: $\langle A_i, X \rangle = b_i$, $X \succeq 0$
- **Dual feasibility**: $C - \sum y_i A_i = S \succeq 0$
- **Complementary slackness**: $\langle S, X \rangle = \text{tr}(SX) = 0$

由于 $S, X \succeq 0$ 且 $\text{tr}(SX) = 0$，这要求 $SX = 0$（半正定矩阵的"互补"）。

**在 CO 中的应用**：SDP 的互补松弛条件 $SX = 0$ 限制了 $X$ 的秩（因为 $\text{rank}(X) + \text{rank}(S) \leq n$），这是 SDP 舍入方案的理论基础。例如，Goemans-Williamson 的 MaxCut 算法中，SDP 解的秩结构决定了舍入的质量。

### 6.4 KKT for Quantum State Discrimination

最小错误量子态辨别可以表述为 SDP：

$$\min \; 1 - \sum_i p_i \text{tr}(\Pi_i \rho_i), \quad \text{s.t.} \; \Pi_i \succeq 0, \; \sum_i \Pi_i = I$$

KKT/对偶条件给出 Helstrom 条件：POVM 元素 $\Pi_i$ 投影到 $p_i \rho_i - \Lambda$ 的正特征空间上（$\Lambda$ 是对偶变量），互补松弛给出 $\Pi_i (p_i \rho_i - \Lambda) \Pi_i = \Pi_i (p_i \rho_i - \Lambda)$。

---

## 7. Sensitivity Analysis via Duality **[Boyd & Vandenberghe, Ch.5, §5.6]**

### Theorem 7.1 (Dual Variables as Sensitivity)

考虑参数化问题：

$$p^*(u, v) = \inf \{f_0(x) \mid f_i(x) \leq u_i, \; h_i(x) = v_i\}$$

在强对偶性下，对偶最优 $\lambda_i^*$ 给出最优值关于约束扰动的灵敏度：

$$\lambda_i^* = -\frac{\partial p^*}{\partial u_i}\bigg|_{u=0}$$

$$\nu_i^* = -\frac{\partial p^*}{\partial v_i}\bigg|_{v=0}$$

**解读**：
- $\lambda_i^*$ 大 $\implies$ 放松第 $i$ 个不等式约束能显著改善目标（该约束"瓶颈"）
- $\lambda_i^* = 0$（由互补松弛，约束非活跃）$\implies$ 小幅放松不影响最优值
- 这就是经济学中"影子价格"（shadow price）的含义

---

## 8. Minimax Interpretation and Saddle Point **[Boyd & Vandenberghe, Ch.5, §5.4]**

### Theorem 8.1 (Saddle Point Characterization)

$(x^*, \lambda^*, \nu^*)$ 是鞍点（saddle point），即

$$L(x^*, \lambda, \nu) \leq L(x^*, \lambda^*, \nu^*) \leq L(x, \lambda^*, \nu^*), \quad \forall x, \; \forall \lambda \geq 0, \; \forall \nu$$

当且仅当 $x^*$ 原最优，$(\lambda^*, \nu^*)$ 对偶最优，且对偶间隙为零。

这给出了 minimax 等式：

$$\max_{\lambda \geq 0, \nu} \min_x L(x, \lambda, \nu) = \min_x \max_{\lambda \geq 0, \nu} L(x, \lambda, \nu) = p^* = d^*$$

**ML 应用**：GAN 的训练本质上是一个 minimax 问题 $\min_G \max_D V(D, G)$，但由于非凸性，鞍点不一定存在/可达。对比：凸优化中强对偶性保证鞍点存在。

---

## 9. Duality for Combinatorial Optimization

### 9.1 LP Relaxation as Lagrangian Relaxation **[Boyd & Vandenberghe, Ch.5; applied to CO]**

对于 ILP $\min c^\top x$, s.t. $Ax \leq b$, $x \in \{0,1\}^n$：

将整数约束视为"复杂约束"，拉格朗日松弛恰好给出 LP 松弛。因此 LP 对偶理论是 CO 松弛方法的基础。

### 9.2 SDP Relaxation for QUBO/MaxCut

QUBO 问题 $\min x^\top Q x$, $x \in \{0,1\}^n$ 可以通过"提升"$X = xx^\top$ 转化为：

$$\min \langle Q, X \rangle, \quad \text{s.t.} \; X_{ii} = x_i, \; X = xx^\top$$

松弛 $X = xx^\top$ 为 $X \succeq 0$（去掉秩-1 约束），加上 Schur complement 条件 $\begin{pmatrix} X & x \\ x^\top & 1 \end{pmatrix} \succeq 0$，得到 SDP 松弛。

SDP 松弛的对偶间隙为零（Slater 条件通常成立），所以可以用对偶解的互补松弛条件分析松弛质量。

### 9.3 QAOA and Duality Gap

QAOA 在 $p \to \infty$ 时理论上能达到最优解，但对有限 $p$，QAOA 的输出质量可以与 SDP 松弛的对偶间隙相关联。这为量子-经典混合算法的性能分析提供了理论框架。

---

## Summary: KKT Conditions Quick Reference

| 条件 | 公式 | 含义 |
|------|------|------|
| Primal feasibility | $f_i(x^*) \leq 0$, $h_i(x^*) = 0$ | 解满足所有约束 |
| Dual feasibility | $\lambda_i^* \geq 0$ | 不等式乘子非负 |
| Complementary slackness | $\lambda_i^* f_i(x^*) = 0$ | 非活跃约束的乘子为零 |
| Stationarity | $\nabla_x L = 0$ | Lagrangian 关于 $x$ 的梯度为零 |

**凸 + 强对偶 $\implies$ KKT 是充要条件**（最重要的结论）。

---

## 10. Theorem of Alternatives (from Boyd Ch.2, §2.5)

### Theorem 10.1 (Theorem of Alternatives for Strict Linear Inequalities) **[Boyd & Vandenberghe, Ch.2, Example 2.21]**

对于严格线性不等式系统 $Ax \prec b$：该系统不可行当且仅当存在 $\lambda \in \mathbb{R}^m$ 满足：

$$\lambda \neq 0, \quad \lambda \succeq 0, \quad A^\top \lambda = 0, \quad \lambda^\top b \leq 0$$

> Boyd 原文 (p.49): "We say that (2.17) and (2.18) form a pair of alternatives: for any data $A$ and $b$, exactly one of them is solvable."

**Proof**: 由分离超平面定理。若 $C = \{b - Ax \mid x \in \mathbb{R}^n\}$（仿射集）和 $D = \mathbb{R}^m_{++}$（开凸集）不相交，则存在分离超平面。利用仿射集上线性函数有界必为零的性质得 $A^\top \lambda = 0$。$\square$

### Theorem 10.2 (Generalized Alternatives) **[Boyd & Vandenberghe, Ch.2, Example 2.26]**

对于广义严格不等式 $Ax \prec_K b$（$K$ 正常锥）：该系统不可行当且仅当存在 $\lambda$ 满足：

$$\lambda \neq 0, \quad \lambda \succeq_{K^*} 0, \quad A^\top \lambda = 0, \quad \lambda^\top b \leq 0$$

---

## 11. Conjugate Functions and Duality (from Boyd Ch.3)

### Theorem 11.1 (Conjugate Function Properties) **[Boyd & Vandenberghe, Ch.3, §3.3]**

共轭函数 $f^*(y) = \sup_x (y^\top x - f(x))$ 满足：

1. $f^*$ 始终是凸函数（作为仿射函数的逐点上确界）
2. **Fenchel-Young 不等式**: $f(x) + f^*(y) \geq x^\top y$
3. 若 $f$ 闭凸，则 $f^{**} = f$
4. 若 $f$ 可微凸，$f^*(y) = y^\top x^* - f(x^*)$，其中 $\nabla f(x^*) = y$

**与对偶问题的关系**：

对于无约束优化 $\min f_0(x) + \sum f_i(x)$，拉格朗日对偶函数可以写成：

$$g(\lambda) = -f_0^*(-A^\top \lambda) - \sum \lambda_i f_i^*(-\lambda_i)$$

> Boyd (p.91): "The conjugate function arises in many dual problems" — 共轭函数是从原问题到对偶问题的代数桥梁。

---

> **See also**: [convex_optimization_basics.md] (凸集, 凸函数, 对偶锥) | [gradient_methods.md] (优化算法) | [relaxation_methods.md] (SDP 松弛与对偶) | [../key_formulas.md]

> **Primary Reference**: Boyd & Vandenberghe, *Convex Optimization*, Cambridge University Press (2004), Ch. 2, 3, 5. Available at https://web.stanford.edu/~boyd/cvxbook/
