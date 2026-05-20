# Day 29 — Multiple & Hybrid Inheritance, Constructor Role, Polymorphism & Overloading

← [Day 28](day_28_inheritance.md) | [Index](00_INDEX.md) | [Day 30](day_30_overriding_abstraction.md) →

---

## Quick Revision — Day 29

| # | Key Point |
|---|-----------|
| 1 | **Multiple inheritance**: `class C(A, B):` — C inherits from both A and B |
| 2 | **MRO (Method Resolution Order)**: left-to-right priority when both parents have same method |
| 3 | To access a specific parent's method manually: `ParentClass.method(self)` inside child |
| 4 | **Hybrid inheritance** = combination of multiple inheritance types (e.g., multiple + multilevel) |
| 5 | Constructor role in inheritance: if child has no constructor, priority goes to parent (following MRO) |
| 6 | **Polymorphism**: poly = many, morph = behavior — same entity showing different behavior |
| 7 | **Static polymorphism** = compile-time = **overloading** (Python does NOT support method/constructor overloading) |
| 8 | **Dynamic polymorphism** = runtime = **overriding** (Python fully supports) |
| 9 | **Operator overloading**: possible in Python using **magic methods** (`__add__`, `__mul__`, etc.) |
| 10 | Method/constructor overloading NOT possible — last method/constructor defined wins |

---

## Navigation

- **Pre-requisite:** [Day 28](day_28_inheritance.md) — Single, multilevel, hierarchical inheritance
- **Next:** [Day 30](day_30_overriding_abstraction.md) — Method overriding, super(), abstract classes
- **Related:** [Day 22](day_22_oop_intro.md) — OOP features overview

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `test16.py` | Multiple inheritance — A, B, C classes |
| `.py` file | `test17.py` | Hybrid inheritance — A, B, C, D chain |
| `.py` file | `test_constructor_inheritance.py` | Constructor role in single/multilevel/multiple |
| `.py` file | `test18.py` | Operator overloading with `__add__`, `__mul__` |
| `.py` file | `test19.py` | Method overloading NOT possible demo |
| Class | `class C(A, B):` | Multiple inheritance |
| Magic method | `def __add__(self, other):` | Overload the `+` operator |
| Magic method | `def __mul__(self, other):` | Overload the `*` operator |

---

## 1. Multiple Inheritance

> **Definition:** Creating a new class from **two or more base classes**.

```python
class C(A, B):    # C inherits from both A and B
    pass
```

```
Diagram:
  A     B         ← parent classes
   \   /
    C             ← child class (inherits from both)
```

### 1.1 Basic Example — Different Functions

```python
class A:
    def f1(self):
        print("F1 function of class A")

class B:
    def f2(self):
        print("F2 function of class B")

class C(A, B):    # multiple inheritance
    def f3(self):
        print("F3 function of class C")


c = C()
c.f1()    # from A
c.f2()    # from B
c.f3()    # from C
```

**Output:**
```
F1 function of class A
F2 function of class B
F3 function of class C
```

### 1.2 Method Resolution Order (MRO)

> **MRO** is the algorithm Python uses to decide which parent's method to call when both parents have a method with the same name.

**Rule: Priority is left-to-right (clockwise), based on the order in the `class C(A, B):` declaration.**

```python
class A:
    def f1(self):
        print("F1 function of class A")

class B:
    def f1(self):                        # same method name!
        print("F1 function of class B")

class C(A, B):    # A is listed first → A gets priority
    pass


c = C()
c.f1()    # Which f1 gets called?
```

**Output:**
```
F1 function of class A    ← A gets priority (listed first)
```

> If you change to `class C(B, A):`, then **B gets priority** and `c.f1()` prints "F1 function of class B".

```
MRO in class C(A, B):
    1. Look in C itself
    2. Look in A (left parent)
    3. Look in B (right parent)
```

### 1.3 Accessing the "Missed" Parent's Method

When A and B have the same method and A takes priority, B's version is "missed". To access it explicitly:

```python
class A:
    def f1(self):
        print("F1 function of class A")

class B:
    def f1(self):
        print("F1 function of class B")

class C(A, B):
    def f3(self):
        B.f1(self)    # explicitly call B's f1 inside C's method


c = C()
c.f1()    # A's f1 (by MRO)
c.f3()    # explicitly calls B's f1
```

**Output:**
```
F1 function of class A
F1 function of class B
```

> Syntax: `ParentClass.method_name(self)` — call the parent's method directly from within a child class method, passing `self` explicitly.

---

## 2. Hybrid Inheritance

> **Definition:** Hybrid inheritance is a **combination** of multiple inheritance types (multiple, multilevel, hierarchical, or single).

