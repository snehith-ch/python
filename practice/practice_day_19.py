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




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What does  import math as m  allow you to do?
#    A) Use math functions without any prefix
#    B) Use math functions with the shorter prefix m.
#    C) Import only the math.m submodule
#    D) Create a copy of the math module named m
# Answer: ___

# Q_MCQ_2. When you run a .py file directly, what is __name__?
#    A) The filename    B) "__main__"    C) "__file__"    D) None
# Answer: ___

# Q_MCQ_3. What does  from math import *  do?
#    A) Imports only math.sqrt
#    B) Imports all public names from math into current namespace
#    C) Imports math as a wildcard module
#    D) Imports math and aliases it as *
# Answer: ___

# Q_MCQ_4. If two modules both define a function called  connect(),
#           and you do  from db import *; from api import *  — which is used?
#    A) db.connect()    B) api.connect() — the last import wins
#    C) Both are available    D) Error — name conflict
# Answer: ___

# Q_MCQ_5. Modules are cached after first import. If you import the same
#           module twice, Python:
#    A) Executes the module code twice
#    B) Uses the cached version — executes only once
#    C) Raises ImportError the second time
#    D) Creates two separate module objects
# Answer: ___

# Q_MCQ_6. if __name__ == "__main__":  is used to:
#    A) Check if the file has a main() function
#    B) Run code only when the file is executed directly, not when imported
#    C) Define the main class
#    D) Start the Python interpreter
# Answer: ___

# Q_MCQ_7. What does  import os; os.getcwd()  return?
#    A) List of all files    B) Current working directory as a string
#    C) Path to Python       D) Username
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. import math as _______ is the common convention for the math module.

# FIB_2. from os import _______ to get the current working directory function.

# FIB_3. __name__ equals "_______ " when a file is run directly.

# FIB_4. from math import pi, sqrt  makes pi and sqrt available
#         _______ the math. prefix.

# FIB_5. A _______ import conflict occurs when two modules define the same name.

# FIB_6. import sys; sys.path  contains the list of directories Python searches
#         for _______.

# FIB_7. Every .py file is called a _______ in Python.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Data Science Toolkit Demo — use 4 modules with different
# import styles to show you understand each style's implications.
#
# Requirements:
#   1. import math  → use math.pi, math.sqrt(144), math.ceil(4.2), math.floor(4.8)
#   2. import random as rnd  → rnd.seed(42), pick 5 numbers between 1-100,
#      shuffle a list, choose one item
#   3. from os import getcwd, listdir, path  → print cwd, check if
#      "practice_day_19.py" exists in current dir
#   4. from datetime import date, datetime  → print today's date,
#      days until next New Year (Jan 1), format as "DD-Mon-YYYY"
#   5. Print a clear header before each section
#   6. At the BOTTOM: add  if __name__ == "__main__":  guard around
#      all the demo code
#
# Expected output (example):
#   === math module (import math) ===
#   pi = 3.14159...   sqrt(144) = 12.0   ceil(4.2) = 5   floor(4.8) = 4
#   === random module (import random as rnd) ===
#   5 random numbers: [15, 72, 3, 94, 48]
#   === os module (from os import ...) ===
#   CWD: /home/snehith/python/practice
#   File exists: True
#   === datetime module (from datetime import ...) ===
#   Today: 2024-01-15   Days to NY: 351   Formatted: 15-Jan-2024

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


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: m  (or any alias you prefer)
# FIB_2: getcwd
# FIB_3: __main__
# FIB_4: without
# FIB_5: name / namespace
# FIB_6: modules
# FIB_7: module

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import math
# import random as rnd
# from os import getcwd, listdir, path
# from datetime import date, datetime
#
# if __name__ == "__main__":
#     print("=== math module ===")
#     print(f"pi={math.pi:.5f}  sqrt(144)={math.sqrt(144)}  ceil(4.2)={math.ceil(4.2)}  floor(4.8)={math.floor(4.8)}")
#     print("=== random module ===")
#     rnd.seed(42)
#     nums = [rnd.randint(1,100) for _ in range(5)]
#     items = ["apple","banana","cherry","date"]
#     rnd.shuffle(items)
#     print(f"5 random numbers: {nums}  |  shuffled: {items}  |  choice: {rnd.choice(items)}")
#     print("=== os module ===")
#     print(f"CWD: {getcwd()}")
#     print(f"File exists: {path.exists('practice_day_19.py')}")
#     print("=== datetime module ===")
#     today = date.today()
#     ny    = date(today.year+1, 1, 1)
#     days  = (ny - today).days
#     print(f"Today: {today}   Days to NY: {days}   Formatted: {today.strftime('%d-%b-%Y')}")

