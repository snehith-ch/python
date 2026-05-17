# ============================================================
# PRACTICE — Day 19: Modules
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================
#
# NOTE: Several questions require you to create a separate file.
# Before running those questions, create the files listed below.
#
# FILE 1 — save as 'sample.py' in the same folder:
# ---------------------------------------------------
#   name = "Snehith"
#   course = "Python"
#   marks = 90
#
#   def add(a, b):
#       return a + b
#
#   def greet(n):
#       print("Hello,", n)
#
#   def square(n):
#       return n * n
#
# FILE 2 — save as 'calc.py' in the same folder:
# ---------------------------------------------------
#   def add(a, b):      return a + b
#   def subtract(a, b): return a - b
#   def multiply(a, b): return a * b
#   def divide(a, b):
#       if b == 0: return "Cannot divide by zero"
#       return a / b
# ---------------------------------------------------


# --------------------------------------------------
# SECTION 1: import module
# --------------------------------------------------

# Q1. After creating sample.py above, predict the output:

import sample

print(sample.name)          # prediction:
print(sample.course)        # prediction:
print(sample.marks)         # prediction:
print(sample.add(10, 20))   # prediction:
sample.greet("Alice")       # prediction:


# Q2. Predict the error — what happens without the module prefix?

# print(name)    # uncomment to see error — prediction (what error?):
# print(add(1))  # uncomment — prediction:


# --------------------------------------------------
# SECTION 2: import module as alias
# --------------------------------------------------

# Q3. Predict the output — aliased import:

import sample as s

print(s.name)
print(s.square(7))     # prediction:
s.greet("Bob")         # prediction:


# Q4. Now try using the original name — predict the error:

# print(sample.name)   # prediction: works or error?
# Note: if you already have 'import sample' above, this works.
# But if ONLY 'import sample as s' was done, the name 'sample' is NOT available.


# --------------------------------------------------
# SECTION 3: from module import *
# --------------------------------------------------

# Q5. Predict the output — no prefix needed:

from sample import *

print(name)             # prediction:
print(course)           # prediction:
print(add(5, 5))        # prediction:
greet("Charlie")        # prediction:
print(square(9))        # prediction:


# --------------------------------------------------
# SECTION 4: from module import member
# --------------------------------------------------

# Q6. Predict the output — only 'add' imported:

from sample import add

print(add(100, 200))   # prediction:
# print(name)          # uncomment — prediction (error?):
# greet("X")           # uncomment — prediction (error?):


# Q7. Predict the output — member aliasing:

from sample import add as total, greet as hello

print(total(3, 7))    # prediction:
hello("Dave")         # prediction:

# Can you still use the original name?
# print(add(1, 2))    # prediction:


# --------------------------------------------------
# SECTION 5: NAME CONFLICT
# --------------------------------------------------

# Q8. Create these two files to test the name conflict:
#
# FILE: mod1.py
#   course = "Python"
#   def info(): print("From mod1")
#
# FILE: mod2.py
#   course = "Java"
#   def info(): print("From mod2")
#
# Then predict the output:

# from mod1 import *
# from mod2 import *
# print(course)    # prediction: "Python" or "Java"?
# info()          # prediction: mod1 or mod2?
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 6: __name__ VARIABLE
# --------------------------------------------------

# Q9. Add these lines to sample.py and predict what prints
#     when you run sample.py DIRECTLY vs when you import it:

# In sample.py, add at the bottom:
#   print("__name__ is:", __name__)
#
# Prediction when running sample.py directly:
# Prediction when importing sample from this file:


# Q10. The guard pattern — predict what runs:
#
# In calc.py, add at the bottom:
#   if __name__ == "__main__":
#       print("Running calc.py directly")
#       print(add(10, 20))
#
# Q10a. What prints when you run calc.py directly?
# YOUR ANSWER:
#
# Q10b. What prints when you do 'import calc' from here?
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 7: USING calc.py
# --------------------------------------------------

# Q11. Import calc and use all four operations — predict:

import calc

print(calc.add(50, 30))         # prediction:
print(calc.subtract(50, 30))    # prediction:
print(calc.multiply(6, 7))      # prediction:
print(calc.divide(100, 4))      # prediction:
print(calc.divide(10, 0))       # prediction:


# Q12. Import just divide from calc — predict:

from calc import divide

print(divide(9, 3))    # prediction:
# calc.add(1, 2)       # prediction (error or works?):


# Q13. help() — what does it display?

# help(sample)   # uncomment to see — describe what you observe:
# YOUR OBSERVATION:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Create a module 'geometry.py' with:
#   - PI = 3.14159
#   - circle_area(r): returns PI * r * r
#   - rect_area(l, w): returns l * w
#   - triangle_area(b, h): returns 0.5 * b * h
# Import it here using all 5 import styles, one at a time (comment out others).
# Call each function and print results.

# YOUR CODE HERE:


# BONUS 2:
# Demonstrate the name conflict problem:
# Create mod1.py and mod2.py each with a variable 'greeting'.
# Import both with 'from ... import *' and show which one wins.
# Then show how to avoid the conflict using the prefix-style import.

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running
# (assumes sample.py exists as described at the top):

import sample as m

results = [m.add(i, i*2) for i in range(1, 6)]
print(results)

squares = list(map(m.square, range(1, 6)))
print(squares)

print(m.name.upper())
print(m.course[:3])

# Your full prediction:


# BONUS 4:
# Create a module 'utils.py' that:
# - Has a constant MAX = 100
# - Has is_valid(n): returns True if 0 <= n <= MAX
# - Has clamp(n): returns MAX if n > MAX, 0 if n < 0, else n
# - Has a guard: if __name__ == "__main__": run a test of each function
# Import utils here. Test clamp(-5), clamp(50), clamp(150).
# Also run utils.py directly to see the guard fire.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "Snehith", "Python", 90, 30, "Hello, Alice"

# Q2: NameError — variables/functions need module prefix without 'from ... import *'

# Q3: "Snehith", 49, "Hello, Bob"

# Q5: "Snehith", "Python", 10, "Hello, Charlie", 81

# Q6: 300; name → NameError; greet → NameError

# Q7: 10; "Hello, Dave"; add → NameError (original name not available)

# Q8: "Java" (mod2 imported last, overwrites); "From mod2"

# Q9: When run directly → "__name__ is: __main__"
#     When imported → "__name__ is: sample"

# Q10a: prints "Running calc.py directly" and result of add(10,20)=30
# Q10b: prints nothing extra (guard not triggered on import)

# Q11: 80, 20, 42, 25.0, "Cannot divide by zero"

# Q12: 3.0; calc.add → NameError (only 'divide' was imported)

# BONUS 3:
# [3, 6, 9, 12, 15]
# [1, 4, 9, 16, 25]
# "SNEHITH"
# "Pyt"
