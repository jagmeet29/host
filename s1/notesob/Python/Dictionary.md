A Python dictionary is a collection of items stored as **key-value pairs**. While similar to other collection types like lists and tuples, a dictionary's structure is based on a unique key that corresponds to a specific value.

## Creating and Structuring a Dictionary

You can create a dictionary by enclosing a comma-separated series of `key: value` pairs within curly brackets `{}`. The built-in function `dict()` can also be used for creation.

```python
# creating a dictionary
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}
print(country_capitals)
# Output: {'Germany': 'Berlin', 'Canada': 'Ottawa', 'England': 'London'}
```

Key characteristics of dictionary structure include:

- **Keys must be immutable**: Keys must be of an immutable data type, such as strings, integers, or tuples. Using a mutable object like a list as a key will result in an error.
- **Values can be any data type**: The values in a dictionary can be of any data type, including mutable types like lists.
- **Keys must be unique**: If a dictionary is created with duplicate keys, the value associated with the last instance of that key will overwrite any previous ones.

## Basic Operations

Since dictionaries are mutable, you can modify them after they are created.

### Accessing Items
You can retrieve the value of an item by placing its key inside square brackets `[]`. The `get()` method can also be used for this purpose.

```python
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa"
}
print(country_capitals["Germany"])
# Output: Berlin
```

### Adding and Changing Items
To add a new item, you can assign a value to a new key. To change an existing item's value, you refer to its key and assign a new value. The `update()` method can also be used to add or change items.

```python
# Add an item
country_capitals["Italy"] = "Rome"
print(country_capitals)
# Output: {'Germany': 'Berlin', 'Canada': 'Ottawa', 'Italy': 'Rome'}

# Change an item
country_capitals["Italy"] = "Venice"
print(country_capitals)
# Output: {'Germany': 'Berlin', 'Canada': 'Ottawa', 'Italy': 'Venice'}
```

### Removing Items
You can remove a specific key-value pair using the `del` statement or the `pop()` method. To remove all items from a dictionary at once, use the `clear()` method.

```python
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa"
}
# Delete an item
del country_capitals["Germany"]
print(country_capitals)
# Output: {'Canada': 'Ottawa'}

# Clear the entire dictionary
country_capitals.clear()
print(country_capitals)
# Output: {}
```

## Additional Functionality

- **Iteration**: As of Python 3.7, dictionaries are ordered, meaning they maintain the insertion order of items. You can iterate through a dictionary's keys using a `for` loop, which allows you to access the corresponding values.
- **Length**: The `len()` function returns the number of key-value pairs in a dictionary.
- **Membership Testing**: The `in` and `not in` operators can check if a specific key exists within a dictionary. These operators do not check for the existence of values.

```python
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
}
print(".pdf" in file_types)
# Output: True
print(".jpg" in file_types)
# Output: False
```

## Common Dictionary Methods

Python provides several built-in methods for working with dictionaries.

| Method | Description |
|---|---|
| `pop()` | Removes the item associated with a specified key. |
| `update()` | Adds or changes dictionary items. |
| `clear()` | Removes all items from the dictionary. |
| `keys()` | Returns a view object displaying all the dictionary's keys. |
| `values()` | Returns a view object displaying all the dictionary's values. |
| `get()` | Returns the value for a specified key. |
| `popitem()` | Removes and returns the last inserted key-value pair as a tuple. |
| `copy()` | Returns a shallow copy of the dictionary. |
