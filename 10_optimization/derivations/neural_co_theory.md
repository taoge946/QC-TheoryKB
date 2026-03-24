# Neural Combinatorial Optimization: Theory

> 神经组合优化的理论基础：注意力模型、GNN 热力图范式、扩散模型（DIFUSCO）、局部重采样（LoRe）。
>
> **References**: **[Bengio et al. 2021, §3--4]** (ML for CO survey); **[Cappart et al. 2023, §4--5]** (GNN for CO)

---

## 1. Attention Model (AM): Autoregressive Construction

### 1.1 Problem Setting

给定组合优化实例（如 TSP 中的城市坐标 $\{c_1, \ldots, c_n\}$），求最优序列 $\pi = (\pi_1, \ldots, \pi_n)$。

自回归方法将解的构造建模为序列决策：

$$p_\theta(\pi | \mathcal{G}) = \prod_{t=1}^{n} p_\theta(\pi_t | \pi_{1:t-1}, \mathcal{G})$$

其中 $\theta$ 是神经网络参数，$\mathcal{G}$ 是问题实例。

### 1.2 Encoder: Transformer-based Embedding

AM（Kool et al., 2019）使用 Multi-Head Attention (MHA) 编码器：

$$\mathbf{h}_i^{(l)} = \text{BN}\left(\mathbf{h}_i^{(l-1)} + \text{MHA}\left(\mathbf{h}_i^{(l-1)}, \{\mathbf{h}_j^{(l-1)}\}_{j}\right)\right)$$

$$\mathbf{h}_i^{(l)} \leftarrow \text{BN}\left(\mathbf{h}_i^{(l)} + \text{FF}(\mathbf{h}_i^{(l)})\right)$$

其中 BN 是 Batch Normalization，FF 是前馈网络。经过 $L$ 层后得到节点嵌入 $\{\mathbf{h}_i^{(L)}\}$。

### 1.3 Decoder: Sequential Selection

在第 $t$ 步，解码器计算选择概率：

$$u_{ij}^{(t)} = \begin{cases} C \cdot \tanh\left(\frac{\mathbf{q}^{(t) \top} \mathbf{k}_j}{\sqrt{d_k}}\right) & \text{if } j \notin \pi_{1:t-1} \\ -\infty & \text{otherwise} \end{cases}$$

$$p_\theta(\pi_t = j | \pi_{1:t-1}) = \frac{\exp(u_{ij}^{(t)})}{\sum_{j'} \exp(u_{ij'}^{(t)})}$$

其中 $\mathbf{q}^{(t)}$ 是由当前状态（上一步选择 + 全局嵌入）生成的 query，$\mathbf{k}_j = W^K \mathbf{h}_j^{(L)}$ 是各节点的 key，$C$ 是裁剪常数（通常 $C=10$）。

### 1.4 Training: REINFORCE with Baseline

使用策略梯度（REINFORCE）训练：

$$\nabla_\theta \mathcal{L} = \mathbb{E}_{\pi \sim p_\theta}\left[(L(\pi) - b(\mathcal{G})) \nabla_\theta \log p_\theta(\pi | \mathcal{G})\right]$$

其中 $L(\pi)$ 是解的代价（如路径长度），$b(\mathcal{G})$ 是基线（baseline），用于减小方差。AM 使用贪心 rollout 基线：$b(\mathcal{G}) = L(\pi^{\text{greedy}}_{\theta^{BL}})$，其中 $\theta^{BL}$ 是周期性更新的网络参数快照。

### 1.5 AM Encoder 详细架构 **[Kool et al. 2019, §3.1]**

AM 编码器是 Transformer 编码器的变体（无位置编码，使用 BN 代替 LN）。初始嵌入从 $d_x$ 维坐标线性投影到 $d_h = 128$ 维：

$$\mathbf{h}_i^{(0)} = W^x \mathbf{x}_i + \mathbf{b}^x$$

$N = 3$ 层注意力层，每层包含 MHA 和 FF 两个子层（均带 skip-connection + BN）**[Kool et al. 2019, §3.1, Eq.(2)-(3)]**：

