Python has two types of types conversion:
## Implicit (automatic)

```python 
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

'''
Value: 124.23
Data Type: <class 'float'>
'''
```

As you can see that python converted `int` to `float`. This is because python always try to convert a smaller data type to larger one to preserve the information.

## Explicit or Typecasting 

Have to ever tried adding `int` and `string`, if yes then you must have got `type error`. Because Python is not able to convert them.

This problem is solved by Explicit conversions which is also called Typecasting because in this we cast (change) one value to an other.

>[!important] Explicit Conversion may result in loss of information 

```python 
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))


'''
Data type of num_string before Type Casting: <class 'str'>
Data type of num_string after Type Casting: <class 'int'>
Sum: 35
Data type of num_sum: <class 'int'>
'''
```


```python
num1 = int(2.3)
print(num1)  # prints 2

num2 = int(-2.8)
print(num2)  # prints -2

num3 = float(5)
print(num3) # prints 5.0

num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)
```

>[!note] You can use `type()` function to find the type and the class of the variable

