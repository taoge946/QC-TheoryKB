# Lattice Surgery Compilation: Volume Lower Bounds via Graph Embedding Theory

> **Tags**: `lattice-surgery`, `compilation`, `graph-embedding`, `VLSI-layout`, `lower-bound`, `bisection-width`, `pathwidth`, `ZX-calculus`
>
> 将 lattice surgery compilation 形式化为 3D 受限图嵌入问题，利用 VLSI layout theory 建立 space-time volume 的可证明下界。

---

## Prerequisites

- **同调与表面码**: [../../08_topology/derivations/topological_codes_connection.md], [../../04_quantum_error_correction/derivations/surface_code_basics.md]
- **NP-hardness 框架**: [np_hard_problems.md]
- **图论基础**: treewidth, pathwidth, bisection width — 见下文 §1
- **ZX calculus 基础**: Kissinger & Meijer-van de Grift, *Quantum* 4, 218 (2020)

---

## 0. Motivation and Context

Lattice surgery is the leading approach for performing logical operations on surface-code qubits. Given a logical quantum circuit, a **lattice surgery compiler** must:
1. Map logical qubits to spatial positions (surface code patches) on a 2D grid.
2. Schedule merge/split operations across time steps.
3. Route ancilla paths between patches to implement each operation.

The output is a 3D space-time layout: 2D space × 1D time. The primary optimization metric is **space-time volume** $V = W \times H \times D$, where $W, H$ are spatial dimensions and $D$ is the time depth.

Herr, Nori & Devitt (2017) proved that optimizing this layout is NP-hard. However, no **lower bounds** on the achievable volume for a given circuit have been established. We fill this gap by connecting to classical VLSI layout theory.

**Source**: Herr et al., arXiv:1702.00591 (2017) | Litinski, *Quantum* 3, 128 (2019)

---

## 1. Graph-Theoretic Preliminaries

### Definition 1.1 (Bisection Width)

For a graph $G = (V, E)$, the **bisection width** $bw(G)$ is the minimum number of edges crossing any balanced partition:

$$bw(G) = \min_{\substack{S \subseteq V \\ \lfloor |V|/2 \rfloor \leq |S| \leq \lceil |V|/2 \rceil}} \left| \left\{ (u,v) \in E : u \in S, \, v \in V \setminus S \right\} \right|$$

Bisection width measures the "communication bottleneck" of a graph. It is a fundamental parameter in VLSI layout theory and parallel computing.

**Examples**:
- Path $P_n$: $bw(P_n) = 1$
- Cycle $C_n$: $bw(C_n) = 2$
- Complete graph $K_n$: $bw(K_n) = \lfloor n^2/4 \rfloor$
- $\sqrt{n} \times \sqrt{n}$ grid: $bw = \Theta(\sqrt{n})$
- Hypercube $Q_d$ ($n = 2^d$): $bw(Q_d) = n/2$

**Source**: Leighton, *Introduction to Parallel Algorithms and Architectures*, Morgan Kaufmann (1992), Ch. 1

### Definition 1.2 (Pathwidth)

A **path decomposition** of $G = (V, E)$ is a sequence of bags $X_1, X_2, \ldots, X_r \subseteq V$ such that:
1. $\bigcup_i X_i = V$
2. For every edge $(u,v) \in E$, there exists $i$ with $u, v \in X_i$
3. For each $v \in V$, $\{i : v \in X_i\}$ forms a contiguous interval

The **pathwidth** $pw(G) = \min \left(\max_i |X_i| - 1\right)$ over all path decompositions.

Pathwidth measures the minimum "temporal bandwidth" needed to process a graph sequentially — at each time step, a "window" of at most $pw + 1$ vertices must be simultaneously active.

**Key inequality**: $pw(G) \geq bw(G) / \Delta(G)$ where $\Delta(G)$ is the maximum degree.

**Source**: Robertson & Seymour, JCTB 35 (1983) | Kinnersley, Inf. Proc. Lett. 42 (1992)

### Definition 1.3 (Treewidth)

A **tree decomposition** of $G$ replaces the path in Definition 1.2 with a tree. The **treewidth** $tw(G)$ is defined analogously. Always $tw(G) \leq pw(G)$.

### Definition 1.4 (3D Grid Embedding)

A **3D grid embedding** of graph $G = (V, E)$ is a mapping:
- $\phi: V \to \mathbb{Z}^3$ (injective; vertices to grid points)
- For each edge $(u,v) \in E$, a rectilinear path $P_{uv}$ in the 3D grid connecting $\phi(u)$ to $\phi(v)$

