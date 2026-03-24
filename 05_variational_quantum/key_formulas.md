# 变分量子算法 - 核心公式集

> Variational Quantum Algorithms: Key Formulas
> 本文档收录变分量子算法（VQE、QAOA、量子自然梯度等）的12个核心公式。

---

## F5.1 变分原理 (Variational Principle)

$$E_0 \leq \langle\psi(\boldsymbol{\theta})|H|\psi(\boldsymbol{\theta})\rangle$$

**中文说明**: 任意参数化试探态的能量期望值始终不低于系统基态能量，这是VQE的理论基础。

**来源**: Rayleigh-Ritz variational principle; Peruzzo et al., *Nat. Commun.* **5**, 4213 (2014).

---

## F5.2 VQE代价函数 (VQE Cost Function)

$$C(\boldsymbol{\theta}) = \langle\psi(\boldsymbol{\theta})|H|\psi(\boldsymbol{\theta})\rangle = \sum_i c_i \langle\psi(\boldsymbol{\theta})|P_i|\psi(\boldsymbol{\theta})\rangle$$

其中 $H = \sum_i c_i P_i$ 是哈密顿量的Pauli分解，$P_i \in \{I, X, Y, Z\}^{\otimes n}$。

**中文说明**: VQE代价函数通过将哈密顿量分解为Pauli项之和，将能量期望值转化为可在量子硬件上逐项测量的形式。

**来源**: Peruzzo et al., *Nat. Commun.* **5**, 4213 (2014); McClean et al., *New J. Phys.* **18**, 023023 (2016).

---

## F5.3 参数平移规则 (Parameter Shift Rule)

$$\frac{\partial}{\partial \theta_k} \langle H \rangle = \frac{1}{2}\left[\langle H \rangle_{\theta_k + \pi/2} - \langle H \rangle_{\theta_k - \pi/2}\right]$$

适用条件：参数化门形如 $U_k(\theta_k) = e^{-i\theta_k G_k/2}$，其中 $G_k$ 满足 $G_k^2 = I$（即生成元的本征值为 $\pm 1$）。

**中文说明**: 参数平移规则允许仅通过两次电路求值精确计算梯度，无需有限差分近似。

**来源**: Mitarai et al., *Phys. Rev. A* **98**, 032309 (2018); Schuld et al., *Phys. Rev. A* **99**, 032331 (2019).

---

## F5.4 QAOA拟设 (QAOA Ansatz)

$$|\boldsymbol{\gamma}, \boldsymbol{\beta}\rangle = \prod_{p=1}^{P} e^{-i\beta_p H_M} e^{-i\gamma_p H_C} |+\rangle^{\otimes n}$$

其中 $P$ 为QAOA层数，$\boldsymbol{\gamma} = (\gamma_1, \dots, \gamma_P)$，$\boldsymbol{\beta} = (\beta_1, \dots, \beta_P)$ 为变分参数。

**中文说明**: QAOA通过交替施加代价哈密顿量和混合哈密顿量的幺正演化构建参数化量子态，层数 $P$ 越大近似越精确。

**来源**: Farhi, Goldstone, Gutmann, arXiv:1411.4028 (2014).

---

## F5.5 QAOA混合哈密顿量 (QAOA Mixing Hamiltonian)

$$H_M = \sum_{i=1}^{n} X_i$$

其中 $X_i$ 是作用在第 $i$ 个量子比特上的Pauli-X算符。

**中文说明**: 标准混合哈密顿量为所有比特上Pauli-X之和，其幺正演化 $e^{-i\beta H_M}$ 实现各比特绕X轴的独立旋转，驱动搜索空间的探索。

**来源**: Farhi, Goldstone, Gutmann, arXiv:1411.4028 (2014).

---

## F5.6 MaxCut的QAOA代价哈密顿量 (QAOA Cost Hamiltonian for MaxCut)

$$H_C = \frac{1}{2}\sum_{(i,j)\in E} (I - Z_i Z_j)$$

对图 $G=(V,E)$，当比特 $i,j$ 取不同值（一个在cut中一个不在）时，对应项贡献 $+1$。

**中文说明**: MaxCut的代价哈密顿量将图的每条边编码为Ising相互作用项，基态对应最大割的解。

**来源**: Farhi, Goldstone, Gutmann, arXiv:1411.4028 (2014).

---

## F5.7 近似比 (Approximation Ratio)

$$r = \frac{\langle \boldsymbol{\gamma}, \boldsymbol{\beta} | H_C | \boldsymbol{\gamma}, \boldsymbol{\beta} \rangle}{C_{\max}}$$

其中 $C_{\max}$ 是最优解的代价函数值。

**中文说明**: 近似比衡量QAOA输出解的质量与最优解之间的比值，$r=1$ 表示达到精确最优。

**来源**: Farhi, Goldstone, Gutmann, arXiv:1411.4028 (2014). 对MaxCut在 $P=1$ 时 $r \geq 0.6924$。

