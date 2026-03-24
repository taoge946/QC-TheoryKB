# NP-Hard Problems: Definitions, Reductions, and Inapproximability

> 组合优化中 NP-hard 问题的形式化定义、问题间的多项式归约关系，以及不可近似性结果。
>
> **References**: **[Boyd & Vandenberghe, Ch.1, §1.4]** (convex vs nonconvex); **[Cappart et al. 2023, §2]** (CO problem definitions); **[Bengio et al. 2021, §2]** (ML for CO problem landscape)

---

## 1. Complexity Classes: P, NP, NP-hard, NP-complete

### Definition 1.1 (P)

$$\text{P} = \bigcup_{k \geq 0} \text{DTIME}(n^k)$$

P 类是所有可以被确定性图灵机在多项式时间内判定的语言的集合。直观理解：存在高效（多项式时间）算法可以求解的问题类。

### Definition 1.2 (NP)

$$\text{NP} = \bigcup_{k \geq 0} \text{NTIME}(n^k)$$

等价定义（验证者视角）：语言 $L \in \text{NP}$ 当且仅当存在多项式时间确定性图灵机 $V$（验证器）和多项式 $p$，使得

$$x \in L \iff \exists \; y \in \{0,1\}^{p(|x|)} \; \text{s.t.} \; V(x, y) = 1$$

NP 类是所有可以在多项式时间内验证解的正确性的判定问题的集合。$y$ 称为"证书"或"证据"（certificate/witness）。

### Definition 1.3 (Polynomial-time Reduction)

语言 $A$ 多项式时间归约到语言 $B$（记作 $A \leq_p B$），如果存在多项式时间可计算函数 $f$ 使得

$$x \in A \iff f(x) \in B$$

若 $A \leq_p B$ 且 $B \in \text{P}$，则 $A \in \text{P}$。归约保持计算难度的"传递"：如果 $B$ 容易则 $A$ 也容易，逆否即如果 $A$ 难则 $B$ 也难。

### Definition 1.4 (NP-hard)

问题 $H$ 是 NP-hard 的，如果对所有 $L \in \text{NP}$，都有 $L \leq_p H$。

NP-hard 问题至少和 NP 中最难的问题一样难。NP-hard 问题本身不一定在 NP 中（可以是判定问题也可以是优化问题）。

### Definition 1.5 (NP-complete)

$$\text{NP-complete} = \text{NP-hard} \cap \text{NP}$$

NP-完全问题既属于 NP（解可以被多项式时间验证），又是 NP-hard 的（NP 中所有问题都可以归约到它）。Cook-Levin 定理证明 SAT 是第一个 NP-complete 问题。

**Source**: Arora & Barak, *Computational Complexity: A Modern Approach* (2009), Ch. 2-3

---

## 2. Polynomial Reductions: MIS ↔ MVC ↔ MCl

### Theorem 2.1 (MIS ↔ MVC Complement)

对于图 $G = (V, E)$，$S \subseteq V$ 是独立集当且仅当 $V \setminus S$ 是顶点覆盖。因此

$$\alpha(G) + \beta(G) = |V|$$

其中 $\alpha(G) = |$MIS$(G)|$ 是独立数，$\beta(G) = |$MVC$(G)|$ 是顶点覆盖数。

**Proof sketch.**

$(\Rightarrow)$：设 $S$ 是独立集。对任意边 $(u,v) \in E$，$u, v$ 不能同时在 $S$ 中，因此至少一个在 $V \setminus S$ 中，故 $V \setminus S$ 覆盖所有边。

$(\Leftarrow)$：设 $C$ 是顶点覆盖。若 $u, v \in V \setminus C$，则边 $(u,v)$ 不可能在 $E$ 中（否则 $C$ 不覆盖该边），故 $V \setminus C$ 是独立集。$\square$

### Theorem 2.2 (MIS ↔ MCl via Complement Graph)

$S$ 是图 $G$ 的独立集当且仅当 $S$ 是补图 $\bar{G}$ 的团。因此

$$\alpha(G) = \omega(\bar{G})$$

其中 $\omega(\bar{G})$ 是补图的团数（最大团大小）。

**Proof sketch.**

