# Day 12 — Lists (Complete) & Tuple

← [Day 11](day_11_strings_advanced_list_intro.md) | [Index](00_INDEX.md) | [Day 13](day_13_sets.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | How do you sort a list in ascending order? | `L.sort()` |
| 2 | How do you sort in descending order? | `L.sort(reverse=True)` |
| 3 | Shallow copy vs deep copy? | Shallow: changes in one affect the other; Deep (`.copy()`): independent |
| 4 | What does `L.count(val)` return? | Number of times `val` appears in `L` |
| 5 | What does `L.index(val)` return? | Index of first occurrence of `val` |
| 6 | How to create a list from range? | `list(range(start, stop, step))` |
| 7 | Tuple creation syntax? | `(1, 2, 3)` — round brackets (optional) |
| 8 | Single-element tuple requires? | Trailing comma: `(10,)` not `(10)` |
| 9 | Is a tuple mutable? | No — immutable (cannot add, remove, or change) |
| 10 | What is tuple packing? | Assigning multiple variables into one tuple: `t = a, b, c` |

---

## 1. `sort()` — Sort a List

`sort()` modifies the list **in place**. It does not return a new list.

```python
L = [5, 1, 7, 6, 4, 3, 9, 2, 2]

# Ascending (default)
L.sort()
print(L)   # [1, 2, 2, 3, 4, 5, 6, 7, 9]

# Descending
L.sort(reverse=True)
print(L)   # [9, 7, 6, 5, 4, 3, 2, 2, 1]
```

---

## 2. Shallow Copy vs Deep Copy

### Shallow copy — `L1 = L`

Both names point to the **same object**. Changes in one affect the other.

```python
L  = [1, 2, 3, 4, 5, 8]
L1 = L             # shallow copy — same object

L.remove(8)
print(L)    # [1, 2, 3, 4, 5]
print(L1)   # [1, 2, 3, 4, 5]  ← also changed!

L1.append(18)
print(L)    # [1, 2, 3, 4, 5, 18]  ← L is also affected
```

### Deep copy — `L1 = L.copy()`

Creates a **separate, independent** copy.

```python
L  = [1, 2, 3, 4, 5]
L1 = L.copy()      # deep copy — independent object

L1.append(18)
print(L)    # [1, 2, 3, 4, 5]   — unchanged
print(L1)   # [1, 2, 3, 4, 5, 18]

L.remove(4)
print(L)    # [1, 2, 3, 5]
print(L1)   # [1, 2, 3, 4, 5, 18]  — unchanged
```

| Copy type | Method | Independent? |
|-----------|--------|-------------|
| Shallow | `L1 = L` | No — changes affect both |
| Deep | `L1 = L.copy()` | Yes — fully independent |

---

## 3. `count()` and `index()`

```python
L = [10, 20, 30, 40, 10, 20, 10]

# count — how many times a value appears
print(L.count(10))    # 3
print(L.count(20))    # 2
print(L.count(100))   # 0  — not present = 0 (no error)

# index — first occurrence of value
print(L.index(10))    # 0  — first 10 is at index 0
print(L.index(30))    # 2
# print(L.index(100)) # ValueError: 100 is not in list
```

---

## 4. Create List from User Input

### Fixed number of items

```python
L = []

item1 = int(input("Enter integer: "))
item2 = input("Enter string: ")
item3 = float(input("Enter float: "))

L.append(item1)
L.append(item2)
L.append(item3)
print(L)

# OR use extend for all at once:
L.extend([item1, item2, item3])
```

### Variable number of items (user decides length)

```python
L = []
n = int(input("Enter length of list: "))

for i in range(n):
    x = input("Enter value: ")
    L.append(x)

print(L)   # print OUTSIDE the loop — not inside!
```

> **Key rule:** Print the final list **outside** the loop. Printing inside prints partial lists every iteration.

---

## 5. Create List from `range()`

```python
# Method 1: list() around range()
L1 = list(range(10))         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 = list(range(2, 10))      # [2, 3, 4, 5, 6, 7, 8, 9]
L3 = list(range(2, 10, 3))   # [2, 5, 8]
print(L1, L2, L3)
```

---

## 6. List — Complete Method Summary

| Method | Purpose |
|--------|---------|
| `append(val)` | Add one item to end |
| `extend([...])` | Add multiple items to end |
| `insert(i, val)` | Insert at index `i` (no replace) |
| `remove(val)` | Remove first occurrence of value |
| `pop(i)` | Remove by index (default: last) |
| `clear()` | Empty the list |
| `sort()` | Sort in place (ascending default) |
| `sort(reverse=True)` | Sort descending |
| `copy()` | Deep copy |
| `count(val)` | Count occurrences |
| `index(val)` | First occurrence index |
| `len(L)` | Number of elements |

---

## 7. Tuple

A **tuple** is an ordered, **immutable** collection that allows duplicate values.

```python
# Creating tuples
t1 = (10, 20, 30)           # with round brackets
t2 = 10, 20, 30             # brackets are optional!
t3 = ()                      # empty tuple
t4 = (10,)                   # single-element tuple — comma required!
t5 = 10,                     # also single-element tuple

print(type(t1))   # <class 'tuple'>
print(type(t2))   # <class 'tuple'>
print(type((10))) # <class 'int'>   — NO comma = just int!
print(type((10,)))# <class 'tuple'> — comma makes it tuple
```

### Indexing and slicing

```python
t = ("a", 10, True, 3.14, "b", None, 20)

print(t[0])      # a
print(t[-1])     # 20
print(t[1:4])    # (10, True, 3.14)
print(t[::-1])   # reversed tuple
```

### Tuples are immutable

```python
t = (10, 20, 30)
# t[0] = 99   # TypeError: 'tuple' object does not support item assignment

# But you CAN delete the whole tuple:
del t
# print(t)   # NameError: name 't' is not defined
```

---

## 8. Tuple Operations

### Concatenation and multiplication

```python
t1 = (10, 20)
t2 = ("a", "b")
t3 = (True, False)

print(t1 + t2 + t3)   # (10, 20, 'a', 'b', True, False)
print(t1 * 3)         # (10, 20, 10, 20, 10, 20)
```

### `count()` and `index()`

```python
t = (10, 20, 10, 20, 10)

print(t.count(10))   # 3
print(t.count(20))   # 2
print(t.index(20))   # 1  — first occurrence
```

### `len()`, `max()`, `min()`, `sum()`

```python
t = (-10, 5.5, 3, 100, -7.2)

print(len(t))    # 5
print(max(t))    # 100
print(min(t))    # -10
print(sum(t))    # 91.3
print(sum(t, 9)) # 100.3  — adds extra value of 9
```

### Membership test

```python
t = (10, 20, 30, 40, 50)

print(30 in t)         # True
print(100 in t)        # False
print(100 not in t)    # True
```

---

## 9. Type Conversion

```python
# String → Tuple (each character becomes an element)
s = "DurgaSoft"
t = tuple(s)
print(t)   # ('D', 'u', 'r', 'g', 'a', 'S', 'o', 'f', 't')

# List → Tuple
L = [10, 20, 30, 40]
t = tuple(L)
print(t)   # (10, 20, 30, 40)

# Tuple → List
t = (1, 2, 3)
L = list(t)
print(L)   # [1, 2, 3]
```

---

## 10. Tuple Packing and Unpacking

### Packing — store individual variables into a tuple

```python
a = 10
b = 20
c = 30

t = a, b, c       # packing: individual values → tuple
print(t)          # (10, 20, 30)
print(type(t))    # <class 'tuple'>
```

### Unpacking — extract tuple values into individual variables

```python
t = (10, 20, 30)

a, b, c = t       # unpacking: tuple → individual variables
print(a)   # 10
print(b)   # 20
print(c)   # 30
```

> **Same concept as multiple assignment** `x, y = y, x` — Python uses tuple packing/unpacking internally.

---

## 11. List vs Tuple

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | Yes | No (immutable) |
| Ordered | Yes | Yes |
| Duplicates | Yes | Yes |
| When to use | Data that changes | Fixed data (coordinates, DB records) |
| Speed | Slower | Faster |
| Methods | Many (sort, append, etc.) | Only `count()`, `index()` |

---

## 12. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: 'tuple' object does not support item assignment` | Modifying a tuple | Use a list instead |
| `(10)` is not a tuple | Missing trailing comma | Write `(10,)` |
| Printing inside the loop | Shows partial lists each iteration | Move `print` outside the loop |
| `L.sort()` returns `None` | `sort()` modifies in place, returns nothing | Don't assign: `L.sort()` not `L = L.sort()` |

---

## 13. Interview Questions

1. What is the difference between `append()` and `extend()`?
2. What is the difference between shallow copy and deep copy?
3. What does `L.sort(reverse=True)` do?
4. What is the difference between a list and a tuple?
5. How do you create a single-element tuple?
6. What is tuple packing and unpacking?
7. Can you modify a tuple? Can you delete one?
8. What does `tuple("Python")` produce?

---

## 14. Try It Yourself

```python
# 1. L = [5, 3, 8, 1, 9, 2, 7, 4, 6]
#    Print sorted ascending, sorted descending, original (hint: use copy before sort)

# 2. L = [1, 2, 3, 1, 2, 1]
#    Find: how many times 1 appears, index of first 2, index of first 1

# 3. Accept 5 numbers from user at runtime, store in list, print sorted

# 4. t = ("Python", 3.10, True, "Python", 42)
#    Print: length, max by index, count of "Python", index of 42

# 5. a, b, c = 100, 200, 300
#    Pack into tuple, print it. Then unpack back to x, y, z, print each.
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `L.sort()` | Sort ascending in place |
| `L.sort(reverse=True)` | Sort descending |
| `L1 = L` | Shallow copy (same object) |
| `L1 = L.copy()` | Deep copy (independent) |
| `L.count(10)` | Count occurrences |
| `L.index(30)` | First occurrence index |
| `list(range(2, 10, 3))` | List from range |
| `t = a, b, c` | Tuple packing |
| `a, b, c = t` | Tuple unpacking |
| `tuple("Durga")` | String to tuple |
| `tuple([1,2,3])` | List to tuple |
