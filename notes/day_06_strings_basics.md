# Day 6 — Data Structures: List, Tuple, Set, Dictionary, Range

← [Day 5](day_05_data_types.md) | [Index](00_INDEX.md) | [Day 7](day_07_operators.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | What does mutable mean? | Value can be changed after creation |
| 2 | What does immutable mean? | Value cannot be changed after creation |
| 3 | Which data structures are mutable? | List, Set, Dictionary |
| 4 | Which data structures are immutable? | Tuple, String, int, float, bool |
| 5 | How do you create an empty set? | `set()` — NOT `{}` (that creates a dict) |
| 6 | Single-element tuple — what's required? | Trailing comma: `(10,)` not `(10)` |
| 7 | Dictionary keys must be...? | Unique and immutable |
| 8 | Dictionary values can be...? | Anything — mutable, duplicate, any type |
| 9 | What does `range(1,10,2)` produce? | 1, 3, 5, 7, 9 (stop is excluded) |
| 10 | What is the default step in range()? | 1 |

---

## 1. Mutable vs Immutable

Python divides all data types into two categories:

```
Mutable (can change)          Immutable (cannot change)
─────────────────────         ──────────────────────────
List      [ ]                 int
Set       { }                 float
Dictionary { : }              bool
                              str
                              tuple  ( )
                              complex
                              None
```

**Key rule:** When you "change" an immutable value, Python actually creates a new object in memory.

```python
x = 10
print(id(x))   # e.g. 140712345

x = 20         # x now points to a NEW object, 10 still exists in memory
print(id(x))   # different address
```

---

## 2. List

- **Ordered** — elements have a fixed position (index 0, 1, 2 …)
- **Mutable** — you can add, remove, or change elements
- **Allows duplicates**
- Created with **square brackets** `[ ]`

```python
fruits = ["apple", "banana", "cherry"]
mixed  = [10, 3.14, "hello", True, None]   # any types together

print(fruits[0])    # apple
print(fruits[-1])   # cherry  (negative indexing)

fruits[1] = "mango"          # change element
fruits.append("grapes")      # add to end
fruits.remove("apple")       # remove by value

print(len(fruits))   # length
```

### List characteristics

| Feature | Value |
|---------|-------|
| Ordered | Yes |
| Mutable | Yes |
| Duplicates | Allowed |
| Syntax | `[1, 2, 3]` |
| Empty | `[]` |

---

## 3. Tuple

- **Ordered** — elements have a fixed position
- **Immutable** — cannot change elements after creation
- **Allows duplicates**
- Created with **parentheses** `( )`
- Faster than list; used for fixed data (coordinates, DB records)

```python
colors = ("red", "green", "blue")
print(colors[0])    # red
print(colors[-1])   # blue

# colors[0] = "yellow"   # TypeError! tuples are immutable
```

### Critical — single-element tuple

```python
t1 = (10)    # NOT a tuple — this is just int 10
t2 = (10,)   # tuple with one element — trailing comma is required

print(type(t1))   # <class 'int'>
print(type(t2))   # <class 'tuple'>
```

### Tuple characteristics

| Feature | Value |
|---------|-------|
| Ordered | Yes |
| Mutable | No (immutable) |
| Duplicates | Allowed |
| Syntax | `(1, 2, 3)` |
| Empty | `()` |

---

## 4. Set

- **Unordered** — no guaranteed position/index
- **Mutable** — can add/remove elements
- **No duplicates** — automatically removes duplicates
- Created with **curly braces** `{ }` BUT **empty set must use `set()`**

```python
nums = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(nums)    # duplicates removed, order not guaranteed

s = set()      # empty set
s.add(10)
s.add(20)
s.remove(10)
```

### Critical pitfall

```python
empty_dict = {}     # This is a DICTIONARY, not a set
empty_set  = set()  # This is a set
```

### Set characteristics

| Feature | Value |
|---------|-------|
| Ordered | No |
| Mutable | Yes |
| Duplicates | Not allowed |
| Syntax | `{1, 2, 3}` |
| Empty | `set()` |

---

## 5. Dictionary

- **Ordered** (since Python 3.7) — insertion order is maintained
- **Mutable** — values can be changed
- **Keys must be unique and immutable**
- **Values can be anything** (mutable, duplicate, any type)
- Created with **curly braces and colons** `{key: value}`

```python
student = {
    "name": "Snehith",
    "age": 22,
    "marks": 95
}

print(student["name"])    # Snehith  — access by key
student["age"] = 23       # update value
student["city"] = "Hyd"   # add new key-value pair

print(student.keys())     # dict_keys(['name', 'age', 'marks', 'city'])
print(student.values())   # dict_values([...])
print(student.items())    # dict_items([...])
```

### Dictionary characteristics

| Feature | Value |
|---------|-------|
| Ordered | Yes (Python 3.7+) |
| Mutable | Yes (values) |
| Keys | Unique + immutable |
| Values | Any type, duplicates OK |
| Syntax | `{"key": value}` |
| Empty | `{}` |

---

## 6. Range

- **Immutable sequence** of numbers
- Used mainly in for loops
- Syntax: `range(stop)` or `range(start, stop)` or `range(start, stop, step)`
- **Stop value is excluded**

```python
range(5)         # 0, 1, 2, 3, 4
range(1, 6)      # 1, 2, 3, 4, 5
range(1, 10, 2)  # 1, 3, 5, 7, 9
range(10, 0, -1) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# convert to list to see contents:
print(list(range(1, 6)))   # [1, 2, 3, 4, 5]
```

---

## 7. Data Structure Comparison Chart

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| Ordered | Yes | Yes | No | Yes (3.7+) |
| Mutable | Yes | No | Yes | Yes (values) |
| Duplicates | Yes | Yes | No | Keys: No, Values: Yes |
| Indexing | Yes (`[0]`) | Yes (`[0]`) | No | By key |
| Syntax | `[1,2]` | `(1,2)` | `{1,2}` | `{k:v}` |
| Empty | `[]` | `()` | `set()` | `{}` |
| Use for | Ordered changeable | Fixed data | Unique items | Key-value pairs |

---

## 8. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: 'tuple' object does not support item assignment` | Trying to change a tuple | Use a list instead |
| `{}` creates a dict, not a set | Empty `{}` is always dict | Use `set()` for empty set |
| `(10)` is not a tuple | Missing trailing comma | Write `(10,)` |
| `KeyError: 'name'` | Key doesn't exist in dict | Check key spelling or use `.get()` |

---

## 9. Interview Questions

1. What is the difference between a list and a tuple?
2. Why would you use a tuple instead of a list?
3. How do you create an empty set in Python?
4. Can a dictionary have duplicate keys?
5. What types can be used as dictionary keys?
6. What is the difference between `{}` and `set()`?
7. What does "ordered" mean for a data structure?
8. What is `range()` and how is it different from a list?

---

## 10. Try It Yourself

```python
# 1. Create a list of 5 cities, print the 3rd one, change it, print again

# 2. Create a tuple of (name, age, city) — try to change age and observe

# 3. Create a set with duplicates — verify duplicates are removed

# 4. Create a student dictionary, add a new key "grade", update "marks"

# 5. Use range(2, 20, 3) — print all values using list()
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `fruits = ["apple", "banana"]` | Basic list |
| `t = (10,)` | Single-element tuple (trailing comma) |
| `s = set()` | Empty set — NOT `{}` |
| `d = {"name": "Snehith", "age": 22}` | Basic dictionary |
| `list(range(1, 10, 2))` | Convert range to list to inspect |
| `id(x)` | Memory address of variable |
