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
