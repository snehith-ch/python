# ============================================================
# PRACTICE — Day 8: Bitwise Operators & Control Flow Intro
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: BINARY AND bin()
# --------------------------------------------------

# Q1. Convert each number to binary manually (show division steps),
#     then verify using bin():

# a) 6
# Manual steps:
# bin(6) = ?

# b) 12
# Manual steps:
# bin(12) = ?

# c) 25
# Manual steps:
# bin(25) = ?


# Q2. Convert each binary back to decimal manually:

# a) 0b1111  = ?   (1×8 + 1×4 + 1×2 + 1×1)
# b) 0b1010  = ?
# c) 0b10000 = ?


# Q3. Predict the output:

# print(bin(7))      # prediction:
# print(bin(8))      # prediction:
# print(bin(15))     # prediction:
# print(bin(255))    # prediction:   ← 8 ones!
# print(bin(0))      # prediction:


# --------------------------------------------------
# SECTION 2: BITWISE OPERATORS
# --------------------------------------------------

# Q4. Work out the binary AND (&) manually, then verify:
#
# Example: 10 & 6
#   10 = 1010
#    6 = 0110
#   & = 0010 = 2

# a) 12 & 10
#    12 = ____
#    10 = ____
#     & = ____  = ?

# b) 9 & 5
#    9 = ____
#    5 = ____
#    & = ____  = ?


# Q5. Work out the binary OR (|) manually:

# a) 12 | 10   = ?
# b) 9 | 5     = ?


# Q6. Work out XOR (^) manually:

# a) 12 ^ 10   = ?
# b) 5 ^ 5     = ?   ← same number XOR itself — interesting!


# Q7. Predict the output of ~n using the formula ~n = -(n+1):

# print(~0)     # prediction:
# print(~1)     # prediction:
# print(~9)     # prediction:
# print(~-1)    # prediction:   ← ~(-1) = -(-1+1) = -(0) = 0


# Q8. Left shift and right shift — predict:

# print(1 << 4)    # prediction:   ← 1 × 2⁴
# print(5 << 2)    # prediction:   ← 5 × 4
# print(64 >> 3)   # prediction:   ← 64 ÷ 8
# print(100 >> 2)  # prediction:


# Q9. QUICK RULE: Without computing, predict:
#     n << k = n × (?)
#     n >> k = n ÷ (?)

# Your answer:


# --------------------------------------------------
# SECTION 3: if / else / elif
# --------------------------------------------------

# Q10. Predict the output — trace through step by step:

marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade F")

# Prediction:


# Q11. Predict the output of BOTH versions and explain the difference:

score = 85

# Version 1: multiple if
if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")

print("---")

# Version 2: elif chain
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")

# Version 1 output:
# Version 2 output:
# Why are they different?


# Q12. Write an if/elif/else for a traffic light system:
#      "red"    → print "Stop"
#      "yellow" → print "Get Ready"
#      "green"  → print "Go"
#      anything else → print "Invalid signal"

light = "green"  # change to test others

# YOUR CODE HERE:


# Q13. Write a nested if:
#      - Get a number from the user
#      - If it's positive, check if it's even or odd
#      - If it's negative, print "Negative"
#      - If it's zero, print "Zero"

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Prove using bit operations that:
# - n << 1 doubles n
# - n >> 1 halves n (integer)
# Test with n = 13

n = 13
# print(n << 1, n * 2)        # should be same
# print(n >> 1, n // 2)       # should be same


# BONUS 2:
# Check if a number is even using bitwise AND:
# Hint: n & 1 gives 0 for even, 1 for odd

# Write a function-less check for numbers 1-10:
# YOUR CODE HERE:


# BONUS 3: PREDICT ALL OUTPUT before running

a, b = 10, 6
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(b >> 1)

# Your full prediction:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What does the bitwise AND (&) operator do?
#    A) Returns 1 when EITHER bit is 1
#    B) Returns 1 ONLY when BOTH bits are 1
#    C) Flips all bits
#    D) Shifts bits left
# Answer: ___

# Q_MCQ_2. What is  5 | 3?  (5=0101, 3=0011)
#    A) 1    B) 6    C) 7    D) 15
# Answer: ___

# Q_MCQ_3. What does  1 << 3  compute?
#    A) 3    B) 4    C) 8    D) 16
# Answer: ___

# Q_MCQ_4. ~5  in Python evaluates to:
#    A) -5    B) -6    C) 4    D) 6
# Answer: ___

# Q_MCQ_5. Which operator returns 1 only when the bits DIFFER?
#    A) &    B) |    C) ^    D) ~
# Answer: ___

