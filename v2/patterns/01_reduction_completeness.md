# Pattern 01: Reduction & Completeness

**Type:** Hardness proof via reduction from a known-hard problem.

**When to use:** You want to show problem B is at least as hard as problem A (known-hard), or that B is complete for a complexity class.

---

## Abstract Template

1. **State the source problem A** with its known hardness (e.g., NP-hard, QMA-complete).
2. **Define the mapping** f: instances of A -> instances of B. Must be efficiently computable.
3. **Completeness (YES case):** If A has a YES answer, show B constructed via f also has a YES answer. Exhibit the witness explicitly.
4. **Soundness (NO case):** If A has a NO answer, show B cannot have a YES answer. Typically by contrapositive: a solution to f(A) would yield a solution to A.
5. **Conclude** B is at least as hard as A. If B is also in the class, B is complete.

---

## QC Instantiation

**Example 1: Local Hamiltonian is QMA-complete**
- Source: 3-SAT (NP-complete) analogy; actual reduction from circuit-to-Hamiltonian.
- Mapping: Kitaev's construction — encode verification circuit into a 5-local Hamiltonian via clock register.
- Completeness: valid witness |psi> gives low energy state.
- Soundness: no valid witness => all states have energy >= gap.
- KB refs: `QC.HAMILTONIAN.KITAEV_LOCAL.01`, `QC.COMPLEXITY.QMA_COMPLETE.01`

**Example 2: Decoding surface codes is NP-hard (via reduction from RBIM)**
- Source: computing partition function of random-bond Ising model.
- Mapping: syndrome -> coupling configuration on lattice.
- KB refs: `QC.QEC.SURFACE_DECODING_HARDNESS.01`, `QC.STATMECH.DENNIS_RBIM.01`

---

## ML Instantiation

**Example 1: Learning parity with noise is hard**
- Source: LPN assumption (cryptographic hardness).
- Mapping: parity instance -> binary classification instance.
- KB refs: `ML.THEORY.COMPUTATIONAL_HARDNESS.01`

**Example 2: Combinatorial optimization NP-hardness transfers to ML formulations**
- Source: MAX-CUT is NP-hard.
- Mapping: graph instance -> GNN input; optimal cut -> model output.
- If GNN solves it in poly time, P=NP. So approximation is the realistic goal.
- KB refs: `ML.GNN.EXPRESSIVITY_WL.01`, `ML.OPTIM.MAXCUT_SDP.01`

---

## Common Mistakes / Anti-Patterns

- **Forgetting polynomial-time computability of f.** The reduction itself must be efficient; otherwise the hardness claim is vacuous.
- **Proving only one direction.** Both completeness (YES->YES) and soundness (NO->NO) are required. A common error is showing the witness maps but not the gap preservation.
- **Wrong gap.** In promise problems (like QMA), the completeness-soundness gap must be preserved or amplifiable. Losing the gap invalidates the reduction.
- **Confusing hardness with impossibility.** NP-hard means no known poly-time exact algorithm, not that good approximations are impossible.
- **Reducing the wrong direction.** To show B is hard, reduce FROM A (hard) TO B. The common error is reducing B to A, which only shows B is no harder than A.
