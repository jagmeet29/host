In Python, a **literal** is a fixed value that is represented directly in the source code. These values are used to define data that will be directly used by the program without requiring computation or input.

For example, in the statement:

```python
val = 'string_s'
```

`'string_s'` is a string literal.

Python supports various types of literals, each representing a specific data type:

### 1. Numeric Literals

Represent numerical values.

*   **a. Integer Literals:** Whole numbers without a decimal point.
    *   *Examples:* `20`, `9`, `-100`
*   **b. Floating-Point Literals:** Numbers with a decimal point or in exponential form.
    *   *Examples:* `0.9`, `0.59`, `3.14`, `1.2e5`
*   **c. Complex Number Literals:** Numbers of the form `a+bj`, where `a` is the real part and `b` is the imaginary part.
    *   *Example:* `2+3j`, `-1.5+0j`

### 2. String Literals

Sequences of characters enclosed in single (`' '`), double (`" "`), or triple (`''' '''` or `""" """`) quotes. Triple-quoted strings can span multiple lines.

*   *Examples:* `'hello world'`, `"Python"`, `'''multi-line string'''`
*   *Note:* Python does not have a separate "character literal" type; a single character enclosed in quotes is simply a string literal of length one (e.g., `'C'` is a string literal).

### 3. Boolean Literals

Represent truth values. There are only two boolean literals:

*   `True`: Represents logical truth.
*   `False`: Represents logical falsity.

### 4. Special Literal (`None`)

Represents the absence of a value or a null value. It is a unique constant of the `NoneType` data type.

*   *Example:* `my_variable = None`

### 5. Collection Literals

Used to create instances of built-in collection types.

*   **a. List Literals:** Ordered, mutable sequences of items, enclosed in square brackets `[]`.
    *   *Example:* `['apple', 'banana', 'cherry']`
*   **b. Tuple Literals:** Ordered, immutable sequences of items, enclosed in parentheses `()`.
    *   *Example:* `(1, 2, 3)`
*   **c. Set Literals:** Unordered collections of unique items, enclosed in curly braces `{}`.
    *   *Example:* `{'red', 'green', 'blue'}`
*   **d. Dictionary Literals:** Unordered collections of key-value pairs, enclosed in curly braces `{}`.
    *   *Example:* `{'name': 'Alice', 'age': 30}`
