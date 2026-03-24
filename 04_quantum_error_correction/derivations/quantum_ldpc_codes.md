# Quantum LDPC Codes

> **Tags**: `ldpc`, `qec`, `product-codes`, `hyperbolic`, `constant-overhead`

## Statement **[Breuckmann & Eberhardt, §2.1.2]**

Quantum low-density parity-check (LDPC) codes are stabilizer codes where the number of qubits per check and checks per qubit are bounded by a constant. Unlike surface codes (where $k = O(1)$ and $d = O(\sqrt{n})$), quantum LDPC codes aim for $k, d$ scaling with $n$. Recent breakthroughs have surpassed the $\text{polylog}(n)\sqrt{n}$ distance barrier.

## Prerequisites

- **CSS Codes**: [css_codes.md]
- **Chain Complexes**: [../../08_topology/derivations/homology_basics.md]
- **Code Distance Bounds**: [code_distance_bounds.md]

---

## Definition **[Breuckmann & Eberhardt, §2.1.2]**

A family of stabilizer codes is LDPC if:
1. The number of qubits participating in each check is bounded by a constant
2. The number of checks acting on each qubit is bounded by a constant

For CSS codes: the Hamming weight of each row and column of $H_X$ and $H_Z$ is bounded by a constant.

**Open Problem** **[Breuckmann & Eberhardt]**: Do **good** quantum LDPC codes exist ($k \in \Theta(n)$ and $d \in \Theta(n)$)?

---

## Geometric Constructions

### Hyperbolic Surface Codes **[Breuckmann & Eberhardt, §3.1.1]**

Defined on tessellations of hyperbolic surfaces (negative curvature). By the Gauss-Bonnet-Chern theorem, the dimension of $H_1$ grows linearly with volume, giving constant encoding rate.

For regular tessellation with $r$-gons, $s$ meeting at each vertex:

$$k = \left(1 - \frac{2}{r} - \frac{2}{s}\right) n + 2$$

Parameters: $k \in \Theta(n)$, $d \in \Theta(\log n)$. Despite logarithmic distance, a threshold under minimum-weight decoding exists **[Breuckmann & Eberhardt, §3.1.1]**.

### 4D Hyperbolic Codes (Guth-Lubotzky) **[Breuckmann & Eberhardt, §3.1.2]**

Parameters: $k \in \Theta(n)$, $d \in \Omega(n^{0.1})$. Upper bound for arithmetic 4D hyperbolic manifolds: $d \leq O(n^{0.3})$. Local decoding strategy by Hastings corrects errors up to size $\log(n)$ **[Breuckmann & Eberhardt, §3.1.2]**.

### Freedman-Meyer-Luo Codes **[Breuckmann & Eberhardt, §3.2]**

Parameters: $[[n, 2, \Omega(\sqrt[4]{\log n} \cdot \sqrt{n})]]$. Construction uses hyperbolic surfaces $\Sigma_g$, Cartesian product with interval, identification with twist of length $\sqrt{\text{sys}_1(\Sigma_g)}$, surgery, and product with a loop. The 2-systole determines the distance **[Breuckmann & Eberhardt, §3.2]**.

---

## Product Constructions **[Breuckmann & Eberhardt, §4]**

### Hypergraph Product (Tillich-Zemor) **[Breuckmann & Eberhardt, §4.1]**

The tensor product of two classical codes yields a quantum CSS code. The toric code arises as the hypergraph product of two repetition codes.

For two good classical $[n, k, d]$ LDPC codes with $k \in \Theta(n)$ and $d \in \Theta(n)$: the hypergraph product gives a quantum code with $k \in \Theta(n)$ and $d \in \Theta(\sqrt{n})$ **[Breuckmann & Eberhardt, §4.1]**.

### Fibre Bundle Codes **[Breuckmann & Eberhardt, §4.3]**

