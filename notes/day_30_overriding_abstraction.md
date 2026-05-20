# Day 30 — Method Overriding, `super()`, Abstract Classes & Abstraction

← [Day 29](day_29_multiple_inheritance_polymorphism.md) | [Index](00_INDEX.md) | Day 31 →

---

## Quick Revision — Day 30

| # | Key Point |
|---|-----------|
| 1 | **Method overriding**: child redefines a parent method with its own implementation |
| 2 | Overriding = **replacement** technique at **runtime** = dynamic polymorphism |
| 3 | `super().method()` — call parent's version of a method from inside a child's method |
| 4 | `super().__init__()` — call parent constructor from inside child constructor |
| 5 | **Abstract method**: `@abstractmethod` + `pass` — declaration only, no implementation |
| 6 | **Abstract class**: inherits from `ABC`; has one or more abstract methods |
| 7 | `from abc import ABC, abstractmethod` — required import |
| 8 | Abstract class **cannot be instantiated** — no direct object creation |
| 9 | Every child of abstract class **must implement all abstract methods** |
| 10 | Abstract class can also have **non-abstract (normal) methods** |

---

## Navigation

- **Pre-requisite:** [Day 29](day_29_multiple_inheritance_polymorphism.md) — Multiple/hybrid inheritance, polymorphism, operator overloading
- **Next:** Day 31 — Exception handling
- **Related:** [Day 28](day_28_inheritance.md) — Inheritance basics; [Day 22](day_22_oop_intro.md) — OOP features overview

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `test20.py` | Method overriding — Parent assets/car, Child redefines car |
| `.py` file | `test19.py` | Constructor overriding with `super().__init__()` |
| `.py` file | `abstract_demo.py` | Abstract class Vehicle, children Car and Bike |
| Method | `def car(self):` in both Parent and Child | Method overriding demo |
| Function | `super().car()` | Call parent's overridden method from child |
| Import | `from abc import ABC, abstractmethod` | Enable abstract class creation |
| Class | `class Vehicle(ABC):` | Abstract class |
| Decorator | `@abstractmethod` | Mark a method as abstract |

---

## 1. Method Overriding

### 1.1 What Is Method Overriding?

> **Definition:** If a child class is not satisfied with the parent class implementation, the child class can **redefine** the parent class methods with its own implementation. This process is called **method overriding**.

```
Overriding in inheritance:
    Parent class has method → method()
    Child class redefines → method() (different implementation)
    During execution, child's version REPLACES parent's version
```

**Key points:**
- Same method name in both parent and child
- Different implementation in each
- Replacement happens at **runtime** → Dynamic polymorphism
- Method name and parameters must match

### 1.2 Real-World Analogy (from class)

```
Parent's assets:  cash + gold + land + old auto car
                                         ↑
                                  Child doesn't want this!
                                  Child wants: Benz car
```

```python
class Parent:
    def assets(self):
        print("Cash + Gold + Land")

    def car(self):
        print("Old auto car")          # parent's version


class Child(Parent):
    # assets() not overridden → child accepts parent's assets
    def car(self):                     # overrides parent's car()
        print("Benz car")             # child's own implementation


c = Child()
c.assets()    # from Parent (not overridden — child accepted it)
c.car()       # Child's version — REPLACES parent's car
```

**Output:**
```
Cash + Gold + Land
Benz car
```

### 1.3 Execution Flow of Overriding

```
During runtime, when c.car() is called:

  Python checks Child class first
    ↓
  Child has car() method → use Child's car()  ← replacement!
    ↓
  Parent's car() is ignored (overridden/replaced)
```

> This replacement at runtime is why it's called **dynamic polymorphism** — the code that runs is determined at execution time, not at compile time.

---

## 2. Using `super()` — Accessing Parent's Overridden Method

Sometimes, the child wants its **own implementation AND** the parent's implementation. Use `super()`.

### 2.1 `super()` with Methods

```python
class Parent:
    def assets(self):
        print("Cash + Gold + Land")

    def car(self):
        print("Old auto car")


class Child(Parent):
    def car(self):
        super().car()              # first, call parent's car()
        print("Benz car")         # then, add child's own
        # OR: call super().car() at the end:
        # print("Benz car")
        # super().car()


c = Child()
c.assets()
c.car()
```

**Output:**
```
Cash + Gold + Land
Old auto car
Benz car
```

> `super()` returns a proxy object that refers to the **parent class**. `super().car()` means "call the parent class's `car()` method".

### 2.2 `super().__init__()` — Constructor Overriding

**Without `super()`:**

```python
class Parent:
    def __init__(self):
        print("Parent class constructor")


class Child(Parent):
    def __init__(self):
        print("Child class constructor")
        # Parent's constructor is overridden — it won't run


c = Child()
```

**Output:**
```
Child class constructor
```

