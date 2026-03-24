# 量子自然梯度推导

> Quantum Natural Gradient: Complete Theory
> 涵盖经典Fisher信息、量子Fisher信息、自然梯度更新推导、Fubini-Study度量及高效估计方法。

---

## 1. 经典优化中的Fisher信息矩阵 (Fisher Information in Classical Optimization)

### 1.1 经典参数化概率分布

考虑参数化概率分布族 $\{p(x; \boldsymbol{\theta})\}_{\boldsymbol{\theta}}$，经典Fisher信息矩阵定义为：

$$F_{ij}^{\text{cl}}(\boldsymbol{\theta}) = \mathbb{E}_{x \sim p(\cdot; \boldsymbol{\theta})}\left[\frac{\partial \log p(x; \boldsymbol{\theta})}{\partial \theta_i} \cdot \frac{\partial \log p(x; \boldsymbol{\theta})}{\partial \theta_j}\right]$$

> Fisher信息矩阵度量参数微小变化引起的概率分布变化，是统计流形上的黎曼度量。

等价形式：

$$F_{ij}^{\text{cl}} = -\mathbb{E}\left[\frac{\partial^2 \log p(x; \boldsymbol{\theta})}{\partial \theta_i \partial \theta_j}\right]$$

### 1.2 KL散度与Fisher信息

Fisher信息矩阵是KL散度在 $\boldsymbol{\theta}$ 处的Hessian：

$$D_{\text{KL}}(p(\cdot; \boldsymbol{\theta}) \| p(\cdot; \boldsymbol{\theta} + \boldsymbol{\delta})) = \frac{1}{2} \boldsymbol{\delta}^T F^{\text{cl}}(\boldsymbol{\theta}) \boldsymbol{\delta} + O(\|\boldsymbol{\delta}\|^3)$$

> Fisher信息矩阵刻画了参数空间中"真实距离"——两组相近参数对应的分布差异。

### 1.3 经典自然梯度

标准梯度下降：$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \nabla C$，隐式假设参数空间是欧几里得的。

当参数空间具有非平凡几何结构时，自然梯度（Amari, 1998）考虑参数流形的度量：

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \left(F^{\text{cl}}\right)^{-1} \nabla C$$

**推导**：自然梯度求解约束优化问题

$$\min_{\boldsymbol{\delta}} C(\boldsymbol{\theta} + \boldsymbol{\delta}) \quad \text{s.t.} \quad D_{\text{KL}}(p_{\boldsymbol{\theta}} \| p_{\boldsymbol{\theta}+\boldsymbol{\delta}}) = \epsilon$$

一阶近似 $C(\boldsymbol{\theta} + \boldsymbol{\delta}) \approx C(\boldsymbol{\theta}) + \nabla C^T \boldsymbol{\delta}$ 与 $D_{\text{KL}} \approx \frac{1}{2}\boldsymbol{\delta}^T F \boldsymbol{\delta}$，用Lagrange乘子法：

$$\mathcal{L} = \nabla C^T \boldsymbol{\delta} + \lambda \left(\frac{1}{2}\boldsymbol{\delta}^T F \boldsymbol{\delta} - \epsilon\right)$$

$$\frac{\partial \mathcal{L}}{\partial \boldsymbol{\delta}} = \nabla C + \lambda F \boldsymbol{\delta} = 0 \implies \boldsymbol{\delta}^* = -\frac{1}{\lambda} F^{-1} \nabla C$$

吸收 $1/\lambda$ 到学习率 $\eta$ 中，得到自然梯度更新。

---

## 2. 量子Fisher信息 (Quantum Fisher Information)

### 2.1 参数化量子态的距离

对参数化量子态 $|\psi(\boldsymbol{\theta})\rangle$，态空间上的自然度量是**Fubini-Study度量**。两个无穷近邻态之间的距离：

$$ds^2_{\text{FS}} = 1 - |\langle\psi(\boldsymbol{\theta})|\psi(\boldsymbol{\theta} + d\boldsymbol{\theta})\rangle|^2$$

