# Topological Measurement-Based Quantum Computation

> **Tags**: `topological-mbqc`, `3d-cluster`, `correlation-surface`, `fault-tolerant`
> **Source**: Primarily from Fujii, K. "Quantum Computation with Topological Codes" (2015), Ch.5

## Statement **[Raussendorf, Harrington & Goyal 2007; Fujii, Ch.5]**

拓扑保护的基于测量的量子计算（Topological MBQC）将拓扑容错量子计算重新表述为三维 cluster state 上的 MBQC。三维中两个空间维度构成表面码，第三个维度对应时间演化。所有操作——真空中的拓扑保护、缺陷编织实现逻辑门、magic state 注入——都通过特定的测量模式实现。该方案是 Raussendorf 等人原始提案的核心。

## Prerequisites

- **MBQC**：[stabilizer_formalism.md] (MBQC section)
- **表面码**：[surface_code_basics.md]
- **链复形**：[../../08_topology/derivations/homology_basics.md]

---

## Part 1: 3D Cluster State [Fujii, Ch.5, §5.1]

> **[Fujii, Ch.5, §5.1]**: 考虑原始立方格子 $\mathcal{L}$ 及其 $\mathbf{Z}_2$ 链复形 $\{C_0, C_1, C_2, C_3\}$，以及对偶立方格子 $\bar{\mathcal{L}}$。量子比特定义在原始和对偶边上（即原始格子的边和面上）。

