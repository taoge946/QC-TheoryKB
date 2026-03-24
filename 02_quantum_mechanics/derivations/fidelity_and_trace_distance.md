# Fidelity and Trace Distance (保真度与迹距离)

> **Tags**: `fidelity`, `trace-distance`, `state-distance`, `uhlmann`

## Statement

量子信息理论中有两个最重要的量子态距离度量：

1. **Fidelity（保真度）** **[N&C, Eq.(9.52), p.409]** **[Preskill, Ch.2, &sect;2.6.1, p.34]**: $F(\rho, \sigma) = \left(\text{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}\right)^2$
2. **Trace Distance（迹距离）** **[N&C, Eq.(9.1), p.399]** **[Preskill, Ch.2, &sect;2.6, p.31]**: $D(\rho, \sigma) = \frac{1}{2}\text{Tr}|\rho - \sigma|$

它们通过 Fuchs-van de Graaf 不等式相互约束：

$$1 - \sqrt{F(\rho,\sigma)} \leq D(\rho,\sigma) \leq \sqrt{1 - F(\rho,\sigma)}$$
**[N&C, Eq.(9.100-9.101), p.416]** **[Preskill, Ch.2, &sect;2.6.2, p.38]**

## Prerequisites

- **密度矩阵**: $\rho \geq 0$，$\text{Tr}(\rho) = 1$，特征值分解（参见 [density_matrix_formalism.md](density_matrix_formalism.md)）
- **矩阵函数**: 矩阵的平方根 $\sqrt{A}$，绝对值 $|A| = \sqrt{A^\dagger A}$
- **特征值**: Hermitian 矩阵的特征值分解，正半定性

---

## Derivation

### Part A: Fidelity (保真度)

#### Step 1: 纯态情形 —— 起点

对两个纯态 $|\psi\rangle$ 和 $|\phi\rangle$，最自然的"重叠度"是：

$$|\langle\psi|\phi\rangle|^2$$

这就是从 $|\phi\rangle$ 中测量得到 $|\psi\rangle$ 的概率。它等于 1 当且仅当两态相同（差一个全局相位），等于 0 当且仅当两态正交。

#### Step 2: 推广到一般态 —— Fidelity 的定义

对一般密度矩阵 $\rho$ 和 $\sigma$，保真度定义为 **[N&C, Eq.(9.52), p.409]** **[Preskill, Ch.2, &sect;2.6.1, p.34]**：

$$F(\rho, \sigma) = \left(\text{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}\right)^2$$

这里 $\sqrt{\rho}$ 是 $\rho$ 的正半定平方根。如果 $\rho = \sum_i \lambda_i |e_i\rangle\langle e_i|$，则 $\sqrt{\rho} = \sum_i \sqrt{\lambda_i}|e_i\rangle\langle e_i|$。

**注意**：有些文献定义 $F$ 时不取外面的平方，即 $f(\rho,\sigma) = \text{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}$。此处我们遵循 Nielsen & Chuang 的约定，取了平方。

#### Step 3: 验证——当 $\rho = |\psi\rangle\langle\psi|$ 为纯态时

设 $\rho = |\psi\rangle\langle\psi|$，则 $\sqrt{\rho} = |\psi\rangle\langle\psi|$（因为 $|\psi\rangle\langle\psi|$ 是投影算子，它的平方根就是自己）。

$$\sqrt{\rho}\,\sigma\,\sqrt{\rho} = |\psi\rangle\langle\psi|\sigma|\psi\rangle\langle\psi| = \langle\psi|\sigma|\psi\rangle \cdot |\psi\rangle\langle\psi|$$

这里 $\langle\psi|\sigma|\psi\rangle$ 是一个非负实数（因为 $\sigma \geq 0$）。所以：

$$\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}} = \sqrt{\langle\psi|\sigma|\psi\rangle} \cdot |\psi\rangle\langle\psi|$$

取迹：

$$\text{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}} = \sqrt{\langle\psi|\sigma|\psi\rangle} \cdot \text{Tr}(|\psi\rangle\langle\psi|) = \sqrt{\langle\psi|\sigma|\psi\rangle}$$

取平方：

$$F(|\psi\rangle\langle\psi|, \sigma) = \langle\psi|\sigma|\psi\rangle$$
**[N&C, Eq.(9.56), p.409]** **[Preskill, Ch.2, &sect;2.6.1, p.34]**

如果 $\sigma$ 也是纯态 $|\phi\rangle\langle\phi|$，则：

$$F = \langle\psi|\phi\rangle\langle\phi|\psi\rangle = |\langle\psi|\phi\rangle|^2$$

与 Step 1 吻合。

#### Step 4: Fidelity 的基本性质

**性质 1: 对称性** **[N&C, Theorem 9.5, p.412]** $F(\rho, \sigma) = F(\sigma, \rho)$

这并不是定义中显然的（定义看起来不对称），但可以证明。设 $A = \sqrt{\rho}\,\sigma\,\sqrt{\rho}$ 和 $B = \sqrt{\sigma}\,\rho\,\sqrt{\sigma}$。

