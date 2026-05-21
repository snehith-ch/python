# Day 37 — Packages in Python

← [Day 36](day_36_binary_files_pickling.md) | [Index](00_INDEX.md) | [Day 38](day_38_database_mssql.md) →

---

## Quick Revision — Day 37

| # | Key Point |
|---|-----------|
| 1 | Package = a **folder/directory** that organizes modules in a project |
| 2 | Hierarchy: **Package → Module (.py) → Class → Method → Variable** |
| 3 | Every package folder contains `__init__.py` file (always empty, marks folder as a package) |
| 4 | To access a module from a package: `import sys; sys.path.append("path/to/package")` |
| 5 | Two import styles: `import module` + `module.function()`, OR `from module import *` + `function()` directly |
| 6 | Use **forward slashes** `/` in paths (not backslashes `\`) |
| 7 | Sub-package = a package inside another package (nested folders) |
| 8 | Packages avoid naming conflicts — `admin/login.py` and `manager/login.py` are different |
| 9 | In PyCharm: right-click project → New → Python Package (creates folder + `__init__.py`) |
| 10 | Copy path: right-click folder → Copy Path/Reference → Absolute Path |

---

## Navigation

- **Pre-requisite:** [Day 19](day_19_modules.md) — Modules, import styles
- **Next:** [Day 38](day_38_database_mssql.md) — Database connectivity with MS SQL Server
- **Related:** [Day 19](day_19_modules.md) — Module imports, `from ... import *`

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| Package | `package1/` | Single package containing two modules |
| Module | `module1.py` in package1 | Contains `display()` function |
| Module | `module2.py` in package1 | Contains `show()` function |
| Package | `sub_package/` inside package1 | Sub-package (nested) |
| Package | `package2/` | Second package for third example |
| Class | `Student` in module1 | Student with `display_student()` method |
| Class | `Employee` in module2 | Employee with `display_emp()` method |
| `.py` file | `main_program.py` | Consumes functions/classes from packages |
| File | `__init__.py` | Created automatically — marks folder as package |
| Module | `sys` | `sys.path.append()` for package path access |

---

## 1. What Is a Package?

```
Python Project Hierarchy
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Package (folder/directory)
    └── Module (.py file)
            └── Class
                    └── Method
                            └── Variable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Package = folder or directory that contains modules
Module  = every .py file is a module
```

**Why packages?**
1. **Organization** — group related files into folders (admin, manager, customer)
2. **Avoid naming conflicts** — `admin/login.py` and `manager/login.py` can coexist
3. **Easy navigation** — find files by category quickly
4. **Hierarchy** — maintain a clean project structure

### 1.1 Real-World Example

```
Project/
├── admin_package/
│   ├── __init__.py
│   ├── login.py
│   └── dashboard.py
├── manager_package/
│   ├── __init__.py
│   ├── login.py        ← same name as admin's, no conflict!
│   └── reports.py
└── customer_package/
    ├── __init__.py
    ├── login.py        ← same name, different package
    └── profile.py
```

Without packages, you cannot have two files named `login.py` in the same folder. With packages, each `login.py` lives in its own folder and is accessed by its full package path.

---

## 2. The `__init__.py` File

```
__init__.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Created automatically when you create a Python Package in PyCharm
→ Marks the folder as a PACKAGE (not a regular folder)
→ Must always remain EMPTY — do NOT implement anything in it
→ Its presence is what distinguishes a package from a plain directory
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> In PyCharm: Right-click project → New → Python Package → give name. The folder is created with `__init__.py` automatically. A plain "Directory" does NOT create `__init__.py`.

---

## 3. Accessing Modules from a Package

### 3.1 Syntax

```python
import sys
sys.path.append("path/to/package")

# Then import from module
import module_name              # Option 1
from module_name import *       # Option 2
```

- `sys` is a built-in system module
- `sys.path` is the list of paths Python searches for modules
- `sys.path.append(path)` adds your package location to the search path
- Use **forward slashes** `/` in the path (copy from PyCharm and replace `\` with `/`)

### 3.2 Getting the Package Path in PyCharm

Right-click the package folder → **Copy Path/Reference** → **Absolute Path** → paste and replace all backslashes `\` with forward slashes `/`.

---

## 4. Example 1 — Importing Modules from a Single Package

### 4.1 Structure

```
Python Project at 7AM/
├── package1/
│   ├── __init__.py
│   ├── module1.py     ← contains display() function
│   └── module2.py     ← contains show() function
└── main_program.py
```

### 4.2 module1.py

```python
def display():
    print("Display function from Module One")
```

### 4.3 module2.py

```python
def show():
    print("Show function from Module Two")
```

### 4.4 main_program.py — Option 1 (import module name)

```python
import sys
sys.path.append("D:/Python project at 7AM/package1")

import module1
import module2

module1.display()    # Display function from Module One
module2.show()       # Show function from Module Two
```

### 4.5 main_program.py — Option 2 (from module import *)

```python
import sys
sys.path.append("D:/Python project at 7AM/package1")

from module1 import *
from module2 import *

display()    # call directly without module prefix
show()
```

**Output (both options):**
```
Display function from Module One
Show function from Module Two
```

---

## 5. Example 2 — Importing Modules from a Sub-Package

### 5.1 Structure

```
Python Project at 7AM/
├── package1/
│   ├── __init__.py
│   ├── module1.py          ← contains display()
│   └── sub_package/
│       ├── __init__.py
│       └── module2.py      ← contains show()
└── main_program.py
```

```
Hierarchy Diagram
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
package1
    ├── module1.py → display()
    └── sub_package
            └── module2.py → show()
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.2 main_program.py

```python
import sys

# Path to package1 (for module1)
sys.path.append("D:/Python project at 7AM/package1")
from module1 import *

# Path to sub_package (for module2)
sys.path.append("D:/Python project at 7AM/package1/sub_package")
from module2 import *

display()    # from module1 (in package1)
show()       # from module2 (in sub_package inside package1)
```

**Output:**
```
Display function from Module One — from package1
Show function from Module Two — from sub_package
```

> Each package and sub-package must have its path added to `sys.path` separately using `sys.path.append()`.

---

## 6. Example 3 — Importing Classes from Two Different Modules and Packages

### 6.1 Structure

```
Python Project at 7AM/
├── package1/
│   ├── __init__.py
│   └── module1.py      ← Student class + display_student()
├── package2/
│   ├── __init__.py
│   └── module2.py      ← Employee class + display_emp()
└── main_program.py
```

```
Class Hierarchy Diagram
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
package1 → module1 → Student class → display_student()
package2 → module2 → Employee class → display_emp()
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 6.2 module1.py (in package1)

```python
class Student:
    def __init__(self, s_id, s_name, s_address):
        self.s_id = s_id
        self.s_name = s_name
        self.s_address = s_address

    def display_student(self):
        print("Student ID:", self.s_id)
        print("Student Name:", self.s_name)
        print("Student Address:", self.s_address)
```

### 6.3 module2.py (in package2)

```python
class Employee:
    def __init__(self, emp_id, emp_name, emp_address):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_address = emp_address

    def display_emp(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Address:", self.emp_address)
```

### 6.4 main_program.py

```python
import sys

# Add package1 path
sys.path.append("D:/Python project at 7AM/package1")
from module1 import *    # imports Student class

# Add package2 path
sys.path.append("D:/Python project at 7AM/package2")
from module2 import *    # imports Employee class

# Create Student object and call method
s = Student(101, "Alice", "HYD")
s.display_student()

# Create Employee object and call method
emp = Employee(201, "Bob", "BLR")
emp.display_emp()
```

**Output:**
```
Student ID: 101
Student Name: Alice
Student Address: HYD
Employee ID: 201
Employee Name: Bob
Employee Address: BLR
```

---

## 7. Complete Package Hierarchy Recap

```
Full Python Hierarchy
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Package (folder/directory)
    Contains → Modules (.py files)
                    Contains → Classes
                                    Contains → Methods
                                                    Contains → Variables
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

We started Python with: Variables
Then added: Functions
Then added: Classes (OOP) — methods contain variables
Then added: Modules — .py files contain classes
Now:        Packages — folders contain modules
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Student Q&A

> **Student Question:** What is the difference between a package and a module?
> **Answer:** A module is a single `.py` file — every Python file is a module. A package is a folder/directory that contains one or more modules. A package provides a higher-level organizational unit. Packages contain modules, modules contain classes, classes contain methods, and methods contain variables.

> **Student Question:** What is the `__init__.py` file inside a package?
> **Answer:** `__init__.py` is a special file that marks a folder as a Python package. Without it, Python treats the folder as a regular directory (not a package). In PyCharm, when you create a "Python Package," it automatically creates this file. It should always remain empty — do not implement any code in it.

> **Student Question:** Why do we need packages if we already have modules?
> **Answer:** Packages provide two main benefits: (1) Organization — you can group related modules in one folder (all admin-related files in an admin package). (2) Conflict avoidance — two packages can each have a `login.py` file without conflict, since they are accessed via their package paths. Without packages, you'd have naming conflicts and a cluttered project structure.

> **Student Question:** Why must we use forward slashes in the path?
> **Answer:** Windows uses backslashes `\` in file paths, but Python treats backslash as an escape character. When you copy a path from PyCharm (Absolute Path), it contains backslashes. You must replace them with forward slashes `/` before using in `sys.path.append()`. Otherwise the path won't work correctly.

> **Student Question:** Instead of `import module_name` and `module_name.function()`, can we use `from module_name import *`?
> **Answer:** Yes — that's Option 2. With `from module_name import *`, all functions and classes from the module are imported directly into the current namespace. You can then call `display()` or `show()` directly without the `module_name.` prefix. Both options work — use whichever is clearer for your use case.

---

## Key Differences

| Feature | Package | Module |
|---------|---------|--------|
| What it is | Folder/directory | `.py` file |
| Contains | Modules | Classes, functions |
| Marker file | `__init__.py` | None needed |
| Creates in PyCharm | New → Python Package | New → Python File |
| Purpose | Organize modules | Organize classes/functions |

| Feature | Option 1 | Option 2 |
|---------|---------|---------|
| Import style | `import module_name` | `from module_name import *` |
| Call function | `module_name.function()` | `function()` directly |
| Explicit? | More explicit (module visible) | Less explicit (shorter) |
| Conflict risk | Lower (namespace separate) | Higher (all names imported) |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: No module named 'module1'` | `sys.path.append()` not called or wrong path | Add the correct package path using `sys.path.append("path/to/package")` |
| Path not working | Backslashes `\` in path string | Replace all `\` with `/` in the path |
| `__init__.py` missing | Created a plain folder, not a Python Package | Right-click → New → Python Package (not Directory) |
| `AttributeError: module has no attribute 'display'` | Typo in function name or wrong module imported | Check spelling of function name and module path |
| Classes not imported | Used `import module_name` but called `ClassName()` without prefix | Use `from module_name import *` or `module_name.ClassName()` |

---

## Interview Questions

**Q: What is a package in Python?**
A: A package is a folder or directory that contains Python modules (`.py` files). It provides an organizational structure for larger projects. A package is identified by the presence of a `__init__.py` file inside it. Packages can contain sub-packages (nested folders), also with their own `__init__.py` files.

**Q: What is the Python project hierarchy?**
A: Package → Module → Class → Method → Variable. Packages contain modules (`.py` files), modules contain classes and functions, classes contain methods, and methods contain variables.

**Q: How do you access a module from a package?**
A: Use `import sys` and `sys.path.append("path/to/package")` to add the package folder to Python's search path. Then import the module with `import module_name` or `from module_name import *`.

**Q: What is `__init__.py`?**
A: It is an initialization file that Python requires to identify a folder as a package. It is created automatically by PyCharm when you select "Python Package." It should always be empty.

**Q: What is a sub-package?**
A: A sub-package is a package inside another package — a folder within a folder, each having its own `__init__.py`. To access a module in a sub-package, you must add both the parent package path AND the sub-package path to `sys.path`.

---

## Try It Yourself

**Exercise 1:** Create a package called `math_package` with two modules: `addition.py` (containing `add(a, b)` function) and `multiplication.py` (containing `multiply(a, b)` function). Access both from a `main.py` file.

<details><summary>Answer</summary>

```python
# math_package/addition.py
def add(a, b):
    print(f"{a} + {b} = {a + b}")

# math_package/multiplication.py
def multiply(a, b):
    print(f"{a} x {b} = {a * b}")

# main.py
import sys
sys.path.append("path/to/math_package")
from addition import *
from multiplication import *

add(10, 5)
multiply(4, 6)
```
</details>

---

**Exercise 2:** Create two packages — `shapes_2d` and `shapes_3d`. Each with a module. `shapes_2d/circle.py` has a `Circle` class with `area()`. `shapes_3d/sphere.py` has a `Sphere` class with `volume()`. Access both from `main.py`.

<details><summary>Answer</summary>

```python
# shapes_2d/circle.py
import math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        print(f"Circle area: {math.pi * self.r ** 2:.2f}")

# shapes_3d/sphere.py
import math
class Sphere:
    def __init__(self, r):
        self.r = r
    def volume(self):
        print(f"Sphere volume: {(4/3) * math.pi * self.r ** 3:.2f}")

# main.py
import sys
sys.path.append("path/to/shapes_2d")
sys.path.append("path/to/shapes_3d")
from circle import *
from sphere import *

c = Circle(5)
c.area()
s = Sphere(5)
s.volume()
```
</details>
