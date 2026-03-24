# Pattern 02: Monotonicity & Information Processing

**Type:** Proving a quantity cannot increase (or decrease) under a class of operations.

**When to use:** Establishing that an information measure is a valid resource monotone, or that a physical process is irreversible in some sense.

---

## Abstract Template

1. **Define the quantity** Q(rho) and the allowed operations class C (e.g., CPTP maps, LOCC, Clifford circuits).
2. **State the monotonicity claim:** For all E in C, Q(E(rho)) <= Q(rho) (or >=, depending on convention).
3. **Prove for elementary operations.** Decompose any E in C into elementary steps. Show Q is monotone under each elementary step.
4. **Handle convexity/concavity.** If C includes classical mixing (probabilistic operations), show Q(sum p_i rho_i) <= sum p_i Q(rho_i) (or reverse) as needed.
5. **Conclude** Q is a valid monotone for the resource theory defined by C.

---

## QC Instantiation

**Example 1: Quantum relative entropy is monotone under CPTP maps (data processing inequality)**
- Quantity: S(rho || sigma) = Tr[rho (log rho - log sigma)].
- Operations: all CPTP maps.
- Proof: Lieb's concavity theorem or Petz recovery argument.
- Consequence: mutual information, coherent information, entanglement measures all inherit this.
- KB refs: `QC.INFO.DPI_RELATIVE_ENTROPY.01`, `QC.INFO.STRONG_SUBADDITIVITY.01`

**Example 2: Entanglement does not increase under LOCC**
- Quantity: entanglement entropy E(rho_AB).
- Operations: LOCC (local operations + classical communication).
- Proof: Schmidt decomposition + majorization under local unitaries.
- KB refs: `QC.INFO.ENTANGLEMENT_MONOTONE.01`, `QC.LINALG.SCHMIDT_DECOMP.01`

---

## ML Instantiation

**Example 1: KL divergence decreases along diffusion forward process**
- Quantity: KL(q(x_t) || p_target).
- Operations: adding Gaussian noise (forward SDE steps).
- Key: each noise step is a contraction in KL; eventual convergence to prior N(0,I).
- KB refs: `ML.DIFFUSION.DDPM_FORWARD.01`, `ML.DIFFUSION.SCORE_SDE_FORWARD.01`

**Example 2: Information bottleneck — mutual information cannot increase through layers**
- Quantity: I(X; T) where T is a hidden representation.
- Operations: deterministic neural network layers (Markov chain X -> T -> Y).
- Data processing inequality: I(X; Y) <= I(X; T).
- KB refs: `ML.THEORY.INFO_BOTTLENECK.01`

---

## Common Mistakes / Anti-Patterns

- **Not verifying the operation class is closed under composition.** If C is not closed, monotonicity under elementary operations does not imply monotonicity under sequences.
- **Confusing strong and weak monotonicity.** Weak: Q does not increase on average. Strong: Q does not increase for any branch of a measurement. Strong is strictly harder to prove.
- **Ignoring the classical register.** In LOCC proofs, forgetting that classical communication can correlate local operations. Must handle the full conditional structure.
- **Assuming monotonicity implies uniqueness.** Many different quantities can be monotone under the same C. Monotonicity is necessary but not sufficient for a "good" measure.
- **Forgetting edge cases.** Q may be undefined or infinite for some states (e.g., relative entropy when supp(rho) not contained in supp(sigma)). Handle domains carefully.
