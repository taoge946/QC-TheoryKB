# ZX-Calculus for Circuit Optimization

> **Tags**: `zx-calculus`, `circuit-optimization`, `t-count`, `pyzx`, `phase-teleportation`, `circuit-extraction`

## Statement

ZX 演算为量子电路优化提供了一种全新的范式：将电路翻译为 ZX 图后，利用图重写规则进行全局化简，最后将化简后的图提取回电路。这种方法能发现传统 peephole 优化无法触及的化简，特别是在 T-count 优化方面表现突出。PyZX 是实现此方法的主要开源工具。

## Prerequisites

- **ZX 基础**：蜘蛛定义、重写规则（见 [zx_basics.md](zx_basics.md), [zx_rewrite_rules.md](zx_rewrite_rules.md)）
- **量子电路**：Clifford+T 门集、电路深度和门数概念
- **图论**：图同构、邻接关系
- **gflow 概念**：测量型量子计算中的广义流

---

## Derivation

### Step 1: Circuit to ZX Translation (电路到 ZX 的翻译) **[van de Wetering, arXiv:2012.13966, Sec.2.3; Duncan et al., arXiv:1902.03178, Sec.2]**

量子电路到 ZX 图的翻译是逐门进行的：

**翻译规则**：

| 电路门 | ZX 表示 |
|--------|--------|
| $R_z(\alpha)$ | 单个 $Z_\alpha^{1,1}$ 蜘蛛 |
| $R_x(\alpha)$ | 单个 $X_\alpha^{1,1}$ 蜘蛛 |
| $H$ | Hadamard 方框，或 $Z_{\pi/2} \cdot X_{\pi/2} \cdot Z_{\pi/2}$ |
| $S = R_z(\pi/2)$ | $Z_{\pi/2}^{1,1}$ |
| $T = R_z(\pi/4)$ | $Z_{\pi/4}^{1,1}$ |
| CNOT | $Z_0^{1,2}$ (control) + $X_0^{2,1}$ (target) 相连 |
| CZ | 两个 $Z_0^{1,2}$ 通过 Hadamard 边相连 |
| SWAP | 交换线（在 ZX 中只是拓扑操作） |

**翻译过程**：
1. 每条量子比特线变为 ZX 图的一根线
2. 每个门替换为对应的 ZX 生成元
3. 门的顺序对应蜘蛛的串联顺序
4. 翻译后，立即应用 spider fusion 合并相邻同色蜘蛛

### Step 2: Graph-Like Form (图样式形式) **[Duncan et al., arXiv:1902.03178, Sec.3, Definition 3.1]**

**定义**：一个 ZX 图称为 **graph-like**，如果：
1. 所有蜘蛛都是 Z-蜘蛛（无 X-蜘蛛）
2. 蜘蛛之间只通过 Hadamard 边相连（无普通边）
3. 两个蜘蛛之间最多一条 Hadamard 边
4. 无自环（self-loop）
5. 每条输入/输出线连接到不同的蜘蛛

**定理** [Duncan et al., arXiv:1902.03178, Proposition 3.2]：任何 ZX 图都可以通过以下步骤转化为 graph-like 形式：
1. 用颜色变换规则 (h) 将所有 X-蜘蛛转为 Z-蜘蛛（在其腿上加 Hadamard）
2. 用 spider fusion (f) 合并相连的同色蜘蛛
3. 用 Hopf 规则消除平行的 Hadamard 边（偶数条 = 无边，奇数条 = 一条边）
4. 用恒等规则消除自环

### Step 3: Phase Teleportation (相位传送) **[van de Wetering, arXiv:2012.13966, Sec.4.1; Kissinger & van de Wetering, arXiv:1904.04735]**

**相位 Gadget** 是 ZX 电路优化的核心工具。一个相位 gadget 是一个通过 Hadamard 边连接到 $n$ 条主线上的 Z-蜘蛛，带相位 $\alpha$：

$$\text{PhaseGadget}(\alpha, n) = \exp\left(-i\frac{\alpha}{2} Z^{\otimes n}\right) = \sum_{x \in \{0,1\}^n} e^{i\alpha \cdot |x|_{\text{odd}}} |x\rangle\langle x|$$

