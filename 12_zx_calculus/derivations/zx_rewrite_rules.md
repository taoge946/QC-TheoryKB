# ZX Rewrite Rules and Completeness

> **Tags**: `zx-calculus`, `rewrite-rules`, `spider-fusion`, `bialgebra`, `completeness`, `clifford`

## Statement

ZX 演算的核心是一组图形重写规则（rewrite rules），用于对 ZX 图进行等价变换。这些规则保持底层线性映射不变（模标量）。ZX 演算的一个关键结果是**完备性**：这组有限的规则足以推导出量子比特量子力学中所有合法的图形等式。

## Prerequisites

- **ZX 基础**：Z-蜘蛛和 X-蜘蛛的定义及其线性映射（见 [zx_basics.md](zx_basics.md)）
- **Pauli 群**：$X, Z$ 门及其对易关系
- **Clifford 群**：由 $H, S, \text{CNOT}$ 生成的群
- **图态**：图态的基本定义

---

## Derivation

### Step 1: Spider Fusion (蜘蛛融合) **[van de Wetering, arXiv:2012.13966, Rule (f); Coecke & Duncan, arXiv:0906.4725]**

**规则 (f)**：两个**同色**蜘蛛如果通过至少一条线相连，则可以融合为一个蜘蛛，相位相加：

$$Z_\alpha^{m_1, k} \circ Z_\beta^{k, n_1} = Z_{\alpha + \beta}^{m_1, n_1} \quad (\text{mod } 2\pi)$$

更一般地，若 Z-蜘蛛 $A$（$m_1$ 个输出、$p + k$ 个输入）和 Z-蜘蛛 $B$（$k + n_1$ 个输出、$q$ 个输入）通过 $k$ 条内部线相连，融合后得到一个 Z-蜘蛛（$m_1 + n_1 - k$ 个输出、$p + q - k$ 个输入），相位为 $\alpha + \beta$。

**证明**（通过矩阵计算）：

两个 Z-蜘蛛在 $k$ 条线上连接的核心计算：

$$\langle 0|^{\otimes k}(|0\rangle^{\otimes k}) = 1, \quad \langle 1|^{\otimes k}(|1\rangle^{\otimes k}) = 1, \quad \langle 0|^{\otimes k}(|1\rangle^{\otimes k}) = 0$$

因此：

$$Z_\alpha \circ Z_\beta = (|0\rangle^{\otimes m_1}\langle 0|^{\otimes k} + e^{i\alpha}|1\rangle^{\otimes m_1}\langle 1|^{\otimes k})(|0\rangle^{\otimes k}\langle 0|^{\otimes n_1} + e^{i\beta}|1\rangle^{\otimes k}\langle 1|^{\otimes n_1})$$

$$= |0\rangle^{\otimes m_1}\langle 0|^{\otimes n_1} + e^{i(\alpha+\beta)}|1\rangle^{\otimes m_1}\langle 1|^{\otimes n_1} = Z_{\alpha+\beta}^{m_1, n_1} \quad \square$$

同样的规则对 X-蜘蛛成立（在 Hadamard 基中相同的论证）。

### Step 2: Color Change via Hadamard (通过 Hadamard 的颜色变换) **[van de Wetering, arXiv:2012.13966, Rule (h)]**

**规则 (h)**：在 Z-蜘蛛的每条腿上放置 Hadamard 门，等价于将其变为 X-蜘蛛（相位不变），反之亦然：

$$H^{\otimes m} \circ Z_\alpha^{m,n} \circ H^{\otimes n} = X_\alpha^{m,n}$$

**证明**：

利用 Hadamard 的基变换性质 $H|0\rangle = |{+}\rangle$, $H|1\rangle = |{-}\rangle$：

$$H^{\otimes m} Z_\alpha^{m,n} H^{\otimes n} = H^{\otimes m}(|0\rangle^{\otimes m}\langle 0|^{\otimes n} + e^{i\alpha}|1\rangle^{\otimes m}\langle 1|^{\otimes n})H^{\otimes n}$$

$$= |{+}\rangle^{\otimes m}\langle{+}|^{\otimes n} + e^{i\alpha}|{-}\rangle^{\otimes m}\langle{-}|^{\otimes n} = X_\alpha^{m,n} \quad \square$$

**推论**：在 ZX 图中，当蜘蛛之间的边全部是 Hadamard 边时，可以自由切换蜘蛛颜色。

### Step 3: Identity Removal (恒等线移除) **[van de Wetering, arXiv:2012.13966, Rule (id)]**

**规则 (id)**：无相位的 1入1出蜘蛛等价于一条线：

$$Z_0^{1,1} = I = X_0^{1,1}$$

**证明**：$Z_0^{1,1} = |0\rangle\langle 0| + |1\rangle\langle 1| = I$。$\square$

**推广规则 (S1, S2)**：