The **volume** of the embedding is $V(\phi) = W \times H \times D$ where $W, H, D$ are the side lengths of the axis-aligned bounding box containing all vertex images and edge paths.

Paths may share grid edges only if the underlying physical system permits it (in LS compilation, paths must be edge-disjoint due to occupancy constraints).

**Source**: Leiserson, *Area-Efficient Graph Layouts*, MIT Press (1983)

---

## 2. Formalizing Lattice Surgery Compilation

### Definition 2.1 (ZX Diagram as a Graph)

Given a quantum circuit $\mathcal{C}$, the ZX calculus produces a **ZX diagram** — an open graph $G_{ZX} = (V_{ZX}, E_{ZX})$ where:
- **Vertices** $V_{ZX}$: spiders (Z-spiders = green nodes, X-spiders = red nodes), each with a phase $\alpha \in [0, 2\pi)$
- **Edges** $E_{ZX}$: wires connecting spiders (including Hadamard edges)

After ZX simplification (spider fusion, local complementation, pivot), the diagram typically has far fewer vertices and edges than the original circuit.

**Key property**: The graph structure of $G_{ZX}$ — its connectivity, degree distribution, and global properties like bisection width — directly constrains the space-time layout.

**Source**: van de Wetering, arXiv:2012.13966 (2020) — ZX-calculus tutorial

### Definition 2.2 (Lattice Surgery Compilation as 3D Embedding)

A **lattice surgery compilation** of ZX diagram $G_{ZX}$ is a 3D grid embedding $\phi$ satisfying:

1. **Spatial constraint**: Each vertex $v \in V_{ZX}$ occupies a surface code patch at position $(x_v, y_v)$ during time interval $[t_v^{\text{start}}, t_v^{\text{end}}]$. Hence $\phi(v) = (x_v, y_v, t_v)$ with the understanding that $v$ occupies the vertical column from $t_v^{\text{start}}$ to $t_v^{\text{end}}$.

2. **Routing constraint**: Each edge $(u,v) \in E_{ZX}$ (representing a merge-split operation or multi-body measurement) requires an ancilla routing path $P_{uv}$ in the 3D grid. The path must connect the spatial footprints of $u$ and $v$ at a compatible time step.

3. **Non-overlap constraint**: Routing paths and patch footprints must not overlap in 3D space-time (edge-disjoint paths in the grid graph).

4. **Topological constraint** (LS-specific): Merge paths must be **homologically trivial** in the ambient space relative to the code patches. A merge path that forms a non-trivial cycle around a patch would implement an unintended logical operator.

The **space-time volume** is:

$$\text{Vol}(\phi) = (x_{\max} - x_{\min} + 1) \times (y_{\max} - y_{\min} + 1) \times (t_{\max} - t_{\min})$$

The **LS compilation problem** is: given $G_{ZX}$, find $\phi$ minimizing $\text{Vol}(\phi)$.

### Proposition 2.3 (LS Compilation ⊇ 3D Grid Embedding)

LS compilation is at least as hard as 3D rectilinear grid embedding with edge-disjoint paths. Any lower bound for the latter applies to the former.

**Proof sketch.** Given any instance of 3D edge-disjoint grid embedding (graph $G$, minimize bounding box volume), we can construct an LS compilation instance by treating each vertex as a Z-spider with phase 0 and each edge as a merge operation. The LS constraints (topological, patch footprint) are strictly more restrictive than plain grid embedding. $\square$

---

## 3. Volume Lower Bounds

### Theorem 3.1 (Separator-Based Volume Lower Bound)

Let $G_{ZX}$ be a simplified ZX diagram with $n$ vertices and bisection width $bw = bw(G_{ZX})$. Any valid LS compilation has space-time volume satisfying:

$$\boxed{\text{Vol} \geq \frac{1}{6} \cdot bw(G_{ZX})^{3/2}}$$

**Proof.**

**Step 1 (3D Grid Separator Theorem).** Consider a 3D grid of dimensions $W \times H \times D$ with volume $V = W \cdot H \cdot D$. By the 3D planar separator theorem (Lipton-Tarjan generalized to higher dimensions, Miller et al. 1997), any axis-aligned balanced bisection of the grid removes at most:

$$S_{3D} \leq 2(WH + WD + HD)$$

