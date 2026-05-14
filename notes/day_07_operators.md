# Day 7 — Python Operators

← [Day 6](day_06_strings_basics.md) | [Index](00_INDEX.md) | [Day 8](day_08_bitwise_operators.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | How many operator categories does Python have? | 7 (arithmetic, relational, assignment, logical, bitwise, membership, identity) |
| 2 | What does `//` do? | Floor division — divides and drops the decimal |
| 3 | What does `**` do? | Exponentiation (power) — `2**3 = 8` |
| 4 | What does `%` return? | Remainder (modulo) |
| 5 | What are the logical operators? | `and`, `or`, `not` (keywords, not symbols) |
| 6 | What does `in` operator do? | Checks if a value exists in a sequence |
| 7 | What does `is` operator do? | Checks if two variables point to the same object (same memory address) |
| 8 | `==` vs `is` difference? | `==` compares values; `is` compares memory addresses |
| 9 | What function returns memory address? | `id()` |
| 10 | What is `x //= 3` equivalent to? | `x = x // 3` |

---

## 1. Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `**` | Exponentiation | `2 ** 3` | `8` |
| `/` | Division | `10 / 3` | `3.3333...` (always float) |
| `//` | Floor Division | `10 // 3` | `3` (drops decimal) |
| `%` | Modulo | `10 % 3` | `1` (remainder) |

```python
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a ** b)   # 1000  (10 to the power 3)
print(a / b)    # 3.3333333333333335  — always returns float
print(a // b)   # 3  — floor division, always truncates
print(a % b)    # 1  — remainder only
```

### Key points
- `/` always returns a **float** even if result is a whole number: `10 / 2 → 5.0`
- `//` always **truncates** (same as int() on a float): `10 // 3 → 3`
- `%` is useful for: checking even/odd (`n % 2 == 0`), cycling through values

---

## 2. Relational (Comparison) Operators

Return either `True` or `False`.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `<` | Less than | `5 < 10` | `True` |
| `>` | Greater than | `5 > 10` | `False` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `5 >= 6` | `False` |
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |

```python
x = 15
print(x > 10)    # True
print(x == 15)   # True
print(x < 5)     # False
print(x != 20)   # True
print(x >= 15)   # True
print(x <= 14)   # False
```

---

## 3. Assignment Operators

Shorthand for updating a variable using an operation.

| Operator | Equivalent to | Example | After |
|----------|--------------|---------|-------|
| `=` | — | `x = 10` | `x = 10` |
| `+=` | `x = x + n` | `x += 5` | `x = 15` |
| `-=` | `x = x - n` | `x -= 3` | `x = 12` |
| `*=` | `x = x * n` | `x *= 2` | `x = 24` |
| `/=` | `x = x / n` | `x /= 4` | `x = 6.0` |
| `//=` | `x = x // n` | `x //= 2` | `x = 3` |
| `%=` | `x = x % n` | `x %= 2` | `x = 1` |
| `**=` | `x = x ** n` | `x **= 3` | `x = 1` |

```python
x = 10
x += 5     # x is now 15
x -= 3     # x is now 12
x *= 2     # x is now 24
x //= 4    # x is now 6
print(x)   # 6
```

---

## 4. Logical Operators

Used to combine conditions. These are **keywords** in Python, not symbols.

| Operator | Meaning | Returns True when |
|----------|---------|-------------------|
| `and` | Both conditions must be true | Left AND right are both True |
| `or` | At least one must be true | Left OR right is True |
| `not` | Reverses the condition | Condition is False |

```python
x = 10
y = 5

print(x > 5 and y > 3)    # True  (both True)
print(x > 5 and y > 10)   # False (second is False)
print(x > 5 or y > 10)    # True  (first is True)
print(x < 5 or y > 10)    # False (both False)
print(not(x > 5))          # False (reverses True)
print(not(x < 5))          # True  (reverses False)
```

### Truth table

| A | B | A and B | A or B |
|---|---|---------|--------|
| T | T | T | T |
| T | F | F | T |
| F | T | F | T |
| F | F | F | F |

---

## 5. Membership Operators

Check if a value **exists inside** a sequence (string, list, tuple, set, dict).

| Operator | Meaning |
|----------|---------|
| `in` | Returns True if value is found |
| `not in` | Returns True if value is NOT found |

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("mango" in fruits)       # False
print("mango" not in fruits)   # True

name = "Snehith"
print("neh" in name)           # True — works on strings too
print("xyz" not in name)       # True
```

---

## 6. Identity Operators

Check if two variables **point to the same object in memory** (same `id()`).

| Operator | Meaning |
|----------|---------|
| `is` | True if both point to the same object |
| `is not` | True if they point to different objects |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a           # c points to SAME object as a

print(a == b)       # True  — same values
print(a is b)       # False — different objects in memory
print(a is c)       # True  — same object

print(id(a))   # e.g. 140344501234
print(id(b))   # different number
print(id(c))   # same as id(a)
```

### `==` vs `is` — the key difference

```python
x = 10
y = 10
print(x == y)   # True  — same value
print(x is y)   # True  — Python caches small integers (-5 to 256)

p = 1000
q = 1000
print(p == q)   # True
print(p is q)   # False — large integers are NOT cached
```

### `id()` function

Returns the memory address of any object.

```python
name = "Snehith"
print(id(name))     # memory address (a large integer)

x = 10
y = x
print(id(x) == id(y))   # True — same object
```

---

## 7. All Operators Summary

| Category | Operators |
|----------|-----------|
| Arithmetic | `+  -  *  **  /  //  %` |
| Relational | `<  >  <=  >=  ==  !=` |
| Assignment | `=  +=  -=  *=  /=  //=  %=  **=` |
| Logical | `and  or  not` |
| Bitwise | `&  \|  ^  ~  <<  >>` (see Day 8) |
| Membership | `in  not in` |
| Identity | `is  is not` |

---

## 8. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `SyntaxError` with `&&` or `\|\|` | These are C/Java style — Python uses words | Use `and`, `or`, `not` |
| `5 = x` | Assignment goes left to right | Write `x = 5` |
| Confusing `=` with `==` | `=` assigns; `==` compares | Use `==` in conditions |
| `is` gives wrong result for large ints | Integer caching only for -5 to 256 | Use `==` for value comparison |

---

## 9. Interview Questions

1. What is the difference between `/` and `//` in Python?
2. What does the `%` operator return?
3. What is the difference between `==` and `is`?
4. What does `id()` return?
5. What are the membership operators?
6. What are the identity operators?
7. Are Python's logical operators keywords or symbols?
8. What does `x **= 3` mean?

---

## 10. Try It Yourself

```python
# 1. a=17, b=5. Print results of all 7 arithmetic operators.

# 2. x=7. Using one print per line, check: x>5, x==7, x<3, x!=7

# 3. age=20, salary=50000.
#    Print True if age > 18 AND salary > 30000.
#    Print True if age < 18 OR salary > 30000.

# 4. Create a list ["cat","dog","fish"]. Check if "dog" is in it and "bird" is not.

# 5. a = [1,2,3]; b = a; c = [1,2,3]
#    Check: a==b, a is b, a==c, a is c — predict before running!
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `10 / 3` → `3.333` | Division always returns float |
| `10 // 3` → `3` | Floor division drops decimal |
| `10 % 3` → `1` | Modulo returns remainder |
| `2 ** 10` → `1024` | Exponentiation |
| `x += 5` | Shorthand assignment |
| `"neh" in "Snehith"` | Membership check on string |
| `id(a) == id(b)` | Compare memory addresses |
| `a is b` | Identity check |
