# Quantum Code Distance Bounds

> **Tags**: `code-distance`, `bounds`, `singleton`, `hamming`, `qec`

## Statement

量子纠错码的参数 $[[n, k, d]]$ 受到基本的数学界限约束。本文推导两个最重要的界限：

1. **Quantum Singleton Bound**（量子 Singleton 界）：$d \leq \frac{n-k}{2} + 1$，对所有量子码成立
2. **Quantum Hamming Bound**（量子 Hamming 界）：$\sum_{j=0}^{t} \binom{n}{j} 3^j \leq 2^{n-k}$，对非退化码成立

## Prerequisites

- **量子纠错基础**：$[[n, k, d]]$ 码的定义，Knill-Laflamme 条件
- **线性代数**：子空间维度、秩-零度定理
- **组合数学**：二项式系数、计数论证

---

## Part 1: Quantum Singleton Bound **[Preskill Ch.7, §7.8.3, pp.32-34, Eq. 7.103; Nielsen & Chuang, Theorem 10.2, p.444; Bacon, p.12-13]**

### 定理陈述

对于任意 $[[n, k, d]]$ 量子纠错码：

$$k + 2(d-1) \leq n$$

等价形式：

$$d \leq \frac{n - k}{2} + 1$$

达到此界限的码称为 **quantum MDS (Maximum Distance Separable) 码**。

### 推导

#### Step 1: Setup and notation

设 $\mathcal{C}$ 是一个 $[[n, k, d]]$ 量子码，码空间维度 $K = 2^k$。$P$ 是向码空间 $\mathcal{C}$ 的投影算子。码距 $d$ 意味着码能纠正任意 $t = \lfloor(d-1)/2\rfloor$ 个错误，且能**检测**任意 $d-1$ 个错误。

"检测 $d-1$ 个错误"的精确含义：对于任意 Pauli 权重 $\leq d-1$ 的错误 $E$（即 $E$ 在至多 $d-1$ 个量子比特上非平凡），要么：
- $E$ 能被检测到（syndrome 非零），即 $E$ 与某个稳定子反对易
- $E$ 是一个稳定子（$E \in \mathcal{S}$），在码空间上作用为恒等

用 Knill-Laflamme 条件表述：对于任意权重 $\leq d-1$ 的 Pauli 算子 $E$：

$$P E P = c(E) P$$

其中 $c(E)$ 是标量（$c(E) = 0$ 如果 $E$ 可检测，$c(E) = 1$ 如果 $E \in \mathcal{S}$）。

#### Step 2: Partition the qubits

将 $n$ 个量子比特分成三组：
- $A$：前 $d - 1$ 个量子比特
- $B$：接下来的 $d - 1$ 个量子比特
- $C$：剩下的 $n - 2(d-1)$ 个量子比特

（需要 $n \geq 2(d-1)$，否则界限平凡成立。）

#### Step 3: Reduced density matrix argument **[Preskill Ch.7, §7.8.3, pp.32-34, Eq. 7.105-7.112]**

考虑码空间中的两个正交态 $|\psi_1\rangle, |\psi_2\rangle \in \mathcal{C}$。

**关键引理（No-cloning bound / Singleton-type argument）**：对于子系统 $A$（含 $d-1$ 个量子比特），码空间中所有态在 $A$ 上的约化密度矩阵相同：

$$\rho_A^{(1)} = \text{tr}_{BC}(|\psi_1\rangle\langle\psi_1|) = \text{tr}_{BC}(|\psi_2\rangle\langle\psi_2|) = \rho_A^{(2)}$$

**证明此引理**：

任意只作用在 $A$ 上的算子 $O_A$ 都可以写为 $O_A \otimes I_{BC}$。$O_A$ 的 Pauli 权重最多为 $|A| = d - 1$。因此，对于码空间中的任意两个正交基矢 $|\psi_i\rangle, |\psi_j\rangle$：

$$\langle\psi_i| O_A \otimes I_{BC} |\psi_j\rangle = \langle\psi_i| (O_A \otimes I_{BC}) |\psi_j\rangle$$

由 Knill-Laflamme 条件（$O_A \otimes I_{BC}$ 的 Pauli 展开中每一项的权重 $\leq d - 1$）：

$$\langle\psi_i| O_A \otimes I_{BC} |\psi_j\rangle = c(O_A) \delta_{ij}$$

