# Convex Optimization: Sets, Functions, and Problems

> 凸优化基础理论：凸集、凸函数、凸优化问题的定义与核心性质。基于 Boyd & Vandenberghe, *Convex Optimization* (2004), Ch. 2-4。

---

## 1. Convex Sets

### Definition 1.1 (Convex Set) **[Boyd & Vandenberghe, Ch.2, §2.1]**

集合 $C \subseteq \mathbb{R}^n$ 是**凸集**，如果对任意 $x_1, x_2 \in C$ 和 $\theta \in [0, 1]$，有

$$\theta x_1 + (1 - \theta) x_2 \in C$$

几何直觉：连接集合内任意两点的线段完全包含在集合内。

### Definition 1.2 (Convex Combination & Convex Hull) **[Boyd & Vandenberghe, Ch.2, §2.1]**

点 $x = \theta_1 x_1 + \cdots + \theta_k x_k$ 是 $x_1, \ldots, x_k$ 的**凸组合**，如果 $\theta_i \geq 0$，$\sum_{i=1}^k \theta_i = 1$。

集合 $C$ 的**凸包** $\text{conv}(C)$ 是 $C$ 中所有点的凸组合的集合：

$$\text{conv}(C) = \left\{ \sum_{i=1}^k \theta_i x_i \;\middle|\; x_i \in C, \; \theta_i \geq 0, \; \sum_{i=1}^k \theta_i = 1 \right\}$$

凸包是包含 $C$ 的最小凸集。

### Definition 1.3 (Cone & Convex Cone) **[Boyd & Vandenberghe, Ch.2, §2.2]**

集合 $C$ 是**锥**（cone），如果对任意 $x \in C$ 和 $\theta \geq 0$，有 $\theta x \in C$。若同时是凸集，则称为**凸锥**：

$$\theta_1 x_1 + \theta_2 x_2 \in C, \quad \forall x_1, x_2 \in C, \; \theta_1, \theta_2 \geq 0$$

### 1.4 Important Examples of Convex Sets **[Boyd & Vandenberghe, Ch.2, §2.2-2.6]**

**超平面与半空间**：

$$\text{Hyperplane: } \{x \mid a^\top x = b\}, \qquad \text{Halfspace: } \{x \mid a^\top x \leq b\}$$

**球与椭球**：

$$\text{Ball: } B(x_c, r) = \{x \mid \|x - x_c\|_2 \leq r\}$$

$$\text{Ellipsoid: } \mathcal{E} = \{x \mid (x - x_c)^\top P^{-1} (x - x_c) \leq 1\}, \quad P \succ 0$$

**多面体**（Polyhedron）：有限个半空间和超平面的交集

$$\mathcal{P} = \{x \mid Ax \preceq b, \; Cx = d\}$$

多面体是凸集。有界多面体称为多胞形（polytope）。

**半正定锥**（Positive Semidefinite Cone）：

$$\mathbb{S}_+^n = \{X \in \mathbb{S}^n \mid X \succeq 0\}$$

$\mathbb{S}_+^n$ 是凸锥。**证明**：若 $A, B \succeq 0$，$\theta_1, \theta_2 \geq 0$，则对任意 $x$：
$$x^\top (\theta_1 A + \theta_2 B) x = \theta_1 x^\top A x + \theta_2 x^\top B x \geq 0 \quad \square$$

半正定锥在 SDP 松弛中起核心作用。

### Theorem 1.5 (Operations Preserving Convexity) **[Boyd & Vandenberghe, Ch.2, §2.3]**

以下操作保持凸性：
1. **交集**：凸集的任意交集仍是凸集
2. **仿射映射**：若 $C$ 凸，$f(x) = Ax + b$，则 $f(C)$ 和 $f^{-1}(C)$ 都是凸集
3. **透视函数**：$P: \mathbb{R}^{n+1} \to \mathbb{R}^n$，$P(z, t) = z/t$（$t > 0$）保持凸性
4. **线性分式函数**：$f(x) = (Ax + b)/(c^\top x + d)$ 保持凸性

**Proof of 1 (交集保持凸性).** 设 $\{C_\alpha\}_\alpha$ 是凸集族，$C = \bigcap_\alpha C_\alpha$。若 $x_1, x_2 \in C$，则对每个 $\alpha$，$x_1, x_2 \in C_\alpha$，由 $C_\alpha$ 的凸性，$\theta x_1 + (1-\theta) x_2 \in C_\alpha$。因此 $\theta x_1 + (1-\theta) x_2 \in C$。$\square$

