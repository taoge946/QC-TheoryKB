# Attention Mechanism: Complete Theory

> **Tags**: `attention`, `transformer`, `self-attention`, `multi-head-attention`, `positional-encoding`, `gnn`

## Statement

推导注意力机制的完整数学理论，包括缩放点积注意力、多头注意力、位置编码、Transformer编码器-解码器架构，以及与图神经网络的深层联系。证明自注意力是完全图上消息传递的特例。

## Prerequisites

- 线性代数：矩阵乘法、softmax 函数
- 概率论：方差分析、独立随机变量
- GNN基础：消息传递框架（见 [gnn_message_passing.md]）
- 神经网络基础：残差连接、层归一化

---

## Part 1: Dot-Product Attention

### 1.1 基本定义 **[Vaswani et al. 2017, §3.2.1]**

注意力函数将一个 query 和一组 key-value 对映射为输出。输出是 values 的加权和，权重由 query 与对应 key 的兼容性函数决定。

给定：
- Query 矩阵 $Q \in \mathbb{R}^{n \times d_k}$
- Key 矩阵 $K \in \mathbb{R}^{m \times d_k}$
- Value 矩阵 $V \in \mathbb{R}^{m \times d_v}$

**Scaled Dot-Product Attention:**

$$\boxed{\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V}$$

其中 softmax 沿最后一个维度（key 维度）计算。

### 1.2 缩放因子 $\sqrt{d_k}$ 的推导 **[Vaswani et al. 2017, §3.2.1, footnote]**

**为什么需要缩放？**

假设 $q, k \in \mathbb{R}^{d_k}$ 的各分量为独立随机变量，均值为 0，方差为 1。

**Step 1**: 点积的均值

$$\mathbb{E}[q \cdot k] = \mathbb{E}\left[\sum_{i=1}^{d_k} q_i k_i\right] = \sum_{i=1}^{d_k} \mathbb{E}[q_i]\mathbb{E}[k_i] = 0$$

**Step 2**: 点积的方差

$$\mathrm{Var}(q \cdot k) = \mathbb{E}[(q \cdot k)^2] - (\mathbb{E}[q \cdot k])^2 = \mathbb{E}[(q \cdot k)^2]$$

由独立性：

$$\mathbb{E}[(q \cdot k)^2] = \mathbb{E}\left[\left(\sum_i q_i k_i\right)^2\right] = \sum_i \mathbb{E}[q_i^2]\mathbb{E}[k_i^2] = \sum_i 1 \cdot 1 = d_k$$

因此 $\mathrm{Var}(q \cdot k) = d_k$。

**Step 3**: 缩放后的方差

$$\mathrm{Var}\left(\frac{q \cdot k}{\sqrt{d_k}}\right) = \frac{1}{d_k} \mathrm{Var}(q \cdot k) = \frac{d_k}{d_k} = 1$$

**结论**: 除以 $\sqrt{d_k}$ 将点积的方差归一化为 1，防止当 $d_k$ 较大时点积值过大导致 softmax 进入饱和区域（梯度趋近于零）。

### 1.3 Softmax 饱和分析

当点积值 $z_i$ 的方差很大时，softmax 输出趋向 one-hot 分布：

$$\mathrm{softmax}(z)_i = \frac{e^{z_i}}{\sum_j e^{z_j}} \xrightarrow{|z_i - z_j| \to \infty} \begin{cases} 1 & i = \arg\max_j z_j \\ 0 & \text{otherwise} \end{cases}$$

此时 $\frac{\partial \mathrm{softmax}(z)_i}{\partial z_j} \approx 0$，梯度消失。缩放避免了此问题。

### 1.4 与加性注意力的比较 **[Vaswani et al. 2017, §3.2.1]**

加性注意力（Bahdanau attention）使用前馈网络计算兼容性：

$$e_{ij} = v^\top \tanh(W_1 q_i + W_2 k_j)$$

