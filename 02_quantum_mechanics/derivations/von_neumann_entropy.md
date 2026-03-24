# Von Neumann Entropy and Related Quantities (冯·诺依曼熵及相关量)

> **Tags**: `entropy`, `von-neumann`, `mutual-information`, `subadditivity`

## Statement

对于密度矩阵 $\rho$，von Neumann 熵定义为：

$$S(\rho) = -\text{Tr}(\rho \log \rho)$$
**[N&C, Eq.(11.51), p.510]** **[Preskill, Ch.2, &sect;2.5.1, p.21]**

它是经典 Shannon 熵的量子推广，是量子信息论中最核心的量。

## Prerequisites

- **密度矩阵**: 谱分解 $\rho = \sum_i \lambda_i|e_i\rangle\langle e_i|$（参见 [density_matrix_formalism.md](density_matrix_formalism.md)）
- **特征值分解**: Hermitian 矩阵对角化
- **经典 Shannon 熵**: $H(X) = -\sum_i p_i \log p_i$（对概率分布）

---

## Derivation

### Step 1: 经典 Shannon 熵回顾

对离散随机变量 $X$，取值为 $x_1, \ldots, x_n$，概率分布为 $p(x_i)$，Shannon 熵定义为：

$$H(X) = -\sum_{i=1}^n p(x_i) \log p(x_i)$$

约定 $0 \log 0 = 0$（取极限 $\lim_{x\to 0^+} x\log x = 0$）。

**性质**：
- $H(X) \geq 0$
- $H(X) = 0$ 当且仅当某个 $p(x_i) = 1$（确定性）
- $H(X) \leq \log n$，等号当且仅当均匀分布 $p(x_i) = 1/n$
- 对数底通常取 2（单位: bit）或 $e$（单位: nat）

### Step 2: Von Neumann 熵的定义

对密度矩阵 $\rho$，设其谱分解为：

$$\rho = \sum_{i=1}^d \lambda_i |e_i\rangle\langle e_i|, \qquad \lambda_i \geq 0, \quad \sum_i \lambda_i = 1$$

定义矩阵函数 $\rho \log \rho$：

$$\rho \log \rho = \sum_{i=1}^d \lambda_i \log \lambda_i \, |e_i\rangle\langle e_i|$$

（对每个特征值应用函数 $f(x) = x\log x$，约定 $0\log 0 = 0$。）

Von Neumann 熵为：

$$S(\rho) = -\text{Tr}(\rho \log \rho) = -\sum_{i=1}^d \lambda_i \log \lambda_i$$

**关键观察**：von Neumann 熵就是 $\rho$ 的特征值分布的 Shannon 熵。

$$\boxed{S(\rho) = H(\{\lambda_i\})}$$
**[N&C, Eq.(11.51), p.510]** **[Preskill, Ch.2, &sect;2.5.1, p.21]**

### Step 3: 性质 1 —— 非负性

**定理** **[N&C, Theorem 11.8(1), p.513]** **[Preskill, Ch.2, &sect;2.5.1, p.22]**: $S(\rho) \geq 0$。

**证明**：由于 $\lambda_i \in [0,1]$，所以 $\log \lambda_i \leq 0$，因此 $-\lambda_i \log \lambda_i \geq 0$。

$$S(\rho) = \sum_i (-\lambda_i \log \lambda_i) \geq 0 \qquad \square$$

### Step 4: 性质 2 —— 纯态的熵为零

**定理** **[N&C, Theorem 11.8(1), p.513]**: $S(\rho) = 0$ 当且仅当 $\rho$ 是纯态。

**证明**：纯态的特征值为 $(1, 0, 0, \ldots, 0)$。

$$S = -(1\cdot\log 1 + 0\cdot\log 0 + \cdots) = -(0 + 0 + \cdots) = 0$$

反过来，$S = 0$ 要求 $-\lambda_i\log\lambda_i = 0$ 对所有 $i$，即每个 $\lambda_i$ 要么是 0 要么是 1。结合 $\sum_i \lambda_i = 1$，只能有恰好一个 $\lambda_i = 1$，其余为 0，即纯态。$\square$

**物理意义**：纯态是完全已知的量子态，没有不确定性，所以熵为零。

### Step 5: 性质 3 —— 最大值

**定理** **[N&C, Theorem 11.8(2), p.513]** **[Preskill, Ch.2, &sect;2.5.1, p.22]**: $S(\rho) \leq \log d$，其中 $d$ 是 Hilbert 空间维数。等号当且仅当 $\rho = I/d$（最大混合态）。

**证明**：这是 Shannon 熵最大值的直接推论——$d$ 个概率值 $\{\lambda_i\}$ 的 Shannon 熵在均匀分布时取最大值 $\log d$。

也可以用 Lagrange 乘子法：最大化 $-\sum_i \lambda_i\log\lambda_i$，约束 $\sum_i \lambda_i = 1$。

$$\frac{\partial}{\partial \lambda_j}\left[-\sum_i \lambda_i\log\lambda_i - \mu\left(\sum_i\lambda_i - 1\right)\right] = 0$$

