# Day 25 — OOP: Types of Methods in a Python Class

← [Day 24](day_24_types_of_variables.md) | [Index](00_INDEX.md) | Day 26 →

---

## Quick Revision — Day 25

| # | Key Point |
|---|-----------|
| 1 | Three types of methods: **Instance**, **Class**, **Static** |
| 2 | **Instance method**: uses instance variables inside; first param is `self` |
| 3 | **Class method**: uses static/class-level variables inside; first param is `cls`; needs `@classmethod` decorator |
| 4 | **Static method**: general utility; no `self` or `cls`; needs `@staticmethod` decorator |
| 5 | Decorator `@classmethod` is what makes a method a class method — not the parameter name `cls` |
| 6 | Decorator `@staticmethod` is what makes a method a static method |
| 7 | Without a decorator, any method (even with `cls`) is treated as an instance method |
| 8 | Instance methods are the most commonly used; class methods are rarely used |
| 9 | Static methods can accept their own parameters (not self or cls) |
| 10 | All three method types can be accessed via class name or object reference |

---

## Navigation

- **Pre-requisite:** [Day 24](day_24_types_of_variables.md) — Types of variables (instance, static, local)
- **Next:** Day 26 — Deleting static variables, OOP features (encapsulation, etc.)
- **Related:** [Day 15](day_15_functions_basics.md) — Function basics; [Day 22](day_22_oop_intro.md) — OOP intro

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `methods_demo.py` | All three method types demonstrated |
| Class | `class Student:` | Instance method — average of marks |
| Class | `class Test:` | All three methods side-by-side |
| Decorator | `@classmethod` | Makes a method a class method |
| Decorator | `@staticmethod` | Makes a method a static method |
| Method | `def avg(self):` | Instance method using `self.m1, self.m2, self.m3` |
| Method | `def m1(cls):` + `@classmethod` | Class method using `cls.INST` |
| Method | `def m2(name):` + `@staticmethod` | Static method with own parameter |

---

## 1. Three Types of Methods — Overview

Just like there are three types of variables in a Python class, there are three types of methods:

```
Class (blueprint)
├── Instance Methods
│     → use instance variables (self.xxx)
│     → first parameter: self
│     → most commonly used
│
├── Class Methods
│     → use static/class variables (cls.xxx)
│     → first parameter: cls
│     → needs @classmethod decorator
│     → rarely used
│
└── Static Methods
      → general utility methods
      → no self or cls
      → needs @staticmethod decorator
      → commonly used for helper functions
```

---

## 2. Instance Methods

### 2.1 Definition

> **Inside the method implementation, when we use instance variables, such methods are called instance methods.**

```
Instance Method — Key Facts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Uses instance variables (self.xxx) inside
2. First parameter is self (mandatory)
3. Access within class: self.method_name()
4. Access outside class: object_reference.method_name()
5. Most commonly used type of method
6. No special decorator needed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2.2 Example — Student Average Marks

```python
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1    # instance variables
        self.m2 = m2
        self.m3 = m3

    def avg(self):       # instance method — uses self.m1, self.m2, self.m3
        return (self.m1 + self.m2 + self.m3) / 3


s1 = Student(67, 89, 56)
s2 = Student(98, 78, 82)

# Access outside class via object reference
print(s1.avg())   # 70.66666...
print(s2.avg())   # 86.0
```

> **Why it's an instance method:** Because inside `avg()` we use `self.m1`, `self.m2`, `self.m3` — these are instance variables. A method that touches instance variables is an instance method.

### 2.3 Calling Instance Methods — Two Ways

```python
# Way 1 — Outside the class (most common)
s1 = Student(67, 89, 56)
print(s1.avg())     # calls avg on s1's data

# Way 2 — Inside the class using self
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        result = self.avg()    # calling instance method from constructor
        print("Average:", result)

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

s1 = Student(67, 89, 56)   # prints Average: 70.666...
```

### 2.4 Common Mistake — Forgetting to Print the Return Value

```python
s1 = Student(67, 89, 56)
s1.avg()       # NO output — return value is discarded
print(s1.avg()) # CORRECT — print the returned value
```

> If a method uses `return`, the caller must `print()` the result to see it. Alternatively, use `print()` inside the method itself.

---

## 3. Class Methods

### 3.1 Definition

> **Inside the method implementation, when we use static (class-level) variables, such methods are called class methods.**

```
Class Method — Key Facts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Uses static/class-level variables (cls.xxx)
2. First parameter is cls (class variable)
3. Needs @classmethod decorator to become a class method
4. Access: class name OR object reference
5. Rarely used in practice
6. WITHOUT the decorator → it is just an instance method
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3.2 What is a Decorator?

