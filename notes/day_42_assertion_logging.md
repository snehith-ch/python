# Day 42 — Assertion and Logging

← [Day 41](day_41_decorators_generators.md) | [Index](00_INDEX.md) | [Day 43](day_43_pandas_matplotlib_part1.md) →

---

## Quick Revision — Day 42

| # | Key Point |
|---|-----------|
| 1 | **Assertion** = debugging Python program using `assert` keyword |
| 2 | `assert conditional_expression, message` — if False, raises `AssertionError` |
| 3 | Advantage over `print`: assert statements need NOT be removed after debugging |
| 4 | Assertion handles **development-time errors**; exceptions handle **runtime errors** |
| 5 | **Logging** = creating log files to track program execution and exceptions |
| 6 | Python module: `import logging` (built-in) |
| 7 | 6 logging levels: CRITICAL(50) > ERROR(40) > WARNING(30) > INFO(20) > DEBUG(10) > NOTSET(0) |
| 8 | `logging.basicConfig(filename="log.txt", level=logging.WARNING)` sets up log file |
| 9 | Only messages at or above the set level are written to the log file |
| 10 | `logging.exception(message)` stores complete exception info (with traceback) to log file |

---

## Navigation

- **Pre-requisite:** [Day 31](day_31_exception_handling.md) — Exception handling; [Day 32](day_32_exception_advanced_custom.md) — try-except-finally
- **Next:** [Day 43](day_43_pandas_matplotlib_part1.md) — Pandas and Matplotlib
- **Related:** [Day 34](day_34_file_handling_advanced.md) — File handling (log files are text files)

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| Keyword | `assert` | Check conditions during debugging |
| Statement | `assert expr, "message"` | Raise AssertionError if expr is False |
| Module | `logging` | Built-in module for creating log files |
| Function | `logging.basicConfig(filename, level)` | Configure log file and minimum level |
| Function | `logging.debug(msg)` | Log a DEBUG level message |
| Function | `logging.info(msg)` | Log an INFO level message |
| Function | `logging.warning(msg)` | Log a WARNING level message |
| Function | `logging.error(msg)` | Log an ERROR level message |
| Function | `logging.critical(msg)` | Log a CRITICAL level message |
| Function | `logging.exception(msg)` | Log exception info with traceback to log file |

---

## 1. Assertion

### 1.1 Why Not Just Use print() for Debugging?

```
Problem with print() for debugging:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Add print statements throughout code for debugging
2. Identify and fix the bug
3. MUST remove all extra print statements afterward
4. If you forget to remove one → console output is cluttered
5. End user sees unwanted debug messages

With assert statements:
1. Add assert statements for debugging
2. Identify and fix the bug
3. No need to remove assert statements
4. If condition is True → executes silently (no output)
5. If condition is False → raises AssertionError with message
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 1.2 Assert Syntax

```python
assert conditional_expression, message
```

- If `conditional_expression` is **True** → program continues normally (no output)
- If `conditional_expression` is **False** → raises `AssertionError` with `message`

### 1.3 Assert Example

```python
def square(n):
    return n ** 2    # Bug: ** means power, should be * for multiply
                     # n ** 2 = n^2 which IS correct for square, 
                     # but n ** 1 would be n^1 which is wrong


# Debug with print (old way — must remove after fixing):
# print("square(3) should be 9:", square(3))    # shows 9

# Debug with assert (better way — no need to remove):
assert square(3) == 9,   "Square of 3 should be 9"
assert square(4) == 16,  "Square of 4 should be 16"
assert square(5) == 25,  "Square of 5 should be 25"
```

**With correct code (n * n):**
```
→ All assertions pass silently → no output → clean console
```

**With buggy code (n ** 3 accidentally):**
```
AssertionError: Square of 3 should be 9
```

### 1.4 Assert Demo — Finding a Bug

```python
def square(n):
    return n ** 3    # BUG: should be n*n or n**2


# These asserts immediately reveal the bug
assert square(3) == 9,  "Square of 3 should be 9"
# → AssertionError: Square of 3 should be 9
# → Programmer checks: oh, ** 3 is wrong, should be * n
```

Fix → use `n * n` → all asserts pass silently → debugging complete — **no cleanup needed**.

---

## 2. Assertion vs Exception

```
Feature             Assertion                  Exception Handling
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Purpose             Debug development errors   Handle runtime errors
Raised by           assert keyword             try-except-finally
Who is alerted      Developer/programmer        End user
When errors occur   During development          During production/runtime
Keyword             assert                      try / except / raise
Can be disabled     Yes (python -O flag)        No
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 3. Logging