这意味着：

$$\text{tr}(\rho_A^{(i)} O_A) = \langle\psi_i| O_A \otimes I_{BC} |\psi_i\rangle = c(O_A)$$

对所有 $i$ 相同。而且当 $i \neq j$ 时：

$$\text{tr}_A(\rho_A^{(i)} O_A) - \text{tr}_A(\rho_A^{(j)} O_A) = c(O_A) - c(O_A) = 0$$

由于这对所有算子 $O_A$ 成立，$\rho_A^{(i)} = \rho_A^{(j)}$ 对所有 $i, j$ 成立。引理得证。

#### Step 4: Dimension counting

同理，子系统 $B$（也含 $d-1$ 个量子比特）也有相同的性质：码空间中所有态在 $B$ 上的约化密度矩阵相同。

现在考虑子系统 $AB$（含 $2(d-1)$ 个量子比特）。码空间中的不同态在 $AB$ 上的约化密度矩阵可以不同（因为 $|AB| = 2(d-1)$ 可能 $\geq d$，Knill-Laflamme 不再保证）。

但我们知道：码空间中的所有信息（$k$ 个逻辑量子比特）最终都编码在 $n$ 个物理量子比特中。由于子系统 $A$ 不携带任何关于编码态的信息（所有态的 $\rho_A$ 相同），所有信息必须在子系统 $BC$ 中恢复。

**Hilbert 空间维度约束**：子系统 $C$ 有 $n - 2(d-1)$ 个量子比特，维度 $2^{n-2(d-1)}$。

由于子系统 $A$ 不携带编码信息，子系统 $BC$ 必须能完全恢复编码态。更严格地，由于 $\rho_A$ 对所有码字相同，通过 Schumacher 的量子信息理论论证，码空间可以"无损地"从 $BC$ 恢复。

但码空间维度 $2^k$ 不能超过子系统 $C$ 的维度 $2^{n-2(d-1)}$（因为 $B$ 也不携带编码信息，同理）。

等等，更准确的论证：由于 $A$ 和 $B$ 都不携带编码信息，我们需要更小心。实际上，关键的约束来自于**量子纠删码的界限**：

#### Step 5: Erasure correction argument（纠删码论证） **[Preskill Ch.7, §7.8.2, pp.31-32; Bacon, p.12]**

一个码距为 $d$ 的量子码可以纠正 $d-1$ 个 qubit 的**擦除**（erasure）错误。

**擦除（erasure）**意味着我们知道哪些量子比特丢失了，只是不知道它们原来的状态。这比一般错误更容易纠正。

**性质**：能纠正 $t$ 个一般错误的码（$d = 2t + 1$）能纠正 $2t = d - 1$ 个擦除错误。

如果子系统 $A$（$d - 1$ 个量子比特）被擦除，码仍然可以从剩余的 $n - (d-1)$ 个量子比特恢复。这意味着码空间的维度不能超过剩余系统的维度：

$$2^k \leq 2^{n-(d-1)}$$

但这只给出 $k \leq n - d + 1$（经典 Singleton bound），不够强。

**量子加强**：在量子情况下，纠正擦除还需要恢复**纠缠**。具体地，如果我们引入一个参考系统 $R$（与码空间纠缠），纠正擦除意味着从子系统 $\bar{A} = BC$ 恢复与 $R$ 的全部纠缠。

由量子信息理论，如果可以从 $\bar{A}$ 恢复态，则 $A$ 和 $R$ 之间没有量子关联：

$$I(A; R) = 0 \quad \text{（量子互信息）}$$

对于纯态 $|\Psi\rangle_{RABC}$，这等价于 $S(A) = S(AB)$（$S$ 是 von Neumann 熵），或 $S(\bar{A}) = S(\bar{A} \cup R) = S(A)$。

但这变得过于信息论化了。让我用更直接的方法。

#### Step 5（替代）: Direct dimensional argument

**核心论证**：码距 $d$ 的码可以纠正任意 $d-1$ 个量子比特的擦除。

将 $n$ 个量子比特分成 $A$（$d-1$ 个）和 $\bar{A}$（$n-d+1$ 个）。

码可以从 $\bar{A}$ 完全恢复，意味着存在恢复操作 $\mathcal{R}_{\bar{A}}$ 使得对任意码字 $\rho$：

