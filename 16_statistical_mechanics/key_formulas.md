# Chapter 16: Statistical Mechanics & Phase Transitions - Key Formulas

> 统计力学与相变核心公式速查表。重点关注与量子纠错阈值理论的联系（Dennis et al. 2002 将 QEC 映射到 random-bond Ising model）。所有公式均使用 LaTeX 记号，解释使用中文。

---

## 经典统计力学基础

### F16.1: Ising Model Hamiltonian（Ising 模型哈密顿量）

$$H = -J \sum_{\langle ij \rangle} s_i s_j - h \sum_i s_i$$

其中 $s_i \in \{+1, -1\}$ 是 Ising 自旋变量，$J$ 是最近邻耦合常数（$J > 0$ 为铁磁，$J < 0$ 为反铁磁），$h$ 是外磁场，$\langle ij \rangle$ 表示对所有最近邻对求和。在 $d$ 维超立方格子上，每个自旋有 $2d$ 个最近邻。

这是统计力学中最重要的格子模型之一。对于 QEC 的应用，我们主要关注 $h = 0$ 且耦合 $J_{ij}$ 可以随机取正负值的情形（random-bond Ising model）。

**Source**: [derivations/ising_model.md] | Ising, Z. Phys. 31, 253 (1925); Onsager, Phys. Rev. 65, 117 (1944)

---

### F16.2: Partition Function（配分函数）

$$Z = \sum_{\{s\}} e^{-\beta H(\{s\})} = \sum_{s_1 = \pm 1} \sum_{s_2 = \pm 1} \cdots \sum_{s_N = \pm 1} e^{-\beta H(s_1, s_2, \ldots, s_N)}$$

其中 $\beta = 1/(k_B T)$ 是逆温度，求和遍历所有 $2^N$ 种自旋构型。配分函数是统计力学的核心对象——所有热力学量（自由能、内能、熵、比热、磁化率等）都可以从 $Z$ 或其导数得到。

**与 QEC 的联系**：Dennis et al. 的映射中，QEC 的最优解码问题等价于计算 random-bond Ising model 的配分函数 [Dennis et al. 2002, Eq. 3.6]。

**Source**: [derivations/ising_model.md] | Boltzmann (1877); Gibbs (1902)

---

### F16.3: Free Energy（自由能）

$$F = -k_B T \ln Z = -\frac{1}{\beta} \ln Z$$

Helmholtz 自由能 $F$ 是温度 $T$ 和体积 $V$ 的函数。在热力学极限（$N \to \infty$）中，自由能密度 $f = F/N$ 的非解析性标志着相变的发生。

**关键热力学关系**：
- 内能：$U = -\partial(\beta F)/\partial \beta = \langle H \rangle$
- 熵：$S = -({\partial F}/{\partial T})_V = \beta(U - F)$
- 比热：$C = -T(\partial^2 F/\partial T^2) = k_B \beta^2 (\langle H^2 \rangle - \langle H \rangle^2)$

**与 QEC 的联系**：quenched free energy $[\beta F]_p = -[\ln Z]_p$ 的奇异性定义了纠错阈值 [Dennis et al. 2002, Eq. 3.12]。

**Source**: [derivations/ising_model.md] | Helmholtz (1882)

---

### F16.4: Boltzmann Distribution（Boltzmann 分布）

$$P(\{s\}) = \frac{e^{-\beta H(\{s\})}}{Z} = \frac{1}{Z} \exp\left(\beta J \sum_{\langle ij \rangle} s_i s_j + \beta h \sum_i s_i\right)$$

这是给定温度 $T$ 下，系统处于构型 $\{s\}$ 的概率。Boltzmann 分布是平衡统计力学的基石。热力学平均值定义为：

$$\langle \mathcal{O} \rangle = \sum_{\{s\}} \mathcal{O}(\{s\}) P(\{s\}) = \frac{1}{Z} \sum_{\{s\}} \mathcal{O}(\{s\}) e^{-\beta H(\{s\})}$$

**Source**: [derivations/ising_model.md] | Boltzmann (1877)

---

### F16.5: Order Parameter — Magnetization（序参量 — 磁化强度）

$$m = \langle s_i \rangle = \frac{1}{N} \sum_i \langle s_i \rangle$$

