Verilog provides a comprehensive set of operators for digital design and hardware description. Here's a complete overview of all operator categories with practical examples.

## Arithmetic Operators

Verilog arithmetic operators perform mathematical operations on operands.

|Operator|Description|Operands|
|---|---|---|
|+|Addition|2|
|-|Subtraction|2|
|*|Multiplication|2|
|/|Division|2|
|%|Modulus|2|
|**|Exponentiation|2|

**Example:**

```verilog
module arithmetic_op;
  reg [3:0] i1, i2;
  initial begin
    i1 = 4'h6;  // 6 in hex
    i2 = 4'h2;  // 2 in hex
    $display("Add: %0h", i1 + i2);  // Output: 8
    $display("Sub: %0h", i1 - i2);  // Output: 4
    $display("Mul: %0h", i1 * i2);  // Output: c (12 in hex)
    $display("Div: %0h", i1 / i2);  // Output: 3
    $display("Pow: %0h", i2 ** 3);  // Output: 8
    $display("Mod: %0h", i1 % i2);  // Output: 0
  end
endmodule
```

## Relational Operators

Relational operators compare two operands and return 1 (true) or 0 (false).

|Operator|Description|
|---|---|
|>|Greater than|
|>=|Greater than or equal|
|<|Less than|
|<=|Less than or equal|
|==|Equal to|
|!=|Not equal to|

**Example:**

```verilog
module relational_op;
  reg [3:0] i1, i2;
  initial begin
    i1 = 4'h6; i2 = 4'h2;
    $display("i1 > i2: %h", i1>i2);   // Output: 1
    $display("i1 >= i2: %h", i1>=i2); // Output: 1
    $display("i1 < i2: %h", i1<i2);   // Output: 0
    $display("i1 <= i2: %h", i1<=i2); // Output: 0
  end
endmodule
```

## Case Equality Operators

Verilog has **four equality operators**:

|Operator|Name|Description|
|---|---|---|
|==|Logical equality|Returns X if either operand contains X or Z|
|!=|Logical inequality|Returns X if either operand contains X or Z|
|===|Case equality|Compares X and Z as distinct values|
|!==|Case inequality|Compares X and Z as distinct values|
### Key Differences with Examples

**Logical Equality (`==`, `!=`):**

```verilog
module logical_equality;
  reg [3:0] a, b;
  initial begin
    a = 4'b101x;
    b = 4'b101x;
    if (a == b)
      $display("Equal");
    else
      $display("Not equal"); // This will execute because of X
    // Result of (a == b) is X (unknown), treated as false in if condition
  end
endmodule
```

**Case Equality (`===`, `!==`):**

```verilog
module case_equality;
  reg [3:0] a, b;
  initial begin
    a = 4'b101x;
    b = 4'b101x;
    if (a === b)
      $display("Case equal"); // This WILL execute
    else
      $display("Case not equal"); // This will NOT execute
    // X and Z values are compared bit-by-bit as distinct values
  end
endmodule
```
## Logical Operators

Logical operators work with Boolean expressions and are used to combine conditions.

| Operator | Description |
| -------- | ----------- |
| &&       | Logical AND |
| \| \|    | Logical OR  |
| !        | Logical NOT |

**Example:**

```verilog
// Logical operators return 1 (true) or 0 (false)
result = (a > b) && (c < d);  // Both conditions must be true
result = (a == b) || (c == d); // Either condition can be true
result = !(a > b);             // Negation of the condition
```

## Bitwise Operators

Bitwise operators perform bit-by-bit operations on operands.

| Operator | Description  |
| -------- | ------------ |
| &        | Bitwise AND  |
| \|       | Bitwise OR   |
| ^        | Bitwise XOR  |
| ~&       | Bitwise NAND |
| ~\|      | Bitwise NOR  |
| ~^       | Bitwise XNOR |
| ~        | Bitwise NOT  |

**Example:**

```verilog
wire [3:0] a, b, c;
assign a = 4'b1010;
assign b = 4'b1100;
assign c = a & b;  // Result: 4'b1000
```

## Reduction Operators

Reduction operators take a multi-bit input and produce a single-bit output by performing the operation across all bits.

| Operator | Description    |
| -------- | -------------- |
| &        | Reduction AND  |
| \|       | Reduction OR   |
| ^        | Reduction XOR  |
| ~&       | Reduction NAND |
| ~\|      | Reduction NOR  |
| ~^       | Reduction XNOR |

**Example:**

```verilog
module reduction_operators();
  reg r_C;
  initial begin
    $display("AND Reduction of 4'b1101 is: %b", &4'b1101);  // Output: 0
    $display("AND Reduction of 4'b1111 is: %b", &4'b1111);  // Output: 1
    $display("OR Reduction of 4'b1101 is: %b", |4'b1101);   // Output: 1
    $display("OR Reduction of 4'b0000 is: %b", |4'b0000);   // Output: 0
    $display("XOR Reduction of 4'b1101 is: %b", ^4'b1101);  // Output: 1
    r_C = |4'b0010;  // Store reduction result
    $display("Stored reduction result: %b", r_C);  // Output: 1
  end
endmodule
```

## Shift Operators

Shift operators move bits left or right by a specified number of positions.

|Operator|Description|
|---|---|
|<<|Logical left shift|
|>>|Logical right shift|
|<<<|Arithmetic left shift|
|>>>|Arithmetic right shift|

**Example:**

```verilog
module shift_op;
  reg [7:0] i1, o1;
  reg signed [7:0] i2, o2;
  initial begin
    // Logical shift
    i1 = 8'b1111_0000;
    o1 = i1 >> 3;  // Result: 00011110
    o1 = i1 << 3;  // Result: 00011110
    // Arithmetic shift (preserves sign bit)
    i2 = 8'b1111_0000;
    o2 = i2 >>> 3;  // Result: 01111110
    o2 = i2 <<< 3;  // Result: 10000000
  end
endmodule
```

## Conditional Operator

The conditional or ternary  operator provides a compact way to select between two values.

|Operator|Description|Operands|
|---|---|---|
|?:|Conditional|3|

**Syntax:** `result = condition ? true_expression : false_expression`

**Example:**

```verilog
module conditional_op;
  reg [3:0] i1, i2, result;
  initial begin
    i1 = 4'h6; i2 = 4'h2;
    result = (i1 > i2) ? 1 : 0;  // Result: 1
    i1 = 4'h6; i2 = 4'h6;
    result = (i1 > i2) ? 1 : 0;  // Result: 0
  end
endmodule
```

## Concatenation and Replication

**Concatenation operator `{}`:** Joins multiple signals together

```verilog
wire [7:0] result = {a[3:0], b[3:0]};  // Combine two 4-bit values
```

**Replication operator `{n{value}}`:** Creates multiple copies

```verilog
wire [7:0] result = {4{2'b10}};  // Result: 8'b10101010
```

These operators form the foundation of Verilog hardware description and are essential for digital system design, providing the building blocks for complex logic implementations and arithmetic operations.