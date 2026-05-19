# Day 23 — OOP: Constructor vs Method, Program Structures & Print Formatting

← [Day 22](day_22_oop_intro.md) | [Index](00_INDEX.md) | [Day 24](day_24_types_of_variables.md) →

---

## Quick Revision — Day 23

| # | Key Point |
|---|-----------|
| 1 | Constructor: special method, name always `__init__`, runs **once per object** automatically |
| 2 | Method: reusable code, any name, runs **only when called**, can be called many times |
| 3 | `self` is NOT a keyword — any name works, but `self` is the universal convention |
| 4 | Including a constructor is optional; including methods is optional — but one of them is required |
| 5 | `__dict__` on an object returns a dictionary of all its instance variables and values |
| 6 | Putting print inside constructor = no control; inside method = full control per object |
| 7 | `.format()` uses placeholders `{}` or `{0}`, `{1}` for ordered substitution |
| 8 | Multiple objects can be created for one class; constructor runs once for each |
| 9 | Method called without `s.method()` → method never executes |
| 10 | `self` works only inside the class; object reference works outside the class |

---

## Navigation

- **Pre-requisite:** [Day 22](day_22_oop_intro.md) — OOP intro, class/object, constructor and method basics
- **Next:** [Day 24](day_24_types_of_variables.md) — Types of variables in a class (instance, static, local)
- **Related:** [Day 15](day_15_functions_basics.md) — Functions (methods are functions inside a class)

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `test1.py` | Constructor + Method (parameterized) |
| `.py` file | `test2.py` | Only constructor (no method) — shows limitation |
| `.py` file | `test3.py` | Constructor + Method — `__dict__` demo |
| `.py` file | `test4.py` | Only methods (no constructor) — get_data + display |
| Method | `def get_data(self):` | Accept student details at runtime via input() |
| Method | `def display(self):` | Multiple print formatting styles |
| Special attr | `s.__dict__` | Show all instance variables as a dictionary |

---

## 1. Constructor — Full Details

### What Is a Constructor?

```
Constructor — Key Facts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. It is a special method of the class
2. Name is always:  __init__
3. self is the first parameter (mandatory)
4. After self, you can add any other parameters
5. Purpose: to declare and initialize variables
6. Executes automatically when object is created
7. For every object, constructor executes exactly ONCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Constructor Execution Timing

```
s1 = Student(101, "Psi", "Hyd")
       ↑
       Object creation happens here
       ↓
Constructor __init__ fires automatically
       ↓
101 → sid, "Psi" → sname, "Hyd" → saddress
       ↓
Object is ready with initialized values
```

### Multiple Objects — Constructor Runs Once Each

```python
class Student:
    def __init__(self, sid, sname):
        self.sid = sid
        self.sname = sname

s1 = Student(101, "Psi")    # constructor runs → s1 gets 101, "Psi"
s2 = Student(102, "Ram")    # constructor runs → s2 gets 102, "Ram"
s3 = Student(103, "Tom")    # constructor runs → s3 gets 103, "Tom"

# Three objects created → constructor ran exactly 3 times (once per object)
```

---

## 2. Method — Full Details

```
Method — Key Facts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. A reusable piece of code
2. Name can be any valid identifier (display, show, m1, get_data...)
3. self is the first parameter of every method
4. Contains business logic code
5. Executes ONLY when called
6. Can be called any number of times
7. For every object, method can be called many times
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 3. Constructor vs Method — Side-by-Side

| Feature | Constructor | Method |
|---------|------------|--------|
| Name | Always `__init__` | Any valid name |
| When executes | Automatically on object creation | Only when explicitly called |
| Times runs | Once per object | Any number of times |
| Purpose | Initialize variables | Business logic / display / computation |
| First parameter | `self` | `self` |
| Including it | Optional | Optional |

---

## 4. About `self`

### `self` is NOT a keyword

```python
class Student:
    def __init__(x, sid, sname):   # 'x' acts as self
        x.sid = sid
        x.sname = sname

    def display(x):                 # 'x' acts as self
        print(x.sid, x.sname)

s = Student(101, "Psi")
s.display()    # works fine
```

> **Output:** `101 Psi`

> **Instructor warning:** Even though any name works, always use `self`. It is the standard convention. If you skip the first parameter entirely, Python raises:
> `TypeError: display() takes 0 positional arguments but 1 was given`
> (Python silently passes the object as the first argument — you must accept it somewhere.)