# Q_MCQ_6. What is  16 >> 2?
#    A) 4    B) 8    C) 64    D) 2
# Answer: ___

# Q_MCQ_7. What is  5 & 3?  (5=0101, 3=0011)
#    A) 7    B) 6    C) 2    D) 1
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. 5 in binary is _______,   3 in binary is _______.

# FIB_2. 5 & 3 = _______  (AND keeps bits where BOTH are 1).

# FIB_3. 5 ^ 3 = _______  (XOR gives 1 where bits _______ ).

# FIB_4. Left shift multiplies by _______.  8 << 1 = _______.

# FIB_5. Right shift divides by _______.  20 >> 2 = _______.

# FIB_6. ~n  equals _______ in Python (two's complement rule).

# FIB_7. bin(13) returns _______.  int('1101', 2) returns _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Access Control System using Bitwise Permission Flags.
# In many real systems (Linux, databases), permissions are stored
# as a single integer using bits.
#
# Flags:
#   READ    = 1   (binary 001)
#   WRITE   = 2   (binary 010)
#   EXECUTE = 4   (binary 100)
#
# Requirements:
#   1. Define the three permission flags as constants
#   2. Create a user with permission = 5 (READ + EXECUTE = 101)
#   3. Check: can the user READ?   (use & flag, result != 0)
#             can the user WRITE?
#             can the user EXECUTE?
#   4. GRANT WRITE permission using | (bitwise OR)
#   5. REVOKE EXECUTE permission using & ~ (AND NOT)
#   6. TOGGLE READ permission using ^ (XOR)
#   7. Print bin() of permission at each step
#
# Expected output:
#   Initial permission: 5 (0b101)
#   Can READ   : True
#   Can WRITE  : False
#   Can EXECUTE: True
#   After granting WRITE : 7 (0b111)
#   After revoking EXECUTE: 3 (0b011)
#   After toggling READ : 2 (0b010)
#
# Hint: To check: (permission & FLAG) != 0
#       To grant:  permission |= FLAG
#       To revoke: permission &= ~FLAG
#       To toggle: permission ^= FLAG

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q2:
# 0b1111  = 15
# 0b1010  = 10
# 0b10000 = 16

# Q3:
# bin(7)   = 0b111
# bin(8)   = 0b1000
# bin(15)  = 0b1111
# bin(255) = 0b11111111
# bin(0)   = 0b0

# Q4:
# a) 12 & 10:  12=1100, 10=1010, & =1000 = 8
# b)  9 & 5:    9=1001,  5=0101, & =0001 = 1

# Q5:
# a) 12 | 10: 1100 | 1010 = 1110 = 14
# b)  9 | 5:  1001 | 0101 = 1101 = 13

# Q6:
# a) 12 ^ 10: 1100 ^ 1010 = 0110 = 6
# b)  5 ^ 5:  0101 ^ 0101 = 0000 = 0  ← any number XOR itself = 0

# Q7: -1, -2, -10, 0

# Q8: 16, 20, 8, 25

# Q9: n << k = n × 2^k;  n >> k = n ÷ 2^k

# Q10: Grade C  (78 >= 70 is True; elif stops there)

# Q11:
# Version 1: B and C both print (85 >= 80 and 85 >= 70 are both True)
# Version 2: Only B prints (elif stops at first True)

# BONUS 3: 2, 14, 12, -11, 20, 3


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: C   Q_MCQ_4: B
# Q_MCQ_5: C   Q_MCQ_6: A   Q_MCQ_7: D

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: 0b101 (101);  0b011 (011)
# FIB_2: 1
# FIB_3: 6;  differ (are different)
# FIB_4: 2;  16
# FIB_5: 4;  5
# FIB_6: -(n+1)   e.g., ~5 = -6
# FIB_7: '0b1101';  13

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# READ, WRITE, EXECUTE = 1, 2, 4
# permission = 5   # READ + EXECUTE
# print(f"Initial permission: {permission} ({bin(permission)})")
# print(f"Can READ   : {bool(permission & READ)}")
# print(f"Can WRITE  : {bool(permission & WRITE)}")
# print(f"Can EXECUTE: {bool(permission & EXECUTE)}")
# permission |= WRITE
# print(f"After granting WRITE : {permission} ({bin(permission)})")
# permission &= ~EXECUTE
# print(f"After revoking EXECUTE: {permission} ({bin(permission)})")
# permission ^= READ
# print(f"After toggling READ : {permission} ({bin(permission)})")

