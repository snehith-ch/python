# Day 26 — Static Variables (Access & Delete), Garbage Collector & Destructor

← [Day 25](day_25_types_of_methods.md) | [Index](00_INDEX.md) | [Day 27](day_27_inner_class_encapsulation.md) →

---

## Quick Revision — Day 26

| # | Key Point |
|---|-----------|
| 1 | Static variables accessed via `self`, `cls`, or class name depending on method type |
| 2 | Inside static method → only class name works (no `self` or `cls` available) |
| 3 | Delete static variable: `del ClassName.var_name` — works from anywhere |
| 4 | Once a static variable is deleted, it cannot be accessed in any subsequent code |
| 5 | **Garbage Collector (GC)** provides automatic memory management in Python |
| 6 | `gc.isenabled()` → True/False; `gc.disable()` → turns off GC; `gc.enable()` → turns on GC |
| 7 | **Destructor** = `__del__(self)` — special method called by GC before deallocating memory |
| 8 | Destructor does NOT delete objects — only does cleanup; GC deletes the object |
| 9 | Constructor builds; Destructor cleans up |
| 10 | We never call the destructor explicitly — GC handles it automatically |

---

## Navigation

- **Pre-requisite:** [Day 25](day_25_types_of_methods.md) — Types of methods (instance, class, static)
- **Next:** [Day 27](day_27_inner_class_encapsulation.md) — Inner classes and Encapsulation
- **Related:** [Day 24](day_24_types_of_variables.md) — Static vs instance vs local variables

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `test9.py` | Static variable access from all 5 places |
| `.py` file | `test10.py` | GC module demo (`isenabled`, `disable`, `enable`) |
| `.py` file | `test11.py` | Destructor `__del__` demo with `time.sleep` |
| Variable | `a = 100` inside class | Static variable |
| Module | `import gc` | Garbage collector module |
| Method | `def __del__(self):` | Destructor |

---

## 1. Static Variables — Where Can They Be Accessed?

Recall from Day 24: a **static variable** is declared inside the class but outside any method. It is shared by all objects.

Now the question is: **from which places can we access static variables?**

```
Static Variable Access Rules
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Place 1: Inside the constructor     → self.var  OR  ClassName.var
Place 2: Inside instance method     → self.var  OR  ClassName.var
Place 3: Inside class method        → cls.var   OR  ClassName.var
Place 4: Inside static method       → ClassName.var  ONLY
          (no self or cls available in static method)
Place 5: Outside the class          → obj_ref.var  OR  ClassName.var
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 1.1 Complete Demonstration

```python
class Test:
    a = 100    # static variable

    # Place 1: Inside constructor
    def __init__(self):
        print("Inside constructor:", self.a)
        print("Inside constructor:", Test.a)

    # Place 2: Inside instance method
    def m1(self):
        print("Inside instance method:", self.a)
        print("Inside instance method:", Test.a)

    # Place 3: Inside class method
    @classmethod
    def m2(cls):
        print("Inside class method:", cls.a)
        print("Inside class method:", Test.a)

    # Place 4: Inside static method — class name ONLY
    @staticmethod
    def m3():
        print("Inside static method:", Test.a)
        # self.a or cls.a → NOT POSSIBLE here


t = Test()        # triggers constructor (Place 1)
t.m1()            # instance method  (Place 2)
Test.m2()         # class method     (Place 3)
Test.m3()         # static method    (Place 4)

# Place 5: Outside the class
print("Outside class (obj ref):", t.a)
print("Outside class (class name):", Test.a)
```

**Output:**
```
Inside constructor: 100
Inside constructor: 100
Inside instance method: 100
Inside instance method: 100
Inside class method: 100
Inside class method: 100
Inside static method: 100
Outside class (obj ref): 100
Outside class (class name): 100
```

> **Why only class name in static method?** Because static methods are declared without `self` and without `cls` — there is no reference to either the object or the class available. The only way to access a class-level variable is by using the actual class name.

---

## 2. Deleting Static Variables

### 2.1 Syntax

```
Anywhere in the program:
    del ClassName.var_name
```

That's the **only** syntax to delete a static variable.

### 2.2 Delete After Constructor — Blocks Subsequent Access

```python
class Test:
    a = 100    # static variable

    def __init__(self):
        print("Inside constructor:", Test.a)
        del Test.a                   # delete static variable here
        print("Deleted inside constructor")

    def m1(self):
        print("Inside instance method:", Test.a)   # ERROR after deletion

    @classmethod
    def m2(cls):
        print("Inside class method:", cls.a)        # ERROR after deletion


t = Test()     # constructor runs → prints 100 → deletes 'a'
t.m1()         # AttributeError: type object 'Test' has no attribute 'a'
```

**Output:**
```
Inside constructor: 100
Deleted inside constructor
AttributeError: type object 'Test' has no attribute 'a'
```

### 2.3 Delete After Instance Method — Blocks Later Access

```python
class Test:
    a = 100

    def __init__(self):
        print("Constructor:", Test.a)    # accessible

    def m1(self):
        print("m1 (before delete):", Test.a)
        del Test.a                        # delete here
        print("m1 (after delete): deleted")

    @classmethod
    def m2(cls):
        print("m2:", cls.a)              # ERROR — 'a' already deleted