$$-\log\lambda_j - 1 - \mu = 0 \implies \lambda_j = e^{-1-\mu}$$

所有 $\lambda_j$ 相等，结合 $\sum_j \lambda_j = 1$，得 $\lambda_j = 1/d$。$\square$

**物理意义**：最大混合态代表"完全不知道系统处于什么态"，不确定性最大。

### Step 6: 性质 4 —— 幺正不变性

**定理** **[N&C, Theorem 11.8, p.513]** **[Preskill, Ch.2, &sect;2.5.1, p.22]**: $S(U\rho U^\dagger) = S(\rho)$。

**证明**：$U\rho U^\dagger$ 与 $\rho$ 有相同的特征值（幺正变换保持特征值），所以 Shannon 熵相同。$\square$

### Step 7: 性质 5 —— 凹性（Concavity）

**定理** **[N&C, p.517]** **[Preskill, Ch.2, &sect;2.5.1, pp.22-23]**: 对概率分布 $\{p_i\}$ 和密度矩阵 $\{\rho_i\}$：

$$S\left(\sum_i p_i \rho_i\right) \geq \sum_i p_i S(\rho_i)$$

**含义**：混合操作增加熵。"混合几个态"比"分别看它们的平均熵"要更不确定。

**证明思路**：利用联合熵 $S(\rho_{XQ})$，其中 $X$ 是标记哪个态的经典变量，$Q$ 是量子系统。

定义：

$$\rho_{XQ} = \sum_i p_i |i\rangle\langle i|_X \otimes \rho_i$$

则 $S(\rho_{XQ}) = H(\{p_i\}) + \sum_i p_i S(\rho_i)$（因为态是分块对角的）。

而 $\rho_Q = \text{Tr}_X(\rho_{XQ}) = \sum_i p_i \rho_i$。

由 subadditivity $S(\rho_{XQ}) \leq S(\rho_X) + S(\rho_Q)$（后面证明），得：

$$H(\{p_i\}) + \sum_i p_i S(\rho_i) \leq H(\{p_i\}) + S\left(\sum_i p_i\rho_i\right)$$

消去 $H(\{p_i\})$ 即得凹性。$\square$

### Step 8: 性质 6 —— Subadditivity（次可加性）

**定理** **[N&C, pp.515-516]** **[Preskill, Ch.2, &sect;2.5.1, pp.22-23]**: 对复合系统 $AB$：

$$S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$$

等号当且仅当 $\rho_{AB} = \rho_A \otimes \rho_B$（无关联）。

**含义**：联合系统的不确定性不超过各子系统不确定性之和。关联的存在减少了联合不确定性。

**证明**：利用量子相对熵 $S(\rho \| \sigma) = \text{Tr}(\rho\log\rho - \rho\log\sigma) \geq 0$（Klein 不等式 **[N&C, Theorem 11.7, p.511]** **[Preskill, Ch.2, &sect;2.5.1, pp.22-23]**）。

取 $\rho = \rho_{AB}$，$\sigma = \rho_A \otimes \rho_B$：

$$S(\rho_{AB} \| \rho_A \otimes \rho_B) = \text{Tr}(\rho_{AB}\log\rho_{AB}) - \text{Tr}(\rho_{AB}\log(\rho_A\otimes\rho_B)) \geq 0$$

其中：

$$\text{Tr}(\rho_{AB}\log(\rho_A\otimes\rho_B)) = \text{Tr}(\rho_{AB}(\log\rho_A \otimes I + I \otimes \log\rho_B))$$

$$= \text{Tr}(\rho_A\log\rho_A) + \text{Tr}(\rho_B\log\rho_B)$$

（用了 $\text{Tr}_B(\rho_{AB}) = \rho_A$ 等。）

代入：

$$-S(\rho_{AB}) - (-S(\rho_A) - S(\rho_B)) \geq 0$$

$$S(\rho_A) + S(\rho_B) - S(\rho_{AB}) \geq 0 \qquad \square$$

### Step 9: 性质 7 —— Strong Subadditivity（强次可加性）

**定理（Lieb & Ruskai, 1973）** **[N&C, Theorem 11.14, p.521]** **[Preskill, Ch.2, &sect;2.5.1, p.23]**: 对三体系统 $ABC$：

$$S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})$$

等价形式：

$$S(A|BC) \leq S(A|B)$$

其中条件熵 $S(A|B) = S(\rho_{AB}) - S(\rho_B)$。

**含义**：给定更多信息（$C$），条件不确定性不会增加。这是量子信息论中最深刻的不等式之一。

**注意**：证明相当技术性（Lieb & Ruskai 的原始证明用了算子凸性），此处不给出完整证明。

### Step 10: Quantum Conditional Entropy（量子条件熵） **[N&C, Eq.(11.60), p.514]** **[Preskill, Ch.2, &sect;2.5.1, pp.23-24]**

定义：

$$S(A|B) = S(\rho_{AB}) - S(\rho_B)$$

**与经典情况的重大区别**：量子条件熵可以为负！

