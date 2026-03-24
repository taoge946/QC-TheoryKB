# Notation Concordance Table

> Cross-reference of notation conventions used across the standard references in this KB.
> Use this when reading derivations that cite multiple sources, or when writing a paper
> that draws on results from different textbooks.

---

## References Key

| Abbrev. | Full Reference |
|---------|---------------|
| **N&C** | Nielsen & Chuang, *Quantum Computation and Quantum Information* (2010) |
| **Watrous** | J. Watrous, *The Theory of Quantum Information* (2018) |
| **Preskill** | J. Preskill, *Lecture Notes on Quantum Information* (Caltech, Ch.2--7) |
| **Gottesman** | D. Gottesman, *Stabilizer Codes and Quantum Error Correction* (PhD thesis, 1997) |
| **Wilde** | M. Wilde, *Quantum Information Theory* (2nd ed., 2017) |
| **Roffe** | J. Roffe, *Quantum Error Correction: An Introductory Guide* (2019) |
| **Boyd** | S. Boyd & L. Vandenberghe, *Convex Optimization* (2004) |

---

## 1. Fidelity

| Aspect | N&C | Watrous | Preskill | Wilde |
|--------|-----|---------|----------|-------|
| **Symbol** | $F(\rho,\sigma)$ | $\mathrm{F}(\rho,\sigma)$ | $F(\rho,\sigma)$ | $F(\rho,\sigma)$ |
| **Definition** | $\left(\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}\right)^2$ | $\lVert\sqrt{\rho}\sqrt{\sigma}\rVert_1^2$ | $\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}$ (no square) | $\left(\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}\right)^2$ |
| **Squared?** | Yes | Yes (equivalent form) | **No** -- sometimes uses the "root fidelity" | Yes |
| **Range** | $[0,1]$ | $[0,1]$ | $[0,1]$ | $[0,1]$ |
| **Pure-state reduction** | $\lvert\langle\psi\lvert\phi\rangle\rvert^2$ | $\lvert\langle\psi\lvert\phi\rangle\rvert^2$ | $\lvert\langle\psi\lvert\phi\rangle\rvert$ or $\lvert\langle\psi\lvert\phi\rangle\rvert^2$ | $\lvert\langle\psi\lvert\phi\rangle\rvert^2$ |

**Equivalence note**: The Watrous form $\lVert\sqrt{\rho}\sqrt{\sigma}\rVert_1^2$ equals the N&C form $(\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}})^2$ because $\lVert A \rVert_1 = \mathrm{Tr}\sqrt{A^\dagger A}$ and $(\sqrt{\rho}\sqrt{\sigma})^\dagger(\sqrt{\rho}\sqrt{\sigma}) = \sqrt{\sigma}\,\rho\,\sqrt{\sigma}$, which shares non-zero eigenvalues with $\sqrt{\rho}\,\sigma\,\sqrt{\rho}$.

**Caution**: Preskill's lecture notes sometimes use $F$ without the square, so $F_{\text{Preskill}} = \sqrt{F_{\text{N\&C}}}$. Always check whether the source squares the trace or not. Some older papers (and Jozsa 1994) also use the unsquared version.

### Recommendation for your paper

Use the **N&C / Wilde convention with the square**: $F(\rho,\sigma) = \left(\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}\right)^2$. This is the most widely adopted convention in quantum computing papers today. State explicitly in the notation section that $F$ includes the square, to avoid ambiguity with the Preskill/Jozsa convention.

---

## 2. Trace Distance

| Aspect | N&C | Watrous | Preskill |
|--------|-----|---------|----------|
| **Symbol** | $D(\rho,\sigma)$ | $\frac{1}{2}\lVert\rho-\sigma\rVert_1$ | $D(\rho,\sigma)$ |
| **Definition** | $\frac{1}{2}\mathrm{Tr}\lvert\rho-\sigma\rvert$ | $\frac{1}{2}\lVert\rho-\sigma\rVert_1$ | $\frac{1}{2}\mathrm{Tr}\lvert\rho-\sigma\rvert$ |
| **Factor of 1/2** | Yes | Yes | Yes |
| **Range** | $[0,1]$ | $[0,1]$ | $[0,1]$ |

