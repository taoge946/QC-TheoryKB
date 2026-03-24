# Key Formulas: Quantum Information Theory

> **Tags**: `quantum-info`, `entropy`, `channels`, `capacity`, `entanglement`, `sdp`, `discrimination`
>
> 本文件汇集量子信息论中 50+ 个核心公式，来源于 Watrous (*Theory of Quantum Information*) 和 Wilde (*From Classical to Quantum Shannon Theory*)。
> 按主题组织，统一使用 F3.x 编号。

---

### F3.1: Hilbert-Schmidt Inner Product (Hilbert-Schmidt 内积)

$$\langle X, Y \rangle = \mathrm{Tr}(X^* Y)$$

> 算符空间上的标准内积，赋予线性算符集合 Hilbert 空间结构。

**Source**: [Watrous, Ch.1, Eq.1.1] — `derivations/classical_information_theory.md`

---

### F3.2: Schatten Norms (Schatten 范数)

$$\|X\|_1 = \mathrm{Tr}\sqrt{X^* X}, \quad \|X\|_\infty = \max\{\|Xu\| : \|u\|=1\}, \quad \|X\|_p = (\mathrm{Tr}(X^*X)^{p/2})^{1/p}$$

> 迹范数 ($p=1$)、谱范数 ($p=\infty$) 和一般 Schatten $p$-范数，是量子态距离度量的基础。

**Source**: [Watrous, Ch.1, Def.1.1–1.3] — `derivations/classical_information_theory.md`

---

### F3.3: Vectorization (算符向量化)

$$\mathrm{vec}(X) = \sum_{i,j} X_{ij} \, e_i \otimes e_j$$

> 将算符映射为向量，连接 Choi 表示与 Kraus 表示的桥梁。

**Source**: [Watrous, Ch.1, Eq.1.15] — `derivations/classical_information_theory.md`

---

### F3.4: Holder's Inequality for Operators (算符 Holder 不等式)

$$|\mathrm{Tr}(X^*Y)| \leq \|X\|_p \|Y\|_q, \quad \frac{1}{p}+\frac{1}{q}=1$$

> 算符空间的对偶范数不等式，迹范数与谱范数互为对偶。

**Source**: [Watrous, Ch.1, Prop.1.10] — `derivations/classical_information_theory.md`

---

### F3.5: Von Neumann Trace Inequality (von Neumann 迹不等式)

$$|\mathrm{Tr}(XY)| \leq \sum_k s_k(X)s_k(Y)$$

> 迹的绝对值受奇异值乘积之和控制。

**Source**: [Watrous, Ch.1, Thm.1.13] — `derivations/classical_information_theory.md`

---

### F3.6: Kraus Representation (Kraus 表示)

$$\Phi(X) = \sum_k A_k X A_k^*$$

> 完全正映射的算符和表示，$\{A_k\}$ 为 Kraus 算符，保迹条件 $\sum_k A_k^* A_k = \mathbb{1}$。

**Source**: [Watrous, Ch.2, Thm.2.22] — `derivations/quantum_channel_capacity.md`

---

### F3.7: Choi Representation (Choi 表示)

$$J(\Phi) = \sum_{i,j} \Phi(|e_i\rangle\langle e_j|) \otimes |e_i\rangle\langle e_j|$$

> Choi-Jamiolkowski 同构将信道映射为算符：$\Phi$ 完全正 $\iff$ $J(\Phi) \geq 0$，保迹 $\iff$ $\mathrm{Tr}_{\mathcal{Y}}(J(\Phi)) = \mathbb{1}$。

**Source**: [Watrous, Ch.2, Def.2.18, Thm.2.22, Prop.2.20] — `derivations/quantum_channel_capacity.md`

---

### F3.8: Stinespring Dilation (Stinespring 膨胀)

$$\Phi(X) = \mathrm{Tr}_{\mathcal{Z}}(AXA^*)$$

> 任何 CPTP 映射都可表示为酉演化后对环境取偏迹，给出信道的物理实现。

**Source**: [Watrous, Ch.2, Thm.2.27] — `derivations/quantum_channel_capacity.md`

---

### F3.9: Depolarizing Channel (去极化信道)

