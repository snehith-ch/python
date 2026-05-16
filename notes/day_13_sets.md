# Day 13 — Sets & Dictionaries (Complete)

← [Day 12](day_12_lists.md) | [Index](00_INDEX.md) | [Day 14](day_14_bytes_frozenset.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | How to create an empty set? | `set()` — NOT `{}` (that's an empty dict) |
| 2 | `add()` vs `update()` on set? | `add()` adds one item; `update()` adds multiple |
| 3 | `discard()` vs `remove()` when value missing? | `discard()` — silent (no error); `remove()` — KeyError |
| 4 | What does union return? | All unique values from both sets combined |
| 5 | What does intersection return? | Only values common to BOTH sets |
| 6 | What does difference return? | Values in A that are NOT in B |
| 7 | What does symmetric difference return? | Unique values from both, EXCLUDING common values |
| 8 | `d[key]` vs `d.get(key)` when key missing? | `d[key]` → KeyError; `d.get(key)` → None |
| 9 | Dictionary membership test works on? | Keys only — not values |
| 10 | What does `popitem()` remove? | The last inserted key-value pair |

---

## PART A — SETS

---

## 1. Set Basics

```python
# Creating a set — curly braces with values
s = {10, 20, 30, 40, 50}
print(s)        # order NOT guaranteed: e.g. {40, 10, 20, 30, 50}
print(type(s))  # <class 'set'>

# Sets ignore duplicates automatically
s2 = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(s2)   # {1, 2, 3, 4, 5, 6, 9}  — duplicates removed, unordered

# Different types in one set
s3 = {10, "hello", True, 3.14, None}

# Empty set — MUST use set() function
empty = set()
print(type(empty))   # <class 'set'>
print(type({}))      # <class 'dict'>  ← this is a dict, NOT a set!
```

### Set properties

| Property | Value |
|----------|-------|
| Ordered | No |
| Mutable | Yes |
| Duplicates | Not allowed |
| Indexing | Not possible (no index) |
| Empty syntax | `set()` |

---

## 2. Adding to a Set

```python
s = {10, 20, 30}

# add() — one item at a time
s.add(45)
print(s)   # {45, 10, 20, 30}  — inserted anywhere (unordered)

# update() — multiple items at once
s.update([23, 67, 77.7])   # requires iterable (square brackets)
print(s)   # contains all original + 23, 67, 77.7
```

| Method | Adds | How many |
|--------|------|---------|
| `add(val)` | One item | 1 at a time |
| `update([...])` | Multiple items | Many at once |

---

## 3. Removing from a Set

```python
s = {10, 20, 30, 40, 50}

# discard() — removes value, NO error if not found
s.discard(10)
print(s)           # {20, 30, 40, 50}

s.discard(100)     # 100 not in set — no error, returns None
print(s)           # unchanged

# remove() — removes value, raises KeyError if not found
s.remove(20)
print(s)           # {30, 40, 50}

# s.remove(100)   # KeyError: 100

# clear() — empties the set (set still exists)
s.clear()
print(s)           # set()
```

| Method | Error if missing? |
|--------|-----------------|
| `discard(val)` | No — silent |
| `remove(val)` | Yes — KeyError |
| `clear()` | Empties set |

---

## 4. Set Operations (Mathematical)

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
```

### Union — all unique values from both sets

```python
print(A | B)             # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))        # same result
```

### Intersection — values common to BOTH sets

```python
print(A & B)             # {4, 5}
print(A.intersection(B)) # same result
```

### Difference — values in A but NOT in B

```python
print(A - B)             # {1, 2, 3}   — in A, not in B
print(B - A)             # {6, 7, 8}   — in B, not in A
print(A.difference(B))   # {1, 2, 3}
```

### Symmetric Difference — unique to each set (excludes common)

```python
print(A ^ B)                      # {1, 2, 3, 6, 7, 8}  — 4,5 excluded
print(A.symmetric_difference(B))  # same result
```

### Summary table

| Operation | Symbol | Method | Returns |
|-----------|--------|--------|---------|
| Union | `\|` | `.union()` | All unique from both |
| Intersection | `&` | `.intersection()` | Common only |
| Difference | `-` | `.difference()` | In A, not in B |
| Symmetric diff | `^` | `.symmetric_difference()` | Unique each, no common |

> **Union vs Symmetric difference:** Union includes common values (once); symmetric difference excludes them.

---

## 5. Set — Other Functions

```python
s = {10, 20, 30, 40, 50}

print(10 in s)       # True   — membership test
print(100 not in s)  # True

print(len(s))   # 5
print(max(s))   # 50
print(min(s))   # 10
print(sum(s))   # 150
print(sum(s, 20))  # 170  — adds extra value
```

---

## PART B — DICTIONARIES

---

## 6. Dictionary Basics

```python
# Creating a dictionary — key: value pairs in curly braces
student = {
    "name": "Snehith",
    "age": 22,
    "marks": 95
}

print(student)
print(type(student))   # <class 'dict'>

# Empty dictionary
d = {}
print(type(d))         # <class 'dict'>
```

### Dictionary properties

| Property | Value |
|----------|-------|
| Ordered | Yes (Python 3.7+) |
| Mutable (values) | Yes |
| Keys | Unique and immutable |
| Values | Any type, duplicates OK |
| Empty syntax | `{}` |

---

## 7. Accessing Values

```python
d = {"name": "Snehith", "age": 22, "marks": 95}

# Method 1: square bracket — KeyError if key missing
print(d["name"])    # Snehith
# print(d["city"])  # KeyError: 'city'

# Method 2: .get() — returns None if key missing (no error)
print(d.get("name"))    # Snehith
print(d.get("city"))    # None
print(d.get("city", "Not Found"))  # "Not Found" — custom default
```

| Access method | Key missing |
|--------------|-------------|
| `d[key]` | KeyError |
| `d.get(key)` | None |
| `d.get(key, default)` | Custom default |

---

## 8. Adding and Updating Values

```python
d = {"name": "Snehith", "age": 22}

# Update existing key — value gets replaced
d["name"] = "Durga"
print(d)   # {"name": "Durga", "age": 22}

# Add new key — key doesn't exist, so it gets added
d["city"] = "Hyderabad"
print(d)   # {"name": "Durga", "age": 22, "city": "Hyderabad"}
```

---

## 9. Valid vs Invalid Dictionary Keys

```python
# Valid keys: immutable types
d = {
    1: "integer key",
    1.5: "float key",
    "name": "string key",
    (1, 2): "tuple key"
}
print(d)   # works fine

# Invalid key: list (mutable — TypeError: unhashable type)
# d = {[1, 2]: "list key"}   # TypeError!

# Rule: dict keys must be immutable → int, float, str, tuple OK
#                                     list, set, dict NOT OK
```

---

## 10. Deleting from a Dictionary

```python
d = {"id": 1234, "name": "Snehith", "age": 22}

# del — removes specific key-value pair
del d["name"]
print(d)   # {"id": 1234, "age": 22}

# del — removes entire dictionary
del d
# print(d)   # NameError: name 'd' is not defined
```

---

## 11. Dictionary Copy (Shallow vs Deep)

```python
d = {"id": 1234, "name": "Snehith"}

# Shallow — same object
d1 = d
d["age"] = 22         # change on d
print(d1)             # d1 also changes!

# Deep — independent copy
d1 = d.copy()
d["city"] = "Hyd"     # change on d
print(d1)             # d1 is unchanged
```

---

## 12. Dictionary Methods

```python
d = {"id": 1234, "name": "Snehith"}

# keys(), values(), items()
print(d.keys())    # dict_keys(['id', 'name'])
print(d.values())  # dict_values([1234, 'Snehith'])
print(d.items())   # dict_items([('id', 1234), ('name', 'Snehith')])

# pop(key) — removes key-value pair, returns the removed VALUE
removed_val = d.pop("name")
print(removed_val)   # Snehith
print(d)             # {'id': 1234}

# popitem() — removes LAST inserted pair, returns it as tuple
d = {"id": 1234, "name": "Snehith", "age": 22}
last_item = d.popitem()
print(last_item)   # ('age', 22)
print(d)           # {'id': 1234, 'name': 'Snehith'}

# clear() — empties the dictionary
d.clear()
print(d)   # {}
```

---

## 13. Membership Test on Dictionary

```python
d = {"id": 1234, "name": "Snehith"}

# Works on KEYS only
print("id" in d)       # True
print("name" in d)     # True
print("city" in d)     # False

# Does NOT work on values
print(1234 in d)       # False — 1234 is a value, not a key!
```

> **Dictionary membership test checks keys only.**

---

## 14. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `KeyError` using `d[key]` | Key doesn't exist | Use `d.get(key)` |
| `KeyError` using `remove()` on set | Value not in set | Use `discard()` |
| `TypeError: unhashable type: 'list'` | List as dict key | Use tuple instead |
| `{}` creates dict not set | Empty curly braces | Use `set()` for empty set |

---

## 15. Interview Questions

1. How is a set different from a list?
2. What is the difference between `discard()` and `remove()` on a set?
3. What is the difference between union and symmetric difference?
4. What is the difference between `d[key]` and `d.get(key)`?
5. Can a list be used as a dictionary key? Why?
6. Does dictionary membership test check keys or values?
7. What does `popitem()` do?
8. What does `d.items()` return?

---

## 16. Try It Yourself

```python
# 1. Create sets A={1,2,3,4,5} and B={3,4,5,6,7}
#    Print: union, intersection, A-B, B-A, symmetric difference

# 2. s = {10, 20, 30}
#    Try: discard(100), remove(100) — observe the difference

# 3. Create a student dictionary with name, age, marks
#    - Access marks using get() with a default if key missing
#    - Add a "grade" key
#    - Delete the "age" key
#    - Print all keys, all values, all items

# 4. Given two lists: keys = ["a", "b", "c"], values = [1, 2, 3]
#    Create a dictionary mapping each key to its value

# 5. d = {"x": 10, "y": 20, "z": 30}
#    Use popitem() twice and print what is removed each time
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `s = set()` | Empty set (not `{}`) |
| `s.add(45)` | Add one item |
| `s.update([23, 67])` | Add multiple items |
| `s.discard(100)` | Remove — no error if absent |
| `s.remove(100)` | Remove — KeyError if absent |
| `A \| B` | Set union |
| `A & B` | Set intersection |
| `A - B` | Set difference |
| `A ^ B` | Symmetric difference |
| `d.get("key")` | Safe access (None if missing) |
| `d.pop("key")` | Remove and return value |
| `d.popitem()` | Remove and return last pair |
| `d.items()` | All key-value pairs |
