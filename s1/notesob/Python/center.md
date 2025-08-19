# Python String `.center()` Method

The `.center()` method is a built-in string method in Python that returns a centered string within a specified **width**, padded with a specified character (or spaces by default).

## Syntax

`string.center(width, fillchar)`

## Parameters

| Parameter  | Type | Required | Description                                                         |
| :--------- | :--- | :------- | :------------------------------------------------------------------ |
| `width`    | int  | Yes      | The total **width** of the returned string                          |
| `fillchar` | str  | No       | Character to use for padding (default is space `' '`)               |

## Return Value

Returns a **new string** that is centered within the specified **width**. The original string remains **not modified**.

## Basic Examples

### Simple Centering with Spaces

```python
text = "Hello"
centered = text.center(15)
print(f"'{centered}'")  # Output: '     Hello     '
print(len(centered))     # Output: 15
```

### Centering with Custom Fill Character

```python
text = "WELCOME"
centered = text.center(21, '-')
print(centered)  # Output: -------WELCOME-------
```

### Different Fill Characters

```python
word = "Python"
print(word.center(12, '*'))  # Output: ***Python***
print(word.center(14, '='))  # Output: ====Python====
print(word.center(16, '.'))  # Output: .....Python.....
```

## Advanced Usage

### Centering in Different Scenarios

```python
# For even padding (when (width - len(string)) is even)
text = "Hi"
print(text.center(8, '-'))  # Output: ---Hi---
# For odd padding (when (width - len(string)) is odd)
text = "Hi"
print(text.center(9, '-'))  # Output: ---Hi---- (Note: Extra character goes to the right side)
```

### Working with Numbers

```python
number = "42"
print(number.center(10, '0'))  # Output: 0000420000
```

### Multi-character Fill (Error Case)

```python
text = "Hello"
# This will raise TypeError
try:
    text.center(15, "ab")
except TypeError as e:
    print(f"Error: {e}")  # Error: The fill character must be exactly one character long
```

## Edge Cases and Behavior

### When Width is Less Than or Equal to String Length

```python
text = "Hello World"
print(text.center(5))   # Output: Hello World (no change)
print(text.center(11))  # Output: Hello World (no change)
print(text.center(15))  # Output:   Hello World   (padded)
```

### Empty String Handling

```python
empty = ""
print(f"'{empty.center(10, '*')}'")  # Output: '**********'
```

### Single Character Fill Only

```python
text = "Test"
# Valid
print(text.center(10, '#'))  # Output: ###Test###
# Invalid - will raise TypeError
# text.center(10, "##")  # TypeError!
```

## Practical Use Cases

### Creating Headers and Banners

```python
title = "REPORT"
width = 50
print(title.center(width, '='))
print("Content goes here".center(width))
print("=" * width)
```

Output:

```text
======================REPORT======================
                 Content goes here                 
==================================================
```

### Formatting Table Headers

```python
headers = ["Name", "Age", "City"]
col_width = 15
for header in headers:
    print(header.center(col_width), end=" | ")
print()
print("-" * (col_width * 3 + 6))
```

### Creating Menu Systems

```python
def create_menu(options, width=30):
    print("=" * width)
    print("MENU".center(width))
    print("=" * width)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}".center(width))
    print("=" * width)
create_menu(["Start Game", "Settings", "Exit"])
```

### Progress Indicators

```python
def show_progress(current, total, width=40):
    progress = f"{current}/{total}"
    filled = int(width * current / total)
    bar = "█" * filled + "░" * (width - filled)
    print(f"[{bar}] {progress.center(10)}")
show_progress(7, 10)
```

## Door Mat Pattern Example (From Previous Code)

In the door mat code, `.center()` was used to create the WELCOME line:

```python
# M is the total width (27 in the example)
print('WELCOME'.center(M, '-')) # Output: ----------WELCOME----------
```

This centers "WELCOME" within 27 characters using dashes as padding.

## Related String Methods

### Comparison with Similar Methods

```python
text = "Hello"
width = 15
# Left-aligned
print(text.ljust(width, '-'))   # Output: Hello----------
# Right-aligned   
print(text.rjust(width, '-'))   # Output: ----------Hello
# Centered
print(text.center(width, '-'))  # Output: -----Hello-----
```

### Method Chaining

```python
text = "python"
result = text.upper().center(20, '*')
print(result)  # Output: *******PYTHON*******
```

## Performance Notes

-   `.center()` creates a **new string** object.
-   Original string is **not modified** (strings are **immutable** in Python).
-   For large strings or frequent operations, consider performance implications.
-   Memory usage increases with the specified **width**.

## Common Mistakes to Avoid

1.  **Using multiple characters as fill**: Only **single characters** are allowed. This will raise a **TypeError**.
2.  **Forgetting that strings are immutable**: `.center()` returns a **new string**.
3.  **Not handling edge cases**: When `width` is less than or equal to string length, the original string is returned (no padding).
4.  **Assuming symmetric padding**: For odd padding, the extra space goes to the right side.

The `.center()` method is particularly useful for creating formatted output, ASCII art, reports, and user interfaces where visual alignment is important.