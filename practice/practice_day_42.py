# ============================================================
# PRACTICE — Day 42: Assertion and Logging
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: assert Statement
# --------------------------------------------------

# Q1. Predict — assert with True condition (silent):

x = 10
assert x > 0, "x must be positive"    # prediction: error or silent?
print("Q1: No error")                  # prediction: prints or not?


# Q2. Predict — assert with False condition:

# assert 5 > 10, "5 is not greater than 10"    # uncomment → prediction (error type + message?):


# Q3. Predict — debugging a function with assert:

def multiply(a, b):
    return a + b    # BUG: should be a * b

# These asserts will FAIL (function has a bug):
# assert multiply(2, 3) == 6, "multiply(2,3) should be 6"
# assert multiply(4, 5) == 20, "multiply(4,5) should be 20"

# Prediction when uncommented:
# - assert multiply(2, 3) == 6  → error or passes?
# - What is the AssertionError message?

# YOUR ANSWER:


# Q4. Fix the function and re-test — predict:

def multiply_fixed(a, b):
    return a * b    # fixed

assert multiply_fixed(2, 3) == 6,   "multiply(2,3) should be 6"
assert multiply_fixed(4, 5) == 20,  "multiply(4,5) should be 20"
assert multiply_fixed(0, 9) == 0,   "multiply(0,9) should be 0"
print("All assertions passed!")    # prediction: prints or error?


# Q5. assert vs print — predict the difference:

def check_with_print(value):
    print(f"DEBUG: value = {value}")    # always prints
    return value * 2

def check_with_assert(value):
    assert value > 0, "value must be positive"    # silent if True
    return value * 2

result1 = check_with_print(5)    # prediction (prints?):
result2 = check_with_assert(5)   # prediction (prints?):

print(result1, result2)          # prediction:


# Q6. assert with complex condition — predict:

name = "Alice"
age = 25

assert isinstance(name, str) and len(name) > 0, "name must be non-empty string"
assert 0 <= age <= 120, "age must be 0-120"
print("Validation passed")    # prediction:

# What if age = -5?
# assert 0 <= -5 <= 120, "age must be 0-120"    # uncomment → prediction:


# --------------------------------------------------
# SECTION 2: Logging
# --------------------------------------------------

# Q7. Predict the logging level numbers:

import logging

print(logging.CRITICAL)    # prediction:
print(logging.ERROR)       # prediction:
print(logging.WARNING)     # prediction:
print(logging.INFO)        # prediction:
print(logging.DEBUG)       # prediction:
print(logging.NOTSET)      # prediction:


# Q8. What gets logged? — predict (don't run — conceptual):

# logging.basicConfig(filename="app.log", level=logging.WARNING)
# logging.debug("Debug info")      → logged or not?
# logging.info("Info message")     → logged or not?
# logging.warning("Warning!")      → logged or not?
# logging.error("Error!")          → logged or not?
# logging.critical("Critical!")    → logged or not?

# YOUR ANSWERS (when level=WARNING):


# Q9. Logging to console (no file) — predict:

import logging

# Reset logging (needed in practice since basicConfig is called once)
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(message)s')

logging.debug("Starting program")
logging.info("Processing...")
logging.warning("Low memory")
logging.error("File missing")
logging.critical("System failure")

# prediction (5 lines with level prefix):


# Q10. Log file creation — predict the file content:

import logging
import os

# Remove old log if exists
if os.path.isfile("practice.log"):
    os.remove("practice.log")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename="practice.log", level=logging.INFO,
                    filemode='w')

logging.info("App started")
logging.warning("Low battery")
logging.error("Connection failed")

# prediction: how many lines in practice.log?
# (only INFO and above when level=INFO)


# Q11. logging.exception() — predict behavior:

import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename="errors.log", level=logging.DEBUG,
                    filemode='w')

try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.exception(e)    # stores exception + traceback

# prediction: what information is stored in errors.log?
# a) Just the error message
# b) Error message + traceback (file, line number, error type)
# c) Nothing (exception is only for raising, not logging)