$$\mathcal{R}_{\bar{A}}(\rho_{\bar{A}}) = \rho$$

这要求码空间的维度不超过 $\bar{A}$ 的 Hilbert 空间维度。但实际上约束更强：

考虑码空间的纯化（purification）。在码空间中取一个最大纠缠态 $|\Phi\rangle_{R \mathcal{C}}$（$R$ 是参考系统，维度 $2^k$）：

$$|\Phi\rangle = \frac{1}{\sqrt{2^k}} \sum_{i=0}^{2^k-1} |i\rangle_R |\psi_i\rangle_{\mathcal{C}}$$

纠正 $A$ 的擦除等价于从 $\bar{A}$ 恢复 $|\Phi\rangle_{R \mathcal{C}}$。由量子数据处理不等式和纯态的 Schmidt 分解：

$$S(R) \leq S(\bar{A}) \leq \log_2(\dim \mathcal{H}_{\bar{A}}) = n - d + 1$$

其中 $S(R) = k$（因为 $|\Phi\rangle$ 是最大纠缠态）。所以 $k \leq n - d + 1$。

但同样地，我们也可以擦除 $B$（另一组 $d-1$ 个量子比特），从 $\bar{B}$（$n-d+1$ 个量子比特）恢复。而 $\bar{B}$ 的补集 $B$ 与 $A$ 不重叠（因为 $|A| + |B| = 2(d-1) \leq n$）。

**关键步骤**：由于可以分别从 $\bar{A}$ 和 $\bar{B}$ 恢复，且 $\bar{A}$ 和 $\bar{B}$ 共享子系统 $C$（$|C| = n - 2(d-1)$ 个量子比特），量子互信息的约束给出：

对于纯态 $|\Phi\rangle_{RABC}$：

$$S(R\bar{A}) + S(R\bar{B}) \geq S(R) + S(\bar{A} \cap \bar{B}) = S(R) + S(\bar{A}\bar{B})$$

这是 strong subadditivity。但让我用更直接的方法。

**直接方法（following Knill-Laflamme 原始论证）**：

由于 $\rho_A$ 对所有码字相同（Step 3），$A$ 携带的逻辑信息为零。类似地，$\rho_B$ 对所有码字相同，$B$ 携带的逻辑信息为零。

编码在 $n$ 个量子比特中的 $k$ 个逻辑量子比特的全部信息必须可以从子系统 $C$（$n - 2(d-1)$ 个量子比特）中恢复。因此：

$$k \leq |C| = n - 2(d-1) = n - 2d + 2$$

即：

$$\boxed{k \leq n - 2(d-1) \quad \Longleftrightarrow \quad d \leq \frac{n-k}{2} + 1}$$ **[Preskill Ch.7, §7.8.3, p.34, Eq. 7.112; Nielsen & Chuang, Theorem 10.2, p.444]**

这就是 **Quantum Singleton Bound**。

#### Step 6: 严格性的注释

上面的"$B$ 也不携带信息所以 $k \leq |C|$"这一步需要更仔细的论证。严格来说：

由于 $\rho_A$ 不依赖于码字，存在从 $\bar{A} = BC$ 到码空间的量子恢复映射。类似地，由于 $\rho_B$ 不依赖于码字，存在从 $\bar{B} = AC$ 到码空间的量子恢复映射。

现在用 quantum no-cloning theorem 的推论：如果同一个量子信息可以分别从两个系统 $\bar{A}$ 和 $\bar{B}$ 恢复，那么信息必须在它们的交集 $\bar{A} \cap \bar{B} = C$ 中。

更精确的论证使用**complementary channel**的性质：如果从 $\bar{A}$ 可以恢复，则 $A$ 到 $R$ 的 complementary channel 的输出是"垃圾"（与输入无关）。类似地对 $B$。因此编码信息完全在 $C$ 中，$k \leq |C|$。

### Quantum Singleton Bound 的例子

| 码 | $n$ | $k$ | $d$ | $d_{\max} = (n-k)/2 + 1$ | 达到界限？ |
|----|-----|-----|-----|--------------------------|----------|
| Steane | 7 | 1 | 3 | 4 | 否 |
| $[[5, 1, 3]]$ | 5 | 1 | 3 | 3 | 是 (MDS) |
| Surface $d=3$ | 17 | 1 | 3 | 9 | 否（远未达到） |
| $[[4, 2, 2]]$ | 4 | 2 | 2 | 2 | 是 (MDS) |