点积注意力与加性注意力在理论复杂度上相似，但点积注意力可利用高度优化的矩阵乘法实现，在实践中更快、更节省空间。对于较小的 $d_k$，两者表现相似；对于较大的 $d_k$，加性注意力优于未缩放的点积注意力。

---

## Part 2: Multi-Head Attention

### 2.1 动机 **[Vaswani et al. 2017, §3.2.2]**

单头注意力使用单一的注意力权重矩阵，限制了模型同时关注不同表示子空间的能力。多头注意力允许模型在不同位置联合关注来自不同子空间的信息。

### 2.2 公式 **[Vaswani et al. 2017, §3.2.2]**

$$\boxed{\mathrm{MultiHead}(Q, K, V) = \mathrm{Concat}(\mathrm{head}_1, \ldots, \mathrm{head}_h) W^O}$$

$$\mathrm{head}_i = \mathrm{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

参数矩阵：
- $W_i^Q \in \mathbb{R}^{d_{\mathrm{model}} \times d_k}$
- $W_i^K \in \mathbb{R}^{d_{\mathrm{model}} \times d_k}$
- $W_i^V \in \mathbb{R}^{d_{\mathrm{model}} \times d_v}$
- $W^O \in \mathbb{R}^{hd_v \times d_{\mathrm{model}}}$

### 2.3 维度设置 **[Vaswani et al. 2017, §3.2.2]**

Vaswani et al. 使用 $h = 8$ 个头，$d_k = d_v = d_{\mathrm{model}} / h = 64$（$d_{\mathrm{model}} = 512$）。

由于每个头的维度降低，多头注意力的总计算量与全维度单头注意力相当：

$$h \cdot O(n^2 \cdot d_k) = h \cdot O\left(n^2 \cdot \frac{d_{\mathrm{model}}}{h}\right) = O(n^2 \cdot d_{\mathrm{model}})$$

### 2.4 展开形式

设 $\mathbf{h}_i \in \mathbb{R}^{d_{\mathrm{model}}}$ 为节点 $i$ 的嵌入，则第 $m$ 个头的注意力权重和输出为：

$$\alpha_{ij}^{(m)} = \frac{\exp\left(\frac{(\mathbf{h}_i W_m^Q)(W_m^K)^\top \mathbf{h}_j^\top}{\sqrt{d_k}}\right)}{\sum_{j'} \exp\left(\frac{(\mathbf{h}_i W_m^Q)(W_m^K)^\top \mathbf{h}_{j'}^\top}{\sqrt{d_k}}\right)}$$

$$\mathrm{head}_m = \sum_j \alpha_{ij}^{(m)} \cdot \mathbf{h}_j W_m^V$$

$$\mathrm{MHA}_i = \mathrm{Concat}(\mathrm{head}_1, \ldots, \mathrm{head}_h) W^O = \sum_{m=1}^{h} W_m^O \mathrm{head}_m$$

最后一个等式说明输出投影可等价地表示为各头输出的加权求和（Kool et al. 使用此形式）**[Kool et al. 2019, Appendix A]**。

---

## Part 3: Self-Attention as Message Passing on Complete Graph

### 3.1 Self-Attention 定义 **[Vaswani et al. 2017, §3.2.3]**

在 self-attention 中，queries、keys、values 全部来自同一序列。设输入序列 $H = [\mathbf{h}_1, \ldots, \mathbf{h}_n]^\top \in \mathbb{R}^{n \times d}$：

$$Q = HW^Q, \quad K = HW^K, \quad V = HW^V$$

每个位置可以 attend 到所有其他位置，形成全连接的信息交换。

### 3.2 MPNN 框架回顾

MPNN 的通用公式（见 [gnn_message_passing.md]）：

$$m_{u \to v}^{(l)} = M^{(l)}(h_v^{(l)}, h_u^{(l)}, e_{uv})$$