$$\Delta_p(\rho) = (1-p)\rho + p\frac{\mathbb{1}}{d}\mathrm{Tr}(\rho)$$

> 以概率 $p$ 将量子态替换为最大混合态，是量子纠错中最常用的噪声模型之一。

**Source**: [Watrous, Ch.2] — `derivations/quantum_channel_capacity.md`

---

### F3.10: Diamond Norm (菱形范数)

$$\|\Phi-\Psi\|_\diamond = \sup_{\rho} \|(\Phi\otimes\mathrm{id})(\rho) - (\Psi\otimes\mathrm{id})(\rho)\|_1$$

> 量子信道之间的最坏情况区分度量，允许辅助系统纠缠，可通过 SDP 高效计算。

**Source**: [Watrous, Ch.2, Def.2.35] — `derivations/quantum_channel_capacity.md`

---

### F3.11: SDP Primal-Dual Pair (半定规划原始-对偶对)

$$\text{Primal: } \sup\{\langle A,X\rangle : \Phi(X)=B, X\geq 0\}, \quad \text{Dual: } \inf\{\langle B,Y\rangle : \Phi^*(Y)\geq A, Y=Y^*\}$$

> 弱对偶性总成立，Slater 条件下强对偶性成立，是量子信息最优化问题的标准工具。

**Source**: [Watrous, Ch.3, Def.3.1, Thm.3.5] — `derivations/sdp_quantum_info.md`

---

### F3.12: Uhlmann Fidelity (Uhlmann 保真度)

$$F(\rho,\sigma) = \left(\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\sqrt{\rho}}\right)^2 = \max_{U}|\mathrm{Tr}(U\sqrt{\rho}\sqrt{\sigma})|^2$$

> 量子态相似度的标准度量，$F=1$ 当且仅当 $\rho=\sigma$，可通过 SDP 计算。

**Source**: [Watrous, Ch.3, Def.3.27, Thm.3.28] — `derivations/sdp_quantum_info.md`

---

### F3.13: Fuchs-van de Graaf Inequalities (Fuchs-van de Graaf 不等式)

$$1-\sqrt{F(\rho,\sigma)}\leq\frac{1}{2}\|\rho-\sigma\|_1\leq\sqrt{1-F(\rho,\sigma)}$$

> 连接保真度与迹距离的基本不等式，允许两种度量之间互相转换。

**Source**: [Watrous, Ch.3, Thm.3.33] — `derivations/sdp_quantum_info.md`

---

### F3.14: Helstrom Bound (Helstrom 界)

$$p_{\mathrm{opt}} = \frac{1}{2}\left(1 + \|p_1\rho_1 - p_0\rho_0\|_1\right)$$

> 两态最小错误判别的最优成功概率，量子假设检验的基本极限。

**Source**: [Watrous, Ch.4, Thm.4.3] — `derivations/quantum_data_processing.md`

---

### F3.15: Unambiguous Discrimination (无歧义判别)

$$p_{\mathrm{unamb}} = 1 - F(\rho_0,\rho_1)$$

> 纯态无歧义判别的最优成功概率，以保真度为代价换取零误判。

**Source**: [Watrous, Ch.4, Thm.4.14] — `derivations/quantum_data_processing.md`

---

### F3.16: Von Neumann Entropy (von Neumann 熵)

$$\mathrm{H}(\rho) = -\mathrm{Tr}(\rho\log\rho)$$

> 量子态的信息量度量，$0 \leq H(\rho) \leq \log d$，最大混合态取最大值。

**Source**: [Watrous, Ch.5, Def.5.1] — `derivations/entropy_inequalities.md`

---

### F3.17: Quantum Relative Entropy (量子相对熵)

$$\mathrm{D}(\rho\|\sigma) = \mathrm{Tr}(\rho\log\rho - \rho\log\sigma)$$

> 量子信息论的"万能不等式"：非负性 $D \geq 0$ 可推导几乎所有熵不等式。

**Source**: [Watrous, Ch.5, Def.5.3] — `derivations/entropy_inequalities.md`

---

### F3.18: Conditional Entropy & Mutual Information (条件熵与互信息)

