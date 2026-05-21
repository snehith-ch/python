# Day 41 — Decorators and Generators

← [Day 40](day_40_multithreading.md) | [Index](00_INDEX.md) | [Day 42](day_42_assertion_logging.md) →

---

## Quick Revision — Day 41

| # | Key Point |
|---|-----------|
| 1 | **Decorator** = a function that takes another function as argument, extends its functionality, and returns modified function |
| 2 | Main objective: extend existing function functionality **without modifying** the original function |
| 3 | Built-in decorators (used earlier): `@classmethod`, `@staticmethod`, `@abstractmethod` |
| 4 | User-defined decorator syntax: `@decorator_name` placed before function definition |
| 5 | Alternative: `d = decorator(f1)` then call `d(args)` to apply decorator without `@` symbol |
| 6 | **Generator** = a function that uses `yield` keyword to return values (not `return`) |
| 7 | `yield` returns value **without destroying local variable state** — resumes from last yield |
| 8 | Generator vs list: generators do NOT store all values in memory — ideal for huge data |
| 9 | Generator expression uses round brackets: `g = (x for x in range(10))` |
| 10 | `next(g)` retrieves the next value from a generator object |

---

## Navigation

- **Pre-requisite:** [Day 40](day_40_multithreading.md) — Multithreading; [Day 28](day_28_oops_advanced.md) — Built-in decorators (`@classmethod`, `@staticmethod`, `@abstractmethod`)
- **Next:** [Day 42](day_42_assertion_logging.md) — Assertion and Logging
- **Related:** [Day 27](day_27_oops_basics.md) — Functions and classes

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| Function | `decor(a_fun)` | User-defined decorator function |
| Pattern | `@decor` | Apply decorator to a function |
| Pattern | `d = decor(f1); d(args)` | Apply decorator without `@` symbol |
| Keyword | `yield` | Return value from generator without losing state |
| Expression | `(x for x in range(n))` | Generator expression (round brackets) |
| Function | `next(g)` | Get next value from generator |
| Pattern | `for val in generator_func():` | Iterate all values from generator |

---

## 1. Decorators

### 1.1 What Is a Decorator?

```
Decorator
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A function that:
  1. Takes another function as an argument/parameter
  2. Extends its functionality
  3. Returns the modified function with extended functionality

Main objective: extend existing functions WITHOUT modifying them
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Example from OOP:** `@abstractmethod` decorator was added to method `M1` to make it abstract — without changing `M1`'s own logic, the decorator added the abstract behavior.

### 1.2 User-Defined Decorator — Basic Example

**Requirement:** `f1(name)` always says "Good morning". For the name "Durga", we want "Good evening" instead — **without modifying `f1`**.

```python
def f1(name):
    print(f"Hello {name}")
    print("Good morning")


def decor(a_fun):               # decorator function — takes f1 as argument
    def inner(name):            # inner function — same params as f1
        if name == "Durga":
            print("Hello Durga")
            print("Good evening")    # different message for Durga
        else:
            a_fun(name)             # call original f1 for all other names
    return inner                # return the inner function


@decor                          # apply decorator to f1
def f1(name):
    print(f"Hello {name}")
    print("Good morning")


f1("Psi")     # → Hello Psi / Good morning
f1("Mohan")   # → Hello Mohan / Good morning
f1("Durga")   # → Hello Durga / Good evening  ← different!
```

**How it works with `@decor`:**
```
When f1("Durga") is called:
  1. Python sees @decor → calls decor(f1) first
  2. decor receives f1 as a_fun
  3. inner(name) executes with name="Durga"
  4. name == "Durga" is True → prints Good evening
  5. For other names → calls original f1(name)
```

### 1.3 Decorator Without `@` Symbol (Object Style)

```python
# Same decorator and f1 as above, but WITHOUT @decor

def f1(name):
    print(f"Hello {name}")
    print("Good morning")

# Apply decorator by creating a decorator object
d = decor(f1)    # d is now the decorator-wrapped version of f1

# Call WITH decorator
d("Durga")       # → Good evening
d("Psi")         # → Good morning

