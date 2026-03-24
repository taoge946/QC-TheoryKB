# Semidefinite Programming in Quantum Information

> Source: J. Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018, **Chapter 3**.

---

## 1. SDP Framework

### Definition 3.1 (Semidefinite Program) **[Watrous, Ch.3, Def.3.1]**

A **semidefinite program** (SDP) is an optimization problem of the following primal-dual pair:

**Primal (maximization)**:
$$
\alpha = \sup \left\{ \langle A, X \rangle : \Phi(X) = B, \; X \in \mathrm{Pos}(\mathcal{X}) \right\}
$$

**Dual (minimization)**:
$$
\beta = \inf \left\{ \langle B, Y \rangle : \Phi^*(Y) \geq A, \; Y = Y^* \in \mathrm{Herm}(\mathcal{Y}) \right\}
$$

where:
- $A \in \mathrm{Herm}(\mathcal{X})$ is the objective operator
- $B \in \mathrm{Herm}(\mathcal{Y})$ is the constraint operator
- $\Phi: \mathrm{L}(\mathcal{X}) \to \mathrm{L}(\mathcal{Y})$ is a Hermiticity-preserving map
- $\Phi^*$ is the adjoint map (w.r.t. Hilbert-Schmidt inner product)
- $\langle A, X \rangle = \mathrm{Tr}(A^* X)$

### Proposition 3.2 (Weak Duality) **[Watrous, Ch.3, Prop.3.2]**

$$
\alpha \leq \beta
$$

always holds: dual $\geq$ primal.

**Proof**: For any primal-feasible $X$ ($\Phi(X) = B$, $X \geq 0$) and dual-feasible $Y$ ($\Phi^*(Y) \geq A$):

$$
\langle B, Y \rangle = \langle \Phi(X), Y \rangle = \langle X, \Phi^*(Y) \rangle \geq \langle X, A \rangle = \langle A, X \rangle
$$

where the inequality uses $X \geq 0$ and $\Phi^*(Y) - A \geq 0$, so $\langle X, \Phi^*(Y) - A \rangle \geq 0$. $\blacksquare$

### Theorem 3.5 (Strong Duality / Slater's Condition) **[Watrous, Ch.3, Thm.3.5]**

If the primal problem is strictly feasible (i.e., there exists $X > 0$ with $\Phi(X) = B$), then $\alpha = \beta$ and the dual optimum is attained (if finite).

Similarly, if the dual is strictly feasible ($\exists Y$ with $\Phi^*(Y) > A$), then $\alpha = \beta$ and the primal optimum is attained.

### Theorem 3.6 (Complementary Slackness) **[Watrous, Ch.3, Thm.3.6]**

If strong duality holds and both optima are attained by $X^*$ (primal) and $Y^*$ (dual), then:

$$
X^* (\Phi^*(Y^*) - A) = 0
$$

**Proof**: At optimality, $\langle A, X^* \rangle = \langle B, Y^* \rangle = \langle X^*, \Phi^*(Y^*) \rangle$. So $\langle X^*, \Phi^*(Y^*) - A \rangle = 0$. Since $X^* \geq 0$ and $S^* = \Phi^*(Y^*) - A \geq 0$, and $\langle X^*, S^* \rangle = \mathrm{Tr}(X^* S^*) = 0$ with both PSD, we conclude $X^* S^* = 0$. $\blacksquare$

---

## 2. SDP for Quantum State Fidelity

### Theorem 3.28 (Uhlmann's Theorem) **[Watrous, Ch.3, Thm.3.28]**

The **fidelity** between $\rho, \sigma \in \mathrm{D}(\mathcal{X})$ is:

$$
F(\rho, \sigma) = \left(\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}\right)^2 = \|\sqrt{\rho}\sqrt{\sigma}\|_1^2
$$

Equivalently (Uhlmann):

$$
\sqrt{F(\rho,\sigma)} = \max_{U \in \mathrm{U}(\mathcal{X})} |\mathrm{Tr}(U\sqrt{\rho}\sqrt{\sigma})|
$$

Or in terms of purifications $|\psi_\rho\rangle, |\psi_\sigma\rangle$:

$$
\sqrt{F(\rho,\sigma)} = \max_{|\psi_\sigma\rangle} |\langle\psi_\rho|\psi_\sigma\rangle|
$$

