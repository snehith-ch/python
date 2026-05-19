# Day 31 — Exception Handling Mechanism

← [Day 30](day_30_overriding_abstraction.md) | [Index](00_INDEX.md) | [Day 32](day_32_exception_advanced_custom.md) →

---

## Quick Revision — Day 31

| # | Key Point |
|---|-----------|
| 1 | Exception = runtime error; an unexpected event that disturbs the normal flow of program execution |
| 2 | Two types of errors: **syntactical** (caught while writing) and **runtime** (occur during execution) |
| 3 | Runtime errors cause **abnormal termination** (unsuccessful termination) |
| 4 | Two exception handling mechanisms: **logical implementation** (first priority) and **try-except** (second priority) |
| 5 | Every exception in Python is a **class** (`ZeroDivisionError`, `ValueError`, `NameError`, etc.) |
| 6 | `Exception` is the **superclass** of all subclass exceptions |
| 7 | **Default except block**: no exception class — catches everything, shows only user-defined messages |
| 8 | **Specific except block**: with exception class — shows actual exception message |
| 9 | Multiple except blocks allowed; default except must always be **last** |
| 10 | Exception handling does NOT repair errors — it shows an alternative execution path |

---

## Navigation

- **Pre-requisite:** [Day 30](day_30_overriding_abstraction.md) — Method overriding and abstract classes
- **Next:** [Day 32](day_32_exception_advanced_custom.md) — finally block, nested try-except, user-defined exceptions
- **Related:** [Day 32](day_32_exception_advanced_custom.md) — completing the exception handling topic

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `test21.py` | Syntax error demo (missing colon, bracket) |
| `.py` file | exception demos | `NameError`, `ValueError`, `TypeError`, `ZeroDivisionError` demos |
| Program | division program | Logical implementation to handle ZeroDivisionError |
| Program | division with try-except | try-except conversion of same program |
| Program | specific except block | `ZeroDivisionError as msg`, `ValueError as msg` |
| Program | multiple except blocks | Two separate except blocks |
| Program | multiple exception classes | `except (ZeroDivisionError, ValueError) as msg:` |
| Program | try-except cases | 5 print statements showing control flow in 4 cases |
| Exception class | `Exception` | Superclass of all exceptions |

---

## 1. What Is an Exception?

```
Exception Definition
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
An unexpected event OR unwanted event that will disturb
the normal flow of program execution is called an
EXCEPTION.

Exception = Runtime Error

When exception occurs:
    → Program stops abruptly
    → Abnormal termination (unsuccessful termination)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> **Key point:** Most exceptions are caused by **programmer's invalid inputs**. The programmer cannot predict them at compile time — they only occur at runtime.

---

## 2. Two Types of Errors

```
Python Errors
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌────────────────────────┬───────────────────────────────────┐
│  Syntactical Errors    │  Runtime Errors (Exceptions)      │
├────────────────────────┼───────────────────────────────────┤
│ Missing colon, bracket │ Wrong input from user             │
│ Wrong keyword spelling │ Division by zero                  │
│ Wrong indentation      │ File not found                    │
│                        │ Type mismatch                     │
├────────────────────────┼───────────────────────────────────┤
│ Caught while WRITING   │ Occur during EXECUTION            │
│ Easily identified      │ Cannot predict in advance         │
│ Easily fixed           │ Cause ABNORMAL TERMINATION        │
│ Does NOT harm execution│ Needs exception handling          │
└────────────────────────┴───────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Exception Handling Mechanism is for RUNTIME errors ONLY.
Not for syntactical errors.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2.1 Syntactical Error Demo

```python
# Missing colon after function definition → SyntaxError
def fun()    # SyntaxError: expected ':'

# Missing closing bracket → SyntaxError
print("hello"    # SyntaxError

# Wrong keyword spelling → SyntaxError
Klass Test:    # SyntaxError: invalid syntax
```

---

## 3. Exception Handling Mechanisms

There are two ways to handle exceptions:

```
Priority Order
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1st Priority: LOGICAL IMPLEMENTATION
   → Use if-else, conditional checks to prevent errors
   → Most situations can be handled this way

2nd Priority: TRY-EXCEPT IMPLEMENTATION
   → Used when logical implementation is not sufficient
   → More powerful — handles any type of exception
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IMPORTANT: Exception handling does NOT repair errors.
It shows an ALTERNATIVE way of program execution.
```

---

## 4. Python Exception Classes

Every exception in Python is a **class**. These exception classes are the building blocks of Python's error handling system.

```
Exception Class Hierarchy
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            Exception   ← SUPERCLASS of all
           /    |    \
     NameError  ValueError  ZeroDivisionError
         |          |             |
    TypeError  FileNotFoundError  FileExistsError
        ...         ...             ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Common Exception Classes

| Exception Class | When It Occurs |
|----------------|----------------|
| `NameError` | Accessing a variable that is not defined |
| `ValueError` | Invalid value for a function/operation (e.g., `int("abc")`) |
| `TypeError` | Operation on incompatible types (e.g., `10 + "hello"`) |
| `ZeroDivisionError` | Dividing by zero |
| `FileNotFoundError` | Opening a file that does not exist |
| `FileExistsError` | Creating a file that already exists (in X mode) |
| `IndexError` | Accessing a list index out of range |
| `KeyError` | Accessing a dictionary key that does not exist |
| `AttributeError` | Accessing an attribute that does not exist |

### 4.1 Exception Class Demos

```python
# NameError — variable not defined
a = 10
print(A)    # NameError: name 'A' is not defined

# ValueError — invalid input format
a = int(input("Enter a number: "))    # user types "23.4"
# ValueError: invalid literal for int() with base 10: '23.4'

# TypeError — incompatible types
result = 10 + "size"    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ZeroDivisionError — divide by zero
result = 10 / 0    # ZeroDivisionError: division by zero
```

---

## 5. Logical Implementation (First Priority)

Use if-else conditions to prevent the exception before it occurs.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b == 0:
    print("Second number cannot be 0")
else:
    c = a / b
    print("Result is:", c)
```

**When it works:** If `b = 0`, we print a message. If `b` is valid, we calculate.

**Limitation:** Cannot handle ALL exceptions. For example, if the user types characters instead of numbers (`abc`), `int()` raises `ValueError` — and logical implementation cannot prevent this.

---

## 6. try-except Implementation (Second Priority)

### 6.1 Syntax

```python
try:
    # Risky code — there is a chance of exception here
    risky_statement_1
    risky_statement_2
except:
    # Handling code — what to do when exception occurs
    handling_statement_1
    handling_statement_2
```

```
Control Flow — try-except
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
START → Enter try block

IF no exception in try block:
    → Execute ALL try statements
    → SKIP except block entirely
    → Normal termination ✓

IF exception occurs in try block:
    → STOP at the line that caused exception
    → Skip remaining try statements
    → Jump to except block
    → Execute except statements
    → Normal termination ✓ (exception was handled)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 6.2 Basic Example

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    c = a / b       # risky code — chance of ZeroDivisionError
    print("Result is:", c)
except:
    print("Something went wrong")
```

**Test 1:** Input 10, 3 → Output: `Result is: 3.333...` (try block executed, except skipped)
**Test 2:** Input 10, 0 → Output: `Something went wrong` (except executed)
**Test 3:** Input abc → Output: `Something went wrong` (except executed)

> **Problem with default except:** It only shows `"Something went wrong"` — does not tell WHAT went wrong. A programmer cannot identify the actual error.

---

## 7. Two Types of except Blocks

```
except Block Types
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type 1: DEFAULT except block
    except:
        print("Something went wrong")
    → No exception class specified
    → Catches ALL exceptions
    → Shows ONLY user-defined messages (not actual error)
    → Good for catching unknown exceptions

Type 2: SPECIFIC except block
    except ZeroDivisionError as msg:
        print(msg)
    → Exception class specified
    → Catches ONLY that exception
    → Shows ACTUAL exception message via msg object
    → Better for clarity and debugging
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 7.1 Specific except Block

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    c = a / b
    print("Result is:", c)
except ZeroDivisionError as msg:
    print(msg)    # prints: division by zero
```

