# Magic State Distillation

> **Tags**: `magic-state`, `non-clifford`, `fault-tolerant`, `T-gate`, `distillation`
> **Source**: Primarily from Fujii, K. "Quantum Computation with Topological Codes" (2015), Ch.2 §2.8

## Statement **[Bravyi & Kitaev 2005; Fujii, Ch.2, §2.8]**

Magic state distillation 是实现容错通用量子计算的关键技术。由于 Clifford 门可以通过稳定子码横截实现（天然容错），但非 Clifford 门（如 $T = e^{-i(\pi/8)Z}$）不能，因此需要通过制备高保真度的"magic state"并利用 gate teleportation 来间接实现非 Clifford 门。蒸馏协议使用多个含噪 magic state 和理想 Clifford 操作，输出少量高纯度 magic state。

## Prerequisites

- **稳定子形式体系**：[stabilizer_formalism.md]
- **CSS 码**：[css_codes.md]
- **Gate teleportation**：one-bit teleportation 的概念
- **Clifford 群**：横截 Clifford 操作

---

## Part 1: Why Magic States Are Needed

### Gottesman-Knill 定理的限制 [Fujii, Ch.2, §2.4]

> **[Fujii, Ch.2, Theorem 2.1]**: Clifford 操作 + 稳定子态 + Pauli 测量可以被经典高效模拟。因此仅有 Clifford 门无法实现通用量子计算。

通用量子计算需要非 Clifford 门。标准选择是 $T$ 门（$\pi/8$ 门）：

$$T = e^{-i(\pi/8)Z} = \begin{pmatrix} 1 & 0 \\ 0 & e^{-i\pi/4} \end{pmatrix}$$

$\{H, S, T, \text{CNOT}\}$ 构成通用门集。

### 横截非 Clifford 门的困难 [Fujii, Ch.2, §2.7]

> **[Fujii, Ch.2, §2.7]**: 非 Clifford 操作不将 Pauli 算子映射到 Pauli 算子：
>
> $$e^{-i(\pi/8)Z} X e^{i(\pi/8)Z} = (X + Y)/\sqrt{2}$$
>
> 因此横截非 Clifford 门很难产生逻辑非 Clifford 门。

---

## Part 2: Gate Teleportation [Fujii, Ch.2, §2.6]

> **[Fujii, Ch.2, §2.6]**: 非 Clifford 门可以通过 one-bit teleportation 实现。对于 $T$ 门，使用 magic state $|T\rangle = (|0\rangle + e^{-i\pi/4}|1\rangle)/\sqrt{2}$，通过 CNOT + $Z$ 基测量 + 条件 $S$ 矫正实现。

关键电路：输入 $|\psi\rangle$ 和辅助 magic state $|T\rangle$，执行 CNOT（$|\psi\rangle$ 为控制），测量 $|\psi\rangle$ 在 $Z$ 基上，根据测量结果施加 $S$ 矫正，输出 $T|\psi\rangle$（在 $|T\rangle$ 的线上）。

---

## Part 3: Knill-Laflamme-Zurek Protocol [Fujii, Ch.2, §2.8.1]

> **[Fujii, Ch.2, §2.8.1]**: 第一个容错 magic state 制备方案。基于 magic state $|A\rangle \equiv e^{-i(\pi/8)Y}|+\rangle$ 是 Hadamard 算子的特征态这一事实。

**步骤**：
1. 将含噪 magic state 编码进 7-qubit Steane 码
2. 横截测量 $H^{\otimes 7}$（Hadamard 具有横截性）
3. 通过 one-bit teleportation 解码

含噪 magic state 经随机化后成为：

$$\rho_A = (1-p)|A\rangle\langle A| + p|A^\perp\rangle\langle A^\perp|, \quad |A^\perp\rangle = Y|A\rangle$$

$Y$ 错误可被横截 $Z$ 测量检测。使用距离 3 的码，输出错误率 $O(p^3)$。需要 15 个含噪 magic state 输入。

---

## Part 4: Bravyi-Kitaev Protocol [Fujii, Ch.2, §2.8.2]

