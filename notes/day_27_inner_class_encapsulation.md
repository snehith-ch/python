# Day 27 — Inner Classes & Encapsulation

← [Day 26](day_26_static_variables_gc_destructor.md) | [Index](00_INDEX.md) | [Day 28](day_28_inheritance.md) →

---

## Quick Revision — Day 27

| # | Key Point |
|---|-----------|
| 1 | **Inner class** = a class declared inside another class |
| 2 | Use inner class when: without the outer object, the inner object cannot exist |
| 3 | To create inner class object: `inner_obj = outer_obj.InnerClass()` |
| 4 | **Public** variable/method: no underscore → accessible anywhere |
| 5 | **Protected** variable/method: single underscore `_var` → accessible in class and child classes |
| 6 | **Private** variable/method: double underscore `__var` → accessible only within same class |
| 7 | **Encapsulation** = restricting access to variables/methods to prevent modification |
| 8 | Private variables CANNOT be accessed outside the class — `AttributeError` |
| 9 | Private methods are called with `self.__method()` inside the class only |
| 10 | Even a child class cannot access the parent's private variables |

---

## Navigation

- **Pre-requisite:** [Day 26](day_26_static_variables_gc_destructor.md) — Static variable access/delete, GC, destructor
- **Next:** [Day 28](day_28_inheritance.md) — Inheritance (single, multilevel, hierarchical, multiple)
- **Related:** [Day 22](day_22_oop_intro.md) — OOP intro, features overview

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `inner_class_demo.py` | Outer and inner class creation and access |
| `.py` file | `test12.py` | Public, protected, private variables demo |
| `.py` file | `test12b.py` | Parent-child access restriction on private vars |
| `.py` file | `car_demo.py` | Private method (`__update_software`) demo |
| `.py` file | `car_speed.py` | Private variable preventing modification |
| Class | `class Outer:` / `class Inner:` | Inner class inside outer class |
| Variable | `x = 10` / `_y = 20` / `__z = 30` | Public / Protected / Private |

---

## 1. Inner Classes

### 1.1 What Is an Inner Class?

An **inner class** is a class declared inside another class.

```python
class Outer:           # outer class
    class Inner:       # inner class — lives inside Outer
        pass
```

The outer class is sometimes called the **outer class** or **enclosing class**. The class inside is the **inner class** or **nested class**.

### 1.2 When to Use Inner Classes

> **Rule:** Without existing one type of object, if there is no chance of existing another type of object → use an inner class.

**Real-world examples:**

| Without this | You can't have this |
|---|---|
| Car | Engine |
| Human | Brain |
| University | Department |
| Book | Chapter |

```
class Car:           ← outer class (car must exist first)
    class Engine:    ← inner class (engine only makes sense inside a car)
```

### 1.3 Creating and Accessing Inner Class

```python
class Outer:
    def __init__(self):
        print("Outer class constructor")

    def f1(self):
        print("Outer class method")

    class Inner:
        def __init__(self):
            print("Inner class constructor")

        def m1(self):
            print("Inner class method")
```

**Option 1 — Separate object references (recommended when both classes have methods):**

```python
o = Outer()            # create outer object → outer constructor runs
i = o.Inner()          # create inner object → inner constructor runs
i.m1()                 # call inner method

o.f1()                 # call outer method
```

**Output:**
```
Outer class constructor
Inner class constructor
Inner class method
Outer class method
```

**Option 2 — Chained creation (when only inner class is needed):**

```python
i = Outer.Inner()      # creates both outer and inner objects in one line
i.m1()
```

**Option 3 — Fully chained access (without storing references):**

```python
Outer.Inner().m1()     # creates outer, creates inner, calls m1 — no variables stored
```

### 1.4 Access Flow Diagram

```
Outer class (Car)
│
└── Inner class (Engine)
         │
         └── Methods of Inner class

To access Inner, you MUST go through Outer:

  Step 1: o = Outer()         ← outer object created
  Step 2: i = o.Inner()       ← inner object created via outer reference
  Step 3: i.m1()              ← inner method called via inner reference
```

### 1.5 Why Option 1 is Better When Both Classes Have Methods

