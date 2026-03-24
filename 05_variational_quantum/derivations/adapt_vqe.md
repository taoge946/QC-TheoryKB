# ADAPT-VQE与自适应拟设理论

> Adaptive Ansatz Construction: ADAPT-VQE and Related Methods
> 涵盖自适应拟设构造的算法框架、梯度选择准则、与贫瘠高原的关系。
> 来源：**[Tilly et al. 2022, §6.2]**, **[Cerezo et al. 2021, §2.2, §4.1]**

---

## 1. ADAPT-VQE算法框架 (ADAPT-VQE Algorithm)

> 基于 **[Tilly et al. 2022, §6.2]**。

### 1.1 动机

固定结构拟设（如UCCSD、HEA）存在两难：
- 过小的拟设无法表达目标态
- 过大的拟设导致参数过多、贫瘠高原、和不必要的电路深度

ADAPT-VQE（Grimsley et al. 2019）通过**迭代选择**算符池中梯度最大的算符来动态构建拟设。**[Tilly et al. 2022, §6.2]**

### 1.2 算法步骤

给定算符池 $\mathcal{P} = \{\hat{A}_1, \hat{A}_2, \ldots, \hat{A}_K\}$（通常取费米子激发算符的反Hermitian形式），ADAPT-VQE的迭代过程为：

1. **初始化**：$|\psi^{(0)}\rangle = |\text{HF}\rangle$（Hartree-Fock态或其他参考态），拟设 $U^{(0)} = I$
2. **梯度评估**：对所有池中算符 $\hat{A}_k$，计算梯度

$$g_k = \frac{\partial}{\partial \theta_k} \langle \psi^{(n)} | e^{-\theta_k \hat{A}_k} H e^{\theta_k \hat{A}_k} | \psi^{(n)} \rangle \bigg|_{\theta_k = 0} = \langle \psi^{(n)} | [H, \hat{A}_k] | \psi^{(n)} \rangle$$

3. **算符选择**：选择 $|g_k|$ 最大的算符 $\hat{A}_{k^*}$
4. **拟设更新**：$U^{(n+1)}(\boldsymbol{\theta}) = e^{\theta_{n+1} \hat{A}_{k^*}} U^{(n)}(\boldsymbol{\theta}_{1:n})$
5. **参数优化**：优化所有参数 $\boldsymbol{\theta}_{1:n+1}$（VQE）
6. **收敛检查**：若 $\max_k |g_k| < \epsilon$，停止；否则返回步骤2

### 1.3 算符池选择 **[Tilly et al. 2022, §6.2]**

常用池：
- **Generalized Singles and Doubles (GSD)**：$\hat{A}_{pq} = a_p^\dagger a_q - a_q^\dagger a_p$，$\hat{A}_{pqrs} = a_p^\dagger a_q^\dagger a_r a_s - \text{h.c.}$
- **Qubit pool**：直接使用Pauli串作为生成元（避免费米子→量子比特映射的开销）
- **Hardware-efficient pool**：适配特定硬件拓扑的门集

---

## 2. ADAPT-VQE变体 (Variants)

> 基于 **[Tilly et al. 2022, §6.2]**。

### 2.1 Qubit-ADAPT-VQE

使用量子比特级别的算符池（而非费米子算符），每次添加的电路更浅。代价是可能需要更多迭代步数。**[Tilly et al. 2022, §6.2]**

### 2.2 ADAPT-VQE与贫瘠高原的关系

**[Tilly et al. 2022, §6.1]** 指出：自适应拟设对贫瘠高原具有一定天然抵抗力，因为：
1. 拟设从浅层开始逐步增长，避免一开始就陷入2-设计区域
2. 每步选择梯度最大的方向，确保信息量最大化
3. 表达能力按需增长，不会过度参数化

但注意：当目标态的纠缠量很高时，ADAPT-VQE最终仍需要深电路，可能受到噪声诱导贫瘠高原（NIBP）的影响。

---

## 3. 与其他自适应方法的比较

> 基于 **[Cerezo et al. 2021, §2.2]** 和 **[Tilly et al. 2022, §6.2]**。

| 方法 | 池类型 | 每步增量 | 特点 |
|------|--------|---------|------|
| ADAPT-VQE | 费米子GSD | 一个算符 | 化学精度高 |
| Qubit-ADAPT | Pauli串 | 一个Pauli旋转 | 电路更浅 |
| IQEB-VQE | 量子比特激发 | 一个门 | 硬件友好 |
| 分层训练 | 固定拟设 | 一层 | 通用 |

**[Cerezo et al. 2021, §4.1]** 将ADAPT-VQE定位为避免贫瘠高原的策略之一："动态选择最大梯度方向的算符逐步构建拟设"。

---

## 4. 理论保证与开放问题

### 4.1 收敛性

ADAPT-VQE在以下条件下保证收敛到基态（在精确算术下）：
- 算符池生成完整的相关空间
- 初态与基态有非零重叠
- VQE子问题可精确求解

但在有限精度和噪声下，收敛性不保证。**[Tilly et al. 2022, §6.2]**

### 4.2 开放问题

- 最优算符池设计的理论框架
- ADAPT-VQE的总参数量与问题规模的缩放关系（对一般哈密顿量未知）
- 多参考态情况下的自适应策略

---

> **See also**: [vqe_theory.md] | [barren_plateaus.md] | [../key_formulas.md]