A **decorator** is a built-in feature in Python that modifies the behavior of a function or method. Written with `@` before the decorator name, placed directly above the method definition.

```python
@classmethod          ← decorator
def method_name(cls):
    ...
```

> We will study user-defined decorators later. For now, know that `@classmethod` and `@staticmethod` are predefined (built-in) decorators.

### 3.3 Example — Institute Name

```python
class Student:
    INST = "Durga Software Solutions"   # static variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod               # decorator — makes m1 a class method
    def m1_class(cls):
        print(cls.INST)        # access static variable via cls


# Access via class name
Student.m1_class()    # Durga Software Solutions

# Access via object reference
s = Student(67, 89, 56)
s.m1_class()          # Durga Software Solutions
```

### 3.4 Critical Point — Decorator Determines Method Type

```python
class Test:
    def method_a(cls):        # no decorator → INSTANCE method
        print("I look like class method but I'm not!")

    @classmethod
    def method_b(cls):        # @classmethod → CLASS method
        print("I am a class method")
```

> Even if you name the first parameter `cls`, **without `@classmethod`**, Python treats the method as an instance method. The decorator is what classifies it.

```python
# This is still an INSTANCE method (no decorator):
def get_info(cls):
    print(cls.INST)

# This is a CLASS method (@classmethod added):
@classmethod
def get_info(cls):
    print(cls.INST)
```

---

## 4. Static Methods

### 4.1 Definition

> **Static methods are general utility methods. They are not tied to any specific object or class variable.**

```
Static Method — Key Facts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. General utility / helper methods
2. No self or cls as first parameter
3. Needs @staticmethod decorator
4. Can have their own parameters (any name, any count)
5. Access: class name OR object reference
6. Commonly used in practice for helper functions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 4.2 Example — Greeting Utility

```python
class Student:
    INST = "Durga Software Solutions"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @staticmethod                    # decorator — makes hello a static method
    def hello(name):                 # own parameter — no self or cls
        print(f"Hello {name}")


# Access via class name
Student.hello("World")    # Hello World

# Access via object reference
s = Student(67, 89, 56)
s.hello("Alice")          # Hello Alice
```

### 4.3 Static Method Without Parameters

```python
class Utility:
    @staticmethod
    def greet():
        print("Hello!")

Utility.greet()   # Hello!
```

### 4.4 Why Static Methods?

Static methods are used for logic that:
- Does not depend on any instance variable (no need for `self`)
- Does not depend on any class variable (no need for `cls`)
- Is a **utility / helper function** that happens to logically belong to the class

Examples:
- A `MathUtils` class with a `square(n)` static method
- A `StringUtils` class with `is_palindrome(s)` static method
- Validation logic that doesn't need object state

---

## 5. All Three Methods in One Class

```python
class Student:
    INST = "Durga Software Solutions"   # static variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1   # instance variables
        self.m2 = m2
        self.m3 = m3

    # ── Instance Method ───────────────────────────────────────────
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # ── Class Method ──────────────────────────────────────────────
    @classmethod
    def get_institute(cls):
        print(cls.INST)

    # ── Static Method ─────────────────────────────────────────────
    @staticmethod
    def hello(name):
        print(f"Hello {name}")


s1 = Student(67, 89, 56)
s2 = Student(98, 78, 82)

# Instance method — called via object
print(s1.avg())    # 70.666...
print(s2.avg())    # 86.0

# Class method — called via class name
Student.get_institute()   # Durga Software Solutions

# Static method — called via class name
Student.hello("Alice")    # Hello Alice
```

---

## 6. How to Recognize Each Method Type

This is what the instructor called out as very important:

```
Recognition Guide
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def method(self, ...):             → INSTANCE method
    # uses self.variable

@classmethod
def method(cls, ...):              → CLASS method
    # uses cls.class_variable