**例子**：对 Bell 态 $|\Phi^+\rangle_{AB}$：

$$S(\rho_{AB}) = 0 \quad \text{（纯态）}$$

$$S(\rho_B) = \log 2 \quad \text{（最大混合态 $I/2$）}$$

$$S(A|B) = 0 - \log 2 = -\log 2 < 0$$

**物理意义**：负条件熵意味着 $B$ 不仅知道关于 $A$ 的所有信息，还拥有"超过所需"的信息——这是纠缠的标志。负条件熵的绝对值等于可以蒸馏出的纠缠比特数。

### Step 11: Quantum Mutual Information（量子互信息） **[N&C, Eq.(11.63-11.65), p.514]** **[Preskill, Ch.2, &sect;2.5.1, pp.22-23]**

定义：

$$I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$$

也可以写成：

$$I(A:B) = S(A) - S(A|B) = S(B) - S(B|A)$$

或者用相对熵：

$$I(A:B) = S(\rho_{AB} \| \rho_A \otimes \rho_B)$$

**性质**：

- $I(A:B) \geq 0$（由 subadditivity 直接得出）
- $I(A:B) = 0$ 当且仅当 $\rho_{AB} = \rho_A \otimes \rho_B$（无关联）
- $I(A:B) \leq 2\min\{S(\rho_A), S(\rho_B)\}$（与经典互信息不同，量子互信息可以大于任一边缘熵）

**例子**：Bell 态 $|\Phi^+\rangle$：

$$I(A:B) = \log 2 + \log 2 - 0 = 2\log 2$$

这超过了 $S(\rho_A) = \log 2$！经典互信息满足 $I \leq H(A)$，但量子互信息可以达到 $2S(A)$。超出经典界限的部分正是量子关联（纠缠）的贡献。

### Step 12: Quantum Relative Entropy（量子相对熵） **[N&C, Eq.(11.52), p.511]** **[Preskill, Ch.2, &sect;2.5.1, pp.22-23]**

定义：

$$S(\rho \| \sigma) = \text{Tr}(\rho \log \rho - \rho \log \sigma)$$

当 $\text{ker}(\sigma) \cap \text{supp}(\rho) \neq \emptyset$ 时定义为 $+\infty$（即 $\rho$ 的支撑不包含在 $\sigma$ 的支撑中时发散）。

**Klein 不等式** **[N&C, Theorem 11.7, p.511]** **[Preskill, Ch.2, &sect;2.5.1, pp.22-23]**: $S(\rho \| \sigma) \geq 0$，等号当且仅当 $\rho = \sigma$。

**证明**：设 $\rho = \sum_i p_i|e_i\rangle\langle e_i|$，$\sigma = \sum_j q_j|f_j\rangle\langle f_j|$。

$$S(\rho \| \sigma) = \sum_i p_i\log p_i - \sum_i \langle e_i|\rho\log\sigma|e_i\rangle$$

$$= \sum_i p_i\log p_i - \sum_{i,j} p_i |\langle e_i|f_j\rangle|^2 \log q_j$$

定义转移矩阵 $T_{ij} = |\langle e_i|f_j\rangle|^2$（双随机矩阵的一般化），则 $\sum_j T_{ij} = 1$。

$$S(\rho \| \sigma) = \sum_i p_i \log p_i - \sum_i p_i \sum_j T_{ij}\log q_j$$

利用 $\log$ 的凹性（Jensen 不等式），$\sum_j T_{ij}\log q_j \leq \log(\sum_j T_{ij} q_j)$：

$$S(\rho\|\sigma) \geq \sum_i p_i\log p_i - \sum_i p_i \log\left(\sum_j T_{ij}q_j\right)$$

$$= \sum_i p_i \log\frac{p_i}{\sum_j T_{ij}q_j}$$

定义 $r_i = \sum_j T_{ij}q_j$，注意 $\sum_i r_i = \sum_j q_j \sum_i T_{ij} = \sum_j q_j \cdot 1 = 1$。

由 Gibbs 不等式 $\sum_i p_i \log(p_i/r_i) \geq 0$（经典相对熵非负），得：

$$S(\rho \| \sigma) \geq 0 \qquad \square$$

**数据处理不等式** **[N&C, Theorem 11.17, p.524]** **[Preskill, Ch.2, &sect;2.5.1, p.23]**：对任何 CPTP 映射 $\mathcal{E}$：

$$S(\mathcal{E}(\rho) \| \mathcal{E}(\sigma)) \leq S(\rho \| \sigma)$$

量子操作不会增加相对熵——信息只会损失，不会凭空产生。

### Step 13: 各种熵之间的关系图

以下关系联系了各种量子信息量：

$$I(A:B) = S(\rho_{AB} \| \rho_A \otimes \rho_B) = S(A) + S(B) - S(AB)$$

$$S(A|B) = S(AB) - S(B) = -S(\rho_{AB} \| I_A \otimes \rho_B) + \log d_A$$

**重要不等式汇总**：

