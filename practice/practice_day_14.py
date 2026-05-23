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
def calling():
    print("Hello, Python!")

calling()
calling()
calling()

# Q12. Write a function greet(name) that prints "Hello, [name]!"
#      Call it with: "Snehith", "Alice", "World"

# YOUR CODE HERE:
def greet(name):
    print("Hello, " + name + "!")

greet("Snehith")
greet("Alice")
greet("World")

# Q13. Predict the output — trace function execution:

def show(x):
    print("Value is:", x)

show(10)
show("Python")
show(True)
show([1, 2, 3])

# Prediction (4 lines):
''' Value is: 10
    Value is: Python
    Value is: True
    Value is: [1, 2, 3] '''

# Q14. Function with two parameters — write and call:
#      add(a, b): prints the sum of a and b
#      Call with: (10, 20), (3.5, 1.5), (100, -50)

# YOUR CODE HERE:
def add(a, b):
    print(a+b)

add(10, 20)
add(3.5, 1.5)
add(100, -50)

# Q15. return vs print — predict the difference:

def add_print(a, b):
    print(a + b)        # just displays

def add_return(a, b):
    return a + b        # sends value back

# What is stored in r1 and r2?
r1 = add_print(10, 20)
r2 = add_return(10, 20)

# print(r1)   # prediction: it will print 30 then we cant use it for further computation
# print(r2)   # prediction: it will print 30 and we can use it for further computation


# Q16. Using return value in further computation:

def square(n):
    return n * n

def cube(n):
    return n * n * n

s = square(5)
c = cube(3)
print("Square of 5:", s)    # prediction: we get 25 and we can use it for further computation
print("Cube of 3:", c)      # prediction: we get 27 and we can use it for further computation
print("Total:", s + c)      # prediction: we get 52 and we can use it for further computation and in this we used the results of both square and cube functions for further computation


# Q17. Write a function is_even(n) that:
#      - Returns True if n is even, False if odd
#      Test with: 4, 7, 0, 13

# YOUR CODE HERE:
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False 

print(is_even(4))   # prediction: True
print(is_even(7))   # prediction: False
print(is_even(0))   # prediction: True
print(is_even(13))  # prediction: False

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




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What is the valid value range for elements in a  bytes  object?
#    A) 0–127    B) 0–255    C) -128–127    D) Any integer
# Answer: ___

# Q_MCQ_2. Which is MUTABLE — bytes or bytearray?
#    A) bytes    B) bytearray    C) Both    D) Neither
# Answer: ___

# Q_MCQ_3. What does  b"hello"[0]  return?
#    A) 'h'    B) 104    C) b'h'    D) Error
# Answer: ___

# Q_MCQ_4. Why can a frozenset be used as a dict key but a regular set cannot?
#    A) frozenset is smaller      B) frozenset is hashable (immutable);
#       regular set is not        C) frozenset is a subclass of dict
#    D) Regular sets can also be dict keys
# Answer: ___

# Q_MCQ_5. To convert a string "hello" to bytes (UTF-8 encoding):
#    A) bytes("hello")        B) "hello".encode()
#    C) b("hello")            D) bytes.from("hello")
# Answer: ___

# Q_MCQ_6. A function is DEFINED with the keyword _______ and CALLED with:
#    A) def / ()     B) func / {}    C) def / []    D) define / ()
# Answer: ___

# Q_MCQ_7. What does bytearray([72, 101, 108, 108, 111]).decode() return?
#    A) [72,101,108,108,111]    B) "Hello"
#    C) b"Hello"                D) Error
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. bytes values must be in the range _______ to _______.

# FIB_2. b"ABC"[0] = _______ (the ASCII value of 'A').

# FIB_3. bytearray is like bytes but _______ (you can change individual bytes).

# FIB_4. frozenset({1,2,3}) is _______, so it can be used as a _______ key.

# FIB_5. "hello".encode() returns b'_______'.

# FIB_6. A function runs only when it is _______.

# FIB_7. def greet(): pass  → calling greet() returns _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Simple Caesar Cipher using bytes and bytearray.
# A Caesar cipher shifts each letter by a fixed number of positions.
#
# Requirements:
#   1. Take a message string from input()
#   2. Encode it to bytes using .encode()
#   3. Create a bytearray from the bytes (so we can modify it)
#   4. Shift each byte by +3 (wrapping A-Z: if > 90 for uppercase,
#      subtract 26; if > 122 for lowercase, subtract 26)
#      — skip non-letter bytes (spaces, digits, punctuation)
#   5. Decode the bytearray back to a string = encrypted message
#   6. Reverse the shift (-3) to decrypt and verify you get back original
#   7. Use a frozenset of unique byte values as a dict key:
#      {frozenset(encoded): "metadata about message"}
#      Print the dict to show frozenset as key works
#
# Expected output (input: "Hello"):
#   Original  : Hello
#   Encrypted : Khoor
#   Decrypted : Hello  ✓ matches original
#   Stored with frozenset key: True
#
# Hint: For shifting, use:  (byte - 65 + 3) % 26 + 65  for uppercase letters.

# YOUR CODE HERE:


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


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: A   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: 0;  255
# FIB_2: 65
# FIB_3: mutable
# FIB_4: immutable (hashable);  dict
# FIB_5: b'hello'
# FIB_6: called  (invoked)
# FIB_7: None

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# msg = input("Enter message: ")
# encoded = msg.encode()
# ba = bytearray(encoded)
# # Encrypt (shift +3)
# for i, b in enumerate(ba):
#     if 65 <= b <= 90:    # uppercase
#         ba[i] = (b - 65 + 3) % 26 + 65
#     elif 97 <= b <= 122: # lowercase
#         ba[i] = (b - 97 + 3) % 26 + 97
# encrypted = ba.decode()
# print(f"Original  : {msg}")
# print(f"Encrypted : {encrypted}")
# # Decrypt (shift -3)
# ba2 = bytearray(encrypted.encode())
# for i, b in enumerate(ba2):
#     if 65 <= b <= 90:    ba2[i] = (b - 65 - 3) % 26 + 65
#     elif 97 <= b <= 122: ba2[i] = (b - 97 - 3) % 26 + 97
# decrypted = ba2.decode()
# print(f"Decrypted : {decrypted}", "✓ matches original" if decrypted==msg else "✗ mismatch")
# fs_key = frozenset(encoded)
# store = {fs_key: "metadata about message"}
# print(f"Stored with frozenset key: {fs_key in store}")

