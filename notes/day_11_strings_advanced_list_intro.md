# Day 11 — Advanced String Functions & List Introduction

← [Day 10](day_10_strings_functions.md) | [Index](00_INDEX.md) | [Day 12](day_12_lists.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | What does `strip()` remove? | Both leading (left) and trailing (right) characters |
| 2 | What does `lstrip()` do? | Removes leading (left) characters only |
| 3 | What does `rstrip()` do? | Removes trailing (right) characters only |
| 4 | `find()` vs `index()` when substring is absent? | `find()` returns `-1`; `index()` raises `ValueError` |
| 5 | What does `rindex()` return? | Highest index (last occurrence) of substring |
| 6 | What does `partition()` return? | A **tuple** — (before, separator, after) at first occurrence |
| 7 | `partition()` vs `split()` return type? | `partition()` → tuple; `split()` → list |
| 8 | What does `isdigit()` check? | All characters are digits (0–9) |
| 9 | What does `isalpha()` check? | All characters are alphabetic (a–z, A–Z) |
| 10 | `isalnum()` vs `isalpha()`? | `isalnum()` allows both letters and digits; `isalpha()` letters only |

---

## 1. Strip Functions

Remove unwanted characters (spaces, custom chars) from string edges.

```python
s = "  DurgaSoft  "

print(s.strip())     # "DurgaSoft"   — removes both sides
print(s.lstrip())    # "DurgaSoft  " — removes left only
print(s.rstrip())    # "  DurgaSoft" — removes right only
```

### Custom character stripping

```python
s = "aaaDurgaSoftaaa"

print(s.strip("a"))    # "DurgaSoft"   — removes 'a' from both sides
print(s.lstrip("a"))   # "DurgaSoftaaa"
print(s.rstrip("a"))   # "aaaDurgaSoft"
```

| Function | Removes from |
|----------|-------------|
| `strip(x)` | Both sides |
| `lstrip(x)` | Left (leading) only |
| `rstrip(x)` | Right (trailing) only |

---

## 2. `len()` — Length

Universal function — works on every data structure.

```python
s = "DurgaSoft"
print(len(s))       # 9

s2 = "Durga Soft"
print(len(s2))      # 10  — space is also a character
```

---

## 3. `find()` and `index()`

Both locate a substring. The difference is what happens when the substring is **not found**.

```python
s = "python is very easy and it is object oriented"

print(s.find("easy"))    # 15 — first occurrence index
print(s.find("xyz"))     # -1 — NOT found → returns -1
print(s.index("easy"))   # 15 — same result when found
# print(s.index("xyz")) # ValueError: substring not found
```

### `rindex()` — last occurrence

```python
s = "python is very easy and it is object oriented"

print(s.index("is"))     # 7   — first occurrence
print(s.rindex("is"))    # 27  — last (highest) occurrence
```

| Method | Found | Not Found |
|--------|-------|-----------|
| `find()` | Returns index | Returns `-1` |
| `index()` | Returns index | Raises `ValueError` |
| `rindex()` | Returns last index | Raises `ValueError` |

---

## 4. `max()` and `min()` — ASCII-based

Return the character with the highest/lowest ASCII value in the string.

```python
s = "DurgaSoft"
print(max(s))   # u  — highest ASCII value in the string
print(min(s))   # D  — lowest ASCII value (uppercase letters < lowercase)

# To see ASCII value of a character:
print(ord("A"))   # 65
print(ord("a"))   # 97
print(ord("u"))   # 117  — u has highest value in "Durga"
```

**ASCII order:** uppercase letters (65–90) < lowercase letters (97–122)

---

## 5. `partition()` — Split into Tuple

Splits string at the **first occurrence** of the separator and returns a **tuple** of 3 parts:
`(before_separator, separator, after_separator)`

```python
s = "python is very easy and it is object oriented"

result = s.partition("is")
print(result)        # ('python ', 'is', ' very easy and it is object oriented')
print(type(result))  # <class 'tuple'>
```

### `partition()` vs `split()`

```python
s = "python is very easy and it is object oriented"

# partition: first occurrence only, returns tuple, separator included
print(s.partition("is"))
# ('python ', 'is', ' very easy and it is object oriented')

# split: all occurrences, returns list, separator NOT included
print(s.split("is"))
# ['python ', ' very easy and ', ' object oriented']
```

| Feature | `partition()` | `split()` |
|---------|--------------|-----------|
| Split at | First occurrence only | All occurrences |
| Return type | Tuple (always 3 parts) | List |
| Separator in result | Yes (middle element) | No |

---

## 6. `startswith()` and `endswith()`

Return `True` or `False`.

```python
s = "DurgaSoft"

print(s.startswith("D"))       # True
print(s.startswith("d"))       # False — case-sensitive!
print(s.startswith(" "))       # False — if s had leading space, True

print(s.endswith("ft"))        # True
print(s.endswith("Soft"))      # True
print(s.endswith(" "))         # False
```

---

## 7. `isdigit()`, `isalpha()`, `isalnum()`

All return `True` or `False`. ALL characters must match.

```python
# isdigit — all must be digits 0–9
print("12345".isdigit())    # True
print("123a5".isdigit())    # False — 'a' is not a digit
print("1 2".isdigit())      # False — space not allowed

# isalpha — all must be letters a–z or A–Z
print("Python".isalpha())   # True
print("Python3".isalpha())  # False — digit present
print("Py thon".isalpha())  # False — space not allowed

# isalnum — letters AND/OR digits (no spaces, no special chars)
print("Python3".isalnum())  # True
print("Python3!".isalnum()) # False — ! is special character
print("123".isalnum())      # True — digits only is also OK
```

| Method | True when |
|--------|-----------|
| `isdigit()` | All characters are digits |
| `isalpha()` | All characters are letters |
| `isalnum()` | All characters are letters or digits (both allowed, spaces NOT) |

---

## 8. Other Identification Methods

```python
s = "hello"
print(s.islower())       # True — all lowercase
print(s.isupper())       # False

s2 = "HELLO"
print(s2.isupper())      # True
print(s2.islower())      # False

# isidentifier — valid Python variable name?
print("empID".isidentifier())    # True
print("7empID".isidentifier())   # False — starts with digit
print("emp ID".isidentifier())   # False — space not allowed
```

---

## 9. Introduction to List

A **list** is an ordered, mutable collection that allows duplicate values and mixed types.

```python
fruits  = ["apple", "banana", "cherry"]
mixed   = [10, 3.14, "hello", True, None]
numbers = [1, 5, 3, 2, 4]
nested  = [10, 20, ["Durga", "Soft"], 30]
```

### Indexing

```python
L = [10, 20, 30, 40, 50]

print(L[0])     # 10   — positive index
print(L[-1])    # 50   — negative index
print(L[1])     # 20
# print(L[11])  # IndexError: list index out of range
```

### Nested list indexing

```python
L = [10, 20, ["Durga", "Soft"], 40]

print(L[2])        # ['Durga', 'Soft']
print(L[2][0])     # Durga  — nested access: outer index, inner index
print(L[2][1])     # Soft
print(L[2][-1])    # Soft   — negative works too
```

### Slicing

```python
L = [10, 20, 30, 40, 50]

print(L[1:3])     # [20, 30]  — same as string slicing
print(L[:3])      # [10, 20, 30]
print(L[2:])      # [30, 40, 50]
print(L[::-1])    # [50, 40, 30, 20, 10]  — reversed
```

---

## 10. Adding Elements to a List

```python
L = [10, 20, 30, 40, 50]

# Method 1: Assignment — REPLACES existing value
L[1] = 33
print(L)   # [10, 33, 30, 40, 50]  — 20 replaced by 33

# Method 2: insert() — INSERTS without replacing (shifts others right)
L.insert(1, 33)
print(L)   # [10, 33, 20, 30, 40, 50]  — 20 still there, shifted

# Method 3: append() — adds ONE item at the END
L.append(60)
print(L)   # [..., 60]

# Method 4: extend() — adds MULTIPLE items at the END
L.extend([70, 80, 90])
print(L)   # [..., 70, 80, 90]
```

| Method | Adds | Where | Replaces? |
|--------|------|-------|-----------|
| `L[i] = val` | One item | At index `i` | Yes |
| `insert(i, val)` | One item | At index `i` | No (shifts) |
| `append(val)` | One item | End | No |
| `extend([...])` | Multiple items | End | No |

---

## 11. Removing Elements from a List

```python
L = [10, 20, 30, 40, 50]

# remove() — removes by VALUE (first occurrence)
L.remove(20)
print(L)   # [10, 30, 40, 50]

# pop() — removes by INDEX (default: last element)
L.pop(2)   # removes index 2 (value 40)
print(L)   # [10, 30, 50]

# clear() — empties the list (list still exists)
L.clear()
print(L)   # []

# del — deletes the entire list object
L = [1, 2, 3]
del L
# print(L)   # NameError: name 'L' is not defined
```

| Method | Removes by | List still exists? |
|--------|-----------|-------------------|
| `remove(val)` | Value | Yes |
| `pop(index)` | Index | Yes |
| `clear()` | All (empties) | Yes (empty) |
| `del L` | Entire list | No |

---

## 12. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ValueError: substring not found` | Using `index()` with missing substring | Use `find()` instead |
| `IndexError: list index out of range` | Accessing list index that doesn't exist | Check `len(L)` first |
| `TypeError: unhashable type: 'list'` | Using list as dict key or in a set | Use tuple instead |

---

## 13. Interview Questions

1. What is the difference between `find()` and `index()`?
2. What is the difference between `partition()` and `split()`?
3. What does `strip()` do? How is it different from `lstrip()` and `rstrip()`?
4. What does `isalnum()` return when the string contains a space?
5. What is the difference between `append()` and `extend()`?
6. What is the difference between `remove()` and `pop()`?
7. What does `del L` do versus `L.clear()`?
8. What does `L.insert(i, val)` do to existing values at index `i`?

---

## 14. Try It Yourself

```python
# 1. Take s = "  hello world  "
#    Print it with: left spaces removed, right spaces removed, both removed

# 2. s = "Python Programming"
#    Find index of "gram", check if "Java" is present using find() safely

# 3. s = "data123"
#    Check: isdigit, isalpha, isalnum — predict before running

# 4. s = "python is fun and it is easy"
#    Use partition("is") and split("is") — compare the outputs

# 5. L = [3, 1, 4, 1, 5, 9, 2, 6]
#    Remove first 1 (by value), remove item at index 2, append 99, extend with [10, 20]
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `s.strip(" ")` | Remove spaces from both sides |
| `s.find("easy")` | Returns index or -1 |
| `s.index("easy")` | Returns index or ValueError |
| `s.rindex("is")` | Last occurrence index |
| `s.partition("is")` | Tuple: (before, sep, after) |
| `"123".isdigit()` | All digits check |
| `"abc".isalpha()` | All letters check |
| `"abc123".isalnum()` | Letters or digits check |
| `L[2][0]` | Nested list access |
| `L.insert(1, 33)` | Insert without replacing |
| `L.append(60)` | Add one item to end |
| `L.extend([70, 80])` | Add multiple to end |
| `L.remove(20)` | Remove by value |
| `L.pop(2)` | Remove by index |