在 $G$ 中，$S$ 是独立集意味着 $S$ 中任意两点在 $G$ 中无边相连。在补图 $\bar{G}$ 中，$G$ 中不存在的边恰好存在，因此 $S$ 中任意两点在 $\bar{G}$ 中有边相连，即 $S$ 构成 $\bar{G}$ 的团。$\square$

### Corollary 2.3 (三问题等价性)

MIS、MVC、MCl 三个问题通过以下关系相互多项式归约：

$$\text{MIS}(G) \xleftrightarrow{\; V \setminus S \;} \text{MVC}(G) \xleftrightarrow{\; \bar{G} \;} \text{MCl}(\bar{G})$$

因此三者的计算复杂性完全等价：一个有多项式算法当且仅当其他两个也有。

**Source**: Garey & Johnson (1979), Ch. 3 | Papadimitriou, *Computational Complexity* (1994)

---

## 3. MaxCut NP-hardness

### Theorem 3.1 (MaxCut is NP-hard)

判定问题 MAX-CUT：给定图 $G = (V, E)$ 和整数 $k$，是否存在将 $V$ 分成 $(S, V \setminus S)$ 使得至少 $k$ 条边被割断？MAX-CUT 是 NP-complete 的。

**Proof sketch (reduction from NAE-3SAT).**

从 Not-All-Equal 3-SAT（NAE-3SAT）归约。NAE-3SAT 要求每个子句的三个文字不全为真也不全为假（每个子句至少有一个真和一个假）。

对于 NAE-3SAT 实例 $\phi$：
1. 对每个变量 $x_i$ 创建顶点 $v_i$（对应 $x_i$）和 $\bar{v}_i$（对应 $\neg x_i$），用大权重边连接确保它们在割的不同侧。
2. 对每个子句 $(l_a, l_b, l_c)$，构造一个三角形（gadget）连接对应文字的顶点。
3. NAE-3SAT 可满足当且仅当存在割值 $\geq k$（$k$ 由构造确定）。

由于 NAE-3SAT 是 NP-complete 的（从 3SAT 归约），MaxCut 也是 NP-complete 的。$\square$

**Source**: Garey, Johnson & Stockmeyer, *STOC* (1976) | Karp's 21 NP-complete problems (1972)

---

## 4. TSP and Hamiltonian Cycle

### Theorem 4.1 (Hamiltonian Cycle is NP-complete)

判定图 $G$ 中是否存在经过每个顶点恰好一次的回路（哈密顿回路）是 NP-complete 问题。

### Theorem 4.2 (TSP is NP-hard)

旅行商问题（TSP）的优化版本是 NP-hard 的。

**Proof sketch (reduction from Hamiltonian Cycle to TSP).**

给定图 $G = (V, E)$，构造 TSP 实例：
- 城市集合 = $V$
- 距离矩阵：$d_{ij} = 1$ 若 $(i,j) \in E$，$d_{ij} = 2$ 若 $(i,j) \notin E$

则 $G$ 有哈密顿回路当且仅当 TSP 最优解的总距离 $= |V|$。

这个归约也说明了一般 TSP（不满足三角不等式）不存在常数近似比算法（除非 P = NP）。$\square$

### Theorem 4.3 (Metric TSP Approximation — Christofides-Serdyukov)

对于满足三角不等式的 TSP（metric TSP），Christofides-Serdyukov 算法的近似比为 $\frac{3}{2}$：

$$\text{ALG} \leq \frac{3}{2} \cdot \text{OPT}$$

算法步骤：(1) 构造最小生成树 $T$；(2) 找 $T$ 中奇度顶点的最小权完美匹配 $M$；(3) 合并 $T \cup M$ 得欧拉图；(4) 求欧拉回路后"抄近路"得哈密顿回路。

**Source**: Christofides (1976) | Serdyukov (1978) | 近期 Karlin, Klein & Gharan 改进至 $\frac{3}{2} - \varepsilon$ (2021)

---

## 5. Approximation Hardness and the PCP Theorem

### Theorem 5.1 (PCP Theorem — Arora, Lund, Motwani, Sudan, Szegedy 1998)

$$\text{NP} = \text{PCP}[\log n, 1]$$

PCP 定理：NP 中每个语言都有概率可检验证明（Probabilistically Checkable Proof），验证器只需读取 $O(\log n)$ 个随机比特和常数个证明比特。