其中 $|x|_{\text{odd}} = x_1 \oplus x_2 \oplus \cdots \oplus x_n$（比特串的奇偶性）。

**相位 gadget 的关键性质**：

1. **可交换性**：不同的相位 gadget 如果作用在同一组量子比特上，顺序无关（因为它们都是对角矩阵）
2. **可融合性**：作用在相同量子比特集上的相位 gadget 可以合并，相位相加
3. **可移动性**：相位 gadget 可以在 ZX 图中自由移动（"传送"），只要保持与主线的连接关系

**Phase teleportation** 的过程：
1. 将电路中的所有 $R_z$ 旋转识别为相位 gadget
2. 利用 CNOT（= Z-copy + X-merge）扩展相位 gadget 的作用范围
3. 寻找可以合并的相位 gadget 并融合
4. 这可以减少 T 门数量（T-count optimization）

### Step 4: Interior Clifford Simplification (内部 Clifford 化简) **[Duncan et al., arXiv:1902.03178, Sec.4; Kissinger & van de Wetering, arXiv:1904.04735, Algorithm 1]**

这是 PyZX 实现的核心化简算法：

**算法（Simplify）**：

**输入**：graph-like ZX 图 $G$

**循环执行直到无变化**：
1. **识别 Clifford 蜘蛛**：找到相位为 $0, \pi/2, \pi, 3\pi/2$ 的内部蜘蛛（interior = 非输入输出端）
2. **相位为 $0$ 或 $\pi$ 的蜘蛛**（proper Clifford）：
   - 如果该蜘蛛连接度 $\leq 1$：直接删除（将相位吸收到邻居中）
   - 如果连接度 $= 2$：应用**局部互补（local complementation）**删除该蜘蛛
   - 如果连接度 $\geq 3$ 且存在与之相连的另一个 proper Clifford 蜘蛛：应用**枢轴操作（pivot）**同时删除两个蜘蛛
3. **相位为 $\pi/2$ 或 $3\pi/2$ 的蜘蛛**：
   - 使用 gadget 融合或特殊规则处理

**关键定理** [Duncan et al., arXiv:1902.03178, Theorem 4.3]：对于纯 Clifford 电路，此算法将 ZX 图化简到**最优形式**（最少的蜘蛛数），且结果是渐近最优的电路大小。

### Step 5: T-Count Optimization (T 门计数优化) **[Kissinger & van de Wetering, arXiv:1904.04735, Sec.4]**

T 门（$T = R_z(\pi/4)$）在容错量子计算中是最"昂贵"的门（需要魔法态蒸馏），因此减少 T-count 是电路优化的首要目标。

**ZX 方法的 T-count 优化策略**：

1. **Phase gadget fusion**：将 T 门转为相位 gadget，寻找可以合并的 gadget 对
   - 若两个 $T$ gadget 作用在相同比特集 → 合并为一个 $S$ 门（Clifford 门，"免费"）
   - 若 $T$ 和 $T^\dagger$ 作用在相同比特集 → 相互抵消

2. **Clifford 简化暴露新的融合机会**：interior Clifford 化简后，原本不同的相位 gadget 可能变得作用于相同比特集

3. **迭代**：重复 gadget 融合 + Clifford 化简，直到无法进一步减少

**PyZX 的实际效果** [Kissinger & van de Wetering, arXiv:1904.04735, Sec.5]：
- 在标准基准电路上，PyZX 的 T-count 优化通常优于其他所有已知方法
- 对于 Clifford 电路，PyZX 给出渐近最优的门数和深度
- 对于 near-Clifford 电路（T 门较少），优化效果尤为显著

### Step 6: ZX to Circuit Extraction (ZX 图到电路提取) **[Duncan et al., arXiv:1902.03178, Sec.5; Backens et al., arXiv:2003.01674]**

化简后的 ZX 图需要提取回量子电路。这是 ZX 优化流程中最关键（也最复杂）的一步。

**前提条件 — gflow**：