$$\hat{\mathbf{h}}_i = \mathrm{BN}\left(\mathbf{h}_i^{(l-1)} + \mathrm{MHA}_i^l(\mathbf{h}_1^{(l-1)}, \ldots, \mathbf{h}_n^{(l-1)})\right)$$

$$\mathbf{h}_i^{(l)} = \mathrm{BN}\left(\hat{\mathbf{h}}_i + \mathrm{FF}^l(\hat{\mathbf{h}}_i)\right)$$

MHA 使用 $M = 8$ 个头，$d_k = d_v = d_h / M = 16$，FF 隐藏维度 512。图嵌入为所有节点嵌入的均值：$\bar{\mathbf{h}}^{(N)} = \frac{1}{n}\sum_i \mathbf{h}_i^{(N)}$。

**关键设计**：不使用位置编码，使得节点嵌入对输入顺序不变（置换不变性），这是处理图问题的正确归纳偏置。

### 1.6 AM Decoder 详细架构 **[Kool et al. 2019, §3.2]**

解码器在每步 $t$ 构造 context embedding，由图嵌入、上一步节点嵌入和首节点嵌入拼接而成：

$$\mathbf{h}_{(c)}^{(N)} = \begin{cases} [\bar{\mathbf{h}}^{(N)}, \mathbf{h}_{\pi_{t-1}}^{(N)}, \mathbf{h}_{\pi_1}^{(N)}] & t > 1 \\ [\bar{\mathbf{h}}^{(N)}, \mathbf{v}^l, \mathbf{v}^f] & t = 1 \end{cases}$$

其中 $\mathbf{v}^l, \mathbf{v}^f$ 是可学习的占位符。解码器执行两步注意力 **[Kool et al. 2019, §3.2]**：

**Step 1** (Glimpse)：多头注意力（$M=8$），仅对 context 节点计算 query，得到 $\mathbf{h}_{(c)}^{(N+1)}$

**Step 2** (Output)：单头注意力（$M=1$），计算带 tanh 裁剪的兼容性作为 logits：

$$u_{(c)j} = \begin{cases} C \cdot \tanh\left(\frac{\mathbf{q}_{(c)}^\top \mathbf{k}_j}{\sqrt{d_k}}\right) & j \notin \pi_{1:t-1} \\ -\infty & \text{otherwise} \end{cases}$$

$$p_\theta(\pi_t = j | s, \pi_{1:t-1}) = \mathrm{softmax}(u_{(c)j})_j$$

tanh 裁剪（$C = 10$）防止 logits 过大导致 softmax 饱和，是 Bello et al. (2016) 的技术。

### 1.7 Greedy Rollout Baseline **[Kool et al. 2019, §4]**

AM 的关键创新之一是使用贪心 rollout 基线代替传统的 critic 网络 **[Kool et al. 2019, §4]**：

$$b(s) = L(\pi^{\mathrm{greedy}}_{\theta^{\mathrm{BL}}})$$

核心思想：实例的难度可以通过算法在其上的表现来估计。基线策略 $\theta^{\mathrm{BL}}$ 每个 epoch 冻结一次，只有当当前策略在独立验证集上通过 paired t-test（$\alpha = 5\%$）显著优于基线时，才更新基线参数。

REINFORCE 梯度估计 **[Kool et al. 2019, §4, Eq.(2)]**：

$$\nabla \mathcal{L}(\theta | s) = \mathbb{E}_{p_\theta(\pi|s)}\left[(L(\pi) - b(s)) \nabla \log p_\theta(\pi | s)\right]$$

当 $L(\pi) < b(s)$（采样解优于贪心解）时，梯度方向强化该解的动作；反之则抑制。这类似于 AlphaGo 的自我对弈机制。

**Remark.** 自回归方法的局限：(1) 推理时间 $O(n)$ 步，无法并行；(2) 解的质量依赖于解码顺序，对不同问题需要设计特定的掩码（mask）逻辑；(3) 泛化到更大规模实例时性能退化。

**Source**: Kool, van Hoof & Welling, ICLR 2019 | Vinyals, Fortunato & Jaitly, NeurIPS 2015

---

## 2. GNN + Heatmap Paradigm (Non-autoregressive)

### 2.1 Core Idea

与自回归逐步构造不同，热力图范式（heatmap paradigm）一次性预测所有决策变量的概率：