# YOUR ANSWER:


# --------------------------------------------------
# SECTION 3: assert vs print vs logging
# --------------------------------------------------

# Q12. Fill in which tool to use for each scenario:

# a) During development, check that a calculation is correct:     ?
# b) Record all exceptions to a file for the testing team:        ?
# c) Quickly add and then manually remove a debug print:          ?  (NOT recommended!)
# d) Track production program execution flow permanently:         ?
# e) Alert programmer if a function receives invalid input:       ?

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q13. Write a function factorial(n) with assert:
#   - Asserts n >= 0 (can't compute factorial of negative)
#   - Returns n! (use a loop or recursion)
#   - Test with factorial(5), factorial(0), then trigger the assert with factorial(-1)

# YOUR CODE HERE:


# Q14. Write a logging setup that:
#   - Logs to "app.log" at INFO level
#   - At program start: logs "Application started"
#   - Calls a division function in a try-except
#   - On ZeroDivisionError: uses logging.exception() to log the error
#   - In finally: logs "Application ended"

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — assertion can be disabled with -O flag (optimize):
# When Python runs with: python -O script.py
# All assert statements are SKIPPED.
# a) Is this useful in production? Why?
# b) Should you use assert for critical security checks?

# YOUR ANSWERS:


# BONUS 2: Predict — assert with no message:

# assert False    # uncomment → prediction (error message?):
# assert False, "Custom message"    # uncomment → prediction:

# What is the difference in the error output?


# BONUS 3: Log multiple messages and read the file:

import logging, os

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

if os.path.isfile("bonus.log"):
    os.remove("bonus.log")

logging.basicConfig(filename="bonus.log", level=logging.DEBUG,
                    filemode='w', format='%(levelname)s:%(message)s')

for i in range(3):
    logging.debug(f"Step {i}")

logging.warning("Something odd")

with open("bonus.log", "r") as f:
    print(f.read())    # prediction (4 lines):



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. assert condition, "message"  raises _______ if condition is False.
#    A) ValueError    B) AssertionError    C) RuntimeError    D) SyntaxError
# Answer: ___

# Q_MCQ_2. Python assertions can be disabled globally by running with:
#    A) python -d    B) python -O    C) python --no-assert    D) python -A
# Answer: ___

# Q_MCQ_3. Which logging level is the LEAST severe?
#    A) WARNING    B) ERROR    C) DEBUG    D) CRITICAL
# Answer: ___

# Q_MCQ_4. logging.basicConfig(level=logging.WARNING) means:
#    A) Only WARNING and above messages are shown
#    B) Only WARNING messages are shown
#    C) DEBUG and INFO are shown too
#    D) All levels are suppressed
# Answer: ___

# Q_MCQ_5. What is the default logging level if not set?
#    A) DEBUG    B) INFO    C) WARNING    D) ERROR
# Answer: ___

# Q_MCQ_6. logging.debug("msg")  is typically used for:
#    A) Production error alerts    B) Development/diagnostic information
#    C) Critical system failures    D) User-facing messages
# Answer: ___

# Q_MCQ_7. To write logs to a file instead of console:
#    A) print("log", file=f)    B) logging.basicConfig(filename="app.log")
#    C) logging.FileHandler only    D) Not possible in Python
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. assert x > 0, "_______"  — the string after the comma is the
#         _______ message shown if the assertion fails.

# FIB_2. Assertions are best used for _______ checks (developer errors),
#         not for handling runtime user errors.

# FIB_3. Logging severity from low to high:
#         DEBUG < _______ < WARNING < ERROR < CRITICAL

# FIB_4. logging.basicConfig(level=logging._______) shows ALL log levels.

# FIB_5. A Logger can have multiple _______ (e.g., FileHandler + StreamHandler).

# FIB_6. logging.getLogger(_______) gets the module-level logger by name.

