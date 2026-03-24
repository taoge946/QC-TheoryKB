# Anyonic Models and Topological Quantum Computation

> **Tags**: `anyons`, `topological-order`, `toric-code`, `fault-tolerance`, `kitaev`

## Statement **[Kitaev 2003; Dennis et al. 2002, §2.3]**

Anyonic excitations in 2D quantum systems with topological order provide a framework for intrinsically fault-tolerant quantum computation. In Kitaev's toric code model, two types of abelian anyons (electric charges and magnetic vortices) exhibit mutual Aharonov-Bohm phases. The ground state degeneracy on a genus-$g$ surface is $4^g$, protected by the energy gap up to exponentially small corrections. Non-abelian anyons (from more general models) could provide universal quantum computation through braiding.

## Prerequisites

- **Toric Code**: [surface_code_basics.md]
- **Stabilizer Formalism**: [stabilizer_formalism.md]
- **Homology**: [../../08_topology/derivations/homology_basics.md]

---

## Toric Code Hamiltonian **[Kitaev 2003, §1, Eq.(2)]**

On a $k \times k$ square lattice on the torus with $n = 2k^2$ qubits on edges:

$$H_0 = -\sum_s A_s - \sum_p B_p$$

where $A_s = \prod_{j \in \text{star}(s)} \sigma_j^x$ and $B_p = \prod_{j \in \text{boundary}(p)} \sigma_j^z$.

**Properties**:
- Ground state = protected subspace of $\text{TOR}(k)$
- $4$-fold degenerate (genus 1)
- Energy gap $\Delta E \geq 2$
- All excited states separated from ground state

---

## Particle Excitations **[Kitaev 2003, §2]**

### String Operators

$$S^z(t) = \prod_{j \in t} \sigma_j^z, \qquad S^x(t') = \prod_{j \in t'} \sigma_j^x$$

where $t$ is a path on the lattice and $t'$ a path on the dual lattice **[Kitaev 2003, §2, Eq.(3)]**.

### Two Types of Anyons

- **$z$-type particles ("electric charges")**: created at endpoints of $S^z(t)$, live on vertices. Violation of $A_s|\xi\rangle = |\xi\rangle$.
- **$x$-type particles ("magnetic vortices")**: created at endpoints of $S^x(t')$, live on faces. Violation of $B_p|\xi\rangle = |\xi\rangle$.

Particles always created in pairs (conservation of charge/vorticity mod 2) **[Kitaev 2003, §2]**.

### Anyonic Phase **[Kitaev 2003, §2]**

When an $x$-type particle moves around a $z$-type particle:

$$|\Psi_\text{final}\rangle = S^x(c) S^z(t) |\psi^x(q)\rangle = -|\Psi_\text{initial}\rangle$$

because $S^x(c)$ and $S^z(t)$ anticommute (the closed path $c$ crosses $t$ once). The global wavefunction acquires phase $-1$. This is characteristic of **abelian anyons** **[Kitaev 2003, §2]**.

No phase change occurs when particles of the same type braid around each other.

---

## Ground State Degeneracy from Anyons **[Kitaev 2003, §2]**

### Einarsson's Argument

Moving a $z$-type particle along loop $c_{z1}$ on the torus corresponds to operator $Z_1$. Moving an $x$-type particle along $c_{x1}$ corresponds to $X_1$. Consider:

$$W = X_1^{-1} Z_1^{-1} X_1 Z_1$$

This is topologically equivalent to winding one particle around the other, giving $W = -1$. Therefore $X_1$ and $Z_1$ anticommute **[Kitaev 2003, §2]**.

Since $X_1, Z_1$ anticommute but both commute with $H_0$, the ground state must be degenerate. For genus-$g$: $4^g$-fold degeneracy.

### Generalization **[Dennis et al. 2002, §2.3]**

For anyons with Aharonov-Bohm phase $\exp(2\pi i p/q)$ (with $\gcd(p,q) = 1$):
- Torus: $q^{2g}$-fold degeneracy
- Annulus: $q$-fold degeneracy
- Disc with $h$ holes: $q^h$-fold degeneracy

---

## Stability Under Perturbation **[Kitaev 2003, §1]**

For perturbation $V = -\vec{h}\sum_j \vec{\sigma}_j - \sum_{j<p} J_{jp}(\vec{\sigma}_j, \vec{\sigma}_p)$:

The ground state energy splitting appears only in the $\lceil k/2 \rceil$-th or higher order of perturbation theory. The splitting vanishes as $\exp(-ak)$ in the thermodynamic limit.

**Physical interpretation**: Virtual particles must tunnel around a non-contractible loop of length $\geq k$ before reannihilating. The tunneling amplitude is:

$$b_{\alpha i} \sim \exp(-a_\alpha L_i), \qquad a_\alpha \sim \sqrt{2m\Delta E}$$

where $m$ is the effective mass and $\Delta E$ the gap **[Kitaev 2003, §2]**.

---

## Materialized Symmetry **[Kitaev 2003, §3]**

The system exhibits a **dynamically created** $\mathbb{Z}_2 \times \mathbb{Z}_2$ symmetry at large distances:
- Electric charge conserved mod 2
- Magnetic charge conserved mod 2

This symmetry is not explicitly present in the Hamiltonian (which has no gauge symmetry) but emerges as a physical local symmetry through the introduction of auxiliary degrees of freedom **[Kitaev 2003, §3]**.

The edge labels $z_j$ (measurable by $\sigma_j^z$) correspond to a $\mathbb{Z}_2$ vector potential. $\sigma_j^x$ corresponds to the electric field. $A_s$ operators are local gauge transformations; $B_p$ is the magnetic field on face $p$.

---

## Physical Fault Tolerance **[Dennis et al. 2002, §2.3]**

The toric code Hamiltonian provides **physical fault tolerance**: protection against decoherence without active information processing. At sufficiently low temperature $T$:

- Defect nucleation suppressed by Boltzmann factor $\exp(-\Delta/kT)$
- Encoded information stored in Aharonov-Bohm phases of quasiparticles around non-trivial cycles
- Memory lifetime grows exponentially with system size (below critical temperature)

For a weakly perturbed finite system, the degeneracy splitting is:

$$A \sim C \exp\left(-\sqrt{2}(m^* \Delta)^{1/2} L/\hbar\right)$$

negligible when system size $L$ is large compared to characteristic length $l = \hbar(m^*\Delta)^{-1/2}$ **[Dennis et al. 2002, §2.3]**.

---

## Towards Non-Abelian Anyons **[Kitaev 2003, §4-8]**

Kitaev's paper also introduces models with **non-abelian anyons** based on Hopf algebras, where:
- The $n$-particle state space is degenerate (particles at fixed positions)
- Moving one particle around another produces a non-trivial **unitary transformation** (not just a phase)
- Braiding operations provide a basis for fault-tolerant quantum computation
- Measurement via fusion: bringing particles together and observing the result

The non-abelian case requires qubit Hilbert space dimension $> 2$ and involves the theory of modular tensor categories.

---

## References

- Kitaev, A. Yu. "Fault-tolerant quantum computation by anyons." Ann. Phys. 303, 2-30 (2003). arXiv:quant-ph/9707021.
- Dennis, E., Kitaev, A., Landahl, A. & Preskill, J. "Topological quantum memory." J. Math. Phys. 43, 4452 (2002).
- Einarsson, T. "Fractional statistics on a torus." PRL 64, 1995 (1990).
- Wen, X. G. "Topological orders in rigid states." Int. J. Mod. Phys. B 4, 239 (1990).