$[[5, 1, 3]]$ 码是最小的能纠正单量子比特错误的完美码，也是 quantum MDS 码。

---

### From Gottesman Thesis: Classical Bounds Applied to Quantum Codes

> **[Gottesman thesis, §1.3]**: The classical **Hamming bound** on $[n, k, 2t+1]$ codes: $\sum_{j=0}^{t} \binom{n}{j} 2^k \leq 2^n$. Asymptotically: $k/n \leq 1 - H(t/n)$ where $H(x) = -x\log_2 x - (1-x)\log_2(1-x)$ is the Hamming entropy.

> **[Gottesman thesis, §1.3]**: The classical **Gilbert-Varshamov bound**: an $[n, k, 2t+1]$ linear code exists whenever $\sum_{j=0}^{2t} \binom{n}{j} 2^k < 2^n$. Asymptotically: $k/n \geq 1 - H(2t/n)$.

> **[Gottesman thesis, §1.3]**: The **capacity** of the binary symmetric channel (error probability $p$) is $1 - H(p)$, coinciding with the Hamming bound for the expected number of errors $t = pn$. These classical results have quantum analogues discussed in Chapter 7.

---

## Part 2: Quantum Hamming Bound **[Preskill Ch.7, §7.8.1, pp.30-32, Eq. 7.100; Nielsen & Chuang, Eq. 10.57, p.444; Gottesman, §1.3; Bacon, p.11-12]**

### 定理陈述

对于一个**非退化** $[[n, k, d]]$ 量子码，能纠正 $t = \lfloor(d-1)/2\rfloor$ 个错误：

$$\sum_{j=0}^{t} \binom{n}{j} 3^j \leq 2^{n-k}$$ **[Preskill Ch.7, Eq. 7.100]**

等价地：

$$2^k \sum_{j=0}^{t} \binom{n}{j} 3^j \leq 2^n$$

达到此界限的码称为 **quantum perfect code**。

### 推导

#### Step 1: Counting correctable errors

一个能纠正 $t$ 个错误的非退化码必须能区分所有权重 $\leq t$ 的错误。

权重为 $j$ 的 Pauli 错误数：

- 选择哪 $j$ 个量子比特出错：$\binom{n}{j}$ 种选择
- 每个出错的量子比特有 3 种非平凡 Pauli 算子（$X, Y, Z$）：$3^j$ 种选择

所以权重恰好为 $j$ 的 Pauli 错误数为 $\binom{n}{j} \cdot 3^j$。

权重 $\leq t$ 的所有 Pauli 错误数（包括恒等 $I$，权重0）：

$$N_t = \sum_{j=0}^{t} \binom{n}{j} 3^j$$

（其中 $j = 0$ 项为 $\binom{n}{0} 3^0 = 1$，对应没有错误。）

#### Step 2: Syndrome subspaces must be distinct

对于非退化码，不同的可纠正错误产生不同的 syndrome。

**非退化（non-degenerate）**意味着：对于任意两个权重 $\leq t$ 的 Pauli 错误 $E_a \neq E_b$，如果 $E_a^\dagger E_b \notin \mathcal{S}$（它们在逻辑上不等价），则它们有不同的 syndrome $\mathbf{s}(E_a) \neq \mathbf{s}(E_b)$。

更强地，非退化意味着：权重 $\leq 2t$ 的非平凡 Pauli 算子都不在稳定子群 $\mathcal{S}$ 中（除了恒等）。因此，$E_a^\dagger E_b$（权重 $\leq 2t$）如果不是恒等，就不在 $\mathcal{S}$ 中，必须有不同的效果。

#### Step 3: Orthogonal subspace argument

由 Knill-Laflamme 条件，对于非退化码：

$$P E_a^\dagger E_b P = c_a \delta_{ab} P$$

（$C_{ab}$ 是对角矩阵。）

这意味着每个错误 $E_a$ 将码空间 $\mathcal{C}$（维度 $2^k$）映射到一个 $2^k$ 维子空间 $\mathcal{C}_a = E_a \mathcal{C}$，且不同错误的子空间相互正交：

$$\mathcal{C}_a \perp \mathcal{C}_b \quad \text{when } a \neq b$$

**证明**：对于码空间中任意 $|\psi\rangle, |\phi\rangle$：