$$\text{GNN}_\theta: \mathcal{G} \mapsto \mathbf{p} \in [0,1]^{n} \text{ (node-level)} \quad \text{or} \quad \mathbf{P} \in [0,1]^{n \times n} \text{ (edge-level)}$$

- **节点级**（MIS/MVC/MCl）：$p_i = \Pr[x_i = 1]$，即节点 $i$ 被选入解的概率
- **边级**（TSP/MaxCut）：$P_{ij} = \Pr[\text{edge } (i,j) \in \text{solution}]$

### 2.2 GNN Architecture

典型使用 Message Passing Neural Network (MPNN)：

$$\mathbf{m}_i^{(l)} = \sum_{j \in \mathcal{N}(i)} \phi^{(l)}(\mathbf{h}_i^{(l)}, \mathbf{h}_j^{(l)}, \mathbf{e}_{ij})$$

$$\mathbf{h}_i^{(l+1)} = \psi^{(l)}(\mathbf{h}_i^{(l)}, \mathbf{m}_i^{(l)})$$

其中 $\phi^{(l)}$ 是消息函数，$\psi^{(l)}$ 是更新函数，$\mathbf{e}_{ij}$ 是边特征。经过 $L$ 轮消息传递后：

$$p_i = \sigma(\text{MLP}(\mathbf{h}_i^{(L)})) \quad \text{或} \quad P_{ij} = \sigma(\text{MLP}(\mathbf{h}_i^{(L)} \| \mathbf{h}_j^{(L)} \| \mathbf{e}_{ij}))$$

其中 $\sigma$ 是 sigmoid 函数。

### 2.3 Training Objectives

**监督学习**（需要标签）：

$$\mathcal{L}_{\text{sup}} = -\sum_i \left[y_i \log p_i + (1-y_i) \log(1-p_i)\right]$$

其中 $y_i \in \{0,1\}$ 是最优解标签（由精确求解器获得）。

**无监督学习**（直接优化目标函数）：

$$\mathcal{L}_{\text{unsup}} = \mathbb{E}_{\mathbf{x} \sim \text{Bernoulli}(\mathbf{p})}[H_{\text{QUBO}}(\mathbf{x})]$$

利用直通估计（straight-through estimator）或 Gumbel-softmax 使采样可微。

**Source**: Li, Chen & Koltun, ICLR 2018 | Joshi, Laurent & Bresson, NeurIPS 2019

---

## 3. Decoding from Heatmaps

### 3.1 Greedy Decoding

最简单的解码策略：

$$x_i = \begin{cases} 1 & \text{if } p_i > 0.5 \\ 0 & \text{otherwise} \end{cases}$$

或对 TSP，从热力图 $\mathbf{P}$ 贪心构造：每步选择概率最高的未访问城市。

### 3.2 Beam Search Decoding

维护 $B$ 个候选（beams），在每步扩展时保留概率最高的 $B$ 个部分解：

$$\text{Score}(\pi_{1:t}) = \sum_{\tau=1}^{t} \log p(\pi_\tau | \pi_{1:\tau-1})$$

Beam search 牺牲推理速度换取更高的解质量，复杂度为 $O(Bn)$。

### 3.3 Sampling + Selection

从热力图采样多个候选解，返回最优的：

$$\mathbf{x}^{(k)} \sim \text{Bernoulli}(\mathbf{p}), \quad k = 1, \ldots, K$$

$$\mathbf{x}^* = \arg\min_{k} H(\mathbf{x}^{(k)}) \quad \text{s.t. } \mathbf{x}^{(k)} \text{ is feasible}$$

通过增大采样数 $K$ 可以提升解质量，利用的是热力图集中在高质量解上的概率质量。采样具有天然的可并行性。

**Source**: Joshi et al. (2019) | Sun et al., NeurIPS 2023

---

## 4. Local Search Post-processing

### 4.1 Motivation

神经网络输出的解通常近似但非最优。局部搜索（local search）通过在解的邻域中迭代改进：

$$\mathbf{x}^{(t+1)} = \arg\min_{\mathbf{x}' \in \mathcal{N}(\mathbf{x}^{(t)})} H(\mathbf{x}')$$

其中 $\mathcal{N}(\mathbf{x})$ 是 $\mathbf{x}$ 的邻域（如翻转一个变量、交换两个城市等）。

