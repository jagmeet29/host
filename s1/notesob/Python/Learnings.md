# Loops with Lists

```python
# Assume X, Y, Z, and N are the integer inputs
X, Y, Z, N = 1, 1, 1, 2

# The list comprehension generates and filters the coordinates
result = [[x, y, z] 
for x in range(X + 1) 
for y in range(Y + 1) 
for z in range(Z + 1) 
if x + y + z != N]

print(result)
# Expected Output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```
##### Is Equivalent To

```python
result = []
for x in range(X + 1):
    for y in range(Y + 1):
        for z in range(Z + 1):
            if x + y + z != N:
                result.append([x, y, z])

```

# Making Array From Spaced Input

```python
arr = map(int, input().split())
```
# List Sorting

```python
sorted(listName)
```

# Duplicates Removal in List

Use Type casting to `set()` 

# Smalless or Largest Value

`-float('inf')`

Here `inf` stands for Infinity

# Iterable Unpacking

```python
name, *line = input().split()
scores = list(map(float, line))
```

- `name` gets the **first item** from the split input (usually a student's name).
- `*line` collects **all the remaining items** into a list (usually the scores).