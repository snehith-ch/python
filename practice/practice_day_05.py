# ============================================================
# PRACTICE — Day 5: Data Types, Type Casting, input(), bool, complex
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: None TYPE
# --------------------------------------------------

# Q1. What is the output of each print?
#     Predict first, then uncomment and run.

result = None
# print(result)
# print(type(result))

# Prediction:
# Line 1 output:
# Line 2 output:


# Q2. Fix the bug — the developer used 'null' instead of Python's keyword:

# score = null
# print(score)

# YOUR FIX HERE:


# Q3. A variable 'connection' starts as None, then gets a value.
#     Write code to:
#     - Declare connection = None and print its type
#     - Reassign connection = "database_connected" and print its type

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 2: int AND float
# --------------------------------------------------

# Q4. Predict the output of each type() call:

a = 100
b = -50
c = 0
d = 3.14
e = -0.001
f = 100.0

# print(type(a))   # prediction:
# print(type(b))   # prediction:
# print(type(c))   # prediction:
# print(type(d))   # prediction:
# print(type(e))   # prediction:
# print(type(f))   # prediction:  ← careful! 100.0 not 100


# Q5. IMPORTANT: What does int() do to a float?
#     Predict the output of each line:

# print(int(9.9))    # prediction:
# print(int(9.1))    # prediction:
# print(int(-9.9))   # prediction:  ← tricky!
# print(int(0.99))   # prediction:

# KEY QUESTION: Does int() round or truncate?
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 3: TYPE CASTING
# --------------------------------------------------

# Q6. Fill in the blank — which conversion function to use?

price = "499"
# To add 100 to price, I need to convert it using: ___________
# Write the working code:


# Q7. Chain of conversions — predict the final value and type:

x = "12.75"
y = float(x)
z = int(y)
# print(z, type(z))
# Prediction: value = ___, type = ___


# Q8. FIX THE BUG — this crashes with ValueError:
#
# result = int("hello")
# print(result)
#
# WHY does it crash?
# HOW would you safely convert only if the string is a number?
# (Hint: use a condition or try/except — just write the logic in comments for now)

# YOUR EXPLANATION:


# Q9. Convert in both directions and verify:

num = 42
as_float = float(num)
as_str   = str(num)
as_bool  = bool(num)

print(as_float, type(as_float))
print(as_str,   type(as_str))
print(as_bool,  type(as_bool))


# --------------------------------------------------
# SECTION 4: input() — THE STRING TRAP
# --------------------------------------------------

# Q10. THE CLASSIC BUG — read this code and answer the questions
#      WITHOUT running it first:
#
# a = input("Enter a number: ")
# b = input("Enter another: ")
# print(a + b)
#
# Q10a. If the user types 5 and 3, what is the output?  ___________
# Q10b. Why?  ___________
# Q10c. How do you fix it?  ___________


# Q11. Write a program that:
#      - Asks the user for their name (string — no casting needed)
#      - Asks for their age (needs casting to int)
#      - Prints:  Hello [name], you are [age] years old.

# YOUR CODE HERE:


# Q12. Write a program that:
#      - Asks the user to enter a float number
#      - Prints its integer version (truncated)
#      - Prints whether it is greater than 10 (True/False)

# YOUR CODE HERE:


# Q13. PREDICT — what type does input() always return?
#      Circle one:   int   /   float   /   str   /   depends on input
#
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 5: bool
# --------------------------------------------------

# Q14. Predict the output of each line:

# print(bool(0))       # prediction:
# print(bool(1))       # prediction:
# print(bool(-5))      # prediction:
# print(bool(0.0))     # prediction:
# print(bool(3.14))    # prediction:
# print(bool(""))      # prediction:  ← empty string
# print(bool("hi"))    # prediction:
# print(bool(None))    # prediction:


# Q15. Arithmetic with booleans — predict:

# print(True + True)         # prediction:
# print(True + True + True)  # prediction:
# print(False + False)       # prediction:
# print(10 + True)           # prediction:
# print(10 - False)          # prediction:
# print(True * 5)            # prediction:


# Q16. Which comparison gives True and which gives False?

