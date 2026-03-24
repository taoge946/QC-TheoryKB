# 热启动与初始化策略

> Warm-Starting Strategies for VQAs: Theory and Methods
> 涵盖经典预计算初始化、参数迁移、恒等初始化、机器学习辅助初始化。
> 来源：**[Cerezo et al. 2021, §4.1]**, **[Tilly et al. 2022, §6.1]**

---

## 1. 动机：随机初始化的问题 (Why Warm-Starting Matters)

> **[Cerezo et al. 2021, §4.1]**, **[Tilly et al. 2022, §6.1]**

随机初始化VQA参数面临两个核心挑战：
1. **贫瘠高原**：随机初始化的深层电路形成近似2-设计，梯度指数消失
2. **局部极小值**：高维非凸景观中随机起点很可能接近低质量的局部极小

热启动（warm-starting）通过智能选择初始参数 $\boldsymbol{\theta}_0$ 来规避这些问题。

---

## 2. QAOA的参数持续模式 (QAOA Parameter Persistence)

> **[Cerezo et al. 2021, §4.1]**

**观察** (Zhou et al. 2018, 引自 **[Cerezo et al. 2021, §4.1]**): QAOA的最优参数在不同图实例间展现**持续模式**（persistent patterns）。基于此观察提出的初始化策略在启发式上优于随机初始化。

**层间迁移**：从 $p$ 层最优参数 $\{(\gamma_l^*, \beta_l^*)\}_{l=1}^p$ 通过线性插值生成 $p+1$ 层的初始参数。

---

## 3. 恒等初始化 (Identity Initialization)

> **[Tilly et al. 2022, §6.1, Grant et al. 2019]**

### 3.1 原理

将拟设分为 $K$ 个深度 $D$ 的块。每块初始化为恒等变换：

$$U_k(\boldsymbol{\theta}_{\text{init}}) = I, \quad \forall k$$

具体方法：每块分为两半，后半部分的参数初始化为前半部分的逆：

$$U_d(\theta_{d,2}^k) W_d = (U_d(\theta_{d,1}^k) W_d)^\dagger$$

### 3.2 理论依据

恒等初始化确保：
- 初始电路不形成2-设计（打破McClean贫瘠高原定理的前提）
- 参数空间搜索从恒等变换附近开始，梯度非零

### 3.3 局限性

- 恒等初始化产生的初始态无纠缠，可能需要额外的随机浅层纠缠
- 对UCC类拟设不直接适用（需要重复某些算符）
- 对HEA一般不能精确实现恒等初始化

**[Tilly et al. 2022, §6.1]**

---

## 4. 经典预计算初始化 (Classical Pre-computation)

> **[Cerezo et al. 2021, §4.1]**

### 4.1 Hartree-Fock初始化 (VQE)

对分子VQE，用经典Hartree-Fock计算获得参考态 $|\text{HF}\rangle$，然后：
- 将UCC拟设的初始参数设为 $\boldsymbol{\theta}_0 = \mathbf{0}$（对应 $e^{0} = I$，初始态即HF态）
- 或用经典耦合簇理论的振幅 $t_{ij}^{ab}$ 作为UCC参数的初始猜测

### 4.2 QAOA的经典预处理

**[Farhi et al. 2014, §2]** 的核心结果：对固定 $p$ 和有界度图，最优QAOA角度可通过**高效经典计算**预先确定，然后直接在量子计算机上使用。

---

## 5. 机器学习辅助初始化 (ML-Assisted Initialization)

> **[Tilly et al. 2022, §6.1]**

### 5.1 FLIP模型

**[Tilly et al. 2022, §6.1, Sauvage et al.]**: FLexible Initializer for arbitrarily-sized Parametrized quantum circuits (FLIP)——训练机器学习模型来识别最适合特定量子电路优化问题族的参数结构。

### 5.2 Beta分布初始化

**[Tilly et al. 2022, §6.1, Kulshrestha & Safro]**: 从Beta分布（而非均匀分布）采样初始参数可减少贫瘠高原的影响。在优化步骤间添加扰动也有助于缓解梯度消失。

---

## 6. 关联参数与降维 (Correlated Parameters)

> **[Cerezo et al. 2021, §4.1]**, **[Tilly et al. 2022, §6.1]**

**[Cerezo et al. 2021, §4.1, Volkoff et al.]**: 通过在拟设中关联参数（空间和时间上），有效降低超参数空间维度，可导致更大的代价函数梯度。

**[Tilly et al. 2022, §6.1, Volkoff et al. 2021]**: 使用时空关联的参数化量子门减少了参数空间维度，增强了对贫瘠高原的抵抗力。

---

## 7. 分层训练 (Layer-wise Training)

> **[Cerezo et al. 2021, §4.1]**, **[Tilly et al. 2022, §6.1]**

逐层训练策略：
1. 训练第1层（浅层电路，梯度良好）
2. 固定第1层，添加并训练第2层
3. 逐层累积
4. 最终可选全局微调

**理论依据** **[Cerezo et al. 2021, §4.1]**: 在第 $l$ 步，有效深度仅为 $l$。当 $l \in O(\log n)$ 时，局部代价函数梯度保持多项式衰减。

**局限** **[Tilly et al. 2022, §6.1, Campos et al. 2021]**: 分层训练可能导致训练能力的突然转变（abrupt transition），即增加新层后可能突然丧失可训练性。

---

## 8. 总结：初始化策略比较

| 策略 | 适用范围 | 优势 | 局限 |
|------|---------|------|------|
| 随机初始化 | 通用 | 简单 | 贫瘠高原风险 |
| 恒等初始化 | 层状拟设 | 避免2-设计 | 需额外纠缠层 |
| HF初始化 | VQE | 物理动机 | 仅限化学问题 |
| 参数迁移 | QAOA/VQE | 利用小系统信息 | 依赖集中现象 |
| ML初始化 | 通用 | 数据驱动 | 需预训练 |
| 分层训练 | 通用 | 渐进增长 | 可能突变 |

---

> **See also**: [barren_plateaus.md] | [vqe_theory.md] | [qaoa_theory.md] | [../key_formulas.md]
