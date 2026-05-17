# ============================================================
# PRACTICE — Day 17: Special Arguments, Aliasing, Nested Functions & Recursion
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: POSITIONAL-ONLY ARGUMENTS (/)
# --------------------------------------------------

# Q1. Predict which call succeeds and which causes an error:

def add(a, b, /):
    return a + b

print(add(10, 20))         # prediction:
# print(add(a=10, b=20))  # uncomment to see error — prediction:


# Q2. Predict the output:

def greet(name, /, message="Hello"):
    print(message, name)

greet("Snehith")               # prediction:
greet("Alice", message="Hi")   # prediction:
# greet(name="Bob")            # prediction (error?):


# --------------------------------------------------
# SECTION 2: KEYWORD-ONLY ARGUMENTS (*)
# --------------------------------------------------

# Q3. Predict which call works:

def connect(*, host, port):
    print("Connecting to", host, "on port", port)

connect(host="localhost", port=8080)   # prediction:
# connect("localhost", 8080)           # uncomment to see error — prediction:


# Q4. Predict the output — mixing / and *:

def transfer(src, /, *, dst):
    print("From", src, "to", dst)

transfer("A", dst="B")   # prediction:
# transfer("A", "B")     # predict the error:
# transfer(src="A", dst="B")  # predict the error:


# --------------------------------------------------
# SECTION 3: FUNCTION ALIASING
# --------------------------------------------------

# Q5. Predict the output — are the ids the same?

def wish(name):
    print("Good morning,", name)

greet = wish

wish("Snehith")    # prediction:
greet("Alice")     # prediction:

print(id(wish))    # prediction (same or different than next line?):
print(id(greet))   # prediction:


# Q6. Predict what happens after deleting one alias:

def say_hi(name):
    print("Hi,", name)

hello = say_hi

del say_hi

hello("Bob")       # prediction: works or error?
# say_hi("Bob")    # uncomment to see — prediction (what error?):


# Q7. How many names point to the function after each step?
# Trace the reference count mentally:

def f():
    print("I am f")

g = f
h = f

del f
del g

h()   # prediction: works or error?


# --------------------------------------------------
# SECTION 4: NESTED FUNCTIONS
# --------------------------------------------------

# Q8. Predict the output:

def outer():
    print("outer: start")

    def inner():
        print("inner: running")

    inner()
    print("outer: end")

outer()   # prediction (3 lines):
# inner()   # uncomment — prediction (what error?):


# Q9. Inner function uses outer's variable — predict:

def outer():
    msg = "Hello from outer"

    def inner():
        print(msg)   # can inner see msg?

    inner()

outer()   # prediction:


# Q10. Inner NOT called — predict the output:

def outer():
    print("outer runs")

    def inner():
        print("inner runs")

    # inner is defined but NOT called

outer()   # prediction: how many lines of output?


# --------------------------------------------------
# SECTION 5: RECURSION
# --------------------------------------------------

# Q11. Trace the factorial function — predict the output:

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(0))   # prediction:
print(factorial(1))   # prediction:
print(factorial(5))   # prediction:
print(factorial(6))   # prediction:


# Q12. Trace the steps for factorial(4):
# Write each call and its return value as a comment:
# factorial(4) = 4 * factorial(3)
# factorial(3) = ???
# ...


# Q13. Write a recursive function sum_digits(n) that returns
# the sum of all digits in a positive integer.
# Example: sum_digits(123) → 6, sum_digits(999) → 27

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 6: math MODULE
# --------------------------------------------------

# Q14. Predict the output of each:

import math

print(math.sqrt(49))      # prediction:
print(math.sqrt(2))       # prediction (approx):
print(math.factorial(0))  # prediction:
print(math.factorial(7))  # prediction:
print(math.ceil(3.001))   # prediction:
print(math.ceil(3.999))   # prediction:
print(math.floor(3.001))  # prediction:
print(math.floor(3.999))  # prediction:
print(math.pow(3, 4))     # prediction: (int or float?)
print(3 ** 4)             # prediction: (int or float?)


# Q15. Predict True or False:

print(math.ceil(5.0) == 5)    # prediction:
print(math.floor(5.0) == 5)   # prediction:
print(type(math.sqrt(4)) == float)   # prediction:
print(type(4 ** 2) == int)           # prediction:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Write a recursive function countdown(n) that prints
# n, n-1, n-2, ... 1, then "Go!"
# Base case: when n == 0, print "Go!" and return.
# Test with countdown(5).

# YOUR CODE HERE:


# BONUS 2:
# Write a recursive function power(base, exp) that computes
# base ** exp WITHOUT using the ** operator or math.pow.
# Base case: exp == 0 → return 1
# Test with power(2, 10) and power(3, 5).

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

def square(n):
    return n * n

sq = square
del square

print(sq(7))

import math
nums = [1, 4, 9, 16, 25]
roots = [math.sqrt(n) for n in nums]
print(roots)

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

for i in range(6):
    print(i, fact(i))

# Your full prediction:


# BONUS 4:
# Write a nested function setup() that:
# - Defines a local variable config = {"debug": True, "version": "1.0"}
# - Inside it, defines show_config() that prints each key-value pair
# - Calls show_config() before returning
# Call setup().

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: 30; TypeError (positional-only)

# Q2: "Hello Snehith"; "Hi Alice"; TypeError (name is positional-only)

# Q3: "Connecting to localhost on port 8080"; TypeError (must use keyword)

# Q4: "From A to B"; TypeError — dst not keyword; TypeError — src is positional-only

# Q5: "Good morning, Snehith"; "Good morning, Alice"; same id printed twice

# Q6: hello("Bob") → "Hi, Bob"; say_hi("Bob") → NameError

# Q7: h() → "I am f" (still works — function alive via h)

# Q8: "outer: start", "inner: running", "outer: end"; inner() → NameError

# Q9: "Hello from outer"

# Q10: one line — "outer runs"  (inner defined but never called)

# Q11: 1, 1, 120, 720

# Q14: 7.0, 1.41..., 1, 5040, 4, 4, 3, 3, 81.0, 81

# Q15: True, True, True, True

# BONUS 3:
# 49
# [1.0, 2.0, 3.0, 4.0, 5.0]
# 0 1
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120
