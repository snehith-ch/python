# Day 22 — Object-Oriented Programming: Introduction

← [Day 21](day_21_arrays_numpy.md) | [Index](00_INDEX.md) | [Day 23](day_23_oop_constructor_method.md) →

---

## Quick Revision — Day 22

| # | Key Point |
|---|-----------|
| 1 | OOP = Object-Oriented Programming. Python supports structured, functional, and OOP styles |
| 2 | Benefits of OOP: **Security**, **Reusability**, **Application Enhancement** |
| 3 | OOP features (pillars): **Encapsulation**, **Abstraction**, **Polymorphism**, **Inheritance** |
| 4 | **Class** = blueprint / template — a collection of variables and methods |
| 5 | **Object** = instance of a class — used to access the class's variables and methods |
| 6 | Syntax: `class ClassName:` — class name should start with a capital letter (convention) |
| 7 | Object creation: `obj = ClassName()` |
| 8 | **Constructor** = `__init__` — executes automatically when an object is created |
| 9 | **`self`** = special variable referring to the current object; first parameter of every method |
| 10 | Methods must be called explicitly: `obj.method_name()` |

---

## Navigation

- **Pre-requisite:** [Day 21](day_21_arrays_numpy.md) — Arrays and NumPy (last Core Python topic)
- **Next:** [Day 23](day_23_oop_constructor_method.md) — Constructor vs Method, program structures
- **Related:** [Day 15](day_15_functions_basics.md) — Functions (methods are functions inside a class)

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `oop_intro.py` | Basic OOP structure demo |
| Class | `class Student:` | First class definition |
| Constructor | `def __init__(self):` | Initialize student data |
| Method | `def display(self):` | Display student details |
| Object | `s = Student()` | Create an instance of Student |
| Built-in | `help(Student)` | Show class documentation |
| Special attr | `s.__doc__` | Access class docstring |

---

## 1. Python Programming Styles

Python supports three programming paradigms:

```
Python Programming Styles
         |
    _____|______________
    |          |       |
Structured  Functional  Object-Oriented
   (if/for)  (functions)  (classes & objects)
```

Until now, we covered:
- **Structured** — `if`, `for`, `while` (Days 8–9)
- **Functional** — `def`, functions (Days 15–18)

From Day 22 onwards: **Object-Oriented Programming (OOP)**

---

## 2. Why OOP? — Benefits

> **Instructor emphasis:** "This is important — remember these three advantages for interviews."

| Benefit | What it means |
|---------|--------------|
| **Security** | Code written inside a class can be restricted from outside access. Private variables/methods prevent unauthorized modification. |
| **Reusability** | Write logic once in a class, use it many times in your application without rewriting. |
| **Application Enhancement** | Easy to extend existing application code with new features as client requirements grow. |

> **Note:** These are **advantages** of OOP, not the same as its **features** (pillars). The features are encapsulation, abstraction, polymorphism, and inheritance.

---

## 3. OOP Features (The Four Pillars)

```
OOP Features (Pillars)
├── Encapsulation
├── Abstraction
├── Polymorphism
└── Inheritance
```

### 3.1 Encapsulation

> **Definition:** Encapsulation is the process of providing restriction to access variables and methods.

**Why?** To **prevent data from modification** — if someone tries to change your internal variables or method logic, encapsulation can block them.

**How?** By making variables and methods **private**.
- **Public** variables/methods → accessible from anywhere, no restriction
- **Private** variables/methods → accessible only within the same class

```python
class BankAccount:
    def __init__(self):
        self.__balance = 10000   # private variable (double underscore)

    def get_balance(self):       # controlled access
        return self.__balance
```

> Encapsulation = **data hiding + access control**.

### 3.2 Abstraction

> **Definition:** Abstraction is the process of hiding the implementation but providing the service.

**Real-world example 1 — Banking website:**
- You visit `sbi.com` to transfer money
- The website provides a **service** (transfer button)
- You don't see the **implementation** (backend code, database queries)

**Real-world example 2 — Service technician:**
- Your TV breaks; you call a technician
- The technician fixes it but doesn't explain how
- You received the **service**; the implementation is hidden

