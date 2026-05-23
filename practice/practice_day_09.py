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




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What is the key difference between  elif  and a second  if?
#    A) No difference — they behave the same
#    B) elif only runs if the previous condition was False;
#       a second if always evaluates regardless
#    C) elif is faster than if
#    D) elif can have multiple conditions, if cannot
# Answer: ___

# Q_MCQ_2. What does  break  do inside a loop?
#    A) Skips the current iteration and continues
#    B) Exits the entire loop immediately
#    C) Pauses the loop temporarily
#    D) Restarts the loop from the beginning
# Answer: ___

# Q_MCQ_3. What does  continue  do?
#    A) Exits the loop
#    B) Skips the rest of the current iteration and goes to the next
#    C) Ends the program
#    D) Pauses execution for 1 second
# Answer: ___

# Q_MCQ_4. The  else  clause on a  for  loop runs when:
#    A) The loop runs zero times
#    B) The loop completes without hitting a break
#    C) An exception occurs in the loop
#    D) The loop variable is None
# Answer: ___

# Q_MCQ_5. What is the purpose of  pass?
#    A) Skips one iteration
#    B) Exits the loop
#    C) Does nothing — acts as a placeholder
#    D) Prints an empty line
# Answer: ___

# Q_MCQ_6. How many times does this loop run?
#           for i in range(2, 10, 3):  print(i)
#    A) 8    B) 3    C) 4    D) 2
# Answer: ___

# Q_MCQ_7. Which loop is best when you DON'T know how many iterations
#           are needed in advance?
#    A) for loop    B) while loop    C) do-while loop    D) pass loop
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. range(1, 11, 2) generates: _______.

# FIB_2. _______ exits the entire loop; _______ skips to the next iteration.

# FIB_3. The  else  on a while loop runs when the condition becomes _______.

# FIB_4. pass is used as a _______ when a block is syntactically required
#         but you have no code to put there yet.

# FIB_5. for i in "Python":  → i takes values: _______.

# FIB_6. A while loop with no way to become False causes an _______ loop.

# FIB_7. The  in  keyword in  for i in range(5)  means "_______ of".


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Number Guessing Game with limited attempts.
#
# Requirements:
#   1. Secret number is 42 (hardcoded — no random needed)
#   2. Player gets 5 attempts (use while loop with counter)
#   3. After each wrong guess: print "Too high!" or "Too low!"
#   4. If guess is correct: print "🎉 Correct! You got it in X tries!"
#      then break the loop
#   5. Skip invalid inputs (negative numbers or zero) using continue
#   6. Use pass as placeholder for any future feature comment
#   7. After the loop: if not guessed, print "Game over! The number was 42."
#   8. Show remaining attempts each turn
#
# Expected output (example run — guesses: 20, 60, 42):
#   Attempt 1/5 — Enter guess: 20
#   Too low!
#   Attempt 2/5 — Enter guess: 60
#   Too high!
#   Attempt 3/5 — Enter guess: 42
#   🎉 Correct! You got it in 3 tries!
#
# Hint: Use a flag variable  guessed = False  to know if the loop
#       exited via break or naturally.

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


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: 1, 3, 5, 7, 9
# FIB_2: break;  continue
# FIB_3: False
# FIB_4: placeholder / syntactic filler
# FIB_5: P, y, t, h, o, n
# FIB_6: infinite
# FIB_7: each element

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# SECRET = 42
# MAX_TRIES = 5
# guessed = False
# attempts = 0
# while attempts < MAX_TRIES:
#     attempts += 1
#     try:
#         guess = int(input(f"Attempt {attempts}/{MAX_TRIES} — Enter guess: "))
#     except ValueError:
#         print("Please enter a number.")
#         attempts -= 1
#         continue
#     if guess <= 0:
#         print("Enter a positive number.")
#         attempts -= 1
#         continue
#     pass  # placeholder for future hint feature
#     if guess == SECRET:
#         print(f"🎉 Correct! You got it in {attempts} tries!")
#         guessed = True
#         break
#     elif guess < SECRET:
#         print("Too low!")
#     else:
#         print("Too high!")
# if not guessed:
#     print(f"Game over! The number was {SECRET}.")

