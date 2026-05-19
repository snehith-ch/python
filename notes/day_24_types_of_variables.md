# Day 24 — OOP: Types of Variables in a Python Class

← [Day 23](day_23_oop_constructor_method.md) | [Index](00_INDEX.md) | [Day 25](day_25_types_of_methods.md) →

---

## Quick Revision — Day 24

| # | Key Point |
|---|-----------|
| 1 | Three types of variables in a Python class: **Instance**, **Static**, **Local** |
| 2 | **Instance variable**: value varies per object; declared with `self`; separate copy for each object |
| 3 | **Static variable**: same value for all objects; declared inside class, outside methods |
| 4 | **Local variable**: exists only during method execution; no `self`, no object access |
| 5 | Instance variables can be declared inside constructor, inside method (with self), or outside class (with object ref) |
| 6 | Static variables accessed via class name (`ClassName.var`) or object reference |
| 7 | Changing a static variable affects **all** objects; changing an instance variable affects **only that object** |
| 8 | `del self.var` deletes instance variable from inside the class |
| 9 | `del obj.var` deletes instance variable from outside the class |
| 10 | Local variables are **temporary** — created when method runs, destroyed when method ends |

---

## Navigation

- **Pre-requisite:** [Day 23](day_23_oop_constructor_method.md) — Constructor vs Method, program structures
- **Next:** [Day 25](day_25_types_of_methods.md) — Types of methods (instance, class, static)
- **Related:** [Day 15](day_15_functions_basics.md) — Local vs global variables in functions

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `test3.py` | Instance variable declaration & access |
| `.py` file | `test4.py` | Instance variable access within/outside class |
| `.py` file | `test5.py` | Instance variable deletion, separate copy demo |
| `.py` file | `test6.py` | Static variable declaration & comparison |
| `.py` file | `test7.py` | Local variable scope demo |
| Variable | `self.a = 10` | Instance variable in constructor |
| Variable | `INST = "Durga"` | Static variable inside class, outside methods |
| Variable | `a = 10` inside method | Local variable |

---

## 1. Overview — Three Types of Variables

```
Class (blueprint)
├── Instance Variables  (object-level)
│     → value is DIFFERENT for each object
│     → declared using self
│     → every object gets its OWN copy
│
├── Static Variables    (class-level)
│     → value is SAME for all objects
│     → declared inside class, OUTSIDE any method
│     → only ONE copy shared among all objects
│
└── Local Variables     (method-level)
      → declared inside a method WITHOUT self
      → accessible ONLY within that specific method
      → temporary: created when method starts, destroyed when it ends
```

| Feature | Instance Variable | Static Variable | Local Variable |
|---------|-----------------|----------------|---------------|
| Also called | Object-level | Class-level | Method-level / Temporary |
| Declared using | `self` | Inside class, outside methods | Inside method, no `self` |
| Scope | Accessible anywhere (with self or obj ref) | Accessible anywhere (class or obj ref) | Only within that method |
| Copies | One per object | One for all objects | One per method call |
| Effect of change | Only that object affected | ALL objects affected | No effect outside method |

---

## 2. Instance Variables (Object-Level)

### 2.1 Definition

> **If the value of a variable varies from object to object, such variables are called instance variables.**

Every object has its **own separate copy** of instance variables. Changing or deleting one object's copy does not affect any other object.

### 2.2 Where to Declare Instance Variables

Instance variables can be declared in **three places**:

```python
class Test:

    def __init__(self):
        self.a = 10        # PLACE 1: inside constructor using self

    def m1(self):
        self.b = 20        # PLACE 2: inside instance method using self


t = Test()
t.c = 30                   # PLACE 3: outside the class using object reference
```

Visual map:

```
┌──────────────────────────────────────────────────────┐
│  class Test:                                          │
│                                                       │
│      def __init__(self):                              │
│          self.a = 10   ← PLACE 1 (constructor)        │
│                                                       │
│      def m1(self):                                    │
│          self.b = 20   ← PLACE 2 (instance method)    │
│                                                       │
└──────────────────────────────────────────────────────┘

t = Test()
t.c = 30                ← PLACE 3 (outside class, via object ref)
```

### 2.3 Demonstration — `__dict__`

```python
class Test:
    def __init__(self):
        self.a = 10       # instance variable in constructor

    def m1(self):
        self.b = 20       # instance variable in method


t = Test()                # constructor runs → a=10 assigned
print(t.__dict__)         # {'a': 10}  — only a is there
                          # b is NOT here because m1 was not called yet

t.m1()                    # now m1 runs → b=20 assigned
print(t.__dict__)         # {'a': 10, 'b': 20}

t.c = 30                  # declared outside class via object ref
print(t.__dict__)         # {'a': 10, 'b': 20, 'c': 30}
```

