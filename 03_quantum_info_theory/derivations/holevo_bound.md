# Holevo Bound and Classical Capacity of Quantum Channels

> Source: Mark M. Wilde, *From Classical to Quantum Shannon Theory* (Cambridge University Press, 2nd edition, 2019)

---

## 1. Accessible Information and Holevo Information

### Setup
**[Wilde, Ch.11, Section 11.8.2]**

Alice prepares an ensemble $\mathcal{E} = \{p_X(x), \rho_B^x\}$ and hands the quantum system to Bob. Bob performs POVM $\{\Lambda_y\}$ to extract classical information.

- The conditional probability: $p_{Y|X}(y|x) = \operatorname{Tr}\{\Lambda_y \rho_x\}$
- The expected density operator: $\rho_B = \sum_x p_X(x) \rho_B^x$

### Definition: Accessible Information
**[Wilde, Ch.10, Section 10.8.2]**

$$I_{\mathrm{acc}}(\mathcal{E}) \equiv \max_{\{\Lambda_y\}} I(X;Y)$$

The maximum classical mutual information extractable by any measurement.

### Definition: Holevo Information
**[Wilde, Ch.11, Section 11.8.1]**

$$\chi(\mathcal{E}) \equiv H(\rho_B) - \sum_x p_X(x) H(\rho_B^x)$$

Equivalently, for the classical-quantum state $\sigma_{XB} = \sum_x p_X(x) |x\rangle\langle x|_X \otimes \rho_B^x$:
$$\chi(\mathcal{E}) = I(X;B)_\sigma$$

---

## 2. The Holevo Bound

### Theorem: Holevo Bound
**[Wilde, Ch.11, Exercise 11.8.4]**

$$I_{\mathrm{acc}}(\mathcal{E}) \leq \chi(\mathcal{E})$$

**Proof via Quantum Data Processing Inequality:**
1. Start with the classical-quantum state $\sigma_{XB} = \sum_x p_X(x) |x\rangle\langle x|_X \otimes \rho_B^x$
2. Bob's measurement $\{\Lambda_y\}$ is a quantum channel $\mathcal{M}: B \to Y$
3. By quantum data processing (Theorem 11.9.2): $I(X;B)_\sigma \geq I(X;Y)$
4. Since the measurement is a specific channel: $\chi(\mathcal{E}) = I(X;B)_\sigma \geq \max_{\{\Lambda_y\}} I(X;Y) = I_{\mathrm{acc}}(\mathcal{E})$

### Dimension Bound
**[Wilde, Ch.11, Exercise 11.8.5]**

$$\chi(\mathcal{E}) = I(X;B)_\sigma \leq \log\left[\min\{\dim(\mathcal{H}_X), \dim(\mathcal{H}_B)\}\right]$$

---

## 3. Holevo Information of a Channel

### Definition
**[Wilde, Ch.20, Eq. 20.4]**

The Holevo information of a quantum channel $\mathcal{N}$ is:
$$\chi(\mathcal{N}) \equiv \max_\rho I(X;B)$$
where the maximization is over classical-quantum states:
$$\rho_{XB} = \sum_x p_X(x) |x\rangle\langle x|_X \otimes \mathcal{N}_{A' \to B}(\psi_{A'}^x)$$

---

## 4. The HSW Theorem (Classical Capacity Theorem)

### Theorem: Holevo-Schumacher-Westmoreland
**[Wilde, Ch.20, Theorem 20.3.1]**

The classical capacity of a quantum channel is:
$$C(\mathcal{N}) = \chi_{\mathrm{reg}}(\mathcal{N})$$
where:
$$\chi_{\mathrm{reg}}(\mathcal{N}) \equiv \lim_{k \to \infty} \frac{1}{k} \chi(\mathcal{N}^{\otimes k})$$

### Direct Coding Theorem
**[Wilde, Ch.20, Section 20.3.1]**

**Statement:** The Holevo information $\chi(\mathcal{N})$ is an achievable rate for classical communication.