**With `super().__init__()`:**

```python
class Parent:
    def __init__(self):
        print("Parent class constructor")


class Child(Parent):
    def __init__(self):
        super().__init__()         # call parent's constructor too
        print("Child class constructor")


c = Child()
```

**Output:**
```
Parent class constructor
Child class constructor
```

### 2.3 `super()` Summary

```python
# To call parent's method from inside child:
super().method_name()

# To call parent's constructor from inside child's constructor:
super().__init__()
super().__init__(arg1, arg2)   # if parent constructor has parameters
```

---

## 3. When Overriding Happens Automatically

> **By default, constructor is overridden.** If both parent and child have constructors, the child's runs when a child object is created — the parent's is automatically "replaced" (overridden).

```python
class Parent:
    def __init__(self):
        print("Parent constructor")


class Child(Parent):
    def __init__(self):
        print("Child constructor")


c = Child()    # Child constructor  ← parent's overridden automatically
```

To also run the parent's constructor, add `super().__init__()` inside the child's constructor.

---

## 4. Overloading vs Overriding — Final Comparison

| | Overloading | Overriding |
|--|-------------|------------|
| Type | Static / compile-time | Dynamic / runtime |
| Where | Same class, multiple methods | Parent vs Child class |
| Python support | ✗ method/constructor; ✓ operator | ✓ fully supported |
| Technique | Refinement | Replacement |
| Method name | Same | Same |
| Parameters | Different | Same (usually) |
| Implementation | Multiple tasks for same method | Child replaces parent's task |

---

## 5. Abstract Classes and Abstract Methods

### 5.1 What Is an Abstract Method?

> **A method which does NOT contain any implementation — only a declaration (signature) — is called an abstract method.**

```python
@abstractmethod
def wheels(self):
    pass
```

- `@abstractmethod` decorator → marks it as abstract
- `pass` → no implementation (body is empty)
- **Must** be overridden (implemented) in every child class

### 5.2 What Is an Abstract Class?

> **A class which contains one or more abstract methods is called an abstract class.**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):         # inherit from ABC to become abstract
    @abstractmethod
    def wheels(self):       # abstract method
        pass

    def engine_type(self):  # non-abstract method (has implementation)
        print("BS6 Engine")
```

**Key facts about abstract class:**

```
Abstract Class Rules
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Must inherit from capital ABC (Abstract Base Class)
2. Must have at least one abstract method
3. CAN also have non-abstract (normal) methods
4. Contains PARTIAL implementation (some abstract + some normal)
5. CANNOT be instantiated directly (no object creation)
6. Every child class MUST implement ALL abstract methods
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.3 Why Use Abstract Classes?

**Problem without abstract class:**

```python
class Vehicle:
    def wheels(self):
        return 4    # Fixed at 4 — wrong for bikes, buses, trucks!
```

A Car has 4 wheels, a Bike has 2 wheels, a Bus has 6+ wheels. As the Vehicle class author, you don't know how many wheels each vehicle will have — **the child classes should decide**.

**Solution — make `wheels()` abstract:**

```python
class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass    # No implementation — child must implement this
```

Now every child class is **forced** to implement `wheels()`. If they don't, Python raises `TypeError` when you try to create an object.

> **Why declare it at all if you don't know the implementation?** Because declaring it as abstract **mandates** that all child classes must implement it. Without the abstract declaration, child classes can skip the implementation — there's no guarantee.

### 5.4 The `abc` Module

```python
from abc import ABC, abstractmethod
```

| Name | What it is | Purpose |
|------|-----------|---------|
| `ABC` | Abstract Base Class (predefined class) | Your abstract class must inherit from this |
| `abstractmethod` | Decorator | Marks a method as abstract |

> In other languages (Java, C#), you use the keyword `abstract`. In Python, you use `ABC` (inheritance) + `@abstractmethod` (decorator).

---

## 6. Complete Abstract Class Example

### 6.1 Vehicle Example — Full Code

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):           # abstract class (inherits ABC)
    @abstractmethod
    def wheels(self):         # abstract method — no implementation
        pass

    @abstractmethod
    def color(self):          # second abstract method
        pass

    def engine_type(self):    # non-abstract method — common to all
        print("BS6 Engine")


class Car(Vehicle):           # concrete child class
    def wheels(self):         # MUST implement abstract method
        print("Car has 4 wheels")

    def color(self):          # MUST implement second abstract method
        print("Car color: Red")


class Bike(Vehicle):          # concrete child class
    def wheels(self):
        print("Bike has 2 wheels")

    def color(self):
        print("Bike color: Black")


# Cannot create object for abstract class:
# v = Vehicle()   # TypeError: Can't instantiate abstract class Vehicle
#                               with abstract methods wheels, color

