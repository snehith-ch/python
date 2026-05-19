# Day 32 — Exception Handling: finally Block, Nested try-except, User-Defined Exceptions

← [Day 31](day_31_exception_handling.md) | [Index](00_INDEX.md) | [Day 33](day_33_file_handling_basics.md) →

---

## Quick Revision — Day 32

| # | Key Point |
|---|-----------|
| 1 | `finally` block: always executes regardless of exception — contains **mandatory messages** |
| 2 | `finally` can be stopped ONLY with `os._exit(0)` which shuts down the Python Virtual Machine |
| 3 | Nested try-except: a try block inside another try, accept, or finally block |
| 4 | If inner except cannot handle exception → outer except takes over |
| 5 | Two types of exceptions: **predefined/built-in** and **user-defined/customized** |
| 6 | User-defined exception class must **inherit from `Exception`** (superclass) |
| 7 | `raise` keyword is used to raise user-defined exceptions |
| 8 | Built-in exceptions raise automatically; user-defined must be raised with `raise` |
| 9 | In Java/C#: `throw` keyword; in Python: `raise` keyword |
| 10 | User-defined exception class constructor: `def __init__(self, arg): self.msg = arg` |

---

## Navigation

- **Pre-requisite:** [Day 31](day_31_exception_handling.md) — try-except basics, exception classes
- **Next:** [Day 33](day_33_file_handling_basics.md) — File handling basics
- **Related:** [Day 31](day_31_exception_handling.md) — completing exception handling

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| Program | finally block demo | Shows finally always executes |
| Program | `os._exit(0)` demo | Stopping finally block and any program |
| Program | nested try-except | Outer/inner try-except flow |
| Program | inner exception not matched | Outer except takes over |
| Class | `TooOldException(Exception)` | User-defined exception (age > 60) |
| Class | `TooYoungException(Exception)` | User-defined exception (age ≤ 16) |
| Program | raise keyword demo | Raising user-defined exceptions |
| Program | handling user-defined exceptions | try-except with custom classes |
| Keyword | `raise` | Raising exceptions manually |
| Module | `os` | `os._exit(0)` to stop PVM |

---

## 1. finally Block

### 1.1 What Is finally?

```
try-except-finally Syntax
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
try:
    # Risky code — chance of exception

except [ExceptionClass as msg]:
    # Handling code — if exception occurs

finally:
    # Mandatory messages — ALWAYS executes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

The `finally` block contains **mandatory messages** — statements that MUST execute regardless of whether an exception was raised or not, and whether the exception was handled or not.

**Why can't you put mandatory messages in try or except?**

```
If mandatory messages are in try block:
    → try block skips when exception occurs
    → mandatory messages get missed

If mandatory messages are in except block:
    → except block skips when no exception occurs
    → mandatory messages get missed

Solution: Put them in finally block
    → finally ALWAYS executes — no matter what
```

> **Including finally is optional.** But if you include it, it is compulsory to execute.

### 1.2 Demo Program

```python
try:
    print("Try block")
except:
    print("Except block")
finally:
    print("Finally block")
```

**Case 1 — No exception:**
```
Try block
Finally block
```
(Except block skipped; finally always runs)

**Case 2 — Exception occurs:**
```python
try:
    print("Try block")
    result = 10 / 0    # exception here
    print("After division")
except:
    print("Except block")
finally:
    print("Finally block")
```
```
Try block
Except block
Finally block
```

Both cases: **finally always executes**.

---

## 2. Stopping finally — `os._exit(0)`

There is **only one** situation where finally block execution can be stopped: using `os._exit(0)`.

```python
import os

try:
    print("Try block")
    os._exit(0)       # PVM shuts down immediately here
except:
    print("Except block")
finally:
    print("Finally block")    # THIS WILL NOT EXECUTE
```

**Output:** `Try block` — then PVM shuts down. Neither except nor finally runs.

### 2.1 What Does `os._exit(0)` Do?

```
os._exit(0)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Immediately shuts down the Python Virtual Machine (PVM)
→ No further code executes after this line
→ Status code 0 = successful termination
→ Can be used ANYWHERE in a Python program — not just
  to stop finally block
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```python
import os

print("Hello")
os._exit(0)       # PVM stops here
print("Hi")       # never executes
print("Welcome")  # never executes
```
**Output:** `Hello` — then program ends.

> `os._exit(0)` is in the `os` (operating system) module. It is not only for stopping finally blocks — it stops execution anywhere in the program.