> Fubini-Study度量是纯态Hilbert空间（射影空间 $\mathbb{CP}^{d-1}$）上的自然黎曼度量。

展开到二阶：

$$ds^2_{\text{FS}} = \sum_{ij} g_{ij}(\boldsymbol{\theta}) \, d\theta_i \, d\theta_j$$

其中度量张量 $g_{ij}$ 即为量子Fisher信息矩阵（的一个版本）。

### 2.2 量子Fisher信息矩阵的推导

$$\langle\psi(\boldsymbol{\theta} + d\boldsymbol{\theta})|\psi(\boldsymbol{\theta})\rangle \approx 1 + \sum_i \langle\partial_i\psi|\psi\rangle d\theta_i + \frac{1}{2}\sum_{ij} \langle\partial_i\psi|\partial_j\psi\rangle d\theta_i d\theta_j + \cdots$$

（注：此处利用了 $\langle\psi|\partial_i\psi\rangle + \langle\partial_i\psi|\psi\rangle = \partial_i\langle\psi|\psi\rangle = 0$。）

取模方：

$$|\langle\psi(\boldsymbol{\theta}+d\boldsymbol{\theta})|\psi(\boldsymbol{\theta})\rangle|^2 \approx 1 + \sum_{ij}\left[\text{Re}(\langle\partial_i\psi|\partial_j\psi\rangle) + \text{Re}(\langle\partial_i\psi|\psi\rangle\langle\psi|\partial_j\psi\rangle)\right] d\theta_i d\theta_j$$

利用 $\langle\partial_i\psi|\psi\rangle = -\langle\psi|\partial_i\psi\rangle$ 为纯虚数，即 $\text{Re}(\langle\partial_i\psi|\psi\rangle) = 0$，得：

$$|\langle\psi+d\psi|\psi\rangle|^2 \approx 1 - \sum_{ij} g_{ij} \, d\theta_i \, d\theta_j$$

其中：

$$\boxed{g_{ij} = F_{ij} = \text{Re}\left[\langle\partial_i\psi|\partial_j\psi\rangle - \langle\partial_i\psi|\psi\rangle\langle\psi|\partial_j\psi\rangle\right]}$$

> 量子Fisher信息矩阵 $F_{ij}$ 等于Fubini-Study度量张量 $g_{ij}$，是纯态空间上的黎曼度量。

### 2.3 等价表达式

利用投影算符 $\Pi = |\psi\rangle\langle\psi|$ 和正交补投影 $\Pi^\perp = I - |\psi\rangle\langle\psi|$：

$$F_{ij} = \text{Re}\left[\langle\partial_i\psi|\Pi^\perp|\partial_j\psi\rangle\right]$$

这清楚表明Fisher信息仅取决于态变化的**正交分量**——平行于 $|\psi\rangle$ 的分量（全局相位变化）不贡献。

### 2.4 性质

1. **半正定**: $F \succeq 0$（因为 $\sum_{ij} v_i F_{ij} v_j = \|\Pi^\perp |\partial_{\mathbf{v}}\psi\rangle\|^2 \geq 0$）
2. **参数化不变**: 自然梯度更新 $F^{-1}\nabla C$ 在参数重参数化下不变
3. **与保真度的关系**: $F(\rho, \rho + d\rho) = ds^2_{\text{Bures}}$（对纯态，Bures度量退化为Fubini-Study）

---

## 3. 自然梯度更新推导 (Natural Gradient Update Derivation)

### 3.1 优化问题

类比经典自然梯度，量子自然梯度求解：

$$\min_{\boldsymbol{\delta}} C(\boldsymbol{\theta} + \boldsymbol{\delta}) \quad \text{s.t.} \quad ds^2_{\text{FS}}(\boldsymbol{\theta}, \boldsymbol{\theta} + \boldsymbol{\delta}) = \epsilon$$

> 量子自然梯度在量子态空间中沿最速下降方向更新，而非参数空间。

### 3.2 推导

一阶近似代价函数：

$$C(\boldsymbol{\theta} + \boldsymbol{\delta}) \approx C(\boldsymbol{\theta}) + \nabla C^T \boldsymbol{\delta}$$