### Theorem 1.6 (Separating Hyperplane Theorem) **[Boyd & Vandenberghe, Ch.2, §2.5]**

设 $C, D$ 是不相交的凸集（$C \cap D = \emptyset$）。则存在 $a \neq 0$ 和 $b$ 使得

$$a^\top x \leq b \; \forall x \in C, \qquad a^\top x \geq b \; \forall x \in D$$

即存在超平面 $\{x \mid a^\top x = b\}$ 将 $C$ 和 $D$ 分离。

**应用**：分离超平面定理是对偶理论的几何基础——它解释了为什么凸优化问题有良好的对偶性质。

### Theorem 1.7 (Supporting Hyperplane Theorem) **[Boyd & Vandenberghe, Ch.2, §2.5]**

设 $C$ 是凸集，$x_0$ 是其边界上的点。则存在**支撑超平面**：

$$a^\top x \leq a^\top x_0, \quad \forall x \in C$$

支撑超平面在 $x_0$ 处"切"到凸集的边界，是 KKT 条件的几何直觉来源。

---

## 2. Convex Functions

### Definition 2.1 (Convex Function) **[Boyd & Vandenberghe, Ch.3, §3.1]**

函数 $f: \mathbb{R}^n \to \mathbb{R}$ 是**凸函数**，如果 $\text{dom}(f)$ 是凸集，且对任意 $x, y \in \text{dom}(f)$，$\theta \in [0, 1]$：

$$f(\theta x + (1-\theta) y) \leq \theta f(x) + (1-\theta) f(y)$$

**严格凸**：当 $x \neq y$ 且 $0 < \theta < 1$ 时不等号严格成立。

**凹函数**：$f$ 是凹的当且仅当 $-f$ 是凸的。

### Theorem 2.2 (First-Order Condition) **[Boyd & Vandenberghe, Ch.3, §3.1.3]**

设 $f$ 可微，则 $f$ 是凸函数当且仅当 $\text{dom}(f)$ 是凸集且

$$f(y) \geq f(x) + \nabla f(x)^\top (y - x), \quad \forall x, y \in \text{dom}(f)$$

**Proof ($\Rightarrow$).** 设 $f$ 凸，对 $\theta \in (0, 1]$：

$$f(x + \theta(y - x)) \leq (1-\theta) f(x) + \theta f(y)$$

整理得 $f(y) \geq f(x) + \frac{f(x + \theta(y-x)) - f(x)}{\theta}$。令 $\theta \to 0^+$，右边趋于 $f(x) + \nabla f(x)^\top (y - x)$。

**Proof ($\Leftarrow$).** 设一阶条件成立。对 $x, y \in \text{dom}(f)$，令 $z = \theta x + (1-\theta) y$：

$$f(x) \geq f(z) + \nabla f(z)^\top (x - z), \qquad f(y) \geq f(z) + \nabla f(z)^\top (y - z)$$

将第一个不等式乘以 $\theta$，第二个乘以 $(1-\theta)$，相加：

$$\theta f(x) + (1-\theta) f(y) \geq f(z) + \nabla f(z)^\top (\theta x + (1-\theta)y - z) = f(z) \quad \square$$

**直觉**：凸函数始终位于其任意切线（一阶 Taylor 展开）的上方。这是梯度下降收敛的理论基础。

### Theorem 2.3 (Second-Order Condition) **[Boyd & Vandenberghe, Ch.3, §3.1.4]**

设 $f$ 二阶可微，则 $f$ 是凸函数当且仅当 $\text{dom}(f)$ 是凸集且

$$\nabla^2 f(x) \succeq 0, \quad \forall x \in \text{dom}(f)$$

即 Hessian 矩阵处处半正定。若 $\nabla^2 f(x) \succ 0$ 对所有 $x$ 成立，则 $f$ 严格凸。

**Proof sketch.** 由一阶条件和 Taylor 展开：

$$f(y) = f(x) + \nabla f(x)^\top (y-x) + \frac{1}{2}(y-x)^\top \nabla^2 f(z) (y-x)$$

