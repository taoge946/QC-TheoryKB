# Classical Information Theory

> Source: Mark M. Wilde, *From Classical to Quantum Shannon Theory* (Cambridge University Press, 2nd edition, 2019)

---

## 1. Shannon Entropy

### Definition: Information Content
**[Wilde, Ch.10, Eq. 10.1]**

The information content (surprisal) of a particular realization $x$ of random variable $X$ is:
$$i(x) \equiv -\log(p_X(x))$$
where the logarithm is base two (units of bits).

**Properties:**
- Non-negative: $i(x) \geq 0$
- Additive for independent events: $i(x_1, x_2) = i(x_1) + i(x_2)$

### Definition: Shannon Entropy
**[Wilde, Ch.10, Definition 10.1.1]**

The entropy of a discrete random variable $X$ with probability distribution $p_X(x)$ is:
$$H(X) \equiv -\sum_x p_X(x) \log(p_X(x))$$
with the convention $0 \cdot \log(0) = 0$.

**Interpretation:** $H(X)$ quantifies the expected information gain (in bits) upon learning the outcome of random variable $X$.

### Properties of Shannon Entropy
**[Wilde, Ch.10, Section 10.1.2]**

1. **Non-negativity:** $H(X) \geq 0$
2. **Concavity:** $H(X_B) \geq q H(X_1) + (1-q) H(X_2)$ where $p_{X_B}(x) = q p_{X_1}(x) + (1-q) p_{X_2}(x)$
3. **Permutation invariance:** $H$ depends only on the probabilities, not the values
4. **Minimum value:** $H(X) = 0$ iff $X$ is deterministic
5. **Maximum value:** $H(X) \leq \log|\mathcal{X}|$, with equality iff $X$ is uniform

### Definition: Binary Entropy Function
**[Wilde, Ch.10, Definition 10.1.2]**

$$h_2(p) \equiv -p \log p - (1-p) \log(1-p)$$

---

## 2. Conditional Entropy

### Definition
**[Wilde, Ch.10, Definition 10.2.1]**

$$H(X|Y) \equiv -\sum_{x,y} p_{X,Y}(x,y) \log(p_{X|Y}(x|y))$$

Equivalently: $H(X|Y) = \sum_y p_Y(y) H(X|Y=y)$.

### Theorem: Conditioning Does Not Increase Entropy
**[Wilde, Ch.10, Theorem 10.2.1]**

$$H(X) \geq H(X|Y)$$
with equality iff $X$ and $Y$ are independent.

**Proof sketch:** Follows from non-negativity of mutual information, which itself follows from non-negativity of relative entropy.

---

## 3. Joint Entropy and Chain Rule

### Definition
**[Wilde, Ch.10, Definition 10.3.1]**

$$H(X,Y) \equiv -\sum_{x,y} p_{X,Y}(x,y) \log(p_{X,Y}(x,y))$$

### Chain Rule for Entropy
**[Wilde, Ch.10, Exercise 10.3.2]**

$$H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)$$

More generally:
$$H(X_1, \ldots, X_n) = H(X_1) + H(X_2|X_1) + \cdots + H(X_n|X_{n-1},\ldots,X_1)$$

### Subadditivity
**[Wilde, Ch.10, Exercise 10.3.3]**

$$H(X_1, \ldots, X_n) \leq \sum_{i=1}^n H(X_i)$$

---

## 4. Mutual Information

### Definition
**[Wilde, Ch.10, Definition 10.4.1]**

$$I(X;Y) \equiv H(X) - H(X|Y) = H(Y) - H(Y|X)$$

Equivalently:
$$I(X;Y) = \sum_{x,y} p_{X,Y}(x,y) \log\left(\frac{p_{X,Y}(x,y)}{p_X(x) p_Y(y)}\right)$$

### Theorem: Non-Negativity of Mutual Information
**[Wilde, Ch.10, Theorem 10.4.1]**

$$I(X;Y) \geq 0$$
with equality iff $X$ and $Y$ are independent.

**Proof:** Follows from $I(X;Y) = D(p_{X,Y} \| p_X \otimes p_Y) \geq 0$ (non-negativity of relative entropy).

---

## 5. Relative Entropy (Kullback-Leibler Divergence)

### Definition
**[Wilde, Ch.10, Definition 10.5.1]**

$$D(p \| q) \equiv \begin{cases} \sum_x p(x) \log\left(\frac{p(x)}{q(x)}\right) & \text{if } \mathrm{supp}(p) \subseteq \mathrm{supp}(q) \\ +\infty & \text{otherwise} \end{cases}$$

### Theorem: Non-Negativity of Relative Entropy
**[Wilde, Ch.10, Theorem 10.6.1]**

Let $p(x)$ be a probability distribution and $q: \mathcal{X} \to [0,1]$ with $\sum_x q(x) \leq 1$. Then:
$$D(p \| q) \geq 0$$
with equality iff $p = q$.

**Proof:** Uses the fundamental inequality $\ln x \leq x - 1$ for $x \geq 0$:
$$D(p\|q) = -\frac{1}{\ln 2}\sum_x p(x) \ln\frac{q(x)}{p(x)} \geq \frac{1}{\ln 2}\sum_x p(x)\left(1 - \frac{q(x)}{p(x)}\right) = \frac{1}{\ln 2}\left(\sum_x p(x) - \sum_x q(x)\right) \geq 0$$

### Key Relation
$$I(X;Y) = D(p_{X,Y} \| p_X \otimes p_Y)$$

---

## 6. Conditional Mutual Information and Strong Subadditivity

### Definition
**[Wilde, Ch.10, Definition 10.5.2]**

$$I(X;Y|Z) \equiv H(Y|Z) - H(Y|X,Z) = H(X|Z) - H(X|Y,Z)$$

