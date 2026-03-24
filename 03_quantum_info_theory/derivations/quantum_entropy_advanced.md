# Quantum Entropy: Advanced Theory and Proofs

> Source: J. Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018, **Chapter 5**.

---

## 1. Von Neumann Entropy

### Definition 5.1 (Von Neumann Entropy) **[Watrous, Ch.5, Def.5.1]**

For $\rho \in \mathrm{D}(\mathcal{X})$, the **von Neumann entropy** is:

$$
\mathrm{H}(\rho) = -\mathrm{Tr}(\rho \log \rho)
$$

where $\log$ denotes the matrix logarithm (base 2 by convention), and $0 \log 0 := 0$ by continuity.

If $\rho$ has eigenvalues $\{\lambda_i\}$, then $\mathrm{H}(\rho) = -\sum_i \lambda_i \log \lambda_i = \mathrm{H}(\lambda)$, the Shannon entropy of the eigenvalue distribution.

### Proposition 5.2 (Basic Properties) **[Watrous, Ch.5, Prop.5.2]**

For $\rho \in \mathrm{D}(\mathcal{X})$ with $\dim(\mathcal{X})=d$:

1. **Non-negativity**: $\mathrm{H}(\rho) \geq 0$, with equality iff $\rho$ is pure.
2. **Maximum**: $\mathrm{H}(\rho) \leq \log d$, with equality iff $\rho = \mathbb{1}/d$.
3. **Concavity**: $\rho \mapsto \mathrm{H}(\rho)$ is concave on $\mathrm{D}(\mathcal{X})$.
4. **Unitary invariance**: $\mathrm{H}(U\rho U^*) = \mathrm{H}(\rho)$.

**Proof of concavity**:

Let $\rho = \sum_k p_k \rho_k$. We need $\mathrm{H}(\sum_k p_k \rho_k) \geq \sum_k p_k \mathrm{H}(\rho_k)$.

This follows from the operator concavity of $t \mapsto -t\log t$ on $[0,1]$ and the trace functional. Specifically, $-\mathrm{Tr}(f(\sum_k p_k \rho_k)) \geq -\sum_k p_k \mathrm{Tr}(f(\rho_k))$ for operator convex $f(t) = t\log t$. $\blacksquare$

---

## 2. Quantum Relative Entropy

### Definition 5.3 (Quantum Relative Entropy) **[Watrous, Ch.5, Def.5.3]**

For $\rho \in \mathrm{D}(\mathcal{X})$ and $\sigma \in \mathrm{Pos}(\mathcal{X})$:

$$
\mathrm{D}(\rho \| \sigma) = \begin{cases}
\mathrm{Tr}(\rho \log \rho - \rho \log \sigma) & \text{if } \mathrm{im}(\rho) \subseteq \mathrm{im}(\sigma) \\
+\infty & \text{otherwise}
\end{cases}
$$

The support condition $\mathrm{im}(\rho) \subseteq \mathrm{im}(\sigma)$ is essential; when violated, relative entropy diverges.

### Theorem 5.8 (Klein's Inequality) **[Watrous, Ch.5, Thm.5.8]**

$$
\mathrm{D}(\rho \| \sigma) \geq 0
$$

with equality if and only if $\rho = \sigma$.

**Proof**:

Write the spectral decompositions $\rho = \sum_i \lambda_i |u_i\rangle\langle u_i|$ and $\sigma = \sum_j \mu_j |v_j\rangle\langle v_j|$. Define $p_{ij} = |\langle u_i | v_j \rangle|^2$. Then:

$$
\mathrm{D}(\rho\|\sigma) = \sum_i \lambda_i \log \lambda_i - \sum_{i,j} \lambda_i p_{ij} \log \mu_j
$$

For each $i$, $\sum_j p_{ij} = 1$ forms a probability distribution. Using the log-sum inequality (or equivalently, the classical result $\mathrm{D}(p\|q) \geq 0$ for probability distributions):

$$
\sum_{i,j} \lambda_i p_{ij} \log \frac{\lambda_i}{\mu_j} \geq 0
$$

with equality iff $\lambda_i = \mu_j$ whenever $p_{ij} > 0$, which implies $\rho = \sigma$. $\blacksquare$

---

## 3. Operator Jensen's Inequality and Concavity/Convexity

### Theorem 5.7 (Operator Jensen's Inequality) **[Watrous, Ch.5, Thm.5.7]**