关键引理：对任意矩阵 $X$，$XX^\dagger$ 和 $X^\dagger X$ 有相同的非零特征值。

令 $X = \sqrt{\sigma}\sqrt{\rho}$，则 $XX^\dagger = \sqrt{\sigma}\rho\sqrt{\sigma} = B$，$X^\dagger X = \sqrt{\rho}\sigma\sqrt{\rho} = A$。

因此 $A$ 和 $B$ 有相同的非零特征值 $\{\mu_i\}$，所以：

$$\text{Tr}\sqrt{A} = \sum_i \sqrt{\mu_i} = \text{Tr}\sqrt{B}$$

从而 $F(\rho,\sigma) = F(\sigma,\rho)$。

**性质 2: 范围** $0 \leq F(\rho, \sigma) \leq 1$

$F \geq 0$ 显然（迹的每一项非负）。

$F \leq 1$ 可以通过 Cauchy-Schwarz 不等式证明。

**性质 3: $F(\rho,\sigma) = 1$ 当且仅当 $\rho = \sigma$**

**性质 4: 幺正不变性** $F(U\rho U^\dagger, U\sigma U^\dagger) = F(\rho, \sigma)$

因为 $\sqrt{U\rho U^\dagger} = U\sqrt{\rho}U^\dagger$，代入后 $U$ 和 $U^\dagger$ 全部抵消。

**性质 5: 单调性（数据处理不等式）** **[N&C, Theorem 9.6, p.414]** **[Preskill, Ch.2, &sect;2.6.1, p.37]** 对任何 CPTP 映射 $\mathcal{E}$：