> **`as` is a keyword.** `msg` is a user-defined object name (can be any name like `e`, `message`, `x`). This object stores the exception message returned by the exception class.

---

## 8. Multiple except Blocks

You can handle different exceptions separately with multiple except blocks.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    c = a / b
    print("Result is:", c)
except ZeroDivisionError as msg:
    print(msg)       # handles division by zero
except ValueError as msg:
    print(msg)       # handles invalid input like "abc"
```

**Input: 10, 0** → `division by zero`
**Input: abc** → `invalid literal for int() with base 10: 'abc'`

---

## 9. Multiple Exception Classes in One except Block

Instead of multiple except blocks, group exceptions together:

```python
try:
    c = a / b
    print("Result is:", c)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
```

> Enclose multiple exception classes in **parentheses** separated by commas.

---

## 10. Using the Superclass `Exception`

Since `Exception` is the superclass of ALL exception classes, you can use it to catch any exception:

```python
try:
    c = a / b
    print("Result is:", c)
except Exception as msg:
    print(msg)
```

> **Not recommended as default practice.** When you use the superclass, Python internally checks ALL subclass exceptions one by one — this is slower. Use specific exception classes when you know what can go wrong. Use `Exception` only when you don't know what exception to expect.

---

## 11. Default + Specific except Combination Rule

```
Rule: Default except MUST be LAST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
try:
    risky_code

except ZeroDivisionError as msg:    # specific — FIRST
    print(msg)

except:                              # default — MUST BE LAST
    print("Something went wrong")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Why?** If the default except is first, it catches ALL exceptions — and the specific except block below it can never execute. Python raises a `SyntaxError: default 'except:' must be last` if you violate this rule.

```python
try:
    c = a / b
    print("Result is:", c)
except ZeroDivisionError as msg:
    print(msg)           # handles known exception
except:
    print("Unknown error occurred")    # handles anything else
```

---

## 12. Four Cases of try-except Flow

The instructor demonstrated all 4 possible execution scenarios:

```python
try:
    print("Statement 1")    # stmt1
    print("Statement 2")    # stmt2
    print("Statement 3")    # stmt3
except:
    print("Statement 4")    # stmt4

print("Statement 5")        # stmt5 — outside try-except
```

```
Case 1: No exception in try block
    Executes: stmt1, stmt2, stmt3, stmt5
    Skips: stmt4 (except block ignored)
    Termination: NORMAL ✓

Case 2: Exception at Statement 1
    Executes: stmt4 (except block), stmt5
    Skips: stmt2, stmt3 (remaining try after exception)
    Termination: NORMAL ✓ (exception was handled)

Case 3: Exception at Statement 1, but wrong except class
    For example: ZeroDivisionError occurs but except says ValueError
    Corresponding except block NOT matched
    Executes: nothing useful
    Termination: ABNORMAL ✗ (unhandled exception)

Case 4: Exception in Statement 4 (inside except block)
    During handling, another exception occurs in except block
    Termination: ABNORMAL ✗
```

> **Case 3 explanation:** If an exception occurs but the corresponding except block does not match the exception type, it is equivalent to having NO except block → **abnormal termination**.

---

## 13. Complete Class Walkthrough

### Step 1: Division Program — Logical Implementation

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b == 0:
    print("Second number cannot be 0")
else:
    c = a / b
    print("Result is:", c)
```

### Step 2: Same Program with try-except (Default except)

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    c = a / b
    print("Result is:", c)
except:
    print("Something went wrong")
```

### Step 3: Specific except Block — ZeroDivisionError

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    c = a / b
    print("Result is:", c)
except ZeroDivisionError as msg:
    print(msg)
