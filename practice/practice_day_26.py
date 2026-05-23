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




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. From how many places can a static (class) variable be accessed?
#    A) 1    B) 3    C) 5    D) Unlimited, but 5 main ways are taught
# Answer: ___

# Q_MCQ_2. __del__ is called:
#    A) When you call del obj     B) When the object's reference count reaches 0
#    C) Both A and B — either triggers it    D) Only at program end
# Answer: ___

# Q_MCQ_3. Python manages memory primarily through:
#    A) Manual malloc/free    B) Reference counting + cyclic GC
#    C) Java-style garbage collection    D) Stack-only allocation
# Answer: ___

# Q_MCQ_4. del obj  in Python:
#    A) Immediately deletes the object from memory
#    B) Removes the name binding; the object is deleted when ref count = 0
#    C) Calls __del__ immediately always    D) Raises an error if obj is referenced elsewhere
# Answer: ___

# Q_MCQ_5. Accessing a static var inside an instance method via self:
#    A) Always changes the class variable    B) Works only if no instance var shadows it
#    C) Raises AttributeError                D) Always creates a new instance variable
# Answer: ___

# Q_MCQ_6. What happens to a local variable's object when the function returns?
#    A) It stays in memory forever    B) Its reference count decreases; GC may collect it
#    C) It's immediately freed        D) It becomes a global variable
# Answer: ___

# Q_MCQ_7. Which is TRUE about  __del__?
#    A) It's guaranteed to run at a specific time
#    B) It may not run if circular references exist without gc.collect()
#    C) It runs exactly when del is called
#    D) It returns the freed memory
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. 5 ways to access a static variable: self.___, ClassName.___,
#         cls.___ (in classmethod), ClassName.___ (outside), obj.___ (outside).

# FIB_2. __del__ is called the _______ method (opposite of constructor).

# FIB_3. Python's GC uses _______ counting as its primary mechanism.

# FIB_4. When an object's reference count drops to _______, Python frees the memory.

# FIB_5. import gc; gc.collect()  manually triggers the _______ garbage collector.

# FIB_6. del x  removes the _______ binding, not necessarily the object.

# FIB_7. A local variable inside a function gets destroyed when
#         the function _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Resource Manager with lifecycle tracking using __del__.
#
# Requirements:
#   Define  FileResource  class:
#   - Class variable: open_files = 0
#   - __init__(filename): increment open_files, store filename,
#     print "📂 Opening: {filename}"
#   - read(): print "Reading from {filename}..."
#   - __del__: decrement open_files, print "🔒 Closing: {filename}"
#   - classmethod get_open_count(): returns open_files
#
# Then:
#   1. Create 3 FileResource objects; print open count
#   2. Read from all 3
#   3. Delete one explicitly using del — observe __del__ print
#   4. Print open count again (should be 2)
#   5. Define a function create_temp():
#      r = FileResource("temp.log"); r.read(); return "done"
#      Call it — the temp resource goes out of scope when function returns
#   6. Call gc.collect() and print open count at the end
#
# Expected output:
#   📂 Opening: data.csv
#   📂 Opening: config.json
#   📂 Opening: log.txt
#   Open files: 3
#   Reading from data.csv...
#   🔒 Closing: data.csv
#   Open files: 2
#   📂 Opening: temp.log
#   Reading from temp.log...
#   🔒 Closing: temp.log  (when function returns)

# YOUR CODE HERE:


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


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: C   Q_MCQ_2: C   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: attribute_name (same name each time)
# FIB_2: destructor
# FIB_3: reference
# FIB_4: 0
# FIB_5: cyclic (generational)
# FIB_6: name / variable
# FIB_7: returns (exits)

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import gc
# class FileResource:
#     open_files = 0
#     def __init__(self, filename):
#         FileResource.open_files += 1
#         self.filename = filename
#         print(f"📂 Opening: {filename}")
#     def read(self):
#         print(f"Reading from {self.filename}...")
#     def __del__(self):
#         FileResource.open_files -= 1
#         print(f"🔒 Closing: {self.filename}")
#     @classmethod
#     def get_open_count(cls): return cls.open_files
#
# r1 = FileResource("data.csv")
# r2 = FileResource("config.json")
# r3 = FileResource("log.txt")
# print(f"Open files: {FileResource.get_open_count()}")
# for r in [r1, r2, r3]: r.read()
# del r1
# print(f"Open files: {FileResource.get_open_count()}")
#
# def create_temp():
#     r = FileResource("temp.log"); r.read(); return "done"
# create_temp()
# gc.collect()
# print(f"Final open files: {FileResource.get_open_count()}")

