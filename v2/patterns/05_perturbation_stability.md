# Pattern 05: Perturbation & Stability

**Type:** Show that small changes in input lead to bounded changes in output. Establishes robustness, continuity, or error propagation bounds.

**When to use:** Analyzing noise sensitivity, proving algorithm robustness, bounding approximation errors, or establishing continuity of a map.

---

## Abstract Template

1. **Define the unperturbed and perturbed settings.** Object X, perturbation X' = X + delta, with ||delta|| <= epsilon in some norm.
2. **Identify the quantity of interest** Q(X) and state the goal: bound |Q(X') - Q(X)|.
3. **Establish a local bound.** Use Taylor expansion, Lipschitz condition, or operator inequality: |Q(X') - Q(X)| <= L * ||delta|| for some L (Lipschitz constant or derivative bound).
4. **Handle higher-order terms** if the linear bound is insufficient. Bound the remainder R via second-order analysis or exact computation.
5. **State the stability result:** Q is stable under perturbations of size epsilon, with degradation at most f(epsilon).

---

## QC Instantiation

**Example 1: Fidelity under small noise (Fuchs-van de Graaf)**
- Unperturbed: ideal state rho. Perturbed: noisy state sigma.
- Quantity: any observable expectation or success probability.
- Bound: 1 - F(rho, sigma) <= T(rho, sigma) <= sqrt(1 - F(rho, sigma)^2).
- Consequence: if fidelity is 1 - epsilon, trace distance is O(sqrt(epsilon)).
- KB refs: `QC.INFO.FUCHS_VAN_DE_GRAAF.01`, `QC.INFO.TRACE_DISTANCE.01`

**Example 2: QEC threshold as stability result**
- Unperturbed: perfect code. Perturbed: physical noise rate p.
- Stability claim: below threshold p < p_th, logical error rate decreases exponentially with code distance.
- Proof: percolation/statistical mechanics mapping.
- KB refs: `QC.QEC.THRESHOLD_THEOREM.01`, `QC.STATMECH.DENNIS_RBIM.01`

---

## ML Instantiation

**Example 1: Score estimation error propagation in diffusion models**
- Unperturbed: true score nabla log p_t(x). Perturbed: estimated score s_theta(x, t).
- Quantity: KL(p_data || p_theta) after reverse sampling.
- Bound: KL <= integral of E[||s_theta - nabla log p_t||^2] dt (score matching objective).
- KB refs: `ML.DIFFUSION.SCORE_SDE_REVERSE.01`, `ML.DIFFUSION.SCORE_MATCHING.01`

**Example 2: Generalization as stability (algorithmic stability)**
- Unperturbed: training set S. Perturbed: S' = S with one sample replaced.
- Quantity: |R(A(S)) - R_emp(A(S))| (generalization gap).
- If algorithm A is beta-uniformly stable, generalization gap <= beta.
- KB refs: `ML.THEORY.GENERALIZATION_BOUNDS.01`

---

## Common Mistakes / Anti-Patterns

- **Using the wrong norm.** Trace distance for quantum states, operator norm for channels, L2 for scores. Mismatched norms give vacuous bounds.
- **Linear bound when the dependence is quadratic (or vice versa).** Always check whether the O(epsilon) bound is tight. If Q has a saddle point, the actual dependence may be O(epsilon^2).
- **Assuming worst-case when average-case suffices.** Stability over typical perturbations (e.g., random noise) can be much better than worst-case. State which you are proving.
- **Ignoring accumulation.** For sequential processes (circuits, diffusion steps), perturbations accumulate. Must track error propagation across T steps, not just one.
- **Confusing local and global stability.** A locally Lipschitz function may have unbounded global Lipschitz constant. Specify the domain of validity.
