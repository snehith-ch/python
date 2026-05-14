# Day 4 — Fundamental Concepts: Comments, Keywords, Indentation, Identifiers, Variables, Multiple Assignment

## Quick Revision — Day 4
| # | Key Point |
|---|-----------|
| 1 | **Single-line comment:** starts with `#` |
| 2 | **Multi-line comment:** wrap in `'''triple quotes'''` or `"""triple quotes"""` |
| 3 | Triple-quoted text assigned to a variable = **string**; not assigned = **comment** |
| 4 | **Keywords** are reserved words — cannot be used as variable/function/class names |
| 5 | Get all keywords: `import keyword; print(keyword.kwlist)` |
| 6 | **Indentation** (4 spaces) replaces `{}` curly braces used in Java/C++ to define blocks |
| 7 | Missing indentation → `IndentationError: expected an indented block` |
| 8 | **Identifier** = any name (variable, function, class); 8 rules apply |
| 9 | Identifiers are **case-sensitive**; cannot start with a digit; cannot be a keyword |
| 10 | **Multiple assignment:** `a = b = c = 10` (one value to many) OR `a, b, c = 10, 20, 30` (many to many) |

---

**Pre-requisite:** Day 3 — PyCharm setup, running Python files
**Next:** Day 5 — Data types (None, int, float, bool, complex, string overview)
**Related:** Day 1 — Case sensitivity, dynamically typed (why no data type in variable declaration)

---

## Code Created This Day
| Item | Name / Example | Purpose |
|------|----------------|---------|
| .py file | test1.py | Comments and indentation demo |
| .py file | keywords_demo.py | Listing all Python keywords |
| .py file | identifiers_demo.py | Identifier rules demonstration |
| .py file | variables_demo.py | Variables and multiple assignment |

---

## 1. Comments

### What Are Comments?

Comments are lines in your program that are **ignored during execution**. They serve two purposes:

1. **Exclude code from execution** — temporarily disable lines without deleting them
2. **Write descriptions** — explain what your code does, for yourself and other developers

### 1.1 Single-Line Comment

Starts with `#`. Everything after `#` on that line is ignored.

```python
# This is a single-line comment
a = 10
b = 20
# c = a + b   ← this line is excluded from execution
print(a + b)   # inline comment — also valid
```

### 1.2 Multi-Line Comment

Wrap multiple lines in triple single-quotes `'''` or triple double-quotes `"""`.

```python
'''
This is a multi-line comment.
This program adds two numbers.
Written by: Student
'''
a = 10
b = 20
print(a + b)
```

```python
"""
This also works as a multi-line comment.
Use triple double-quotes or triple single-quotes.
"""
```

### Critical Rule: Comment vs. String

> **Common Mistake / Important Point:**
> Triple quotes are multi-line comments ONLY when they are NOT assigned to a variable.
> If assigned to a variable, they become a **multi-line string**.

```python
# This is a COMMENT — not assigned to any variable:
'''
This text is ignored during execution.
'''

# This is a STRING — assigned to variable s:
s = '''
Durga Soft
Hyderabad
'''
print(s)   # Output: Durga Soft\n Hyderabad
```

### Practical Use of Comments

```python
# test1.py — before comments
a = 10
b = 20
print("Sum:", a + b)
print("Hello")

# test1.py — after adding comment to exclude "Hello" line:
a = 10
b = 20
print("Sum:", a + b)
# print("Hello")   ← now excluded from execution
```

---

## 2. Keywords (Reserved Words)

### What Are Keywords?

**Keywords** are words that Python has reserved for specific built-in purposes. You cannot use them as your own variable names, function names, or class names.

> **Definition:** Keywords are reserved words. The words which are reserved for something — that purpose only we have to use. Same purpose, same word. No other purpose.

### Getting the Complete Keyword List

```python
import keyword
print(keyword.kwlist)
```

**Output (Python 3.10.4 — 35 keywords):**
```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
 'return', 'try', 'while', 'with', 'yield']
```

> **Exam Tip:** Three keywords start with a **capital letter**: `False`, `None`, `True`. All other keywords are lowercase.

### Why Can't You Use Keywords as Variable Names?

```python
# WRONG — 'if' is a keyword reserved for conditional checks:
if = 10       # SyntaxError!

# CORRECT — use a different name:
if_value = 10   # This works (not a keyword)
```

Keywords convey a **special message to the interpreter**. When the interpreter sees `if`, it expects a condition. Using `if` as a variable name confuses the interpreter.

### Every Keyword Has a Purpose

