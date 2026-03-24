# Quantum Capacity and Coherent Information

> Source: Mark M. Wilde, *From Classical to Quantum Shannon Theory* (Cambridge University Press, 2nd edition, 2019)

---

## 1. Coherent Information

### Definition
**[Wilde, Ch.11, Definition 11.6.1]**

The coherent information of a bipartite state $\rho_{AB}$ is:
$$I(A\rangle B)_\rho \equiv H(B)_\rho - H(AB)_\rho = -H(A|B)_\rho$$

### Key Properties

**Negative of conditional entropy:**
$$I(A\rangle B)_\rho = -H(A|B)_\rho$$

**Duality of conditional entropy:**
**[Wilde, Ch.11, Exercise 11.6.3]**

For a purification $|\psi\rangle_{ABE}$ of $\rho_{AB}$:
$$I(A\rangle B)_\rho = H(B)_\psi - H(E)_\psi = H(A|E)_\psi$$

**Interpretation:** The coherent information measures the difference between Bob's uncertainty and the environment's uncertainty. Positive coherent information means Bob has more information than the environment.

### Bounds on Coherent Information
**[Wilde, Ch.11, Theorem 11.6.1]**

$$|H(A|B)_\rho| \leq \log \dim(\mathcal{H}_A)$$
Equivalently: $-\log d_A \leq I(A\rangle B)_\rho \leq \log d_A$.

**Proof:** Upper bound: $H(A|B) \leq H(A) \leq \log d_A$.
Lower bound: By duality, $H(A|B) = -H(A|E) \geq -H(A) \geq -\log d_A$.

### Examples

- **Maximally entangled state** $|\Phi\rangle_{AB} = d^{-1/2} \sum_i |i\rangle_A |i\rangle_B$:
  $I(A\rangle B)_\Phi = \log d$

- **Product state** $\rho_A \otimes \sigma_B$:
  $I(A\rangle B) = -H(A) \leq 0$

- **Separable states:** $I(A\rangle B)_\rho \leq 0$ always **[Wilde, Ch.11, Exercise 11.9.7]**

### Convexity of Coherent Information
**[Wilde, Ch.11, Exercise 11.10.5]**

The coherent information is *convex* (not concave!):
$$\sum_x p_X(x) I(A\rangle B)_{\rho^x} \geq I(A\rangle B)_\rho$$
where $\rho = \sum_x p_X(x) \rho^x$.

---

## 2. Quantum Data Processing Inequality

### Theorem: Data Processing for Coherent Information
**[Wilde, Ch.11, Theorem 11.9.1]**