### 4.2 Common Neighborhoods

| 问题 | 邻域 | 描述 |
|------|------|------|
| MIS/MVC | 1-flip | 翻转一个节点的选择状态 |
| TSP | 2-opt | 删除两条边、重连为另一种方式 |
| TSP | Or-opt | 将一段子路径移到其他位置 |
| MaxCut | 1-swap | 将一个顶点移到另一侧 |

### 4.3 Neural-guided Local Search

用神经网络指导局部搜索的方向，而非盲目搜索：

$$\mathbf{x}' = \arg\min_{\mathbf{x}' \in \mathcal{N}(\mathbf{x})} \left[H(\mathbf{x}') - \lambda \log p_\theta(\mathbf{x}')\right]$$

神经网络的"先验"$p_\theta(\mathbf{x}')$ 引导搜索偏向高概率区域，减少无效搜索。

**Source**: Chen & Tian, ICLR 2019 | Xin et al., NeurIPS 2021

---

## 5. DIFUSCO: Diffusion as Iterative Refinement for CO

### 5.1 Core Idea

DIFUSCO（Sun et al., NeurIPS 2023）将扩散模型应用于组合优化。核心思想：将离散优化解的生成建模为去噪过程。

### 5.2 Forward Process (Noise Addition)

对于离散变量 $\mathbf{x} \in \{0,1\}^n$，使用 Bernoulli 噪声：

$$q(\mathbf{x}_t | \mathbf{x}_0) = \prod_i \text{Bernoulli}(x_{t,i} | \bar{\alpha}_t x_{0,i} + (1-\bar{\alpha}_t) \cdot 0.5)$$

在时间步 $t$，每个变量以概率 $1 - \bar{\alpha}_t$ 被随机翻转（趋向均匀分布 $0.5$）。$\bar{\alpha}_t$ 是噪声调度参数，从 $\bar{\alpha}_0 \approx 1$（几乎无噪声）衰减到 $\bar{\alpha}_T \approx 0$（完全噪声）。

也可使用连续高斯扩散（在 $[0,1]$ 上）：

$$q(\mathbf{x}_t | \mathbf{x}_0) = \mathcal{N}(\mathbf{x}_t; \sqrt{\bar{\alpha}_t} \mathbf{x}_0, (1-\bar{\alpha}_t)\mathbf{I})$$

### 5.3 Reverse Process (Denoising / Solution Generation)

训练去噪网络 $f_\theta(\mathbf{x}_t, t, \mathcal{G}) \approx \mathbf{x}_0$ 预测清洁解：

$$\mathcal{L}_{\text{DIFUSCO}} = \mathbb{E}_{t, \mathbf{x}_0, \mathbf{x}_t} \left[\|f_\theta(\mathbf{x}_t, t, \mathcal{G}) - \mathbf{x}_0\|^2\right]$$

去噪网络采用 GNN 架构（如 Graph Transformer），将时间步 $t$ 通过 sinusoidal embedding 注入。

### 5.4 Inference: Iterative Refinement

推理时，从纯噪声 $\mathbf{x}_T \sim \text{Uniform}$ 出发，逐步去噪：

$$\hat{\mathbf{x}}_0^{(t)} = f_\theta(\mathbf{x}_t, t, \mathcal{G})$$

$$\mathbf{x}_{t-1} \sim q(\mathbf{x}_{t-1} | \mathbf{x}_t, \hat{\mathbf{x}}_0^{(t)})$$

经过 $T$ 步后得到热力图 $\hat{\mathbf{x}}_0^{(1)}$，再通过贪心解码或采样获得离散解。

关键优势：扩散模型的迭代去噪过程可以逐步细化解的质量，比一次性预测更精确。多次采样（不同随机种子）可以探索解空间的多样性。

### 5.5 Training with Optimal Solutions

DIFUSCO 采用监督学习，训练数据 $\{(\mathcal{G}_i, \mathbf{x}_i^*)\}$ 中的 $\mathbf{x}_i^*$ 来自精确求解器（如 Gurobi）。网络学习在给定图结构和噪声水平下恢复最优解。

**Source**: Sun, Yang & Li, NeurIPS 2023

---

## 5.5: DiffUCO — Unsupervised CO with Diffusion

> **[DiffUCO, Sanokowski et al. 2024]**

### 5.5.1 核心思想 **[DiffUCO, §1]**

DiffUCO（Diffusion for Unsupervised Combinatorial Optimization）将扩散模型与**无监督**训练结合，消除了对最优解标签的依赖。不同于 DIFUSCO 需要精确求解器生成训练数据，DiffUCO 直接优化 CO 问题的目标函数（能量函数）。

### 5.5.2 能量基训练 **[DiffUCO, §3]**

给定 QUBO/Ising 形式的 CO 问题，目标函数 $H(\mathbf{x})$（如 MaxCut 的割值、MIS 的独立集大小）。DiffUCO 的训练目标是最小化去噪后解的期望能量：

$$\mathcal{L}_{\text{DiffUCO}} = \mathbb{E}_{\mathcal{G} \sim \mathcal{D}}\left[\mathbb{E}_{t, \mathbf{x}_t}\left[H\left(\hat{\mathbf{x}}_0^{(t)}\right) + \lambda \cdot \mathcal{P}(\hat{\mathbf{x}}_0^{(t)})\right]\right]$$

其中：
- $\hat{\mathbf{x}}_0^{(t)} = f_\theta(\mathbf{x}_t, t, \mathcal{G})$ 是网络在时间步 $t$ 对干净解的预测
- $H(\cdot)$ 是 CO 目标函数（需最小化或最大化）
- $\mathcal{P}(\cdot)$ 是约束违反的惩罚项（如 MIS 中相邻节点同时选中的惩罚）
- $\lambda$ 是惩罚系数

### 5.5.3 连续松弛 **[DiffUCO, §3]**

为了使能量函数对网络输出可微，DiffUCO 使用连续松弛：网络输出 $\hat{\mathbf{x}}_0 \in [0,1]^n$（通过 sigmoid），直接计算松弛后的能量：

$$H_{\text{relaxed}}(\mathbf{p}) = \sum_{(i,j) \in E} w_{ij} \cdot g(p_i, p_j) + \sum_i c_i \cdot p_i$$

其中 $g$ 是二次项的松弛（如 $x_i x_j \to p_i p_j$ 或使用 Gumbel-softmax 采样）。

### 5.5.4 与 DIFUSCO 的对比

| 特征 | DIFUSCO | DiffUCO |
|---|---|---|
| 训练方式 | **监督**（需要最优解标签） | **无监督**（直接优化目标函数） |
| 训练目标 | $\|\hat{\mathbf{x}}_0 - \mathbf{x}_0^*\|^2$ | $\mathbb{E}[H(\hat{\mathbf{x}}_0)]$ + 惩罚 |
| 标签获取 | 精确求解器（Gurobi等） | 不需要 |
| 可扩展性 | 受限于求解器的规模限制 | 原则上可扩展到任意规模 |
| 扩散过程 | Bernoulli / Gaussian | Bernoulli / Gaussian |
| 去噪网络 | GNN / Graph Transformer | GNN / Graph Transformer |

### 5.5.5 理论优势

1. **消除标签偏差**：无监督训练不受训练数据分布的限制（cf. Yehuda et al. 2020 的结果：多项式时间采样器生成的标签来自"更容易的子问题"）
2. **端到端优化**：直接优化 CO 目标函数，避免了监督学习中"学习近似最优解"与"直接优化目标"之间的 gap
3. **扩散的多样性**：扩散模型的随机性天然提供解的多样性，采样多个候选后选最优

**Source**: Sanokowski, Berger, Seidl & Hochreiter, NeurIPS 2024

---

## 6. LoRe: Local Resampling with Boundary Correction

### 6.1 Motivation

大规模 CO 问题（$n > 1000$）中，全局一次性预测的质量下降。LoRe（Li et al.）提出分治策略：在局部子问题上重采样并修正边界效应。

### 6.2 Framework

给定当前解 $\mathbf{x}$，LoRe 的一轮迭代：

1. **子问题选择**：选取局部区域 $\mathcal{R} \subset V$（通过空间邻近性或图距离）
2. **边界固定**：将 $\mathcal{R}$ 外的变量固定为当前值 $x_i$（$i \notin \mathcal{R}$）
3. **条件重采样**：用神经网络对子问题重新采样

$$\mathbf{x}_{\mathcal{R}}^{\text{new}} \sim p_\theta(\mathbf{x}_{\mathcal{R}} | \mathbf{x}_{V \setminus \mathcal{R}}, \mathcal{G})$$

4. **边界修正**：扩大修正区域到 $\mathcal{R}$ 的邻域 $\partial \mathcal{R}$，重新优化边界变量

### 6.3 Boundary Correction Theory

子问题的边界引入人为约束，可能导致次优解。设 $\mathbf{x}^*$ 是全局最优解，$\hat{\mathbf{x}}$ 是局部重采样解，边界修正的目标是减小

$$\Delta H = H(\hat{\mathbf{x}}) - H(\mathbf{x}^*) = \underbrace{H_{\text{interior}}}_{\text{子问题内部}} + \underbrace{H_{\text{boundary}}}_{\text{边界交互}}$$

边界修正通过"松弛-重优化"策略：先松弛边界变量，再对扩大的子问题重新求解，减小 $H_{\text{boundary}}$ 项。

### 6.4 Convergence

LoRe 可以视为一种随机化局部搜索。若子问题的选择覆盖所有变量（ergodicity），且每次局部重采样不劣于当前解（monotonicity），则

$$H(\mathbf{x}^{(t+1)}) \leq H(\mathbf{x}^{(t)})$$

序列 $\{H(\mathbf{x}^{(t)})\}$ 单调不增且有下界，因此收敛。收敛速度取决于子问题大小 $|\mathcal{R}|$ 与问题总规模 $n$ 的比值。

### 6.5 Integration with DIFUSCO

LoRe 天然与 DIFUSCO 结合：
- DIFUSCO 提供高质量的局部条件采样能力
- LoRe 提供可扩展的分治框架
- 组合后可处理 $n > 10000$ 的大规模实例

具体流程：(1) 用 DIFUSCO 生成初始全局解；(2) 迭代应用 LoRe 局部重采样；(3) 每次局部重采样使用 DIFUSCO 作为条件生成器；(4) 边界修正后接受或拒绝新解。

**Source**: Li et al. (BAQIS) | Sun et al., NeurIPS 2023

---

## Summary: Neural CO Paradigms

| 范式 | 代表方法 | 解构造方式 | 优点 | 局限 |
|------|---------|-----------|------|------|
| Autoregressive | AM, Pointer Network | 逐步选择 | 天然满足约束 | 推理慢，不可并行 |
| GNN + Heatmap | Joshi et al. | 一次性预测概率 | 并行，快速 | 需后处理保证可行性 |
| Diffusion (supervised) | DIFUSCO | 迭代去噪生成 | 高质量，多样性 | 训练需标签，多步推理 |
| Diffusion (unsupervised) | DiffUCO | 迭代去噪+能量优化 | 无需标签，端到端优化 | 连续松弛精度，惩罚调参 |
| Local Resampling | LoRe | 局部重采样+修正 | 可扩展到大规模 | 依赖基础模型质量 |

**核心理论联系**：所有神经 CO 方法本质上都在学习从问题实例到解的条件分布 $p(\mathbf{x} | \mathcal{G})$。差异在于如何参数化这个分布（自回归 vs 非自回归 vs 扩散）以及如何从中采样/解码。

---

## 7. GNN的形式化定义与消息传递 (Formal GNN Definition)

> 基于 **[Cappart et al. 2023, §2.3]** JMLR综述。

### 7.1 邻域聚合框架 **[Cappart et al. 2023, §2.3, Eq.(1)]**

设 $(G, l)$ 为带标签图，初始节点着色 $f^{(0)}: V(G) \to \mathbb{R}^{1 \times d}$ 与标签一致。GNN的每层 $t > 0$ 计算：

$$f^{(t)}(v) = \sigma\left(f^{(t-1)}(v) \cdot W_1^{(t)} + \sum_{w \in N(v)} f^{(t-1)}(w) \cdot W_2^{(t)}\right)$$

其中 $W_1^{(t)}, W_2^{(t)} \in \mathbb{R}^{d \times e}$ 为可训练参数矩阵，$\sigma$ 为非线性激活函数。**[Cappart et al. 2023, §2.3, Eq.(1)]**

### 7.2 通用消息传递形式 **[Cappart et al. 2023, §2.3, Eq.(2)]**

更一般地：

$$f^{(t)}(v) = f_{\text{merge}}^{W_1}\left(f^{(t-1)}(v), \; f_{\text{aggr}}^{W_2}\left(\{\!\!\{f^{(t-1)}(w) \mid w \in N(v)\}\!\!\}\right)\right)$$

其中 $f_{\text{aggr}}^{W_2}$ 对邻域特征的多重集（multiset）进行聚合，$f_{\text{merge}}^{W_1}$ 合并节点自身表示与邻域聚合结果。二者均为可微参数化函数。**[Cappart et al. 2023, §2.3, Eq.(2)]**

---

## 8. GNN表达能力的理论限制 (Expressivity Limits of GNNs)

> 基于 **[Cappart et al. 2023, §5.1]**。这些是GNN用于CO的核心理论结果。

### 8.1 Weisfeiler-Leman上界 **[Cappart et al. 2023, §5.1]**

**定理** (Morris et al. 2019, Xu et al. 2019, 引自 **[Cappart et al. 2023, §5.1]**): 任何GNN架构区分非同构图的能力，其上界为**1维Weisfeiler-Leman (1-WL)** 算法——图同构问题的经典多项式时间启发式。

1-WL已知的局限包括：
- 无法检测环结构信息
- 无法区分某些非同构二部图
- 存在多对1-WL无法区分的非同构图

**CO的直接影响**：这意味着存在成对的不等价MIP实例，**没有任何GNN架构能区分**。

### 8.2 更强表达力的GNN变体

为突破1-WL上界，已提出更高阶WL对应的GNN **[Cappart et al. 2023, §5.1]**：
- $k$-WL GNNs (Morris et al. 2019)
- Invariant Graph Networks (Maron et al. 2019)
- Random node features augmentation (Sato et al. 2020, Abboud et al. 2020)

然而，这些高阶模型通常**无法扩展到大规模图**，限制了其在CO中的实际应用。

### 8.3 GNN的近似比理论界 **[Cappart et al. 2023, §5.1]**

**定理** (Sato et al. 2019, 引自 **[Cappart et al. 2023, §5.1]**): 通过分布式局部算法的结果迁移，一大类GNN在以下问题上可达到的最佳近似比为：

| 问题 | GNN最佳近似比 | 最佳经典算法 |
|------|-------------|------------|
| 最小顶点覆盖 (MVC) | **2** | $2 - \Theta(1/\sqrt{\log n})$ |
| 最小支配集 | 次最优 | $O(\log n)$ |
| 最大匹配 | 次最优 | 精确（多项式时间） |

即GNN在MVC上的近似比为2，这是**次最优的**（经典算法可以做得更好）。**[Cappart et al. 2023, §5.1, Sato et al. 2019]**

### 8.4 GNN的最小深度和宽度要求 **[Cappart et al. 2023, §5.1]**

**定理** (Loukas 2020, 引自 **[Cappart et al. 2023, §5.1]**): 某些GNN可能太"小"而无法计算图的某些性质（如直径、最小生成树），并给出了此类任务的最小深度和宽度要求。

---

## 9. GNN泛化理论 (Generalization Theory)

> **[Cappart et al. 2023, §5.1]** 与 **[Bengio et al. 2021, §1]**。

### 9.1 泛化界 **[Cappart et al. 2023, §5.1]**

**定理** (Garg et al. 2020, 引自 **[Cappart et al. 2023, §5.1]**): 一大类GNN的泛化界主要依赖于：
- 图的最大度
- GNN层数
- 宽度
- 学习参数矩阵的范数

重要推论：泛化界**强烈依赖于输入稀疏性**——图越稠密，GNN的泛化能力越差。

### 9.2 训练数据的固有限制 **[Cappart et al. 2023, §5.1]**

**定理** (Yehuda et al. 2020, 引自 **[Cappart et al. 2023, §5.1]**): 假设NP $\neq$ co-NP，任何多项式时间样本生成器对NP-hard问题生成的样本来自一个**更容易的子问题**。这意味着监督方法在NP-hard CO任务上的观测性能指标可能被**高估**。

### 9.3 Bengio等人的分布视角 **[Bengio et al. 2021, §1]**

**[Bengio et al. 2021, §1]** 提出ML4CO的核心框架：将优化问题视为数据点，从**问题分布**的角度思考学习。

形式化地，设 $P$ 为问题实例的未知联合分布。监督学习目标：

$$\min_{\theta \in \mathbb{R}^p} \mathbb{E}_{X, Y \sim P} \, \ell(Y, f_\theta(X))$$

由于 $P$ 未知，用经验分布近似：

$$\min_{\theta \in \mathbb{R}^p} \sum_{(x, y) \in D_{\text{train}}} \frac{1}{|D_{\text{train}}|} \ell(y, f_\theta(x))$$

**[Bengio et al. 2021, §2, Eq.(2)-(3)]**

关键洞察：ML4CO算法在训练分布上表现好，但**分布外泛化**仍是开放挑战。传统CO算法本身也常针对特定问题结构优化，而非对所有可能实例通用。

---

## 10. ML增强精确求解器 (ML-Enhanced Exact Solvers)

> 基于 **[Cappart et al. 2023, §3.2]** 和 **[Bengio et al. 2021, §3]**。

### 10.1 分支定界中的ML **[Bengio et al. 2021, §3]**

分支定界（Branch-and-Bound）是MIP求解的核心框架。关键决策点包括：
- **分支变量选择**：选择哪个分数变量进行分支
- **节点选择**：在搜索树中选择下一个探索节点
- **切割平面选择**：选择添加哪些有效不等式

**[Bengio et al. 2021, §3]** 指出：ML可以通过**模仿学习**（imitation learning）学习强分支（strong branching）策略的近似，以低得多的计算成本做出接近最优的决策。

### 10.2 ML在CO中的两种范式 **[Bengio et al. 2021, §3]**

**[Bengio et al. 2021, §3]** 区分两种正交视角：

1. **学习方法维度**：
   - 模仿学习（Imitation Learning）：从专家（如强分支oracle）收集决策数据进行监督训练
   - 强化学习（RL）：通过试错交互发现最优策略

2. **算法结构维度**：
   - 端到端学习（End-to-end）：神经网络直接输出完整解
   - 嵌入式学习（ML inside CO）：ML作为现有求解器的组件

**[Bengio et al. 2021, §3]** 强调：虽然ML是近似的，但集成到CO中不一定意味着丧失理论保证。

---

## 11. GNN用于CO的系统分类 (Taxonomy of GNN for CO)

> **[Cappart et al. 2023, §3-4]**

### 11.1 原始侧：寻找可行解 **[Cappart et al. 2023, §3]**

GNN可用于：
- **直接启发式**：GNN一次性预测解或逐步构造解
- **学习搜索启发式**：GNN生成热力图指导局部搜索
- **连续松弛代理**：GNN的连续输出作为离散优化的代理损失

### 11.2 对偶侧：证明最优性 **[Cappart et al. 2023, §4]**

GNN增强精确算法：
- **分支策略**：用GNN模仿强分支
- **切割平面**：用GNN选择有效切割
- **分解策略**：用GNN指导Dantzig-Wolfe分解

### 11.3 算法推理 **[Cappart et al. 2023, §4.3]**

GNN作为算法执行器：在潜空间中模拟经典组合算法的迭代步骤，允许将算法泛化到自然（非抽象化）输入。

---

## 12. 过平滑与瓶颈问题 (Over-smoothing and Bottleneck)

> **[Cappart et al. 2023, §5.1]**

### 12.1 过平滑 **[Cappart et al. 2023, §5.1]**

GNN节点特征在多层传递后趋于不可区分。这限制了GNN捕获全局信息的能力——而许多CO问题需要全局结构信息（如最短路径）。

### 12.2 表示瓶颈 **[Cappart et al. 2023, §5.1]**

GNN难以准确表示大邻域信息（Alon & Yahav 2021）。这同样限制了捕获长程依赖的能力。

---

> **See also**: [../key_formulas.md] (F10.13, F10.14, F10.15) | [qubo_ising_mapping.md] | [np_hard_problems.md]
