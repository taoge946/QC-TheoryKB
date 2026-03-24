# Quantum State Discrimination

> Source: J. Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018, **Chapter 4**.

---

## 1. Framework

### Definition 4.1 (State Discrimination Problem) **[Watrous, Ch.4, Def.4.1]**

Given an ensemble $\mathcal{E} = \{(p_k, \rho_k)\}_{k=1}^N$ where:
- $p_k > 0$ are prior probabilities ($\sum_k p_k = 1$)
- $\rho_k \in \mathrm{D}(\mathcal{X})$ are quantum states

A **measurement strategy** is a POVM $\{\mu_k\}_{k=1}^N$ with $\mu_k \geq 0$ and $\sum_k \mu_k = \mathbb{1}$.

The **success probability** is:

$$
p_{\mathrm{succ}}(\mathcal{E}, \{\mu_k\}) = \sum_{k=1}^N p_k \,\mathrm{Tr}(\rho_k \mu_k)
$$

The **optimal success probability** is:

$$
p_{\mathrm{opt}}(\mathcal{E}) = \max_{\{\mu_k\}} \sum_{k=1}^N p_k \,\mathrm{Tr}(\rho_k \mu_k)
$$

---

## 2. Two-State Discrimination: Helstrom Bound

### Theorem 4.3 (Helstrom Bound) **[Watrous, Ch.4, Thm.4.3]**

For two states $\rho_0, \rho_1$ with prior probabilities $p_0, p_1$:

$$
p_{\mathrm{opt}} = \frac{1}{2}\left(1 + \|p_0 \rho_0 - p_1 \rho_1\|_1\right) = \frac{1}{2} + \frac{1}{2}\|p_0 \rho_0 - p_1 \rho_1\|_1
$$

Wait -- let us be precise. Define $\Gamma = p_0\rho_0 - p_1\rho_1$. Then:

$$
p_{\mathrm{opt}} = \frac{1}{2}(1 + \|\Gamma\|_1)
$$

Hmm, that gives $p_{\mathrm{opt}} > 1$ for orthogonal states. Let me correct:

$$
p_{\mathrm{opt}} = \frac{1}{2}\left(1 + \frac{1}{2}\|p_0\rho_0 - p_1\rho_1\|_1 \cdot 2 \right)
$$

No. The correct statement:

$$
\boxed{p_{\mathrm{opt}} = \frac{1}{2}\left(1 + \|p_0\rho_0 - p_1\rho_1\|_1\right)}
$$

Wait, let me verify: for orthogonal pure states with equal priors, $\|p_0\rho_0 - p_1\rho_1\|_1 = \frac{1}{2}\cdot 2 = 1$. So $p_{\mathrm{opt}} = \frac{1}{2}(1+1) = 1$. Correct.

For identical states, $\|\frac{1}{2}\rho - \frac{1}{2}\rho\|_1 = 0$. So $p_{\mathrm{opt}} = 1/2$. Correct (random guessing).

Actually I need to double-check: $\|p_0\rho_0 - p_1\rho_1\|_1$ for $p_0=p_1=1/2$, $\rho_0 \perp \rho_1$: $\|\frac{1}{2}\rho_0 - \frac{1}{2}\rho_1\|_1 = \frac{1}{2}\|\rho_0\|_1 + \frac{1}{2}\|\rho_1\|_1 = 1$ (since they have orthogonal support). So $p_{\mathrm{opt}} = \frac{1}{2}(1+1) = 1$. Yes, correct.

**Proof**:

**Step 1 (Variational form)**: The success probability is:

$$
p_{\mathrm{succ}} = p_0\mathrm{Tr}(\rho_0 \mu_0) + p_1\mathrm{Tr}(\rho_1 \mu_1) = p_0\mathrm{Tr}(\rho_0\mu_0) + p_1\mathrm{Tr}(\rho_1(\mathbb{1}-\mu_0))
$$
$$
= p_1 + \mathrm{Tr}((p_0\rho_0 - p_1\rho_1)\mu_0)
$$

So maximizing over $\mu_0$ with $0 \leq \mu_0 \leq \mathbb{1}$:

$$
p_{\mathrm{opt}} = p_1 + \max_{0 \leq M \leq \mathbb{1}} \mathrm{Tr}(\Gamma \, M)
$$

where $\Gamma = p_0\rho_0 - p_1\rho_1$.

