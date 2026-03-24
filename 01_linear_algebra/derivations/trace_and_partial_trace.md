# Trace and Partial Trace (迹与偏迹)

## Metadata
- **Topic**: Linear Algebra
- **Tags**: `trace`, `partial-trace`, `reduced-density-matrix`
- **Prerequisites**: tensor products, density matrices, linear maps
- **Related Formulas**: F1.4, F1.7
- **References**: Nielsen & Chuang Section 2.4.3; Preskill Lecture Notes Chapter 3; **[Watrous, Ch.1, §1.1.2]**; **[Slofstra, Ch.9, §9.4]**

---

## Statement (定理陈述)

**Trace (迹)**: 方阵 $A \in \mathbb{C}^{n \times n}$ 的迹定义为对角元素之和：

$$\mathrm{Tr}(A) = \sum_{i=1}^{n} A_{ii} = \sum_{i=1}^{n} \langle i|A|i\rangle$$

迹是基无关的（即不依赖于所选正交归一基的选择）。

**Partial Trace (偏迹)** **[Watrous, Ch.2, §2.1.3]** **[Slofstra, Ch.9, §9.4]**: 设 $\rho_{AB}$ 是复合系统 $\mathcal{H}_A \otimes \mathcal{H}_B$ 上的算符。偏迹 $\mathrm{Tr}_B: \mathcal{L}(\mathcal{H}_A \otimes \mathcal{H}_B) \to \mathcal{L}(\mathcal{H}_A)$ 定义为满足以下条件的唯一线性映射：

$$\mathrm{Tr}_B(X \otimes Y) = X \cdot \mathrm{Tr}(Y)$$

约化密度矩阵 $\rho_A = \mathrm{Tr}_B(\rho_{AB})$ 完整描述了子系统 $A$ 上所有局域可观测量的统计。

---

## Derivation (完整推导)

### Part I: Trace (迹)

#### Step 1: 迹的定义与基无关性

**定义**: 对于正交归一基 $\{|i\rangle\}_{i=1}^n$：

$$\mathrm{Tr}(A) = \sum_{i=1}^{n} \langle i|A|i\rangle$$

