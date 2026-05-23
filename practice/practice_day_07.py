# ============================================================
# PRACTICE — Day 7: Python Operators
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: ARITHMETIC OPERATORS
# --------------------------------------------------

# Q1. Predict the output of each:

a = 17
b = 5

# print(a + b)    # prediction:
# print(a - b)    # prediction:
# print(a * b)    # prediction:
# print(a ** b)   # prediction:   ← 17 to the power 5
# print(a / b)    # prediction:   ← always float!
# print(a // b)   # prediction:
# print(a % b)    # prediction:


# Q2. What type does `/` always return, even for whole-number results?

# print(type(10 / 2))   # prediction:
# print(10 / 2)         # prediction:   ← careful!


# Q3. Tricky — predict the output:

# print(7 // 2)     # prediction:
# print(-7 // 2)    # prediction:   ← tricky! floor division on negative
# print(7 % 2)      # prediction:
# print(-7 % 2)     # prediction:   ← tricky!


# Q4. Use `%` to check which numbers from 1-10 are even.
#     Write the code using a for loop:

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 2: RELATIONAL OPERATORS
# --------------------------------------------------

# Q5. Predict True or False for each:

x = 15

# print(x > 10)     # prediction:
# print(x == 15)    # prediction:
# print(x != 15)    # prediction:
# print(x < 5)      # prediction:
# print(x >= 15)    # prediction:
# print(x <= 14)    # prediction:


# Q6. What is the output?

score = 85
# print(score >= 90)    # prediction:
# print(score >= 80)    # prediction:
# print(score == 85.0)  # prediction:   ← int vs float comparison!


# --------------------------------------------------
# SECTION 3: ASSIGNMENT OPERATORS
# --------------------------------------------------

# Q7. Trace through and predict the final value of x:

x = 20
x += 5     # x = ?
x -= 3     # x = ?
x *= 2     # x = ?
x //= 4    # x = ?
x **= 2    # x = ?
print(x)

# Your step-by-step trace:
# After +=5:  x =
# After -=3:  x =
# After *=2:  x =
# After //=4: x =
# After **=2: x =
# Final print:


# --------------------------------------------------
# SECTION 4: LOGICAL OPERATORS
# --------------------------------------------------

# Q8. Predict True or False:

a = 10
b = 20
c = 5

# print(a > 5 and b > 15)    # prediction:
# print(a > 5 and b < 15)    # prediction:
# print(a > 15 or b > 15)    # prediction:
# print(a > 15 or b < 15)    # prediction:
# print(not(a > 5))          # prediction:
# print(not(a > 15))         # prediction:


# Q9. Write a single condition using `and` that checks:
#     - temperature > 20
#     - humidity < 80
#     - is_raining is False
#     Print "Good weather" if all three are true.

temperature = 25
humidity = 60
is_raining = False

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 5: MEMBERSHIP OPERATORS
# --------------------------------------------------

# Q10. Predict True or False:

fruits = ["apple", "banana", "cherry"]

# print("banana" in fruits)       # prediction:
# print("mango" in fruits)        # prediction:
# print("mango" not in fruits)    # prediction:
# print("grape" not in fruits)    # prediction:


# Q11. Membership on strings — predict:

name = "Snehith"
# print("neh" in name)      # prediction:
# print("xyz" in name)      # prediction:
# print("S" in name)        # prediction:
# print("s" in name)        # prediction:   ← case sensitive!


# --------------------------------------------------
# SECTION 6: IDENTITY OPERATORS
# --------------------------------------------------

# Q12. Predict True or False AND explain why:

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# print(a == b)    # prediction:    (why?)
# print(a is b)    # prediction:    (why?)
# print(a == c)    # prediction:    (why?)
# print(a is c)    # prediction:    (why?)


# Q13. Integer caching — predict:

x = 5
y = 5
p = 1000
q = 1000

# print(x is y)    # prediction:   (small integers are cached!)
# print(p is q)    # prediction:   (large integers are NOT cached!)
# print(x == y)    # prediction:
# print(p == q)    # prediction:


# Q14. Use id() to verify Q12 answers:

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))
print(id(b))
print(id(c))

# Which two IDs are the same?


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Using ONE line of print with operators:
# Given: price = 199, quantity = 3, discount = 20
# Print: Final price after 20% discount applied to total

price = 199
quantity = 3
discount = 20
# YOUR CODE (one line):


# BONUS 2:
# Use only the `%` and `//` operators to extract:
# - The hundreds digit of 9876  → expected: 8
# - The tens digit of 9876      → expected: 7
# - The units digit of 9876     → expected: 6

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