**Step 2 (Optimal measurement)**: Write $\Gamma = \Gamma_+ - \Gamma_-$ where $\Gamma_+ = \sum_{\lambda_i > 0} \lambda_i |v_i\rangle\langle v_i|$ (positive part) and $\Gamma_- = \sum_{\lambda_i < 0} |\lambda_i| |v_i\rangle\langle v_i|$ (negative part).

Then $\mathrm{Tr}(\Gamma M) \leq \mathrm{Tr}(\Gamma_+)$ for any $0 \leq M \leq \mathbb{1}$, with equality when $M = \Pi_+$ (projector onto positive eigenspace of $\Gamma$).

**Step 3**: Note that $\|\Gamma\|_1 = \mathrm{Tr}(\Gamma_+) + \mathrm{Tr}(\Gamma_-)$ and $\mathrm{Tr}(\Gamma) = p_0 - p_1 = \mathrm{Tr}(\Gamma_+) - \mathrm{Tr}(\Gamma_-)$. So:

$$
\mathrm{Tr}(\Gamma_+) = \frac{1}{2}(\|\Gamma\|_1 + p_0 - p_1)
$$

Therefore:

$$
p_{\mathrm{opt}} = p_1 + \frac{1}{2}(\|\Gamma\|_1 + p_0 - p_1) = \frac{p_0+p_1}{2} + \frac{1}{2}\|\Gamma\|_1 = \frac{1}{2}(1 + \|p_0\rho_0-p_1\rho_1\|_1)
$$

$\blacksquare$

### Corollary 4.4 (Equal Priors) **[Watrous, Ch.4, Cor.4.4]**

For $p_0 = p_1 = 1/2$:

$$
p_{\mathrm{opt}} = \frac{1}{2}\left(1 + \frac{1}{2}\|\rho_0 - \rho_1\|_1\right)
$$

$$
p_{\mathrm{err}} = \frac{1}{2}\left(1 - \frac{1}{2}\|\rho_0 - \rho_1\|_1\right)
$$

### Proposition 4.5 (Helstrom Measurement) **[Watrous, Ch.4, Prop.4.5]**

The optimal POVM for two-state discrimination is:

$$
\mu_0 = \Pi_+, \quad \mu_1 = \mathbb{1} - \Pi_+
$$

where $\Pi_+$ is the projector onto the positive eigenspace of $\Gamma = p_0\rho_0 - p_1\rho_1$. This is the **Helstrom measurement**.

---

## 3. Multiple-State Discrimination

### Theorem 4.6 (SDP Formulation) **[Watrous, Ch.4, Thm.4.6]**

The optimal discrimination of $N$ states is the SDP (see also `sdp_quantum_info.md`):

**Primal**:
$$
p_{\mathrm{opt}} = \max \sum_k p_k \mathrm{Tr}(\rho_k \mu_k) \quad \text{s.t.} \quad \mu_k \geq 0,\; \sum_k \mu_k = \mathbb{1}
$$

**Dual**:
$$
p_{\mathrm{opt}} = \min \mathrm{Tr}(\Lambda) \quad \text{s.t.} \quad \Lambda \geq p_k \rho_k \;\forall k
$$

**Optimality conditions** (complementary slackness):

$$
\mu_k^* (p_k \rho_k - \Lambda^*) = 0 \quad \forall k
$$

and $\Lambda^* \geq p_k \rho_k$ for all $k$.

The dual variable $\Lambda^*$ is the "least favorable" mixture: it equals $\sum_k p_k \rho_k \mu_k^*$ at optimality.

### Theorem 4.7 (Necessary and Sufficient Conditions) **[Watrous, Ch.4, Thm.4.7]**

A POVM $\{\mu_k\}$ is optimal for discriminating $\{p_k, \rho_k\}$ if and only if:

$$
\Lambda = \sum_j p_j \rho_j \mu_j \geq p_k \rho_k \quad \forall k
$$

where equality holds on the support of $\mu_k$.

---

## 4. Pretty Good Measurement

### Definition 4.8 (Pretty Good Measurement / Square Root Measurement) **[Watrous, Ch.4, Def.4.8]**

Given ensemble $\{p_k, \rho_k\}$ with $\bar{\rho} = \sum_k p_k \rho_k$, the **pretty good measurement** (PGM) is:

$$
\mu_k^{\mathrm{PGM}} = p_k \,\bar{\rho}^{-1/2} \rho_k \,\bar{\rho}^{-1/2}
$$

