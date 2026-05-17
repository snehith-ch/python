# ============================================================
# PRACTICE — Day 20: Built-in Modules (math, datetime, calendar, random)
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: math MODULE
# --------------------------------------------------

# Q1. Predict the output — and note the return type (int or float):

import math

print(math.sqrt(64))        # prediction:
print(math.sqrt(2))         # prediction (approximate):
print(math.factorial(0))    # prediction:
print(math.factorial(5))    # prediction:
print(math.ceil(3.1))       # prediction:
print(math.ceil(3.9))       # prediction:
print(math.floor(3.1))      # prediction:
print(math.floor(3.9))      # prediction:
print(math.pow(2, 10))      # prediction: int or float?
print(type(math.pow(2, 10))) # prediction:


# Q2. Compare math.pow vs ** — predict:

print(2 ** 10)               # prediction: int or float?
print(math.pow(2, 10))       # prediction: int or float?
print(type(2 ** 10))         # prediction:
print(type(math.pow(2, 10))) # prediction:


# Q3. Using from math import * — predict the output:

from math import *

print(pi)            # prediction:
print(sqrt(100))     # prediction: (no 'math.' prefix now)
print(ceil(-2.3))    # prediction: what does ceil do to negatives?
print(floor(-2.3))   # prediction: what does floor do to negatives?


# Q4. Write code using math functions:
# a) Area of a circle with radius 7 (A = π * r²)
# b) Hypotenuse of a right triangle with sides 3 and 4 (√(3² + 4²))

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 2: datetime MODULE
# --------------------------------------------------

# Q5. Predict what each line displays (run to confirm exact values):

import datetime

now = datetime.datetime.now()
print(now)            # prediction (format):
print(type(now))      # prediction:
print(now.year)       # prediction:
print(now.month)      # prediction:
print(now.day)        # prediction:
print(now.hour)       # prediction:
print(now.minute)     # prediction:


# Q6. Predict the output — strftime format codes:

now = datetime.datetime.now()

print(now.strftime("%A"))   # prediction: full weekday name
print(now.strftime("%a"))   # prediction: short weekday name
print(now.strftime("%B"))   # prediction: full month name
print(now.strftime("%b"))   # prediction: short month name
print(now.strftime("%Y"))   # prediction: 4-digit year
print(now.strftime("%y"))   # prediction: 2-digit year
print(now.strftime("%d"))   # prediction: day of month


# Q7. Create a specific date — predict the output:

d = datetime.date(2000, 1, 1)
print(d)              # prediction:
print(d.year)         # prediction:
print(d.month)        # prediction:
print(d.day)          # prediction:
print(d.strftime("%A, %d %B %Y"))   # prediction (format this date):


# Q8. Write code to print today's date in this format:
# "Today is Wednesday, 17 May 2026"

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 3: calendar MODULE
# --------------------------------------------------

# Q9. Predict what these print:

import calendar

print(calendar.isleap(2000))   # prediction:
print(calendar.isleap(1900))   # prediction:   ← tricky!
print(calendar.isleap(2024))   # prediction:
print(calendar.isleap(2023))   # prediction:


# Q10. Count leap years — predict:

print(calendar.leapdays(2000, 2026))   # prediction: how many leap years?
# Note: leapdays(y1, y2) counts from y1 UP TO BUT NOT INCLUDING y2

# List the leap years from 2000 to 2024 manually:
# YOUR ANSWER:


# Q11. Print the calendar for a month — just run this and observe the format:

print(calendar.month(2026, 5))


# --------------------------------------------------
# SECTION 4: random MODULE
# --------------------------------------------------

# Q12. Predict the TYPE of each result (values vary — that's random):

from random import *

r1 = random()           # type prediction:
r2 = randint(1, 10)     # type prediction:
r3 = uniform(1.0, 5.0)  # type prediction:
r4 = randrange(0, 10, 2)  # type prediction:

print(type(r1), type(r2), type(r3), type(r4))   # prediction:


