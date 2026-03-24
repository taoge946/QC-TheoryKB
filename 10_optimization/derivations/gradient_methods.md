# Gradient Methods, Newton's Method, and Interior Point Methods

> 无约束与约束优化算法：梯度下降收敛性分析、Newton 法、内点法，以及 ML 训练中的 Adam 优化器。基于 Boyd & Vandenberghe, *Convex Optimization* (2004), Ch. 9, 11。

---

## 1. Gradient Descent

### 1.1 Algorithm **[Boyd & Vandenberghe, Ch.9, §9.3]**

无约束凸优化 $\min f(x)$，$f$ 可微凸函数。

**梯度下降迭代**：

$$x^{(k+1)} = x^{(k)} - t_k \nabla f(x^{(k)})$$

其中 $t_k > 0$ 是步长（学习率）。

**负梯度方向是最速下降方向**：在所有单位方向 $\|v\| = 1$ 中，$f$ 沿 $v = -\nabla f(x) / \|\nabla f(x)\|$ 方向下降最快：

$$\min_{\|v\|=1} \nabla f(x)^\top v = -\|\nabla f(x)\|$$

### 1.2 Step Size Selection **[Boyd & Vandenberghe, Ch.9, §9.2]**

**精确线搜索**：$t_k = \arg\min_{t \geq 0} f(x^{(k)} - t \nabla f(x^{(k)}))$

**Backtracking line search**（更实用）：参数 $\alpha \in (0, 0.5)$，$\beta \in (0, 1)$。从 $t = 1$ 开始，反复令 $t := \beta t$ 直到 Armijo 条件满足：

$$f(x - t \nabla f(x)) \leq f(x) - \alpha t \|\nabla f(x)\|^2$$

Armijo 条件保证目标函数有足够的下降量。$\alpha$ 控制"足够下降"的阈值，$\beta$ 控制步长收缩速率。

### 1.3 Convergence for Lipschitz Gradient **[Boyd & Vandenberghe, Ch.9, §9.3.1]**

**Assumption.** $f$ 是凸的，$\nabla f$ 是 $L$-Lipschitz 连续的（$\|\nabla f(x) - \nabla f(y)\| \leq L\|x-y\|$）。

**Theorem (Sublinear Convergence).** 用固定步长 $t = 1/L$，梯度下降满足：

$$f(x^{(k)}) - f^* \leq \frac{L \|x^{(0)} - x^*\|^2}{2k}$$

即收敛速率为 $O(1/k)$。要达到 $\varepsilon$-精度，需要 $O(L/\varepsilon)$ 次迭代。

**Proof.** 由 $L$-Lipschitz 梯度：

$$f(y) \leq f(x) + \nabla f(x)^\top (y-x) + \frac{L}{2}\|y-x\|^2$$

令 $y = x - \frac{1}{L}\nabla f(x)$：

$$f(x^{(k+1)}) \leq f(x^{(k)}) - \frac{1}{2L}\|\nabla f(x^{(k)})\|^2$$

由凸性的一阶条件 $f^* \geq f(x^{(k)}) + \nabla f(x^{(k)})^\top (x^* - x^{(k)})$，得：

$$\|\nabla f(x^{(k)})\|^2 \geq 2L(f(x^{(k)}) - f^*) \cdot \frac{\|\nabla f(x^{(k)})\|^2}{\|\nabla f(x^{(k)})\|^2}$$

更精细地，令 $\delta_k = f(x^{(k)}) - f^*$，通过递推不等式和 $\|x^{(k)} - x^*\|^2$ 的单调递减性，可得 $\delta_k \leq \frac{L\|x^{(0)} - x^*\|^2}{2k}$。$\square$

### 1.4 Linear Convergence for Strongly Convex Functions **[Boyd & Vandenberghe, Ch.9, §9.3.1]**

**Assumption.** $f$ 是 $m$-强凸的（$\nabla^2 f \succeq mI$），$\nabla f$ 是 $L$-Lipschitz。条件数 $\kappa = L/m$。

**Theorem (Linear/Geometric Convergence).** 用固定步长 $t = 1/L$：