---

## 3. Nested try-except-finally

### 3.1 What Is Nested?

A **try, except, or finally block** that contains **another try-except-finally** inside it is called **nested try-except-finally**.

```python
try:                          # outer try
    print("Outer try")
    try:                      # inner try
        print("Inner try")
    except:                   # inner except
        print("Inner except")
    finally:                  # inner finally
        print("Inner finally")
except:                       # outer except
    print("Outer except")
finally:                      # outer finally
    print("Outer finally")
```

### 3.2 Flow — No Exception Anywhere

```
Output:
    Outer try
    Inner try
    Inner finally    ← inner finally always runs
    Outer finally    ← outer finally always runs

Note: Both inner and outer except blocks skipped
      (no exception anywhere)
```

### 3.3 Flow — Exception Inside Inner try

```python
try:
    print("Outer try")
    try:
        print("Inner try")
        result = 10 / 0    # exception in inner try
    except ZeroDivisionError:
        print("Inner except")
    finally:
        print("Inner finally")
except:
    print("Outer except")
finally:
    print("Outer finally")
```

```
Output:
    Outer try
    Inner try
    Inner except     ← inner except handles it
    Inner finally    ← inner finally runs
    Outer finally    ← outer finally runs

Outer except: not executed (inner except handled it)
```

### 3.4 Flow — Inner except Does NOT Match

```python
try:
    print("Outer try")
    try:
        print("Inner try")
        result = 10 / 0    # ZeroDivisionError
    except ValueError:     # WRONG — does not match
        print("Inner except")
    finally:
        print("Inner finally")
except ZeroDivisionError:  # CORRECT match
    print("Outer except")
finally:
    print("Outer finally")
```

```
Output:
    Outer try
    Inner try
    Inner finally    ← inner finally still runs
    Outer except     ← outer except takes over!
    Outer finally

Rule: If inner except cannot handle the exception,
      OUTER except takes responsibility to handle it.
```

> **Key Rule:** When exception occurs in the inner try block, the **inner except** handles it first. If inner except does NOT match (wrong exception class), control goes to **outer except** to handle it.

---

## 4. User-Defined (Customized) Exceptions

### 4.1 Why User-Defined Exceptions?

```
Built-in exceptions:     NameError, ValueError, ZeroDivisionError...
Problem:                 Sometimes they don't meet your requirements

Solution:                Create your own exception classes
                         These are called USER-DEFINED or CUSTOMIZED exceptions
```

**Example use case:** A policy application that only accepts ages between 17 and 59. There's no built-in `TooOldError` or `TooYoungError` — you need to create them yourself.

### 4.2 How to Create a User-Defined Exception Class

```python
class YourExceptionName(Exception):    # MUST inherit from Exception
    def __init__(self, arg):
        self.msg = arg                 # store the exception message
```

**Rules:**
1. Your class name can be anything (follow Python naming conventions)
2. It **must** inherit from `Exception` (or another exception class) — otherwise it won't be treated as an exception
3. Include a constructor that stores the message

### 4.3 How to Raise User-Defined Exceptions

```
Built-in exceptions:    Raised AUTOMATICALLY by Python
User-defined exceptions: You must raise them MANUALLY using raise keyword

raise keyword syntax:
    raise ExceptionClassName(message)

Note:
    Java/C# use: throw keyword
    Python uses: raise keyword
```

### 4.4 Complete Example — Policy Application

```python
# Step 1: Define custom exception classes
class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg

class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg

# Step 2: Program logic — raise exceptions based on condition
age = int(input("Enter your age: "))

if age >= 60:
    raise TooOldException("Age should not be 60 or more")
elif age <= 16:
    raise TooYoungException("Age should not be 16 or below")
else:
    print("You are eligible to take policy")
```

**Test 1:** age = 78 → `TooOldException: Age should not be 60 or more`
**Test 2:** age = 14 → `TooYoungException: Age should not be 16 or below`
**Test 3:** age = 38 → `You are eligible to take policy`

### 4.5 Handling User-Defined Exceptions with try-except

```python
class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg

class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg

try:
    age = int(input("Enter your age: "))

    if age >= 60:
        raise TooOldException("Age should not be 60 or more")
    elif age <= 16:
        raise TooYoungException("Age should not be 16 or below")
    else:
        print("You are eligible to take policy")

except (TooOldException, TooYoungException) as msg:
    print(msg.msg)         # prints: Age should not be 60 or more
except ValueError as msg:
    print(msg)             # handles non-integer input
```