@staticmethod
def method(your_params):           → STATIC method
    # no self, no cls

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Key recognition tips:**

1. Is there `self` as the first parameter AND the method uses instance variables inside? → **Instance method**
2. Is there `@classmethod` decorator AND `cls` as first parameter? → **Class method**
3. Is there `@staticmethod` decorator AND no `self`/`cls`? → **Static method**

---

## 7. Comparison Table — All Three Methods

| Feature | Instance Method | Class Method | Static Method |
|---------|---------------|--------------|--------------|
| Uses | Instance variables (`self.x`) | Static/class variables (`cls.x`) | Neither (own params only) |
| First parameter | `self` | `cls` | None (your own params) |
| Decorator | Not needed | `@classmethod` | `@staticmethod` |
| Access | Object reference | Class name or obj ref | Class name or obj ref |
| How common | Very common | Rarely used | Commonly used |
| Can access instance vars | Yes (via self) | No | No |
| Can access static vars | Yes (via self or ClassName) | Yes (via cls) | Yes (via ClassName directly) |

---

## 8. What Else You Should Know

### 8.1 Decorators — Brief Introduction

A **decorator** is a design pattern in Python that allows you to modify the behavior of a function or method. The built-in ones we've seen:

```python
@classmethod    # makes a method a class method
@staticmethod   # makes a method a static method
```

Decorators are placed on the line immediately above the function definition. You will learn to create your own (user-defined) decorators in a later session.

### 8.2 `cls` Name Convention

Just like `self` is a convention (not a keyword), `cls` is also a convention. You can use any name, but `cls` is universally used for class methods and you should always follow it.

### 8.3 Accessing Static Variables Inside Static Methods

A static method has no `cls`, so to access static variables from within a static method, use the class name directly:

```python
class Demo:
    X = 100    # static variable

    @staticmethod
    def show():
        print(Demo.X)    # use class name, not cls (no cls available)

Demo.show()   # 100
```

---

## 9. Student Q&A

> **Student Question:** What is an instance method in invocation — is it necessary to use `obj = ClassName()` with variables?
> **Answer:** Yes, if the constructor has parameters, you must pass them when creating the object. The constructor is called automatically when you write `s = Student(67, 89, 56)`. Those values go into the constructor and are stored as instance variables. You can also call the method directly from outside if you want to pass arguments differently, but you always need an object to call an instance method.

> **Student Question:** Why doesn't `obj.static_method()` always work the same as `ClassName.static_method()`?
> **Answer:** Normally both work. The problem in the class was that a variable named `s1` was already holding a different object reference, so calling `s1.method()` was trying to call it on that specific object. In general, both `ClassName.method()` and `obj.method()` work for class and static methods.

> **Student Question:** When would you use a class method vs a static method?
> **Answer:** Use a class method when the method needs to access or modify a class-level (static) variable — it uses `cls.variable`. Use a static method for utility logic that doesn't need any object state or class state — it's just a helper function that logically belongs to the class.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: method() takes 0 positional arguments but 1 was given` | Method defined without `self` but no `@staticmethod` decorator | Either add `self` (instance method) or add `@staticmethod` |
| `TypeError: method() missing 1 required positional argument: 'self'` | Calling instance method on class name instead of object | Create an object first: `obj = Class(); obj.method()` |
| `AttributeError: type object 'Test' has no attribute 'x'` | Trying to access instance variable via class name | Instance variables need an object: `obj = Test(); print(obj.x)` |
| Method not decorated but named with `cls` — still shows `self` error | Without `@classmethod`, Python treats it as instance method; `cls` receives object | Add `@classmethod` decorator |
| `NameError: name 'x' is not defined` in static method | Trying to access a class variable without prefix | Use `ClassName.x` inside a static method |

---

## Interview Questions

**Q: What are the three types of methods in a Python class?**
A: Instance methods (use instance variables, first param is `self`), class methods (use class-level variables, first param is `cls`, needs `@classmethod` decorator), and static methods (general utility, no `self` or `cls`, needs `@staticmethod` decorator).

**Q: What is an instance method?**
A: An instance method is a method that uses instance variables inside its implementation. Its first parameter is `self`. It is the most commonly used method type and is accessed via an object reference.

**Q: What is the difference between a class method and a static method?**
A: A class method uses class-level (static) variables and receives `cls` as its first parameter — it needs `@classmethod` decorator. A static method is a general utility method that doesn't use any instance or class variables — it needs `@staticmethod` decorator and doesn't have `self` or `cls`.

**Q: What is a decorator in Python?**
A: A decorator is a special syntax (`@name`) placed above a function or method that modifies its behavior. `@classmethod` makes a method into a class method; `@staticmethod` makes it a static method. Python also allows user-defined decorators for custom behaviors.

**Q: How do you recognize an instance method, class method, and static method in code?**
A: Instance method — has `self` as first parameter, uses instance variables. Class method — has `@classmethod` decorator and `cls` as first parameter. Static method — has `@staticmethod` decorator and no `self` or `cls`. The decorator is the definitive signal for class and static methods.

**Q: Can you call a static method on an object reference?**
A: Yes. Static methods can be called both via class name (`ClassName.method()`) and via an object reference (`obj.method()`). Both work identically.

**Q: Is `cls` a keyword in Python?**
A: No. Like `self`, `cls` is just a naming convention. You can technically name it anything. But always use `cls` for class methods — it is the universal Python convention.

---

## Try It Yourself

**Exercise 1:** Create a class `Circle` with a constructor accepting `radius`. Add an instance method `area()` that returns `π × r²`. Create two Circle objects with different radii and print their areas.

<details><summary>Answer</summary>

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c1 = Circle(5)
c2 = Circle(10)
print(f"Circle 1 area: {c1.area():.2f}")   # 78.54
print(f"Circle 2 area: {c2.area():.2f}")   # 314.16
```
</details>