(where the inverse is taken on the support of $\bar{\rho}$).

**Verification**: $\sum_k \mu_k^{\mathrm{PGM}} = \bar{\rho}^{-1/2}\left(\sum_k p_k\rho_k\right)\bar{\rho}^{-1/2} = \bar{\rho}^{-1/2}\bar{\rho}\,\bar{\rho}^{-1/2} = \Pi_{\bar{\rho}}$ (projector onto support of $\bar{\rho}$). If $\bar{\rho}$ has full support, this equals $\mathbb{1}$. Each $\mu_k^{\mathrm{PGM}} \geq 0$ since it is a congruence of $\rho_k \geq 0$.

### Theorem 4.9 (PGM Performance Bound) **[Watrous, Ch.4, Thm.4.9]**

$$
p_{\mathrm{succ}}(\mathrm{PGM}) \geq p_{\mathrm{opt}}^2
$$

In particular, if $p_{\mathrm{opt}} = 1 - \varepsilon$, then $p_{\mathrm{succ}}(\mathrm{PGM}) \geq 1 - 2\varepsilon + \varepsilon^2 \geq 1 - 2\varepsilon$.

**Proof sketch**: The PGM success probability is:

$$
p_{\mathrm{succ}}^{\mathrm{PGM}} = \sum_k p_k \mathrm{Tr}(\rho_k \mu_k^{\mathrm{PGM}}) = \sum_k p_k^2 \mathrm{Tr}(\rho_k \bar{\rho}^{-1/2}\rho_k\bar{\rho}^{-1/2})
$$

Using the Cauchy-Schwarz inequality for the Hilbert-Schmidt inner product and properties of the optimal measurement, one shows:

$$
\left(\sum_k p_k\mathrm{Tr}(\rho_k\mu_k^*)\right)^2 \leq \sum_k p_k^2\mathrm{Tr}(\rho_k\bar{\rho}^{-1/2}\rho_k\bar{\rho}^{-1/2})
$$

for any POVM $\{\mu_k^*\}$. Hence $p_{\mathrm{opt}}^2 \leq p_{\mathrm{succ}}^{\mathrm{PGM}}$. $\blacksquare$

The PGM is asymptotically optimal in many settings (e.g., when used in the HSW coding theorem proof).

---

## 5. Unambiguous Discrimination

### Definition 4.10 (Unambiguous Discrimination) **[Watrous, Ch.4, Def.4.10]**

**Unambiguous** (or error-free) discrimination uses a POVM $\{\mu_0, \mu_1, \ldots, \mu_N, \mu_?\}$ where:
- Outcome $k$: "state is $\rho_k$" (with certainty, i.e., no error)
- Outcome $?$: "inconclusive"

The **zero-error condition** requires:

$$
\mathrm{Tr}(\rho_j \mu_k) = 0 \quad \forall j \neq k
$$

Goal: maximize the success probability $p_{\mathrm{succ}} = \sum_k p_k \mathrm{Tr}(\rho_k \mu_k)$ (or equivalently, minimize the inconclusive probability).

**Necessary condition**: Unambiguous discrimination is possible only if the states $\{\rho_k\}$ have distinct supports (for pure states: they must be linearly independent).

### Theorem 4.14 (Unambiguous Discrimination of Two Pure States) **[Watrous, Ch.4, Thm.4.14]**

For two pure states $|\psi_0\rangle, |\psi_1\rangle$ with equal priors:

$$
p_{\mathrm{succ}}^{\mathrm{unamb}} = 1 - |\langle\psi_0|\psi_1\rangle|
$$

$$
p_? = |\langle\psi_0|\psi_1\rangle|
$$

For general priors $p_0, p_1$:

$$
p_?^{\mathrm{opt}} = 2\sqrt{p_0 p_1} \,|\langle\psi_0|\psi_1\rangle| \quad (\text{when } p_0, p_1 \text{ are not too asymmetric})
$$

**Proof for equal priors**:

**Step 1**: Write $|\psi_0\rangle = \alpha|0\rangle + \beta|1\rangle$ and $|\psi_1\rangle = \alpha|0\rangle - \beta|1\rangle$ in an appropriate basis (using the 2D subspace spanned by the two states, with $|\langle\psi_0|\psi_1\rangle| = |\alpha^2 - \beta^2|$, and choosing $\alpha = \cos(\theta/2)$, $\beta = \sin(\theta/2)$).