grid points (the "cutting planes" parallel to each pair of axes).

By the AM-GM inequality applied to products:

$$WH + WD + HD \leq \frac{(W + H + D)^2}{3}$$

and using $V = WHD \leq \left(\frac{W+H+D}{3}\right)^3$ (AM-GM), we get $W + H + D \geq 3V^{1/3}$, thus:

$$S_{3D} \leq 2 \cdot \frac{(W + H + D)^2}{3} \leq 2 \cdot \frac{(W + H + D)^2}{3}$$

A sharper and more direct argument: among the three coordinate-aligned cutting planes through the grid's midpoint, the one with the smallest cross-section has area at most $V^{2/3}$ (since $WH \cdot WD \cdot HD = V^2$, the geometric mean of the three cross-sections is $V^{2/3}$, and the minimum is at most the geometric mean). Thus:

$$\min(WH, WD, HD) \leq V^{2/3}$$

This means there exists a coordinate-aligned plane that separates the grid into two halves, cutting through at most $V^{2/3}$ grid points.

**Step 2 (Embedding implies separator).** If $G_{ZX}$ is embedded in a 3D grid of volume $V$, then any balanced bisection of the grid induces a (not necessarily balanced) partition of the embedded vertices. However, we can choose the cutting plane position along one axis to achieve an approximately balanced partition of the $n$ embedded vertices: by sweeping a plane along the $x$-axis, the number of vertices on each side changes by at most the number of vertices in each slice, so by a pigeonhole argument we can find a cut that is balanced to within $O(V^{1/3})$ vertices.

**Step 3 (Bisection width constraint).** A balanced partition of $G_{ZX}$'s vertices must cut at least $bw(G_{ZX})$ edges. Each cut edge has a routing path that crosses the cutting plane. If paths are edge-disjoint (non-overlap constraint), each crossing requires at least one distinct grid point on the cutting plane. Therefore:

$$bw(G_{ZX}) \leq V^{2/3}$$

$$\Rightarrow \quad V \geq bw(G_{ZX})^{3/2}$$

Accounting for constant factors from the balancing argument:

$$V \geq \frac{1}{6} \cdot bw(G_{ZX})^{3/2}$$

$\square$

**Remark 3.2.** The constant $1/6$ is not tight and can be improved with more careful analysis. The key point is the **scaling**: volume grows at least as $\Omega(bw^{3/2})$.

**Remark 3.3.** If the non-overlap constraint is relaxed (allowing path sharing), the bound weakens to $V \geq \Omega(bw)$ since each crossing needs only $O(1)$ space. However, in LS compilation, path sharing is physically forbidden (simultaneous merges on overlapping ancillas corrupt the code), so the $\Omega(bw^{3/2})$ bound applies.

**Source for technique**: Thompson, *Complexity of VLSI Circuits*, CMU-CS-80-140 (1980) | Leighton (1992), Ch. 5 | Miller, Teng, Thurston & Vavasis, JCSS 56 (1997)

---

### Theorem 3.4 (Depth Lower Bound via Pathwidth)

The time depth $D$ of any valid LS compilation satisfies:

$$\boxed{D \geq pw(G_{ZX}) + 1}$$

**Proof.**

Consider the time axis of the LS compilation. At each time step $t$, the set of "active" vertices — those whose surface code patch is alive (i.e., $t_v^{\text{start}} \leq t \leq t_v^{\text{end}}$) — forms a subset $A_t \subseteq V_{ZX}$.

**Claim**: The sequence of active sets $A_1, A_2, \ldots, A_D$ forms a path decomposition of $G_{ZX}$.

*Verification of path decomposition axioms:*
1. **Coverage**: Every vertex $v$ is active during $[t_v^{\text{start}}, t_v^{\text{end}}]$, so $v \in A_t$ for at least one $t$. Hence $\bigcup_t A_t = V_{ZX}$.
2. **Edge coverage**: For each edge $(u,v) \in E_{ZX}$ (merge operation), the merge must occur at some time $t^*$ when both $u$ and $v$ have active patches. Thus $u, v \in A_{t^*}$.
3. **Consecutiveness**: Each vertex $v$ is active during a contiguous time interval $[t_v^{\text{start}}, t_v^{\text{end}}]$ — a surface code patch cannot be "paused" and "resumed" (deactivating a patch destroys the encoded information unless explicitly teleported, which would create a new vertex in the ZX diagram).