| 不等式 | 公式 | 条件 |
|--------|------|------|
| 非负性 | $S(\rho) \geq 0$ | 总成立 |
| 最大值 | $S(\rho) \leq \log d$ | 等号: $\rho = I/d$ |
| Araki-Lieb **[N&C, p.516]** **[Preskill, Ch.2, p.23]** | $S(AB) \geq \|S(A) - S(B)\|$ | 总成立 |
| Subadditivity | $S(AB) \leq S(A) + S(B)$ | 等号: $\rho_{AB} = \rho_A \otimes \rho_B$ |
| Strong subadditivity | $S(ABC) + S(B) \leq S(AB) + S(BC)$ | 总成立 |
| 互信息非负 | $I(A:B) \geq 0$ | 等号: 无关联 |

---

## Summary

| 量 | 定义 | 范围 |
|----|------|------|
| Von Neumann 熵 | $S(\rho) = -\text{Tr}(\rho\log\rho)$ | $[0, \log d]$ |
| 条件熵 | $S(A\|B) = S(AB) - S(B)$ | $[-\log d_A, \log d_A]$ |
| 互信息 | $I(A:B) = S(A)+S(B)-S(AB)$ | $[0, 2\log\min(d_A,d_B)]$ |
| 相对熵 | $S(\rho\\\|\sigma) = \text{Tr}(\rho\log\rho - \rho\log\sigma)$ | $[0, +\infty]$ |

---

## Nielsen & Chuang: Theorems and Formal Results

### Chapter 11 Overview **[Nielsen & Chuang, Ch. 11, pp.500-558]**
Chapter 11 "Entropy and information" is the primary reference for quantum entropy theory. Key sections: 11.1 (Shannon entropy), 11.2 (Basic properties of entropy), 11.3 (Von Neumann entropy).

### Definition (Von Neumann Entropy) **[Nielsen & Chuang, Eq. 11.51, p.510]**
$$S(\rho) \equiv -\text{Tr}(\rho \log \rho)$$
If $\rho$ has eigenvalues $\lambda_x$ then $S(\rho) = H(\lambda_x) = -\sum_x \lambda_x \log \lambda_x$.

### Definition (Quantum Relative Entropy) **[Nielsen & Chuang, Eq. 11.52, p.511]**
$$S(\rho \| \sigma) \equiv \text{Tr}(\rho \log \rho) - \text{Tr}(\rho \log \sigma)$$
Defined as $+\infty$ when $\text{supp}(\rho) \not\subseteq \text{supp}(\sigma)$.

### Theorem 11.1 (Non-negativity of Classical Relative Entropy) **[Nielsen & Chuang, Theorem 11.1, p.505]**
The classical relative entropy is non-negative: $H(p(x)\|q(x)) \geq 0$, with equality if and only if $p(x) = q(x)$ for all $x$.

**Proof** **[Nielsen & Chuang, p.505]**: Uses $-\log x \geq (1-x)/\ln 2$: $H(p\|q) = -\sum_x p(x)\log\frac{q(x)}{p(x)} \geq \frac{1}{\ln 2}\sum_x p(x)(1 - q(x)/p(x)) = \frac{1}{\ln 2}(1-1) = 0$.

### Theorem 11.2 (Maximum Shannon Entropy) **[Nielsen & Chuang, Theorem 11.2, p.505]**
Suppose $X$ is a random variable with $d$ outcomes. Then $H(X) \leq \log d$, with equality if and only if $X$ is uniformly distributed.

**Proof** **[Nielsen & Chuang, p.505]**: Setting $q(x) = 1/d$ in the relative entropy: $0 \leq H(p\|1/d) = \log d - H(X)$.

### Theorem 11.3 (Basic Properties of Shannon Entropy) **[Nielsen & Chuang, Theorem 11.3, p.506]**
1. $H(X,Y) = H(Y,X)$, $H(X:Y) = H(Y:X)$
2. $H(Y|X) \geq 0$, with equality iff $Y = f(X)$
3. $H(X) \leq H(X,Y)$, with equality iff $Y = f(X)$
4. Subadditivity: $H(X,Y) \leq H(X) + H(Y)$, equality iff $X,Y$ independent
5. $H(Y|X) \leq H(Y)$ and $H(X:Y) \geq 0$, equality iff independent
6. Strong subadditivity: $H(X,Y,Z) + H(Y) \leq H(X,Y) + H(Y,Z)$
7. Conditioning reduces entropy: $H(X|Y,Z) \leq H(X|Y)$

### Theorem 11.4 (Chaining Rule for Conditional Entropies) **[Nielsen & Chuang, Theorem 11.4, p.508]**
$H(X_1, \ldots, X_n|Y) = \sum_{i=1}^n H(X_i|Y, X_1, \ldots, X_{i-1})$.

### Theorem 11.5 (Data Processing Inequality) **[Nielsen & Chuang, Theorem 11.5, p.509]**
Suppose $X \to Y \to Z$ is a Markov chain. Then $H(X) \geq H(X:Y) \geq H(X:Z)$. The first inequality is saturated iff, given $Y$, $X$ can be reconstructed.

