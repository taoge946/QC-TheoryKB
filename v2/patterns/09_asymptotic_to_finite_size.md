# Pattern 09: Asymptotic to Finite-Size Conversion

**Type:** Convert an asymptotic result (n -> infinity) into an explicit finite-n bound with computable error terms.

**When to use:** Making theoretical guarantees practical, analyzing real experiments with finite resources, or comparing theory to numerical simulation.

---

## Abstract Template

1. **State the asymptotic result:** "As n -> infinity, Q_n -> Q* at rate Theta(f(n))."
2. **Identify the proof technique** that gave the asymptotic result. Locate where limits, approximations, or existence arguments were used.
3. **Make each step quantitative.** Replace: limit with explicit n-dependent bound, typicality with concentration inequality (Pattern 06), union bound with explicit cardinality, channel coding with finite blocklength bound.
4. **Collect all error terms** into a single finite-n expression: |Q_n - Q*| <= g(n, epsilon, delta) with explicit constants.
5. **Evaluate numerically** for practically relevant n to check the bound is non-vacuous.

---

## QC Instantiation

**Example 1: Finite-size surface code threshold**
- Asymptotic: below threshold p < p_th ~ 10.3%, logical error rate -> 0 as d -> infinity.
- Finite-size: p_L(d, p) ~ A * (p/p_th)^{d/2} for specific A (depends on decoder).
- Method: replace percolation argument with explicit cluster counting.
- Practical: for d=17, p=0.1%, gives p_L ~ 10^{-12}. These numbers actually matter for architecture design.
- KB refs: `QC.QEC.THRESHOLD_THEOREM.01`, `QC.QEC.SURFACE_CODE_DISTANCE.01`

**Example 2: Finite-copy quantum state discrimination**
- Asymptotic: Chernoff bound gives error ~ exp(-n * xi(rho, sigma)) for n copies.
- Finite-n: Audenaert et al. give explicit prefactors and second-order terms.
- Bound: -log P_err = n * xi + sqrt(n) * V * Phi^{-1}(epsilon) + O(log n).
- KB refs: `QC.INFO.QUANTUM_HYPOTHESIS_TESTING.01`, `QC.INFO.CHERNOFF_BOUND.01`

---

## ML Instantiation

**Example 1: Finite-step diffusion sampling error**
- Asymptotic: as T -> infinity, reverse SDE converges to p_data.
- Finite-T: discretization error from Euler-Maruyama is O(1/T) per step.
- Total error: KL(p_data || p_theta) <= (score error) + O(d/T) + O(exp(-T) * initial mismatch).
- Practical: T=1000 steps in DDPM; T=50 in DDIM via non-Markovian correction.
- KB refs: `ML.DIFFUSION.DDPM_REVERSE.01`, `ML.DIFFUSION.DDIM_SAMPLING.01`

**Example 2: Finite-width neural network approximation**
- Asymptotic: universal approximation — infinite-width networks approximate any continuous function.
- Finite-width: width-m network approximates f to error O(1/sqrt(m)) in L2 for Barron-class functions.
- Includes explicit dependence on Barron norm of target function.
- KB refs: `ML.THEORY.UNIVERSAL_APPROX.01`, `ML.THEORY.BARRON_THEOREM.01`

---

## Common Mistakes / Anti-Patterns

- **Vacuous bounds.** A finite-n bound that exceeds 1 (for probabilities) or exceeds trivial limits is useless. Always evaluate numerically for target n before claiming the result is meaningful.
- **Hidden constants from asymptotic proofs.** O(1/n) hides a constant that could be 10^6. When converting, track all constants explicitly through the proof.
- **Wrong order of limits.** In multi-parameter settings (e.g., n samples, T steps, d dimensions), the order n -> inf first vs. T -> inf first can give different results. State which regime you are in.
- **Replacing existential with constructive without justification.** Asymptotic proofs often use "there exists a code/estimator." Finite-size versions need explicit constructions, which may have worse constants.
- **Ignoring lower-order terms that dominate at practical n.** The sqrt(n) second-order term can dominate the n * rate term for n < 10^4. Include at least the second-order correction.