在铁磁 Ising 模型中，磁化强度 $m$ 是相变的序参量：
- **有序相**（$T < T_c$）：$m \neq 0$，自发对称性破缺
- **无序相**（$T > T_c$）：$m = 0$，高温下无长程序
- **临界点**（$T = T_c$）：$m \to 0$，伴随临界涨落

临界指数 $\beta_{\text{mag}}$（注意不同于逆温度 $\beta$）定义了 $m$ 在 $T_c$ 附近的行为：

$$m \sim |T - T_c|^{\beta_{\text{mag}}}, \quad T \to T_c^-$$

2D Ising: $\beta_{\text{mag}} = 1/8$; 3D Ising: $\beta_{\text{mag}} \approx 0.3265$; Mean field: $\beta_{\text{mag}} = 1/2$。

**Source**: [derivations/ising_model.md] | Onsager (1944); Yang, Phys. Rev. 85, 808 (1952)

---

### F16.6: Critical Temperature of 2D Ising Model（2D Ising 模型临界温度）

$$\sinh(2\beta_c J) = 1 \quad \Longleftrightarrow \quad \frac{k_B T_c}{J} = \frac{2}{\ln(1 + \sqrt{2})} \approx 2.269$$

这是 Kramers-Wannier 对偶性给出的精确结果。Onsager (1944) 给出了 2D Ising 模型自由能的精确解：

$$f = -k_B T \left[\ln 2 + \frac{1}{2\pi^2} \int_0^\pi d\theta_1 \int_0^\pi d\theta_2 \, \ln\left(\cosh^2 2\beta J - \sinh 2\beta J (\cos\theta_1 + \cos\theta_2)\right)\right]$$

Kramers-Wannier 对偶将高温展开映射到低温展开，临界点恰好在自对偶点上。

**与 QEC 的关键联系**：对于 random-bond Ising model，Nishimori 线（F16.10）与对偶线的交点给出 QEC 阈值。

**Source**: [derivations/ising_model.md] | Kramers & Wannier, Phys. Rev. 60, 252 (1941); Onsager, Phys. Rev. 65, 117 (1944)

---

### F16.7: Correlation Length（关联长度）

$$\xi \sim |T - T_c|^{-\nu}$$

关联长度 $\xi$ 描述空间关联函数 $G(r) = \langle s_i s_j \rangle - \langle s_i \rangle \langle s_j \rangle$ 的衰减尺度：

$$G(r) \sim e^{-r/\xi}, \quad r \gg 1 \text{ (远离临界点)}$$

在临界点 $T = T_c$ 上，关联长度发散（$\xi \to \infty$），关联函数变为幂律衰减：

$$G(r) \sim r^{-(d-2+\eta)}, \quad T = T_c$$

其中 $\eta$ 是反常维度指数。

**临界指数 $\nu$ 的值**：2D Ising: $\nu = 1$; 3D Ising: $\nu \approx 0.6300$; Mean field: $\nu = 1/2$。

**与 QEC 的联系**：在 QEC 映射中，$\xi$ 的发散对应于纠错能力的丧失——当关联长度超过系统尺寸时，错误链可以跨越整个系统。

**Source**: [derivations/ising_model.md] | Fisher, Rev. Mod. Phys. 46, 597 (1974)

---

## 渗流理论

### F16.8: Percolation Threshold（渗流阈值）

$$p_c = \begin{cases} 1/2 & \text{(2D square lattice, bond percolation)} \\ 0.592746\ldots & \text{(2D square lattice, site percolation)} \\ 0.2488\ldots & \text{(3D cubic lattice, bond percolation)} \\ 0.3116\ldots & \text{(3D cubic lattice, site percolation)} \end{cases}$$

当占据概率 $p > p_c$ 时，存在spanning infinite cluster（无穷连通簇）；当 $p < p_c$ 时，所有连通簇都是有限的。渗流序参量 $P_\infty(p)$（属于无穷簇的概率）在 $p_c$ 处从零连续增长：

$$P_\infty(p) \sim (p - p_c)^{\beta_{\text{perc}}}, \quad p \to p_c^+$$

2D: $\beta_{\text{perc}} = 5/36$; 3D: $\beta_{\text{perc}} \approx 0.4181$。

渗流的关联长度同样发散：$\xi_{\text{perc}} \sim |p - p_c|^{-\nu_{\text{perc}}}$，其中 2D: $\nu_{\text{perc}} = 4/3$; 3D: $\nu_{\text{perc}} \approx 0.8765$。

