# Day 21 — Arrays: `array` Module & NumPy

← [Day 20](day_20_builtin_modules.md) | [Index](00_INDEX.md) | [Day 22](day_22_oop_intro.md) →

---

## Quick Revision — Day 21

| # | Key Point |
|---|-----------|
| 1 | `array` module creates 1D arrays only; NumPy creates 1D and 2D arrays |
| 2 | Array is **homogeneous** — all elements must be the same data type |
| 3 | List is **heterogeneous** — can hold any mix of data types |
| 4 | Type code is mandatory with the `array` module: `'i'`=int, `'f'`=float, `'u'`=Unicode char |
| 5 | NumPy must be installed explicitly; `array` module is built-in |
| 6 | `import numpy as np` — `np` is the standard alias |
| 7 | NumPy array properties: `dtype`, `size`, `ndim`, `shape` |
| 8 | 2D array access: `a[row_index, col_index]` |
| 9 | `axis=0` → column-wise operations; `axis=1` → row-wise operations |
| 10 | `flatten()` converts a 2D NumPy array into a 1D array |

---

## Navigation

- **Pre-requisite:** [Day 20](day_20_builtin_modules.md) — Built-in modules, `array` module intro
- **Next:** [Day 22](day_22_oop_intro.md) — Object-Oriented Programming introduction
- **Related:** [Day 12](day_12_lists.md) — Lists (arrays are like typed lists)

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `arrays_demo.py` | All array module examples |
| `.py` file | `numpy_demo.py` | All NumPy examples |
| Import | `import array` | Load the built-in array module |
| Import | `import numpy as np` | Load NumPy with standard alias |
| Variable | `a = array.array('i', [10, 20, 30, 40])` | Integer array using array module |
| Variable | `a = np.array([10, 20, 30, 40])` | NumPy 1D array |
| Variable | `a = np.array([[20,30,40,28],[15,25,35,45],[43,87,93,21]])` | NumPy 2D array |

---

## 1. Why Arrays? — List vs Array

Before the `array` module, Python gives us lists. But arrays are a separate concept:

```
List — Heterogeneous (mixed types allowed)
+------+------+------+------+
| 10   | "hi" | 3.14 | True |   ← int, str, float, bool all in one list
+------+------+------+------+

Array — Homogeneous (all same type)
+------+------+------+------+
| 10   | 20   | 30   | 40   |   ← all integers (type code 'i')
+------+------+------+------+
```

| Feature | List | Array (`array` module) | NumPy Array |
|---------|------|----------------------|-------------|
| Data types | Mixed (heterogeneous) | Same type (homogeneous) | Same type (homogeneous) |
| Dimensions | 1D only (nested lists for 2D) | 1D only | 1D and 2D (multi-dimensional) |
| Type code | Not needed | Required (`'i'`, `'f'`, `'u'`) | Optional (`dtype`) |
| Install | Built-in | Built-in | Must install (`pip install numpy`) |
| Speed | Slower for math | Faster than list | Fastest (C-backed) |

---

## 2. `array` Module — Single Dimension Arrays

### 2.1 Type Codes

When using the `array` module, you must declare what type of elements the array will hold. This is called the **type code**.

| Type Code | C Type | Python Type | Size |
|-----------|--------|-------------|------|
| `'b'` | signed char | int | 1 byte |
| `'B'` | unsigned char | int | 1 byte |
| `'i'` | signed int | int | 2 bytes |
| `'I'` | unsigned int | int | 2 bytes |
| `'l'` | signed long | int | 4 bytes |
| `'f'` | float | float | 4 bytes |
| `'d'` | double | float | 8 bytes |
| `'u'` | Py_UNICODE | Unicode char | 2 bytes |

Most commonly used: `'i'` for integers, `'f'` for floats, `'u'` for characters.

### 2.2 Creating Arrays

```python
import array

# Syntax: array.array(typecode, [elements])
a = array.array('i', [10, 20, 30, 40])
print(a)           # array('i', [10, 20, 30, 40])
print(type(a))     # <class 'array.array'>
print(a.typecode)  # i
```

**Import style options:**

```python
# Style 1 — standard import (use module.method)
import array
a = array.array('i', [10, 20, 30])

# Style 2 — alias (shorter to type)
import array as ar
a = ar.array('i', [10, 20, 30])

# Style 3 — from import (no module name needed)
from array import *
a = array('i', [10, 20, 30])
```

### 2.3 Wrong Way (without type code)

