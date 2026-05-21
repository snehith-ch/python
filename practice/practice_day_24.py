# ============================================================
# PRACTICE — Day 24: Types of Variables
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Instance Variables
# --------------------------------------------------

# Q1. Predict — each object gets its OWN copy:

class Student:
    def __init__(self, name, marks):
        self.name = name       # instance variable
        self.marks = marks     # instance variable

s1 = Student("Alice", 90)
s2 = Student("Bob", 75)

print(s1.name)     # prediction:
print(s2.name)     # prediction:
print(s1.marks)    # prediction:
print(s2.marks)    # prediction:


# Q2. Modifying one object's instance variable — predict:

s1.marks = 95
print(s1.marks)    # prediction:
print(s2.marks)    # prediction (should s2 change?):


# Q3. Instance variables can be added outside __init__ — predict:

class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Rex")
d.age = 3          # adding instance variable outside __init__

print(d.name)      # prediction:
print(d.age)       # prediction:

d2 = Dog("Max")
# print(d2.age)    # uncomment → prediction (error?):


# --------------------------------------------------
# SECTION 2: Static (Class) Variables
# --------------------------------------------------

# Q4. Predict — static variable is SHARED across all objects:

class Circle:
    pi = 3.14159    # static variable — belongs to class

    def __init__(self, radius):
        self.radius = radius    # instance variable

    def area(self):
        return Circle.pi * self.radius ** 2

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi)   # prediction: access via class name
print(c1.pi)       # prediction: access via object (also works)
print(c1.area())   # prediction (approx):
print(c2.area())   # prediction (approx):


# Q5. Changing static variable — predict who is affected:

class Counter:
    count = 0    # static variable

    def __init__(self):
        Counter.count += 1

c1 = Counter()
print(Counter.count)    # prediction:
c2 = Counter()
print(Counter.count)    # prediction:
c3 = Counter()
print(Counter.count)    # prediction:


# Q6. Tricky: instance variable shadows static variable — predict:

class Foo:
    x = 10    # static

    def change(self):
        self.x = 99    # creates instance variable! doesn't change static

f1 = Foo()
f2 = Foo()

print(f1.x)       # prediction: reads static
f1.change()
print(f1.x)       # prediction: now reads instance variable
print(f2.x)       # prediction: f2 unchanged, still reads static
print(Foo.x)      # prediction: class variable unchanged


# --------------------------------------------------
# SECTION 3: Local Variables
# --------------------------------------------------

# Q7. Local variables — predict the error:

class Calculator:
    def add(self, a, b):
        result = a + b    # local variable — exists only inside add()
        return result

calc = Calculator()
print(calc.add(3, 4))    # prediction:
# print(result)           # uncomment → prediction (error?):


# Q8. Predict — local vs instance:

class Temp:
    def __init__(self):
        self.x = 100    # instance variable

    def process(self):
        x = 200         # local variable (shadows self.x inside method)
        print(x)        # prediction:
        print(self.x)   # prediction:

t = Temp()
t.process()


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q9. Define a class Employee:
#   - Static variable: company = "TechCorp"
#   - Instance variables: name, salary
#   - Method display(): prints company, name, salary
# Create 2 employees. Change the company name via class name.
# Verify both employees see the new company name.

# YOUR CODE HERE:


# Q10. Predict then verify — delete a static variable:

class Config:
    debug = True
    version = "1.0"

print(Config.debug)        # prediction:
del Config.debug
# print(Config.debug)       # uncomment → prediction (error?):
print(Config.version)      # prediction (still accessible?):


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict ALL output:

class Example:
    val = "class_val"

    def __init__(self):
        self.val = "instance_val"

    def show(self):
        val = "local_val"
        print(val)          # prediction:
        print(self.val)     # prediction:
        print(Example.val)  # prediction:

e = Example()
e.show()


# BONUS 2:
# Create a class BankAccount with:
#   - Static: bank_name = "National Bank", interest_rate = 0.05
#   - Instance: owner, balance
#   - Method annual_interest(): returns balance * interest_rate
# Change interest_rate to 0.07 via class name.
# Create 2 accounts and verify both use the new rate.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: Alice, Bob, 90, 75

# Q2: 95, 75 (s2 is not affected — each has its own copy)

# Q3: Rex, 3
#     AttributeError: 'Dog' object has no attribute 'age' (d2 has no .age)

# Q4: 3.14159, 3.14159, 78.53975, 314.159

# Q5: 1, 2, 3

# Q6: 10 (reads static), 99 (reads instance — shadowed), 10 (f2 still reads static), 10 (class unchanged)

# Q7: 7
#     NameError: name 'result' is not defined (local variable gone after method ends)

# Q8: 200 (local), 100 (instance — self.x unchanged)

# Q10: True, AttributeError after del Config.debug, "1.0"

# BONUS 1: local_val, instance_val, class_val
