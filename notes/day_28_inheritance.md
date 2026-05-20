# Day 28 — Inheritance: Single, Multilevel, Hierarchical & Multiple

← [Day 27](day_27_inner_class_encapsulation.md) | [Index](00_INDEX.md) | [Day 29](day_29_multiple_inheritance_polymorphism.md) →

---

## Quick Revision — Day 28

| # | Key Point |
|---|-----------|
| 1 | **Inheritance** = creating a new class from an existing class |
| 2 | Existing class = Parent / Base / Super class |
| 3 | New class = Child / Derived / Sub class |
| 4 | Child class gets ALL parent class members automatically (reusability) |
| 5 | **Single inheritance**: one child from one parent — `class Child(Parent):` |
| 6 | **Multilevel inheritance**: chain A → B → C; C gets all from B and A |
| 7 | **Hierarchical inheritance**: one parent, multiple children |
| 8 | **Multiple inheritance**: one child from two or more parents; uses MRO |
| 9 | `isinstance(obj, Class)` → True if obj is an instance of Class (or its parent) |
| 10 | `issubclass(Child, Parent)` → True if Child is a subclass of Parent |

---

## Navigation

- **Pre-requisite:** [Day 27](day_27_inner_class_encapsulation.md) — Inner classes, encapsulation (private variables/methods)
- **Next:** [Day 29](day_29_multiple_inheritance_polymorphism.md) — Multiple/hybrid inheritance, constructor role, polymorphism
- **Related:** [Day 22](day_22_oop_intro.md) — OOP pillars overview

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `test14.py` | Branch + Employee single inheritance demo |
| `.py` file | `test14b.py` | Multilevel: Branch → Employee → EmpSalary |
| `.py` file | `test15.py` | Hierarchical: Parent, Child1, Child2 |
| Class | `class Employee(Branch):` | Single inheritance syntax |
| Class | `class EmpSalary(Employee):` | Multilevel: child of a child |
| Class | `class Child1(Parent):` / `class Child2(Parent):` | Hierarchical inheritance |
| Built-in | `isinstance(obj, ClassName)` | Check if object is instance of class |
| Built-in | `issubclass(ChildClass, ParentClass)` | Check if class is subclass of another |

---

## 1. What Is Inheritance?

> **Definition:** Inheritance is the process of creating a new class from an existing class.

```
Existing class  →  Parent class  /  Base class  /  Super class
New class       →  Child class   /  Derived class / Sub class
```

**Main advantages:**
1. **Reusability** — logic written in the parent class is available to all child classes without re-writing
2. **Extensibility** — you can add new child classes that extend existing functionality

**Real-world analogy:** Just like children inherit properties (money, land) from parents by default, a child class inherits all variables and methods from the parent class automatically.

```
Inheritance Flow:
Parent class (existing)
    ↓
Child class (new)
    └── Gets all parent members automatically
    └── Can add its own members on top
    └── Can create objects and access both parent and child members
```

---

## 2. Syntax of Inheritance

```python
# Syntax:
class ChildClass(ParentClass):
    # child class body

# Example:
class Employee(Branch):    # Employee inherits from Branch
    pass
```

> **Remember:** If you don't use inheritance, you write `class ClassName:` (no parent). With inheritance, you write `class ChildClass(ParentClass):`.

---

## 3. Single Inheritance

> **Definition:** Creating a new class from a **single** base class.

```
Branch (parent)
    │
    └── Employee (child)
```

### 3.1 Real-World Problem (Company Scenario)

A company asked to computerize their **branch details**, then later **employee details**, then asked "which employee belongs to which branch?"

**Step 1 — Branch class alone:**

```python
class Branch:
    def get_branch_data(self):
        self.b_code = input("Enter branch code: ")
        self.b_name = input("Enter branch name: ")
        self.b_address = input("Enter branch address: ")

    def display_branch_data(self):
        print("Branch Code:", self.b_code)
        print("Branch Name:", self.b_name)
        print("Branch Address:", self.b_address)


b = Branch()
b.get_branch_data()
b.display_branch_data()
```

**Step 2 — Employee class alone (no relation):**