```
A     B         ← parent classes
 \   /
   C            ← child of A and B (multiple inheritance)
   |
   D            ← child of C (multilevel inheritance)
```

This is hybrid because: A,B→C is **multiple**; C→D is **multilevel**; A,B are **hierarchical siblings** of C.

```python
class A:
    def f1(self):
        print("F1 of class A")

class B:
    def f1(self):
        print("F1 of class B")

class C(A, B):          # multiple inheritance
    def f3(self):
        B.f1(self)      # explicitly access B's f1
        print("F3 of class C")

class D(C):             # multilevel inheritance
    def f4(self):
        print("F4 of class D")


d = D()
d.f1()    # A's f1 (MRO: D → C → A → B)
d.f3()    # explicitly calls B.f1, then prints F3
d.f4()    # D's own
```

**Output:**
```
F1 of class A
F1 of class B
F3 of class C
F4 of class D
```

---

## 3. Constructor Role in Inheritance

### 3.1 Single Inheritance

```
If child has constructor → child constructor runs
If child has NO constructor → parent constructor runs (automatic)
```

```python
class A:
    def __init__(self):
        print("A class constructor")

class B(A):
    def __init__(self):
        print("B class constructor")


b = B()    # Output: B class constructor (child's constructor)
```

If B has no constructor:

```python
class B(A):
    pass

b = B()    # Output: A class constructor (falls back to parent)
```

### 3.2 Multilevel Inheritance

```
C inherits B, B inherits A.
Create object for C.
If C has constructor → C's constructor runs
If C has no constructor → check B
If B has no constructor → check A
```

```python
class A:
    def __init__(self):
        print("A class constructor")

class B(A):
    def __init__(self):
        print("B class constructor")

class C(B):
    def __init__(self):
        print("C class constructor")


c = C()    # C class constructor
```

Remove C's constructor → B's runs. Remove B's too → A's runs.

### 3.3 Multiple Inheritance

```
class C(A, B): — order matters for constructor priority
If C has no constructor → MRO applies → A's constructor runs first
If A also has no constructor → B's constructor runs
```

```python
class A:
    def __init__(self):
        print("A class constructor")

class B:
    def __init__(self):
        print("B class constructor")

class C(A, B):
    pass               # no constructor


c = C()    # Output: A class constructor (A is first in MRO)
```

```python
class C(B, A):
    pass

c = C()    # Output: B class constructor (B is now first in MRO)
```

### 3.4 Constructor Role Summary

```
In any inheritance:
    1. If child class has constructor → child's constructor runs
    2. If child has no constructor → parent's constructor runs (MRO order for multiple)
    3. If parent also has no constructor → grandparent's constructor runs
    4. Priority chain follows MRO throughout
```

---

## 4. Polymorphism

> **Definition:** Poly = many, Morph = behavior/form. The ability of the same entity (function/operator) to show different behavior in different situations.

```
Polymorphism
├── Static Polymorphism  (compile-time) → Overloading
│   ├── Operator overloading ✓ (via magic methods)
│   ├── Method overloading   ✗ (NOT supported in Python)
│   └── Constructor overloading ✗ (NOT supported in Python)
└── Dynamic Polymorphism (runtime)     → Overriding
    ├── Method overriding    ✓
    └── Constructor overriding ✓
```

**Real-world analogy:** The same person behaves differently with family, friends, and strangers — one person, many behaviors. That's polymorphism.

**Python example:**
```python
# Same operator, different behavior:
print(10 + 20)         # 30   → addition
print("Hi" + " Bye")  # "Hi Bye" → concatenation
print(3 * "ha")        # "hahaha" → repetition
```

---

## 5. Operator Overloading

> **Python supports operator overloading via magic methods (dunder methods).**

Every Python operator has a corresponding magic method. When you use an operator, Python internally calls its magic method.

### 5.1 Magic Method Map

| Operator | Symbol | Magic Method |
|----------|--------|-------------|
| Addition | `+` | `__add__` |
| Subtraction | `-` | `__sub__` |
| Multiplication | `*` | `__mul__` |
| Division | `/` | `__truediv__` |
| Floor division | `//` | `__floordiv__` |
| Modulo | `%` | `__mod__` |
| Power | `**` | `__pow__` |
| Less than | `<` | `__lt__` |
| Greater than | `>` | `__gt__` |
| Less than or equal | `<=` | `__le__` |
| Greater than or equal | `>=` | `__ge__` |
| Equal | `==` | `__eq__` |

### 5.2 Without Overloading — Error