### Theorem 11.7 (Klein's Inequality) **[Nielsen & Chuang, Theorem 11.7, p.511]**
The quantum relative entropy is non-negative: $S(\rho \| \sigma) \geq 0$, with equality if and only if $\rho = \sigma$.

**Proof** **[Nielsen & Chuang, pp.511-513]**: Let $\rho = \sum_i p_i|i\rangle\langle i|$ and $\sigma = \sum_j q_j|j\rangle\langle j|$. Define $P_{ij} \equiv |\langle i|j\rangle|^2 \geq 0$ (doubly stochastic). Then $S(\rho\|\sigma) = \sum_i p_i(\log p_i - \sum_j P_{ij}\log q_j)$. By strict concavity of $\log$: $\sum_j P_{ij}\log q_j \leq \log(\sum_j P_{ij}q_j) = \log r_i$, giving $S(\rho\|\sigma) \geq \sum_i p_i \log(p_i/r_i) \geq 0$ by classical Gibbs inequality. Equality iff $P_{ij}$ is a permutation matrix and $p_i = r_i$, i.e., $\rho = \sigma$.

### Theorem 11.6 (Fannes' Inequality) **[Nielsen & Chuang, Theorem 11.6, p.512]**
Suppose $\rho$ and $\sigma$ are density matrices such that the trace distance satisfies $T(\rho, \sigma) \leq 1/e$. Then:
$$|S(\rho) - S(\sigma)| \leq T(\rho,\sigma)\log d + \eta(T(\rho,\sigma))$$
where $d$ is the dimension and $\eta(x) \equiv -x\log x$. Without the restriction: $|S(\rho) - S(\sigma)| \leq T(\rho,\sigma)\log d + 1/e$.

**Proof sketch** **[Nielsen & Chuang, pp.512-513]**: Let $r_i, s_i$ be eigenvalues of $\rho, \sigma$ in descending order. Show $T(\rho,\sigma) \geq \sum_i|r_i - s_i|$. Use calculus: $|r_i - s_i| \leq 1/2$ implies $|\eta(r_i) - \eta(s_i)| \leq \eta(|r_i - s_i|)$. Set $\Delta = \sum_i|r_i - s_i|$, apply Theorem 11.2 to get the bound.

### Theorem 11.8 (Basic Properties of Von Neumann Entropy) **[Nielsen & Chuang, Theorem 11.8, p.513]**
1. The entropy is non-negative. $S(\rho) = 0$ iff $\rho$ is pure.
2. In a $d$-dimensional space, $S(\rho) \leq \log d$, with equality iff $\rho = I/d$.
3. For a composite system $AB$ in a pure state: $S(A) = S(B)$ (follows from Schmidt decomposition).
4. Suppose $p_i$ are probabilities and $\rho_i$ have support on orthogonal subspaces. Then $S(\sum_i p_i\rho_i) = H(p_i) + \sum_i p_i S(\rho_i)$.
5. Joint entropy theorem: $S(\sum_i p_i|i\rangle\langle i| \otimes \rho_i) = H(p_i) + \sum_i p_i S(\rho_i)$.

**Proof of (2)** **[Nielsen & Chuang, p.513]**: $0 \leq S(\rho\|I/d) = -S(\rho) + \log d$.
**Proof of (3)** **[Nielsen & Chuang, p.513]**: From Schmidt decomposition, $\rho_A$ and $\rho_B$ have identical nonzero eigenvalues.
**Proof of (4)** **[Nielsen & Chuang, p.514]**: If $\rho_i$ have orthogonal supports with eigenpairs $\lambda_i^j, |e_i^j\rangle$, then $p_i\lambda_i^j$ and $|e_i^j\rangle$ are the eigenpairs of $\sum_i p_i\rho_i$, giving $S = -\sum_{ij}p_i\lambda_i^j\log(p_i\lambda_i^j) = H(p_i) + \sum_i p_i S(\rho_i)$.

### Theorem 11.9 (Projective Measurements Increase Entropy) **[Nielsen & Chuang, Theorem 11.9, p.515]**
Suppose $P_i$ is a complete set of orthogonal projectors and $\rho$ is a density operator. Then: $S(\rho') \geq S(\rho)$ where $\rho' \equiv \sum_i P_i\rho P_i$, with equality iff $\rho = \rho'$.

**Proof** **[Nielsen & Chuang, p.515]**: Apply Klein's inequality: $0 \leq S(\rho'\|\rho) = -S(\rho) - \text{Tr}(\rho\log\rho')$. Since $P_i$ commutes with $\rho'$ and thus with $\log\rho'$: $-\text{Tr}(\rho\log\rho') = -\text{Tr}(\sum_i P_i\rho P_i\log\rho') = -\text{Tr}(\rho'\log\rho') = S(\rho')$.

### Subadditivity **[Nielsen & Chuang, p.515-516]**
$$S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$$
with equality iff $\rho_{AB} = \rho_A \otimes \rho_B$.