对某个 $z$ 在 $x$ 和 $y$ 之间。一阶条件要求 $\frac{1}{2}(y-x)^\top \nabla^2 f(z) (y-x) \geq 0$ 对所有 $y-x$，即 $\nabla^2 f(z) \succeq 0$。$\square$

### 2.4 Important Examples of Convex/Concave Functions **[Boyd & Vandenberghe, Ch.3, §3.1.5]**

| 函数 | 凸/凹 | Hessian 验证 |
|------|--------|-------------|
| $f(x) = ax + b$ | 凸且凹（仿射） | $\nabla^2 f = 0$ |
| $f(x) = x^2$ | 凸 | $\nabla^2 f = 2 > 0$ |
| $f(x) = e^{ax}$ | 凸 | $\nabla^2 f = a^2 e^{ax} \geq 0$ |
| $f(x) = -\log x$ | 凸（$x > 0$） | $\nabla^2 f = 1/x^2 > 0$ |
| $f(x) = x \log x$ | 凸（$x > 0$） | $\nabla^2 f = 1/x > 0$ |
| $f(x) = \log(\sum_i e^{x_i})$ | 凸（log-sum-exp） | 见下文 |
| $f(x) = \|x\|_p$ ($p \geq 1$) | 凸 | 三角不等式 |
| $f(X) = \log\det(X^{-1})$ | 凸（$X \succ 0$） | 见 §2.6 |
| $f(x) = \log x$ | 凹（$x > 0$） | $\nabla^2 f = -1/x^2 < 0$ |
| 熵 $H(x) = -\sum x_i \log x_i$ | 凹 | $\nabla^2 H = -\text{diag}(1/x_i)$ |

### Theorem 2.5 (Log-Sum-Exp is Convex) **[Boyd & Vandenberghe, Ch.3, §3.1.5]**

函数 $f(x) = \log\left(\sum_{i=1}^n e^{x_i}\right)$ 是凸函数。

**Proof.** 计算 Hessian：

$$\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{e^{x_i} \mathbf{1}_{i=j}}{\sum_k e^{x_k}} - \frac{e^{x_i} e^{x_j}}{(\sum_k e^{x_k})^2}$$

令 $z_i = e^{x_i} / \sum_k e^{x_k}$（即 softmax），则 $\nabla^2 f = \text{diag}(z) - zz^\top$。

对任意 $v$：$v^\top \nabla^2 f \, v = \sum_i z_i v_i^2 - (\sum_i z_i v_i)^2 = \text{Var}_z[v] \geq 0$。

这里用到了 $\text{Var}[X] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 \geq 0$。$\square$

**ML 应用**：Log-sum-exp 是 softmax 函数的基础，其凸性保证了交叉熵损失在 logits 上的凸性（固定标签时）。

### Theorem 2.6 (Operations Preserving Convexity) **[Boyd & Vandenberghe, Ch.3, §3.2]**

以下操作保持函数凸性：

1. **非负加权和**：若 $f_1, \ldots, f_m$ 凸，$w_i \geq 0$，则 $f = \sum w_i f_i$ 凸
2. **与仿射映射复合**：若 $f$ 凸，则 $g(x) = f(Ax + b)$ 凸
3. **逐点最大**：若 $f_1, \ldots, f_m$ 凸，则 $f(x) = \max_i f_i(x)$ 凸
4. **逐点上确界**：若对每个 $y$，$f(x, y)$ 关于 $x$ 凸，则 $g(x) = \sup_y f(x, y)$ 凸
5. **透视**：若 $f$ 凸，则 $g(x, t) = t f(x/t)$（$t > 0$）凸

**Proof of 3 (逐点最大值).** 对 $\theta \in [0,1]$：

$$f(\theta x + (1-\theta)y) = \max_i f_i(\theta x + (1-\theta)y) \leq \max_i [\theta f_i(x) + (1-\theta) f_i(y)]$$

$$\leq \theta \max_i f_i(x) + (1-\theta) \max_i f_i(y) = \theta f(x) + (1-\theta) f(y) \quad \square$$

**应用**：SDP 的最大特征值函数 $\lambda_{\max}(A) = \sup_{\|x\|=1} x^\top A x$ 是 $A$ 的元素的凸函数（逐点上确界定理的推论）。

### Definition 2.7 (Conjugate Function / Fenchel Conjugate) **[Boyd & Vandenberghe, Ch.3, §3.3]**

函数 $f$ 的**共轭函数**定义为：

