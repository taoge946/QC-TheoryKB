# SVD and Polar Decomposition (奇异值分解与极分解)

## Metadata
- **Topic**: Linear Algebra
- **Tags**: `svd`, `polar-decomposition`, `singular-values`
- **Prerequisites**: eigenvalues, Hermitian matrices, spectral theorem
- **Related Formulas**: F1.2, F1.10, F1.13
- **References**: Horn & Johnson Chapter 7; Nielsen & Chuang Theorem 2.3; **[Watrous, Ch.1, §1.1.3]**; **[Slofstra, Ch.11]**

---

## Statement (定理陈述)

**Singular Value Decomposition (SVD)** **[Watrous, Ch.1, Thm.1.1]** **[Slofstra, Ch.11, Thm.11.4]**: 任意矩阵 $A \in \mathbb{C}^{m \times n}$ 都可以分解为：

$$A = U \Sigma V^\dagger$$

其中 $U \in \mathbb{C}^{m \times m}$ 和 $V \in \mathbb{C}^{n \times n}$ 是酉矩阵，$\Sigma \in \mathbb{R}^{m \times n}$ 是对角矩阵，对角元素 $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$（$r = \mathrm{rank}(A)$）称为奇异值。

**Polar Decomposition (极分解)** **[Watrous, Ch.1, Thm.1.2]**: 任意方阵 $A \in \mathbb{C}^{n \times n}$ 都可以分解为：

$$A = U|A| \qquad (\text{left polar decomposition})$$

$$A = |A'|U \qquad (\text{right polar decomposition})$$

其中 $U$ 为酉矩阵，$|A| = \sqrt{A^\dagger A} \geq 0$，$|A'| = \sqrt{AA^\dagger} \geq 0$。

---

## Derivation (完整推导)

### Step 1: $A^\dagger A$ 的性质

**引理**: 对任意矩阵 $A$，$A^\dagger A$ 是半正定 Hermitian 矩阵。

*证明 (Hermitian 性)*: $(A^\dagger A)^\dagger = A^\dagger (A^\dagger)^\dagger = A^\dagger A$ $\checkmark$

*证明 (半正定性)*: 对任意 $|v\rangle$：

$$\langle v|A^\dagger A|v\rangle = \langle Av|Av\rangle = \|A|v\rangle\|^2 \geq 0 \quad \square$$

由谱定理，$A^\dagger A$ 可以对角化：

$$A^\dagger A = \sum_{i=1}^{n} \mu_i |v_i\rangle\langle v_i|$$

其中 $\mu_i \geq 0$，$\{|v_i\rangle\}$ 是正交归一基。

**定义**: 奇异值 $\sigma_i = \sqrt{\mu_i}$，即 $A^\dagger A$ 的特征值的非负平方根。

按降序排列：$\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0 = \sigma_{r+1} = \cdots = \sigma_n$，其中 $r = \mathrm{rank}(A)$。

### Step 2: 构造 SVD

**Step 2a: 构造右酉矩阵 $V$**

取 $V = [|v_1\rangle, |v_2\rangle, \ldots, |v_n\rangle]$，即 $A^\dagger A$ 的特征向量按列排列。

**Step 2b: 构造左酉矩阵 $U$**

对 $i = 1, 2, \ldots, r$（非零奇异值），定义：

$$|u_i\rangle = \frac{1}{\sigma_i} A|v_i\rangle$$

**验证 $\{|u_i\rangle\}_{i=1}^r$ 正交归一**:

$$\langle u_i|u_j\rangle = \frac{1}{\sigma_i \sigma_j} \langle v_i|A^\dagger A|v_j\rangle = \frac{1}{\sigma_i \sigma_j} \langle v_i|\sigma_j^2|v_j\rangle = \frac{\sigma_j}{\sigma_i} \langle v_i|v_j\rangle = \frac{\sigma_j}{\sigma_i} \delta_{ij} = \delta_{ij} \quad \checkmark$$

将 $\{|u_i\rangle\}_{i=1}^r$ 扩展为 $\mathbb{C}^m$ 的正交归一基 $\{|u_1\rangle, \ldots, |u_m\rangle\}$（补充 $m-r$ 个正交向量）。

令 $U = [|u_1\rangle, |u_2\rangle, \ldots, |u_m\rangle]$。

**Step 2c: 验证 $A = U\Sigma V^\dagger$**

由构造，$A|v_i\rangle = \sigma_i |u_i\rangle$ 对 $i = 1, \ldots, r$。

