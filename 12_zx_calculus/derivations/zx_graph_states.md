# ZX-Calculus and Graph States

> **Tags**: `zx-calculus`, `graph-states`, `local-complementation`, `pivot`, `mbqc`, `stabilizer`

## Statement

图态（graph states）是一类重要的多量子比特纠缠态，由图的拓扑结构完全决定。在 ZX 演算中，图态有一个特别自然的表示：每个顶点对应一个无相位 Z-蜘蛛，每条边对应一个 Hadamard 连接。ZX 演算中的局部互补（local complementation）和枢轴（pivot）操作恰好对应图态上的核心图变换，这些操作构成了 Clifford 电路化简的完备工具集。

## Prerequisites

- **ZX 基础**：Z-蜘蛛、X-蜘蛛、Hadamard 边（见 [zx_basics.md](zx_basics.md)）
- **ZX 重写规则**：spider fusion, color change, bialgebra（见 [zx_rewrite_rules.md](zx_rewrite_rules.md)）
- **稳定子形式体系**：稳定子态、Clifford 群
- **图论基础**：图、邻接矩阵、邻域

---

## Derivation

### Step 1: Graph States — Definition and ZX Representation **[van de Wetering, arXiv:2012.13966, Sec.5.1; Hein et al., arXiv:quant-ph/0602096]**

**定义**：给定无向图 $G = (V, E)$，其中 $|V| = n$，图态 $|G\rangle$ 定义为：

$$|G\rangle = \prod_{(i,j) \in E} CZ_{ij} \cdot |{+}\rangle^{\otimes n}$$

其中 $CZ_{ij} = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes Z$ 是受控 Z 门。

**等价定义（通过稳定子）**：图态 $|G\rangle$ 是以下 $n$ 个稳定子的共同 $+1$ 特征态：

$$K_v = X_v \prod_{u \in N(v)} Z_u, \quad \forall v \in V$$

其中 $N(v)$ 是顶点 $v$ 的邻域。

**ZX 表示**：在 ZX 演算中，图态 $|G\rangle$ 表示为：

$$|G\rangle \quad \longleftrightarrow \quad \text{每个顶点 } v \in V \text{ 对应 } Z_0^{1,0} \text{（无相位 Z-蜘蛛，1个输出）}$$
$$\text{每条边 } (i,j) \in E \text{ 对应两个蜘蛛之间的 Hadamard 边}$$

**推导**：CZ 门在 ZX 中表示为两个 Z-蜘蛛通过 Hadamard 边相连。$|{+}\rangle = H|0\rangle = X_0^{1,0}$（无相位 X-蜘蛛，作为态）。通过颜色变换规则 (h)，$X_0^{1,0}$ 可以吸收到相邻的 Hadamard 中，最终每个顶点变为 Z-蜘蛛。

### Step 2: Local Clifford Operations on Graph States **[van de Wetering, arXiv:2012.13966, Sec.5.1]**

**定理**（LC + graph state 分类）：任何稳定子态（stabilizer state）都可以表示为一个图态加上每个量子比特上的局部 Clifford 操作。

在 ZX 图中，这意味着任何稳定子态对应一个 graph-like ZX 图，其中每个蜘蛛的相位是 Clifford 相位（$0, \pi/2, \pi, 3\pi/2$ 之一）。

**Clifford 门在 ZX 中的效果**：
- $Z_\alpha$ 旋转（$\alpha$ 为 Clifford 相位）：直接作为蜘蛛的相位
- $H$ 门：在输出线上添加 Hadamard
- $S$ 门：$Z_{\pi/2}^{1,1}$ 蜘蛛
- CNOT：修改图的边结构

### Step 3: Local Complementation in ZX (局部互补) **[van de Wetering, arXiv:2012.13966, Sec.5.2; Duncan et al., arXiv:1902.03178, Sec.4.1]**

**定义**（图论中的局部互补）：对于图 $G = (V,E)$，围绕顶点 $v$ 的局部互补 $\tau_v$ 定义为：

$$\tau_v(G) = (V, E \triangle \{(i,j) : i,j \in N(v), i \neq j\})$$

即：$v$ 的邻域中的所有边取补（有边 → 无边，无边 → 有边），其余边不变。

**在量子力学中的含义** [Van den Nest et al., PRA 69, 022316 (2004)]：