x, y = 7, 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
print(x > y and x < 10)
print(x > y or x > 10)
print(not(x == 7))
print("x" in "Python")
print(x is y)

# Your full prediction:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What does  10 // 3  return?
#    A) 3.33    B) 3    C) 1    D) 0
# Answer: ___

# Q_MCQ_2. What is the result of  2 ** 10?
#    A) 20    B) 200    C) 1024    D) 512
# Answer: ___

# Q_MCQ_3. x += 5  is equivalent to:
#    A) x = 5      B) x = x + 5    C) x == x + 5    D) x =+ 5
# Answer: ___

# Q_MCQ_4. What does  5 is 5  evaluate to (for small ints)?
#    A) False    B) True — same value      C) True — same object in memory
#    D) Error — 'is' only works on strings
# Answer: ___

# Q_MCQ_5. Which checks if 7 is in the list [1, 3, 5, 7, 9]?
#    A) 7 == [1,3,5,7,9]    B) 7 in [1,3,5,7,9]
#    C) 7.in([1,3,5,7,9])   D) contains(7, [1,3,5,7,9])
# Answer: ___

# Q_MCQ_6. What does  not (5 > 3)  return?
#    A) True    B) False    C) 5    D) 3
# Answer: ___

# Q_MCQ_7. What is  17 % 5?
#    A) 3    B) 2    C) 1    D) 4
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. The operator that gives the REMAINDER of division is _______.
#         15 % 4 = _______.

# FIB_2. The floor division operator is _______. 11 // 4 = _______.

# FIB_3. True and False = _______,   True or False = _______.

# FIB_4. "not in" checks if a value is _______ in a sequence.

# FIB_5. x **= 3  means x = x _______ 3.

# FIB_6. (3 + 4 * 2)  evaluates to _______ because _______ has
#         higher precedence than _______.

# FIB_7. x = 10; x //= 3  → x becomes _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Smart Calculator App — supports all operator types.
#
# Requirements:
#   1. Take two numbers (as input, convert to float) and an
#      operator (+, -, *, /, //, %, **) as input
#   2. Compute the result using if/elif based on operator
#   3. After computing, also show:
#      a) Is the result positive? (use > 0)
#      b) Is result an integer? (use % 1 == 0)
#      c) Is result in range 1–100? (use 'in range')
#      d) Is result None? (use 'is not None')
#   4. Handle ZeroDivisionError for / and //
#
# Expected output (example — inputs: 15, 4, %):
#   15.0 % 4.0 = 3.0
#   Positive      : True
#   Whole number  : True
#   In range 1-100: True
#   Is None       : False
#
# Hint: Use a dict {'+': lambda a,b: a+b, ...} for clean operator lookup.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: 22, 12, 85, 1419857, 3.4, 3, 2

# Q2: float — 10/2 = 5.0 not 5

# Q3:
# 7 // 2  = 3  (floor of 3.5)
# -7 // 2 = -4 (floor of -3.5 is -4, NOT -3)
# 7 % 2   = 1
# -7 % 2  = 1  (Python modulo is always non-negative)

# Q6: False, True, True  (85 == 85.0 is True — Python compares values)

# Q7:
# 25, 22, 44, 11, 121

# Q8: True, False, True, False, False, True

# Q11: True, False, True, False  (case-sensitive — "s" not in "Snehith")

# Q12:
# a==b: True  (same values)
# a is b: False  (different objects in memory)
# a==c: True
# a is c: True  (c points to same object as a)

# Q13: True (cached), False (not cached), True, True

# Q14: id(a) == id(c), id(b) is different


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: B   Q_MCQ_4: C
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: %  (modulo);  3
# FIB_2: //;  2
# FIB_3: False;  True
# FIB_4: NOT present
# FIB_5: **
# FIB_6: 11;  multiplication (*);  addition (+)
# FIB_7: 3

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# a  = float(input("Enter first number : "))
# b  = float(input("Enter second number: "))
# op = input("Operator (+,-,*,/,//,%,**): ")
# ops = {'+': lambda x,y: x+y, '-': lambda x,y: x-y,
#        '*': lambda x,y: x*y, '**': lambda x,y: x**y,
#        '%': lambda x,y: x%y}
# try:
#     if op in ('/', '//'):
#         if b == 0: raise ZeroDivisionError
#         result = a/b if op=='/' else a//b
#     elif op in ops:
#         result = ops[op](a, b)
#     else:
#         print("Unknown operator"); result = None
#     if result is not None:
#         print(f"{a} {op} {b} = {result}")
#         print(f"Positive      : {result > 0}")
#         print(f"Whole number  : {result % 1 == 0}")
#         print(f"In range 1-100: {1 <= result <= 100}")
#         print(f"Is None       : {result is None}")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

