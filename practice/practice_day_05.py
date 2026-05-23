# ============================================================
# PRACTICE — Day 5: Data Types, Type Casting, input(), bool, complex
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: None TYPE
# --------------------------------------------------

# Q1. What is the output of each print?
#     Predict first, then uncomment and run.

result = None
# print(result)
# print(type(result))

# Prediction:
# Line 1 output:
# Line 2 output:


# Q2. Fix the bug — the developer used 'null' instead of Python's keyword:

# score = null
# print(score)

# YOUR FIX HERE:


# Q3. A variable 'connection' starts as None, then gets a value.
#     Write code to:
#     - Declare connection = None and print its type
#     - Reassign connection = "database_connected" and print its type

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 2: int AND float
# --------------------------------------------------

# Q4. Predict the output of each type() call:

a = 100
b = -50
c = 0
d = 3.14
e = -0.001
f = 100.0

# print(type(a))   # prediction:
# print(type(b))   # prediction:
# print(type(c))   # prediction:
# print(type(d))   # prediction:
# print(type(e))   # prediction:
# print(type(f))   # prediction:  ← careful! 100.0 not 100


# Q5. IMPORTANT: What does int() do to a float?
#     Predict the output of each line:

# print(int(9.9))    # prediction:
# print(int(9.1))    # prediction:
# print(int(-9.9))   # prediction:  ← tricky!
# print(int(0.99))   # prediction:

# KEY QUESTION: Does int() round or truncate?
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 3: TYPE CASTING
# --------------------------------------------------

# Q6. Fill in the blank — which conversion function to use?

price = "499"
# To add 100 to price, I need to convert it using: ___________
# Write the working code:


# Q7. Chain of conversions — predict the final value and type:

x = "12.75"
y = float(x)
z = int(y)
# print(z, type(z))
# Prediction: value = ___, type = ___


# Q8. FIX THE BUG — this crashes with ValueError:
#
# result = int("hello")
# print(result)
#
# WHY does it crash?
# HOW would you safely convert only if the string is a number?
# (Hint: use a condition or try/except — just write the logic in comments for now)

# YOUR EXPLANATION:


# Q9. Convert in both directions and verify:

num = 42
as_float = float(num)
as_str   = str(num)
as_bool  = bool(num)

print(as_float, type(as_float))
print(as_str,   type(as_str))
print(as_bool,  type(as_bool))


# --------------------------------------------------
# SECTION 4: input() — THE STRING TRAP
# --------------------------------------------------

# Q10. THE CLASSIC BUG — read this code and answer the questions
#      WITHOUT running it first:
#
# a = input("Enter a number: ")
# b = input("Enter another: ")
# print(a + b)
#
# Q10a. If the user types 5 and 3, what is the output?  ___________
# Q10b. Why?  ___________
# Q10c. How do you fix it?  ___________


# Q11. Write a program that:
#      - Asks the user for their name (string — no casting needed)
#      - Asks for their age (needs casting to int)
#      - Prints:  Hello [name], you are [age] years old.

# YOUR CODE HERE:


# Q12. Write a program that:
#      - Asks the user to enter a float number
#      - Prints its integer version (truncated)
#      - Prints whether it is greater than 10 (True/False)

# YOUR CODE HERE:


# Q13. PREDICT — what type does input() always return?
#      Circle one:   int   /   float   /   str   /   depends on input
#
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 5: bool
# --------------------------------------------------

# Q14. Predict the output of each line:

# print(bool(0))       # prediction:
# print(bool(1))       # prediction:
# print(bool(-5))      # prediction:
# print(bool(0.0))     # prediction:
# print(bool(3.14))    # prediction:
# print(bool(""))      # prediction:  ← empty string
# print(bool("hi"))    # prediction:
# print(bool(None))    # prediction:


# Q15. Arithmetic with booleans — predict:

# print(True + True)         # prediction:
# print(True + True + True)  # prediction:
# print(False + False)       # prediction:
# print(10 + True)           # prediction:
# print(10 - False)          # prediction:
# print(True * 5)            # prediction:


# Q16. Which comparison gives True and which gives False?

x = 15
# print(x > 10)    # prediction:
# print(x == 15)   # prediction:
# print(x < 5)     # prediction:
# print(x != 20)   # prediction:


# --------------------------------------------------
# SECTION 6: complex
# --------------------------------------------------

# Q17. Create a complex number with real=4, imaginary=7
#      and print:  the number, its real part, its imaginary part, its type

# YOUR CODE HERE:


# Q18. Add two complex numbers:
#      a = 3 + 5j
#      b = 2 + 4j
#      Print their sum.
#      Predicted sum: ___________

# YOUR CODE HERE:


# Q19. Does Python use 'i' or 'j' for the imaginary part?
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 7: dir() and help()
# --------------------------------------------------

# Q20. Run this — how many methods does str have?
methods = dir(str)
print("Number of str methods:", len(methods))
# Count:


# Q21. Which function gives you FULL DOCUMENTATION (with descriptions)?
#      a) dir(str)
#      b) help(str)
#      c) type(str)
# YOUR ANSWER:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Write a program that accepts a student's 3 subject marks
# at runtime (use input + int conversion), calculates and
# prints the average as a float.

# YOUR CODE HERE:


# BONUS 2:
# A shopkeeper wants a bill calculator.
# Ask the user for:
#   - Item name (string)
#   - Price per item (float)
#   - Quantity (int)
# Print:  [item name]: Rs. [total]  where total = price * quantity

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL the output of this program WITHOUT running it.
# Then run it to verify.

p = "5"
q = "3"
print(p + q)
print(int(p) + int(q))
print(float(p) + float(q))
print(bool(p))
print(bool(int(p) - 5))

# Your full prediction:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What does  int(9.9)  return?
#    A) 10    B) 9    C) 9.9    D) Error
# Answer: ___

# Q_MCQ_2. What does  input()  ALWAYS return, regardless of what
#           the user types?
#    A) int    B) float    C) str    D) The type that matches the input
# Answer: ___

# Q_MCQ_3. What is the type of  None  in Python?
#    A) NoneType    B) null    C) undefined    D) void
# Answer: ___

# Q_MCQ_4. What does  bool(0)  return?
#    A) True    B) False    C) 0    D) Error
# Answer: ___

# Q_MCQ_5. Which conversion raises a ValueError?
#    A) int("42")      B) float("3.14")
#    C) int("hello")   D) str(100)
# Answer: ___

# Q_MCQ_6. What does  int(-9.9)  return? (tricky!)
#    A) -10    B) -9    C) 9    D) Error
# Answer: ___

# Q_MCQ_7. The real and imaginary parts of  3+4j  are:
#    A) 3.0 and 4.0    B) 3 and 4    C) "3" and "4j"    D) 3j and 4j
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. int() does NOT round — it _______ toward zero.
#         int(9.9) = _______,   int(-9.9) = _______.

# FIB_2. type(None) returns _______.

# FIB_3. bool("") = _______,   bool("hello") = _______.

# FIB_4. To convert the string "42" to an integer: _______.
#         To convert the string "3.14" to a float: _______.

# FIB_5. The complex number 5+3j has .real = _______ and .imag = _______.

# FIB_6. str(3.14) converts the float to the string _______.

# FIB_7. To safely convert user input to int, always wrap it:
#         age = _______( input("Age: ") )


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Build a shop billing calculator that handles all types
#           and conversions explicitly.
#
# Requirements:
#   1. Take 3 item names and their prices as input (strings from input())
#   2. Convert prices to float (show the type before and after conversion)
#   3. Calculate subtotal
#   4. Apply 18% GST: gst = subtotal * 0.18
#   5. Print a formatted bill with item name, price, subtotal, GST, total
#   6. Show "Cash received" (input as string → float) and compute change
#   7. Handle edge case: if change < 0, print "Insufficient cash!"
#
# Expected output:
#   ====== BILL ======
#   Pen         :  10.50
#   Notebook    :  45.00
#   Eraser      :   5.00
#   ------------------
#   Subtotal    :  60.50
#   GST (18%)   :  10.89
#   TOTAL       :  71.39
#   Cash given  : 100.00
#   Change      :  28.61
#
# Hint: Use  f"{value:>8.2f}"  for right-aligned 2-decimal formatting.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1:  None  /  <class 'NoneType'>