```python
class Book:
    def __init__(self, pages):
        self.pages = pages


b1 = Book(10)
b2 = Book(20)
print(b1 + b2)    # TypeError: unsupported operand type(s) for +: 'Book' and 'Book'
```

### 5.3 With `__add__` — Overloading `+`

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages    # define what + means for Book objects


b1 = Book(10)
b2 = Book(20)
print(b1 + b2)    # 30 — calls __add__ internally
```

**How it works:**
```
b1 + b2
    ↓
Python internally calls:
b1.__add__(b2)
    ↓
self = b1 → self.pages = 10
other = b2 → other.pages = 20
    ↓
return 10 + 20 = 30
```

### 5.4 With `__mul__` — Overloading `*`

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __mul__(self, other):
        return self.pages * other.pages


b1 = Book(10)
b2 = Book(20)
print(b1 + b2)    # 30
print(b1 * b2)    # 200
```

> **Key rule:** To overload any operator for custom objects, you must **override** the corresponding magic method in your class.

---

## 6. Method Overloading — NOT Supported in Python

> **Definition (general):** Method overloading = multiple methods with the same name but different numbers/types of parameters.

**In Python: NOT POSSIBLE.** When multiple methods have the same name, **only the last one is kept**. All previous definitions are replaced.

```python
class Test:
    def m1(self):
        print("No argument method")

    def m1(self, a):
        print("One argument method:", a)

    def m1(self, a, b):
        print("Two argument method:", a, b)


t = Test()
t.m1()          # TypeError: m1() missing 2 required positional arguments
t.m1(10)        # TypeError: m1() missing 1 required positional argument
t.m1(10, 20)    # Two argument method: 10 20  ← ONLY this works
```

**Why?** When Python processes the class, each new `def m1(...)` replaces the previous one. After processing all three, only `m1(self, a, b)` remains in memory.

```
After class definition:
    Test.m1 → only the LAST m1 exists (two argument version)
    The other two are gone!
```

> If you want Python-style "overloading", use default parameters:
> ```python
> def m1(self, a=None, b=None):
>     if a is None: print("No args")
>     elif b is None: print("One arg:", a)
>     else: print("Two args:", a, b)
> ```

---

## 7. Constructor Overloading — NOT Supported in Python

Same reason as method overloading — only the **last constructor** is kept.

```python
class Test:
    def __init__(self):
        print("No argument constructor")

    def __init__(self, a):       # replaces the previous __init__
        print("One argument constructor:", a)


t = Test()       # TypeError: __init__() missing 1 required positional argument: 'a'
t2 = Test(10)   # One argument constructor: 10  ← ONLY this works
```

> Only the last `__init__` is active. The first one is completely overwritten.

---

## 8. Complete Overloading vs Overriding Table

| | Overloading | Overriding |
|--|-------------|------------|
| Type | Static / compile-time | Dynamic / runtime |
| Concept | Multiple methods, same name, different params | Child redefines parent's method |
| When | Before execution | During execution |
| Python support | ✗ (method/constructor overloading) | ✓ |
| Exception | ✓ (operator overloading via magic methods) | — |
| Technique | Refinement | Replacement |

---

## 9. Student Q&A

> **Student Question:** If both parent A and parent B have `f1()`, which one does the child get?
> **Answer:** The one listed first in the class definition: `class C(A, B):` → A's `f1` takes priority. `class C(B, A):` → B's `f1` takes priority. This is Method Resolution Order (MRO) — always left-to-right based on how parents are listed.

> **Student Question:** Can I get both A's and B's `f1` when they have the same name?
> **Answer:** Yes. The one from the first listed parent comes automatically via `c.f1()`. To explicitly call the other parent's version, inside a child method use: `B.f1(self)` — pass `self` explicitly because you're calling it as an unbound method.

> **Student Question:** Why doesn't Python support method overloading?
> **Answer:** Because in Python, a function is just an object assigned to a name in a namespace. When you write `def m1(...)` twice, the second definition simply overwrites the first. There's no mechanism to keep multiple definitions of the same name. In Java/C++, the compiler handles overloading at compile time, distinguishing by parameter types — Python doesn't have that mechanism.

> **Student Question:** What is a magic method?
> **Answer:** Magic methods (also called dunder methods — Double UNDERscore on both sides) are special predefined methods in Python that the interpreter calls automatically in response to certain operations. For example, `__init__` is called when an object is created, `__add__` is called when `+` is used, `__del__` is called by GC. You can override these to customize how your class behaves with built-in operations.

---

## Key Differences — Overloading vs Overriding