$$\langle\psi| E_a^\dagger E_b |\phi\rangle = \langle\psi| P E_a^\dagger E_b P |\phi\rangle = c_a \delta_{ab} \langle\psi|\phi\rangle$$

当 $a \neq b$ 时，$\langle\psi| E_a^\dagger E_b |\phi\rangle = 0$，即 $E_a|\psi\rangle \perp E_b|\phi\rangle$。

#### Step 4: Dimension counting

这 $N_t$ 个正交子空间 $\mathcal{C}_a$（每个维度 $2^k$）都是 $n$ 量子比特 Hilbert 空间 $\mathcal{H} = (\mathbb{C}^2)^{\otimes n}$（维度 $2^n$）的子空间。由于它们相互正交，它们的维度之和不能超过总维度：

$$N_t \cdot 2^k \leq 2^n$$

$$\sum_{j=0}^{t} \binom{n}{j} 3^j \cdot 2^k \leq 2^n$$

$$\boxed{\sum_{j=0}^{t} \binom{n}{j} 3^j \leq 2^{n-k}}$$ **[Preskill Ch.7, §7.8.1, Eq. 7.100; Nielsen & Chuang, Eq. 10.57, p.444]**

这就是 **Quantum Hamming Bound**。

#### Step 5: 与经典 Hamming Bound 的对比

经典 $[n, k, d]$ 码的 Hamming bound（sphere-packing bound）：

$$\sum_{j=0}^{t} \binom{n}{j} \leq 2^{n-k}$$

量子版本多了 $3^j$ 因子，因为每个位置有 3 种非平凡 Pauli 错误（经典只有 1 种 bit-flip 错误）。

#### Step 6: Degeneracy 和违反

**退化码可以违反 Quantum Hamming Bound** **[Preskill Ch.7, §7.8.1, p.31; Steane, p.13]**。

退化（degenerate）意味着存在两个不同的低权重错误 $E_a \neq E_b$ 使得 $E_a^\dagger E_b \in \mathcal{S}$——它们在码空间上有相同的效果，不需要被区分。

例如，表面码是高度退化的：码距为 $d$ 的 $d \times d$ 表面码有 $n \approx d^2$ 个物理量子比特，$k = 1$，但：

$$\sum_{j=0}^{t} \binom{d^2}{j} 3^j \gg 2^{d^2 - 1}$$

对于大 $d$，这远超 Hamming bound 允许的范围。表面码之所以可行，正是因为它的高度简并性——大量不同的错误模式在码空间上有相同的效果。

### Quantum Hamming Bound 的例子

**$[[5, 1, 3]]$ 码**：$n=5, k=1, t=1$

$$\sum_{j=0}^{1} \binom{5}{j} 3^j = 1 + 5 \cdot 3 = 16 = 2^4 = 2^{5-1}$$

等号成立！所以 $[[5, 1, 3]]$ 是 quantum perfect code。

**Steane 码 $[[7, 1, 3]]$**：$n=7, k=1, t=1$

$$\sum_{j=0}^{1} \binom{7}{j} 3^j = 1 + 7 \cdot 3 = 22 \leq 64 = 2^{7-1} = 2^6$$

满足但不紧。Steane 码不是 perfect code。

---

## Part 3: Other Bounds（简要提及）

### Quantum Gilbert-Varshamov Bound（下界） **[Gottesman, §1.3; Steane, p.16; Preskill Ch.7, §7.8.4, p.34]**

存在 $[[n, k, d]]$ 量子码只要：

$$\sum_{j=0}^{d-2} \binom{n}{j} 3^j < 2^{n-k}$$

这是一个存在性界限（非构造性），说明"好码"存在。

### Quantum Plotkin Bound

对于 $d > n/3$ 的 $[[n, k, d]]$ 码：

$$2^k \leq \frac{2d}{3d - n}$$

### Linear Programming Bound

通过 Shor-Laflamme 量子 weight enumerator 和线性规划，可以得到更紧的界限，但不像 Singleton 和 Hamming 有简单的闭式表达。

---

## Summary

| 界限 | 公式 | 适用范围 | 类型 |
|------|------|---------|------|
| Quantum Singleton | $d \leq (n-k)/2 + 1$ | 所有量子码 | 上界 |
| Quantum Hamming | $\sum_{j=0}^t \binom{n}{j} 3^j \leq 2^{n-k}$ | 非退化码 | 上界 |
| Quantum GV | $\sum_{j=0}^{d-2} \binom{n}{j} 3^j < 2^{n-k}$ | 存在性 | 下界 |