> **Note:** For user-defined exceptions, the message is stored in `msg.msg` (the `.msg` attribute you defined). For built-in exceptions, `print(msg)` shows the message directly.

### 4.6 Using Superclass Exception to Handle All

```python
try:
    age = int(input("Enter your age: "))
    if age >= 60:
        raise TooOldException("Age should not be 60 or more")
    elif age <= 16:
        raise TooYoungException("Age should not be 16 or below")
    else:
        print("You are eligible to take policy")
except Exception as msg:
    print(msg)    # works for both user-defined and built-in
```

Since `TooOldException` and `TooYoungException` inherit from `Exception`, the superclass except catches them all.

---

## 5. Built-in vs User-Defined Exceptions

```
Exception Types — Complete Picture
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type 1: Predefined / Built-in Exceptions
    Examples: NameError, ValueError, TypeError,
              ZeroDivisionError, FileNotFoundError
    Raised by: Python system automatically
    Handle with: except ExceptionClass as msg

Type 2: User-Defined / Customized Exceptions
    Created by: Programmer when built-ins don't meet needs
    Raised by: Programmer using raise keyword
    Handle with: except YourExceptionClass as msg
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 6. `raise` Keyword

```
raise keyword
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Purpose:    Raise exceptions based on requirement in your program
Used for:   User-defined exceptions (built-ins raise automatically)
Syntax:     raise ExceptionClassName("message")
Equivalent: Java/C# → throw keyword

When to use:
    - You created your own exception class
    - According to your program logic, condition to raise is met
    - You call raise YourException("message")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Student Q&A

> **Student Question:** Why do we need the finally block when we can put statements in try or except?
> **Answer:** If mandatory statements are in the try block, they get skipped when an exception occurs (try block stops at the exception line). If they're in the except block, they get skipped when there's no exception (except block is ignored). The finally block solves this — it always executes regardless of exception status. It is the only guaranteed place for compulsory execution statements.

> **Student Question:** When will the finally block NOT execute?
> **Answer:** In only one situation — when you use `os._exit(0)`. This function immediately shuts down the Python Virtual Machine itself, so no further code (including finally) can run. This is the only way to stop finally block execution.

> **Student Question:** If exception occurs in the inner try block, which except handles it?
> **Answer:** The inner except block takes responsibility first. If the inner except block matches the exception (correct exception class), it handles it and the outer except is ignored. If the inner except does NOT match, control passes to the outer except block to handle it.

> **Student Question:** Why does the user-defined exception class need to inherit from Exception?
> **Answer:** Because in Python, every exception is a class, and all exception classes must be derived from the `Exception` superclass. Without this inheritance, your class is just a normal Python class — not an exception class. Inheriting from `Exception` makes your class part of the exception hierarchy and allows it to be used with raise and except.

> **Student Question:** In other languages like Java, the keyword is `throw`. What about Python?
> **Answer:** Python uses the `raise` keyword to raise exceptions. `throw` is used in Java and C#. The purpose is the same — to raise an exception based on a condition — but the keyword differs.

---

## Key Differences

| Feature | try block | except block | finally block |
|---------|-----------|--------------|---------------|
| Purpose | Risky code | Handling code | Mandatory messages |
| Executes when | Always (no exception) | Only on exception | Always |
| Skipped when | Exception occurs | No exception | Never (except `os._exit(0)`) |
| Required? | Yes | Yes (≥1) | Optional |