| Feature | Overloading | Overriding |
|---------|-------------|------------|
| Also called | Compile-time polymorphism | Runtime polymorphism |
| Happens when | Multiple definitions in same class | Child redefines parent method |
| Python support | Only operators (via magic methods) | Yes, fully supported |
| Technique | Refinement — keep adding | Replacement — swap out |
| Method exists at | Same class | Both parent and child |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: m1() missing 2 required positional arguments` | Tried to call overloaded first version but only last version is active | Python doesn't support overloading; use default parameters instead |
| `TypeError: unsupported operand type(s) for +: 'Book' and 'Book'` | No `__add__` magic method defined | Add `def __add__(self, other):` to the class |
| Wrong parent's method called in multiple inheritance | MRO picks the wrong parent | Check the order in `class C(A, B):`; swap if needed |
| `TypeError: __init__() missing 1 required positional argument` | Constructor overloading attempted — last constructor needs 1 arg | Only last constructor is active; provide the required argument |

---

## Interview Questions

**Q: What is multiple inheritance in Python?**
A: Multiple inheritance is when a class inherits from two or more parent classes: `class C(A, B):`. Python supports multiple inheritance using the Method Resolution Order (MRO) algorithm to resolve conflicts when both parents have the same method.

**Q: What is MRO (Method Resolution Order)?**
A: MRO is the algorithm Python uses to determine the order in which parent classes are searched when a method is called in multiple inheritance. The order is left-to-right based on the parent classes listed in the class definition. For `class C(A, B):`, Python checks C → A → B in that order.

**Q: What is operator overloading in Python?**
A: Operator overloading allows you to redefine the behavior of built-in operators (`+`, `-`, `*`, etc.) for custom objects by overriding magic methods. Example: override `__add__` to define what `obj1 + obj2` means for your class.

**Q: Does Python support method overloading?**
A: No. If you define multiple methods with the same name, only the last definition is kept. All previous definitions are overwritten. For Python-style overloading, use default parameters (`def m1(self, a=None, b=None):`).

**Q: What is polymorphism?**
A: Polymorphism (poly = many, morph = behavior) is the ability of the same function, operator, or method to show different behavior depending on the situation. Python supports two types: static polymorphism (operator overloading via magic methods) and dynamic polymorphism (method overriding).

**Q: What is hybrid inheritance?**
A: Hybrid inheritance is a combination of two or more types of inheritance (multiple, multilevel, hierarchical, or single). For example, A,B → C (multiple), then C → D (multilevel) together form hybrid inheritance.

**Q: What is the constructor role in inheritance?**
A: In inheritance, if the child class has a constructor, it runs when the child object is created. If the child has no constructor, Python follows the MRO to find and call the nearest ancestor's constructor.

---

## Try It Yourself

**Exercise 1:** Create multiple inheritance — class `Flyable` with method `fly()`, class `Swimmable` with method `swim()`. Create class `Duck(Flyable, Swimmable)` with its own `quack()`. Test all three methods.

<details><summary>Answer</summary>

```python
class Flyable:
    def fly(self):
        print("Flying!")

class Swimmable:
    def swim(self):
        print("Swimming!")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack!")

d = Duck()
d.fly()
d.swim()
d.quack()
```
</details>

---

**Exercise 2:** Show MRO in action. Create class `A` and class `B` both with method `greet()`. Create `class C(A, B)` and `class D(B, A)`. Call `greet()` on objects of C and D and observe which parent's version is called.

<details><summary>Answer</summary>

```python
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):    # A has priority
    pass

class D(B, A):    # B has priority
    pass

c = C()
c.greet()   # Hello from A

d = D()
d.greet()   # Hello from B

# Inspect MRO
print(C.__mro__)   # (<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>)
print(D.__mro__)   # (<class 'D'>, <class 'B'>, <class 'A'>, <class 'object'>)
```
</details>

---

**Exercise 3:** Implement operator overloading. Create a class `Vector` with `x` and `y`. Override `__add__` to add two vectors, `__mul__` to multiply by a scalar, and `__str__` to display as `(x, y)`.

<details><summary>Answer</summary>

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)    # (4, 6)
print(v1 * 3)     # (3, 6)
```
</details>

---

**Exercise 4:** Prove method overloading is not supported. Create a class `Calculator` with three versions of `add()` (0 args, 1 arg, 2 args). Show which one actually works and which fail.

<details><summary>Answer</summary>

```python
class Calculator:
    def add(self):
        print("No args")

    def add(self, a):
        print("One arg:", a)

    def add(self, a, b):
        print("Two args:", a + b)


c = Calculator()
# c.add()         # TypeError — last add() needs 2 args
# c.add(5)        # TypeError — last add() needs 2 args
c.add(3, 4)       # Works! Output: Two args: 7
```
</details>