| Keyword | Purpose | When You'll Use It |
|---------|---------|-------------------|
| `if`, `elif`, `else` | Conditional statements | Day 9 |
| `for`, `while` | Loop statements | Day 9 |
| `break`, `continue`, `pass` | Transfer statements | Day 9 |
| `def` | Define a function | Day 15 |
| `class` | Define a class | Day 22 |
| `import` | Import a module/library | Day 19 |
| `return` | Return value from function | Day 15 |
| `True`, `False` | Boolean values | Day 5 |
| `None` | Null/empty value | Day 5 |
| `and`, `or`, `not` | Logical operators | Day 7 |
| `in`, `is` | Membership/identity operators | Day 7 |
| `try`, `except`, `finally` | Exception handling | Later |

```python
# In class demo — import is itself a keyword:
import keyword          # 'import' is being used for its reserved purpose (importing)
print(keyword.kwlist)   # keyword is a module; kwlist is its attribute
```

---

## 3. Indentation

### What Is Indentation?

**Indentation** is the use of spaces at the beginning of a line to define a **block of code**.

In languages like Java, C, C++, blocks are defined using curly braces `{ }`:

```java
// Java — curly braces define blocks:
if (a == 10) {
    System.out.println("true");
} else {
    System.out.println("false");
}
```

**Python uses indentation instead of curly braces:**

```python
# Python — 4 spaces define blocks:
a = 10
if a == 10:
    print("true")    # 4 spaces → belongs to if block
else:
    print("false")   # 4 spaces → belongs to else block
```

```
Block structure in Python:
┌──────────────────────┐
│ if a == 10:          │  ← no curly braces
│     print("true")   │  ← indented 4 spaces = inside if block
│ else:                │
│     print("false")  │  ← indented 4 spaces = inside else block
└──────────────────────┘
```

### The IndentationError

```python
# WRONG — no indentation:
a = 10
if a == 10:
print("true")    # ← not indented!
```

```
IndentationError: expected an indented block after 'if' statement on line 2
```

```python
# CORRECT — 4 spaces indentation:
a = 10
if a == 10:
    print("true")    # ← 4 spaces indentation
else:
    print("false")
```

### Rules for Indentation

- **Default standard:** 4 spaces (used by PyCharm automatically)
- **Minimum required:** at least 1 space
- Any number of spaces works (1, 2, 3, 4) **as long as you are consistent within the same block**
- **PyCharm auto-indents** — after you type `if ...:` and press Enter, PyCharm automatically adds 4 spaces on the next line

> **Why beginners struggle here:** Programmers from Java/C++ try to write Python in Notepad without knowing the indentation rule — they get `IndentationError` on every block statement. This is why PyCharm is recommended for beginners — it handles indentation automatically.

> **Interview Question:** How does Python define code blocks, unlike Java or C++?
> **Answer:** Python uses indentation (spaces) to define blocks of code. Java and C++ use curly braces `{}`. Missing indentation in Python causes an `IndentationError`.

### Where Indentation Is Required

Indentation is required inside every block:

```python
if condition:
    # indented block
elif condition:
    # indented block
else:
    # indented block

for item in list:
    # indented block

while condition:
    # indented block

def function_name():
    # indented block

class ClassName:
    # indented block
```

---

## 4. Identifiers

### What Is an Identifier?

An **identifier** is any name you give to a variable, function, class, or any other user-defined element in Python.

```python
emp_id = 1234      # emp_id is an identifier (variable name)
def greet():       # greet is an identifier (function name)
class Employee:    # Employee is an identifier (class name)
```

### 8 Rules for Defining Identifiers

**Rule 1:** Can use **lowercase and uppercase letters** (a–z, A–Z)
```python
name = "Durga"    # valid
NAME = "Durga"    # valid (different from 'name')
```

**Rule 2:** Identifiers are **case-sensitive**
```python
emp_id = 1234
print(emp_id)    # works
print(EMP_ID)    # NameError: name 'EMP_ID' is not defined
print(Emp_Id)    # NameError: name 'Emp_Id' is not defined
```

**Rule 3:** Can include **digits (0–9)**, but **cannot START with a digit**
```python
emp1 = 100       # valid — digit at end
id9name = "abc"  # valid — digit in middle
1emp = 100       # INVALID — starts with digit → SyntaxError
```

**Rule 4:** Can include **underscore `_`**
```python
emp_id = 1234       # valid
_emp_id = 1234      # valid (but has special meaning — see Rule 7)
__emp_id = 1234     # valid (but has special meaning — see Rule 7)
```

**Rule 5:** **Cannot have spaces** (an identifier must be one word)
```python
emp id = 1234    # INVALID — two words, space not allowed
emp_id = 1234    # CORRECT — use underscore to combine two words
```

**Rule 6:** Can be of **any length** — no restriction on how long a name can be

**Rule 7:** Identifiers starting with `_` have **special meaning**:
```python
_name = "value"     # single underscore → indicates private variable
__name = "value"    # double underscore → strongly private (name mangling in OOP)
```
> This will be explained in detail during Object-Oriented Programming sessions.

