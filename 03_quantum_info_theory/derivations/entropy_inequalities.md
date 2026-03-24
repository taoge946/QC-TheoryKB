# Quantum Entropy Inequalities

> Source: Mark M. Wilde, *From Classical to Quantum Shannon Theory* (Cambridge University Press, 2nd edition, 2019)

---

## 1. Von Neumann Entropy

### Definition
**[Wilde, Ch.11, Definition 11.1.1]**

For a quantum state $\rho_A \in \mathcal{D}(\mathcal{H}_A)$:
$$H(A)_\rho \equiv -\operatorname{Tr}\{\rho_A \log \rho_A\}$$

If $\rho_A = \sum_x p_X(x) |x\rangle\langle x|_A$ (spectral decomposition), then $H(A)_\rho = H(X)$ (Shannon entropy of eigenvalues).

### Properties
**[Wilde, Ch.11, Section 11.1.1]**

1. **Non-negativity:** $H(\rho) \geq 0$
2. **Minimum value:** $H(\rho) = 0$ iff $\rho$ is a pure state
3. **Maximum value:** $H(\rho) \leq \log d$ where $d = \dim(\mathcal{H})$, with equality for maximally mixed state
4. **Isometric invariance:** $H(\rho) = H(U\rho U^\dagger)$ for isometry $U$
5. **Concavity:** $H(\sum_x p_X(x) \rho_x) \geq \sum_x p_X(x) H(\rho_x)$ **[Wilde, Ch.11, Property 11.1.4]**
6. **Additivity:** $H(\rho_A \otimes \sigma_B) = H(\rho_A) + H(\sigma_B)$

### Alternate Characterization
**[Wilde, Ch.11, Theorem 11.1.1]**

$$H(\rho) = \min_{\{\Lambda_y\}} \left[-\sum_y \operatorname{Tr}\{\Lambda_y \rho\} \log \operatorname{Tr}\{\Lambda_y \rho\}\right]$$
where the minimum is over rank-one POVMs. The minimum is achieved by the eigenbasis measurement.

---

## 2. Conditional Quantum Entropy

### Definition
**[Wilde, Ch.11, Definition 11.5.1]**

$$H(A|B)_\rho \equiv H(AB)_\rho - H(B)_\rho$$

### Key Departure from Classical Theory
**[Wilde, Ch.11, Section 11.5.2]**

The conditional quantum entropy can be **negative**! For a maximally entangled state $|\Phi^+\rangle_{AB}$:
$$H(A|B)_\Phi = H(AB)_\Phi - H(B)_\Phi = 0 - 1 = -1$$

**Physical interpretation:** We can be more certain about the joint state of a quantum system than about any individual part. This is the informational signature of entanglement.

**Operational meaning (State Merging):** If $H(A|B) < 0$, Alice can transfer her share to Bob using *zero* qubits and they *gain* $|H(A|B)|$ ebits.

### Bounds
**[Wilde, Ch.11, Theorem 11.6.1]**

$$-\log d_A \leq H(A|B)_\rho \leq \log d_A$$

### Duality
**[Wilde, Ch.11, Exercise 11.6.3]**

For purification $|\psi\rangle_{ABE}$:
$$H(A|B)_\rho = -H(A|E)_\psi$$

---

## 3. Quantum Relative Entropy

### Definition
**[Wilde, Ch.11, Definition 11.8.1]**

$$D(\rho \| \sigma) \equiv \operatorname{Tr}\{\rho[\log \rho - \log \sigma]\}$$
if $\operatorname{supp}(\rho) \subseteq \operatorname{supp}(\sigma)$, and $+\infty$ otherwise.

### Expressing Other Entropies via Relative Entropy
**[Wilde, Ch.11, Exercises 11.8.2-11.8.4]**

- **Mutual information:** $I(A;B)_\rho = D(\rho_{AB} \| \rho_A \otimes \rho_B) = \min_{\sigma_B} D(\rho_{AB} \| \rho_A \otimes \sigma_B)$
- **Coherent information:** $I(A\rangle B)_\rho = D(\rho_{AB} \| I_A \otimes \rho_B) = \min_{\sigma_B} D(\rho_{AB} \| I_A \otimes \sigma_B)$
- **Conditional entropy:** $H(A|B)_\rho = -D(\rho_{AB} \| I_A \otimes \rho_B)$
- **CQMI:** $I(A;B|C)_\rho = D(\rho_{ABC} \| \omega_{ABC})$ where $\omega_{ABC} = 2^{\log \rho_{AC} + \log \rho_{BC} - \log \rho_C}$