约束条件：

$$ds^2_{\text{FS}} = \boldsymbol{\delta}^T F(\boldsymbol{\theta}) \boldsymbol{\delta} = \epsilon$$

Lagrange乘子法：

$$\mathcal{L}(\boldsymbol{\delta}, \lambda) = \nabla C^T \boldsymbol{\delta} + \lambda (\boldsymbol{\delta}^T F \boldsymbol{\delta} - \epsilon)$$

$$\frac{\partial \mathcal{L}}{\partial \boldsymbol{\delta}} = \nabla C + 2\lambda F \boldsymbol{\delta} = 0$$

$$\boldsymbol{\delta}^* = -\frac{1}{2\lambda} F^{-1} \nabla C$$

令 $\eta = \frac{1}{2\lambda}$（有效学习率），得到更新规则：

$$\boxed{\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \, F^{-1}(\boldsymbol{\theta}_t) \, \nabla_{\boldsymbol{\theta}} C(\boldsymbol{\theta}_t)}$$

### 3.3 几何意义

标准梯度 $\nabla C$ 是参数空间中的最速下降方向（欧几里得度量下）。

自然梯度 $\tilde{\nabla} C = F^{-1} \nabla C$ 是态空间中的最速下降方向（Fubini-Study度量下）。

协变梯度向量满足：

$$\tilde{\nabla}_i C = \sum_j g^{ij} \frac{\partial C}{\partial \theta_j}$$

其中 $g^{ij} = (F^{-1})_{ij}$ 是逆度量张量。这正是黎曼流形上梯度的标准定义。

---

## 4. 与Fubini-Study度量的联系 (Connection to Fubini-Study Metric)

### 4.1 射影Hilbert空间

量子态 $|\psi\rangle$ 和 $e^{i\phi}|\psi\rangle$ 物理等价，因此纯态空间是射影空间 $\mathbb{CP}^{d-1}$（$d = 2^n$）。

Fubini-Study度量是 $\mathbb{CP}^{d-1}$ 上的标准黎曼度量：

$$ds^2_{\text{FS}} = \frac{\langle d\psi|d\psi\rangle}{\langle\psi|\psi\rangle} - \frac{\langle d\psi|\psi\rangle\langle\psi|d\psi\rangle}{\langle\psi|\psi\rangle^2}$$

> Fubini-Study度量扣除了全局相位的贡献，刻画物理上可区分的态变化。

对归一化态 $\langle\psi|\psi\rangle = 1$，参数化诱导的度量为：

$$ds^2 = \sum_{ij} g_{ij} d\theta_i d\theta_j, \quad g_{ij} = \text{Re}[\langle\partial_i\psi|\partial_j\psi\rangle - \langle\partial_i\psi|\psi\rangle\langle\psi|\partial_j\psi\rangle]$$

这**完全**等同于第2节推导的量子Fisher信息矩阵 $F_{ij} = g_{ij}$。

### 4.2 例子：单量子比特

参数化态 $|\psi(\theta, \phi)\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle$（Bloch球坐标）。

$$g = \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{1}{4}\sin^2\theta \end{pmatrix}$$

这是球面 $S^2$ 上标准度量 $ds^2 = \frac{1}{4}(d\theta^2 + \sin^2\theta \, d\phi^2)$ 的 $1/4$ 倍——即半径为 $1/2$ 的球面。

在极点 $\theta = 0$ 附近，$\phi$ 方向的Fisher信息趋零，反映了 $\phi$ 在 $|0\rangle$ 附近不影响量子态——自然梯度会自动抑制该方向的更新。

---

## 5. 高效估计方法 (Efficient Estimation Methods)

### 5.1 直接方法的困难

$F_{ij}$ 有 $O(p^2)$ 个矩阵元（$p$ 为参数数），每个矩阵元需要量子电路求值。直接计算的总代价：$O(p^2 \cdot N_s)$（$N_s$ 为每个矩阵元的采样数）。

对大 $p$，这在经典端和量子端都是瓶颈。

### 5.2 块对角近似 (Block-Diagonal Approximation)

