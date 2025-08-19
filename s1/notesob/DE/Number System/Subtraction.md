## Subtraction in Various Bases: Normal and Shortcut Methods

### Normal (Standard) Methods

#### Right-to-Left Standard Algorithm

This is the most common approach, working from the rightmost column and moving left.

**Key Principle:** When borrowing in any base $b$, you add the base value to the digit you're borrowing from.

**Example in Base 5: $421_5 - 132_5$**

```
    421₅ 
  - 132₅
  ------
    234₅
```

**Step-by-step process:**

1. **Ones place**: $1 - 2$ is impossible, so borrow from the next column.
2. **Borrowing rule**: Add the base ($5$) to the digit: $1 + 5 = 6$.
3. **Calculate**: $6 - 2 = 4$.
4. **Next column**: The borrowed-from digit becomes $1$, so $1 - 3$ requires borrowing again.
5. **Add base again**: $1 + 5 = 6$, then $6 - 3 = 3$.
6. **Final column**: $4$ becomes $3$ after borrowing, so $3 - 1 = 2$.

#### Left-to-Right Algorithm

This method postpones regrouping until the end.

**Process:**

1. Start from the leftmost column and subtract.
2. If borrowing is needed, put a "$1$" in front of the top digit.
3. Mark previous digits in the answer with a slash.
4. At the end, subtract $1$ from all marked digits.

#### Subtract from the Base Algorithm

This method ensures you never subtract from numbers larger than the base.

**Advantage:** When the bottom digit is larger than the top digit, you:

1. Regroup as in the traditional method.
2. Subtract the bottom number from the base.
3. Add the result to the top number.

### Detailed Examples by Base

#### Binary (Base 2) Subtraction

**Example: $11001_2 - 110_2$**

```
    11001₂ 
  -   110₂
   -------
     10011₂
```

**Process:**

- **Ones**: $1 - 0 = 1$.
- **Twos**: $0 - 1$ requires borrowing; $0$ becomes $2$ (base value), so $2 - 1 = 1$.
- **Fours**: After borrowing, $1$ becomes $0$, and $0 - 1$ requires more borrowing.
- **Continue pattern** following base-2 borrowing rules.

#### Base 5 Subtraction

**Example: $404_5 - 323_5$**

**Borrowing rule:** When you borrow, the digit becomes its value plus $5$.

```
    404₅ 
  - 323₅
  ------
    031₅
```

**Process:**

- **Ones**: $4 - 3 = 1$.
- **Fives**: $0 - 2$ requires borrowing; $0 + 5 = 5$, so $5 - 2 = 3$.
- **Twenty-fives**: $4$ becomes $3$ after lending, so $3 - 3 = 0$.

#### Base 8 Subtraction

**Example: $7243_8 - 4536_8$**

```
    7243₈ 
  - 4536₈
  --------
    2505₈
```

**Key point:** When borrowing, add $8$ to the digit (since base = $8$).

### Shortcut Methods

#### Method 1: Changing the Base

This mental math technique modifies the subtrahend to make calculation easier.

**Example: $55 - 39$**

1. **Change $39$ to $40$** (easier to subtract).
2. **Calculate**: $55 - 40 = 15$.
3. **Adjust**: Add back the $1$ you added to $39$.
4. **Result**: $15 + 1 = 16$.

#### Method 2: Subtraction in Parts

Break the subtrahend into convenient parts.

**Example: $144 - 95$**

1. **Break $95$ into $90 + 5$**.
2. **Calculate**: $144 - 90 = 54$.
3. **Then**: $54 - 5 = 49$.

#### Method 3: Conversion Method

For complex base calculations:

1. **Convert both numbers to base 10**.
2. **Subtract in base 10**.
3. **Convert result back to original base**.

**Example: $421_5 - 132_5$**

1. $421_5 = 4 \times 25 + 2 \times 5 + 1 = 111_{10}$.
2. $132_5 = 1 \times 25 + 3 \times 5 + 2 = 42_{10}$.
3. $111_{10} - 42_{10} = 69_{10}$.
4. Convert $69_{10}$ back to base 5: $234_5$.

### Key Rules for Any Base

#### Universal Borrowing Rule

When you need to borrow in base $b$:

- **Subtract $1$** from the digit you're borrowing from.
- **Add the base value $b$** to the digit you're borrowing to.

#### Verification Method

Always check your answer by adding the result to the subtrahend - you should get the minuend.

### Comparison of Methods

| Method                 | Best For                  | Complexity | Speed             |
| -----------------------| ------------------------- | ---------- | ---------------- |
| Right-to-Left Standard | All bases                 | Medium     | Medium            |
| Left-to-Right          | Avoiding multiple borrows | Medium     | Medium            |
| Subtract from Base     | Mental calculation        | Low        | Fast              |
| Changing Base          | Mental math in base 10    | Low        | Very fast         |
| Conversion Method      | Unfamiliar bases          | High       | Slow but reliable |
| Changing Base          | Mental math in base 10    | Low        | Very fast         |
| Conversion Method      | Unfamiliar bases          | High       | Slow but reliable |

### Common Mistakes to Avoid

1. Forgetting to adjust the base when borrowing.
2. Using base $10$ borrowing rules in other bases.
3. Not marking borrowed digits properly.
4. Forgetting to include the base notation in the final answer.

---

### Binary Subtraction Using Complement Methods

Binary subtraction using complement methods transforms subtraction operations into addition operations, making them easier to implement in digital systems. Here are both methods with examples for different conditions:

#### Binary Subtraction Using 1's Complement

**Method:** Convert subtraction $A - B$ into addition $A + (1's complement of B)$.

**Steps:**

1. Find the 1's complement of the subtrahend (number being subtracted)
2. Add it to the minuend (first number)
3. Handle the carry based on the result

**Condition 1: Result with Carry (Positive)**

Example: $28 - 19 = 9$

**Step 1:** Convert to binary

- $28_{10} = 011100_{2}$
- $19_{10} = 010011_{2}$

**Step 2:** Find 1's complement of 19

- 1's complement of $010011 = 101100$

**Step 3:** Add minuend + 1's complement

  $011100 + 101100 = 1001000$

**Step 4:** Since there's a carry, drop it and add 1 to the result

- Drop carry: $001000$
- Add 1: $001000 + 1 = 001001_{2} = 9_{10}$

**Condition 2: Result without Carry (Negative)**

Example: $101011_{2} - 111001_{2}$

**Step 1:** Find 1's complement of $111001_{2} = 000110_{2}$

**Step 2:** Add

  $101011 + 000110 = 110001$

**Step 3:** No carry exists, so take 1's complement of result for final answer

- 1's complement of $110001 = 001110$
- Result: $-001110_{2}$

#### Binary Subtraction Using 2's Complement

**Method:** Convert subtraction $A - B$ into addition $A + (2's complement of B)$.

**Steps:**

1. Find the 2's complement of the subtrahend
2. Add it to the minuend
3. Handle carry based on the result

**Finding 2's Complement:**

- First find 1's complement, then add 1
- Example: 2's complement of $101_{2} = (010 + 1) = 011_{2}$

**Condition 1: Larger Number - Smaller Number (Positive Result)**

Example: $110_{2} - 101_{2}$

**Step 1:** Find 2's complement of $101_{2}$

- 1's complement: $010_{2}$
- Add 1: $010 + 1 = 011_{2}$

**Step 2:** Add minuend + 2's complement

  $110 + 011 = 1001$

**Step 3:** Drop the carry (leftmost 1)

- Result: $001_{2}$

**Condition 2: Equal Bit Numbers with Carry**

Example: $1111_{2} - 1010_{2}$

**Step 1:** Find 2's complement of $1010_{2} = 0110_{2}$

**Step 2:** Add

  $1111 + 0110 = 10101$

**Step 3:** Drop carry to get $0101_{2}$

**Condition 3: Result without Carry (Negative)**

When there's no carry in 2's complement subtraction, the result represents a negative number, and you take the 2's complement of the sum to get the magnitude of the negative result.

#### Key Differences

**1's Complement:**

- When carry exists: drop carry and add 1 to result
- When no carry: take 1's complement of result (negative)

**2's Complement:**

- When carry exists: simply drop the carry
- When no carry: take 2's complement of result for negative value
- More commonly used in computer systems as it's simpler

Both methods ensure all numbers use the same bit width by padding with leading zeros when necessary.