**Rule 8:** **Cannot use keywords** as identifiers
```python
if = 10       # INVALID — 'if' is a keyword → SyntaxError
for = 20      # INVALID — 'for' is a keyword → SyntaxError
deff = 10     # VALID — 'deff' is not a keyword
```

### Uppercase Convention for Constants

Python does not have a `const` keyword like C or Java. However, by convention:
- Variables declared in **ALL CAPS** signal to other programmers: "treat this as a constant — don't change it"

```python
PI = 3.14159       # convention: this is a constant
MAX_SIZE = 100     # convention: do not change this value
```

> **Important:** Python does NOT enforce this. Other programmers can still change `PI = 99` — it just signals intent. Real constants are not supported in Python.

---

## 5. Variables

### What Is a Variable?

A **variable** is a **named memory location** used to store a value.

```
Variable declaration in Python:

variable_name = value

a = 10    →    memory location named 'a' holds value 10
```

```
Memory Model:
┌─────────────┐
│  value: 10  │  ← memory location
└─────────────┘
       ↑
       a         ← 'a' is the name (identifier) for this location
```

### Variable Declaration Rules

```python
# CORRECT Python syntax:
a = 10

# WRONG — do NOT declare data type (this is Java/C syntax):
int a = 10    # SyntaxError in Python!

# WRONG — semicolon not required (optional, but not needed):
a = 10;       # works, but unnecessary
```

- No data type needed (dynamically typed)
- No semicolon needed (optional)
- Use `type()` to check what data type Python assigned:

```python
a = 10
print(type(a))      # <class 'int'>

a = 10.5
print(type(a))      # <class 'float'>

a = "Durga"
print(type(a))      # <class 'str'>

a = 'x'            # single character — still a string, not 'char'
print(type(a))      # <class 'str'>
```

> **Important:** Python has NO `char` data type. Even a single character like `'x'` is treated as a **string** (`str`).

---

## 6. Multiple Assignment

### Type 1: Assign One Value to Multiple Variables

```python
a = b = c = 10

print(a)    # 10
print(b)    # 10
print(c)    # 10

# Print all on one line using separator:
print(a, b, c, sep=", ")    # 10, 10, 10

# Print all on one line using end attribute:
print(a, end=" ")
print(b, end=" ")
print(c)
# Output: 10 10 10
```

```
a ──┐
b ──┼──→ 10   (all three point to the same value)
c ──┘
```

### Type 2: Assign Multiple Values to Multiple Variables

```python
a, b, c = 10, 20, 30

print(a)    # 10
print(b)    # 20
print(c)    # 30

print(a, b, c, sep=", ")   # 10, 20, 30
```

```
a → 10
b → 20
c → 30
```

### The `sep` and `end` Attributes of print()

```python
# sep: separator between values (default is a space)
print(10, 20, 30)               # Output: 10 20 30
print(10, 20, 30, sep=", ")     # Output: 10, 20, 30
print(10, 20, 30, sep=" | ")    # Output: 10 | 20 | 30

# end: what to print at the end (default is newline \n)
print("Hello", end=" ")
print("World")
# Output: Hello World  (on the same line)
```

> **Note:** The `end` attribute on the last variable's `print()` is not needed — after printing the last value, the line naturally ends.

---

## 7. Complete Class Walkthrough

**Step 1:** Open PyCharm → Python Project at 7AM

**Step 2:** Create a new file `test1.py` — demonstrate comments:
```python
# test1.py

a = 10
b = 20
print("Sum:", a + b)   # Output: Sum: 30

# print("Hello")   ← excluded with single-line comment

'''
This is a multi-line comment.
These lines are all excluded from execution.
'''
```

**Step 3:** Create `keywords_demo.py`:
```python
import keyword
print(keyword.kwlist)
```

**Step 4:** Show that keywords cannot be used as variables:
```python
# if = 10    ← SyntaxError — uncomment to see error
a = 10
print(a)
```

**Step 5:** Create `indentation_demo.py` — show in Notepad first (wrong way):
```python
# Written in notepad without indentation — produces IndentationError:
a = 10
if a == 10:
print("true")   # ← no indentation → IndentationError
```

Then show the correct way:
```python
a = 10
if a == 10:
    print("true")
else:
    print("false")
```

**Step 6:** Identifier rules demonstration:
```python
emp_id = 1234
print(emp_id)       # works
# print(EMP_ID)     # would give NameError

# 1emp = 100        # SyntaxError — starts with digit
emp1 = 100          # valid — digit not at start
```

**Step 7:** Variables and multiple assignment:
```python
# Single assignment:
a = 10
print(type(a))   # <class 'int'>

# Multiple assignment — one value to many:
x = y = z = 100
print(x, y, z, sep=", ")   # 100, 100, 100

# Multiple assignment — many values to many:
p, q, r = 10, 20, 30
print(p, q, r, sep=", ")   # 10, 20, 30
```