- **(S1)** 无相位、0入1出的 Z-蜘蛛接上无相位、1入0出的 Z-蜘蛛 = 标量 2
- **(S2)** 无相位、0入0出的 Z-蜘蛛 = 标量 $1 + 1 = 2$

这些标量规则在某些证明中需要仔细处理。

### Step 4: Bialgebra Rule (双代数规则 / 强互补性) **[van de Wetering, arXiv:2012.13966, Rule (b); Coecke & Duncan, arXiv:0906.4725, Sec.5]**

**规则 (b)**：不同颜色的无相位蜘蛛之间满足双代数律。图形化地：

一个"绿色蛛网"（$Z_0^{1,2}$ 复制后 $Z_0^{2,1}$ 合并）和一个"红色蛛网"（$X_0^{1,2}$ 复制后 $X_0^{2,1}$ 合并）的连接可以"拉开"：

$$Z_0^{2,1} \circ X_0^{1,2} = (X_0^{1,2} \otimes X_0^{1,2}) \circ X_0^{2,2} \circ (Z_0^{2,1} \otimes Z_0^{2,1})$$

直观理解：当无相位的绿色蜘蛛和红色蜘蛛相互交错时，它们会"滑过"彼此，建立所有可能的连接。

**证明**：直接矩阵计算。左端：

$$Z_0^{2,1} \circ X_0^{1,2} = (|00\rangle\langle 0| + |11\rangle\langle 1|)(|{+}\rangle\langle{+}{+}| + |{-}\rangle\langle{-}{-}|)$$

通过展开 $|{\pm}\rangle$ 并整理，可验证等于右端的矩阵。$\square$

**推论（Hopf rule）**：当双代数规则应用于"单输入单输出"的情形时：

$$Z_0^{0,1} \circ X_0^{1,0} = \text{scalar}$$

即不同颜色的"cup"和"cap"相连等于一个标量（=2）。此规则也称为 **Hopf 规则**。

### Step 5: Pi-Copy Rule ($\pi$-复制规则) **[van de Wetering, arXiv:2012.13966, Rule ($\pi$)]**

**规则 ($\pi$)**：$\pi$ 相位的蜘蛛穿过不同颜色的蜘蛛时，会将其相位取反并在每条输出线上"复制"自己：

$$X_\pi^{1,1} \circ Z_\alpha^{m,n} = Z_{-\alpha}^{m,n} \circ (X_\pi^{1,1})^{\otimes n}$$

等价地：$X \cdot Z_\alpha = Z_{-\alpha} \cdot X$，这是 Pauli 关系 $XZX = -Z$ 的蜘蛛推广。

**证明**：

$$X_\pi^{1,1} \circ Z_\alpha^{m,n} = X \cdot (|0\rangle^{\otimes m}\langle 0|^{\otimes n} + e^{i\alpha}|1\rangle^{\otimes m}\langle 1|^{\otimes n})$$

利用 $X|0\rangle = |1\rangle$, $X|1\rangle = |0\rangle$（对输出端作用）：

$$= |1\rangle^{\otimes m}\langle 0|^{\otimes n} + e^{i\alpha}|0\rangle^{\otimes m}\langle 1|^{\otimes n}$$

$$= |0\rangle^{\otimes m}\langle 1|^{\otimes n} + e^{-i\alpha}|1\rangle^{\otimes m}\langle 0|^{\otimes n} \cdot e^{i\alpha}$$

重排后等于 $Z_{-\alpha}^{m,n}$ 在输入端接 $X^{\otimes n}$。$\square$

**重要特例**：
- $X Z_\alpha X = Z_{-\alpha}$：X 门翻转 Z-旋转的方向
- $Z X_\alpha Z = X_{-\alpha}$：Z 门翻转 X-旋转的方向（对偶版本）

### Step 6: State Copy Rule (态复制规则) **[van de Wetering, arXiv:2012.13966, Sec.3]**

**规则**：$|0\rangle$ 和 $|1\rangle$ 可以被 Z-蜘蛛"复制"：

$$Z_0^{1,2} \circ |0\rangle = |00\rangle, \quad Z_0^{1,2} \circ |1\rangle = |11\rangle$$

类似地，$|{+}\rangle$ 和 $|{-}\rangle$ 可以被 X-蜘蛛"复制"：

$$X_0^{1,2} \circ |{+}\rangle = |{+}{+}\rangle, \quad X_0^{1,2} \circ |{-}\rangle = |{-}{-}\rangle$$

但 Z-蜘蛛**不能**复制 $|{+}\rangle$（no-cloning theorem 的体现），X-蜘蛛也不能复制 $|0\rangle$。

### Step 7: Supplementarity Rule (补充性规则) **[van de Wetering, arXiv:2012.13966, Sec.6.1]**

**规则 (SUP)**：此规则在完备性证明中是关键的非 Clifford 规则：

