# Quantum Channel Capacities

> Source: J. Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018, **Chapter 6**.

---

## 1. Framework: Channel Coding

### Definition 6.1 (Quantum Channel Code) **[Watrous, Ch.6, Def.6.1]**

An $(n, m, \varepsilon)$ code for a channel $\Phi: \mathrm{L}(\mathcal{X}) \to \mathrm{L}(\mathcal{Y})$ consists of:
- An encoding channel $\mathcal{E}: \mathrm{L}(\mathbb{C}^m) \to \mathrm{L}(\mathcal{X}^{\otimes n})$
- A decoding channel $\mathcal{D}: \mathrm{L}(\mathcal{Y}^{\otimes n}) \to \mathrm{L}(\mathbb{C}^m)$

such that the worst-case error satisfies:

$$
\max_{1 \leq j \leq m} \left(1 - \langle j | (\mathcal{D} \circ \Phi^{\otimes n} \circ \mathcal{E})(|j\rangle\langle j|) |j\rangle\right) \leq \varepsilon
$$

The **rate** is $R = \frac{\log m}{n}$.

---

## 2. Classical Capacity

### 2.1 Holevo Information

### Definition 6.2 (Holevo Information) **[Watrous, Ch.6, Def.6.2]**

For a channel $\Phi$ and an ensemble $\{(p_k, \rho_k)\}$:

$$
\chi(\{p_k, \rho_k\}; \Phi) = \mathrm{H}\!\left(\sum_k p_k \Phi(\rho_k)\right) - \sum_k p_k \,\mathrm{H}(\Phi(\rho_k))
$$

The **Holevo capacity** (single-letter) is:

$$
\chi(\Phi) = \max_{\{p_k, \rho_k\}} \chi(\{p_k, \rho_k\}; \Phi)
$$

### Proposition 6.3 (Alternative Expressions) **[Watrous, Ch.6, Prop.6.3]**

$$
\chi(\Phi) = \max_\rho \left[\mathrm{H}(\Phi(\rho)) - \min_{\{p_k,\rho_k\}: \sum p_k\rho_k = \rho} \sum_k p_k \mathrm{H}(\Phi(\rho_k))\right]
$$

For entanglement-breaking channels, $\chi(\Phi)$ equals the classical capacity.

### 2.2 HSW Theorem

### Theorem 6.7 (Holevo-Schumacher-Westmoreland) **[Watrous, Ch.6, Thm.6.7]**

The classical capacity of a quantum channel $\Phi$ is:

$$
C(\Phi) = \lim_{n \to \infty} \frac{1}{n} \chi(\Phi^{\otimes n})
$$

In particular, $C(\Phi) \geq \chi(\Phi)$.

**Proof outline (achievability, i.e., $C(\Phi) \geq \chi(\Phi)$)**:

**Step 1 (Random coding)**: Fix an ensemble $\{p_k, \rho_k\}_{k=1}^K$ achieving $\chi$. For each message $m \in \{1,\ldots,M\}$ where $M = 2^{nR}$, independently choose a codeword $(x_{m,1}, \ldots, x_{m,n})$ where each $x_{m,i}$ is drawn i.i.d. from $\{p_k\}$.

**Step 2 (Encoding)**: Encode message $m$ as $\rho_{x_{m,1}} \otimes \cdots \otimes \rho_{x_{m,n}}$.

**Step 3 (Decoding via pretty good measurement)**: The output state given message $m$ is:

$$
\sigma_m = \Phi(\rho_{x_{m,1}}) \otimes \cdots \otimes \Phi(\rho_{x_{m,n}})
$$

The average output is $\bar{\sigma} = \sum_m \frac{1}{M} \sigma_m$. Define the pretty good measurement (PGM):

$$
\mu_m = \bar{\sigma}^{-1/2} \sigma_m \bar{\sigma}^{-1/2} / M
$$

(normalized appropriately to form a POVM).

**Step 4 (Error analysis via quantum typical subspaces)**: By the quantum asymptotic equipartition property (AEP), for large $n$:
- $\sigma_m$ is essentially supported on a "conditionally typical" subspace of dimension $\approx 2^{n\mathrm{H}(\Phi(\rho_k))}$
- $\bar{\sigma}$ is essentially supported on a typical subspace of dimension $\approx 2^{n\mathrm{H}(\bar{\sigma})}$

The PGM succeeds with probability $\to 1$ as $n \to \infty$ provided:

$$
R < \mathrm{H}(\bar{\sigma}) - \sum_k p_k \mathrm{H}(\Phi(\rho_k)) = \chi(\{p_k, \rho_k\}; \Phi)
$$

**Step 5 (Derandomization)**: A random code achieves low average error, so there exists a deterministic code achieving the same rate.

**Proof outline (converse, i.e., $C(\Phi) \leq \lim \frac{1}{n}\chi(\Phi^{\otimes n})$)**:

**Step 1**: For any $(n, 2^{nR}, \varepsilon)$ code with encoding states $\rho_m$, the Holevo bound gives:

$$
nR(1-\varepsilon) \leq \chi(\{1/M, \rho_m\}; \Phi^{\otimes n}) + 1 \leq \chi(\Phi^{\otimes n}) + 1
$$

The first inequality uses Fano's inequality. The second uses the definition of $\chi$.

**Step 2**: Dividing by $n$ and taking $n \to \infty$, $\varepsilon \to 0$:

$$
R \leq \lim_{n\to\infty} \frac{1}{n}\chi(\Phi^{\otimes n}) \quad\blacksquare
$$

### Remark on Superadditivity **[Watrous, Ch.6]**

The regularization is necessary: there exist channels where $\chi(\Phi^{\otimes 2}) > 2\chi(\Phi)$ (Hastings 2009). Thus $C(\Phi) > \chi(\Phi)$ in general -- the classical capacity is **not** single-letter.

---

## 3. Quantum Capacity

### 3.1 Coherent Information

### Definition 6.15 (Coherent Information) **[Watrous, Ch.6, Def.6.15]**

For a channel $\Phi$ and input state $\rho$:

$$
I_c(\rho, \Phi) = \mathrm{H}(\Phi(\rho)) - \mathrm{H}_e(\Phi, \rho)
$$

where $\mathrm{H}_e(\Phi, \rho)$ is the entropy exchange. Equivalently, for a purification $|\psi\rangle_{RA}$ of $\rho$:

$$
I_c(\rho, \Phi) = \mathrm{H}(B)_\sigma - \mathrm{H}(RB)_\sigma = -\mathrm{H}(R|B)_\sigma
$$

where $\sigma_{RB} = (\mathrm{id}_R \otimes \Phi)(|\psi\rangle\langle\psi|)$.

### Definition 6.17 (Maximum Coherent Information) **[Watrous, Ch.6, Def.6.17]**

$$
Q^{(1)}(\Phi) = \max_{\rho \in \mathrm{D}(\mathcal{X})} I_c(\rho, \Phi)
$$

### Proposition 6.18 (Properties of Coherent Information) **[Watrous, Ch.6, Prop.6.18]**

1. $I_c(\rho, \Phi) \leq \mathrm{H}(\rho)$ (follows from Araki-Lieb).
2. $I_c(\rho, \Phi)$ can be negative (unlike Holevo information).
3. $I_c$ is **not** concave in $\rho$ in general.
4. Data processing: $I_c(\rho, \Psi \circ \Phi) \leq I_c(\rho, \Phi)$ for channels $\Psi$.

### 3.2 LSD Theorem

### Theorem 6.24 (Lloyd-Shor-Devetak) **[Watrous, Ch.6, Thm.6.24]**

The quantum capacity of $\Phi$ is:

$$
Q(\Phi) = \lim_{n \to \infty} \frac{1}{n} Q^{(1)}(\Phi^{\otimes n})
$$

**Proof outline (achievability)**:

**Step 1 (Random stabilizer codes)**: For a given input state $\rho$ achieving high coherent information, use random stabilizer codes of rate $R < I_c(\rho, \Phi)$.

**Step 2 (Decoupling argument)**: The key idea (due to Devetak, building on Schumacher-Nielsen and Lloyd) is the **decoupling principle**: if the environment $E$ (complementary channel output) is nearly decoupled from the reference $R$, then the information can be recovered from $B$.

Formally, if $\rho_{RE}$ is close to $\rho_R \otimes \rho_E$, then there exists a decoding channel $\mathcal{D}: \mathrm{L}(\mathcal{Y}) \to \mathrm{L}(\mathcal{X})$ such that $\mathcal{D} \circ \Phi \approx \mathrm{id}$ on the code subspace.

**Step 3 (Rate analysis)**: The decoupling condition is satisfied when:

$$
R < I_c(\rho, \Phi) = \mathrm{H}(B) - \mathrm{H}(E)
$$