$$\mathrm{H}(A|B)_\rho = \mathrm{H}(AB) - \mathrm{H}(B), \quad \mathrm{I}(A:B)_\rho = \mathrm{H}(A)+\mathrm{H}(B)-\mathrm{H}(AB)$$

> 量子条件熵可以为负（纠缠态），互信息度量量子关联总量。

**Source**: [Watrous, Ch.5, Def.5.16, 5.18] — `derivations/entropy_inequalities.md`

---

### F3.19: Strong Subadditivity (强次可加性)

$$\mathrm{H}(ABC)+\mathrm{H}(B)\leq\mathrm{H}(AB)+\mathrm{H}(BC)$$

> 量子熵最深刻的不等式，等价于条件互信息非负，由 Lieb-Ruskai 证明。

**Source**: [Watrous, Ch.5, Thm.5.25] — `derivations/entropy_inequalities.md`

---

### F3.20: Data Processing Inequality (数据处理不等式)

$$\mathrm{D}(\Phi(\rho)\|\Phi(\sigma))\leq\mathrm{D}(\rho\|\sigma)$$

> 量子信道不增加可区分性，是相对熵单调性的直接推论。

**Source**: [Watrous, Ch.5, Thm.5.13] — `derivations/quantum_data_processing.md`

---

### F3.21: Klein's Inequality (Klein 不等式)

$$\mathrm{D}(\rho\|\sigma)\geq 0, \quad \text{等号成立} \iff \rho=\sigma$$

> 相对熵非负性，是几乎所有熵不等式的起点。

**Source**: [Watrous, Ch.5, Thm.5.8] — `derivations/entropy_inequalities.md`

---

### F3.22: Subadditivity & Araki-Lieb (次可加性与 Araki-Lieb 不等式)

$$|\mathrm{H}(A)-\mathrm{H}(B)| \leq \mathrm{H}(AB) \leq \mathrm{H}(A)+\mathrm{H}(B)$$

> 联合熵的上下界，上界（次可加性）由相对熵非负性推出，下界（Araki-Lieb）由纯化论证得出。

**Source**: [Watrous, Ch.5, Cor.5.26, 5.27] — `derivations/entropy_inequalities.md`

---

### F3.23: Holevo Capacity (Holevo 容量)

$$\chi(\Phi) = \max_{p,\rho} \left[\mathrm{H}\!\left(\sum p_k\Phi(\rho_k)\right) - \sum p_k\mathrm{H}(\Phi(\rho_k))\right]$$

> 单次使用信道的经典信息传输上界，一般需正则化 $C = \lim_n \frac{1}{n}\chi(\Phi^{\otimes n})$。

**Source**: [Watrous, Ch.6, Def.6.2, Thm.6.7; Wilde, Ch.20, Thm.20.3.1] — `derivations/holevo_bound.md`

---

### F3.24: Quantum Capacity — LSD Theorem (量子容量)

$$Q(\Phi) = \lim_{n\to\infty}\frac{1}{n}Q^{(1)}(\Phi^{\otimes n}), \quad Q^{(1)}(\Phi) = \max_\rho [\mathrm{H}(\Phi(\rho)) - \mathrm{H}_e(\Phi,\rho)]$$

> 量子信道传输量子信息的极限速率，由相干信息的正则化给出，degradable 信道不需要正则化。

**Source**: [Watrous, Ch.6, Thm.6.24; Wilde, Ch.24, Thm.24.3.1] — `derivations/quantum_capacity.md`

---

### F3.25: Entanglement-Assisted Classical Capacity (纠缠辅助经典容量)

$$C_E(\Phi) = \max_\rho [\mathrm{H}(\rho)+\mathrm{H}(\Phi(\rho))-\mathrm{H}_e(\Phi,\rho)] = \max_\rho \mathrm{I}(A:B)_{\sigma}$$

> Bennett-Shor-Smolin-Thapliyal 定理，不需要正则化，互信息可加性保证单字母公式。

**Source**: [Watrous, Ch.6, Thm.6.33; Wilde, Ch.21, Thm.21.4.1] — `derivations/quantum_channel_capacity.md`

---

### F3.26: Capacity Hierarchy (容量层次)

