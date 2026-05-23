# ============================================================
# PRACTICE — Day 37: Packages
# ============================================================
# Instructions:
#   - These are conceptual and code-writing questions
#   - Some questions test understanding without running code
# ============================================================


# --------------------------------------------------
# SECTION 1: Package Hierarchy
# --------------------------------------------------

# Q1. Fill in the hierarchy from largest to smallest:

# Package → ________ → ________ → ________ → Variable

# YOUR ANSWER:


# Q2. What file makes a folder a Python package?

# a) __main__.py
# b) __init__.py
# c) setup.py
# d) package.py

# YOUR ANSWER:


# Q3. Fill in the blank:

# Without sys.path.append(), Python searches for modules in:
# a) The __________ directory only
# b) System-level Python library directories
# c) Only directories listed in ______________

# A package in a custom location needs:
# import sys
# sys.path.append("________________")

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 2: Import Styles
# --------------------------------------------------

# Q4. Match each import style to its advantage:

# a) import module1                    → _______________________________
# b) from module1 import *             → no need to use module name as prefix
# c) from module1 import display       → imports only one specific function
# d) import module1 as m1              → shorter alias

# YOUR ANSWERS:


# Q5. Predict — which import style avoids name conflicts?

# Suppose module1 has display() and module2 also has display().

# Style A (using import *):
# from module1 import *
# from module2 import *
# display()    → prediction: calls module1 or module2 version?

# Style B (using module names):
# import module1
# import module2
# module1.display()   → prediction:
# module2.display()   → prediction:

# Which style is safer? Why?

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 3: Code Tracing
# --------------------------------------------------

# Q6. Given this package structure:
#
# mypackage/
#   __init__.py
#   greetings.py    ← contains: def hello(): print("Hello!")
#
# Predict what each import style does:

# import sys
# sys.path.append("path/to/mypackage")

# Style 1:
# import greetings
# greetings.hello()    → prediction:

# Style 2:
# from greetings import hello
# hello()              → prediction:

# Style 3:
# from greetings import *
# hello()              → prediction:

# YOUR ANSWERS:


# Q7. Sub-package structure:
#
# company/
#   __init__.py
#   sales/
#     __init__.py
#     report.py    ← contains: def summary(): print("Sales summary")
#
# How would you import summary() from report.py?
# (Write the import statements)

# YOUR CODE:


# --------------------------------------------------
# SECTION 4: Practical Setup
# --------------------------------------------------

# Q8. Write the steps (in order) to set up and use a custom package:
# Assume: package folder = "D:/mypackages/utils/"
#         module name = "string_helpers.py"
#         function = "reverse_string()"

# Step 1:
# Step 2:
# Step 3:
# Step 4:
# Step 5:

# YOUR ANSWERS:


# Q9. True or False — predict:

# a) A folder without __init__.py can be imported as a package.  → ?
# b) sys.path.append() adds the path permanently.                → ?
# c) from module import * imports everything including __name__. → ?
# d) You can have a sub-package inside a package.               → ?
# e) Two packages can have modules with the same name.          → ?

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 5: Write Code
# --------------------------------------------------

# Q10. Write a simulated package scenario using a single file:
# Imagine math_utils.py has these functions:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

# Now import and use them as if they were a package:
from math_utils import add, subtract, multiply, divide

# Wait — math_utils is THIS file. Let's just call them directly:
print(add(10, 3))        # prediction:
print(subtract(10, 3))   # prediction:
print(multiply(10, 3))   # prediction:
print(divide(10, 3))     # prediction (approximate):
print(divide(10, 0))     # prediction:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Answer these conceptual questions:
# a) Why is __init__.py needed in a package folder?
# b) What does sys.path contain by default?
# c) If two modules in different packages both have a class named "Utils",
#    how do you use both without conflict?

# YOUR ANSWERS:


# BONUS 2: Package hierarchy exercise:
# Map this real-world scenario to Python packages:
# Company → Department → Team → Employee → employee_id

# What would be:
# Package name:     ?
# Sub-package name: ?
# Module name:      ?
# Class name:       ?
# Attribute name:   ?

# YOUR ANSWERS:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What file makes a directory a Python package?
#    A) main.py    B) __init__.py    C) setup.py    D) package.py
# Answer: ___

# Q_MCQ_2. from math import sqrt  — which import style is this?
#    A) import module    B) import module as alias
#    C) from module import name    D) from module import *
# Answer: ___