### 2.4 Accessing Instance Variables

```python
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        # WITHIN the class → use self
        print(self.a)    # 10
        print(self.b)    # 20


t = Test()
t.m1()

# OUTSIDE the class → use object reference
print(t.a)   # 10
print(t.b)   # 20
```

Rule:
```
Inside class  → self.variable_name
Outside class → object_reference.variable_name
```

### 2.5 Deleting Instance Variables

```python
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def m1(self):
        del self.a       # DELETE inside class → del self.variable


t = Test()
print(t.__dict__)        # {'a': 10, 'b': 20, 'c': 30}

t.m1()                   # deletes 'a'
print(t.__dict__)        # {'b': 20, 'c': 30}

del t.b                  # DELETE outside class → del obj.variable
print(t.__dict__)        # {'c': 30}
```

Syntax summary:
```
Inside class:  del self.variable_name
Outside class: del object_reference.variable_name
```

### 2.6 Separate Copy Per Object — The Key Concept

> **Key Rule:** We can create any number of objects for a class. For every object, a **separate copy** of instance variables is created. If we change or delete one object's copy, other objects' copies are **not affected**.

```python
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def m1(self):
        del self.a       # delete 'a' for whichever object calls this


t1 = Test()
t2 = Test()

print(t1.__dict__)   # {'a': 10, 'b': 20, 'c': 30}
print(t2.__dict__)   # {'a': 10, 'b': 20, 'c': 30}

t1.m1()              # deletes 'a' from t1's copy only

print(t1.__dict__)   # {'b': 20, 'c': 30}      ← 'a' gone from t1
print(t2.__dict__)   # {'a': 10, 'b': 20, 'c': 30}  ← t2 unchanged

# Change a value in t1 only
t1.c = 99
print(t1.__dict__)   # {'b': 20, 'c': 99}      ← t1's c changed
print(t2.__dict__)   # {'a': 10, 'b': 20, 'c': 30}  ← t2 still 30
```

Memory diagram:

```
After Test() called for both t1 and t2:

t1 → [ a=10  b=20  c=30 ]    ← separate copy
t2 → [ a=10  b=20  c=30 ]    ← separate copy

After t1.m1() (deletes a from t1):

t1 → [       b=20  c=30 ]    ← a is gone from t1
t2 → [ a=10  b=20  c=30 ]    ← t2 untouched
```

---

## 3. Static Variables (Class-Level)

### 3.1 Definition

> **If the value of a variable does NOT vary from object to object, declare it inside the class but outside any method. Such variables are called static variables (or class-level variables).**

The variables which are declared **within the class** but **outside any methods** are called static variables.

### 3.2 One Copy for All Objects

For static variables, there is **only one copy** maintained throughout the class. All objects share that same copy:

```
class Student:
    school = "ABC School"   ← static variable
    │
    ├── s1 → sees school = "ABC School"
    ├── s2 → sees school = "ABC School"
    └── s3 → sees school = "ABC School"   ← all see SAME copy
```

If the static variable is changed, **all objects see the change**:

```
Test.a = 99
    │
    ├── t1 → sees a = 99
    └── t2 → sees a = 99   ← both updated simultaneously
```

### 3.3 Declaring and Accessing Static Variables

```python
class Test:
    a = 10                  # static variable — inside class, OUTSIDE method

    def __init__(self):
        self.b = 20         # instance variable (different for each object)

    def m1(self):
        print(self.a)       # can access static var inside method using self
        print(self.b)


t1 = Test()
t2 = Test()

# Access via class name (recommended for static)
print(Test.a)    # 10

# Access via object reference (also works)
print(t1.a)      # 10
print(t2.a)      # 10
```

### 3.4 Changing a Static Variable Affects All Objects

```python
class Test:
    a = 10    # static variable


t1 = Test()
t2 = Test()
print(t1.a, t2.a)   # 10 10

# Change via class name — affects ALL objects
Test.a = 99
print(t1.a, t2.a)   # 99 99   ← both changed!
```

### 3.5 Comparing Static vs Instance Variable Behavior

```python
class Test:
    a = 10    # static

    def __init__(self):
        self.b = 20   # instance


t1 = Test()
t2 = Test()

# Change static → affects all
Test.a = 99
print(t1.a, t2.a)   # 99 99

# Change instance on t1 → only t1 affected
t1.b = 55
print(t1.b, t2.b)   # 55 20
```

