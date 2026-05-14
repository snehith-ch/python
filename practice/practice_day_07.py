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
