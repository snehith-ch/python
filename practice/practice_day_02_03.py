# ============================================================
# PRACTICE — Day 2 & 3: Installation, Features, PyCharm
# ============================================================
# These are knowledge-check questions — answer as comments.
# A few small code tasks are included at the end.
# ============================================================


# --------------------------------------------------
# Q1. Match each feature of Python to its meaning.
#     Write the correct feature name next to each meaning.
#     Features: simple, free & open source, high level,
#               platform independent, portable, dynamically typed,
#               extensible, huge standard libraries
#
#     a) No license required, source code available to all  → ___________
#     b) No need to write code for memory management        → ___________
#     c) Runs on Windows, Linux, macOS without changes      → ___________
#     d) Data type assigned automatically at runtime        → ___________
#     e) Can use C/C++ code inside Python programs          → ___________
#     f) Syntax reads like English, less code needed        → ___________
#     g) Move programs between platforms, same result       → ___________
#     h) pandas, numpy, matplotlib available built-in       → ___________
# --------------------------------------------------

# YOUR ANSWERS:
# a)
# b)
# c)
# d)
# e)
# f)
# g)
# h)


# --------------------------------------------------
# Q2. Fill in the blanks about Python installation.
#
#     a) Official download site: _______________
#     b) Version used in this course: _______________
#     c) The critical checkbox during installation: _______________
#     d) Command to check installed version: _______________
#     e) IDLE stands for: _______________
# --------------------------------------------------

# YOUR ANSWERS:
# a)
# b)
# c)
# d)
# e)


# --------------------------------------------------
# Q3. List the 4 ways to write and run Python code
#     (in order from simplest to most powerful):
# --------------------------------------------------

# YOUR ANSWERS:
# 1)
# 2)
# 3)
# 4)


# --------------------------------------------------
# Q4. True or False — write T or F next to each:
#
#     a) You should install PyCharm before Python         ___
#     b) Community Edition of PyCharm is free             ___
#     c) print() is required in the IDLE interactive shell___
#     d) Both `python file.py` and `py file.py` work      ___
#     e) Every .py file is called a module in Python      ___
#     f) PyCharm shows errors only after you run the code ___
# --------------------------------------------------

# YOUR ANSWERS:
# a)  b)  c)  d)  e)  f)


# --------------------------------------------------
# Q5. CODE TASK: Run these lines in the interactive shell
#     OR write them here and run this file.
#     Observe what type Python assigns to each value.
# --------------------------------------------------

values = [42, 3.14, True, None, "hello", 2+3j]

for v in values:
    print(v, "-->", type(v))


# --------------------------------------------------
# Q6. CODE TASK: Verify your Python version from inside a script.
#     Run this and confirm it matches 3.10.x
# --------------------------------------------------

import sys
print("Python version:", sys.version)


# ============================================================
# SOLUTIONS
# ============================================================

# Q1:
# a) free & open source
# b) high level
# c) platform independent
# d) dynamically typed
# e) extensible
# f) simple
# g) portable
# h) huge standard libraries

# Q2:
# a) www.python.org
# b) Python 3.10.4
# c) "Add Python 3.10 to PATH"
# d) python --version  (in Command Prompt)
# e) Integrated Development Learning and Running (Environment)

# Q3:
# 1) Interactive mode (IDLE shell)
# 2) Script mode (Notepad + .py + Command Prompt)
# 3) Python IDLE file editor (File > New File)
# 4) PyCharm editor

# Q4:
# a) F  — install Python FIRST, then PyCharm
# b) T
# c) F  — print() is optional in interactive shell
# d) T
# e) T
# f) F  — PyCharm shows errors IN REAL TIME as you type

# Q5 Expected output:
# 42         --> <class 'int'>
# 3.14       --> <class 'float'>
# True       --> <class 'bool'>
# None       --> <class 'NoneType'>
# hello      --> <class 'str'>
# (2+3j)     --> <class 'complex'>
