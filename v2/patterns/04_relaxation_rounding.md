# Pattern 04: Relaxation & Rounding

**Type:** Relax a discrete/hard problem to a continuous/tractable one, solve it, then round back to a feasible solution with bounded quality loss.

**When to use:** Combinatorial optimization where exact solutions are NP-hard, but continuous relaxations (LP, SDP, spectral) admit efficient solvers.

---

## Abstract Template

1. **Formulate the original problem** P: min_{x in D} f(x), where D is discrete (e.g., {0,1}^n, permutations).
2. **Relax:** Define P': min_{x in D'} f'(x), where D' contains D (e.g., [0,1]^n, doubly stochastic matrices). Prove OPT(P') <= OPT(P).
3. **Solve the relaxation.** Obtain x* in D' via LP/SDP/spectral methods.
4. **Round:** Apply a rounding scheme R: D' -> D to get x_hat = R(x*). The rounding must be efficient.
5. **Analyze the approximation ratio:** Show f(x_hat) <= alpha * OPT(P) for some alpha >= 1 (minimization). The gap alpha is the integrality gap.

---

## QC Instantiation

**Example 1: SDP relaxation for optimal quantum measurements (state discrimination)**
- Original: maximize success probability over all POVMs.
- Relaxation: SDP where POVM elements are PSD matrices summing to I.
- Already continuous, so the "rounding" is projecting to rank-1 if a simpler measurement is desired.
- KB refs: `QC.INFO.STATE_DISCRIMINATION.01`, `QC.INFO.HELSTROM_BOUND.01`

**Example 2: Qubit routing via relaxation**
- Original: find minimum-depth SWAP sequence (discrete, NP-hard in general).
- Relaxation: fractional matching on the coupling graph, or token swapping LP.
- Rounding: greedy layer-by-layer SWAP assignment.
- KB refs: `QC.COMPILE.ROUTING_SABRE.01`, `QC.COMPILE.ROUTING_OPTIMAL.01`

---

## ML Instantiation

**Example 1: MAX-CUT SDP relaxation (Goemans-Williamson)**
- Original: max_{x in {-1,1}^n} sum_{(i,j) in E} (1 - x_i x_j)/2.
- Relaxation: max_{X PSD, X_ii=1} sum_{(i,j)} (1 - X_ij)/2.
- Rounding: random hyperplane — sample r ~ N(0,I), set x_i = sign(v_i . r).
- Ratio: alpha >= 0.878. Used as baseline for GNN-based CO solvers.
- KB refs: `ML.OPTIM.MAXCUT_SDP.01`, `ML.OPTIM.GW_ROUNDING.01`

**Example 2: Discrete diffusion via continuous relaxation**
- Original: generate discrete structures (graphs, sequences).
- Relaxation: diffuse in continuous space R^d, train continuous denoiser.
- Rounding: argmax or Gumbel-softmax at final step to recover discrete output.
- KB refs: `ML.DIFFUSION.DIFUSCO_CONTINUOUS.01`, `ML.DIFFUSION.D3PM_DISCRETE.01`

---

## Common Mistakes / Anti-Patterns

- **Ignoring the integrality gap.** The relaxation bound is optimistic. If the integrality gap is unbounded, the approach gives no useful guarantee. Always characterize or bound the gap.
- **Rounding destroys feasibility.** After rounding, x_hat may violate constraints of P. Must prove feasibility or add a repair step.
- **Non-deterministic rounding without expectation analysis.** Randomized rounding gives guarantees in expectation. For high-probability bounds, need concentration arguments (see Pattern 06).
- **Claiming SDP is "exact" for quantum problems.** Many quantum optimization problems (e.g., state discrimination) are naturally SDPs, but others (e.g., entanglement detection) have SDP relaxations that are not tight.
- **Forgetting solver complexity.** LP is polynomial, SDP is polynomial but with large constants. For n > 10^4, SDP may be impractical even if theoretically polynomial.
