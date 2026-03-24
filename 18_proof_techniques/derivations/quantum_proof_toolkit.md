# Quantum Proof Toolkit

> 量子信息论中特有的证明工具——经典工具不够用时的"量子升级版"。
> 这些定理在量子信息论文的 theory section 中频繁出现。
> 每个定理带完整陈述、证明思路、使用场景。

---

## 1. Decoupling Technique (解耦技术)

### 1.1 Intuition

> 一行解释：如果 Alice 对她的系统做随机酉操作，则 Bob 的系统与 Alice 的参考系统"解耦"——信息从 Alice 转移到了 Bob。

### 1.2 Formal Statement

**Theorem** [Dupuis, Hayden, Li, 2010; Szehr, Dupuis, Tomamichel, Renner, 2013]:

设 $\rho_{ABR}$ 是三方态，Alice 对 $A$ 系统施加随机酉 $U$（关于 Haar 测度均匀选取）。则：

$$\mathbb{E}_U\left[\left\|(U \otimes I_{BR}) \rho_{ABR} (U^\dagger \otimes I_{BR}) - \frac{I_A}{d_A} \otimes \rho_{BR}\right\|_1\right] \leq 2^{-\frac{1}{2}(H_{\min}(A|B)_\rho - \log d_A)} + \text{small corrections}$$

**One-shot version** (更精确):