$$f(x^{(k)}) - f^* \leq \left(1 - \frac{1}{\kappa}\right)^k \cdot \left(f(x^{(0)}) - f^*\right)$$

即线性收敛（函数值差以几何级数递减），速率 $1 - 1/\kappa$。要达到 $\varepsilon$-精度：

$$k = O\left(\kappa \log \frac{1}{\varepsilon}\right) \text{ iterations}$$

**Proof sketch.** 由强凸性和 Lipschitz 梯度：

$$f(x^{(k+1)}) - f^* \leq f(x^{(k)}) - f^* - \frac{1}{2L}\|\nabla f(x^{(k)})\|^2$$

由强凸性：$\|\nabla f(x)\|^2 \geq 2m(f(x) - f^*)$，代入：

$$\delta_{k+1} \leq \delta_k - \frac{m}{L} \delta_k = \left(1 - \frac{m}{L}\right) \delta_k = \left(1 - \frac{1}{\kappa}\right) \delta_k \quad \square$$

**条件数的影响**：$\kappa$ 大（病态问题）$\implies$ 收敛慢。例如 $\kappa = 10^4$ 时需要约 $10^4 \ln(1/\varepsilon)$ 次迭代。这促使了加速方法（Nesterov）和二阶方法（Newton）的发展。

---

## 2. Accelerated Gradient Methods (Nesterov)

### 2.1 Nesterov's Accelerated Gradient Descent

$$y^{(k)} = x^{(k)} + \frac{k-1}{k+2}(x^{(k)} - x^{(k-1)})$$

$$x^{(k+1)} = y^{(k)} - \frac{1}{L} \nabla f(y^{(k)})$$

### Theorem 2.2 (Nesterov Acceleration) **[Nesterov 1983; context from Boyd & Vandenberghe, Ch.9]**

对 $L$-光滑凸函数：

$$f(x^{(k)}) - f^* \leq \frac{2L \|x^{(0)} - x^*\|^2}{(k+1)^2} = O(1/k^2)$$

收敛速率从 $O(1/k)$ 提升到 $O(1/k^2)$，达到了一阶方法的**理论下界**（Nemirovsky & Yudin 1983）。

对 $m$-强凸 + $L$-光滑：

$$f(x^{(k)}) - f^* \leq O\left(\left(1 - \frac{1}{\sqrt{\kappa}}\right)^k\right)$$

迭代复杂度从 $O(\kappa \log(1/\varepsilon))$ 降到 $O(\sqrt{\kappa} \log(1/\varepsilon))$，二次根号加速。

---

## 3. Newton's Method

### 3.1 Newton Step **[Boyd & Vandenberghe, Ch.9, §9.5]**

$$\Delta x_{\text{nt}} = -[\nabla^2 f(x)]^{-1} \nabla f(x)$$

Newton 迭代：$x^{(k+1)} = x^{(k)} + t_k \Delta x_{\text{nt}}$，其中 $t_k$ 由 backtracking 线搜索确定。

**Newton 步的几何解释**：在 $x^{(k)}$ 处用二次 Taylor 展开近似 $f$：

$$\hat{f}(x) = f(x^{(k)}) + \nabla f(x^{(k)})^\top (x - x^{(k)}) + \frac{1}{2}(x - x^{(k)})^\top \nabla^2 f(x^{(k)}) (x - x^{(k)})$$

$\hat{f}$ 的最小点恰好是 $x^{(k)} + \Delta x_{\text{nt}}$。

### 3.2 Newton Decrement **[Boyd & Vandenberghe, Ch.9, §9.5.2]**

**Newton 递减量**定义为：

$$\lambda(x) = \left(\nabla f(x)^\top [\nabla^2 f(x)]^{-1} \nabla f(x)\right)^{1/2}$$

性质：
- $f(x) - \inf_y \hat{f}(y) = \frac{1}{2}\lambda(x)^2$（二次近似的目标下降量）
- $\lambda(x)$ 是仿射不变的（不依赖于坐标选择）
- 停止准则：$\lambda(x)^2 / 2 \leq \varepsilon$ 时 $f(x) - f^* \lesssim \varepsilon$

