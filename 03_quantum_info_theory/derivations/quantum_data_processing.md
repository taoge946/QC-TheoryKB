# Quantum Data Processing Inequalities (量子数据处理不等式)

> **Tags**: `data-processing`, `relative-entropy`, `monotonicity`, `coherent-information`, `mutual-information`
>
> **Primary Source**: M. Wilde, *From Classical to Quantum Shannon Theory*, Ch.11--12
> (`references/wilde_shannon_theory/qit-notes.tex`)
>
> **Secondary Source**: J. Watrous, *The Theory of Quantum Information*, Ch.5

## Statement

量子数据处理不等式是量子信息论的核心原则：**对量子数据施加信道操作不会增加信息量**。其最基本形式为量子相对熵的单调性，其他数据处理不等式（互信息版、相干信息版、strong subadditivity 等）都是它的推论。

---

## Prerequisites

- **量子相对熵**: $D(\rho \| \sigma) = \text{Tr}[\rho(\log\rho - \log\sigma)]$ — 参见 [quantum_entropy_advanced.md](quantum_entropy_advanced.md)
- **量子信道 (CPTP映射)**: 参见 [../../02_quantum_mechanics/derivations/quantum_channels_kraus.md]
- **Von Neumann 熵**: 参见 [../../02_quantum_mechanics/derivations/von_neumann_entropy.md]
- **量子互信息**: $I(A;B) = S(A) + S(B) - S(AB) = D(\rho_{AB} \| \rho_A \otimes \rho_B)$

---

## Derivation

### Part I: 量子相对熵的单调性（Monotonicity）

#### Theorem 1: Monotonicity of Quantum Relative Entropy **[Wilde, Ch.11, Thm.11.8.1]** **[Watrous, Ch.5, Thm.5.13]**