# Call WITHOUT decorator (original function)
f1("Mohan")      # → Good morning (unchanged)
```

> Both `@decor` and `d = decor(f1)` achieve the same result. The `@` symbol is just syntactic sugar.

### 1.4 Decorator for Exception Handling

```python
def smart_division(division):
    def inner(a, b):
        if b == 0:
            print("Cannot divide")
            return
        else:
            return division(a, b)
    return inner


@smart_division
def division(a, b):
    print(f"Result: {a / b}")


division(20, 2)    # → Result: 10.0
division(20, 0)    # → Cannot divide  (no ZeroDivisionError!)
```

> The decorator handles the error **without modifying** the `division` function's core logic.

---

## 2. Generators

### 2.1 What Is a Generator?

```
Generator
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A function which is responsible to generate a sequence of values.
Uses yield keyword instead of return.

How to recognize a generator function:
  → Function body contains yield keyword
  → (If return/print → normal function)
  → (If yield → generator function)

Main advantage: generates huge values WITHOUT memory error
Best use case: reading large data from files or databases
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2.2 Generator Expression vs List Expression

```python
# List expression — stores ALL values in memory upfront
L = [x for x in range(10)]    # uses [] square brackets
print(type(L))                 # <class 'list'>

# Generator expression — generates values ON THE FLY
g = (x for x in range(10))    # uses () round brackets
print(type(g))                 # <class 'generator'>
```

**Memory problem with lists:**
```python
# 10 lakh values → takes time to load
L = [x for x in range(1000000)]    # possible but slow
# 10 crore values → MEMORY ERROR
L = [x for x in range(100000000)]  # will crash with MemoryError
```

**No memory problem with generators:**
```python
# Any number of values → no memory error
g = (x for x in range(100000000))    # works fine
for val in g:
    print(val)    # generates values on the fly, one at a time
```

> Generator does NOT store all values in memory at the start. Values are generated **on the fly** as you iterate. That is why generators can handle crore/lakh values without memory errors.

### 2.3 Generator Function with yield

```python
def f1():
    yield 1        # yield — not return
    yield "Psi"
    yield "HYD"
    yield 25


# Iterating generator function
for i in f1():
    print(i)
# Output: 1, Psi, HYD, 25

# Generator object
g = f1()           # g is a generator object
print(type(g))     # <class 'generator'>

# Using next()
print(next(g))     # 1
print(next(g))     # Psi
print(next(g))     # HYD
print(next(g))     # 25
# print(next(g))   # StopIteration error — no more values
```

### 2.4 yield Keyword — Key Behavior

```python
def counter():
    yield 1    # stops here, returns 1, saves state
    yield 2    # on next call, resumes here, returns 2
    yield 3    # resumes here on third call

g = counter()
print(next(g))    # 1 — pauses at first yield
print(next(g))    # 2 — resumes from yield 2
print(next(g))    # 3 — resumes from yield 3
```

> `yield` is used to return from a function **without destroying the state of its local variables**. When the function is called again, execution resumes from the **last yield statement** — not from the beginning.

---

## 3. Generator vs Normal Collection

| Feature | Normal List | Generator |
|---------|-------------|-----------|
| Brackets | `[x for x in ...]` | `(x for x in ...)` |
| Type | `list` | `generator` |
| Memory | All values stored upfront | Values generated one at a time |
| Huge data | May cause MemoryError | No memory issue |
| Access | Index access `L[0]` | `next(g)` or `for` loop |
| Iteration | Can iterate multiple times | Can iterate only once |

## 4. yield vs return

| Feature | `return` | `yield` |
|---------|----------|---------|
| Function type | Normal function | Generator function |
| After executing | Function terminates | Function pauses, saves state |
| Called again | Starts from beginning | Resumes from last yield |
| Memory | Executes once | Can produce infinite sequence |
| Value count | One value per call | Multiple values per call |

---

## Student Q&A

> **Student Question:** What is a decorator in Python?
> **Answer:** A decorator is a function that takes another function as an argument, extends its functionality without modifying the original function, and returns the modified function. You apply it using the `@decorator_name` syntax before a function definition. The main purpose is to add extra behavior to existing functions without touching their code.

