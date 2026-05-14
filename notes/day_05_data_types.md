# Day 5 — Data Types: None, Numeric (int, float, bool, complex), Type Casting, input(), and Data Structures Overview

## Quick Revision — Day 5
| # | Key Point |
|---|-----------|
| 1 | Python has two categories of data types: **basic** (None, int, float, bool, complex) and **sequence/data structures** (str, list, tuple, set, dict, range, bytes, bytearray, frozenset) |
| 2 | `None` is Python's equivalent of `null` in other languages |
| 3 | **Type casting:** `int()`, `float()`, `str()`, `bool()` convert between types |
| 4 | `input()` function always returns a **string** — you must cast to int/float if you need numbers |
| 5 | `bool` has only two values: `True` and `False`; internally `True = 1`, `False = 0` |
| 6 | `complex` numbers use **j** (not i) for the imaginary part: e.g., `2+3j` |
| 7 | Python has **no `char` data type** — even a single character is `str` |
| 8 | Use `type()` to check the data type of any variable |
| 9 | `print(dir(str))` lists all methods available for strings |
| 10 | `print(help(str))` gives full documentation of string methods |

---

**Pre-requisite:** Day 4 — Fundamental concepts (variables, identifiers, indentation)
**Next:** Day 6 — Strings: creation, indexing, slicing, and string methods
**Related:** Day 7 — Operators (used with all data types)

---

## Code Created This Day
| Item | Name / Example | Purpose |
|------|----------------|---------|
| .py file | data_types_demo.py | None, int, float, type casting demo |
| .py file | input_demo.py | Accepting runtime input |
| .py file | bool_complex_demo.py | Boolean and complex types |
| .py file | string_overview.py | String creation and dir/help |

---

## 1. What Is a Data Type?

A **data type** tells Python what kind of value is stored in a variable.

```python
# Python decides the data type automatically (dynamically typed):
a = 10         # int
a = 10.5       # float
a = "Durga"    # str
a = True       # bool
a = None       # NoneType
```

Use `type()` to check:
```python
print(type(10))       # <class 'int'>
print(type(10.5))     # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
print(type(None))     # <class 'NoneType'>
```

---

## 2. Python Data Types Overview

```
Python Data Types
├── Basic Data Types
│   ├── NoneType    → None
│   └── Numeric
│       ├── int     → 10, -5, 0
│       ├── float   → 10.5, -3.14
│       ├── bool    → True, False
│       └── complex → 2+3j, 4-1j
│
└── Sequence / Data Structures (covered in later sessions)
    ├── str         → "hello"
    ├── list        → [1, 2, 3]
    ├── tuple       → (1, 2, 3)
    ├── set         → {1, 2, 3}
    ├── dict        → {"key": "value"}
    ├── range       → range(0, 10)
    ├── bytes       → b"hello"
    ├── bytearray   → bytearray(5)
    └── frozenset   → frozenset({1, 2, 3})
```

---

## 3. None Type

### What Is None?

`None` represents the **absence of a value**. It is Python's equivalent of `null` in Java, C#, etc.

```python
# Other languages use 'null' → NOT valid in Python:
k = null      # NameError: name 'null' is not defined

# Python uses 'None':
k = None
print(k)           # None
print(type(k))     # <class 'NoneType'>
```

### When to Use None

- When you want to declare a variable but not assign a value yet
- As a default return value for functions that don't return anything
- As a placeholder

```python
result = None     # declared, no value yet

# Later in the program:
result = 42       # now assigned a real value
print(type(result))   # <class 'int'>
```

> **Interview Question:** What is `None` in Python?
> **Answer:** `None` is a special constant representing the absence of a value. It is Python's equivalent of `null`. It has its own data type called `NoneType`. Use `if x is None:` to check for it.

---

## 4. Integer (int)

An integer is a whole number — positive, negative, or zero. No decimal point.

```python
a = 10
b = -5
c = 0

print(type(a))    # <class 'int'>
print(type(b))    # <class 'int'>
```

