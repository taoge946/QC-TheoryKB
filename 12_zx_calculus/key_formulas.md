# Chapter 12: ZX-Calculus - Key Formulas

> ZX 演算（ZX-Calculus）核心公式速查表。所有公式均使用 LaTeX 记号，解释使用中文。

---

## 基本定义

### F12.1: Z-Spider Definition (Z-蜘蛛的线性映射)

$$\tikz{Z}_\alpha^{m,n} := |0\rangle^{\otimes m}\langle 0|^{\otimes n} + e^{i\alpha} |1\rangle^{\otimes m}\langle 1|^{\otimes n}$$

Z-蜘蛛（绿色节点）是 ZX 演算的基本生成元之一。它是一个具有 $n$ 个输入和 $m$ 个输出的线性映射，参数 $\alpha \in [0, 2\pi)$ 称为相位（phase）。当 $\alpha = 0$ 时简称为无相位蜘蛛。零输入零输出的 Z-蜘蛛等价于标量 $1 + e^{i\alpha}$。

**Source**: [derivations/zx_basics.md] | **[van de Wetering, arXiv:2012.13966, Eq.(1), Sec.2]**; Coecke & Duncan, arXiv:0906.4725

---

### F12.2: X-Spider Definition (X-蜘蛛的线性映射)

$$\tikz{X}_\alpha^{m,n} := |{+}\rangle^{\otimes m}\langle{+}|^{\otimes n} + e^{i\alpha} |{-}\rangle^{\otimes m}\langle{-}|^{\otimes n}$$

X-蜘蛛（红色节点）是 ZX 演算的另一个基本生成元。其定义与 Z-蜘蛛完全对偶，将计算基 $\{|0\rangle, |1\rangle\}$ 替换为 Hadamard 基 $\{|+\rangle, |-\rangle\}$。等价地，X-蜘蛛等于 Z-蜘蛛的每条腿上接一个 Hadamard 门。

**Source**: [derivations/zx_basics.md] | **[van de Wetering, arXiv:2012.13966, Eq.(2), Sec.2]**

---

## 重写规则（Rewrite Rules）

### F12.3: Spider Fusion Rule (蜘蛛融合规则)

$$\tikz{Z}_\alpha \circ \tikz{Z}_\beta = \tikz{Z}_{\alpha + \beta}$$

更精确地：两个相连的同色蜘蛛可以融合为一个蜘蛛，相位相加。若 Z-蜘蛛 $Z_\alpha^{m_1, k}$ 和 $Z_\beta^{k, n_1}$ 通过 $k$ 条线相连，则融合后得到 $Z_{\alpha+\beta}^{m_1, n_1}$。此规则是 ZX 演算中最常用的化简规则。对 X-蜘蛛同样成立。

**Source**: [derivations/zx_rewrite_rules.md] | **[van de Wetering, arXiv:2012.13966, Rule (f)]**; Coecke & Duncan, arXiv:0906.4725

---

### F12.4: Color Change / Hadamard Rule (颜色变换规则)

$$H^{\otimes m} \circ \tikz{Z}_\alpha^{m,n} \circ H^{\otimes n} = \tikz{X}_\alpha^{m,n}$$

在 Z-蜘蛛的每条输入和输出线上放置 Hadamard 门，等价于将其变为 X-蜘蛛（相位不变），反之亦然。这体现了 Z 基和 X 基之间的 Hadamard 对偶性。在图中，Hadamard 用黄色方框（$\boxed{H}$）表示。

**Source**: [derivations/zx_rewrite_rules.md] | **[van de Wetering, arXiv:2012.13966, Rule (h)]**

---

### F12.5: Bialgebra Rule (双代数规则)

$$\tikz{Z}^{2,1}_0 \circ \tikz{X}^{1,2}_0 = (\tikz{X}^{1,2}_0 \otimes \tikz{X}^{1,2}_0) \circ \tikz{X}^{2,2}_0 \circ (\tikz{Z}^{2,1}_0 \otimes \tikz{Z}^{2,1}_0)$$

等价地用图描述：一个无相位绿色蜘蛛（1入2出）接一个无相位红色蜘蛛（2入1出），等价于四个蜘蛛组成的"交叉"结构。此规则表达了 Z 和 X 可观测量之间的**强互补性（strong complementarity）**。它也可以简述为：不同颜色的无相位蜘蛛"滑过"彼此时会产生所有可能的连接。