$$m_v^{(l)} = \bigoplus_{u \in \mathcal{N}(v)} m_{u \to v}^{(l)}$$

$$h_v^{(l+1)} = U^{(l)}(h_v^{(l)}, m_v^{(l)})$$

### 3.3 Transformer 作为 MPNN 的特例

**定理**: 单头 self-attention 是完全图 $K_n$ 上的一种特殊消息传递，其中邻居集 $\mathcal{N}(v) = V$（所有节点）。

| MPNN 组件 | Self-Attention 对应 |
|---|---|
| 图结构 | 完全图 $K_n$，$\mathcal{N}(v) = V \setminus \{v\}$（或含自环 $V$）|
| Message $M$ | $m_{u \to v} = \alpha_{vu} \cdot (h_u W^V)$，其中 $\alpha_{vu} = \mathrm{softmax}_u\left(\frac{(h_v W^Q)(h_u W^K)^\top}{\sqrt{d_k}}\right)$ |
| Aggregate $\bigoplus$ | 加权求和 $\sum_{u}$（权重由 softmax 归一化） |
| Update $U$ | 残差连接 + 层归一化 + FFN |

**证明**:

Self-attention 层对节点 $v$ 的更新可写为：

$$\hat{h}_v = \sum_{u=1}^{n} \alpha_{vu} \cdot h_u W^V$$

其中 $\alpha_{vu} = \frac{\exp(h_v W^Q (W^K)^\top h_u^\top / \sqrt{d_k})}{\sum_{u'} \exp(h_v W^Q (W^K)^\top h_{u'}^\top / \sqrt{d_k})}$

这精确对应于在完全图上的消息传递：
1. **消息函数** $M$：对每个邻居 $u$，计算 value $h_u W^V$ 并乘以数据依赖的注意力权重 $\alpha_{vu}$
2. **聚合函数** $\bigoplus = \sum$：加权求和（softmax 保证权重归一化）
3. **邻居集**：所有节点，即完全图

与一般 MPNN 的关键差异：
- **邻居集是全局的**：不受图拓扑限制，每个节点可以"看到"所有其他节点
- **注意力权重是数据依赖的**：权重通过 query-key 兼容性动态计算（cf. GAT 使用拼接+LeakyReLU）
- **归一化方式**：softmax（全局归一化），而非 GCN 的度归一化 $\frac{1}{\sqrt{d_v d_u}}$

### 3.4 Kool et al. 的图注意力视角 **[Kool et al. 2019, §3, Appendix A]**

Kool et al. 明确指出他们的 Attention Model 可以视为 Graph Attention Network：

> "the model can be considered a Graph Attention Network and take graph structure into account by a masking procedure"

在 TSP 等全连接问题上，编码器的 self-attention 在完全图上操作。对于一般图，通过将非邻接节点的兼容性设为 $-\infty$ 来限制消息传递 **[Kool et al. 2019, Appendix A, Eq.(A.2)]**：

$$u_{ij} = \begin{cases} \frac{\mathbf{q}_i^\top \mathbf{k}_j}{\sqrt{d_k}} & \text{if } i \text{ adjacent to } j \\ -\infty & \text{otherwise} \end{cases}$$

这使得 softmax 后的注意力权重对非邻接节点为 0，从而恢复稀疏图上的消息传递。

### 3.5 对比表

| 特征 | GCN | GAT | Transformer Self-Attn |
|---|---|---|---|
| 图结构 | 给定稀疏图 | 给定稀疏图 | 完全图 |
| 权重计算 | 固定: $\frac{1}{\sqrt{d_v d_u}}$ | 可学习: $\mathrm{LeakyReLU}(a^\top[Wh_i \| Wh_j])$ | 可学习: $\frac{(h_i W^Q)(h_j W^K)^\top}{\sqrt{d_k}}$ |
| 多头 | 无（原始版本） | $\|_{k=1}^K$ 拼接 | $\mathrm{Concat}(\mathrm{head}_1, \ldots) W^O$ |
| 复杂度 | $O(\|E\| \cdot d)$ | $O(\|E\| \cdot d)$ | $O(n^2 \cdot d)$ |
| 感受野 | $L$-hop（$L$ 层后） | $L$-hop | 全局（1层即可） |

