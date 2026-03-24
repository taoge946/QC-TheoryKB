# Reinforcement Learning Theory for Combinatorial Optimization

> **Tags**: `reinforcement-learning`, `policy-gradient`, `ppo`, `reinforce`, `combinatorial-optimization`

## Statement

推导强化学习中策略梯度方法的核心理论，包括 REINFORCE 算法、基线减法的方差缩减、PPO 的 clipped surrogate 目标，以及它们在组合优化中的应用联系。

## Prerequisites

- 概率论：期望、方差、重要性采样
- 马尔可夫决策过程 (MDP) 基本定义
- 随机梯度优化
- 对数导数技巧 (log-derivative trick)

---

## Part 1: Policy Gradient Theorem (REINFORCE)

### 1.1 MDP 设置

- 状态 $s \in \mathcal{S}$，动作 $a \in \mathcal{A}$
- 策略 $\pi_\theta(a|s)$：参数化的概率策略
- 轨迹 $\tau = (s_0, a_0, r_0, s_1, a_1, r_1, \ldots)$
- 回报 $R(\tau) = \sum_{t=0}^{T} \gamma^t r_t$

**目标**：最大化期望回报

$$J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)]$$

### 1.2 策略梯度定理

**定理** (Williams, 1992; Sutton et al., 2000)：

$$\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}\left[R(\tau) \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t|s_t)\right]$$

**推导**：

轨迹的概率为：

$$p_\theta(\tau) = p(s_0) \prod_{t=0}^{T} \pi_\theta(a_t|s_t)\, p(s_{t+1}|s_t, a_t)$$

$$\nabla_\theta J(\theta) = \nabla_\theta \int p_\theta(\tau) R(\tau)\, d\tau$$

**Log-derivative trick**（对数导数技巧）：

$$\nabla_\theta p_\theta(\tau) = p_\theta(\tau) \nabla_\theta \log p_\theta(\tau)$$

因此：

$$\nabla_\theta J(\theta) = \int p_\theta(\tau) R(\tau) \nabla_\theta \log p_\theta(\tau)\, d\tau = \mathbb{E}_{\tau \sim \pi_\theta}\left[R(\tau) \nabla_\theta \log p_\theta(\tau)\right]$$

展开 $\log p_\theta(\tau)$：

$$\log p_\theta(\tau) = \log p(s_0) + \sum_{t=0}^{T}\left[\log \pi_\theta(a_t|s_t) + \log p(s_{t+1}|s_t, a_t)\right]$$

只有 $\log \pi_\theta(a_t|s_t)$ 依赖于 $\theta$，因此：

$$\boxed{\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}\left[R(\tau) \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t|s_t)\right]}$$

$\blacksquare$

### 1.3 REINFORCE 算法

```
Algorithm: REINFORCE (Williams, 1992)
Input: 可微策略 π_θ(a|s)，学习率 α
Repeat:
    用策略 π_θ 生成轨迹 τ = (s_0, a_0, r_0, ..., s_T, a_T, r_T)
    For t = 0, ..., T:
        G_t ← Σ_{k=t}^{T} γ^{k-t} r_k  (从时间 t 开始的回报)
    θ ← θ + α Σ_{t=0}^{T} G_t ∇_θ log π_θ(a_t|s_t)
Until 收敛
```

**关键性质**：
- 无偏梯度估计
- 方差极高（回报 $R(\tau)$ 的波动直接影响梯度）
- 只需要轨迹采样，不需要环境模型

---

## Part 2: Baseline Subtraction — Variance Reduction

### 2.1 基线不改变期望

**定理**：对于任何不依赖于动作的基线 $b(s)$：

$$\mathbb{E}_{\pi_\theta}\left[b(s_t) \nabla_\theta \log \pi_\theta(a_t|s_t)\right] = 0$$

**证明**：