$$f^*(y) = \sup_{x \in \text{dom}(f)} \left( y^\top x - f(x) \right)$$

$f^*$ 一定是凸函数（作为仿射函数的逐点上确界），无论 $f$ 是否凸。

**重要性质**：
- **Fenchel 不等式**：$f(x) + f^*(y) \geq x^\top y$（对所有 $x, y$）
- 若 $f$ 是闭凸函数，则 $f^{**} = f$（双共轭等于自身）
- 若 $f$ 可微且凸，则 $f^*(y) = y^\top x^* - f(x^*)$，其中 $x^* = (\nabla f)^{-1}(y)$

**Examples**:

| $f(x)$ | $f^*(y)$ |
|---------|----------|
| $\frac{1}{2}x^\top Q x$ ($Q \succ 0$) | $\frac{1}{2}y^\top Q^{-1} y$ |
| $-\log x$ ($x > 0$) | $-1 - \log(-y)$ ($y < 0$) |
| $e^x$ | $y \log y - y$ ($y > 0$) |
| $\|x\|$ | $0$ if $\|y\|_* \leq 1$, $+\infty$ otherwise |

**应用**：共轭函数是对偶理论的代数基础。Lagrangian 对偶问题可以用共轭函数优雅表述。在 ML 中，变分推断中的 ELBO 推导依赖于 KL 散度的变分表示，而这本质上是 $f$-divergence 的共轭对偶。

---

## 3. Convex Optimization Problems

### Definition 3.1 (Standard Form) **[Boyd & Vandenberghe, Ch.4, §4.1]**

凸优化问题的标准形式：

$$\begin{aligned}
\min \quad & f_0(x) \\
\text{s.t.} \quad & f_i(x) \leq 0, \quad i = 1, \ldots, m \\
& a_i^\top x = b_i, \quad i = 1, \ldots, p
\end{aligned}$$

其中 $f_0, f_1, \ldots, f_m$ 是凸函数，等式约束是仿射的。

### Theorem 3.2 (Local Optimum = Global Optimum) **[Boyd & Vandenberghe, Ch.4, §4.2.2]**

**凸优化的基本定理**：凸优化问题的任何局部最优解都是全局最优解。

**Proof.** 设 $x$ 是局部最优但非全局最优，即存在可行 $y$ 使 $f_0(y) < f_0(x)$。存在 $R > 0$ 使得 $x$ 在 $B(x, R)$ 内最优。

取 $z = \theta y + (1-\theta) x$，选 $\theta > 0$ 足够小使 $\|z - x\| = \theta\|y - x\| < R$。$z$ 是可行的（凸集+凸函数），且

$$f_0(z) \leq \theta f_0(y) + (1-\theta) f_0(x) < \theta f_0(x) + (1-\theta) f_0(x) = f_0(x)$$

与 $x$ 在 $B(x, R)$ 内最优矛盾。$\square$

**意义**：这是凸优化相对于一般非凸优化的根本优势。神经网络的损失函数是非凸的，所以梯度下降只能保证收敛到局部最优（或鞍点）。

### Theorem 3.3 (Optimality Condition for Differentiable $f_0$) **[Boyd & Vandenberghe, Ch.4, §4.2.3]**

设无约束凸优化问题 $\min f_0(x)$，$f_0$ 可微。则 $x^*$ 是全局最优解当且仅当

$$\nabla f_0(x^*) = 0$$

**Proof.** $(\Leftarrow)$：由一阶条件，$f_0(y) \geq f_0(x^*) + \nabla f_0(x^*)^\top (y - x^*) = f_0(x^*)$ 对所有 $y$。

$(\Rightarrow)$：若 $\nabla f_0(x^*) \neq 0$，取 $y = x^* - t \nabla f_0(x^*)$（$t > 0$ 足够小），则 $f_0(y) < f_0(x^*)$。$\square$

---

## 4. Linear Program (LP) **[Boyd & Vandenberghe, Ch.4, §4.3]**

### Definition 4.1 (LP Standard Form)

$$\min \; c^\top x, \quad \text{s.t.} \; Ax \leq b, \; Cx = d$$

目标函数和约束都是仿射的。LP 是最简单的凸优化问题。

**几何解释**：LP 是在多面体 $\{x \mid Ax \leq b, Cx = d\}$ 上最小化线性函数。最优解（如果存在）一定在多面体的顶点（vertex/extreme point）处取得。