**与 QEC 的联系**：表面码在独立 $X/Z$ 噪声下的阈值上界来自 2D bond percolation 的 $p_c = 1/2$（连 MWPM 都不需要），而实际 MWPM 解码器的阈值 $\approx 10.3\%$ 来自更精细的 RBIM 分析。参见 [04_qec/threshold_theorem.md, Step 5]。

**Source**: [derivations/percolation_theory.md] | Broadbent & Hammersley, Proc. Camb. Phil. Soc. 53, 629 (1957); Kesten, Comm. Math. Phys. 74, 41 (1980)

---

## Random-Bond Ising Model 与 QEC 映射

### F16.9: Random-Bond Ising Model Hamiltonian（随机键 Ising 模型）

$$H = -\sum_{\langle ij \rangle} J_{ij} \, s_i s_j, \qquad J_{ij} = \begin{cases} +J & \text{with probability } 1 - p \\ -J & \text{with probability } p \end{cases}$$

其中 $J_{ij}$ 是 quenched（淬火）随机变量：一旦选定，在热力学平均中保持不变。这是 **Dennis et al. 2002 将表面码 QEC 映射到的核心模型**。

**物理含义**：
- $J_{ij} = +J$ 的键是铁磁键（相邻自旋倾向对齐）
- $J_{ij} = -J$ 的键是反铁磁键（相邻自旋倾向反对齐，称为 frustrated bond）
- frustrated bond 的位置对应量子纠错中的错误位置

配分函数中需要对 quenched disorder 取平均：

$$[F]_p = -k_B T \, [\ln Z]_p \neq -k_B T \ln [Z]_p$$

**注意 quenched average $[\ln Z]_p$ 与 annealed average $\ln[Z]_p$ 的区别**——前者才是物理的。

**Source**: [derivations/qec_stat_mech_mapping.md] | Edwards & Anderson, J. Phys. F 5, 965 (1975); Dennis et al. 2002, Eq. 3.6

---

### F16.10: Nishimori Line（西森线）

$$e^{-2\beta J} = \frac{p}{1-p} \quad \Longleftrightarrow \quad \beta J = \frac{1}{2} \ln \frac{1-p}{p}$$

Nishimori 线是 random-bond Ising model 相图中的一条特殊线，定义了逆温度 $\beta$ 与 disorder 参数 $p$ 之间的关系。在这条线上，模型具有增强的对称性（gauge symmetry），使得很多精确结果成立。

**Nishimori 线的关键性质**（$\beta = \beta_N(p)$）：
1. **Internal energy 精确**：$[U]_p = -NJ(1-2p)$
2. **上半平面无相变**：Nishimori 线以上（$\beta > \beta_N$）的有序相与 Nishimori 线以下相同
3. **Gauge symmetry**：quenched average 和 thermal average 之间的精确关系

**对 QEC 的物理意义**：在 Dennis et al. 映射中，Nishimori 条件 $e^{-2\beta J} = p/(1-p)$ 恰好是"解码器使用正确的噪声模型"的条件。换言之，ML（最大似然）解码器的性能由 Nishimori 线上的相变点决定。Nishimori 线上从有序到无序的相变点即为最优纠错阈值 $p_c \approx 10.9\%$。

**Source**: [derivations/qec_stat_mech_mapping.md] | Nishimori, Prog. Theor. Phys. 66, 1169 (1981); Dennis et al. 2002, §3.3

---

### F16.11: $Z_2$ Gauge Theory Partition Function（$Z_2$ 规范理论配分函数）

$$Z[J, \eta] = \sum_{\{\sigma_\ell\}} \exp\left(J \sum_P \eta_P \, u_P\right), \qquad u_P = \prod_{\ell \in P} \sigma_\ell$$

其中 $\sigma_\ell \in \{+1, -1\}$ 是定义在格子边上的 $Z_2$ 规范变量，$u_P$ 是绕面 $P$ 一圈的 Wilson loop（plaquette variable），$\eta_P \in \{+1, -1\}$ 是 quenched disorder。

**这是 Dennis et al. 对 circuit-level noise 的推广**：
- **2D model**（完美 syndrome 测量，$q = 0$）：映射到 2D random-bond Ising model（F16.9）
- **3D model**（含 syndrome 测量错误，$q > 0$）：映射到 3D random-plaquette $Z_2$ gauge theory