$$\mathbb{E}_{a \sim \pi_\theta(\cdot|s)}\left[b(s) \nabla_\theta \log \pi_\theta(a|s)\right] = b(s) \sum_a \pi_\theta(a|s) \frac{\nabla_\theta \pi_\theta(a|s)}{\pi_\theta(a|s)}$$

$$= b(s) \sum_a \nabla_\theta \pi_\theta(a|s) = b(s) \nabla_\theta \underbrace{\sum_a \pi_\theta(a|s)}_{= 1} = 0$$

$\blacksquare$

因此，带基线的梯度估计仍然无偏：

$$\nabla_\theta J(\theta) = \mathbb{E}_{\tau}\left[\sum_{t=0}^{T} (G_t - b(s_t)) \nabla_\theta \log \pi_\theta(a_t|s_t)\right]$$

### 2.2 最优基线

最小方差的基线为：

$$b^*(s) = \frac{\mathbb{E}\left[(\nabla_\theta \log \pi)^2 \cdot G_t \,|\, s_t = s\right]}{\mathbb{E}\left[(\nabla_\theta \log \pi)^2 \,|\, s_t = s\right]}$$

实际中常用更简单的近似：$b(s) \approx V^\pi(s)$（状态价值函数）。

### 2.3 优势函数 (Advantage Function)

$$A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)$$

使用优势函数的策略梯度：

$$\nabla_\theta J(\theta) = \mathbb{E}_{\tau}\left[\sum_{t=0}^{T} A^{\pi_\theta}(s_t, a_t) \nabla_\theta \log \pi_\theta(a_t|s_t)\right]$$

**优势**：$A^\pi$ 自动居中（$\mathbb{E}_{a \sim \pi}[A^\pi(s, a)] = 0$），有效降低方差。

### 2.4 广义优势估计 (GAE) **[Schulman et al. 2016]**

$$\hat{A}_t^{\mathrm{GAE}(\gamma, \lambda)} = \sum_{l=0}^{\infty} (\gamma\lambda)^l \delta_{t+l}^V$$

其中 TD 误差 $\delta_t^V = r_t + \gamma V(s_{t+1}) - V(s_t)$。

- $\lambda = 0$：$\hat{A}_t = \delta_t^V$（高偏差、低方差）
- $\lambda = 1$：$\hat{A}_t = \sum_{l=0}^{\infty} \gamma^l \delta_{t+l}^V = G_t - V(s_t)$（低偏差、高方差）
- $\lambda \in (0,1)$：在偏差与方差之间取平衡

---

## Part 3: PPO — Proximal Policy Optimization **[Schulman et al. 2017]**

### 3.1 信赖域动机 **[Schulman et al. 2017, §1-2]**

标准策略梯度的问题：步长过大导致策略急剧变化，性能可能崩溃。

**信赖域策略优化 (TRPO)** 的目标 **[Schulman et al. 2015]**：

$$\max_\theta \; \mathbb{E}_t\left[\frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)} \hat{A}_t\right] \quad \text{s.t.} \quad \mathbb{E}_t\left[D_{\mathrm{KL}}(\pi_{\theta_{\text{old}}}(\cdot|s_t) \| \pi_\theta(\cdot|s_t))\right] \leq \delta$$

TRPO 需要约束优化（共轭梯度 + 线搜索），实现复杂。PPO 用 clipping 替代约束。

### 3.2 重要性采样比 **[Schulman et al. 2017, §3]**

定义概率比：

$$r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)}$$

保守策略迭代 (CPI) 的代理目标：

$$L^{\mathrm{CPI}}(\theta) = \hat{\mathbb{E}}_t\left[r_t(\theta) \hat{A}_t\right]$$

**问题**：没有约束时，$L^{\mathrm{CPI}}$ 允许过大的策略更新。

### 3.3 Clipped Surrogate Objective **[Schulman et al. 2017, §3]**

