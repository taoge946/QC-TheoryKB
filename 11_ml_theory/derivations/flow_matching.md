# Flow Matching: Complete Mathematical Framework

> **Tags**: `flow-matching`, `cnf`, `optimal-transport`, `generative-model`, `cfm`

## Statement

推导 Flow Matching (FM) 和 Conditional Flow Matching (CFM) 的完整数学框架 **[Lipman et al. 2023]**。从连续正则化流 (CNF) 出发，定义流匹配目标，推导条件流匹配等价性，建立一般高斯条件路径的向量场公式，推导最优传输 (OT) 路径作为特例，并与基于得分的扩散模型进行比较。

Flow Matching 是一种新范式，它直接操作概率路径和向量场，无需通过随机微分方程推导，从而打开了扩散路径之外的设计空间。

## Prerequisites

- 连续扩散模型（DDPM/SDE）基础（见 [diffusion_models_math.md](diffusion_models_math.md)）
- 概率密度函数与变量替换公式
- 常微分方程基础
- 高斯分布性质
- 最优传输基本概念（Wasserstein距离）

---

## Part 1: Continuous Normalizing Flows (CNF) 基础

### 1.1 核心对象

两个核心数学对象 **[Lipman et al. 2023, §2]**：

1. **概率密度路径** $p: [0,1] \times \mathbb{R}^d \to \mathbb{R}_{>0}$，时间相关的概率密度函数，$\int p_t(x)\,dx = 1$
2. **时间相关向量场** $v: [0,1] \times \mathbb{R}^d \to \mathbb{R}^d$

### 1.2 流 (Flow)

向量场 $v_t$ 通过 ODE 构造一个时间相关的微分同胚映射，称为**流** $\phi: [0,1] \times \mathbb{R}^d \to \mathbb{R}^d$：

$$\boxed{\frac{d}{dt}\phi_t(x) = v_t(\phi_t(x)), \quad \phi_0(x) = x}$$

### 1.3 推前 (Push-forward) 方程

CNF 通过流 $\phi_t$ 将简单先验 $p_0$（如标准高斯）变换为复杂分布 $p_1$：

$$p_t = [\phi_t]_* p_0$$

其中推前算子定义为（变量替换公式）**[Lipman et al. 2023, Eq.(3)]**：

$$[\phi_t]_* p_0(x) = p_0(\phi_t^{-1}(x))\,\det\left(\frac{\partial \phi_t^{-1}}{\partial x}(x)\right)$$

### 1.4 连续性方程

向量场 $v_t$ **生成**概率密度路径 $p_t$，当且仅当它们满足连续性方程：

$$\frac{\partial}{\partial t} p_t(x) + \mathrm{div}(p_t(x)\, v_t(x)) = 0$$

这是 Flow Matching 理论证明的关键工具。

### 1.5 CNF 的似然计算

给定 $x_1 \in \mathbb{R}^d$，其在 CNF 下的对数似然可以通过瞬时变量替换公式计算：

$$\log p_1(x_1) = \log p_0(\phi_1^{-1}(x_1)) - \int_0^1 \mathrm{div}(v_t(\phi_t(\phi_1^{-1}(x_1))))\,dt$$

这需要 ODE 求解，计算代价高。Flow Matching 的目标是提供无模拟 (simulation-free) 的训练方法。

---

## Part 2: Flow Matching 目标 **[Lipman et al. 2023, §3]**

### 2.1 设定

- $x_1 \sim q(x_1)$：未知数据分布（只有样本访问）
- $p_0(x) = \mathcal{N}(x\,|\,0, I)$：简单先验（标准高斯）
- $p_t$：概率密度路径，$p_0 = \mathcal{N}(0, I)$，$p_1 \approx q$
- $u_t$：生成 $p_t$ 的目标向量场

注意时间约定：$t=0$ 对应噪声，$t=1$ 对应数据（与某些扩散模型文献相反）。

### 2.2 Flow Matching (FM) 目标

$$\boxed{\mathcal{L}_{\mathrm{FM}}(\theta) = \mathbb{E}_{t \sim \mathcal{U}[0,1],\, x \sim p_t(x)} \|v_t(x;\theta) - u_t(x)\|^2}$$

其中 $v_t(x;\theta)$ 是参数化的神经网络向量场。当损失为零时，学到的 CNF 将生成 $p_t(x)$。

**问题**：FM 目标本身不可行，因为：
1. 我们不知道什么是合适的 $p_t$ 和 $u_t$
2. 即使知道 $p_t$，边际向量场 $u_t$ 通常不可解析

---

## Part 3: 从条件路径构造边际路径

### 3.1 条件概率路径

