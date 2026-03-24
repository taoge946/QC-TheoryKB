# 贫瘠高原理论推导

> Barren Plateaus in Variational Quantum Circuits: Complete Theory
> 涵盖定义、McClean定理、Haar测度证明、代价函数依赖性、噪声诱导与缓解策略。

---

## 1. 定义：指数衰减的梯度 (Definition: Exponentially Vanishing Gradients)

### 1.1 严格定义

考虑参数化量子电路 $U(\boldsymbol{\theta})$ 和代价函数 $C(\boldsymbol{\theta}) = \text{tr}[O \, U(\boldsymbol{\theta})\rho_0 U^\dagger(\boldsymbol{\theta})]$。

> 贫瘠高原指代价函数梯度的均值为零且方差随量子比特数指数衰减，使基于梯度的优化不可行。

**贫瘠高原条件**：若存在 $b > 1$ 使得

$$\mathbb{E}_{\boldsymbol{\theta}}\left[\frac{\partial C}{\partial \theta_k}\right] = 0, \quad \text{Var}_{\boldsymbol{\theta}}\left[\frac{\partial C}{\partial \theta_k}\right] \leq O(b^{-n})$$

则称代价景观在参数 $\theta_k$ 方向上存在贫瘠高原。

### 1.2 实际后果

若 $\text{Var}[\partial_k C] \in O(2^{-n})$，则以高概率 $|\partial_k C| \in O(2^{-n/2})$。

由Chebyshev不等式：

$$\Pr\left[|\partial_k C| > \delta\right] \leq \frac{\text{Var}[\partial_k C]}{\delta^2} \leq \frac{c}{2^n \delta^2}$$

要以常数概率检测到非零梯度，需要精度 $\delta \sim 2^{-n/2}$，这意味着需要 $O(2^n)$ 次测量——与经典穷举搜索无异。

---

## 2. McClean等人2018年的结果 (McClean et al. 2018)

### 2.1 主定理

**定理** (McClean, Boixo, Smelyanskiy, Neven, Barren, *Nat. Commun.* 2018):

对 $n$ 量子比特的参数化电路 $U(\boldsymbol{\theta})$，若电路深度足够使得 $U(\boldsymbol{\theta})$ 形成Hilbert空间上的**近似2-设计**（approximate 2-design），则对任意可观测量 $O$：

$$\text{Var}_{\boldsymbol{\theta}}\left[\frac{\partial C}{\partial \theta_k}\right] \leq \frac{c_n}{2^{2n}}$$

> 当参数化电路足够随机（构成2-设计）时，梯度方差以指数速率趋零。

其中 $c_n$ 仅依赖于可观测量 $O$ 的性质，而非系统大小。

### 2.2 核心条件

贫瘠高原出现的充分条件：
1. 电路形成（近似）2-设计
2. 随机参数初始化
3. 足够的电路深度（对局部随机电路，深度 $\Omega(n)$ 即可）

---

## 3. 证明概要：2-设计与Haar测度 (Proof Sketch)

### 3.1 框架设置

将电路分解为 $U(\boldsymbol{\theta}) = U_R \, U_k(\theta_k) \, U_L$，其中：
- $U_L$：参数 $\theta_k$ 左侧的所有门
- $U_k(\theta_k) = e^{-i\theta_k G_k/2}$：含参数 $\theta_k$ 的门
- $U_R$：参数 $\theta_k$ 右侧的所有门

代价函数的偏导数：

$$\frac{\partial C}{\partial \theta_k} = -\frac{i}{2}\text{tr}\left[O \, U_R [G_k, U_L \rho_0 U_L^\dagger] U_R^\dagger\right]$$

> 梯度可表示为含参门生成元与密度矩阵的对易子在右侧电路下的期望值。

### 3.2 2-设计的积分公式

若 $U_L$（或 $U_R$）的分布构成幺正群上的2-设计，则对任意线性函数 $f$：

$$\mathbb{E}_{U \sim \text{2-design}}[f(U\rho U^\dagger)] = \mathbb{E}_{U \sim \text{Haar}}[f(U\rho U^\dagger)]$$

