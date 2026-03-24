# Routing Algorithms

> **Tags**: `sabre`, `olsq`, `token-swapping`, `a-star`, `routing`, `heuristic`, `optimal`

## Statement

量子比特路由算法是量子线路编译器的核心组件，负责在有限连通性的硬件上实现逻辑线路。现有算法覆盖从精确求解到快速启发式的完整谱：OLSQ 提供最优解但只适用于小规模实例，SABRE 在可接受时间内给出高质量的启发式解，是目前工业编译器的标准选择。

## Prerequisites

- **量子比特路由理论**：[derivations/qubit_routing_theory.md]
- **图论**：最短路径算法、图搜索
- **组合优化**：SAT/SMT、整数线性规划
- **搜索算法**：A* 搜索、启发式设计

---

## Derivation

### Step 1: SABRE Algorithm **[Li et al., ASPLOS 2019]**

SABRE（SWAP-based Bidirectional heuristic search Algorithm for REversible computation）是目前最广泛使用的路由算法，被 Qiskit、t|ket>、Cirq 等主流编译器采用。

**核心思想**：维护一个**前沿层**（front layer），贪心地选择使前沿层中不满足邻接约束的门距离减小最多的 SWAP。

**算法流程**：

```
Input: 逻辑线路 C, 耦合图 G, 初始映射 π₀
Output: 物理线路 C', 最终映射 π_final

1. 构建 DAG(C)，初始化前沿层 F ← DAG 的根节点集
2. while F ≠ ∅:
3.   // 执行所有可直接执行的门
4.   for gate(q_i, q_j) ∈ F:
5.     if (π(q_i), π(q_j)) ∈ E:
6.       执行 gate, 从 F 中移除, 更新 F 加入后继门
7.   // 若还有不满足约束的门, 选择最优 SWAP
8.   if F 中仍有不可执行的门:
9.     candidates ← {SWAP(u,v) : (u,v) ∈ E, u 或 v 涉及 F 中的量子比特}
10.    best_swap ← argmin_{s ∈ candidates} H(s)
11.    执行 best_swap, 更新 π
12. return C', π_final
```

**代价函数 $H$**（核心公式）：

对于候选 SWAP$(u, v)$，设执行后映射为 $\pi'$：

$$H(\text{SWAP}) = H_{\text{basic}} + W \cdot H_{\text{extended}}$$

$$H_{\text{basic}} = \frac{1}{|F|} \sum_{\text{gate}(q_i, q_j) \in F} d_G(\pi'(q_i), \pi'(q_j))$$

$$H_{\text{extended}} = \frac{1}{|E_{\text{set}}|} \sum_{\text{gate}(q_i, q_j) \in E_{\text{set}}} d_G(\pi'(q_i), \pi'(q_j))$$

其中：
- $F$：前沿层（当前可调度但不满足约束的门）
- $E_{\text{set}}$：扩展集（前沿层之后的下一批门，提供前瞻信息）
- $W$：权重参数，控制前瞻的重要性（原文 $W = 0.5$）
- $d_G$：耦合图上的最短路径距离（预计算的距离矩阵）

**双向搜索策略**：SABRE 的关键创新是**双向遍历**：

1. **前向遍历**：从 $\pi_0$ 开始，按门的时序顺序处理，得到映射 $\pi_{\text{fwd}}$
2. **反向遍历**：以 $\pi_{\text{fwd}}$ 为初始映射，**逆序**处理门（等价于反转线路），得到 $\pi_{\text{bwd}}$
3. **重复**：以 $\pi_{\text{bwd}}$ 为新的初始映射，再次前向遍历
4. **收敛**：交替进行直到连续两轮的 SWAP 数不再减少

双向搜索的效果是**同时优化初始映射和 SWAP 插入**，因为反向遍历隐式优化了前向遍历的初始映射。

**时间复杂度**：

$$T_{\text{SABRE}} = O(|G_{\text{gates}}| \cdot |E_{\text{hw}}| \cdot d_{\max} \cdot N_{\text{iter}})$$

其中 $|G_{\text{gates}}|$ 是门数，$|E_{\text{hw}}|$ 是耦合图边数，$d_{\max}$ 是图直径，$N_{\text{iter}}$ 是双向搜索迭代次数（通常 3--5）。

### Step 2: OLSQ — Optimal Layout Synthesis **[Tan & Cong, ICCAD 2020; DAC 2021]**

OLSQ（Optimal Layout Synthesis for Quantum computing）使用 **SMT**（Satisfiability Modulo Theories）求解器来寻找**最优**的映射和路由方案。

**决策变量**：

对于时间步 $t = 0, 1, \ldots, T$ 和逻辑量子比特 $q \in Q$：