Therefore $(A_1, \ldots, A_D)$ is a valid path decomposition. The width of this decomposition is $\max_t |A_t| - 1$, which is at least $pw(G_{ZX})$ by the minimality of pathwidth. Since the depth $D$ is the number of distinct time steps and the decomposition has $D$ bags:

$$D \geq pw(G_{ZX}) + 1$$

(We need at least $pw + 1$ time steps because in the worst case, the optimal path decomposition of width $pw$ requires at least $pw + 1$ bags to accommodate a clique of size $pw + 1$ in $G_{ZX}$.)

$\square$

**Corollary 3.5.** Since pathwidth is at least treewidth, we also have $D \geq tw(G_{ZX}) + 1$. Furthermore, pathwidth is NP-hard to compute exactly but admits efficient approximation algorithms.

**Remark 3.6.** This theorem has a **direct practical implication**: for any circuit whose ZX diagram has large pathwidth, no compiler (classical or ML-based) can achieve small depth. The pathwidth is a **certificate of irreducible temporal complexity**.

---

### Theorem 3.7 (Combined Space-Depth Tradeoff)

Let $A = W \times H$ be the spatial area and $D$ the depth of an LS compilation. Then:

$$\boxed{A \cdot D \geq \frac{1}{6} \, bw(G_{ZX})^{3/2} \qquad \text{and} \qquad A \geq \frac{bw(G_{ZX})}{D}}$$

In particular, for any fixed depth $D$, the minimum area scales as $A \geq \Omega(bw / D)$. Conversely, for fixed area $A$, the minimum depth scales as $D \geq \Omega(bw / A)$.

**Proof.** The first inequality is Theorem 3.1 restated as $V = A \cdot D \geq \frac{1}{6} bw^{3/2}$. The second follows from the 2D version of the separator argument applied to a single time-slice: a cutting line through the 2D $W \times H$ area separates at most $\min(W,H) \leq \sqrt{A}$ grid points. At any time step $t$, the active vertices and their routing paths within that time slice must accommodate the edge crossings. By counting arguments analogous to Theorem 3.1 Step 3, $\sqrt{A} \geq$ (number of edges crossing the cut at time $t$). Summing over all time steps and using bisection width: $D \cdot \sqrt{A} \geq bw$, giving $A \geq bw^2 / D^2$ and $A \cdot D \geq bw^2 / D$. Combining with Theorem 3.1: $A \geq bw / D$ (from the volumetric bound). $\square$

---

## 4. Concrete Bounds for Circuit Families

We compute bisection width and pathwidth for ZX diagrams arising from standard quantum circuit families.

### Proposition 4.1 (Linear / Chain Circuit)

A chain of $n$ CNOT gates on $n+1$ qubits (each gate between consecutive qubits) has ZX diagram with:
- $bw(G_{ZX}) = O(1)$ (after spider fusion, the graph is a path-like structure)
- $pw(G_{ZX}) = O(1)$
- **Volume bound**: $\text{Vol} \geq \Omega(1)$, actual optimal volume $= \Theta(n)$

The lower bound is trivially loose here because the graph is sparse. This is expected: linear circuits are "easy" to compile.

### Proposition 4.2 (GHZ State Preparation)

GHZ on $n$ qubits (star graph of CNOTs from qubit 1 to all others):
- ZX diagram after simplification: star graph with central Z-spider connected to $n-1$ boundary spiders
- $bw(G_{ZX}) = \lfloor n/2 \rfloor$ (any balanced cut must sever $\geq n/2$ edges through center)
- $pw(G_{ZX}) = n - 1$ (the star requires all vertices in one bag)
- **Volume bound**: $\text{Vol} \geq \Omega(n^{3/2})$, $D \geq n$

### Proposition 4.3 (Quantum Fourier Transform on $n$ Qubits)

QFT has all-to-all two-qubit interactions. After ZX simplification:
- The ZX diagram retains $\Theta(n^2)$ edges with $\Theta(n)$ vertices
- $bw(G_{ZX}) = \Theta(n)$ (complete-graph-like connectivity among $n$ qubits)
- $pw(G_{ZX}) = \Theta(n)$
- **Volume bound**: $\text{Vol} \geq \Omega(n^{3/2})$, $D \geq \Omega(n)$

**Remark**: QFT is among the hardest circuits to compile for LS, matching intuition.

### Proposition 4.4 (Random Clifford+T Circuits)

