# ============================================================
# PRACTICE — Day 31: Exception Handling
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Types of Errors
# --------------------------------------------------

# Q1. Identify the error type and predict what happens:

# a) Syntactical error — uncomment to see:
# if True
#     print("hello")    # prediction (error type):

# b) Runtime error:
# x = 10 / 0           # uncomment → prediction (error name):

# c) Logical error (no exception — just wrong output):
def avg(a, b):
    return a + b / 2    # bug: should be (a + b) / 2

print(avg(4, 6))    # prediction (expected 5.0, actual?):


# --------------------------------------------------
# SECTION 2: try-except Basics
# --------------------------------------------------

# Q2. Predict the output for each input scenario:

def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")

safe_divide(10, 2)    # prediction:
safe_divide(10, 0)    # prediction:
safe_divide(7, 3)     # prediction:


# Q3. Default except vs specific except — predict:

def test(value):
    try:
        x = int(value)
        print(f"Converted: {x}")
    except ValueError:
        print("ValueError caught")
    except:
        print("Some other error caught")

test("42")      # prediction:
test("hello")   # prediction:
test(None)      # prediction (int(None) raises what?):


# Q4. Predict the flow — 4 cases:

def demo(a, b):
    print("Before try")
    try:
        result = a / b
        print(f"Inside try: {result}")
    except ZeroDivisionError:
        print("Inside except")
    print("After try-except")

# Case 1: no exception
demo(10, 2)
print("---")

# Case 2: exception raised
demo(10, 0)
print("---")

# What is the prediction for each? (3 lines for case 1, 3 lines for case 2)


# --------------------------------------------------
# SECTION 3: Multiple except Blocks
# --------------------------------------------------

# Q5. Predict which except catches each call:

def process(value, index):
    data = [10, 20, 30]
    try:
        x = int(value)
        result = data[index] / x
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")
    except IndexError:
        print("IndexError")

process("2", 1)     # prediction: 20/2 = ?
process("0", 1)     # prediction: 20/0 → ?
process("abc", 0)   # prediction: int("abc") → ?
process("5", 10)    # prediction: data[10] → ?


# Q6. Catching multiple errors in one except — predict:

def risky(x, y):
    try:
        return x / y + int(x)
    except (ZeroDivisionError, ValueError) as msg:
        print(f"Caught: {msg}")

print(risky(10, 2))     # prediction:
print(risky(10, 0))     # prediction (ZeroDivisionError):
print(risky("a", 1))    # prediction (ValueError from int("a")):


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q7. Write a function safe_list_access(lst, index):
#   - Tries to return lst[index]
#   - Catches IndexError: prints "Index out of range"
#   - Catches TypeError: prints "Invalid index type"
# Test with: safe_list_access([1,2,3], 1), safe_list_access([1,2,3], 10),
#            safe_list_access([1,2,3], "a")

# YOUR CODE HERE:


# Q8. Write a function parse_and_double(s):
#   - Converts s to int, doubles it, returns result
#   - Catches ValueError: returns None and prints "Not a number"
# Test with "5", "abc", "0"

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict ALL output — trace carefully:

def chain(x):
    try:
        a = 10 / x
        b = int("hello")    # always fails
        print(f"a={a}, b={b}")
    except ZeroDivisionError:
        print("ZeroDivision")
    except ValueError:
        print("ValueError")
    print("Done")

chain(2)    # prediction (2 lines):
chain(0)    # prediction (2 lines):


# BONUS 2: Predict — what does `as msg` give you?

try:
    x = int("abc")
except ValueError as msg:
    print(type(msg))    # prediction:
    print(msg)          # prediction (exact message):
    print(str(msg))     # prediction (same as above?):


# BONUS 3:
# Write a program that:
# 1. Asks user for two numbers
# 2. Handles ValueError (non-numeric input) and ZeroDivisionError
# 3. Prints the division result or appropriate error message
# (Don't actually use input() — pass values directly to a function)

# YOUR CODE HERE:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Which block runs ONLY when an exception occurs?
#    A) try    B) except    C) else    D) finally
# Answer: ___

# Q_MCQ_2. What happens if you use a bare  except:  clause?
#    A) Catches only ValueError
#    B) Catches ALL exceptions including SystemExit
#    C) Raises a SyntaxError
#    D) Only catches user-defined exceptions
# Answer: ___

