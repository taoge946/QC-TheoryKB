# Pattern 08: Canonical Form & Equivalence

**Type:** Show that every object in a class can be transformed into a standard (canonical) form, then prove properties on the canonical form.

**When to use:** Simplifying proofs by reducing to a normal form, classifying objects up to equivalence, or showing two apparently different objects are equivalent.

---

## Abstract Template

1. **Define the equivalence relation** ~ on the class of objects O. (e.g., unitary equivalence, graph isomorphism, gauge equivalence.)
2. **Define the canonical form** C(x) for each x in O. Must satisfy: (a) C(x) ~ x, and (b) x ~ y iff C(x) = C(y).
3. **Construct the canonicalization map.** Give an explicit (efficient) procedure to compute C(x) from x. Prove it terminates and is well-defined.
4. **Prove properties on canonical forms.** Since C(x) ~ x, any property invariant under ~ transfers from C(x) to x.
5. **Derive consequences:** classification (count canonical forms), decidability (test equivalence via C(x) = C(y)), simplification (work only with canonical representatives).

---

## QC Instantiation

**Example 1: Stabilizer codes in standard form**
- Objects: stabilizer groups S <= G_n (n-qubit Paulis).
- Equivalence: Clifford equivalence (S ~ C S C^dag).
- Canonical form: generators in row-echelon form on the binary symplectic representation.
- Use: two codes are Clifford-equivalent iff their canonical generator matrices match.
- KB refs: `QC.QEC.STABILIZER_FORMALISM.01`, `QC.GROUP.CLIFFORD_GROUP.01`, `QC.QEC.GOTTESMAN_BINARY.01`

**Example 2: Quantum channels in Stinespring vs. Kraus form**
- Objects: CPTP maps.
- Equivalence: Kraus representations {K_i} and {L_j} give the same channel iff K_i = sum_j U_ij L_j for some unitary U.
- Canonical form: Stinespring dilation (unique up to isometry on environment).
- Use: proves properties like complementary channels, degradability.
- KB refs: `QC.INFO.STINESPRING_DILATION.01`, `QC.INFO.KRAUS_REPRESENTATION.01`

---

## ML Instantiation

**Example 1: GNN and WL canonical coloring**
- Objects: graphs with node features.
- Equivalence: isomorphism (permutation of nodes).
- Canonical form: WL color histogram after convergence.
- Key result: message-passing GNNs are at most as powerful as 1-WL test for distinguishing non-isomorphic graphs.
- KB refs: `ML.GNN.WL_TEST.01`, `ML.GNN.GIN_EXPRESSIVITY.01`

**Example 2: Normalizing flows and change of variables**
- Objects: probability distributions on R^d.
- Canonical form: standard Gaussian N(0,I) as the base distribution.
- Map: invertible transformation f such that p(x) = N(f(x)) |det Jf(x)|.
- Any distribution expressible this way is equivalent to specifying f.
- KB refs: `ML.GENERATIVE.FLOW_MATCHING.01`, `ML.GENERATIVE.NORMALIZING_FLOW.01`

---

## Common Mistakes / Anti-Patterns

- **Canonical form is not unique.** If C(x) is not uniquely determined, it is not truly canonical — it is merely a normal form. Must verify condition (b): x ~ y iff C(x) = C(y).
- **Canonicalization is computationally hard.** Graph canonicalization is not known to be in P (though practical for most instances). If the reduction to canonical form is expensive, the proof strategy may be non-constructive.
- **Properties not invariant under ~.** Only properties preserved by the equivalence relation transfer from canonical form to the original. Verify invariance before transferring.
- **Confusing equivalence with equality.** Two Kraus representations being equivalent means they give the same channel, not that the operators are the same. Track the level of equivalence carefully.
- **Incomplete case analysis.** When classifying via canonical forms, must prove every object reduces to one of the listed forms. Forgetting edge cases (e.g., degenerate eigenvalues) leads to incomplete classification.
