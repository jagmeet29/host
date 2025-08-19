Precedence is the concept which tells us which operation will be perfumed first if there are a number of operators working other in a statement.

Give bellow is the precedence of the python operators in descending order:

|Operators|Meaning|
|---|---|
|`()`|Parentheses|
|`**`|Exponent|
|`+x`, `-x`, `~x`|Unary plus, Unary minus, Bitwise NOT|
|`*`, `/`, `//`, `%`|Multiplication, Division, Floor division, Modulus|
|`+`, `-`|Addition, Subtraction|
|`<<`, `>>`|Bitwise shift operators|
|`&`|Bitwise AND|
|`^`|Bitwise XOR|
|`\|`|Bitwise OR|
|`==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in`|Comparisons, Identity, Membership operators|
|`not`|Logical NOT|
|`and`|Logical AND|
|`or`|Logical OR|

# Associativity

Associativity helps us determine the order of operation will be performed first if both have the same priority.

>[!note] Exponent operator `**` has right-to-left associativity in Python.

## Non Associative Operator 

Assignment and comparison operator has not priority in python.

>[!note] while chaining of assignments like `x = y = z = 1` is perfectly valid, `x = y = z+= 2` will result in error.