# Q_MCQ_3. What does  except (ValueError, TypeError):  do?
#    A) Catches ValueError first, then TypeError separately
#    B) Catches either ValueError or TypeError in one handler
#    C) Raises both at once
#    D) SyntaxError — cannot combine exceptions
# Answer: ___

# Q_MCQ_4. Which block executes REGARDLESS of whether an exception occurred?
#    A) try    B) except    C) else    D) finally
# Answer: ___

# Q_MCQ_5. What is the output?
#    try:
#        x = int("abc")
#    except ValueError as e:
#        print("caught")
#    else:
#        print("no error")
#    A) caught no error    B) no error    C) caught    D) nothing
# Answer: ___

# Q_MCQ_6. ZeroDivisionError is raised when:
#    A) int("0")    B) 10 / 0    C) 10 // 1    D) 0 ** 0
# Answer: ___

# Q_MCQ_7. Which is NOT a built-in Python exception?
#    A) ValueError    B) TypeError    C) KeyError    D) NullPointerError
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. The  _______  block contains code that might raise an exception.

# FIB_2. To access the exception message use  except ExceptionType as _______:

# FIB_3. int("hello")  raises a _______ exception.

# FIB_4. my_list[99]  on a 3-element list raises _______.

# FIB_5. The  _______  block runs only if no exception was raised in try.

# FIB_6. my_dict["missing_key"]  raises _______.

# FIB_7. To prevent crashes from bad user input, wrap  int(input(...))  in a
#         _______ block.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Build a Robust Calculator that handles all common errors.
#
# Requirements:
#   1. Ask the user for two numbers and an operator (+, -, *, /)
#   2. Handle ValueError if non-numeric input is entered
#   3. Handle ZeroDivisionError for division by zero
#   4. Handle KeyError / unsupported operator with a clear message
#   5. Use the else block to print the result only when no error
#   6. Use finally to always print "Calculator session ended."
#   7. Loop until the user types "quit" as the first number
#
# Expected output (example run):
#   Enter first number (or 'quit'): 10
#   Enter second number: 0
#   Enter operator (+,-,*,/): /
#   Error: Cannot divide by zero!
#   Calculator session ended.
#   Enter first number (or 'quit'): 10
#   Enter second number: 5
#   Enter operator (+,-,*,/): *
#   Result: 50.0
#   Calculator session ended.
#   Enter first number (or 'quit'): quit
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: avg(4,6) → 4 + 6/2 = 4 + 3 = 7 (wrong! expected 5.0)

# Q2: "Result: 5.0", "Cannot divide by zero", "Result: 2.3333..."

# Q3: "Converted: 42", "ValueError caught", "Some other error caught"
#     (int(None) raises TypeError, caught by default except)

# Q4: Case 1: "Before try", "Inside try: 5.0", "After try-except"
#     Case 2: "Before try", "Inside except", "After try-except"

# Q5: "Result: 10.0", "ZeroDivisionError", "ValueError", "IndexError"

# Q6: 15.0, "Caught: division by zero", "Caught: invalid literal for int()..."
#     (risky("a",1) fails at int("a") before division)

# BONUS 1: "ValueError", "Done" for chain(2)  — ZeroDivision doesn't happen, ValueError does
#          "ZeroDivision", "Done" for chain(0) — fails at 10/0 before int("hello")

# BONUS 2: <class 'ValueError'>, "invalid literal for int() with base 10: 'abc'", same

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: D
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: D

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: try
# FIB_2: e  (or any variable name — 'e' is convention)
# FIB_3: ValueError
# FIB_4: IndexError
# FIB_5: else
# FIB_6: KeyError
# FIB_7: try/except

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# ops = {"+": lambda a,b: a+b, "-": lambda a,b: a-b,
#         "*": lambda a,b: a*b, "/": lambda a,b: a/b}
# while True:
#     first = input("Enter first number (or 'quit'): ")
#     if first.lower() == "quit":
#         break
#     try:
#         a = float(first)
#         b = float(input("Enter second number: "))
#         op = input("Enter operator (+,-,*,/): ")
#         if op not in ops:
#             raise KeyError(f"Unknown operator: {op}")
#         result = ops[op](a, b)
#     except ValueError:
#         print("Error: Please enter valid numbers!")
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero!")
#     except KeyError as e:
#         print(f"Error: {e}")
#     else:
#         print(f"Result: {result}")
#     finally:
#         print("Calculator session ended.")

