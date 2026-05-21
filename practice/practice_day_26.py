# ============================================================
# PRACTICE — Day 26: Static Variables, GC, and Destructor
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Static Variable Access (5 Places)
# --------------------------------------------------

# Q1. Predict — 5 ways to access a static variable:

class School:
    name = "ABC School"    # static variable

    def __init__(self):
        print(School.name)         # Place 1: inside __init__ via class name

    def show(self):
        print(School.name)         # Place 2: inside instance method via class name

    @classmethod
    def class_show(cls):
        print(cls.name)            # Place 3: inside class method via cls

    @staticmethod
    def static_show():
        print(School.name)         # Place 4: inside static method via class name

s = School()             # prediction (prints during creation):
s.show()                 # prediction:
School.class_show()      # prediction:
School.static_show()     # prediction:
print(School.name)       # prediction (Place 5: outside class via class name):


# Q2. Deleting a static variable — predict:

class Config:
    debug = True

print(Config.debug)      # prediction:
del Config.debug
# print(Config.debug)    # uncomment → prediction (error?):


# --------------------------------------------------
# SECTION 2: Static Methods and Class Variables
# --------------------------------------------------

# Q3. Static method CANNOT access class variables directly — predict:

class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def reset():
        Counter.count = 0    # must use class name explicitly

    @staticmethod
    def show():
        print(Counter.count)

Counter.increment()
Counter.increment()
Counter.show()        # prediction:
Counter.reset()
Counter.show()        # prediction:


# --------------------------------------------------
# SECTION 3: Garbage Collector
# --------------------------------------------------

# Q4. Predict the output — GC module:

import gc

print(gc.isenabled())    # prediction (GC on by default?):
gc.disable()
print(gc.isenabled())    # prediction:
gc.enable()
print(gc.isenabled())    # prediction:


# Q5. GC collects objects with no references — trace:

class Box:
    def __init__(self, label):
        self.label = label
        print(f"Box {label} created")

b1 = Box("A")     # prediction:
b2 = Box("B")     # prediction:
b1 = None         # b1 no longer references the object — GC can collect "A"
print("b1 reassigned")
print(b2.label)   # prediction:


# --------------------------------------------------
# SECTION 4: Destructor __del__
# --------------------------------------------------

# Q6. Predict the order of prints:

class Resource:
    def __init__(self, name):
        print(f"Created: {name}")
        self.name = name

    def __del__(self):
        print(f"Destroyed: {self.name}")

r = Resource("FileHandle")   # prediction:
print("Using resource")
r = None                     # prediction (destructor called?):
print("After r = None")


# Q7. Predict — destructor at end of program:

class Logger:
    def __init__(self):
        print("Logger started")

    def __del__(self):
        print("Logger stopped")

log = Logger()     # prediction:
print("Program running")
# destructor runs when program ends or log goes out of scope


# Q8. Objects in a list — when is destructor called?

class Item:
    def __init__(self, n):
        self.n = n

    def __del__(self):
        print(f"Item {self.n} deleted")

items = [Item(1), Item(2), Item(3)]
items.clear()    # prediction: how many destructors called?
print("List cleared")


# --------------------------------------------------
# SECTION 5: Write Code
# --------------------------------------------------

# Q9. Define a class Connection with:
#   - Static variable: max_connections = 5
#   - Instance variable: conn_id
#   - __init__: prints "Connection {id} opened"
#   - __del__: prints "Connection {id} closed"
# Create 2 connections, then set both to None.

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict ALL output — careful with order!

class Managed:
    instances = 0

    def __init__(self, name):
        self.name = name
        Managed.instances += 1
        print(f"Created {name}, total: {Managed.instances}")

    def __del__(self):
        Managed.instances -= 1
        print(f"Destroyed {self.name}, total: {Managed.instances}")

a = Managed("A")   # prediction:
b = Managed("B")   # prediction:
a = None           # prediction:
print(f"Still alive: {Managed.instances}")   # prediction:


# BONUS 2: Why does this NOT raise an error for accessing deleted var?

class Tricky:
    shared = [1, 2, 3]

t = Tricky()
del Tricky.shared     # deletes the class attribute

# But t still has access via instance? Try:
# print(t.shared)     # uncomment → error or not?
# Explanation: after del Tricky.shared, accessing t.shared raises AttributeError


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: All 5 print "ABC School"

# Q2: True, AttributeError: type object 'Config' has no attribute 'debug'

# Q3: 2, 0

# Q4: True, False, True

# Q5: "Box A created", "Box B created", "b1 reassigned", "B"

# Q6: "Created: FileHandle", "Using resource", "Destroyed: FileHandle", "After r = None"

# Q7: "Logger started", "Program running", "Logger stopped" (at program end)

# Q8: "Item 1 deleted", "Item 2 deleted", "Item 3 deleted" — all 3 destructors called

# BONUS 1: "Created A, total: 1", "Created B, total: 2", "Destroyed A, total: 1",
#           "Still alive: 1"