```python
class Employee:
    def get_emp_data(self):
        self.emp_id = input("Enter Employee ID: ")
        self.emp_name = input("Enter Employee Name: ")
        self.emp_address = input("Enter Employee Address: ")

    def display_emp_data(self):
        print("EMP ID:", self.emp_id)
        print("EMP Name:", self.emp_name)
        print("EMP Address:", self.emp_address)


e = Employee()
e.get_emp_data()
e.display_emp_data()
```

> **Problem:** Branch and Employee are separate classes — you can't tell which employee belongs to which branch.

**Step 3 — Employee inherits from Branch (single inheritance):**

```python
class Branch:
    def get_branch_data(self):
        self.b_code = input("Enter branch code: ")
        self.b_name = input("Enter branch name: ")
        self.b_address = input("Enter branch address: ")

    def display_branch_data(self):
        print("Branch Code:", self.b_code)
        print("Branch Name:", self.b_name)
        print("Branch Address:", self.b_address)


class Employee(Branch):    # ← inheritance happens here
    def get_emp_data(self):
        self.emp_id = input("Enter Employee ID: ")
        self.emp_name = input("Enter Employee Name: ")
        self.emp_address = input("Enter Employee Address: ")

    def display_emp_data(self):
        print("EMP ID:", self.emp_id)
        print("EMP Name:", self.emp_name)
        print("EMP Address:", self.emp_address)


e = Employee()            # child class object
e.get_branch_data()       # accessing PARENT method via child object ✓
e.get_emp_data()
e.display_branch_data()
e.display_emp_data()
```

> Now we can see both branch and employee details together — which employee belongs to which branch.

### 3.2 Diagram

```
class Branch:                     ← Parent class
    get_branch_data()
    display_branch_data()

class Employee(Branch):           ← Child class — inherits Branch
    get_emp_data()                ← own methods
    display_emp_data()
    + get_branch_data()           ← inherited from Branch (automatic)
    + display_branch_data()       ← inherited from Branch (automatic)

e = Employee()
e.get_branch_data()    ← works! (from parent)
e.get_emp_data()       ← works! (from child itself)
```

---

## 4. Multilevel Inheritance

> **Definition:** Creating a new class from an **already derived class** (child of a child).

```
Branch (grandparent)
    │
Employee (parent = child of Branch)
    │
EmpSalary (child = child of Employee)
```

**Real-world:** Company later asked to also computerize **salary details** — extending the existing employee structure.

```python
class Branch:
    def get_branch_data(self):
        self.b_code = input("Enter branch code: ")
        self.b_name = input("Enter branch name: ")
        self.b_address = input("Enter branch address: ")

    def display_branch_data(self):
        print("Branch Code:", self.b_code)
        print("Branch Name:", self.b_name)
        print("Branch Address:", self.b_address)


class Employee(Branch):             # inherits from Branch
    def get_emp_data(self):
        self.emp_id = input("Enter Employee ID: ")
        self.emp_name = input("Enter Employee Name: ")
        self.emp_address = input("Enter Employee Address: ")

    def display_emp_data(self):
        print("EMP ID:", self.emp_id)
        print("EMP Name:", self.emp_name)
        print("EMP Address:", self.emp_address)


class EmpSalary(Employee):          # inherits from Employee (multilevel)
    def get_salary(self):
        self.basic = float(input("Enter basic salary: "))

    def calculate(self):
        self.da = self.basic * 0.03
        self.hra = self.basic * 0.04
        self.gross = self.basic + self.da + self.hra

    def display_salary(self):
        print("Basic:", self.basic)
        print("DA:", self.da)
        print("HRA:", self.hra)
        print("Gross:", self.gross)


e = EmpSalary()         # create object for the last child class
e.get_branch_data()     # from Branch (grandparent)
e.get_emp_data()        # from Employee (parent)
e.get_salary()          # own method
e.calculate()
e.display_branch_data()
e.display_emp_data()
e.display_salary()
```

> **Rule:** In multilevel inheritance, create an object for the **last (deepest) child class**. That object gives access to all ancestors automatically.

### 4.1 Extensibility Concept

> Inheritance allows you to extend existing functionality. First we built Branch, then Employee, then EmpSalary — each extension adds new features without rewriting existing code. This is called **extensibility**.

---

## 5. Hierarchical Inheritance

> **Definition:** Creating **multiple child classes** from a **single parent class**.

```
       Parent
      /      \
  Child1    Child2    (both inherit from same Parent)
```

