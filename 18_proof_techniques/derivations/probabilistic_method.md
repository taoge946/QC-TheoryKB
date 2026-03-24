# The Probabilistic Method

> 概率方法：通过证明随机对象"以正概率满足性质"来证明存在性。
> 核心参考：Alon & Spencer, "The Probabilistic Method" (4th ed.)
> 在编码理论（随机码存在性）和组合优化中广泛使用。

---

## 1. First Moment Method (一阶矩方法/期望论证)

### 1.1 Basic Principle

**Theorem**: 若 $X$ 是非负整值随机变量，$\mathbb{E}[X] > 0$，则 $P(X > 0) > 0$。

等价地：若 $\mathbb{E}[X] < 1$，则 $P(X = 0) > 0$。

**Proof**: $\mathbb{E}[X] = \sum_{k \geq 0} k \cdot P(X=k) \leq \sum_{k \geq 1} k \cdot P(X = k)$。若 $P(X > 0) = 0$，则 $\mathbb{E}[X] = 0$，矛盾。$\square$

> 一行解释：期望大于零 → 至少存在一个正值的实现；期望小于 1 → 至少存在一个零值的实现。

### 1.2 Deletion/Alteration Method (删除法)

**Strategy**:
1. 从随机对象开始
2. 计算"坏性质"的期望数量 $\mu$
3. 通过删除/修改消除坏性质，代价至多 $\mu$
4. 得到一个满足所有要求的确定性对象

### 1.3 Application: Ramsey Number Lower Bound

**Theorem** [Erdős, 1947]: $R(k, k) \geq 2^{k/2}$。

**Proof**: 对 $K_n$（$n$ 阶完全图）随机 2-着色，每条边独立等概率红/蓝。

$X = $ 单色 $k$-团的数量。$\mathbb{E}[X] = \binom{n}{k} \cdot 2 \cdot 2^{-\binom{k}{2}}$。

当 $n = 2^{k/2}$ 时：

$$\mathbb{E}[X] = \binom{2^{k/2}}{k} \cdot 2^{1-\binom{k}{2}} < \frac{2^{k^2/4}}{k!} \cdot 2^{1-k(k-1)/2} < 1$$

因此 $P(X = 0) > 0$，即存在无单色 $k$-团的 2-着色。$\square$

**When to use**: 证明某种"好"对象存在——通常无法构造，但可以证明随机构造以正概率成功。

---

## 2. Second Moment Method [F18.17]

### 2.1 Paley-Zygmund Inequality

**Theorem**: 若 $X \geq 0$，$\mathbb{E}[X^2] < \infty$，则：

$$P(X > 0) \geq \frac{(\mathbb{E}[X])^2}{\mathbb{E}[X^2]}$$

更一般地，对 $0 < \theta < 1$：

$$P(X \geq \theta \mathbb{E}[X]) \geq (1-\theta)^2 \cdot \frac{(\mathbb{E}[X])^2}{\mathbb{E}[X^2]}$$

**Proof**:

$$\mathbb{E}[X] = \mathbb{E}[X \cdot \mathbf{1}_{X > 0}] \leq \sqrt{\mathbb{E}[X^2]} \cdot \sqrt{P(X > 0)}$$

（Cauchy-Schwarz）。平方并整理得 $P(X > 0) \geq (\mathbb{E}[X])^2 / \mathbb{E}[X^2]$。$\square$

### 2.2 When First Moment Fails, Second Moment Saves

**Typical scenario**: 你想证明 $P(X > 0) \to 1$（而非仅 $> 0$）。

- First moment: $\mathbb{E}[X] \to \infty$ 只能说 $P(X > 0) > 0$（不能排除 $P(X > 0) \to 0$）
- Second moment: 如果 $\mathbb{E}[X^2] / (\mathbb{E}[X])^2 \to 1$（即 $\mathrm{Var}(X) = o((\mathbb{E}[X])^2)$），则 $P(X > 0) \to 1$

> 一行解释：方差足够小 → 随机变量集中在均值附近 → 以高概率为正。

### 2.3 Application: Random Graph Threshold

**Theorem**: 在 $G(n, p)$ 随机图中，当 $p = c/n$（$c > 1$）时，以高概率存在巨连通分量。

**Proof sketch (second moment on component size)**:
- $X$ = 大小 $\geq \alpha n$ 的连通分量中的顶点数
- $\mathbb{E}[X] = \Theta(n)$（当 $c > 1$）
- $\mathbb{E}[X^2] = O(n^2)$
- 由二阶矩：$P(X > 0) \geq \Theta(1)$

