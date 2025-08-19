## Machine Learning Algorithms Framework

This text introduces the formal framework for **machine learning algorithms** and explores **linear classifiers** in depth.

### Hypothesis Class H

A **hypothesis class H** is the set of all possible classifiers that a learning algorithm can choose from. Think of it as the "menu" of available models:

- **H** can be finite (e.g., decision trees with max depth 5) or infinite (e.g., all possible linear classifiers).
- Each element $h \in H$ represents a mapping from $\mathbb{R}^d \to \{-1, +1\}$.
- **Key insight**: The choice of $H$ dramatically affects performance.

### Learning Algorithm Process

The learning process follows this flow:

$$
D_n \to \text{learning algorithm (H)} \to h
$$

The algorithm examines the training data $D_n$ and selects the "best" classifier $h$ from the hypothesis class $H$.

### The Expressiveness Trade-off

- **More expressive H** (larger, more complex):
  - Can fit training data better (lower training error).
  - Risk of overfitting (poor generalization).
  
- **Less expressive H** (smaller, simpler):
  - May not fit training data perfectly.
  - Often generalizes better to new data.

### Linear Classifiers

#### Mathematical Definition

A linear classifier in $d$ dimensions is parameterized by:

- **$\theta \in \mathbb{R}^d$**: weight vector (a $d \times 1$ column vector).
- **$\theta_0 \in \mathbb{R}$**: bias term (a scalar).

The classifier function is:

$$
h(x; \theta, \theta_0) = \text{sign}(\theta^\top x + \theta_0) =
\begin{cases}
+1 & \text{if } \theta^\top x + \theta_0 > 0 \\
-1 & \text{otherwise}
\end{cases}
$$

#### Geometric Interpretation

Linear classifiers define a **hyperplane** in $\mathbb{R}^d$:

- The hyperplane equation: $\theta^\top x + \theta_0 = 0$.
- **$\theta$** is the normal vector (perpendicular to the hyperplane).
- **$\theta_0$** determines the hyperplane's distance from the origin.
- Points are classified based on which side of the hyperplane they fall on.

### Working Through the Example

Given: $\theta = [-1, 1.5]^\top$, $\theta_0 = 3$.

- **For $x^{(1)} = [3, 0]^\top$:**

$$
h(x^{(1)}) = \text{sign}([-1, 1.5]^\top [3, 0]^\top + 3) = \text{sign}(-3 + 0 + 3) = \text{sign}(0) = +1
$$

- **For $x^{(2)} = [4, -1]^\top$:**

$$
h(x^{(2)}) = \text{sign}([-1, 1.5]^\top [4, -1]^\top + 3) = \text{sign}(-4 - 1.5 + 3) = \text{sign}(-2.5) = -1
$$

### Study Questions Answered

#### Question 1: Normal Vector

The **green vector normal to the hyperplane** is simply **$\theta$**:

$$
\text{Normal vector} = \begin{bmatrix} -1 \\ 1.5 \end{bmatrix}
$$

This vector points perpendicular to the decision boundary and indicates the direction of the positive half-space.

#### Question 2: Flipping Classifications

To keep the hyperplane in the same location but **flip all classifications**, multiply both parameters by $-1$:

- **New parameters:**
  - $\theta_{\text{new}} = -\theta = [1, -1.5]^\top$
  - $\theta_{0,\text{new}} = -\theta_0 = -3$

This changes $\theta^\top x + \theta_0$ to $-\theta^\top x - \theta_0 = -(\theta^\top x + \theta_0)$, which flips the sign of the decision function while keeping the hyperplane $\theta^\top x + \theta_0 = 0$ unchanged.

### Why Linear Classifiers Matter

Linear classifiers are fundamental because they are:

- **Mathematically tractable**: Easy to analyze and optimize.
- **Computationally efficient**: Fast training and prediction.
- **Interpretable**: $\theta$ coefficients show feature importance.
- **Foundation for advanced methods**: SVMs, neural networks, etc.
- **Surprisingly powerful**: Work well on many real-world problems.

The simplicity of linear classifiers makes them an excellent starting point for understanding more complex machine learning algorithms.