t = Test()
t.m1()
t.m2()    # AttributeError
```

> **Key point:** Once deleted with `del ClassName.var`, the static variable is gone from that point onward in program execution. Any method called after the deletion will raise `AttributeError` if it tries to access the variable.

---

## 3. Garbage Collector

### 3.1 What is Garbage Collector?

Python is a **high-level language**. For low-level activities like memory management, you don't write explicit code. Python handles this automatically via the **Garbage Collector (GC)**.

> **Automatic memory management:** The process of allocating memory to objects that need it, and deallocating memory from objects that are no longer needed. This is what GC does — automatically, behind the scenes.

```
Without GC (old languages like C++):
    Programmer must manually allocate and free memory
    → Error-prone, complex

With GC (Python, Java, .NET):
    GC automatically tracks objects
    → Allocates memory when objects are created
    → Deallocates memory when objects are no longer needed
    → No manual work required
```

### 3.2 The `gc` Module

Python provides a built-in module called `gc` for interacting with the garbage collector.

```python
import gc
```

| Method | Purpose | Returns |
|--------|---------|---------|
| `gc.isenabled()` | Check if GC is currently active | `True` or `False` |
| `gc.disable()` | Turn off the garbage collector | Nothing |
| `gc.enable()` | Turn on the garbage collector | Nothing |

### 3.3 Demo Program

```python
import gc

print(gc.isenabled())   # True  — GC is active by default

gc.disable()
print(gc.isenabled())   # False — GC is now disabled

gc.enable()
print(gc.isenabled())   # True  — GC is enabled again
```

**Output:**
```
True
False
True
```

> **By default:** Every Python program has an active garbage collector. You almost never need to disable it — this demo is just to show you the module exists and how it works.

---

## 4. Destructor

### 4.1 What is a Destructor?

```
Destructor — Key Facts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. A special method of the class
2. Name is always:  __del__(self)
3. Called AUTOMATICALLY by the garbage collector
4. Purpose: memory cleanup activities (deallocation)
5. Does NOT delete the object — only cleans up
6. Garbage collector deletes the object AFTER __del__ completes
7. We NEVER call the destructor explicitly in our programs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 4.2 Constructor vs Destructor

| | Constructor | Destructor |
|--|------------|------------|
| Name | `__init__(self)` | `__del__(self)` |
| Purpose | Initialize variables, build object | Clean up memory (deallocate) |
| Called by | Python when object is created | Garbage Collector when object is no longer needed |
| Explicit call | Never (automatic) | Never (GC handles it) |
| Analogy | Build a house | Demolish (clean up) a house |

### 4.3 Demo Program

```python
import time

class Test:
    def __init__(self):
        self.a = 10
        print("Constructor executed")

    def __del__(self):
        print("Destructor executed")


t = Test()
time.sleep(3)    # wait 3 seconds
# After the program finishes, GC calls __del__ for cleanup
```

**Output:**
```
Constructor executed
[3 second pause]
Destructor executed
```

> **Observation:** Constructor runs immediately when the object is created. The destructor runs after the program completes (or when the object goes out of scope), called by the GC.

### 4.4 Execution Flow

```
Memory Lifecycle of an Object
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: t = Test()
            ↓
        Object created in memory
        __init__ runs → variables initialized
            ↓
Step 2: Object is used (methods called, variables accessed)
            ↓
Step 3: Object is no longer needed (program ends / out of scope)
            ↓
        Garbage Collector detects unused object
            ↓
Step 4: GC calls __del__
        Cleanup activities (memory deallocation)
            ↓
Step 5: GC destroys the object
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> **Critical point:** `__del__` does NOT destroy the object. It performs cleanup. The actual deletion happens when GC removes the object after `__del__` completes.

---

## 5. Complete Class Walkthrough

### Step 1: Static Variable Access from All 5 Places (test9.py)

```python
class Test:
    a = 100    # static variable

    def __init__(self):                          # Place 1: constructor
        print("Constructor self:", self.a)
        print("Constructor class name:", Test.a)

    def m1(self):                                # Place 2: instance method
        print("Instance method self:", self.a)
        print("Instance method class name:", Test.a)

    @classmethod
    def m2(cls):                                 # Place 3: class method
        print("Class method cls:", cls.a)
        print("Class method class name:", Test.a)

    @staticmethod
    def m3():                                    # Place 4: static method
        print("Static method class name:", Test.a)


t = Test()
t.m1()
Test.m2()
Test.m3()
print("Outside via obj ref:", t.a)             # Place 5
print("Outside via class name:", Test.a)        # Place 5
```

### Step 2: GC Module Demo (test10.py)

```python
import gc

print(gc.isenabled())   # True
gc.disable()
print(gc.isenabled())   # False
gc.enable()
print(gc.isenabled())   # True
```

### Step 3: Destructor Demo (test11.py)

```python
import time