**Source**: [derivations/zx_rewrite_rules.md] | **[van de Wetering, arXiv:2012.13966, Rule (b)]**; Coecke & Duncan, arXiv:0906.4725, Sec.5

---

### F12.6: Pi-Copy Rule ($\pi$-复制规则)

$$\tikz{X}^{1,m}_\pi \circ \tikz{Z}^{1,1}_\alpha = \tikz{Z}^{1,1}_{-\alpha} \circ \tikz{X}^{1,m}_\pi$$

一个 $\pi$ 相位的 X-蜘蛛与 Z-蜘蛛相连时，$\pi$ 相位会"复制"到 Z-蜘蛛的每条输出线上，并将 Z-蜘蛛的相位取反。等价地：$\pi$ 相位的蜘蛛穿过不同颜色的蜘蛛时，会将该蜘蛛的相位取负。此规则是 $X Z X = -Z$ 的图形化推广。

**Source**: [derivations/zx_rewrite_rules.md] | **[van de Wetering, arXiv:2012.13966, Rule ($\pi$)]**

---

### F12.7: Identity Removal (恒等线移除)

$$\tikz{Z}^{1,1}_0 = \text{wire} \quad (\text{即直线})$$

无相位、1入1出的蜘蛛等价于一条直线（恒等映射），可直接删除。更一般地，无相位、2入0出的蜘蛛等价于 cup（Bell 态），无相位、0入2出等价于 cap。

**Source**: [derivations/zx_rewrite_rules.md] | **[van de Wetering, arXiv:2012.13966, Rule (id)]**

---

### F12.8: Euler Decomposition of Hadamard (Hadamard 的 Euler 分解)

$$H = \tikz{Z}_{\pi/2} \circ \tikz{X}_{\pi/2} \circ \tikz{Z}_{\pi/2}$$

Hadamard 门可以分解为三个蜘蛛的串联：$Z_{\pi/2}$, $X_{\pi/2}$, $Z_{\pi/2}$（忽略全局相位）。这对应于经典的 Euler 分解 $H = e^{i\pi/4} R_z(\pi/2) R_x(\pi/2) R_z(\pi/2)$。此分解使得 ZX 图中只需使用蜘蛛就可以消除所有 Hadamard 门。

**Source**: [derivations/zx_rewrite_rules.md] | **[van de Wetering, arXiv:2012.13966, Sec.3.2]**

---

## 高级概念

### F12.9: Phase Gadget (相位 Gadget)

$$\text{PhaseGadget}(\alpha, n) = \sum_{x \in \{0,1\}^n} e^{i\alpha \cdot \text{parity}(x)} |x\rangle\langle x| = \exp\left(-i\frac{\alpha}{2} Z^{\otimes n}\right)$$

在 ZX 图中，相位 gadget 表示为一个带 $\alpha$ 相位的 Z-蜘蛛通过 Hadamard 线连接到 $n$ 条主线上。它对计算基态施加依赖于奇偶性的相位：当输入比特串的奇偶性为奇时施加 $e^{i\alpha}$ 相位。相位 gadget 是 ZX 电路优化中的核心工具，因为它们可以自由地沿电路移动和合并。

**Source**: [derivations/zx_circuit_optimization.md] | **[van de Wetering, arXiv:2012.13966, Sec.4.1]**; Kissinger & van de Wetering, arXiv:1904.04735

---

### F12.10: Graph State Representation (图态的 ZX 表示)

$$|G\rangle = \prod_{(i,j) \in E} CZ_{ij} |{+}\rangle^{\otimes n} \quad \longleftrightarrow \quad \text{全绿无相位蜘蛛 + Hadamard 边}$$

图态 $|G\rangle$（由图 $G = (V, E)$ 定义）在 ZX 演算中表示为：每个顶点对应一个无相位 Z-蜘蛛（1个输出），图的每条边对应一个 Hadamard 连接。这是因为 $CZ = $ Hadamard 在一条线上 + CNOT 的 ZX 分解的直接推论。图态是 Clifford 电路化简和基于测量的量子计算（MBQC）的基础。

**Source**: [derivations/zx_graph_states.md] | **[van de Wetering, arXiv:2012.13966, Sec.5.1]**

---

### F12.11: CNOT Decomposition in ZX (CNOT 的 ZX 分解)

$$\text{CNOT} = \tikz{Z}^{1,2}_0 \circ \tikz{X}^{2,1}_0 \quad \text{(控制比特用 Z-蜘蛛复制，目标比特用 X-蜘蛛合并)}$$