**Proof outline:**
1. **Random code generation:** Select $|\mathcal{M}| \approx 2^{n \chi(\mathcal{N})}$ classical codewords $\{x^n(m)\}$ from a pruned i.i.d. distribution supported on the typical set
2. **Quantum codewords:** $\rho^{x^n(m)} = \rho^{x_1(m)} \otimes \cdots \otimes \rho^{x_n(m)}$
3. **Encoding:** Alice transmits the quantum codeword through $n$ uses of the channel
4. **Collective decoding:** Bob performs a *collective* measurement (POVM) over all $n$ channel outputs simultaneously. This is the key quantum feature -- individual measurements are insufficient.
5. **Error analysis:** Uses the quantum packing lemma (Sen's non-commutative union bound or sequential decoding) to show that the average error vanishes for:
   $$|\mathcal{M}| \leq 2^{n[I(X;B) - \delta]}$$
   where $I(X;B)$ is evaluated on the classical-quantum channel output state

### Converse Theorem
**[Wilde, Ch.20, Section 20.3.2]**

**Statement:** Any achievable rate $C$ satisfies $C \leq \chi_{\mathrm{reg}}(\mathcal{N})$.

**Proof outline:**
1. Relate classical communication to randomness distribution
2. For an $(n, C, \varepsilon)$ code, the shared state $\omega_{MM'}$ satisfies $\frac{1}{2}\|\overline{\Phi}_{MM'} - \omega_{MM'}\|_1 \leq \varepsilon$
3. Apply the AFW continuity inequality: $H(M)_{\overline{\Phi}} \approx H(M)_\omega$ (up to $\varepsilon$ corrections)
4. Use quantum data processing inequality: $I(M;B^n) \leq I(M; B^n)$
5. Chain rule + memorylessness: $I(M;B^n) \leq \sum_i I(X_i; B_i) \leq n \chi(\mathcal{N}^{\otimes n}/n)$
6. Divide by $n$ and take $n \to \infty$

### Regularization Issue
**[Wilde, Ch.20, Section 20.1]**

The regularization $\chi_{\mathrm{reg}}$ is necessary in general because Hastings (2009) proved that the Holevo information can be **superadditive**: there exist channels $\mathcal{N}$ with:
$$\chi(\mathcal{N} \otimes \mathcal{N}) > 2\chi(\mathcal{N})$$

This means entangled inputs at the encoder can boost classical communication rates.

### Additive Channels (Single-Letter Capacity Known)
**[Wilde, Ch.20, Section 20.4]**

For the following channels, $\chi_{\mathrm{reg}}(\mathcal{N}) = \chi(\mathcal{N})$:
- **Entanglement-breaking channels** (including classical channels)
- **Quantum Hadamard channels** (complementary channel is entanglement-breaking)
- **Depolarizing channel:** $\mathcal{N}(\rho) = (1-p)\rho + p \cdot \pi$
- **Dephasing channel**
- **Erasure channel**

---

## 5. Naive vs. Optimal Strategy

### Naive Strategy (Product Measurements)
**[Wilde, Ch.20, Section 20.1]**

If Bob performs individual measurements on each channel output:
- Achievable rate: $I_{\mathrm{acc}}(\mathcal{N}) = \max_{\{p_X, \rho_x, \Lambda\}} I(X;Y)$
- This is generally *strictly less* than $\chi(\mathcal{N})$

### Optimal Strategy (Collective Measurements)
**[Wilde, Ch.20, Section 20.3.1]**

Bob performs a **collective measurement** over all $n$ channel outputs jointly:
- Achievable rate: $\chi(\mathcal{N})$ (single-letter for additive channels)
- Uses quantum-mechanical features at the decoder

### Key Insight
The gap $\chi(\mathcal{N}) - I_{\mathrm{acc}}(\mathcal{N})$ demonstrates a genuine quantum advantage in classical communication: collective quantum measurements can extract more classical information than any sequence of individual measurements.

---

## 6. Connections and Implications

### Relation to Quantum Mutual Information
For a classical-quantum state $\sigma_{XB}$:
$$\chi(\mathcal{E}) = I(X;B)_\sigma = H(B)_\sigma - H(B|X)_\sigma$$

### Holevo Bound as Consequence of SSA
The Holevo bound follows from:
1. Quantum data processing inequality for mutual information
2. Which follows from monotonicity of quantum relative entropy
3. Which is equivalent to strong subadditivity

### Upper Bound on Holevo Information
$$\chi(\mathcal{E}) \leq \min\{H(X), \log \dim(\mathcal{H}_B)\}$$