```python
o = Outer()
i = o.Inner()

o.f1()    # outer method — called on outer object
i.m1()    # inner method — called on inner object
```

If you use `Outer.Inner().m1()`, the outer constructor runs again each time — constructor is called twice unnecessarily when you need to call both `f1` and `m1`.

---

## 2. Encapsulation

### 2.1 What Is Encapsulation?

> **Definition:** Encapsulation is the process of providing restriction to access variables and methods.

**Why?** To **prevent data from modification** — if someone tries to modify your internal variables or logic, encapsulation stops them.

**How?** By making variables and methods **private**.

```
Encapsulation Goal:
  Prevent modification of internal data by outsiders
        ↓
  Make variables and methods private
        ↓
  Private members → accessible only within the class they are declared in
```

### 2.2 Access Modifiers in Python

Unlike Java or C# which have keywords (`private`, `protected`, `public`), Python uses **naming conventions** (underscore symbols):

| Type | Syntax | Convention | Where Accessible |
|------|--------|-----------|-----------------|
| Public | `x = 10` | No underscore | Anywhere — class, child class, outside |
| Protected | `_y = 20` | Single underscore | Class + child classes (convention only — not strictly enforced) |
| Private | `__z = 30` | Double underscore | Only within the same class (strictly enforced) |

```python
class Test:
    x = 10      # public
    _y = 20     # protected
    __z = 30    # private
```

### 2.3 Access Within the Class — All Three Work

```python
class Test:
    def __init__(self):
        self.x = 10      # public instance variable
        self._y = 20     # protected
        self.__z = 30    # private

        # All accessible within the class:
        print(self.x)    # 10
        print(self._y)   # 20
        print(self.__z)  # 30


t = Test()    # prints 10, 20, 30
```

### 2.4 Access Outside the Class

```python
class Test:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.__z = 30


t = Test()
print(t.x)    # 10  — public, works fine
print(t._y)   # 20  — protected, technically works (convention only)
print(t.__z)  # AttributeError — private, strictly blocked!
```

**Output:**
```
10
20
AttributeError: 'Test' object has no attribute '__z'
```

> **Why does protected work outside the class?** Python does not enforce protected access. The single underscore `_` is just a **convention** — a signal to other programmers saying "treat this as internal." Python itself does not block access.

> **Why does private fail?** Python applies **name mangling** to double-underscore attributes. `__z` becomes `_Test__z` internally. That's why `t.__z` fails — the actual attribute name is `_Test__z`. This is how Python enforces privacy.

### 2.5 Access in Child Classes

```python
class Parent:
    x = 10      # public
    _y = 20     # protected
    __z = 30    # private


class Child(Parent):
    def show(self):
        print(Parent.x)    # 10  — public, accessible in child
        print(Parent._y)   # 20  — protected, accessible in child
        print(Parent.__z)  # AttributeError — private, NOT accessible even in child!


c = Child()
c.show()
```

**Output:**
```
10
20
AttributeError: type object 'Parent' has no attribute '_Child__z'
```

> **Key rule:** Private variables belong exclusively to the class they are declared in. **Not even child classes can access parent's private variables.**

### 2.6 Access Modifier Summary Diagram

```
        Public (_x=10)     Protected (_y=20)     Private (__z=30)
        ──────────────     ─────────────────     ────────────────
Same class:   ✓                   ✓                    ✓
Child class:  ✓                   ✓                    ✗
Outside:      ✓                   ✓ (convention)        ✗
```

---

## 3. Private Methods

Just as variables can be private, **methods** can also be private using the double underscore prefix.

### 3.1 Private Method Example

```python
class Car:
    def __init__(self):
        pass
        self.__update_software()    # calling private method INSIDE the class ✓

    def __update_software(self):    # private method
        print("Updating car software")
        print("Software updated successfully")


c = Car()    # constructor calls __update_software internally — works
```

**Output:**
```
Updating car software
Software updated successfully
```

**Trying to access private method outside the class:**

```python
c = Car()
c.__update_software()    # AttributeError — private method, not accessible outside
```

**Output:**
```
AttributeError: 'Car' object has no attribute '__update_software'
```

### 3.2 Why Private Methods?

