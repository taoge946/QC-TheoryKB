# ZX-Calculus Basics

> **Tags**: `zx-calculus`, `quantum-circuits`, `graphical-language`, `spiders`, `tensor-network`

## Statement

ZX 演算（ZX-Calculus）是一种用于推理量子计算的图形化语言。它将量子电路和量子态表示为由两类基本节点（Z-蜘蛛和 X-蜘蛛）组成的图，通过一组重写规则进行等价变换。与量子电路不同，ZX 图只关心**拓扑连接性**（哪些节点相连），而不关心线的几何排布。ZX 演算对量子比特量子力学是**完备**的：任何通过矩阵计算可证的等式都可以纯粹用图形重写规则来证明。

## Prerequisites

- **线性代数**：张量积、线性映射、Dirac 记号
- **量子计算基础**：量子比特、量子门（H, S, T, CNOT, CZ）
- **基本范畴论概念**（可选）：严格对称幺半范畴

---

## Derivation

### Step 1: Generators of the ZX-Calculus **[Coecke & Duncan, arXiv:0906.4725, Sec.3; van de Wetering, arXiv:2012.13966, Sec.2]**

ZX 演算的图（ZX-diagram）由以下**生成元（generators）**通过组合构成：

**1. Z-蜘蛛（Z-spider，绿色节点）**：具有 $n$ 个输入和 $m$ 个输出，带相位参数 $\alpha \in [0, 2\pi)$。

其对应的线性映射为：

$$Z_\alpha^{m,n} : (\mathbb{C}^2)^{\otimes n} \to (\mathbb{C}^2)^{\otimes m}$$

$$Z_\alpha^{m,n} = |0\rangle^{\otimes m}\langle 0|^{\otimes n} + e^{i\alpha} |1\rangle^{\otimes m}\langle 1|^{\otimes n}$$

特例：
- $Z_0^{1,1} = |0\rangle\langle 0| + |1\rangle\langle 1| = I$（恒等映射）
- $Z_\alpha^{1,0} = |0\rangle + e^{i\alpha}|1\rangle$（量子态，非归一化）
- $Z_\alpha^{0,1} = \langle 0| + e^{i\alpha}\langle 1|$（效应/测量）
- $Z_0^{1,2} = |0\rangle\langle 00| + |1\rangle\langle 11|$（$\delta$-复制）
- $Z_0^{2,1} = |00\rangle\langle 0| + |11\rangle\langle 1|$（$\delta$-合并）
- $Z_\pi^{1,1} = |0\rangle\langle 0| - |1\rangle\langle 1| = Z$（Pauli-Z）
- $Z_{\pi/2}^{1,1} = |0\rangle\langle 0| + i|1\rangle\langle 1| = S$（S-gate）
- $Z_{\pi/4}^{1,1} = |0\rangle\langle 0| + e^{i\pi/4}|1\rangle\langle 1| = T$（T-gate）

**2. X-蜘蛛（X-spider，红色节点）**：与 Z-蜘蛛完全对偶，使用 Hadamard 基。

$$X_\alpha^{m,n} = |{+}\rangle^{\otimes m}\langle{+}|^{\otimes n} + e^{i\alpha} |{-}\rangle^{\otimes m}\langle{-}|^{\otimes n}$$

其中 $|{\pm}\rangle = \frac{1}{\sqrt{2}}(|0\rangle \pm |1\rangle)$。

特例：
- $X_\pi^{1,1} = |{+}\rangle\langle{+}| - |{-}\rangle\langle{-}| = X$（Pauli-X）
- $X_0^{1,2} = |{+}\rangle\langle{+}{+}| + |{-}\rangle\langle{-}{-}|$（X 基复制）

**3. Hadamard 门（黄色方框）**：

$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = |{+}\rangle\langle 0| + |{-}\rangle\langle 1|$$

**4. Wire（线/导线）**：表示恒等映射 $I : \mathbb{C}^2 \to \mathbb{C}^2$。

**5. Empty diagram（空图）**：表示标量 $1 \in \mathbb{C}$。

### Step 2: Composition Operations **[van de Wetering, arXiv:2012.13966, Sec.2.1]**

ZX 图通过两种组合操作构建：

**顺序组合（Sequential composition, $\circ$）**：将图 $D_1$ 的输出连接到 $D_2$ 的输入。对应线性映射的复合（矩阵乘法）：

$$\llbracket D_2 \circ D_1 \rrbracket = \llbracket D_2 \rrbracket \cdot \llbracket D_1 \rrbracket$$

**并行组合（Parallel composition, $\otimes$）**：将两个图 $D_1$ 和 $D_2$ 并排放置。对应线性映射的张量积：

$$\llbracket D_1 \otimes D_2 \rrbracket = \llbracket D_1 \rrbracket \otimes \llbracket D_2 \rrbracket$$

**关键性质**：ZX 图遵循**只有连接性重要（only connectivity matters）**的原则 **[van de Wetering, arXiv:2012.13966, Sec.2.2]**。即：

> 对于任何 ZX 图，只要保持蜘蛛之间的连接关系不变，线的几何排布（弯曲、交叉、上下左右位置）不影响所表示的线性映射。

这与量子电路的严格"从左到右"顺序形成鲜明对比，也是 ZX 演算比电路表示更灵活的根本原因。