```python
class Parent:
    def p1(self):
        print("Parent class function")


class Child1(Parent):
    def c1(self):
        print("Child1 class function")


class Child2(Parent):
    def c2(self):
        print("Child2 class function")


obj1 = Child1()
obj1.p1()    # parent function via Child1 object
obj1.c1()    # child1's own function

obj2 = Child2()
obj2.p1()    # parent function via Child2 object — SAME parent
obj2.c2()    # child2's own function
```

**Output:**
```
Parent class function
Child1 class function
Parent class function
Child2 class function
```

> Both `Child1` and `Child2` share the same parent's `p1()` method — that is reusability in hierarchical inheritance.

---

## 6. `isinstance()` and `issubclass()`

These two built-in functions are especially useful when working with inheritance.

### 6.1 `isinstance(object, class)`

Checks whether an object is an instance of a particular class (or any of its parent classes).

```python
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

print(isinstance(obj1, Child1))    # True  — obj1 is a Child1 instance
print(isinstance(obj1, Child2))    # False — obj1 is NOT a Child2 instance
print(isinstance(obj2, Child2))    # True

# Now the interesting case:
print(isinstance(obj1, Parent))    # True!  — Child1 inherits from Parent
print(isinstance(obj2, Parent))    # True!  — Child2 inherits from Parent
```

> **Key insight:** `isinstance(obj1, Parent)` returns `True` because `Child1` inherits from `Parent` — so `obj1` is technically also an instance of `Parent`.

### 6.2 `issubclass(child, parent)`

Checks whether one class is a subclass of another.

```python
print(issubclass(Child1, Parent))    # True
print(issubclass(Child2, Parent))    # True
print(issubclass(Child1, Child2))    # False — they are siblings, not parent-child
print(issubclass(Parent, Child1))    # False — Parent is NOT a subclass of Child1
```

### 6.3 Summary

| Function | Purpose | Returns |
|----------|---------|---------|
| `isinstance(obj, Class)` | Is this object an instance of this class (or its ancestor)? | `True` / `False` |
| `issubclass(SubClass, ParentClass)` | Is this class a subclass of another class? | `True` / `False` |

---

## 7. Multiple Inheritance (Introduction)

> **Definition:** Creating a new class from **two or more base classes**.

Full coverage in [Day 29](day_29_multiple_inheritance_polymorphism.md). Preview:

```python
class A:
    def f1(self):
        print("F1 of class A")

class B:
    def f2(self):
        print("F2 of class B")

class C(A, B):        # multiple inheritance — C inherits from both A and B
    def f3(self):
        print("F3 of class C")


c = C()
c.f1()    # from A
c.f2()    # from B
c.f3()    # C's own
```

> Python uses **Method Resolution Order (MRO)** to handle multiple inheritance — covered in detail next session.

---

## 8. Inheritance Types — Summary Diagram