PCP 定理是近似不可能性结果的基石。它直接推出：对于 MAX-3SAT，不存在多项式时间 $(1-\varepsilon)$-近似算法（对某个 $\varepsilon > 0$），除非 P = NP。

### Corollary 5.2 (Approximation Hardness Cascade)

PCP 定理及其推广给出了一系列不可近似性结果：

| 问题 | 近似比下界 | 条件 |
|------|-----------|------|
| MAX-3SAT | $7/8 + \varepsilon$ 不可达 | P $\neq$ NP |
| MaxCut | $\alpha_{\text{GW}} + \varepsilon$ 不可超过 | Unique Games Conjecture |
| Set Cover | $(1-\varepsilon)\ln n$ 不可达 | P $\neq$ NP |
| MIS | $n^{1-\varepsilon}$ 不可达 | P $\neq$ NP |
| Chromatic Number | $n^{1-\varepsilon}$ 不可达 | P $\neq$ NP |

**Source**: Arora & Barak (2009), Ch. 11 | Dinur (2007) PCP 定理简化证明

---

## 6. Inapproximability of MIS

### Theorem 6.1 (MIS Inapproximability — Zuckerman 2007)

除非 P = NP，不存在多项式时间算法在 $n$ 个顶点的图上将最大独立集近似到 $n^{1-\varepsilon}$ 因子内，即对任意 $\varepsilon > 0$：

$$\nexists \; \text{poly-time } \mathcal{A} \; \text{s.t.} \; \frac{\alpha(G)}{\mathcal{A}(G)} \leq n^{1-\varepsilon} \; \forall G$$

**Proof idea (high-level).**

证明通过以下步骤链：
1. **PCP 定理** 将 NP 问题转化为约束满足问题（CSP），使得 YES 实例几乎全部约束可满足，NO 实例只有很少比例可满足。
2. **从 CSP 到 MIS 的归约**：构造"约束图"，其中顶点对应约束的满足赋值，边连接不相容的赋值对。满足所有约束等价于找到大独立集。
3. **间隙放大**：通过图的张量积（graph product）操作，将近似间隙从常数放大到多项式。若 $G$ 的独立数为 $\alpha$，则 $G^{\otimes k}$（$k$ 次张量积）的独立数为 $\alpha^k$，但图大小为 $n^k$，从而

$$\frac{\alpha(G^{\otimes k})}{|V(G^{\otimes k})|} = \left(\frac{\alpha(G)}{n}\right)^k$$

选择 $k = O(\log n / \varepsilon)$ 可将间隙放大到 $n^{1-\varepsilon}$。

### Remark 6.2

MIS 的强不可近似性使其成为组合优化中"最难近似"的问题之一。相比之下，MVC 有 2-近似（LP 舍入），MaxCut 有 0.878-近似（SDP 舍入），但 MIS 甚至不存在 $n^{0.999}$-近似。这也说明了为什么神经组合优化方法在 MIS 上的理论保证非常有限。

**Source**: Zuckerman, *STOC* (2007) | Hastad, *JACM* 46 (1999) | Khot, *STOC* (2001)

---

---

## 7. Cappart综述：CO问题的图结构视角 (Graph Perspective from Cappart et al.)

> 基于 **[Cappart et al. 2023, §2.1]**。

### 7.1 图作为CO的核心对象 **[Cappart et al. 2023, §1]**

**[Cappart et al. 2023, §1]** 指出：在Karp的21个NP-complete问题中，10个是图优化问题的判定版本。其余大多数（如集合覆盖）也可在图上建模。MIP中变量与约束的交互自然诱导二部图结构。

### 7.2 近似算法分类 **[Cappart et al. 2023, §2.1]**

**[Cappart et al. 2023, §2.1]** 给出近似算法的形式分类：

- **PTAS** (Polynomial-Time Approximation Scheme): 对任意 $\epsilon > 0$，在多项式时间内给出 $(1+\epsilon)$-近似解。例如 Arora (1996) 给出的欧几里得TSP的PTAS。
- **FPTAS** (Fully Polynomial-Time Approximation Scheme): 运行时间还关于 $1/\epsilon$ 为多项式。
- **元启发式** (Metaheuristics): 模拟退火、禁忌搜索、遗传算法、变邻域搜索等——无近似保证但在实践中有效。

