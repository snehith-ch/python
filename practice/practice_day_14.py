# ============================================================
# PRACTICE — Day 14: Bytes, Bytearray, Frozenset & Functions Intro
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: bytes
# --------------------------------------------------

# Q1. Predict the type and output:

x = [10, 50, 100, 200, 255]
b = bytes(x)

# print(x)            # prediction:
# print(type(x))      # prediction:
# print(b)            # prediction:   ← binary format
# print(type(b))      # prediction:


# Q2. Access by index — predict:

b = bytes([10, 20, 30, 40, 50])

# print(b[0])    # prediction:
# print(b[-1])   # prediction:
# print(b[2])    # prediction:


# Q3. bytes are immutable — predict the error:

b = bytes([10, 20, 30])
# b[0] = 99   # uncomment to see error — what error?
# YOUR PREDICTION:


# Q4. Range restriction — predict which line crashes:

# bytes([0, 100, 255])   # valid? prediction:
# bytes([0, 256])        # valid? prediction:   ← what error?


# Q5. Iterate over bytes — write the code and predict output:

b = bytes([5, 10, 15])
for val in b:
    print(val)

# Prediction:


# --------------------------------------------------
# SECTION 2: bytearray
# --------------------------------------------------

# Q6. Difference between bytes and bytearray — predict:

x = [10, 20, 30]
b  = bytes(x)
ba = bytearray(x)

# Can you change bytes?
# b[0] = 99     # prediction:

# Can you change bytearray?
ba[0] = 99
print(ba)   # prediction:


# Q7. Both have the same range restriction — predict:

# bytearray([255])   # prediction: valid or error?
# bytearray([256])   # prediction: valid or error?


# --------------------------------------------------
# SECTION 3: frozenset
# --------------------------------------------------

# Q8. Create a frozenset and check its type:

s  = {10, 20, 30, 40}
fs = frozenset(s)

# print(type(s))    # prediction:
# print(type(fs))   # prediction:
# print(fs)         # prediction:


# Q9. frozenset is immutable — predict the error:

fs = frozenset({1, 2, 3})
# fs.add(4)      # uncomment to see error — what error?
# YOUR PREDICTION:


# Q10. Differences between set and frozenset — fill in the table:
#
# Feature    | set   | frozenset
# -----------|-------|----------
# Mutable    |  Yes  |  ???
# Indexing   |  No   |  ???
# Duplicates |  No   |  ???
# Can add    |  Yes  |  ???


# --------------------------------------------------
# SECTION 4: FUNCTIONS — Basics
# --------------------------------------------------

# Q11. Write a function that prints "Hello, Python!" and call it 3 times.
#      (No parameters, no return value)

# YOUR CODE HERE:


# Q12. Write a function greet(name) that prints "Hello, [name]!"
#      Call it with: "Snehith", "Alice", "World"

# YOUR CODE HERE:


# Q13. Predict the output — trace function execution:

def show(x):
    print("Value is:", x)

show(10)
show("Python")
show(True)
show([1, 2, 3])

# Prediction (4 lines):


# Q14. Function with two parameters — write and call:
#      add(a, b): prints the sum of a and b
#      Call with: (10, 20), (3.5, 1.5), (100, -50)

# YOUR CODE HERE:


# Q15. return vs print — predict the difference:

def add_print(a, b):
    print(a + b)        # just displays

def add_return(a, b):
    return a + b        # sends value back

# What is stored in r1 and r2?
r1 = add_print(10, 20)
r2 = add_return(10, 20)

# print(r1)   # prediction:
# print(r2)   # prediction:


# Q16. Using return value in further computation:

def square(n):
    return n * n

def cube(n):
    return n * n * n

s = square(5)
c = cube(3)
print("Square of 5:", s)    # prediction:
print("Cube of 3:", c)      # prediction:
print("Total:", s + c)      # prediction:


# Q17. Write a function is_even(n) that:
#      - Returns True if n is even, False if odd
#      Test with: 4, 7, 0, 13

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Write a function that accepts a list and returns:
# (min_val, max_val, average) — all three as a return
# But: is this good practice? What would be the better approach?

# YOUR CODE HERE:


# BONUS 2:
# Write functions for a simple calculator:
#   - add(a, b): returns a + b
#   - subtract(a, b): returns a - b
#   - multiply(a, b): returns a * b
#   - divide(a, b): returns a / b (handle division by zero)
# Call each and print results.

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

def greet(name):
    return "Hello, " + name + "!"

def loud(text):
    return text.upper()

result = greet("Python")
print(result)
print(loud(result))
print(greet("World"))
print(type(greet("test")))

# Your full prediction:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: [10,50,100,200,255] list; bytes — binary representation; <class 'bytes'>

# Q2: 10, 50, 30

# Q3: TypeError: 'bytes' object does not support item assignment

# Q4: [0,100,255] valid; [0,256] → ValueError: bytes must be in range(0, 256)

# Q6: b[0]=99 → TypeError (immutable); ba[0]=99 works — bytearray(b'\x63\x14\x1e')

# Q8: set, frozenset, frozenset({10, 20, 30, 40})

# Q9: AttributeError: 'frozenset' object has no attribute 'add'

# Q13:
# Value is: 10
# Value is: Python
# Value is: True
# Value is: [1, 2, 3]

# Q15: r1 = None (add_print returns nothing); r2 = 30

# Q16: 25, 27, 52

# BONUS 3:
# "Hello, Python!"
# "HELLO, PYTHON!"
# "Hello, World!"
# <class 'str'>
