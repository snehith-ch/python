# Day 17 — Special Arguments, Aliasing, Nested Functions & Recursion

← [Day 16](day_16_arguments.md) | [Index](00_INDEX.md) | [Day 18](day_18_lambda.md) →

---

## Quick Revision

| # | Concept | One-line Summary |
|---|---------|-----------------|
| 1 | Positional-only `/` | Params before `/` can only be passed positionally |
| 2 | Keyword-only `*` | Params after `*` must be passed by keyword |
| 3 | Function aliasing | `f2 = f1` — both names point to the same function object |
| 4 | Same `id()` | Aliased names share identical `id()` — same memory object |
| 5 | Delete alias | `del f1` removes one name; the function still exists via `f2` |
| 6 | Nested function | A function defined inside another function |
| 7 | Inner scope | Inner function only accessible inside outer; outer must be called |
| 8 | Recursion | A function that calls itself; must have a base case |
| 9 | Base case | The stopping condition that prevents infinite recursion |
| 10 | `math` module | `sqrt`, `factorial`, `ceil`, `floor`, `pow` |

---

## 1. Positional-Only Arguments (`/`)

Place `/` in the parameter list. Everything **before** `/` must be passed positionally.

```python
def add(a, b, /):
    print(a + b)

add(10, 20)           # OK — positional
# add(a=10, b=20)    # TypeError: got some positional-only arguments passed as keyword arguments
```

Use case: when argument names are an implementation detail and should not be part of the public interface.

---

## 2. Keyword-Only Arguments (`*`)

Place `*` in the parameter list. Everything **after** `*` must be passed by keyword.

```python
def add(*, a, b):
    print(a + b)

add(a=10, b=20)   # OK — keyword
# add(10, 20)     # TypeError: takes 0 positional arguments but 2 were given
```

You can combine both in one function:

```python
def f(pos_only, /, normal, *, kw_only):
    print(pos_only, normal, kw_only)

f(1, 2, kw_only=3)           # OK
f(1, normal=2, kw_only=3)    # OK
```

---

## 3. Function Aliasing

Assign a function to another variable name — both point to the **same object**.

```python
def wish(name):
    print("Hello,", name)

greet = wish          # aliasing — greet is another name for wish

wish("Snehith")       # Hello, Snehith
greet("Alice")        # Hello, Alice

print(id(wish))       # same id
print(id(greet))      # same id — same object in memory
```

**After deleting one name:**

```python
del wish              # removes the name 'wish', NOT the function
greet("Bob")          # still works — function alive via 'greet'
# wish("Bob")         # NameError — 'wish' is gone
```

The function object is deleted from memory only when **all** names pointing to it are removed.

---

## 4. Nested Functions

A function defined **inside** another function.

```python
def outer():
    print("Outer starts")

    def inner():
        print("Inner runs")

    inner()            # must call inner from inside outer
    print("Outer ends")

outer()
# inner()   # NameError — inner is not visible outside outer
```

- The inner function is **local** to the outer function
- It only exists while outer is executing
- Outer must be called for inner to ever run

```python
# Practical use — inner uses outer's variable:
def outer():
    message = "Hello from outer"

    def inner():
        print(message)    # inner can see outer's variable (closure)

    inner()

outer()
```

---

## 5. Recursion

A function that **calls itself**. Every recursion must have a **base case** (stopping condition).

```python
def factorial(n):
    if n == 0:           # base case — stop here
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))   # 120
# Trace: 5 * factorial(4) → 5 * 4 * factorial(3) → ... → 5*4*3*2*1*1 = 120
```

**What happens without a base case:**

```python
def infinite(n):
    return n * infinite(n - 1)   # never stops → RecursionError
```

Python's default recursion limit is ~1000 calls (`sys.getrecursionlimit()`).

**Another example — sum of digits:**

```python
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

print(digit_sum(123))   # 6  (1+2+3)
```

---

## 6. `math` Module

```python
import math

print(math.sqrt(16))        # 4.0
print(math.factorial(5))    # 120
print(math.ceil(4.3))       # 5  — round UP
print(math.floor(4.9))      # 4  — round DOWN
print(math.pow(2, 10))      # 1024.0  — returns float
```

Compare with built-in `**` operator:

```python
print(2 ** 10)       # 1024  — int (built-in power)
print(math.pow(2, 10))  # 1024.0  — float (math module)
```

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: positional-only argument passed as keyword` | Using keyword for a `/` param | Pass it positionally |
| `TypeError: keyword-only argument` | Passing positionally after `*` | Pass it by keyword |
| `NameError: inner` called outside outer | Inner function is local to outer | Call inner from inside outer only |
| `RecursionError: maximum recursion depth exceeded` | Missing or wrong base case | Add/fix the base case |
| `NameError: name 'wish' is not defined` | Deleted the only name for the function | Keep at least one alias alive |

---

## Interview Questions

1. What does placing `/` in a function signature enforce?
2. What does placing `*` in a function signature enforce?
3. When you write `f2 = f1`, do `f1` and `f2` have the same `id()`? Why?
4. If you `del f1`, does the function get deleted from memory?
5. What is a nested function? Can you call the inner function from outside the outer?
6. What is recursion? What is a base case and why is it required?
7. What is the difference between `math.pow(2, 3)` and `2 ** 3`?
8. What happens if you exceed Python's recursion limit?

---

## Try It Yourself

1. Write `add(a, b, /)`. Try calling it with `add(a=1, b=2)` — observe the error.
2. Write `greet(*, name, message)`. Call it two ways: correct and incorrect.
3. Alias a function `square` as `sq`. Delete `square`. Confirm `sq` still works.
4. Write a nested function where `inner()` prints a variable defined in `outer()`.
5. Write a recursive function `power(base, exp)` that computes `base ** exp` without using `**`.

---

## Code Created

| Snippet | Purpose |
|---------|---------|
| `def add(a, b, /)` | Positional-only argument demo |
| `def add(*, a, b)` | Keyword-only argument demo |
| `greet = wish; del wish` | Function aliasing and deletion |
| `def outer()` containing `def inner()` | Nested function demo |
| `def factorial(n): if n == 0: return 1` | Recursion with base case |
| `math.sqrt / factorial / ceil / floor / pow` | `math` module methods |

---

← [Day 16](day_16_arguments.md) | [Index](00_INDEX.md) | [Day 18](day_18_lambda.md) →