(using $\mathrm{H}(E) = \mathrm{H}_e(\Phi,\rho)$ for pure input).

**Step 4 (Regularization)**: Apply the argument to $\Phi^{\otimes n}$ and optimize, giving the regularized formula.

**Proof outline (converse)**:

Uses the no-cloning bound and quantum Fano inequality. If a code transmits $Q$ qubits per channel use with error $\varepsilon \to 0$, then:

$$
Q \leq \frac{1}{n} Q^{(1)}(\Phi^{\otimes n}) + \delta(\varepsilon)
$$

where $\delta(\varepsilon) \to 0$ as $\varepsilon \to 0$. $\blacksquare$

### Remark on Superadditivity **[Watrous, Ch.6]**

The quantum capacity is also superadditive: $Q^{(1)}(\Phi^{\otimes n})$ can exceed $nQ^{(1)}(\Phi)$. Smith-Yard (2008) showed that two zero-capacity channels can have positive joint capacity: $Q(\Phi_1) = Q(\Phi_2) = 0$ but $Q(\Phi_1 \otimes \Phi_2) > 0$ ("superactivation").

---

## 4. Entanglement-Assisted Classical Capacity

### Theorem 6.33 (Bennett-Shor-Smolin-Thapliyal) **[Watrous, Ch.6, Thm.6.33]**

The entanglement-assisted classical capacity is:

$$
C_E(\Phi) = \max_{\rho \in \mathrm{D}(\mathcal{X})} I(R;B)_\sigma
$$

where $\sigma_{RB} = (\mathrm{id}_R \otimes \Phi)(|\psi\rangle\langle\psi|_{RA})$ and $|\psi\rangle$ is a purification of $\rho$.

Explicitly:

$$
C_E(\Phi) = \max_\rho \left[\mathrm{H}(\rho) + \mathrm{H}(\Phi(\rho)) - \mathrm{H}_e(\Phi, \rho)\right]
$$

**Key properties**:
1. **Single-letter**: No regularization needed! $C_E$ is additive.
2. $C_E(\Phi) \geq C(\Phi)$ (entanglement can only help).
3. $C_E(\Phi) \geq 2Q(\Phi)$ (by superdense coding protocol).
4. $C_E(\Phi) = 2C(\Phi)$ for the quantum erasure channel.

**Proof sketch (achievability)**:

**Step 1**: Alice and Bob share maximally entangled pairs. Alice encodes classical messages by performing operations on her half of the entangled pairs, then sends through $\Phi^{\otimes n}$.

**Step 2**: Bob's decoding exploits both the channel output and his entanglement. The mutual information $I(R;B)$ quantifies how much classical information can be extracted.

**Step 3**: The achievability follows from a quantum version of the covering lemma, using the shared entanglement to create effective "codewords" with higher distinguishability.

**Proof sketch (converse)**:

For any $(n, 2^{nR}, \varepsilon)$ entanglement-assisted code:

$$
nR \leq I(M; B^n)_\sigma + n\delta(\varepsilon) \leq \sum_{i=1}^n I(R_i; B_i) + n\delta(\varepsilon)
$$

where the second inequality uses the chain rule and data processing. Maximizing over inputs gives $R \leq C_E(\Phi)$. $\blacksquare$

---

## 5. Private Classical Capacity

### Definition 6.35 (Private Information) **[Watrous, Ch.6, Def.6.35]**

$$
P^{(1)}(\Phi) = \max_{\{p_k,\rho_k\}} \left[\chi(\{p_k, \rho_k\}; \Phi) - \chi(\{p_k, \rho_k\}; \hat{\Phi})\right]
$$

where $\hat{\Phi}$ is the complementary channel.

### Theorem 6.38 (Private Capacity) **[Watrous, Ch.6, Thm.6.38]**

$$
C_P(\Phi) = \lim_{n\to\infty} \frac{1}{n} P^{(1)}(\Phi^{\otimes n})
$$

### Theorem 6.40 (Relation to Quantum Capacity) **[Watrous, Ch.6, Thm.6.40]**

$$
C_P(\Phi) \geq Q(\Phi)
$$

with equality for degradable channels. More precisely, $P^{(1)}(\Phi) \geq Q^{(1)}(\Phi)$ always, and for degradable channels both are additive and equal.

---

## 6. Degradable and Anti-degradable Channels

### Definition 6.42 (Degradable Channel) **[Watrous, Ch.6, Def.6.42]**

