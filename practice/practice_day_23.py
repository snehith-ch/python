# ============================================================
# PRACTICE — Day 23: OOP — Constructor and Method Patterns
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Four Program Structures
# --------------------------------------------------

# Q1. Structure 1: Constructor + Method — predict:

class Employee:
    def __init__(self, emp_no, name, salary):
        self.emp_no = emp_no
        self.name = name
        self.salary = salary

    def display(self):
        print(self.emp_no, self.name, self.salary)

e = Employee(101, "Sita", 50000)
e.display()        # prediction:

e2 = Employee(102, "Ravi", 45000)
e2.display()       # prediction:


# Q2. Structure 2: Constructor only (no method) — predict:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Point: ({self.x}, {self.y})")

p = Point(3, 4)    # prediction: what prints?
# How do you access x after this?
print(p.x)         # prediction:
print(p.y)         # prediction:


# Q3. __dict__ — predict:

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

c = Car("Toyota", 120)
print(c.__dict__)      # prediction (format):
print(type(c.__dict__)) # prediction:


# --------------------------------------------------
# SECTION 2: print Formatting Styles
# --------------------------------------------------

# Q4. Predict identical outputs — 4 ways to print:

name = "Ali"
age = 28
salary = 35000.5

# Style 1: comma-separated
print(name, age, salary)           # prediction:

# Style 2: \n in string
print(name + "\n" + str(age) + "\n" + str(salary))   # prediction:

# Style 3: .format()
print("{} {} {}".format(name, age, salary))           # prediction:

# Style 4: f-string
print(f"{name} {age} {salary}")                       # prediction:


# Q5. Positional vs keyword format — predict:

print("{0} is {1} years old".format("Bob", 25))       # prediction:
print("{name} earns {amt}".format(name="Sita", amt=60000))  # prediction:
print("{1} is first, {0} is second".format("A", "B"))  # prediction:


# --------------------------------------------------
# SECTION 3: Multiple Objects
# --------------------------------------------------

# Q6. Predict — each object is independent:

class Box:
    def __init__(self, label):
        self.label = label
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        print(f"{self.label}: {self.items}")

b1 = Box("Red Box")
b2 = Box("Blue Box")

b1.add("apple")
b1.add("banana")
b2.add("pen")

b1.show()    # prediction:
b2.show()    # prediction:
print(b1.items is b2.items)   # prediction (same list?):


# Q7. Objects in a list — predict:

class Coin:
    def __init__(self, value):
        self.value = value

coins = [Coin(1), Coin(2), Coin(5), Coin(10)]
total = 0
for coin in coins:
    total += coin.value

print(total)     # prediction:
print(len(coins))  # prediction:


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q8. Define a class Product:
#   - Constructor: name, price, quantity
#   - Method total_value(): returns price * quantity
#   - Method display(): prints name, price, quantity, and total value
# Create 2 products and call display() on each.

# YOUR CODE HERE:


# Q9. Rewrite this using all four print styles:
# Print: "Employee: Alice, Age: 30, Salary: 75000.0"

name = "Alice"
age = 30
salary = 75000.0

# Style 1 (comma):
# Style 2 (\n or concatenation):
# Style 3 (.format()):
# Style 4 (f-string):


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict:

class Tracker:
    def __init__(self, name):
        self.name = name
        self.log = []

    def record(self, event):
        self.log.append(event)
        return self    # returns self — allows chaining!

t = Tracker("System")
t.record("start").record("login").record("logout")
print(t.log)     # prediction:


# BONUS 2:
# Create a class Inventory with 3 attributes set in constructor.
# Use __dict__ to print all attribute names and values as a loop:
# for key, value in obj.__dict__.items():
#     print(f"{key}: {value}")

# YOUR CODE HERE:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. When you write  obj.display(), Python automatically passes:
#    A) The class    B) The object as self    C) None    D) The module
# Answer: ___

# Q_MCQ_2. Two objects of the same class:
#    A) Share all instance variables    B) Each have their own instance variables
#    C) Must have different method names    D) Cannot exist simultaneously
# Answer: ___

# Q_MCQ_3. __str__(self)  should return:
#    A) None    B) A printable string representation of the object
#    C) The class name    D) The memory address
# Answer: ___

# Q_MCQ_4. Which output format uses placeholders like %s and %d?
#    A) f-string          B) .format() method
#    C) % formatting      D) print() default
# Answer: ___

# Q_MCQ_5. Defining a method OUTSIDE the class body (then assigning it)
#           works in Python — what is this called?
#    A) Monkey patching    B) Inheritance    C) Encapsulation    D) Abstraction
# Answer: ___

