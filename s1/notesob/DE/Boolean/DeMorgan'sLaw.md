# Boolean Algebra De Morgan's Law: Proof
## 1. De Morgan's First Theorem: $\overline{A + B} = \overline{A} \cdot \overline{B}$

To prove this, we verify that $\overline{A} \cdot \overline{B}$ satisfies the **complementarity law** with $A + B$:

### Step 1: Show $(A + B) \cdot (\overline{A} \cdot \overline{B}) = 0$

$$
\begin{aligned}
(A + B)(A \cdot B) &= \\
&= A \cdot A \cdot B + B \cdot A \cdot B && \text{Distributive Law} \\
&= 0 \cdot B + 0 \cdot A && [\text{Complementarity Law: } A \cdot A = 0] \\
&= 0 + 0 = 0
\end{aligned}
$$

### Step 2: Show $(A + B) + (\overline{A} \cdot \overline{B}) = 1$
$$
\begin{align*}
(A + B) + (\overline{A} \cdot \overline{B}) 
&= (A + B + \overline{A}) \cdot (A + B + \overline{B}) 
&& \text{[Distributive Law]} \\
&= (1 + B) \cdot (1 + A) 
&& \text{[Complementarity Law: } A + \overline{A} = 1 \text{]} \\
&= 1 \cdot 1 = 1
\end{align*}
$$

Since both conditions hold, $\overline{A + B} = \overline{A} \cdot \overline{B}$.

---

## 2. De Morgan's Second Theorem: $\overline{A \cdot B} = \overline{A} + \overline{B}$

Similarly, verify $\overline{A} + \overline{B}$ complements $A \cdot B$:

### Step 1: Show $(A \cdot B) \cdot (\overline{A} + \overline{B}) = 0$
$$
\begin{align*}
(A \cdot B)(\overline{A} + \overline{B}) 
&= A \cdot B \cdot \overline{A} + A \cdot B \cdot \overline{B} 
&& \text{[Distributive Law]} \\
&= 0 \cdot B + 0 \cdot A 
&& \text{[Complementarity Law]} \\
&= 0 + 0 = 0
\end{align*}
$$


### Step 2: Show $(A \cdot B) + (\overline{A} + \overline{B}) = 1$
$$
\begin{align*}
(A \cdot B) + (\overline{A} + \overline{B}) 
&= (A + \overline{A} + \overline{B}) \cdot (B + \overline{A} + \overline{B}) 
&& \text{[Distributive Law]} \\
&= (1 + \overline{B}) \cdot (1 + \overline{A}) 
&& \text{[Complementarity Law: } A + \overline{A} = 1] \\
&= 1 \cdot 1 = 1
\end{align*}
$$

Thus, $\overline{A \cdot B} = \overline{A} + \overline{B}$ is proven.

---

## Key Boolean Laws Used

- **Distributive Law**: $X(Y + Z) = XY + XZ$
- **Complementarity Law**: $X + \overline{X} = 1$ , $X \cdot \overline{X} = 0$
- **Identity Law**: $X \cdot 1 = X$ , $X + 0 = X$

---

## Practical Implications

De Morgan's theorems enable logic gate transformations:

- **NAND ⇔ Bubbled OR** (Theorem 1):  
    $\overline{A \cdot B} = \overline{A} + \overline{B}$  
    NAND to OR
- **NOR ⇔ Bubbled AND** (Theorem 2):  
    $\overline{A + B} = \overline{A} \cdot \overline{B}$  
    NOR to AND

These equivalences simplify circuit design by reducing component count and optimizing performance.

---

## Example Verification via Truth Table

For $A = 0, B = 1$:

- $\overline{A + B} = \overline{1} = 0$
- $\overline{A} \cdot \overline{B} = 1 \cdot 0 = 0$

All cases align, confirming the theorems.