Haar积分的核心结果（Weingarten函数方法）：

$$\int dU \, U^{\otimes 2} \rho (U^\dagger)^{\otimes 2} = \frac{1}{d^2 - 1}\left[(\text{tr}\rho)^2 - \frac{\text{tr}(\rho^2)}{d}\right]\frac{I \otimes I}{1} + \cdots$$

其中 $d = 2^n$。

### 3.3 方差计算

**步骤1**: 计算均值 $\mathbb{E}[\partial_k C]$。

对Haar随机 $U_L$：$\mathbb{E}[U_L \rho_0 U_L^\dagger] = \frac{I}{d}$，因此：

$$\mathbb{E}\left[\frac{\partial C}{\partial \theta_k}\right] = -\frac{i}{2}\text{tr}\left[O \, U_R \left[G_k, \frac{I}{d}\right] U_R^\dagger\right] = 0$$

因为 $[G_k, I] = 0$。

**步骤2**: 计算方差 $\text{Var}[\partial_k C] = \mathbb{E}[(\partial_k C)^2]$。

这需要Haar测度的二阶矩：

$$\mathbb{E}[(\partial_k C)^2] = \frac{1}{4}\text{tr}\left[(O \otimes O)(U_R \otimes U_R) \, \mathbb{E}_{U_L}[\cdot] \, (U_R^\dagger \otimes U_R^\dagger)\right]$$

利用2-设计的二阶矩公式，经过代数化简得到：

$$\text{Var}[\partial_k C] = -\frac{\text{tr}(O^2) - \text{tr}(O)^2/d}{d(d^2-1)} \cdot \text{tr}(G_k^2 - G_k^2/d)$$

### 3.4 渐近行为

对 $d = 2^n \to \infty$，主项为：

$$\text{Var}[\partial_k C] \sim \frac{\text{tr}(O^2)}{2^{2n}} \cdot \text{tr}(G_k^2)$$

> 方差以 $O(1/2^{2n})$ 衰减（对于 $\text{tr}(O^2)$ 为常数的可观测量），甚至更快于 $2^{-n}$。

若 $O$ 是全局可观测量且 $\text{tr}(O^2) = O(1)$，则 $\text{Var}[\partial_k C] \in O(2^{-2n})$。

若 $O$ 作用在 $k$ 个量子比特上，$\text{tr}(O^2) = O(2^{n-k})$，则 $\text{Var} \in O(2^{-(n+k)})$。$\blacksquare$

---

## 4. 代价函数依赖：局部与全局可观测量 (Local vs Global Observables)

### 4.1 全局代价函数

$$C_{\text{global}} = \text{tr}[O_{\text{global}} \, |\psi(\boldsymbol{\theta})\rangle\langle\psi(\boldsymbol{\theta})|]$$

其中 $O_{\text{global}}$ 作用在所有 $n$ 个量子比特上（如投影到目标态 $|\phi\rangle\langle\phi|$）。

> 全局代价函数的梯度以 $O(2^{-2n})$ 衰减——总是存在贫瘠高原。

**结果** (Cerezo et al., *Nat. Commun.* 2021): 全局代价函数**必定**产生贫瘠高原，即使电路很浅。

### 4.2 局部代价函数

$$C_{\text{local}} = \sum_{i=1}^{n} \text{tr}[O_i \otimes I_{\bar{i}} \, |\psi(\boldsymbol{\theta})\rangle\langle\psi(\boldsymbol{\theta})|]$$

其中 $O_i$ 仅作用在第 $i$ 个（或少数几个）量子比特上。

> 局部代价函数在浅层电路中可避免贫瘠高原，但深层电路中仍无法幸免。

**结果** (Cerezo et al., 2021):
- **浅层电路**（$L \in O(\log n)$）：$\text{Var}[\partial_k C_{\text{local}}] \in \Omega(1/\text{poly}(n))$ ——**无**贫瘠高原
- **深层电路**（$L \in \Omega(n)$）：$\text{Var}[\partial_k C_{\text{local}}] \in O(2^{-n})$ ——**有**贫瘠高原

### 4.3 VQE代价函数的分类