### Theorem 3.3 (Newton's Method Convergence) **[Boyd & Vandenberghe, Ch.9, §9.5.3]**

Newton 法（带 backtracking 线搜索）的收敛分为两个阶段：

**Phase I（阻尼 Newton 阶段）**：当 $\|\nabla^2 f(x)^{-1/2} \nabla f(x)\|$ 较大时，每步目标函数至少下降常数 $\gamma > 0$：

$$f(x^{(k+1)}) \leq f(x^{(k)}) - \gamma$$

**Phase II（二次收敛阶段）**：当足够接近最优解时，步长 $t_k = 1$，收敛变为**二次的**：

$$\|\nabla^2 f(x^{(k+1)})^{-1/2} \nabla f(x^{(k+1)})\| \leq C \cdot \|\nabla^2 f(x^{(k)})^{-1/2} \nabla f(x^{(k)})\|^2$$

**二次收敛的含义**：有效数字在每次迭代中翻倍。例如，$10^{-3}$ 精度 $\to$ $10^{-6}$ $\to$ $10^{-12}$。因此 Phase II 通常只需 5-6 次迭代就能达到机器精度。

**总迭代次数**：$O\left(\frac{f(x^{(0)}) - f^*}{\gamma}\right) + O\left(\log\log \frac{1}{\varepsilon}\right)$

Phase I 的次数与初始点质量有关，Phase II 的次数与精度的 $\log\log$ 成正比（极少）。

### 3.4 Comparison: Gradient Descent vs Newton

| 性质 | 梯度下降 | Newton 法 |
|------|---------|----------|
| 每步复杂度 | $O(n)$ | $O(n^3)$（求解线性系统） |
| 收敛速率 | 线性 $O(\kappa \log(1/\varepsilon))$ | 二次（近最优点） |
| 仿射不变 | 否（依赖坐标） | 是 |
| 需要 Hessian | 否 | 是 |
| 适用规模 | 大规模 ($n \sim 10^6$+) | 中等规模 ($n \sim 10^3$) |

### 3.5 Quasi-Newton Methods (BFGS) **[Related to Boyd & Vandenberghe, Ch.9]**

当 Hessian 计算或存储不可行时，拟 Newton 法用秩-2 更新近似 Hessian 的逆：

$$H_{k+1} = \left(I - \frac{s_k y_k^\top}{y_k^\top s_k}\right) H_k \left(I - \frac{y_k s_k^\top}{y_k^\top s_k}\right) + \frac{s_k s_k^\top}{y_k^\top s_k}$$

其中 $s_k = x^{(k+1)} - x^{(k)}$，$y_k = \nabla f(x^{(k+1)}) - \nabla f(x^{(k)})$。

BFGS 收敛速率是超线性的（优于梯度下降，但不如完整 Newton）。L-BFGS 是有限内存版本，只存储最近 $m$ 步的 $(s_k, y_k)$ 对，适合大规模优化。

---

## 4. Interior Point Methods **[Boyd & Vandenberghe, Ch.11]**

### 4.1 Barrier Method **[Boyd & Vandenberghe, Ch.11, §11.2]**

考虑凸优化问题：$\min f_0(x)$, s.t. $f_i(x) \leq 0$, $Ax = b$。

**对数障碍函数**：

$$\phi(x) = -\sum_{i=1}^{m} \log(-f_i(x))$$

当 $x$ 接近可行域边界（某个 $f_i(x) \to 0^-$）时，$\phi(x) \to +\infty$，形成"障碍"。

**中心路径（Central Path）**：对参数 $t > 0$，定义

$$x^*(t) = \arg\min_x \left\{ t \cdot f_0(x) + \phi(x) \right\}, \quad \text{s.t.} \; Ax = b$$

当 $t \to \infty$ 时，$x^*(t) \to x^*$（原问题最优解）。中心路径上的每一点的 KKT 条件给出：

$$t \nabla f_0(x) + \sum_{i=1}^{m} \frac{1}{-f_i(x)} \nabla f_i(x) + A^\top \nu = 0$$