All major references agree on trace distance. The only variation is whether it is written using the trace norm $\lVert\cdot\rVert_1$ or the explicit $\mathrm{Tr}\lvert\cdot\rvert$ form.

### Recommendation for your paper

Use $T(\rho,\sigma) = \frac{1}{2}\lVert\rho-\sigma\rVert_1$ or $D(\rho,\sigma) = \frac{1}{2}\mathrm{Tr}\lvert\rho-\sigma\rvert$. Both are standard. If your paper uses many operator norms, prefer the $\lVert\cdot\rVert_1$ notation for consistency.

---

## 3. Quantum Channels

| Aspect | N&C | Watrous | Preskill |
|--------|-----|---------|----------|
| **Name** | "quantum operation" or "quantum channel" | "quantum channel" | "TPCP map" |
| **Symbol** | $\mathcal{E}$ | $\Phi$ | $\mathcal{E}$ or $\mathcal{N}$ |
| **Kraus / operator-sum** | $\mathcal{E}(\rho) = \sum_k E_k \rho E_k^\dagger$ | $\Phi(\rho) = \sum_k A_k \rho A_k^*$ | $\mathcal{E}(\rho) = \sum_\mu M_\mu \rho M_\mu^\dagger$ |
| **Kraus operators** | $\{E_k\}$ ("operation elements") | $\{A_k\}$ ("Kraus operators") | $\{M_\mu\}$ |
| **Completeness** | $\sum_k E_k^\dagger E_k = I$ (TP) | $\sum_k A_k^* A_k = \mathbb{1}$ (TP) | $\sum_\mu M_\mu^\dagger M_\mu = I$ (TP) |
| **Adjoint notation** | $\dagger$ | $*$ (Watrous uses $*$ for adjoint) | $\dagger$ |
| **Choi matrix** | $\chi$ matrix (process matrix) | $J(\Phi)$ (Choi representation) | not primary |
| **Stinespring** | $\mathcal{E}(\rho) = \mathrm{Tr}_E(V\rho V^\dagger)$ | $\Phi(X) = \mathrm{Tr}_{\mathcal{Z}}(VXV^*)$ | $\mathcal{E}(\rho) = \mathrm{Tr}_E(U\rho U^\dagger)$ |
| **CPTP** | "trace-preserving quantum operation" | "quantum channel" = CPTP | "TPCP map" |

**Key difference**: Watrous uses $*$ for the Hilbert-space adjoint where N&C and Preskill use $\dagger$. Watrous also prefers calligraphic $\mathcal{X}, \mathcal{Y}$ for Hilbert spaces and uses the Choi representation $J(\Phi)$ as the primary matrix representation of channels, whereas N&C uses the $\chi$-matrix (process matrix in a fixed Pauli basis).

### Recommendation for your paper

Use $\mathcal{E}$ or $\mathcal{N}$ with $\dagger$ for the adjoint (physics convention). Write the operator-sum as $\mathcal{E}(\rho) = \sum_k E_k \rho E_k^\dagger$. If you need the Choi matrix, use $J(\mathcal{E})$ following Watrous but keep $\dagger$ instead of $*$. State "CPTP map" or "quantum channel" -- both are understood.

---

## 4. Entropy

| Aspect | N&C | Watrous | Preskill | Wilde |
|--------|-----|---------|----------|-------|
| **Symbol** | $S(\rho)$ | $\mathrm{H}(\rho)$ | $S(\rho)$ | $H(\rho)$ |
| **Definition** | $-\mathrm{Tr}(\rho \log_2 \rho)$ | $-\mathrm{Tr}(\rho \log \rho)$ | $-\mathrm{Tr}(\rho \ln \rho)$ | $-\mathrm{Tr}(\rho \log_2 \rho)$ |
| **Log base** | $\log_2$ (bits) | $\log_2$ (stated as convention) | $\ln$ (nats, physics) | $\log_2$ (bits) |
| **Relative entropy** | $S(\rho\lVert\sigma)$ | $\mathrm{D}(\rho\lVert\sigma)$ | $S(\rho\lVert\sigma)$ or $D(\rho\lVert\sigma)$ | $D(\rho\lVert\sigma)$ |
| **Mutual information** | $S(A:B)$ or $I(A:B)$ | $\mathrm{I}(A:B)$ | $I(A:B)$ | $I(A;B)$ |
| **Conditional entropy** | $S(A\lvert B)$ | $\mathrm{H}(A\lvert B)$ | $S(A\lvert B)$ | $H(A\lvert B)$ |