VQE的哈密顿量 $H = \sum_i c_i P_i$ 通常包含局部Pauli项：
- **2-local**（如Ising模型 $Z_iZ_j$）：属于局部代价函数
- **$k$-local**（$k$ 为常数）：同样属于局部代价函数
- 在浅层电路下有多项式衰减的梯度——原则上可训练

---

## 5. 噪声诱导的贫瘠高原 (Noise-Induced Barren Plateaus)

### 5.1 Wang等人2021年的结果

**定理** (Wang, Cerezo, Verdon, Coles, *Nat. Commun.* 2021):

在退极化噪声模型下，即使使用局部代价函数和浅层电路，只要噪声率 $p$ 为常数，对深度 $L \in \Omega(\log n)$ 的电路：

$$\text{Var}[\partial_k C] \leq c \cdot e^{-\alpha n L p}$$

> 噪声会额外诱导贫瘠高原，即使电路结构本身不产生贫瘠高原。

### 5.2 物理直觉

噪声将量子态推向最大混合态 $I/2^n$：

$$\mathcal{E}(\rho) = (1-p)\rho + p \cdot \frac{I}{2^n}$$

经过 $L$ 层噪声后：

$$\rho_{\text{noisy}} \approx (1-p)^{nL} \rho_{\text{ideal}} + [1-(1-p)^{nL}] \frac{I}{2^n}$$

当 $nLp \gg 1$ 时，$\rho_{\text{noisy}} \approx I/2^n$，代价函数趋于平凡值 $\text{tr}(O)/2^n$，梯度消失。

### 5.3 临界深度

噪声诱导贫瘠高原的临界深度：

$$L_{\text{crit}} \sim \frac{1}{np}$$

超过此深度，梯度信号被噪声淹没。对当前NISQ设备（$p \sim 10^{-3}$ 到 $10^{-2}$），有效训练深度受严格限制。

---

## 6. 缓解策略 (Mitigation Strategies)

### 6.1 结构化拟设 (Structured Ansatze)

**核心思想**: 限制电路的表达能力以避免2-设计行为。

> 问题启发的结构化拟设通过限制搜索空间来保持梯度可训练性。

- **对称性保持拟设**: 限制 $U(\boldsymbol{\theta})$ 保持 $H$ 的对称性（如粒子数守恒），减小有效Hilbert空间维度
- **QAOA型拟设**: 仅 $2P$ 个参数，远少于HEA的 $O(nL)$ 参数，天然避免过参数化
- **Hamiltonian variational ansatz**: $U(\boldsymbol{\theta}) = \prod_l e^{-i\theta_l H_l}$，其中 $H_l$ 是哈密顿量的子项

**定理** (Larocca et al., 2022): 若拟设保持对称性群 $\mathcal{G}$，有效维度从 $2^n$ 降至 $\dim(\mathcal{H}_{\text{irr}})$，梯度方差的衰减由不可约表示的维度控制。

### 6.2 分层训练 (Layer-wise Training)

**协议**:
1. 初始化 $L$ 层电路，仅训练第1层的参数，其余层设为恒等
2. 固定第1层，训练第2层
3. 逐层添加并训练
4. 最后全局微调

> 分层训练通过逐步增加有效深度避免一开始就陷入贫瘠高原。

**理论依据**: 在第 $l$ 步，有效电路仅有 $l$ 层深度，对 $l \in O(\log n)$，局部代价函数的梯度保持多项式衰减。

### 6.3 预训练/热启动 (Warm Starting)

- **经典预计算**: 用经典方法（如Hartree-Fock）获得初始参数 $\boldsymbol{\theta}_0$，使初始态接近基态
- **参数迁移**: 从小系统训练的参数迁移到大系统
- **扰动初始化**: 在已知好参数附近加入小扰动，而非完全随机初始化

### 6.4 局部代价函数设计

将全局代价函数转化为等价的局部代价函数：

$$C_{\text{local}} = 1 - \frac{1}{n}\sum_{i=1}^{n} \text{tr}_i[\rho_i^{\text{target}} \, \text{tr}_{\bar{i}}(\rho)]$$

> 用局部约化密度矩阵的逐比特保真度替代全局保真度。