---

## Key Differences: Comment Types

| Feature | Single-line comment | Multi-line comment |
|---------|--------------------|--------------------|
| Syntax | `# comment text` | `'''text'''` or `"""text"""` |
| Scope | One line only | Any number of lines |
| Position | Anywhere (start of line or after code) | Standalone block |
| When to use | Short notes, excluding one line | Long descriptions, excluding many lines |

---

## Common Errors — Day 4

| Error | Cause | Fix |
|-------|-------|-----|
| `IndentationError: expected an indented block` | No spaces after `if:`, `for:`, `def:`, etc. | Add 4 spaces at the start of the block |
| `SyntaxError: invalid syntax` on `if = 10` | Using a keyword as a variable name | Rename the variable (e.g., `if_val = 10`) |
| `SyntaxError: invalid syntax` on `1emp = 100` | Identifier starts with a digit | Start the name with a letter or underscore |
| `NameError: name 'EMP_ID' is not defined` | Variable declared as `emp_id` but accessed as `EMP_ID` | Match the case exactly |
| `SyntaxError` on `emp id = 10` | Space in identifier | Use underscore: `emp_id = 10` |

---

## Interview Questions — Day 4

**Q: What are comments in Python and why are we used?**
A: Comments are lines ignored during execution. They are used either to exclude code from running temporarily, or to write descriptions explaining what the code does. Python supports single-line comments (`#`) and multi-line comments (`'''`).

**Q: What is the difference between a single-line and multi-line comment?**
A: A single-line comment starts with `#` and covers one line. A multi-line comment uses triple quotes (`'''` or `"""`) and can span any number of lines.

**Q: What are keywords in Python?**
A: Keywords are reserved words that Python uses for specific built-in purposes. They cannot be used as variable names, function names, or class names. Python 3 has 35 keywords. Three start with capitals: `True`, `False`, `None`.

**Q: How do you get a list of all Python keywords?**
A: `import keyword; print(keyword.kwlist)`

**Q: How does Python define blocks of code?**
A: Python uses indentation (typically 4 spaces) instead of curly braces `{}`. Any code at the same indentation level belongs to the same block.

**Q: What is an IndentationError?**
A: An error raised when a block of code is expected after a statement like `if`, `for`, `def`, or `class`, but no indentation is found. Fix: add at least one space (4 spaces is standard) before the block's code.

**Q: What is an identifier in Python?**
A: An identifier is any name given to a variable, function, class, or other element. Rules: can contain letters, digits, underscores; cannot start with a digit; cannot be a keyword; is case-sensitive.

**Q: What is multiple assignment in Python?**
A: Assigning values to multiple variables in one line. Two forms: `a = b = c = 10` (one value to multiple variables) and `a, b, c = 10, 20, 30` (multiple values to multiple variables).

**Q: Does Python support constants?**
A: Not officially — there is no `const` keyword. By convention, variables named in ALL_CAPS signal "treat as constant" to other developers, but Python does not enforce this. The value can still be changed.

**Q: Why can't Python identifiers start with a digit?**
A: Python's parser would confuse `1emp` with a number literal. By rule, all identifiers must start with a letter or underscore so the interpreter can distinguish variable names from numeric values.

---

## Try It Yourself — Day 4

**Exercise 1:** Get and print the complete keyword list:
```python
import keyword
print(keyword.kwlist)
print("Total keywords:", len(keyword.kwlist))
```

**Exercise 2:** Try to use keywords as variables — observe the errors:
```python
# Uncomment one at a time and see the error:
# if = 10
# for = 20
# class = "test"
# import = 5
```

**Exercise 3:** Practice indentation with an if-else block:
```python
temperature = 35
if temperature > 30:
    print("It's hot outside!")
    print("Drink water.")
else:
    print("It's comfortable outside.")
print("This line always runs.")   # no indentation = outside both blocks
```
*Notice that the last print runs regardless of the condition.*

**Exercise 4:** Test identifier rules:
```python
# Valid identifiers:
student_name = "Rahul"
_age = 25
score1 = 95

# Print all:
print(student_name, _age, score1)

# Now try (remove comment to test):
# 1score = 90     # starts with digit — error
# student name = "Rahul"   # space — error
```

**Exercise 5:** Practice multiple assignment:
```python
# One value to three variables:
x = y = z = 100
print("x =", x, "y =", y, "z =", z)

# Three values to three variables:
a, b, c = 10, 20, 30
print(a, b, c, sep=" | ")

# Swap two values using multiple assignment (no temp variable needed!):
p = 5
q = 10
p, q = q, p
print("After swap: p =", p, "q =", q)
```
*The swap trick in Exercise 5 is a commonly asked interview question.*