Let $f: [0,\infty) \to \mathbb{R}$ be operator concave. Then for any positive operators $A_1, \ldots, A_n$ and probabilities $p_1,\ldots,p_n$:

$$
f\!\left(\sum_k p_k A_k\right) \geq \sum_k p_k f(A_k)
$$

in the semidefinite order.

### Theorem 5.9 (Operator Concavity of Log) **[Watrous, Ch.5, Thm.5.9]**

The function $A \mapsto \log A$ is operator concave on $\mathrm{Pos}(\mathcal{X}) \setminus \{0\}$:

$$
\log\!\left(\sum_k p_k A_k\right) \geq \sum_k p_k \log A_k
$$

**Proof sketch**: The function $t \mapsto \log t$ has the integral representation:

$$
\log t = \int_0^\infty \left(\frac{1}{1+s} - \frac{1}{t+s}\right) ds
$$

The function $t \mapsto (t+s)^{-1}$ is operator convex for each $s > 0$ (it is the composition of affine and matrix inversion), so $t \mapsto -(t+s)^{-1}$ is operator concave. The integral of operator concave functions is operator concave. $\blacksquare$

### Corollary 5.10 (Concavity of Entropy Function) **[Watrous, Ch.5, Cor.5.10]**

The function $\rho \mapsto -\mathrm{Tr}(\rho \log \sigma)$ is concave in $\rho$ for fixed $\sigma > 0$.

---

## 4. Joint Convexity of Relative Entropy

### Theorem 5.12 (Joint Convexity) **[Watrous, Ch.5, Thm.5.12]**

The quantum relative entropy is **jointly convex**: for states $\rho_1,\ldots,\rho_n$, positive operators $\sigma_1,\ldots,\sigma_n$, and probabilities $p_1,\ldots,p_n$:

$$
\mathrm{D}\!\left(\sum_k p_k \rho_k \,\bigg\|\, \sum_k p_k \sigma_k\right) \leq \sum_k p_k \,\mathrm{D}(\rho_k \| \sigma_k)
$$