---

## Part 4: Positional Encoding

### 4.1 必要性 **[Vaswani et al. 2017, §3.5]**

Self-attention 本身是置换等变的（permutation equivariant），即输出不依赖于输入的顺序。对于需要位置信息的序列任务（如语言），必须注入位置信息。

**注意**: 对于图任务（如 CO 问题），通常**不使用**位置编码，因为图天然无序。Kool et al. 明确不使用位置编码以保持节点嵌入的置换不变性 **[Kool et al. 2019, §3.1]**。

### 4.2 Sinusoidal Positional Encoding **[Vaswani et al. 2017, §3.5]**

$$\boxed{PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{\mathrm{model}}}}\right), \quad PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{\mathrm{model}}}}\right)}$$

其中 $pos$ 是位置索引，$i$ 是维度索引。

**性质**:

1. **波长几何级数**：不同维度对应的正弦波波长从 $2\pi$ 到 $10000 \cdot 2\pi$，形成几何级数
2. **相对位置的线性表示**：对于固定偏移 $k$，$PE_{pos+k}$ 可以表示为 $PE_{pos}$ 的线性函数

**证明**（线性性质）：

设 $\omega_i = 1/10000^{2i/d_{\mathrm{model}}}$。对于偶数维度：

$$\sin(\omega_i(pos+k)) = \sin(\omega_i \cdot pos)\cos(\omega_i k) + \cos(\omega_i \cdot pos)\sin(\omega_i k)$$

这是 $PE_{(pos, 2i)}$ 和 $PE_{(pos, 2i+1)}$ 的线性组合（系数 $\cos(\omega_i k)$ 和 $\sin(\omega_i k)$ 是仅依赖于偏移 $k$ 的常数）。即存在矩阵 $M_k$（仅依赖 $k$）使得：

$$PE_{pos+k} = M_k \cdot PE_{pos}$$

这使得模型可以容易地学习基于相对位置的注意力模式。

### 4.3 Learned Positional Embeddings

替代方案：为每个位置学习一个 $d_{\mathrm{model}}$ 维的嵌入向量。

Vaswani et al. 发现两种方法效果几乎相同 **[Vaswani et al. 2017, Table 3, row (E)]**，但选择 sinusoidal 版本是因为其可能泛化到训练时未见过的更长序列。

---

## Part 5: Transformer Encoder-Decoder Architecture

### 5.1 Encoder **[Vaswani et al. 2017, §3.1]**

编码器由 $N = 6$ 个相同的层堆叠而成。每层包含两个子层：

$$\hat{H}^{(l)} = \mathrm{LayerNorm}\left(H^{(l-1)} + \mathrm{MHA}(H^{(l-1)}, H^{(l-1)}, H^{(l-1)})\right)$$

$$H^{(l)} = \mathrm{LayerNorm}\left(\hat{H}^{(l)} + \mathrm{FFN}(\hat{H}^{(l)})\right)$$

其中 FFN 是逐位置前馈网络：

