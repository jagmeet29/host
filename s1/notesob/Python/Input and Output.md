## Python Output

Python `print()` function has 5 parameters:
- **object** - value(s) to be printed
- **sep** (optional) -  to separate multiple **objects** inside `print()`.
- **end** (optional) - to add add specific values like new line `"\n"`, tab `"\t"`
- **file** (optional) - where the values are printed. It's default value is `sys.stdout` (screen)
- **flush** (optional) - boolean specifying if the output is flushed or buffered. Default: `False`

### Concatenation

Concatenation can be done inside print statement using `+`.

```python
print('Programiz is ' + 'awesome.')

'''print('Programiz is ' + 'awesome.')'''
```

### Output formatting

Output can be formatted using `str.format()` method.

```python
x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))
```

## Python Input

We can use `input()` method to get input. We can also give input string which will be displayed to get the input which is optional.

>[!important] The return type of input is always a string. It must be type casted to convert it into `int` or `folat`. 

```python 
# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))

'''
Enter a number: 10
You Entered: 10
Data type of num: <class 'str'>
'''
```

