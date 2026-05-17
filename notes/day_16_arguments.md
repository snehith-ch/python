# Day 16 — Function Arguments: Positional, Keyword, Default, *args, **kwargs

← [Day 15](day_15_functions_basics.md) | [Index](00_INDEX.md) | [Day 17](day_17_special_functions.md) →

---

## Quick Revision

| # | Concept | One-line Summary |
|---|---------|-----------------|
| 1 | Formal arguments | Parameters listed in `def` — the placeholders |
| 2 | Actual arguments | Values passed at call time |
| 3 | Positional arguments | Matched by position; count must match exactly |
| 4 | Keyword arguments | Passed by name; order doesn't matter |
| 5 | Default arguments | Pre-set value used when caller skips that param |
| 6 | Non-default rule | Non-default params must come BEFORE default params |
| 7 | `*args` | Accepts any number of positional values → stored as tuple |
| 8 | `**kwargs` | Accepts any number of keyword values → stored as dict |
| 9 | Zero args allowed | `*args` and `**kwargs` both accept zero arguments |
| 10 | Mixing rule | Positional args must come before keyword args in a call |

---

## 1. Formal vs Actual Arguments

```python
def greet(name):        # 'name' is a FORMAL argument (in the definition)
    print("Hello", name)

greet("Snehith")        # "Snehith" is the ACTUAL argument (at the call)
```

- **Formal arguments** = the variable names inside `def`
- **Actual arguments** = the values you pass when calling the function

---

## 2. Positional Arguments

Values matched to parameters **in order**. Count must match exactly.

```python
def student(name, course, marks):
    print(name, course, marks)

student("Snehith", "Python", 90)   # OK — 3 values, 3 params
# student("Snehith", "Python")     # TypeError: missing 1 required argument
# student("Snehith", 90, "Python") # runs but gives wrong assignment
```

**Rules:**
- Order matters — first value → first param, second → second, etc.
- Wrong count → `TypeError`
- Wrong order → wrong values assigned (no error, but wrong output)

---

## 3. Keyword Arguments

Values passed **by parameter name**. Order doesn't matter.

```python
def student(name, course, marks):
    print(name, course, marks)

student(course="Python", marks=90, name="Snehith")   # order doesn't matter
student(name="Alice", marks=85, course="Java")        # same function, different order
```

**Rules:**
- Use `param=value` syntax at the call site
- All parameters must still be covered
- Positional args must come before keyword args in a single call

```python
# Mixing positional and keyword — positional FIRST
student("Snehith", marks=90, course="Python")   # OK
# student(name="Snehith", "Python", 90)         # SyntaxError — keyword before positional
```

---

## 4. Default Arguments

A parameter with a **pre-set value** used when the caller doesn't provide one.

```python
def student(name, course="Python", marks=0):
    print(name, course, marks)

student("Snehith")                      # uses defaults: Python, 0
student("Alice", "Java")               # overrides course; marks=0
student("Bob", "C++", 95)             # overrides both defaults
```

**Critical rule — non-default BEFORE default:**

```python
# CORRECT:
def f(a, b, c=10):       # non-defaults (a, b) before default (c)
    pass

# WRONG:
# def f(a=10, b, c):     # SyntaxError: non-default argument follows default argument
```

---

## 5. Variable Length Arguments — `*args`

Accept **any number** of positional arguments, including zero.

```python
def total(*args):
    print(type(args))   # <class 'tuple'>
    print(args)
    s = 0
    for n in args:
        s += n
    print("Sum:", s)

total(10, 20, 30)        # args = (10, 20, 30)
total(1, 2, 3, 4, 5)    # args = (1, 2, 3, 4, 5)
total()                  # args = ()  — zero arguments allowed
```

- `*args` collects all extra positional values into a **tuple**
- The name `args` is convention — any name after `*` works (`*nums`, `*values`)
- Iterate with a `for` loop to process all values

---

## 6. Keyword Variable Length Arguments — `**kwargs`

Accept **any number** of keyword arguments, stored as a **dictionary**.

```python
def display(**kwargs):
    print(type(kwargs))   # <class 'dict'>
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)

display(name="Snehith", course="Python", marks=90)
# Output:
# {'name': 'Snehith', 'course': 'Python', 'marks': 90}
# name : Snehith
# course : Python
# marks : 90

display()   # kwargs = {}  — zero arguments allowed
```

- `**kwargs` collects keyword arguments into a **dict**
- Access keys and values with `.items()`, `.keys()`, `.values()`

---

## 7. Combining Argument Types

You can mix argument types — but order in the definition matters:

```
def f(positional, default=val, *args, **kwargs):
```

```python
def example(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

example(1, 2, 3, 4, x=5, y=6)
# a: 1
# b: 2
# args: (3, 4)
# kwargs: {'x': 5, 'y': 6}
```

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: missing N required positional arguments` | Too few positional args | Pass the correct number of values |
| `TypeError: takes N positional arguments but M were given` | Too many positional args | Reduce or use `*args` |
| `SyntaxError: non-default argument follows default argument` | Default param before non-default | Put non-defaults first |
| `TypeError: got multiple values for argument` | Param passed both positionally and by keyword | Use one or the other, not both |

---

## Interview Questions

1. What is the difference between formal and actual arguments?
2. What happens if you pass the wrong number of positional arguments?
3. Can you mix positional and keyword arguments in one call? What rule applies?
4. What is the restriction on default arguments relative to non-default arguments?
5. What type does `*args` produce inside the function?
6. What type does `**kwargs` produce inside the function?
7. Can `*args` and `**kwargs` accept zero arguments?
8. What is the order rule when combining all four argument types in one function definition?

---

## Try It Yourself

1. Write `describe(name, age, city="Hyderabad")`. Call it three ways: all positional, all keyword, mixed.
2. Write `multiply(*args)` that returns the product of all passed numbers. Test with 2, 3, and 5 arguments.
3. Write `profile(**kwargs)` that prints each key-value pair. Call it with name, age, and job.
4. Write `add(a, b=5)`. Call it as: `add(3)`, `add(3, 10)`, `add(b=20, a=1)`.
5. Try to write `def broken(a=1, b)` — observe the error. Explain why.

---

## Code Created

| Snippet | Purpose |
|---------|---------|
| `def f(name, course, marks)` → called with 3 positional values | Positional argument demo |
| `student(course="Python", marks=90, name="Snehith")` | Keyword argument demo |
| `def student(name, course="Python", marks=0)` | Default argument demo |
| `def total(*args)` with `for n in args` loop | Variable-length positional args |
| `def display(**kwargs)` with `.items()` loop | Variable-length keyword args |

---

← [Day 15](day_15_functions_basics.md) | [Index](00_INDEX.md) | [Day 17](day_17_special_functions.md) →