class Test:
    def __init__(self):
        self.a = 10
        print("Constructor execution")

    def __del__(self):
        print("Destructor execution")


t = Test()
time.sleep(3)
```

---

## Student Q&A

> **Student Question:** Why can't we use `self.a` inside a static method to access a static variable?
> **Answer:** Because static methods are declared without `self` — Python does not pass the object as a parameter. There is no `self` variable available inside a static method. The only way to refer to a class-level (static) variable from inside a static method is by using the class name directly.

> **Student Question:** Does the destructor delete the object?
> **Answer:** No — this is a common misconception. The destructor (`__del__`) only performs **cleanup activities** like releasing external resources (files, database connections, etc.). The actual deletion of the object is done by the **Garbage Collector** after the destructor completes. Think of the destructor as packing up belongings before moving out; the GC is the one that actually demolishes the house.

> **Student Question:** Do we ever write a destructor in our programs?
> **Answer:** Rarely. In most Python programs, you never need to write `__del__`. Python's garbage collector handles memory automatically. You might write one only if your class holds external resources (like file handles or network connections) that need to be explicitly released. In normal application programming, the constructor is used frequently but the destructor almost never.

---

## Key Differences — Constructor vs Destructor

| Feature | Constructor (`__init__`) | Destructor (`__del__`) |
|---------|--------------------------|------------------------|
| Purpose | Initialize object | Cleanup memory |
| Called by | Python (on object creation) | Garbage Collector |
| When | Object created | Object no longer needed |
| Explicit call | Never | Never |
| Common in practice | Very common | Rarely needed |
| Deletes object? | No | No (only cleans up) |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `AttributeError: type object 'Test' has no attribute 'a'` | Accessing static variable after deleting it with `del Test.a` | Don't access after deletion, or check if it exists |
| `NameError: name 'self' is not defined` in static method | Trying to use `self.a` inside a `@staticmethod` | Use `ClassName.a` instead |
| `AttributeError: Test has no attribute 'isenabled'` | Called `Test.isenabled()` instead of `gc.isenabled()` | `import gc` and use `gc.isenabled()` |

---

## Interview Questions

**Q: How do you access a static variable from inside a static method?**
A: Using the class name: `ClassName.variable`. Since static methods have no `self` or `cls`, the class name is the only way.

**Q: What is the garbage collector in Python?**
A: The garbage collector is Python's automatic memory management system. It tracks all objects in memory, allocates memory when objects are created, and deallocates memory when objects are no longer needed. Programmers don't write memory management code because GC handles it automatically.

**Q: What is a destructor in Python?**
A: A destructor is a special method named `__del__(self)`. It is called automatically by the garbage collector when an object is about to be removed from memory. Its purpose is to perform cleanup activities like releasing external resources. It does NOT delete the object — the GC does that after the destructor runs.

**Q: How do you delete a static variable?**
A: Using `del ClassName.variable_name`. This syntax works from anywhere — inside any method or outside the class.

**Q: What happens if you try to access a static variable after deleting it?**
A: Python raises `AttributeError: type object 'ClassName' has no attribute 'variable_name'`.

**Q: What is the `gc` module in Python?**
A: The `gc` module provides functions to interact with the garbage collector: `gc.isenabled()` (check if active), `gc.enable()` (turn on), `gc.disable()` (turn off). In normal programs, you never need to import or use this module.

---

## Try It Yourself

**Exercise 1:** Create a class `Config` with a static variable `debug_mode = True`. Access it from a constructor, an instance method, a class method, and a static method. Print a label for each location.

<details><summary>Answer</summary>

```python
class Config:
    debug_mode = True

    def __init__(self):
        print("Constructor:", Config.debug_mode)

    def instance_method(self):
        print("Instance method:", self.debug_mode)

    @classmethod
    def class_method(cls):
        print("Class method:", cls.debug_mode)

    @staticmethod
    def static_method():
        print("Static method:", Config.debug_mode)


c = Config()
c.instance_method()
Config.class_method()
Config.static_method()
print("Outside:", Config.debug_mode)
```
</details>

---

**Exercise 2:** Create a class with a static variable `count = 0`. In the constructor, increment `count` by 1. Create 3 objects and print `count` after each creation to show all objects share the same variable.

<details><summary>Answer</summary>

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        print(f"Object created. Total count: {Counter.count}")


c1 = Counter()   # Total count: 1
c2 = Counter()   # Total count: 2
c3 = Counter()   # Total count: 3
```
</details>

---

**Exercise 3:** Demonstrate the destructor. Create a class with a constructor and destructor. Print messages in both. Use `time.sleep(2)` to see the timing clearly.

<details><summary>Answer</summary>

```python
import time

class Session:
    def __init__(self, name):
        self.name = name
        print(f"Session '{self.name}' started (constructor)")

    def __del__(self):
        print(f"Session '{self.name}' ended (destructor — cleanup)")


s = Session("Python Class")
time.sleep(2)
print("About to end program...")
```
</details>
