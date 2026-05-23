# ============================================================
# PRACTICE — Day 41: Decorators and Generators
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Decorators — Basics
# --------------------------------------------------

# Q1. Identify the decorator — predict the output:

def shout(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return inner

@shout
def greet(name):
    return f"hello, {name}"

print(greet("alice"))    # prediction:
print(greet("bob"))      # prediction:


# Q2. Decorator WITHOUT @ symbol — predict:

def add_border(func):
    def inner():
        print("=" * 20)
        func()
        print("=" * 20)
    return inner

def message():
    print("Important message!")

decorated = add_border(message)
decorated()      # prediction (3 lines):
message()        # prediction (original — no border):


# Q3. @decorator order of execution — trace:

def logger(func):
    def inner(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done {func.__name__}")
        return result
    return inner

@logger
def add(a, b):
    return a + b

result = add(3, 4)
print(f"Result: {result}")

# prediction (3 lines):


# Q4. Decorator for exception handling — predict:

def safe_divide(func):
    def inner(a, b):
        if b == 0:
            print("Cannot divide by zero")
            return None
        return func(a, b)
    return inner

@safe_divide
def divide(a, b):
    return a / b

print(divide(10, 2))    # prediction:
print(divide(10, 0))    # prediction:


# Q5. Decorator applied to wrong function type — predict:

def repeat(func):
    def inner():
        func()
        func()
    return inner

@repeat
def wave():
    print("Hello!")

wave()    # prediction (how many times?):

# What if wave took arguments?
# @repeat
# def greet2(name):
#     print(f"Hi {name}")
# greet2("Alice")    # uncomment → prediction (error?):


# --------------------------------------------------
# SECTION 2: Generators
# --------------------------------------------------

# Q6. Generator expression vs list expression — predict types:

L = [x**2 for x in range(5)]    # list expression
g = (x**2 for x in range(5))    # generator expression

print(type(L))    # prediction:
print(type(g))    # prediction:
print(L)          # prediction:
print(g)          # prediction (what does printing a generator show?):


# Q7. Iterating a generator — predict:

g = (x**2 for x in range(5))
for val in g:
    print(val)    # prediction (5 values):


# Q8. Generator function with yield — predict:

def count_up(n):
    for i in range(1, n+1):
        yield i       # pauses here each time

g = count_up(4)
print(next(g))    # prediction:
print(next(g))    # prediction:
print(next(g))    # prediction:
print(next(g))    # prediction:
# print(next(g))  # uncomment → prediction (error?):


# Q9. yield vs return — predict the difference:

def normal():
    return 1
    return 2    # dead code — never reached

def generator():
    yield 1
    yield 2     # reached on second next() call
    yield 3

print(normal())   # prediction:

g = generator()
print(next(g))    # prediction:
print(next(g))    # prediction:
print(next(g))    # prediction:


# Q10. Generator function with logic — predict:

def even_numbers(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2

for val in even_numbers(10):
    print(val)    # prediction (6 values):


# Q11. Generator saves state — predict:

def counter():
    x = 0
    while True:
        yield x
        x += 1    # state is preserved between yields

g = counter()
print(next(g))    # prediction:
print(next(g))    # prediction:
print(next(g))    # prediction:
print(next(g))    # prediction:


# --------------------------------------------------
# SECTION 3: Generator vs List Memory
# --------------------------------------------------

# Q12. Predict the type and behavior:

# Large list — stores all values in memory
L = [x for x in range(1000000)]
print(type(L))      # prediction:
print(len(L))       # prediction:

# Large generator — generates on the fly
g = (x for x in range(1000000))
print(type(g))      # prediction:
# print(len(g))     # uncomment → prediction (error? generators have no len):


# Q13. Generator can only be iterated ONCE — predict:

g = (x for x in range(3))
print(list(g))    # prediction: consumes generator
print(list(g))    # prediction: generator exhausted → ?


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q14. Write a decorator validate_positive that:
#   - Checks if both arguments to a function are positive
#   - If not, prints "Arguments must be positive" and returns None
#   - Otherwise calls the original function
# Apply it to multiply(a, b).

# YOUR CODE HERE:


# Q15. Write a generator function fibonacci() that yields
# the Fibonacci sequence indefinitely. Print the first 8 values.

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — what does `type()` show for a generator function call?

def gen():
    yield 1

print(type(gen))     # prediction (the function itself):
print(type(gen()))   # prediction (calling the function):


# BONUS 2: Decorator stacking — predict:

def double(func):
    def inner(x):
        return func(x) * 2
    return inner

def negate(func):
    def inner(x):
        return -func(x)
    return inner

@double
@negate
def value(x):
    return x

print(value(5))    # prediction: decorators apply bottom-up → negate first, then double


# BONUS 3: Generator for lazy reading — explain:
# Why is a generator better than a list when reading 1 million records from a database?
# YOUR ANSWER:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. A decorator is a function that:
#    A) Adds syntax sugar to loops    B) Wraps another function to extend it
#    C) Replaces class methods    D) Only works with built-in functions
# Answer: ___

# Q_MCQ_2. The @decorator syntax is equivalent to:
#    A) decorator = func    B) func = decorator(func)
#    C) func.apply(decorator)    D) import decorator
# Answer: ___

# Q_MCQ_3. A generator function uses  _______ instead of return.
#    A) send    B) yield    C) produce    D) output
# Answer: ___

# Q_MCQ_4. next(gen)  on a generator:
#    A) Resets the generator    B) Produces the next yielded value
#    C) Returns all values    D) Raises StopIteration immediately
# Answer: ___

# Q_MCQ_5. What does  functools.wraps(func)  do inside a decorator?
#    A) Wraps the function in a class    B) Preserves the original function's name and docstring
#    C) Caches the function's result    D) Makes the function thread-safe
# Answer: ___

# Q_MCQ_6. Generators are memory-efficient because:
#    A) They use C extensions    B) They compute values lazily (one at a time)
#    C) They compress data    D) They cache all results
# Answer: ___

# Q_MCQ_7. Which is a valid generator expression?
#    A) [x*2 for x in range(5)]    B) {x*2 for x in range(5)}
#    C) (x*2 for x in range(5))    D) <x*2 for x in range(5)>
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. A decorator is applied to a function using the _______ symbol.

# FIB_2. def outer(func):
#             def wrapper(*args, **kwargs):
#                 ...
#                 return func(*args, **kwargs)
#             return _______   ← the decorator returns this.

# FIB_3. A generator pauses at _______ and resumes when next() is called.

# FIB_4. Calling a generator function returns a _______ object.

# FIB_5. from functools import _______ is used to preserve metadata in decorators.

# FIB_6. Generator expressions use _______ brackets (not square or curly).

# FIB_7. StopIteration is raised when the generator has no more _______ to yield.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Data Pipeline using decorators + generators.
#
# Requirements:
#   1. Write a decorator  @timer  that prints how long a function takes
#   2. Write a decorator  @logger  that prints function name + args on each call
#   3. Write a generator  infinite_counter(start=0)  that yields 0, 1, 2, ...
#   4. Write a generator  csv_row_reader(filename)  that yields one row at a
#      time from a CSV file (lazy — does NOT load all rows at once)
#   5. Apply @timer and @logger to a  process_data(n)  function that
#      consumes n values from infinite_counter and returns their sum
#   6. Print the first 5 rows from csv_row_reader using next()
#
# Expected output:
#   [LOG] process_data called with args=(10,)
#   [TIMER] process_data took 0.0001s
#   Sum of first 10 = 45
#   Row 1: ['Name', 'Score']
#   Row 2: ['Alice', '92']
#   ...
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "HELLO, ALICE", "HELLO, BOB"

# Q2: "====================", "Important message!", "====================" (decorated)
#     "Important message!" (original — no border)

# Q3: "Calling add", "Done add", "Result: 7"

# Q4: 5.0, "Cannot divide by zero" then None (printed)

# Q5: "Hello!" twice; greet2("Alice") → TypeError (inner takes no args, 'name' not passed)

# Q6: <class 'list'>, <class 'generator'>
#     [0, 1, 4, 9, 16], <generator object ...> (shows memory address, not values)

# Q7: 0, 1, 4, 9, 16

# Q8: 1, 2, 3, 4; StopIteration error on 5th next()

# Q9: 1 (normal() only returns first value), generator: 1, 2, 3

# Q10: 0, 2, 4, 6, 8, 10

# Q11: 0, 1, 2, 3

# Q12: <class 'list'>, 1000000, <class 'generator'>
#      TypeError: object of type 'generator' has no len()

# Q13: [0, 1, 2], [] (empty — generator already exhausted)

# BONUS 1: <class 'function'>, <class 'generator'>

# BONUS 2: negate(value)(5) = -5, double(-5) = -10 → prints -10

# BONUS 3: List stores all 1M records in RAM before processing.
#          Generator yields one record at a time — constant memory usage, works for any size.

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: C

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: @  (at sign)
# FIB_2: wrapper
# FIB_3: yield
# FIB_4: generator
# FIB_5: wraps
# FIB_6: round / parentheses ( )
# FIB_7: values

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import time, csv
# from functools import wraps
#
# def timer(func):
#     @wraps(func)
#     def wrapper(*a, **kw):
#         t0 = time.time()
#         result = func(*a, **kw)
#         print(f"[TIMER] {func.__name__} took {time.time()-t0:.4f}s")
#         return result
#     return wrapper
#
# def logger(func):
#     @wraps(func)
#     def wrapper(*a, **kw):
#         print(f"[LOG] {func.__name__} called with args={a}")
#         return func(*a, **kw)
#     return wrapper
#
# def infinite_counter(start=0):
#     n = start
#     while True:
#         yield n; n += 1
#
# def csv_row_reader(filename):
#     with open(filename, newline="") as f:
#         for row in csv.reader(f):
#             yield row
#
# @logger
# @timer
# def process_data(n):
#     gen = infinite_counter()
#     return sum(next(gen) for _ in range(n))
#
# print(f"Sum of first 10 = {process_data(10)}")
#
# # Create a sample CSV first
# with open("sample.csv","w",newline="") as f:
#     csv.writer(f).writerows([["Name","Score"],["Alice","92"],["Bob","78"],
#                               ["Carol","85"],["David","91"],["Eve","77"]])
# reader = csv_row_reader("sample.csv")
# for i in range(5):
#     print(f"Row {i+1}: {next(reader)}")

