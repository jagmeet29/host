## `for` Loop

### Looping Throw List, Strings, etc

```python
languages = ['Swift', 'Python', 'Go']

# access elements of the list one by one
for lang in languages:
    print(lang)

'''
Swift
Python
Go
'''
```

### Looping With `range()` Function

```python
# iterate from i = 0 to i = 3
for i in range(0, 4):
    print(i)

'''
0
1
2
3
'''
```

#### For Looping Without Assessing Sequence 

```python
# iterate from i = 0 to 3
for _ in range(0, 4:
    print('Hi')

'''
0
1
2
3
'''
```

## `while` Loop

```python
number = 1

while number <= 3:
    print(number)
    number = number + 1

'''
1
2
3
'''
```

### `while` loop with `else`

```python
counter = 0

while counter  <  2:
    print('This is inside loop')
    counter = counter + 1
else:
    print('This is inside else block')

'''
This is inside loop
This is inside loop
This is inside else block
'''
```

>[!note] The `else` block will not execute if the `while` loop is terminated by a `break` statement.
## Loops Support

 1. `break`- exits the loop.
 2. `continue`- exits the current iteration of loop.
 3. `pass`- for function or loop with is not yet implemented.
 4. Nested Loops are also supported.
 
