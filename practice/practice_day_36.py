# ============================================================
# PRACTICE — Day 36: Binary Files — Pickling and Unpickling
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: pickle Basics
# --------------------------------------------------

# Q1. Pickle a simple value — predict:

import pickle

# Pickle a list
data = [10, 20, 30, 40, 50]
with open("data.dat", "wb") as f:
    pickle.dump(data, f)
print("Pickled")    # prediction:

# Unpickle it
with open("data.dat", "rb") as f:
    restored = pickle.load(f)

print(restored)       # prediction:
print(type(restored)) # prediction:


# Q2. Pickle vs text file — what file mode do you use?

# For pickling:   mode = ?
# For unpickling: mode = ?

# YOUR ANSWERS:


# Q3. What does the .dat file look like if you open it in a text editor?

# a) Readable Python code
# b) Binary/garbled characters — unreadable
# c) JSON format

# YOUR ANSWER:


# --------------------------------------------------
# SECTION 2: Pickling Objects
# --------------------------------------------------

# Q4. Pickle a class instance — predict:

import pickle

class Employee:
    def __init__(self, emp_no, name, address):
        self.emp_no = emp_no
        self.name = name
        self.address = address

    def display(self):
        print(self.emp_no, self.name, self.address)

# Pickle
e = Employee(101, "Sita", "HYD")
with open("emp.dat", "wb") as f:
    pickle.dump(e, f)
print("Employee pickled")   # prediction:

# Unpickle
with open("emp.dat", "rb") as f:
    obj = pickle.load(f)

print(type(obj))     # prediction (what class?):
obj.display()        # prediction:
print(obj.name)      # prediction:


# Q5. Pickle stores complete object state — predict:

import pickle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3, 4)
with open("point.dat", "wb") as f:
    pickle.dump(p, f)

with open("point.dat", "rb") as f:
    p2 = pickle.load(f)

print(p2.x)           # prediction:
print(p2.y)           # prediction:
print(p2.distance())  # prediction:


# --------------------------------------------------
# SECTION 3: Multiple Objects
# --------------------------------------------------

# Q6. Pickle multiple objects — predict:

import pickle

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

items = [Item("Apple", 50), Item("Banana", 20), Item("Mango", 80)]

with open("items.dat", "wb") as f:
    for item in items:
        pickle.dump(item, f)   # dump one by one

print("All pickled")   # prediction:

# Unpickle all — use loop until EOFError
with open("items.dat", "rb") as f:
    while True:
        try:
            obj = pickle.load(f)
            print(obj.name, obj.price)    # prediction (3 lines):
        except EOFError:
            break    # end of file reached


# Q7. Pickling a dictionary — predict:

import pickle

student = {
    "name": "Alice",
    "marks": [90, 85, 92],
    "grade": "A"
}

with open("student.dat", "wb") as f:
    pickle.dump(student, f)

with open("student.dat", "rb") as f:
    data = pickle.load(f)

print(data)              # prediction:
print(data["name"])      # prediction:
print(sum(data["marks"])) # prediction:


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q8. Create a class Book with title, author, pages.
#   - Pickle 3 Book objects to "books.dat" (one by one)
#   - Unpickle all and print each book's details

# YOUR CODE HERE:


# Q9. Write code that:
#   a) Pickles a list of 5 favorite movies to "movies.dat"
#   b) Unpickles and prints each movie name

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — pickle stores the TYPE of the object:

import pickle

x = 42
y = 3.14
z = "hello"

with open("mixed.dat", "wb") as f:
    pickle.dump(x, f)
    pickle.dump(y, f)
    pickle.dump(z, f)

with open("mixed.dat", "rb") as f:
    a = pickle.load(f)
    b = pickle.load(f)
    c = pickle.load(f)

print(type(a), a)    # prediction:
print(type(b), b)    # prediction:
print(type(c), c)    # prediction:


# BONUS 2: What happens if you try to pickle a file object or database connection?

# import pickle
# f = open("test.txt", "w")
# pickle.dump(f, open("bad.dat", "wb"))    # prediction (error?):

# Answer: Some objects (file handles, DB connections, lambdas) are NOT picklable.
# They raise: TypeError: cannot pickle '_io.TextIOWrapper' object


# BONUS 3:
# Demonstrate "without pickling → data lost":
# Create an Employee object, print it, then simulate "program restart"
# by reassigning the variable to None.
# Then use pickling to save and restore the same employee.