给定数据样本 $x_1$，定义**条件概率路径** $p_t(x|x_1)$ 满足：
- $p_0(x|x_1) = p(x) = \mathcal{N}(x\,|\,0,I)$（$t=0$ 时为先验）
- $p_1(x|x_1) = \mathcal{N}(x\,|\,x_1, \sigma_{\min}^2 I)$（$t=1$ 时集中在 $x_1$ 附近）

### 3.2 边际概率路径

通过对数据分布 $q(x_1)$ 边际化得到 **[Lipman et al. 2023, Eq.(5)]**：

$$\boxed{p_t(x) = \int p_t(x|x_1)\, q(x_1)\, dx_1}$$

特别地，在 $t=1$ 时：

$$p_1(x) = \int p_1(x|x_1)\, q(x_1)\, dx_1 \approx q(x)$$

### 3.3 边际向量场

类似地，从条件向量场构造边际向量场 **[Lipman et al. 2023, Eq.(6)]**：

$$\boxed{u_t(x) = \int u_t(x|x_1)\,\frac{p_t(x|x_1)\, q(x_1)}{p_t(x)}\, dx_1}$$

其中 $u_t(\cdot|x_1)$ 是生成 $p_t(\cdot|x_1)$ 的条件向量场。

### 3.4 Theorem 1：边际向量场生成边际路径 **[Lipman et al. 2023, Theorem 1]**

**定理**：给定条件向量场 $u_t(x|x_1)$ 生成条件概率路径 $p_t(x|x_1)$，对任意分布 $q(x_1)$，边际向量场 $u_t$（公式 (6)）生成边际概率路径 $p_t$（公式 (5)），即 $u_t$ 和 $p_t$ 满足连续性方程。

**证明思路**：

$$\frac{\partial}{\partial t} p_t(x) = \int \frac{\partial}{\partial t} p_t(x|x_1)\, q(x_1)\, dx_1 = -\int \mathrm{div}(u_t(x|x_1)\, p_t(x|x_1))\, q(x_1)\, dx_1$$

$$= -\mathrm{div}\left(\int u_t(x|x_1)\, p_t(x|x_1)\, q(x_1)\, dx_1\right) = -\mathrm{div}(u_t(x)\, p_t(x))$$

最后一步用了 $u_t(x)\, p_t(x) = \int u_t(x|x_1)\, p_t(x|x_1)\, q(x_1)\, dx_1$（即边际向量场的定义）。

---

## Part 4: Conditional Flow Matching (CFM) **[Lipman et al. 2023, §3.2]**

### 4.1 CFM 目标

$$\boxed{\mathcal{L}_{\mathrm{CFM}}(\theta) = \mathbb{E}_{t \sim \mathcal{U}[0,1],\, x_1 \sim q(x_1),\, x \sim p_t(x|x_1)} \|v_t(x;\theta) - u_t(x|x_1)\|^2}$$

与 FM 目标的区别：CFM 从条件路径 $p_t(x|x_1)$ 采样，回归条件向量场 $u_t(x|x_1)$，而非边际量。

**优势**：只要能高效从 $p_t(x|x_1)$ 采样并计算 $u_t(x|x_1)$，CFM 就是可行的。条件量仅依赖单个数据样本，通常有解析表达式。

### 4.2 Theorem 2：FM 与 CFM 梯度等价 **[Lipman et al. 2023, Theorem 2]**

**定理**：假设 $p_t(x) > 0$ 对所有 $x \in \mathbb{R}^d$ 和 $t \in [0,1]$ 成立，则 $\mathcal{L}_{\mathrm{CFM}}$ 和 $\mathcal{L}_{\mathrm{FM}}$ 相差一个与 $\theta$ 无关的常数，因此：

$$\boxed{\nabla_\theta \mathcal{L}_{\mathrm{FM}}(\theta) = \nabla_\theta \mathcal{L}_{\mathrm{CFM}}(\theta)}$$

**证明**：

展开 $\mathcal{L}_{\mathrm{CFM}}$：

$$\mathcal{L}_{\mathrm{CFM}} = \mathbb{E}_{t, q(x_1), p_t(x|x_1)}\left[\|v_t(x)\|^2 - 2\langle v_t(x), u_t(x|x_1)\rangle + \|u_t(x|x_1)\|^2\right]$$

第一项：$\mathbb{E}_{q(x_1), p_t(x|x_1)}[\|v_t(x)\|^2] = \mathbb{E}_{p_t(x)}[\|v_t(x)\|^2]$（因为 $\int p_t(x|x_1) q(x_1) dx_1 = p_t(x)$）

第二项交叉项：