**稳定子生成元**定义在原始和对偶初等面 $f_m$, $\bar{f}_{m'}$ 上：

$$K_{f_m} = X_{f_m} Z(\partial f_m), \qquad K_{\bar{f}_{m'}} = X_{\bar{f}_{m'}} Z(\partial \bar{f}_{m'})$$

**乘积性质**：

$$K(c_2) \equiv \prod_m K_{f_m}^{z_m} = X(c_2) Z(\partial c_2)$$

且 $K(c_2 + c'_2) = K(c_2)K(c'_2)$。

---

## Part 2: 与表面码的关系 [Fujii, Ch.5, §5.1]

> **[Fujii, Ch.5, §5.1]**: 三维 cluster state 中：
> - 水平面上的 plaquette syndrome 测量 = 生成 $K(f_m)$（水平面）
> - star syndrome 测量 = 生成 $K(\bar{f}_l)$（水平对偶面，含 Hadamard 基变换）
> - 垂直 CZ 门连接相邻层的水平边量子比特
>
> 两个空间维度构成表面码，第三维度为 MBQC 的时间轴。偶数和奇数层分别对应 plaquette 和 star syndrome 测量。

---

## Part 3: 三类区域 [Fujii, Ch.5, §5.2]

> **[Fujii, Ch.5, §5.2]**: 立方格子分为三类区域：

**真空区域 $\mathcal{V}$**：所有量子比特在 $X$ 基测量，拓扑量子纠错保护量子信息。

**缺陷区域 $\mathcal{D}$**：
- 原始缺陷 $D$（一组原始立方体）
- 缺陷内部面量子比特 $Z$ 基测量，边界面量子比特 $X$ 基测量
- 缺陷内边量子比特 $X$ 基测量
- 实现缺陷编织等拓扑操作

**奇异量子比特 $\mathcal{S}$**：位于两缺陷之间，$Y$ 基或 $(X+Y)/\sqrt{2}$ 基测量，用于 magic state 注入。非拓扑保护。

---

## Part 4: 逻辑算子和关联面 [Fujii, Ch.5, §5.3]

### 逻辑量子比特定义

> **[Fujii, Ch.5, §5.3]**: 时间步 $t$ 的逻辑算子：
>
> $$L_Z^{(t)} = Z(c_1), \qquad L_X^{(t)} = X(\overleftarrow{\bar{c}_1})Z(\bar{c}_1)$$
>
> 其中 $c_1$ 是围绕缺陷的原始 1-cycle，$\bar{c}_1$ 是连接两缺陷的对偶 1-chain，$\overleftarrow{\bar{c}_1}$ 是 $t$ 步偶数层上 $\bar{c}_1$ 的左邻对偶面量子比特。

### Identity Gate（恒等门）

> **[Fujii, Ch.5, §5.3]**: 关联面 $c_2$ 上的稳定子 $K(c_2) = Z(\partial c_2)X(c_2)$ 将不同时间步的逻辑算子关联起来。$X$ 基测量后：
>
> $$L_Z^{(t)} \sim L_Z^{(t+1)}, \qquad L_X^{(t)} \sim L_X^{(t+1)}$$
>
> 逻辑信息从时间步 $t$ 传播到 $t+1$，无操作——实现逻辑恒等门。

### 态制备

> **[Fujii, Ch.5, §5.3]**: $Z$ 基态制备：关联面 $K(c_2) = X(c_2)L_Z^{(t)}$，因 $X(c_2)$ 与测量对易，态被 $L_Z^{(t)}$ 稳定化。$X$ 基态制备类似，使用对偶关联面。

### CNOT Gate by Braiding

> **[Fujii, Ch.5, §5.3]**: 原始缺陷绕对偶缺陷编织时，关联面分析给出：
>
> $$L_Z^{(t)} \sim L_Z^{(t')}L'_Z{}^{(t')}, \quad L_X^{(t)} \sim L_X^{(t')}, \quad L'_X{}^{(t)} \sim L_X^{(t')}L'_X{}^{(t')}$$
>
> 这些变换关系等价于 CNOT 门的逻辑算子变换规则。

---

## Part 5: Magic State Injection [Fujii, Ch.5, §5.3]

> **[Fujii, Ch.5, §5.3]**: 奇异量子比特（singular qubit）上的测量实现 magic state 注入。两个关联面给出：
>
> $$K(c_2) = Z(\partial c_2)X(c_2\setminus s)X_s, \quad K(\bar{c}_2) = Z_s Z(\partial\bar{c}_2\setminus s)X(\bar{c}_2)$$

- **$Y$ 基测量**：$K(c_2)K(\bar{c}_2) \simeq L_X^{(t)}L_Z^{(t)} \equiv L_Y^{(t)}$ — 制备逻辑 $Y$ 基态，用于实现 $S$ 门
- **$(X+Y)/\sqrt{2}$ 基测量**：$[K(\bar{c}_2)+K(c_2)K(\bar{c}_2)]/\sqrt{2} \simeq (L_X^{(t)}+L_Y^{(t)})/\sqrt{2}$ — 制备 magic state，用于实现 $T$ 门

奇异量子比特不受拓扑保护（缺陷距离缩短），需通过 magic state distillation 纯化。

---

## Part 6: 3D 拓扑纠错 [Fujii, Ch.5, §5.4]

> **[Fujii, Ch.5, §5.4]**: 真空区域中所有测量为 $X$ 基。每个原始立方体 $q_n$ 的稳定子为 $K(\partial q_n) = \prod_{f_m \in \partial q_n} X_{f_m}$（无 $Z$ 项，因 $\partial\circ\partial q_n = 0$）。
>
> **纠错准则**：若无错误，每个立方体六次 $X$ 基测量结果的奇偶性为偶。错误 $E = Z(\bar{c}_1)$ 导致 $\partial\bar{c}_1$ 上的立方体奇偶性为奇。任务：从奇偶性分布估计 $\bar{c}'_1$，若 $\bar{c}_1 + \bar{c}'_1$ 平凡则成功，非平凡（绕缺陷缠绕）则失败。

> **[Fujii, Ch.5, §5.4]**: 若错误概率小于常数阈值，纠错失败概率随缺陷尺寸和距离指数下降。缺陷边界上的额外奇偶性检查将边界错误简化为二维 toric code 纠错问题。

---

## Part 7: Thermal State Applications [Fujii, Ch.5, §5.5]

> **[Fujii, Ch.5, §5.5]**: 三维 cluster state 的稳定子 Hamiltonian $H_{\rm fc} = -J[\sum_f K(f) + \sum_{\bar{f}} K(\bar{f})]$ 的热态可用于研究量子多体态在有限温度下的计算能力。通过 CZ 变换映射到自由自旋模型的热态，以及与 3D $\mathbf{Z}_2$ 格点规范理论的联系，可以分析拓扑 MBQC 的热稳定性。

---

## Summary

拓扑 MBQC 的完整操作集：

| 操作 | 测量模式 | 拓扑保护 |
|------|---------|---------|
| 恒等门 | 真空 $X$ 基 | 是 |
| $Z$ 基态制备 | 缺陷创建 | 是 |
| $X$ 基态制备 | 缺陷创建+湮灭 | 是 |
| CNOT | 缺陷编织 | 是 |
| $S$ 门 | $Y$ 基注入 + 蒸馏 | 注入点否，蒸馏后是 |
| $T$ 门 | $(X+Y)/\sqrt{2}$ 注入 + 蒸馏 | 注入点否，蒸馏后是 |

所有操作仅需最近邻两量子比特门和单量子比特测量，适合二维量子比特阵列实现。

---

## References

- Raussendorf, R., Harrington, J. & Goyal, K. "Topological fault-tolerance in cluster state quantum computation." New J. Phys. 9, 199 (2007).
- Raussendorf, R. & Harrington, J. "Fault-tolerant quantum computation with high threshold in two dimensions." PRL 98, 190504 (2007).
- Fujii, K. "Quantum Computation with Topological Codes." SpringerBriefs (2015), Ch.5.