（完整证明需要更精细的分析。）

**When to use**: 证明随机对象的某性质以常数概率（或高概率）出现；证明阈值现象。

---

## 3. Lovász Local Lemma (LLL) [F18.16]

### 3.1 Symmetric Version

**Theorem** [Erdős & Lovász, 1975]: 设事件 $A_1, \ldots, A_n$ 满足：
1. $P(A_i) \leq p$ for all $i$
2. 每个 $A_i$ 至多与 $d$ 个其他事件相关（dependency graph 的最大度 $\leq d$）

若 $ep(d+1) \leq 1$，则：

$$P\left(\bigcap_{i=1}^n \overline{A_i}\right) > 0$$

**Comparison with union bound**: Union bound 要求 $np < 1$。LLL 只要求 $p \cdot d \lesssim 1$——当 $d \ll n$ 时（稀疏依赖），LLL 远强于 union bound。

### 3.2 Asymmetric (General) Version

**Theorem**: 设有赋值 $x_i \in (0, 1)$ 满足：

$$P(A_i) \leq x_i \prod_{j \in \Gamma(i)} (1 - x_j)$$

其中 $\Gamma(i)$ 是 $A_i$ 在依赖图中的邻居。则：

$$P\left(\bigcap_{i=1}^n \overline{A_i}\right) \geq \prod_{i=1}^n (1 - x_i) > 0$$

### 3.3 Proof of Symmetric LLL

**Proof**: 用一般版本。取 $x_i = 1/(d+1)$ for all $i$。

需验证：$p \leq \frac{1}{d+1}\left(1 - \frac{1}{d+1}\right)^d \geq \frac{1}{d+1} \cdot \frac{1}{e} = \frac{1}{e(d+1)}$。

因此条件 $ep(d+1) \leq 1$ 保证 $p \leq \frac{1}{e(d+1)} \leq x_i \prod_{j \in \Gamma(i)}(1-x_j)$。

由一般版本得 $P(\cap \overline{A_i}) \geq (1 - 1/(d+1))^n > 0$。$\square$

### 3.4 Constructive LLL [Moser & Tardos, 2010]

**Algorithm (Resample)**:
1. 独立采样所有随机变量
2. While 存在发生的坏事件 $A_i$：重采样 $A_i$ 依赖的变量
3. Output 当前赋值

**Theorem**: 在 LLL 条件下，算法期望在 $O(n/(d+1))$ 轮后终止。

> 一行解释：LLL 不仅是存在性证明，还有高效的构造算法。

### 3.5 Application: Hypergraph 2-Coloring

**Problem**: 给定 $n$-uniform 超图 $\mathcal{H}$（每条边 $n$ 个顶点），每条边最多与 $\Delta$ 条其他边相交。求 2-着色使每条边都不单色。

**Setup**: 每个坏事件 $A_e$ = 边 $e$ 单色。$P(A_e) = 2 \cdot 2^{-n} = 2^{1-n}$。依赖度 $d \leq \Delta \cdot n$。

**By LLL**: 若 $e \cdot 2^{1-n} \cdot (\Delta n + 1) \leq 1$，即 $\Delta \leq 2^{n-1}/(en) - 1/n$，则好着色存在。

---

## 4. Alteration Method (修改法)

### 4.1 Strategy

1. 随机构造一个对象
2. 计算"缺陷"（不满足条件的部分）的期望
3. 用确定性方法修复所有缺陷
4. 修复代价 ≤ 缺陷期望

### 4.2 Application: Independent Set

**Theorem** [Turán]: 任何 $n$ 顶点、$m$ 边的图 $G$ 有独立集大小 $\geq n^2/(2m+n)$。

**Proof (probabilistic + alteration)**:

**Step 1**: 以概率 $p$ 独立选每个顶点进入集合 $S$。

**Step 2**: $\mathbb{E}[|S|] = np$。$S$ 中的边数期望 $= m p^2$。

**Step 3 (Alteration)**: 对每条 $S$ 内的边，删除一个端点。得到独立集大小 $\geq np - mp^2$。

**Step 4**: 取 $p = n/(2m+n)$，得大小 $\geq n^2/(2(2m+n))$。

（更精细的分析给出 $n^2/(2m+n)$。）$\square$

---

## 5. Applications to Coding Theory (编码理论应用)