对比标准 KKT 的驻点条件，等价于令 $\lambda_i = \frac{1}{-t \cdot f_i(x)}$，这是 KKT 条件的近似（互补松弛 $\lambda_i f_i = -1/t \approx 0$）。

### 4.2 Barrier Method Algorithm **[Boyd & Vandenberghe, Ch.11, §11.3]**

**算法**：

给定严格可行初始点 $x^{(0)}$，参数 $\mu > 1$（通常 $\mu = 10$ 或 $20$），初始 $t := t^{(0)} > 0$。

重复：
1. **Centering step**: 用 Newton 法求解 $x^*(t) = \arg\min \{t f_0(x) + \phi(x)\}$
2. **更新**: $x := x^*(t)$
3. **停止准则**: 如果 $m/t \leq \varepsilon$，停止（$m/t$ 是对偶间隙的上界）
4. **增大 $t$**: $t := \mu t$

### Theorem 4.3 (Barrier Method Convergence) **[Boyd & Vandenberghe, Ch.11, §11.3.2]**

中心路径上的点 $x^*(t)$ 满足：

$$f_0(x^*(t)) - p^* \leq \frac{m}{t}$$

因此：
- 外层迭代（centering steps）次数：$\left\lceil \frac{\log(m / (t^{(0)} \varepsilon))}{\log \mu} \right\rceil + 1$
- 每次 centering step 内：Newton 法的迭代次数（通常 $O(\sqrt{m})$ 步，或因为热启动而很少）

**总复杂度**（LP/SOCP/SDP 的内点法）：

$$O\left(\sqrt{m} \cdot \log \frac{m}{\varepsilon}\right) \text{ Newton steps}$$

每个 Newton 步的代价取决于问题结构（LP: $O(n^2 m)$，SDP: $O(n^3 m)$）。

### 4.4 Primal-Dual Interior Point Method **[Boyd & Vandenberghe, Ch.11, §11.7]**

比纯障碍法更高效，直接同时求解原始和对偶变量。核心思想：将 KKT 条件中的互补松弛 $\lambda_i f_i(x) = 0$ 替换为 $\lambda_i (-f_i(x)) = 1/t$，然后用 Newton 法同时求解 $(x, \lambda, \nu)$。

**修正的 KKT 系统**（$r_t = 0$）：

$$r_t(x, \lambda, \nu) = \begin{pmatrix} \nabla f_0(x) + Df(x)^\top \lambda + A^\top \nu \\ -\text{diag}(\lambda) f(x) - (1/t) \mathbf{1} \\ Ax - b \end{pmatrix} = 0$$

Newton 方向通过求解线性系统得到。这就是商用求解器（MOSEK, Gurobi, CPLEX）的核心算法。

### 4.5 Complexity Summary for Standard Problems

| 问题类型 | 内点法 Newton 步数 | 每步代价 | 总复杂度 |
|---------|-------------------|---------|---------|
| LP ($n$ vars, $m$ constraints) | $O(\sqrt{m} \log(m/\varepsilon))$ | $O(n^2 m)$ | $O(n^2 m^{1.5} \log(m/\varepsilon))$ |
| QP | $O(\sqrt{m} \log(m/\varepsilon))$ | $O(n^2 m)$ | 类似 LP |
| SOCP ($m$ cones) | $O(\sqrt{m} \log(m/\varepsilon))$ | $O(n^2 m)$ | 类似 LP |
| SDP ($n \times n$ matrix, $m$ constraints) | $O(\sqrt{m} \log(m/\varepsilon))$ | $O(n^3 m + n^2 m^2)$ | 更高 |

---

## 5. Stochastic Gradient Descent (SGD) and ML Optimizers

### 5.1 SGD **[Not in Boyd directly; standard ML extension]**

对于有限和目标 $f(x) = \frac{1}{N} \sum_{i=1}^N f_i(x)$：

$$x^{(k+1)} = x^{(k)} - t_k \nabla f_{i_k}(x^{(k)})$$

其中 $i_k$ 是随机采样的索引。

**收敛**（凸情况，递减步长 $t_k = O(1/\sqrt{k})$）：

