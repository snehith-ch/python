# Day 20 — Built-in Modules: math, datetime, calendar, random & Arrays

← [Day 19](day_19_modules.md) | [Index](00_INDEX.md) | [Day 21](day_21_oops_intro.md) →

---

## Quick Revision

| # | Concept | One-line Summary |
|---|---------|-----------------|
| 1 | Built-in modules | Pre-installed with Python; no `pip install` needed |
| 2 | `math` | Mathematical functions: sqrt, factorial, ceil, floor, pow |
| 3 | `datetime` | Date and time operations; `.now()`, `.strftime()` |
| 4 | `calendar` | Display calendars, check leap years |
| 5 | `random` | Generate random numbers and pick random items |
| 6 | `random()` | Float between 0 and 1 (exclusive) |
| 7 | `randint(a, b)` | Integer between a and b, both inclusive |
| 8 | `choice(seq)` | Random single item from a sequence |
| 9 | Array module | 1D only, homogeneous type, built-in |
| 10 | NumPy | 1D + 2D arrays, must be installed separately |

---

## 1. `math` Module

```python
import math
# or: from math import *  (then no need for 'math.' prefix)

print(math.sqrt(25))        # 5.0     — square root (always float)
print(math.factorial(6))    # 720     — 6!
print(math.ceil(4.1))       # 5       — round UP to nearest int
print(math.floor(4.9))      # 4       — round DOWN to nearest int
print(math.pow(2, 8))       # 256.0   — power (always float)
print(math.pi)              # 3.141592653589793
```

With `from math import *`:

```python
from math import *

print(sqrt(16))     # 4.0  — no 'math.' prefix needed
print(ceil(3.2))    # 4
```

---

## 2. `datetime` Module

### Get current date and time

```python
import datetime

now = datetime.datetime.now()
print(now)               # 2026-05-17 14:30:22.123456

print(now.year)          # 2026
print(now.month)         # 5
print(now.day)           # 17
print(now.hour)          # 14
print(now.minute)        # 30
print(now.second)        # 22
print(now.microsecond)   # 123456
```

### Create a specific date

```python
d = datetime.date(2025, 1, 15)
print(d)   # 2025-01-15
```

### Format with `strftime()`

```python
now = datetime.datetime.now()

print(now.strftime("%A"))   # Monday        — full weekday name
print(now.strftime("%a"))   # Mon           — short weekday name
print(now.strftime("%B"))   # January       — full month name
print(now.strftime("%b"))   # Jan           — short month name
print(now.strftime("%Y"))   # 2026          — 4-digit year
print(now.strftime("%y"))   # 26            — 2-digit year
print(now.strftime("%d"))   # 17            — day (zero-padded)
print(now.strftime("%H:%M:%S"))  # 14:30:22
```

---

## 3. `calendar` Module

```python
import calendar

# Print a month calendar:
print(calendar.month(2026, 5))
# Output:
#       May 2026
# Mo Tu We Th Fr Sa Su
#                  1  2  3
#  4  5  6  7  8  9 10
# ...

# Print a full year calendar:
print(calendar.calendar(2026))

# Count leap days between two years:
print(calendar.leapdays(2000, 2026))   # number of leap years from 2000 to 2026

# Check if a year is a leap year:
print(calendar.isleap(2024))   # True
print(calendar.isleap(2023))   # False
```

---

## 4. `random` Module

```python
from random import *

# Float between 0 and 1 (0 and 1 excluded):
print(random())          # e.g. 0.7341829...

# Integer between a and b (both inclusive):
print(randint(1, 10))    # e.g. 7

# Float between a and b:
print(uniform(1.0, 5.0)) # e.g. 3.14159...

# Integer using step (like range — stop is excluded):
print(randrange(1, 10, 2))   # odd numbers: 1,3,5,7,9

# Random item from a sequence:
colors = ["red", "green", "blue", "yellow"]
print(choice(colors))    # e.g. "green"
```

**Summary table:**

| Function | Returns | Range |
|----------|---------|-------|
| `random()` | float | 0 < x < 1 |
| `randint(a, b)` | int | a ≤ x ≤ b (inclusive) |
| `uniform(a, b)` | float | a ≤ x ≤ b |
| `randrange(start, stop, step)` | int | start ≤ x < stop |
| `choice(seq)` | element | one random item |

---

## 5. Array Module vs NumPy

### Built-in `array` module

```python
from array import array

# Syntax: array(typecode, initializer)
a = array('i', [10, 20, 30, 40])   # 'i' = signed int
print(a)          # array('i', [10, 20, 30, 40])
print(a[0])       # 10
```

Limitations:
- **1D only** — no multi-dimensional arrays
- **Homogeneous** — all elements must be the same type
- Built-in — no installation needed

### NumPy

```python
import numpy as np

# 1D array:
a = np.array([1, 2, 3, 4, 5])
print(a)         # [1 2 3 4 5]

# 2D array (matrix):
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b)
# [[1 2 3]
#  [4 5 6]]
```

Advantages over built-in array:
- Supports **1D and 2D** (and higher) arrays
- More mathematical operations built in
- Foundation for data science (pandas, matplotlib, etc.)

**Installing NumPy:**
- PyCharm: Settings → Project → Python Interpreter → `+` → search "numpy" → Install Package
- Terminal: `pip install numpy`

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `AttributeError: module 'datetime' has no attribute 'now'` | Used `datetime.now()` instead of `datetime.datetime.now()` | Add the second `datetime` |
| `ModuleNotFoundError: No module named 'numpy'` | NumPy not installed | `pip install numpy` |
| `ValueError: array typecode must be a character` | Wrong typecode in `array()` | Use `'i'`, `'f'`, `'d'` etc. |
| `random()` gives 0 or 1 | It won't — these are excluded | But `randint` includes both ends |

---

## Interview Questions

1. What is the difference between a built-in module and a user-defined module?
2. What does `math.ceil()` vs `math.floor()` return? Give an example.
3. What is the output of `datetime.datetime.now().strftime("%A")`?
4. What is the difference between `random()`, `randint()`, and `uniform()`?
5. Which `random` function picks one item from a list?
6. What is the difference between the `array` module and NumPy?
7. How do you check if a year is a leap year using the `calendar` module?
8. How do you install a third-party module like NumPy?

---

## Try It Yourself

1. Use the `math` module to compute: `√144`, `7!`, `ceil(9.01)`, `floor(9.99)`, `2^16`.
2. Use `datetime` to print today's date in the format: `"Saturday, 17 May 2026"`.
3. Use `calendar` to print the calendar for the current month. Check if 2000 was a leap year.
4. Use `random` to simulate rolling a 6-sided die 10 times (print each result).
5. Create a NumPy 2D array representing a 3×3 identity matrix manually (no special functions).

---

## Code Created

| Snippet | Purpose |
|---------|---------|
| `math.sqrt(25)`, `math.factorial(6)` | math module functions |
| `datetime.datetime.now().strftime("%A, %d %B %Y")` | Formatted date string |
| `calendar.isleap(2024)`, `calendar.month(2026, 5)` | Calendar module |
| `randint(1, 6)`, `choice(colors)` | Random number/item |
| `np.array([[1,2],[3,4]])` | NumPy 2D array |

---

← [Day 19](day_19_modules.md) | [Index](00_INDEX.md) | [Day 21](day_21_oops_intro.md) →
