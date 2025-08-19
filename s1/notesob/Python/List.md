# Python Lists and Their Methods

Python lists are **mutable, ordered collections** that can store elements of different data types. Lists are one of the most versatile and commonly used data structures in Python, supporting a wide range of built-in methods for manipulation and processing.

## Python List Methods

Here's a comprehensive table of all Python list methods with descriptions and examples:

| Method | Description | Syntax | Example |
|---|---|---|---|
| `append()` | Adds a single element to the end of the list | `list.append(element)` | `lst = [1, 2, 3]` <br> `lst.append(4)` → `[1, 2, 3, 4]` |
| `clear()` | Removes all elements from the list | `list.clear()` | `lst = [1, 2, 3]` <br> `lst.clear()` → `[]` |
| `copy()` | Returns a shallow copy of the list | `list.copy()` | `lst = [1, 2, 3]` <br> `new_lst = lst.copy()` → `[1, 2, 3]` |
| `count()` | Returns the number of times a specified element appears in the list | `list.count(element)` | `lst = [1, 2, 2, 3]` <br> `lst.count(2)` → $2$ |
| `extend()` | Adds elements from another iterable to the end of the current list | `list.extend(iterable)` | `lst = [1, 2]` <br> `lst.extend([3, 4])` → `[1, 2, 3, 4]` |
| `index()` | Returns the index of the first occurrence of a specified element | `list.index(element)` | `lst = [1, 2, 3, 2]` <br> `lst.index(2)` → $1$ |
| `insert()` | Inserts an element at a specified position | `list.insert(index, element)` | `lst = [1, 3, 4]` <br> `lst.insert(1, 2)` → `[1, 2, 3, 4]` |
| `pop()` | Removes and returns the element at the specified position (or last element if no index specified) | `list.pop([index])` | `lst = [1, 2, 3, 4]` <br> `lst.pop(1)` → returns $2$, list becomes `[1, 3, 4]` |
| `remove()` | Removes the first occurrence of a specified element | `list.remove(element)` | `lst = [1, 2, 3, 2]` <br> `lst.remove(2)` → `[1, 3, 2]` |
| `reverse()` | Reverses the order of elements in the list | `list.reverse()` | `lst = [1, 2, 3]` <br> `lst.reverse()` → `[3, 2, 1]` |
| `sort()` | Sorts the list in ascending order (by default) | `list.sort(key=None, reverse=False)` | `lst = [3, 1, 2]` <br> `lst.sort()` → `[1, 2, 3]` |

## Common List Functions

These built-in Python functions work with lists but are not methods of the list object:

| Function | Description | Syntax | Example |
|---|---|---|---|
| `len()` | Returns the number of items in the list | `len(list)` | `lst = [1, 2, 3]` <br> `len(lst)` → $3$ |
| `max()` | Returns the largest item in the list | `max(list)` | `lst = [1, 2, 3]` <br> `max(lst)` → $3$ |
| `min()` | Returns the smallest item in the list | `min(list)` | `lst = [1, 2, 3]` <br> `min(lst)` → $1$ |
| `sum()` | Returns the sum of all items in the list | `sum(list)` | `lst = [1, 2, 3]` <br> `sum(lst)` → $6$ |
| `list()` | Creates a list from an iterable | `list(iterable)` | `s = "abc"` <br> `lst = list(s)` → `['a', 'b', 'c']` |

## Key Points to Remember

- **In-place operations**: Methods like `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `reverse()`, `sort()`, and `clear()` modify the original list and return `None`.
- **Return values**: Methods like `copy()`, `count()`, `index()`, and `pop()` return values without modifying the original list structure.
- **Error handling**: Methods like `index()` and `remove()` raise `ValueError` if the element is not found in the list.

These methods provide powerful tools for **list manipulation**, making Python lists extremely versatile for data processing and storage operations.