---

**Exercise 2:** Create a class `Company` with a static variable `company_name`. Add a class method `show_company()` that prints the company name using `cls`. Call it via class name and via an object reference.

<details><summary>Answer</summary>

```python
class Company:
    company_name = "TechCorp Inc."

    def __init__(self, emp_name):
        self.emp_name = emp_name

    @classmethod
    def show_company(cls):
        print("Company:", cls.company_name)


# Via class name
Company.show_company()      # Company: TechCorp Inc.

# Via object reference
e = Company("Alice")
e.show_company()            # Company: TechCorp Inc.
```
</details>

---

**Exercise 3:** Create a class `MathUtils` with three static methods: `square(n)`, `cube(n)`, and `is_even(n)`. Call each method using the class name.

<details><summary>Answer</summary>

```python
class MathUtils:
    @staticmethod
    def square(n):
        return n * n

    @staticmethod
    def cube(n):
        return n * n * n

    @staticmethod
    def is_even(n):
        return n % 2 == 0


print(MathUtils.square(5))    # 25
print(MathUtils.cube(3))      # 27
print(MathUtils.is_even(4))   # True
print(MathUtils.is_even(7))   # False
```
</details>

---

**Exercise 4:** Create a class `Student` that has all three method types. Instance method `grade()` that returns "Pass" if average marks ≥ 50 else "Fail". Class method `school()` that prints a static variable `school_name`. Static method `info()` that prints "Student Management System".

<details><summary>Answer</summary>

```python
class Student:
    school_name = "ABC High School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def grade(self):              # instance method
        avg = (self.m1 + self.m2 + self.m3) / 3
        return "Pass" if avg >= 50 else "Fail"

    @classmethod
    def school(cls):              # class method
        print("School:", cls.school_name)

    @staticmethod
    def info():                   # static method
        print("Student Management System")


s = Student(60, 45, 55)
print(s.grade())          # Pass
Student.school()          # School: ABC High School
Student.info()            # Student Management System
```
</details>

---

**Exercise 5:** Demonstrate that naming a parameter `cls` without `@classmethod` decorator does NOT make it a class method. Show the error you get and then fix it.

<details><summary>Answer</summary>

```python
class Demo:
    X = 100

    # Without decorator — still an INSTANCE method!
    def show_wrong(cls):
        print(cls.X)    # 'cls' here is actually the object, not the class


d = Demo()
d.show_wrong()   # prints 100 — works only because d.X accesses static via object
                 # but this is still an instance method, not a class method

# Correct way — add decorator
class DemoFixed:
    X = 100

    @classmethod
    def show_correct(cls):
        print(cls.X)    # cls is now truly the class


DemoFixed.show_correct()   # 100
```
</details>
