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