### 7.3 Bengio等人的CO形式化 **[Bengio et al. 2021, §2.1]**

**[Bengio et al. 2021, §2.1]** 给出CO的标准形式化：

CO问题可表述为约束最小化程序。约束建模问题的自然或施加限制，变量定义需做出的决策，目标函数度量每个可行赋值的质量。若目标和约束均为线性，问题称为LP；若部分变量还限制为整数，则为MILP。

**[Bengio et al. 2021, §2.1]** 的关键洞察：MILP的NP-hardness与整数约束相关，去掉整数约束（LP松弛）后变为多项式可解。这直接启发了分支定界框架。

---

## 8. SAT问题的形式定义 (Boolean Satisfiability)

> **[Cappart et al. 2023, §2.1]**

**定义** **[Cappart et al. 2023, §2.1]**: 布尔可满足性问题（SAT）——给定命题逻辑公式 $\varphi$ 和变量集 $V$，是否存在使 $\varphi$ 为真的变量赋值？

SAT是第一个被证明为NP-complete的问题（Cook-Levin定理）。它是所有NP问题归约的起点。

---

---

## 9. Complexity Context from Convex Optimization **[Boyd & Vandenberghe, Ch.1, Ch.4]**

### 9.1 The Complexity Landscape: Convex vs Combinatorial

Boyd & Vandenberghe (2004) 强调了核心观点：**凸优化问题是"易处理的"，而组合优化问题通常是"难处理的"**。

**易处理（Tractable）**：
- LP, QP, SOCP, SDP 均可在多项式时间内求解（内点法）
- 凸优化的局部最优 = 全局最优
- KKT 条件给出充要的最优性条件

**难处理（Intractable）**：
- ILP, QUBO, MIS, MaxCut, TSP 是 NP-hard
- 局部搜索可能陷入局部最优
- 不存在多项式时间精确算法（除非 P = NP）

### 9.2 Convex Relaxation Hierarchy for CO **[Boyd & Vandenberghe, Ch.4; Lasserre 2001]**

系统的松弛层级，从弱到强：

1. **LP 松弛**：$x \in \{0,1\}^n \to x \in [0,1]^n$
2. **Sherali-Adams 层级**：通过乘积变量逐步加强 LP
3. **Lovász-Schrijver 层级**：结合 LP 和 SDP
4. **SDP (Lasserre) 层级**：用矩矩阵 $X \succeq 0$ 约束所有 $k$ 阶矩

Lasserre 层级的第 $r$ 层在 $n^{O(r)}$ 时间内可解，$r = n$ 时给出精确最优解。

### 9.3 Constraints Determine Complexity **[Boyd & Vandenberghe, Ch.1, Ch.4]**

| 问题 | 约束 | 复杂性 |
|------|------|--------|
| $\min c^\top x$, $Ax \leq b$, $x \geq 0$ | 连续、线性 | **P**（LP） |
| $\min c^\top x$, $Ax \leq b$, $x \in \{0,1\}^n$ | 整数 | **NP-hard**（ILP） |
| $\min x^\top Q x$, $x \in \mathbb{R}^n$ | 无约束、连续 | **P**（$Q \succeq 0$ 时） |
| $\min x^\top Q x$, $x \in \{-1,+1\}^n$ | 离散 | **NP-hard** |
| $\min \langle C, X \rangle$, $X \succeq 0$ | 矩阵半正定 | **P**（SDP） |
| $\min \langle C, X \rangle$, $X \succeq 0$, rank 1 | 矩阵 + 秩 | **NP-hard** |

核心洞察：**将离散/秩约束松弛为凸约束**是近似算法的基本范式。

### 9.4 Implications for Quantum Computing

- **QAOA** 的有限 $p$ 性能可与 SDP 松弛质量关联
- **量子退火** 原生求解 Ising/QUBO，但无已证明的超多项式加速
- **Grover** 对无结构搜索 $\sqrt{N}$ 加速，NP-complete 从 $2^n$ 到 $2^{n/2}$
- **量子 SDP 求解器**（Brandao-Svore 2016）在某些参数范围有多项式加速

---

> **See also**: [../key_formulas.md] (F10.2, F10.3, F10.4, F10.10) | [relaxation_methods.md] | [qubo_ising_mapping.md] | [convex_optimization_basics.md] | [duality_kkt.md]