对 $i = r+1, \ldots, n$，$\sigma_i = 0$，且 $A|v_i\rangle = 0$（因为 $\|A|v_i\rangle\|^2 = \langle v_i|A^\dagger A|v_i\rangle = \mu_i = 0$）。

因此 $A|v_i\rangle = \sigma_i|u_i\rangle$ 对所有 $i = 1, \ldots, n$ 成立（约定 $\sigma_i = 0$ 时右边为零向量）。

写成矩阵形式：

$$AV = U\Sigma$$

$$A = U\Sigma V^\dagger \quad \square$$

### Step 3: 奇异值的唯一性

**命题**: 矩阵 $A$ 的奇异值是唯一的（不依赖于分解的选择）。

*证明*: 奇异值定义为 $A^\dagger A$ 的特征值的非负平方根。由于 $A^\dagger A$ 是 Hermitian 的，其特征值是唯一确定的（可能有不同的特征向量选择，但特征值集合唯一）。$\square$

注意：$U$ 和 $V$ 一般不唯一，特别是当有奇异值简并或零奇异值时。

### Step 4: SVD 的紧凑形式

当 $r = \mathrm{rank}(A) < \min(m,n)$ 时，可以写紧凑 (compact/thin) SVD：

$$A = U_r \Sigma_r V_r^\dagger = \sum_{i=1}^{r} \sigma_i |u_i\rangle\langle v_i|$$

其中 $U_r = [|u_1\rangle, \ldots, |u_r\rangle] \in \mathbb{C}^{m \times r}$，$\Sigma_r = \mathrm{diag}(\sigma_1, \ldots, \sigma_r) \in \mathbb{R}^{r \times r}$，$V_r = [|v_1\rangle, \ldots, |v_r\rangle] \in \mathbb{C}^{n \times r}$。

这个形式清楚地展示了 $A$ 作为 $r$ 个秩-1 矩阵 $\sigma_i |u_i\rangle\langle v_i|$ 之和的结构。

### Step 5: 从 SVD 推导极分解

**Left Polar Decomposition**: $A = U_{\text{polar}}|A|$

由 SVD $A = U\Sigma V^\dagger$，令：

$$U_{\text{polar}} = UV^\dagger, \qquad |A| = V\Sigma V^\dagger$$

**验证 $|A| = \sqrt{A^\dagger A}$**:

$$A^\dagger A = (U\Sigma V^\dagger)^\dagger (U\Sigma V^\dagger) = V\Sigma^\dagger U^\dagger U \Sigma V^\dagger = V\Sigma^2 V^\dagger$$

因此 $\sqrt{A^\dagger A} = V|\Sigma|V^\dagger = V\Sigma V^\dagger = |A|$（因为奇异值非负，$|\Sigma| = \Sigma$）。$\checkmark$

**验证乘积**:

$$U_{\text{polar}} \cdot |A| = UV^\dagger \cdot V\Sigma V^\dagger = U\Sigma V^\dagger = A \quad \checkmark$$

**验证 $U_{\text{polar}}$ 酉性**: $U_{\text{polar}}^\dagger U_{\text{polar}} = (UV^\dagger)^\dagger(UV^\dagger) = VU^\dagger UV^\dagger = VV^\dagger = I$ $\checkmark$

**Right Polar Decomposition**: 类似地，$A = |A'|U_{\text{polar}}$，其中 $|A'| = \sqrt{AA^\dagger} = U\Sigma U^\dagger$。

### Step 6: 极分解的唯一性

**命题**: 若 $A$ 可逆，则极分解 $A = U|A|$ 中 $U$ 和 $|A|$ 唯一确定。

*证明*: $|A| = \sqrt{A^\dagger A}$ 由 $A$ 唯一确定（半正定矩阵的平方根唯一）。$A$ 可逆则 $|A|$ 可逆，故 $U = A|A|^{-1}$ 唯一。$\square$

若 $A$ 不可逆，$|A|$ 仍唯一，但 $U$ 不唯一（$\ker(A)$ 上的自由度）。此时 $U$ 可取为部分等距 (partial isometry)。

### Step 7: 几何解释

SVD 的几何意义：任意线性变换 $A: \mathbb{C}^n \to \mathbb{C}^m$ 可以分解为三步：

1. **$V^\dagger$**: 在输入空间中旋转（选择"最佳"方向）
2. **$\Sigma$**: 沿坐标轴缩放（奇异值决定缩放因子）
3. **$U$**: 在输出空间中旋转（对齐输出方向）