```python
import array
a = array.array([10, 20, 30])   # WRONG — no type code!
# TypeError: array() argument 1 must be a unicode character, not list
```

> **Common Mistake:** Forgetting the type code. The `array` module requires a type code as the first argument. The `list` constructor does not.

### 2.4 Accessing Array Elements

```python
from array import *
a = array('i', [10, 20, 30, 40])

# Index-based access (same as list)
print(a[0])   # 10
print(a[1])   # 20
print(a[3])   # 40
```

Array indexing:

```
 10   20   30   40
  0    1    2    3    ← positive index
 -4   -3   -2   -1   ← negative index
```

### 2.5 Iterating Over an Array

```python
from array import *
a = array('i', [10, 20, 30, 40])

# Method 1 — for-in (cleaner, recommended)
for i in a:
    print(i)
# Output: 10  20  30  40

# Method 2 — range with index
for i in range(len(a)):
    print(a[i])
# Output: 10  20  30  40
```

> **Instructor tip:** Use `range(len(a))` instead of a hardcoded number like `range(4)`. If you add or remove elements, the length updates automatically — you don't have to change the loop.

### 2.6 Array Operations

```python
from array import *
a = array('i', [10, 20, 30, 40])

# Remove by VALUE (not index)
a.remove(20)
print(a)   # array('i', [10, 30, 40])

# Insert at INDEX: insert(index, value)
a.insert(1, 33)
print(a)   # array('i', [10, 33, 30, 40])

# Reverse
a.reverse()
print(a)   # array('i', [40, 30, 33, 10])

# Append
a.append(50)
print(a)   # array('i', [40, 30, 33, 10, 50])

# Length
print(len(a))   # 5
```

> **Common Mistake:** `remove()` takes a **value**, not an index.
> `a.remove(2)` removes the value `2`, not the element at index 2.
> Use `del a[2]` or `a.pop(2)` to remove by index.

### 2.7 Accepting Array Values at Runtime

```python
from array import *

a = array('i', [])          # start with empty integer array
n = int(input("Enter length of array: "))
for i in range(n):
    x = int(input("Enter value: "))
    a.append(x)

print(a)
```

**Sample run:**

```
Enter length of array: 4
Enter value: 10
Enter value: 20
Enter value: 30
Enter value: 40
array('i', [10, 20, 30, 40])
```

---

## 3. NumPy — Numerical Python

### 3.1 What is NumPy?

- **NumPy** = **Num**erical **Py**thon
- A third-party library for multi-dimensional array processing
- Supports 1D and 2D (and higher) arrays
- Must be installed explicitly — not built-in like `array`

### 3.2 Installing NumPy in PyCharm

1. Open **File → Settings**
2. Expand your project (e.g., `Python_project_7am`)
3. Click **Python Interpreter**
4. Click the **`+`** (plus) button
5. Search for `numpy` in the search box
6. Click **Install Package**
7. Wait for "Package installed successfully" message

```
File → Settings → Python Interpreter → [+] → search "numpy" → Install
```

### 3.3 Importing NumPy

```python
# Standard (recommended)
import numpy as np       # 'np' is the universal alias

# Full name
import numpy

# From import
from numpy import *
```

### 3.4 NumPy Array Methods Overview

| Method | Purpose |
|--------|---------|
| `np.array()` | Create array from a list — most commonly used |
| `np.linspace(start, stop, num)` | `num` evenly spaced values from start to stop |
| `np.logspace(start, stop, num)` | `num` logarithmically spaced values |
| `np.arange(start, stop, step)` | Like `range()` but returns a NumPy array |
| `np.zeros(n)` | Array of `n` zeros (float by default) |
| `np.ones(n)` | Array of `n` ones (float by default) |

---

## 4. NumPy — 1D Arrays

### 4.1 Creating a 1D Array

```python
import numpy as np

a = np.array([10, 20, 30, 40])
print(a)           # [10 20 30 40]
print(type(a))     # <class 'numpy.ndarray'>
print(a.dtype)     # int64       — data type of elements
print(a.size)      # 4           — number of elements
print(a.ndim)      # 1           — number of dimensions
print(a.shape)     # (4,)        — (rows,)   for 1D
```

> `ndarray` = **n-dimensional array**. `ndim` tells you how many dimensions the array has.

### 4.2 No Type Code Needed

NumPy automatically detects the data type:

```python
import numpy as np

a = np.array([10, 20, 30, 40])
print(a.dtype)   # int64   — all integers → int

b = np.array([10, 20, 30, 40.8])
print(b)         # [10.  20.  30.  40.8]   ← ONE float makes ALL float
print(b.dtype)   # float64
```

> **Important:** If even ONE element is a float, NumPy converts ALL elements to float automatically. This is called **type promotion**.

### 4.3 Forcing a Data Type with `dtype`

```python
import numpy as np

# Force integer even if float values are given
a = np.array([10, 20, 30, 40.8], dtype=int)
print(a)         # [10 20 30 40]   ← 40.8 truncated to 40
print(a.dtype)   # int64
```

### 4.4 Accessing 1D Array Elements

```python
import numpy as np

a = np.array([10, 20, 30, 40])
print(a[0])    # 10
print(a[3])    # 40
print(a[-1])   # 40   — negative indexing works
```

### 4.5 `linspace` — Evenly Spaced Values

```python
import numpy as np

# linspace(start, stop, num_values)
a = np.linspace(2, 20, 7)    # 7 values from 2 to 20
print(a)
# [ 2.          4.66666667  7.33333333 10.         12.66666667 15.33333333 18.        20.        ]
# Wait — linspace(2, 20, 7) gives exactly 7 values including both endpoints

a = np.linspace(2, 20, 9)    # 9 values from 2 to 20
print(a)
# [ 2.    4.25  6.5   8.75 11.   13.25 15.5  17.75 20.  ]
```

> By default, `linspace` returns **floating point** values (divides the range evenly, so decimals appear).

### 4.6 `logspace` — Logarithmically Spaced Values

```python
import numpy as np

a = np.logspace(2, 20, 9)
print(a)
# [1.e+02  1.e+04  ... ]  — logarithmic values
```

### 4.7 `arange` — Range-based Array

```python
import numpy as np

# arange(start, stop, step)   — step value (not num_parts)
a = np.arange(2, 20, 2)    # even numbers from 2 to 20
print(a)    # [ 2  4  6  8 10 12 14 16 18]

a = np.arange(2, 20, 3)    # step of 3
print(a)    # [ 2  5  8 11 14 17]
```

> **Difference:** `linspace(2, 20, 9)` → you specify **number of values**. `arange(2, 20, 3)` → you specify **step size**.

### 4.8 `zeros` and `ones`

```python
import numpy as np

z = np.zeros(10)              # 10 zeros (float by default)
print(z)   # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

z = np.zeros(10, dtype=int)   # 10 zeros as integers
print(z)   # [0 0 0 0 0 0 0 0 0 0]

o = np.ones(10)               # 10 ones (float by default)
print(o)   # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```

---

## 5. NumPy — 2D Arrays

### 5.1 Creating a 2D Array

```python
import numpy as np

a = np.array([
    [20, 30, 40, 28],
    [15, 25, 35, 45],
    [43, 87, 93, 21]
])
```

Visual structure:

```
         col0  col1  col2  col3
row 0  [  20    30    40    28  ]
row 1  [  15    25    35    45  ]
row 2  [  43    87    93    21  ]
```

### 5.2 2D Array Properties

```python
print(a)          # [[20 30 40 28]
                  #  [15 25 35 45]
                  #  [43 87 93 21]]

print(a.ndim)     # 2      — 2 dimensions (rows + columns)
print(a.size)     # 12     — total elements (3 rows × 4 cols)
print(a.shape)    # (3, 4) — 3 rows, 4 columns
```

### 5.3 Accessing Elements in a 2D Array

```python
# Syntax: a[row_index, col_index]
#    OR:  a[row_index][col_index]

print(a[0, 0])   # 20   — row 0, col 0
print(a[1, 2])   # 35   — row 1, col 2
print(a[2, 0])   # 43   — row 2, col 0
```

Visual indexing guide:

```
         col0  col1  col2  col3
row 0  [  20    30    40    28  ]    a[0,0]=20  a[0,2]=40
row 1  [  15    25    35    45  ]    a[1,2]=35  a[1,3]=45
row 2  [  43    87    93    21  ]    a[2,0]=43  a[2,2]=93
```

### 5.4 Max, Min, and Sum Operations

```python
import numpy as np

a = np.array([
    [10, 30, 40],
    [15, 25, 45],
    [43, 87, 21]
])

# Overall max and min
print(a.max())   # 87   — highest value in entire array
print(a.min())   # 10   — lowest value in entire array
print(a.sum())   # sum of all elements

# axis=1 → row-wise (across columns of each row)
print(a.max(axis=1))   # [40 45 87] — max in each row
print(a.min(axis=1))   # [10 15 21] — min in each row

# axis=0 → column-wise (across rows of each column)
print(a.max(axis=0))   # [43 87 45] — max in each column
print(a.min(axis=0))   # [10 25 21] — min in each column
```