# FIB_7. logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
#         adds a _______ to each log line.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Bank Transaction Logger with assertions and proper logging.
#
# Requirements:
#   1. Create a BankAccount class with: balance, deposit(amt), withdraw(amt)
#   2. Use assert to validate: deposit amount > 0, withdrawal <= balance
#   3. Set up logging to BOTH console (INFO+) and "bank.log" (DEBUG+)
#   4. Log every deposit/withdrawal at INFO level
#   5. Log assertion errors at ERROR level (catch AssertionError)
#   6. Log the final balance at INFO level
#   7. Test with: 3 valid transactions + 1 invalid withdrawal + 1 negative deposit
#
# Expected output (console):
#   INFO:bank: Account created. Balance: 1000
#   INFO:bank: Deposited 500. Balance: 1500
#   INFO:bank: Withdrew 200. Balance: 1300
#   ERROR:bank: AssertionError: Withdrawal 2000 exceeds balance 1300
#   ERROR:bank: AssertionError: Deposit amount must be positive
#   INFO:bank: Final balance: 1300
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: Silent (True condition) → prints "Q1: No error"

# Q2: AssertionError: 5 is not greater than 10

# Q3: AssertionError: multiply(2,3) should be 6
#     (2 + 3 = 5, not 6)

# Q4: All pass silently → prints "All assertions passed!"

# Q5: check_with_print(5): prints "DEBUG: value = 5" (always visible)
#     check_with_assert(5): silent (5 > 0 is True)
#     result1=10, result2=10 → prints "10 10"

# Q6: "Validation passed"; age=-5 → AssertionError: age must be 0-120

# Q7: 50, 40, 30, 20, 10, 0

# Q8: debug=NO, info=NO, warning=YES, error=YES, critical=YES

# Q9: DEBUG: Starting program, INFO: Processing..., WARNING: Low memory,
#     ERROR: File missing, CRITICAL: System failure

# Q10: 3 lines (INFO, WARNING, ERROR — all at or above INFO level)

# Q11: b) Error message + full traceback (file, line, ZeroDivisionError: division by zero)

# Q12: a)assert, b)logging.exception(), c)print (bad!), d)logging, e)assert

# BONUS 1: a) Yes — disabling asserts speeds up production code
#          b) NO — asserts can be disabled; use if/raise for security checks

# BONUS 2: "AssertionError" (no message), "AssertionError: Custom message"

# BONUS 3: DEBUG:Step 0, DEBUG:Step 1, DEBUG:Step 2, WARNING:Something odd

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: C   Q_MCQ_4: A
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: AssertionError  (the string is the error message)
# FIB_2: internal / invariant / programmer
# FIB_3: INFO
# FIB_4: DEBUG
# FIB_5: handlers
# FIB_6: __name__  (the module name)
# FIB_7: timestamp

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import logging
#
# logger = logging.getLogger("bank")
# logger.setLevel(logging.DEBUG)
# fmt = logging.Formatter("%(levelname)s:%(name)s: %(message)s")
# sh = logging.StreamHandler(); sh.setLevel(logging.INFO); sh.setFormatter(fmt)
# fh = logging.FileHandler("bank.log"); fh.setLevel(logging.DEBUG); fh.setFormatter(fmt)
# logger.addHandler(sh); logger.addHandler(fh)
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#         logger.info(f"Account created. Balance: {self.balance}")
#     def deposit(self, amt):
#         assert amt > 0, f"Deposit amount must be positive"
#         self.balance += amt
#         logger.info(f"Deposited {amt}. Balance: {self.balance}")
#     def withdraw(self, amt):
#         assert amt <= self.balance, f"Withdrawal {amt} exceeds balance {self.balance}"
#         self.balance -= amt
#         logger.info(f"Withdrew {amt}. Balance: {self.balance}")
#
# acc = BankAccount(1000)
# for op, val in [("deposit",500),("withdraw",200),("withdraw",2000),("deposit",-100)]:
#     try:
#         getattr(acc, op)(val)
#     except AssertionError as e:
#         logger.error(f"AssertionError: {e}")
# logger.info(f"Final balance: {acc.balance}")

