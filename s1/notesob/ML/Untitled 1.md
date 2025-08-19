## Binary Classifiers

A **binary classifier** is a function that takes a real-valued vector as input and outputs one of two possible labels: {-1, +1}. The notation shows:

- **Input**: $x \in \mathbb{R}^d$ (a d-dimensional vector of real numbers)
- **Classifier**: $h$ (the hypothesis/learned model)
- **Output**: $y \in \{-1, +1\}$ (the predicted class label)

The process flows as: $x \rightarrow h \rightarrow y$

## Feature Representation

In practice, raw data (songs, images, people) isn't naturally in numerical vector form. The **feature function** $\phi(x)$ transforms real-world objects into numerical representations:

- $\phi$ extracts measurable characteristics (person's height, song's bass level, image pixel values)
- The classifier then operates on $\phi(x)$ rather than the raw input
- This preprocessing step is often implicit but crucial

## Supervised Learning Setup

**Training data** consists of labeled examples: $D_n = \{(x^{(1)}, y^{(1)}), \ldots, (x^{(n)}, y^{(n)})\}$

- Each $x^{(i)}$ is a $d \times 1$ column vector (features)
- Each $y^{(i)}$ is the correct label for $x^{(i)}$
- The goal: learn $h$ such that $h(x^{(i)}) \approx y^{(i)}$

## Training Error vs Test Error

**Training Error** $E_n(h)$ measures performance on training data:
$$E_n(h) = \frac{1}{n}\sum_{i=1}^{n} \begin{cases} 1 & \text{if } h(x^{(i)}) \neq y^{(i)} \\ 0 & \text{otherwise} \end{cases}$$

This counts the fraction of training examples misclassified.

**Test Error** $E(h)$ measures performance on new, unseen data:
$$E(h) = \frac{1}{n'}\sum_{i=n+1}^{n+n'} \begin{cases} 1 & \text{if } h(x^{(i)}) \neq y^{(i)} \\ 0 & \text{otherwise} \end{cases}$$

## The Generalization Challenge

The key insight is that **what matters is test error, not training error**. A classifier is only useful if it performs well on new data it hasn't seen during training.

**Key assumptions**:
- Training and test data are drawn from the same probability distribution
- Training and test examples are independent

**The strategy**: Find a classifier with low training error and hope it **generalizes** well (achieves low test error). However, simply minimizing training error can lead to **overfitting**, where the model memorizes training data but fails on new examples. This tension between training performance and generalization ability is central to machine learning and motivates techniques like regularization, cross-validation, and complexity control.