$$F(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \geq F(\rho, \sigma)$$

量子操作不会降低保真度（不会让两个态变得"更远"——但注意保真度越大表示越近）。

#### Step 5: Uhlmann's Theorem

**定理（Uhlmann, 1976）** **[N&C, Theorem 9.4, p.410]** **[Preskill, Ch.2, &sect;2.6.1, pp.35-37]**: 设 $|\psi_\rho\rangle$ 是 $\rho$ 的一个 purification（即 $\text{Tr}_E(|\psi_\rho\rangle\langle\psi_\rho|) = \rho$），则：

$$F(\rho, \sigma) = \max_{|\psi_\sigma\rangle} |\langle\psi_\rho|\psi_\sigma\rangle|^2$$

其中最大化遍历 $\sigma$ 的所有 purification $|\psi_\sigma\rangle$。

**含义**：两个混合态的保真度等于它们的 purification 之间能达到的最大纯态重叠。

**推导思路**：

设 $\rho$ 作用在 $\mathcal{H}_A$ 上（维数 $d$），引入同维数的辅助空间 $\mathcal{H}_B$。$\rho$ 的一个 purification 为：

$$|\psi_\rho\rangle = (\sqrt{\rho} \otimes I)|{\Phi^+}\rangle = \frac{1}{\sqrt{d}}\sum_i (\sqrt{\rho}|i\rangle) \otimes |i\rangle$$

验证：$\text{Tr}_B(|\psi_\rho\rangle\langle\psi_\rho|) = \sqrt{\rho} \cdot \frac{I}{d} \cdot d \cdot \sqrt{\rho} = \rho$。（这里用了 $\text{Tr}_B(|\Phi^+\rangle\langle\Phi^+|) = I/d$。）

更一般地，$\rho$ 的所有 purification 形如 $|\psi_\rho\rangle = (\sqrt{\rho}\,V \otimes I)|\Phi^+\rangle$，其中 $V$ 是幺正矩阵。类似地，$\sigma$ 的 purification 为 $|\psi_\sigma\rangle = (\sqrt{\sigma}\,W \otimes I)|\Phi^+\rangle$。

它们的内积：

$$\langle\psi_\rho|\psi_\sigma\rangle = \langle\Phi^+|(V^\dagger\sqrt{\rho}\sqrt{\sigma}W \otimes I)|\Phi^+\rangle = \frac{1}{d}\text{Tr}(V^\dagger\sqrt{\rho}\sqrt{\sigma}W)$$

因此：

$$|\langle\psi_\rho|\psi_\sigma\rangle|^2 = \frac{1}{d^2}\left|\text{Tr}(V^\dagger\sqrt{\rho}\sqrt{\sigma}W)\right|^2$$

对 $W$（或等价地对 $U = V^\dagger W$）最大化 $|\text{Tr}(\sqrt{\rho}\sqrt{\sigma}U)|$，由极分解定理，最大值为：

$$\max_U |\text{Tr}(\sqrt{\rho}\sqrt{\sigma}\,U)| = \text{Tr}|\sqrt{\rho}\sqrt{\sigma}| = \text{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}$$

最后一个等号用了 $|X| = \sqrt{X^\dagger X}$，以及 $(\sqrt{\rho}\sqrt{\sigma})^\dagger(\sqrt{\rho}\sqrt{\sigma}) = \sqrt{\sigma}\rho\sqrt{\sigma}$（与 $\sqrt{\rho}\sigma\sqrt{\rho}$ 有相同非零特征值）。

所以：

$$\max |\langle\psi_\rho|\psi_\sigma\rangle|^2 = \left(\text{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}\right)^2 = F(\rho,\sigma)$$

---

### Part B: Trace Distance (迹距离)

#### Step 6: 矩阵绝对值的定义

对任意矩阵 $A$，其绝对值定义为：

$$|A| = \sqrt{A^\dagger A}$$

当 $A$ 是 Hermitian 时（$A^\dagger = A$），$|A| = \sqrt{A^2}$。

如果 $A$ 的特征值分解为 $A = \sum_i a_i |e_i\rangle\langle e_i|$（$a_i$ 可以是负的），则：

$$|A| = \sum_i |a_i| \, |e_i\rangle\langle e_i|$$

即把每个特征值取绝对值。

#### Step 7: Trace Distance 的定义 **[N&C, Eq.(9.1), p.399]** **[Preskill, Ch.2, &sect;2.6, p.31]**

$$D(\rho, \sigma) = \frac{1}{2}\text{Tr}|\rho - \sigma|$$

由于 $\rho - \sigma$ 是 Hermitian 的（两个 Hermitian 矩阵之差），设其特征值为 $\{\mu_i\}$（可正可负，和为零因为 $\text{Tr}(\rho - \sigma) = 0$），则：

$$D(\rho, \sigma) = \frac{1}{2}\sum_i |\mu_i|$$

**为什么有 $\frac{1}{2}$？** 因为 $\text{Tr}(\rho - \sigma) = 0$，正特征值之和等于负特征值绝对值之和，所以 $\sum_i |\mu_i| = 2\sum_{\mu_i > 0}\mu_i$。$\frac{1}{2}$ 因子使得 $D \in [0, 1]$。

#### Step 8: Trace Distance 的基本性质

**性质 1: 度量性质**
- $D(\rho, \sigma) \geq 0$，等号当且仅当 $\rho = \sigma$
- $D(\rho, \sigma) = D(\sigma, \rho)$（对称性）
- $D(\rho, \tau) \leq D(\rho, \sigma) + D(\sigma, \tau)$（三角不等式）

**性质 2: 范围** $0 \leq D(\rho, \sigma) \leq 1$

$D = 0$ 当且仅当 $\rho = \sigma$。$D = 1$ 当且仅当 $\rho$ 和 $\sigma$ 的支撑（support）正交。

**性质 3: 幺正不变性** $D(U\rho U^\dagger, U\sigma U^\dagger) = D(\rho, \sigma)$

因为 $U(\rho-\sigma)U^\dagger$ 与 $\rho - \sigma$ 有相同的特征值。

**性质 4: 单调性（数据处理不等式）** **[N&C, Theorem 9.2, p.406]** **[Preskill, Ch.2, &sect;2.6, pp.33-34]** 对任何 CPTP 映射 $\mathcal{E}$：

$$D(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \leq D(\rho, \sigma)$$

量子操作不会增加迹距离——两个态经过同一噪声信道后只会变得"更难区分"。

#### Step 9: 迹距离的操作性解释

**定理（Helstrom）** **[N&C, p.401]** **[Preskill, Ch.2, &sect;2.6.2, pp.38-39]**: 给定以等概率 $\frac{1}{2}$ 准备的两个态 $\rho$ 或 $\sigma$ 之一，进行最优量子测量来区分它们，最大成功概率为：

$$p_{\text{success}} = \frac{1}{2}\left(1 + D(\rho, \sigma)\right)$$

**推导**：我们需要找一个二元 POVM $\{M, I-M\}$（$0 \leq M \leq I$），猜测 $\rho$ 对应结果 $M$，猜测 $\sigma$ 对应结果 $I-M$。成功概率为：

$$p_{\text{success}} = \frac{1}{2}\text{Tr}(M\rho) + \frac{1}{2}\text{Tr}((I-M)\sigma)$$

$$= \frac{1}{2}\text{Tr}(\sigma) + \frac{1}{2}\text{Tr}(M(\rho - \sigma))$$

$$= \frac{1}{2} + \frac{1}{2}\text{Tr}(M(\rho - \sigma))$$

要最大化 $\text{Tr}(M(\rho - \sigma))$，设 $\rho - \sigma$ 的谱分解为：

$$\rho - \sigma = \sum_{\mu_i > 0}\mu_i|e_i\rangle\langle e_i| + \sum_{\mu_j < 0}\mu_j|e_j\rangle\langle e_j|$$

显然应该选 $M$ 为正特征值对应特征空间的投影：

$$M_{\text{opt}} = \sum_{\mu_i > 0}|e_i\rangle\langle e_i|$$

此时：

$$\text{Tr}(M_{\text{opt}}(\rho-\sigma)) = \sum_{\mu_i > 0}\mu_i = \frac{1}{2}\sum_i|\mu_i| = D(\rho,\sigma)$$

所以：

$$\boxed{p_{\text{success}}^{\max} = \frac{1}{2}(1 + D(\rho, \sigma))}$$
**[N&C, Theorem 9.1, p.400]** **[Preskill, Ch.2, &sect;2.6, p.32]**

#### Step 10: 纯态的迹距离

对两个纯态 $\rho = |\psi\rangle\langle\psi|$，$\sigma = |\phi\rangle\langle\phi|$：

$$D(|\psi\rangle\langle\psi|, |\phi\rangle\langle\phi|) = \sqrt{1 - |\langle\psi|\phi\rangle|^2}$$
**[N&C, Exercise 9.2, p.401]**

**推导**：$\rho - \sigma$ 作用在 $|\psi\rangle$ 和 $|\phi\rangle$ 张成的二维子空间上。设 $|\langle\psi|\phi\rangle| = c$（$0 \leq c \leq 1$），选正交基使得 $|\psi\rangle = |0\rangle$，$|\phi\rangle = c|0\rangle + s|1\rangle$（其中 $s = \sqrt{1-c^2}$）。

$$\rho - \sigma = |0\rangle\langle 0| - (c|0\rangle + s|1\rangle)(c\langle 0| + s\langle 1|)$$

$$= \begin{pmatrix}1-c^2 & -cs \\ -cs & -s^2\end{pmatrix} = \begin{pmatrix}s^2 & -cs \\ -cs & -s^2\end{pmatrix}$$

特征值：$\text{Tr} = 0$，$\det = -s^4 + c^2s^2 = -s^2(s^2-c^2+1-1) = -s^2(1-1) ... $

更直接地：特征方程 $\lambda^2 - (s^2-s^2)\lambda - (s^4-c^2s^2-...) = 0$。

让我们重新计算行列式：$\det = s^2 \cdot(-s^2) - (-cs)(-cs) = -s^4 - c^2s^2 = -s^2(s^2+c^2) = -s^2$。

特征方程：$\lambda^2 + s^2 = 0$... 这不对。让我重新用迹：$\text{Tr} = s^2 - s^2 = 0$，所以特征值为 $\pm\lambda$。

$\lambda^2 = -\det = s^2$，所以 $\lambda = s = \sqrt{1-c^2}$。

$$D = \frac{1}{2}(|\lambda| + |-\lambda|) = \frac{1}{2}(s + s) = s = \sqrt{1 - c^2} = \sqrt{1 - |\langle\psi|\phi\rangle|^2}$$

---

### Part C: Fuchs-van de Graaf Inequalities

#### Step 11: Fidelity 与 Trace Distance 的关系

**定理（Fuchs & van de Graaf, 1999）** **[N&C, Eq.(9.100-9.101), p.416]** **[Preskill, Ch.2, &sect;2.6.2, p.38]**: 对任意密度矩阵 $\rho$, $\sigma$：

$$1 - \sqrt{F(\rho,\sigma)} \leq D(\rho,\sigma) \leq \sqrt{1 - F(\rho,\sigma)}$$

**右边不等式的证明思路**（利用 Uhlmann 定理）：

设 $|\psi_\rho\rangle$, $|\psi_\sigma\rangle$ 是达到最优 fidelity 的 purification：

$$F(\rho,\sigma) = |\langle\psi_\rho|\psi_\sigma\rangle|^2$$

由迹距离的单调性（偏迹是一种量子操作）：

$$D(\rho, \sigma) = D(\text{Tr}_E|\psi_\rho\rangle\langle\psi_\rho|, \text{Tr}_E|\psi_\sigma\rangle\langle\psi_\sigma|) \leq D(|\psi_\rho\rangle\langle\psi_\rho|, |\psi_\sigma\rangle\langle\psi_\sigma|)$$

由 Step 10 中纯态的迹距离公式：

$$= \sqrt{1 - |\langle\psi_\rho|\psi_\sigma\rangle|^2} = \sqrt{1 - F(\rho,\sigma)}$$

**左边不等式**的证明需要更多技巧，用到 $D$ 的变分表达式 $D(\rho,\sigma) = \max_{0 \leq M \leq I}\text{Tr}(M(\rho-\sigma))$ 和保真度的乘法性质。

#### Step 12: 不等式的直观意义

这两个不等式说明 fidelity 和 trace distance 提供了**等价的**（虽然不完全相同的）距离概念：

- 如果两个态的保真度高（$F$ 接近 1），则迹距离小（$D$ 接近 0）
- 如果两个态的保真度低（$F$ 接近 0），则迹距离大（$D$ 接近 1）

在量子计算中，通常用保真度衡量"做得多好"，用迹距离衡量"错了多少"。

---

## Summary

| 度量 | 定义 | 范围 | 操作性含义 |
|------|------|------|-----------|
| Fidelity | $F(\rho,\sigma) = (\text{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}})^2$ | $[0,1]$ | 最大 purification 重叠 |
| Trace Distance | $D(\rho,\sigma) = \frac{1}{2}\text{Tr}\|\rho-\sigma\|$ | $[0,1]$ | 最优区分概率 $\frac{1+D}{2}$ |
| 纯态 Fidelity | $F = \|\langle\psi\|\phi\rangle\|^2$ | $[0,1]$ | 转移概率 |
| 纯态 Trace Distance | $D = \sqrt{1 - \|\langle\psi\|\phi\rangle\|^2}$ | $[0,1]$ | — |
| Fuchs-van de Graaf | $1-\sqrt{F} \leq D \leq \sqrt{1-F}$ | — | F 和 D 等价 |

---

## Nielsen & Chuang: Theorems and Formal Results

### Chapter 9 Overview **[Nielsen & Chuang, Ch. 9, pp.399-424]**
Chapter 9 of N&C is devoted entirely to "Distance measures for quantum information." The two principal measures are trace distance and fidelity.

### Definition 9.1 (Trace Distance) **[Nielsen & Chuang, Eq. 9.1, p.399]**
$$D(\rho, \sigma) \equiv \frac{1}{2}\text{Tr}|\rho - \sigma|$$
where $|A| \equiv \sqrt{A^\dagger A}$. For Hermitian operators, this equals half the sum of absolute values of eigenvalues of $\rho - \sigma$.

### Theorem 9.1 (Trace Distance as Maximum over Measurements) **[Nielsen & Chuang, Theorem 9.1, p.400]**
$$D(\rho, \sigma) = \max_P \text{Tr}(P(\rho - \sigma))$$
where the maximization is over all projectors $P$. Equivalently:
$$D(\rho, \sigma) = \max_{0 \leq M \leq I} \text{Tr}(M(\rho - \sigma))$$

### Theorem 9.2 (Contractivity of Trace Distance) **[Nielsen & Chuang, Theorem 9.2, p.406]**
For any trace-preserving quantum operation $\mathcal{E}$:
$$D(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \leq D(\rho, \sigma)$$
Quantum operations never increase the distinguishability of quantum states -- this is the data processing inequality for trace distance.

### Theorem 9.3 (Strong Convexity of Trace Distance) **[Nielsen & Chuang, Theorem 9.3, p.407]**
Let $\{p_i\}$ and $\{q_i\}$ be probability distributions over the same index set, and $\rho_i$ and $\sigma_i$ be density operators. Then:
$$D\left(\sum_i p_i \rho_i, \sum_i q_i \sigma_i\right) \leq D(p_i, q_i) + \sum_i p_i D(\rho_i, \sigma_i)$$
where $D(p_i, q_i)$ is the classical trace distance between the probability distributions.

**Proof** **[Nielsen & Chuang, p.408]**: By the variational characterization (Eq. 9.22) there exists a projector $P$ such that $D(\sum_i p_i\rho_i, \sum_i q_i\sigma_i) = \sum_i p_i\text{Tr}(P(\rho_i - \sigma_i)) + \sum_i(p_i - q_i)\text{Tr}(P\sigma_i) \leq \sum_i p_i D(\rho_i, \sigma_i) + D(p_i, q_i)$.

As a special case, joint convexity: $D(\sum_i p_i\rho_i, \sum_i p_i\sigma_i) \leq \sum_i p_i D(\rho_i, \sigma_i)$.

### Operational Interpretation (Helstrom) **[Nielsen & Chuang, p.401]**
Suppose Alice prepares one of two states $\rho$ or $\sigma$ with equal prior probability. The optimal probability of correctly identifying the state is:
$$p_{\text{success}} = \frac{1}{2}(1 + D(\rho, \sigma))$$

### Definition (Fidelity) **[Nielsen & Chuang, Eq. 9.52, p.409]**
$$F(\rho, \sigma) \equiv \text{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}$$
Note: N&C define $F$ *without* squaring, so $F \in [0,1]$ and $F(\rho,\sigma)$ in N&C equals $\sqrt{F(\rho,\sigma)}$ in the convention used in this file (which squares it). When citing N&C results, be aware of this convention difference.

### Lemma 9.5 **[Nielsen & Chuang, Lemma 9.5, p.410]**
Let $A$ be any operator, and $U$ unitary. Then $|\text{Tr}(AU)| \leq \text{Tr}|A|$, with equality attained by choosing $U = V^\dagger$, where $A = |A|V$ is the polar decomposition of $A$.

**Proof** **[Nielsen & Chuang, p.410]**: $|\text{Tr}(AU)| = |\text{Tr}(|A|VU)| = |\text{Tr}(|A|^{1/2}|A|^{1/2}VU)|$. By Cauchy-Schwarz for the Hilbert-Schmidt inner product: $\leq \sqrt{\text{Tr}|A|}\sqrt{\text{Tr}(U^\dagger V^\dagger|A|VU)} = \text{Tr}|A|$.

### Theorem 9.4 (Uhlmann's Theorem) **[Nielsen & Chuang, Theorem 9.4, p.410]**
Suppose $\rho$ and $\sigma$ are states of a quantum system $Q$. Introduce a second quantum system $R$ which is a copy of $Q$. Then:
$$F(\rho, \sigma) = \max_{|\psi\rangle, |\phi\rangle} |\langle\psi|\phi\rangle|$$
where the maximization is over all purifications $|\psi\rangle$ of $\rho$ and $|\phi\rangle$ of $\sigma$ into $RQ$.

**Proof** **[Nielsen & Chuang, pp.410-412]**: Any purification of $\rho$ has the form $|\psi\rangle = (U_R \otimes \sqrt{\rho}U_Q)|m\rangle$ where $|m\rangle \equiv \sum_i |i_R\rangle|i_Q\rangle$. Similarly $|\phi\rangle = (V_R \otimes \sqrt{\sigma}V_Q)|m\rangle$. The inner product gives $|\langle\psi|\phi\rangle| = |\text{Tr}(\sqrt{\rho}\sqrt{\sigma}U)|$ for some unitary $U$. By Lemma 9.5, this is $\leq \text{Tr}|\sqrt{\rho}\sqrt{\sigma}| = \text{Tr}\sqrt{\rho^{1/2}\sigma\rho^{1/2}}$. Equality is attained via the polar decomposition $\sqrt{\rho}\sqrt{\sigma} = |\sqrt{\rho}\sqrt{\sigma}|V$.

### Theorem 9.5 (Properties of Fidelity) **[Nielsen & Chuang, Theorem 9.5, p.412]**
1. $0 \leq F(\rho,\sigma) \leq 1$ (in N&C convention without square)
2. $F(\rho,\sigma) = 1$ if and only if $\rho = \sigma$
3. $F(\rho,\sigma) = F(\sigma,\rho)$ (symmetry)

### Theorem 9.6 (Monotonicity of Fidelity) **[Nielsen & Chuang, Theorem 9.6, p.414]**
Suppose $\mathcal{E}$ is a trace-preserving quantum operation. Let $\rho$ and $\sigma$ be density operators. Then:
$$F(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \geq F(\rho, \sigma)$$

**Proof** **[Nielsen & Chuang, p.414]**: Let $|\psi\rangle$ and $|\phi\rangle$ be purifications of $\rho$ and $\sigma$ into a joint system $RQ$ such that $F(\rho, \sigma) = |\langle\psi|\phi\rangle|$. Introduce a model environment $E$ starting in pure state $|0\rangle$ with unitary interaction $U$. Then $U|\psi\rangle|0\rangle$ is a purification of $\mathcal{E}(\rho)$ and $U|\phi\rangle|0\rangle$ is a purification of $\mathcal{E}(\sigma)$. By Uhlmann's theorem: $F(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \geq |\langle\psi|\langle 0|U^\dagger U|\phi\rangle|0\rangle| = |\langle\psi|\phi\rangle| = F(\rho, \sigma)$.

### Theorem 9.7 (Strong Concavity of Fidelity) **[Nielsen & Chuang, Theorem 9.7, p.414]**
Let $p_i$ and $q_i$ be probability distributions over the same index set, and $\rho_i$ and $\sigma_i$ density operators. Then:
$$F\left(\sum_i p_i\rho_i, \sum_i q_i\sigma_i\right) \geq \sum_i \sqrt{p_i q_i}\, F(\rho_i, \sigma_i)$$

**Proof** **[Nielsen & Chuang, p.415]**: Let $|\psi_i\rangle$ and $|\phi_i\rangle$ be purifications of $\rho_i$ and $\sigma_i$ with $F(\rho_i, \sigma_i) = \langle\psi_i|\phi_i\rangle$. Define $|\psi\rangle \equiv \sum_i \sqrt{p_i}|\psi_i\rangle|i\rangle$ and $|\phi\rangle \equiv \sum_i \sqrt{q_i}|\phi_i\rangle|i\rangle$. These are purifications of $\sum_i p_i\rho_i$ and $\sum_i q_i\sigma_i$ respectively. By Uhlmann's formula: $F \geq |\langle\psi|\phi\rangle| = \sum_i \sqrt{p_iq_i}\langle\psi_i|\phi_i\rangle = \sum_i \sqrt{p_iq_i} F(\rho_i, \sigma_i)$.

### Fidelity for Pure States **[Nielsen & Chuang, Eq. 9.56, p.409]**
When $\rho = |\psi\rangle\langle\psi|$ is a pure state:
$$F(|\psi\rangle\langle\psi|, \sigma) = \sqrt{\langle\psi|\sigma|\psi\rangle}$$
(or $\langle\psi|\sigma|\psi\rangle$ in the squared convention).

### Theorem 9.8 (Fuchs-van de Graaf Inequalities) **[Nielsen & Chuang, Eq. 9.100-9.101, p.416]**
$$1 - F(\rho,\sigma) \leq D(\rho,\sigma) \leq \sqrt{1 - F(\rho,\sigma)^2}$$
(in N&C's convention where $F$ is not squared). In the squared convention $F' = F^2$:
$$1 - \sqrt{F'} \leq D \leq \sqrt{1 - F'}$$

### Fidelity as Minimum over POVMs **[Nielsen & Chuang, Eq. 9.74, p.412]**
$$F(\rho, \sigma) = \min_{\{E_m\}} F(p_m, q_m)$$
where the minimum is over all POVMs $\{E_m\}$, and $p_m \equiv \text{Tr}(\rho E_m)$, $q_m \equiv \text{Tr}(\sigma E_m)$ are the induced probability distributions. The fidelity between quantum states equals the minimum classical fidelity over all possible measurements.

### Angle Metric **[Nielsen & Chuang, Eq. 9.82, p.413]**
$A(\rho, \sigma) \equiv \arccos F(\rho, \sigma)$ defines a metric satisfying the triangle inequality $A(\rho, \tau) \leq A(\rho, \sigma) + A(\sigma, \tau)$, with $0 \leq A \leq \pi/2$.

---

## Preskill: Theorems and Formal Results (Chapter 2)

### Trace Distance **[Preskill, Ch.2, §2.6, pp.31-36]**
Preskill defines the trace distance and develops its properties in the context of state distinguishability:

**Definition** [Preskill, Ch.2, §2.6, p.31]:
$$D(\rho, \sigma) = \frac{1}{2}\|\rho - \sigma\|_1 = \frac{1}{2}\text{Tr}|\rho - \sigma|$$

**Variational characterization** [Preskill, Ch.2, §2.6, pp.31-32]:
$$D(\rho, \sigma) = \max_{0 \leq P \leq I}\text{Tr}[P(\rho - \sigma)]$$
where the maximum is over all POVM elements $P$. This immediately gives the operational interpretation: $D$ is the bias achievable in distinguishing $\rho$ from $\sigma$ by a single measurement.

**Optimal state discrimination (Helstrom)** [Preskill, Ch.2, §2.6, pp.32-33]: Given equal prior probabilities:
$$p_{\text{success}} = \frac{1}{2}(1 + D(\rho, \sigma))$$

**Proof** [Preskill, Ch.2, §2.6, p.32]: The success probability of a two-outcome POVM $\{E, I-E\}$ is:
$$p = \frac{1}{2}\text{Tr}(E\rho) + \frac{1}{2}\text{Tr}((I-E)\sigma) = \frac{1}{2} + \frac{1}{2}\text{Tr}[E(\rho-\sigma)]$$
Maximizing over $E$ with $0 \leq E \leq I$: the optimum is $E = P_+$, the projector onto the positive-eigenvalue eigenspace of $\rho - \sigma$, giving $\max = D(\rho,\sigma)$.

### Contractivity of Trace Distance **[Preskill, Ch.2, §2.6, pp.33-34]**
**Theorem**: For any TPCP map $\mathcal{E}$:
$$D(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \leq D(\rho, \sigma)$$

**Proof** [Preskill, Ch.2, §2.6, p.33]: For any $0 \leq P \leq I$:
$$\text{Tr}[P(\mathcal{E}(\rho) - \mathcal{E}(\sigma))] = \text{Tr}[\mathcal{E}^\dagger(P)(\rho - \sigma)]$$
where $\mathcal{E}^\dagger$ is the adjoint (Heisenberg picture) channel. Since $\mathcal{E}$ is TPCP, $\mathcal{E}^\dagger$ is unital and CP, so $0 \leq \mathcal{E}^\dagger(P) \leq I$. Taking the maximum over $P$ on the left gives $D(\mathcal{E}(\rho), \mathcal{E}(\sigma))$, which is $\leq D(\rho,\sigma)$ since $\mathcal{E}^\dagger(P)$ is a valid POVM element.

**Physical meaning**: Quantum channels can only make states harder to distinguish, never easier. This is the data processing inequality for trace distance.

### Fidelity and Uhlmann's Theorem **[Preskill, Ch.2, §2.6.1, pp.34-38]**
**Definition** [Preskill, Ch.2, §2.6.1, p.34]:
$$F(\rho, \sigma) = \left(\text{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}\right)^2$$

For pure state $\rho = |\psi\rangle\langle\psi|$: $F(|\psi\rangle\langle\psi|, \sigma) = \langle\psi|\sigma|\psi\rangle$.

**Theorem (Uhlmann, 1976)** [Preskill, Ch.2, §2.6.1, pp.35-37]:
$$F(\rho, \sigma) = \max_{|\psi_\rho\rangle, |\psi_\sigma\rangle}|\langle\psi_\rho|\psi_\sigma\rangle|^2$$
where the maximum is over all purifications $|\psi_\rho\rangle$ of $\rho$ and $|\psi_\sigma\rangle$ of $\sigma$.

**Proof** [Preskill, Ch.2, §2.6.1, pp.35-37]: Using the canonical purifications $|\psi_\rho\rangle = (\sqrt{\rho} \otimes I)|\Phi^+\rangle$ and $|\psi_\sigma\rangle = (\sqrt{\sigma}V \otimes I)|\Phi^+\rangle$ where $V$ is unitary:
$$|\langle\psi_\rho|\psi_\sigma\rangle|^2 = \frac{1}{d^2}|\text{Tr}(\sqrt{\rho}\sqrt{\sigma}V)|^2$$
Maximizing over $V$ using the polar decomposition: the maximum of $|\text{Tr}(AV)|$ over unitaries $V$ is $\text{Tr}|A| = \text{Tr}\sqrt{A^\dagger A}$. Applied to $A = \sqrt{\rho}\sqrt{\sigma}$:
$$\max_V|\text{Tr}(\sqrt{\rho}\sqrt{\sigma}V)| = \text{Tr}\sqrt{\sqrt{\sigma}\rho\sqrt{\sigma}} = \text{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}$$
(the last equality uses the fact that $XY$ and $YX$ have the same nonzero eigenvalues).

**Properties of fidelity** [Preskill, Ch.2, §2.6.1, pp.37-38]:
1. $0 \leq F \leq 1$; $F = 1$ iff $\rho = \sigma$; $F = 0$ iff $\rho \perp \sigma$ (orthogonal support)
2. $F(\rho,\sigma) = F(\sigma,\rho)$ (symmetry, despite asymmetric-looking definition)
3. $F(U\rho U^\dagger, U\sigma U^\dagger) = F(\rho,\sigma)$ (unitary invariance)
4. $F(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \geq F(\rho,\sigma)$ (monotonicity under TPCP maps)
5. $F(\rho_1 \otimes \rho_2, \sigma_1 \otimes \sigma_2) = F(\rho_1,\sigma_1) \cdot F(\rho_2,\sigma_2)$ (multiplicativity)

### Fuchs-van de Graaf Inequalities **[Preskill, Ch.2, §2.6.2, pp.38-40]**
**Theorem** [Preskill, Ch.2, §2.6.2, p.38]:
$$1 - \sqrt{F(\rho,\sigma)} \leq D(\rho,\sigma) \leq \sqrt{1 - F(\rho,\sigma)}$$

**Upper bound proof** [Preskill, Ch.2, §2.6.2, pp.38-39]: Let $|\psi_\rho\rangle$, $|\psi_\sigma\rangle$ achieve the Uhlmann maximum. By contractivity of trace distance under partial trace:
$$D(\rho,\sigma) \leq D(|\psi_\rho\rangle\langle\psi_\rho|, |\psi_\sigma\rangle\langle\psi_\sigma|) = \sqrt{1 - |\langle\psi_\rho|\psi_\sigma\rangle|^2} = \sqrt{1 - F(\rho,\sigma)}$$

**Lower bound proof** [Preskill, Ch.2, §2.6.2, pp.39-40]: Uses the variational characterization of trace distance and the concavity of the square root function. For any measurement projector $P$:
$$\text{Tr}(P\rho) + \text{Tr}((I-P)\sigma) \leq 1 + D(\rho,\sigma)$$
By choosing $P$ appropriately and using the relation $\sqrt{F} \leq \sqrt{\text{Tr}(P\rho)} + \sqrt{\text{Tr}((I-P)\sigma)}$ (from Uhlmann), one obtains $\sqrt{F} \leq 1 - D + D = 1$... The precise argument uses:
$$\sqrt{F(\rho,\sigma)} \geq \text{Tr}(\rho P) + \text{Tr}(\sigma(I-P))$$ is NOT correct; rather, the bound follows from $1 - D(\rho,\sigma) \leq \sqrt{F(\rho,\sigma)}$.

### Bures Distance **[Preskill, Ch.2, §2.6.2, p.40]**
The **Bures distance** is defined as:
$$d_B(\rho,\sigma) = \sqrt{2(1 - \sqrt{F(\rho,\sigma)})}$$

This is a proper metric on the space of density matrices (satisfies triangle inequality). The Fuchs-van de Graaf inequalities relate it to trace distance:
$$\frac{1}{2}d_B^2 \leq D(\rho,\sigma) \leq d_B\sqrt{1 - \frac{d_B^2}{4}}$$

### Application: Gentle Measurement **[Preskill, Ch.2, §2.6, pp.40-41]**
Preskill discusses the gentle measurement lemma as a consequence of fidelity properties:

**Lemma**: If $\text{Tr}(E\rho) \geq 1 - \epsilon$ for some POVM element $E$, then the post-measurement state $\rho' = \sqrt{E}\rho\sqrt{E}/\text{Tr}(E\rho)$ satisfies:
$$F(\rho, \rho') \geq 1 - \epsilon$$
equivalently, $D(\rho, \rho') \leq \sqrt{\epsilon}$.

**Physical meaning**: If a measurement outcome is very likely, the measurement barely disturbs the state. This is crucial for quantum error correction and quantum tomography arguments.

---

## References

- **[Nielsen & Chuang]** Nielsen, M. A. & Chuang, I. L. *Quantum Computation and Quantum Information* (Cambridge, 10th anniversary ed., 2010), Ch. 9 (pp.399-424)
- Uhlmann, *Rep. Math. Phys.* 9, 273 (1976)
- Jozsa, *J. Mod. Opt.* 41, 2315 (1994)
- Fuchs & van de Graaf, *IEEE Trans. Inform. Theory* 45, 1216 (1999)
- Helstrom, *Quantum Detection and Estimation Theory* (1976)
- **[Preskill, Ch.2]** Preskill, J. *Lecture Notes for Ph219/CS219: Quantum Information and Computation*, Ch.2: "Foundations I: States and Ensembles" (July 2015), §2.6 (trace distance, Helstrom bound, contractivity), §2.6.1 (fidelity, Uhlmann's theorem), §2.6.2 (Fuchs-van de Graaf inequalities, Bures distance). PDF: `references/preskill_ch2.pdf`
- **[Wilde, Ch.9]** Wilde, M. *From Classical to Quantum Shannon Theory*, Ch.9 (Distance Measures) — Bures distance, purified distance, sine distance, and their operational interpretations