# Q13. Predict the RANGE of each (min possible, max possible):

# random():             min? max? (are 0 and 1 included?)
# randint(1, 6):        min? max? (inclusive?)
# uniform(0, 1):        min? max?
# randrange(0, 10, 2):  what values are possible?

# YOUR ANSWERS:


# Q14. choice() — predict:

fruits = ["apple", "banana", "cherry", "date"]
pick = choice(fruits)
print(type(pick))      # prediction:
# Can you predict the exact value? Why or why not?


# Q15. Simulate a die roll — write code that rolls two dice
# 10 times and prints the result of each roll (two numbers per roll).

# YOUR CODE HERE:


# Q16. Predict: is it possible for randint(1, 6) to return 6?
#               is it possible for randrange(1, 6) to return 6?
#               what values can randrange(0, 10, 3) return?
# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 5: ARRAY vs NumPy
# --------------------------------------------------

# Q17. Predict the output:

from array import array

a = array('i', [10, 20, 30, 40, 50])
print(type(a))     # prediction:
print(a)           # prediction (format):
print(a[0])        # prediction:
print(a[-1])       # prediction:
print(len(a))      # prediction:


# Q18. array is homogeneous — predict the error:

# mixed = array('i', [1, 2, "three"])   # uncomment — prediction (error?):


# Q19. NumPy — if installed, predict the output:

# import numpy as np
# a1 = np.array([1, 2, 3, 4, 5])
# print(a1)
# print(type(a1))
# print(a1 * 2)   # element-wise multiplication — prediction:
#
# a2 = np.array([[1, 2, 3],
#                [4, 5, 6]])
# print(a2)
# print(a2.shape)  # prediction: (rows, columns)


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Use datetime to calculate:
# a) How many days until New Year's Day 2027 from today
# b) What day of the week was January 1, 2000?
# Hint: datetime.date objects support subtraction.

import datetime
# YOUR CODE HERE:


# BONUS 2:
# Write a function random_password(length) that generates
# a random password of the given length using:
# - letters a-z and A-Z (hint: use chr() and range())
# - digits 0-9
# - choice() to pick each character
# Print a password of length 12.

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

import math, datetime
from random import randint, choice

print(math.ceil(math.pi))      # prediction:
print(math.floor(math.e))      # prediction:

now = datetime.datetime.now()
print(now.strftime("%Y"))      # prediction:

items = ["rock", "paper", "scissors"]
print(choice(items))           # prediction (exact value? or just type?):

print(randint(1, 1))           # prediction:

# Your full prediction:


# BONUS 4:
# Write a program that:
# 1. Asks the user for a year
# 2. Prints whether it's a leap year
# 3. Prints the full calendar for that year
# 4. Counts and prints the number of leap years since 1900 up to (not including) that year

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: 8.0, 1.414..., 1, 120, 4, 4, 3, 3, 1024.0, <class 'float'>

# Q2: 1024 (int), 1024.0 (float); <class 'int'>, <class 'float'>

# Q3: 3.14159..., 10.0, -2 (ceil goes toward positive infinity), -3 (floor goes toward negative infinity)

# Q9: True (2000 divisible by 400), False (1900 divisible by 100 but NOT 400), True, False

# Q10: 7 leap years (2000,2004,2008,2012,2016,2020,2024)

# Q12: <class 'float'>, <class 'int'>, <class 'float'>, <class 'int'>

# Q13:
# random(): 0 < x < 1 (exclusive)
# randint(1,6): 1 to 6 inclusive
# uniform(0,1): 0 to 1 inclusive
# randrange(0,10,2): 0,2,4,6,8

# Q16: randint(1,6) CAN return 6 (inclusive)
#      randrange(1,6) CANNOT return 6 (stop is exclusive) → returns 1,2,3,4,5
#      randrange(0,10,3) → 0, 3, 6, 9

# Q17: <class 'array.array'>, array('i',[10,20,30,40,50]), 10, 50, 5

# BONUS 3: 4, 2, current year, any one of the 3 strings, 1