3D 模型中：
- $\sigma_\ell$ 住在 3D 格子的边上
- $u_P = \prod_{\ell \in P} \sigma_\ell$ 是面上的 plaquette variable
- 激发的 plaquette（$\eta_P u_P = -1$）形成磁通管（flux tubes）
- 磁通管的端点是磁单极子（monopoles），对应 3D syndrome 缺陷

**相结构**：
- **有序相（confined phase）**：flux tubes 被抑制，错误可纠正
- **无序相（deconfined phase）**：flux tubes 弥散，错误不可纠正
- 阈值由 Nishimori 线上的 confinement-deconfinement 相变决定

**Source**: [derivations/qec_stat_mech_mapping.md] | Dennis et al. 2002, Eq. 3.10-3.11; Wegner, J. Math. Phys. 12, 2259 (1971)

---

### F16.12: QEC Threshold as Phase Transition（QEC 阈值 = 相变）

$$p < p_c \;\Longleftrightarrow\; \text{errors correctable (ordered phase)}$$

Dennis et al. 2002 的核心结果：**表面码的纠错阈值是 random-bond Ising model / $Z_2$ gauge theory 中的热力学相变**。

**完美 syndrome 测量**（$q = 0$，2D 模型）：

$$p_c \approx 10.9\% \quad \text{(2D RBIM on Nishimori line)}$$

数值结果来自 Honecker, Picco & Pujol (2000)；也可以用 hashing bound 给出精确条件：

$$H_2(p_x) + H_2(p_z) = 1$$

对于独立 $X/Z$ 噪声（$p_x = p_z = p$），这给出 $H_2(p) = 1/2$，即 $p_c \approx 11.0\%$。

**含 syndrome 测量错误**（$q > 0$，3D 模型）：

$$p_c(q) < p_c(0) \approx 10.9\%$$

对于 $p = q$（代码容量等于测量容量），$p_c \approx 3.3\%$（3D $Z_2$ gauge theory 的 Nishimori 临界点）。实际 MWPM 解码器的阈值约 $\approx 1\%$（去极化噪声）或 $\approx 10.3\%$（独立 $X/Z$，完美 syndrome）。

**映射字典**：

| 量子纠错 | 统计力学 |
|---------|---------|
| 物理错误 | Frustrated bond ($J_{ij} = -J$) |
| Syndrome 缺陷 | Ising vortex / domain wall 端点 |
| 错误链 | Domain wall |
| 逻辑错误（跨越链） | 跨越系统的 domain wall |
| ML 解码 | 在 Nishimori 线上求自由能最小 |
| MWPM 解码 | 零温能量最小化（$T = 0$ 近似） |
| 纠错阈值 | 有序-无序相变临界点 |
| 测量噪声 | 额外一个空间维度（2D $\to$ 3D） |

**Source**: [derivations/qec_stat_mech_mapping.md] | Dennis et al., J. Math. Phys. 43, 4452 (2002); 交叉参考 [04_qec/threshold_theorem.md, F4.6]

---

## 补充公式

### F16.13: Transfer Matrix Method for 1D Ising（1D Ising 转移矩阵）

$$Z = \text{Tr}(T^N) = \lambda_+^N + \lambda_-^N$$

其中转移矩阵 $T$ 和本征值为：

$$T = \begin{pmatrix} e^{\beta J + \beta h} & e^{-\beta J} \\ e^{-\beta J} & e^{\beta J - \beta h} \end{pmatrix}, \quad \lambda_\pm = e^{\beta J} \cosh(\beta h) \pm \sqrt{e^{2\beta J} \sinh^2(\beta h) + e^{-2\beta J}}$$

对 $h = 0$：$\lambda_+ = 2\cosh(\beta J)$, $\lambda_- = 2\sinh(\beta J)$。在热力学极限 $N \to \infty$：

$$f = -k_B T \ln \lambda_+ = -k_B T \ln[2\cosh(\beta J)]$$

1D Ising 模型在 $T > 0$ 时无相变（$\lambda_+ > \lambda_- > 0$，自由能密度解析），只在 $T = 0$ 时有序。

**Source**: [derivations/ising_model.md] | Kramers & Wannier (1941)

---

### F16.14: Mean Field Theory Critical Temperature（平均场理论临界温度）