---

## 4. Local Variables (Method-Level)

### 4.1 Definition

> **Variables declared inside a particular method without `self` are called local variables (method-level variables).**

### 4.2 Local Variables are Temporary

- Created when the method **starts executing**
- Destroyed when the method **finishes executing**
- Not accessible from outside the method or from other methods

```python
class Test:
    def m1(self):
        a = 10          # local variable — declared without self
        print(a)        # accessible here

    def m2(self):
        b = 20          # local variable in m2
        print(b)        # accessible here


t = Test()
t.m1()   # prints 10
t.m2()   # prints 20
```

### 4.3 Local Variables Cannot Cross Method Boundaries

```python
class Test:
    def m1(self):
        a = 10    # local to m1

    def m2(self):
        print(a)  # NameError: name 'a' is not defined
                  # 'a' belongs to m1 — m2 cannot see it


t = Test()
t.m1()
t.m2()   # ERROR
```

**Output:**
```
NameError: name 'a' is not defined
```

### 4.4 Local vs Instance Variable

```python
class Test:
    def m1(self):
        self.a = 10   # instance variable (with self) — accessible from anywhere
        b = 20        # local variable (no self) — only accessible in m1

    def m2(self):
        print(self.a)  # OK — instance variable is accessible here
        # print(b)     # ERROR — b is local to m1, not accessible here


t = Test()
t.m1()
t.m2()   # prints 10
```

> **Rule:** If you want a variable to be shared across methods, add `self.`. Without `self`, the variable is local and dies when the method ends.

---

## 5. Complete Summary Diagram

```
class MyClass:
    X = 100            ← STATIC variable
    │                     (inside class, outside method)
    │
    ├── def __init__(self):
    │       self.Y = 200  ← INSTANCE variable
    │                       (inside constructor, using self)
    │
    ├── def m1(self):
    │       self.Z = 300  ← INSTANCE variable
    │                       (inside method, using self)
    │       W = 400       ← LOCAL variable
    │                       (inside method, no self)
    │
    └── (outside class)
obj = MyClass()
obj.A = 500            ← INSTANCE variable
                         (outside class, using object ref)
```

---

## 6. Student Q&A

> **Student Question:** Why is the static variable called "static"?
> **Answer:** The word "static" means unchanging or fixed across the class. In Python, a variable declared inside a class but outside methods is shared among all objects — it does not vary (is not "instance-specific"). In languages like Java, the `static` keyword is explicitly used. Python detects it by position: inside class, outside methods.

> **Student Question:** What happens if both a static and instance variable have the same name?
> **Answer:** Python checks instance variables first. So if an object has an instance variable named `a`, `self.a` refers to the instance copy, not the class-level static `a`. This can cause confusion — avoid giving them the same name.

> **Student Question:** Why would I ever declare an instance variable outside the class?
> **Answer:** It is technically possible (`t.new_var = 99`), but it is not a good practice. It adds a variable only to that specific object, not to all objects. Other objects of the same class will not have that variable. This is mainly used for quick testing or debugging.

> **Student Question:** Can I access a local variable after the method finishes?
> **Answer:** No. Local variables are temporary. Once the method's execution is complete, all local variables are destroyed. If you need the value later, store it as an instance variable (`self.a = ...`) or return it with a `return` statement.

---

## Key Differences — All Three Types

| Attribute | Instance Variable | Static Variable | Local Variable |
|-----------|-----------------|----------------|---------------|
| Declared with | `self` | Inside class, outside method | Inside method, no `self` |
| Scope | Throughout the class (via self) or outside (via obj ref) | Throughout the class and outside (via class name or obj ref) | Only within that method |
| Object copies | One per object | One for entire class | One per method call |
| Change effect | Only that object | All objects | No external effect |
| Lifetime | Exists as long as object exists | Exists as long as class exists | From method start to method end |
| Also called | Object-level | Class-level | Method-level / Temporary |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `AttributeError: 'Test' object has no attribute 'b'` | `self.b` accessed but the method that declares it was never called | Call the method first, or move declaration to `__init__` |
| `NameError: name 'a' is not defined` | Accessing a local variable from another method or outside | Use `self.a` if you need it across methods |
| `AttributeError: 'Test' object has no attribute 'x'` | Trying to access instance variable that was deleted with `del` | Check before accessing or re-initialize |
| Static variable not updating for all objects | Changed via object reference (`t1.a = 99`) instead of class name | Use `Test.a = 99` to update the shared static copy |