### Where `self` Works

```
Inside the class  → use self  (self.sid, self.display())
Outside the class → use object reference (s.sid, s.display())
```

---

## 5. Four Program Structures

### Structure 1 — Constructor + Method (Standard)

```python
class Student:
    def __init__(self, sid, sname, saddress):
        self.sid = sid
        self.sname = sname
        self.saddress = saddress

    def display(self):
        print("Student ID:", self.sid)
        print("Student Name:", self.sname)
        print("Student Address:", self.saddress)


s1 = Student(101, "Psi", "Hyd")
s2 = Student(102, "Ram", "Hyd")

s1.display()
s2.display()
```

**Output:**
```
Student ID: 101
Student Name: Psi
Student Address: Hyd
Student ID: 102
Student Name: Ram
Student Address: Hyd
```

---

### Structure 2 — Only Constructor (No Method) — Shows Limitation

```python
class Student:
    def __init__(self, sid, sname, saddress):
        self.sid = sid
        self.sname = sname
        self.saddress = saddress
        print("Student ID:", self.sid)
        print("Student Name:", self.sname)
        print("Student Address:", self.saddress)


s1 = Student(101, "Psi", "Hyd")
s2 = Student(102, "Ram", "Hyd")
```

**Output:**
```
Student ID: 101
Student Name: Psi
Student Address: Hyd
Student ID: 102
Student Name: Ram
Student Address: Hyd
```

> **Problem:** When print is inside the constructor, it prints **every time an object is created** — you cannot choose to skip printing for a specific object. You have no control.

> **Why method is better:** If display were a method, you could call `s1.display()` without calling `s2.display()` — giving you full flexibility over which object's data to show.

---

### Structure 3 — Constructor Only, Use `__dict__` to Display

When there is no method to display data, use `__dict__`:

```python
class Student:
    def __init__(self, x, y, z):
        self.sid = x
        self.sname = y
        self.saddress = z


s1 = Student(101, "Psi", "Hyd")
s2 = Student(102, "Ram", "Hyd")

print(s1.__dict__)   # {'sid': 101, 'sname': 'Psi', 'saddress': 'Hyd'}
print(s2.__dict__)   # {'sid': 102, 'sname': 'Ram', 'saddress': 'Hyd'}
```

> **`__dict__`** is a special (magic/dunder) attribute that returns all instance variables of an object as a dictionary. Keys are variable names; values are their current values.

> **Note:** Parameter names in the constructor (`x, y, z`) and the field names (`self.sid, self.sname`) do **not** have to match. The assignment maps parameter → field.

---

### Structure 4 — Only Methods (No Constructor)

```python
class Student:
    def get_data(self):
        self.sid = input("Enter Student ID: ")
        self.sname = input("Enter Student Name: ")
        self.saddress = input("Enter Student Address: ")

    def display(self):
        print("Student ID:", self.sid)
        print("Student Name:", self.sname)
        print("Student Address:", self.saddress)


s1 = Student()
s2 = Student()

s1.get_data()
s1.display()

s2.get_data()
s2.display()
```

**Sample run:**
```
Enter Student ID: 1234
Enter Student Name: Psi
Enter Student Address: Hyd
Student ID: 1234
Student Name: Psi
Student Address: Hyd
Enter Student ID: 3435
Enter Student Name: Ram
Enter Student Address: Hyd
Student ID: 3435
Student Name: Ram
Student Address: Hyd
```

> **When to use which:**
> - Use **constructor** for data that should be initialized for **all objects equally** at creation time
> - Use **methods** for data or logic that you want to invoke **selectively** (only for specific objects)

---

## 6. Print Formatting Styles Inside a Method

The instructor showed multiple ways to print data inside a method. All produce the same output — just different coding styles.

### Style 1 — Separate print statements (line by line)

```python
def display(self):
    print("Student ID:", self.sid)
    print("Student Name:", self.sname)
    print("Student Address:", self.saddress)
```

### Style 2 — All on one line with commas

```python
def display(self):
    print(self.sid, self.sname, self.saddress)
```

Output: `101 Psi Hyd`

### Style 3 — Multi-line with `\n` (newline escape)

```python
def display(self):
    print(self.sid, "\n", self.sname, "\n", self.saddress)
```

Output:
```
101
 Psi
 Hyd
```

### Style 4 — Placeholder format with `.format()`

