# Canonical Forms

![[Boolean_CanonicalForm.png]]
In digital logic, Canonical Forms are standard ways of representing Boolean functions. Think of them as the "official" or "standardized" forms. Why do we need them? Because they provide a unique representation for each Boolean function.

### This is super useful for:

- **Comparing Boolean expressions:** It becomes easy to check if two different looking expressions are actually the same function.
- **Implementation:** Canonical forms can be directly implemented using standard logic gates.
- **Simplification:** They serve as a starting point for simplifying complex Boolean expressions.

## There are two main types of Canonical Forms:

1. Sum of Products (SOP) Canonical Form
2. Product of Sums (POS) Canonical Form

Let's break down each one.

### Sum of Products (SOP) Canonical Form (also called Minterm Canonical Form)

- **"Sum of Products"**: The name itself gives you a hint. It's a sum (OR operation) of product terms (AND operations).

- **Minterms**: The key building blocks of the SOP canonical form are called minterms.

  - **What is a Minterm?** A minterm is a product (AND) term that contains all the variables of the Boolean function, either in their true (uncomplemented) form or complemented form.

  - For a function with $n$ variables, there are $2^n$ possible minterms.

  - Each minterm is assigned a unique index number. For example, with 2 variables (say, $A$ and $B$), we have $2^2 = 4$ minterms:

    $$
    \begin{array}{|c|c|c|}
    \hline
    \text{Minterm Index} & \text{Minterm} & \text{Variables (A, B)} \\
    \hline
    m_0 & A'B' & A = 0, B = 0 \\
    \hline
    m_1 & A'B & A = 0, B = 1 \\
    \hline
    m_2 & AB' & A = 1, B = 0 \\
    \hline
    m_3 & AB & A = 1, B = 1 \\
    \hline
    \end{array}
    $$

  - **Notice**:
    - For each minterm, when the variable value is '0', we use the complemented form (e.g., $A'$).
    - When the variable value is '1', we use the true form (e.g., $A$).
    - Each minterm is true (evaluates to '1') for only one combination of input variable values and false ('0') for all others.

  - **Example:** Let's say we have a Boolean function $F(A, B)$ whose truth table is:

    $$
    \begin{array}{|c|c|c|}
    \hline
    A & B & F(A, B) \\
    \hline
    0 & 0 & 0 \\
    \hline
    0 & 1 & 1 \\
    \hline
    1 & 0 & 0 \\
    \hline
    1 & 1 & 1 \\
    \hline
    \end{array}
    $$

  - The function $F(A, B)$ is '1' for the input combinations $(A=0, B=1)$ and $(A=1, B=1)$. These correspond to minterms $m_1$ $(A'B)$ and $m_3$ $(AB)$.

  - Therefore, the canonical SOP form for $F(A, B)$ is:

    $$
    F(A, B) = m_1 + m_3 = A'B + AB
    $$

  - We can also represent this in a more compact way using the minterm indices:

    $$
    F(A, B) = \sum m(1, 3)
    $$

    The $\sum$ (sigma) indicates "sum of", and $m(1, 3)$ lists the indices of the minterms included in the sum.

### Product of Sums (POS) Canonical Form (also called Maxterm Canonical Form)

- **"Product of Sums"**: Again, the name is informative. It's a product (AND operation) of sum terms (OR operations).

- **Maxterms**: The building blocks of the POS canonical form are called maxterms.

  - **What is a Maxterm?** A maxterm is a sum (OR) term that contains all the variables of the Boolean function, either in their true or complemented form.

  - For a function with $n$ variables, there are also $2^n$ possible maxterms.

  - Each maxterm is assigned a unique index number, just like minterms. For 2 variables $(A, B)$:

    $$
    \begin{array}{|c|c|c|}
    \hline
    \text{Maxterm Index} & \text{Maxterm} & \text{Variables (A, B)} \\
    \hline
    M_0 & A + B & A = 0, B = 0 \\
    \hline
    M_1 & A + B' & A = 0, B = 1 \\
    \hline
    M_2 & A' + B & A = 1, B = 0 \\
    \hline
    M_3 & A' + B' & A = 1, B = 1 \\
    \hline
    \end{array}
    $$

  - **Notice**:
    - For each maxterm, when the variable value is '0', we use the true form (e.g., $A$).
    - When the variable value is '1', we use the complemented form (e.g., $A'$).
    - Each maxterm is false (evaluates to '0') for only one combination of input variable values and true ('1') for all others.

  - **Example (using the same $F(A, B)$ truth table):**

    $$
    \begin{array}{|c|c|c|}
    \hline
    A & B & F(A, B) \\
    \hline
    0 & 0 & 0 \\
    \hline
    0 & 1 & 1 \\
    \hline
    1 & 0 & 0 \\
    \hline
    1 & 1 & 1 \\
    \hline
    \end{array}
    $$

  - The function $F(A, B)$ is '0' for the input combinations $(A=0, B=0)$ and $(A=1, B=0)$. These correspond to maxterms $M_0$ $(A + B)$ and $M_2$ $(A' + B)$.

  - Therefore, the canonical POS form for $F(A, B)$ is:

    $$
    F(A, B) = M_0 \cdot M_2 = (A + B) \cdot (A' + B)
    $$

  - Compact representation using maxterm indices:

    $$
    F(A, B) = \prod M(0, 2)
    $$

    The $\prod$ (pi) indicates "product of", and $M(0, 2)$ lists the indices of the maxterms included in the product.

## Why Terms Must Have All Variables for Canonical Forms (Minterms and Maxterms)

You are absolutely right to point out that if a term doesn't contain all the variables, it's not a minterm or a maxterm, and therefore, the expression is not in canonical form.

### Minterms and Maxterms are "Full" Terms:

The defining characteristic of minterms and maxterms is that they must include every variable of the function. This ensures that each minterm/maxterm corresponds to a specific row in the truth table, representing a unique combination of input variable values.

### Terms that do not include all variables are not minterms or maxterms, and expressions containing such terms are **not in canonical form**.

- **To convert a non-canonical expression to canonical SOP form**, we need to expand each term to include all variables. For example, consider the function $G(X, Y, Z)$:

  $$
  G(X, Y, Z) = XY + X'Z'
  $$

  - **For $XY$**: Multiply by $(Z + Z')$ (which is always '1', so it doesn't change the value):

    $$\begin{align*}
    XY = XY(Z + Z') = XYZ + XYZ' \quad \\(\text{These are now minterms: } m_7 \text{ and } m_6)
    \end{align*}$$

  - **For $X'Z'$**: Multiply by $(Y + Y')$:

    $$\begin{align*}
    X'Z' = X'Z'(Y + Y') = X'YZ' + X'Y'Z' \quad \\(\text{These are also minterms: } m_2 \text{ and } m_0)
     \end{align*}$$

  - **So, the canonical SOP form of $G(X, Y, Z)$ is:**

    $$\begin{align*}{c}
    G(X, Y, Z) &= XYZ + XYZ' + X'YZ' + X'Y'Z' \\&= m_7 + m_6 + m_2 + m_0\\ &= \sum m(0, 2, 6, 7)
     \end{align*}$$

### In Summary:

- Canonical SOP form is a sum of minterms.
- Canonical POS form is a product of maxterms.
- **Minterms and maxterms must include all variables** of the function.
- Terms that do not include all variables are not minterms or maxterms, and expressions containing such terms are **not in canonical form**.