You might have internal helper methods that implement sensitive logic. By making them private, you ensure:
- External code cannot call them directly
- External code cannot modify their behavior
- The internal logic is protected

---

## 4. Private Variables — Preventing Modification

```python
class Car:
    def __init__(self, car_name):
        self.__name = car_name           # private
        self.__max_speed = 100           # private

    def drive(self):
        print(f"Car: {self.__name}")
        print(f"Driving at speed: {self.__max_speed}")


c = Car("Ferrari")
c.drive()

# Attempt to change private variable from outside:
c.__max_speed = 200    # This does NOT change the actual private variable!
c.drive()              # Still shows 100!
```

**Output:**
```
Car: Ferrari
Driving at speed: 100
Car: Ferrari
Driving at speed: 100   ← unchanged! private variable protected
```

> **Why didn't `c.__max_speed = 200` work?** Because Python creates a **new attribute** `__max_speed` on the object (as a public attribute), while the actual private attribute is stored as `_Car__max_speed`. The `drive()` method still reads `self.__max_speed` which refers to `_Car__max_speed` = 100.

**Contrast — public variable (no protection):**

```python
class Car:
    def __init__(self, car_name):
        self.name = car_name
        self.max_speed = 100    # public

    def drive(self):
        print(f"Car: {self.name}, Speed: {self.max_speed}")


c = Car("Ferrari")
c.drive()              # Speed: 100

c.max_speed = 200      # public variable CAN be changed from outside
c.drive()              # Speed: 200 — changed!
```

> This is exactly why we use encapsulation — to prevent unwanted modification of sensitive data like `max_speed`.

---

## 5. Name Mangling — Python's Privacy Mechanism

Python does not truly "hide" private attributes. Instead it renames them:

```
self.__var_name  →  internally stored as  _ClassName__var_name
```

This is called **name mangling**. You can still access private attributes if you know the mangled name (but you should never do this — it breaks encapsulation):

```python
class Test:
    def __init__(self):
        self.__secret = 42


t = Test()
# print(t.__secret)       # AttributeError
print(t._Test__secret)   # 42  — name mangling bypassed (not recommended!)
```

---

## 6. Student Q&A

> **Student Question:** Can we access a protected variable outside the class?
> **Answer:** Yes — technically Python does not block it. `t._y` will work. But the single underscore is a **convention** telling other programmers "this is internal — don't access it from outside." It is not enforced by Python. Double underscore (`__`) is what Python actually enforces.

> **Student Question:** Why can't the child class access the parent's private variable?
> **Answer:** Because private variables are strictly restricted to the class they are declared in. Python applies name mangling: `__z` in `Parent` becomes `_Parent__z`. When a child class tries `Parent.__z`, Python cannot find `_Parent__z` under the child's scope — so `AttributeError` is raised.

> **Student Question:** If I write `c.__max_speed = 200` outside the class, why doesn't it change the speed?
> **Answer:** Because Python creates a **new public attribute** `__max_speed` on the object `c`. The actual private attribute is stored as `_Car__max_speed`. The `drive()` method accesses `_Car__max_speed` (which is still 100). The new `__max_speed = 200` is a completely different attribute that the method never reads.

> **Student Question:** When should I use inner classes?
> **Answer:** When the inner object cannot logically exist without the outer object. Example: a `Car` and its `Engine` — an engine alone doesn't make sense without a car context. In practice, inner classes are used for helper classes, iterators, and data containers that are tightly tied to the enclosing class.

---

## Key Differences — Public vs Protected vs Private

| | Public | Protected | Private |
|--|--------|-----------|---------|
| Syntax | `var` (no prefix) | `_var` | `__var` |
| Same class access | ✓ | ✓ | ✓ |
| Child class access | ✓ | ✓ | ✗ |
| Outside class access | ✓ | ✓ (convention) | ✗ |
| Python enforcement | None | Convention only | Name mangling |
| Internal storage | `var` | `_var` | `_ClassName__var` |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `AttributeError: 'Test' object has no attribute '__z'` | Accessing private variable outside the class | Access only within the class using `self.__z` |
| `AttributeError: type object 'Parent' has no attribute '_Child__z'` | Child class trying to access parent's private variable | Private variables are class-only; don't access from child |
| `AttributeError: 'Car' object has no attribute '__update_software'` | Calling private method outside the class | Private methods can only be called inside the class (`self.__update_software()`) |
| Private variable not changing from outside | `c.__max_speed = 200` creates a new attribute, not modifying the real one | Encapsulation is working as designed — modify via a public setter method inside the class |