x = 15
# print(x > 10)    # prediction:
# print(x == 15)   # prediction:
# print(x < 5)     # prediction:
# print(x != 20)   # prediction:


# --------------------------------------------------
# SECTION 6: complex
# --------------------------------------------------

# Q17. Create a complex number with real=4, imaginary=7
#      and print:  the number, its real part, its imaginary part, its type

# YOUR CODE HERE:


# Q18. Add two complex numbers:
#      a = 3 + 5j
#      b = 2 + 4j
#      Print their sum.
#      Predicted sum: ___________

# YOUR CODE HERE:


# Q19. Does Python use 'i' or 'j' for the imaginary part?
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 7: dir() and help()
# --------------------------------------------------

# Q20. Run this — how many methods does str have?
methods = dir(str)
print("Number of str methods:", len(methods))
# Count:


# Q21. Which function gives you FULL DOCUMENTATION (with descriptions)?
#      a) dir(str)
#      b) help(str)
#      c) type(str)
# YOUR ANSWER:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Write a program that accepts a student's 3 subject marks
# at runtime (use input + int conversion), calculates and
# prints the average as a float.

# YOUR CODE HERE:


# BONUS 2:
# A shopkeeper wants a bill calculator.
# Ask the user for:
#   - Item name (string)
#   - Price per item (float)
#   - Quantity (int)
# Print:  [item name]: Rs. [total]  where total = price * quantity

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL the output of this program WITHOUT running it.
# Then run it to verify.

p = "5"
q = "3"
print(p + q)
print(int(p) + int(q))
print(float(p) + float(q))
print(bool(p))
print(bool(int(p) - 5))

# Your full prediction:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1:  None  /  <class 'NoneType'>

# Q2:
# score = None
# print(score)

# Q3:
# connection = None
# print(type(connection))       # <class 'NoneType'>
# connection = "database_connected"
# print(type(connection))       # <class 'str'>

# Q4: int, int, int, float, float, float  (100.0 is float even though it looks like a whole number)

# Q5:
# int(9.9)   → 9    (NOT 10 — truncates, does NOT round)
# int(9.1)   → 9
# int(-9.9)  → -9   (tricky! truncates toward zero, not toward -10)
# int(0.99)  → 0
# KEY: int() TRUNCATES (drops decimal), does NOT round

# Q6:
# int() or float()  — use int() if you want whole numbers
# result = int(price) + 100
# print(result)   # 599

# Q7: value = 12, type = <class 'int'>

# Q8:
# Crash reason: "hello" cannot be converted to a number
# Safe approach:
# text = "hello"
# if text.isdigit():
#     result = int(text)
# else:
#     print("Not a valid number")

# Q10:
# a) Output: 53  (string concatenation "5"+"3" = "53")
# b) input() always returns str; + on strings concatenates
# c) a = int(input(...)); b = int(input(...))

# Q11:
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello", name + ", you are", age, "years old.")

# Q12:
# num = float(input("Enter a float number: "))
# print("Integer version:", int(num))
# print("Greater than 10:", num > 10)

# Q13: str — always, no matter what the user types

# Q14:
# bool(0)    → False
# bool(1)    → True
# bool(-5)   → True   (any non-zero = True)
# bool(0.0)  → False
# bool(3.14) → True
# bool("")   → False  (empty string = False)
# bool("hi") → True   (non-empty string = True)
# bool(None) → False

# Q15:
# True + True        → 2
# True+True+True     → 3
# False + False      → 0
# 10 + True          → 11
# 10 - False         → 10
# True * 5           → 5

# Q16: True, True, False, True

# Q17:
# c = complex(4, 7)  OR  c = 4 + 7j
# print(c)         # (4+7j)
# print(c.real)    # 4.0
# print(c.imag)    # 7.0
# print(type(c))   # <class 'complex'>

# Q18:
# a = 3 + 5j
# b = 2 + 4j
# print(a + b)    # (5+9j)

# Q19: j  (not i)

# Q21: b) help(str)

# BONUS 3 Prediction:
# 53          (string concat)
# 8           (int addition)
# 8.0         (float addition)
# True        (non-empty string)
# False       (int("5")-5 = 0 → bool(0) = False)