### 5.1 Gilbert-Varshamov Bound (经典码)

**Theorem**: 存在 $[n, k]_2$ 线性码，最小距离 $d$，只要：

$$2^{n-k} > \sum_{i=0}^{d-2} \binom{n-1}{i}$$

即码率 $R = k/n \geq 1 - H_2((d-1)/n) + o(1)$（渐近）。

**Proof (First moment/greedy)**:

构造 parity check matrix $H \in \mathbb{F}_2^{(n-k) \times n}$，逐列选取。第 $j$ 列不能落在前 $j-1$ 列生成的"forbidden"集合中（即前 $j-1$ 列的所有 $\leq d-2$ 个列的线性组合）。

Forbidden 集大小 $\leq \sum_{i=0}^{d-2} \binom{j-1}{i} < \sum_{i=0}^{d-2} \binom{n-1}{i}$。

只要 $2^{n-k}$ 大于此数，总能找到合法列。$\square$

### 5.2 Random LDPC Code Threshold (随机 LDPC 码阈值)

**Setup**: 随机 $(d_v, d_c)$-regular LDPC 码。

**Threshold theorem** [Richardson & Urbanke, 2001]: 存在阈值 $p^*$ 使得：
- $p < p^*$: BP 解码以高概率成功
- $p > p^*$: BP 解码以高概率失败

**Key tool**: 密度进化（density evolution）分析 BP 消息分布的演化。收敛性用**压缩映射** [F18.13] 在函数空间上分析。

**Existence of good LDPC codes**: 随机 LDPC 码的 minimum distance 以高概率 $\geq \delta n$（线性距离）。

**Proof**: 用 **first moment method** — 权重为 $w$ 的码字数的期望 $\mathbb{E}[N_w] = \binom{n}{w} \cdot P(\text{random word of weight } w \text{ is a codeword})$。当 $w < \delta n$ 时 $\mathbb{E}[N_w] \to 0$，因此以高概率不存在小权码字。

### 5.3 Quantum Code Existence

**Gilbert-Varshamov for CSS codes**: 存在 $[[n, k, d]]$ CSS 码，只要：

$$\frac{k}{n} \geq 1 - 2H_2(d/n) + o(1)$$

**Proof**: 类似经典情况，但对 $X$ 和 $Z$ stabilizer 分别应用 GV bound，再用 CSS 构造。

**Random stabilizer codes**: 随机 stabilizer 码（Haar 随机 Clifford unitary 生成）以高概率有好的距离参数。第一矩方法 + union bound [F18.20]。

---

## 6. Derandomization (去随机化)

### 6.1 Method of Conditional Expectations

**Strategy**: 将概率论证转化为确定性算法。

1. 概率论证给出 $\mathbb{E}[f(X)] \geq c$
2. 逐步固定 $X_1, X_2, \ldots$，每步选择使条件期望不减少的值
3. 最终 $f(x_1, \ldots, x_n) \geq c$

### 6.2 Application to Derandomize Max-Cut

**Theorem**: 随机割的期望值 $\geq m/2$（$m$ = 边数）。

**Derandomization**: 逐个顶点决定放哪边。对顶点 $v_i$：
- 计算 $\mathbb{E}[C | X_1,\ldots,X_{i-1}, X_i = 0]$
- 计算 $\mathbb{E}[C | X_1,\ldots,X_{i-1}, X_i = 1]$
- 选较大者

结果：确定性算法保证割 $\geq m/2$（与 QAOA 的 0.5 保证相同，但确定性）。

---

## Cross-References (交叉引用)

- **Union bound** → [concentration_inequalities.md] [F18.20]: LLL 与 union bound 的对比
- **Chernoff bound** → [concentration_inequalities.md] [F18.4]: 随机码分析中使用
- **Contraction mapping** → [convergence_methods.md] [F18.13]: BP/density evolution 收敛
- **QEC codes** → [../04_quantum_error_correction/derivations/]: CSS codes, stabilizer codes
- **QAOA** → [../05_variational_quantum/derivations/]: Max-Cut 与 QAOA 比较
- **LDPC codes** → [../04_quantum_error_correction/derivations/]: LDPC decoding
- **Original references**:
  - Alon & Spencer, "The Probabilistic Method", 4th ed., Wiley, 2016
  - Moser & Tardos, "A constructive proof of the general LLL", JACM 2010
  - Richardson & Urbanke, "Modern Coding Theory", Cambridge 2008
