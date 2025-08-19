# Base Conversion Methods and Advanced Binary Conversion Shortcut

---

## 1. Normal (Standard) Conversion Methods

### Converting from Any Base to Decimal (Base 10)

Use positional notation: multiply each digit by the base raised to its positional power.

**Formula:**
For a number $d_n d_{n-1} ... d_1 d_0$ in base $b$:

$d_n \times b^n + d_{n-1} \times b^{n-1} + ... + d_1 \times b^1 + d_0 \times b^0$

**Examples:**

- $6028 = 6 \times 8^2 + 0 \times 8^1 + 2 \times 1 = 386_{10}$
- $53617 = 5 \times 7^3 + 3 \times 7^2 + 6 \times 7^1 + 1 \times 1 = 1905_{10}$
- $F3EA7_{16} = 15 \times 16^4 + 3 \times 16^3 + 14 \times 16^2 + 10 \times 16^1 + 7 \times 1 = 1040687_{10}$

---

### Converting from Decimal to Any Base

Use repeated division by the target base and record remainders.

**Algorithm:**

1. Divide the decimal number by the target base.
2. Record the remainder.
3. Divide the quotient by the base again.
4. Repeat until the quotient becomes zero.
5. The base-converted number is the remainders read in reverse order.

**Example: Convert 236 to base 5**

$236 \div 5 = 47 \text{ remainder } 1$
$47 \div 5 = 9 \text{ remainder } 2$
$9 \div 5 = 1 \text{ remainder } 4$
$1 \div 5 = 0 \text{ remainder } 1$

Reading remainders backwards: $1421_5$

---

### Converting Between Two Non-Decimal Bases

Two-step process:

1. Convert source base to decimal.
2. Convert decimal to target base.

**Example: Convert $1627_7$ to base 8**

$1627_7 = 1 \times 7^3 + 6 \times 7^2 + 2 \times 1 = 343 + 294 + 2 = 639_{10}$

$639_{10} = 1357_8$

---

## 2. Shortcut Methods for Bases That Are Powers of Each Other

### Binary ↔ Octal Conversion (Base 2 and Base 8)

Since $8 = 2^3$, group binary digits into sets of 3 (from right).

**Example:** $1011010011111_2$

Group: $(1 \ 011)(010)(011)(111)$

Convert each group to an octal digit.

### Binary ↔ Hexadecimal Conversion (Base 2 and Base 16)

Since $16 = 2^4$, group binary digits into sets of 4.

**Example:** $11110112111101121111011_2$

Group and pad as needed, then convert each group to hex digits.

---

## 3. Advanced Binary Conversion Shortcut: Consecutive 1s Formula

### Core Formula

A string of $n$ consecutive 1s = $2^n - 1$

This simplifies adding powers of two for consecutive 1s.

---

### Why It Works

Binary consecutive 1s represent a geometric series:

$111_2 = 2^2 + 2^1 + 2^0 = 7 = 2^3 - 1$

---

### Basic Examples

| Binary | Number of 1s | Formula   | Decimal |
| ------ | ------------ | --------- | ------- |
| 1      | 1            | $2^1 - 1$ | 1       |
| 11     | 2            | $2^2 - 1$ | 3       |
| 111    | 3            | $2^3 - 1$ | 7       |
| 1111   | 4            | $2^4 - 1$ | 15      |
| 11111  | 5            | $2^5 - 1$ | 31      |

---

### Verification Example

For $11111_2$:

Sum of powers: $16 + 8 + 4 + 2 + 1 = 31$

Using shortcut: $2^5 - 1 = 32 - 1 = 31$

---

### Advanced Applications

#### Non-Starting Consecutive 1s

Identify the position of the consecutive 1s, apply the formula, and multiply by the power of two corresponding to the starting position.

**Example:** $1011100_2$

Three consecutive 1s at positions 2, 3, 4 (0-indexed from right)

Value: $(2^3 - 1) \times 2^2 = 7 \times 4 = 28$

Add remaining bits: $1 \times 2^6 + 1 \times 2^1 = 64 + 2 = 66$

Total = $28 + 66 = 94$

#### Multiple Groups of Consecutive 1s

Break binary into groups of consecutive 1s, calculate each, and sum.

---

### Pattern Recognition Shortcuts

| Pattern | Value |
|---|---|
| $n$ consecutive 1s followed by $m$ zeros | $(2^n - 1) \times 2^m$ |
| All ones (length $n$) | $2^n - 1$ |
| Single 1 followed by $n$ zeros | $2^n$ |

---

### Practical Example

Binary $11110000_2$ (4 ones followed by 4 zeros):

$(2^4 - 1) \times 2^4 = 15 \times 16 = 240$

---

## 4. Comparison of Methods and Time Complexity

| Method | Best For | Time Complexity | Example |
|---|---|---|---|
| Standard via Decimal | Any base conversion | Medium $O(n)$ | $1627_7 \to 639_{10} \to 1357_8$ |
| Direct Grouping (Shortcut) | Powers of 2 (2, 16) | Low $O(1)$ | Binary to Hex conversion |
| Division Method | Decimal to any base | Medium $O(n)$ | $236_{10} \to 1421_5$ |
| Positional Expansion | Any base to decimal | Low $O(n)$ | $6028 \to 386_{10}$ |
| Consecutive 1s Formula | Long binary strings of 1s | Very Low $O(1)$ per group | $11111_2 = 31_{10}$ |

---

## 5. Key Advantages

### Normal Methods

- Universal: Work for any bases
- Systematic and easy to understand
- Reliable for all conversions

### Shortcut Methods

- Faster for compatible bases (powers of each other)
- Reduce calculation errors
- Crucial in computer science and digital systems for efficiency

### Consecutive 1s Formula

- Drastically reduces calculation for long runs of 1s in binary
- Enables quick mental math and error checking
- Highly valuable in analyzing digital circuits and systems