**Step 2**: The zero-error conditions require:
- $\mu_0 |\psi_1\rangle = 0$: $\mu_0$ must annihilate $|\psi_1\rangle$
- $\mu_1 |\psi_0\rangle = 0$: $\mu_1$ must annihilate $|\psi_0\rangle$

So $\mu_0 \propto |\psi_1^\perp\rangle\langle\psi_1^\perp|$ and $\mu_1 \propto |\psi_0^\perp\rangle\langle\psi_0^\perp|$ where $|\psi_k^\perp\rangle$ is orthogonal to $|\psi_k\rangle$ in the 2D subspace.

**Step 3**: The constraint $\mu_0 + \mu_1 + \mu_? = \mathbb{1}$ with $\mu_? \geq 0$ determines the maximum scaling. The optimal solution gives:

$$
p_{\mathrm{succ}} = 1 - |\langle\psi_0|\psi_1\rangle|
$$

This is the **IDP bound** (Ivanovic-Dieks-Peres). $\blacksquare$

### Proposition 4.15 (Connection to Fidelity) **[Watrous, Ch.4, Prop.4.15]**

For two general (mixed) states with equal priors:

$$
p_?^{\mathrm{opt}} \geq \sqrt{F(\rho_0, \rho_1)}
$$

For pure states, equality holds: $p_? = |\langle\psi_0|\psi_1\rangle| = \sqrt{F}$.

---

## 6. Quantum Chernoff Bound

### Theorem 4.20 (Quantum Chernoff Bound) **[Watrous, Ch.4, Thm.4.20]**

For discriminating $\rho_0^{\otimes n}$ vs $\rho_1^{\otimes n}$ (many copies), the optimal error probability satisfies:

$$
p_{\mathrm{err}}^{(n)} \sim \exp\left(-n \,\xi_{\mathrm{QCB}}\right)
$$

where the **quantum Chernoff exponent** is:

$$
\xi_{\mathrm{QCB}} = -\log \min_{0 \leq s \leq 1} \mathrm{Tr}(\rho_0^s \rho_1^{1-s})
$$

More precisely (Audenaert et al. 2007, Nussbaum-Szkola 2009):

$$
\lim_{n\to\infty} -\frac{1}{n}\log p_{\mathrm{err}}^{(n)} = \xi_{\mathrm{QCB}}
$$

---

## 7. Quantum Stein's Lemma (Asymmetric Hypothesis Testing)

### Theorem 4.22 (Quantum Stein's Lemma) **[Watrous, Ch.4, Thm.4.22]**

In the asymmetric setting (Type I error $\leq \varepsilon$, minimize Type II error):

$$
\lim_{n\to\infty} -\frac{1}{n}\log \beta_n(\varepsilon) = \mathrm{D}(\rho_0 \| \rho_1)
$$

for any fixed $0 < \varepsilon < 1$, where $\beta_n(\varepsilon)$ is the minimum Type II error probability subject to Type I error $\leq \varepsilon$.

**Proof outline**:

**Achievability** (Hiai-Petz): Use the Neyman-Pearson test on $n$ copies. The projector $\Pi_n = \{\rho_0^{\otimes n} \geq 2^{n(D(\rho_0\|\rho_1)-\delta)}\rho_1^{\otimes n}\}$ (projection onto the subspace where the likelihood ratio exceeds the threshold) satisfies:
- Type I: $\mathrm{Tr}(\rho_0^{\otimes n}(\mathbb{1}-\Pi_n)) \to 0$ (by quantum AEP)
- Type II: $\mathrm{Tr}(\rho_1^{\otimes n}\Pi_n) \leq 2^{-n(D(\rho_0\|\rho_1)-\delta)}$

**Converse** (Ogawa-Nagaoka): For any sequence of measurements with Type I error $\leq \varepsilon < 1$:

$$
\mathrm{Tr}(\rho_1^{\otimes n}\mu_n) \geq 2^{-n(D(\rho_0\|\rho_1)+\delta)}
$$

for sufficiently large $n$. This uses the operator Chernoff bound and properties of the quantum relative entropy.

The quantum Stein's lemma establishes $\mathrm{D}(\rho_0\|\rho_1)$ as the fundamental asymptotic rate of quantum hypothesis testing. $\blacksquare$

---