CNOT 门在 ZX 演算中分解为一个无相位 Z-蜘蛛（1入2出，作为复制）和一个无相位 X-蜘蛛（2入1出，作为 XOR/加法），通过一条线连接。类似地，$CZ$ 门分解为两个 Z-蜘蛛通过一条 Hadamard 线连接。这些分解使得 ZX 演算能够直接处理量子电路。

**Source**: [derivations/zx_basics.md] | **[van de Wetering, arXiv:2012.13966, Sec.2.3]**

---

### F12.12: Completeness Theorem (完备性定理)

**定理**：ZX 演算对于量子比特量子力学是**完备**的。即：对于任意两个表示相同线性映射的 ZX 图 $D_1$ 和 $D_2$，存在一个仅使用 ZX 重写规则的推导序列将 $D_1$ 变换为 $D_2$。

形式化地：

$$\llbracket D_1 \rrbracket = \llbracket D_2 \rrbracket \implies D_1 \stackrel{\text{ZX rules}}{\longleftrightarrow} D_2$$

完备性结果的历史：(1) Backens 2014 证明了 ZX 对稳定子量子力学（Clifford 片段）的完备性；(2) Backens 2015 证明了单量子比特 Clifford+T 的完备性；(3) Hadzihasanovic, Ng, Wang 2018 和 Vilmart 2019 独立证明了对一般量子力学的完备性。

**Source**: [derivations/zx_rewrite_rules.md] | **[Backens, arXiv:1307.7025, Theorem 1]**; Hadzihasanovic et al., arXiv:1805.05631; Vilmart, arXiv:1812.09114; [van de Wetering, arXiv:2012.13966, Sec.6]

---

### F12.13: Local Complementation (局部互补)

对于图态 $|G\rangle$，围绕顶点 $v$ 的局部互补操作 $\tau_v$ 将 $v$ 的邻居子图的边集取补：

$$\tau_v(G): \quad E' = E \triangle \{ (i,j) : i,j \in N(v), i \neq j \}$$

其中 $\triangle$ 是对称差，$N(v)$ 是 $v$ 的邻居集。在 ZX 演算中，局部互补对应于在顶点 $v$ 上施加 $e^{-i\frac{\pi}{4}X}$，并在其所有邻居上施加 $e^{i\frac{\pi}{4}Z}$：

$$\tau_v: \quad |G'\rangle = \left(\prod_{u \in N(v)} \sqrt{iZ_u}\right) \sqrt{-iX_v} |G\rangle$$

**Source**: [derivations/zx_graph_states.md] | **[van de Wetering, arXiv:2012.13966, Sec.5.2]**; Duncan et al., arXiv:1902.03178, Sec.4

---

### F12.14: Pivot Rule (枢轴操作)

对于图中相邻的两个顶点 $u, v$，枢轴操作等价于连续三次局部互补：

$$\wedge_{uv}(G) = \tau_u \circ \tau_v \circ \tau_u (G)$$

枢轴操作的效果：(1) $u$ 和 $v$ 各自的独有邻居集交换连接关系；(2) $u$ 和 $v$ 之间的边可能改变。在 ZX 电路化简中，局部互补和枢轴操作构成了 Clifford 电路化简的**完备**图变换集。

**Source**: [derivations/zx_graph_states.md] | **[Duncan et al., arXiv:1902.03178, Sec.4]**; [van de Wetering, arXiv:2012.13966, Sec.5.2]

---

### F12.15: ZX to Circuit Extraction (ZX 图到电路的提取)

**输入**：graph-like ZX 图（所有蜘蛛为 Z 类型，边为 Hadamard 边）

**步骤**：
1. **验证 gflow**：检查化简后的 ZX 图是否具有广义流（generalised flow, gflow）
2. **gflow 排序**：按 gflow 的偏序关系排列蜘蛛
3. **逐层提取**：从输出端开始，使用 CNOT 行操作将每层蜘蛛提取为电路门
4. **相位提取**：将蜘蛛的相位转化为 $R_z$ 旋转门
5. **Hadamard 处理**：剩余的 Hadamard 边转化为 $H$ 门

**条件**：提取算法成功当且仅当 ZX 图具有 gflow。对于由量子电路翻译而来的 ZX 图，gflow 始终存在（因此算法必定成功）。

**Source**: [derivations/zx_circuit_optimization.md] | **[Duncan et al., arXiv:1902.03178, Sec.5, Theorem 5.4]**; Backens et al., arXiv:2003.01674

---