### Theorem 4.2 (LP Duality) **[Boyd & Vandenberghe, Ch.4, §4.3; Ch.5, §5.2]**

Primal LP: $\min \; c^\top x, \quad \text{s.t.} \; Ax \leq b$

Dual LP: $\max \; b^\top \lambda, \quad \text{s.t.} \; A^\top \lambda = c, \; \lambda \geq 0$

LP 的强对偶性**始终成立**（无需额外条件），且对偶的对偶是原问题。

**互补松弛条件**：在最优解 $(x^*, \lambda^*)$ 处，

$$\lambda_i^* (a_i^\top x^* - b_i) = 0, \quad \forall i$$

即每个约束要么紧的（取等），要么对应的乘子为零。

---

## 5. Quadratic Program (QP) **[Boyd & Vandenberghe, Ch.4, §4.4]**

### Definition 5.1 (QP Standard Form)

$$\min \; \frac{1}{2} x^\top P x + q^\top x + r, \quad \text{s.t.} \; Ax \leq b, \; Cx = d$$

其中 $P \succeq 0$（半正定），保证目标函数是凸的。

**ML 应用**：
- **岭回归**（Ridge regression）：$\min \|Ax - b\|_2^2 + \lambda \|x\|_2^2$，无约束 QP
- **SVM 对偶**：$\max \sum \alpha_i - \frac{1}{2} \sum \alpha_i \alpha_j y_i y_j k(x_i, x_j)$，带约束 QP
- **Portfolio Optimization**（Markowitz）：$\min x^\top \Sigma x$，s.t. $\mu^\top x \geq r$，$\mathbf{1}^\top x = 1$

### 5.2 Quadratically Constrained QP (QCQP)

$$\min \; \frac{1}{2} x^\top P_0 x + q_0^\top x, \quad \text{s.t.} \; \frac{1}{2} x^\top P_i x + q_i^\top x + r_i \leq 0$$

其中 $P_i \succeq 0$。约束也是凸二次函数。

---

## 6. Second-Order Cone Program (SOCP) **[Boyd & Vandenberghe, Ch.4, §4.4.2]**

### Definition 6.1 (SOCP Standard Form)

$$\min \; f^\top x, \quad \text{s.t.} \; \|A_i x + b_i\|_2 \leq c_i^\top x + d_i, \quad i = 1, \ldots, m$$

SOCP 推广了 LP 和 QCQP：
- LP $\subset$ QCQP $\subset$ SOCP $\subset$ SDP

每个二阶锥约束定义了一个"冰淇淋锥"（Lorentz cone）中的可行域。

**应用**：
- **鲁棒优化**：不确定参数的最坏情况优化通常可以转化为 SOCP
- **Minimax 问题**：$\min_x \max_i \|A_i x - b_i\|$ 可转化为 SOCP
- **量子信息**：某些量子态辨别问题可以表示为 SOCP

---

## 7. Semidefinite Program (SDP) **[Boyd & Vandenberghe, Ch.4, §4.6]**

### Definition 7.1 (SDP Standard Form)

$$\min \; \langle C, X \rangle, \quad \text{s.t.} \; \langle A_i, X \rangle = b_i, \; i = 1, \ldots, m, \quad X \succeq 0$$

其中 $X \in \mathbb{S}^n$（对称矩阵），$\langle A, B \rangle = \text{tr}(A^\top B)$，$X \succeq 0$ 表示半正定。

**等价形式**（Linear Matrix Inequality, LMI）：

$$\min \; c^\top x, \quad \text{s.t.} \; F(x) = F_0 + \sum_{i=1}^n x_i F_i \succeq 0$$

### Theorem 7.2 (SDP Includes LP, QP, SOCP)

**Proof that LP is a special case of SDP:** 令 $X = \text{diag}(x)$，约束 $X \succeq 0$ 等价于 $x \geq 0$（对角矩阵半正定当且仅当对角元非负），$\langle C, X \rangle = c^\top x$。

**SDP 在 CO 中的角色**：
- MaxCut 的 Goemans-Williamson 0.878 近似比来自 SDP 松弛
- 量子 MAXSAT 和量子博弈的界也来自 SDP
- 量子纠缠检测（PPT criterion）本质上是 SDP 可行性问题
- 量子信道容量的某些界通过 SDP 计算