$\Phi$ is **degradable** if there exists a channel $\mathcal{D}$ such that $\hat{\Phi} = \mathcal{D} \circ \Phi$ (the complementary channel can be obtained by further degrading the output).

### Theorem 6.44 (Capacity of Degradable Channels) **[Watrous, Ch.6, Thm.6.44]**

For degradable $\Phi$:

$$
Q(\Phi) = Q^{(1)}(\Phi) = \max_\rho I_c(\rho, \Phi)
$$

The capacity is single-letter! This follows because coherent information is additive for degradable channels.

**Proof**: For degradable $\Phi$, $I_c(\rho, \Phi)$ is concave in $\rho$ (unlike the general case). Concavity + additivity of $Q^{(1)}$ for degradable channels gives the single-letter formula.

The concavity is proved using the degrading channel $\mathcal{D}$: since $\hat{\Phi} = \mathcal{D}\circ\Phi$, data processing gives $\mathrm{H}_e(\Phi,\rho) = \mathrm{H}(\hat{\Phi}(\rho)) = \mathrm{H}(\mathcal{D}(\Phi(\rho)))$, and the composed entropy expression becomes concave. $\blacksquare$

### Definition 6.46 (Anti-degradable Channel) **[Watrous, Ch.6, Def.6.46]**

$\Phi$ is **anti-degradable** if there exists $\mathcal{D}$ such that $\Phi = \mathcal{D} \circ \hat{\Phi}$.

### Proposition 6.47 **[Watrous, Ch.6, Prop.6.47]**

If $\Phi$ is anti-degradable, then $Q(\Phi) = 0$. (No quantum information can be transmitted because the environment has all the information.)

---

## 7. Capacity Hierarchy Summary

For a quantum channel $\Phi$:

$$
Q(\Phi) \leq C_P(\Phi) \leq C(\Phi) \leq C_E(\Phi)
$$

$$
Q(\Phi) \leq \frac{1}{2} C_E(\Phi)
$$

Additional relations:
- $C(\Phi) \geq \chi(\Phi)$ (HSW)
- $Q(\Phi) \geq Q^{(1)}(\Phi)$ (LSD)
- For degradable channels: $Q(\Phi) = C_P(\Phi) = Q^{(1)}(\Phi)$ (single-letter)
- For entanglement-breaking channels: $Q(\Phi) = 0$ and $C(\Phi) = \chi(\Phi)$ (single-letter)

---

## 8. Quantum Capacity of Specific Channels

### Example: Depolarizing Channel **[Watrous, Ch.6]**

$\Delta_p(\rho) = (1-p)\rho + \frac{p}{d^2-1}\sum_{i \neq 0} W_i \rho W_i^*$ for Weyl operators $W_i$.

- $Q^{(1)}(\Delta_p) = \log d + (1-p)\log(1-p) + p\log(p/(d^2-1))$ (hashing bound)
- $Q(\Delta_p) = 0$ for $p \geq p^*$ (anti-degradable regime)
- Exact $Q(\Delta_p)$ is unknown for intermediate $p$

### Example: Erasure Channel **[Watrous, Ch.6]**

$\mathcal{E}_p(\rho) = (1-p)\rho \oplus p|e\rangle\langle e|\mathrm{Tr}(\rho)$ (erases with probability $p$).

- $Q(\mathcal{E}_p) = (1-2p)\log d$ for $p \leq 1/2$, and 0 for $p > 1/2$
- $C(\mathcal{E}_p) = (1-p)\log d$
- $C_E(\mathcal{E}_p) = 2(1-p)\log d$

The erasure channel is degradable for $p \leq 1/2$ and anti-degradable for $p > 1/2$.

---

## 9. Quantum Data Processing and No-Cloning Bound

### Theorem 6.50 (No-Cloning Bound) **[Watrous, Ch.6, Thm.6.50]**

For any channel $\Phi$:

$$
Q(\Phi) \leq \log d - \mathrm{H}_{\min}(\hat{\Phi})
$$

where $\mathrm{H}_{\min}$ is the min-entropy of the complementary channel evaluated at the maximally mixed input.

### Theorem (Quantum Singleton Bound) **[Watrous, Ch.6]**

An $((n, K, d))$ quantum error-correcting code satisfies:

$$
\log K \leq n - 2(d-1)
$$

in qubits. This is the quantum analogue of the classical Singleton bound.

---

## 10. Supplement: Key Results from Wilde