**Proof** **[Nielsen & Chuang, p.515]**: By Klein's inequality with $\sigma = \rho_A \otimes \rho_B$:
$$0 \leq S(\rho_{AB} \| \rho_A \otimes \rho_B) = -S(\rho_{AB}) - \text{Tr}(\rho_{AB}\log(\rho_A \otimes \rho_B)) = -S(\rho_{AB}) + S(\rho_A) + S(\rho_B)$$

### Theorem 11.10 (Araki-Lieb Inequality / Triangle Inequality) **[Nielsen & Chuang, p.516]**
$$S(\rho_{AB}) \geq |S(\rho_A) - S(\rho_B)|$$
Combined with subadditivity: $|S(A) - S(B)| \leq S(A,B) \leq S(A) + S(B)$.

**Proof** **[Nielsen & Chuang, p.516]**: Introduce purifying system $R$. By subadditivity: $S(R) + S(A) \geq S(A,R)$. Since $ABR$ is pure: $S(A,R) = S(B)$ and $S(R) = S(A,B)$. Rearranging: $S(A,B) \geq S(B) - S(A)$. By symmetry in $A \leftrightarrow B$: $S(A,B) \geq |S(A) - S(B)|$.

### Concavity of Entropy **[Nielsen & Chuang, p.517]**
$$S\left(\sum_i p_i \rho_i\right) \geq \sum_i p_i S(\rho_i)$$

**Proof** **[Nielsen & Chuang, p.517]**: Introduce auxiliary system $B$ with orthonormal $|i\rangle$ states. Define $\rho_{AB} \equiv \sum_i p_i\rho_i \otimes |i\rangle\langle i|$. Then $S(A) = S(\sum_i p_i\rho_i)$, $S(B) = H(p_i)$, $S(A,B) = H(p_i) + \sum_i p_i S(\rho_i)$. By subadditivity: $S(A,B) \leq S(A) + S(B)$, which gives $\sum_i p_i S(\rho_i) \leq S(\sum_i p_i\rho_i)$.

### Theorem 11.10 (Upper Bound on Entropy of Mixture) **[Nielsen & Chuang, Theorem 11.10, p.518]**
$$S(\rho) \leq \sum_i p_i S(\rho_i) + H(p_i)$$
where $\rho = \sum_i p_i\rho_i$, with equality iff the states $\rho_i$ have support on orthogonal subspaces. Together with concavity: $\sum_i p_i S(\rho_i) \leq S(\sum_i p_i\rho_i) \leq \sum_i p_i S(\rho_i) + H(p_i)$.

### Theorem 11.11 (Lieb's Theorem) **[Nielsen & Chuang, Theorem 11.11, p.520]**
Let $X$ be a matrix, and $0 \leq t \leq 1$. Then the function $f(A,B) \equiv \text{Tr}(X^\dagger A^t X B^{1-t})$ is jointly concave in positive matrices $A$ and $B$.

### Theorem 11.12 (Convexity of the Relative Entropy) **[Nielsen & Chuang, Theorem 11.12, p.520]**
The relative entropy $S(\rho\|\sigma)$ is jointly convex in its arguments.

**Proof** **[Nielsen & Chuang, p.520]**: Follows from Lieb's theorem. Define $I_t(A,X) \equiv \text{Tr}(X^\dagger A^t X A^{1-t}) - \text{Tr}(X^\dagger X A)$, which is concave in $A$. Taking derivative at $t=0$ gives $I(A,X) = \text{Tr}(X^\dagger(\log A)XA) - \text{Tr}(X^\dagger X(\log A)A)$, also concave. Using block matrices $A = \text{diag}(\rho, \sigma)$, $X = [[0,0],[I,0]]$ gives $I(A,X) = -S(\rho\|\sigma)$.

### Corollary 11.13 (Concavity of Conditional Entropy) **[Nielsen & Chuang, Corollary 11.13, p.520]**
The conditional entropy $S(A|B)$ is concave in the state $\rho_{AB}$.

**Proof** **[Nielsen & Chuang, pp.520-521]**: $S(\rho_{AB}\|I/d \otimes \rho_B) = -S(A|B) + \log d$. Concavity of $S(A|B)$ follows from joint convexity of relative entropy.

### Theorem 11.14 (Strong Subadditivity) **[Nielsen & Chuang, Theorem 11.14, p.521]**
For any trio of quantum systems $A, B, C$:
$$S(A) + S(B) \leq S(A,C) + S(B,C) \qquad (11.107)$$
$$S(A,B,C) + S(B) \leq S(A,B) + S(B,C) \qquad (11.108)$$

**Proof** **[Nielsen & Chuang, pp.521-522]**: The two forms are equivalent. Define $T(\rho_{ABC}) \equiv S(A) + S(B) - S(A,C) - S(B,C) = -S(C|A) - S(C|B)$. By concavity of conditional entropy, $T$ is convex. Decompose $\rho_{ABC} = \sum_i p_i|i\rangle\langle i|$, so $T(\rho) \leq \sum_i p_i T(|i\rangle\langle i|) = 0$ (since for pure states $S(A,C) = S(B)$ and $S(B,C) = S(A)$). The second form follows by purifying $ABC$ with system $R$: $S(R) = S(A,B,C)$ and $S(R,C) = S(A,B)$.