$$\pi_t(q) \in V \quad \text{（量子比特 } q \text{ 在时间 } t \text{ 的物理位置）}$$

**约束条件**：

1. **单射约束**（不同逻辑量子比特不能映射到同一物理位置）：
$$\forall t, \forall q_i \neq q_j: \; \pi_t(q_i) \neq \pi_t(q_j)$$

2. **邻接约束**（两量子比特门的量子比特必须相邻）：
$$\forall \text{gate}(q_i, q_j) \text{ at time } t: \; (\pi_t(q_i), \pi_t(q_j)) \in E$$

3. **SWAP 一致性**（映射变化只能由 SWAP 引起）：
$$\pi_{t+1}(q) = \begin{cases} \pi_t(q') & \text{if SWAP}(\pi_t(q), \pi_t(q')) \text{ at time } t \\ \pi_t(q) & \text{otherwise} \end{cases}$$

4. **依赖约束**（门的执行顺序必须满足数据依赖）：
$$\forall g_1 \prec g_2: \; t(g_2) > t(g_1)$$

**目标函数**：

$$\min \sum_{t=0}^{T} \sum_{(u,v) \in E} s_{t,u,v}$$

其中 $s_{t,u,v} \in \{0, 1\}$ 表示在时间 $t$ 是否在边 $(u,v)$ 上执行 SWAP。

**OLSQ-TB**（Transition Based）[Tan & Cong, DAC 2021]：通过引入**转换点**（transition point）减少变量数。不为每个时间步建模，而只在映射发生变化时记录：

$$T_{\text{variables}} = O(|Q| \cdot L) \quad \text{vs.} \quad O(|Q| \cdot T) \text{ (原始 OLSQ)}$$

其中 $L$ 是 SWAP 层数（远小于总时间步 $T$）。

**可扩展性**：

| 方法 | 量子比特数 | 门数 | 求解时间 |
|------|----------|------|---------|
| OLSQ (精确) | $\leq 20$ | $\leq 100$ | 分钟级 |
| OLSQ-TB | $\leq 50$ | $\leq 500$ | 分钟级 |
| SABRE | $\leq 1000+$ | $\leq 100000+$ | 秒级 |

### Step 3: Token Swapping Algorithms **[Miltzow et al., ESA 2016; Vaughan, 2015]**

Token Swapping 在特殊图上有精确算法。

**树上的 Token Swapping** [Vaughan, 2015]：

**算法（Happy Swap）**：
```
while 存在不在目标位置的 token:
    找到叶子节点 v，其 token t 的目标不是 v
    将 t 沿最短路径向目标移动一步（SWAP with parent）
    如果移动使某个 token "happy"（到达目标），优先执行
```

**定理**：Happy Swap 在树上给出最优解。

**证明思路**：在树上，每次 SWAP 至少使一个 token 更接近目标（或到达目标）。由于树上任意两点间路径唯一，不存在"绕路"的情况。最终所需 SWAP 数恰好等于下界 $\frac{1}{2}\sum_v d(v, \sigma(v))$。

**路径图上的 Token Swapping**（冒泡排序）：

在路径 $P_n$ 上，Token Swapping 等价于冒泡排序（bubble sort）。逆序数（inversion count）恰好等于所需 SWAP 数：

$$\text{SWAP count} = \text{inv}(\sigma) = |\{(i,j) : i < j, \; \sigma(i) > \sigma(j)\}|$$

**4-近似算法（一般图）** [Miltzow et al., ESA 2016]：

```
for each token t not at target:
    move t along shortest path to target
    (may temporarily displace other tokens)
```

近似比分析：每个 token 移动 $d(v, \sigma(v))$ 步，总步数 $\leq 2\sum_v d(v, \sigma(v))$（考虑被 displaced 的 token 的额外移动）。下界为 $\frac{1}{2}\sum_v d(v, \sigma(v))$，因此近似比为 4。

### Step 4: A* Search for Routing **[Zulehner et al., DATE 2018; Zhou et al., DAC 2020]**

A* 搜索可以用于寻找**最优**的 SWAP 序列。

**状态空间**：
- **状态** $s = (\pi, F)$：当前映射 $\pi$ 和当前前沿层 $F$
- **初始状态**：$s_0 = (\pi_0, F_0)$
- **目标状态**：$F = \emptyset$（所有门已执行）
- **转移**：执行一个 SWAP（修改 $\pi$）或执行一个满足约束的门（修改 $F$）

**启发式函数**（admissible heuristic）：

$$h(s) = \sum_{\text{gate}(q_i, q_j) \in \text{remaining}} \max(d_G(\pi(q_i), \pi(q_j)) - 1, 0)$$

这是**松弛下界**：假设每对量子比特独立路由，忽略路径冲突。

**改进启发式**（考虑未来门）[Zhou et al., DAC 2020]：