设 $\rho \in \mathcal{D}(\mathcal{H})$，$\sigma \in \mathcal{L}(\mathcal{H})$ 正半定，$\mathcal{N}: \mathcal{L}(\mathcal{H}) \to \mathcal{L}(\mathcal{H}')$ 为量子信道。则：

$$\boxed{D(\rho \| \sigma) \geq D(\mathcal{N}(\rho) \| \mathcal{N}(\sigma))}$$

**物理意义**：对两个态施加相同的噪声信道后，它们变得更难区分。信息在噪声过程中只会丢失，不会凭空产生。

#### Step 1: 相对熵非负性（作为单调性的推论）**[Wilde, Ch.11, Thm.11.8.2]**

取 $\mathcal{N}$ 为 trace-out 映射（$\mathcal{N}(\cdot) = \text{Tr}(\cdot)$），立即得到：

$$D(\rho \| \sigma) \geq D(\text{Tr}(\rho) \| \text{Tr}(\sigma)) = 1 \cdot \log\frac{1}{\text{Tr}(\sigma)} \geq 0$$

（当 $\text{Tr}(\sigma) \leq 1$ 时。）等号条件：$D(\rho \| \sigma) = 0 \iff \rho = \sigma$。

**等号条件证明思路** **[Wilde, Ch.11, Thm.11.8.2]**：若 $D(\rho\|\sigma) = 0$，对任意测量信道 $\mathcal{M}$ 由单调性得 $D(\mathcal{M}(\rho)\|\mathcal{M}(\sigma)) = 0$，经典相对熵为零意味着 $\mathcal{M}(\rho) = \mathcal{M}(\sigma)$。由于对**任意**测量成立，故 $\rho = \sigma$。

#### Step 2: 其他熵量作为相对熵的特例 **[Wilde, Ch.11, Exercises 11.8.2--11.8.5]**

以下关系使得单调性可以推导出几乎所有量子熵不等式：

| 熵量 | 相对熵表示 |
|------|-----------|
| 互信息 | $I(A;B)_\rho = D(\rho_{AB} \| \rho_A \otimes \rho_B)$ |
| 相干信息 | $I(A\rangle B)_\rho = D(\rho_{AB} \| I_A \otimes \rho_B) - \log d_A$ |
| 条件互信息 | $I(A;B|C)_\rho = D(\rho_{ABC} \| \mathcal{R}_{B\to BC}(\rho_{AC}))$ (其中 $\mathcal{R}$ 是 Petz 恢复映射) |

---

### Part II: 相干信息的数据处理不等式

#### Theorem 2: Data Processing for Coherent Information **[Wilde, Ch.11, Thm.11.9.3]**

设 $\rho_{AB} \in \mathcal{D}(\mathcal{H}_A \otimes \mathcal{H}_B)$，$\mathcal{N}: \mathcal{L}(\mathcal{H}_B) \to \mathcal{L}(\mathcal{H}_{B'})$ 为量子信道。令 $\sigma_{AB'} = \mathcal{N}_{B\to B'}(\rho_{AB})$。则：

$$\boxed{I(A\rangle B)_\rho \geq I(A\rangle B')_\sigma}$$

**证明** **[Wilde, Ch.11, Thm.11.9.3]**：

利用相干信息的相对熵表示：

$$I(A\rangle B)_\rho = D(\rho_{AB} \| I_A \otimes \rho_B) - \log d_A$$

$$I(A\rangle B')_\sigma = D(\sigma_{AB'} \| I_A \otimes \sigma_{B'}) - \log d_A$$

注意到：

$$\sigma_{AB'} = (\text{id}_A \otimes \mathcal{N}_{B\to B'})(\rho_{AB})$$

$$I_A \otimes \sigma_{B'} = (\text{id}_A \otimes \mathcal{N}_{B\to B'})(I_A \otimes \rho_B)$$

由 Theorem 1（量子相对熵单调性），取 $\tilde{\mathcal{N}} = \text{id}_A \otimes \mathcal{N}_{B\to B'}$：

$$D(\rho_{AB} \| I_A \otimes \rho_B) \geq D(\tilde{\mathcal{N}}(\rho_{AB}) \| \tilde{\mathcal{N}}(I_A \otimes \rho_B)) = D(\sigma_{AB'} \| I_A \otimes \sigma_{B'})$$

两边减去 $\log d_A$ 即得结论。$\square$

**物理意义**：Bob 对其份额施加任何操作后，他与 Alice 之间的量子关联不会增加。

---

### Part III: 互信息的数据处理不等式

#### Theorem 3: Data Processing for Quantum Mutual Information **[Wilde, Ch.11, Thm.11.9.4]**

设 $\rho_{AB} \in \mathcal{D}(\mathcal{H}_A \otimes \mathcal{H}_B)$，$\mathcal{N}_A: \mathcal{L}(\mathcal{H}_A) \to \mathcal{L}(\mathcal{H}_{A'})$，$\mathcal{M}_B: \mathcal{L}(\mathcal{H}_B) \to \mathcal{L}(\mathcal{H}_{B'})$ 为量子信道。令 $\sigma = (\mathcal{N}_A \otimes \mathcal{M}_B)(\rho_{AB})$。则：

$$\boxed{I(A;B)_\rho \geq I(A';B')_\sigma}$$

**证明** **[Wilde, Ch.11, Thm.11.9.4]**：

利用互信息的相对熵表示：

$$I(A;B)_\rho = D(\rho_{AB} \| \rho_A \otimes \rho_B)$$

$$I(A';B')_\sigma = D(\sigma_{A'B'} \| \sigma_{A'} \otimes \sigma_{B'})$$

观察到：

$$\sigma_{A'B'} = (\mathcal{N}_A \otimes \mathcal{M}_B)(\rho_{AB})$$

$$\sigma_{A'} \otimes \sigma_{B'} = \mathcal{N}_A(\rho_A) \otimes \mathcal{M}_B(\rho_B) = (\mathcal{N}_A \otimes \mathcal{M}_B)(\rho_A \otimes \rho_B)$$

由 Theorem 1：

$$D(\rho_{AB} \| \rho_A \otimes \rho_B) \geq D((\mathcal{N}_A \otimes \mathcal{M}_B)(\rho_{AB}) \| (\mathcal{N}_A \otimes \mathcal{M}_B)(\rho_A \otimes \rho_B))$$

即 $I(A;B)_\rho \geq I(A';B')_\sigma$。$\square$

---

### Part IV: 关键推论

#### Corollary 1: Conditioning Does Not Increase Entropy **[Wilde, Ch.11, Thm.11.4.1]**

$$H(A)_\rho \geq H(A|B)_\rho$$

**证明**：由 $I(A;B) \geq 0$（互信息非负），展开得 $H(A) - H(A|B) = I(A;B) \geq 0$。$\square$

#### Corollary 2: Strong Subadditivity **[Wilde, Ch.11]**; Lieb & Ruskai (1973)

$$S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})$$

**证明**：等价于 $H(A|BC) \leq H(A|B)$，即"给定更多信息不会增加条件熵"。这是量子相对熵单调性的推论——取 trace-out map $\text{Tr}_C$ 作为信道，由条件熵单调性得出。$\square$

#### Corollary 3: Holevo Bound **[Wilde, Ch.11, Exercise 11.9.8]**

$$I_{\text{acc}}(\mathcal{E}) \leq \chi(\mathcal{E}) = S\!\left(\sum_x p_x \rho_x\right) - \sum_x p_x S(\rho_x)$$

对量子系综 $\mathcal{E} = \{p_x, \rho_x\}$，经典地可获取的信息（通过最优测量）不超过 Holevo 信息 $\chi$。

**证明思路**：考虑经典-量子态 $\rho_{XB} = \sum_x p_x |x\rangle\langle x| \otimes \rho_x$，任何测量 $\{M_m\}$ 对应量子信道 $\mathcal{M}$，由数据处理不等式 $I(X;Y)_{\text{post}} \leq I(X;B)_\rho = \chi(\mathcal{E})$。$\square$

---

### Part V: 加强版——可恢复性定理（Recoverability）

#### Theorem 4: Recoverability Theorem **[Wilde, Ch.12, Thm.12.1.1]**

在 Theorem 1 的条件下，存在恢复信道 $\mathcal{R}_{\sigma,\mathcal{N}}$（仅依赖于 $\sigma$ 和 $\mathcal{N}$）使得：

$$D(\rho \| \sigma) - D(\mathcal{N}(\rho) \| \mathcal{N}(\sigma)) \geq -\log F\!\left(\rho, (\mathcal{R}_{\sigma,\mathcal{N}} \circ \mathcal{N})(\rho)\right)$$

且 $(\mathcal{R}_{\sigma,\mathcal{N}} \circ \mathcal{N})(\sigma) = \sigma$（完美恢复 $\sigma$）。

**关键意义**：
- 右边非负（因为 $F \leq 1$），所以蕴含 Theorem 1
- 量化了"信道作用后信息损失"与"可恢复程度"的关系
- 证明使用了 **Stein-Hirschman 复插值定理**和 **Renyi 相对熵差**

---

## Summary

| 不等式 | 公式 | 证明核心 |
|--------|------|----------|
| 相对熵单调性 | $D(\rho\|\sigma) \geq D(\mathcal{N}(\rho)\|\mathcal{N}(\sigma))$ | 基础定理 |
| 相对熵非负性 | $D(\rho\|\sigma) \geq 0$ | 取 $\mathcal{N} = \text{Tr}$ |
| 相干信息数据处理 | $I(A\rangle B) \geq I(A\rangle B')$ | 相对熵单调性 |
| 互信息数据处理 | $I(A;B) \geq I(A';B')$ | 相对熵单调性 |
| Strong subadditivity | $S(ABC)+S(B) \leq S(AB)+S(BC)$ | 条件熵单调性 |
| Holevo bound | $I_{\text{acc}} \leq \chi$ | 互信息数据处理 |
| 可恢复性 | 见 Theorem 4 | 复插值理论 |

所有这些不等式的逻辑关系：**量子相对熵单调性** $\Rightarrow$ 其他所有不等式。

---

## References

- Wilde, *From Classical to Quantum Shannon Theory*, Ch.11--12 (primary derivations)
- Watrous, *The Theory of Quantum Information*, Ch.5
- Lindblad, Commun. Math. Phys. 40, 147 (1975)
- Lieb & Ruskai, J. Math. Phys. 14, 1938 (1973)
- Petz, Commun. Math. Phys. 105, 123 (1986)
