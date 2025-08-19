```python
if condition1:
    # code block 1

elif condition2:
    # code block 2

else: 
    # code block 3
```

- ## Compact `if`
  id:: 689a3520-7699-4740-bb11-71d7a181108f
  
  ```python
  number = 10
  
  if number > 0: print('Positive')
  ```
- ## Ternary Operator like 
  
  Python does not have a ternary operator so if statement can be used as it.
  
  ```python
  grade = 40
  
  result = 'pass' if number >= 50 else 'fail'
  
  print(result)
  ```
- ## Multiple Conditions
  
  Multiple conditions can be used with `and`, `or`.
  
  ```python
  age = 35
  salary = 6000
  
  # add two conditions using and operator
  if age >= 30 and salary >= 5000:
    print('Eligible for the premium membership.')
  else:
    print('Not eligible for the premium membership')
  ```