**基无关性证明**: 设 $\{|j'\rangle\}$ 是另一组正交归一基，$|j'\rangle = \sum_i U_{ij}|i\rangle$（$U$ 为酉矩阵）。

$$\sum_{j} \langle j'|A|j'\rangle = \sum_{j} \sum_{k,l} U_{kj}^* U_{lj} \langle k|A|l\rangle$$

$$= \sum_{k,l} \left(\sum_j U_{kj}^* U_{lj}\right) \langle k|A|l\rangle = \sum_{k,l} (U^\dagger U)_{kl} \langle k|A|l\rangle$$

$$= \sum_{k,l} \delta_{kl} \langle k|A|l\rangle = \sum_k \langle k|A|k\rangle = \mathrm{Tr}(A) \quad \square$$

#### Step 2: 迹的基本性质

**性质 1 (线性性)**:

$$\mathrm{Tr}(\alpha A + \beta B) = \alpha\,\mathrm{Tr}(A) + \beta\,\mathrm{Tr}(B)$$

*证明*:

$$\mathrm{Tr}(\alpha A + \beta B) = \sum_i \langle i|(\alpha A + \beta B)|i\rangle = \alpha\sum_i\langle i|A|i\rangle + \beta\sum_i\langle i|B|i\rangle = \alpha\,\mathrm{Tr}(A) + \beta\,\mathrm{Tr}(B) \quad \square$$

**性质 2 (循环性)**:

$$\mathrm{Tr}(AB) = \mathrm{Tr}(BA)$$

*证明*:

$$\mathrm{Tr}(AB) = \sum_i \langle i|AB|i\rangle = \sum_i \sum_j \langle i|A|j\rangle\langle j|B|i\rangle$$

$$= \sum_j \sum_i \langle j|B|i\rangle\langle i|A|j\rangle = \sum_j \langle j|BA|j\rangle = \mathrm{Tr}(BA) \quad \square$$

**推广**: 对多个矩阵，$\mathrm{Tr}(ABC) = \mathrm{Tr}(BCA) = \mathrm{Tr}(CAB)$。

注意：一般 $\mathrm{Tr}(ABC) \neq \mathrm{Tr}(ACB)$！循环性只允许循环置换，不允许任意排列。

**性质 3 (外积的迹)**:

$$\mathrm{Tr}(|a\rangle\langle b|) = \langle b|a\rangle$$

*证明*:

$$\mathrm{Tr}(|a\rangle\langle b|) = \sum_i \langle i|a\rangle\langle b|i\rangle = \langle b|\left(\sum_i |i\rangle\langle i|\right)|a\rangle = \langle b|a\rangle \quad \square$$

**性质 4 (正性)**: 若 $A \geq 0$（半正定），则 $\mathrm{Tr}(A) \geq 0$。

*证明*: $\mathrm{Tr}(A) = \sum_i \lambda_i$，其中 $\lambda_i \geq 0$ 为 $A$ 的特征值。$\square$

更一般地：若 $A \geq 0$ 且 $B \geq 0$，则 $\mathrm{Tr}(AB) \geq 0$。

*证明*: $\mathrm{Tr}(AB) = \mathrm{Tr}(\sqrt{B}A\sqrt{B}) = \mathrm{Tr}(\sqrt{B}\sqrt{A}\sqrt{A}\sqrt{B}) = \mathrm{Tr}(C^\dagger C) \geq 0$，其中 $C = \sqrt{A}\sqrt{B}$。$\square$

**性质 5 (张量积的迹)**:

$$\mathrm{Tr}(A \otimes B) = \mathrm{Tr}(A) \cdot \mathrm{Tr}(B)$$

*证明*: 取 $\mathcal{H}_A$ 的基 $\{|i\rangle\}$ 和 $\mathcal{H}_B$ 的基 $\{|j\rangle\}$：

$$\mathrm{Tr}(A \otimes B) = \sum_{i,j} \langle i,j|(A \otimes B)|i,j\rangle = \sum_{i,j} \langle i|A|i\rangle \langle j|B|j\rangle$$

$$= \left(\sum_i \langle i|A|i\rangle\right)\left(\sum_j \langle j|B|j\rangle\right) = \mathrm{Tr}(A) \cdot \mathrm{Tr}(B) \quad \square$$

**性质 6 (酉不变性)**:

$$\mathrm{Tr}(UAU^\dagger) = \mathrm{Tr}(A)$$

*证明*: 由循环性，$\mathrm{Tr}(UAU^\dagger) = \mathrm{Tr}(U^\dagger UA) = \mathrm{Tr}(A)$。$\square$

#### Step 3: 迹在量子力学中的角色

**期望值**: 可观测量 $O$ 在态 $\rho$ 中的期望值：

$$\langle O \rangle = \mathrm{Tr}(\rho O)$$

*推导 (纯态)*: 对纯态 $\rho = |\psi\rangle\langle\psi|$：

$$\mathrm{Tr}(|\psi\rangle\langle\psi| O) = \sum_i \langle i|\psi\rangle\langle\psi|O|i\rangle = \langle\psi|O|\psi\rangle \quad \checkmark$$

*推导 (混合态)*: 对 $\rho = \sum_k p_k|\psi_k\rangle\langle\psi_k|$：

$$\mathrm{Tr}(\rho O) = \sum_k p_k \mathrm{Tr}(|\psi_k\rangle\langle\psi_k|O) = \sum_k p_k \langle\psi_k|O|\psi_k\rangle$$

这是经典概率 $p_k$ 对量子期望值的加权平均。$\checkmark$

**Born 规则 (测量概率)**: 测量结果 $m$ 对应投影 $P_m$，概率为：

$$p(m) = \mathrm{Tr}(P_m \rho)$$

**态的归一化**: $\mathrm{Tr}(\rho) = 1$

**纯度**: $\mathrm{Tr}(\rho^2) \leq 1$，等号当且仅当 $\rho$ 是纯态。

*证明*: 设 $\rho = \sum_i p_i |i\rangle\langle i|$，$p_i \geq 0$，$\sum p_i = 1$。

$$\mathrm{Tr}(\rho^2) = \sum_i p_i^2 \leq \left(\sum_i p_i\right)^2 = 1$$

等号成立当且仅当只有一个 $p_i = 1$，其余为 0（纯态）。$\square$

#### Step 4: Hilbert-Schmidt 内积

**定义**: 算符空间 $\mathcal{L}(\mathcal{H})$ 上的内积：

$$\langle A, B \rangle_{\mathrm{HS}} = \mathrm{Tr}(A^\dagger B)$$

*验证内积公理*:

1. 线性性: $\langle A, \alpha B + \beta C \rangle = \alpha\langle A, B\rangle + \beta\langle A, C\rangle$ $\checkmark$（迹的线性性）
2. 共轭对称: $\langle A, B\rangle^* = \mathrm{Tr}(A^\dagger B)^* = \mathrm{Tr}(B^\dagger A) = \langle B, A\rangle$ $\checkmark$
3. 正定性: $\langle A, A\rangle = \mathrm{Tr}(A^\dagger A) = \sum_{ij}|A_{ij}|^2 \geq 0$，等于 0 当且仅当 $A = 0$ $\checkmark$

Hilbert-Schmidt 范数：$\|A\|_{\mathrm{HS}} = \sqrt{\mathrm{Tr}(A^\dagger A)} = \|A\|_F$（即 Frobenius 范数）。

---

### Part II: Partial Trace (偏迹)

#### Step 5: 偏迹的动机与定义

**物理动机**: 考虑复合系统 $AB$ 处于态 $\rho_{AB}$。若只对子系统 $A$ 进行测量，需要一个仅关于 $A$ 的有效描述。

**要求**: 找到 $\rho_A$ 使得对任意只作用在 $A$ 上的可观测量 $O_A$：

$$\mathrm{Tr}_{AB}(\rho_{AB} (O_A \otimes I_B)) = \mathrm{Tr}_A(\rho_A \cdot O_A)$$

这等价于定义偏迹 $\rho_A = \mathrm{Tr}_B(\rho_{AB})$。

**正式定义**: $\mathrm{Tr}_B: \mathcal{L}(\mathcal{H}_A \otimes \mathcal{H}_B) \to \mathcal{L}(\mathcal{H}_A)$ 是满足以下条件的线性映射：

$$\mathrm{Tr}_B(X_A \otimes Y_B) = X_A \cdot \mathrm{Tr}(Y_B)$$

然后通过线性扩展到一般算符。

#### Step 6: 偏迹的显式计算

选取 $\mathcal{H}_B$ 的正交归一基 $\{|b_k\rangle\}_{k=1}^{d_B}$，偏迹可以写为：

$$\mathrm{Tr}_B(M) = \sum_{k=1}^{d_B} (I_A \otimes \langle b_k|) \, M \, (I_A \otimes |b_k\rangle)$$

**等价性证明**: 对 $M = X_A \otimes Y_B$：

$$\sum_k (I_A \otimes \langle b_k|)(X_A \otimes Y_B)(I_A \otimes |b_k\rangle)$$

$$= \sum_k X_A \otimes (\langle b_k|Y_B|b_k\rangle) = X_A \cdot \sum_k \langle b_k|Y_B|b_k\rangle = X_A \cdot \mathrm{Tr}(Y_B) \quad \checkmark \quad \square$$

**分量形式**: 设 $\{|a_i\rangle\}$ 是 $\mathcal{H}_A$ 的基，$\{|b_j\rangle\}$ 是 $\mathcal{H}_B$ 的基。

一般算符 $M = \sum_{i,j,k,l} M_{ij,kl} |a_i\rangle\langle a_j| \otimes |b_k\rangle\langle b_l|$。

$$(\mathrm{Tr}_B(M))_{ij} = \sum_k M_{ij,kk}$$

即偏迹就是对 $B$ 的指标求对角和。

#### Step 7: 偏迹的基本性质

**性质 1 (线性性)**: $\mathrm{Tr}_B(\alpha M + \beta N) = \alpha\,\mathrm{Tr}_B(M) + \beta\,\mathrm{Tr}_B(N)$

**性质 2 (保正性)**: 若 $M \geq 0$，则 $\mathrm{Tr}_B(M) \geq 0$。

*证明*: 对任意 $|a\rangle \in \mathcal{H}_A$：

$$\langle a|\mathrm{Tr}_B(M)|a\rangle = \sum_k \langle a| (I \otimes \langle b_k|) M (I \otimes |b_k\rangle) |a\rangle = \sum_k \langle a, b_k|M|a, b_k\rangle \geq 0$$

最后一步用到 $M \geq 0$。$\square$

**性质 3 (保迹性)**:

$$\mathrm{Tr}_A(\mathrm{Tr}_B(M)) = \mathrm{Tr}_{AB}(M)$$

*证明*:

$$\mathrm{Tr}_A(\mathrm{Tr}_B(M)) = \sum_i \langle a_i|\mathrm{Tr}_B(M)|a_i\rangle = \sum_i \sum_k \langle a_i, b_k|M|a_i, b_k\rangle = \mathrm{Tr}_{AB}(M) \quad \square$$

**性质 4 (与局域算符的交换)**:

$$\mathrm{Tr}_B\big[(A_1 \otimes I_B) \, M \, (A_2 \otimes I_B)\big] = A_1 \, \mathrm{Tr}_B(M) \, A_2$$

*证明*:

$$\sum_k (I \otimes \langle b_k|)(A_1 \otimes I)(M)(A_2 \otimes I)(I \otimes |b_k\rangle)$$

$$= \sum_k (A_1 \otimes \langle b_k|) M (A_2 \otimes |b_k\rangle) = A_1 \left[\sum_k (I \otimes \langle b_k|)M(I \otimes |b_k\rangle)\right] A_2$$

$$= A_1 \,\mathrm{Tr}_B(M)\, A_2 \quad \square$$

这个性质在推导量子信道的 Kraus 表示时非常有用。

#### Step 8: 具体例子——两量子比特系统

考虑两量子比特系统，$\mathcal{H}_A = \mathcal{H}_B = \mathbb{C}^2$，基为 $\{|0\rangle, |1\rangle\}$。

**例 1: 可分态**

$$|\Psi\rangle = |0\rangle \otimes |+\rangle = |0\rangle \otimes \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$

$$\rho_{AB} = |0\rangle\langle 0| \otimes |+\rangle\langle+| = |0\rangle\langle 0| \otimes \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$$

$$\rho_A = \mathrm{Tr}_B(\rho_{AB}) = |0\rangle\langle 0| \cdot \mathrm{Tr}(|+\rangle\langle+|) = |0\rangle\langle 0| \cdot 1 = |0\rangle\langle 0|$$

结果是纯态，说明 $A$ 与 $B$ 没有纠缠。

**例 2: Bell 态 (最大纠缠态)**

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

$$\rho_{AB} = |\Phi^+\rangle\langle\Phi^+| = \frac{1}{2}(|00\rangle + |11\rangle)(\langle 00| + \langle 11|)$$

$$= \frac{1}{2}\big(|00\rangle\langle 00| + |00\rangle\langle 11| + |11\rangle\langle 00| + |11\rangle\langle 11|\big)$$

$$= \frac{1}{2}\big(|0\rangle\langle 0| \otimes |0\rangle\langle 0| + |0\rangle\langle 1| \otimes |0\rangle\langle 1| + |1\rangle\langle 0| \otimes |1\rangle\langle 0| + |1\rangle\langle 1| \otimes |1\rangle\langle 1|\big)$$

逐项取偏迹：

$$\mathrm{Tr}_B(|0\rangle\langle 0| \otimes |0\rangle\langle 0|) = |0\rangle\langle 0| \cdot \mathrm{Tr}(|0\rangle\langle 0|) = |0\rangle\langle 0| \cdot 1 = |0\rangle\langle 0|$$

$$\mathrm{Tr}_B(|0\rangle\langle 1| \otimes |0\rangle\langle 1|) = |0\rangle\langle 1| \cdot \mathrm{Tr}(|0\rangle\langle 1|) = |0\rangle\langle 1| \cdot \langle 1|0\rangle = 0$$

$$\mathrm{Tr}_B(|1\rangle\langle 0| \otimes |1\rangle\langle 0|) = |1\rangle\langle 0| \cdot \langle 0|1\rangle = 0$$

$$\mathrm{Tr}_B(|1\rangle\langle 1| \otimes |1\rangle\langle 1|) = |1\rangle\langle 1| \cdot 1 = |1\rangle\langle 1|$$

因此：

$$\rho_A = \frac{1}{2}(|0\rangle\langle 0| + |1\rangle\langle 1|) = \frac{I}{2}$$

约化密度矩阵是**最大混合态**，纯度 $\mathrm{Tr}(\rho_A^2) = 1/2$。这是最大纠缠态的特征标志。

**例 3: 一般两量子比特态**

$$|\Psi\rangle = \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle$$

密度矩阵 $\rho_{AB} = |\Psi\rangle\langle\Psi|$ 是 $4 \times 4$ 矩阵，写成分块形式（以 $A$ 的基为块索引）：

$$\rho_{AB} = \begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix}_A$$