**In code:** You call a function, get a result — you don't need to know the internal logic.

> Abstraction = **hiding "how", exposing "what"**.

### 3.3 Polymorphism

> **Definition:** Poly = many, Morph = behavior → **Many behaviors from one entity**.

**Real-world example:** A person behaves differently with family, friends, and strangers — same person, different behaviors based on situation.

**In Python:**

```python
# Same operator (+) doing different things:
print(10 + 20)        # 30        — addition
print("Hi" + " there")# "Hi there" — concatenation

# Same method name, different behavior:
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"
```

**Two types of polymorphism:**

| Type | Also Called | Concept |
|------|------------|---------|
| Static Polymorphism | Compile-time polymorphism | **Method Overloading** |
| Dynamic Polymorphism | Runtime polymorphism | **Method Overriding** |

- **Overloading** = same method name, different parameters (refinement)
- **Overriding** = child class replaces parent class method (replacement)

### 3.4 Inheritance

> **Definition:** Inheritance is the process of creating a new class from an existing class.

| Term | Also known as |
|------|--------------|
| Existing class | Parent class / Base class / Super class |
| New class | Child class / Derived class / Sub class |

**Main advantages:** Reusability and Extensibility

Whatever logic is implemented in the parent class is **automatically available** in the child class — just like how children inherit properties from parents.

**Types of Inheritance:**

```
Types of Inheritance
├── Single Inheritance
├── Multiple Inheritance
├── Multilevel Inheritance
├── Hybrid Inheritance
└── Hierarchical Inheritance
```

---

## 4. Class and Object

### 4.1 Class

> **Definition:** A class is a collection of variables and methods.

Think of a class as a **blueprint** or **template**:
- A blueprint for a house is not a house itself — it describes how to build one
- A class is not an object — it describes how to create objects

```
Class (Blueprint)
├── Variables → store data
│   ├── Instance variables
│   ├── Static variables
│   └── Local variables
└── Methods → define behavior
    ├── Instance methods
    ├── Class methods
    └── Static methods
```

### 4.2 Object

> **Definition:** An object is an instance of a class. It is used to represent a class and access its functionality.

```
Class: Student (blueprint)
    ↓ object creation
Object: s = Student()
    → can now access all variables and methods of Student
```

> **Analogy:** Class = cookie cutter mold. Object = the actual cookie made from the mold. You can make many cookies (objects) from one mold (class).

### 4.3 Class vs Object

| Concept | Class | Object |
|---------|-------|--------|
| What it is | Blueprint / Template | Instance of a class |
| Memory | Defined only once | Each object gets its own memory |
| Access | Cannot use directly | Used to access class members |
| Creation | `class Student:` | `s = Student()` |

---

## 5. Syntax

### 5.1 Creating a Class

```python
class ClassName:
    # variables and methods go here
    pass
```

**Example:**

```python
class Student:
    # class body
    pass
```

> **Convention:** Class names should start with a **capital letter**. `Student` not `student`. This is a naming convention from real-world Python projects (called PascalCase).

### 5.2 Creating an Object

```python
# object_name = ClassName()
s = Student()
```

`s` is an **object reference variable** — a variable that holds a reference (pointer) to the object in memory.

```
Memory Model:
s ──→ [ Student object in memory ]
         └── variables
         └── methods
```

---

## 6. Class Documentation — `help()` and `__doc__`

```python
class Student:
    """This is a Student class to display student details."""
    pass

# Method 1 — using help()
help(Student)
# Output:
# Help on class Student in module __main__:
# class Student(builtins.object)
#  |  This is a Student class to display student details.

# Method 2 — using __doc__ via object
s = Student()
print(s.__doc__)
# Output: This is a Student class to display student details.
```

> **`__doc__`** is a **magic method** (also called **dunder method** — double underscore on both sides). These are special methods in OOP. We will see many more of these in upcoming sessions.

---

## 7. Constructor — `__init__`

### What is a Constructor?

- A constructor is a **special method** in the class
- Constructor name is always: `__init__` (double underscore, `init`, double underscore)
- `init` stands for **initialization**
- The constructor **executes automatically** when an object is created