极分解的几何意义：$A = U|A|$ 将线性变换分为：
1. **$|A|$**: 纯"拉伸"（半正定，类似复数的模 $|z|$）
2. **$U$**: 纯"旋转"（酉，类似复数的相位 $e^{i\theta}$）

这与复数的极坐标表示 $z = e^{i\theta}|z|$ 完全类比。

---

## Applications in Quantum Computing (量子计算中的应用)

### 1. 保真度 (Fidelity) 计算

两个量子态 $\rho$ 和 $\sigma$ 的保真度定义为：

$$F(\rho, \sigma) = \left(\mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}\right)^2$$

计算中涉及半正定矩阵的平方根，直接与 SVD/极分解相关。

对纯态 $|\psi\rangle$ 和混合态 $\sigma$：$F(|\psi\rangle\langle\psi|, \sigma) = \langle\psi|\sigma|\psi\rangle$。

### 2. Uhlmann's Theorem (Uhlmann 定理)

**定理**: 设 $\rho, \sigma$ 是密度矩阵，$|\psi_\rho\rangle, |\psi_\sigma\rangle$ 分别是它们的纯化 (purifications)，则：

$$F(\rho, \sigma) = \max_{|\psi_\sigma\rangle} |\langle\psi_\rho|\psi_\sigma\rangle|^2$$

最大值在 $|\psi_\sigma\rangle = (U \otimes I)|\psi_\sigma^0\rangle$ 处取得，其中 $U$ 来自 $\sqrt{\rho}\sqrt{\sigma}$ 的极分解。

*推导关键步骤*:

设 $\rho = \sum_i p_i|i\rangle\langle i|$，纯化为 $|\psi_\rho\rangle = \sum_i \sqrt{p_i}|i\rangle|i\rangle$。

类似地，$|\psi_\sigma\rangle = (I \otimes U_\sigma)\sum_j \sqrt{q_j}|j\rangle|j\rangle$。

内积 $\langle\psi_\rho|\psi_\sigma\rangle = \mathrm{Tr}(\sqrt{\rho}\, U_\sigma \sqrt{\sigma})$（经过计算）。

最大化 $|\mathrm{Tr}(\sqrt{\rho}\, U_\sigma \sqrt{\sigma})|$ 关于酉矩阵 $U_\sigma$。

设 $\sqrt{\rho}\sqrt{\sigma} = W|{\sqrt{\rho}\sqrt{\sigma}}|$ 是极分解，取 $U_\sigma = W^\dagger$ 即可达到最大值：

$$\max_{U_\sigma} |\mathrm{Tr}(\sqrt{\rho}\,U_\sigma\sqrt{\sigma})| = \mathrm{Tr}|\sqrt{\rho}\sqrt{\sigma}| = \mathrm{Tr}\sqrt{\sqrt{\rho}\,\sigma\,\sqrt{\rho}}$$

最后一步用到 $|X| = \sqrt{X^\dagger X}$ 的性质和 $\mathrm{Tr}|X| = \mathrm{Tr}\sqrt{X^\dagger X}$。

### 3. 迹距离 (Trace Distance)

$$D(\rho, \sigma) = \frac{1}{2}\|\rho - \sigma\|_1 = \frac{1}{2}\mathrm{Tr}|\rho - \sigma| = \frac{1}{2}\sum_i |\lambda_i(\rho - \sigma)|$$

其中 $|\rho - \sigma| = \sqrt{(\rho-\sigma)^\dagger(\rho-\sigma)}$ 通过极分解/SVD 计算。

由于 $\rho - \sigma$ 是 Hermitian 的，$|\rho - \sigma|$ 的特征值就是 $\rho - \sigma$ 的特征值的绝对值。

**迹距离与保真度的关系 (Fuchs-van de Graaf 不等式)**:

$$1 - \sqrt{F(\rho, \sigma)} \leq D(\rho, \sigma) \leq \sqrt{1 - F(\rho, \sigma)}$$

### 4. 算符范数的 SVD 表示

所有常见矩阵范数都可以用奇异值表示：

| 范数 | SVD 表示 | 意义 |
|------|----------|------|
| 算符范数 $\\|A\\|_\infty$ | $\sigma_1 = \sigma_{\max}$ | 最大拉伸因子 |
| 迹范数 $\\|A\\|_1$ | $\sum_i \sigma_i$ | Schatten 1-范数 |
| Frobenius 范数 $\\|A\\|_F$ | $\sqrt{\sum_i \sigma_i^2}$ | Schatten 2-范数 |
| Schatten $p$-范数 | $(\sum_i \sigma_i^p)^{1/p}$ | 一般化 |