**Log base matters**: When comparing numerical values across sources, remember $\log_2 x = \ln x / \ln 2$. Entropy in nats = entropy in bits $\times \ln 2$. The choice only affects numerical values, not the form of inequalities (SSA, data processing, etc.).

**Watrous note**: Although the derivation file `quantum_entropy_advanced.md` states "base 2 by convention" for Watrous, the original Watrous textbook uses $\log$ without specifying base in most theorems (the results hold for any base). The KB file adopts base 2.

### Recommendation for your paper

Use $S(\rho) = -\mathrm{Tr}(\rho \log_2 \rho)$ with $\log_2$ (bits) if writing for a quantum computing audience. Use $S(\rho) = -\mathrm{Tr}(\rho \ln \rho)$ (nats) if writing for a physics journal. State the convention once in your preliminaries. For relative entropy, $D(\rho\lVert\sigma)$ is the more common modern notation (over $S(\rho\lVert\sigma)$).

---

## 5. Pauli Group

| Aspect | Gottesman | N&C | Preskill | Roffe |
|--------|-----------|-----|----------|-------|
| **Pauli matrices** | $\sigma_x, \sigma_y, \sigma_z$ | $X, Y, Z$ | $\sigma_x, \sigma_y, \sigma_z$ or $X, Y, Z$ | $X, Y, Z$ |
| **Pauli group symbol** | $\mathcal{G}$ or $\mathcal{G}_n$ | $\mathcal{G}_n$ | $\mathcal{P}_n$ | $\mathcal{G}_n$ |
| **Phase factors** | $\{\pm 1, \pm i\}$ | $\{\pm 1, \pm i\}$ | $\{\pm 1, \pm i\}$ | $\{\pm 1, \pm i\}$ |
| **Group order** | $\lvert\mathcal{G}_n\rvert = 4 \cdot 4^n$ | $\lvert\mathcal{G}_n\rvert = 4 \cdot 4^n$ | same | same |
| **Pauli string notation** | $XZZXI$ (juxtaposition) | $X_1 Z_2 Z_3 X_4 I_5$ (subscripts) | both | $XZZXI$ (juxtaposition) |

**Gottesman vs. N&C on Paulis**: Gottesman's thesis uses $\sigma_x, \sigma_y, \sigma_z$ in exposition but switches to compact notation $XZZXI$ for code examples. N&C uses $X, Y, Z$ throughout. Modern QEC papers universally use $X, Y, Z$.

### Recommendation for your paper

Use $X, Y, Z$ (not $\sigma_x, \sigma_y, \sigma_z$) and $\mathcal{G}_n$ for the $n$-qubit Pauli group. Use juxtaposition for Pauli strings: $XZZXI$ rather than $X \otimes Z \otimes Z \otimes X \otimes I$. This is the standard in modern QEC literature.

---

## 6. Stabilizer Codes

| Aspect | Gottesman | N&C | Preskill | Roffe |
|--------|-----------|-----|----------|-------|
| **Code parameters** | $[n,k]$ or $[n,k,d]$ (single brackets) | $[[n,k,d]]$ (double brackets) | $[[n,k,d]]$ | $[[n,k,d]]$ |
| **Stabilizer group** | $S$ | $\mathcal{S}$ | $\mathcal{S}$ | $\mathcal{S}$ |
| **Generators** | $M_1, \ldots, M_{n-k}$ | $g_1, \ldots, g_{n-k}$ | $g_i$ | $g_i$ or $P_i$ |
| **Normalizer** | $N(S)$ | $N(\mathcal{S})$ | $N(\mathcal{S})$ | $N(\mathcal{S})$ |
| **Centralizer** | $C(S) = N(S)$ | $N(\mathcal{S})$ | $N(\mathcal{S})$ | $N(\mathcal{S})$ |
| **Codespace** | $T$ | $\mathcal{C}(\mathcal{S})$ or $V_S$ | $\mathcal{C}$ | codespace |
| **Logical operators** | $\bar{X}_i, \bar{Z}_i$ | $\bar{X}_i, \bar{Z}_i$ or $X_L, Z_L$ | $\bar{X}, \bar{Z}$ | $X_L, Z_L$ |
| **Projector onto codespace** | $\sum_{M \in S} M / \lvert S\rvert$ | $\prod_i \frac{I + g_i}{2}$ | same | same |
| **Syndrome** | $f(E) \in \mathbb{Z}_2^{n-k}$ | $\mathbf{s}(E) \in \mathbb{F}_2^{n-k}$ | syndrome vector | syndrome |

