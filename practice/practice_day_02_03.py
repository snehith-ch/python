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




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Running the same .py file on Windows, Linux, macOS
#           without changes describes Python as:
#    A) Portable          B) Platform Independent
#    C) Extensible        D) High Level
# Answer: ___

# Q_MCQ_2. "Python can use C/C++ code inside it" → which feature?
#    A) Free & Open Source  B) Simple
#    C) Extensible          D) Dynamically Typed
# Answer: ___

# Q_MCQ_3. The critical checkbox during Python installation:
#    A) "Install for all users"    B) "Add Python to PATH"
#    C) "Install IDLE"             D) "Install pip only"
# Answer: ___

# Q_MCQ_4. IDLE stands for:
#    A) Integrated Development and Learning Environment
#    B) Interactive Dynamic Language Editor
#    C) Interpreted Data Layout Engine
#    D) Inline Debugger for Lazy Execution
# Answer: ___

# Q_MCQ_5. Which PyCharm edition is completely free?
#    A) Professional   B) Enterprise   C) Community   D) Academic
# Answer: ___

# Q_MCQ_6. In the IDLE interactive shell, do you need print()?
#    A) Yes, always
#    B) No — the shell auto-displays expression results
#    C) Only for strings
#    D) Only when running a script file
# Answer: ___

# Q_MCQ_7. "Data type assigned automatically at runtime" → which feature?
#    A) High Level        B) Simple
#    C) Extensible        D) Dynamically Typed
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. "No license required, source code freely available" →
#         Python is ___________________.

# FIB_2. "No need to manually manage memory" →
#         Python is a _____________ level language.

# FIB_3. Command to verify Python is installed: _____________.

# FIB_4. pandas, numpy, matplotlib are examples of Python's
#         _________________ standard libraries.

# FIB_5. Moving the same program to a different OS and getting
#         the same result = the _____________ feature.

# FIB_6. Simple syntax that reads like English = the _____________ feature.

# FIB_7. Every .py file is also called a _____________ in Python.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Write a single program that DEMONSTRATES all 4 key
# Python features through running code.
#
# Requirements:
#   1. Dynamic Typing — reassign x through int → float → str, print type()
#   2. Huge Standard Library — import math, print math.pi and math.sqrt(144)
#   3. Simple/Readable — clean if/else with a temperature check
#   4. Interactive — input() to ask user's name and greet them
#   Print a clear "--- Feature Name ---" header before each demo.
#
# Expected output (example):
#   --- Dynamic Typing ---
#   x = 42 → <class 'int'>   x = "hi" → <class 'str'>
#   --- Standard Library ---
#   pi = 3.141592653589793    sqrt(144) = 12.0
#   --- Simple Syntax ---
#   38°C: You have a fever!
#   --- Interactive ---
#   Hello, Snehith! Python is awesome.
#
# Hint: Each feature is shown by running actual code, not just printing text.

# YOUR CODE HERE:


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


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: B   Q_MCQ_4: A
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: D

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: Free & Open Source
# FIB_2: high
# FIB_3: python --version
# FIB_4: huge / large
# FIB_5: Portable
# FIB_6: Simple
# FIB_7: module

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import math
# print("--- Dynamic Typing ---")
# x = 42;       print(f"x = 42 → {type(x)}", end="   ")
# x = "hi";     print(f'x = "hi" → {type(x)}')
# print("--- Standard Library ---")
# print(f"pi = {math.pi}    sqrt(144) = {math.sqrt(144)}")
# print("--- Simple Syntax ---")
# temp = 38
# print(f"{temp}°C: {'You have a fever!' if temp > 37 else 'Normal.'}")
# print("--- Interactive ---")
# name = input("Your name: ")
# print(f"Hello, {name}! Python is awesome.")