### Step 3: Spider Notation and Phase Convention **[van de Wetering, arXiv:2012.13966, Sec.2]**

**蜘蛛的图形表示约定**：

| 符号 | 图形 | 含义 |
|------|------|------|
| Z-蜘蛛 | 绿色圆圈，标注 $\alpha$ | $Z_\alpha^{m,n}$ |
| X-蜘蛛 | 红色圆圈，标注 $\alpha$ | $X_\alpha^{m,n}$ |
| Hadamard | 黄色方框 $\boxed{H}$ | Hadamard 门 |
| Hadamard 边 | 蓝色虚线 | 两个蜘蛛之间接 Hadamard |
| 无标注蜘蛛 | 无相位标记 | $\alpha = 0$ |

**相位约定**：
- 相位 $\alpha$ 通常以 $\pi$ 的倍数表示，例如 $\frac{\pi}{2}$ 写为 $\frac{\pi}{2}$ 或简写为 $\frac{1}{2}$
- 负相位 $-\alpha$ 等价于 $2\pi - \alpha$
- 相位运算 modulo $2\pi$

### Step 4: Standard Quantum Gates in ZX **[van de Wetering, arXiv:2012.13966, Sec.2.3]**

任何量子电路都可以翻译为 ZX 图。常见门的分解：

**单量子比特门**：

$$R_z(\alpha) = Z_\alpha^{1,1} = |0\rangle\langle 0| + e^{i\alpha}|1\rangle\langle 1| \quad \text{（Z-旋转 = 1入1出 Z-蜘蛛）}$$

$$R_x(\alpha) = X_\alpha^{1,1} = |{+}\rangle\langle{+}| + e^{i\alpha}|{-}\rangle\langle{-}| \quad \text{（X-旋转 = 1入1出 X-蜘蛛）}$$

$$Z = Z_\pi^{1,1}, \quad X = X_\pi^{1,1}, \quad S = Z_{\pi/2}^{1,1}, \quad T = Z_{\pi/4}^{1,1}$$

$$H = Z_{\pi/2}^{1,1} \circ X_{\pi/2}^{1,1} \circ Z_{\pi/2}^{1,1} \quad \text{（Euler 分解，忽略全局相位）}$$

**双量子比特门**：

$$\text{CNOT} = (I \otimes X_0^{2,1}) \circ (Z_0^{1,2} \otimes I)$$

即控制比特通过 Z-蜘蛛复制（$|0\rangle \to |00\rangle, |1\rangle \to |11\rangle$），然后一个副本作为 X-蜘蛛的输入与目标比特合并（XOR 操作）。

$$CZ = (I \otimes H) \circ \text{CNOT} \circ (I \otimes H)$$

在 ZX 图中，CZ 表示为两个 Z-蜘蛛通过一条 Hadamard 边相连。

**SWAP 门**：三个 CNOT 组成，或在 ZX 图中简单地交换两条线（因为只有连接性重要）。

### Step 5: Interpretation as Linear Maps **[Coecke & Duncan, arXiv:0906.4725, Sec.3; van de Wetering, arXiv:2012.13966, Sec.2.1]**

ZX 图 $D$ 的**语义（interpretation）** $\llbracket D \rrbracket$ 是一个线性映射，通过以下方式计算：

1. 每个生成元（蜘蛛、Hadamard、线）对应其矩阵
2. 顺序组合对应矩阵乘法
3. 并行组合对应 Kronecker 积
4. 弯曲的线（cup/cap）对应 Bell 态 $\sum_i |ii\rangle$ 和 $\sum_i \langle ii|$

**定理**（语义保持性）：ZX 重写规则保持语义不变。即，若 $D_1 \to D_2$ 是一条重写规则，则 $\llbracket D_1 \rrbracket = \llbracket D_2 \rrbracket$（可能差一个非零标量）。

### Step 6: ZX vs Circuit Model — Key Differences **[van de Wetering, arXiv:2012.13966, Sec.1]**

| 特性 | 量子电路 | ZX 图 |
|------|---------|------|
| 结构约束 | 严格分层（从左到右） | 任意拓扑 |
| 基本单元 | 固定门集（H, S, T, CNOT...） | 两类蜘蛛 + Hadamard |
| 等价判定 | 无已知高效方法 | 重写规则系统 |
| 完备性 | N/A（无重写规则） | 对量子力学完备 |
| 开放线 | 输入在左、输出在右 | 无方向限制 |
| 优化 | 局部门替换（peephole） | 全局图变换 |

---

## Key Results

1. ZX 图由 Z-蜘蛛、X-蜘蛛、Hadamard 门和线四种生成元组成
2. 每个 ZX 图对应一个唯一的线性映射（模标量）
3. ZX 图只关心拓扑连接性，不关心几何排布
4. 任何量子电路都可以翻译为 ZX 图，反之需要满足 gflow 条件
5. ZX 演算比电路模型更灵活，允许全局化简

## References

- [1] Coecke, B. & Duncan, R. "Interacting Quantum Observables: Categorical Algebra and Diagrammatics." New J. Phys. 13, 043016 (2011). arXiv:0906.4725
- [2] van de Wetering, J. "ZX-calculus for the working quantum computer scientist." arXiv:2012.13966 (2020)
- [3] Kissinger, A. & van de Wetering, J. "PyZX: Large Scale Automated Diagrammatic Reasoning." arXiv:1904.04735 (2019)