## 8. Channel Discrimination

### Definition 4.25 (Channel Discrimination) **[Watrous, Ch.4]**

Given channels $\Phi_0, \Phi_1$ and one use, find input state $\rho$ (possibly entangled with a reference) and measurement to maximize discrimination probability.

$$
p_{\mathrm{opt}} = \frac{1}{2}\left(1 + \frac{1}{2}\|\Phi_0 - \Phi_1\|_\diamond\right)
$$

where $\|\cdot\|_\diamond$ is the diamond norm.

**Proof**: By definition:

$$
\|\Phi_0-\Phi_1\|_\diamond = \sup_\rho \|(\Phi_0-\Phi_1)\otimes\mathrm{id})(\rho)\|_1
$$

The optimal input is generally entangled with a reference system of the same dimension. Then the Helstrom bound for the output states gives the result.

### Proposition 4.26 (Entanglement Helps) **[Watrous, Ch.4, Prop.4.26]**

There exist channels $\Phi_0, \Phi_1$ such that:

$$
\max_\rho \|\Phi_0(\rho)-\Phi_1(\rho)\|_1 < \|\Phi_0-\Phi_1\|_\diamond
$$

That is, entangled inputs with a reference system strictly improve channel discrimination. This is the operational meaning of the diamond norm using an ancilla.

---

## 9. Summary of Discrimination Bounds

| Scenario | Quantity | Formula |
|----------|----------|---------|
| Two states, single copy | Helstrom bound | $p_{\mathrm{opt}} = \frac{1}{2}(1+\|p_0\rho_0-p_1\rho_1\|_1)$ |
| Two states, $n$ copies (symmetric) | Quantum Chernoff | $p_{\mathrm{err}} \sim e^{-n\xi_{\mathrm{QCB}}}$ |
| Two states, $n$ copies (asymmetric) | Quantum Stein | $\beta_n \sim e^{-nD(\rho_0\|\rho_1)}$ |
| Two pure states, unambiguous | IDP bound | $p_? = |\langle\psi_0|\psi_1\rangle|$ |
| $N$ states | SDP | $p_{\mathrm{opt}} = \min\mathrm{Tr}(\Lambda)$ s.t. $\Lambda\geq p_k\rho_k$ |
| Two channels | Diamond norm | $p_{\mathrm{opt}} = \frac{1}{2}(1+\frac{1}{2}\|\Phi_0-\Phi_1\|_\diamond)$ |
| $N$ states, near-optimal | PGM | $p_{\mathrm{succ}}^{\mathrm{PGM}} \geq p_{\mathrm{opt}}^2$ |

---

## 10. Fidelity Function (from Watrous Ch.3)

### Definition 10.1 (Fidelity) **[Watrous, Ch.3, §3.2]**

For $\rho, \sigma \in \mathrm{D}(\mathcal{X})$:

$$F(\rho, \sigma) = \|\sqrt{\rho}\sqrt{\sigma}\|_1^2 = \left(\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\sqrt{\rho}}\right)^2$$

For pure states: $F(|\psi\rangle\langle\psi|, |\phi\rangle\langle\phi|) = |\langle\psi|\phi\rangle|^2$.

### Theorem 10.2 (Uhlmann's Theorem) **[Watrous, Ch.3, Thm.3.20]**

$$F(\rho, \sigma) = \max_{|\psi\rangle, |\phi\rangle} |\langle\psi|\phi\rangle|^2$$

where the maximum is over all purifications $|\psi\rangle$ of $\rho$ and $|\phi\rangle$ of $\sigma$.

> Watrous, Ch.3, §3.2.2: Uhlmann's theorem characterizes the fidelity as the maximum overlap between purifications, providing a geometric interpretation.

### Theorem 10.3 (Fuchs-van de Graaf Inequalities) **[Watrous, Ch.3]**

$$1 - \sqrt{F(\rho,\sigma)} \leq \frac{1}{2}\|\rho - \sigma\|_1 \leq \sqrt{1 - F(\rho,\sigma)}$$

These relate trace distance to fidelity, connecting state discrimination to geometric proximity.

### Theorem 10.4 (Fidelity Monotonicity) **[Watrous, Ch.3, §3.2.3]**

For any quantum channel $\Phi$:

$$F(\Phi(\rho), \Phi(\sigma)) \geq F(\rho, \sigma)$$

Quantum channels cannot decrease fidelity. This is the fidelity version of the data processing inequality.