Stokes et al. (2020) 提出将 $F$ 近似为块对角矩阵，每个块对应一层电路：

$$F \approx \text{diag}(F^{(1)}, F^{(2)}, \dots, F^{(L)})$$

> 块对角近似将 $O(p^2)$ 的矩阵元数减少到 $O(p \cdot n)$，每块仅涉及同层参数。

其中 $F^{(l)}$ 为第 $l$ 层内参数之间的Fisher信息子矩阵（维度 $n_l \times n_l$，$n_l$ 为该层参数数）。

### 5.3 对角近似

更激进的近似：仅保留对角元素

$$F \approx \text{diag}(F_{11}, F_{22}, \dots, F_{pp})$$

每个对角元 $F_{kk} = \langle\partial_k\psi|\partial_k\psi\rangle - |\langle\partial_k\psi|\psi\rangle|^2$ 可以通过参数平移规则估计：

$$F_{kk} = \frac{1}{2}\left[1 - |\langle\psi(\boldsymbol{\theta})|\psi(\boldsymbol{\theta}_k')\rangle|^2\right]$$

其中 $\boldsymbol{\theta}_k'$ 是将 $\theta_k$ 平移 $\pi/2$ 后的参数向量，重叠可通过SWAP测试估计。

### 5.4 随机近似 (Stochastic Approximation)

在每步仅估计 $F$ 的随机子集元素，利用随机矩阵近似：

$$\tilde{F} = \frac{p}{m}\sum_{(i,j) \in \mathcal{S}} F_{ij} e_i e_j^T$$

其中 $\mathcal{S}$ 为随机采样的 $m$ 个索引对。

### 5.5 Hadamard测试方法

$F_{ij}$ 的非对角元可通过修改的Hadamard测试电路计算：

$$\text{Re}[\langle\partial_i\psi|\partial_j\psi\rangle] = \frac{1}{4}\left[\langle\psi|_{+,ij} - \langle\psi|_{-,ij}\right]$$

其中 $|\psi\rangle_{\pm,ij}$ 为同时平移参数 $\theta_i, \theta_j$ 得到的态。

### 5.6 量子模拟方法

对门型电路 $U(\boldsymbol{\theta}) = \prod_k e^{-i\theta_k G_k/2}$，Fisher信息矩阵元可表示为：

$$F_{ij} = \text{Re}\left[\langle 0|V_i^\dagger V_j|0\rangle - \langle 0|V_i^\dagger|\psi\rangle\langle\psi|V_j|0\rangle\right]$$

其中 $V_i = U^\dagger(\boldsymbol{\theta})\frac{\partial U(\boldsymbol{\theta})}{\partial \theta_i}$，可在量子电路中高效实现。

---

## 6. 与普通梯度下降的比较 (Comparison with Vanilla Gradient Descent)

### 6.1 理论比较

| 特性 | 普通梯度下降 (VGD) | 量子自然梯度 (QNG) |
|------|------------------|------------------|
| 更新规则 | $\boldsymbol{\theta} - \eta \nabla C$ | $\boldsymbol{\theta} - \eta F^{-1}\nabla C$ |
| 度量 | 欧几里得（参数空间） | Fubini-Study（态空间） |
| 参数化不变性 | 否 | 是 |
| 每步计算代价 | $O(p)$ 梯度求值 | $O(p^2)$ + 矩阵求逆 |
| 收敛速率 | 依赖条件数 $\kappa(H)$ | 对条件数不敏感 |
| 对贫瘠高原 | 脆弱 | 部分缓解 |

> 量子自然梯度以更高的每步代价换取更快的收敛和参数化无关性。

### 6.2 参数化不变性

**关键优势**: 若进行参数重参数化 $\boldsymbol{\theta} \to \boldsymbol{\phi}(\boldsymbol{\theta})$，普通梯度下降的行为改变，但自然梯度不变。

设 $\theta_i = \theta_i(\boldsymbol{\phi})$，则梯度变换为 $\nabla_\phi C = J^T \nabla_\theta C$（$J$ 为Jacobian），Fisher矩阵变换为 $F_\phi = J^T F_\theta J$。

自然梯度：

$$F_\phi^{-1} \nabla_\phi C = (J^T F_\theta J)^{-1} J^T \nabla_\theta C = J^{-1} F_\theta^{-1} \nabla_\theta C$$

在 $\phi$ 空间中的更新 $\delta\phi = -\eta J^{-1} F_\theta^{-1} \nabla_\theta C$ 等价于在 $\theta$ 空间中的更新 $\delta\theta = -\eta F_\theta^{-1} \nabla_\theta C$——几何上是同一方向。

### 6.3 对贫瘠高原的效果

在贫瘠高原区域，$\nabla C \sim O(2^{-n/2})$，但 $F$ 的某些本征值也可能很小。若 $F$ 的小本征值方向与梯度方向对齐，$F^{-1}\nabla C$ 可以放大信号。

然而，QNG并不能完全解决贫瘠高原：
- 若代价函数景观本身是平坦的（信号淹没在噪声中），放大梯度同时放大噪声
- $F$ 的估计在贫瘠高原区域本身精度不足
- QNG主要帮助应对"假性"贫瘠高原（由不良参数化引起的平坦景观）

### 6.4 数值比较实例

对VQE求解 $H_2$ 分子的典型行为：

| 指标 | VGD | QNG |
|------|-----|-----|
| 达到化学精度所需迭代 | ~200-500 | ~20-50 |
| 每步量子电路调用 | $O(p)$ | $O(p^2)$ |
| 总量子电路调用 | 较多 | 通常更少 |
| 对初始点敏感性 | 高 | 低 |

### 6.5 实践建议

1. **小规模问题** ($p \leq 50$): QNG优势明显，Fisher矩阵计算可承受
2. **中等规模** ($50 < p \leq 500$): 使用块对角近似的QNG
3. **大规模** ($p > 500$): 对角近似或切换至Adam/SPSA等经典优化器
4. **噪声环境**: QNG对噪声更敏感（$F$ 的估计误差被放大），考虑正则化 $F + \epsilon I$

### 6.6 正则化Fisher矩阵

实际使用中，$F$ 可能奇异或病态，常用Tikhonov正则化：

$$\tilde{F} = F + \epsilon I$$

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta (F + \epsilon I)^{-1} \nabla C$$

$\epsilon$ 起到在QNG和VGD之间插值的作用：$\epsilon \to 0$ 恢复纯QNG，$\epsilon \to \infty$ 退化为VGD（带缩放）。

---

## 7. 与虚时间演化的等价性 (Equivalence to Imaginary Time Evolution)

> 基于 **[Tilly et al. 2022, §7]** 和 **[Cerezo et al. 2021, §2.4]**。

### 7.1 虚时间演化定义 **[Tilly et al. 2022, §7]**

虚时间演化将Schrodinger方程中的时间替换为虚时间 $\tau$：

$$|\psi(\tau)\rangle = A(\tau) e^{-H\tau} |\psi(0)\rangle$$

其中 $A(\tau)$ 是归一化常数。当 $\tau \to \infty$ 时，$|\psi(\tau)\rangle$ 收敛到 $H$ 的基态（假设初态与基态有非零重叠）。

### 7.2 等价性证明 **[Tilly et al. 2022, §7, Stokes et al.]**

**定理** (Stokes et al. 2020, 引自 **[Tilly et al. 2022, §7]**): 纯态量子自然梯度下降等价于变分虚时间演化。

具体地，McLachlan变分原理给出的参数演化方程为：

$$F \dot{\boldsymbol{\theta}} = -\nabla_{\boldsymbol{\theta}} E$$

其中 $F$ 为Fubini-Study度量张量。这恰好是以 $F$ 为度量的自然梯度下降的连续时间极限。

### 7.3 KL散度与信息几何 **[Tilly et al. 2022, §7]**

自然梯度的基础在于参数空间的信息几何。Fisher信息矩阵是KL散度的Hessian：

$$ds^2 = d\boldsymbol{\theta}^T F \, d\boldsymbol{\theta}$$

自然梯度最大化每步中的KL散度变化。**[Tilly et al. 2022, §7]**

---

## 8. 混合态推广的Fubini-Study度量 (Mixed-State Generalization)

> 基于 **[Tilly et al. 2022, §7]**。

### 8.1 对称对数导数形式 **[Tilly et al. 2022, §7, Koczor et al.]**

对混合态 $\rho(\boldsymbol{\theta})$，Fubini-Study度量推广为：

$$(F)_{ij} = \frac{1}{2} \text{tr}[\rho(\boldsymbol{\theta})(L_i L_j + L_j L_i)]$$

其中 $L_k$ 是对称对数导数（symmetric logarithmic derivative），定义为：

$$\partial_k \rho(\boldsymbol{\theta}) = \frac{1}{2}(L_k \rho(\boldsymbol{\theta}) + \rho(\boldsymbol{\theta}) L_k)$$

### 8.2 NISQ设备上的高效近似 **[Tilly et al. 2022, §7]**

设密度矩阵保真度 $f_{\text{id}} = 1 - \epsilon$，则Fisher信息矩阵可近似为：

$$(F)_{ij} \approx 2 \text{tr}\left[\frac{(\partial_i \rho_\epsilon)(\partial_j \rho_\epsilon)}{f_{\text{id}}}\right] + O\left(\frac{1-f_{\text{id}}}{d}\right)$$

项 $\text{tr}[(\partial_i \rho_\epsilon)(\partial_j \rho_\epsilon)]$ 是黎曼度量张量，可通过SWAP测试在量子硬件上估计。**[Tilly et al. 2022, §7]**

---

## 9. 半逆与正则化自然梯度 (Half-Inversion and Regularized QNG)

> **[Tilly et al. 2022, §7, Haug et al.]**

### 9.1 广义正则化 **[Tilly et al. 2022, §7]**

除标准Tikhonov正则化外，可使用"半逆"：

$$\tilde{g} = F^{-\alpha} \nabla \mathcal{L}(\boldsymbol{\theta})$$

其中 $\alpha$ 为正则化参数：
- $\alpha = 0$：标准梯度（无预条件）
- $\alpha = 1$：完整自然梯度
- $\alpha = 0.5$：**推荐的实用设置**，平衡稳定性与收敛速度

**[Tilly et al. 2022, §7, Haug et al. 2021]**

### 9.2 随机近似自然梯度 (Stochastic QNG) **[Tilly et al. 2022, §7]**

Fisher信息矩阵可通过SPSA方法近似以降低构造成本 **[Tilly et al. 2022, §7, Gacon et al.]**：

$$\tilde{F}^{(k)} = \frac{\delta F}{2\epsilon^2} \frac{\Delta_1^{(k)} \Delta_2^{(k)T} + \Delta_2^{(k)} \Delta_1^{(k)T}}{2}$$

使用指数平滑估计器累积：

$$\bar{F}^{(k)} = \frac{k}{k+1} \bar{F}^{(k-1)} + \frac{1}{k+1} \tilde{F}^{(k)}$$

随机近似自然梯度虽不如精确QNG效果好，但仍优于标准梯度下降，且将每步量子电路调用从 $O(p^2)$ 降至 $O(1)$。**[Tilly et al. 2022, §7]**

---

## 10. Cerezo综述中关于QNG的定位 (QNG in the Cerezo VQA Review)

> **[Cerezo et al. 2021, §2.4]**

**[Cerezo et al. 2021, §2.4]** 将量子自然梯度定位为VQA优化器工具箱中的关键方法：

1. **信息几何基础**：QNG基于参数流形的度量张量，在参数化变换下不变
2. **加速收敛**：使用度量张量通常加速梯度更新步的收敛，减少达到给定精度所需的迭代次数
3. **噪声推广**：已扩展到考虑噪声效应的版本 (Koczor et al.)
4. **收敛分析限制**：VQA代价景观一般非凸，难以给出一般性收敛保证；但在最小值附近的凸区域内，使用参数平移规则的SGD方法已证明具有比仅使用目标值的方法（包括有限差分）更小的优化复杂度上界。**[Cerezo et al. 2021, §2.4, Harrow et al.]**