### Constructor Syntax

```python
class Student:
    def __init__(self):
        # initialization code here
        self.sid = 1234
        self.sname = "Psi"
        self.saddress = "Hyd"
```

> **In Java/C#:** Constructor name must match class name. In **Python:** Constructor name is always `__init__` — no matter what the class name is.

### Self — The Special Variable

- `self` is the **first parameter** of every constructor (and every method)
- `self` is a special variable that refers to the **current object**
- Through `self`, you can access all variables and methods of the current class
- `self` works **only inside the class** — outside the class, use the object reference

```python
class Student:
    def __init__(self):
        self.sid = 1234          # self refers to current Student object
        self.sname = "Psi"
        self.saddress = "Hyd"
```

---

## 8. Methods

A **method** is a function defined inside a class:

```python
class Student:
    def __init__(self):
        self.sid = 1234
        self.sname = "Psi"
        self.saddress = "Hyd"

    def display(self):           # method — can have any name
        print("Student ID:", self.sid)
        print("Student Name:", self.sname)
        print("Student Address:", self.saddress)
```

> Method name can be anything — `display`, `show`, `m1`, `m2`, etc. Constructor name is fixed (`__init__`).

### Calling a Method

Methods do **not execute automatically** — you must call them:

```python
s = Student()         # constructor runs automatically
s.display()           # method runs only when explicitly called
```

---

## 9. First Complete OOP Program

```python
class Student:
    """This is a Student class to display student details."""

    def __init__(self):
        self.sid = 1234
        self.sname = "Psi"
        self.saddress = "Hyd"

    def display(self):
        print("Student ID:", self.sid)
        print("Student Name:", self.sname)
        print("Student Address:", self.saddress)


s = Student()     # object creation → constructor runs automatically
s.display()       # call the display method
```

**Output:**

```
Student ID: 1234
Student Name: Psi
Student Address: Hyd
```

### Step-by-step Execution Flow

```
1. s = Student()
        ↓
   Constructor __init__ executes automatically
        ↓
   self.sid = 1234  (stored in memory for object s)
   self.sname = "Psi"
   self.saddress = "Hyd"
        ↓
2. s.display()
        ↓
   display method executes
        ↓
   Prints: Student ID: 1234
           Student Name: Psi
           Student Address: Hyd
```

---

## 10. Parameterized Constructor

To store different data in different objects, use a **parameterized constructor**:

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

## 11. OOP Structure Diagram

```
OOP Program Structure
─────────────────────────────────────────────────────
class Student:                    ← class definition

    def __init__(self, sid, sname):   ← constructor
        self.sid = sid                    (special method, auto-runs)
        self.sname = sname

    def display(self):            ← method (user-defined)
        print(self.sid)               (runs only when called)
        print(self.sname)

─────────────────────────────────────────────────────
s = Student(101, "Psi")          ← object creation (outside class)

s.display()                      ← method call (outside class)
─────────────────────────────────────────────────────

Inside class  → use self to access variables/methods
Outside class → use object reference (s) to access
```

---

## Student Q&A

> **Student Question:** Is `self` a keyword in Python?
> **Answer:** No, `self` is **not** a keyword. It is just a naming convention. You can technically name it anything (like `this` or `me`), and it will still work. However, always use `self` — it is the standard convention that all Python developers follow, and IDEs expect it.

> **Student Question:** What is the difference between a function and a method?
> **Answer:** A function defined outside a class is called a **function**. The same function, when defined inside a class, is called a **method**. The behavior is very similar — both use `def`, both can have parameters and return values. But methods always have `self` as their first parameter.

> **Student Question:** What if I don't include a constructor or method in a class?
> **Answer:** In OOP, either a constructor or at least one method must be present — you can't have a completely empty class body (without `pass`). But a class can have only a constructor without methods, or only methods without a constructor — either one works.

---

## Key Differences Table