```python
def display(self):
    print("ID: {} Name: {} Address: {}".format(self.sname, self.sid, self.saddress))
```

> **Order matters:** Whatever you pass to `.format()` first fills `{}` first. Here `self.sname` → first `{}`, `self.sid` → second `{}`.

```python
# Example:
print("{} {} {}".format(self.sname, self.sid, self.saddress))
# → Psi 101 Hyd
```

### Style 5 — Index-based placeholder format

```python
def display(self):
    print("{1} {0} {2}".format(self.sname, self.sid, self.saddress))
    #      ↑        ↑
    #    index 0  index 1 — refers to the order in .format()
```

- `{0}` → first argument in `.format()` → `self.sname` = "Psi"
- `{1}` → second argument → `self.sid` = 101
- `{2}` → third argument → `self.saddress` = "Hyd"

Output: `101 Psi Hyd`

> **Note:** The index number in `{0}`, `{1}`, `{2}` refers to the position in `.format()`, not to the variable value. You can reorder them to print in any sequence you want.

### Style 6 — f-string (modern, recommended)

```python
def display(self):
    print(f"ID: {self.sid}  Name: {self.sname}  Address: {self.saddress}")
```

> f-strings (formatted string literals) are the most readable and modern way to format output. They embed expressions directly inside `{}` within the string.

---

## 7. Complete Worked Example — All in One File

```python
# ── Program 1: Constructor + Method (parameterized) ──────────────────
class Student:
    def __init__(self, sid, sname, saddress):
        self.sid = sid
        self.sname = sname
        self.saddress = saddress

    def display(self):
        print(f"ID: {self.sid}  Name: {self.sname}  Address: {self.saddress}")

s1 = Student(101, "Psi", "Hyd")
s2 = Student(102, "Ram", "Hyd")
s1.display()
s2.display()

print()

# ── Program 2: Only Methods ───────────────────────────────────────────
class Employee:
    def get_data(self):
        self.eid = input("Employee ID: ")
        self.ename = input("Employee Name: ")

    def display(self):
        print(f"EID: {self.eid}  Name: {self.ename}")

e1 = Employee()
e1.get_data()
e1.display()
```

---

## Class Walkthrough — Step by Step

**Step 1:** Open PyCharm, right-click the project → New Python File → name it `test1.py`

**Step 2:** Create a class with a default constructor (no parameters)

```python
class Student:
    def __init__(self):
        self.sid = 1234
        self.sname = "Psi"
        self.saddress = "Hyd"

    def display(self):
        print("Student ID:", self.sid)
        print("Student Name:", self.sname)
        print("Student Address:", self.saddress)

s = Student()
s.display()
```

**Step 3:** Observe that both objects show the same data (since constructor has fixed values)

```python
s1 = Student()
s2 = Student()
s1.display()   # same output
s2.display()   # same output
```

**Step 4:** Switch to parameterized constructor to give different data per object

```python
class Student:
    def __init__(self, sid, sname, saddress):
        self.sid = sid
        self.sname = sname
        self.saddress = saddress
    ...
s1 = Student(101, "Psi", "Hyd")
s2 = Student(102, "Ram", "Hyd")
```

**Step 5:** Try removing the method and putting print inside constructor — observe the limitation

**Step 6:** Try with only methods (no constructor) — accept values via `input()` inside `get_data()`

---

## Student Q&A

> **Student Question:** What is the `__dict__` attribute?
> **Answer:** `__dict__` is a special magic attribute available on every object. It returns a Python dictionary where the keys are the instance variable names and the values are their current values. It is useful when you don't have a `display()` method and want to inspect an object's data.

> **Student Question:** If I use `x` instead of `self`, will it work?
> **Answer:** Yes — Python does not enforce the name. Whatever name you give to the first parameter of a constructor or method, Python passes the current object into it. But **always use `self`** — it is the universal Python convention and every Python developer, IDE, and linter expects it.

> **Student Question:** Can I create an object without passing parameters to the constructor?
> **Answer:** Only if the constructor is defined without parameters (or has default values). If the constructor expects parameters, you must supply them at object creation time: `s = Student(101, "Psi", "Hyd")`.

