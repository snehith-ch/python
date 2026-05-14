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