Let $\rho_{AB} \in \mathcal{D}(\mathcal{H}_A \otimes \mathcal{H}_B)$ and $\mathcal{N}: B \to B'$ be a quantum channel. Then:
$$I(A\rangle B)_\rho \geq I(A\rangle B')_\sigma$$
where $\sigma_{AB'} = \mathcal{N}_{B \to B'}(\rho_{AB})$.

**Proof:**
1. $I(A\rangle B)_\rho = D(\rho_{AB} \| I_A \otimes \rho_B)$ **[Wilde, Ch.11, Exercise 11.8.3]**
2. $I(A\rangle B')_\sigma = D(\mathcal{N}(\rho_{AB}) \| \mathcal{N}(I_A \otimes \rho_B))$
3. By monotonicity of quantum relative entropy: $D(\rho_{AB} \| I_A \otimes \rho_B) \geq D(\mathcal{N}(\rho_{AB}) \| \mathcal{N}(I_A \otimes \rho_B))$

**Interpretation:** Quantum correlations (as measured by coherent information) can only decrease under local quantum processing on Bob's side.

### Theorem: Data Processing for Mutual Information
**[Wilde, Ch.11, Theorem 11.9.2]**

For channels $\mathcal{N}: A \to A'$ and $\mathcal{M}: B \to B'$:
$$I(A;B)_\rho \geq I(A';B')_\sigma$$
where $\sigma = (\mathcal{N} \otimes \mathcal{M})(\rho_{AB})$.

---

## 3. Channel Coherent Information

### Definition
**[Wilde, Ch.24, Theorem 24.3.1]**

The channel coherent information of $\mathcal{N}_{A' \to B}$ is:
$$Q(\mathcal{N}) \equiv \max_{\phi_{AA'}} I(A\rangle B)_\sigma$$
where $\sigma_{AB} = \mathcal{N}_{A' \to B}(\phi_{AA'})$ and the optimization is over pure bipartite input states.

### Equivalent Form
For an isometric extension $U^{\mathcal{N}}_{A' \to BE}$:
$$Q(\mathcal{N}) = \max_{\phi_{AA'}} [H(B)_\sigma - H(E)_\sigma]$$

This captures the no-cloning intuition: quantum capacity is determined by how much more information goes to Bob than to the environment.

---

## 4. The Quantum Capacity Theorem (LSD Theorem)

### Theorem
**[Wilde, Ch.24, Theorem 24.3.1]**

The quantum capacity of a quantum channel $\mathcal{N}_{A' \to B}$ is:
$$C_Q(\mathcal{N}) = Q_{\mathrm{reg}}(\mathcal{N})$$
where:
$$Q_{\mathrm{reg}}(\mathcal{N}) \equiv \lim_{k \to \infty} \frac{1}{k} Q(\mathcal{N}^{\otimes k})$$

Named after Lloyd, Shor, and Devetak who independently proved this result.

### Information-Processing Task: Entanglement Transmission
**[Wilde, Ch.24, Section 24.1]**

- Alice shares an arbitrary state $|\varphi\rangle_{RA_1}$ with an inaccessible reference $R$
- She encodes: $\mathcal{E}_{A_1 \to A'^n}$
- Transmits through $n$ uses of $\mathcal{N}$
- Bob decodes: $\mathcal{D}_{B^n \to B_1}$
- Goal: $\frac{1}{2}\|\varphi_{RA_1} - \omega_{RB_1}\|_1 \leq \varepsilon$ for all $|\varphi\rangle_{RA_1}$
- Rate: $Q = \frac{1}{n} \log \dim(\mathcal{H}_{A_1})$

### Direct Coding Theorem
**[Wilde, Ch.24, Section 24.4]**

**Strategy:** Construct coherent versions of private classical codes.

**Key steps:**
1. Start with a density operator $\rho_{A'} = \sum_x p_X(x) |\psi_x\rangle\langle\psi_x|_{A'}$ (spectral decomposition)
2. The isometric extension gives outputs: $|\psi_x\rangle_{BE} = U^{\mathcal{N}}|\psi_x\rangle_{A'}$
3. From the private classical capacity theorem, there exists a codebook $\{x^n(m,k)\}$ such that:
   - Bob can detect both $m$ and $k$: $\operatorname{Tr}\{\Lambda^{m,k}_{B^n} \rho^{x^n(m,k)}_{B^n}\} \geq 1-\varepsilon$
   - Eve learns nothing about $m$: $\|\frac{1}{|\mathcal{K}|}\sum_k \omega^{x^n(m,k)}_{E^n} - \omega^{\otimes n}\|_1 \leq \varepsilon$
4. **Coherent version:** Construct quantum codewords:
   $$|\phi_m\rangle_{A'^n} = \frac{1}{\sqrt{|\mathcal{K}|}} \sum_{k \in \mathcal{K}} e^{i\gamma_{m,k}} |\psi^{x^n(m,k)}\rangle_{A'^n}$$
5. The rate is:
   $$I(X;B)_\sigma - I(X;E)_\sigma = H(B)_\sigma - H(E)_\sigma = I(A\rangle B)$$

**The private information equals the coherent information:**
$$I(X;B) - I(X;E) = H(B) - H(B|X) - H(E) + H(E|X) = H(B) - H(E)$$
using $H(B|X) = H(E|X)$ (pure states conditioned on $X$).

### Converse Theorem
**[Wilde, Ch.24, Section 24.5]**

Uses:
- AFW continuity inequality
- Quantum data processing inequality
- Chain rule arguments

Shows that any achievable rate $Q$ satisfies $Q \leq Q_{\mathrm{reg}}(\mathcal{N})$.

---

## 5. No-Cloning Intuition
**[Wilde, Ch.24, Section 24.2]**

The no-cloning theorem provides the physical intuition:
- Every quantum channel has an isometric extension: Alice's input goes to both Bob and Eve
- If Eve can decode the quantum information, Bob cannot (no-cloning)
- The quantum code must find a subspace where information goes to Bob but NOT to Eve
- The coherent information $H(B) - H(E)$ precisely measures this asymmetry

**Example: Erasure channel** with parameter $\varepsilon = 1/2$
- Channel to Eve is identical to channel to Bob
- By no-cloning: $C_Q = 0$
- Coherent information confirms: $I(A\rangle B) = 0$ for $\varepsilon \geq 1/2$

---

## 6. Degradable Channels (Single-Letter Capacity)
**[Wilde, Ch.24, Section 24.6]**

A channel $\mathcal{N}_{A' \to B}$ is **degradable** if there exists a degrading channel $\mathcal{D}_{B \to E}$ such that the complementary channel $\mathcal{N}^c$ satisfies:
$$\mathcal{N}^c = \mathcal{D} \circ \mathcal{N}$$

For degradable channels:
$$C_Q(\mathcal{N}) = Q(\mathcal{N}) = \max_\phi I(A\rangle B)_\sigma$$
(No regularization needed!)

**Examples:**
- Quantum erasure channel ($\varepsilon < 1/2$): $C_Q = (1 - 2\varepsilon)\log d$
- Amplitude damping channel
- Dephasing channel

---

## 7. Entanglement-Assisted Classical Capacity

### Theorem: Bennett-Shor-Smolin-Thapliyal (BSST)
**[Wilde, Ch.21, Theorem 21.4.1]**

The entanglement-assisted classical capacity is:
$$C_{\mathrm{EA}}(\mathcal{N}) = I(\mathcal{N}) \equiv \max_{\varphi_{AA'}} I(A;B)_\rho$$
where $\rho_{AB} = \mathcal{N}_{A' \to B}(\varphi_{AA'})$.

**Key features:**
- **No regularization needed!** $I(\mathcal{N})$ itself is the capacity
- **Convex optimization:** Quantum mutual information is concave in the input state
- **The strongest known capacity result** in quantum Shannon theory

### Direct Coding Theorem
**[Wilde, Ch.21, Theorem 21.5.1]**

$$\langle \mathcal{N} \rangle + H(A)_\rho [qq] \geq I(A;B)_\rho [c \to c]$$

**Proof strategy:** Based on a generalized super-dense coding scheme:
1. Alice and Bob share $n$ copies of a pure entangled state $|\varphi\rangle_{AB}$
2. Alice applies random unitaries (generalized Pauli operators) to her shares
3. She transmits through the channel
4. Bob performs collective measurement on channel outputs + his entanglement shares

### Why No Regularization?
**[Wilde, Ch.21, Section 21.6]**

The converse proof uses:
1. Quantum data processing inequality
2. **Additivity of quantum mutual information** for channels: $I(\mathcal{N}_1 \otimes \mathcal{N}_2) = I(\mathcal{N}_1) + I(\mathcal{N}_2)$

This additivity (proven via chain rule + tensor product structure) is what eliminates the regularization.

### Quantum Feedback Does Not Help
**[Wilde, Ch.21, Section 21.6]**

$$C_{\mathrm{EA, feedback}}(\mathcal{N}) = C_{\mathrm{EA}}(\mathcal{N})$$

The entanglement-assisted classical capacity with a quantum feedback channel equals the entanglement-assisted classical capacity without feedback.

---

## 8. Hierarchy of Capacities

For a quantum channel $\mathcal{N}$:

$$C_Q(\mathcal{N}) \leq C(\mathcal{N}) \leq C_{\mathrm{EA}}(\mathcal{N})$$

- **Quantum capacity** $C_Q$: regularized coherent information (hardest to compute)
- **Classical capacity** $C$: regularized Holevo information (generally intractable)
- **EA classical capacity** $C_{\mathrm{EA}}$: mutual information (single-letter, computable!)

---

## 9. Superadditivity and Superactivation

### Superadditivity of Coherent Information
**[Wilde, Ch.24, Section 24.7]**

For the depolarizing channel, there exist cases where:
$$Q(\mathcal{N} \otimes \mathcal{N}) > 2 Q(\mathcal{N})$$

This means the best strategy uses *entangled* inputs across multiple channel uses.

### Superactivation of Quantum Capacity
**[Wilde, Ch.24, Section 24.7]**

There exist channels $\mathcal{N}_1, \mathcal{N}_2$ with:
$$C_Q(\mathcal{N}_1) = 0, \quad C_Q(\mathcal{N}_2) = 0, \quad C_Q(\mathcal{N}_1 \otimes \mathcal{N}_2) > 0$$

Two individually useless channels can transmit quantum information when used jointly. This is arguably the most surprising result in quantum Shannon theory.