其中 $\rho_{ij}$ 是 $2 \times 2$ 矩阵：$(\rho_{ij})_{kl} = \langle ik|\rho_{AB}|jl\rangle$。

偏迹（对 $B$）就是取分块矩阵的"对角块之和"：

$$\rho_A = \mathrm{Tr}_B(\rho_{AB}) = \sum_k \rho_{kk} = \begin{pmatrix} |\alpha|^2 + |\beta|^2 & \alpha\gamma^* + \beta\delta^* \\ \gamma\alpha^* + \delta\beta^* & |\gamma|^2 + |\delta|^2 \end{pmatrix}$$

#### Step 9: 偏迹作为量子操作

偏迹可以理解为一个量子操作 (quantum operation)。具体来说：

$$\mathrm{Tr}_B(\rho_{AB}) = \sum_k (I_A \otimes \langle b_k|)\, \rho_{AB}\, (I_A \otimes |b_k\rangle)$$

这正是 Kraus 表示的形式，Kraus 算符为 $K_k = I_A \otimes \langle b_k|$。

验证 CPTP 条件：

$$\sum_k K_k^\dagger K_k = \sum_k (I_A \otimes |b_k\rangle)(I_A \otimes \langle b_k|) = I_A \otimes \left(\sum_k |b_k\rangle\langle b_k|\right) = I_A \otimes I_B = I_{AB}$$