---

## Bounds for Geometrical and LDPC Codes (from Breuckmann & Eberhardt)

### BPT Bound (Bravyi-Poulin-Terhal) **[Breuckmann & Eberhardt, §3.5]**

For any $[[n,k,d]]$ stabilizer code on a $D$-dimensional Euclidean lattice:

$$k d^\alpha \leq O(n), \qquad \alpha = \frac{2}{D-1}$$

Special cases:
- $D = 2$: $k d^2 \leq O(n)$ (surface codes with $k = O(1)$ and $d = O(\sqrt{n})$ saturate this)
- $D = 3$: $k d \leq O(n)$
- $D = 4$: $k d^{2/3} \leq O(n)$

**Note**: This bound does **not** extend to non-Euclidean lattices. Hyperbolic surface codes in 2D violate $kd^2 \leq O(n)$ **[Breuckmann & Eberhardt, §3.5]**.

### Surface Code Distance Bound **[Breuckmann & Eberhardt, §3.5]**

Any code from a tessellation of a surface (closed or with boundary) satisfies $d^2 \leq O(n)$ (Fetaya). Extended: $kd^2 \leq O(\log^2(k) \cdot n)$ (Delfosse).

### Best Known LDPC Code Parameters **[Breuckmann & Eberhardt, Table I]**

| Code Family | $k$ | $d$ |
|------------|-----|-----|
| 2D hyperbolic | $\Theta(n)$ | $\Theta(\log n)$ |
| 4D hyperbolic (Guth-Lubotzky) | $\Theta(n)$ | $\Omega(n^{1/10})$ |
| Freedman-Meyer-Luo | $2$ | $\Omega(\sqrt[4]{\log n} \cdot \sqrt{n})$ |
| Hypergraph product (good classical) | $\Theta(n)$ | $\Theta(\sqrt{n})$ |
| Fibre bundle codes | $\Theta(n^{3/5}/\text{polylog})$ | $\Omega(n^{3/5}/\text{polylog})$ |
| Lifted product codes | $\Theta(n^\alpha \log n)$ | $\Omega(n^{1-\alpha}/\log n)$ |
| Balanced product codes | $\Theta(n^{4/5})$ | $\Omega(n^{3/5})$ |

### Hyperbolic Surface Code Encoding Rate **[Breuckmann & Eberhardt, §3.1.1]**

For regular tessellations of hyperbolic surfaces with $r$-gons, $s$ meeting at each vertex:

$$k = \left(1 - \frac{2}{r} - \frac{2}{s}\right) n + 2$$

This follows from the Gauss-Bonnet-Chern theorem. Check weights: $r$ for $Z$-checks, $s$ for $X$-checks, so there is a trade-off between check weight and encoding rate **[Breuckmann & Eberhardt, §3.1.1]**.

### Open Problem: Good Quantum LDPC Codes **[Breuckmann & Eberhardt]**

Whether $k \in \Theta(n)$ and $d \in \Theta(n)$ simultaneously is achievable for quantum LDPC codes remains a major open problem. Random sparse parity check matrices do not work (the CSS commutativity constraint $H_Z H_X^T = 0$ is not satisfied). Recent product constructions have surpassed the $\text{polylog}(n)\sqrt{n}$ distance barrier **[Breuckmann & Eberhardt, §4]**.

### Systolic Geometry Connection **[Breuckmann & Eberhardt, §3]**

The code distance is related to the $i$-systole $\text{sys}_i(M)$, the size of the smallest non-contractible $i$-dimensional submanifold. Improving bounds on quantum LDPC codes relates to deep questions in systolic geometry **[Breuckmann & Eberhardt, §3.5]**.

---

## References