$$\boxed{L^{\mathrm{CLIP}}(\theta) = \hat{\mathbb{E}}_t\left[\min\left(r_t(\theta) \hat{A}_t, \; \operatorname{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t\right)\right]}$$

**[Schulman et al. 2017, Eq.(7)]**

其中 $\epsilon$ 是超参数（通常 $\epsilon = 0.2$）。

**分析**：

$$\operatorname{clip}(r, 1-\epsilon, 1+\epsilon) = \begin{cases} 1-\epsilon & \text{if } r < 1-\epsilon \\ r & \text{if } 1-\epsilon \leq r \leq 1+\epsilon \\ 1+\epsilon & \text{if } r > 1+\epsilon \end{cases}$$

**两种情况**：

1. **$\hat{A}_t > 0$**（好动作）：$\min(r_t \hat{A}_t, (1+\epsilon)\hat{A}_t)$
   - 限制 $r_t$ 不超过 $1+\epsilon$，防止策略向好动作过度倾斜

2. **$\hat{A}_t < 0$**（坏动作）：$\min(r_t \hat{A}_t, (1-\epsilon)\hat{A}_t)$（注意 $\hat{A}_t < 0$ 时 min 变成限制 $r_t$ 不低于 $1-\epsilon$）
   - 限制 $r_t$ 不低于 $1-\epsilon$，防止策略过度远离坏动作

**直觉**：clip 创建了一个悲观的（保守的）策略改进下界。

### 3.4 完整 PPO 目标 **[Schulman et al. 2017, §4]**

如果共享策略网络和价值网络：

$$L^{\mathrm{CLIP+VF+S}}_t(\theta) = \hat{\mathbb{E}}_t\left[L^{\mathrm{CLIP}}_t(\theta) - c_1 L^{\mathrm{VF}}_t(\theta) + c_2 S[\pi_\theta](s_t)\right]$$

其中：
- $L^{\mathrm{VF}}_t = (V_\theta(s_t) - V_t^{\text{target}})^2$：价值函数损失
- $S[\pi_\theta](s_t)$：策略熵奖励（鼓励探索）
- $c_1 = 0.5$, $c_2 = 0.01$：权重系数

### 3.5 PPO 算法 **[Schulman et al. 2017, Algorithm 1]**

```
Algorithm: PPO, Actor-Critic Style
For iteration = 1, 2, ...:
    For actor = 1, 2, ..., N (parallel):
        用策略 π_{θ_old} 收集 T 步数据
        计算优势估计 Â_1, ..., Â_T (使用 GAE)
    用收集的 NT 个样本上的 L^{CLIP+VF+S} 优化 θ，K epochs
    θ_old ← θ
```

**关键超参数**（原文推荐）**[Schulman et al. 2017, §5]**：
- $\epsilon = 0.2$（clip 范围）
- $K = 3\text{-}15$ epochs per update
- $T = 128\text{-}2048$ steps per actor
- $N = 8\text{-}32$ parallel actors
- 学习率 $3 \times 10^{-4}$，线性衰减

### 3.6 Adaptive KL Penalty 替代方案 **[Schulman et al. 2017, §4]**

另一种 PPO 变体使用自适应 KL 惩罚：

$$L^{\mathrm{KLPEN}}(\theta) = \hat{\mathbb{E}}_t\left[r_t(\theta)\hat{A}_t - \beta\, D_{\mathrm{KL}}(\pi_{\theta_{\text{old}}}(\cdot|s_t) \| \pi_\theta(\cdot|s_t))\right]$$

$\beta$ 根据实际 KL 散度自适应调整：
- 若 $D_{\mathrm{KL}} < d_{\text{targ}}/1.5$：$\beta \leftarrow \beta/2$
- 若 $D_{\mathrm{KL}} > d_{\text{targ}} \times 1.5$：$\beta \leftarrow 2\beta$

实验中 clipped 版本通常优于 KL penalty 版本 **[Schulman et al. 2017, §6]**。

---

## Part 4: Connection to Combinatorial Optimization

### 4.1 REINFORCE for Attention Model **[Kool et al. 2019, based on Bello et al. 2017]**

组合优化问题（如 TSP、VRP）可以建模为序列决策：

- **状态** $s_t$：已选择的节点集合 + 当前节点
- **动作** $a_t$：选择下一个节点
- **策略** $\pi_\theta(a_t|s_t)$：注意力机制（Transformer）输出的概率
- **回报** $R(\tau) = -C(\tau)$：负的路径代价（最小化代价 = 最大化回报）

**损失函数**：

$$\nabla_\theta \mathcal{L}(\theta) = \mathbb{E}_{p_\theta(\boldsymbol{\pi}|\mathbf{x})}\left[(C(\boldsymbol{\pi}) - b(\mathbf{x})) \nabla_\theta \log p_\theta(\boldsymbol{\pi}|\mathbf{x})\right]$$

其中 $C(\boldsymbol{\pi})$ 是解 $\boldsymbol{\pi}$ 的代价，$b(\mathbf{x})$ 是基线。

### 4.2 基线选择对 CO 的影响

| 基线类型 | 方法 | 效果 |
|---|---|---|
| 指数移动平均 | Bello et al. (2017) | 简单但偏差大 |
| Greedy rollout | Kool et al. (2019) | 无偏，效果好 |
| 批内平均 | POMO (Kwon et al., 2020) | 利用对称性，方差更低 |
| Critic 网络 | Actor-Critic | 需要额外网络 |

### 4.3 为什么 REINFORCE 而非 PPO 在 CO 中更常用？

1. **单步决策**：许多 CO 方法将整个解作为一个"轨迹"，不需要多步信赖域
2. **基线足够好**：greedy rollout 基线已经大幅降低方差
3. **简单性**：REINFORCE 实现简单，与 Transformer 架构结合自然
4. **PPO 在某些 CO 问题中也有应用**：特别是需要多步交互的调度问题

### 4.4 REINFORCE 的变体在 CO 中的应用

| 方法 | RL 技术 | CO 问题 | 参考 |
|---|---|---|---|
| Attention Model | REINFORCE + greedy baseline | TSP, CVRP | Kool et al., 2019 |
| POMO | REINFORCE + batch baseline | TSP, CVRP | Kwon et al., 2020 |
| RL4CO | PPO/REINFORCE | 多种 CO | Berto et al., 2023 |
| ECO-DQN | DQN (value-based) | Max-Cut | Barrett et al., 2020 |

---

## Summary

策略梯度方法的发展脉络：

$$\underbrace{\text{REINFORCE}}_{\text{无偏但高方差}} \xrightarrow{\text{基线减法}} \underbrace{R(\tau) - b(s)}_{\text{方差缩减}} \xrightarrow{\text{优势函数}} \underbrace{A^\pi(s,a)}_{\text{自动居中}} \xrightarrow{\text{信赖域}} \underbrace{\text{PPO}}_{\text{稳定更新}}$$

在组合优化中的应用：

$$\text{CO 问题} \xrightarrow{\text{序列决策建模}} \text{MDP} \xrightarrow{\text{Attention 策略}} \pi_\theta \xrightarrow{\text{REINFORCE + baseline}} \text{端到端训练}$$

---

## References

1. Williams, R.J. (1992). Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning. Machine Learning.
2. Sutton, R.S. et al. (2000). Policy Gradient Methods for RL with Function Approximation. NeurIPS.
3. Schulman, J. et al. (2015). Trust Region Policy Optimization (TRPO). ICML.
4. Schulman, J. et al. (2016). High-Dimensional Continuous Control Using GAE. ICLR.
5. Schulman, J. et al. (2017). Proximal Policy Optimization Algorithms. arXiv:1707.06347.
6. Kool, W. et al. (2019). Attention, Learn to Solve Routing Problems! ICLR.
7. Kwon, Y.-D. et al. (2020). POMO: Policy Optimization with Multiple Optima. NeurIPS.
8. Bello, I. et al. (2017). Neural Combinatorial Optimization with Reinforcement Learning. ICLR Workshop.
