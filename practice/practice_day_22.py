# ============================================================
# PRACTICE — Day 22: OOP Introduction
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Class and Object Basics
# --------------------------------------------------

# Q1. Predict the output:

class Dog:
    def bark(self):
        print("Woof!")

    def info(self, name, breed):
        print(f"Name: {name}, Breed: {breed}")

d = Dog()
print(type(d))        # prediction:
d.bark()              # prediction:
d.info("Rex", "Lab")  # prediction:


# Q2. How many objects can be created from one class?

class Car:
    def drive(self):
        print("Vroom!")

c1 = Car()
c2 = Car()
c3 = Car()

print(c1 is c2)       # prediction (same object?):
c1.drive()            # prediction:
c2.drive()            # prediction:


# --------------------------------------------------
# SECTION 2: __init__ Constructor
# --------------------------------------------------

# Q3. Predict the output:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} is {self.age} years old")

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

p1.display()          # prediction:
p2.display()          # prediction:
print(p1.name)        # prediction:
print(p2.age)         # prediction:


# Q4. Predict — what happens if constructor arguments are missing?

# p3 = Person("Charlie")   # uncomment → prediction (error?):


# Q5. Predict the output — constructor runs automatically:

class Counter:
    def __init__(self):
        print("Counter created!")
        self.count = 0

    def increment(self):
        self.count += 1
        print(f"Count: {self.count}")

c = Counter()          # prediction: what prints here?
c.increment()          # prediction:
c.increment()          # prediction:


# --------------------------------------------------
# SECTION 3: self parameter
# --------------------------------------------------

# Q6. Predict — each object has its own data:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show(self):
        print(f"{self.owner}: Rs.{self.balance}")

acc1 = BankAccount("Sita", 10000)
acc2 = BankAccount("Ravi", 5000)

acc1.show()            # prediction:
acc2.show()            # prediction:

acc1.deposit(2000)
acc1.show()            # prediction:
acc2.show()            # prediction (acc2 unchanged?):


# Q7. Trace the execution — predict each print:

class Point:
    def __init__(self, x, y):
        print(f"Creating point ({x}, {y})")
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3, 4)        # prediction:
print(p.distance_from_origin())    # prediction:


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q8. Define a class Rectangle with:
#   - Constructor: width, height
#   - Method area(): returns width * height
#   - Method perimeter(): returns 2 * (width + height)
#   - Method display(): prints both area and perimeter
# Create one Rectangle(5, 3) and call display().

# YOUR CODE HERE:


# Q9. Define a class Student with:
#   - Constructor: name, marks (a list of 3 numbers)
#   - Method average(): returns the average of marks
#   - Method result(): prints "Pass" if average >= 40, else "Fail"
# Create two students and call result() on each.

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict the output (tricky!):

class Foo:
    def __init__(self):
        self.x = 10

    def double(self):
        self.x *= 2
        return self.x

f = Foo()
print(f.double())     # prediction:
print(f.double())     # prediction:
print(f.x)            # prediction:


# BONUS 2:
# Create a class Temperature with:
#   - Constructor takes celsius value
#   - Method to_fahrenheit(): returns (celsius * 9/5) + 32
#   - Method to_kelvin(): returns celsius + 273.15
# Create Temperature(100) and print both conversions.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: <class '__main__.Dog'>, Woof!, Name: Rex, Breed: Lab

# Q2: False (different objects), Vroom!, Vroom!

# Q3: Alice is 25 years old, Bob is 30 years old, Alice, 30

# Q4: TypeError: __init__() missing 1 required positional argument: 'age'

# Q5: "Counter created!" (printed when c = Counter()), Count: 1, Count: 2

# Q6: Sita: Rs.10000, Ravi: Rs.5000, Sita: Rs.12000, Ravi: Rs.5000 (unchanged)

# Q7: "Creating point (3, 4)", 5.0

# BONUS 1: 20, 40, 40