# Q_MCQ_3. import numpy as np  — what does  as np  do?
#    A) Renames the module permanently
#    B) Creates a local alias for the module in this script
#    C) Installs numpy with alias np
#    D) Imports only np from numpy
# Answer: ___

# Q_MCQ_4. from os.path import join, exists  imports:
#    A) The entire os module    B) join and exists functions specifically
#    C) os and path separately    D) Everything from os
# Answer: ___

# Q_MCQ_5. A package can contain:
#    A) Only .py files    B) Only __init__.py
#    C) Sub-packages and modules    D) Only one module
# Answer: ___

# Q_MCQ_6. What is the role of  __init__.py  in a package?
#    A) Runs tests automatically
#    B) Marks the directory as a package; can expose public API
#    C) Installs the package
#    D) Required only for third-party packages
# Answer: ___

# Q_MCQ_7. Which import style should be AVOIDED in production code?
#    A) import math    B) from math import sqrt
#    C) from math import *    D) import math as m
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. A Python package is a directory containing a special file named
#         _______.

# FIB_2. import pandas as pd  — pd is called a module _______.

# FIB_3. from mypackage.utils import helper  imports  helper  from the
#         _______ module inside mypackage.

# FIB_4. from os import *  imports _______ names from the os module
#         (this style pollutes the _______ namespace).

# FIB_5. The  sys.path  list tells Python where to _______ modules.

# FIB_6. pip install requests  installs a _______ package into site-packages.

# FIB_7. Relative import syntax (inside a package): from ._______  import func


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Build a Calculator Package with sub-modules.
#
# Requirements:
#   1. Create a package folder: mymath/
#      - mymath/__init__.py  (expose: add, sub, mul, div, circle_area)
#      - mymath/basic.py     (add, sub, mul, div functions)
#      - mymath/geometry.py  (circle_area, rect_area functions)
#   2. In a main script, import using 3 styles:
#      - import mymath
#      - from mymath import circle_area
#      - from mymath.basic import mul
#   3. Use each import style to compute something and print results
#   4. Print the package's __doc__ (docstring from __init__.py)
#
# Expected output:
#   mymath package: Math utilities — basic and geometry
#   add(10, 5) = 15        (via import mymath)
#   circle_area(7) = 153.94  (via from mymath import)
#   mul(4, 6) = 24          (via from mymath.basic import)
#
# Hint: Set __doc__ in __init__.py as a module docstring.
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: Package → Module → Class → Method → Variable

# Q2: b) __init__.py

# Q3: Current directory; sys.path; the actual folder path to the package

# Q4: a) module name required as prefix
#     b) no prefix needed (but name conflicts possible)
#     c) only that function imported (precise)
#     d) shorter name for long module names

# Q5: Style A → calls module2's display() (last import wins)
#     Style B → module1.display() or module2.display() — both work, no conflict
#     Style B is safer (avoids name conflict)

# Q6: All 3 styles call hello() → "Hello!" printed

# Q9: a) False (in Python 3 it works as namespace package, but __init__.py is best practice)
#     b) False (only for current session)
#     c) False (__name__ is not imported with *)
#     d) True
#     e) True (module names are per-package)

# Q10: 13, 7, 30, 3.333..., None

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: C

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: __init__.py
# FIB_2: alias
# FIB_3: utils
# FIB_4: all public; global
# FIB_5: search / look up
# FIB_6: third-party
# FIB_7: . (current package) — e.g. from .utils import helper

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# # mymath/__init__.py
# "Math utilities -- basic and geometry"
# from .basic import add, sub, mul, div
# from .geometry import circle_area, rect_area
#
# # mymath/basic.py
# def add(a, b): return a + b
# def sub(a, b): return a - b
# def mul(a, b): return a * b
# def div(a, b): return a / b if b != 0 else None
#
# # mymath/geometry.py
# import math
# def circle_area(r): return round(math.pi * r * r, 2)
# def rect_area(l, w): return l * w
#
# # main.py (run from directory containing mymath/)
# import mymath
# from mymath import circle_area
# from mymath.basic import mul
#
# print(f"mymath package: {mymath.__doc__}")
# print(f"add(10, 5)      = {mymath.add(10, 5)}")
# print(f"circle_area(7)  = {circle_area(7)}")
# print(f"mul(4, 6)       = {mul(4, 6)}")