# Can create objects for child classes:
c = Car()
c.wheels()          # Car has 4 wheels
c.color()           # Car color: Red
c.engine_type()     # BS6 Engine  ← inherited from parent

b = Bike()
b.wheels()          # Bike has 2 wheels
b.color()           # Bike color: Black
b.engine_type()     # BS6 Engine
```

**Output:**
```
Car has 4 wheels
Car color: Red
BS6 Engine
Bike has 2 wheels
Bike color: Black
BS6 Engine
```

### 6.2 What Happens If Child Doesn't Implement an Abstract Method?

```python
class Truck(Vehicle):
    def wheels(self):
        print("Truck has 10 wheels")
    # color() not implemented!


t = Truck()    # TypeError: Can't instantiate abstract class Truck with abstract method color
```

> Python forces every child to implement **every** abstract method. If even one is missing, the child class itself becomes abstract and cannot be instantiated.

### 6.3 Abstract Class Diagram

```
from abc import ABC, abstractmethod

class Vehicle(ABC):           ← abstract class
   │
   ├── @abstractmethod        ← abstract method (no body except pass)
   │   def wheels(self):
   │       pass
   │
   └── def engine_type(self): ← non-abstract method (has implementation)
           print("BS6 Engine")

            │
     ┌──────┴──────┐
     │             │
  class Car      class Bike    ← concrete child classes
  def wheels():  def wheels():
      4 wheels       2 wheels
```

---

## 7. Abstract Class vs Normal Class vs Interface

| Feature | Normal Class | Abstract Class | Interface (Python) |
|---------|-------------|----------------|-------------------|
| Object creation | Yes | No (cannot instantiate) | No |
| Methods | All implemented | Mix: some abstract + some normal | All abstract (by convention) |
| Inheritance required | Optional | Yes (inherit ABC) | Yes (inherit ABC) |
| Use case | Direct use | Template for child classes | Contract for unrelated classes |

> Python does not have a separate `interface` keyword. You achieve interface-like behavior using abstract classes where all methods are abstract.

---

## 8. Complete Walkthrough

**Step 1:** Import required components

```python
from abc import ABC, abstractmethod
```

**Step 2:** Create abstract class (must inherit ABC)

```python
class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass

    def engine_type(self):
        print("BS6 Engine")