---

## F5.8 贫瘠高原 (Barren Plateau)

$$\text{Var}\left[\frac{\partial C}{\partial \theta_k}\right] \leq F(n), \quad F(n) \in O\left(\frac{1}{2^n}\right)$$

对足够深的随机参数化电路，代价函数梯度的方差随量子比特数 $n$ 指数衰减。

**中文说明**: 贫瘠高原现象指随机初始化的深层变分电路中，梯度以指数速率趋近于零，导致基于梯度的优化实际不可行。

**来源**: McClean et al., *Nat. Commun.* **9**, 4812 (2018).

---

## F5.9 硬件高效拟设结构 (Hardware-Efficient Ansatz)

$$U(\boldsymbol{\theta}) = \prod_{l=1}^{L} \left[ W_l(\boldsymbol{\theta}_l) \cdot V_l \right]$$

其中 $W_l(\boldsymbol{\theta}_l) = \bigotimes_{i=1}^{n} R_{Y}(\theta_{l,i}^{(1)}) R_{Z}(\theta_{l,i}^{(2)})$ 为单比特参数化旋转层，$V_l$ 为固定的纠缠层（如相邻CNOT链）。

**中文说明**: 硬件高效拟设按照实际量子硬件的连接拓扑设计，交替单比特旋转与纠缠层，参数数量为 $O(nL)$。

**来源**: Kandala et al., *Nature* **549**, 242 (2017).

---

## F5.10 量子自然梯度 (Quantum Natural Gradient)

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \, F^{-1}(\boldsymbol{\theta}_t) \, \nabla_{\boldsymbol{\theta}} C(\boldsymbol{\theta}_t)$$

其中 $F(\boldsymbol{\theta})$ 为量子Fisher信息矩阵，$\eta$ 为学习率。

**中文说明**: 量子自然梯度用Fisher信息矩阵的逆对梯度进行预处理，使参数更新遵循量子态空间的黎曼几何结构，加速收敛。

**来源**: Stokes et al., *Quantum* **4**, 269 (2020).

---

## F5.11 量子Fisher信息矩阵 (Quantum Fisher Information Matrix)

$$F_{ij}(\boldsymbol{\theta}) = \text{Re}\left[\langle \partial_i \psi(\boldsymbol{\theta}) | \partial_j \psi(\boldsymbol{\theta}) \rangle - \langle \partial_i \psi(\boldsymbol{\theta}) | \psi(\boldsymbol{\theta}) \rangle \langle \psi(\boldsymbol{\theta}) | \partial_j \psi(\boldsymbol{\theta}) \rangle\right]$$

其中 $|\partial_i \psi\rangle \equiv \frac{\partial}{\partial \theta_i}|\psi(\boldsymbol{\theta})\rangle$。

**中文说明**: 量子Fisher信息矩阵是参数化量子态空间上Fubini-Study度量的实部，刻画了参数微小变化引起的态变化的几何结构。

**来源**: Stokes et al., *Quantum* **4**, 269 (2020); Provost & Vallee, *Commun. Math. Phys.* **76**, 289 (1980).

---

## F5.12 经典影子估计 (Classical Shadow Estimation)

给定未知量子态 $\rho$，经典影子协议：
1. 对 $\rho$ 施加随机幺正 $U$ （从某酉群采样）
2. 测量得到经典比特串 $|b\rangle$
3. 构造单次快照：$\hat{\rho} = \mathcal{M}^{-1}(U^\dagger |b\rangle\langle b| U)$

$$\hat{o}_i = \text{tr}(O_i \hat{\rho}), \quad \text{需要 } T = O\!\left(\frac{\log M}{\epsilon^2} \cdot \max_i \|O_i\|_{\text{shadow}}^2\right) \text{ 次测量}$$

其中 $\|O\|_{\text{shadow}}^2$ 为shadow范数，$M$ 为待估计观测量的数目。

**中文说明**: 经典影子方法用少量随机测量数据高效估计多个观测量的期望值，测量次数仅对观测量数目取对数依赖。

**来源**: Huang, Kueng, Preskill, *Nat. Phys.* **16**, 1050 (2020).

---

## 公式速查表