### Theorem 11.15 (Consequences of Strong Subadditivity) **[Nielsen & Chuang, Theorem 11.15, p.522]**
1. Conditioning reduces entropy: $S(A|B,C) \leq S(A|B)$
2. Discarding quantum systems never increases mutual information: $S(A:B) \leq S(A:B,C)$
3. Quantum operations never increase mutual information: if $\mathcal{E}$ is trace-preserving on $B$, then $S(A':B') \leq S(A:B)$

### Theorem 11.16 (Subadditivity of Conditional Entropy) **[Nielsen & Chuang, Theorem 11.16, p.523]**
Joint subadditivity: $S(A,B|C,D) \leq S(A|C) + S(B|D)$.
First-entry subadditivity: $S(A,B|C) \leq S(A|C) + S(B|C)$.
Second-entry subadditivity: $S(A|B,C) \leq S(A|B) + S(A|C)$.

### Theorem 11.17 (Monotonicity of Relative Entropy) **[Nielsen & Chuang, Theorem 11.17, p.524]**
For any density operators $\rho_{AB}$ and $\sigma_{AB}$:
$$S(\rho_A\|\sigma_A) \leq S(\rho_{AB}\|\sigma_{AB})$$
Discarding a quantum system can only decrease the relative entropy.

### Quantum Conditional Entropy **[Nielsen & Chuang, Eq. 11.60-11.62, p.514]**
$$S(A|B) \equiv S(A,B) - S(B)$$
Unlike classical conditional entropy, quantum conditional entropy can be negative (e.g., $S(A|B) = -\log 2$ for a Bell state). Negative conditional entropy indicates entanglement.

### Quantum Mutual Information **[Nielsen & Chuang, Eq. 11.63-11.65, p.514]**
$$I(A:B) \equiv S(A) + S(B) - S(A,B) = S(\rho_{AB} \| \rho_A \otimes \rho_B)$$
By Klein's inequality, $I(A:B) \geq 0$, with equality iff $\rho_{AB} = \rho_A \otimes \rho_B$.

### Fannes' Inequality **[Nielsen & Chuang, Theorem 11.10, p.520]**
If $D(\rho, \sigma) \leq 1/e$ then:
$$|S(\rho) - S(\sigma)| \leq D(\rho,\sigma)\log(d-1) + \eta(D(\rho,\sigma))$$
where $\eta(x) = -x\log x$ and $d$ is the dimension. This provides continuity bounds for entropy.

---

## Preskill: Theorems and Formal Results (Chapter 2)

### Von Neumann Entropy Definition and Properties **[Preskill, Ch.2, §2.5.1, pp.21-23]**
Preskill introduces the von Neumann entropy in the context of ensemble ambiguity and convexity:

$$S(\rho) = -\text{Tr}(\rho\log\rho)$$

If $\rho = \sum_i \lambda_i|i\rangle\langle i|$ (spectral decomposition), then $S(\rho) = H(\{\lambda_i\}) = -\sum_i \lambda_i\log\lambda_i$.

**Basic properties** [Preskill, Ch.2, §2.5.1]:
1. $S(\rho) \geq 0$, with equality iff $\rho$ is pure
2. $S(\rho) \leq \log d$, with equality iff $\rho = I/d$
3. $S(U\rho U^\dagger) = S(\rho)$ (unitary invariance)
4. For bipartite pure state: $S(\rho_A) = S(\rho_B)$ (from Schmidt decomposition)

### Quantum Relative Entropy and Klein's Inequality **[Preskill, Ch.2, §2.5.1, pp.22-23]**
**Definition**: The quantum relative entropy is:
$$S(\rho\|\sigma) = \text{Tr}(\rho\log\rho) - \text{Tr}(\rho\log\sigma)$$

**Theorem (Klein's inequality)**: $S(\rho\|\sigma) \geq 0$ with equality iff $\rho = \sigma$.

**Proof sketch** [Preskill, Ch.2, §2.5.1]: Using the operator inequality $\log x \leq x - 1$ (with equality iff $x = 1$), applied in the spectral basis of $\rho$:
$$-S(\rho\|\sigma) = \text{Tr}(\rho\log\sigma) - \text{Tr}(\rho\log\rho) = \text{Tr}(\rho\log(\rho^{-1/2}\sigma\rho^{-1/2}))$$
$$\leq \text{Tr}(\rho(\rho^{-1/2}\sigma\rho^{-1/2} - I)) = \text{Tr}(\sigma) - \text{Tr}(\rho) = 0$$

### Subadditivity from Klein's Inequality **[Preskill, Ch.2, §2.5.1, pp.22-23]**
**Theorem**: $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$.

**Proof** [Preskill, Ch.2, §2.5.1]: Direct application of Klein's inequality with $\sigma = \rho_A \otimes \rho_B$:
$$0 \leq S(\rho_{AB}\|\rho_A \otimes \rho_B) = -S(\rho_{AB}) + S(\rho_A) + S(\rho_B)$$

The quantity $I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB}) = S(\rho_{AB}\|\rho_A \otimes \rho_B) \geq 0$ is the **quantum mutual information**.