$$C_Q(\mathcal{N}) \leq C(\mathcal{N}) \leq C_{\mathrm{EA}}(\mathcal{N})$$

> 量子容量 $\leq$ 经典容量 $\leq$ 纠缠辅助容量，degradable 信道和 entanglement-breaking 信道有单字母公式。

**Source**: [Wilde, Ch.20-24] — `derivations/quantum_channel_capacity.md`

---

### F3.27: Entanglement of Formation (纠缠形成)

$$E_F(\rho) = \min\sum_k p_k \mathrm{H}(\mathrm{Tr}_B(|\psi_k\rangle\langle\psi_k|))$$

> 通过纯态分解的最小平均纠缠熵定义，度量制备纠缠态所需的 ebit 资源。

**Source**: [Watrous, Ch.7, Def.7.46] — `derivations/entanglement_theory.md`

---

### F3.28: Distillable Entanglement & Entanglement Cost (可蒸馏纠缠与纠缠代价)

$$E_D(\rho) = \sup\{r : \lim_{n\to\infty}\inf_\Lambda \|\Lambda(\rho^{\otimes n})-\Phi_+^{\otimes\lfloor rn\rfloor}\|_1=0\}$$

> $E_D$ 度量从混态中蒸馏 Bell 对的最大速率，$E_C$ 度量从 Bell 对制备混态的最小速率，满足 $E_D \leq E_F \leq E_C$。

**Source**: [Watrous, Ch.7, Def.7.55, 7.60] — `derivations/entanglement_theory.md`

---

### F3.29: Logarithmic Negativity (对数负性)

$$E_N(\rho) = \log\|\rho^{T_B}\|_1$$

> 可计算的纠缠度量，基于部分转置的迹范数，是可蒸馏纠缠的上界。

**Source**: [Watrous, Ch.7, Def.7.35] — `derivations/entanglement_theory.md`

---

### F3.30: PPT Criterion — Peres-Horodecki (PPT 判据)

$$\rho \in \mathrm{Sep} \Rightarrow (\mathrm{id}\otimes T)(\rho)\geq 0$$

> 可分态必为 PPT，$2\times2$ 和 $2\times3$ 系统中 PPT 等价于可分，高维存在 PPT 纠缠态。

**Source**: [Watrous, Ch.7, Thm.7.15–7.17] — `derivations/entanglement_theory.md`

---

### F3.31: Nielsen's Majorization Criterion (Nielsen 优化准则)

$$|\psi\rangle\xrightarrow{\mathrm{LOCC}}|\phi\rangle \iff \lambda_\psi \prec \lambda_\phi$$

> LOCC 下纯态转换的充要条件由 Schmidt 系数的优化关系决定。

**Source**: [Watrous, Ch.7, Thm.7.8] — `derivations/entanglement_theory.md`

---

### F3.32: Operator Jensen Inequality (算符 Jensen 不等式)

$$f \text{ operator concave} \Rightarrow \mathrm{Tr}(f(\sum p_k A_k))\geq\sum p_k\mathrm{Tr}(f(A_k))$$

> 算符凹性工具，$A\mapsto \log A$ 和 $A\mapsto A^t$ ($0<t\leq 1$) 的凹性是熵不等式证明的关键。

**Source**: [Watrous, Ch.5, Thm.5.7] — `derivations/entropy_inequalities.md`

---

### F3.33: Quantum Entropy as Minimum Measurement Entropy (量子熵的测量最优性)

$$H(\rho) = \min_{\{\Lambda_y\}} \left[ -\sum_y \mathrm{Tr}(\Lambda_y \rho) \log \mathrm{Tr}(\Lambda_y \rho) \right]$$

> 量子熵等于最优测量（$\rho$ 的特征基投影）给出的 Shannon 熵，最小化遍历所有 rank-one POVM。

**Source**: [Wilde, Ch.11, Theorem 11.1.1] — `derivations/entropy_inequalities.md`

---

### F3.34: Negative Conditional Entropy & State Merging (负条件熵与态合并)

$$H(A|B)_{\Phi^+} = -\log 2 < 0$$

> 量子条件熵可为负，操作含义：$H(A|B)<0$ 时态合并协议不需量子信道且净产生 $n|H(A|B)|$ 个 ebit。

