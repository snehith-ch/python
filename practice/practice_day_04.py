# ============================================================
# PRACTICE — Day 4: Comments, Keywords, Indentation,
#                   Identifiers, Variables, Multiple Assignment
# ============================================================
# Instructions:
#   - Fix the bugs, fill in the blanks, and write small programs
#   - Try each task before looking at the SOLUTIONS section
# ============================================================


# --------------------------------------------------
# SECTION 1: COMMENTS
# --------------------------------------------------

# Q1. Add a single-line comment above the print statement
#     describing what it does.

print("Total students:", 45)


# Q2. The developer wants to temporarily disable the second
#     and third print lines without deleting them.
#     Use comments to exclude them.

print("Server started")
print("Loading database...")     # disable this line
print("Connecting to API...")    # disable this line
print("App is ready")


# Q3. Add a multi-line comment at the top of this mini-program
#     that says:
#       Program: Grade Calculator
#       Author: Your Name
#       Purpose: Calculate average of 3 marks

marks1 = 80
marks2 = 75
marks3 = 90
average = (marks1 + marks2 + marks3) / 3
print("Average:", average)


# --------------------------------------------------
# SECTION 2: KEYWORDS
# --------------------------------------------------

# Q4. Run this code to print all Python keywords.
#     Count how many there are and write the count as a comment.

import keyword
print(keyword.kwlist)
print("Total:", len(keyword.kwlist))
# Number of keywords in Python 3.10: ___


# Q5. SPOT THE BUG — each line below has an error because
#     a keyword is used as a variable name.
#     Fix each one by renaming the variable.

# for = 10
# print(for)

# class = "Python"
# print(class)

# if = True
# print(if)

# YOUR FIXED CODE HERE:


# Q6. Which of these are VALID identifiers?
#     Write VALID or INVALID and the reason.

# a) myVariable       → ___________
# b) 2ndValue         → ___________
# c) _secret          → ___________
# d) my variable      → ___________
# e) while            → ___________
# f) total_marks99    → ___________
# g) True             → ___________
# h) empID            → ___________


# --------------------------------------------------
# SECTION 3: INDENTATION
# --------------------------------------------------

# Q7. FIX THE INDENTATION ERROR in this code:

temperature = 38
if temperature > 37:
print("You have a fever!")    # fix this line
print("Please rest.")          # fix this line


# Q8. What is the output of this code?
#     Predict BEFORE running it, then verify.

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
else:
    print("Grade: C")
print("Evaluation complete")   # which block does this belong to?

# Your prediction:
# Actual output after running:


# Q9. Rewrite this Java-style block in proper Python syntax:
#
#   int x = 10;
#   if (x > 5) {
#       System.out.println("Greater");
#   } else {
#       System.out.println("Smaller or equal");
#   }

# YOUR PYTHON CODE HERE:


# --------------------------------------------------
# SECTION 4: IDENTIFIERS — Rules Practice
# --------------------------------------------------

# Q10. Fix all identifier errors in this code block:

# 1name = "Rahul"          # error 1
# emp salary = 50000       # error 2
# for = "Python"           # error 3

# YOUR FIXED VERSIONS:
# name1 = "Rahul"
# (write fix for error 2 and 3)


# Q11. What naming convention should you use for a variable
#      that should act as a constant (e.g., maximum login attempts)?
#      Write the variable declaration as a comment:

# YOUR ANSWER:


# --------------------------------------------------
# SECTION 5: VARIABLES & MULTIPLE ASSIGNMENT
# --------------------------------------------------

# Q12. Declare 3 variables and print each with its type:
#      - student_name holds "Arjun"
#      - student_age holds 22
#      - student_gpa holds 8.75

# YOUR CODE HERE:


# Q13. Assign the value 0 to five variables (a, b, c, d, e)
#      using a SINGLE line of code (one-value to many).

# YOUR CODE HERE:


# Q14. Assign values 10, 20, 30, 40, 50 to variables
#      p, q, r, s, t using a SINGLE line of code.
#      Then print all 5 on one line separated by " - "

# YOUR CODE HERE:


# Q15. SWAP the values of x and y WITHOUT using a third variable.
#      (This is a classic Python trick using multiple assignment.)

x = 100
y = 200
print("Before swap: x =", x, "y =", y)

# YOUR SWAP CODE HERE (one line):

print("After swap: x =", x, "y =", y)
# Expected:
# Before swap: x = 100  y = 200
# After swap:  x = 200  y = 100


# Q16. What does this output? Predict then run.

a, b = 5, 10
a, b = b, a + b
print(a, b)

# Your prediction:
# Actual:


# --------------------------------------------------
# BONUS CHALLENGE
# --------------------------------------------------

# Q17. Write a program that:
#      - Declares 3 subject marks as variables (any values you choose)
#      - Uses multiple assignment to set all 3 marks to 0 first
#      - Then assigns proper values: physics=88, chemistry=92, maths=95
#      - Prints all three and their total
#      - Uses a meaningful comment at the top

# YOUR CODE HERE:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Which symbol creates a single-line comment in Python?
#    A) //    B) /*    C) #    D) --
# Answer: ___

# Q_MCQ_2. Which of these is a VALID Python identifier?
#    A) 2ndValue    B) my variable    C) _secret    D) while
# Answer: ___

# Q_MCQ_3. What is the correct way to assign 0 to variables a, b, c
#           all in ONE line?
#    A) a, b, c = 0        B) a = b = c = 0
#    C) a=0 b=0 c=0        D) assign a,b,c to 0
# Answer: ___

# Q_MCQ_4. Naming convention for a CONSTANT in Python:
#    A) camelCase           B) PascalCase
#    C) ALL_CAPS_WITH_UNDERSCORE    D) snake_case
# Answer: ___

# Q_MCQ_5. What does  a, b = b, a  do?
#    A) Creates two new variables     B) Swaps the values of a and b
#    C) Adds a and b                  D) Deletes both variables
# Answer: ___

# Q_MCQ_6. Which of these CANNOT be used as a variable name?
#    A) my_var    B) _data    C) class    D) total99
# Answer: ___

# Q_MCQ_7. A multi-line comment (docstring) in Python uses:
#    A) /* ... */    B) // ... //    C) ''' ... '''    D) ## ... ##
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. To disable a line of code without deleting it, use _______ before it.

# FIB_2. Python has _______ reserved keywords (in Python 3.10).

# FIB_3. Identifiers CANNOT start with a _______ or contain _______.

# FIB_4. p, q, r = 10, 20, 30  is called _______ assignment.

# FIB_5. x, y = y, x  swaps values using Python's _______ assignment trick.

# FIB_6. class_name = "Python"  fixes the bug where _______ was used
#         as a variable name (which is a keyword).

# FIB_7. A variable that should not change by convention is written
#         in _______ case, e.g. MAX_RETRIES = 3.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Set up a student report card system using proper Python
#           conventions for variables, comments, and assignment.
#
# Requirements:
#   1. Add a multi-line comment (triple-quote) at the top:
#      Program: Student Report Card,  Author: your name,  Purpose: ...
#   2. Use chained assignment to initialize 5 subject marks to 0
#      (english = maths = science = history = art = 0)
#   3. Use multiple assignment to set real values in ONE line:
#      english=85, maths=92, science=78, history=88, art=95
#   4. Use a CONSTANT for the pass mark: PASS_MARK = 50
#   5. Print each subject and mark. Check each against PASS_MARK.
#   6. Print total and average. Swap the highest and lowest marks
#      using the one-line swap trick and print before/after.
#
# Expected output:
#   English  : 85 ✓ Pass
#   Maths    : 92 ✓ Pass
#   Science  : 78 ✓ Pass
#   History  : 88 ✓ Pass
#   Art      : 95 ✓ Pass
#   Total: 438   Average: 87.6
#   Before swap — highest: 95, lowest: 78
#   After swap  — highest: 78, lowest: 95
#
# Hint: Use f-strings with :<8 to align subject names.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1:
# # Prints the total number of students
# print("Total students:", 45)

