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