$$k_B T_c^{\text{MF}} = z J$$

其中 $z$ 是配位数（最近邻数目）。平均场自洽方程为：

$$m = \tanh(\beta z J m + \beta h)$$

在 $h = 0$ 时，$m = 0$ 在 $T > T_c^{\text{MF}}$ 时是唯一解；在 $T < T_c^{\text{MF}}$ 时出现非零解 $m \neq 0$。平均场给出的临界指数是 $\beta_{\text{mag}} = 1/2$, $\gamma = 1$, $\nu = 1/2$, $\alpha = 0$（对数修正），适用于 $d > d_c = 4$ 的上临界维度以上。

**Source**: [derivations/ising_model.md] | Weiss (1907); Bragg & Williams (1934)

---

### F16.15: Multicritical Nishimori Point for Biased Noise（偏置噪声的多临界 Nishimori 点）

对于 biased noise model（$p_x \neq p_z$），表面码的阈值由 RBIM 的多临界点决定。hashing bound 条件推广为：

$$H_2(p_x) + H_2(p_z) = 1$$

其中 $H_2(p) = -p\log_2 p - (1-p)\log_2(1-p)$ 是二元熵函数。这定义了 $(p_x, p_z)$ 平面上的一条曲线，是最优（ML）解码器可纠正的边界。

对于纯 $Z$ 噪声（$p_x = 0$），$p_z^{\text{th}} = 50\%$（trivial，因为只有一种错误类型，变成经典纠错）。对于对称噪声（$p_x = p_z = p$），$H_2(p) = 1/2$ 给出 $p \approx 11.0\%$。

**Source**: [derivations/qec_stat_mech_mapping.md] | Dennis et al. 2002, §5; Bombin et al., Phys. Rev. X 2, 021004 (2012)

---

## 快速参考表

| 公式编号 | 名称 | 核心表达式 | 应用场景 |
|---------|------|-----------|---------|
| F16.1 | Ising Hamiltonian | $H = -J\sum s_i s_j - h\sum s_i$ | 格子模型基础 |
| F16.2 | Partition function | $Z = \sum e^{-\beta H}$ | 统计力学核心 |
| F16.3 | Free energy | $F = -k_BT\ln Z$ | 热力学量计算 |
| F16.4 | Boltzmann distribution | $P = e^{-\beta H}/Z$ | 平衡态概率 |
| F16.5 | Magnetization | $m = \langle s_i \rangle \sim \|T-T_c\|^{\beta}$ | 相变序参量 |
| F16.6 | 2D Ising $T_c$ | $\sinh(2\beta_c J) = 1$ | 精确临界温度 |
| F16.7 | Correlation length | $\xi \sim \|T-T_c\|^{-\nu}$ | 临界行为 |
| F16.8 | Percolation threshold | $p_c = 1/2$ (2D bond) | 渗流相变 |
| F16.9 | RBIM | $J_{ij} \in \{+J, -J\}$ | QEC 映射核心模型 |
| F16.10 | Nishimori line | $e^{-2\beta J} = p/(1-p)$ | ML 解码器条件 |
| F16.11 | $Z_2$ gauge theory | $Z = \sum \exp(J\sum \eta_P u_P)$ | Circuit-level noise |
| F16.12 | QEC threshold = 相变 | $p < p_c \Leftrightarrow$ correctable | 阈值的物理本质 |
| F16.13 | Transfer matrix (1D) | $Z = \text{Tr}(T^N)$ | 精确解方法 |
| F16.14 | Mean field $T_c$ | $k_BT_c = zJ$ | 近似方法 |
| F16.15 | Biased noise threshold | $H_2(p_x)+H_2(p_z)=1$ | 偏置噪声阈值 |

---

## 交叉引用

- **[04_qec/key_formulas.md]**: F4.6（阈值定理）、F4.7（toric code Hamiltonian）、F4.8（MWPM 解码器）
- **[04_qec/threshold_theorem.md]**: Part 2, Step 5（渗流理论联系）
- **[04_qec/decoder_theory.md]**: ML 解码器的统计力学解释
- **[04_qec/surface_code_basics.md]**: 表面码格子结构
- **[08_topology/]**: 同调理论与拓扑码的联系
- **[10_optimization/qubo_ising_mapping.md]**: QUBO-Ising 映射（优化问题的 Ising 编码）
