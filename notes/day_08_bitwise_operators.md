# Day 8 — Bitwise Operators & Control Flow Introduction

← [Day 7](day_07_operators.md) | [Index](00_INDEX.md) | [Day 9](day_09_control_flow.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | What function converts a number to binary in Python? | `bin()` |
| 2 | What prefix does binary notation use? | `0b` (e.g., `0b1010`) |
| 3 | What does `&` (AND) do on bits? | Returns 1 only when BOTH bits are 1 |
| 4 | What does `\|` (OR) do on bits? | Returns 1 when at LEAST ONE bit is 1 |
| 5 | What does `^` (XOR) do on bits? | Returns 1 when bits are DIFFERENT |
| 6 | What does `~` (NOT) do? | Flips all bits; result = `-(n+1)` |
| 7 | What does `<<` do? | Left shift — multiplies by 2 per shift |
| 8 | What does `>>` do? | Right shift — divides by 2 per shift |
| 9 | What are the 3 types of control flow? | Conditional, Iterative (loops), Transfer |
| 10 | PyCharm debug shortcut to step over? | `Fn + F8` (or F8 on some keyboards) |

---

## 1. Why Bitwise Operators?

Computers store all data in **binary (base-2)** — 0s and 1s. Bitwise operators work directly on the binary representation of numbers.

> **Note from instructor:** Bitwise operators are rarely used in everyday Python programming. They matter most in: embedded systems, networking (IP masking), cryptography, and performance-critical code.

---

## 2. Binary Basics

### Decimal to Binary conversion (manual)

Divide by 2, collect remainders from bottom to top:

```
10 ÷ 2 = 5  remainder 0
 5 ÷ 2 = 2  remainder 1
 2 ÷ 2 = 1  remainder 0
 1 ÷ 2 = 0  remainder 1
                         ↑ read upward
10 in binary = 1010
```

### Python — `bin()` function

```python
print(bin(10))    # 0b1010
print(bin(5))     # 0b101
print(bin(255))   # 0b11111111

# The 0b prefix just means "this is binary" — not part of the value
```

### Binary to decimal (powers of 2)

```
1010 = 1×2³ + 0×2² + 1×2¹ + 0×2⁰
     = 8    + 0    + 2    + 0
     = 10
```

---

## 3. Bitwise Operators

### & (AND)

Returns 1 only when **both** corresponding bits are 1.

```
a = 10  →  1 0 1 0
b =  5  →  0 1 0 1
a & b   →  0 0 0 0  = 0
```

```python
a = 10
b = 5
print(a & b)   # 0
print(bin(a & b))   # 0b0
```

```
a = 10  →  1 0 1 0
b =  6  →  0 1 1 0
a & b   →  0 0 1 0  = 2
```

```python
print(10 & 6)   # 2
```

### | (OR)

Returns 1 when **at least one** bit is 1.

```
a = 10  →  1 0 1 0
b =  5  →  0 1 0 1
a | b   →  1 1 1 1  = 15
```

```python
print(10 | 5)   # 15
```

### ^ (XOR — eXclusive OR)

Returns 1 when bits are **different**.

```
a = 10  →  1 0 1 0
b =  5  →  0 1 0 1
a ^ b   →  1 1 1 1  = 15

a = 10  →  1 0 1 0
b =  6  →  0 1 1 0
a ^ b   →  1 1 0 0  = 12
```

```python
print(10 ^ 5)    # 15
print(10 ^ 6)    # 12
```

### ~ (NOT — bitwise complement)

Flips all bits. Formula: `~n = -(n + 1)`

```python
print(~10)   # -11  (because -(10+1) = -11)
print(~5)    # -6
print(~0)    # -1
```

### << (Left Shift)

Shifts bits left by n positions. Each shift **multiplies by 2**.

```
10 = 1010
10 << 1 = 10100 = 20   (×2)
10 << 2 = 101000 = 40  (×4)
```

```python
print(10 << 1)   # 20
print(10 << 2)   # 40
print(10 << 3)   # 80
```

### >> (Right Shift)

Shifts bits right by n positions. Each shift **divides by 2** (integer division).

```
10 = 1010
10 >> 1 = 101 = 5   (÷2)
10 >> 2 = 10  = 2   (÷4)
```

```python
print(10 >> 1)   # 5
print(10 >> 2)   # 2
print(10 >> 3)   # 1
```

### Summary table

| Operator | Name | Rule | Example |
|----------|------|------|---------|
| `&` | AND | 1 only if both are 1 | `10 & 5 = 0` |
| `\|` | OR | 1 if at least one is 1 | `10 \| 5 = 15` |
| `^` | XOR | 1 if bits differ | `10 ^ 5 = 15` |
| `~` | NOT | flips all bits | `~10 = -11` |
| `<<` | Left shift | multiply by 2ⁿ | `10 << 2 = 40` |
| `>>` | Right shift | divide by 2ⁿ | `10 >> 2 = 2` |

---

## 4. Control Flow — Introduction

Control flow determines the **order** in which code executes. Python has 3 categories:

```
Control Flow Statements
├── Conditional     → if / else / elif / nested if
├── Iterative       → for loop / while loop
└── Transfer        → break / continue / pass
```

> Python has **NO**: `switch-case`, `do-while`, `for-each` (the for loop handles everything)

---

## 5. if / else / elif

```python
# Basic if
if condition:
    # runs if condition is True

# if-else
if condition:
    # runs if True
else:
    # runs if False

# if-elif-else
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition2 is True (and condition1 was False)
else:
    # runs if none of the above were True
```

### Example — grade calculator

```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Output: Grade: C
```

### Nested if

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Too young to vote")
```

---

## 6. Debugging in PyCharm

The instructor demonstrated PyCharm's debugger to trace if/elif conditions step by step.

| Action | How |
|--------|-----|
| Set a breakpoint | Click in the left margin (red dot appears) |
| Run in debug mode | Right-click → Debug (or bug icon) |
| Step over (next line) | `Fn + F8` (or `F8`) |
| See variable values | Watch panel / hover over variable |

**Why debug?** The debugger lets you pause execution and inspect values at each step — much faster than adding many `print()` statements.

---

## 7. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `SyntaxError` using `&` for logical AND | `&` is bitwise, not logical | Use `and` |
| `~10` gives `-11` (unexpected) | `~` does bitwise complement | Formula: `~n = -(n+1)` |
| `if x = 5:` | Single `=` is assignment, not comparison | Use `==` |
| Missing colon after `if` | `if condition` needs `:` | Write `if condition:` |
| `IndentationError` | Block not indented after `if` | Indent 4 spaces |

---

## 8. Interview Questions

1. What does `bin()` do in Python?
2. What is the result of `10 & 6`? Show the binary working.
3. What is the result of `~10`? Explain the formula.
4. What is the difference between `<<` and `>>`?
5. Left shift by 1 is equivalent to what arithmetic operation?
6. What are the three categories of control flow in Python?
7. Does Python have switch-case? What do you use instead?
8. What is the difference between multiple `if` statements and `elif`?

---

## 9. Try It Yourself

```python
# 1. Use bin() to see binary of: 7, 15, 64, 255

# 2. Compute and verify manually:
#    a) 12 & 10
#    b) 12 | 10
#    c) 12 ^ 10
#    d) ~12
#    e) 4 << 3
#    f) 64 >> 3

# 3. Write an if/elif/else to categorize a temperature:
#    >= 40: "Very Hot"
#    >= 30: "Hot"
#    >= 20: "Pleasant"
#    else:  "Cold"

# 4. Write a nested if: check if a number is positive,
#    then check if it is even or odd.
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `bin(10)` → `'0b1010'` | Binary representation |
| `10 & 6` → `2` | Bitwise AND |
| `10 \| 5` → `15` | Bitwise OR |
| `10 ^ 5` → `15` | Bitwise XOR |
| `~10` → `-11` | Bitwise NOT = -(n+1) |
| `10 << 2` → `40` | Left shift (×4) |
| `10 >> 2` → `2` | Right shift (÷4) |
| `if/elif/else` grade block | Conditional flow demo |