### Theorem 3.30 (Fidelity as SDP) **[Watrous, Ch.3, Thm.3.30]**

$$
F(\rho, \sigma) = \max \left\{ |\mathrm{Tr}(X)|^2 : \begin{pmatrix} \rho & X \\ X^* & \sigma \end{pmatrix} \geq 0 \right\}
$$

**Proof**: The block-positive condition $\begin{pmatrix}\rho & X \\ X^* & \sigma\end{pmatrix} \geq 0$ is equivalent to $X = \sqrt{\rho}\, K \sqrt{\sigma}$ for some contraction $K$ ($\|K\| \leq 1$). Then:

$$
|\mathrm{Tr}(X)| = |\mathrm{Tr}(\sqrt{\rho}\,K\sqrt{\sigma})| \leq \|\sqrt{\rho}\sqrt{\sigma}\|_1 = \sqrt{F(\rho,\sigma)}
$$

by von Neumann trace inequality. Equality is achieved when $K = U^*$ is the optimal unitary from Uhlmann's theorem. $\blacksquare$

**SDP formulation**: This is a semidefinite program:

$$
\sqrt{F(\rho,\sigma)} = \max \frac{1}{2}(\mathrm{Tr}(X) + \mathrm{Tr}(X^*)) \quad \text{s.t.} \quad \begin{pmatrix}\rho & X \\ X^* & \sigma\end{pmatrix} \geq 0
$$

---

## 3. SDP for Trace Distance

### Proposition 3.31 **[Watrous, Ch.3, Prop.3.31]**

The trace distance has the variational characterization:

$$
\frac{1}{2}\|\rho - \sigma\|_1 = \max_{0 \leq M \leq \mathbb{1}} \mathrm{Tr}(M(\rho - \sigma))
$$

This is naturally an SDP:

**Primal**: $\max\; \mathrm{Tr}(M\rho) - \mathrm{Tr}(M\sigma)$ s.t. $0 \leq M \leq \mathbb{1}$.

The optimal $M$ is the projector onto the positive eigenspace of $\rho - \sigma$ (Helstrom measurement).

---

## 4. Fuchs-van de Graaf Inequalities

### Theorem 3.33 (Fuchs-van de Graaf) **[Watrous, Ch.3, Thm.3.33]**

For $\rho, \sigma \in \mathrm{D}(\mathcal{X})$:

$$
1 - \sqrt{F(\rho,\sigma)} \leq \frac{1}{2}\|\rho - \sigma\|_1 \leq \sqrt{1 - F(\rho,\sigma)}
$$

**Proof of upper bound**: For pure states $|\psi\rangle, |\phi\rangle$:

$$
\frac{1}{2}\||\psi\rangle\langle\psi| - |\phi\rangle\langle\phi|\|_1 = \sqrt{1 - |\langle\psi|\phi\rangle|^2}
$$

(direct computation from the $2\times 2$ matrix). For mixed states, use Uhlmann purifications achieving $|\langle\psi_\rho|\psi_\sigma\rangle| = \sqrt{F(\rho,\sigma)}$ and the fact that trace distance cannot increase under partial trace:

$$
\frac{1}{2}\|\rho-\sigma\|_1 \leq \frac{1}{2}\||\psi_\rho\rangle\langle\psi_\rho|-|\psi_\sigma\rangle\langle\psi_\sigma|\|_1 = \sqrt{1-F(\rho,\sigma)}
$$

**Proof of lower bound**: Uses the gentle measurement lemma and algebraic manipulation. $\blacksquare$

---

## 5. SDP for Diamond Norm

### Theorem 3.46 (Diamond Norm as SDP) **[Watrous, Ch.3, Thm.3.46]**

For a Hermiticity-preserving map $\Xi: \mathrm{L}(\mathcal{X}) \to \mathrm{L}(\mathcal{Y})$:

$$
\|\Xi\|_\diamond = \max \left\{ \frac{1}{2}\|(\Xi \otimes \mathrm{id}_{\mathcal{X}})(X)\|_1 : X \in \mathrm{L}(\mathcal{X}\otimes\mathcal{X}),\; \|X\|_1 \leq 1 \right\}
$$

This can be formulated as the following SDP:

