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




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. In OOP, a CLASS is best described as:
#    A) An instance of a blueprint    B) A blueprint for creating objects
#    C) A function that creates data  D) A module of related functions
# Answer: ___

# Q_MCQ_2. What does  __init__  do?
#    A) Destroys the object    B) Automatically runs when an object is created
#    C) Returns the object     D) Imports the class
# Answer: ___

# Q_MCQ_3. What does  self  refer to?
#    A) The class itself    B) The current instance (object)
#    C) The parent class    D) The module
# Answer: ___

# Q_MCQ_4. Class names in Python should use:
#    A) snake_case    B) ALL_CAPS    C) PascalCase    D) camelCase
# Answer: ___

# Q_MCQ_5. obj1 = Student("Alice"); obj2 = Student("Bob")
#           Do obj1 and obj2 share the same data?
#    A) Yes — they share the same instance variables
#    B) No — each object has its own copy of instance variables
#    C) Only if defined with class variables
#    D) Yes — they share self
# Answer: ___

# Q_MCQ_6. How do you call the method  display()  of object  book1?
#    A) display(book1)    B) Book.display()
#    C) book1.display()   D) self.display()
# Answer: ___

# Q_MCQ_7. self.title = title  inside __init__ creates:
#    A) A class variable    B) A local variable
#    C) An instance variable    D) A global variable
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. class _______ keyword defines a class in Python.

# FIB_2. __init__ is called the _______ method.

# FIB_3. The first parameter of every instance method must be _______.

# FIB_4. Student("Alice", 20) creates an _______ of the Student class.

# FIB_5. Class naming convention: use _______ (e.g., BankAccount, not bank_account).

# FIB_6. self.name = name  stores name as an _______ variable.

# FIB_7. You can create _______ objects from a single class, each with
#         independent data.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Library Book Management System.
#
# Requirements:
#   Define a  Book  class with:
#   - __init__(self, title, author, pages, is_available=True)
#   - display(self): prints all details in a formatted card
#   - borrow(self): if available, sets is_available=False, prints
#     "📖 Borrowed: {title}"; else prints "❌ Sorry, already borrowed."
#   - return_book(self): sets is_available=True, prints
#     "✅ Returned: {title}"
#   - __str__(self): returns "'{title}' by {author} ({pages} pages)"
#
# Then:
#   1. Create 3 Book objects
#   2. Display all using display()
#   3. Borrow book1; try to borrow it again (show "already borrowed")
#   4. Return book1; borrow it again (works this time)
#   5. Print all using str() to show __str__
#
# Expected output (partial):
#   ================================
#   📚 The Alchemist
#   Author: Paulo Coelho | Pages: 208
#   Status: Available ✓
#   ================================
#   📖 Borrowed: The Alchemist
#   ❌ Sorry, already borrowed.
#   ✅ Returned: The Alchemist
#   📖 Borrowed: The Alchemist

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


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: C
# Q_MCQ_5: B   Q_MCQ_6: C   Q_MCQ_7: C

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: class
# FIB_2: constructor (initializer)
# FIB_3: self
# FIB_4: object / instance
# FIB_5: PascalCase
# FIB_6: instance
# FIB_7: multiple

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# class Book:
#     def __init__(self, title, author, pages, is_available=True):
#         self.title        = title
#         self.author       = author
#         self.pages        = pages
#         self.is_available = is_available
#
#     def display(self):
#         status = "Available ✓" if self.is_available else "Borrowed ✗"
#         print("=" * 32)
#         print(f"📚 {self.title}")
#         print(f"Author: {self.author} | Pages: {self.pages}")
#         print(f"Status: {status}")
#         print("=" * 32)
#
#     def borrow(self):
#         if self.is_available:
#             self.is_available = False
#             print(f"📖 Borrowed: {self.title}")
#         else:
#             print(f"❌ Sorry, '{self.title}' is already borrowed.")
#
#     def return_book(self):
#         self.is_available = True
#         print(f"✅ Returned: {self.title}")
#
#     def __str__(self):
#         return f"'{self.title}' by {self.author} ({self.pages} pages)"
#
# b1 = Book("The Alchemist", "Paulo Coelho", 208)
# b2 = Book("Atomic Habits", "James Clear", 320)
# b3 = Book("Python Crash Course", "Eric Matthes", 544)
# for b in [b1, b2, b3]: b.display()
# b1.borrow(); b1.borrow()   # second should say "already borrowed"
# b1.return_book(); b1.borrow()
# for b in [b1, b2, b3]: print(str(b))