> **[Fujii, Ch.2, §2.8.2]**: 基于 $[[15,1,3]]$ Reed-Muller CSS 码的蒸馏协议。

### 15-Qubit Reed-Muller 码的关键性质

> **[Fujii, Ch.2, §2.8.2]**: 逻辑态 $|0_L\rangle$ 中每项含 8 个 1，$|1_L\rangle$ 中每项含 7 个 1。因此横截 $T$ 门作用为：
>
> $$T^{\otimes 15}|0_L\rangle = e^{i\pi/8}|0_L\rangle, \quad T^{\otimes 15}|1_L\rangle = e^{-i\pi/8}|1_L\rangle$$
>
> 即横截 $T$ 门实现逻辑 $T^\dagger$ 门（在码空间上）。

### 蒸馏电路

1. 用 CNOT 编码将 15 个含噪 magic state 编码进 Reed-Muller 码
2. 通过 one-bit teleportation 施加横截 $T$ 门
3. 横截 $X$ 基测量解码，检测 $Z$ 错误

含噪 magic state：$\rho_T = (1-p)|T\rangle\langle T| + p\,Z|T\rangle\langle T|Z$

### 误差分析：MacWilliams 恒等式 [Fujii, Ch.2, §2.8.2]

> **[Fujii, Ch.2, §2.8.2]**: 使用权重计数器 $W_V(x,y) = \sum_{\mathbf{c}\in V} x^{n-\mathrm{wt}(\mathbf{c})}y^{\mathrm{wt}(\mathbf{c})}$ 和 MacWilliams 恒等式：
>
> $$W_V(x,y) = \frac{1}{|V|}W_{V^\perp}(x+y, x-y)$$

通过蒸馏的概率：

$$p_{\rm pass} = W_{V_{H_x}^\perp}(1-p, p) = \frac{1+15(1-2p)^8}{16}$$

输出错误率：

$$p' = \frac{1+15(2p-1)^8+15(2p-1)^7+(2p-1)^{15}}{2[1+15(1-2p)^8]} = 35p^3 + O(p^4)$$ **[Fujii, Ch.2, §2.8.2; Bravyi & Kitaev 2005]**

### 迭代蒸馏

> **[Fujii, Ch.2, §2.8.2]**: 蒸馏阈值 $p < 0.141$。经 $l$ 轮蒸馏后：
>
> $$p^{(l)} \to \frac{(\sqrt{35}\,p)^{3^l}}{\sqrt{35}}$$
>
> 误差率以 $3^l$ 的指数超指数下降。每轮消耗 15 个 magic state 输出 1 个。

---

## Part 5: KLZ 与 BK 协议的等价性

> **[Fujii, Ch.2, §2.8.2]**: Reichardt 证明 Knill-Laflamme-Zurek 和 Bravyi-Kitaev 协议虽然形式不同，实际上是等价的。

---

## Summary

| 协议 | 输入码 | 输入数 | 输出误差率 | 蒸馏阈值 |
|------|--------|--------|-----------|---------|
| KLZ | $[[7,1,3]]$ Steane | 15 | $O(p^3)$ | — |
| BK | $[[15,1,3]]$ Reed-Muller | 15 | $35p^3+O(p^4)$ | $p < 14.1\%$ |

Magic state distillation 是连接 Clifford 容错和通用容错量子计算的桥梁。在拓扑码方案中，Clifford 操作通过缺陷编织拓扑保护地实现，而 magic state 通过 singular qubit injection 注入后蒸馏。

---

## References

- Bravyi, S. & Kitaev, A. "Universal quantum computation with ideal Clifford gates and noisy ancillas." PRA 71, 022316 (2005).
- Knill, E., Laflamme, R. & Zurek, W. "Resilient quantum computation." Science 279, 342 (1998).
- Reichardt, B. W. "Quantum universality from magic states distillation applied to CSS codes." QIC 5, 181 (2005).
- Fujii, K. "Quantum Computation with Topological Codes." SpringerBriefs (2015), Ch.2 §2.8.