### 7.3 Hierarchy: LP $\subset$ QCQP $\subset$ SOCP $\subset$ SDP **[Boyd & Vandenberghe, Ch.4]**

$$\text{LP} \subset \text{QCQP} \subset \text{SOCP} \subset \text{SDP} \subset \text{Conic Programming}$$

每一级都严格推广前一级。求解复杂度随层级增加而增长：
- LP：$O(n^{3.5} L)$（内点法）或更快（单纯形法实际表现）
- SOCP：$O(n^{3.5})$（内点法）
- SDP：$O(n^{3.5} m)$（内点法，$m$ 为约束数）

---

## 8. Properties of Convex Functions Relevant to ML

### 8.1 Jensen's Inequality **[Boyd & Vandenberghe, Ch.3, §3.1.8]**

若 $f$ 是凸函数，$X$ 是随机变量，则

$$f(\mathbb{E}[X]) \leq \mathbb{E}[f(X)]$$

**ML 应用**：
- **ELBO 推导**：$\log p(x) = \log \mathbb{E}_{q}[p(x,z)/q(z)] \geq \mathbb{E}_{q}[\log(p(x,z)/q(z))]$（由 $-\log$ 的凸性 + Jensen 不等式）
- **KL 散度非负性**：$D_{\text{KL}}(p\|q) = \mathbb{E}_p[-\log(q/p)] \geq -\log \mathbb{E}_p[q/p] = 0$
- **EM 算法**：E-step 的正确性依赖于 Jensen 不等式

### 8.2 Strong Convexity **[Boyd & Vandenberghe, Ch.9, §9.1]**

函数 $f$ 是 **$m$-强凸** 的，如果 $f(x) - \frac{m}{2}\|x\|^2$ 是凸函数，即

$$f(y) \geq f(x) + \nabla f(x)^\top (y - x) + \frac{m}{2}\|y - x\|^2$$

等价于 $\nabla^2 f(x) \succeq mI$ 对所有 $x$。

**意义**：强凸性保证梯度下降以线性速率收敛（见 gradient_methods.md）。$L_2$ 正则化使目标函数变为强凸的：$f(x) + \frac{\lambda}{2}\|x\|^2$ 至少是 $\lambda$-强凸的。

### 8.3 Lipschitz Continuity of Gradient **[Boyd & Vandenberghe, Ch.9, §9.1]**

$\nabla f$ 是 **$L$-Lipschitz** 的，如果

$$\|\nabla f(x) - \nabla f(y)\| \leq L \|x - y\|, \quad \forall x, y$$

等价于 $\nabla^2 f(x) \preceq LI$ 对所有 $x$。

**条件数**：$\kappa = L/m$（$m$ 是强凸参数，$L$ 是 Lipschitz 常数）衡量了问题的"病态程度"。$\kappa$ 越大，梯度下降收敛越慢。

---

## 9. Convexity in Quantum Computing

### 9.1 Density Matrices as Convex Set

量子态的集合（密度矩阵）$\mathcal{D} = \{\rho \mid \rho \succeq 0, \text{tr}(\rho) = 1\}$ 是凸集（SDP 可行域的特例），极点是纯态 $|\psi\rangle\langle\psi|$。

### 9.2 Quantum Channels and Convexity

量子信道（CPTP 映射）的集合是凸集。量子信道容量的许多界可以表述为 SDP。

### 9.3 QAOA and Variational Landscape

QAOA 的代价函数 $\langle \gamma, \beta | H_C | \gamma, \beta \rangle$ 关于参数 $(\gamma, \beta)$ 一般**不是凸的**，这使得变分量子算法面临局部极小值和 barren plateau 问题。对比：经典 SDP 松弛总是能找到全局最优。

---

## 10. Affine Sets and Subspaces (from Boyd Ch.2 Text)

### Definition 10.1 (Affine Set) **[Boyd & Vandenberghe, Ch.2, §2.1.2]**

集合 $C \subseteq \mathbb{R}^n$ 是**仿射集**，如果通过 $C$ 中任意两个不同点的直线仍在 $C$ 中：对任意 $x_1, x_2 \in C$ 和 $\theta \in \mathbb{R}$，有 $\theta x_1 + (1-\theta) x_2 \in C$。

**与子空间的关系**：若 $C$ 是仿射集且 $x_0 \in C$，则 $V = C - x_0 = \{x - x_0 \mid x \in C\}$ 是子空间。