$$\mathbb{E}_U\left[\left\|\mathrm{tr}_{A'}[\mathcal{U}_A \rho_{ABR}] - \frac{I_{A''}}{d_{A''}} \otimes \rho_{BR}\right\|_1\right] \leq 2^{-\frac{1}{2}H_{\min}^{\epsilon}(A|B)_\rho} \cdot \sqrt{d_{A''}} + \epsilon'$$

其中 $A$ 被分为 $A' A''$，$A'$ 发送给 Bob，$A''$ 保留。

### 1.3 Proof Sketch

**Step 1**: 用 Haar 积分公式（2-design 即可）计算 $\mathbb{E}_U[\cdot]$。

**Step 2**: 利用 operator Cauchy-Schwarz: $\|\rho\|_1 \leq \sqrt{d} \|\rho\|_2$。

**Step 3**: 计算 2-norm 的二阶矩 $\mathbb{E}_U[\|\cdot\|_2^2]$，这归结为 swap trick：

$$\mathbb{E}_U[U \otimes U^\dagger \cdot (\cdot) \cdot U^\dagger \otimes U] = \text{projection onto symmetric/antisymmetric subspace}$$

**Step 4**: 化简得到的表达式涉及 $\mathrm{tr}[\rho_A^2]$（即 $2^{-H_2(A)}$），用 smooth min-entropy bound。$\square$

### 1.4 When to Use

- **量子信道编码定理**: 证明随机码以高概率实现量子信道容量
- **量子态合并 (state merging)**: Alice 将她的量子态转移给 Bob
- **一次性信息论 (one-shot information theory)**: 有限块长（finite blocklength）编码界
- **Random circuit sampling**: 随机电路使局部约化密度矩阵接近最大混合态

**Cross-ref**: [../03_quantum_info_theory/derivations/]: 量子信道容量

---

## 2. Post-Selection Technique (后选择技术)

### 2.1 Statement

**Theorem** [Christandl, König, Renner, 2009]: 设 $\mathcal{E}$ 是一个量子信道（CPTP map），$\rho$ 是 $n$-copy 对称态（permutation invariant）。则：

$$\|\mathcal{E}(\rho) - \mathcal{E}(\sigma)\|_1 \leq (n+1)^{d^2-1} \cdot \|\mathcal{E}(\rho_{\text{de Finetti}}) - \mathcal{E}(\sigma_{\text{de Finetti}})\|_1$$

其中 $\rho_{\text{de Finetti}} = \int \tau^{\otimes n} d\mu(\tau)$ 是 de Finetti 态。

> 一行解释：对称态上的分析可以"后选择"到 i.i.d. 态上，代价是多项式的维度因子。

### 2.2 Key Application

**QKD security proofs**: 将一般攻击 (coherent attack) 归约到集体攻击 (collective attack)。

1. 协议设计保证密钥态是 permutation invariant 的
2. Post-selection technique: 分析集体攻击 → 加多项式因子 → 对一般攻击也成立
3. 避免了直接分析指数大 Hilbert 空间上的信道

**When to use**: 当你有 $n$ 份量子态的对称性，想把分析简化为单份态时。

---

## 3. Quantum Union Bound (量子联合界)

### 3.1 Sen's Quantum Union Bound

**Theorem** [Sen, 2012]: 设 $\Pi_1, \ldots, \Pi_m$ 是投影算子（事件），$\rho$ 是量子态。若 $\mathrm{tr}[\Pi_i \rho] \geq 1 - \epsilon_i$，则存在一个单一投影 $\Pi$ 使得：

$$\mathrm{tr}[\Pi \rho] \geq 1 - 2\sum_{i=1}^m \sqrt{\epsilon_i}$$

**Standard (non-quantum) union bound** [F18.20] 给出 $1 - \sum \epsilon_i$（更弱）。

### 3.2 Gao's Quantum Union Bound

**Theorem** [Gao, 2015]: 更紧的版本：

$$\mathrm{tr}\left[\left(\prod_{i=m}^1 \Pi_i\right) \rho \left(\prod_{i=1}^m \Pi_i\right)\right] \geq 1 - 4\sum_{i=1}^m \epsilon_i$$

> 一行解释：量子态上"多个好事件同时发生"的概率控制——因为投影不对易，需要量子版本的 union bound。

### 3.3 Proof Sketch (Sen's version)

**Key idea**: 使用 gentle measurement lemma (下面推导) 逐步应用投影。

**Step 1**: $\Pi_1$ 几乎不扰动 $\rho$（因为 $\mathrm{tr}[\Pi_1 \rho] \geq 1-\epsilon_1$）。

**Step 2**: 由 gentle measurement: $\|\Pi_1 \rho \Pi_1 / \mathrm{tr}[\Pi_1 \rho] - \rho\|_1 \leq 2\sqrt{\epsilon_1}$。

**Step 3**: 对 $\Pi_2$ 应用于扰动后的态，误差累积 $\leq 2\sqrt{\epsilon_1} + 2\sqrt{\epsilon_2}$。

**Step 4**: 归纳得 $\sum 2\sqrt{\epsilon_i}$。$\square$

### 3.4 When to Use

- **量子假设检验**: 需要同时满足多个量子约束
- **量子随机编码**: 证明随机码以高概率同时满足多个解码条件
- **QEC 分析**: 量子纠错码同时纠正多种错误类型
- **Measurement-based QC**: 多步自适应测量的成功概率

**Cross-ref**: [../03_quantum_info_theory/derivations/]: 量子假设检验；[concentration_inequalities.md] [F18.20]: 经典 union bound

---

## 4. Gentle Measurement Lemma (温和测量引理)

### 4.1 Statement

**Lemma** [Winter, 1999; Ogawa & Nagaoka, 2007]:

设 $\rho$ 是密度算子，$0 \leq M \leq I$ 是测量算子。若 $\mathrm{tr}[M\rho] \geq 1 - \epsilon$，则：

$$\left\|\sqrt{M}\, \rho\, \sqrt{M} - \rho\right\|_1 \leq 2\sqrt{\epsilon}$$

等价形式（对纯态 $|\psi\rangle$）：

$$\left\|\sqrt{M}|\psi\rangle - |\psi\rangle\right\| \leq \sqrt{2\epsilon}$$

> 一行解释：如果测量结果几乎确定（概率 $\geq 1-\epsilon$），则测量几乎不扰动量子态。

### 4.2 Proof

**For pure states**: 设 $|\psi\rangle$ 是纯态。

$$\left\|\sqrt{M}|\psi\rangle - |\psi\rangle\right\|^2 = \langle\psi|M|\psi\rangle - 2\langle\psi|\sqrt{M}|\psi\rangle + 1$$

因 $\sqrt{M} \leq I$（算子单调性 of $x \mapsto \sqrt{x}$）：
$$\langle\psi|\sqrt{M}|\psi\rangle \geq \langle\psi|M|\psi\rangle \geq 1-\epsilon$$

（第一个不等式用了 $\sqrt{M} \geq M$ for $0 \leq M \leq I$。）

因此：$\left\|\sqrt{M}|\psi\rangle - |\psi\rangle\right\|^2 \leq 1 - 2(1-\epsilon) + 1 = 2\epsilon$。

取平方根得 $\left\|\sqrt{M}|\psi\rangle - |\psi\rangle\right\| \leq \sqrt{2\epsilon}$。

**For mixed states**: 净化 $\rho = \mathrm{tr}_R[|\psi\rangle\langle\psi|_{AR}]$，对净化应用纯态版本，再 trace out R 得到 trace distance 界。$\square$

### 4.3 When to Use

- **量子纠错**: 证明纠错操作后的态接近原态
- **量子密钥分发**: 隐私放大 (privacy amplification) 中的扰动分析
- **量子 union bound 的证明**: 每步投影的扰动由此引理控制
- **Sequential measurements**: 多步测量的累积误差分析

**Cross-ref**: [../02_quantum_mechanics/derivations/measurement_theory.md]: POVM, measurement postulates

---

## 5. Operator Monotonicity and Operator Convexity (算子单调性和凸性)

### 5.1 Operator Monotone Functions

**Definition**: $f: [0, \infty) \to \mathbb{R}$ 是算子单调的，如果 $A \preceq B \Rightarrow f(A) \preceq f(B)$。

**Key examples**:
- $f(x) = x^r$ 对 $0 \leq r \leq 1$ 是算子单调的 (Löwner-Heinz inequality)
- $f(x) = \log x$ 是算子单调的
- $f(x) = x^r$ 对 $r > 1$ 不是算子单调的

### 5.2 Löwner-Heinz Inequality

**Theorem**: 若 $A \succeq B \succeq 0$，则对 $0 \leq r \leq 1$：

$$A^r \succeq B^r$$

**Proof sketch**: 用积分表示 $x^r = \frac{\sin(r\pi)}{\pi} \int_0^\infty \frac{x}{x+t} t^{r-1} dt$，再利用 $x \mapsto x/(x+t)$ 的算子单调性（这是 resolvent，可直接验证）。$\square$

### 5.3 Operator Convex Functions

**Definition**: $f$ 是算子凸的，如果 $f(\lambda A + (1-\lambda)B) \preceq \lambda f(A) + (1-\lambda) f(B)$。

**Key examples**:
- $f(x) = x^r$ 对 $1 \leq r \leq 2$ 是算子凸的
- $f(x) = -x^r$ 对 $0 \leq r \leq 1$ 是算子凸的 (即 $x^r$ 算子凹)
- $f(x) = x \log x$ 是算子凸的

### 5.4 Applications in Quantum Information

**Joint convexity of relative entropy**: $D(\rho\|\sigma) = \mathrm{tr}[\rho(\log\rho - \log\sigma)]$ 是 $(\rho, \sigma)$ 的联合凸函数。

*Proof uses*: $x \log x$ 的算子凸性 + Lieb's concavity theorem。

**Data processing inequality**: $D(\mathcal{E}(\rho)\|\mathcal{E}(\sigma)) \leq D(\rho\|\sigma)$。

*Proof uses*: 相对熵的联合凸性 + Stinespring 表示。

**When to use**: 证明量子熵不等式；分析量子信道的单调性；量子 Fisher 信息的性质。

**Cross-ref**: [../03_quantum_info_theory/derivations/entropy_inequalities.md]: 详细推导

---

## 6. Quantum de Finetti Theorem (量子 de Finetti 定理)

### 6.1 Statement

**Theorem** [Caves, Fuchs, Schack, 2002; Christandl, König, Mitchison, Renner, 2007]:

设 $\rho_{A_1 \cdots A_n}$ 是 $n$ 个 $d$ 维系统上的 permutation invariant 态。对任意 $k \leq n$，存在概率测度 $\mu$ on 密度矩阵使得：

$$\left\|\mathrm{tr}_{A_{k+1} \cdots A_n}[\rho] - \int \sigma^{\otimes k} d\mu(\sigma)\right\|_1 \leq \frac{2kd^2}{n}$$

> 一行解释：对称量子态的约化态近似 i.i.d.——"量子交换性蕴含近似独立性"。

### 6.2 Proof Idea

**Step 1**: 对称态可以分解在不可约表示上（Schur-Weyl duality）。

**Step 2**: 每个不可约表示对应一个"type"（频率向量）。

**Step 3**: 当 $k \ll n$ 时，对 $k$ 个系统的约化几乎不依赖具体是哪 $k$ 个——近似为 $\sigma^{\otimes k}$ 的混合。

**Step 4**: 逼近误差 $O(kd^2/n)$ 来自"类型数量"的控制（多项式 vs 指数）。

### 6.3 Finite de Finetti (Operational Version)

**Theorem** [Renner, 2007]: 对 permutation invariant 态，约化到 $k$ 个系统的态 $\epsilon$-接近某个 separable 态，其中 $\epsilon = O(kd^2/n)$。

### 6.4 Applications

1. **QKD security**: 将一般攻击归约为 collective 攻击
   - Eve 的攻击与 Alice/Bob 的态联合是 permutation invariant
   - de Finetti → 可以假设 Eve 在每轮做相同攻击
   - 安全性分析简化为单轮分析

2. **Entanglement detection**: 对称态的 entanglement 可以在低维空间检测

3. **Quantum hypothesis testing**: 多份态假设检验的最优性分析

**When to use**: 有 $n$ 份对称量子态，想简化为 i.i.d. 分析时。代价：$O(d^2/n)$ 的逼近误差。

**Cross-ref**: Post-selection technique (Section 2) 是 de Finetti 定理的推论/变体；[../03_quantum_info_theory/derivations/entanglement_theory.md]

---

## 7. Additional Tools (补充工具)

### 7.1 Fuchs-van de Graaf Inequalities

$$1 - F(\rho, \sigma) \leq \frac{1}{2}\|\rho - \sigma\|_1 \leq \sqrt{1 - F(\rho, \sigma)^2}$$

连接 fidelity 和 trace distance。当 $F \approx 1$ 时：$\frac{1}{2}\|\rho-\sigma\|_1 \leq \sqrt{1-F} \approx \sqrt{2(1-F)}$。

**Cross-ref**: [../02_quantum_mechanics/derivations/fidelity_and_trace_distance.md]

### 7.2 Fannes-Audenaert Inequality

$$|S(\rho) - S(\sigma)| \leq T \log(d-1) + H_2(T)$$

其中 $T = \frac{1}{2}\|\rho-\sigma\|_1$，$H_2$ 是二元熵，$d$ 是维度。

> 一行解释：态接近 → 熵也接近（连续性）。

**When to use**: 从 trace distance 的界推导 entropy 的界；QKD 安全性证明中的连续性论证。

### 7.3 Quantum Pinsker Inequality

$$\frac{1}{2}\|\rho - \sigma\|_1^2 \leq D(\rho\|\sigma) = \mathrm{tr}[\rho(\log\rho - \log\sigma)]$$

**When to use**: 将相对熵的界转化为 trace distance 的界（如 data processing inequality → trace distance 不增）。

### 7.4 Hayashi-Nagaoka Inequality

**Theorem**: 对 $0 \leq S \leq I$，$T \geq 0$：

$$I - (S+T)^{-1/2} S (S+T)^{-1/2} \leq 2(I - S) + 4T$$

**When to use**: 量子假设检验中的错误概率分析；量子信道编码的一次性界。

---

## Summary: When to Use Each Tool

| Tool | Use When | Key Feature |
|------|----------|-------------|
| Decoupling | 证明随机编码达到容量 | Haar 随机酉消除相关性 |
| Post-selection | 对称态归约到 i.i.d. | 多项式维度因子代价 |
| Quantum union bound | 多个量子约束同时成立 | $\sum\sqrt{\epsilon_i}$ 而非 $\sum\epsilon_i$ |
| Gentle measurement | 高概率测量几乎不扰动态 | $2\sqrt{\epsilon}$ 误差 |
| Operator monotonicity | 量子熵不等式、DPI | 矩阵函数的序保持 |
| de Finetti | 对称态 → i.i.d. 近似 | QKD安全性、假设检验 |
| Fuchs-van de Graaf | Fidelity ↔ trace distance | 两种距离度量的桥梁 |
| Fannes-Audenaert | Trace distance → entropy bounds | 熵的连续性 |
| Pinsker | Relative entropy → trace distance | KL散度的几何意义 |
| Hayashi-Nagaoka | 一次性假设检验 | 有限块长界 |

---

## Cross-References (交叉引用)

- **Concentration inequalities** → [concentration_inequalities.md]: Classical analogues
- **Union bound** → [concentration_inequalities.md] [F18.20]: Classical version
- **Fidelity/trace distance** → [../02_quantum_mechanics/derivations/fidelity_and_trace_distance.md]
- **Entropy inequalities** → [../03_quantum_info_theory/derivations/entropy_inequalities.md]
- **Quantum channels** → [../02_quantum_mechanics/derivations/quantum_channels_kraus.md]
- **QKD** → [../03_quantum_info_theory/derivations/]: Key distribution protocols
- **Original references**:
  - Dupuis, Hayden, Li, "A father protocol for quantum broadcast channels", IEEE TIT 2010
  - Christandl, König, Renner, "Postselection technique for quantum channels", PRL 2009
  - Sen, "Achieving the Han-Kobayashi inner bound", Ann. Stat. 2012
  - Winter, "Coding theorem and strong converse for quantum channels", IEEE TIT 1999
  - Watrous, "Theory of Quantum Information", Cambridge 2018 — [../03_quantum_info_theory/]