- Knill, E. & Laflamme, R. "Theory of quantum error-correcting codes." PRA 55, 900 (1997).
- Rains, E. M. "Nonbinary quantum codes." IEEE Trans. Inf. Theory 45, 1827 (1999).
- Calderbank, A. R. et al. "Quantum error correction via codes over GF(4)." IEEE Trans. Inf. Theory 44, 1369 (1998).
- Gottesman, D. "Stabilizer Codes and Quantum Error Correction." PhD thesis, Caltech (1997).
- Breuckmann, N. P. & Eberhardt, J. N. "Quantum LDPC Codes." PRX Quantum 2, 040101 (2021).
- Bravyi, S., Poulin, D. & Terhal, B. "Tradeoffs for reliable quantum information storage in 2D systems." PRL 104, 050503 (2010).
- Fetaya, E. "Bounding the distance of quantum surface codes." JMP 53, 062202 (2012).
- Delfosse, N. "Tradeoffs for reliable quantum information storage in surface codes and color codes." IEEE ISIT (2013).
- **[Preskill, Ch.7]** Preskill, J. *Lecture Notes for Ph219/CS219*, Ch.7: "Quantum Error Correction". Quantum Hamming bound (§7.8.1, pp.30-32), no-cloning bound (§7.8.2, pp.31-32), quantum Singleton bound (§7.8.3, pp.32-34, Eq. 7.103). PDF: `references/preskill_ch7.pdf`
- **[Bacon intro, §2.3--2.4]** Bacon, D. -- quantum Singleton bound, quantum Hamming bound. PDF: `references/bacon_intro_qec.pdf`

---

## Preskill: Theorems and Formal Results (Chapter 7)

### Quantum Hamming Bound **[Preskill, Ch.7, §7.8.1, pp.30-32]**
For nondegenerate $[[n,k,2t+1]]$ codes, the number of correctable errors $N(t) = \sum_{j=0}^t 3^j\binom{n}{j}$ must fit in the available space (Eq. 7.100):
$$\sum_{j=0}^t 3^j\binom{n}{j} \leq 2^{n-k}$$
The factor $3^j$ accounts for three types of single-qubit Pauli errors ($X$, $Y$, $Z$). For $k=1$, $t=1$: $1 + 3n \leq 2^{n-1}$ (Eq. 7.101), giving $n \geq 5$. The $[[5,1,3]]$ code is **perfect** (saturates with equality: $1 + 15 = 16$).

Note: this bound applies only to nondegenerate codes. No degenerate codes violating it have been found [Preskill, Ch.7, p.31].

### No-Cloning Bound **[Preskill, Ch.7, §7.8.2, pp.31-32]**
An $[[n,k\geq 1,d]]$ code requires (Eq. 7.102):
$$n > 2(d-1)$$
**Proof** [Preskill, Ch.7, pp.31-32]: A $[[4,1,3]]$ code would allow splitting the 4-qubit block into two 2-qubit sub-blocks. Appending $|00\rangle$ to each gives two blocks with 2 located errors each. Since $d=3$ corrects 2 located errors, recovery would produce two copies of the encoded qubit -- violating no-cloning. Hence $n \geq 5$ for $[[n,1,3]]$.

### Quantum Singleton Bound **[Preskill, Ch.7, §7.8.3, pp.32-34]**
$$n - k \geq 2(d-1) \qquad \text{(Eq. 7.103)}$$
**Proof** [Preskill, Ch.7, pp.32-34]: Construct $|\Psi\rangle_{AQ} = \frac{1}{\sqrt{2^k}}\sum_x|x\rangle_A|\bar{x}\rangle_Q$ (Eq. 7.105), maximally entangling $k$-qubit ancilla with codewords. Entropy $S(A) = k$ (Eq. 7.106). Divide code block $Q$ into $Q^{(1)}_{d-1}$, $Q^{(2)}_{d-1}$, $Q^{(3)}_{n-2(d-1)}$. Since $d-1$ located errors are correctable, $AQ^{(1)}$ is uncorrelated: $S(AQ^{(1)}) = S(A) + S(Q^{(1)})$ (Eq. 7.107). Combined with subadditivity $S(Q^{(1)}Q^{(3)}) \leq S(Q^{(1)}) + S(Q^{(3)})$ (Eq. 7.109), one derives $k \leq S(Q^{(3)}) \leq n - 2(d-1)$ (Eq. 7.112).

### Rains' Improvement **[Preskill, Ch.7, §7.8.3, p.33]**
For $[[n,k\geq 1,2t+1]]$ codes, Rains showed (Eq. 7.113): $t \leq \lfloor(n+1)/6\rfloor$. Minimal block sizes for $k=1$ codes correcting $t = 1,2,3,4,5$ errors: $n = 5, 11, 17, 23, 29$.