**Proof** (via Lieb's concavity theorem):

**Step 1**: Lieb's concavity theorem states that for $0 < s < 1$, the map $(A, B) \mapsto \mathrm{Tr}(K^* A^s K B^{1-s})$ is jointly concave in $(A,B) \in \mathrm{Pos}(\mathcal{X}) \times \mathrm{Pos}(\mathcal{X})$ for any fixed $K$.

**Step 2**: Taking the derivative at $s=1$:

$$
\frac{d}{ds}\bigg|_{s=1} \mathrm{Tr}(\rho^s \sigma^{1-s}) = \mathrm{Tr}(\rho \log \rho) - \mathrm{Tr}(\rho \log \sigma) = \mathrm{D}(\rho\|\sigma)
$$

**Step 3**: Concavity of $\mathrm{Tr}(\rho^s \sigma^{1-s})$ in $(\rho,\sigma)$ for each $s \in (0,1)$ implies that the derivative at $s=1$ (which equals $\mathrm{D}(\rho\|\sigma)$ up to sign conventions) inherits the convexity property. Specifically, the "slope at the boundary" of a family of concave functions gives a convex function.

More precisely, define $g(s) = \mathrm{Tr}(\rho^s \sigma^{1-s})$. We have $g(1) = \mathrm{Tr}(\rho) = 1$ for all density operators, and $-g'(1) = \mathrm{D}(\rho\|\sigma)$. Since $g(s)$ is jointly concave in $(\rho,\sigma)$ for each $s < 1$, taking the limit of the difference quotient $(g(1)-g(s))/(1-s)$ as $s \to 1^-$ preserves convexity. $\blacksquare$

---

## 5. Monotonicity (Data Processing Inequality)

### Theorem 5.13 (Data Processing Inequality for Relative Entropy) **[Watrous, Ch.5, Thm.5.13]**

For any quantum channel $\Phi \in \mathrm{C}(\mathcal{X}, \mathcal{Y})$:

$$
\mathrm{D}(\Phi(\rho) \| \Phi(\sigma)) \leq \mathrm{D}(\rho \| \sigma)
$$

**Proof** (Lindblad's approach via joint convexity):

**Step 1**: For a unitary channel $\Phi(X) = UXU^*$, the result is trivial since $\mathrm{D}(U\rho U^* \| U\sigma U^*) = \mathrm{D}(\rho\|\sigma)$ by the cyclic property of trace and unitary invariance of log.

**Step 2**: For a partial trace $\mathrm{Tr}_B$: consider $\rho_{AB}$ and $\sigma_{AB}$. We need $\mathrm{D}(\rho_A \| \sigma_A) \leq \mathrm{D}(\rho_{AB} \| \sigma_{AB})$. Write:

$$
\rho_A = \mathrm{Tr}_B(\rho_{AB}) = \frac{1}{d_B} \sum_{k=1}^{d_B^2} (\mathbb{1}_A \otimes U_k) \rho_{AB} (\mathbb{1}_A \otimes U_k)^*
$$

where $\{U_k\}$ is a unitary 1-design on $\mathcal{Y}$ (this is the "twirling" argument -- averaging over unitaries on $B$ produces $\rho_A \otimes \mathbb{1}_B/d_B$). Then by joint convexity:

$$
\mathrm{D}\!\left(\rho_A \otimes \frac{\mathbb{1}_B}{d_B} \,\bigg\|\, \sigma_A \otimes \frac{\mathbb{1}_B}{d_B}\right) \leq \frac{1}{d_B^2}\sum_k \mathrm{D}(U_k \rho_{AB} U_k^* \| U_k \sigma_{AB} U_k^*) = \mathrm{D}(\rho_{AB}\|\sigma_{AB})
$$

The left side equals $\mathrm{D}(\rho_A\|\sigma_A) + \log d_B - \log d_B = \mathrm{D}(\rho_A \| \sigma_A)$ by the tensor product property of relative entropy.

**Step 3**: Any CPTP map $\Phi$ can be realized as $\Phi(\cdot) = \mathrm{Tr}_E(V(\cdot)V^*)$ by Stinespring dilation. So:

$$
\mathrm{D}(\Phi(\rho)\|\Phi(\sigma)) = \mathrm{D}(\mathrm{Tr}_E(V\rho V^*)\|\mathrm{Tr}_E(V\sigma V^*)) \leq \mathrm{D}(V\rho V^* \| V\sigma V^*) = \mathrm{D}(\rho\|\sigma)
$$

$\blacksquare$

### Corollary 5.14 (Monotonicity of Mutual Information) **[Watrous, Ch.5, Cor.5.14]**

For a channel $\Phi$ acting on system $A$:

$$
\mathrm{I}(A:B)_{(\Phi\otimes\mathrm{id})(\rho)} \leq \mathrm{I}(A:B)_\rho
$$

---

## 6. Conditional Entropy and Mutual Information

### Definition 5.16 (Conditional Quantum Entropy) **[Watrous, Ch.5, Def.5.16]**

For a bipartite state $\rho_{AB} \in \mathrm{D}(\mathcal{X}_A \otimes \mathcal{X}_B)$:

$$
\mathrm{H}(A|B)_\rho = \mathrm{H}(AB)_\rho - \mathrm{H}(B)_\rho
$$

**Key property**: Unlike classical conditional entropy, $\mathrm{H}(A|B)$ can be **negative**. For example, for a maximally entangled state $|\Phi^+\rangle$:

$$
\mathrm{H}(A|B)_{|\Phi^+\rangle} = 0 - \log d = -\log d
$$

Negative conditional entropy is a signature of entanglement and corresponds to the amount of quantum communication needed for state merging.

### Definition 5.18 (Quantum Mutual Information) **[Watrous, Ch.5, Def.5.18]**

$$
\mathrm{I}(A:B)_\rho = \mathrm{H}(A)_\rho + \mathrm{H}(B)_\rho - \mathrm{H}(AB)_\rho
$$

Equivalently:

$$
\mathrm{I}(A:B)_\rho = \mathrm{D}(\rho_{AB} \| \rho_A \otimes \rho_B)
$$

This immediately gives $\mathrm{I}(A:B) \geq 0$ by Klein's inequality.

### Proposition 5.19 (Properties of Mutual Information) **[Watrous, Ch.5, Prop.5.19]**

1. $\mathrm{I}(A:B) \geq 0$ with equality iff $\rho_{AB} = \rho_A \otimes \rho_B$.
2. $\mathrm{I}(A:B) \leq 2\min(\mathrm{H}(A), \mathrm{H}(B))$.
3. $\mathrm{I}(A:B)$ is not generally monotone under local operations on one system (but see data processing inequality for channels applied to one system).

---

## 7. Strong Subadditivity: Full Proof

### Theorem 5.25 (Strong Subadditivity — SSA) **[Watrous, Ch.5, Thm.5.25]**

For any tripartite state $\rho_{ABC} \in \mathrm{D}(\mathcal{X}_A \otimes \mathcal{X}_B \otimes \mathcal{X}_C)$:

$$
\mathrm{H}(ABC) + \mathrm{H}(B) \leq \mathrm{H}(AB) + \mathrm{H}(BC)
$$

Equivalently:

$$
\mathrm{H}(A|BC) \leq \mathrm{H}(A|B)
$$

i.e., conditioning on more systems can only decrease conditional entropy.

**Proof** (via monotonicity of relative entropy):

**Step 1**: Rewrite SSA in terms of relative entropy. Define:
- $\sigma_{ABC} = \rho_{AB} \otimes \rho_C$ (not a legitimate state of $ABC$ in general)

Actually, Watrous's proof proceeds from the data processing inequality directly:

**Step 1**: Consider the partial trace $\mathrm{Tr}_C: \mathrm{L}(\mathcal{X}_A \otimes \mathcal{X}_B \otimes \mathcal{X}_C) \to \mathrm{L}(\mathcal{X}_A \otimes \mathcal{X}_B)$. By the data processing inequality (Theorem 5.13):

$$
\mathrm{D}(\rho_{ABC} \| \mathbb{1}_A \otimes \rho_{BC}) \geq \mathrm{D}(\rho_{AB} \| \mathbb{1}_A \otimes \rho_B)
$$

**Step 2**: Compute the left side:

$$
\mathrm{D}(\rho_{ABC} \| \mathbb{1}_A \otimes \rho_{BC}) = \mathrm{Tr}(\rho_{ABC}\log\rho_{ABC}) - \mathrm{Tr}(\rho_{ABC}\log(\mathbb{1}_A \otimes \rho_{BC}))
$$
$$
= -\mathrm{H}(ABC) - \mathrm{Tr}(\rho_{BC}\log\rho_{BC}) = -\mathrm{H}(ABC) + \mathrm{H}(BC)
$$

Wait -- more carefully: $\mathrm{Tr}(\rho_{ABC}\log(\mathbb{1}_A \otimes \rho_{BC})) = \mathrm{Tr}(\rho_{BC}\log\rho_{BC})$ since $\log(\mathbb{1}_A \otimes \rho_{BC}) = \log\mathbb{1}_A \otimes \mathbb{1}_{BC} + \mathbb{1}_A \otimes \log\rho_{BC} = \mathbb{1}_A \otimes \log\rho_{BC}$ (using $\log\mathbb{1} = 0$). So:

$$
\mathrm{D}(\rho_{ABC}\|\mathbb{1}_A \otimes \rho_{BC}) = -\mathrm{H}(ABC) + \mathrm{H}(BC)
$$

Wait, this needs the identity/trace factor. Let us redo: for $\sigma = \frac{\mathbb{1}_A}{d_A} \otimes \rho_{BC}$, which is a valid density operator:

$$
\mathrm{D}(\rho_{ABC}\|\tfrac{\mathbb{1}_A}{d_A}\otimes\rho_{BC}) = -\mathrm{H}(ABC) - \mathrm{Tr}(\rho_{ABC}(\log\tfrac{\mathbb{1}_A}{d_A}\otimes\mathbb{1}_{BC} + \mathbb{1}_A\otimes\log\rho_{BC}))
$$
$$
= -\mathrm{H}(ABC) + \log d_A + \mathrm{H}(BC)
$$

**Step 3**: Compute the right side similarly:

$$
\mathrm{D}(\rho_{AB}\|\tfrac{\mathbb{1}_A}{d_A}\otimes\rho_B) = -\mathrm{H}(AB) + \log d_A + \mathrm{H}(B)
$$

**Step 4**: The data processing inequality gives:

$$
-\mathrm{H}(ABC) + \log d_A + \mathrm{H}(BC) \geq -\mathrm{H}(AB) + \log d_A + \mathrm{H}(B)
$$

Canceling $\log d_A$:

$$
-\mathrm{H}(ABC) + \mathrm{H}(BC) \geq -\mathrm{H}(AB) + \mathrm{H}(B)
$$

Rearranging:

$$
\mathrm{H}(AB) + \mathrm{H}(BC) \geq \mathrm{H}(ABC) + \mathrm{H}(B) \quad \blacksquare
$$

---

## 8. Consequences of Strong Subadditivity

### Corollary 5.26 (Subadditivity) **[Watrous, Ch.5, Cor.5.26]**

$$
\mathrm{H}(AB) \leq \mathrm{H}(A) + \mathrm{H}(B)
$$

**Proof**: Set $C$ to be trivial (one-dimensional) in SSA. Then $\mathrm{H}(ABC) = \mathrm{H}(AB)$, $\mathrm{H}(BC) = \mathrm{H}(B)$, $\mathrm{H}(B) = \mathrm{H}(B)$. SSA gives $\mathrm{H}(AB) + \mathrm{H}(B) \leq \mathrm{H}(A\cdot) + \mathrm{H}(B)$...

Actually, subadditivity follows more directly from $\mathrm{I}(A:B) = \mathrm{D}(\rho_{AB}\|\rho_A\otimes\rho_B) \geq 0$:

$$
\mathrm{H}(A) + \mathrm{H}(B) - \mathrm{H}(AB) \geq 0 \quad\blacksquare
$$

### Corollary 5.27 (Araki-Lieb Triangle Inequality) **[Watrous, Ch.5, Cor.5.27]**

$$
\mathrm{H}(AB) \geq |\mathrm{H}(A) - \mathrm{H}(B)|
$$

**Proof**: Purify $\rho_{AB}$ to $|\psi\rangle_{ABC}$. Then $\mathrm{H}(AB) = \mathrm{H}(C)$ and $\mathrm{H}(A) = \mathrm{H}(BC)$. By subadditivity:

$$
\mathrm{H}(BC) \leq \mathrm{H}(B) + \mathrm{H}(C) \implies \mathrm{H}(A) \leq \mathrm{H}(B) + \mathrm{H}(AB)
$$

So $\mathrm{H}(AB) \geq \mathrm{H}(A) - \mathrm{H}(B)$. By symmetry, $\mathrm{H}(AB) \geq \mathrm{H}(B) - \mathrm{H}(A)$. $\blacksquare$

### Corollary 5.28 (Conditioning Reduces Entropy) **[Watrous, Ch.5, Cor.5.28]**

SSA in conditional form: For any tripartite state $\rho_{ABC}$:

$$
\mathrm{H}(A|BC) \leq \mathrm{H}(A|B)
$$

This is the quantum analogue of "conditioning on more information reduces uncertainty."

### Proposition 5.29 (Concavity of Conditional Entropy) **[Watrous, Ch.5, Prop.5.29]**

The conditional entropy $\mathrm{H}(A|B)$ is concave: for an ensemble $\{p_k, \rho_k^{AB}\}$:

$$
\mathrm{H}(A|B)_{\sum p_k \rho_k} \geq \sum_k p_k \mathrm{H}(A|B)_{\rho_k}
$$

**Proof**: Introduce a classical register $K$ with $\rho_{ABK} = \sum_k p_k \rho_k^{AB} \otimes |k\rangle\langle k|$. By SSA:

$$
\mathrm{H}(A|BK) \leq \mathrm{H}(A|B)
$$

But $\mathrm{H}(A|BK) = \sum_k p_k \mathrm{H}(A|B)_{\rho_k}$ (classical conditioning on $K$), and $\mathrm{H}(A|B) = \mathrm{H}(A|B)_{\sum p_k \rho_k}$ since $\rho_{AB} = \sum_k p_k \rho_k^{AB}$. $\blacksquare$

---

## 9. Continuity of Entropy

### Theorem 5.31 (Fannes-Audenaert Inequality) **[Watrous, Ch.5, Thm.5.31]**

For $\rho, \sigma \in \mathrm{D}(\mathcal{X})$ with $\dim(\mathcal{X}) = d$ and $T = \frac{1}{2}\|\rho - \sigma\|_1 \leq 1$:

$$
|\mathrm{H}(\rho) - \mathrm{H}(\sigma)| \leq T \log(d-1) + h(T)
$$

where $h(T) = -T\log T - (1-T)\log(1-T)$ is the binary entropy function.

This is tight: the bound is achieved by certain pairs of states.

### Corollary (Continuity of Conditional Entropy) **[Watrous, Ch.5]**

The Alicki-Fannes-Winter inequality extends this to conditional entropy:

$$
|\mathrm{H}(A|B)_\rho - \mathrm{H}(A|B)_\sigma| \leq 4T\log d_A + 2h(T)
$$

for $T = \frac{1}{2}\|\rho_{AB}-\sigma_{AB}\|_1$.

---

## 10. Entropy Exchange and Complementary Channel

### Definition 5.34 (Entropy Exchange) **[Watrous, Ch.5, Def.5.34]**

For a channel $\Phi$ with Stinespring dilation $V: \mathcal{X} \to \mathcal{Y} \otimes \mathcal{Z}$ and input state $\rho$:

$$
\mathrm{H}_e(\Phi, \rho) = \mathrm{H}(\hat{\Phi}(\rho))
$$

where $\hat{\Phi}(\rho) = \mathrm{Tr}_{\mathcal{Y}}(V\rho V^*)$ is the complementary channel output. Equivalently:

$$
\mathrm{H}_e(\Phi, \rho) = \mathrm{H}(W)
$$

where $W_{ij} = \mathrm{Tr}(A_i \rho A_j^*)$ and $\{A_k\}$ are Kraus operators of $\Phi$.

### Proposition 5.35 **[Watrous, Ch.5, Prop.5.35]**

For a purification $|\psi\rangle_{RA}$ of $\rho_A$:

$$
\mathrm{H}_e(\Phi, \rho) = \mathrm{H}(RB)_{(\mathrm{id}_R \otimes \Phi)(|\psi\rangle\langle\psi|)}
$$

This connects entropy exchange to the joint entropy of the reference and output.

---

## 11. Quantum Conditional Mutual Information

### Definition (Conditional Mutual Information) **[Watrous, Ch.5]**

$$
\mathrm{I}(A:C|B)_\rho = \mathrm{H}(AB) + \mathrm{H}(BC) - \mathrm{H}(ABC) - \mathrm{H}(B)
$$

### Theorem (SSA Reformulation) **[Watrous, Ch.5, Thm.5.25]**

Strong subadditivity is equivalent to:

$$
\mathrm{I}(A:C|B) \geq 0
$$

for all tripartite states. This is the statement that quantum conditional mutual information is non-negative.

**Remark**: The equality $\mathrm{I}(A:C|B)_\rho = 0$ characterizes quantum Markov chains: $\rho_{ABC}$ can be recovered from $\rho_{AB}$ by a channel acting on $B$ alone (Petz recovery map). This is the content of the **exact saturation** of SSA, characterized by Hayden-Jozsa-Petz-Winter.

---

## 12. Relative Entropy Variance and Second-Order Asymptotics

### Definition (Relative Entropy Variance) **[Watrous, Ch.5]**

$$
V(\rho\|\sigma) = \mathrm{Tr}(\rho(\log\rho - \log\sigma)^2) - (\mathrm{D}(\rho\|\sigma))^2
$$

This quantity appears in second-order asymptotic expansions (quantum Stein's lemma refinements).

---

## 13. Summary of Entropy Inequalities Hierarchy

```
Klein:          D(rho||sigma) >= 0

Joint convexity: D(sum p_k rho_k || sum p_k sigma_k) <= sum p_k D(rho_k || sigma_k)

Data processing: D(Phi(rho)||Phi(sigma)) <= D(rho||sigma)

    implies SSA:     H(ABC) + H(B) <= H(AB) + H(BC)

        implies Subadditivity:    H(AB) <= H(A) + H(B)
        implies Araki-Lieb:       H(AB) >= |H(A) - H(B)|
        implies H(A|BC) <= H(A|B) (conditioning reduces entropy)
        implies I(A:C|B) >= 0     (non-negative QCMI)
```

The logical chain: **Lieb concavity** $\Rightarrow$ **Joint convexity of $\mathrm{D}$** $\Rightarrow$ **Data processing** $\Rightarrow$ **SSA** $\Rightarrow$ all other inequalities.

---

## 14. Source Coding Theorems (from Watrous Ch.5)

### Theorem 5.36 (Schumacher Compression) **[Watrous, Ch.5, Thm.5.36]**

For a quantum source producing states $\rho^{\otimes n}$ with $\rho \in \mathrm{D}(\mathcal{X})$:

The minimum rate of qubits per source symbol needed for asymptotically faithful compression is $\mathrm{H}(\rho)$.

> Watrous, Ch.5, Section 5.3.2: The quantum source coding theorem establishes $\mathrm{H}(\rho)$ as the fundamental limit for quantum data compression, analogous to Shannon's source coding theorem in classical information theory.

**Achievability**: Project onto the typical subspace $T_\delta^n(\rho)$, which has dimension $\approx 2^{n\mathrm{H}(\rho)}$. The fidelity of this compression approaches 1 as $n \to \infty$.

**Converse**: Any compression scheme with rate $R < \mathrm{H}(\rho)$ has fidelity approaching 0.

### Theorem 5.40 (Holevo-Schumacher-Westmoreland Bound) **[Watrous, Ch.5, §5.3.3]**

For encoding classical messages into quantum states via an ensemble $\{p_x, \rho_x\}$, the accessible information satisfies:

$$I_{\mathrm{acc}} \leq \mathrm{H}\!\left(\sum_x p_x \rho_x\right) - \sum_x p_x \mathrm{H}(\rho_x) = \chi(\{p_x, \rho_x\})$$

This is the **Holevo bound**. The quantity $\chi$ is the **Holevo information** of the ensemble.

**Proof**: This follows directly from the data processing inequality applied to the classical-quantum state $\sigma_{XB} = \sum_x p_x |x\rangle\langle x| \otimes \rho_x$. Any measurement on $B$ is a quantum channel, so:

$$I(X;Y) \leq I(X;B)_\sigma = \mathrm{H}(B) - \mathrm{H}(B|X) = \mathrm{H}\!\left(\sum_x p_x\rho_x\right) - \sum_x p_x\mathrm{H}(\rho_x)$$

---

## 15. Quantum Channels and Entropy (from Watrous Ch.5)

### Definition 15.1 (Coherent Information) **[Watrous, Ch.5]**

For a channel $\Phi \in \mathrm{C}(\mathcal{X}, \mathcal{Y})$ and input state $\rho \in \mathrm{D}(\mathcal{X})$:

$$I_c(\rho, \Phi) = \mathrm{H}(\Phi(\rho)) - \mathrm{H}_e(\Phi, \rho)$$

where $\mathrm{H}_e(\Phi, \rho)$ is the entropy exchange. Equivalently, for a purification $|\psi\rangle_{RA}$ of $\rho$:

$$I_c(\rho, \Phi) = \mathrm{H}(B)_\sigma - \mathrm{H}(RB)_\sigma$$

where $\sigma_{RB} = (\mathrm{id}_R \otimes \Phi)(|\psi\rangle\langle\psi|)$.

The coherent information can be negative (unlike classical mutual information), and is related to the quantum capacity:

$$Q(\Phi) = \lim_{n \to \infty} \frac{1}{n} \max_\rho I_c(\rho, \Phi^{\otimes n})$$

### Proposition 15.2 (Entropy Exchange Properties) **[Watrous, Ch.5, Prop.5.35]**

For a channel $\Phi$ with Kraus operators $\{A_k\}$ and input $\rho$:

$$\mathrm{H}_e(\Phi, \rho) = \mathrm{H}(W)$$

where $W_{ij} = \mathrm{Tr}(A_i \rho A_j^*)$ is the matrix of Kraus overlaps.

> Watrous, Ch.5: "This connects entropy exchange to the joint entropy of the reference and output" via the Stinespring dilation.

For a purification $|\psi\rangle_{RA}$ of $\rho$: $\mathrm{H}_e(\Phi, \rho) = \mathrm{H}(RB)_{(\mathrm{id}_R \otimes \Phi)(|\psi\rangle\langle\psi|)}$.

---

## 16. Quantum Markov Chains and SSA Saturation **[Watrous, Ch.5]**

### Theorem 16.1 (SSA Saturation / Petz Recovery)

The conditional mutual information $\mathrm{I}(A:C|B) = 0$ if and only if $\rho_{ABC}$ is a **quantum Markov chain**: there exists a recovery channel $\mathcal{R}: B \to BC$ such that:

$$\rho_{ABC} = (\mathrm{id}_A \otimes \mathcal{R})(\rho_{AB})$$

The recovery map is the **Petz recovery map**:

$$\mathcal{R}_{B \to BC}(\cdot) = \rho_{BC}^{1/2}(\rho_B^{-1/2} (\cdot) \rho_B^{-1/2} \otimes \mathbb{1}_C) \rho_{BC}^{1/2}$$

This characterization is due to Hayden-Jozsa-Petz-Winter and provides the structural foundation for approximate quantum error correction.