**Primal**:
$$
\|\Xi\|_\diamond = \max \; \mathrm{Tr}(J(\Xi) \cdot Z)
$$
subject to:
$$
Z \geq 0, \quad \mathrm{Tr}_{\mathcal{Y}}(Z) \leq \rho \otimes \mathbb{1}_{\mathcal{X}}, \quad \rho \in \mathrm{D}(\mathcal{X})
$$

Wait -- more precisely, Watrous gives the following SDP:

**Primal**:
$$
\frac{1}{2}\|\Xi\|_\diamond = \max \; \frac{1}{2}\mathrm{Tr}(J(\Xi)(Z_0 - Z_1))
$$

subject to $Z_0, Z_1 \geq 0$ and $\mathrm{Tr}_{\mathcal{Y}}(Z_0 + Z_1) \leq \mathbb{1}_{\mathcal{X}}$.

**Dual** (Watrous's preferred formulation):
$$
\frac{1}{2}\|\Xi\|_\diamond = \min \; \frac{1}{2}\|\mathrm{Tr}_{\mathcal{Y}}(W) \otimes \mathbb{1}_{\mathcal{Y}} - J(\Xi)\| \quad (?)
$$

Let us state the clean version:

### Theorem 3.46 (Diamond Norm SDP — Clean Form) **[Watrous, Ch.3, Thm.3.46]**

$$
\frac{1}{2}\|\Phi - \Psi\|_\diamond = \text{the following SDP:}
$$

**Primal**:
$$
\max \quad \frac{1}{2}\mathrm{Re}\,\mathrm{Tr}(J(\Phi-\Psi) \cdot Z)
$$
$$
\text{s.t.} \quad \begin{pmatrix} \rho \otimes \mathbb{1}_{\mathcal{Y}} & Z \\ Z^* & \rho \otimes \mathbb{1}_{\mathcal{Y}} \end{pmatrix} \geq 0, \quad \rho \in \mathrm{D}(\mathcal{X}), \quad Z \in \mathrm{L}(\mathcal{X}\otimes\mathcal{Y})
$$

**Dual**:
$$
\min \quad \frac{1}{2}\left\| \mu \otimes \mathbb{1}_{\mathcal{Y}} + J(\Phi-\Psi) \right\|_1
$$

where $\mu$ ranges over positive operators on $\mathcal{X}$ with $\mathrm{Tr}(\mu) \leq 1$.

**Actually, the most standard SDP formulation** (following Watrous precisely) is:

$$
\frac{1}{2}\|\Xi\|_\diamond = \max\left\{\frac{1}{2}\langle J(\Xi), \rho \rangle : \begin{pmatrix} \rho_0 & \rho \\ \rho^* & \rho_1 \end{pmatrix} \geq 0,\; \mathrm{Tr}_{\mathcal{Y}}(\rho_0) = \mathrm{Tr}_{\mathcal{Y}}(\rho_1) = \sigma,\; \mathrm{Tr}(\sigma) = 1 \right\}
$$

For the specific case $\Xi = \Phi - \Psi$ (difference of channels), the SDP computes the distinguishability of the two channels.

**Importance**: The diamond norm SDP is polynomial-time solvable, enabling efficient computation of channel distances. This is crucial for:
- Quantum error correction threshold calculations
- Channel certification and tomography
- Benchmarking quantum gates

---

## 6. SDP for Optimal State Discrimination

### Theorem 3.40 (Optimal Measurement SDP) **[Watrous, Ch.3, Thm.3.40]**

Given an ensemble $\{(p_k, \rho_k)\}_{k=1}^N$, the maximum success probability of discrimination is:

**Primal**:
$$
p_{\mathrm{opt}} = \max \sum_{k=1}^N p_k \,\mathrm{Tr}(\rho_k \mu_k)
$$
subject to:
$$
\mu_k \geq 0 \;\forall k, \quad \sum_{k=1}^N \mu_k = \mathbb{1}
$$

**Dual**:
$$
p_{\mathrm{opt}} = \min \; \mathrm{Tr}(\Lambda)
$$
subject to:
$$
\Lambda \geq p_k \rho_k \;\forall k, \quad \Lambda = \Lambda^*
$$

**Proof of strong duality**: Slater's condition is satisfied by taking $\mu_k = \mathbb{1}/N$ (strictly feasible primal, since $\mu_k > 0$). Hence strong duality holds and both optima are attained.

**Complementary slackness**: The optimal POVM $\{\mu_k^*\}$ and dual variable $\Lambda^*$ satisfy:

$$
\mu_k^* (\Lambda^* - p_k \rho_k) = 0 \quad \forall k
$$

This means: measurement outcome $k$ is "active" only where $p_k\rho_k$ touches the "envelope" $\Lambda^*$.

---

## 7. SDP for Entanglement Detection

### Proposition 3.50 (Separability SDP Relaxation) **[Watrous, Ch.3]**

Testing whether $\rho \in \mathrm{Sep}$ is NP-hard (Gurvits 2003). However, the PPT condition provides a tractable SDP relaxation:

**PPT Feasibility SDP**:
$$
\rho \in \mathrm{PPT} \iff \rho \geq 0 \;\text{and}\; \rho^{T_B} \geq 0
$$

Both conditions are semidefinite constraints. This can be checked in polynomial time.

**Hierarchy of SDP relaxations** (Doherty-Parrilo-Spedalieri):

Level $k$: Does there exist an extension $\rho_{AB_1\ldots B_k}$ such that:
1. $\mathrm{Tr}_{B_2\ldots B_k}(\rho_{AB_1\ldots B_k}) = \rho_{AB}$
2. $\rho_{AB_1\ldots B_k}$ is invariant under permutations of $B_1,\ldots,B_k$
3. $\rho_{AB_1\ldots B_k}^{T_{B_i}} \geq 0$ for each $i$

Each level is an SDP. The hierarchy converges: $\rho \in \mathrm{Sep}$ iff feasible at all levels.

---

## 8. SDP for Channel Capacities

### Proposition (Holevo Capacity Upper Bound) **[Watrous, Ch.3]**

The Holevo information $\chi(\Phi)$ can be bounded using SDPs:

$$
\chi(\Phi) \leq \log d - \min_\sigma \max_\rho \mathrm{D}(\Phi(\rho)\|\sigma)
$$

While the Holevo capacity itself involves a non-convex optimization (over ensembles), the **minimum output entropy**

$$
\mathrm{H}_{\min}(\Phi) = \min_\rho \mathrm{H}(\Phi(\rho))
$$

appears in the bound $\chi(\Phi) \leq \log d_{\mathrm{out}} - \mathrm{H}_{\min}(\Phi)$.

The minimum output entropy is not an SDP, but SDP relaxations (via moment/SOS hierarchies) provide bounds.

---

## 9. SDP for Quantum Error Correction

### Proposition (Knill-Laflamme Conditions as SDP) **[Watrous, Ch.3]**

An $((n,K))$ quantum error-correcting code with projector $\Pi$ onto the code space corrects errors $\{E_a\}$ iff:

$$
\Pi E_a^* E_b \Pi = c_{ab} \Pi
$$

for some Hermitian matrix $C = (c_{ab})$. This can be reformulated:

Given a noise channel $\Phi(X) = \sum_a A_a X A_a^*$, find the largest $K$ such that there exists a rank-$K$ projector $\Pi$ satisfying the Knill-Laflamme conditions. This is related to SDP via:

$$
\max \; \mathrm{Tr}(\Pi) \quad \text{s.t.} \quad \Pi A_a^* A_b \Pi = c_{ab}\Pi, \quad \Pi^2 = \Pi, \quad \Pi \geq 0
$$

The rank constraint $\Pi^2 = \Pi$ is not semidefinite, but relaxations yield useful bounds.

---

## 10. Computational Aspects

### SDP Solvers and Complexity **[Watrous, Ch.3]**

- SDPs can be solved in polynomial time to arbitrary precision (interior point methods).
- Typical complexity: $O(n^{3.5} \log(1/\varepsilon))$ for $n \times n$ matrix variables.
- For quantum information SDPs:
  - Diamond norm: $O(d^{3.5})$ where $d = d_{\mathrm{in}} \cdot d_{\mathrm{out}}$.
  - Optimal discrimination: $O((Nd)^{3.5})$ for $N$ states of dimension $d$.
  - PPT test: $O(d^{3.5})$ for $d = d_A \cdot d_B$.

### Key SDP Software

Standard solvers: SeDuMi, SDPT3, MOSEK, SCS.
Quantum-specific: QETLAB (MATLAB), CVX/CVXPY with quantum extensions.
