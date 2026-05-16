# Day 15 — Functions: Return Values, Local & Global Variables

← [Day 14](day_14_bytes_frozenset.md) | [Index](00_INDEX.md) | [Day 16](day_16_scope_arguments.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | Can a function return multiple values? | Yes — but one function, one task is better practice |
| 2 | What does returning multiple values actually return? | A tuple (Python packs them automatically) |
| 3 | What is a local variable? | Declared inside a function — accessible only within that function |
| 4 | What is a global variable? | Declared outside all functions — accessible from any function |
| 5 | Can a local variable be accessed outside its function? | No — NameError |
| 6 | What does the `global` keyword do? | Makes a global variable modifiable from inside a function |
| 7 | When local and global share a name, which wins? | Local takes priority inside the function |
| 8 | How to access the global variable when names conflict? | Use `globals()["var_name"]` |
| 9 | Can you declare a global variable inside a function? | Yes — with the `global` keyword |
| 10 | Do changes to a global variable carry forward? | Yes — all functions called after see the updated value |

---

## 1. Function Returning Multiple Values

Python allows a single function to return multiple values. They are automatically packed into a **tuple**.

```python
def some_sub(a, b):
    some = a + b
    sub  = a - b
    return some, sub   # returns a tuple (some, sub)

x, y = some_sub(10, 20)   # unpacking the returned tuple
print("Sum:", x)    # 30
print("Sub:", y)    # -10
```

### Adding more return values

```python
def some_sub_mul(a, b):
    some = a + b
    sub  = a - b
    mul  = a * b
    return some, sub, mul

x, y, z = some_sub_mul(10, 20)
print(x, y, z)   # 30, -10, 200
```

---

## 2. Why Multiple Returns Per Function is NOT Good Practice

```
Good practice:             Bad practice:
───────────────            ─────────────────────────
def add(a, b):             def add_sub_mul(a, b):
    return a + b               return a+b, a-b, a*b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
```

**Problem with one function doing everything:**

> Once you assign multiple tasks to a function, you cannot selectively call only one task. Every time you call it, **all** tasks run — even if you only needed one.

**Best practice: one function = one task.**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Now call only what you need:
result = add(10, 20)        # only addition runs
print(result)               # 30
```

---

## 3. Local Variables

**Local variables** are declared **inside** a function. They exist only within that function.

```python
def f1():
    a = 10          # local to f1
    print(a)

def f2():
    b = 20          # local to f2
    print(b)

f1()   # 10
f2()   # 20
```

### Local variables cannot be accessed from another function

```python
def f1():
    a = 10
    print(a)

def f2():
    print(a)   # NameError: name 'a' is not defined
               # a belongs to f1, not f2

f1()
f2()   # crashes!
```

---

## 4. Global Variables

**Global variables** are declared **outside** all functions. They are accessible from any function in the program.

```python
a = 10   # global variable

def f1():
    print(a)   # can access — reads the global value

def f2():
    print(a)   # can access — reads the global value

f1()   # 10
f2()   # 10
```

### Global vs local — summary

| | Local Variable | Global Variable |
|--|----------------|----------------|
| Declared | Inside a function | Outside all functions |
| Accessible | Only within that function | In any function |
| Scope | Function scope | Program scope |

---

## 5. The `global` Keyword

Even though global variables can be **read** inside functions, they cannot be **modified** without the `global` keyword.

### Without `global` — modification creates a local copy

```python
a = 10   # global

def f1():
    a = 99     # this creates a NEW local variable named 'a'
    print(a)   # 99 (local)

def f2():
    print(a)   # 10 (global — unchanged)

f1()   # 99  (local a)
f2()   # 10  (global a untouched)
```

### With `global` — actually modifies the global variable

```python
a = 10   # global

def f1():
    global a       # tell Python: use the GLOBAL 'a'
    a = 99         # now actually modifies the global variable
    print(a)       # 99

def f2():
    print(a)       # also 99 — the global was changed

f1()   # 99
f2()   # 99   ← carries forward!
```

---

## 6. Call Order Matters

When you modify a global variable inside a function using `global`, the change is **permanent and forward-looking**. Functions called **after** the modification see the new value.

```python
a = 10   # global

def f1():
    global a
    a = 99   # global a is now 99

def f2():
    print(a)   # sees whatever global a is at the time of calling

f2()   # called BEFORE f1 → prints 10
f1()   # modifies global a to 99
f2()   # called AFTER f1 → prints 99
```

---

## 7. Declaring Global Variables Inside a Function

You can also **create** a global variable from inside a function using the `global` keyword.

```python
def f1():
    global a    # declare 'a' as global (even though it's inside f1)
    a = 10      # create and assign

def f2():
    print(a)    # can access because 'a' is global

f1()    # creates global 'a'
f2()    # 10
```

---

## 8. Name Conflict — Local and Global Same Name

When a local variable and global variable share the same name, **local takes priority** inside the function.

```python
a = 10   # global

def f1():
    a = 99     # local — shadows global inside this function
    print(a)   # 99 (local wins)

def f2():
    print(a)   # 10 (global — f2 has no local 'a')

f1()   # 99
f2()   # 10
```

### Accessing global when names conflict — `globals()`

```python
a = 10   # global

def f1():
    a = 99
    print(a)              # 99 — local
    print(globals()["a"]) # 10 — global, accessed by name as string
```

---

## 9. Best Practices Summary

```
✓ One function = one task
✓ Use return to send results back (so they can be reused)
✓ Use local variables inside functions (clean, isolated)
✓ Use global variables sparingly — only when truly shared state is needed
✓ Use global keyword when you need to modify a global from inside a function
✗ Avoid functions that return too many values
✗ Avoid global variables for everything — makes debugging hard
```

---

## 10. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `NameError: name 'a' is not defined` | Accessing local variable outside its function | Declare it globally or pass as parameter |
| `UnboundLocalError` | Using a variable inside function before assigning (Python treats it as local) | Add `global a` at top of function |
| Modifying global without `global` keyword | Creates a local copy, doesn't change global | Add `global var_name` inside function |

---

## 11. Interview Questions

1. What is the difference between a local and a global variable?
2. Can a local variable be accessed outside its function?
3. What happens if you try to modify a global variable without the `global` keyword?
4. What does the `global` keyword do?
5. If a local and global variable have the same name, which takes priority inside the function?
6. Is it good practice for a function to return multiple values? Why?
7. What is `globals()` and when would you use it?
8. Does modifying a global variable inside a function affect functions called after it?

---

## 12. Try It Yourself

```python
# 1. Write a function that calculates and returns both area and perimeter
#    of a rectangle (length, width as parameters).
#    Is this one task or two? How would you refactor into two functions?

# 2. Demonstrate local scope:
#    def f1(): x = 100
#    def f2(): print(x)  ← predict what happens when you call f2()

# 3. Set a global counter = 0
#    Write a function increment() that uses global to add 1 each call
#    Call it 5 times and print counter after each call

# 4. What is the output? Predict before running:
#    n = 5
#    def f1():
#        n = 10
#        print(n)
#    def f2():
#        print(n)
#    f1(); f2()

# 5. What is the output?
#    n = 5
#    def f1():
#        global n
#        n = 10
#    f2 = lambda: print(n)
#    f2(); f1(); f2()
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `return some, sub` | Return multiple values (tuple) |
| `x, y = func(10, 20)` | Unpack multiple return values |
| `def add(a, b): return a + b` | Single-task function |
| `a = 10` outside functions | Global variable |
| `a = 99` inside function | Local variable (shadows global) |
| `global a` inside function | Modify the actual global variable |
| `globals()["a"]` | Access global when name conflicts with local |
