# ============================================================
# PRACTICE — Day 9: elif, for loop, while loop, break, continue, pass
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: elif vs multiple if
# --------------------------------------------------

# Q1. Predict the output of BOTH programs. They look similar but behave differently.

score = 75

# Program A — multiple if
print("=== Program A ===")
if score >= 90:
    print("A")
if score >= 75:
    print("B")
if score >= 60:
    print("C")

# Program B — elif
print("=== Program B ===")
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")

# Program A output:
# Program B output:
# Difference:


# Q2. FIX THE BUG — Python does NOT allow "else if" as two words:
#
# age = 20
# if age >= 18:
#     print("Adult")
# else if age >= 13:    ← bug here
#     print("Teen")
# else:
#     print("Child")

# YOUR FIX:


# --------------------------------------------------
# SECTION 2: for loop
# --------------------------------------------------

# Q3. Predict the output:

for i in range(5):
    print(i)

# Prediction (all values):


# Q4. Predict the output:

for i in range(2, 10, 3):
    print(i)

# Prediction:


# Q5. Predict the output:

for i in range(10, 0, -2):
    print(i, end=" ")
print()

# Prediction:


# Q6. Write a for loop that prints the multiplication table of 7
#     (7×1 through 7×10), one result per line.

# YOUR CODE HERE:


# Q7. Loop over a list and print each element with its index:
#     Output should look like:
#     0: apple
#     1: banana
#     2: cherry

fruits = ["apple", "banana", "cherry"]

# YOUR CODE HERE:


# Q8. FIX THE BUG:
#
# for i in range(1, 6)
#     print(i)

# YOUR FIX:


# --------------------------------------------------
# SECTION 3: Nested for loop
# --------------------------------------------------

# Q9. Predict EXACTLY what is printed — count carefully:

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Prediction (list all output lines):


# Q10. Predict the output:

for i in range(1, 5):
    print("*" * i)

# Prediction:


# Q11. Write a nested for loop to print this pattern:
#      1
#      1 2
#      1 2 3
#      1 2 3 4

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 4: while loop
# --------------------------------------------------

# Q12. Predict the output:

i = 1
while i <= 5:
    print(i)
    i += 1

# Prediction:


# Q13. Predict the output:

i = 10
while i > 0:
    print(i, end=" ")
    i -= 3
print()

# Prediction:


# Q14. FIX THE BUG — this is an infinite loop:
#
# i = 1
# while i <= 5:
#     print(i)    # forgot increment!

# YOUR FIX:


# Q15. Write a while loop that asks the user for a number
#      and keeps running until they enter 0. Print the sum of all entered numbers.

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 5: break, continue, pass
# --------------------------------------------------

# Q16. Predict the output:

for i in range(1, 8):
    if i == 5:
        break
    print(i)

# Prediction:


# Q17. Predict the output:

for i in range(1, 8):
    if i == 5:
        continue
    print(i)

# Prediction:


# Q18. Predict the output:

for i in range(1, 8):
    if i == 5:
        pass
    print(i)

# Prediction:
# How does pass differ from break and continue here?


# Q19. CRITICAL — this while loop has a bug with continue:
#
# i = 0
# while i < 5:
#     if i % 2 == 0:
#         continue     # what goes wrong?
#     print(i)
#     i += 1
#
# WHY is this an infinite loop?
# HOW do you fix it?

# YOUR FIX HERE:


# Q20. Write a for loop that:
#      - Loops from 1 to 20
#      - Skips multiples of 3 (use continue)
#      - Stops completely when it reaches 15 (use break)

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Print all prime numbers from 2 to 30.
# Hint: A prime number has no divisors other than 1 and itself.
# Use nested loops or break/continue.

# YOUR CODE HERE:


# BONUS 2:
# FizzBuzz — classic interview question:
# Print numbers from 1 to 30.
# For multiples of 3, print "Fizz" instead.
# For multiples of 5, print "Buzz" instead.
# For multiples of both 3 and 5, print "FizzBuzz".

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

# Your prediction:


# BONUS 4:
# While loop guessing game:
# - Set secret = 7
# - Keep asking user to guess a number
# - Print "Too high!" / "Too low!" / "Correct!"
# - Stop when they guess correctly

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1:
# Program A: B and C (both 75>=75 and 75>=60 are True)
# Program B: B only (elif stops at first True)

# Q3: 0, 1, 2, 3, 4

# Q4: 2, 5, 8

# Q5: 10 8 6 4 2

# Q9:
# 1 1 / 1 2 / 1 3
# 2 1 / 2 2 / 2 3
# 3 1 / 3 2 / 3 3

# Q10:
# *
# **
# ***
# ****

# Q12: 1, 2, 3, 4, 5

# Q13: 10 7 4 1  (stops before -2 because -2 > 0 is False)

# Q16: 1 2 3 4  (stops when i hits 5)

# Q17: 1 2 3 4 6 7  (5 is skipped, rest continue)

# Q18: 1 2 3 4 5 6 7  (pass does nothing — all print including 5)

# Q19: i never increments because continue skips i+=1
# Fix: put i += 1 BEFORE the continue

# BONUS 3: 1, 3  (2 is skipped by continue, 4 triggers break)