$$|G'\rangle = \tau_v(|G\rangle) = e^{-i\frac{\pi}{4}X_v} \prod_{u \in N(v)} e^{i\frac{\pi}{4}Z_u} |G\rangle$$

即在顶点 $v$ 上施加 $\sqrt{-iX} = e^{-i\pi X/4}$，在其所有邻居上施加 $\sqrt{iZ} = e^{i\pi Z/4}$。

**在 ZX 图中的操作** [Duncan et al., arXiv:1902.03178, Lemma 4.1]：

考虑 graph-like ZX 图中一个相位为 $0$（或 $\pi$）的内部蜘蛛 $v$：

1. 将 $v$ 的相位变为 $-\pi/2$（即施加 $\sqrt{-iX}$ 的等价操作）
2. 将 $v$ 的每个邻居 $u$ 的相位增加 $\pi/2$（即施加 $\sqrt{iZ}$）
3. 对 $v$ 的邻域子图取边补
4. 删除蜘蛛 $v$（通过 spider fusion 吸收其相位）

**净效果**：删除一个 degree-$d$ 的 proper Clifford 蜘蛛，同时修改其邻域的边结构和相位。

### Step 4: Pivot Operation in ZX (枢轴操作) **[Duncan et al., arXiv:1902.03178, Sec.4.2]**

**定义**：对于图 $G$ 中相邻的两个顶点 $u, v$，枢轴操作定义为三次连续局部互补：

$$\wedge_{uv}(G) = \tau_u \circ \tau_v \circ \tau_u(G)$$

**枢轴操作的图论效果**：设 $N(u) \setminus \{v\} = A \cup C$，$N(v) \setminus \{u\} = B \cup C$，其中 $C = N(u) \cap N(v) \setminus \{u,v\}$（共同邻居）。则枢轴操作：

1. 取补 $A \times B$ 之间的所有边（$A$ 中的顶点与 $B$ 中的顶点之间）
2. 取补 $A \times C$ 之间的所有边
3. 取补 $B \times C$ 之间的所有边
4. 可能改变 $u, v$ 之间的连接

**在 ZX 图中的操作** [Duncan et al., arXiv:1902.03178, Lemma 4.4]：

考虑 graph-like ZX 图中两个通过 Hadamard 边相连的 proper Clifford 蜘蛛 $u, v$（相位均为 $0$ 或 $\pi$）：

1. 修改 $u, v$ 邻域之间的边（按上述枢轴规则）
2. 调整 $u, v$ 及其邻居的相位（每个邻居的相位变化取决于它属于 $A, B, C$ 中的哪个集合）
3. 删除蜘蛛 $u$ 和 $v$

**净效果**：一次操作删除两个 proper Clifford 蜘蛛。

### Step 5: Completeness of LC + Pivot for Clifford Group **[Duncan et al., arXiv:1902.03178, Sec.4; van de Wetering, arXiv:2012.13966, Sec.5.2]**

**定理** [Duncan et al., arXiv:1902.03178, Theorem 4.3]：对于 Clifford 电路（稳定子电路），局部互补和枢轴操作构成了一组**完备**的图变换集。即：任何 Clifford ZX 图都可以通过反复应用 LC 和 Pivot 操作化简到唯一的最简形式。

**推论**：
1. PyZX 对 Clifford 电路的化简是最优的
2. 化简后的 Clifford 电路具有最少的双量子比特门
3. 对最近邻架构，这给出了新的（更小的）门深度上界

### Step 6: Connection to Measurement-Based Quantum Computation (MBQC) **[van de Wetering, arXiv:2012.13966, Sec.5.3; Raussendorf & Briegel, PRL 86, 5188 (2001)]**

图态是**基于测量的量子计算（MBQC）**的核心资源。在 MBQC 中：

1. 准备一个大的图态（通常是 cluster state = 方格子图态）
2. 通过对单个量子比特的测量来执行计算
3. 测量基的选择决定了计算内容
4. 测量结果需要前馈（feed-forward）来纠正随机性

**ZX 演算与 MBQC 的关系**：

ZX 图可以自然地描述 MBQC 的计算流程：
- **图态准备**：graph-like ZX 图中的 Z-蜘蛛网络
- **测量**：将蜘蛛的输出线"弯回"变为输入线（对应投影测量）
- **前馈校正**：通过 $\pi$-copy 规则传播 Pauli 修正