```

### Step 4: Multiple Specific except Blocks

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    c = a / b
    print("Result is:", c)
except ZeroDivisionError as msg:
    print(msg)
except ValueError as msg:
    print(msg)
```

### Step 5: Multiple Exceptions in One except Block

```python
try:
    c = a / b
    print("Result is:", c)
except (ZeroDivisionError, ValueError) as msg:
    print(msg)
```

### Step 6: Using Superclass Exception

```python
try:
    c = a / b
    print("Result is:", c)
except Exception as msg:
    print(msg)
```

### Step 7: Specific + Default except Combination

```python
try:
    c = a / b
    print("Result is:", c)
except ZeroDivisionError as msg:
    print(msg)
except:
    print("Something went wrong")
```

---

## Student Q&A

> **Student Question:** What is the difference between syntactical errors and runtime errors?
> **Answer:** Syntactical errors occur when we make mistakes while writing code — missing colons, brackets, wrong spelling. These are caught immediately when writing and can be easily fixed. Runtime errors (exceptions) occur during program execution, often due to invalid inputs or unexpected conditions. They cause the program to stop abruptly (abnormal termination) and must be handled using exception handling mechanisms.

> **Student Question:** Is exception handling only for runtime errors?
> **Answer:** Yes — exception handling mechanisms (try-except) are designed only for runtime errors. Syntactical errors cannot be handled with try-except because the program doesn't even start executing if there's a syntax error.

> **Student Question:** What is the difference between default and specific except blocks?
> **Answer:** A default except block has no exception class — it catches all exceptions but can only show user-defined messages (like "something went wrong"). A specific except block has an exception class name and an `as msg` clause — it shows the actual internal exception message. Specific blocks give more clarity to the programmer about what went wrong.

> **Student Question:** Can we use the `Exception` superclass instead of individual exception classes?
> **Answer:** Yes, you can. But it is not recommended as the default approach because Python internally has to check all subclass exceptions when using the superclass, which is slower. Use specific exception classes when you know what exceptions might occur. Use `Exception` superclass only when you're unsure what type of exception might be raised.

---

## Key Differences — Exception Handling Mechanisms

| Feature | Logical Implementation | try-except Implementation |
|---------|------------------------|--------------------------|
| Priority | First | Second (when logical fails) |
| Syntax | if-else conditions | try: ... except: ... |
| Can handle all exceptions? | No | Yes |
| Code clarity | Clear | Slightly more verbose |
| When to use | When you know the condition to check | When exception is unpredictable |
| Example | `if b == 0:` | `except ZeroDivisionError:` |

| Feature | Default except | Specific except |
|---------|---------------|-----------------|
| Syntax | `except:` | `except ExceptionClass as msg:` |
| Catches | All exceptions | Only specified exception |
| Message shown | User-defined only | Actual exception message |
| Position | Must be LAST | Can be anywhere above default |
| Recommended? | Avoid unless necessary | Preferred for clarity |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `SyntaxError: default 'except:' must be last` | Default except block placed before specific except block | Move default except to the last position |
| `ZeroDivisionError: division by zero` | Dividing a number by zero | Add a check: `if b != 0:` or use try-except |
| `ValueError: invalid literal for int()` | Passing non-integer string to `int()` | Validate input or use try-except with `ValueError` |
| `NameError: name 'A' is not defined` | Using a variable name with wrong case | Python is case-sensitive — check variable name spelling |
| `TypeError: unsupported operand type(s)` | Adding incompatible types like `int + str` | Use `str(n)` or `int(s)` to convert types |

---

## Interview Questions

**Q: What is an exception in Python?**
A: An exception is an unexpected or unwanted event that occurs during program execution and disturbs the normal flow of the program. Exceptions are runtime errors — they cause abnormal (unsuccessful) termination of the program if not handled.

**Q: What is the difference between a syntax error and a runtime error?**
A: Syntax errors occur while writing code (missing colon, bracket, wrong keyword). They are caught before execution and are easy to fix. Runtime errors (exceptions) occur during program execution due to invalid inputs or unexpected conditions. They cause abnormal termination and must be handled with exception handling mechanisms.

