# Chapter 2: Quantum Mechanics — Key Formulas

> 量子力学基础公式速查表。公式和术语用英文，解释用中文。
> 所有公式均使用 LaTeX 标记。

---

### F2.1: Density Matrix (密度矩阵)
$$\rho = \sum_i p_i \, |\psi_i\rangle\langle\psi_i|$$
密度矩阵是量子态最一般的描述方式：纯态对应 $\rho = |\psi\rangle\langle\psi|$（$\text{Tr}(\rho^2)=1$），混合态对应概率 $p_i$ 加权的纯态系综（$\text{Tr}(\rho^2)<1$）。

**Source**: [derivations/density_matrix_formalism.md] | **[Nielsen & Chuang, Theorem 2.5, p.101]**

---

### F2.2: Partial Trace (偏迹)
$$\rho_A = \text{Tr}_B(\rho_{AB}) = \sum_j (I_A \otimes \langle j|_B)\, \rho_{AB}\, (I_A \otimes |j\rangle_B)$$
对复合系统 $AB$ 的密度矩阵关于子系统 $B$ 求偏迹，可得到子系统 $A$ 的约化密度矩阵；这是描述子系统量子态的唯一正确方法。

**Source**: [derivations/density_matrix_formalism.md] | **[Nielsen & Chuang, Theorem 2.7, Eq. 2.178, p.105]**

---

### F2.3: Von Neumann Entropy (冯·诺依曼熵)
$$S(\rho) = -\text{Tr}(\rho \log \rho) = -\sum_i \lambda_i \log \lambda_i$$
量子态的熵，其中 $\lambda_i$ 是 $\rho$ 的特征值。纯态熵为零，最大混合态 $\rho = I/d$ 的熵为 $\log d$。是经典 Shannon 熵的量子推广。

**Source**: [derivations/von_neumann_entropy.md] | **[Nielsen & Chuang, Eq. 11.51, p.510; Theorem 11.3, p.515]**

---

### F2.4: Fidelity (保真度)
$$F(\rho, \sigma) = \left( \text{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}} \right)^2$$
衡量两个量子态之间"接近程度"的度量。$F=1$ 表示两态完全相同，$F=0$ 表示完全正交。当其中一个态为纯态 $|\psi\rangle$ 时简化为 $F = \langle\psi|\sigma|\psi\rangle$。

**Source**: [derivations/fidelity_and_trace_distance.md] | **[Nielsen & Chuang, Eq. 9.52, p.409; Theorem 9.4 (Uhlmann), p.410]**

---

### F2.5: Trace Distance (迹距离)
$$D(\rho, \sigma) = \frac{1}{2}\text{Tr}|\rho - \sigma| = \frac{1}{2}\text{Tr}\sqrt{(\rho-\sigma)^\dagger(\rho-\sigma)}$$
另一种量子态距离度量，具有运算不增性（任何量子操作不会增加迹距离）。$D \in [0,1]$，可操作性解释：区分两个态的最大成功概率为 $\frac{1}{2}(1+D)$。

**Source**: [derivations/fidelity_and_trace_distance.md] | **[Nielsen & Chuang, Eq. 9.1, p.399; Theorem 9.2 (contractivity), p.406; Theorem 9.3 (Helstrom), p.401]**

---

### F2.6: Quantum Channel — Kraus Representation (量子信道 — Kraus 表示)
$$\mathcal{E}(\rho) = \sum_k E_k \, \rho \, E_k^\dagger, \qquad \sum_k E_k^\dagger E_k = I$$
任何合法的量子操作（CPTP映射）都可以用一组 Kraus 算子 $\{E_k\}$ 表示。完备性条件 $\sum_k E_k^\dagger E_k = I$ 保证了迹守恒（概率守恒）。

**Source**: [derivations/quantum_channels_kraus.md] | **[Nielsen & Chuang, Theorem 8.1, p.360; Eq. 8.8, p.360]**

---

### F2.7: Choi-Jamiołkowski Isomorphism (Choi-Jamiołkowski 同构)
$$J(\mathcal{E}) = (I \otimes \mathcal{E})\left(|\Phi^+\rangle\langle\Phi^+|\right), \qquad |\Phi^+\rangle = \frac{1}{\sqrt{d}}\sum_{i=0}^{d-1}|i\rangle|i\rangle$$
量子信道 $\mathcal{E}$ 与一个正算子（Choi 矩阵）之间的一一对应关系。$\mathcal{E}$ 是 CPTP 当且仅当 $J(\mathcal{E}) \geq 0$（半正定）且 $\text{Tr}_{\text{out}}(J(\mathcal{E})) = I/d$。

**Source**: [derivations/quantum_channels_kraus.md] | **[Nielsen & Chuang, Theorem 8.3, p.374]**; Choi (1975); Jamiołkowski (1972)

---

### F2.8: CPTP Conditions (完全正、迹守恒条件)
$$\text{Complete Positivity:} \quad (I_R \otimes \mathcal{E})(\rho_{RA}) \geq 0 \;\;\forall\; \rho_{RA} \geq 0$$
$$\text{Trace Preserving:} \quad \text{Tr}[\mathcal{E}(\rho)] = \text{Tr}[\rho] \;\;\forall\;\rho$$
合法的量子信道必须满足：(1) 完全正性——即使系统与任意参考系统纠缠，操作后仍保持正性；(2) 迹守恒——概率之和始终为 1。

**Source**: [derivations/quantum_channels_kraus.md] | **[Nielsen & Chuang, Box 8.2, p.368; Section 8.2.4, p.363]**

---