**gflow 的 MBQC 起源**：gflow（广义流）最初是在 MBQC 的语境中定义的 [Browne et al., 2007]，用于判断 MBQC 计算模式是否具有确定性。在 ZX 电路优化中，gflow 被重新利用来判断 ZX 图是否可以提取为电路。

### Step 7: Relation to Stabilizer Formalism (与稳定子形式体系的关系) **[Gottesman, arXiv:quant-ph/9705052; van de Wetering, arXiv:2012.13966, Sec.5]**

ZX 演算和稳定子形式体系是描述 Clifford 量子计算的两种互补视角：

| 概念 | 稳定子形式 | ZX 演算 |
|------|-----------|--------|
| 态表示 | 稳定子生成元列表 | Graph-like ZX 图 |
| Clifford 门 | 稳定子变换 $g \mapsto UgU^\dagger$ | 图重写规则（LC, Pivot） |
| 测量 | 添加/移除稳定子生成元 | 投影/弯线 |
| 经典模拟 | Gottesman-Knill 定理 | ZX 图化简 |
| 正规形 | 表格形式（tableau） | 化简后的 graph-like 图 |

**Gottesman-Knill 定理的 ZX 证明** [van de Wetering, arXiv:2012.13966, Sec.5.4]：

ZX 演算提供了 Gottesman-Knill 定理的一个简洁图形化证明：
1. 任何 Clifford 电路翻译为 ZX 图后，所有蜘蛛相位都是 Clifford（$k\pi/2$）
2. LC + Pivot 化简在多项式时间内完成
3. 化简后的图直接给出模拟结果（测量概率可以从图中读出）

因此，Clifford 电路的经典模拟复杂度为 $O(\text{poly}(n))$。

### Step 8: Graph State Entanglement and Quantum Codes **[Hein et al., arXiv:quant-ph/0602096; Schlingemann & Werner, PRA 65, 012308 (2001)]**

图态与量子纠错码之间有深刻联系：

**定理**（图态码）：任何稳定子码 $[[n, k, d]]$ 都可以表示为 $(n+k)$ 量子比特的图态上对 $k$ 个量子比特进行编码。

**在 ZX 中的表现**：
- 码空间 = ZX 图中特定蜘蛛的自由相位
- 稳定子 = 图的对称性
- 码距 = 图中最短的非平凡环

这个联系使得 ZX 演算可以用于分析和优化量子纠错码的编码电路。

---

## Key Results

1. 图态在 ZX 中有最自然的表示：Z-蜘蛛 + Hadamard 边
2. 局部互补（LC）对应在一个顶点的邻域内取边补
3. 枢轴（Pivot）= 三次 LC，可以同时删除两个 Clifford 蜘蛛
4. LC + Pivot 对 Clifford 群构成完备的图变换集
5. gflow 的起源是 MBQC，在 ZX 优化中用于判断电路可提取性
6. ZX 演算提供了 Gottesman-Knill 定理的简洁图形化证明

## References

- [1] van de Wetering, J. "ZX-calculus for the working quantum computer scientist." arXiv:2012.13966 (2020)
- [2] Duncan, R., Kissinger, A., Perdrix, S. & van de Wetering, J. "Graph-theoretic Simplification of Quantum Circuits with the ZX-calculus." Quantum 4, 279 (2020). arXiv:1902.03178
- [3] Hein, M., Eisert, J. & Briegel, H.J. "Multi-party entanglement in graph states." Phys. Rev. A 69, 062311 (2004). arXiv:quant-ph/0307130
- [4] Van den Nest, M., Dehaene, J. & De Moor, B. "Graphical description of the action of local Clifford transformations on graph states." Phys. Rev. A 69, 022316 (2004)
- [5] Backens, M. "The ZX-calculus is complete for stabilizer quantum mechanics." New J. Phys. 16, 093021 (2014). arXiv:1307.7025
- [6] Browne, D.E., Kashefi, E., Mhalla, M. & Perdrix, S. "Generalised flow and determinism in measurement-based quantum computation." New J. Phys. 9, 250 (2007)
- [7] Raussendorf, R. & Briegel, H.J. "A One-Way Quantum Computer." Phys. Rev. Lett. 86, 5188 (2001)
- [8] Gottesman, D. "Stabilizer Codes and Quantum Error Correction." PhD thesis, Caltech (1997). arXiv:quant-ph/9705052