---

## 4. Monotonicity of Quantum Relative Entropy

### Theorem
**[Wilde, Ch.11, Theorem 11.8.2]**

For $\rho \in \mathcal{D}(\mathcal{H})$, positive semi-definite $\sigma$, and quantum channel $\mathcal{N}$:
$$D(\rho \| \sigma) \geq D(\mathcal{N}(\rho) \| \mathcal{N}(\sigma))$$

**This is the most fundamental inequality in quantum information theory.** It is equivalent to strong subadditivity.

### Corollary: Non-Negativity
**[Wilde, Ch.11, Theorem 11.8.3]**

If $\operatorname{Tr}\{\sigma\} \leq 1$:
$$D(\rho \| \sigma) \geq 0$$
with equality iff $\rho = \sigma$.

**Proof:** Apply monotonicity with the trace-out channel:
$$D(\rho\|\sigma) \geq D(\operatorname{Tr}\{\rho\} \| \operatorname{Tr}\{\sigma\}) = \log\frac{1}{\operatorname{Tr}\{\sigma\}} \geq 0$$

---

## 5. Strong Subadditivity

### Theorem
**[Wilde, Ch.11, Theorem 11.10.1]**

For any tripartite state $\rho_{ABC}$:
$$I(A;B|C)_\rho \geq 0$$

### Equivalent Forms
**[Wilde, Ch.11, Exercise 11.10.3]**

1. $H(AC) + H(BC) \geq H(C) + H(ABC)$
2. $H(B|C) \geq H(B|AC)$ (conditioning on more cannot increase entropy)
3. $H(AB|C) \leq H(A|C) + H(B|C)$ (conditional subadditivity)

### Proof
**[Wilde, Ch.11, Theorem 11.10.1]**

Follows from monotonicity of quantum relative entropy. Express $I(A;B|C)_\rho = D(\rho_{ABC} \| \omega_{ABC})$ where $\omega_{ABC} = 2^{\log \rho_{AC} + \log \rho_{BC} - \log \rho_C}$, then apply non-negativity of quantum relative entropy.

**Historical note:** First proved by Lieb and Ruskai (1973). It is far more difficult than the classical version, which follows trivially from non-negativity of mutual information.

### Consequences
- **Subadditivity:** $H(A) + H(B) \geq H(AB)$
- **Araki-Lieb triangle inequality:** $|H(A) - H(B)| \leq H(AB)$ **[Wilde, Ch.11, Exercise 11.10.7]**
- **Conditioning reduces entropy:** $H(A) \geq H(A|B)$
- **Concavity of conditional entropy:** $\sum_x p(x) H(A|B)_{\rho^x} \leq H(A|B)_\rho$
- **Convexity of coherent information:** $\sum_x p(x) I(A\rangle B)_{\rho^x} \geq I(A\rangle B)_\rho$

---

## 6. Fannes-Audenaert Inequality (Continuity of Entropy)

### Theorem
**[Wilde, Ch.11, Theorem 11.10.2]**

Let $\rho, \sigma \in \mathcal{D}(\mathcal{H})$ with $\frac{1}{2}\|\rho - \sigma\|_1 \leq \varepsilon \in [0,1]$. Then:
$$|H(\rho) - H(\sigma)| \leq \varepsilon \log(\dim(\mathcal{H}) - 1) + h_2(\varepsilon)$$

**Proof outline:**
1. Let $\bar{\Delta}_\sigma$ be the completely dephasing channel in the eigenbasis of $\sigma$
2. $\bar{\Delta}_\sigma(\sigma) = \sigma$ and $H(\rho) \leq H(\bar{\Delta}_\sigma(\rho))$ (unital channels increase entropy)
3. So $H(\rho) - H(\sigma) \leq H(\bar{\Delta}_\sigma(\rho)) - H(\bar{\Delta}_\sigma(\sigma))$
4. The RHS is a classical problem: apply the Zhang-Audenaert inequality
5. Use monotonicity of trace distance: $\|\bar{\Delta}_\sigma(\rho) - \bar{\Delta}_\sigma(\sigma)\|_1 \leq \|\rho - \sigma\|_1$