### 6.5 自适应方法

- **ADAPT-VQE** (Grimsley et al., 2019): 动态选择最大梯度方向的算符逐步构建拟设
- **量子自然梯度**: 用Fisher信息矩阵重标定梯度，部分补偿平坦景观

### 6.6 其他方法

- **参数相关初始化**: 按特定分布（非均匀Haar）采样初始参数
- **量子卷积神经网络** (QCNN): 浅层+多尺度结构天然避免贫瘠高原
- **纠缠控制**: 限制电路中的纠缠生长速率

---

## 7. 表达能力与可训练性的权衡 (Expressibility vs Trainability Tradeoff)

### 7.1 表达能力量化

电路的表达能力可通过其输出态分布与Haar随机态分布的距离衡量：

$$\mathcal{A}(U) = \left\| \int_{\boldsymbol{\theta}} d\boldsymbol{\theta} \, |\psi(\boldsymbol{\theta})\rangle\langle\psi(\boldsymbol{\theta})|^{\otimes t} - \int_{\text{Haar}} dU \, U|0\rangle\langle 0|U^\dagger)^{\otimes t} \right\|$$

> $\mathcal{A} = 0$ 意味着电路完全等价于Haar随机——此时必有贫瘠高原。

### 7.2 基本矛盾

**表达能力要求**: 拟设应能覆盖目标态所在的Hilbert空间区域
**可训练性要求**: 拟设不应过于"均匀"地覆盖整个Hilbert空间

两者之间存在根本张力：

$$\text{高表达能力} \iff \text{接近2-设计} \implies \text{贫瘠高原}$$

### 7.3 最优权衡点

Holmes et al. (2022) 的"过参数化"结果：当参数数 $p$ 满足：

$$p \sim d_{\text{eff}} = \dim(\text{可达态空间})$$

时，达到最优的表达/可训练权衡。

**实践指导**:
- 参数数远少于 $d_{\text{eff}}$：欠参数化，可能无法表达目标态
- 参数数远大于 $d_{\text{eff}}$：过参数化，接近2-设计，出现贫瘠高原
- 参数数约等于 $d_{\text{eff}}$：刚好覆盖需要的态空间，同时保持梯度

### 7.4 总结：避免贫瘠高原的设计原则

1. **使用局部代价函数**而非全局代价函数
2. **控制电路深度**在 $O(\log n)$ 到 $O(\text{poly}\log n)$ 范围
3. **利用问题对称性**减小有效Hilbert空间
4. **智能初始化**（热启动、经典预计算、参数迁移）
5. **分层训练**逐步增加电路复杂度
6. **控制纠缠**：避免过快的纠缠增长

---

## 8. Tilly综述的补充：VQE上下文中的贫瘠高原 (Barren Plateaus in VQE Context)

> 以下内容基于 **[Tilly et al. 2022, §6.1]**。

### 8.1 VQE代价函数的形式化贫瘠高原条件

**[Tilly et al. 2022, §6.1]** 给出VQE中贫瘠高原的严格表述。设VQE代价函数 $E(\boldsymbol{\theta}) = \langle\psi(\boldsymbol{\theta})|\hat{H}|\psi(\boldsymbol{\theta})\rangle$，此代价函数存在贫瘠高原当且仅当：对任意 $\theta_i \in \boldsymbol{\theta}$ 和任意 $\epsilon > 0$，存在 $b > 1$ 使得

$$\Pr(|\partial_{\theta_i} E(\boldsymbol{\theta})| \geq \epsilon) \leq O\left(\frac{1}{b^N}\right)$$

此结果是Chebyshev不等式的直接推论。**[Tilly et al. 2022, §6.1]**

### 8.2 层状拟设的梯度解析表达式 **[Tilly et al. 2022, §6.1, Eq.]**

对层状拟设 $U(\boldsymbol{\theta}) = \prod_{l=1}^L U_l(\theta_l) \mathcal{W}_l$，梯度为：

$$\partial_{\theta_i} E = i \langle 0| U_{1 \to (i-1)}^\dagger [\hat{V}_i, U_{i \to L}^\dagger \hat{H} U_{i \to L}] U_{1 \to (i-1)} |0\rangle$$