> Boyd 原文 (p.22): "The subspace $V$ associated with the affine set $C$ does not depend on the choice of $x_0$, so $x_0$ can be chosen as any point in $C$."

**Example**: 线性方程组 $\{x \mid Ax = b\}$ 的解集是仿射集，其对应子空间是 $A$ 的零空间。

### Definition 10.2 (Affine Hull & Relative Interior) **[Boyd & Vandenberghe, Ch.2, §2.1.3]**

**仿射包**：$\text{aff}(C) = \{\theta_1 x_1 + \cdots + \theta_k x_k \mid x_i \in C, \sum \theta_i = 1\}$

**相对内部**：
$$\text{relint}(C) = \{x \in C \mid B(x, r) \cap \text{aff}(C) \subseteq C \text{ for some } r > 0\}$$

> Boyd 原文 (p.23): "We define the relative interior of the set $C$, denoted relint $C$, as its interior relative to aff $C$."

**Example** (Boyd Example 2.2): $C = \{x \in \mathbb{R}^3 \mid -1 \leq x_1 \leq 1, -1 \leq x_2 \leq 1, x_3 = 0\}$。$C$ 在 $\mathbb{R}^3$ 中无内点，但相对内部为 $\{x \mid -1 < x_1 < 1, -1 < x_2 < 1, x_3 = 0\}$。

---

## 11. Separating and Supporting Hyperplane Theorems — Full Proofs

### Theorem 11.1 (Separating Hyperplane Theorem — Proof) **[Boyd & Vandenberghe, Ch.2, §2.5.1]**

**定理**：设 $C, D$ 是不相交的凸集（$C \cap D = \emptyset$）。则存在 $a \neq 0$ 和 $b$ 使得 $a^\top x \leq b$ 对所有 $x \in C$，$a^\top x \geq b$ 对所有 $x \in D$。

**Proof** (特殊情况：$\text{dist}(C, D) > 0$ 且最近点存在):

设 $c \in C$ 和 $d \in D$ 是达到 $\text{dist}(C, D)$ 的最近点对。定义：

$$a = d - c, \qquad b = \frac{\|d\|_2^2 - \|c\|_2^2}{2}$$

> Boyd 原文 (p.48): "This hyperplane is perpendicular to the line segment between $c$ and $d$, and passes through its midpoint."

**验证 $f(x) = a^\top x - b$ 在 $D$ 上非负**：假设存在 $u \in D$ 使 $f(u) < 0$。展开：

$$f(u) = (d-c)^\top(u - d) + \frac{1}{2}\|d-c\|_2^2$$

因此 $(d-c)^\top(u-d) < 0$。但是：

$$\frac{d}{dt}\|d + t(u-d) - c\|_2^2\Big|_{t=0} = 2(d-c)^\top(u-d) < 0$$

所以存在小的 $t > 0$ 使得 $d + t(u-d)$ 比 $d$ 更接近 $c$，而 $d + t(u-d) \in D$（凸性），矛盾。$\square$

### Theorem 11.2 (Supporting Hyperplane Theorem — Proof) **[Boyd & Vandenberghe, Ch.2, §2.5.2]**

**定理**：设 $C$ 是非空凸集，$x_0 \in \text{bd}(C)$。则存在 $a \neq 0$ 使得 $a^\top x \leq a^\top x_0$ 对所有 $x \in C$。

**Proof**: 若 $\text{int}(C) \neq \emptyset$，对 $\{x_0\}$ 和 $\text{int}(C)$ 应用分离超平面定理即可。若 $\text{int}(C) = \emptyset$，则 $C$ 在某仿射集中，包含该仿射集的超平面即为（平凡的）支撑超平面。$\square$

> Boyd 原文 (p.51): "A basic result, called the supporting hyperplane theorem, states that for any nonempty convex set $C$, and any $x_0 \in \text{bd } C$, there exists a supporting hyperplane to $C$ at $x_0$."

**部分逆定理**：若集合是闭的、有非空内部、且在边界每个点都有支撑超平面，则该集合是凸的。

---

## 12. Dual Cones and Self-Duality

### Definition 12.1 (Dual Cone) **[Boyd & Vandenberghe, Ch.2, §2.6.1]**

$$K^* = \{y \mid x^\top y \geq 0 \text{ for all } x \in K\}$$