### Theorem: Strong Subadditivity (Classical)
**[Wilde, Ch.10, Theorem 10.5.1]**

$$I(X;Y|Z) \geq 0$$
Equivalently:
- $H(XY|Z) \leq H(X|Z) + H(Y|Z)$
- $H(XYZ) + H(Z) \leq H(XZ) + H(YZ)$
- $H(X|YZ) \leq H(X|Z)$

Saturation iff $X - Z - Y$ forms a Markov chain.

**Proof:** $I(X;Y|Z) = \sum_z p_Z(z) I(X;Y|Z=z) \geq 0$ since each term is non-negative by non-negativity of mutual information.

---

## 7. Data Processing Inequality

### Theorem: Mutual Information DPI
**[Wilde, Ch.10, Theorem 10.6.2]**

If $X \to Y \to Z$ forms a Markov chain, then:
$$I(X;Y) \geq I(X;Z)$$

**Proof:** Expand $I(X;YZ)$ two ways:
$$I(X;YZ) = I(X;Y) + \underbrace{I(X;Z|Y)}_{=0 \text{ (Markov)}} = I(X;Z) + \underbrace{I(X;Y|Z)}_{\geq 0 \text{ (SSA)}}$$
Therefore $I(X;Y) = I(X;Z) + I(X;Y|Z) \geq I(X;Z)$.

### Theorem: Monotonicity of Relative Entropy
**[Wilde, Ch.10, Corollary 10.6.1]**

For a classical channel $N(y|x)$:
$$D(p \| q) \geq D(Np \| Nq)$$
where $(Np)(y) = \sum_x N(y|x) p(x)$.

**Saturation:** $D(p\|q) = D(Np\|Nq)$ iff $RNp = p$, where $R$ is the Bayes recovery channel: $R(x|y)(Nq)(y) = N(y|x)q(x)$.

---

## 8. Fano's Inequality

### Theorem
**[Wilde, Ch.10, Theorem 10.6.3]**

If $X \to Y \to \hat{X}$ is a Markov chain with $p_e \equiv \Pr\{\hat{X} \neq X\}$, then:
$$H(X|Y) \leq H(X|\hat{X}) \leq h_2(p_e) + p_e \log(|\mathcal{X}| - 1)$$

**Proof outline:**
1. Let $E$ be indicator of error: $E = \mathbf{1}[\hat{X} \neq X]$
2. $H(EX|\hat{X}) = H(X|\hat{X})$ (since $E$ is determined by $X, \hat{X}$)
3. Also $H(EX|\hat{X}) = H(E|\hat{X}) + H(X|E,\hat{X}) \leq h_2(p_e) + p_e \log(|\mathcal{X}|-1)$
4. DPI gives $H(X|\hat{X}) \geq H(X|Y)$

**Importance:** The bound is sharp. Fano's inequality is the key tool for proving converse theorems in information theory.

---

## 9. Continuity of Entropy (Zhang-Audenaert)

### Theorem
**[Wilde, Ch.10, Theorem 10.6.5]**

Let $p_X, p_Y$ be distributions on alphabet $\mathcal{A}$ with $T = \frac{1}{2}\|p_X - p_Y\|_1$. Then:
$$|H(X) - H(Y)| \leq T \log(|\mathcal{A}| - 1) + h_2(T)$$

This bound is optimal (tight for specific distributions).

**Proof:** Uses Fano's inequality applied to a maximal coupling of the two random variables.

---

## 10. Pinsker's Inequality

### Theorem
**[Wilde, Ch.10, Theorem 10.7.1]**

$$D(p \| q) \geq \frac{1}{2 \ln 2} \|p - q\|_1^2$$

**Proof:** Applies monotonicity of relative entropy under a coarse-graining channel $\mathcal{A}$ that maps to a binary alphabet $\{A, A^c\}$ where $A = \{x : p(x) \geq q(x)\}$, then uses the calculus lemma: $a \ln(a/b) + (1-a)\ln((1-a)/(1-b)) \geq 2(a-b)^2$.

**Importance:** Connects the "information-theoretic distance" (relative entropy) to the "statistical distance" (trace distance). Fundamental for near-saturation analysis.

---

## 11. Shannon's Source Coding Theorem

### Theorem (Informal)
**[Wilde, Ch.2, Section 2.1.3]**

An i.i.d. source with entropy $H(X)$ can be compressed to $H(X)$ bits per symbol. Conversely, compression below $H(X)$ bits per symbol is impossible with vanishing error.

**Key idea:** The typical set $T_\delta^{X^n}$ has approximately $2^{nH(X)}$ sequences, each with probability approximately $2^{-nH(X)}$. We can enumerate them with $nH(X)$ bits.

---

## 12. Shannon's Channel Coding Theorem

### Theorem (Informal)
**[Wilde, Ch.2, Section 2.2]**

The capacity of a discrete memoryless channel $p_{Y|X}(y|x)$ is:
$$C = \max_{p_X} I(X;Y)$$

Rates below $C$ are achievable with vanishing error; rates above $C$ have error bounded away from zero.

**Direct part:** Random coding + joint typicality decoding.
**Converse:** Uses Fano's inequality + data processing inequality.

---

## 13. Refined Monotonicity of Relative Entropy

### Theorem
**[Wilde, Ch.10, Theorem 10.7.3]**

For classical channel $N$ with recovery channel $R(x|y)(Nq)(y) = N(y|x)q(x)$:
$$D(p \| q) - D(Np \| Nq) \geq D(p \| RNp)$$

**Interpretation:** If relative entropy decreases little under channel $N$, then the Bayes recovery channel $R$ approximately recovers $p$ from $Np$. This is the classical precursor of quantum recoverability theorems.
