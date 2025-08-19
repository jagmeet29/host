### Case Sensitivity

**Verilog** is **case-sensitive**, so `var_a` and `var_A` are different. All lines should be terminated by a semi-colon.

### Comments

There are two ways to write comments in **Verilog**:

1.  A **single line** comment starts with `//` and tells the **Verilog** compiler to treat everything after this point to the end of the line as a comment.
2.  A **multiple-line** comment starts with `/*` and ends with `*/` and cannot be nested.

However, single line comments can be nested in a multiple line comment.

```verilog
// This is a single line comment.

integer a;   // Creates an int variable called a, and treats everything to the right of // as a comment;

/*
This is a
multiple-line or
block comment
*/;

/* This is /*
an invalid nested
block comment */
*/;

/* However,
// this one is okay
*/;

// This is also okay.
///////////// Still okay.
```

### Whitespace

**Whitespace** is a term used to represent the characters for spaces, tabs, newlines, and formfeeds, and is usually ignored by **Verilog** except when it separates **tokens**. In fact, this helps in the indentation of code to make it easier to read.

```verilog
module dut;              // 'module' is a keyword,
                         // 'dut' is an identifier.
reg [8*6:1] name = "Hello!";   // The 2 spaces in the beginning are ignored.
```

However, blanks (spaces) and tabs (from TAB key) are not ignored in **strings**. In the example below, the **string** variable called `addr` gets the value `"Earth "` because of preservation of spaces in **strings**.

```verilog
   // There is no space in the beginning of this line,
   // but there's a space in the string.
   reg [8*6:1] addr = "Earth ";
endmodule;
```

### Operators

There are three types of **operators**: **unary**, **binary**, and **ternary** or **conditional**.

-   **Unary operators** shall appear to the left of their operand.
-   **Binary operators** shall appear between their operands.
-   **Conditional operators** have two separate operators that separate three operands.

```verilog
x = ~y;                // ~ is a unary operator, and y is the operand.
x = y | z;             // | is a binary operator, where y and z are its operands.
x = (y > 5) ? w : z;   // ?: is a ternary operator, and the expression (y>5), w and z are its operands.
```

If the expression `(y > 5)` is true, then variable `x` will get the value in `w`, else the value in `z`.

### Identifiers

**Identifiers** are names of variables so that they can be referenced later on. They are made up of alphanumeric characters `[a-z][A-Z][0-9]`, underscores `_` or dollar sign `$` and are **case sensitive**. They cannot start with a digit or a dollar sign.

```verilog
integer var_a;        // Identifier contains alphabets and underscore -> Valid.
integer $var_a;       // Identifier starts with $ -> Invalid.
integer v$ar_a;       // Identifier contains alphabets and $ -> Valid.
integer 2var;         // Identifier starts with a digit -> Invalid.
integer var23_g;      // Identifier contains alphanumeric characters and underscore -> Valid.
integer 23;           // Identifier contains only numbers -> Invalid.
```

### Keywords

**Keywords** are special **identifiers** reserved to define the language constructs and are in lower case. A list of important **keywords** is given below.

![[Identifiers.png]]
### Numbers and Radix.

We are most familiar with numbers being represented as **decimals**. However, numbers can also be represented in **binary**, **octal**, and **hexadecimal**. By default, **Verilog** simulators treat numbers as **decimals**. In order to represent them in a different **radix**, certain rules have to be followed.

The decimal number $16$ can be represented in various bases:

-   $16$ (decimal).
-   $0x10$ (hexadecimal).
-   $10000$ (binary).
-   $20$ (octal).

#### Sized Numbers

**Sized numbers** are represented as shown below, where **size** is written only in decimal to specify the number of bits in the number.

```verilog
[size]'[base_format][number]
```

-   **base_format** can be either decimal (`'d` or `'D`), hexadecimal (`'h` or `'H`), and octal (`'o` or `'O`) and specifies what base the **number** part represents.
-   **number** is specified as consecutive digits from $0, 1, 2 \dots 9$ for decimal **base_format** and $0, 1, 2 \dots 9, A, B, C, D, E, F$ for **hexadecimal**.

```verilog
3'b010;     // size is 3, base format is binary ('b), and the number is 010 (indicates value 2 in binary).
3'd2;       // size is 3, base format is decimal ('d) and the number is 2 (specified in decimals).
8'h70;      // size is 8, base format is hexadecimal ('h) and the number is 0x70 (in hex) to represent decimal 112.
9'h1FA;     // size is 9, base format is hexadecimal ('h) and the number is 0x1FA (in hex) to represent decimal 506.

4'hA = 4'd10 = 4'b1010 = 4'o12;	// Decimal 10 can be represented in any of the four formats.
8'd234 = 8'D234;                 // Legal to use either lower case or upper case for base format.
32'hFACE_47B2;                  // Underscore (_) can be used to separate 16 bit numbers for readability.
```

Uppercase letters are legal for **number specification** when the **base format** is **hexadecimal**.

```verilog
16'hcafe;         // lowercase letters Valid.
16'hCAFE;         // uppercase letters Valid.
32'h1D40_CAFE;    // underscore can be used as separator between 4 letters Valid.
```

Numbers without a **base_format** specification are **decimal numbers** by **default**. Numbers without a **size** specification have a **default number of bits** depending on the type of simulator and machine.

```verilog
integer a = 5423;       // base format is not specified, a gets a decimal value of 5423.
integer a = 'h1AD7;     // size is not specified, because a is int (32 bits) value stored in a = 32'h0000_1AD7.
```


#### Negative Numbers

**Negative numbers** are specified by placing a minus `-` sign before the **size** of a number. They stored in 2's complement form in Verilog. It is illegal to have a minus sign between **base format** and **number**.

```verilog
-6'd3;            // 8-bit negative number stored as two's complement of 3.
-6'sd9;           // For signed maths.
8'd-4;            // Illegal.
```


>[!question] What will be the decimal value of `-8'b1`?
>>[!success]- Answer
>>`00000001` → `11111110` (1's complement)
>>`11111110` → `11111111` (adding 1 as 2's complement)
>>-128

#### Verilog Padding Rules

For **Numeric Literals** (Constants):

- If the **MSB** (leftmost bit) is `x` or `z`, that value (`x` or `z`) will be used to pad the remaining bits to the left.
- If the **MSB** is `0` or `1`, zeros will be used to pad the remaining bits to the left.
- **Unsigned** values get zero-padded regardless of content
- **Negative values** are padded which ones because of 2'complement. 

## Additional Notes

Regarding `?` and `_`:

- `?` can be used as a wildcard in case statements (equivalent to `x`).
- `_` is used as a separator for readability in numbers (e.g., `32'b1010_1100_1111_0000`).

### Strings.

A sequence of characters enclosed in a double quote `" "` is called a **string**. It cannot be split into multiple lines and every character in the **string** takes $1$-byte to be stored.

```verilog
"Hello World!";        // String with 12 characters -> require 12 bytes.
"x + z";               // String with 5 characters.

"How are you
feeling today ?";      // Illegal for a string to be split into multiple lines.
```

