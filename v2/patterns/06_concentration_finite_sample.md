# Pattern 06: Concentration & Finite-Sample Bounds

**Type:** Show that a random variable concentrates around its mean with high probability given finite samples.

**When to use:** Converting expected-value guarantees into high-probability statements, bounding estimation errors, proving sample complexity results.

---

## Abstract Template

1. **Identify the random variable** X = g(Z_1, ..., Z_n) as a function of n independent (or weakly dependent) random variables.
2. **Compute or bound E[X]** (the quantity X concentrates around).
3. **Verify conditions** for a concentration inequality: boundedness (Hoeffding), sub-Gaussianity (sub-Gaussian tail), Lipschitz in each coordinate (McDiarmid), or martingale structure (Azuma).
4. **Apply the inequality:** Pr[|X - E[X]| > t] <= 2 exp(-c * n * t^2 / B^2) or similar. State the constants explicitly.
5. **Invert for sample complexity:** To achieve |X - E[X]| <= epsilon with probability >= 1 - delta, need n >= (B^2 / c*epsilon^2) * log(2/delta).

---

## QC Instantiation

**Example 1: Shadow tomography sample complexity**
- Random variable: estimator Tr[O * rho_hat] from n random Clifford measurements.
- E[X] = Tr[O * rho] (unbiased).
- Concentration: each measurement outcome is bounded, apply median-of-means.
- Sample complexity: n = O(log(M) / epsilon^2) for M observables.
- KB refs: `QC.QEC.RANDOM_MEASUREMENT.01`, `QC.INFO.TOMOGRAPHY.01`

**Example 2: Randomized benchmarking confidence intervals**
- Random variable: average gate fidelity estimator from m random sequences of length l.
- Model: exponential decay A * p^l + B with depolarizing parameter p.
- Concentration: bounded random variable, Hoeffding gives CI width O(1/sqrt(m)).
- KB refs: `QC.HARDWARE.RB_PROTOCOL.01`, `QC.HARDWARE.MAGESAN_RB.01`

---

## ML Instantiation

**Example 1: Generalization bound via Rademacher complexity**
- Random variable: sup_{f in F} |R(f) - R_hat(f)| (uniform deviation).
- Bound: E[sup] <= 2 * Rad_n(F). Then McDiarmid: sup concentrates around its mean.
- Result: with prob >= 1-delta, R(f) <= R_hat(f) + 2*Rad_n(F) + sqrt(log(1/delta)/(2n)).
- KB refs: `ML.THEORY.RADEMACHER_COMPLEXITY.01`, `ML.THEORY.GENERALIZATION_BOUNDS.01`

**Example 2: Finite-sample DDPM loss approximation**
- Random variable: empirical denoising loss L_hat = (1/n) sum ||epsilon - epsilon_theta(x_t, t)||^2.
- Each term is bounded (assuming bounded data and network output).
- Hoeffding: |L_hat - L| <= O(1/sqrt(n)) with high probability.
- KB refs: `ML.DIFFUSION.DDPM_SIMPLE_LOSS.01`

---

## Common Mistakes / Anti-Patterns

- **Applying Hoeffding to unbounded variables.** Hoeffding requires bounded range [a,b]. For unbounded variables, use sub-Gaussian or truncation arguments.
- **Ignoring dependence.** Standard concentration inequalities assume independence. For Markov chain samples (MCMC, sequential decisions), use mixing time arguments or martingale methods.
- **Union bound over too many events.** When bounding M simultaneous deviations, the log(M) factor matters. If M grows exponentially, the bound may become vacuous.
- **Confusing expectation bounds with high-probability bounds.** Markov's inequality gives Pr[X > t] <= E[X]/t, which is often too loose. Concentration gives exponentially decaying tails.
- **Off-by-constant errors in sample complexity.** The constants in concentration inequalities matter for practical sample sizes. Report them explicitly rather than hiding in O-notation.