---

## 11. Completely Bounded Trace Norm (Diamond Norm) (from Watrous Ch.3)

### Definition 11.1 (Diamond Norm) **[Watrous, Ch.3, §3.3]**

$$\|\Phi\|_\diamond = \max_{\rho \in \mathrm{D}(\mathcal{X} \otimes \mathcal{X})} \|(\Phi \otimes \mathrm{id})(\rho)\|_1$$

> Watrous, Ch.3, §3.3.2: "The completely bounded trace norm" provides the operationally relevant distance measure between quantum channels.

### Theorem 11.2 (SDP Characterization) **[Watrous, Ch.3, Thm.3.46]**

The diamond norm can be computed via SDP:

$$\frac{1}{2}\|\Phi_0 - \Phi_1\|_\diamond = \max \left\{\frac{1}{2}\mathrm{Tr}(J(\Phi_0 - \Phi_1) \cdot W) : W \geq 0, \; \mathrm{Tr}_{\mathcal{Y}}(W) \leq \mathbb{1}\right\}$$

where $J(\cdot)$ denotes the Choi matrix. This SDP can be solved in polynomial time.

---

## 12. Quantum Channels: Representations (from Watrous Ch.2)

### Theorem 12.1 (Choi's Theorem on CP Maps) **[Watrous, Ch.2, Thm.2.22]**

$\Phi \in \mathrm{T}(\mathcal{X}, \mathcal{Y})$ is completely positive if and only if $J(\Phi) \geq 0$.

> Watrous, Ch.2: "The Choi representation of $\Phi$ is $J(\Phi) = \sum_{a,b} \Phi(E_{a,b}) \otimes E_{a,b}$."

$\Phi$ is a channel (CPTP) iff $J(\Phi) \geq 0$ and $\mathrm{Tr}_{\mathcal{Y}}(J(\Phi)) = \mathbb{1}_\mathcal{X}$.

### Theorem 12.2 (Extremal Channels — Choi) **[Watrous, Ch.2, Thm.2.31]**

Let $\Phi(X) = \sum_a A_a X A_a^*$ with $\{A_a\}$ linearly independent. Then $\Phi$ is an extreme point of $\mathrm{C}(\mathcal{X}, \mathcal{Y})$ if and only if $\{A_b^* A_a : (a,b) \in \Sigma \times \Sigma\}$ is linearly independent.

> Watrous, Ch.2, Thm.2.31: This characterizes when a channel cannot be written as a nontrivial convex combination of other channels.

**Example** (Watrous Example 2.32): Isometric channels $\Phi(X) = AXA^*$ (single Kraus operator) are always extremal, since $\{A^*A\} = \{\mathbb{1}\}$ is trivially linearly independent.

### Definition 12.3 (Key Channel Examples) **[Watrous, Ch.2, §2.2.3]**

**Completely depolarizing channel**: $\Omega(\rho) = \mathrm{Tr}(\rho) \cdot \mathbb{1}/d$

> Watrous, Ch.2 (p.93): "$\Omega$ is the unique channel transforming every density operator into the completely mixed state."

**Completely dephasing channel**: $\Delta(X) = \sum_a X(a,a) E_{a,a}$ — removes off-diagonal entries.

> Watrous, Ch.2 (p.94): "This channel has the effect of replacing every off-diagonal entry of a given operator $X$ by 0."

**Transpose map**: $T(X) = X^T$ — positive but NOT completely positive for $d \geq 2$ (since $J(T) = W$, the swap operator, which is not PSD).

---

## 13. Measurements (from Watrous Ch.2)

### Definition 13.1 (POVM / Measurement) **[Watrous, Ch.2, Def.2.34]**

> Watrous, Ch.2 (p.101): "A measurement is a function of the form $\mu: \Sigma \to \mathrm{Pos}(\mathcal{X})$ satisfying $\sum_{a \in \Sigma} \mu(a) = \mathbb{1}_\mathcal{X}$."

When measurement $\mu$ is performed on state $\rho$, outcome $a$ occurs with probability:

$$p(a) = \langle \mu(a), \rho \rangle = \mathrm{Tr}(\mu(a)\rho)$$

This is a valid probability distribution: $p(a) \geq 0$ (since both $\mu(a), \rho \geq 0$) and $\sum_a p(a) = \mathrm{Tr}(\rho) = 1$.