**Bracket convention**: Gottesman's thesis often uses single brackets $[n,k,d]$ (or $[n,k]$ when distance is unspecified). The double-bracket $[[n,k,d]]$ convention is now universal in QEC papers and distinguishes quantum codes from classical $[n,k,d]$ codes.

**Gottesman's centralizer = normalizer**: For Pauli groups, $C(S) = N(S)$ because any $A \in \mathcal{G}_n$ satisfies $A^\dagger M A = \pm M$, and since $-I \notin S$, commuting ($AMA^\dagger = M$) is equivalent to normalizing.

### Recommendation for your paper

Use $[[n,k,d]]$ with double brackets. Use $\mathcal{S}$ (calligraphic) for the stabilizer group with generators $g_1, \ldots, g_{n-k}$. Use $\bar{X}_i, \bar{Z}_i$ for logical operators (the overbar convention is the most common). For the codespace, $\mathcal{C}$ or $C_{\mathcal{S}}$ are both fine.

---

## 7. Hilbert Space and Operators

| Aspect | N&C | Watrous | Preskill |
|--------|-----|---------|----------|
| **Hilbert space** | $\mathcal{H}$ | $\mathcal{X}, \mathcal{Y}$ (complex Euclidean spaces) | $\mathcal{H}$ |
| **Density operators** | $\rho \geq 0, \mathrm{Tr}(\rho)=1$ | $\rho \in \mathrm{D}(\mathcal{X})$ | $\rho$ |
| **Set of density ops** | not formalized | $\mathrm{D}(\mathcal{X})$ | not formalized |
| **Set of positive ops** | not formalized | $\mathrm{Pos}(\mathcal{X})$ | not formalized |
| **Set of linear ops** | $\mathcal{L}(\mathcal{H})$ | $\mathrm{L}(\mathcal{X})$ | $\mathcal{L}(\mathcal{H})$ |
| **Identity** | $I$ | $\mathbb{1}$ or $\mathbb{1}_{\mathcal{X}}$ | $I$ or $\mathbb{1}$ |
| **Adjoint** | $A^\dagger$ | $A^*$ | $A^\dagger$ |
| **Trace norm** | $\lVert A \rVert_{\mathrm{tr}}$ | $\lVert A \rVert_1$ | $\lVert A \rVert_1$ |
| **Tensor product** | $\otimes$ | $\otimes$ | $\otimes$ |
| **Partial trace** | $\mathrm{Tr}_B$ | $\mathrm{Tr}_{\mathcal{Y}}$ | $\mathrm{Tr}_B$ |
| **Dimension** | $d$ or $N$ | $\dim(\mathcal{X})$ | $d$ |

**Watrous's $*$ vs $\dagger$**: This is purely a convention difference. Watrous writes $A^*$ where physicists write $A^\dagger$. Both mean the conjugate transpose.

**Watrous's complex Euclidean spaces**: Watrous works with $\mathcal{X} = \mathbb{C}^n$ as "complex Euclidean spaces" rather than abstract Hilbert spaces. This is mathematically more precise but functionally identical for finite dimensions.

### Recommendation for your paper

Use $\mathcal{H}$ for Hilbert spaces, $\dagger$ for the adjoint, $I$ for the identity, and $\mathrm{Tr}_B$ for partial trace. These are the standard physics conventions. If you need Watrous's formal sets, write $\mathrm{D}(\mathcal{H})$ for density operators and $\mathrm{Pos}(\mathcal{H})$ for positive operators.

