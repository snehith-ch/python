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