```

**Step 3:** Try to create object for abstract class (intentional error)

```python
v = Vehicle()    # TypeError: Can't instantiate abstract class Vehicle...
```

**Step 4:** Create concrete child classes

```python
class Car(Vehicle):
    def wheels(self):
        print("4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("2 wheels")
```

**Step 5:** Create objects for children and call methods

```python
c = Car()
c.wheels()
c.engine_type()

b = Bike()
b.wheels()
b.engine_type()
```

---

## 9. Student Q&A

> **Student Question:** What is the difference between overriding and overloading?
> **Answer:** Overriding = replacement — child class has the same method name as parent but with different implementation; child's version replaces parent's at runtime. Overloading = refinement — same class has multiple methods with same name but different parameters; Python does NOT support method overloading (only operator overloading via magic methods).

> **Student Question:** If I override a method in the child class, can I still access the parent's version?
> **Answer:** Yes! Use `super().method_name()` inside the child class method. This calls the parent's version. You can call it before or after your child's implementation, or conditionally.

> **Student Question:** Why can't we create an object for an abstract class?
> **Answer:** Because an abstract class has methods with no implementation. If Python allowed creating objects, you could call `v.wheels()` on a `Vehicle` object, but `wheels()` has no code to run — it would crash. Python prevents this by blocking object creation for abstract classes.

> **Student Question:** Can an abstract class have regular (non-abstract) methods?
> **Answer:** Yes. Abstract class contains **partial implementation** — some methods are abstract (no implementation, to be completed by children) and some are non-abstract (fully implemented, common behavior shared by all children). Example: `engine_type()` is non-abstract because all vehicles (car, bike, bus) have the same BS6 engine.

> **Student Question:** If a child class doesn't implement all abstract methods, what happens?
> **Answer:** The child class itself becomes abstract — you cannot create objects for it either. Python raises `TypeError: Can't instantiate abstract class ChildClass with abstract method method_name`. Every child in the chain must implement ALL abstract methods to become a concrete (instantiable) class.

---

## Key Differences — Overriding vs Abstract Method

| | Method Overriding | Abstract Method |
|--|-------------------|-----------------|
| Where | Child redefines parent method | Parent declares, child must implement |
| Parent has implementation? | Yes | No (only `pass`) |
| Child must implement? | No (optional — they can use parent's) | Yes (mandatory) |
| Keyword/decorator | None needed | `@abstractmethod` |
| Can skip? | Yes — child can inherit parent's version | No — child must implement or stay abstract |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: Can't instantiate abstract class Vehicle with abstract method wheels` | Trying to create object for abstract class | Create object for a child class that implements all abstract methods |
| `TypeError: Can't instantiate abstract class Car with abstract method color` | Child class didn't implement all abstract methods | Implement every abstract method in the child class |
| `AttributeError: 'super' object has no attribute 'method_name'` | Calling `super().method_name()` but parent doesn't have that method | Check parent class has the method you're trying to call via super() |
| `ImportError: cannot import name 'ABC' from 'abc'` | Import typo | Use `from abc import ABC, abstractmethod` (capital ABC) |
| Abstract method body has code | Misunderstanding — abstract methods should be empty | Use `pass` as the body of abstract methods |

---

## Interview Questions

**Q: What is method overriding in Python?**
A: Method overriding is when a child class redefines a method from the parent class with its own implementation. The child's version replaces the parent's at runtime. This is dynamic polymorphism — the decision of which method to call is made at program execution time.

**Q: What is the `super()` function in Python?**
A: `super()` returns a proxy object representing the parent class. It is used inside a child class to call parent class methods or the parent constructor. `super().method()` calls the parent's method. `super().__init__()` calls the parent's constructor.

**Q: What is an abstract class in Python?**
A: An abstract class is a class that contains one or more abstract methods and inherits from `ABC` (from the `abc` module). It represents an incomplete class — it cannot be instantiated directly. Child classes must implement all abstract methods before they can be instantiated.

**Q: What is an abstract method?**
A: An abstract method is a method that has only a declaration (signature) but no implementation. It is marked with `@abstractmethod` decorator and has `pass` as its body. Every child class that inherits the abstract class must implement (override) all abstract methods.

**Q: Why do we use abstract classes?**
A: Abstract classes act as a template or blueprint. They declare what methods child classes must implement, without specifying how. This is useful when the parent knows WHAT operations are needed but not HOW they should work for each child (e.g., Vehicle knows all vehicles have wheels, but doesn't know how many each type has).

**Q: Can abstract classes have non-abstract methods?**
A: Yes. Abstract classes contain partial implementation — some methods are abstract (to be implemented by children) and some are fully implemented normal methods (common behavior shared by all children).

**Q: What is the difference between method overriding and abstract methods?**
A: In overriding, the parent already has a full implementation but the child redefines it. Abstract methods have NO implementation in the parent — the child is FORCED to provide one. Overriding is optional (child can inherit parent's version); implementing abstract methods is mandatory.

---

## Try It Yourself

**Exercise 1:** Demonstrate method overriding. Create a `Payment` parent class with a `process()` method. Create child classes `CreditCard` and `UPI` that each override `process()` with their own message. Call the method on objects of each child.

<details><summary>Answer</summary>

```python
class Payment:
    def process(self):
        print("Processing generic payment")


class CreditCard(Payment):
    def process(self):
        print("Processing credit card payment via Visa network")


class UPI(Payment):
    def process(self):
        print("Processing UPI payment via BHIM app")


cc = CreditCard()
upi = UPI()
cc.process()    # CreditCard's version
upi.process()   # UPI's version
```
</details>

---

**Exercise 2:** Demonstrate `super()`. Create a `Vehicle` parent class with constructor that prints "Vehicle created". Create `Car` child class that also calls parent's constructor using `super().__init__()`.

<details><summary>Answer</summary>

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle created: {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)        # call parent constructor
        self.model = model
        print(f"Car model: {self.model}")


c = Car("Toyota", "Camry")
```

Output:
```
Vehicle created: Toyota
Car model: Camry
```
</details>

---

**Exercise 3:** Create an abstract class `Shape` with abstract methods `area()` and `perimeter()`. Create concrete classes `Rectangle` and `Circle` that implement both. Try to create a Shape object and observe the error.

<details><summary>Answer</summary>

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Shape object — will fail
try:
    s = Shape()
except TypeError as e:
    print("Error:", e)

r = Rectangle(5, 3)
print(f"Rectangle area: {r.area()}, perimeter: {r.perimeter()}")

c = Circle(7)
print(f"Circle area: {c.area():.2f}, perimeter: {c.perimeter():.2f}")
```
</details>

---

**Exercise 4:** Show what happens when a child doesn't implement all abstract methods. Create abstract class `Animal` with abstract methods `sound()` and `move()`. Create a child `Dog` that only implements `sound()` but not `move()`. Try to create a Dog object.

<details><summary>Answer</summary>

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Woof!")
    # move() NOT implemented!


try:
    d = Dog()    # TypeError — move() is still abstract
except TypeError as e:
    print("Error:", e)
    # Error: Can't instantiate abstract class Dog with abstract method move

# Fix — implement move() too:
class DogFixed(Animal):
    def sound(self):
        print("Woof!")

    def move(self):
        print("Dog runs on 4 legs")


d = DogFixed()
d.sound()
d.move()
```
</details>