### Optimal Fannes-Audenaert (Tight Version)
**[Wilde, Ch.11, Theorem 11.10.3]**

$$|H(\rho) - H(\sigma)| \leq T \log(\dim(\mathcal{H}) - 1) + h_2(T)$$
where $T = \frac{1}{2}\|\rho - \sigma\|_1$. This bound is **optimal** (saturated by specific states).

---

## 7. AFW Inequality (Continuity of Conditional Entropy)

### Theorem: Alicki-Fannes-Winter
**[Wilde, Ch.11, Theorem 11.10.4]**

Let $\rho_{AB}, \sigma_{AB} \in \mathcal{D}(\mathcal{H}_A \otimes \mathcal{H}_B)$ with $\frac{1}{2}\|\rho_{AB} - \sigma_{AB}\|_1 \leq \varepsilon$. Then:
$$|H(A|B)_\rho - H(A|B)_\sigma| \leq 2\varepsilon \log \dim(\mathcal{H}_A) + g_2(\varepsilon)$$
where $g_2(\varepsilon) = (1+\varepsilon)\log(1+\varepsilon) - \varepsilon \log \varepsilon$.

**Key advantage:** The bound depends only on $\dim(\mathcal{H}_A)$, not on $\dim(\mathcal{H}_B)$.

### AFW for Classical-Quantum States
**[Wilde, Ch.11, Theorem 11.10.4]**

For classical-quantum states:
- $|H(X|B)_\rho - H(X|B)_\sigma| \leq \varepsilon \log \dim(\mathcal{H}_X) + g_2(\varepsilon)$
- $|H(B|X)_\rho - H(B|X)_\sigma| \leq \varepsilon \log \dim(\mathcal{H}_B) + g_2(\varepsilon)$

### AFW Corollaries
**[Wilde, Ch.11, Exercises 11.10.5-11.10.6]**

- **For coherent information:** $|I(A\rangle B)_\rho - I(A\rangle B)_\sigma| \leq 2\varepsilon \log d_A + g_2(\varepsilon)$
- **For mutual information:** $|I(A;B)_\rho - I(A;B)_\sigma| \leq 3\varepsilon \log d_A + 2g_2(\varepsilon)$

**Importance:** The AFW inequality is the fundamental tool for proving converse theorems in quantum Shannon theory. It translates trace-distance error bounds into entropic bounds.

---

## 8. Pinsker's Inequality (Quantum Version)

### Theorem
**[Wilde, Ch.10, Theorem 10.7.1 and quantum extension]**

For quantum states:
$$D(\rho \| \sigma) \geq \frac{1}{2 \ln 2} \|\rho - \sigma\|_1^2$$

**Follows from** the classical Pinsker inequality + monotonicity of quantum relative entropy under a measurement channel.

---

## 9. Quantum Mutual Information

### Definition
**[Wilde, Ch.11, Definition 11.7.1]**

$$I(A;B)_\rho \equiv H(A)_\rho + H(B)_\rho - H(AB)_\rho = H(A) - H(A|B) = H(B) - H(B|A)$$

### Theorem: Non-Negativity
**[Wilde, Ch.11, Theorem 11.7.1]**

$$I(A;B)_\rho \geq 0$$

**Proof:** $I(A;B) = D(\rho_{AB} \| \rho_A \otimes \rho_B) \geq 0$ by non-negativity of quantum relative entropy.

### Dimension Bound
**[Wilde, Ch.11, Exercise 11.7.2]**

$$I(A;B)_\rho \leq 2 \log[\min\{d_A, d_B\}]$$

Note: The factor of 2 (vs. classical $\log \min\{|\mathcal{X}|, |\mathcal{Y}|\}$) reflects the stronger-than-classical correlations possible in quantum states. A maximally entangled state on two qubits has $I(A;B) = 2$ bits.

---

## 10. Recoverability Theorem

### Theorem
**[Wilde, Ch.12, Theorem 12.1.1]**

