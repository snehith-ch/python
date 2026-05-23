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




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. def f(a, b, /, c): — which arguments are positional-only?
#    A) All of them    B) Only c    C) a and b    D) b and c
# Answer: ___

# Q_MCQ_2. def f(a, *, b): — which is TRUE?
#    A) b can be passed positionally      B) b MUST be passed as keyword
#    C) a must be passed as keyword       D) Both a and b are keyword-only
# Answer: ___

# Q_MCQ_3. alias = my_function — what does alias refer to?
#    A) A copy of the function    B) The same function object
#    C) A new function            D) A backup that can't be called
# Answer: ___

# Q_MCQ_4. A recursive function MUST have:
#    A) A return statement        B) A base case to stop recursion
#    C) At least 2 parameters     D) A global variable
# Answer: ___

# Q_MCQ_5. factorial(5) using recursion = ?
#    A) 25    B) 60    C) 120    D) 720
# Answer: ___

# Q_MCQ_6. An inner (nested) function can access variables from:
#    A) Only its own local scope
#    B) Its own scope AND the enclosing outer function's scope
#    C) Only global scope
#    D) Only built-in scope
# Answer: ___

# Q_MCQ_7. What does the / separator in def f(a, b, /, c) prevent?
#    A) Passing too many arguments     B) Passing a and b as keyword arguments
#    C) Passing c positionally         D) Calling the function with less than 3 args
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. def f(a, b, /, c, d): — a and b are _______ only;
#         c and d can be positional OR _______.

# FIB_2. def f(a, *, b, c): — b and c are _______ only.

# FIB_3. square = power  creates an _______ — both names point to the
#         _______ function object.

# FIB_4. A recursive function calls _______.

# FIB_5. Base case for factorial: factorial(0) = _______ and factorial(1) = _______.

# FIB_6. Without a base case, recursion causes _______ error.

# FIB_7. The inner function has access to the outer function's variables
#         through the _______ scope (E in LEGB).


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Math Utility Library with all advanced function features.
#
# Requirements:
#   1. power(base, exp, /) — POSITIONAL-ONLY, compute base**exp recursively
#      Base case: exp==0 → return 1;  Recursive: base * power(base, exp-1)
#   2. greet(*, name, greeting="Namaste") — KEYWORD-ONLY
#      Prints: "{greeting}, {name}! Welcome to Python."
#   3. make_multiplier(n) — returns a nested function multiply(x)
#      that multiplies x by n (demonstrates closure)
#   4. fibonacci(n) — recursive;  fib(0)=0, fib(1)=1, else fib(n-1)+fib(n-2)
#   5. Create aliases:  square = power,  double = make_multiplier(2)
#   6. Demonstrate:
#      a) square(5, 2)  → 25  (using alias)
#      b) double(7)     → 14  (using closure alias)
#      c) greet(name="Snehith")  → uses default greeting
#      d) fib sequence for n=0..7
#      e) Try calling power(base=2, exp=3) → should raise TypeError
#
# Expected output (partial):
#   power(3, 4)   = 81
#   square(5, 2)  = 25
#   double(7)     = 14
#   greet → Namaste, Snehith! Welcome to Python.
#   fib(7) = 13
#   Fibonacci 0-7: [0,1,1,2,3,5,8,13]
#   Calling power(base=2, exp=3) → TypeError (positional-only violated)

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


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: C   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: positional;  keyword
# FIB_2: keyword
# FIB_3: alias;  same
# FIB_4: itself
# FIB_5: 1;  1
# FIB_6: RecursionError (maximum recursion depth exceeded)
# FIB_7: enclosing

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# def power(base, exp, /):
#     if exp == 0: return 1
#     return base * power(base, exp - 1)
#
# def greet(*, name, greeting="Namaste"):
#     print(f"{greeting}, {name}! Welcome to Python.")
#
# def make_multiplier(n):
#     def multiply(x):
#         return x * n
#     return multiply
#
# def fibonacci(n):
#     if n <= 0: return 0
#     if n == 1: return 1
#     return fibonacci(n-1) + fibonacci(n-2)
#
# square = power
# double = make_multiplier(2)
#
# print(f"power(3, 4)   = {power(3, 4)}")
# print(f"square(5, 2)  = {square(5, 2)}")
# print(f"double(7)     = {double(7)}")
# greet(name="Snehith")
# print(f"fib(7) = {fibonacci(7)}")
# print(f"Fibonacci 0-7: {[fibonacci(i) for i in range(8)]}")
# try:
#     power(base=2, exp=3)
# except TypeError as e:
#     print(f"Calling power(base=2, exp=3) → TypeError: {e}")