```
TYPES OF INHERITANCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Single:              Parent → Child

Multilevel:          A → B → C  (chain)

Hierarchical:        Parent → Child1
                     Parent → Child2
                     Parent → Child3

Multiple:            A \
                        → C  (C inherits from A AND B)
                     B /

Hybrid:              Combination of the above (e.g., multiple + multilevel)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 9. Student Q&A

> **Student Question:** If I create an object for the parent class, can I access child class methods?
> **Answer:** No. When you create an object of the parent class, you can only access parent class methods. Only when you create an object of the child class, do you get access to both child and parent methods. The child includes the parent — not the other way around.

> **Student Question:** Do I always have to create an object for the last (deepest) child class in multilevel inheritance?
> **Answer:** Not always — you can create objects at any level. But if you want access to ALL ancestors' methods (branch + employee + salary), then yes, you must create an object of the deepest child class (`EmpSalary`). Creating an object of `Employee` gives you only Branch and Employee methods, not Salary.

> **Student Question:** What is extensibility in inheritance?
> **Answer:** Extensibility means adding new child classes to existing code without modifying the existing classes. In the example, we first built `Branch`, then `Employee`, then `EmpSalary`. Each time the company had new requirements, we extended the class hierarchy. We never touched or rewrote the original `Branch` class.

> **Student Question:** `isinstance(obj1, Parent)` returns True even though obj1 is a Child1 object. Why?
> **Answer:** Because `Child1` inherits from `Parent`. An instance of `Child1` is also technically an instance of `Parent` — just like a son is also a member of his father's family. `isinstance()` checks the entire inheritance chain, not just the immediate class.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `AttributeError: 'Employee' object has no attribute 'b_code'` | Called `display_branch_data()` before `get_branch_data()` — variables not set yet | Call `get_branch_data()` first to accept input |
| `AttributeError: 'Branch' object has no attribute 'emp_id'` | Created object for parent (`Branch`) and called a child method | Create object for child class (`Employee`) instead |
| Calling parent method gives error "not defined" | Forgot to add `(ParentClass)` in child class definition | Use `class Child(Parent):` not `class Child:` |
| `TypeError: issubclass() arg 1 must be a class` | Passed an object to `issubclass()` instead of a class | Use `issubclass(Child1, Parent)` not `issubclass(obj1, Parent)` |

---

## Interview Questions

**Q: What is inheritance in Python?**
A: Inheritance is the process of creating a new class (child/derived/subclass) from an existing class (parent/base/superclass). The child class automatically gets all the variables and methods of the parent class. The main advantages are reusability (use parent code without rewriting) and extensibility (add new functionality through new child classes).

**Q: What is single inheritance?**
A: Single inheritance is when a new class is created from exactly one parent class. Example: `class Employee(Branch):` — Employee inherits all methods from Branch.

**Q: What is multilevel inheritance?**
A: Multilevel inheritance is when a child class is created from an already derived class — a chain. Example: Branch → Employee → EmpSalary. EmpSalary gets methods from both Employee and Branch.

**Q: What is hierarchical inheritance?**
A: When multiple child classes are derived from a single parent class. Example: both `Child1` and `Child2` inherit from the same `Parent`. Each child gets the parent's methods independently.

**Q: What is the difference between `isinstance()` and `issubclass()`?**
A: `isinstance(obj, Class)` checks if an object is an instance of a class (or its ancestors) — works on objects. `issubclass(Sub, Parent)` checks if one class is a subclass of another — works on classes.

**Q: Can a child class object access parent class methods?**
A: Yes. When you create an object of the child class, it automatically has access to all parent class methods through inheritance. You don't need to create a parent class object separately.

---

## Try It Yourself

**Exercise 1:** Create single inheritance — `Animal` parent with `breathe()` method. `Dog` child inheriting from Animal with its own `bark()` method. Create a Dog object and call both methods.

<details><summary>Answer</summary>

```python
class Animal:
    def breathe(self):
        print("Animal breathing...")

class Dog(Animal):
    def bark(self):
        print("Dog barking: Woof!")

d = Dog()
d.breathe()   # from parent
d.bark()      # own method
```
</details>

---

**Exercise 2:** Create multilevel inheritance — `Vehicle` → `Car` → `ElectricCar`. Each class has one unique method. Create an `ElectricCar` object and call methods from all three levels.

<details><summary>Answer</summary>

```python
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("Car is being driven")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

ec = ElectricCar()
ec.move()     # from Vehicle
ec.drive()    # from Car
ec.charge()   # own method
```
</details>

---

**Exercise 3:** Demonstrate `isinstance()`. Create classes `Shape`, `Circle(Shape)`, `Rectangle(Shape)`. Create objects for Circle and Rectangle. Test `isinstance()` with all combinations and explain the results.

<details><summary>Answer</summary>

```python
class Shape:
    pass

class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

c = Circle()
r = Rectangle()

print(isinstance(c, Circle))       # True
print(isinstance(c, Shape))        # True  — inherits from Shape
print(isinstance(c, Rectangle))    # False — not a Rectangle
print(isinstance(r, Shape))        # True  — inherits from Shape
print(issubclass(Circle, Shape))   # True
print(issubclass(Rectangle, Circle)) # False — siblings
```
</details>

---

**Exercise 4:** Create hierarchical inheritance — `Person` parent with `introduce()`. `Student(Person)` with `study()`. `Teacher(Person)` with `teach()`. Create objects for both children and call parent method on each.

<details><summary>Answer</summary>

```python
class Person:
    def introduce(self):
        print("Hello, I am a person.")

class Student(Person):
    def study(self):
        print("Student is studying.")

class Teacher(Person):
    def teach(self):
        print("Teacher is teaching.")

s = Student()
s.introduce()    # from Parent
s.study()

t = Teacher()
t.introduce()    # from Parent (same method, different object)
t.teach()
```
</details>