| Feature | Built-in Exception | User-Defined Exception |
|---------|--------------------|------------------------|
| Examples | `ZeroDivisionError`, `ValueError` | `TooOldException`, `TooYoungException` |
| Created by | Python team | Programmer |
| Raised by | Python system automatically | Programmer using `raise` |
| Inherits from | `Exception` | `Exception` (mandatory) |
| Use case | Standard errors | Business logic validation |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: exceptions must derive from BaseException` | User-defined class does not inherit from `Exception` | Add `(Exception)` to the class definition |
| `NameError: name 'TooOldException' is not defined` | Using exception class before defining it | Define the class before using `raise` |
| Abnormal termination in nested try | Inner except class does not match exception | Check exception class name; outer except will handle it |
| `finally` not executing | `os._exit(0)` used before finally block | This is intended — remove `os._exit(0)` if you need finally to run |
| `AttributeError: 'TooOldException' has no attribute 'msg'` | Forgot to define `self.msg = arg` in constructor | Add constructor: `def __init__(self, arg): self.msg = arg` |

---

## Interview Questions

**Q: What is the finally block in Python?**
A: The finally block is an optional block in try-except-finally that always executes regardless of whether an exception was raised or handled. It is used for mandatory statements — code that must run no matter what, such as closing resources or printing completion messages.

**Q: In what situation does the finally block NOT execute?**
A: The finally block does not execute when `os._exit(0)` is called. This function shuts down the Python Virtual Machine immediately, preventing any further code from running.

**Q: What is nested try-except?**
A: A try, except, or finally block that contains another try-except-finally inside it is called nested try-except. If an exception occurs in the inner try block, the inner except handles it first. If inner except cannot handle it (wrong exception class), the outer except takes over.

**Q: How do you create a user-defined exception in Python?**
A: Create a class that inherits from `Exception`. Add a constructor that accepts a message argument and stores it in `self.msg`. Then use the `raise` keyword with your exception class to raise it where needed.

**Q: What is the `raise` keyword in Python?**
A: The `raise` keyword is used to manually raise exceptions. Built-in exceptions are raised automatically by Python, but user-defined exceptions must be raised explicitly using `raise ExceptionClassName("message")`. Java and C# use `throw` for the same purpose.

**Q: What are the two types of exceptions in Python?**
A: (1) Predefined/Built-in exceptions — already available in Python (`ZeroDivisionError`, `ValueError`, etc.). They are raised automatically by the system. (2) User-defined/Customized exceptions — created by the programmer when built-in exceptions don't meet requirements. They must be raised manually using the `raise` keyword.

---

## Try It Yourself

**Exercise 1:** Write a program with try-except-finally that divides two numbers. Show that the finally block always executes by printing "Calculation complete" in it.

<details><summary>Answer</summary>

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input — please enter integers")
finally:
    print("Calculation complete")    # always prints
```
</details>

---

**Exercise 2:** Demonstrate `os._exit(0)` stopping the finally block. Write a try-finally program and place `os._exit(0)` inside the try block. Observe that finally does NOT execute.

<details><summary>Answer</summary>

```python
import os

try:
    print("Inside try block")
    os._exit(0)               # PVM shuts down here
    print("This won't print")
finally:
    print("Finally block")    # this won't print either
```
</details>

---

**Exercise 3:** Create a user-defined exception `InvalidAgeException` that is raised when a user enters an age less than 0 or greater than 120. Handle it with try-except.

<details><summary>Answer</summary>

```python
class InvalidAgeException(Exception):
    def __init__(self, arg):
        self.msg = arg

try:
    age = int(input("Enter age: "))
    if age < 0 or age > 120:
        raise InvalidAgeException("Age must be between 0 and 120")
    print("Valid age:", age)
except InvalidAgeException as e:
    print("Error:", e.msg)
except ValueError:
    print("Please enter a valid integer")
```
</details>

---

**Exercise 4:** Write a nested try-except program where the inner try raises a `ZeroDivisionError`, but the inner except only handles `ValueError`. Show that the outer except handles the ZeroDivisionError.

<details><summary>Answer</summary>

```python
try:
    print("Outer try")
    try:
        print("Inner try")
        result = 10 / 0        # ZeroDivisionError
    except ValueError:         # wrong match
        print("Inner except")
    finally:
        print("Inner finally")
except ZeroDivisionError as msg:
    print("Outer except handled it:", msg)
finally:
    print("Outer finally")
```
</details>

---

**Exercise 5:** Create two user-defined exceptions: `NegativeNumberException` and `TooBigException`. Write a program that accepts a number and raises the appropriate exception if it's negative or greater than 1000.

<details><summary>Answer</summary>

```python
class NegativeNumberException(Exception):
    def __init__(self, arg):
        self.msg = arg

class TooBigException(Exception):
    def __init__(self, arg):
        self.msg = arg

try:
    n = int(input("Enter a number: "))
    if n < 0:
        raise NegativeNumberException("Number cannot be negative")
    elif n > 1000:
        raise TooBigException("Number cannot be greater than 1000")
    else:
        print("Valid number:", n)
except (NegativeNumberException, TooBigException) as e:
    print("Validation error:", e.msg)
except ValueError:
    print("Please enter a valid integer")
```
</details>