| | Constructor (`__init__`) | Method (any name) |
|--|--------------------------|-------------------|
| Name | Always `__init__` | Any valid name |
| When runs | Automatically when object is created | Only when explicitly called |
| Times it runs | Once per object | Any number of times |
| Purpose | Initialize variables | Business logic / display / computation |
| First param | `self` | `self` |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: __init__() takes 1 positional argument but 2 were given` | Constructor has no parameters but you passed one | Add the parameter to `__init__` |
| `AttributeError: 'Student' object has no attribute 'sid'` | Variable not defined in `__init__`, accessed via `self` | Define `self.sid` inside `__init__` |
| `TypeError: display() takes 0 positional arguments but 1 was given` | Method defined without `self` | Add `self` as first parameter |
| `NameError: name 'self' is not defined` | Tried to use `self` outside of a class method | Use object reference outside the class |
| `IndentationError: expected an indented block` | Class body is not indented correctly | Indent all class content with 4 spaces |

---

## Interview Questions

**Q: What is Object-Oriented Programming (OOP)?**
A: OOP is a programming paradigm that organizes code around objects. An object is a real-world entity that has state (variables) and behavior (methods). OOP makes code more secure, reusable, and easier to extend.

**Q: What are the four pillars of OOP?**
A: Encapsulation (data hiding and access control), Abstraction (hiding implementation, exposing service), Polymorphism (same name, different behavior), and Inheritance (new class from existing class).

**Q: What is a class in Python?**
A: A class is a blueprint or template that defines a collection of variables and methods. You create objects from a class. Syntax: `class ClassName:`.

**Q: What is an object?**
A: An object is an instance of a class. It occupies memory and can access all the variables and methods defined in its class. Created using `obj = ClassName()`.

**Q: What is `__init__` in Python?**
A: `__init__` is the constructor method. It is a special method that runs automatically every time a new object is created. It is used to initialize the variables of the class.

**Q: What is `self` in Python?**
A: `self` is a reference to the current object. It is the first parameter of every instance method and constructor. Through `self`, you can access the current object's variables and methods from within the class.

**Q: What is the difference between encapsulation and abstraction?**
A: Encapsulation is about **restricting access** — hiding data so it cannot be modified from outside. Abstraction is about **hiding complexity** — hiding how something works, only showing what it does (the service). Both are security mechanisms but at different levels.

**Q: What are the types of inheritance in Python?**
A: Single, Multiple, Multilevel, Hybrid, and Hierarchical inheritance. Python supports all five types, which is an advantage over languages like Java (which doesn't support multiple inheritance directly).

---

## Try It Yourself

**Exercise 1:** Create a class `Car` with a constructor that initializes `brand`, `model`, and `year`. Add a `display()` method that prints these details. Create two Car objects with different values.

<details><summary>Answer</summary>

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

c1 = Car("Toyota", "Camry", 2022)
c2 = Car("Honda", "Civic", 2023)
c1.display()
c2.display()
```
</details>

---

**Exercise 2:** Create a class `Rectangle` with `length` and `width` initialized in the constructor. Add a method `area()` that returns `length × width` and a method `perimeter()` that returns `2 × (length + width)`.

<details><summary>Answer</summary>

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(5, 3)
print("Area:", r.area())           # 15
print("Perimeter:", r.perimeter()) # 16
```
</details>

---

**Exercise 3:** Create a class `BankAccount` with `account_number` and `balance`. Add a `deposit(amount)` method that adds to the balance, a `withdraw(amount)` method that deducts from the balance (if funds are sufficient), and a `show_balance()` method.

<details><summary>Answer</summary>

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def show_balance(self):
        print(f"Account: {self.account_number}, Balance: {self.balance}")

acc = BankAccount("ACC001", 5000)
acc.show_balance()
acc.deposit(1000)
acc.withdraw(2000)
acc.withdraw(6000)
```
</details>

---

**Exercise 4:** Show that a class can have a docstring and access it via `help()` and `__doc__`. Create a class `Circle` with a docstring explaining its purpose.

<details><summary>Answer</summary>

```python
class Circle:
    """This class represents a circle. It can calculate area and circumference."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

c = Circle(5)
print(c.__doc__)
help(Circle)
```
</details>
