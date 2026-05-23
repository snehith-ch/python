# ============================================================
# PRACTICE — Day 16: Function Arguments
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: POSITIONAL ARGUMENTS
# --------------------------------------------------

# Q1. Predict the output — trace the argument assignment:

def student(name, course, marks):
    print(name, course, marks)

student("Snehith", "Python", 90)   # prediction:
student("Alice", "Java", 85)       # prediction:


# Q2. Predict which call causes an error and why:

def greet(first, last):
    print("Hello,", first, last)

greet("John", "Doe")        # prediction:
# greet("John")             # uncomment to see error — prediction:
# greet("A", "B", "C")     # uncomment to see error — prediction:


# Q3. Wrong ORDER — no error but wrong output. Predict:

def describe(name, age, city):
    print(name, "is", age, "from", city)

describe("Snehith", 22, "Hyderabad")    # correct order — prediction:
describe(22, "Hyderabad", "Snehith")    # wrong order — prediction:


# --------------------------------------------------
# SECTION 2: KEYWORD ARGUMENTS
# --------------------------------------------------

# Q4. Predict the output — does order matter with keyword arguments?

def book(title, author, year):
    print(title, "by", author, "("+str(year)+")")

book(title="Python Crash Course", author="Eric", year=2023)   # prediction:
book(year=2020, title="Clean Code", author="Martin")          # prediction:
book("Fluent Python", year=2022, author="Ramalho")            # prediction:


# Q5. FIX THE BUG — predict the error first, then fix it:

# def show(a, b, c):
#     print(a, b, c)
#
# show(a=1, 2, 3)   # what error? prediction:
# YOUR FIX:


# Q6. Predict the output — mixing positional and keyword:

def info(name, age, city):
    print(name, age, city)

info("Snehith", age=22, city="Hyderabad")   # prediction:
# info("Snehith", city="Hyderabad", 22)     # predict the error:


# --------------------------------------------------
# SECTION 3: DEFAULT ARGUMENTS
# --------------------------------------------------

# Q7. Predict the output for each call:

def register(name, course="Python", fee=5000):
    print(name, course, fee)

register("Alice")                     # prediction:
register("Bob", "Java")               # prediction:
register("Charlie", "C++", 8000)      # prediction:
register("Dave", fee=6000)            # prediction:


# Q8. FIX THE BUG — predict the error, then fix:

# def broken(name="Unknown", age):   # what error?
#     print(name, age)
# YOUR PREDICTION:
# YOUR FIX:


# Q9. Predict the output — default not used when value is provided:

def power(base, exp=2):
    return base ** exp

print(power(3))       # prediction:
print(power(3, 3))    # prediction:
print(power(5))       # prediction:
print(power(2, 10))   # prediction:


# --------------------------------------------------
# SECTION 4: *args — Variable Length Positional
# --------------------------------------------------

# Q10. Predict the type and content of args:

def show(*args):
    print(type(args))
    print(args)

show(10, 20, 30)          # prediction (type, content):
show("a", "b")            # prediction:
show()                    # prediction:   ← zero arguments


# Q11. Predict the output — iterate over *args:

def total(*args):
    s = 0
    for n in args:
        s += n
    print("Sum:", s)

total(10, 20, 30)      # prediction:
total(1, 2, 3, 4, 5)   # prediction:
total(100)             # prediction:


# Q12. Write a function using *args:
# avg(*args): calculates and prints the average of all passed numbers.
# Test with: (10, 20, 30), (5, 15), (100, 200, 300, 400)

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 5: **kwargs — Variable Length Keyword
# --------------------------------------------------

# Q13. Predict the type and content of kwargs:

def display(**kwargs):
    print(type(kwargs))
    print(kwargs)

display(name="Snehith", age=22)       # prediction (type, content):
display(course="Python", marks=90)    # prediction:
display()                             # prediction:   ← zero arguments


# Q14. Predict the output — iterate over **kwargs:

def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