> **Student Question:** What is the difference between `@decor` syntax and the `d = decor(f1)` approach?
> **Answer:** Both do the same thing. `@decor` placed before a function definition is syntactic sugar — it automatically wraps the function with the decorator. `d = decor(f1)` manually creates a decorator object and you call it as `d(args)`. With `@decor`, calling `f1(args)` automatically applies the decorator. Without `@decor`, you can still call `f1(args)` using the original behavior, while `d(args)` uses the decorated version.

> **Student Question:** What is the difference between a generator function and a normal function?
> **Answer:** A normal function uses `return` or `print` to output values and terminates after execution. A generator function uses `yield` to return values — after yielding, the function pauses and saves its state. When called again, it resumes from the last yield statement. Generators can produce a sequence of values over multiple calls without restarting. They also avoid memory errors for huge datasets since values are generated on the fly.

> **Student Question:** What is the advantage of generators over lists?
> **Answer:** Lists store all values in memory at once — for huge datasets (lakhs or crores of values), this causes MemoryError. Generators produce values one at a time on the fly — no values are stored in memory beforehand. This makes generators ideal for reading large files or database records. The cost is that generators can only be iterated once (no index access).

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `StopIteration` | Calling `next()` after generator is exhausted | Use `for` loop or check with `try-except StopIteration` |
| Decorator not applying | Forgot `@` symbol or applied to wrong function | Add `@decorator_name` directly above the function definition |
| Generator not creating | Used `[]` instead of `()` | Use round brackets `()` for generator expression |
| `MemoryError` | Used list for huge data | Switch to generator expression with `()` |

---

## Interview Questions

**Q: What is a decorator in Python?**
A: A decorator is a function that takes another function as a parameter, extends its functionality without modifying it, and returns the modified function. It is applied using `@decorator_name` syntax. Python provides built-in decorators like `@classmethod`, `@staticmethod`, and `@abstractmethod`, and you can create user-defined decorators. The main use is to add extra behavior (like logging, authentication, exception handling) to existing functions.

**Q: What is a generator function?**
A: A generator function is a function that uses the `yield` keyword to return values instead of `return`. When `yield` is encountered, the function pauses and saves its state. On the next call, execution resumes from the last yield statement. A function containing `yield` is automatically treated as a generator function. Generators are used to produce large sequences of values without storing them all in memory.

**Q: What is the difference between `yield` and `return`?**
A: `return` terminates the function and returns one value; the function's state is lost. `yield` pauses the function and returns a value, but preserves the function's state (local variables). When called again, execution resumes from the last yield statement rather than the beginning. `yield` makes a function a generator, capable of producing a sequence of values over multiple calls.

**Q: What are the advantages of generators over lists?**
A: (1) Memory efficiency — generators produce values one at a time on the fly; lists store all values upfront. (2) For huge datasets (lakhs/crores of values), lists cause MemoryError; generators handle any size. (3) Generators are best for reading large files or database records. The limitation is that generators can only be traversed once (no index access like lists).

---

## Try It Yourself

**Exercise 1:** Write a user-defined decorator `uppercase_decorator` that takes a function returning a string and converts the result to uppercase. Apply it to a function `greeting(name)` that returns `"hello, {name}"`.

<details><summary>Answer</summary>

```python
def uppercase_decorator(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return inner


@uppercase_decorator
def greeting(name):
    return f"hello, {name}"


print(greeting("alice"))    # HELLO, ALICE
```
</details>

---

**Exercise 2:** Write a generator function that generates the Fibonacci sequence indefinitely (0, 1, 1, 2, 3, 5, 8, ...). Print the first 10 values using `next()`.

<details><summary>Answer</summary>

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


g = fibonacci()
for _ in range(10):
    print(next(g))
# 0 1 1 2 3 5 8 13 21 34
```
</details>

---

**Exercise 3:** Write a generator expression that produces squares of numbers from 1 to 100. Use a `for` loop to print all values. Demonstrate why a generator is better than a list for this purpose.

<details><summary>Answer</summary>

```python
# Generator expression — no memory issue
squares_gen = (x*x for x in range(1, 101))
for val in squares_gen:
    print(val)

# vs list (stores all 100 values in memory — fine here, but not scalable)
squares_list = [x*x for x in range(1, 101)]
# For range(1, 10_000_001) — generator is better; list risks memory issues
```
</details>