### F2.9: Bloch Sphere Representation (Bloch 球表示)
$$\rho = \frac{1}{2}\left(I + \vec{r} \cdot \vec{\sigma}\right) = \frac{1}{2}\begin{pmatrix} 1+r_z & r_x - ir_y \\ r_x + ir_y & 1-r_z \end{pmatrix}$$
单量子比特密度矩阵可由 Bloch 向量 $\vec{r} = (r_x, r_y, r_z)$ 完全描述，其中 $r_i = \text{Tr}(\rho\,\sigma_i)$。纯态满足 $|\vec{r}|=1$（球面上），混合态满足 $|\vec{r}|<1$（球内部）。

**Source**: **[Nielsen & Chuang, p.15, Eq. 1.15-1.16]**; Sakurai, Ch. 1

---

### F2.10: Pauli Matrices and Algebra (Pauli 矩阵及其代数)
$$\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \quad \sigma_y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}, \quad \sigma_z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

核心代数关系：
$$\sigma_i \sigma_j = \delta_{ij} I + i\epsilon_{ijk}\sigma_k, \qquad [\sigma_i, \sigma_j] = 2i\epsilon_{ijk}\sigma_k, \qquad \{\sigma_i, \sigma_j\} = 2\delta_{ij}I$$
Pauli 矩阵是 $2\times 2$ Hermitian 幺正矩阵，构成单比特算子空间的一组基。它们的对易和反对易关系是量子计算中大量推导的基础。

**Source**: **[Nielsen & Chuang, Section 2.1.3, p.65]**; Sakurai, Ch. 1

---

### F2.11: Tensor Product of States and Operators (态与算子的张量积)
$$|\psi\rangle_{AB} = |\psi\rangle_A \otimes |\phi\rangle_B, \qquad (A \otimes B)(|u\rangle \otimes |v\rangle) = (A|u\rangle) \otimes (B|v\rangle)$$
$$\dim(\mathcal{H}_A \otimes \mathcal{H}_B) = \dim(\mathcal{H}_A) \times \dim(\mathcal{H}_B)$$
复合量子系统的 Hilbert 空间是各子系统空间的张量积。不能写成张量积形式的态称为**纠缠态**。

**Source**: [derivations/schmidt_decomposition.md] | **[Nielsen & Chuang, Postulate 4, p.94; Section 2.1.7, p.71]**

---

### F2.12: Schmidt Decomposition (Schmidt 分解)
$$|\psi\rangle_{AB} = \sum_{i=1}^{r} \lambda_i \, |a_i\rangle_A \otimes |b_i\rangle_B, \qquad \lambda_i > 0,\; \sum_i \lambda_i^2 = 1$$
任何双体纯态都可以分解为 Schmidt 形式，其中 $\{|a_i\rangle\}$、$\{|b_i\rangle\}$ 分别是两个子系统的标准正交基，$\lambda_i$ 是 Schmidt 系数，$r$ 是 Schmidt 秩。$r=1$ 当且仅当态是可分的（非纠缠）。

**Source**: [derivations/schmidt_decomposition.md] | **[Nielsen & Chuang, Theorem 2.7, p.109]**

---

### F2.13: Entanglement Entropy (纠缠熵)
$$E(|\psi\rangle_{AB}) = S(\rho_A) = S(\rho_B) = -\sum_i \lambda_i^2 \log \lambda_i^2$$
双体纯态的纠缠度量，等于任一子系统约化密度矩阵的 von Neumann 熵，也等于 Schmidt 系数平方的 Shannon 熵。$E=0$ 对应可分态，$E=\log d$ 对应最大纠缠态。

**Source**: [derivations/von_neumann_entropy.md], [derivations/schmidt_decomposition.md] | Bennett et al. (1996)

---

### F2.14: POVM Measurement (POVM 测量)
$$\{M_m\}: \quad M_m \geq 0, \quad \sum_m M_m = I$$
$$p(m) = \text{Tr}(M_m \, \rho)$$
POVM（正算子值测量）是最一般的量子测量描述。每个测量结果 $m$ 对应一个正半定算子 $M_m$，得到该结果的概率为 $p(m) = \text{Tr}(M_m\rho)$。投影测量是 POVM 的特殊情况（$M_m = |m\rangle\langle m|$）。

**Source**: [derivations/measurement_theory.md] | **[Nielsen & Chuang, Postulate 3, p.84; Section 2.2.6, p.90]**

---

### F2.15: Quantum Mutual Information (量子互信息)
$$I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$$
衡量复合系统 $AB$ 中子系统之间的总关联（包括经典和量子关联）。由 subadditivity 保证 $I(A:B) \geq 0$，由 strong subadditivity 可以推导出许多重要的信息论不等式。

**Source**: [derivations/von_neumann_entropy.md] | **[Nielsen & Chuang, Eq. 11.63-11.65, p.514; Theorem 11.4 (subadditivity), p.515; Theorem 11.8 (strong subadditivity), p.519]**

---

## Cross-References

| Formula | Related Derivations |
|---------|-------------------|
| F2.1, F2.2 | [density_matrix_formalism.md](derivations/density_matrix_formalism.md) |
| F2.3, F2.13, F2.15 | [von_neumann_entropy.md](derivations/von_neumann_entropy.md) |
| F2.4, F2.5 | [fidelity_and_trace_distance.md](derivations/fidelity_and_trace_distance.md) |
| F2.6, F2.7, F2.8 | [quantum_channels_kraus.md](derivations/quantum_channels_kraus.md) |
| F2.11, F2.12, F2.13 | [schmidt_decomposition.md](derivations/schmidt_decomposition.md) |
| F2.14 | [measurement_theory.md](derivations/measurement_theory.md) |