> **Tricky Detail:** If you do `t1.a = 99` when `a` is a static variable, Python does NOT change the static variable. Instead, it creates a **new instance variable** named `a` on `t1` only. To update the shared static variable, always use `ClassName.a = 99`.

---

## Interview Questions

**Q: What are the three types of variables allowed in a Python class?**
A: Instance variables (object-level) — value varies per object, declared with `self`. Static variables (class-level) — shared by all objects, declared inside class outside methods. Local variables (method-level) — temporary, exists only during method execution.

**Q: What is the difference between instance variables and static variables?**
A: Instance variables have one copy per object — each object independently holds its own values, and changing one does not affect others. Static variables have one shared copy for all objects — changing the static variable (via class name) affects all objects simultaneously.

**Q: Where can instance variables be declared?**
A: In three places: (1) inside the constructor using `self`, (2) inside any instance method using `self`, (3) outside the class using an object reference (`obj.var = value`).

**Q: What is a local variable in a class?**
A: A local variable is declared inside a method without `self`. It exists only during that method's execution and is destroyed when the method ends. It cannot be accessed from other methods or outside the class.

**Q: What happens if you delete an instance variable of one object?**
A: Only that object's copy is deleted. Other objects' copies of the same instance variable are completely unaffected. This is because each object maintains a separate copy of its instance variables.

**Q: How do you access static variables?**
A: Via the class name (`ClassName.var`) or via an object reference (`obj.var`). Using the class name is preferred and more clear in intent.

**Q: If I change `t1.a = 99` where `a` is a static variable, does it change for all objects?**
A: No. Assigning `t1.a = 99` creates a new **instance variable** `a` on `t1`, shadowing the static one. The static variable is unchanged. To change the static variable for all objects, use `ClassName.a = 99`.

---

## Try It Yourself

**Exercise 1:** Demonstrate instance variable isolation. Create a class `Box` with instance variable `color`. Create two Box objects. Change the color of one and print both — show they are independent.

<details><summary>Answer</summary>

```python
class Box:
    def __init__(self, color):
        self.color = color

b1 = Box("Red")
b2 = Box("Blue")
print(b1.color, b2.color)   # Red Blue

b1.color = "Green"
print(b1.color, b2.color)   # Green Blue  ← b2 unchanged
```
</details>

---

**Exercise 2:** Demonstrate static variable shared behavior. Create a class `School` with a static variable `school_name`. Create three objects. Change `school_name` via class name and show all objects see the change.

<details><summary>Answer</summary>

```python
class School:
    school_name = "ABC School"   # static variable

    def __init__(self, student):
        self.student = student


s1 = School("Alice")
s2 = School("Bob")
s3 = School("Carol")

print(s1.school_name, s2.school_name, s3.school_name)
# ABC School  ABC School  ABC School

School.school_name = "XYZ School"   # change static via class name
print(s1.school_name, s2.school_name, s3.school_name)
# XYZ School  XYZ School  XYZ School  ← all updated
```
</details>

---

**Exercise 3:** Show that a local variable cannot be accessed from another method. Create a class with two methods. Declare a variable in one method without `self` and try to access it in the other method.

<details><summary>Answer</summary>

```python
class Demo:
    def m1(self):
        x = 100    # local variable

    def m2(self):
        print(x)   # NameError — x is local to m1


d = Demo()
d.m1()
try:
    d.m2()
except NameError as e:
    print("Error:", e)   # Error: name 'x' is not defined

# Fix: use self to make it an instance variable
class DemoFixed:
    def m1(self):
        self.x = 100   # instance variable — accessible everywhere

    def m2(self):
        print(self.x)   # works!


d = DemoFixed()
d.m1()
d.m2()   # 100
```
</details>

---

**Exercise 4:** Demonstrate all three variable types in one class. Create `Employee` with a static `company_name`, an instance variable `emp_name` (in constructor), and a local variable inside a method. Print all of them.

<details><summary>Answer</summary>

```python
class Employee:
    company_name = "TechCorp"       # static variable

    def __init__(self, name):
        self.emp_name = name        # instance variable

    def work(self):
        task = "Coding"             # local variable
        print(f"Company: {Employee.company_name}")
        print(f"Employee: {self.emp_name}")
        print(f"Task: {task}")      # accessible only here


e1 = Employee("Alice")
e2 = Employee("Bob")

e1.work()
e2.work()
```

Output:
```
Company: TechCorp
Employee: Alice
Task: Coding
Company: TechCorp
Employee: Bob
Task: Coding
```
</details>