For random circuits of depth $d$ on $n$ qubits with gate density $\rho$:
- With high probability, $bw(G_{ZX}) = \Theta(\min(n, nd\rho/n)) = \Theta(n)$ for $d = \Omega(n)$
- **Volume bound**: $\text{Vol} \geq \Omega(n^{3/2})$ w.h.p. for sufficiently deep random circuits

### Proposition 4.5 (QAOA / Variational Circuits)

QAOA on a graph $G_{\text{prob}}$ with $p$ rounds:
- ZX diagram inherits the structure of $G_{\text{prob}}$ (each edge → ZZ interaction → spider pair)
- $bw(G_{ZX}) = \Theta(bw(G_{\text{prob}}))$ (bisection width of the problem graph)
- **Volume bound**: $\text{Vol} \geq \Omega(bw(G_{\text{prob}})^{3/2})$

This is particularly interesting: the compilability of QAOA is **directly governed by the bisection width of the optimization problem instance**.

---

## 5. ZX Simplification and Bound Reduction (Theorem 3)

### Theorem 5.1 (Spider Fusion Reduces or Preserves Bisection Width)

Let $G_{ZX}$ contain two adjacent spiders $u, v$ of the same color (both Z or both X) with edge $(u,v) \in E_{ZX}$. Spider fusion merges $u, v$ into a single spider $w$, producing $G'_{ZX}$. Then:

$$bw(G'_{ZX}) \leq bw(G_{ZX})$$

**Proof.**

Let $(S^*, \bar{S}^*)$ be an optimal balanced bisection of $G_{ZX}$ with cut size $bw(G_{ZX})$.

**Case 1**: $u, v$ on the same side (both in $S^*$ or both in $\bar{S}^*$). WLOG $u, v \in S^*$. After fusion, $w$ replaces $\{u, v\}$ in $S^*$. The partition $(S^* \setminus \{u,v\}) \cup \{w\}, \bar{S}^*)$ is a valid partition of $G'_{ZX}$. Any edge from $u$ or $v$ to $\bar{S}^*$ in $G_{ZX}$ becomes an edge from $w$ to $\bar{S}^*$ in $G'_{ZX}$ — but parallel edges are identified (since $G'_{ZX}$ is a simple graph), so the cut size can only decrease or stay the same. The balance condition may be off by 1 vertex (since $|V'| = |V| - 1$), but the adjusted bisection width differs by at most $\Delta(G)$, which is $O(1)$ for bounded-degree ZX diagrams.

