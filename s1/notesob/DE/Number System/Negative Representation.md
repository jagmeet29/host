## Representation of Negative Numbers in Binary

There are three primary methods to represent negative numbers in binary systems, each with distinct advantages and disadvantages. Understanding these methods is crucial for computer arithmetic and digital system design.

### Sign Magnitude Representation

#### Method

In sign magnitude representation, the most significant bit (MSB) serves as the sign bit, while the remaining bits represent the magnitude (absolute value) of the number.

**Sign Bit Rules:**

- 0 = Positive number
- 1 = Negative number

#### Process

1. For positive numbers: Set sign bit to 0, followed by binary magnitude
2. For negative numbers: Set sign bit to 1, followed by binary magnitude

#### Examples (4-bit representation)

| Decimal | Sign Magnitude |
|---|---|
| +6 | 0110 |
| -6 | 1110 |
| +7 | 0111 |
| -7 | 1111 |
| +0 | 0000 |
| -0 | 1000 |

#### Range

For n-bit sign magnitude representation: $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$

| Word Size | Range                      |
| --------- | -------------------------- |
| 4 bits    | -7 to +7                   |
| 8 bits    | -127 to +127               |
| 16 bits   | -32767 to +32767           |
| 32 bits   | -2147483647 to +2147483647 |

#### Limitations

- Two representations for zero (+0 and -0), which complicates arithmetic operations
- Complex arithmetic: Addition and subtraction require different algorithms
- Inefficient storage: Requires more hardware for arithmetic operations

### 1's Complement Representation

#### Method

1's complement extends the sign magnitude concept by flipping all bits (not just the sign bit) to represent negative numbers.

**Formula**: For negative number -x in n-bit system: $-x = 2^n - x - 1$

#### Process

1. For positive numbers: Use standard binary representation
2. For negative numbers: Flip all bits of the positive representation

#### Examples (4-bit representation)

| Decimal | Binary | 1's Complement |
|---|---|---|
| +6 | 0110 | 0110 |
| -6 |  | 1001 |
| +7 | 0111 | 0111 |
| -7 |  | 1000 |
| +0 | 0000 | 0000 |
| -0 |  | 1111 |

**Verification Example**: For -12 in 8-bit system

- +12 = 00001100
- -12 = 11110011 (all bits flipped)

#### Range

For n-bit 1's complement representation: $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$

| Word Size | Range |
|---|---|
| 4 bits | -7 to +7 |
| 8 bits | -127 to +127 |
| 16 bits | -32767 to +32767 |
| 32 bits | -2147483647 to +2147483647 |

#### Limitations

- Two representations for zero (0000 and 1111 in 1111)
- Complex arithmetic: Requires end-around carry for proper addition
- Hardware complexity: More complex than 2's complement for arithmetic operations

### 2's Complement Representation

#### Method

2's complement is the most widely used method for representing signed integers in modern computers. It eliminates the problems associated with dual zero representations.

#### Process

1. For positive numbers: Use standard binary representation
2. For negative numbers: Flip all bits and add 1

$$ -x = \overline{x} + 1 $$

#### Alternative Method

Instead of flipping then adding 1, you can subtract 1 from the positive number before flipping all bits.

#### Examples (4-bit representation)

**Converting +5 to -5**:

- +5 = 0101
- Flip bits: 1010
- Add 1: 1011
- Therefore, -5 = 1011

| Decimal | 2's Complement |
|---|---|
| +7 | 0111 |
| +6 | 0110 |
| +1 | 0001 |
| +0 | 0000 |
| -1 | 1111 |
| -6 | 1010 |
| -7 | 1001 |
| -8 | 1000 |

#### Range

For n-bit 2's complement representation: $-2^{n-1}$ to $+(2^{n-1} - 1)$

| Word Size | Range |
|---|---|
| 4 bits | -8 to +7 |
| 8 bits | -128 to +127 |
| 16 bits | -32768 to +32767 |
| 32 bits | -2147483648 to +2147483647 |

#### Key Advantages

- Single zero representation
- Simplified arithmetic: Same hardware can handle signed and unsigned addition/subtraction
- Extra negative number: Can represent one additional negative number compared to other methods
- Overflow behavior: Provides predictable overflow from maximum positive to maximum negative

### Comparison Summary

| Method | Zero Representations | Range (n-bit) | Arithmetic Complexity | Usage |
|---|---|---|---|---|
| **Sign Magnitude** | Two (+0, -0) | $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$ | High | Rarely used |
| **1's Complement** | Two (0000, 1111) | $-(2^{n-1} - 1)$ to $+(2^{n-1} - 1)$ | Medium | Legacy systems |
| **2's Complement** | One (0000) | $-2^{n-1}$ to $+(2^{n-1} - 1)$ | Low | Modern computers |
**Note:** I'd recommend double-checking the formatting in a LaTeX rendering engine to ensure perfect appearance (e.g., a tool or website that supports LaTeX).  The characters within the dollar signs will be rendered as mathematical expressions.