Axis direction diagram:

```
axis=1 → operates ACROSS columns (→→→) — gives one value per ROW
axis=0 → operates ACROSS rows    (↓↓↓) — gives one value per COLUMN

         col0  col1  col2
row 0  [  10    30    40  ]   axis=1 max → 40
row 1  [  15    25    45  ]   axis=1 max → 45
row 2  [  43    87    21  ]   axis=1 max → 87
         ↓     ↓     ↓
axis=0   43    87    45      (max of each column)
```

### 5.5 `flatten()` — Convert 2D to 1D

```python
import numpy as np

a = np.array([
    [10, 30, 40],
    [15, 25, 45],
    [43, 87, 21]
])

print(a.ndim)      # 2

b = a.flatten()    # collapse all rows into one row
print(b)           # [10 30 40 15 25 45 43 87 21]
print(b.ndim)      # 1
```

> `flatten()` returns a **copy** (original `a` is unchanged). All rows are joined left-to-right in order.

---

## 6. Complete Class Walkthrough — `array` Module

**Step 1:** Create a new PyCharm file `arrays_demo.py`

**Step 2:** Import the array module

```python
from array import *
```

**Step 3:** Create an integer array and inspect it

```python
a = array('i', [10, 20, 30, 40])
print(a)             # array('i', [10, 20, 30, 40])
print(type(a))       # <class 'array.array'>
print(a.typecode)    # i
```

**Step 4:** Try without type code (intentional error to learn)

```python
a = array([10, 20, 30])   # TypeError — no type code!
```

**Step 5:** Access, insert, remove, reverse

```python
a = array('i', [10, 20, 30, 40])
print(a[1])        # 20
a.remove(20)       # remove by value
a.insert(1, 33)    # insert 33 at index 1
a.reverse()
print(a)
```

**Step 6:** Iterate using `for` loop

```python
for i in a:
    print(i)
```

---

## 7. Complete Class Walkthrough — NumPy

**Step 1:** Install NumPy (PyCharm → Settings → Interpreter → `+` → numpy)

**Step 2:** Create `numpy_demo.py`

**Step 3:** Create 1D array

```python
import numpy as np

a = np.array([10, 20, 30, 40])
print(a)
print(a.dtype)
print(a.size)
print(a.ndim)
print(a.shape)
```

**Step 4:** Test type promotion (float overrides int)

```python
b = np.array([10, 20, 30, 40.8])
print(b.dtype)   # float64
```

**Step 5:** Create 2D array and explore

```python
a = np.array([[20,30,40,28],[15,25,35,45],[43,87,93,21]])
print(a.shape)       # (3, 4)
print(a[1, 2])       # 35
print(a.max())       # 93
print(a.max(axis=1)) # row-wise max
print(a.flatten())   # 1D version
```

---

## Student Q&A

> **Student Question:** How can I accept array values from the user at runtime?
> **Answer:** Create an empty array, ask the user how many values they want to enter (`n`), then use `range(n)` to loop and `append()` each value. This is the same pattern as filling a list at runtime.

```python
from array import *
a = array('i', [])
n = int(input("Enter length: "))
for i in range(n):
    x = int(input("Enter value: "))
    a.append(x)
print(a)
```

> **Student Question:** Can a NumPy array hold mixed types like a list?
> **Answer:** No — NumPy arrays are homogeneous. If you mix int and float, NumPy automatically converts all to float (type promotion). If you add a string, it converts everything to a string type. NumPy always picks one common type.

> **Student Question:** What is the difference between `remove()` in array module and `del`?
> **Answer:** `remove(value)` searches for that **value** and removes the first occurrence. `del a[index]` removes the element at that specific **index** position.

---

## Key Differences Summary