# Q_MCQ_6. What is the purpose of a separate display() method vs __str__?
#    A) display() can have complex logic, printing side effects;
#       __str__ just returns a string for str()/print() integration
#    B) No difference
#    C) __str__ is faster
#    D) display() is for subclasses only
# Answer: ___

# Q_MCQ_7. obj1 = Employee(1, "Alice"); obj2 = Employee(2, "Bob")
#           obj2.salary = 50000  — does this affect obj1?
#    A) Yes    B) No — obj2.salary is an instance variable for obj2 only
#    C) Only if salary is a class variable    D) Yes, if both were created from same class
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. self always refers to the _______ that called the method.

# FIB_2. __str__ is called when you use _______ or _______ on an object.

# FIB_3. f"Name: {self.name}" is an _______ string (introduced in Python 3.6).

# FIB_4. Two objects created from the same class share the _______ (methods,
#         class variables) but have separate _______ variables.

# FIB_5. obj.display()  is syntactic sugar for  _______.display(obj).

# FIB_6. To define a method that operates on an instance: the first parameter
#         must be _______.

# FIB_7. "%-10s" % name  prints name _______ in a 10-character wide field.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Employee Directory for an HR system.
#
# Requirements:
#   Define  Employee  class with:
#   - __init__(emp_id, name, department, salary)
#   - display(): print a formatted employee card (borders + aligned fields)
#   - give_raise(percent): update salary, print "Salary: old → new"
#   - promote(new_dept): update department, print "Promoted to: new_dept"
#   - __str__: returns "EmpID:{id} | {name} | {dept} | ₹{salary:,}"
#
#   Then:
#   1. Create 4 employees in different departments
#   2. Give a 15% raise to Employee 1
#   3. Promote Employee 3 to "Engineering"
#   4. Print all employees using display()
#   5. Print all using str() to demonstrate __str__
#   6. Show that modifying one employee does NOT affect others
#
# Expected output (partial):
#   ╔════════════════════════════╗
#   ║ EmpID: E001               ║
#   ║ Name  : Alice Kumar       ║
#   ║ Dept  : Marketing         ║
#   ║ Salary: ₹45,000           ║
#   ╚════════════════════════════╝
#   Salary raised: ₹45,000 → ₹51,750
#   Promoted to: Engineering

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: 101 Sita 50000, 102 Ravi 45000

# Q2: "Point: (3, 4)" printed during object creation, then 3, 4

# Q3: {'brand': 'Toyota', 'speed': 120}, <class 'dict'>

# Q4: Ali 28 35000.5 (all 4 styles give same result)

# Q5: "Bob is 25 years old", "Sita earns 60000", "B is first, A is second"

# Q6: "Red Box: ['apple', 'banana']", "Blue Box: ['pen']", False

# Q7: 18, 4

# BONUS 1: ['start', 'login', 'logout']


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: C
# Q_MCQ_5: A   Q_MCQ_6: A   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: object (instance)
# FIB_2: str();  print()
# FIB_3: f-string
# FIB_4: class structure (methods, class vars);  instance
# FIB_5: ClassName
# FIB_6: self
# FIB_7: left-aligned

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# class Employee:
#     def __init__(self, emp_id, name, department, salary):
#         self.emp_id     = emp_id
#         self.name       = name
#         self.department = department
#         self.salary     = salary
#
#     def display(self):
#         w = 30
#         print("╔" + "═"*w + "╗")
#         print(f"║ EmpID : {self.emp_id:<{w-9}}║")
#         print(f"║ Name  : {self.name:<{w-9}}║")
#         print(f"║ Dept  : {self.department:<{w-9}}║")
#         print(f"║ Salary: ₹{self.salary:<{w-10},}║")
#         print("╚" + "═"*w + "╝")
#
#     def give_raise(self, percent):
#         old = self.salary
#         self.salary = int(old * (1 + percent/100))
#         print(f"Salary raised: ₹{old:,} → ₹{self.salary:,}")
#
#     def promote(self, new_dept):
#         self.department = new_dept
#         print(f"Promoted to: {new_dept}")
#
#     def __str__(self):
#         return f"EmpID:{self.emp_id} | {self.name} | {self.department} | ₹{self.salary:,}"
#
# e1 = Employee("E001","Alice Kumar","Marketing",45000)
# e2 = Employee("E002","Bob Singh","Finance",55000)
# e3 = Employee("E003","Priya Rao","HR",48000)
# e4 = Employee("E004","Raj Patel","Sales",42000)
# e1.give_raise(15); e3.promote("Engineering")
# for e in [e1,e2,e3,e4]: e.display()
# for e in [e1,e2,e3,e4]: print(str(e))

