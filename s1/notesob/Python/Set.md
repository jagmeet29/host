## What are Sets?

A **set** is an unordered collection of **unique elements** in Python. Sets are **mutable**, but they can only contain **immutable** (hashable) objects like numbers, strings, and tuples.

## Key Characteristics

- **Unordered**: Elements have no defined order
- **Unique**: No duplicate elements allowed
- **Mutable**: Can add/remove elements after creation
- **Iterable**: Can loop through elements

## Creating Sets

### Empty Set

```python
empty_set = set()  # Note: {} creates a dictionary, not a set
```

### Set with Elements

```python
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14}
```

### From Other Iterables

```python
list_to_set = set([1, 2, 2, 3, 3, 4])  # Result: {1, 2, 3, 4}
string_to_set = set("hello")  # Result: {'h', 'e', 'l', 'o'}
```

## Common Set Operations

### Adding Elements

```python
fruits = {"apple", "banana"}
fruits.add("orange")        # Add single element
fruits.update(["grape", "mango"])  # Add multiple elements
```

### Removing Elements

```python
fruits.remove("apple")      # Raises KeyError if not found
fruits.discard("apple")     # No error if not found
popped = fruits.pop()       # Remove and return arbitrary element
fruits.clear()              # Remove all elements
```

### Checking Membership

```python
"apple" in fruits           # True/False
"apple" not in fruits       # True/False
```

## Set Mathematical Operations

### Union (|)

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2           # {1, 2, 3, 4, 5}
union_set = set1.union(set2)      # Same result
```

### Intersection (&)

```python
intersection = set1 & set2        # {3}
intersection = set1.intersection(set2)  # Same result
```

### Difference (-)

```python
difference = set1 - set2          # {1, 2}
difference = set1.difference(set2)  # Same result
```

### Symmetric Difference (^)

```python
sym_diff = set1 ^ set2            # {1, 2, 4, 5}
sym_diff = set1.symmetric_difference(set2)  # Same result
```

## Useful Set Methods

```python
# Size and emptiness
len(my_set)                 # Number of elements
bool(my_set)                # False if empty, True otherwise

# Subset/Superset checks
set1.issubset(set2)         # Is set1 ⊆ set2?
set1.issuperset(set2)       # Is set1 ⊇ set2?
set1.isdisjoint(set2)       # No common elements?

# Copy
new_set = my_set.copy()     # Shallow copy
```

## Frozen Sets

**Immutable** version of sets:

```python
frozen = frozenset([1, 2, 3, 4]) # Cannot add/remove elements, but can use in other sets or as dict keys
```

## Common Use Cases

### Remove Duplicates

```python
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))  # [1, 2, 3, 4, 5]
```

### Find Common Elements

```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)    # {3, 4}
```

### Check if Lists Have Same Elements

```python
list1 = [1, 2, 3]
list2 = [3, 2, 1]
same_elements = set(list1) == set(list2)  # True
```

## Performance Notes

- Set operations are generally **$O(1)$** for add, remove, and membership testing
- Much faster than lists for checking if an element exists
- Use sets when you need **unique elements** and **fast lookups**

## Important Reminders

- Sets cannot contain **mutable objects** (lists, dictionaries, other sets)
- **Order is not preserved** (use `dict.fromkeys()` if you need ordered unique elements)
- **Cannot access elements by index** - sets are not subscript able

## Built-in Functions with Set

| Function     | Description                                                                                          |
| ------------- | ---------------------------------------------------------------------------------------------------- |
| all()        | Returns `True` if all elements of the set are true (or if the set is empty).                         |
| any()       | Returns `True` if any element of the set is true. If the set is empty, returns `False`.              |
| enumerate() | Returns an enumerate object. It contains the index and value for all the items of the set as a pair. |
| len()       | Returns the length (the number of items) in the set.                                                 |
| max()       | Returns the largest item in the set.                                                                 |
| min()       | Returns the smallest item in the set.                                                                |
| sorted()    | Returns a new sorted list from elements in the set(does not sort the set itself).                    |
| sum()       | Returns the sum of all elements in the set.                                                          |