# YOUR CODE HERE:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Which module serializes Python objects to binary files?
#    A) json    B) csv    C) pickle    D) struct
# Answer: ___

# Q_MCQ_2. pickle.dump(obj, file)  requires the file to be opened with:
#    A) "w"    B) "wb"    C) "r"    D) "rb"
# Answer: ___

# Q_MCQ_3. pickle.load(file)  requires the file to be opened with:
#    A) "r"    B) "rb"    C) "w"    D) "wb"
# Answer: ___

# Q_MCQ_4. What is "pickling"?
#    A) Compressing a file    B) Converting Python object → bytes
#    C) Encrypting data    D) Sorting a list
# Answer: ___

# Q_MCQ_5. Compared to JSON, pickle can store:
#    A) Only strings    B) Only numbers
#    C) Any Python object including custom classes    D) Only lists/dicts
# Answer: ___

# Q_MCQ_6. To append a new pickled object to an existing binary file:
#    A) "w"    B) "ab"    C) "rb"    D) "xb"
# Answer: ___

# Q_MCQ_7. Reading a pickle file from an untrusted source is dangerous because:
#    A) It is too slow    B) It can execute arbitrary code during unpickling
#    C) It corrupts the file    D) Python does not support it
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. import _______ to use Python's binary serialization module.

# FIB_2. pickle._______(object, file)  serializes an object to a binary file.

# FIB_3. The reverse operation of pickling is called _______.

# FIB_4. Pickle can store _______ Python objects, including custom class instances.

# FIB_5. To open a file for binary reading: open("data.pkl", "_______").

# FIB_6. JSON stores data as _______, while pickle stores as _______.

# FIB_7. pickle.dumps(obj) returns the pickled object as _______ (not writing
#         to a file).


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Student Database with Pickle — persist student records.
#
# Requirements:
#   1. Create a Student class with: name, age, marks (list of 3 subjects)
#      and a method  average() -> float
#   2. Create a list of 5 Student objects
#   3. Pickle the list to "students.pkl"
#   4. Load the list back from "students.pkl" (unpickle)
#   5. Display each student's name and average mark
#   6. Add one more student, re-pickle the updated list
#   7. Verify by loading and printing the count
#
# Expected output:
#   Saved 5 students to students.pkl
#   === Loaded Students ===
#   Alice  : avg = 85.3
#   Bob    : avg = 72.0
#   ...
#   Added Carol. Total: 6 students in students.pkl
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "Pickled", [10, 20, 30, 40, 50], <class 'list'>

# Q2: Pickle mode = "wb" (write binary); Unpickle mode = "rb" (read binary)

# Q3: b) Binary/garbled characters — unreadable in a text editor

# Q4: "Employee pickled", <class '__main__.Employee'>, 101 Sita HYD, Sita

# Q5: 3, 4, 5.0

# Q6: "All pickled", "Apple 50", "Banana 20", "Mango 80"

# Q7: {'name': 'Alice', 'marks': [90, 85, 92], 'grade': 'A'}, Alice, 267

# BONUS 1: <class 'int'> 42, <class 'float'> 3.14, <class 'str'> hello

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: C   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: pickle
# FIB_2: dump
# FIB_3: unpickling  (deserializing)
# FIB_4: any / all
# FIB_5: "rb"
# FIB_6: human-readable text; binary bytes
# FIB_7: a bytes object

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import pickle
#
# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name; self.age = age; self.marks = marks
#     def average(self):
#         return sum(self.marks) / len(self.marks)
#
# students = [
#     Student("Alice", 20, [90, 85, 81]),
#     Student("Bob",   21, [70, 75, 71]),
#     Student("Carol", 22, [88, 92, 95]),
#     Student("David", 20, [60, 65, 58]),
#     Student("Eve",   21, [77, 80, 83]),
# ]
# with open("students.pkl", "wb") as f:
#     pickle.dump(students, f)
# print(f"Saved {len(students)} students to students.pkl")
#
# with open("students.pkl", "rb") as f:
#     loaded = pickle.load(f)
# print("=== Loaded Students ===")
# for s in loaded:
#     print(f"{s.name:<8}: avg = {s.average():.1f}")
#
# loaded.append(Student("Frank", 23, [88, 91, 87]))
# with open("students.pkl", "wb") as f:
#     pickle.dump(loaded, f)
# with open("students.pkl", "rb") as f:
#     final = pickle.load(f)
# print(f"Added Frank. Total: {len(final)} students in students.pkl")

