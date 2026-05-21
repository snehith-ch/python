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