profile(name="Alice", role="Developer", city="Hyderabad")
# prediction (3 lines):


# Q15. What is stored — predict the type:

def check(**kwargs):
    print(type(kwargs))           # prediction:
    print(kwargs.get("name"))     # prediction:

check(name="Bob", age=30)


# --------------------------------------------------
# SECTION 6: COMBINING ARGUMENT TYPES
# --------------------------------------------------

# Q16. Predict the output — trace which value goes where:

def example(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

example(1)                          # prediction (4 lines):
example(1, 2)                       # prediction (4 lines):
example(1, 2, 3, 4, x=5, y=6)      # prediction (4 lines):


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Write max_val(*args) that returns the largest value
# WITHOUT using Python's built-in max().
# Test with: (3, 1, 4, 1, 5, 9, 2, 6)

# YOUR CODE HERE:


# BONUS 2:
# Write describe(**kwargs) that prints a sentence for each key-value pair:
# e.g., "name is Snehith", "age is 22", etc.
# Call it with at least 4 keyword arguments.

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

def f(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

f(1)
f(1, 3)
f(1, 3, 5, 7)
f(1, 3, 5, x=9, y=11)

# Your full prediction:


# BONUS 4:
# Write a function order_total(*items, discount=0, tax=0.18)
# - items are prices (positional, any number)
# - discount is an optional keyword argument (default 0)
# - tax is an optional keyword argument (default 0.18)
# Calculate: subtotal = sum(items)
#            after_discount = subtotal - discount
#            final = after_discount + (after_discount * tax)
# Print each step.

# YOUR CODE HERE:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What is the type of  *args  inside a function?
#    A) list    B) tuple    C) set    D) dict
# Answer: ___

# Q_MCQ_2. What is the type of  **kwargs  inside a function?
#    A) list    B) tuple    C) set    D) dict
# Answer: ___

# Q_MCQ_3. def f(a, b=10) — which of these is a VALID call?
#    A) f()        B) f(1, 2, 3)    C) f(5)    D) f(b=5)
# Answer: ___

# Q_MCQ_4. Which argument type MUST come last in a function signature?
#    A) Positional    B) Default    C) *args    D) **kwargs
# Answer: ___

# Q_MCQ_5. f(b=2, a=1)  uses which type of arguments?
#    A) Positional    B) Keyword    C) Default    D) *args
# Answer: ___

# Q_MCQ_6. Can a positional argument appear AFTER a keyword argument in a call?
#    A) Yes    B) No — SyntaxError    C) Only with *args    D) Only in Python 3.10+
# Answer: ___

# Q_MCQ_7. def total(*nums): return sum(nums) — calling total(1,2,3,4) returns:
#    A) [1,2,3,4]    B) 10    C) (1,2,3,4)    D) Error
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. *args collects extra positional arguments into a _______.

# FIB_2. **kwargs collects extra keyword arguments into a _______.

# FIB_3. Default arguments must come _______ non-default arguments in def.

# FIB_4. def f(a, b=5, *args, **kw): — calling f(1,2,3,x=9) →
#         a=_______, b=_______, args=_______, kw=_______.

# FIB_5. To unpack a list as positional args: f(*my_list) uses _______ unpacking.

# FIB_6. To unpack a dict as keyword args: f(**my_dict) uses _______ unpacking.

# FIB_7. def greet(name, greeting="Hello"): — greeting is a _______ argument.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Flexible Restaurant Order System.
#
# Requirements:
#   1. def place_order(customer_name, *items, table=1, **extras):
#      - customer_name: required positional
#      - *items: list of ordered dishes (variable)
#      - table: keyword with default=1
#      - **extras: any extras (e.g., spicy=True, discount=10, note="...")
#   2. Inside: calculate total (each item costs ₹150 for simplicity)
#              apply discount if in extras
#              add a service charge of 10%
#   3. Print a formatted order receipt
#   4. Call it 3 ways:
#      a) place_order("Snehith", "Biryani", "Lassi")
#      b) place_order("Priya", "Dosa", "Coffee", table=5, spicy=True)
#      c) place_order("Raj", "Burger", "Fries", "Shake", table=3,
#                     discount=15, note="Birthday treat")
#
# Expected output (call c):
#   ========== ORDER RECEIPT ==========
#   Customer : Raj          Table: 3
#   Items    : Burger, Fries, Shake
#   Subtotal : ₹ 450.00
#   Discount : 15%  → -₹ 67.50
#   After discount: ₹ 382.50
#   Service (10%): ₹  38.25
#   TOTAL    : ₹ 420.75
#   Note     : Birthday treat
#   ====================================
#
# Hint: for key, val in extras.items(): handle each extra separately.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "Snehith Python 90", "Alice Java 85"

# Q2: "Hello, John Doe"; missing arg → TypeError; too many → TypeError

# Q3: "Snehith is 22 from Hyderabad"; "22 is Hyderabad from Snehith"

# Q4: "Python Crash Course by Eric (2023)"; "Clean Code by Martin (2020)"; "Fluent Python by Ramalho (2022)"

# Q5: SyntaxError — keyword arg before positional arg. Fix: show(1, 2, 3) or show(a=1, b=2, c=3)

# Q7: "Alice Python 5000"; "Bob Java 5000"; "Charlie C++ 8000"; "Dave Python 6000"

# Q8: SyntaxError: non-default argument follows default argument
#     Fix: def fixed(age, name="Unknown"):

# Q9: 9, 27, 25, 1024

# Q10: <class 'tuple'>, (10,20,30); <class 'tuple'>, ('a','b'); <class 'tuple'>, ()

# Q11: Sum: 60; Sum: 15; Sum: 100

# Q13: <class 'dict'>, {'name':'Snehith','age':22}; {'course':'Python','marks':90}; {}

# Q14:
# name : Alice
# role : Developer
# city : Hyderabad

# Q15: <class 'dict'>; "Bob"

# Q16:
# example(1)           → a:1, b:10, args:(), kwargs:{}
# example(1,2)         → a:1, b:2, args:(), kwargs:{}
# example(1,2,3,4,x=5,y=6) → a:1, b:2, args:(3,4), kwargs:{'x':5,'y':6}

# BONUS 3:
# 1 2 () {}
# 1 3 () {}
# 1 3 (5, 7) {}
# 1 3 (5,) {'x': 9, 'y': 11}


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: D   Q_MCQ_3: C   Q_MCQ_4: D
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: tuple
# FIB_2: dict
# FIB_3: after
# FIB_4: 1;  2;  (3,);  {'x':9}
# FIB_5: list/positional
# FIB_6: dict/keyword
# FIB_7: default

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# def place_order(customer_name, *items, table=1, **extras):
#     price_each = 150
#     subtotal   = len(items) * price_each
#     discount   = extras.get("discount", 0)
#     after_disc = subtotal * (1 - discount/100)
#     service    = after_disc * 0.10
#     total      = after_disc + service
#     print("=" * 36)
#     print(f"Customer : {customer_name:<12}  Table: {table}")
#     print(f"Items    : {', '.join(items)}")
#     print(f"Subtotal : ₹ {subtotal:>7.2f}")
#     if discount:
#         print(f"Discount : {discount}%  → -₹ {subtotal*discount/100:.2f}")
#         print(f"After discount: ₹ {after_disc:.2f}")
#     print(f"Service (10%): ₹ {service:>6.2f}")
#     print(f"TOTAL    : ₹ {total:>7.2f}")
#     if "note" in extras: print(f"Note     : {extras['note']}")
#     if "spicy" in extras: print("🌶 Spicy order!")
#     print("=" * 36)
#
# place_order("Snehith", "Biryani", "Lassi")
# place_order("Priya", "Dosa", "Coffee", table=5, spicy=True)
# place_order("Raj","Burger","Fries","Shake",table=3,discount=15,note="Birthday treat")

