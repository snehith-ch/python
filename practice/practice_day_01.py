# ============================================================
# PRACTICE — Day 1: Introduction to Python
# ============================================================
# Instructions:
#   1. Read each question carefully
#   2. Write your answer in the space provided
#   3. Check the SOLUTIONS section at the bottom
# ============================================================


# --------------------------------------------------
# Q1. Print your name and the message "is learning Python"
#     Expected output:  Snehith is learning Python
# --------------------------------------------------

# YOUR CODE HERE:


# --------------------------------------------------
# Q2. Print the following 3 lines using 3 separate print statements:
#     Line 1: Python is a general purpose language
#     Line 2: Python is interpreted
#     Line 3: Python is dynamically typed
# --------------------------------------------------

# YOUR CODE HERE:


# --------------------------------------------------
# Q3. A variable 'x' is declared below.
#     Without changing the value, just print the DATA TYPE of x.
#     Then reassign x to 3.14 and print its type again.
#     Then reassign x to "Python" and print its type again.
#     (This demonstrates dynamic typing)

x = 100

# YOUR CODE HERE:


# --------------------------------------------------
# Q4. Python is case sensitive. Predict what happens when
#     you run the code below, then uncomment it and verify.
#
#     language = "Python"
#     print(Language)
# --------------------------------------------------

# UNCOMMENT TO TEST:
# language = "Python"
# print(Language)


# --------------------------------------------------
# Q5. Fill in the blanks (answer as a comment):
#
#     a) Python was created by: _______________
#     b) First version released in year: _______________
#     c) Python was named after: _______________
#     d) Current version used in this course: _______________
#     e) Official website: _______________
# --------------------------------------------------

# YOUR ANSWERS:
# a)
# b)
# c)
# d)
# e)




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------
# Write the letter of the correct answer.

# Q_MCQ_1. Python was created by:
#    A) Linus Torvalds     B) Guido van Rossum
#    C) Dennis Ritchie     D) James Gosling
# Answer: ___

# Q_MCQ_2. Python is "interpreted". This means:
#    A) Compiled to machine code before running
#    B) Executed line-by-line at runtime without a pre-compile step
#    C) Requires a virtual machine like Java
#    D) Converted to C before execution
# Answer: ___

# Q_MCQ_3. What does  type(True + 1)  return?
#    A) <class 'bool'>    B) <class 'str'>
#    C) <class 'int'>     D) <class 'float'>
# Answer: ___

# Q_MCQ_4. Python was named after:
#    A) The Python snake              B) A Greek god
#    C) Monty Python's Flying Circus  D) A Unix utility
# Answer: ___

# Q_MCQ_5. Which demonstrates dynamic typing?
#    A) int x = 10        B) x = 10; x = "hello"
#    C) var x = 10        D) declare x as int
# Answer: ___

# Q_MCQ_6. What happens when you run  print(Language)  if only
#           language = "Python"  exists?
#    A) Prints "Python"   B) Prints None
#    C) NameError         D) Prints "language"
# Answer: ___

# Q_MCQ_7. In which year was Python first released?
#    A) 1985   B) 1989   C) 1991   D) 1995
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. Python was created by _______________ in the year _______.

# FIB_2. The built-in function used to display output is _______().

# FIB_3. Python is case-sensitive, so `score` and `Score` are
#         treated as _____________ variables.

# FIB_4. type(True)  returns _____________ because bool is a
#         subclass of _____________.

# FIB_5. Python was named after _________________________________,
#         NOT the reptile.

# FIB_6. In Python, the data type of a variable is determined at
#         _____________, not declared ahead of time.

# FIB_7. The official Python website is _____________.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Build a welcome screen for a Python learning app.
#
# Requirements:
#   1. Print a decorative border using * (40+ characters wide)
#   2. Inside the border: student name, age, city, favourite language
#   3. Print one Python fun fact below the border
#   4. Demonstrate dynamic typing: assign x = 100, print type,
#      reassign x = 3.14, print type, reassign x = "Python", print type
#
# Expected output (example):
#   ==========================================
#   *   Student Profile Card                 *
#   *   Name    : Snehith                    *
#   *   Age     : 20                         *
#   *   City    : Hyderabad                  *
#   *   Language: Python                     *
#   ==========================================
#   Fun fact: Python was named after Monty Python, not the snake!
#   Python created by Guido van Rossum — released in 1991.
#   --- Dynamic Typing Demo ---
#   x = 100      → <class 'int'>
#   x = 3.14     → <class 'float'>
#   x = "Python" → <class 'str'>
#
# Hint: Use f-strings and :<width> for aligned columns.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS — uncover only after attempting!
# ============================================================

# Q1 Solution:
# print("Snehith is learning Python")

# Q2 Solution:
# print("Python is a general purpose language")
# print("Python is interpreted")
# print("Python is dynamically typed")

# Q3 Solution:
# x = 100
# print(type(x))      # <class 'int'>
# x = 3.14
# print(type(x))      # <class 'float'>
# x = "Python"
# print(type(x))      # <class 'str'>

# Q4 Solution:
# NameError: name 'Language' is not defined
# Python is case sensitive — 'language' and 'Language' are different

# Q5 Answers:
# a) Guido van Rossum
# b) 1991
# c) Monty Python's Flying Circus (BBC TV show)
# d) Python 3.10.4
# e) www.python.org


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: C   Q_MCQ_4: C
# Q_MCQ_5: B   Q_MCQ_6: C   Q_MCQ_7: C

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: Guido van Rossum, 1991
# FIB_2: print
# FIB_3: different (two separate names)
# FIB_4: <class 'bool'>,  int
# FIB_5: Monty Python's Flying Circus (BBC TV show)
# FIB_6: runtime
# FIB_7: www.python.org

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# name = "Snehith"
# age, city = 20, "Hyderabad"
# border = "=" * 42
# print(border)
# print(f"*   {'Student Profile Card':<38}*")
# print(f"*   {'Name    : ' + name:<38}*")
# print(f"*   {'Age     : ' + str(age):<38}*")
# print(f"*   {'City    : ' + city:<38}*")
# print(f"*   {'Language: Python':<38}*")
# print(border)
# print("Fun fact: Python was named after Monty Python, not the snake!")
# print("Python created by Guido van Rossum — released in 1991.")
# print("--- Dynamic Typing Demo ---")
# x = 100;   print(f"x = 100      → {type(x)}")
# x = 3.14;  print(f"x = 3.14     → {type(x)}")
# x = "Python"; print(f'x = "Python" → {type(x)}')