$$\mathbb{E}_{q(x_1), p_t(x|x_1)}[\langle v_t(x), u_t(x|x_1)\rangle] = \int \langle v_t(x), u_t(x|x_1)\rangle p_t(x|x_1) q(x_1)\, dx_1\, dx$$

$$= \int \langle v_t(x), \underbrace{\int u_t(x|x_1) \frac{p_t(x|x_1) q(x_1)}{p_t(x)} dx_1}_{= u_t(x)}\rangle p_t(x)\, dx = \mathbb{E}_{p_t(x)}[\langle v_t(x), u_t(x)\rangle]$$

第三项 $\mathbb{E}[\|u_t(x|x_1)\|^2]$ 不依赖 $\theta$。

因此 $\mathcal{L}_{\mathrm{CFM}} = \mathbb{E}_{t, p_t(x)}[\|v_t(x)\|^2 - 2\langle v_t(x), u_t(x)\rangle] + C = \mathcal{L}_{\mathrm{FM}} + C'$，其中 $C, C'$ 不含 $\theta$。

---

## Part 5: 一般高斯条件路径 **[Lipman et al. 2023, §4]**

### 5.1 高斯条件路径参数化

考虑如下形式的条件概率路径 **[Lipman et al. 2023, Eq.(8)]**：

$$p_t(x|x_1) = \mathcal{N}(x\,|\,\mu_t(x_1),\; \sigma_t(x_1)^2\, I)$$

边界条件：
- $\mu_0(x_1) = 0$，$\sigma_0(x_1) = 1$（$t=0$ 时所有路径汇聚到标准高斯）
- $\mu_1(x_1) = x_1$，$\sigma_1(x_1) = \sigma_{\min}$（$t=1$ 时集中在数据点）

### 5.2 条件流映射

对应的条件流 $\psi_t$（仿射变换）**[Lipman et al. 2023, Eq.(9)]**：

$$\psi_t(x) = \sigma_t(x_1)\, x + \mu_t(x_1)$$

当 $x \sim \mathcal{N}(0, I)$ 时，$\psi_t(x) \sim \mathcal{N}(\mu_t(x_1), \sigma_t(x_1)^2 I) = p_t(\cdot|x_1)$。即 $[\psi_t]_* p_0 = p_t(\cdot|x_1)$。

### 5.3 Theorem 3：条件向量场的闭式公式 **[Lipman et al. 2023, Theorem 3]**

**定理**：设 $p_t(x|x_1)$ 是上述高斯条件路径，$\psi_t$ 是对应流映射，则 $\psi_t$ 的唯一生成向量场为：