### Concavity of Entropy **[Preskill, Ch.2, §2.5.1, pp.22-23]**
**Theorem**: $S(\sum_i p_i\rho_i) \geq \sum_i p_i S(\rho_i)$.

**Proof** [Preskill, Ch.2, §2.5.1]: Consider the classical-quantum state $\rho_{XQ} = \sum_i p_i|i\rangle\langle i|_X \otimes \rho_i^Q$. Then:
$$S(\rho_{XQ}) = H(\{p_i\}) + \sum_i p_i S(\rho_i)$$
By subadditivity: $S(\rho_{XQ}) \leq S(\rho_X) + S(\rho_Q) = H(\{p_i\}) + S(\sum_i p_i\rho_i)$.
Combining: $\sum_i p_i S(\rho_i) \leq S(\sum_i p_i\rho_i)$.

### Araki-Lieb Inequality **[Preskill, Ch.2, §2.5.1, p.23]**
**Theorem**: $S(\rho_{AB}) \geq |S(\rho_A) - S(\rho_B)|$.

**Proof** [Preskill, Ch.2, §2.5.1]: Introduce a purifying system $C$ such that $|\Psi\rangle_{ABC}$ is pure. Then $S(\rho_{AB}) = S(\rho_C)$ and $S(\rho_A) = S(\rho_{BC})$. By subadditivity on $BC$:
$$S(\rho_A) = S(\rho_{BC}) \leq S(\rho_B) + S(\rho_C) = S(\rho_B) + S(\rho_{AB})$$
Therefore $S(\rho_{AB}) \geq S(\rho_A) - S(\rho_B)$. By symmetry (swapping $A \leftrightarrow B$): $S(\rho_{AB}) \geq |S(\rho_A) - S(\rho_B)|$.

### Strong Subadditivity **[Preskill, Ch.2, §2.5.1, p.23]**
**Theorem (Lieb-Ruskai, 1973)**: For tripartite system $ABC$:
$$S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})$$

Equivalently, in terms of conditional entropy $S(A|B) = S(AB) - S(B)$:
$$S(A|BC) \leq S(A|B)$$

Preskill notes this is the most powerful entropy inequality in quantum information theory. It implies:
1. **Conditioning reduces entropy**: Having more information (system $C$) cannot increase uncertainty about $A$
2. **Data processing inequality for mutual information**: $I(A:BC) \geq I(A:B)$
3. **Monotonicity of relative entropy under partial trace**: $S(\rho_{AB}\|\sigma_{AB}) \geq S(\rho_A\|\sigma_A)$

### Quantum Conditional Entropy Can Be Negative **[Preskill, Ch.2, §2.5.1, pp.23-24]**
Preskill emphasizes that quantum conditional entropy $S(A|B) = S(AB) - S(B)$ can be negative, unlike its classical counterpart:

**Example**: For Bell state $|\Phi^+\rangle_{AB}$:
$$S(A|B) = S(AB) - S(B) = 0 - \log 2 = -\log 2$$

**Operational meaning**: $-S(A|B)$ quantifies the entanglement that can be distilled from the state (when $S(A|B) < 0$) or the quantum communication cost of state merging (when $S(A|B) > 0$).

### Entropy and Ensemble Distinguishability **[Preskill, Ch.2, §2.5.2, pp.23-25]**
**Holevo bound** (mentioned in context): For an ensemble $\{p_i, \rho_i\}$ with average state $\rho = \sum_i p_i\rho_i$, the accessible classical information from any measurement satisfies:
$$I_{\text{accessible}} \leq \chi = S(\rho) - \sum_i p_i S(\rho_i)$$
This quantity $\chi$ (Holevo information) is bounded by the entropy difference, connecting entropy to practical information extraction.

---

## References

- **[Nielsen & Chuang]** Nielsen, M. A. & Chuang, I. L. *Quantum Computation and Quantum Information* (Cambridge, 10th anniversary ed., 2010), Ch. 11 (pp.500-558)
- **[Preskill, Ch.2]** Preskill, J. *Lecture Notes for Ph219/CS219: Quantum Information and Computation*, Ch.2: "Foundations I: States and Ensembles" (July 2015), §2.5.1 (entropy, Klein's inequality, subadditivity, strong subadditivity, Araki-Lieb, conditional entropy, Holevo bound). PDF: `references/preskill_ch2.pdf`
- **[Wilde, Ch.11]** Wilde, M. *From Classical to Quantum Shannon Theory*, Ch.11 (Quantum Information and Entropy) — 对 von Neumann 熵的完整处理，包括量子熵作为最小测量熵的刻画 (Thm 11.1.1)、负条件熵的操作解释 (state merging)、相干信息定义等。详见 [03_quantum_info_theory/derivations/quantum_data_processing.md]
- Von Neumann, *Mathematische Grundlagen der Quantenmechanik* (1932)
- Lieb & Ruskai, *J. Math. Phys.* 14, 1938 (1973)