> 以下内容补充自 Wilde, *From Classical to Quantum Shannon Theory*
> (`references/wilde_shannon_theory/qit-notes.tex`)，侧重 Watrous 未详细展开的证明细节。

### 10.1 Additivity of Channel Mutual Information **[Wilde, Ch.13, Thm.13.3.1]**

$$I(\mathcal{N} \otimes \mathcal{M}) = I(\mathcal{N}) + I(\mathcal{M})$$

**完整证明**：

*非平凡方向* ($\leq$): 设 $\phi_{AA_1'A_2'}$ 为最优输入纯态，$\rho_{AB_1B_2} = (\mathcal{N} \otimes \mathcal{M})(\phi)$。

利用互信息链式法则：

$$I(A;B_1B_2) = I(A;B_1) + I(AB_1;B_2) - I(B_1;B_2) \leq I(A;B_1) + I(AB_1;B_2)$$

由于 $A$ 延伸了 $\mathcal{N}$ 的参考系统：$I(A;B_1) \leq I(\mathcal{N})$。

由于 $AB_1$ 延伸了 $\mathcal{M}$ 的参考系统：$I(AB_1;B_2) \leq I(\mathcal{M})$。$\square$

**意义**: 纠缠辅助经典容量 $C_{EA} = I(\mathcal{N})$ 是单字母可计算的。

### 10.2 Coherent Information Additivity for Degradable Channels **[Wilde, Ch.13, Thm.13.4.1]**

**证明的核心步骤**: 对纯态 $\rho_{AB_1E_1B_2E_2}$：

$$Q(\mathcal{N}\otimes\mathcal{M}) = H(B_1B_2) - H(E_1E_2) = [H(B_1)-H(E_1)] + [H(B_2)-H(E_2)] - [I(B_1;B_2)-I(E_1;E_2)]$$

Degradability 条件使得 $I(B_1;B_2) \geq I(E_1;E_2)$（因为 $E$ 是 $B$ 的退化版本，数据处理不等式保证相关性不增），所以最后一项 $\leq 0$。

### 10.3 Schumacher Compression **[Wilde, Ch.18]**

量子信源压缩的最优速率 $R = H(\rho)$。证明使用量子典型子空间：

- $\rho^{\otimes n}$ 的典型子空间 $T_\delta^n$ 有维度 $\approx 2^{nH(\rho)}$
- 投影到典型子空间的保真度 $F \to 1$ (当 $n \to \infty$)

这是量子版本的 Shannon 信源编码定理。

### 10.4 Quantum Capacity: No-Cloning Intuition **[Wilde, Ch.24]**

量子容量的直觉来自不可克隆定理：

1. 信道的等距扩展将 Alice 的输入送到 Bob 和 Eve
2. Alice 需要找一个子空间，使得只有 Bob 能恢复信息而 Eve 不能
3. 如果 Eve 也能恢复，违反不可克隆定理
4. 这个子空间的维度与 $2^{n \cdot [H(B)-H(E)]}$ 成正比——即相干信息

### 10.5 Superactivation **[Wilde, Ch.24, Section 24.6]**; Smith & Yard (2008)

存在 $\mathcal{N}_1$ (PPT entangled state generating channel) 和 $\mathcal{N}_2$ (50% erasure channel)，各自量子容量为零，但：

$$Q(\mathcal{N}_1 \otimes \mathcal{N}_2) > 0$$

这是量子 Shannon 理论中最出人意料的结果之一，表明量子容量的行为与经典容量本质不同。

---

## References (Complete)

- Watrous, *The Theory of Quantum Information*, Ch.6
- Wilde, *From Classical to Quantum Shannon Theory*, Ch.13, 18--24
- Holevo, Probl. Inf. Transm. 9, 177 (1973)
- Schumacher & Westmoreland, Phys. Rev. A 56, 131 (1997)
- Hausladen et al., Phys. Rev. A 54, 1869 (1996)
- Schumacher, Phys. Rev. A 51, 2738 (1995)
- Lloyd, Phys. Rev. A 55, 1613 (1997)
- Shor, MSRI lecture (2002)
- Devetak, IEEE Trans. Inf. Theory 51, 44 (2005)
- Bennett, Shor, Smolin, Thapliyal, IEEE Trans. Inf. Theory 48, 2637 (2002)
- Devetak & Shor, Commun. Math. Phys. 256, 287 (2005) — degradable channels
- Hastings, Nature Physics 5, 255 (2009) — non-additivity of Holevo information
- Smith & Yard, Science 321, 1812 (2008) — superactivation
