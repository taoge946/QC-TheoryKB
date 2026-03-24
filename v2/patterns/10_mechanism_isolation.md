# Pattern 10: Mechanism Isolation

**Type:** Decompose a complex system into independent mechanisms, analyze each in isolation, then recombine to explain the whole.

**When to use:** Understanding why an algorithm/protocol works, ablation-style theoretical analysis, identifying which component is responsible for a given property.

---

## Abstract Template

1. **Identify the composite system** S that produces outcome Y from input X through multiple interacting mechanisms M_1, ..., M_k.
2. **Isolate each mechanism.** Define a simplified system S_i that retains M_i but replaces all other mechanisms with idealized/trivial versions.
3. **Analyze each S_i independently.** Prove: S_i achieves property P_i (what M_i contributes). Conversely, removing M_i (S without M_i) fails to achieve P_i.
4. **Prove composition.** Show that the combined effect of M_1, ..., M_k yields the overall performance. This requires bounding interaction terms: ||S - S_1 compose ... compose S_k|| <= epsilon.
5. **State the decomposition theorem:** Performance of S = sum/product of individual mechanism contributions + bounded interaction term.

---

## QC Instantiation

**Example 1: Fault-tolerant QEC = code + syndrome extraction + decoder**
- M_1 (code): provides distance d, so weight < d errors are detectable.
- M_2 (syndrome extraction): flag circuits detect hook errors without spreading.
- M_3 (decoder): MWPM/UF maps syndromes to corrections.
- Isolation: analyze code distance alone (M_1), then noisy syndrome extraction (M_2), then decoder accuracy (M_3).
- Composition: total logical error = P(undetected by code) + P(syndrome misread) + P(decoder fails | correct syndrome).
- KB refs: `QC.QEC.FAULT_TOLERANCE.01`, `QC.QEC.SURFACE_DECODING.01`, `QC.QEC.KNILL_LAFLAMME.01`

**Example 2: VQE = ansatz expressibility + optimizer convergence + measurement noise**
- M_1: ansatz reaches ground state subspace (expressibility).
- M_2: optimizer finds the global minimum (no barren plateaus, good landscape).
- M_3: finite-shot measurements introduce sampling noise.
- Each can be analyzed independently; total error bounded by sum.
- KB refs: `QC.VAR.VQE_FRAMEWORK.01`, `QC.VAR.BARREN_PLATEAUS.01`, `QC.VAR.MEASUREMENT_OVERHEAD.01`

---

## ML Instantiation

**Example 1: Diffusion model = forward process + score network + sampler**
- M_1 (forward): Gaussian noise schedule determines signal-to-noise at each t.
- M_2 (score network): neural network approximates nabla log p_t(x).
- M_3 (sampler): ODE/SDE integrator converts scores to samples.
- Isolation: score error is pure M_2, discretization error is pure M_3, schedule design is M_1.
- Total KL <= (score matching loss from M_2) + (discretization error from M_3) + (prior mismatch from M_1).
- KB refs: `ML.DIFFUSION.DDPM_LOSS_DECOMP.01`, `ML.DIFFUSION.SCORE_SDE_REVERSE.01`, `ML.DIFFUSION.DDIM_SAMPLING.01`

**Example 2: GNN for CO = graph encoding + message passing + readout/decoding**
- M_1: initial node/edge features encode the problem instance.
- M_2: message passing propagates local information (limited by receptive field ~ number of layers).
- M_3: readout aggregates node states into a solution.
- WL-test limitation is purely an M_2 property. Readout design (M_3) affects solution quality independently.
- KB refs: `ML.GNN.GIN_EXPRESSIVITY.01`, `ML.GNN.WL_TEST.01`, `ML.OPTIM.GNN_CO_FRAMEWORK.01`

---

## Common Mistakes / Anti-Patterns

- **Mechanisms are not actually independent.** If M_1 and M_2 interact strongly (e.g., ansatz choice affects optimizer landscape), analyzing them in isolation gives misleading conclusions. Must bound the interaction term explicitly.
- **Missing a mechanism.** If the decomposition is incomplete (e.g., ignoring measurement noise in VQE), the recombination will undercount errors. Enumerate all mechanisms before isolating.
- **Isolation changes the regime.** Removing M_2 from the system might change the operating regime of M_1 (e.g., removing error correction changes the effective noise model). The idealized replacement must be carefully chosen.
- **Additive vs. multiplicative composition.** Errors sometimes add (independent noise sources) and sometimes multiply (cascaded channels). Using the wrong composition rule gives wrong bounds.
- **Confusing necessary and sufficient.** Showing M_i is necessary (removing it breaks the system) does not mean M_i alone is sufficient. All mechanisms together are needed.