$$\mathbb{E}[f(\bar{x}^{(K)})] - f^* = O\left(\frac{1}{\sqrt{K}}\right)$$

其中 $\bar{x}^{(K)}$ 是迭代的某种平均。比确定性 GD 慢，但每步代价从 $O(N)$ 降到 $O(1)$。

### 5.2 SGD with Momentum

$$v^{(k+1)} = \beta v^{(k)} + \nabla f_{i_k}(x^{(k)})$$

$$x^{(k+1)} = x^{(k)} - t_k v^{(k+1)}$$

动量（$\beta \approx 0.9$）通过累积梯度历史来加速收敛并减少振荡。

### 5.3 Adam Optimizer **[Kingma & Ba, ICLR 2015]**

Adam 结合了动量和自适应学习率。超参数：学习率 $\alpha$，衰减率 $\beta_1, \beta_2$，稳定常数 $\varepsilon$。

$$m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t \quad \text{(一阶矩估计)}$$

$$v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2 \quad \text{(二阶矩估计)}$$

$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t} \quad \text{(偏差校正)}$$

$$x_{t+1} = x_t - \alpha \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \varepsilon}$$

**默认超参数**：$\alpha = 0.001$，$\beta_1 = 0.9$，$\beta_2 = 0.999$，$\varepsilon = 10^{-8}$。

**偏差校正的推导**：初始化 $m_0 = 0$，展开递推：

$$m_t = (1-\beta_1) \sum_{i=1}^{t} \beta_1^{t-i} g_i$$

$$\mathbb{E}[m_t] = (1-\beta_1) \sum_{i=1}^{t} \beta_1^{t-i} \mathbb{E}[g_i] = (1-\beta_1^t) \mathbb{E}[g]$$

因此 $\mathbb{E}[\hat{m}_t] = \mathbb{E}[g]$，校正了零初始化导致的偏差。

**AdamW**（解耦权重衰减）：将 L2 正则化改为直接的权重衰减 $x_t \to (1 - \lambda)x_t$，避免自适应学习率对正则化的影响。这是当前 LLM 训练的标准优化器。

### 5.4 Connection to Convex Theory

虽然神经网络训练是非凸问题，凸优化理论仍然提供关键 insights：

1. **学习率选择**：$t \leq 1/L$ 的梯度下降收敛条件启发了学习率调度策略
2. **条件数**：Batch Normalization、预条件等技巧本质上在改善"有效条件数"
3. **强凸性与正则化**：L2 正则化（权重衰减）使问题更接近强凸，改善收敛
4. **对偶性**：GAN 训练是 minimax 问题，对偶理论提供稳定性分析框架
5. **KKT 条件**：约束优化（如 RLHF 中的 KL 约束）需要 Lagrangian 方法

---

## 6. Optimization in Quantum Computing

### 6.1 VQE/QAOA Parameter Optimization

变分量子算法中的参数优化 $\min_{\theta} \langle \psi(\theta) | H | \psi(\theta) \rangle$ 是**非凸优化**，面临：

- **Barren plateaus**：梯度指数级消失，类似于深度网络的梯度消失
- **Local minima**：参数空间中存在大量局部极小
- **Noise**：量子测量的统计噪声使梯度估计有方差

常用优化器：COBYLA（无梯度）、SPSA（随机扰动）、Adam（参数偏移梯度 + Adam）。

### 6.2 SDP Solvers for Quantum Problems

量子信息中的 SDP（如态辨别、纠缠检测、信道容量）通常用内点法求解：

- **CVXPY + SCS/MOSEK**：Python 接口，适合中等规模
- **大规模 SDP**：first-order methods（如 ADMM）或 Burer-Monteiro 低秩方法

SDP 的内点法复杂度 $O(n^{3.5})$ 限制了可处理的量子系统大小（约 $n \sim 10^3$ 量级的密度矩阵维度）。

---

## 7. Equality Constrained Optimization (from Boyd Ch.10)

### 7.1 Newton's Method for Equality Constraints **[Boyd & Vandenberghe, Ch.10, §10.2]**

对于等式约束优化 $\min f_0(x)$, s.t. $Ax = b$：

