# Day 14 — Bytes, Bytearray, Frozenset & Functions Introduction

← [Day 13](day_13_sets.md) | [Index](00_INDEX.md) | [Day 15](day_15_functions_basics.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | Allowed value range for bytes/bytearray? | 0 to 255 (not 256 — up to but not including 256) |
| 2 | bytes vs bytearray — mutability? | `bytes` immutable; `bytearray` mutable |
| 3 | How to create bytes? | From other data structure: `bytes(list)` |
| 4 | frozenset vs set? | `frozenset` immutable; `set` mutable |
| 5 | How to create frozenset? | `frozenset(set_object)` |
| 6 | What is the keyword to define a function? | `def` |
| 7 | What are the two main advantages of functions? | Reusability and avoiding code repetition |
| 8 | Two types of functions in Python? | Built-in (predefined) and user-defined |
| 9 | Parameters vs arguments? | Parameters: in function definition; Arguments: values passed when calling |
| 10 | `return` vs `print` inside a function? | `return` sends value back to caller; `print` only displays |

---

## PART A — BYTES, BYTEARRAY, FROZENSET

---

## 1. Bytes

```
bytes — represents byte numbers (like an array)
      — immutable (cannot change values)
      — range: 0 to 255 only
      — created FROM other data structures (not directly)
      — used for: images, audio files, video files, binary file I/O
```

```python
# Create list first, then convert to bytes
x = [10, 20, 30, 40]
b = bytes(x)

print(x)            # [10, 20, 30, 40]  — list
print(type(x))      # <class 'list'>
print(b)            # b'\n\x14\x1e('    — binary format
print(type(b))      # <class 'bytes'>

# Access by index (same as list)
print(b[0])   # 10
print(b[1])   # 20
print(b[2])   # 30

# Iterate over bytes
for val in b:
    print(val)   # 10, 20, 30, 40
```

### Range restriction

```python
# Only 0-255 allowed
x = [10, 20, 255]     # OK
b = bytes(x)          # works

x = [10, 20, 256]     # 256 is OUT OF RANGE
# b = bytes(x)        # ValueError: bytes must be in range(0, 256)
```

### Bytes are immutable

```python
b = bytes([10, 20, 30])
# b[1] = 99   # TypeError: 'bytes' object does not support item assignment
```

---

## 2. Bytearray

Same as `bytes` but **mutable** — you can change values.

```python
x = [10, 20, 30, 40]
ba = bytearray(x)

print(ba)         # bytearray(b'\n\x14\x1e(')
print(type(ba))   # <class 'bytearray'>

# Bytearray IS mutable — can change values
ba[1] = 99
print(ba)   # bytearray with 99 at index 1

# Same 0-255 range restriction applies
# ba[0] = 256   # ValueError: byte must be in range(0, 256)
```

| Feature | bytes | bytearray |
|---------|-------|-----------|
| Mutable | No | Yes |
| Range | 0–255 | 0–255 |
| Created from | Other data structures | Other data structures |
| Use case | Binary file read | Binary file read/write |

---

## 3. Frozenset

A **frozenset** is an **immutable** version of a set.

```python
# Create a set first, then convert to frozenset
s = {10, 20, 30, 40, 50}
fs = frozenset(s)

print(s)            # {10, 20, 30, 40, 50}
print(type(s))      # <class 'set'>
print(fs)           # frozenset({10, 20, 30, 40, 50})
print(type(fs))     # <class 'frozenset'>
```

### Frozenset is immutable

```python
s  = {10, 20, 30}
fs = frozenset(s)

# Set is mutable — can add
s.add(99)          # works fine

# Frozenset is immutable — cannot add
# fs.add(99)       # AttributeError: 'frozenset' object has no attribute 'add'
```

| Feature | set | frozenset |
|---------|-----|-----------|
| Mutable | Yes | No |
| Indexing | No | No |
| Duplicates | No | No |
| Can add/remove | Yes | No |

---

## 4. Data Structures — Complete Summary

| Data Structure | Syntax | Ordered | Mutable | Duplicates | Notes |
|----------------|--------|---------|---------|------------|-------|
| str | `"abc"` | Yes | No | Yes | Characters |
| list | `[1,2]` | Yes | Yes | Yes | Most used |
| tuple | `(1,2)` | Yes | No | Yes | Fixed data |
| set | `{1,2}` | No | Yes | No | Unique only |
| dict | `{k:v}` | Yes (3.7+) | Yes (values) | Keys: No | Key-value |
| range | `range()` | Yes | No | — | Numbers |
| bytes | `bytes()` | Yes | No | Yes | 0–255, binary |
| bytearray | `bytearray()` | Yes | Yes | Yes | 0–255, binary |
| frozenset | `frozenset()` | No | No | No | Immutable set |

---

## PART B — FUNCTIONS

---

## 5. What is a Function?

A **function** is a group of statements that performs a specific task. You write it once and can call it many times.

### Why use functions?

1. **Reusability** — write once, use many times
2. **Avoid repetition** — no need to copy-paste the same code
3. **Readability** — code is split into logical pieces
4. **Easy maintenance** — fix a bug in one place, not everywhere

```
Without functions:         With functions:
─────────────────          ──────────────
10 lines of code           def add(a, b):       ← write once
10 lines repeated              return a + b
10 lines repeated
...                        add(10, 20)          ← call anywhere
```

---

## 6. Two Types of Functions

| Type | Description | Examples |
|------|-------------|---------|
| Built-in (predefined) | Come with Python installation | `print()`, `input()`, `len()`, `type()`, `id()` |
| User-defined | Created by the programmer | Any function you write with `def` |

---

## 7. Function Syntax

```python
def function_name(parameters):
    """docstring (optional description)"""
    # statements
    return value   # optional
```

- `def` — keyword to define a function (check with `keyword.kwlist`)
- `function_name` — follows identifier rules (no digits start, no spaces, no keywords)
- `parameters` — optional input values
- `return` — optional; sends a value back to the caller
- `:` — mandatory at end of function header

---

## 8. Function Examples

### No parameters, no return

```python
def greet():
    print("Hello, World!")

greet()    # calling the function
greet()    # call again — reuses same logic
```

### With a single parameter

```python
def greet(name):
    print("Hello", name)

greet("Snehith")   # Hello Snehith
greet("Python")    # Hello Python
```

### With two parameters

```python
def add(a, b):
    result = a + b
    print("Sum:", result)

add(10, 20)    # Sum: 30
add(5.5, 4.5)  # Sum: 10.0
```

### `pass` — empty function placeholder

```python
def my_function():
    pass    # no implementation yet — prevents IndentationError

my_function()   # works fine — does nothing
```

---

## 9. `return` vs `print` Inside a Function

```python
# Version 1: function PRINTS result
def add_print(a, b):
    print(a + b)   # only displays — value is gone after this

add_print(10, 20)   # 30 is shown, but cannot be stored or reused

# Version 2: function RETURNS result
def add_return(a, b):
    return a + b   # sends value back to whoever called it

result = add_return(10, 20)    # 30 stored in 'result'
print("Sum is:", result)       # can use the value further

# Further reuse:
def subtract(x, y):
    return x - y

r = add_return(10, 20)   # 30
answer = subtract(r, 6)  # 30 - 6 = 24
print(answer)
```

### Key difference

| `print()` inside function | `return` inside function |
|--------------------------|--------------------------|
| Just displays output | Sends value to caller |
| Value cannot be reused | Value can be stored and reused |
| `R = func()` → `R` is `None` | `R = func()` → `R` holds the returned value |

---

## 10. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ValueError: bytes must be in range(0, 256)` | Value > 255 in list | Keep values 0–255 |
| `TypeError: 'bytes' object does not support item assignment` | Modifying bytes | Use `bytearray` instead |
| `AttributeError: 'frozenset' object has no attribute 'add'` | Adding to frozenset | Use regular `set` |
| `SyntaxError` on `def function()` | Missing `:` at end | Write `def function():` |
| Function defined but never called | Forgot to call it | Add `function_name()` after the def block |

---

## 11. Interview Questions

1. What is the difference between `bytes` and `bytearray`?
2. What value range does `bytes` accept?
3. What is a `frozenset`? How does it differ from `set`?
4. What are the two advantages of using functions?
5. What is the `def` keyword used for?
6. What is the difference between a parameter and an argument?
7. What does the `return` statement do?
8. What is the difference between `print()` and `return` inside a function?

---

## 12. Try It Yourself

```python
# 1. Create list [10, 50, 100, 200, 255] and convert to bytes
#    Access each element by index, then iterate with for loop

# 2. Create bytearray([10, 20, 30]), change index 1 to 99, print result

# 3. s = {1, 2, 3, 4, 5}
#    Convert to frozenset, try to add 6 (catch the error), print the frozenset

# 4. Write a function greet(name) that prints "Hello, name! Welcome to Python"
#    Call it 3 times with different names

# 5. Write two functions:
#    - square(n): returns n*n
#    - cube(n): returns n*n*n
#    Call both with n=5, store results, print them
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `bytes([10, 20, 30])` | Create bytes from list |
| `b[0]` | Access byte by index |
| `for val in b: print(val)` | Iterate over bytes |
| `bytearray([10, 20])` | Mutable bytes |
| `ba[1] = 99` | Modify bytearray |
| `frozenset(s)` | Immutable set |
| `def f1():` | Define a function |
| `f1()` | Call a function |
| `def add(a, b): return a + b` | Function with return |
| `result = add(10, 20)` | Store returned value |