**[Tilly et al. 2022, §6.1, Eq.]**。若 $U_{1 \to (i-1)}$ 和 $U_{i \to L}$ 均为2-设计，梯度方差具有精确表达式：

$$\text{Var}[\partial_{\theta_i} E] \approx \frac{1}{2^{3N-1}} \text{tr}[\hat{H}^2] \, \text{tr}[\rho^2] \, \text{tr}[\hat{V}^2]$$

**[Tilly et al. 2022, §6.1, McClean et al.]**

### 8.3 噪声诱导贫瘠高原 (NIBP) 的严格界 **[Tilly et al. 2022, §6.1]**

**定理** (Wang et al. 2021, 引自 **[Tilly et al. 2022, §6.1]**):

$$\left|\frac{\partial \langle \hat{H}(\boldsymbol{\theta}) \rangle}{\partial \theta_i}\right| \leq G(N) \cdot q^{L+1}$$

其中 $q < 1$ 是噪声参数，$G(N) \sim O(2^{-\alpha N})$，$L$ 是层数。

关键区别：NIBP是梯度本身的界（而非方差），物理表现为期望值函数振幅的衰减和远离最小值的偏差，而非景观的平坦化。NIBP与参数初始化和代价函数局部性无关。**[Tilly et al. 2022, §6.1]**

### 8.4 纠缠度驱动的贫瘠高原 **[Tilly et al. 2022, §6.1]**

**定理** (Patti et al., Ortiz Marrero et al., 引自 **[Tilly et al. 2022, §6.1]**): 试探波函数的纠缠熵与梯度消失直接关联。即使在浅层电路深度下，高纠缠也可导致贫瘠高原。量子神经网络中可见层和隐层之间的纠缠同样降低可训练性。

### 8.5 恒等初始化策略 **[Tilly et al. 2022, §6.1, Grant et al.]**

将拟设分为 $K$ 个深度 $D$ 的块。每块 $U_k(\boldsymbol{\theta}_k)$ 分为两个等深度部分：

$$U_k(\boldsymbol{\theta}_k) = \prod_{d=1}^{D/2-1} U_d(\theta_{d,1}^k) W_d \prod_{d=D/2}^{D} U_d(\theta_{d,2}^k) W_d$$

初始化时令 $\theta_{d,2}^k$ 使得 $U_d(\theta_{d,2}^k) W_d = (U_d(\theta_{d,1}^k) W_d)^\dagger$，从而

$$U_k(\boldsymbol{\theta}_{\text{init}}) = I_k, \quad U(\boldsymbol{\theta}_{\text{init}}) = I$$

初始电路为恒等变换，避免在随机2-设计区域启动。**[Tilly et al. 2022, §6.1, Grant et al. 2019]**

### 8.6 VQE特有的缓解优势 **[Tilly et al. 2022, §6.1, Holmes et al.]**

VQE相比一般VQA具有独特优势：
1. **问题对称性**可用于减小有效Hilbert空间
2. **物理动机拟设**（如UCC）天然限制搜索空间
3. **局部编码**（Bravyi-Kitaev vs Jordan-Wigner）可降低代价函数的非局部性

具体地，Bravyi-Kitaev编码的Pauli权重为 $O(\log N)$，而Jordan-Wigner为 $O(N)$，前者产生更局部的代价函数，梯度方差可大一个数量级。**[Tilly et al. 2022, §6.1, Uvarov et al.]**

---

## 9. Cerezo综述：梯度无关优化器也受贫瘠高原影响

> **[Cerezo et al. 2021, §4.1]**

**关键结论** **[Cerezo et al. 2021, §4.1]**：贫瘠高原不仅影响基于梯度的优化器，也影响无梯度优化器（如COBYLA、Nelder-Mead）。这是因为在贫瘠高原区域，代价函数值本身集中在 $\text{tr}(O)/2^n$ 附近，任何依赖代价函数差异来指导搜索的方法都将失效。

需要 $O(2^n)$ 精度的代价函数评估才能检测到有意义的差异——这与经典暴力搜索的资源消耗相当。