Introduce a twist in the tensor product (analogous to fibre bundles in topology). Parameters: $k \in \Theta(n^{3/5}/\text{polylog}(n))$, $d \in \Omega(n^{3/5}/\text{polylog}(n))$ **[Breuckmann & Eberhardt, §4.3]**.

### Lifted Product Codes **[Breuckmann & Eberhardt, §4.4]**

Parameters: $k \in \Theta(n^\alpha \log n)$, $d \in \Omega(n^{1-\alpha}/\log n)$ for tunable $\alpha$. These generalize the hypergraph product by allowing group actions **[Breuckmann & Eberhardt, §4.4]**.

### Balanced Product Codes **[Breuckmann & Eberhardt, §4.5]**

Parameters: $k \in \Theta(n^{4/5})$, $d \in \Omega(n^{3/5})$. Achieve better parameter trade-offs through balanced quotient constructions **[Breuckmann & Eberhardt, §4.5]**.

---

## Constant Overhead Fault Tolerance **[Breuckmann & Eberhardt, §5]**

**Gottesman's Theorem** (2013): Quantum LDPC codes with constant encoding rate $k/n$ can reduce the overhead of fault-tolerant quantum computation to a **constant**. This contrasts with surface-code-based schemes where overhead grows with computation length.

---

## Challenges **[Breuckmann & Eberhardt, §5]**

1. **Non-local connectivity**: Unlike surface codes (2D planar layout), LDPC codes generally require non-local qubit interactions
2. **Decoding**: Standard decoders (MWPM) may not apply; belief propagation with post-processing (OSD) is promising
3. **Syndrome extraction circuits**: Parallelized extraction circuits that preserve the LDPC property are needed
4. **Single-shot decoding**: Some codes (e.g., 4D hyperbolic) have intrinsic robustness against measurement errors

---

## Haah's Cubic Code **[Breuckmann & Eberhardt, §3.3]**

Defined on a 3D cubic lattice of size $L^3$ with two qubits per site. Number of encoded qubits grows with $L$ in a non-trivial way. Distance bounds: $\Omega(n^{1/3}) \leq d \leq O(n^{2/3})$. Logical operators are fractals. Candidate for self-correcting quantum memory **[Breuckmann & Eberhardt, §3.3]**.

---

## Summary: Best Known Quantum LDPC Parameters

| Code Family | $k$ | $d$ | Source |
|------------|-----|-----|--------|
| Surface/toric | $O(1)$ | $O(\sqrt{n})$ | Kitaev 1997 |
| 2D hyperbolic | $\Theta(n)$ | $\Theta(\log n)$ | Breuckmann et al. |
| 4D hyperbolic | $\Theta(n)$ | $\Omega(n^{0.1})$ | Guth-Lubotzky |
| Hypergraph product | $\Theta(n)$ | $\Theta(\sqrt{n})$ | Tillich-Zemor |
| Fibre bundle | $\Theta(n^{3/5})$ | $\Omega(n^{3/5})$ | Hastings-Haah-O'Donnell |
| Balanced product | $\Theta(n^{4/5})$ | $\Omega(n^{3/5})$ | Breuckmann-Eberhardt |

---

## References

- Breuckmann, N. P. & Eberhardt, J. N. "Quantum LDPC Codes." PRX Quantum 2, 040101 (2021).
- Tillich, J.-P. & Zemor, G. "Quantum LDPC codes with positive rate and minimum distance proportional to the square root of the blocklength." IEEE Trans. Inf. Theory 60, 1193 (2014).
- Gottesman, D. "Fault-tolerant quantum computation with constant overhead." QIC 14, 1338 (2014).
- Hastings, M. B., Haah, J. & O'Donnell, R. "Fiber bundle codes." STOC 2021.
- Guth, L. & Lubotzky, A. "Quantum error correcting codes and 4-dimensional arithmetic hyperbolic manifolds." JMP 55, 082202 (2014).
- Haah, J. "Local stabilizer codes in three dimensions without string logical operators." PRA 83, 042330 (2011).