**Case 2**: $u \in S^*, v \in \bar{S}^*$. After fusion, place $w$ on either side. The edge $(u,v)$ is eliminated (internal to $w$), reducing the cut by 1. New edges from $w$ may cross the cut, but each new crossing edge from $w$ to the other side was already a crossing edge from $u$ or $v$ in $G_{ZX}$. Net effect: cut size decreases by at least 1 (the removed edge $(u,v)$) minus any new crossings from parallel edge merging. For simple graphs, $bw(G'_{ZX}) \leq bw(G_{ZX})$.

In both cases $bw(G'_{ZX}) \leq bw(G_{ZX})$. $\square$

**Corollary 5.2.** Every sequence of spider fusions can only decrease (or maintain) the volume lower bound. This provides a **formal justification** for the first stage of TopoLS-style compilers (ZX simplification before layout).

### Proposition 5.3 (Local Complementation May Increase Bisection Width)

Unlike spider fusion, the **local complementation** ZX rewrite can increase bisection width. Consider a vertex $v$ with neighbors $N(v)$; local complementation toggles all edges within $N(v)$. If $N(v)$ straddles a balanced cut, toggling can add new crossing edges.

**Implication**: Not all ZX rewrites are guaranteed to help. A compiler should preferentially apply bisection-width-reducing rewrites.

### Theorem 5.5 (Homological Concurrency Bound — Planarity of Merge Paths)

At any single time step $t$ in an LS compilation with spatial dimensions $W \times H$, the maximum number of **simultaneously active merge operations** $m_t$ satisfies:

$$\boxed{m_t \leq W + H - 1}$$

**Proof.**

**Step 1 (Merge paths are planar non-crossing curves).** At time step $t$, the 2D spatial layout contains:
- Active surface code patches $\{P_1, \ldots, P_{q_t}\}$, each occupying a connected region of the $W \times H$ grid.
- Active merge paths $\{\gamma_1, \ldots, \gamma_{m_t}\}$, where each $\gamma_i$ is a rectilinear path connecting two patches.

We claim that **no two merge paths can cross** in the 2D spatial slice.

*Proof of claim.* Consider two merge paths $\gamma_1$ (connecting patches $A, B$) and $\gamma_2$ (connecting patches $C, D$). Suppose they cross at a grid point $p$. At the crossing, the physical qubits at $p$ participate simultaneously in two independent lattice surgery merge operations. This is physically impossible: a merge operation creates an extended stabilizer across the ancilla corridor, and a qubit participating in two such stabilizers would introduce an unintended joint measurement, corrupting both operations.

More precisely, in the homological language [Dennis et al. 2002; Fujii Ch.5]: the merge path $\gamma_i$ creates a 1-chain in the spatial chain complex $C_1(\Sigma_t)$ (where $\Sigma_t$ is the 2D spatial slice at time $t$). For the merge to implement the correct logical operation, $\gamma_i$ must be **homologically trivial relative to the code patches** — i.e., $\gamma_i \in B_1(\Sigma_t \setminus \bigcup_j P_j)$ in the relative homology of the complement. If two paths $\gamma_1, \gamma_2$ share a 1-cell (crossing), their sum $\gamma_1 + \gamma_2$ (in $\mathbb{F}_2$) could form a non-trivial cycle encircling a patch, which would implement an unintended logical operator [see topological_codes_connection.md, Step 4-5].

Therefore, merge paths at any single time step form a **planar set of non-crossing rectilinear paths** in the $W \times H$ grid (with patches as obstacles).

**Step 2 (Counting non-crossing paths in a grid).** In a $W \times H$ grid, any set of vertex-disjoint non-crossing rectilinear paths has size at most $W + H - 1$. This follows from a sweep-line argument: consider a vertical sweep line moving from $x = 0$ to $x = W$. Each path either:
- (a) is entirely to the left or right of the line (contributes 0 crossings), or
- (b) crosses the line at some $y$-coordinate (contributes at least 1 grid point on the line).

The sweep line has at most $H$ grid points. A path crossing the line uses at least one such point, and since paths are non-crossing and vertex-disjoint, each uses a distinct point. So at most $H$ paths cross any vertical line. Similarly, at most $W$ paths cross any horizontal line. A path that crosses neither type of line is contained in a single column or row, and there are at most $W + H$ such slots. In total, $m_t \leq W + H - 1$ (accounting for paths that must use space). $\square$

**Remark 5.6.** The bound $m_t \leq W + H - 1$ is **not captured by Theorem 3.1** (bisection width). Theorem 3.1 constrains total volume but says nothing about instantaneous parallelism. Theorem 5.5 constrains the **rate** at which edges of $G_{ZX}$ can be processed.

### Corollary 5.7 (Edge-Based Depth Lower Bound)

The time depth $D$ of any LS compilation satisfies:

$$\boxed{D \geq \frac{|E_{ZX}|}{W + H - 1} \geq \frac{|E_{ZX}|}{\sqrt{2A}}}$$

where $|E_{ZX}|$ is the number of edges in the ZX diagram (= number of merge operations) and $A = W \times H$.

**Proof.** Each edge of $G_{ZX}$ corresponds to one merge operation that must be scheduled at some time step. By Theorem 5.5, at most $W + H - 1$ merges execute per time step. By pigeonhole, $D \geq |E_{ZX}| / (W + H - 1)$. Using AM-GM: $W + H \leq \sqrt{2(W^2 + H^2)} \leq \sqrt{2} \cdot \sqrt{WH + WH} = \sqrt{2} \cdot \sqrt{2A} = 2\sqrt{A}$, but more directly $W + H \leq 2\sqrt{WH} = 2\sqrt{A}$ by AM-GM. $\square$

### Corollary 5.8 (Edge-Based Volume Lower Bound)

$$\boxed{V \geq \frac{|E_{ZX}|^{3/2}}{\sqrt{2}} \cdot \frac{1}{\sqrt[4]{1}}}$$

More precisely, optimizing the space-depth tradeoff:

$$V = A \cdot D \geq A \cdot \frac{|E_{ZX}|}{2\sqrt{A}} = \frac{|E_{ZX}| \cdot \sqrt{A}}{2}$$

Minimizing $V = A \cdot D$ subject to $D \geq |E_{ZX}| / (2\sqrt{A})$:

$$V \geq A \cdot \frac{|E_{ZX}|}{2\sqrt{A}} = \frac{|E_{ZX}| \sqrt{A}}{2}$$

Since also $V = A \cdot D \geq A$, we substitute $A = V/D$:

$$V \geq \frac{|E_{ZX}|}{2} \cdot \sqrt{V/D} \implies V^2 \geq \frac{|E_{ZX}|^2}{4} \cdot \frac{V}{D} \implies V \cdot D \geq \frac{|E_{ZX}|^2}{4}$$

This is already $V \cdot D \geq |E|^2/4$, but since $D \leq V$ (area $A \geq 1$):

$$V^2 \geq V \cdot D \geq \frac{|E_{ZX}|^2}{4} \implies V \geq \frac{|E_{ZX}|}{2}$$

For a tighter bound, combine with Theorem 3.1. The **combined lower bound** is:

$$\boxed{V \geq \max\left(\frac{bw^{3/2}}{6}, \; \frac{|E_{ZX}| \cdot \sqrt{A}}{2}\right)}$$

The two bounds are **complementary**: Theorem 3.1 is stronger for dense graphs with high bisection width, while Corollary 5.8 is stronger for graphs with many edges but moderate bisection width (e.g., bounded-degree expanders).

### Theorem 5.9 (Magic State Transport Penalty)

Let the circuit contain $N_T$ non-Clifford ($T$) gates. Each $T$ gate requires magic state injection via a dedicated ancilla path connecting a distillation factory to the consumption point [Fujii Ch.2 §2.8; magic_state_distillation.md]. These transport paths are subject to the same non-crossing constraint as merge paths (Theorem 5.5).

If magic state factories occupy a spatial footprint $A_{\text{factory}}$, then the **effective routing area** for merges at any time step is reduced to $A - A_{\text{factory}}$, giving:

$$m_t \leq 2\sqrt{A - A_{\text{factory}}}$$

Furthermore, magic state transports compete with merges for time slots. If $r$ magic states must be transported per time step (to keep up with T-gate consumption rate), then:

$$m_t + r \leq W + H - 1$$

This gives a refined depth bound:

$$\boxed{D \geq \frac{|E_{ZX}| + N_T}{W + H - 1}}$$

where $N_T$ is the number of T gates (each requiring one magic state transport that occupies one merge slot).

**Proof.** Each T gate's magic state injection occupies at least one merge slot at the time step when the injection occurs (the ancilla path from factory to target patch follows the same routing constraints as a merge path). Thus the total number of "routing events" over all time steps is at least $|E_{ZX}| + N_T$, and the rate is bounded by $W + H - 1$ per step. $\square$

**Remark 5.10.** This theorem formally confirms a weaker version of Conjecture 6.1 (§6.3): the T-gate count adds a linear contribution to the depth lower bound, and consequently to the volume. For circuits with $N_T = \Omega(n^2)$ (typical for chemistry applications), this can dominate the bisection-width bound.

---

## 6. Discussion: Tightness and Gaps

### 6.1 When is the Bound Tight?

The $\Omega(bw^{3/2})$ bound is **tight up to constants** for graphs that admit efficient 3D embeddings. For example:
- $\sqrt{n} \times \sqrt{n}$ grid graph: $bw = \Theta(\sqrt{n})$, bound gives $V \geq \Omega(n^{3/4})$, actual optimal embedding $V = \Theta(n)$ — bound is loose by factor $n^{1/4}$.
- Complete graph $K_n$: $bw = \Theta(n^2)$, bound gives $V \geq \Omega(n^3)$, actual $V = \Theta(n^3)$ — **tight**.

For **dense** ZX diagrams (QFT, random circuits), the bound is expected to be near-tight. For **sparse** diagrams (linear circuits), the bound is loose but the compilation is easy anyway.

### 6.2 Comparison with Thompson's 2D Bound

Thompson (1980) proved for 2D VLSI layout: $A \geq \Omega(bw^2)$. Our 3D result $V \geq \Omega(bw^{3/2})$ is weaker in exponent because the extra dimension provides more "room" to route. This is consistent with the intuition that 3D compilation is more efficient than 2D — one of the motivations for considering the time dimension explicitly.

### 6.3 Hierarchy of Bounds

The full set of lower bounds forms a complementary hierarchy:

| Bound | Source | Best for |
|-------|--------|----------|
| $V \geq \frac{1}{6} bw^{3/2}$ | Thm 3.1 (separator) | Dense graphs (QFT, random) |
| $D \geq pw + 1$ | Thm 3.4 (pathwidth) | Circuits with high sequential depth |
| $D \geq \frac{|E| + N_T}{W+H-1}$ | Thm 5.5 + 5.9 (concurrency) | Many-edge, many-T circuits |
| $A \geq bw / D$ | Thm 3.7 (tradeoff) | Fixed-depth compilation |

For a given circuit, the tightest bound is $V \geq \max(\text{all applicable bounds})$. ML compilers should compute all bounds and report the **optimality gap** relative to the tightest one.

### 6.4 Open Problems

1. **Tight volume bound for surface code circuits**: Incorporate the surface code patch geometry (each patch occupies $d \times d$ physical qubits, not a single grid point). This scales all bounds by $d^2$ in the spatial dimensions.

2. **Homological tightening beyond planarity**: Theorem 5.5 uses the non-crossing property of merge paths but does not fully exploit the **homological triviality constraint**. A merge path that is homologically trivial relative to patches must be "contractible" in the complement space, which is a stronger constraint than non-crossing. This could yield tighter bounds for specific patch configurations.

3. **Distillation-aware bounds**: Theorem 5.9 treats magic state factories as blackboxes. Incorporating the internal structure of distillation protocols (e.g., Bravyi-Kitaev 15-to-1, see [magic_state_distillation.md]) could refine the $A_{\text{factory}}$ term.

---

## 7. Implications for ML-Based Compilation

### 7.1 Optimality Certificate

For any ML compiler output with volume $V_{\text{ML}}$, compute:

$$\text{Optimality Ratio} = \frac{V_{\text{ML}}}{bw(G_{ZX})^{3/2} / 6}$$

A ratio close to 1 certifies near-optimality. A ratio $\gg 1$ indicates room for improvement.

### 7.2 Feature Design

The lower bound theorems suggest that an ML model for LS compilation should encode:
- **Bisection width** (or approximation thereof) as a global graph feature
- **Pathwidth / treewidth** as indicators of temporal complexity
- **Degree distribution** (spider fusion opportunities = potential $bw$ reduction)
- **Local density** (subgraph bisection widths for spatial congestion prediction)

### 7.3 Reward Shaping

Instead of raw volume as reward, use the **normalized volume**:

$$r = -\frac{V_{\text{actual}}}{V_{\text{lower bound}}}$$

This normalizes across circuits of different sizes and focuses the learning signal on approaching the theoretical limit.

---

## 8. Summary of Results

| Theorem | Statement | Tightness | Source |
|---------|-----------|-----------|--------|
| 3.1 | $\text{Vol} \geq \frac{1}{6} bw^{3/2}$ | Tight for dense, loose for sparse | 3D separator |
| 3.4 | $D \geq pw + 1$ | Tight | Path decomposition |
| 3.7 | $A \geq bw / D$ | Follows from 3.1 | Space-depth tradeoff |
| 5.1 | Spider fusion: $bw' \leq bw$ | Exact | Bisection argument |
| 5.3 | Local comp.: $bw'$ may increase | N/A (negative) | Counterexample |
| **5.5** | **$m_t \leq W + H - 1$** | **Tight for grid** | **Homological planarity** |
| **5.7** | **$D \geq |E| / (W+H-1)$** | **Complementary to 3.4** | **Concurrency + pigeonhole** |
| **5.9** | **$D \geq (|E|+N_T)/(W+H-1)$** | **Adds T-gate cost** | **Magic state transport** |

**Computability**: $bw$ is NP-hard to compute exactly but admits $O(\log n)$-approximation (Leighton & Rao, JACM 1999). For bounded-degree graphs (typical for ZX diagrams), faster algorithms exist. $pw$ is NP-hard in general but computable in $O(n)$ for fixed $pw$ (Bodlaender, JCSS 1996). $|E_{ZX}|$ and $N_T$ are trivially computable from the circuit.

**Key insight**: Theorems 3.1/3.4 and 5.5/5.7/5.9 capture **orthogonal** aspects of compilation difficulty. The bisection-width bounds (§3) measure global connectivity bottlenecks. The concurrency bounds (§5.5-5.9) measure instantaneous parallelism limits imposed by the planarity of merge paths and the homological triviality constraint. A complete lower bound uses both.

---

**See also**: [np_hard_problems.md] (complexity framework) | [../../08_topology/key_formulas.md] (F8.1-F8.12 for homological background) | [neural_co_theory.md] (ML methods for CO)
