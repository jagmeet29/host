# Ripple Carry Subtractor

![[Riplesub.png|500]]
## Concept of Two's Complement Subtraction

In digital electronics, subtraction $A - B$ is performed by **adding $A$ to the two's complement of $B$**.

- **Two's complement of $B$** = Invert all bits of $B$ ($\overline{B}$) + 1.
- This converts subtraction into addition: $A−B=A+(\overline{B}+1)$

---

## Building a Subtractor Using Full Adders

A **ripple carry subtractor** can be implemented using full adders with minor modifications:

### Circuit Design

1. **Invert $B$**: Use XOR gates to invert each bit of $B$.

    - XOR acts as a programmable inverter:

        - When subtraction mode is enabled (via a control signal $\text{SUB} = 1$), $B$ is inverted.
        - For addition ($\text{SUB} = 0$), $B$ remains unchanged.

        $B_{\text{inverted}}=B \oplus \text{SUB}$
2. **Add 1**: Set the carry-in ($C_{\text{in}}$) of the least significant bit (LSB) to 1 during subtraction.

    - This completes the $\overline{B} + 1$ operation.
3. **Ripple Carry Structure**: Connect full adders in series, like a ripple carry adder, but with inverted $B$ and $C_{\text{in}} = 1$.

Ripple Carry Subtractor Diagram
_(Conceptual diagram: Full adders with XOR gates and $C_{\text{in}} = 1$)_

---

### Step-by-Step Example: $5 - 3$ (4-bit)

1. **Convert to Binary**:

    - $A = 0101$, $B = 0011$.
    - Two's complement of $B$: $\overline{B} = 1100$, then $\overline{B} + 1 = 1101$.
2. **Perform Addition**:

    $0101 \ (5) + 1101 \ (-3) = \underbrace{1}_{C_{\text{out}}} \ 0010 \ (2)$
    - **Result**: $0010$ (2) with carry-out $C_{\text{out}} = 1$.
    - **Ignore $C_{\text{out}}$**: In two's complement arithmetic, the final carry is discarded.

---

### Key Equations for Full Adders

For each bit position $i$:

1. **Sum**: $S_i=A_i \oplus B_i \oplus C_{\text{in},i}$
2. **Carry-Out**: $C_{\text{out},i} = (A_i \cdot \overline{B_i}) + (C_{\text{in},i} \cdot (A_i \oplus \overline{B_i}))$

---

## Advantages & Limitations

| Advantages                                   | Limitations                                   |
| -------------------------------------------- | --------------------------------------------- |
| Reuses full adder hardware for subtraction  | Propagation delay (same as ripple adder)      |
| Simple design with minimal components        | Requires additional XOR gates for $B$-inversion |
| Works for both signed and unsigned numbers | Final carry must be discarded                  |

---

## Real-World Applications

1. **Arithmetic Logic Units (ALUs)**: Perform both addition and subtraction with the same circuit.
2. **Microcontrollers**: Execute arithmetic operations in embedded systems.
3. **Binary Multipliers/Dividers**: Used in complex arithmetic circuits.

---

By leveraging two's complement and full adders, this design efficiently converts subtraction into addition, minimizing hardware complexity while maintaining computational accuracy.