$$\mathrm{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2$$

参数设置：$d_{\mathrm{model}} = 512$，$d_{\mathrm{ff}} = 2048$（FFN 的隐藏维度）。

**Kool et al. 的变体** **[Kool et al. 2019, §3.1]**：使用 Batch Normalization 代替 Layer Normalization，发现效果更好。

### 5.2 Decoder **[Vaswani et al. 2017, §3.1]**

解码器也由 $N = 6$ 个相同的层堆叠。每层包含三个子层：

1. **Masked self-attention**：防止位置 attend 到后续位置（通过将 softmax 输入中的对应位置设为 $-\infty$），保证自回归性质
2. **Encoder-decoder attention**：queries 来自解码器上一层，keys 和 values 来自编码器输出
3. **FFN**：与编码器相同

$$\text{Masked-MHA}: \quad u_{ij} = \begin{cases} \frac{q_i^\top k_j}{\sqrt{d_k}} & j \leq i \\ -\infty & j > i \end{cases}$$

### 5.3 Attention 的三种用途 **[Vaswani et al. 2017, §3.2.3]**

| 用途 | Q 来源 | K, V 来源 | 描述 |
|---|---|---|---|
| Encoder self-attention | 编码器上一层 | 编码器上一层 | 全连接，每个位置看到所有位置 |
| Decoder self-attention | 解码器上一层 | 解码器上一层 | 因果掩码，只能看到已生成的位置 |
| Encoder-decoder attention | 解码器上一层 | 编码器输出 | 解码器查询编码器的完整表示 |

### 5.4 Input Embedding **[Vaswani et al. 2017, §3.4]**

输入 token 通过学习到的嵌入矩阵转换为 $d_{\mathrm{model}}$ 维向量。嵌入权重乘以 $\sqrt{d_{\mathrm{model}}}$：

$$\text{Input}_i = \sqrt{d_{\mathrm{model}}} \cdot \mathrm{Embedding}(x_i) + PE_i$$

乘以 $\sqrt{d_{\mathrm{model}}}$ 是为了使嵌入的量级与位置编码匹配。

---

## Part 6: Computational Complexity

### 6.1 Self-Attention 复杂度 **[Vaswani et al. 2017, §4, Table 1]**

| 层类型 | 每层复杂度 | 顺序操作数 | 最大路径长度 |
|---|---|---|---|
| Self-Attention | $O(n^2 \cdot d)$ | $O(1)$ | $O(1)$ |
| Recurrent | $O(n \cdot d^2)$ | $O(n)$ | $O(n)$ |
| Convolutional | $O(k \cdot n \cdot d^2)$ | $O(1)$ | $O(\log_k n)$ |
| Restricted Self-Attn | $O(r \cdot n \cdot d)$ | $O(1)$ | $O(n/r)$ |

### 6.2 复杂度分析

Self-attention 的计算分解：

1. **Query-Key 矩阵乘法**: $QK^\top \in \mathbb{R}^{n \times n}$，复杂度 $O(n^2 d_k)$
2. **Softmax**: $O(n^2)$
3. **注意力加权求和**: $\mathrm{softmax}(\cdot) V$，复杂度 $O(n^2 d_v)$

总复杂度: $O(n^2 d)$，其中 $d = d_k = d_v$。

**关键权衡** **[Vaswani et al. 2017, §4]**：
- 当 $n < d$ 时（大多数 NLP 场景），self-attention 比 RNN 快
- 当 $n > d$ 时，self-attention 变慢，可用 restricted attention（窗口大小 $r$）缓解
- Self-attention 的最大路径长度为 $O(1)$（直接连接任意两个位置），优于 RNN 的 $O(n)$

### 6.3 FFN 的复杂度

$$\mathrm{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2$$

复杂度: $O(n \cdot d \cdot d_{\mathrm{ff}}) = O(n \cdot d^2)$（当 $d_{\mathrm{ff}} = 4d$）

**FFN 作为参数注意力** **[Vaswani et al. 2017, Appendix]**：FFN 可视为一种注意力，其中 keys 和 values 是可训练的参数矩阵行，兼容性函数使用 ReLU 而非 softmax。

---

## Part 7: Connection to GNN — Transformer = GNN on Complete Graph

### 7.1 统一视角

将 Transformer 和各类 GNN 统一为消息传递框架的特例：

$$h_v^{(l+1)} = U\left(h_v^{(l)}, \bigoplus_{u \in \mathcal{N}(v)} M(h_v^{(l)}, h_u^{(l)})\right)$$

| 方法 | 图结构 | 消息函数 $M$ | 聚合 $\bigoplus$ | 更新 $U$ |
|---|---|---|---|---|
| GCN | 稀疏图 $G$ | $\frac{1}{\sqrt{d_v d_u}} Wh_u$ | $\sum$ | $\sigma(\cdot)$ |
| GAT | 稀疏图 $G$ | $\alpha_{vu}^{\mathrm{GAT}} Wh_u$ | $\sum$ | $\sigma(\cdot)$ |
| Transformer | 完全图 $K_n$ | $\alpha_{vu}^{\mathrm{attn}} h_u W^V$ | $\sum$ | LN(residual + FFN) |

### 7.2 关键推论

**推论 1**（全局感受野）：单层 Transformer self-attention 的感受野覆盖所有节点，等价于 GNN 在直径为 1 的完全图上传播。$L$ 层 Transformer 可以建模 $L$ 阶交互。

**推论 2**（表达力）：Transformer（在完全图上）不受 1-WL test 上界的限制（因为完全图是正则图，但位置编码或不同输入特征打破了对称性），可以表达超越标准 MPNN 的图函数。

**推论 3**（Over-smoothing 的缓解）：完全图上的消息传递会更快趋向 over-smoothing，但 Transformer 通过以下机制缓解：
- 残差连接
- 层归一化
- 多头注意力（不同头学习不同的注意力模式）
- FFN（非线性逐位置处理）

### 7.3 Graph Transformer 范式

将 Transformer 思想引入图学习：

1. **在稀疏图上使用 Transformer**：通过掩码限制注意力到邻居（如 Kool et al.）
2. **在全图上使用 Transformer + 位置/结构编码**：使用 Laplacian eigenvectors 或 random walk 编码注入图结构信息
3. **混合架构**：GNN 层（局部消息传递）+ Transformer 层（全局注意力）交替使用

---

## Summary

### 核心公式速查

| 公式 | 表达式 | 来源 |
|---|---|---|
| Scaled Dot-Product Attention | $\mathrm{softmax}(QK^\top / \sqrt{d_k})V$ | **[Vaswani et al. 2017, §3.2.1]** |
| 缩放因子推导 | $\mathrm{Var}(q \cdot k) = d_k \implies$ 除以 $\sqrt{d_k}$ | **[Vaswani et al. 2017, §3.2.1]** |
| Multi-Head Attention | $\mathrm{Concat}(\mathrm{head}_1, \ldots, \mathrm{head}_h)W^O$ | **[Vaswani et al. 2017, §3.2.2]** |
| Sinusoidal PE | $\sin(pos/10000^{2i/d})$, $\cos(pos/10000^{2i/d})$ | **[Vaswani et al. 2017, §3.5]** |
| FFN | $\max(0, xW_1 + b_1)W_2 + b_2$ | **[Vaswani et al. 2017, §3.3]** |
| Self-Attn 复杂度 | $O(n^2 d)$，路径长度 $O(1)$ | **[Vaswani et al. 2017, §4]** |

### 核心联系

$$\text{Transformer Self-Attention} = \text{GNN on Complete Graph} + \text{Positional Encoding}$$

$$\text{AM Encoder (Kool et al.)} = \text{Transformer Encoder} - \text{Positional Encoding}$$

---

## References

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L., & Polosukhin, I. (2017). Attention Is All You Need. NeurIPS.
2. Kool, W., van Hoof, H., & Welling, M. (2019). Attention, Learn to Solve Routing Problems! ICLR.
3. Velickovic, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., & Bengio, Y. (2018). Graph Attention Networks. ICLR.
4. Gilmer, J., Schoenholz, S.S., Riley, P.F., Vinyals, O., & Dahl, G.E. (2017). Neural Message Passing for Quantum Chemistry. ICML.
5. Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural Machine Translation by Jointly Learning to Align and Translate. ICLR.