# Q2:
# print("Server started")
# # print("Loading database...")
# # print("Connecting to API...")
# print("App is ready")

# Q3:
# '''
# Program: Grade Calculator
# Author: Your Name
# Purpose: Calculate average of 3 marks
# '''

# Q4: 35 keywords

# Q5:
# loop_var = 10
# print(loop_var)
# class_name = "Python"
# print(class_name)
# condition = True
# print(condition)

# Q6:
# a) VALID
# b) INVALID — starts with a digit
# c) VALID — underscore prefix is allowed (means private)
# d) INVALID — space not allowed; use my_variable
# e) INVALID — 'while' is a keyword
# f) VALID
# g) INVALID — 'True' is a keyword (bool constant)
# h) VALID

# Q7:
# temperature = 38
# if temperature > 37:
#     print("You have a fever!")
#     print("Please rest.")

# Q8 Output:
# Grade: B
# Evaluation complete
# ('Evaluation complete' is outside the if/elif/else — always runs)

# Q9:
# x = 10
# if x > 5:
#     print("Greater")
# else:
#     print("Smaller or equal")

# Q10:
# name1 = "Rahul"
# emp_salary = 50000
# language = "Python"

# Q11:
# MAX_LOGIN_ATTEMPTS = 3

# Q12:
# student_name = "Arjun"
# student_age = 22
# student_gpa = 8.75
# print(student_name, type(student_name))
# print(student_age, type(student_age))
# print(student_gpa, type(student_gpa))

# Q13:
# a = b = c = d = e = 0

# Q14:
# p, q, r, s, t = 10, 20, 30, 40, 50
# print(p, q, r, s, t, sep=" - ")

# Q15:
# x, y = y, x

# Q16:
# a = 10, b = 15
# (a gets old b=10, b gets a+b = 5+10 = 15)

# Q17:
# # Subject marks calculator
# physics = chemistry = maths = 0       # initialize all to 0
# physics, chemistry, maths = 88, 92, 95
# total = physics + chemistry + maths
# print("Physics:", physics)
# print("Chemistry:", chemistry)
# print("Maths:", maths)
# print("Total:", total)


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: C   Q_MCQ_2: C   Q_MCQ_3: B   Q_MCQ_4: C
# Q_MCQ_5: B   Q_MCQ_6: C   Q_MCQ_7: C

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: #  (hash/pound sign)
# FIB_2: 35
# FIB_3: digit (number);  spaces or special characters
# FIB_4: multiple (tuple unpacking)
# FIB_5: multiple / tuple unpacking
# FIB_6: class  (a reserved keyword)
# FIB_7: UPPER (ALL_CAPS)

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# '''
# Program: Student Report Card
# Author: Snehith
# Purpose: Track and display marks for 5 subjects
# '''
# PASS_MARK = 50
# english = maths = science = history = art = 0          # chained assignment
# english, maths, science, history, art = 85, 92, 78, 88, 95   # multiple assignment
# subjects = [("English", english), ("Maths", maths), ("Science", science),
#             ("History", history), ("Art", art)]
# for name, mark in subjects:
#     status = "✓ Pass" if mark >= PASS_MARK else "✗ Fail"
#     print(f"{name:<8}: {mark} {status}")
# total = english + maths + science + history + art
# print(f"Total: {total}   Average: {total/5:.1f}")
# highest, lowest = 95, 78
# print(f"Before swap — highest: {highest}, lowest: {lowest}")
# highest, lowest = lowest, highest
# print(f"After swap  — highest: {highest}, lowest: {lowest}")