Given $\rho$, $\sigma$, and quantum channel $\mathcal{N}$, there exists a recovery channel $\mathcal{R}_{\sigma,\mathcal{N}}$ (depending only on $\sigma$ and $\mathcal{N}$) such that:
$$D(\rho\|\sigma) - D(\mathcal{N}(\rho)\|\mathcal{N}(\sigma)) \geq -\log F(\rho, (\mathcal{R}_{\sigma,\mathcal{N}} \circ \mathcal{N})(\rho))$$
and $(\mathcal{R}_{\sigma,\mathcal{N}} \circ \mathcal{N})(\sigma) = \sigma$.

**Implications:**
- Monotonicity of relative entropy as a corollary (since $-\log F \geq 0$)
- If relative entropy decreases little, recovery is approximately possible
- Strengthens strong subadditivity, joint convexity, and other inequalities

### Petz Recovery Map
**[Wilde, Ch.12, Definition 12.3.1]**

The recovery channel is based on the **Petz recovery map**:
$$\mathcal{P}_{\sigma,\mathcal{N}}(Q) = \sigma^{1/2} \mathcal{N}^\dagger([\mathcal{N}(\sigma)]^{-1/2} Q [\mathcal{N}(\sigma)]^{-1/2}) \sigma^{1/2}$$

The actual recovery channel is a **rotated Petz map** averaged over a continuous family of unitaries:
$$\mathcal{R}^t_{\sigma,\mathcal{N}} = \mathcal{U}_{\sigma,-t} \circ \mathcal{P}_{\sigma,\mathcal{N}} \circ \mathcal{U}_{\mathcal{N}(\sigma),t}$$
where $\mathcal{U}_{\sigma,t}(M) = \sigma^{it} M \sigma^{-it}$.

---

## 11. Joint Entropy of Pure Bipartite States

### Theorem
**[Wilde, Ch.11, Theorem 11.2.1]**

For a pure bipartite state $|\phi\rangle_{AB}$:
$$H(A)_\phi = H(B)_\phi, \qquad H(AB)_\phi = 0$$

**Proof:** Uses the Schmidt decomposition: $|\phi\rangle_{AB} = \sum_i \sqrt{\lambda_i} |i\rangle_A |i\rangle_B$. Both marginals have the same eigenvalues $\{\lambda_i\}$.

**Significance:** The joint entropy can be strictly less than either marginal entropy. This is impossible classically and reflects entanglement.

---

## 12. Summary of Key Inequalities

| Inequality | Statement | Reference |
|---|---|---|
| Non-neg. relative entropy | $D(\rho\|\sigma) \geq 0$ | [Wilde, Ch.11, Thm 11.8.3] |
| Monotonicity | $D(\rho\|\sigma) \geq D(\mathcal{N}(\rho)\|\mathcal{N}(\sigma))$ | [Wilde, Ch.11, Thm 11.8.2] |
| Strong subadditivity | $I(A;B\|C) \geq 0$ | [Wilde, Ch.11, Thm 11.10.1] |
| Subadditivity | $H(AB) \leq H(A) + H(B)$ | [Wilde, Ch.11, Cor 11.8.1] |
| Araki-Lieb | $|H(A) - H(B)| \leq H(AB)$ | [Wilde, Ch.11, Ex 11.10.7] |
| Fannes-Audenaert | $|H(\rho)-H(\sigma)| \leq T\log(d-1) + h_2(T)$ | [Wilde, Ch.11, Thm 11.10.3] |
| AFW | $|H(A\|B)_\rho - H(A\|B)_\sigma| \leq 2\varepsilon \log d_A + g_2(\varepsilon)$ | [Wilde, Ch.11, Thm 11.10.4] |
| Pinsker | $D(\rho\|\sigma) \geq \frac{1}{2\ln 2}\|\rho-\sigma\|_1^2$ | [Wilde, Ch.10, Thm 10.7.1] |
| DPI (coherent info) | $I(A\rangle B) \geq I(A\rangle B')$ under $B \to B'$ | [Wilde, Ch.11, Thm 11.9.1] |
| DPI (mutual info) | $I(A;B) \geq I(A';B')$ under $A\to A', B\to B'$ | [Wilde, Ch.11, Thm 11.9.2] |
| Recoverability | $D(\rho\|\sigma) - D(\mathcal{N}(\rho)\|\mathcal{N}(\sigma)) \geq -\log F(\rho, \mathcal{R}\circ\mathcal{N}(\rho))$ | [Wilde, Ch.12, Thm 12.1.1] |
