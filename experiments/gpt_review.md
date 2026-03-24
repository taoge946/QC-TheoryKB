# QC-TheoryKB Independent Review Report

> **Date**: 2026-03-24
> **Reviewers**: GPT-5.4 (via Chrome DevTools MCP) + Claude Opus 4.6 (self-review agents)
> **Files Reviewed**: BUILDING_BLOCKS.md (structure) + 3 derivation files (math correctness)

---

## 1. BUILDING_BLOCKS.md Structural Review (by GPT-5.4)

### Overall Assessment
GPT's verdict: **"Right now this is a strong personal notebook pretending to be a theorem KB."**

### 1.1 Missing Important Proof Goals

GPT identified **8 major gaps**:

| # | Missing Area | Why It Matters |
|---|-------------|----------------|
| A | **Quantum complexity** (BQP/QMA/QCMA, query complexity, oracle separations) | Cannot support quantum-theory papers without this |
| B | **Hamiltonian simulation** (Trotter/Suzuki, qDRIFT, LCU, block-encoding) | Huge hole for quantum algorithms |
| C | **Tensor networks** (MPS, PEPS, area law, contraction complexity) | Needed for simulation, circuit compression, entanglement |
| D | **Information-theoretic security** (min-entropy, leftover hash, privacy amplification) | Required for QKD, verification, certification |
| E | **Open quantum systems** (Lindblad, GKLS, diamond norm, Pauli twirling) | Current noise layer too QEC-centric |
| F | **Concentration/matrix inequalities** (matrix Bernstein, Levy's lemma, Weyl, Davis-Kahan) | Substrate for barren plateaus, generalization, spectral stability |
| G | **QML theory** (barren plateau proofs, expressivity-trainability tradeoff, quantum kernel generalization) | ML block is method-heavy, not theory-balanced |
| H | **Statistical inference** (multiple comparison, bootstrap, power analysis, calibration drift) | F17 block too narrow |

### 1.2 Part 2 Proof Patterns: "These are paper narratives, not proof patterns"

GPT proposes replacing the current 7 domain-specific patterns (A-G) with **10 domain-agnostic proof patterns**:

1. **Reduction/completeness** — reduce known hard problem, preserve structure
2. **Monotonicity/information inequality** — apply DPI/contractivity/convexity
3. **Variational decomposition** — ELBO decompose, isolate terms, optimize surrogate
4. **Relaxation-rounding/approximation sandwich** — relax, solve, round, bound gap
5. **Perturbation/stability** — define ideal, inject noise, propagate via Lipschitz
6. **Concentration/generalization** — define estimator, concentration, uniform convergence
7. **Achievability vs converse** — construct scheme + prove converse = characterize gap
8. **Canonical-form/equivalence** — transform preserves semantics, map to normal form
9. **Asymptotic-to-finite-size** — leading order + remainder bound
10. **Mechanism-isolation/ablation-to-causality** — formalize contribution decomposition

### 1.3 F-code Numbering Issues

- F11 is too heterogeneous (diffusion+GNN+RL+GAN+flow matching in one bucket)
- Position-based IDs are brittle for expansion
- GPT suggests: **semantic IDs** (e.g., `QEC.KL.01`) + numeric aliases for backward compatibility

### 1.4 Structural Problems

- Part 1 mixes 3 incompatible dimensions (proof intent / domain / artifact type)
- Granularity inconsistent (some entries are single theorems, some are entire method families)
- Missing: assumption registry, prerequisite DAG, "don't use this when..." field

---

## 2. concentration_inequalities.md Math Review (by CC Agent)

### Grade: B-

### ERRORS: 0 confirmed (2 CC false positives corrected by GPT)

**~~E1. Chernoff δ>1~~ → FALSE POSITIVE (GPT corrected)**
- CC agent claimed $e^{-\mu\delta/3}$ was wrong. GPT proved it IS correct: $\delta^2/(2+\delta) \geq \delta/3$ when $\delta \geq 1$.

**~~E2. McDiarmid-Azuma factor-of-4~~ → FALSE POSITIVE (GPT corrected)**
- CC agent flagged factor-of-4 discrepancy. GPT explained: Azuma uses $|D_i| \leq c_i$ (symmetric, range $2c_i$), McDiarmid uses interval length $\leq c_i$. Factor of 4 is the correct gain from tighter hypothesis.
- **Remaining issue**: The KB proof conflates these conventions without explanation. Should clarify.

### WARNINGS (5)
- W1: Bennett's $\sigma^2$ convention changes between Bennett and Bernstein sections
- W2: Chernoff lower tail missing $\delta \in (0,1)$ restriction
- W3: Bernstein proof is just a pointer, not a real proof
- W4: Sub-Gaussian equivalences too imprecise
- W5: QAOA application conflates edges with independent random inputs

### CITATION ISSUES
- **Zero external citations** — no textbook, no paper, no theorem number. Unacceptable for a reference KB.
- Missing: Hoeffding (1963), Bernstein (1924), McDiarmid (1989), Azuma (1967), Boucheron-Lugosi-Massart (2013)

---

## 3. diffusion_models_math.md Math Review (by CC Agent)

### Grade: B+

### ERRORS (1 definite, 2 notation issues)

**E1. Classifier-Free Guidance formula (line 308)**
- File uses: $\tilde{s} = s_\varnothing + (1+w)[s_c - s_\varnothing]$
- Standard (Ho & Salimans 2022): $\tilde{s} = s_\varnothing + w[s_c - s_\varnothing]$
- Non-standard parameterization without flagging it. Confusing for readers comparing with original.

**Notation issues**:
- $\beta_t$ vs $1-\alpha_t$ used interchangeably (line 169 vs 324)
- Bold vs non-bold vectors switches mid-document (line 340)
- Score function $\nabla_{x_t}$ vs $\nabla_x$ inconsistent

### SKIPPED STEPS (5)
- S1: VLB telescoping derivation (Part 4.1) — the most important step is hand-waved
- S2: KL divergence of two Gaussians formula not stated
- S3: Posterior mean simplification algebra terse
- S4: Marginal consistency lemma "cross terms cancel" without showing integral
- S5: Anderson reverse SDE stated without proof

### CITATIONS
- **Excellent** — nearly all equation numbers verified correct against Ho et al. and Song et al. source tex
- One imprecise: VP-SDE cited as [Song et al. 2021, Eq.(5)] but should be Eq.(22)/(32)
- Duplicate references section

---

## 4. stabilizer_formalism.md Math Review (by CC Agent)

### Grade: B-

### ERRORS (6 definite)

**E1. [MAJOR] Phantom N&C theorem citations**
- "Theorem 10.3, p.457" (line 73) and "Theorem 10.4, p.458" (lines 178, 385-388) — **these theorems do not exist in N&C**. N&C Ch.10 contains only Theorems 10.1, 10.2, 10.6, 10.7, 10.8. The content is real but appears as unnumbered definitions, not numbered theorems.

**E2. [MAJOR] Threshold Theorem citation wrong**
- File cites "Theorem 10.6, p.480" for the Threshold Theorem
- N&C Theorem 10.6 (p.462) is about **Clifford gates**, not fault tolerance
- The Threshold Theorem in N&C is **unnumbered**, on p.516

**E3. Pauli group order inconsistency**
- Step 1: $|\mathcal{G}_n| = 4 \cdot 4^n = 2^{2n+2}$ (Gottesman convention, $\pm i$ phases)
- Preskill section: $|G_n| = 2^{2n+1}$ ($\pm$ phases only)
- Presented without noting they use **different conventions**. Direct contradiction at face value.

**E4. Single-qubit group order contradiction**
- Step 1: $|\mathcal{G}_1| = 16$ (with $\pm i$)
- Preskill: $|G_1| = 8$ (without $\pm i$)
- Never reconciled in the document.

**E5. Gottesman's "quaternionic group" claim uncritically quoted**
- Preskill explicitly says it is NOT the quaternion group but "the symmetry group of the square"
- File quotes Gottesman without flagging the discrepancy.

**E6. Shor code generators differ between sections without explanation**
- Gottesman: $M_1 = Z_1Z_2, M_2 = Z_1Z_3, ...$
- Preskill: $Z_1Z_2, Z_2Z_3, Z_4Z_5, Z_5Z_6, ...$
- Both generate the same stabilizer group but via different generator choices. Not noted.

### WARNINGS (8)
- W1: Shor code codeword normalization missing in Gottesman section
- W2: Five-qubit code codeword not normalized ($1/4$ factor missing)
- W3: "Every element squared = $\pm I$" statement imprecise
- W4: $|N(\mathcal{S})| = 4 \cdot 2^{n+k}$ stated without proof
- W5: Syndrome additivity $\mathbf{s}(E_1 E_2) = \mathbf{s}(E_1) \oplus \mathbf{s}(E_2)$ proof missing
- W6: Steane's binary vector example has untracked phase ($-i$ from $Y = -iXZ$)
- W7: CSS code distance formula inconsistent between N&C and Steane versions
- W8: Clifford gates page number off by 1 (p.461 vs actual p.462)

### CITATION ISSUES
- **3 phantom theorem numbers** (10.3, 10.4, and misattributed 10.6) — anyone checking would find they don't exist
- Fowler 2025 reference extremely vague (no arXiv ID)
- Convention conflicts ($H_x|H_z$ vs $H_Z|H_X$ ordering) between Steane and Preskill not reconciled

### KEY INSIGHT
The file is a **compilation** from 7+ sources (Gottesman, N&C, Preskill, Roffe, Steane, Bacon, Fujii) but fails to reconcile their different conventions. Steps 1-6 core derivation is correct; the surrounding reference material has convention conflicts that would confuse readers.

---

## 5. GPT Math Reviews (Tabs 2 & 3)

### 5.1 GPT Tab 2: DDPM + Concentration Inequalities

**DDPM verdict**: All formulas confirmed correct (posterior variance, mean, ε-substitution, L_simple).
- Minor citation issue: the pointwise $L_{t-1}$ formula should cite Eq.(8) not Eq.(12); Eq.(12) is the ε-parameterized version
- Should explicitly state $t \sim \text{Uniform}(\{1,...,T\})$ in $L_{\text{simple}}$

**Chernoff δ>1**: GPT proved $e^{-\mu\delta/3}$ IS correct. Key: $\delta^2/(2+\delta) \geq \delta/3 \iff 2\delta \geq 2 \iff \delta \geq 1$.

**McDiarmid-Azuma**: GPT confirmed NOT an error. Azuma uses symmetric bound $|D_i| \leq c_i$ (range $2c_i$, gives $c_i^2/2$). McDiarmid uses interval length $\leq c_i$ (gives $c_i^2/8$). The factor of 4 is the correct gain. KB proof should clarify the convention difference.

### 5.2 GPT Tab 3: Stabilizer Formalism

**Core claims confirmed correct**: dimension formula, projector normalization, syndrome convention, distance formula.

**Issues found (consistent with CC agent)**:
- Pauli group order: $4^{n+1}$ correct for $\pm i$ convention, $2^{2n+1}$ for Preskill's $\pm$ convention. **Not reconciled in document.**
- Error correction proof: "distinct syndromes" is wrong for degenerate codes. Correct condition: $E_a^\dagger E_b \notin N(S)\setminus S$.
- GPT provides the complete correct proof: if $\text{wt}(E_a^\dagger E_b) < d$, then either $E_a^\dagger E_b \in S$ (harmless degeneracy) or $E_a^\dagger E_b \notin N(S)$ (distinguishable by syndrome).

---

## 6. Cross-Review Analysis: CC Agent vs GPT Agreement

| Finding | CC Agent | GPT | Verdict |
|---------|----------|-----|---------|
| Chernoff δ>1 bound | ERROR | CORRECT | **GPT right** — CC false positive |
| McDiarmid-Azuma factor | ERROR | NOT ERROR (convention diff) | **GPT right** — CC false positive |
| Stabilizer Pauli group convention | ERROR (inconsistency) | CONFIRMED inconsistency | **Both agree** |
| Phantom N&C Theorem 10.3/10.4 | ERROR | Not tested (not sent) | CC finding stands |
| Threshold Theorem citation | ERROR | Not tested | CC finding stands |
| CFG non-standard parameterization | ERROR | Not tested | CC finding stands |
| Degenerate code proof gap | WARNING | CONFIRMED gap | **Both agree** |
| Zero citations in concentration | ISSUE | Not tested | CC finding stands |

**Key insight**: CC agents found 2 false positives on concentration inequalities that GPT corrected. This validates the multi-reviewer approach.

---

## Summary of Action Items

### Priority 1: Fix Errors (CRITICAL — would embarrass if cited in a paper)
- [ ] **stabilizer_formalism.md**: Remove phantom N&C Theorem 10.3, 10.4 citations — these don't exist
- [ ] **stabilizer_formalism.md**: Fix Threshold Theorem citation (not Theorem 10.6 p.480; it's unnumbered, p.516)
- [ ] **stabilizer_formalism.md**: Reconcile Pauli group order conventions ($2^{2n+2}$ vs $2^{2n+1}$)
- [ ] ~~**concentration_inequalities.md**: Fix Chernoff δ>1~~ → GPT confirmed it's correct
- [ ] ~~**concentration_inequalities.md**: Fix McDiarmid-Azuma factor-of-4~~ → GPT confirmed not an error, but clarify convention in proof
- [ ] **diffusion_models_math.md**: Fix or flag CFG non-standard $(1+w)$ parameterization

### Priority 2: Add Missing Content
- [ ] **concentration_inequalities.md**: Add ALL external citations (currently zero — Hoeffding 1963, Bernstein 1924, McDiarmid 1989, Azuma 1967, Boucheron-Lugosi-Massart 2013)
- [ ] **diffusion_models_math.md**: Fill in VLB telescoping derivation (most important step, currently hand-waved)
- [ ] **concentration_inequalities.md**: Add real Bernstein inequality proof (currently just a pointer)
- [ ] **stabilizer_formalism.md**: Add convention reconciliation section (Gottesman vs Preskill vs N&C)

### Priority 3: Structural Improvements (from GPT)
- [ ] Add missing KB modules: quantum complexity, Hamiltonian simulation, tensor networks, security, open systems, matrix concentration
- [ ] Replace Part 2 paper narratives with domain-agnostic proof patterns
- [ ] Split oversized F11 module into sub-namespaces
- [ ] Add assumption registry, prerequisite DAG, and "don't use when..." fields