因此偏迹是 trace-preserving 的 $\checkmark$。

#### Step 10: 偏迹与纠缠熵

**von Neumann 熵**: $S(\rho) = -\mathrm{Tr}(\rho \ln \rho) = -\sum_i \lambda_i \ln \lambda_i$

对于纯态 $|\Psi\rangle_{AB}$ 的约化密度矩阵 $\rho_A = \mathrm{Tr}_B(|\Psi\rangle\langle\Psi|)$：

**纠缠熵 (Entanglement Entropy)**:

$$E(|\Psi\rangle) = S(\rho_A) = -\sum_i \lambda_i^2 \ln(\lambda_i^2) = -2\sum_i \lambda_i^2 \ln\lambda_i$$

其中 $\{\lambda_i\}$ 是 Schmidt 系数。

- 可分态: $E = 0$（$\rho_A$ 是纯态，只有一个非零 Schmidt 系数）
- 最大纠缠态: $E = \ln d$（$\rho_A = I/d$，Schmidt 系数均为 $1/\sqrt{d}$）

纠缠熵是纯态纠缠度量的基本量。

---

## From Linear Algebra References

### Strong Subadditivity **[Slofstra, §7; LinAlg for QC, §6]**

**von Neumann 熵的强次加性**：对三体系统 $ABC$：