两个 $\pi/2$ 相位的环（loop）可以互相替换。形式化地：将两个相位为 $\pi/4$ 的蜘蛛以特定方式连接的图等于另一种连接方式。

此规则是 Vilmart (2019) 的完备性证明中引入的核心新规则，它补充了 Clifford 片段的规则以处理 T 门和一般相位。

### Step 8: Completeness Theorem **[Backens, arXiv:1307.7025; Hadzihasanovic et al., arXiv:1805.05631; Vilmart, arXiv:1812.09114; van de Wetering, arXiv:2012.13966, Sec.6]**

**ZX 演算完备性的历史发展**：

**定理 1**（Clifford 完备性）[Backens 2014]：ZX 演算的规则 $\{(f), (h), (b), (\pi), (id), (S1), (S2)\}$ 对于**稳定子量子力学**（Clifford 片段）是完备的。即：对于任意两个仅包含 Clifford 门的 ZX 图 $D_1, D_2$：

$$\llbracket D_1 \rrbracket = \llbracket D_2 \rrbracket \implies D_1 \stackrel{\text{Clifford rules}}{\longleftrightarrow} D_2$$

Backens 的证明策略：将 ZX 图化为基于图态和局部 Clifford 操作的**正规形（normal form）**，利用图态的分类理论证明正规形的唯一性。

**定理 2**（Clifford+T 完备性）[Backens 2015, arXiv:1412.8553]：对于单量子比特 Clifford+T 电路，ZX 演算也是完备的。

**定理 3**（一般完备性）[Hadzihasanovic, Ng & Wang 2018; Vilmart 2019]：通过添加补充性规则（supplementarity rule 或等价的新规则），ZX 演算对于一般的量子比特量子力学是完备的：

$$\forall D_1, D_2: \quad \llbracket D_1 \rrbracket = \llbracket D_2 \rrbracket \iff D_1 \stackrel{\text{ZX rules}}{\longleftrightarrow} D_2$$

**完备规则集总结**：

| 规则 | 名称 | 描述 |
|------|------|------|
| (f) | Spider fusion | 同色蜘蛛融合，相位相加 |
| (h) | Color change | Hadamard 切换蜘蛛颜色 |
| (id) | Identity | 无相位 1-1 蜘蛛 = 线 |
| (b) | Bialgebra | 不同色无相位蜘蛛的交换律 |
| ($\pi$) | Pi-copy | $\pi$ 相位穿过异色蜘蛛取反 |
| (S1), (S2) | Scalar rules | 标量处理 |
| (SUP) | Supplementarity | 非 Clifford 完备性的关键 |

### Step 9: Derived Rules (导出规则) **[van de Wetering, arXiv:2012.13966, Sec.3]**

从基本规则可以推导出许多有用的规则：

**1. NOT-copy（NOT 复制）**：$X = X_\pi$ 可以通过 Z-蜘蛛"复制"：

$$Z_0^{1,m} \circ X_\pi^{1,1} = (X_\pi^{1,1})^{\otimes m} \circ Z_0^{1,m}$$

由 $\pi$-copy 规则直接得出。

**2. Phase commutation（相位交换）**：对于 Clifford 相位（$\alpha = k\pi/2$），Z 相位和 X 相位可以通过特定规则交换位置。

**3. Color swap（颜色交换）**：整个 ZX 图中所有蜘蛛的颜色同时取反（绿变红、红变绿），得到的图与原图有相同的语义（模 Hadamard 共轭）。

---

## Key Results

1. ZX 演算的核心规则只有 7-8 条，但足以推导出量子力学中所有合法的图等式
2. Spider fusion 是最常用的规则，直觉上对应"同类蜘蛛合并"
3. Bialgebra 规则体现了 Z 和 X 可观测量的强互补性
4. Clifford 片段的完备性（Backens 2014）是 ZX 电路优化的理论基础
5. 一般完备性（2018-2019）需要额外的 supplementarity 规则

## References

- [1] Coecke, B. & Duncan, R. "Interacting Quantum Observables." New J. Phys. 13, 043016 (2011). arXiv:0906.4725
- [2] van de Wetering, J. "ZX-calculus for the working quantum computer scientist." arXiv:2012.13966 (2020)
- [3] Backens, M. "The ZX-calculus is complete for stabilizer quantum mechanics." New J. Phys. 16, 093021 (2014). arXiv:1307.7025
- [4] Backens, M. "The ZX-calculus is complete for the single-qubit Clifford+T group." arXiv:1412.8553 (2015)
- [5] Hadzihasanovic, A., Ng, K.F. & Wang, Q. "Two complete axiomatisations of pure-state qubit quantum computing." arXiv:1805.05631 (2018)
- [6] Vilmart, R. "A near-minimal axiomatisation of ZX-calculus for pure qubit quantum mechanics." arXiv:1812.09114 (2019)