# Q2:
# score = None
# print(score)

# Q3:
# connection = None
# print(type(connection))       # <class 'NoneType'>
# connection = "database_connected"
# print(type(connection))       # <class 'str'>

# Q4: int, int, int, float, float, float  (100.0 is float even though it looks like a whole number)

# Q5:
# int(9.9)   → 9    (NOT 10 — truncates, does NOT round)
# int(9.1)   → 9
# int(-9.9)  → -9   (tricky! truncates toward zero, not toward -10)
# int(0.99)  → 0
# KEY: int() TRUNCATES (drops decimal), does NOT round

# Q6:
# int() or float()  — use int() if you want whole numbers
# result = int(price) + 100
# print(result)   # 599

# Q7: value = 12, type = <class 'int'>

# Q8:
# Crash reason: "hello" cannot be converted to a number
# Safe approach:
# text = "hello"
# if text.isdigit():
#     result = int(text)
# else:
#     print("Not a valid number")

# Q10:
# a) Output: 53  (string concatenation "5"+"3" = "53")
# b) input() always returns str; + on strings concatenates
# c) a = int(input(...)); b = int(input(...))

# Q11:
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello", name + ", you are", age, "years old.")

# Q12:
# num = float(input("Enter a float number: "))
# print("Integer version:", int(num))
# print("Greater than 10:", num > 10)

# Q13: str — always, no matter what the user types

# Q14:
# bool(0)    → False
# bool(1)    → True
# bool(-5)   → True   (any non-zero = True)
# bool(0.0)  → False
# bool(3.14) → True
# bool("")   → False  (empty string = False)
# bool("hi") → True   (non-empty string = True)
# bool(None) → False

# Q15:
# True + True        → 2
# True+True+True     → 3
# False + False      → 0
# 10 + True          → 11
# 10 - False         → 10
# True * 5           → 5

# Q16: True, True, False, True

# Q17:
# c = complex(4, 7)  OR  c = 4 + 7j
# print(c)         # (4+7j)
# print(c.real)    # 4.0
# print(c.imag)    # 7.0
# print(type(c))   # <class 'complex'>

# Q18:
# a = 3 + 5j
# b = 2 + 4j
# print(a + b)    # (5+9j)

# Q19: j  (not i)

# Q21: b) help(str)

# BONUS 3 Prediction:
# 53          (string concat)
# 8           (int addition)
# 8.0         (float addition)
# True        (non-empty string)
# False       (int("5")-5 = 0 → bool(0) = False)


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: A   Q_MCQ_4: B
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: A

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: truncates;  9;  -9
# FIB_2: <class 'NoneType'>
# FIB_3: False;  True  (empty string is falsy, non-empty is truthy)
# FIB_4: int("42");  float("3.14")
# FIB_5: 5.0;  3.0
# FIB_6: "3.14"
# FIB_7: int

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# items = []
# for _ in range(3):
#     name  = input("Item name : ")
#     price = input("Price     : ")
#     price = float(price)          # str → float conversion
#     items.append((name, price))
# subtotal = sum(p for _, p in items)
# gst      = subtotal * 0.18
# total    = subtotal + gst
# print("====== BILL ======")
# for name, price in items:
#     print(f"{name:<12}: {price:>7.2f}")
# print("-" * 18)
# print(f"{'Subtotal':<12}: {subtotal:>7.2f}")
# print(f"{'GST (18%)':<12}: {gst:>7.2f}")
# print(f"{'TOTAL':<12}: {total:>7.2f}")
# cash = float(input("Cash given: "))
# change = cash - total
# print(f"{'Cash given':<12}: {cash:>7.2f}")
# if change < 0:
#     print("Insufficient cash!")
# else:
#     print(f"{'Change':<12}: {change:>7.2f}")