### 3.1 What Is Logging?

```
Logging
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Logging = means of tracking events while software runs

Purpose:
  → Store complete program execution flow in a log file
  → Store exception information with traceback
  → Help developers debug problems without being present

Real-world flow:
  Developer writes code → Tester finds issues → Tester cannot
  explain verbally → Log file is generated → Log file shared
  with developer → Developer reads log and fixes the issue

Module: import logging (built-in)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3.2 Logging Levels

| Level | Number | Represents |
|-------|--------|------------|
| CRITICAL | 50 | Very serious problem — needs highest attention |
| ERROR | 40 | Serious error — attention required |
| WARNING | 30 | Warning message — caution required |
| INFO | 20 | Informational message |
| DEBUG | 10 | Debug information |
| NOTSET | 0 | Level not set |

> When you set a level, **only that level and higher** are written to the log file. Setting `WARNING` means WARNING + ERROR + CRITICAL are logged. Setting `DEBUG` means ALL messages are logged.

### 3.3 Basic Logging Setup

```python
import logging

# Create log file and set minimum level
logging.basicConfig(
    filename="log.txt",          # log file name
    level=logging.WARNING        # minimum level to log
)

# Log messages at different levels
logging.debug("This is debug message")      # NOT written (below WARNING)
logging.info("This is info message")        # NOT written (below WARNING)
logging.warning("This is warning message")  # written
logging.error("This is error message")      # written
logging.critical("This is critical message") # written
```

**Contents of `log.txt`:**
```
WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message
```

### 3.4 Log All Messages (level=DEBUG)

```python
logging.basicConfig(filename="log.txt", level=logging.DEBUG)

logging.debug("debug message")    # now written
logging.info("info message")      # now written
logging.warning("warning")        # written
logging.error("error")            # written
logging.critical("critical")      # written
```

All 5 messages appear in `log.txt`.

### 3.5 Logging Exceptions to Log File

```python
import logging

logging.basicConfig(filename="mylog.txt", level=logging.INFO)

con = None

try:
    logging.info("New request came")
    
    x = int(input("Enter num1: "))
    y = int(input("Enter num2: "))
    result = x / y
    print(f"Result: {result}")

except ZeroDivisionError as msg:
    print("Cannot divide with zero")
    logging.exception(msg)    # stores full exception + traceback to log file

except ValueError as msg:
    print("Please provide integer values only")
    logging.exception(msg)

finally:
    logging.info("Request process completed")
```

**Contents of `mylog.txt` (after ZeroDivisionError):**
```
INFO:root:New request came
ERROR:root:division by zero
Traceback (most recent call last):
  File "gen.py", line 9, in <module>
    result = x / y
ZeroDivisionError: division by zero
INFO:root:Request process completed
```

> `logging.exception(msg)` automatically stores the exception message, traceback, file name, line number, and error type — everything a developer needs to diagnose the issue.

**Contents when correct input (no exceptions):**
```
INFO:root:New request came
INFO:root:Request process completed
```

---

## 4. Complete Logging Reference

```python
import logging

# Setup
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG    # log everything
)

# Log at different levels
logging.debug("Debug info here")
logging.info("User logged in")
logging.warning("Disk space low")
logging.error("File not found")
logging.critical("System crash!")

# Log exception with full traceback
try:
    x = 1 / 0
except ZeroDivisionError as e:
    logging.exception(e)    # logs: ERROR level + traceback