$K^*$ 始终是闭凸锥，即使 $K$ 不凸。

### Theorem 12.2 (Self-Duality of $\mathbb{S}_+^n$) **[Boyd & Vandenberghe, Ch.2, §2.6.1]**

半正定锥 $\mathbb{S}_+^n$ 是自对偶的：$(\mathbb{S}_+^n)^* = \mathbb{S}_+^n$。

**Proof** (来自 Boyd Example 2.24):

($\Rightarrow$) 设 $Y \notin \mathbb{S}_+^n$，则存在 $q$ 使 $q^\top Y q = \text{Tr}(qq^\top Y) < 0$。取 $X = qq^\top \in \mathbb{S}_+^n$，得 $\text{Tr}(XY) < 0$，故 $Y \notin (\mathbb{S}_+^n)^*$。

($\Leftarrow$) 设 $X, Y \in \mathbb{S}_+^n$。$X$ 的谱分解为 $X = \sum_i \lambda_i q_i q_i^\top$（$\lambda_i \geq 0$）。则：

$$\text{Tr}(YX) = \sum_i \lambda_i q_i^\top Y q_i \geq 0$$

因为每个 $q_i^\top Y q_i \geq 0$（$Y \succeq 0$）。$\square$

非负正交锥 $\mathbb{R}_+^n$ 也是自对偶的：$x^\top y \geq 0$ 对所有 $x \geq 0$ 当且仅当 $y \geq 0$。

### 12.3 Properties of Dual Cones **[Boyd & Vandenberghe, Ch.2, §2.6.1]**

- $K^*$ 是闭凸锥
- $K_1 \subseteq K_2 \implies K_2^* \subseteq K_1^*$
- 若 $K$ 有非空内部，则 $K^*$ 是尖的（pointed）
- 若 $K$ 的闭包是尖的，则 $K^*$ 有非空内部
- $K^{**}$ 是 $K$ 的凸包的闭包；若 $K$ 凸且闭，则 $K^{**} = K$
- 若 $K$ 是正常锥，则 $K^*$ 也是正常锥

### 12.4 Dual Generalized Inequalities **[Boyd & Vandenberghe, Ch.2, §2.6.2]**

$x \preceq_K y$ 当且仅当 $\lambda^\top x \leq \lambda^\top y$ 对所有 $\lambda \succeq_{K^*} 0$。

**应用**：对偶锥理论是 SDP 对偶理论的基础。SDP 中 $\langle S, X \rangle = \text{Tr}(SX) \geq 0$（当 $S, X \succeq 0$）正是半正定锥自对偶性的直接推论。

---

## 13. Generalized Inequalities and Proper Cones

### Definition 13.1 (Proper Cone) **[Boyd & Vandenberghe, Ch.2, §2.4.1]**

锥 $K \subseteq \mathbb{R}^n$ 是**正常锥**，如果它满足：
1. $K$ 是凸的
2. $K$ 是闭的
3. $K$ 是实心的（有非空内部）
4. $K$ 是尖的（$x \in K, -x \in K \implies x = 0$）

正常锥诱导偏序 $x \preceq_K y \iff y - x \in K$ 和严格偏序 $x \prec_K y \iff y - x \in \text{int}(K)$。

> Boyd 原文 (p.43): "A proper cone $K$ can be used to define a generalized inequality, which is a partial ordering on $\mathbb{R}^n$ that has many of the properties of the standard ordering on $\mathbb{R}$."

**最小元 vs 极小元**：
- **最小元**：$x$ 是 $S$ 的最小元 $\iff S \subseteq x + K$
- **极小元**：$x$ 是 $S$ 的极小元 $\iff (x - K) \cap S = \{x\}$

对偶刻画：$x$ 是 $S$ 的最小元 $\iff$ 对所有 $\lambda \succ_{K^*} 0$，$x$ 是 $\lambda^\top z$ 在 $z \in S$ 上的唯一最小化点。

---

> **See also**: [duality_kkt.md] (KKT 条件, 对偶理论) | [gradient_methods.md] (梯度下降收敛) | [relaxation_methods.md] (LP/SDP 松弛) | [../key_formulas.md]

> **Primary Reference**: Boyd & Vandenberghe, *Convex Optimization*, Cambridge University Press (2004), Ch. 2-4. Available at https://web.stanford.edu/~boyd/cvxbook/
