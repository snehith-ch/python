# Day 9 — Control Flow: elif, for, while, break, continue, pass

← [Day 8](day_08_bitwise_operators.md) | [Index](00_INDEX.md) | [Day 10](day_10_strings_functions.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | What does `elif` mean? | "else if" — Python's keyword (NOT `else if` as two words) |
| 2 | Syntax of a for loop? | `for variable in sequence:` |
| 3 | How do you increment in Python? | `i += 1` — Python has NO `i++` |
| 4 | What does `break` do? | Stops the loop entirely |
| 5 | What does `continue` do? | Skips the current iteration, resumes from next |
| 6 | What does `pass` do? | Placeholder — does nothing, prevents empty-block error |
| 7 | What happens with multiple `if` vs `elif`? | Multiple `if`: all conditions checked; `elif`: stops at first True |
| 8 | Nested for loop — how many times does inner run? | Inner loop completes ALL iterations for each outer iteration |
| 9 | Risk with `continue` in a while loop? | Infinite loop if increment is placed after `continue` |
| 10 | Python has which loops? | `for` and `while` (no do-while, no for-each) |

---

## 1. elif — else-if in Python

Python uses the **single keyword** `elif` (not `else if` as two separate words).

```python
# WRONG — SyntaxError in Python:
# if x > 0:
#     print("positive")
# else if x < 0:       ← Python does NOT allow this
#     print("negative")

# CORRECT:
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
```

### Multiple `if` vs `elif` — critical difference

```python
marks = 85

# Using multiple if — EVERY condition is checked
if marks >= 90:
    print("A")
if marks >= 80:
    print("B")    # This ALSO runs because 85 >= 80 is True
if marks >= 70:
    print("C")    # This ALSO runs — all 3 print!

print("---")

# Using elif — stops at first True match
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")    # Runs — and stops here
elif marks >= 70:
    print("C")    # Skipped
```

**Rule:** Use `elif` when conditions are mutually exclusive (only one should apply). Use multiple `if` when each condition is independent.

---

## 2. for Loop

Iterates over any **sequence** (list, tuple, string, range, set, dict).

### Syntax

```python
for variable in sequence:
    # body (runs once per element)
```

### Examples

```python
# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop over a string
for char in "Python":
    print(char)

# Loop with range
for i in range(5):
    print(i)           # 0 1 2 3 4

for i in range(1, 6):
    print(i)           # 1 2 3 4 5

for i in range(1, 10, 2):
    print(i)           # 1 3 5 7 9

# Countdown
for i in range(10, 0, -1):
    print(i)           # 10 9 8 7 6 5 4 3 2 1
```

### No `i++` in Python

```python
# Python has NO increment operator:
# i++   ← SyntaxError
# ++i   ← SyntaxError (silently does nothing; actually parses as +(+i))

# Always use:
i += 1   # increment
i -= 1   # decrement
```

---

## 3. Nested for Loop

A for loop inside another for loop.

**Key rule:** For every **1 iteration of the outer loop**, the inner loop runs **all** its iterations.

```python
for i in range(1, 4):        # outer: 1, 2, 3
    for j in range(1, 4):    # inner: 1, 2, 3
        print(i, j)

# Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
```

### Multiplication table using nested for

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()   # newline after each row
```

### Star pattern example

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
```

---

## 4. while Loop

Runs **as long as** a condition is True. Use when you don't know how many iterations you need.

### Syntax

```python
while condition:
    # body
    # must have a way to eventually make condition False
```

### Examples

```python
# Count 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1     # must increment — otherwise infinite loop!

# Sum until user enters 0
total = 0
n = int(input("Enter number (0 to stop): "))
while n != 0:
    total += n
    n = int(input("Enter number (0 to stop): "))
print("Total:", total)
```

### while vs for — when to use which

| for loop | while loop |
|----------|------------|
| Number of iterations known | Number of iterations unknown |
| Iterating over a sequence | Repeating until a condition |
| `for i in range(10):` | `while user_input != "quit":` |

---

## 5. break

**Stops the loop entirely** — exits immediately, skips the rest.

```python
for i in range(1, 11):
    if i == 5:
        break      # stops when i reaches 5
    print(i)

# Output: 1 2 3 4
```

```python
# Find first even number
numbers = [3, 7, 11, 4, 9, 2]
for n in numbers:
    if n % 2 == 0:
        print("First even:", n)
        break
# Output: First even: 4
```

---

## 6. continue

**Skips the current iteration** — jumps to the next one. Loop does NOT stop.

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue   # skip even numbers
    print(i)

# Output: 1 3 5 7 9
```

### Critical — `continue` in while loop

If you use `continue` in a `while` loop, make sure the **increment comes BEFORE `continue`**, otherwise the loop runs forever.

```python
# WRONG — infinite loop!
i = 0
while i < 10:
    if i % 2 == 0:
        continue       # skips increment — i stays at 0 forever!
    print(i)
    i += 1

# CORRECT:
i = 0
while i < 10:
    i += 1             # increment FIRST
    if i % 2 == 0:
        continue       # now safe to skip
    print(i)
```

---

## 7. pass

**Does nothing** — used as a placeholder so Python doesn't raise an error for an empty block.

```python
# Empty if block — SyntaxError without pass:
if True:
    pass   # valid — do nothing for now

# Empty function — placeholder during development:
def my_function():
    pass

# Empty loop:
for i in range(5):
    pass
```

---

## 8. break vs continue vs pass

| Statement | What it does | Loop continues? |
|-----------|-------------|-----------------|
| `break` | Exits the loop entirely | No |
| `continue` | Skips rest of current iteration, goes to next | Yes |
| `pass` | Does nothing — placeholder | Yes |

```python
for i in range(1, 6):
    if i == 3:
        break        # stops at 3: prints 1, 2
    print(i)

for i in range(1, 6):
    if i == 3:
        continue     # skips 3: prints 1, 2, 4, 5
    print(i)

for i in range(1, 6):
    if i == 3:
        pass         # does nothing at 3: prints 1, 2, 3, 4, 5
    print(i)
```

---

## 9. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `SyntaxError: invalid syntax` on `else if` | Python uses `elif` (one word) | Change to `elif` |
| Infinite while loop | No increment, or increment after `continue` | Put increment before `continue` |
| `i++` gives SyntaxError | Python has no increment operator | Use `i += 1` |
| All `if` blocks run unexpectedly | Using multiple `if` instead of `elif` | Use `elif` for exclusive conditions |
| `IndentationError` inside loop | Body not indented | Indent 4 spaces |

---

## 10. Interview Questions

1. What is the difference between `elif` and `else if`?
2. What is the difference between multiple `if` and `elif`?
3. How do you increment a counter in Python?
4. What is the difference between `break` and `continue`?
5. When would you use `pass`?
6. What is the risk of using `continue` in a while loop?
7. How does a nested for loop work?
8. When would you prefer a while loop over a for loop?

---

## 11. Try It Yourself

```python
# 1. Print all numbers from 1-20 that are divisible by 3 OR 5

# 2. Print the multiplication table of 7 (7×1 to 7×10)

# 3. Print a right-angled number pattern:
#    1
#    1 2
#    1 2 3
#    1 2 3 4
#    1 2 3 4 5

# 4. Use a while loop to keep asking for a password
#    until the user enters "python123"

# 5. Loop 1-50. Skip multiples of 7. Stop completely at 40.
#    (uses both continue AND break)
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `if/elif/else` grade block | elif vs multiple if demo |
| `for fruit in fruits:` | Iterating a list |
| `for i in range(1,10,2):` | Step range — odd numbers |
| Nested `for` star pattern | Inner loop completes fully each outer turn |
| `while i <= 5: i += 1` | Basic while with counter |
| `break` at i==5 | Exit loop early |
| `continue` for even skip | Skip iteration, continue loop |
| `pass` in empty block | Placeholder syntax |