| Feature | `array` Module | NumPy |
|---------|---------------|-------|
| Built-in | Yes | No (install with `pip`) |
| Dimensions | 1D only | 1D, 2D, and higher |
| Type code | Required (`'i'`, `'f'`, etc.) | Optional (`dtype`) |
| Type detection | Manual | Automatic |
| Math operations | Limited | Full (max, min, sum, axis) |
| Alias | — | `np` (standard) |
| Used in pandas/matplotlib | No | Yes (core dependency) |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: array() argument 1 must be a unicode character, not list` | Missing type code in `array.array()` | Add type code as first argument: `array('i', [1,2,3])` |
| `TypeError: an integer is required` | Passing float values to `'i'` type code | Use `'f'` for floats or convert to int |
| `ValueError: 'x' is not in array` | `remove(x)` called but `x` does not exist in array | Check element exists before removing |
| `IndexError: array index out of range` | Accessing index beyond array length | Use `len(a)` to check bounds |
| `ModuleNotFoundError: No module named 'numpy'` | NumPy not installed | Run `pip install numpy` or install via PyCharm Interpreter settings |

---

## Interview Questions

**Q: What is the difference between a Python list and an array?**
A: A list is heterogeneous — it can hold any mix of data types. An array (from the `array` module or NumPy) is homogeneous — all elements must be the same data type. Arrays are more memory-efficient and faster for numerical computation.

**Q: What is a type code in the `array` module?**
A: A type code is a single character that tells the `array` module what data type the elements will be. For example, `'i'` means integers, `'f'` means floats, `'u'` means Unicode characters. It is the first argument to `array.array()` and is mandatory.

**Q: What does NumPy stand for?**
A: NumPy stands for **Numerical Python**. It is a library for multi-dimensional array processing, commonly used for scientific computing, data analysis, and as the foundation for pandas and matplotlib.

**Q: What is the difference between `linspace` and `arange` in NumPy?**
A: `linspace(start, stop, num)` creates `num` evenly spaced values from `start` to `stop`. `arange(start, stop, step)` creates values from `start` to `stop` incrementing by `step`. Use `linspace` when you know how many values you want; use `arange` when you know the step size.

**Q: What is `ndim`, `size`, and `shape` in NumPy?**
A: `ndim` = number of dimensions (1 for 1D, 2 for 2D). `size` = total number of elements. `shape` = tuple of (rows, columns) — e.g., `(3, 4)` means 3 rows and 4 columns.

**Q: What does `axis=0` and `axis=1` mean in NumPy?**
A: `axis=0` operates down the rows (column-wise result). `axis=1` operates across the columns (row-wise result). For example, `a.max(axis=1)` gives the maximum value in each row.

**Q: What does `flatten()` do?**
A: `flatten()` collapses a multi-dimensional array into a 1D array. A 3×4 2D array becomes a single row of 12 elements. It returns a copy, leaving the original unchanged.

**Q: Is NumPy array mutable?**
A: Yes. You can change individual elements with index assignment (`a[0] = 99`). However, the size (number of elements) is fixed after creation — you cannot append to a NumPy array like a list.

---

## Try It Yourself

**Exercise 1:** Create an integer array of 5 values `[5, 10, 15, 20, 25]` using the `array` module. Print it, print its type code, reverse it, and print it again.

<details><summary>Answer</summary>

```python
from array import *

a = array('i', [5, 10, 15, 20, 25])
print(a)            # array('i', [5, 10, 15, 20, 25])
print(a.typecode)   # i
a.reverse()
print(a)            # array('i', [25, 20, 15, 10, 5])
```
</details>

---

**Exercise 2:** Using NumPy, create a 1D array `[1, 2, 3, 4, 5]`. Print its `dtype`, `size`, `ndim`, and `shape`.

<details><summary>Answer</summary>

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a.dtype)   # int64
print(a.size)    # 5
print(a.ndim)    # 1
print(a.shape)   # (5,)
```
</details>

---

**Exercise 3:** Create a 2D NumPy array with 2 rows and 3 columns. Print the element at row 1, column 2. Then find the max value in each row.

<details><summary>Answer</summary>

```python
import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(a[1, 2])          # 60
print(a.max(axis=1))    # [30 60]
```
</details>

---

**Exercise 4:** Accept 5 integer values from the user and store them in an `array` module array. Then print the array, its length, and the maximum value.

<details><summary>Answer</summary>

```python
from array import *

a = array('i', [])
for i in range(5):
    x = int(input(f"Enter value {i+1}: "))
    a.append(x)

print(a)
print("Length:", len(a))
print("Max:", max(a))
```
</details>

---

**Exercise 5:** Create a 3×3 NumPy array of your choice. Flatten it to 1D and print both the 2D and 1D versions along with their `ndim`.

<details><summary>Answer</summary>

```python
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a)
print("ndim:", a.ndim)   # 2

b = a.flatten()
print(b)
print("ndim:", b.ndim)   # 1
```
</details>