**Q: What are the two exception handling mechanisms in Python?**
A: (1) Logical implementation — using if-else conditions to prevent exceptions before they occur. (2) try-except implementation — placing risky code in a try block and handling exceptions in except blocks. Logical implementation has first priority; try-except is used when logical implementation is not sufficient.

**Q: What is `Exception` in Python?**
A: `Exception` is the superclass (base class) of all exception classes in Python. Classes like `ZeroDivisionError`, `ValueError`, `TypeError`, `NameError` all inherit from `Exception`. You can use `Exception` in an except block to catch any exception.

**Q: What is the difference between default and specific except blocks?**
A: A default except block (`except:`) catches all exceptions but can only print user-defined messages. A specific except block (`except ZeroDivisionError as msg:`) catches only the named exception and can print the actual exception message via the `msg` object. Specific blocks are preferred for clarity. When combining both, the default except must always be last.

**Q: Can we have multiple except blocks?**
A: Yes. Python allows multiple except blocks for a single try block. Each except block handles a different exception type. You can also combine multiple exception classes in one except block using parentheses: `except (ZeroDivisionError, ValueError) as msg:`.

**Q: What happens when an exception is not handled?**
A: The program terminates abnormally (unsuccessful termination). Python displays the full traceback and error message, and the remaining code in the program does not execute.

**Q: Does exception handling repair the error?**
A: No. Exception handling does NOT repair the error. It provides an alternative execution path — showing a meaningful message to the user instead of crashing. The goal is graceful degradation, not error repair.

---

## Try It Yourself

**Exercise 1:** Write a program that accepts two numbers and divides the first by the second. Use try-except to handle both `ZeroDivisionError` and `ValueError` (in case user enters non-numeric input). Display the actual exception message.

<details><summary>Answer</summary>

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print("Result:", c)
except ZeroDivisionError as msg:
    print("Error:", msg)
except ValueError as msg:
    print("Error:", msg)
```
</details>

---

**Exercise 2:** Write a program that asks the user for a list index and retrieves an element from the list `[10, 20, 30, 40, 50]`. Handle `IndexError` and `ValueError` (in case user enters a non-integer index).

<details><summary>Answer</summary>

```python
data = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter index (0-4): "))
    print("Element:", data[index])
except IndexError as msg:
    print("Index out of range:", msg)
except ValueError as msg:
    print("Invalid input:", msg)
```
</details>

---

**Exercise 3:** Demonstrate all four try-except cases by creating a program with statements 1-5 where you can comment/uncomment exceptions inside the try block to see different flows.

<details><summary>Answer</summary>

```python
try:
    print("Statement 1")
    # Uncomment the next line to trigger Case 2 (exception at stmt 1):
    # result = 10 / 0
    print("Statement 2")
    print("Statement 3")
except ZeroDivisionError as msg:
    print("Statement 4 (except):", msg)

print("Statement 5 (always runs)")
```
</details>

---

**Exercise 4:** Write a program that accepts a number and computes its square root. Handle the case where the user enters a negative number (hint: `math.sqrt(-1)` raises `ValueError`).

<details><summary>Answer</summary>

```python
import math

try:
    num = float(input("Enter a number: "))
    result = math.sqrt(num)
    print("Square root:", result)
except ValueError as msg:
    print("Cannot compute square root of a negative number:", msg)
except TypeError as msg:
    print("Invalid input type:", msg)
```
</details>

---

**Exercise 5:** Demonstrate the difference between default and specific except blocks by writing the same division program twice — once with default except, once with specific except — and compare the output when `b = 0`.

<details><summary>Answer</summary>

```python
a, b = 10, 0

# Version 1: Default except
try:
    print(a / b)
except:
    print("Something went wrong")    # no detail

print("---")

# Version 2: Specific except
try:
    print(a / b)
except ZeroDivisionError as msg:
    print("Error:", msg)    # shows: division by zero
```
</details>