**Source**: [Wilde, Ch.11, Section 11.5.2; Horodecki-Oppenheim-Winter, 2005] — `derivations/entropy_inequalities.md`

---

### F3.35: Conditional Entropy Duality (条件熵对偶性)

$$H(A|B)_\rho = -H(A|E)_\psi$$

> 对三体纯态 $|\psi\rangle_{ABE}$，Alice 对 Bob 的不确定性的负值等于对环境的不确定性。

**Source**: [Wilde, Ch.11, Exercise 11.5.3] — `derivations/entropy_inequalities.md`

---

### F3.36: Coherent Information Bounds (相干信息界)

$$|H(A|B)_\rho| \leq \log \dim(\mathcal{H}_A)$$

> 条件熵绝对值有界，上界由乘积态饱和，下界由最大纠缠态饱和。

**Source**: [Wilde, Ch.11, Theorem 11.5.2] — `derivations/quantum_capacity.md`

---

### F3.37: Recoverability Theorem (可恢复性定理)

$$D(\rho \| \sigma) - D(\mathcal{N}(\rho) \| \mathcal{N}(\sigma)) \geq -\log F\!\left(\rho, (\mathcal{R}_{\sigma,\mathcal{N}} \circ \mathcal{N})(\rho)\right)$$

> 相对熵单调性的加强版，存在仅依赖 $\sigma,\mathcal{N}$ 的恢复信道量化信道作用的可逆程度。

**Source**: [Wilde, Ch.12, Theorem 12.1.1] — `derivations/quantum_data_processing.md`

---

### F3.38: Shannon Entropy (Shannon 熵)

$$H(X) = -\sum_x p_X(x) \log p_X(x)$$

> 经典信息论基础量，满足 $0 \leq H(X) \leq \log|\mathcal{X}|$、凹性和链式法则。

**Source**: [Wilde, Ch.10, Section 10.1] — `derivations/classical_information_theory.md`

---

### F3.39: Relative Entropy Non-Negativity — Master Inequality (相对熵非负性)

$$D(p\|q) \geq 0, \quad \text{等号} \iff p=q$$

> 经典信息论的主不等式，可推出最大熵、互信息非负、条件化降低熵、强次可加性等全部基本不等式。

**Source**: [Wilde, Ch.10, Theorem 10.6.1] — `derivations/classical_information_theory.md`

---

### F3.40: Fano's Inequality (Fano 不等式)

$$H(X|Y) \leq h_2(p_e) + p_e \log(|\mathcal{X}|-1)$$

> 将信息损失与错误概率联系起来的基本逆定理工具，对对称信道紧。

**Source**: [Wilde, Ch.10, Theorem 10.6.3] — `derivations/classical_information_theory.md`

---

### F3.41: Pinsker's Inequality (Pinsker 不等式)

$$D(p\|q) \geq \frac{1}{2\ln 2}\|p-q\|_1^2$$

> 信息散度控制统计距离，证明使用相对熵在粗粒化下的单调性。

**Source**: [Wilde, Ch.10, Theorem 10.7.1] — `derivations/classical_information_theory.md`

---

### F3.42: Fannes-Audenaert Inequality (Fannes-Audenaert 不等式)

$$|H(\rho) - H(\sigma)| \leq T \log(d-1) + h_2(T), \quad T = \tfrac{1}{2}\|\rho - \sigma\|_1$$

> von Neumann 熵的最优连续性界，对所有 $T$ 和 $d$ 紧。

**Source**: [Wilde, Ch.11, Theorem 11.10.3] — `derivations/entropy_inequalities.md`

---

### F3.43: AFW Inequality — Conditional Entropy Continuity (AFW 条件熵连续性)

$$|H(A|B)_\rho - H(A|B)_\sigma| \leq 2\varepsilon \log d_A + g_2(\varepsilon)$$

> 条件熵的连续性界，关键优势：仅依赖 $d_A$ 而不依赖条件系统维度。

**Source**: [Wilde, Ch.11, Theorem 11.10.4] — `derivations/entropy_inequalities.md`

---

### F3.44: Additivity of Mutual Information of Channels (信道互信息可加性)