$$h'(s) = h(s) + \alpha \sum_{\text{gate} \in \text{lookahead}} \max(d_G(\pi(q_i), \pi(q_j)) - 1, 0) / |\text{lookahead}|$$

其中 lookahead 包含未来若干层的门。

**可扩展性限制**：状态空间大小为 $O(|V|! \cdot 2^{|G_{\text{gates}}|})$，指数级增长。实际中只能处理小规模实例（$\leq 20$ 量子比特，$\leq 50$ 门）。

### Step 5: Other Notable Approaches

**Noise-Aware Routing** [Murali et al., ASPLOS 2019; Tannu & Qureshi, MICRO 2019]：

考虑硬件噪声的非均匀性，将门保真度纳入路由代价：

$$H_{\text{noise}}(\text{SWAP}) = H_{\text{basic}} + \lambda \sum_{\text{executed gates}} (1 - f_{\text{gate}})$$

其中 $f_{\text{gate}}$ 是从硬件校准数据获取的门保真度。

**RL-based Routing** [Pozzi et al., ACM TQCI 2022; Fosel et al., 2021]：

用强化学习训练路由策略。状态为 $(\pi, F, G)$，动作为选择 SWAP 或执行门，奖励为 $-1$（每步惩罚）或 $+r$（执行门奖励）。

**Temporal Planning** [Botea et al., AAAI 2018]：

将路由问题建模为**时间规划**（temporal planning）问题，使用 PDDL 语言描述，调用规划求解器。

---

## Comparison Table

| 算法 | 类型 | 最优性 | 可扩展性 | 时间复杂度 | 核心技术 | 引用 |
|------|------|--------|---------|----------|---------|------|
| SABRE | 启发式 | 否 | +++++ | $O(mn \cdot d)$ | 贪心+双向搜索 | Li 2019 |
| t\|ket> | 启发式 | 否 | +++++ | $O(mn)$ | 图划分+路由 | Cowtan 2019 |
| OLSQ | 精确(SMT) | 是 | ++ | 指数级 | SMT 求解 | Tan 2020 |
| OLSQ-TB | 精确(SMT) | 是 | +++ | 指数级(更快) | 转换点+SMT | Tan 2021 |
| A* Search | 精确 | 是 | + | 指数级 | A*+启发式 | Zulehner 2018 |
| RL-based | 学习型 | 否 | ++++ | 推理 $O(mn)$ | 强化学习 | Pozzi 2022 |
| Noise-Aware | 启发式 | 否 | ++++ | $O(mn \cdot d)$ | 噪声感知代价 | Murali 2019 |

注：$m$ = 门数，$n$ = 量子比特数，$d$ = 耦合图直径。可扩展性用 + 表示（越多越好）。

---

## Key Insights for QROB Project

1. **SABRE 是 baseline**：大多数工作以 SABRE 为基准，QROB 也应如此
2. **噪声感知是重要方向**：在真实硬件上，考虑噪声的路由显著优于忽略噪声的路由
3. **深度 vs 门数权衡**：有时牺牲少量门数可以显著减少深度（反之亦然）
4. **初始映射很重要**：好的初始映射可以减少 30%--50% 的 SWAP 数 [Siraichi 2018]
5. **RL 方法的优势**：可以学习到针对特定硬件拓扑的路由策略，但泛化性是挑战

---

## References

1. Li, G., Ding, Y. & Xie, Y. "Tackling the qubit mapping problem for NISQ-era quantum devices." *ASPLOS 2019*. -- SABRE
2. Cowtan, A., et al. "On the qubit routing problem." *TCAD 2019*. -- t|ket> 路由
3. Tan, B. & Cong, J. "Optimal layout synthesis for quantum computing." *ICCAD 2020*. -- OLSQ
4. Tan, B. & Cong, J. "Optimal layout synthesis for quantum computing (extended)." *DAC 2021*. -- OLSQ-TB
5. Zulehner, A., Paler, A. & Wille, R. "An efficient methodology for mapping quantum circuits." *DATE 2018*. -- A* 方法
6. Zhou, X., Li, S. & Feng, Y. "Quantum circuit transformation based on subgraph isomorphism and tabu search." *DAC 2020*.
7. Miltzow, T., et al. "Approximation and hardness for Token Swapping." *ESA 2016*.
8. Vaughan, J. "Token swapping on trees." *ArXiv 2015*.
9. Murali, P., et al. "Noise-adaptive compiler mappings." *ASPLOS 2019*.
10. Pozzi, M. G., et al. "Using reinforcement learning to perform qubit routing." *ACM TQCI 2022*.
11. Botea, A., Kishimoto, A. & Marinescu, R. "On the complexity of quantum circuit compilation." *AAAI 2018*.