---

## 8. Quantum Error Correction

| Aspect | N&C | Gottesman | Preskill | Roffe |
|--------|-----|-----------|----------|-------|
| **Knill-Laflamme condition** | $\langle\psi_i\lvert E_a^\dagger E_b \lvert\psi_j\rangle = C_{ab}\delta_{ij}$ | $\langle\psi_i\lvert E_a^\dagger E_b \lvert\psi_j\rangle = \delta_{ab}\delta_{ij}$ (nondegenerate) | same as N&C | same as N&C |
| **Error model** | $\mathcal{E}(\rho) = \sum_k E_k \rho E_k^\dagger$ | errors $E \in \mathcal{G}_n$ | TPCP map | errors $E \in \mathcal{G}_n$ |
| **Recovery** | $\mathcal{R}$ | $R$ (Pauli correction) | $\mathcal{R}$ | $\mathcal{R}$ |
| **Code distance** | $d = \min_{E \in N(\mathcal{S})\setminus\mathcal{S}} \mathrm{wt}(E)$ | same | same | same |
| **Correctable errors** | weight $\leq t = \lfloor(d-1)/2\rfloor$ | same | same | same |
| **Degenerate code** | $C_{ab} \neq \delta_{ab}$ in KL condition | $S$ contains elements of weight $< d$ | same concept | same |

### Recommendation for your paper

Use the full Knill-Laflamme condition $\langle i \lvert E_a^\dagger E_b \lvert j \rangle = C_{ab}\delta_{ij}$ (allows degenerate codes). For stabilizer-specific results, the syndrome-based formulation from Gottesman is cleaner.

---

## 9. Common Symbols Quick Reference

| Concept | Recommended Symbol | Alternatives to Watch For |
|---------|--------------------|--------------------------|
| Fidelity | $F(\rho,\sigma)$ (squared) | $f(\rho,\sigma)$ (unsquared, Jozsa/Preskill) |
| Trace distance | $D(\rho,\sigma)$ or $T(\rho,\sigma)$ | $d(\rho,\sigma)$, $\delta(\rho,\sigma)$ |
| Von Neumann entropy | $S(\rho)$ | $H(\rho)$ (Watrous, Wilde, info-theory) |
| Relative entropy | $D(\rho\lVert\sigma)$ | $S(\rho\lVert\sigma)$ (N&C) |
| Mutual information | $I(A:B)$ | $I(A;B)$ (semicolon, Wilde), $S(A:B)$ |
| Quantum channel | $\mathcal{E}$ or $\mathcal{N}$ | $\Phi$ (Watrous), $\Lambda$ |
| Pauli group | $\mathcal{G}_n$ | $\mathcal{P}_n$ (Preskill) |
| Stabilizer group | $\mathcal{S}$ | $S$ (Gottesman, but ambiguous with entropy) |
| Code parameters | $[[n,k,d]]$ | $[n,k,d]$ (Gottesman thesis, classical) |
| Logical operators | $\bar{X}, \bar{Z}$ | $X_L, Z_L$ (subscript $L$) |
| Identity | $I$ | $\mathbb{1}$ (Watrous, common in European literature) |
| Adjoint | $A^\dagger$ | $A^*$ (Watrous, math convention) |

---

## 10. Unit and Base Conventions

| Convention | Used by | Context |
|------------|---------|---------|
| $\log_2$ (bits) | N&C, Wilde, most QC papers | Quantum computing, information theory |
| $\ln$ (nats) | Preskill, statistical mechanics texts | Physics, thermodynamics |
| $\log$ (unspecified) | Watrous (theorems hold for any base) | Pure mathematics |

**Conversion**: $S_{\text{nats}} = S_{\text{bits}} \times \ln 2$. All entropy inequalities (SSA, subadditivity, data processing) hold regardless of log base.

### Recommendation for your paper

Use $\log$ to mean $\log_2$ and state this once. If targeting a physics journal (e.g., PRA, PRX Quantum), $\ln$ is also acceptable but less common in quantum computing contexts.
