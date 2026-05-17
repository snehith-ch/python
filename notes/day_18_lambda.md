# Day 18 — Lambda Functions, filter(), map(), reduce()

← [Day 17](day_17_special_functions.md) | [Index](00_INDEX.md) | [Day 19](day_19_modules.md) →

---

## Quick Revision

| # | Concept | One-line Summary |
|---|---------|-----------------|
| 1 | Lambda | Anonymous (nameless) single-expression function |
| 2 | Syntax | `lambda arguments: expression` |
| 3 | No `return` needed | The expression IS the return value |
| 4 | Best use | Passing a function as an argument to another function |
| 5 | `filter()` | Keeps only elements where the function returns `True` |
| 6 | `map()` | Applies function to every element; returns same-length result |
| 7 | `reduce()` | Reduces sequence to a single cumulative value |
| 8 | `reduce` import | Must `from functools import reduce` |
| 9 | `list()` wrapper | `filter` and `map` return iterators — wrap with `list()` |
| 10 | Lambda advantage | Replaces 4–8 lines of `def` with 1 concise line |

---

## 1. Lambda Functions

A lambda is an **anonymous function** — it has no name.

**Syntax:**
```
lambda arguments: expression
```

```python
# Regular function:
def square(n):
    return n * n

# Equivalent lambda:
square = lambda n: n * n

print(square(5))   # 25
```

- The expression is automatically returned — no `return` keyword
- Can have multiple arguments: `lambda a, b: a + b`

```python
add = lambda a, b: a + b
print(add(10, 20))   # 30

greet = lambda name: "Hello, " + name
print(greet("Snehith"))   # Hello, Snehith
```

---

## 2. Why Lambda?

**Without lambda** — extra function needed (8 lines):

```python
def is_even(n):
    return n % 2 == 0

nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(is_even, nums))
print(result)   # [2, 4, 6, 8]
```

**With lambda** — inline, 3 lines:

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda n: n % 2 == 0, nums))
print(result)   # [2, 4, 6, 8]
```

Lambda shines when you only need the function **once** and it's simple enough to fit on one line.

---

## 3. `filter(function, sequence)`

Keeps only the elements for which the function returns `True`.

```python
nums = [10, 15, 20, 25, 30, 35]

# Keep numbers > 20:
result = list(filter(lambda n: n > 20, nums))
print(result)   # [25, 30, 35]

# Keep even numbers:
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)   # [10, 20, 30]
```

- `filter()` returns an **iterator** — use `list()` to see the result
- Result has **fewer or equal** elements compared to the original

---

## 4. `map(function, sequence)`

Applies the function to **every element** — always returns the same number of elements.

```python
nums = [1, 2, 3, 4, 5]

# Square every element:
squares = list(map(lambda n: n * n, nums))
print(squares)   # [1, 4, 9, 16, 25]

# Double every element:
doubled = list(map(lambda n: n * 2, nums))
print(doubled)   # [2, 4, 6, 8, 10]
```

- `map()` returns an **iterator** — use `list()` to see the result
- Result always has the **same length** as the input sequence

**Comparison — filter vs map:**

| Feature | `filter()` | `map()` |
|---------|-----------|---------|
| Elements kept | Only where function returns `True` | All elements |
| Result length | ≤ original | Same as original |
| Function purpose | Decide yes/no | Transform each value |

---

## 5. `reduce(function, sequence)`

Reduces the entire sequence to a **single value** by applying the function cumulatively.

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, nums)
print(total)   # 15
# Trace: ((((1+2)+3)+4)+5) = 15

product = reduce(lambda a, b: a * b, nums)
print(product)   # 120
# Trace: ((((1*2)*3)*4)*5) = 120
```

- Must import from `functools`
- Takes two arguments at a time, reduces left to right
- Final result is a **single value** (int, float, string, etc.)

---

## 6. All Three Together — Side by Side

```python
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter: keep evens
evens = list(filter(lambda n: n % 2 == 0, nums))
print("filter:", evens)       # [2, 4, 6, 8, 10]

# map: square all
squares = list(map(lambda n: n ** 2, nums))
print("map:", squares)        # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# reduce: sum all
total = reduce(lambda a, b: a + b, nums)
print("reduce:", total)       # 55
```

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `NameError: reduce is not defined` | Forgot to import from functools | `from functools import reduce` |
| Lambda result not visible | Forgot to wrap in `list()` | `list(filter(...))` or `list(map(...))` |
| `SyntaxError` in lambda | Tried to write multi-line logic | Use `def` for complex logic |
| Lambda with `return` | Lambdas don't use `return` keyword | Remove `return`; just write the expression |

---

## Interview Questions

1. What is a lambda function? How is it different from a `def` function?
2. Write the syntax for a lambda that adds two numbers.
3. What does `filter()` do? What type does it return?
4. What does `map()` do? How is it different from `filter()`?
5. What does `reduce()` do? Which module must you import it from?
6. When should you use a lambda instead of a named function?
7. Can a lambda function have multiple arguments? Give an example.
8. What happens if you forget to wrap `filter()` or `map()` in `list()`?

---

## Try It Yourself

1. Write a lambda that cubes a number. Test it with 3, 4, and 5.
2. Use `filter()` with a lambda to keep only strings longer than 4 characters from `["hi", "hello", "hey", "python", "ok"]`.
3. Use `map()` with a lambda to convert a list of Celsius temperatures to Fahrenheit. Formula: `F = C * 9/5 + 32`.
4. Use `reduce()` to find the maximum value in a list without using `max()`.
5. Combine all three: start with numbers 1–20, filter odd numbers, map them to their squares, reduce to their sum.

---

## Code Created

| Snippet | Purpose |
|---------|---------|
| `lambda n: n * n` assigned to `square` | Basic lambda syntax |
| `lambda a, b: a + b` | Multi-argument lambda |
| `list(filter(lambda n: n % 2 == 0, nums))` | Filter even numbers |
| `list(map(lambda n: n ** 2, nums))` | Square all elements |
| `reduce(lambda a, b: a + b, nums)` | Sum entire list to one value |

---

← [Day 17](day_17_special_functions.md) | [Index](00_INDEX.md) | [Day 19](day_19_modules.md) →