**Newton 步**通过求解 KKT 系统获得：

$$\begin{pmatrix} \nabla^2 f_0(x) & A^\top \\ A & 0 \end{pmatrix} \begin{pmatrix} \Delta x_{\text{nt}} \\ w \end{pmatrix} = \begin{pmatrix} -\nabla f_0(x) \\ 0 \end{pmatrix}$$

> Boyd 原文 (Ch.10): "The Newton step for the equality constrained problem is obtained by minimizing a quadratic approximation of $f_0$ subject to the linearized equality constraints."

这个线性系统的求解是 Newton 法的核心计算瓶颈。

### 7.2 Infeasible Start Newton Method **[Boyd & Vandenberghe, Ch.10, §10.3]**

当初始点不满足 $Ax = b$ 时，修正的 Newton 方向同时减小目标函数和约束违反量。KKT 系统变为：

$$\begin{pmatrix} \nabla^2 f_0(x) & A^\top \\ A & 0 \end{pmatrix} \begin{pmatrix} \Delta x \\ \nu \end{pmatrix} = \begin{pmatrix} -\nabla f_0(x) \\ b - Ax \end{pmatrix}$$

---

## 8. Interior Point Methods — Detailed Analysis (from Boyd Ch.11)

### 8.1 Central Path and KKT Connection **[Boyd & Vandenberghe, Ch.11, §11.2]**

> Boyd 原文 (Ch.11, p.565): 中心路径上每一点的 KKT 条件给出 "$t \nabla f_0(x) + \sum_{i=1}^m \frac{1}{-f_i(x)} \nabla f_i(x) + A^\top \nu = 0$"。

等价于令 $\lambda_i = \frac{1}{-t \cdot f_i(x)}$，此时互补松弛条件变为 $\lambda_i (-f_i(x)) = 1/t$，在 $t \to \infty$ 时趋近于精确互补松弛 $\lambda_i f_i(x) = 0$。

**代理对偶间隙**：中心路径上点 $x^*(t)$ 的代理对偶间隙为 $m/t$，这给出停止准则。

### 8.2 Self-Concordant Barriers **[Boyd & Vandenberghe, Ch.11, §11.5]**

内点法的收敛分析依赖于自协调障碍函数理论（Nesterov-Nemirovski）。

**定义**：$f$ 是自协调的，如果 $|f'''(x)| \leq 2 f''(x)^{3/2}$ 对所有 $x \in \text{dom}(f)$。

$-\log(-t)$ 是自协调的。对数障碍 $\phi(x) = -\sum \log(-f_i(x))$ 的自协调性保证了 Newton 法在内点法的 centering step 中的二次收敛，且复杂度为 $O(\sqrt{m} \log(m/\varepsilon))$ 个 Newton 步。

---

## 9. Proximal Gradient Methods **[Not in Boyd directly; modern extension]**

对于复合目标 $\min f(x) + g(x)$（$f$ 光滑凸，$g$ 凸但可能不光滑，如 $\ell_1$ 范数）：

$$x^{(k+1)} = \text{prox}_{t_k g}\left(x^{(k)} - t_k \nabla f(x^{(k)})\right)$$

其中 $\text{prox}_{tg}(v) = \arg\min_x \left\{g(x) + \frac{1}{2t}\|x - v\|^2\right\}$。

**ISTA** (Iterative Shrinkage-Thresholding): 当 $g = \lambda\|x\|_1$ 时，proximal 算符退化为软阈值。

**FISTA** (Fast ISTA): 加入 Nesterov 加速，收敛率从 $O(1/k)$ 提升到 $O(1/k^2)$。

---

> **See also**: [convex_optimization_basics.md] (凸函数性质, 对偶锥) | [duality_kkt.md] (KKT 条件, 替代定理) | [relaxation_methods.md] (SDP 求解) | [../key_formulas.md]

> **Primary Reference**: Boyd & Vandenberghe, *Convex Optimization*, Cambridge University Press (2004), Ch. 9, 10, 11. | Nesterov, *Introductory Lectures on Convex Optimization* (2004). | Kingma & Ba, "Adam", ICLR (2015).