$$\boxed{u_t(x|x_1) = \frac{\sigma_t'(x_1)}{\sigma_t(x_1)}(x - \mu_t(x_1)) + \mu_t'(x_1)}$$

其中 $f' = \frac{d}{dt}f$ 表示对时间的导数。

**证明**：

由 $\psi_t(x) = \sigma_t x + \mu_t$（省略对 $x_1$ 的依赖），有

$$\frac{d}{dt}\psi_t(x) = \sigma_t' x + \mu_t'$$

由 ODE 定义 $\frac{d}{dt}\psi_t(x) = u_t(\psi_t(x)|x_1)$，需要将 $x$ 用 $\psi_t(x)$ 表示：

$$x = \frac{\psi_t(x) - \mu_t}{\sigma_t}$$

代入：

$$u_t(\psi_t(x)|x_1) = \sigma_t' \cdot \frac{\psi_t(x) - \mu_t}{\sigma_t} + \mu_t' = \frac{\sigma_t'}{\sigma_t}(\psi_t(x) - \mu_t) + \mu_t'$$

令 $y = \psi_t(x)$，得到 $u_t(y|x_1) = \frac{\sigma_t'}{\sigma_t}(y - \mu_t) + \mu_t'$，即所证公式。

### 5.4 CFM 损失的实用形式 **[Lipman et al. 2023, Eq.(10)]**

利用重参数化 $x = \psi_t(x_0)$，其中 $x_0 \sim p_0 = \mathcal{N}(0, I)$：

$$\mathcal{L}_{\mathrm{CFM}}(\theta) = \mathbb{E}_{t, q(x_1), p(x_0)} \left\|v_t(\psi_t(x_0);\theta) - \frac{d}{dt}\psi_t(x_0)\right\|^2$$

训练步骤：
1. 采样 $t \sim \mathcal{U}[0,1]$，$x_0 \sim \mathcal{N}(0, I)$，$x_1 \sim q(x_1)$（数据集）
2. 计算 $x_t = \psi_t(x_0) = \sigma_t x_0 + \mu_t$
3. 计算目标 $\dot{\psi}_t(x_0) = \sigma_t' x_0 + \mu_t'$
4. 最小化 $\|v_t(x_t;\theta) - \dot{\psi}_t(x_0)\|^2$

---

## Part 6: 特殊实例

### 6.1 实例 I：VP 扩散条件向量场 **[Lipman et al. 2023, §4.1]**

对 Variance Preserving (VP) 扩散路径（时间反转，noise→data）：

$$\mu_t(x_1) = \alpha_{1-t}\, x_1, \quad \sigma_t(x_1) = \sqrt{1 - \alpha_{1-t}^2}$$

其中 $\alpha_t = e^{-\frac{1}{2}T(t)}$，$T(t) = \int_0^t \beta(s)\,ds$。

代入 Theorem 3 **[Lipman et al. 2023, Eq.(11)]**：

$$u_t(x|x_1) = \frac{\alpha'_{1-t}}{1-\alpha_{1-t}^2}(\alpha_{1-t}\, x - x_1) = -\frac{T'(1-t)}{2}\left[\frac{e^{-T(1-t)}x - e^{-\frac{1}{2}T(1-t)}x_1}{1-e^{-T(1-t)}}\right]$$

此向量场与 Song et al. (2021) 的概率流 ODE 中的向量场一致。

### 6.2 实例 I'：VE 扩散条件向量场

对 Variance Exploding (VE) 路径：$\mu_t(x_1) = x_1$，$\sigma_t(x_1) = \sigma_{1-t}$。

代入 Theorem 3 **[Lipman et al. 2023, Eq.(10 applied to VE)]**：

$$u_t(x|x_1) = -\frac{\sigma'_{1-t}}{\sigma_{1-t}}(x - x_1)$$

### 6.3 实例 II：最优传输 (OT) 条件向量场 **[Lipman et al. 2023, §4.1, Example II]**

选择均值和标准差随时间**线性变化**：

$$\boxed{\mu_t(x_1) = t\, x_1, \quad \sigma_t(x_1) = 1 - (1-\sigma_{\min})t}$$

代入 Theorem 3 **[Lipman et al. 2023, Eq.(12)]**：

$$\boxed{u_t(x|x_1) = \frac{x_1 - (1-\sigma_{\min})x}{1-(1-\sigma_{\min})t}}$$

对应的条件流 **[Lipman et al. 2023, Eq.(13)]**：

$$\psi_t(x) = (1-(1-\sigma_{\min})t)\, x + t\, x_1$$

CFM 损失简化为 **[Lipman et al. 2023, Eq.(14)]**：

$$\boxed{\mathcal{L}_{\mathrm{CFM}}^{\mathrm{OT}}(\theta) = \mathbb{E}_{t, q(x_1), p(x_0)} \left\|v_t(\psi_t(x_0);\theta) - (x_1 - (1-\sigma_{\min})x_0)\right\|^2}$$

---

## Part 7: 最优传输的连接

### 7.1 OT 位移映射

条件流 $\psi_t(x) = (1-t)x + t\psi(x)$（当 $\sigma_{\min} \to 0$）恰好是两个高斯 $p_0(x|x_1) = \mathcal{N}(0, I)$ 和 $p_1(x|x_1) = \delta(x - x_1)$ 之间的 Wasserstein-2 **OT 位移映射** **[McCann 1997, Definition 1.1, Example 1.7]**。

### 7.2 OT 路径 vs 扩散路径的比较

| 性质 | 扩散路径 | OT 路径 |
|---|---|---|
| 轨迹形状 | 弯曲（可能"超调"后回退） | **直线**（常速度常方向） |
| 向量场复杂度 | 方向和大小随时间变化 | **方向恒定**（$u_t = g(t)\cdot h(x|x_1)$） |
| 时间定义域 | 需要截断（$t < 1-\epsilon$） | 全 $[0,1]$ 区间定义良好 |
| ODE 求解 | 需要较多步数 | 较少步数（直线容易积分） |
| 训练稳定性 | 需要损失加权 | 均匀 $L_2$ 损失即可 |

### 7.3 注意事项

条件流是最优的（条件高斯之间的 OT），但这**不意味着边际向量场也是 OT 最优的**。不过，边际向量场仍然相对简单，因为它是简单条件向量场的加权平均。

---

## Part 8: 与基于得分的扩散模型的比较

### 8.1 三种训练范式

| 方法 | 回归目标 | 损失函数 |
|---|---|---|
| **DDPM** (Ho et al. 2020) | 噪声 $\epsilon$ | $\|\epsilon_\theta(x_t, t) - \epsilon\|^2$ |
| **DSM** (Song et al. 2021) | 得分 $\nabla_x \log p_t(x)$ | $\|s_\theta(x_t, t) - \nabla_{x_t}\log p_t(x_t|x_0)\|^2$ |
| **CFM** (Lipman et al. 2023) | 向量场 $u_t(x)$ | $\|v_\theta(x_t, t) - u_t(x_t|x_1)\|^2$ |

### 8.2 等价关系

对于VP扩散路径，三者在最优解处等价：

$$\nabla_x \log p_t(x|x_1) = -\frac{x - \alpha_t x_1}{1 - \alpha_t^2}$$

$$u_t(x|x_1) = \frac{\alpha'_t}{1-\alpha_t^2}(\alpha_t x - x_1) = -\frac{1}{2}\beta_t\left[\frac{x + \nabla_x\log p_t(x|x_1)}{1}\right] \cdot (\text{适当缩放})$$

即 CFM 目标在扩散路径上等价于 DSM/DDPM 目标（差一个不依赖于 $\theta$ 的项）。

### 8.3 CFM 的优势

1. **一般性**：适用于任意高斯条件路径，不限于扩散过程
2. **稳定性**：不需要损失加权（$\lambda(t)$），直接用均匀 $L_2$ 损失
3. **灵活性**：可以使用 OT 路径等非扩散路径，获得更快训练和采样
4. **简洁性**：直接定义概率路径，无需推导随机过程

---

## Part 9: 训练与采样算法

### 9.1 CFM 训练算法

```
输入：数据分布 q(x_1)，选定的 mu_t, sigma_t
重复：
  1. 采样 t ~ U[0,1], x_0 ~ N(0,I), x_1 ~ q(x_1)
  2. 计算 x_t = sigma_t * x_0 + mu_t        # 条件流
  3. 计算 target = sigma_t' * x_0 + mu_t'    # 流的时间导数
  4. 最小化 ||v_theta(x_t, t) - target||^2
直到收敛
```

对于 OT 路径（$\mu_t = t x_1$，$\sigma_t = 1-(1-\sigma_{\min})t$），步骤简化为：
- $x_t = (1-(1-\sigma_{\min})t) x_0 + t x_1$
- target $= x_1 - (1-\sigma_{\min}) x_0$

### 9.2 CNF 采样算法

```
输入：训练好的 v_theta, ODE solver
1. 采样 x_0 ~ N(0,I)
2. 求解 ODE: dx/dt = v_theta(x, t), x(0) = x_0, t: 0 -> 1
3. 返回 x_1 = x(1)
```

可用任意 ODE solver（Euler, RK45, Dopri5 等），自适应步长 solver 可根据 VF 复杂度自动调整步数。

---

## Summary

Flow Matching 的数学核心：

1. **CNF 基础**：向量场 → 流 → 推前方程 → 概率路径
2. **FM 目标**：回归目标向量场（不可行）
3. **边际化构造**：条件路径 → 边际路径，条件 VF → 边际 VF（Theorem 1）
4. **CFM 等价**：$\nabla_\theta \mathcal{L}_{\mathrm{FM}} = \nabla_\theta \mathcal{L}_{\mathrm{CFM}}$，可行的训练目标（Theorem 2）
5. **高斯条件 VF**：$u_t(x|x_1) = \frac{\sigma'_t}{\sigma_t}(x-\mu_t) + \mu_t'$（Theorem 3）
6. **特例**：扩散路径（VE/VP）是高斯路径的特殊选择；OT 路径产生直线轨迹
7. **与扩散的关系**：CFM 在扩散路径上等价于 DSM，但允许使用更好的 OT 路径

---

## References

1. Lipman, Y., Chen, R.T.Q., Ben-Hamu, H., Nickel, M., & Le, M. (2023). Flow Matching for Generative Modeling. ICLR 2023.
2. Chen, R.T.Q., Rubanova, Y., Bettencourt, J., & Duvenaud, D. (2018). Neural Ordinary Differential Equations. NeurIPS 2018.
3. Song, Y., Sohl-Dickstein, J., Kingma, D.P., Kumar, A., Ermon, S., & Poole, B. (2021). Score-Based Generative Modeling through Stochastic Differential Equations. ICLR 2021.
4. Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. NeurIPS 2020.
5. McCann, R.J. (1997). A Convexity Principle for Interacting Gases. Advances in Mathematics.
6. Liu, X., Gong, C., & Liu, Q. (2022). Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow. ICLR 2023.
7. Albergo, M.S. & Vanden-Eijnden, E. (2022). Building Normalizing Flows with Stochastic Interpolants. ICLR 2023.