**定义**（广义流, generalised flow, gflow）[Browne et al., 2007]：graph-like ZX 图 $G$ 具有 gflow，如果存在一个映射 $g$ 和一个偏序 $\prec$，使得对每个非输出蜘蛛 $v$：
1. $v \prec w$ 对所有 $w \in g(v)$
2. $v \in \text{Odd}(g(v))$（$v$ 在 $g(v)$ 的奇邻域中）
3. $w \in \text{Odd}(g(v)) \setminus \{v\} \implies v \prec w$

**定理** [Duncan et al., arXiv:1902.03178, Theorem 5.4]：graph-like ZX 图可以提取为量子电路当且仅当它具有 gflow。

**提取算法**：

**输入**：具有 gflow 的 graph-like ZX 图

1. **计算 gflow** 并确定蜘蛛的偏序
2. **从输出端开始**，按照 gflow 偏序的逆序处理每个蜘蛛：
   a. 用 CNOT（行操作）将当前蜘蛛与其 gflow 关联的输出线对齐
   b. 提取蜘蛛的相位为 $R_z$ 门
   c. 提取 Hadamard 边为 $H$ 门
3. **处理剩余的连接**为 CZ 门
4. **输出**：等价的量子电路

**重要保证**：对于由量子电路翻译而来的 ZX 图，即使经过化简，gflow 始终保持（即提取总是成功的）。

### Step 7: Complete PyZX Pipeline (完整 PyZX 流水线) **[Kissinger & van de Wetering, arXiv:1904.04735]**

```
输入电路
  │
  ▼
[1] Circuit → ZX: 逐门翻译
  │
  ▼
[2] 转化为 graph-like 形式
  │
  ▼
[3] Interior Clifford 化简 (LC + Pivot)
  │
  ▼
[4] Phase gadget 融合 (T-count 优化)
  │
  ▼
[5] 重复 [3]-[4] 直到收敛
  │
  ▼
[6] Circuit extraction (gflow → 电路)
  │
  ▼
[7] 后处理: 局部门优化 (可选)
  │
  ▼
优化后的电路
```

### Step 8: Comparison with Traditional Transpilers (与传统编译器的对比) **[Kissinger & van de Wetering, arXiv:1904.04735, Sec.5]**

| 特性 | Qiskit Transpiler | PyZX (ZX-calculus) |
|------|------------------|-------------------|
| 优化方法 | Peephole 优化、门合并、路由 | 全局图变换 |
| T-count 优化 | 有限 | 强（phase gadget 融合） |
| Clifford 优化 | 启发式 | 最优（理论保证） |
| 硬件映射 | 内置 | 需外部工具 |
| 可验证性 | 矩阵比较 | 图等价（ZX 规则） |
| 适用场景 | 通用 | Clifford 密集 / 高 T-count 电路 |
| 最佳实践 | 单独使用 | 与 Qiskit 结合使用 |

**实际建议**：先用 PyZX 进行 T-count 和全局化简，再用 Qiskit 进行硬件映射和布线。

---

## Key Results

1. 电路 → ZX → 化简 → 电路 的流水线是 ZX 电路优化的标准工作流
2. Phase gadget 是 T-count 优化的核心工具，允许相位的全局融合
3. Interior Clifford 化简通过 LC 和 Pivot 操作对 Clifford 部分达到最优
4. 电路提取依赖于 gflow 条件，对电路来源的 ZX 图总是满足
5. PyZX 在 T-count 优化方面通常优于所有其他已知方法

## References

- [1] Duncan, R., Kissinger, A., Perdrix, S. & van de Wetering, J. "Graph-theoretic Simplification of Quantum Circuits with the ZX-calculus." Quantum 4, 279 (2020). arXiv:1902.03178
- [2] Kissinger, A. & van de Wetering, J. "PyZX: Large Scale Automated Diagrammatic Reasoning." EPTCS 318, pp.229-241 (2020). arXiv:1904.04735
- [3] van de Wetering, J. "ZX-calculus for the working quantum computer scientist." arXiv:2012.13966 (2020)
- [4] Backens, M., Kissinger, A., Miller-Bakewell, H., van de Wetering, J. & Wolffs, S. "There and back again: A circuit extraction tale." arXiv:2003.01674 (2020)
- [5] Browne, D.E., Kashefi, E., Mhalla, M. & Perdrix, S. "Generalised flow and determinism in measurement-based quantum computation." New J. Phys. 9, 250 (2007)