$$I(\mathcal{N} \otimes \mathcal{M}) = I(\mathcal{N}) + I(\mathcal{M})$$

> 纠缠辅助经典容量的可加性保证，证明关键工具为互信息链式法则。

**Source**: [Wilde, Ch.13, Theorem 13.3.1] — `derivations/quantum_channel_capacity.md`

---

### F3.45: Coherent Information Additivity for Degradable Channels (Degradable 信道相干信息可加性)

$$Q(\mathcal{N} \otimes \mathcal{M}) = Q(\mathcal{N}) + Q(\mathcal{M}) \quad \text{(both degradable)}$$

> Degradable 信道的量子容量为单字母公式 $C_Q = \max_\phi I(A\rangle B)$，不需正则化。

**Source**: [Wilde, Ch.13, Theorem 13.4.1; Devetak & Shor, 2005] — `derivations/quantum_capacity.md`

---

### F3.46: Quantum Erasure Channel Capacity (量子擦除信道容量)

$$C_Q(\mathcal{N}_\varepsilon) = \max(1 - 2\varepsilon, 0)$$

> 擦除概率 $\varepsilon > 1/2$ 时容量为零（no-cloning bound），是量子容量理论的典型例子。

**Source**: [Wilde, Ch.24, Section 24.4; Bennett-DiVincenzo-Smolin, 1997] — `derivations/quantum_capacity.md`

---

### F3.47: Superadditivity & Superactivation (超可加性与超激活)

$$\chi(\mathcal{N}^{\otimes 2}) > 2\chi(\mathcal{N}) \;\text{(Hastings 2009)}, \quad C_Q(\mathcal{N}_1)=C_Q(\mathcal{N}_2)=0 \;\text{but}\; C_Q(\mathcal{N}_1\otimes\mathcal{N}_2)>0$$

> Holevo 信息和相干信息均可超可加，量子容量甚至可超激活，说明正则化不可避免。

**Source**: [Wilde, Ch.20, §20.5; Ch.24, §24.7] — `derivations/quantum_channel_capacity.md`

---

## Cross-Reference: File Map for Detailed Derivations

| File | Content | Key References |
|------|---------|---------------|
| `derivations/classical_information_theory.md` | Shannon entropy, channel coding, data processing, Fano, Pinsker | Wilde Ch.2, 10 |
| `derivations/holevo_bound.md` | Holevo bound, accessible info, HSW theorem, classical capacity | Wilde Ch.11, 20 |
| `derivations/quantum_capacity.md` | Coherent info, quantum capacity (LSD), EA capacity (BSST) | Wilde Ch.11, 21, 24 |
| `derivations/entropy_inequalities.md` | SSA, Fannes-Audenaert, AFW, monotonicity, recoverability, DPI | Wilde Ch.11, 12 |
| `derivations/quantum_channel_capacity.md` | HSW, LSD, EA capacity theorems (from Watrous) | Watrous Ch.6; Wilde Ch.18-24 |
| `derivations/entanglement_theory.md` | LOCC, measures, PPT, distillation, coherent info | Watrous Ch.7; Wilde Ch.11-12, 19 |
| `derivations/quantum_data_processing.md` | Relative entropy monotonicity, data processing inequalities | Watrous Ch.5; Wilde Ch.11-12 |
| `derivations/sdp_quantum_info.md` | SDP formulations for fidelity, diamond norm, optimal measurement | Watrous Ch.3 |

---

## References

1. Watrous, J. (2018). *The Theory of Quantum Information*. Cambridge University Press.
2. Wilde, M.M. (2017). *From Classical to Quantum Shannon Theory*. Cambridge University Press.
3. Horodecki, M., Oppenheim, J., & Winter, A. (2005). Partial quantum information. Nature.
4. Hastings, M.B. (2009). Superadditivity of communication capacity using entangled inputs. Nature Physics.
5. Devetak, I. & Shor, P.W. (2005). The capacity of a quantum channel for simultaneous transmission of classical and quantum information. CMP.
6. Bennett, C.H., DiVincenzo, D.P., & Smolin, J.A. (1997). Capacities of quantum erasure channels. PRL.