| 编号 | 名称 | 核心表达式 | 应用 |
|------|------|-----------|------|
| F5.1 | 变分原理 | $E_0 \leq \langle\psi(\theta)\|H\|\psi(\theta)\rangle$ | VQE理论基础 |
| F5.2 | VQE代价函数 | $C(\theta) = \sum_i c_i \langle P_i \rangle$ | 能量估计 |
| F5.3 | 参数平移规则 | $\partial_\theta \langle H\rangle = \frac{1}{2}[\langle H\rangle_+ - \langle H\rangle_-]$ | 梯度计算 |
| F5.4 | QAOA拟设 | $\prod_p e^{-i\beta_p H_M} e^{-i\gamma_p H_C}\|+\rangle^n$ | 组合优化 |
| F5.5 | 混合哈密顿量 | $H_M = \sum_i X_i$ | QAOA搜索驱动 |
| F5.6 | MaxCut代价 | $H_C = \frac{1}{2}\sum_{(i,j)} (I - Z_iZ_j)$ | MaxCut编码 |
| F5.7 | 近似比 | $r = \langle H_C\rangle / C_{\max}$ | 解质量评估 |
| F5.8 | 贫瘠高原 | $\text{Var}[\partial_k C] \in O(2^{-n})$ | 可训练性分析 |
| F5.9 | 硬件高效拟设 | $\prod_l [W_l(\theta_l) \cdot V_l]$ | 电路设计 |
| F5.10 | 量子自然梯度 | $\theta_{t+1} = \theta_t - \eta F^{-1}\nabla C$ | 优化加速 |
| F5.11 | QFI矩阵 | $F_{ij} = \text{Re}[\langle\partial_i\psi\|\partial_j\psi\rangle - \cdots]$ | 几何度量 |
| F5.12 | 经典影子 | $T = O(\log M / \epsilon^2)$ | 高效测量 |

---

## F5.13 QAOA单调性与极限收敛 (QAOA Monotonicity and Limit)

$$M_p \geq M_{p-1}, \quad \lim_{p \to \infty} M_p = \max_z C(z)$$

其中 $M_p = \max_{\boldsymbol{\gamma}, \boldsymbol{\beta}} F_p(\boldsymbol{\gamma}, \boldsymbol{\beta})$。

**中文说明**: QAOA最优期望值随层数单调不减，且在无穷层极限下收敛到精确最优解（通过绝热定理+Trotter化证明）。

**来源**: **[Farhi et al. 2014, Eq.(10)-(11)]**

---

## F5.14 QAOA方差集中界 (QAOA Variance Concentration Bound)

$$\text{Var}[C(z)] \leq 2 \left[\frac{(v-1)^{2p+2} - 1}{(v-1) - 1}\right] \cdot m$$

对度为 $v$ 的正则图、$p$ 层QAOA、$m$ 条边。标准差为 $O(\sqrt{m})$。

**中文说明**: QAOA输出的代价函数值集中在其均值附近，方差被图的度和QAOA层数控制。

**来源**: **[Farhi et al. 2014, Eq.(31)]**

---

## F5.15 VQA通用代价函数 (General VQA Cost Function)

$$C(\vec{\theta}) = \sum_k f_k\left(\text{tr}[O_k U(\vec{\theta}) \rho_k U^\dagger(\vec{\theta})]\right)$$

**中文说明**: 变分量子算法的通用代价函数形式——将参数化酉作用于输入态后测量可观测量，再经函数 $f_k$ 组合。

**来源**: **[Cerezo et al. 2021, Eq.(2)]**

---

## F5.16 拟设表达能力度量 (Ansatz Expressibility Measure)

$$\varepsilon_{\mathbb{U}} := \left\|\int_{\text{Haar}} dV \, V^{\otimes 2}(\cdot)(V^\dagger)^{\otimes 2} - \int_{\mathbb{U}} dU \, U^{\otimes 2}(\cdot)(U^\dagger)^{\otimes 2}\right\|_2$$

$\varepsilon = 0$ 对应最大表达力（2-设计），但同时意味着贫瘠高原。

**中文说明**: 拟设表达能力通过其输出分布与Haar随机分布的二阶差异量化。表达能力越高（$\varepsilon$ 越小），越接近2-设计，梯度消失越严重。

**来源**: **[Tilly et al. 2022, §6]**, Sim et al. (2019), Holmes et al. (2022)

---

## F5.17 虚时间演化 (Imaginary Time Evolution)

$$|\psi(\tau)\rangle = A(\tau) e^{-H\tau} |\psi(0)\rangle, \quad \tau \to \infty \implies |\psi\rangle \to |E_0\rangle$$

**中文说明**: 虚时间演化将量子态投影到基态。变分虚时间演化等价于量子自然梯度下降。

**来源**: **[Tilly et al. 2022, §7]**, McArdle et al. (2019), Stokes et al. (2020)

---

## 公式速查表（续）

| 编号 | 名称 | 核心表达式 | 应用 |
|------|------|-----------|------|
| F5.13 | QAOA极限收敛 | $\lim_{p\to\infty} M_p = \max_z C(z)$ | QAOA理论完备性 |
| F5.14 | QAOA方差集中 | $\text{Var}[C] \leq O((v-1)^{2p+2} m)$ | 采样效率 |
| F5.15 | VQA通用代价 | $C(\theta) = \sum_k f_k(\text{tr}[O_k U\rho U^\dagger])$ | VQA框架 |
| F5.16 | 表达能力度量 | $\varepsilon = \|\text{Haar} - \mathbb{U}\|$ | 拟设设计 |
| F5.17 | 虚时间演化 | $|\psi(\tau)\rangle \propto e^{-H\tau}|\psi(0)\rangle$ | 基态制备 |
