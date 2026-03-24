# Pattern 03: Variational Decomposition

**Type:** Expressing a hard-to-compute quantity as an optimization (sup/inf) over a tractable family, then bounding or approximating.

**When to use:** The exact quantity is intractable, but you can write it as a variational problem and either solve it analytically or bound it.

---

## Abstract Template

1. **Identify the target quantity** F(x) that is hard to compute directly.
2. **Write the variational form:** F(x) = sup_{y in Y} G(x, y) (or inf). Prove equality (the variational characterization).
3. **Lower bound (achievability):** Pick a specific y* in Y. Then F(x) >= G(x, y*). The art is choosing a good y*.
4. **Upper bound (converse):** Show that for all y in Y, G(x, y) <= B(x). Often uses convexity, duality, or constraint relaxation.
5. **Tighten:** Show the gap between lower and upper bounds vanishes (or characterize when it does).

---

## QC Instantiation

**Example 1: Quantum channel capacity via coherent information**
- Target: quantum capacity Q(N) of a channel N.
- Variational form: Q(N) = lim (1/n) max_{rho} I_c(rho, N^{otimes n}).
- Lower bound: pick a specific input state (e.g., Bell states for depolarizing channel).
- Upper bound: use degradability or no-cloning bound.
- KB refs: `QC.INFO.COHERENT_INFO.01`, `QC.INFO.CHANNEL_CAPACITY.01`

**Example 2: Fidelity as variational expression**
- F(rho, sigma) = (Tr sqrt(sqrt(rho) sigma sqrt(rho)))^2.
- Variational form (Uhlmann): F = max_{|psi>, |phi> purifications} |<psi|phi>|^2.
- KB refs: `QC.INFO.UHLMANN_FIDELITY.01`, `QC.INFO.PURIFICATION.01`

---

## ML Instantiation

**Example 1: ELBO as variational bound on log-likelihood**
- Target: log p(x) (intractable due to marginalization over z).
- Variational form: log p(x) >= E_{q(z|x)}[log p(x|z)] - KL(q(z|x) || p(z)) = ELBO.
- Lower bound: any q gives a valid bound. Tighter q -> tighter bound.
- Gap: KL(q(z|x) || p(z|x)) >= 0, equality iff q = true posterior.
- KB refs: `ML.GENERATIVE.VAE_ELBO.01`, `ML.DIFFUSION.DDPM_SIMPLE_LOSS.01`

**Example 2: Diffusion loss as variational bound**
- Target: log p_theta(x_0).
- Decomposition: ELBO = L_0 + sum_t L_t + L_T (reconstruction + denoising + prior terms).
- Each L_t is a KL between Gaussians, computable in closed form.
- KB refs: `ML.DIFFUSION.DDPM_LOSS_DECOMP.01`, `ML.DIFFUSION.DDIM_ELBO.01`

---

## Common Mistakes / Anti-Patterns

- **Claiming tightness without proof.** A variational lower bound is always valid, but asserting it is tight requires showing the optimal y* is achieved or the gap vanishes.
- **Optimizing over too small a family Y.** The bound is only as good as Y. If Y is restricted (e.g., mean-field family), the gap can be large and uncontrolled.
- **Swapping sup and lim.** In regularized quantities like channel capacity, Q = lim sup_{n} (1/n) max ... The order matters and sup_{n} (1/n) max != max lim.
- **Forgetting the variational equality proof.** The decomposition step (step 2) itself needs a proof. Often relies on Fenchel duality, minimax theorems, or purification arguments.
- **Not checking convexity of G in y.** If G is not convex/concave, the variational problem may have local optima and the bound may be hard to evaluate.