```

---

## 5. assert vs print vs logging

| Feature | `print` | `assert` | `logging` |
|---------|---------|----------|-----------|
| Purpose | Debug output | Condition check | Track execution |
| Remove after debug? | Yes — must remove | No — keeps silently | No — stays in log file |
| Output location | Console | Console (on fail) | Log file |
| Used in production? | No (bad practice) | No (dev only) | Yes — essential |
| End user sees? | Yes (bad) | Only if assert fails | No (file only) |

---

## Student Q&A

> **Student Question:** What is assertion and why is it better than using print for debugging?
> **Answer:** Assertion is debugging using the `assert` keyword. `assert condition, "message"` — if the condition is True, nothing happens; if False, AssertionError is raised with the message. It is better than print because: (1) print statements must be manually removed after debugging — if forgotten, end users see the debug messages; (2) assert statements can stay in code forever — when the condition is True they're completely silent, and only fail with an error message when a bug is detected.

> **Student Question:** What is the difference between assertion and exception handling?
> **Answer:** Assertion handles development-time errors — the developer uses `assert` to verify conditions while writing and testing code. Exception handling (`try-except`) handles runtime errors — unexpected situations when end users run the program (like dividing by zero or invalid input). Assertions alert the programmer; exceptions alert the end user.

> **Student Question:** What is logging and why do we need it?
> **Answer:** Logging is creating log files to track the execution flow and exceptions of a program. In real-time: developers write code, testers test it. When testers find bugs, they cannot always explain them to developers verbally — instead, log files capture exactly what happened (which function ran, what exception occurred, at what line, with traceback). Developers read the log file to diagnose and fix issues. Python's built-in `logging` module creates these files.

> **Student Question:** What is the difference between logging levels?
> **Answer:** Logging levels are numeric priorities: CRITICAL(50) > ERROR(40) > WARNING(30) > INFO(20) > DEBUG(10) > NOTSET(0). When you set a minimum level in `basicConfig`, only messages at that level or higher are written to the log file. For example: `level=WARNING` writes only WARNING, ERROR, CRITICAL. `level=DEBUG` writes all 5 levels. Use the lowest level (DEBUG) during development and higher levels (WARNING or ERROR) in production.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `AssertionError` with no message | Used `assert condition` without message | Add message: `assert condition, "message"` |
| Log file not created | `basicConfig()` not called before logging | Call `logging.basicConfig(filename=..., level=...)` first |
| Nothing written to log file | Level too high for the messages | Lower the level in `basicConfig` or use higher-level log functions |
| Log file keeps growing | `basicConfig` opens file in append mode by default | Add `filemode='w'` to overwrite each run |

---

## Interview Questions

**Q: What is assertion in Python?**
A: Assertion is a debugging technique using the `assert` keyword. Syntax: `assert conditional_expression, message`. If the expression evaluates to True, the program continues normally. If False, it raises an `AssertionError` with the message. The advantage over `print` is that assert statements need not be removed after debugging — they stay silent when the condition is True and only surface an error when a bug exists.

**Q: What is the difference between assertion and exception handling?**
A: Assertion (`assert`) is for development-time debugging — the developer uses it to check conditions and verify logic during coding and testing. Exception handling (`try-except`) is for runtime errors — it protects end users from unexpected conditions like invalid input or zero division during production use. Assert alerts the developer; exception handling protects the end user.

**Q: What is logging in Python?**
A: Logging is the process of recording events, messages, and exceptions that occur during program execution to a log file. Python's built-in `logging` module provides functions like `debug()`, `info()`, `warning()`, `error()`, `critical()`, and `exception()`. Use `logging.basicConfig(filename="log.txt", level=logging.WARNING)` to configure the log file and minimum message level.

**Q: What are logging levels in Python?**
A: Python has 6 logging levels: CRITICAL(50), ERROR(40), WARNING(30), INFO(20), DEBUG(10), NOTSET(0). When setting `level=logging.WARNING`, only WARNING, ERROR, and CRITICAL messages are written to the log file. `level=logging.DEBUG` logs all messages. Choose the level based on how much information you want to capture in production vs development.

---

## Try It Yourself

**Exercise 1:** Write a function `divide(a, b)` that divides `a` by `b`. Use `assert` statements to verify that `divide(10, 2)` returns `5.0` and `divide(9, 3)` returns `3.0`.

<details><summary>Answer</summary>

```python
def divide(a, b):
    return a / b


assert divide(10, 2) == 5.0, "divide(10, 2) should be 5.0"
assert divide(9, 3) == 3.0,  "divide(9, 3) should be 3.0"
print("All assertions passed — function is correct")
```
</details>

---

**Exercise 2:** Set up a log file `app.log` with level DEBUG. Write log messages at all five levels and verify what gets written to the file.

<details><summary>Answer</summary>

```python
import logging

logging.basicConfig(filename="app.log", level=logging.DEBUG)

logging.debug("Starting application")
logging.info("User connected")
logging.warning("Low memory warning")
logging.error("File read failed")
logging.critical("System shutdown")

# app.log will contain all 5 messages since level=DEBUG
```
</details>

---

**Exercise 3:** Write a program that takes two numbers from the user, divides them, and logs exceptions to `error.log` using `logging.exception()`. Use try-except-finally.

<details><summary>Answer</summary>

```python
import logging

logging.basicConfig(filename="error.log", level=logging.INFO)

try:
    logging.info("Request started")
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(f"Result: {a / b}")

except ZeroDivisionError as e:
    print("Cannot divide by zero")
    logging.exception(e)

except ValueError as e:
    print("Please enter integers only")
    logging.exception(e)

finally:
    logging.info("Request completed")
```
</details>
