# Python Console Output Formatting Methods

Python provides multiple ways to format output in the console, each with its own advantages and use cases. Here are all the primary methods available:

## F-Strings (Formatted String Literals)

**F-strings are the most modern and recommended approach** for string formatting in Python $3.6+$. They offer excellent readability and performance:

```python
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")
print(f"Total cost: ${49.95 * 3:.2f}")  # Supports expressions
```

F-strings support expressions, function calls, and format specifiers directly within the curly braces.

## The `.format()` Method

The `.format()` method provides flexible string formatting and works with older Python versions:

```python
# Basic usage
print("Hello, {}!".format("World"))

# Multiple placeholders
print("{} is {} years old.".format("Bob", 30))

# Named placeholders
print("{name} is {age} years old.".format(name="Charlie", age=35))

# Number formatting with precision
print("Formatted Number: {:.2f}".format(123.4567))  # Output: 123.46
```

The format method supports **positional arguments**, **keyword arguments**, and **detailed formatting options** such as alignment, width, and precision.

## String Modulo Operator (%)

The **% operator** provides printf-style formatting, which is considered legacy but still widely used:

```python
name = "David"
age = 40
print("My name is %s and I'm %d years old." % (name, age))

# With padding and alignment
print('%03d %5.2f' % (5, 22/7.0))  # Output: 005  3.14
```

Common format specifiers include:
- `%s` for strings
- `%d` for integers
- `%f` for floats
- `%c` for characters

## String Concatenation

Simple concatenation using the `+` operator for basic string joining:

```python
name = "Mark"
age = 37
print("Hi " + name + " your age is " + str(age) + " years")
```

**Note**: This method requires converting non-string variables to strings using `str()`.

## Print Function with Multiple Arguments

Using **comma-separated arguments** in the `print` function:

```python
name = "Mark"
age = 37
print("Hi", name, "your age is", age, "years")
```

## Customizing Print Behavior

The `print` function accepts several parameters for output control:

- `sep`: Changes the separator between arguments
- `end`: Modifies what appears at the end of the line
- `file`: Directs output to a file instead of console

```python
print("a", "b", "c", sep="-")           # Output: a-b-c
print("Hello", end="")                  # No newline at end
print("Hi", name, "your age is", age, "years", sep="\n")  # Each on new line
```

## String Alignment Methods

Python provides **built-in string methods** for alignment and padding:

```python
text = "Python"
print("'{:>10}'".format(text))     # Right-align: '    Python'
print("'{:<10}'".format(text))     # Left-align: 'Python    '
print("'{:^10}'".format(text))     # Center-align: '  Python  '

# Using string methods directly
print(text.rjust(10))              # Right-justify
print(text.ljust(10))              # Left-justify
print(text.center(10))             # Center
```

## Template Strings

The `string.Template` class provides a simpler alternative for basic substitution:

```python
from string import Template
template = Template("Hello $name, you are $age years old.")
print(template.substitute(name="Alice", age=30))
```

## Advanced Formatting Options

### Number Formatting

```python
number = 1234.5678
print(f"{number:,.2f}")           # Comma separator: 1,234.57
print(f"{number:>10.2f}")         # Right-aligned with width: '   1234.57'
print(f"{number:0>10.2f}")        # Zero-padded: '001234.57'
```

### Percentage and Scientific Notation

```python
value = 0.1234
print(f"{value:.2%}")             # Percentage: 12.34%
print(f"{value:.2e}")             # Scientific: 1.23e-01
```

## Pretty Printing for Data Structures

For **complex data structures**, use the `pprint` module:

```python
import pprint
data = {'name': 'Alice', 'scores': [95, 87, 92], 'info': {'age': 25, 'city': 'NYC'}}
pprint.pprint(data)
```

## File Output

**Direct output to files** using the `file` parameter:

```python
with open('output.txt', 'w') as f:
    print("This is written to a file.", file=f)
```

## Best Practices

1.  **Use f-strings for Python $3.6+$** - they're the most readable and efficient.
2.  **Use `.format()` for older Python versions** or when you need more complex formatting logic.
3.  **Avoid % formatting** for new code unless maintaining legacy systems.
4.  **Choose the right method** based on your specific formatting needs and Python version requirements.

Each method has its place depending on your Python version, complexity requirements, and personal preference, but **f-strings** are generally recommended for modern Python development.