### 5. 低秩近似

**Eckart-Young-Mirsky 定理**: SVD 给出最佳低秩近似。在 Frobenius 范数下，$A$ 的最佳秩 $k$ 近似为：

$$A_k = \sum_{i=1}^{k} \sigma_i |u_i\rangle\langle v_i|, \qquad \|A - A_k\|_F = \sqrt{\sum_{i=k+1}^{r} \sigma_i^2}$$

在量子计算中，这用于矩阵乘积态 (MPS) 的截断和张量网络的压缩。

### 6. 量子信道的 Stinespring 表示

量子信道 $\mathcal{E}(\rho) = \sum_k E_k \rho E_k^\dagger$ 的 Kraus 算符 $\{E_k\}$ 与 Choi 矩阵的 SVD 密切相关。Choi 矩阵 $J(\mathcal{E})$ 的 SVD 提供了最小的 Kraus 分解。

---

## Summary (总结)

1. SVD 存在性证明的核心：$A^\dagger A$ 半正定 $\to$ 正交归一特征基 $\to$ 构造 $U, \Sigma, V$
2. 奇异值唯一，但 $U, V$ 一般不唯一
3. 极分解 $A = U|A|$ 直接从 SVD 得到：$U = UV^\dagger$，$|A| = V\Sigma V^\dagger$
4. 几何意义：旋转-缩放-旋转（SVD）或 缩放-旋转（极分解）
5. 量子计算核心应用：保真度、Uhlmann 定理、迹距离、矩阵范数

---

## From Linear Algebra References

### SVD in Quantum Channel Theory **[Slofstra, §8; LinAlg for QC, §7]**

**Choi 矩阵的 SVD 给出最小 Kraus 分解**：

设 $J(\mathcal{E}) \in \mathcal{L}(\mathcal{H}_B \otimes \mathcal{H}_A)$ 是量子信道的 Choi 矩阵，其谱分解为 $J = \sum_{i=1}^r \lambda_i |v_i\rangle\langle v_i|$，其中 $r = \text{rank}(J)$。

则 $K_i = \sqrt{\lambda_i}\,\text{unvec}(|v_i\rangle)$ 给出 $\mathcal{E}$ 的最小 Kraus 分解（Kraus 算子数等于 Choi 秩 $r$）。

**信道的 Stinespring rank**：$r = \text{rank}(J(\mathcal{E}))$ 是最小的 Kraus 算子数，也称为 Choi rank。

### Matrix Majorization and Quantum Entanglement **[Slofstra, §9]**

**定义**：$\mathbf{x} \prec \mathbf{y}$（$\mathbf{x}$ 被 $\mathbf{y}$ majorize）当且仅当对所有 $k = 1, \ldots, n$：

$$\sum_{i=1}^k x_i^{\downarrow} \leq \sum_{i=1}^k y_i^{\downarrow}$$

且 $\sum x_i = \sum y_i$，其中 $\downarrow$ 表示降序排列。

**Nielsen 定理**：纯态 $|\psi\rangle$ 可以通过 LOCC（局域操作 + 经典通信）转化为 $|\phi\rangle$ 当且仅当：

$$\lambda(\rho_A^{\psi}) \prec \lambda(\rho_A^{\phi})$$

其中 $\lambda(\cdot)$ 表示特征值向量（即 Schmidt 系数的平方）。

### Partial Isometries and Quantum Error Correction **[LinAlg for QC, §8]**

**定义**：$V$ 是 partial isometry 当且仅当 $V^\dagger V$ 是投影算子。

在量子纠错中，编码映射 $V_{\text{enc}}: \mathcal{H}_{\text{logical}} \to \mathcal{H}_{\text{physical}}$ 是一个等距映射（isometry），满足 $V_{\text{enc}}^\dagger V_{\text{enc}} = I_{\text{logical}}$。

SVD 提供了编码映射的标准构造：给定码空间的正交归一基 $\{|\bar{i}\rangle\}$ 和逻辑基 $\{|i\rangle\}$，编码映射为 $V = \sum_i |\bar{i}\rangle\langle i|$。

---

## References

- **[LinAlg for QC]** — Linear algebra for QC: SVD in channel theory, partial isometries, encoding maps.
- **[Slofstra]** — Slofstra: majorization, Nielsen's theorem, Choi rank.
- Horn & Johnson Chapter 7; Nielsen & Chuang Theorem 2.3; Watrous Chapter 1.