---

## Interview Questions

**Q: What is encapsulation in Python?**
A: Encapsulation is the process of restricting access to variables and methods to prevent unauthorized modification. It is achieved by making variables and methods private (using double underscore prefix). The goal is to protect internal data from being changed by code outside the class.

**Q: How do you make a variable private in Python?**
A: By prefixing it with double underscore: `self.__variable_name`. Python applies name mangling to store it as `_ClassName__variable_name`, making it inaccessible from outside the class.

**Q: What is the difference between public, protected, and private in Python?**
A: Public (no underscore): accessible everywhere. Protected (single underscore `_var`): convention for internal use — accessible everywhere but signals "don't use outside class/child". Private (double underscore `__var`): enforced restriction — only accessible within the declaring class; name mangling prevents external access.

**Q: Can a child class access the parent's private variables?**
A: No. Private variables are restricted to the class they are declared in. Even child classes cannot access them.

**Q: What is an inner class?**
A: An inner class is a class declared inside another class. It is used when one object logically cannot exist without another — for example, an Engine inside a Car. To create an inner class object, you must first create an outer class object: `inner_obj = outer_obj.InnerClass()`.

**Q: What is name mangling in Python?**
A: Name mangling is Python's mechanism for enforcing privacy. When you declare `self.__var`, Python stores it as `_ClassName__var`. This means `obj.__var` from outside will fail (wrong name), while `self.__var` inside the class works (Python resolves the name correctly within the class scope).

---

## Try It Yourself

**Exercise 1:** Create a class `Employee` with public `name`, protected `_department`, and private `__salary`. Try accessing all three from outside the class and observe the results.

<details><summary>Answer</summary>

```python
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self._department = dept
        self.__salary = salary


e = Employee("Alice", "IT", 60000)
print(e.name)           # Alice  — public, works
print(e._department)    # IT     — protected, works (convention only)
try:
    print(e.__salary)   # AttributeError — private!
except AttributeError as err:
    print("Error:", err)
```
</details>

---

**Exercise 2:** Create a class `BankAccount` with a private `__balance`. Add a `deposit(amount)` method and a `get_balance()` method (inside the class) to safely access the balance. Show that direct outside access fails but method access works.

<details><summary>Answer</summary>

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance       # controlled access via method


acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())    # 1500 — works through method

try:
    print(acc.__balance)    # AttributeError — direct access blocked
except AttributeError as e:
    print("Error:", e)
```
</details>

---

**Exercise 3:** Create an `Outer` class with a method `greet()`. Inside it, create an `Inner` class with a method `info()`. Demonstrate all three ways to access the inner class.

<details><summary>Answer</summary>

```python
class Outer:
    def __init__(self):
        print("Outer constructor")

    def greet(self):
        print("Hello from Outer!")

    class Inner:
        def __init__(self):
            print("Inner constructor")

        def info(self):
            print("Info from Inner!")


# Option 1 — separate references
o = Outer()
i = o.Inner()
o.greet()
i.info()

# Option 2 — chained creation
print("---")
i2 = Outer.Inner()
i2.info()

# Option 3 — fully chained, no variable
print("---")
Outer.Inner().info()
```
</details>

---

**Exercise 4:** Create a `Car` class with a private method `__check_engine()` that prints "Engine OK". Call this private method from the constructor. Then try to call it from outside the class and handle the error.

<details><summary>Answer</summary>

```python
class Car:
    def __init__(self, model):
        self.model = model
        self.__check_engine()       # private method called internally

    def __check_engine(self):
        print(f"{self.model}: Engine OK")


c = Car("Tesla")    # prints "Tesla: Engine OK"

try:
    c.__check_engine()   # should fail
except AttributeError as e:
    print("Error:", e)   # private method not accessible outside
```
</details>