Python integers have **no size limit** — they can be as large as your memory allows (unlike Java's `int` which is 32-bit).

---

## 5. Float

A float is a number with a decimal point.

```python
a = 10.5
b = -3.14
c = 0.0

print(type(a))    # <class 'float'>
```

---

## 6. Type Casting (Type Conversion)

**Type casting** is converting a value from one data type to another.

```
Type casting functions:
int()     → converts to integer
float()   → converts to float
str()     → converts to string
bool()    → converts to boolean
complex() → converts to complex
```

### int → float

```python
a = 10                   # integer
b = float(a)             # convert to float
print(a, type(a))        # 10  <class 'int'>
print(b, type(b))        # 10.0  <class 'float'>
```

### float → int (truncates — does NOT round)

```python
a = 10.9
b = int(a)
print(b)          # 10  (not 11 — decimal part is dropped)
print(type(b))    # <class 'int'>
```

> **Important:** `int()` truncates — it drops the decimal part. It does NOT round. `int(10.9)` = 10, `int(10.1)` = 10.

### str → int and str → float

```python
s = "100"          # this is a string, not a number
n = int(s)         # convert string to int
print(n + 5)       # 105

s2 = "3.14"
f = float(s2)
print(f + 1)       # 4.140000000000001
```

> **Note:** You can only convert strings that contain valid numbers. `int("abc")` raises a `ValueError`.

---

## 7. The input() Function — Runtime Input

### What Is input()?

`input()` is a built-in function that **accepts a value from the user at runtime** (while the program is running).

```python
name = input("Enter your name: ")
print("Your name is", name)
```

```
Run output:
Enter your name: Mohan
Your name is Mohan
```

### Critical Rule: input() Always Returns a String

> **Very Important:** Whatever value the user types — numbers, words, anything — `input()` always returns it as a **string**.

```python
a = input("Enter num1: ")
print(type(a))    # <class 'str'>   ← even if user types 10, it is '10' (string)
```

**The string concatenation problem:**

```python
a = input("Enter num1: ")   # user types 10 → a = "10" (string)
b = input("Enter num2: ")   # user types 20 → b = "20" (string)
c = a + b
print("Result:", c)
# Output: Result: 1020   ← WRONG! '10' + '20' = '1020' (string concat, not addition)
```

**The fix — type casting:**

```python
a = input("Enter num1: ")   # "10" (string)
b = input("Enter num2: ")   # "20" (string)

# Convert to int before adding:
x = int(a)    # 10 (integer)
y = int(b)    # 20 (integer)
c = x + y
print("Result:", c)    # Result: 30   ← CORRECT
```

**Shortcut — convert directly inside input():**

```python
a = int(input("Enter num1: "))     # accepts input AND converts to int immediately
b = int(input("Enter num2: "))
print("Result:", a + b)            # Result: 30
```

**For float input:**

```python
a = float(input("Enter num1: "))   # accepts floats like 23.45
b = float(input("Enter num2: "))
print("Result:", a + b)
```

```
Run:
Enter num1: 23
Enter num2: 45.67
Result: 68.67
```

> **Common Mistake:** Forgetting to cast input() result to int/float. Always cast when you need arithmetic operations on user input.

```
Data flow:
User types "10"  →  input() returns "10" (str)  →  int("10")  →  10 (int)
```

### print() vs input()

| Function | Purpose | Returns |
|----------|---------|---------|
| `print()` | Displays output to user | Nothing (None) |
| `input()` | Accepts input from user at runtime | Always a string (str) |

---

## 8. Boolean (bool)

**bool** stores only two values: `True` or `False`.

```python
a = True
b = False

print(type(a))    # <class 'bool'>
print(type(b))    # <class 'bool'>
```

> **Case sensitivity:** `True` and `False` must have capital T and F. `true` or `false` gives a `NameError`.

### Boolean from Conditions

Booleans are typically the result of comparisons:

```python
a = 10
b = 20

c = (a < b)
print(c)           # True
print(type(c))     # <class 'bool'>

c = (a > b)
print(c)           # False
```

### True = 1, False = 0

Internally, Python treats `True` as `1` and `False` as `0`:

```python
# Convert bool to int:
print(int(True))    # 1
print(int(False))   # 0

# Arithmetic with booleans:
print(True + True)    # 2   (1 + 1)
print(9 + True)       # 10  (9 + 1)
print(5 + False)      # 5   (5 + 0)
print(True + True + True)   # 3

# Convert int to bool:
print(bool(1))    # True
print(bool(0))    # False
print(bool(5))    # True  (any non-zero number is True)
```

> **Interview Question:** What are the two values of bool in Python, and what are their integer equivalents?
> **Answer:** `True` and `False`. Internally, `True` = 1 and `False` = 0. Python represents any non-zero integer as `True` and zero as `False`.

---

## 9. Complex Numbers (complex)

A complex number has two parts:
- **Real part**
- **Imaginary part**

In mathematics, imaginary is written as `i`. In Python, it is written as **`j`** (not `i`).

```
Mathematical form:  a + bi
Python form:        a + bj
```

```python
a = 2 + 3j
b = 4 + 6j

print(a)           # (2+3j)
print(type(a))     # <class 'complex'>

# Extract real and imaginary parts:
print(a.real)      # 2.0
print(a.imag)      # 3.0

# Add two complex numbers:
c = a + b
print(c)           # (6+9j)
```

**Creating complex using complex() function:**

```python
x = 2
y = 3
c = complex(x, y)
print(c)            # (2+3j)
print(type(c))      # <class 'complex'>
```

> **Note:** `complex` is rarely used in everyday Python programming. It is used in scientific applications, engineering, analytical calculations, and MATLAB-type programs.

---

## 10. Key Differences — Basic Data Types

| Data Type | Values | Example | Use Case |
|-----------|--------|---------|---------|
| `int` | Whole numbers | `10, -5, 0` | Counting, indexing |
| `float` | Decimal numbers | `3.14, -0.5` | Measurements, calculations |
| `bool` | True or False | `True, False` | Conditions, flags |
| `complex` | Real + imaginary | `2+3j` | Scientific/engineering |
| `NoneType` | None only | `None` | No value / placeholder |

---

## 11. Data Structures Overview (Sequence Data Types)

The instructor gave a brief overview — detailed coverage in later sessions.

### String (str)

A string is a **sequence of characters** (group of characters).

```python
# Creating strings — 4 ways:
s1 = 'Durga'              # single quotes
s2 = "Durga"              # double quotes
s3 = '''Durga Soft'''     # triple single quotes
s4 = """Durga Soft"""     # triple double quotes

print(type(s1))   # <class 'str'>
```

**Why double quotes are preferred:**

```python
# Problem with single quotes containing an apostrophe:
s = 'Durga's'    # SyntaxError!

# Fix with backslash:
s = 'Durga\'s'   # works

# Better: use double quotes:
s = "Durga's"    # no issue
```

**Triple quotes for multi-line strings:**

```python
s = """
Durga Soft
Hyderabad
Python Course
"""
print(s)
# Output (multi-line):
# Durga Soft
# Hyderabad
# Python Course
```

**No `char` type in Python:**
```python
c = 'x'
print(type(c))    # <class 'str'>   ← not 'char', still a string
```

### Getting String Methods — dir() and help()

```python
# List all string methods:
print(dir(str))
# Output: ['capitalize', 'casefold', 'center', 'count', 'endswith',
#           'find', 'format', 'index', 'join', 'lower', 'lstrip', ...]

# Full documentation for string:
help(str)
# Shows each method with its description and parameters
```

You can do the same for any data structure:
```python
print(dir(list))   # list methods
help(list)         # list documentation
```

> **Tip for beginners:** Instead of memorizing all methods, use `dir()` to see what's available and `help()` to understand how each method works.

---

## 12. Complete Class Walkthrough

**Step 1:** Open PyCharm → open existing project

**Step 2:** Create `data_types_demo.py`:
```python
# None type
k = None
print(k)           # None
print(type(k))     # <class 'NoneType'>

# Assign a value later
k = 10
print(k)           # 10
print(type(k))     # <class 'int'>
```

**Step 3:** Type casting demo:
```python
# int to float
a = 10
b = float(a)
print(a, type(a))    # 10 <class 'int'>
print(b, type(b))    # 10.0 <class 'float'>

# float to int
a = 10.9
b = int(a)
print(b)             # 10 (truncated, not rounded)
```

**Step 4:** Create `input_demo.py` — the string problem:
```python
# Incorrect (string concatenation instead of addition):
a = input("Enter num1: ")
b = input("Enter num2: ")
print("Result:", a + b)         # "1020" — WRONG

# Correct (cast to int):
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
print("Result:", a + b)         # 30 — CORRECT
```

**Step 5:** Boolean demo:
```python
a = 10
b = 20
c = (a < b)
print(c)           # True
print(type(c))     # <class 'bool'>
print(int(True))   # 1
print(int(False))  # 0
print(True + True) # 2
print(9 + True)    # 10
```

**Step 6:** Complex demo:
```python
a = 2
b = 3
c = complex(a, b)
print(c)            # (2+3j)
print(c.real)       # 2.0
print(c.imag)       # 3.0

x = 2 + 3j
y = 4 + 6j
print(x + y)        # (6+9j)
```

**Step 7:** String and dir/help:
```python
s = "Durga"
print(type(s))       # <class 'str'>
print(dir(str))      # list of string methods
# help(str)          # full docs (outputs a lot — use in IDLE)
```

---

## Common Errors — Day 5

| Error | Cause | Fix |
|-------|-------|-----|
| `NameError: name 'null' is not defined` | Using `null` instead of `None` | Use `None` (capital N) |
| `NameError: name 'true' is not defined` | Using lowercase `true` | Use `True` (capital T) |
| `Result: 1020` instead of `30` | Forgot to cast `input()` to `int` | Use `int(input(...))` |
| `ValueError: invalid literal for int() with base 10: '3.14'` | Trying to use `int()` on a float string | Use `float()` first, then `int()`: `int(float("3.14"))` |
| `ValueError: invalid literal for int() with base 10: 'abc'` | Passing non-numeric string to `int()` | Validate input or handle with try/except |
| `SyntaxError: invalid syntax` on `int a = 10` | Using Java/C data type syntax | Remove `int` — just write `a = 10` |

---

## Interview Questions — Day 5

**Q: What are the basic data types in Python?**
A: NoneType (`None`), and Numeric types: `int`, `float`, `bool`, and `complex`.

**Q: What is `None` in Python?**
A: `None` is a special constant representing the absence of a value. It is equivalent to `null` in Java or C#. Its type is `NoneType`.

**Q: Why does `input()` cause problems in arithmetic operations?**
A: `input()` always returns a string. Even if the user types `10`, Python receives `"10"` (a string). Adding two strings concatenates them (`"10" + "20" = "1020"`). You must cast with `int()` or `float()` to do arithmetic.

**Q: What is type casting?**
A: Type casting is converting a value from one data type to another. Functions: `int()`, `float()`, `str()`, `bool()`, `complex()`.

**Q: What happens when you convert `float` to `int`?**
A: The decimal part is **truncated** (not rounded). `int(10.9)` gives `10`, not `11`.

**Q: What are True and False equal to numerically in Python?**
A: `True` equals `1` and `False` equals `0`. So `True + True` = `2`, `9 + True` = `10`, `5 + False` = `5`.

**Q: How is imaginary part represented in Python complex numbers?**
A: Using `j` (not `i`). Example: `2 + 3j`. The real part is `2`, imaginary part is `3`.

**Q: Does Python have a `char` data type?**
A: No. Python has no `char` type. Even a single character like `'x'` is of type `str`.

**Q: What is the difference between `print()` and `input()`?**
A: `print()` is an output function — it displays values to the user. `input()` is an input function — it accepts a value from the user at runtime and always returns it as a string.

**Q: How do you find all methods available for a data type?**
A: Use `dir(type_name)` to list all methods. Example: `print(dir(str))`. Use `help(str)` for full documentation.

---

## Key Differences: int vs float vs bool vs complex vs None

| Feature | int | float | bool | complex | NoneType |
|---------|-----|-------|------|---------|----------|
| Example | `10` | `10.5` | `True` | `2+3j` | `None` |
| Decimal | No | Yes | No | Yes (imag) | — |
| Values | Any integer | Any decimal | True/False only | Real + Imaginary | Only `None` |
| Integer value | itself | itself | True=1, False=0 | — | — |
| Type keyword | `int` | `float` | `bool` | `complex` | `NoneType` |

---

## Try It Yourself — Day 5

**Exercise 1:** Experiment with `None` and type checking:
```python
x = None
print(x)
print(type(x))

x = 99
print(x)
print(type(x))
```

**Exercise 2:** Practice type casting:
```python
# Try each conversion and check type:
a = int(3.9)
b = float(5)
c = int("42")
d = str(100)
e = bool(0)
f = bool(99)

for val in [a, b, c, d, e, f]:
    print(val, "→", type(val))
```

**Exercise 3:** Fix the input program (the common mistake):
```python
# Run this as-is first — observe wrong output:
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("Sum:", num1 + num2)     # shows concatenation

# Now fix it:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)     # shows addition
```

**Exercise 4:** Explore booleans with comparisons:
```python
print(5 > 3)        # True
print(5 < 3)        # False
print(5 == 5)       # True
print(5 != 3)       # True

print(int(True))    # 1
print(int(False))   # 0
print(bool(0))      # False
print(bool(42))     # True
print(bool(""))     # False
print(bool("hi"))   # True
```

**Exercise 5:** Create a mini calculator that accepts two numbers from the user at runtime and prints sum, difference, product, and quotient:
```python
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
if b != 0:
    print("Division:", a / b)
else:
    print("Cannot divide by zero")
```