$$S(ABC) + S(B) \leq S(AB) + S(BC)$$

等价形式：条件互信息非负 $I(A:C|B) \geq 0$。

这是量子信息理论中最基本的不等式之一，由 Lieb & Ruskai (1973) 证明。

### Trace Inequalities for QEC **[LinAlg for QC, §6]**

**Klein's inequality**: 若 $f$ 是凸函数，$A, B$ Hermitian，则：

$$\text{Tr}[f(A) - f(B) - (A-B)f'(B)] \geq 0$$

取 $f(x) = x\ln x$ 得到 **quantum relative entropy** 的非负性：

$$D(\rho \| \sigma) = \text{Tr}(\rho \ln \rho - \rho \ln \sigma) \geq 0$$

等号当且仅当 $\rho = \sigma$。

**Fannes-Audenaert inequality**: 若 $\|\rho - \sigma\|_1 \leq \epsilon$，则：

$$|S(\rho) - S(\sigma)| \leq \epsilon \log(d-1) + H_2(\epsilon)$$

其中 $H_2(\epsilon) = -\epsilon\ln\epsilon - (1-\epsilon)\ln(1-\epsilon)$ 是二元熵。

### Inner Product on Operators (from Watrous Ch.1) **[Watrous, Ch.1, §1.1.2]**

> Watrous 原文 (p.10): "The operator $A^* \in L(\mathcal{Y}, \mathcal{X})$ is the uniquely determined operator that satisfies $\langle v, Au \rangle = \langle A^*v, u \rangle$ for all $u \in \mathcal{X}$ and $v \in \mathcal{Y}$."

Watrous 使用的算符内积 $\langle A, B \rangle = \text{Tr}(A^* B)$ 与 Hilbert-Schmidt 内积一致。关键恒等式：

- 向量与算符的关系：$u^* v = \langle u, v \rangle$ 对所有 $v \in \mathcal{X}$
- 秩-1 算符：$(vu^*)w = \langle u, w \rangle v$
- 秩关系：$\text{rank}(A) = \text{rank}(AA^*) = \text{rank}(A^*A)$
- 维度公式：$\dim(\ker(A)) + \dim(\text{im}(A)) = \dim(\mathcal{X})$

### Kernel and Image via Adjoint **[Watrous, Ch.1, Eq.1.53]**

> Watrous 原文 (p.11): "$\ker(A) = \ker(A^*A)$ and $\text{im}(A) = \text{im}(AA^*)$."

### Pauli Basis Expansion **[LinAlg for QC, §3]**

$n$ 量子比特密度矩阵可以在 Pauli 基中展开（Pauli Transfer Matrix 表示）：

$$\rho = \frac{1}{2^n}\sum_{P \in \{I,X,Y,Z\}^{\otimes n}} \text{Tr}(P\rho) \cdot P$$

其中 $\text{Tr}(P\rho) = \langle P \rangle$ 是 Pauli 可观测量的期望值。

**量子信道的 Pauli Transfer Matrix (PTM)**：

$$R_{PQ} = \frac{1}{2^n}\text{Tr}(P \cdot \mathcal{E}(Q))$$

信道 $\mathcal{E}$ 在 Pauli 基下表示为 $4^n \times 4^n$ 实矩阵 $R$，密度矩阵的 Pauli 展开系数通过 $\vec{r}' = R\vec{r}$ 变换。

---

## Summary (总结)

### 迹

| 性质 | 公式 |
|------|------|
| 线性性 | $\mathrm{Tr}(\alpha A + \beta B) = \alpha\mathrm{Tr}(A) + \beta\mathrm{Tr}(B)$ |
| 循环性 | $\mathrm{Tr}(ABC) = \mathrm{Tr}(CAB) = \mathrm{Tr}(BCA)$ |
| 外积 | $\mathrm{Tr}(\|a\rangle\langle b\|) = \langle b\|a\rangle$ |
| 张量积 | $\mathrm{Tr}(A \otimes B) = \mathrm{Tr}(A)\mathrm{Tr}(B)$ |
| 正性 | $A \geq 0 \Rightarrow \mathrm{Tr}(A) \geq 0$ |
| 酉不变 | $\mathrm{Tr}(UAU^\dagger) = \mathrm{Tr}(A)$ |

### 偏迹

| 要点 | 说明 |
|------|------|
| 定义 | $\mathrm{Tr}_B(X \otimes Y) = X \cdot \mathrm{Tr}(Y)$ |
| 显式计算 | $\mathrm{Tr}_B(M) = \sum_k (I \otimes \langle b_k\|)M(I \otimes \|b_k\rangle)$ |
| 物理意义 | 给出子系统的约化密度矩阵 $\rho_A = \mathrm{Tr}_B(\rho_{AB})$ |
| 保正性 | $M \geq 0 \Rightarrow \mathrm{Tr}_B(M) \geq 0$ |
| 纠缠诊断 | $\rho_A$ 的纯度反映纠缠强度 |
| 量子操作 | 偏迹本身是一个 CPTP 映射 |
