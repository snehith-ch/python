# ============================================================
# PRACTICE — Day 28: Inheritance
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Single Inheritance
# --------------------------------------------------

# Q1. Predict — child inherits parent methods:

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} breathes")

    def eat(self):
        print(f"{self.name} eats")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

d = Dog("Rex")
d.breathe()       # prediction (from parent):
d.eat()           # prediction (from parent):
d.bark()          # prediction (own method):
print(d.name)     # prediction:


# Q2. Child constructor vs parent — predict:

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle: {brand}")

    def start(self):
        print(f"{self.brand} started")

class Car(Vehicle):
    def __init__(self, brand, seats):
        Vehicle.__init__(self, brand)    # call parent constructor
        self.seats = seats
        print(f"Car with {seats} seats")

    def honk(self):
        print("Beep!")

c = Car("Toyota", 5)    # prediction (2 lines):
c.start()               # prediction:
c.honk()                # prediction:


# Q3. isinstance() and issubclass() — predict:

class Shape:
    pass

class Circle(Shape):
    pass

class Square(Shape):
    pass

c = Circle()

print(isinstance(c, Circle))    # prediction:
print(isinstance(c, Shape))     # prediction (parent class?):
print(isinstance(c, Square))    # prediction (sibling class?):

print(issubclass(Circle, Shape))   # prediction:
print(issubclass(Shape, Circle))   # prediction (reverse?):


# --------------------------------------------------
# SECTION 2: Multilevel Inheritance
# --------------------------------------------------

# Q4. Predict — chain of inheritance:

class Grandparent:
    def g_method(self):
        print("Grandparent method")

class Parent(Grandparent):
    def p_method(self):
        print("Parent method")

class Child(Parent):
    def c_method(self):
        print("Child method")

obj = Child()
obj.c_method()     # prediction:
obj.p_method()     # prediction (from parent):
obj.g_method()     # prediction (from grandparent):


# Q5. Multilevel with data — predict:

class A:
    def __init__(self):
        self.a = "A"

class B(A):
    def __init__(self):
        A.__init__(self)
        self.b = "B"

class C(B):
    def __init__(self):
        B.__init__(self)
        self.c = "C"

obj = C()
print(obj.a)    # prediction:
print(obj.b)    # prediction:
print(obj.c)    # prediction:
print(obj.__dict__)   # prediction:


# --------------------------------------------------
# SECTION 3: Hierarchical Inheritance
# --------------------------------------------------

# Q6. Predict — one parent, multiple children:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        Employee.__init__(self, name, salary)
        self.team_size = team_size

    def info(self):
        self.display()
        print(f"Team size: {self.team_size}")

class Intern(Employee):
    def __init__(self, name, salary, duration):
        Employee.__init__(self, name, salary)
        self.duration = duration

    def info(self):
        self.display()
        print(f"Internship duration: {self.duration} months")

m = Manager("Alice", 80000, 10)
i = Intern("Bob", 15000, 6)

m.info()    # prediction (2 lines):
i.info()    # prediction (2 lines):

print(isinstance(m, Employee))    # prediction:
print(isinstance(i, Manager))     # prediction:


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q7. Build a class hierarchy:
#   - Animal: name, sound (instance vars), speak() prints "{name} says {sound}"
#   - Cat(Animal): constructor adds color; purr() prints "{name} purrs"
#   - Kitten(Cat): constructor adds weight; tiny() prints "{name} is a tiny {weight}kg kitten"
# Create a Kitten and call speak(), purr(), and tiny().

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict ALL output:

class X:
    def hello(self):
        print("X.hello")

class Y(X):
    def hello(self):
        print("Y.hello")    # overrides X.hello

class Z(Y):
    pass    # no hello — inherits from Y

z = Z()
z.hello()               # prediction (X or Y?):
print(isinstance(z, X)) # prediction:
print(isinstance(z, Y)) # prediction:


# BONUS 2:
# Use issubclass() to check a 3-level hierarchy:
# class A → class B(A) → class C(B)
# Predict: issubclass(C, A), issubclass(A, C), issubclass(C, B)

class A: pass
class B(A): pass
class C(B): pass

print(issubclass(C, A))    # prediction:
print(issubclass(A, C))    # prediction:
print(issubclass(C, B))    # prediction:
print(issubclass(B, A))    # prediction:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "{Rex} breathes", "{Rex} eats", "{Rex} barks", "Rex"

# Q2: "Vehicle: Toyota", "Car with 5 seats", "{Toyota} started", "Beep!"

# Q3: True, True, False, True, False

# Q4: "Child method", "Parent method", "Grandparent method"

# Q5: "A", "B", "C", {'a': 'A', 'b': 'B', 'c': 'C'}

# Q6: "Name: Alice, Salary: 80000", "Team size: 10",
#     "Name: Bob, Salary: 15000", "Internship duration: 6 months"
#     True, False (i is Intern, not Manager)

# BONUS 1: "Y.hello" (Y overrides X; Z inherits from Y), True, True

# BONUS 2: True, False, True, True
