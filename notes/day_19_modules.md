# Day 19 — Modules: Creating, Importing & Using

← [Day 18](day_18_lambda.md) | [Index](00_INDEX.md) | [Day 20](day_20_builtin_modules.md) →

---

## Quick Revision

| # | Concept | One-line Summary |
|---|---------|-----------------|
| 1 | Module | A `.py` file containing variables, functions, and classes |
| 2 | Purpose | Reusability — write once, import anywhere |
| 3 | `import module` | Import the whole module; access with `module.name` |
| 4 | `import module as alias` | Import with a shorter alias name |
| 5 | `from module import *` | Import everything; access directly without prefix |
| 6 | `from module import member` | Import one specific item |
| 7 | `from module import member as alias` | Import one item with a custom name |
| 8 | Name conflict | When two modules share a name, last-imported `*` wins |
| 9 | `__name__` | `"__main__"` when run directly; module name when imported |
| 10 | `help(module)` | Displays module documentation in the terminal |

---

## 1. What Is a Module?

Every `.py` file is a module. A module groups related variables, functions, and classes together so they can be **reused** in other programs.

```
sample.py        ← this IS a module
main.py          ← this imports from sample.py
```

```python
# sample.py
name = "Snehith"
course = "Python"

def add(a, b):
    return a + b

def greet(n):
    print("Hello,", n)
```

---

## 2. Import Styles

### Style 1 — `import module`

```python
import sample

print(sample.name)        # "Snehith"
print(sample.add(10, 20)) # 30
sample.greet("Alice")     # Hello, Alice
```

Access everything with `module.member` prefix.

---

### Style 2 — `import module as alias`

```python
import sample as s

print(s.name)
s.greet("Bob")
```

Useful when the module name is long.

---

### Style 3 — `from module import *`

```python
from sample import *

print(name)        # direct access — no prefix needed
print(add(5, 5))   # 10
greet("Charlie")
```

**Warning:** if two modules both have a variable called `name` and you do `from mod1 import *` then `from mod2 import *`, the second one overwrites the first.

---

### Style 4 — `from module import member`

```python
from sample import add

print(add(3, 7))    # 10
# print(name)       # NameError — only 'add' was imported
```

Import only what you need.

---

### Style 5 — `from module import member as alias`

```python
from sample import add as total

print(total(10, 20))   # 30
```

Rename the imported item to avoid conflicts or for clarity.

---

## 3. Importing Multiple Modules

```python
import module1, module2    # on one line
# or
import module1
import module2             # separate lines (preferred for clarity)
```

---

## 4. Name Conflict Warning

```python
# mod1.py
course = "Python"

# mod2.py
course = "Java"
```

```python
from mod1 import *
from mod2 import *

print(course)   # "Java" — mod2 wins because it was imported last
```

To avoid this: use `import mod1; mod1.course` style instead of `import *`.

---

## 5. `__name__` Special Variable

Every Python file has a built-in variable `__name__`.

- When you **run a file directly**: `__name__` equals `"__main__"`
- When a file is **imported** by another: `__name__` equals the module's file name

```python
# sample.py
def add(a, b):
    return a + b

print(__name__)    # prints "__main__" when run directly
                   # prints "sample" when imported from main.py
```

**Common pattern — guard code that should only run directly:**

```python
# sample.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))   # runs only when executed directly, not when imported
```

This prevents demo/test code in a module from running when another file imports it.

---

## 6. `help()` and Module Documentation

```python
import sample
help(sample)   # prints all functions, variables, and docstrings in sample
```

Works for any module — built-in or user-defined.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError` | Module file not in same folder or Python path | Place module file in the same directory |
| `AttributeError: module has no attribute` | Typo in member name | Check spelling; use `help(module)` |
| `NameError` after `from mod import add` | Trying to use a member not imported | Import it or use `import mod` style |
| Stale `import *` override | Two modules share a name; last-imported wins | Use `import mod; mod.member` to be explicit |

---

## Interview Questions

1. What is a Python module? Is every `.py` file a module?
2. What is the difference between `import sample` and `from sample import *`?
3. What happens when two modules both define `course` and you do `from mod1 import *; from mod2 import *`?
4. What does `import sample as s` allow you to do?
5. What is the value of `__name__` when a file is run directly vs when it is imported?
6. What is the purpose of `if __name__ == "__main__":`?
7. How do you import just one function from a module?
8. What does `help(module)` display?

---

## Try It Yourself

1. Create `calculator.py` with `add`, `subtract`, `multiply`, `divide`. Import it in `main.py` using all five import styles — one at a time.
2. Create two modules that both define a variable called `greeting`. Import both with `import *` and observe which one wins.
3. Add `if __name__ == "__main__":` to `calculator.py` with a test call. Verify it does NOT run when you import from `main.py`.
4. Import your `calculator.py` as `calc`. Call `calc.add(5, 3)`.
5. Use `help()` on the `math` built-in module. Read the output.

---

## Code Created

| Snippet | Purpose |
|---------|---------|
| `import sample; sample.add(10, 20)` | Standard import with prefix |
| `from sample import *; add(10, 20)` | Wildcard import — no prefix |
| `from sample import add as total` | Member aliasing |
| `if __name__ == "__main__":` | Guard against running on import |
| `help(sample)` | View module documentation |

---

← [Day 18](day_18_lambda.md) | [Index](00_INDEX.md) | [Day 20](day_20_builtin_modules.md) →
