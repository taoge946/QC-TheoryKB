# Pattern 07: Achievability & Converse (Matching Bounds)

**Type:** Prove a quantity is exactly C by showing (a) C is achievable and (b) no scheme can exceed C.

**When to use:** Establishing capacity theorems, tight complexity bounds, optimal rates, or exact thresholds.

---

## Abstract Template

1. **State the operational task** and the figure of merit (rate, fidelity, error probability).
2. **Achievability (lower bound / direct theorem):** Construct an explicit protocol or coding scheme that achieves rate R = C - epsilon for any epsilon > 0. Often uses random coding + typicality or explicit algebraic construction.
3. **Converse (upper bound / impossibility):** Show that any protocol achieving rate R > C must fail. Typically uses information-theoretic inequalities (Fano, data processing) or entropic arguments.
4. **Match the bounds:** Show the achievability and converse bounds coincide: R* = C.
5. **State the capacity theorem** with its single-letter or multi-letter form.

---

## QC Instantiation

**Example 1: Quantum channel capacity (Hashing bound + no-cloning converse)**
- Task: transmit quantum information through channel N at rate R.
- Achievability: random stabilizer codes achieve R = I_c(rho, N) (coherent information). Proven via random coding over stabilizer codes.
- Converse: no code can exceed Q(N) = lim (1/n) max I_c(rho, N^n). Uses no-cloning and data processing inequality.
- Complication: not single-letter in general (superadditivity). Single-letter for degradable channels.
- KB refs: `QC.INFO.COHERENT_INFO.01`, `QC.INFO.CHANNEL_CAPACITY.01`, `QC.INFO.DPI_RELATIVE_ENTROPY.01`

**Example 2: QEC threshold**
- Task: reliable computation with physical error rate p.
- Achievability: concatenated codes (or surface codes) achieve fault tolerance for p < p_th.
- Converse: above p_th, logical error rate bounded away from 0 (percolation argument).
- KB refs: `QC.QEC.THRESHOLD_THEOREM.01`, `QC.QEC.CONCATENATED_DISTANCE.01`

---

## ML Instantiation

**Example 1: Minimax optimal estimation rates**
- Task: estimate parameter theta from n samples under loss L.
- Achievability: construct an estimator (e.g., MLE, James-Stein) with risk <= C/n.
- Converse: Fano's inequality or Le Cam's method shows no estimator can achieve risk < c/n.
- Matching: risk = Theta(1/n) with explicit constant.
- KB refs: `ML.THEORY.MINIMAX_RATES.01`

**Example 2: Score matching achieves optimal KL rate for diffusion**
- Task: learn distribution p_data to KL accuracy epsilon.
- Achievability: score-based diffusion with L steps and n samples achieves KL <= O(d/n + 1/L).
- Converse: any method needs n = Omega(d/epsilon) samples (information-theoretic lower bound).
- KB refs: `ML.DIFFUSION.SCORE_MATCHING.01`, `ML.DIFFUSION.SCORE_SDE_CONVERGENCE.01`

---

## Common Mistakes / Anti-Patterns

- **Achievability without explicit construction.** "There exists a code" via random coding is fine for existence proofs, but for practical claims, must show the construction is efficient.
- **Weak converse vs. strong converse.** Weak: rate above C implies error does not vanish. Strong: error goes to 1. The strong converse is strictly more powerful and often requires different techniques.
- **Single-letter vs. regularized.** Many quantum capacities are only known in regularized (multi-letter) form. Claiming a single-letter formula requires proving additivity, which is often hard or false.
- **Forgetting the asymptotic regime.** Achievability-converse pairs are typically asymptotic (n -> infinity). Finite-size performance can differ significantly (see Pattern 09).
- **Mismatched operational definitions.** Achievability and converse must use the same operational definition (same error criterion, same resource model). A common error is proving achievability with average error but converse with worst-case error.