> **Student Question:** Can a method be called any number of times?
> **Answer:** Yes. Unlike the constructor (which runs once per object), a method can be called as many times as needed. For example, you could call `s.display()` five times and it will execute five times.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: __init__() takes 1 positional argument but 4 were given` | Constructor defined only with `self` but you passed 3 extra values | Add parameters to `__init__`: `def __init__(self, sid, sname, saddress)` |
| `AttributeError: 'Student' object has no attribute 'sid'` | Accessing `self.sid` in method but it was never set in constructor | Define `self.sid` inside `__init__` |
| `TypeError: display() takes 0 positional arguments but 1 was given` | `def display():` — missing `self` | Change to `def display(self):` |
| Method not printing anything | Method was never called | Add `s.display()` after object creation |
| `IndexError: Replacement index 3 out of range for positional args tuple` | Used `{3}` in format string but only 3 args passed (index 0,1,2) | Fix the index numbers to match the number of arguments |

---

## Interview Questions

**Q: What is the difference between a constructor and a method in Python?**
A: Constructor (`__init__`) is a special method that runs automatically once when an object is created — used to initialize variables. A method is a user-defined function inside a class with any name, runs only when explicitly called, and can be called any number of times. Both have `self` as their first parameter.

**Q: Is `self` a keyword in Python?**
A: No. `self` is a naming convention, not a keyword. Python passes the current object as the first argument to instance methods — you must accept it, but can name it anything. However, `self` is universally used and you should always follow this convention.

**Q: What is `__dict__` in Python?**
A: `__dict__` is a special attribute on every object that returns a dictionary of all instance variables and their current values. Example: `s.__dict__` returns `{'sid': 101, 'sname': 'Psi'}`.

**Q: Is it mandatory to have both a constructor and methods in a class?**
A: No. A class can have only a constructor, or only methods, or both. However, at least one of them must be present (unless you use `pass` for an empty class body). Including both gives the most flexibility.

**Q: What happens if I don't call a method?**
A: Nothing — the method code never executes. Methods run only when explicitly called using `object.method_name()`. This is unlike constructors, which run automatically.

**Q: What is the difference between `.format()` with and without index numbers?**
A: Without indexes: `"{} {}".format(a, b)` — fills placeholders left to right in order. With indexes: `"{1} {0}".format(a, b)` — `{0}` gets the first argument, `{1}` gets the second. Indexes let you reorder or repeat values.

---

## Try It Yourself

**Exercise 1:** Create a `Book` class with a parameterized constructor accepting `title`, `author`, and `price`. Add a `display()` method that prints these details using f-string formatting. Create 2 book objects.

<details><summary>Answer</summary>

```python
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}  Author: {self.author}  Price: ₹{self.price}")

b1 = Book("Python Basics", "Durga", 500)
b2 = Book("Django Guide", "Ram", 700)
b1.display()
b2.display()
```
</details>

---

**Exercise 2:** Create a `Person` class with only methods (no constructor). Add a `get_info()` method that accepts `name` and `age` from the user via `input()`. Add a `show_info()` method that prints the details. Create 2 Person objects and call both methods.

<details><summary>Answer</summary>

```python
class Person:
    def get_info(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person()
p2 = Person()
p1.get_info()
p1.show_info()
p2.get_info()
p2.show_info()
```
</details>

---

**Exercise 3:** Demonstrate `__dict__`. Create a `Product` class with fields `name`, `price`, and `quantity` initialized in the constructor. Create an object and print its `__dict__`. Then change one field value and print `__dict__` again.

<details><summary>Answer</summary>

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

p = Product("Laptop", 50000, 10)
print(p.__dict__)   # {'name': 'Laptop', 'price': 50000, 'quantity': 10}

p.price = 45000     # update value
print(p.__dict__)   # {'name': 'Laptop', 'price': 45000, 'quantity': 10}
```
</details>

---

**Exercise 4:** Show all three constructor scenarios: (a) constructor with print inside, (b) constructor + separate method. Create 2 objects for each and observe which gives more control over output.

<details><summary>Answer</summary>

```python
# (a) Print inside constructor — no control
class A:
    def __init__(self, x):
        self.x = x
        print("Value:", self.x)   # always prints on creation

a1 = A(10)   # prints automatically
a2 = A(20)   # prints automatically — can't suppress

print()

# (b) Print inside method — full control
class B:
    def __init__(self, x):
        self.x = x

    def display(self):
        print("Value:", self.x)

b1 = B(10)
b2 = B(20)
b1.display()   # choose to print only b1
# b2 is skipped — no output for b2
```
</details>
