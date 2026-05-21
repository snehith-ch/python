# Day 36 — Binary Files: Pickling and Unpickling

← [Day 35](day_35_zip_csv_files.md) | [Index](00_INDEX.md) | [Day 37](day_37_packages.md) →

---

## Quick Revision — Day 36

| # | Key Point |
|---|-----------|
| 1 | Binary files store **binary data** — including Python objects (class instances) |
| 2 | **Pickling** = writing the state of an object to a file (serialization) |
| 3 | **Unpickling** = reading the state of an object from a file (deserialization) |
| 4 | Use `import pickle` module for both operations |
| 5 | `pickle.dump(obj, file)` → stores object into file (pickling) |
| 6 | `pickle.load(file)` → retrieves object from file (unpickling) |
| 7 | File mode for pickling: `wb` (write binary); for unpickling: `rb` (read binary) |
| 8 | Common file extension for pickle files: `.dat` |
| 9 | Without pickling, object data is lost when program ends — pickling makes it permanent |
| 10 | Object type: when you print `type(e)`, it shows `<class '__main__.Employee'>` — class type |

---

## Navigation

- **Pre-requisite:** [Day 35](day_35_zip_csv_files.md) — ZIP/CSV files, binary file modes
- **Next:** [Day 37](day_37_packages.md) — Packages and module hierarchy
- **Related:** [Day 33](day_33_file_handling_basics.md) — File modes, binary vs text files

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `file15.py` | Employee class + pickling + unpickling demo |
| Class | `Employee` | Constructor + `display()` method |
| Module | `pickle` | Built-in pickling/unpickling module |
| Method | `pickle.dump(obj, f)` | Store object data into binary file |
| Method | `pickle.load(f)` | Retrieve object data from binary file |
| File created | `emp.dat` | Binary file containing pickled Employee object |
| File mode | `wb` | Write binary — required for pickling |
| File mode | `rb` | Read binary — required for unpickling |

---

## 1. Why Binary Files? The Problem Without Pickling

```python
class Employee:
    def __init__(self, emp_no, emp_name, emp_address):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.emp_address = emp_address

    def display(self):
        print(self.emp_no, self.emp_name, self.emp_address)


e = Employee(101, "Sita", "HYD")
e.display()    # works fine while running
```

**Problem:** Once the program ends, all this object data is **destroyed**. The next time you run the program, it's gone. There is no permanent storage.

```
Without Pickling:
    Run program → create object → use object → program ends → DATA LOST

With Pickling:
    Run program → create object → pickle.dump() → data saved to file → PERMANENT
    Later run  → pickle.load() → object restored → DATA RETRIEVED
```

---

## 2. What Is Pickling?

```
Pickling — Key Facts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pickling   = Process of writing the STATE of an object to a file
             (also called serialization)

Unpickling = Process of reading the STATE of an object from a file
             (also called deserialization)

Module:    import pickle
File type: Binary file (wb / rb modes)
Extension: .dat (common) — any name works
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 3. Pickling — Storing Object to File

### 3.1 Syntax

```python
import pickle

with open("filename.dat", "wb") as f:
    pickle.dump(obj, f)
```

- `pickle.dump(obj, f)` — dumps (stores) the object `obj` into file `f`
- File mode must be `"wb"` (write binary)

### 3.2 Full Pickling Demo

```python
import pickle

class Employee:
    def __init__(self, emp_no, emp_name, emp_address):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.emp_address = emp_address

    def display(self):
        print(self.emp_no, "\t", self.emp_name, "\t", self.emp_address)


# Create object
e = Employee(101, "Sita", "HYD")

# Pickle — store object to binary file
with open("emp.dat", "wb") as f:
    pickle.dump(e, f)

print("Pickling of Employee object completed")
```

**Output:** `Pickling of Employee object completed`

The file `emp.dat` is created. If you open it in a text editor, it shows unreadable binary content — that's expected. The data is stored in binary (pickle) format.

---

## 4. Unpickling — Retrieving Object from File

### 4.1 Syntax

```python
import pickle

with open("filename.dat", "rb") as f:
    obj = pickle.load(f)
```

- `pickle.load(f)` — loads (retrieves) the pickled object from file `f`
- File mode must be `"rb"` (read binary)
- Assign to a temporary object variable, then use it

### 4.2 Full Unpickling Demo

```python
import pickle

class Employee:
    def __init__(self, emp_no, emp_name, emp_address):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.emp_address = emp_address

    def display(self):
        print(self.emp_no, "\t", self.emp_name, "\t", self.emp_address)


# Unpickle — retrieve object from binary file
with open("emp.dat", "rb") as f:
    obj = pickle.load(f)

print("Employee information after unpickling:")
obj.display()
```

**Output:**
```
Employee information after unpickling:
101     Sita    HYD
```

> `obj` is a **temporary object** that holds the restored state of the pickled object. All attributes (`emp_no`, `emp_name`, `emp_address`) and methods (`display()`) are fully available on this restored object.

---

## 5. Complete Pickle + Unpickle in One Program

```python
import pickle

class Employee:
    def __init__(self, emp_no, emp_name, emp_address):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.emp_address = emp_address

    def display(self):
        print(self.emp_no, "\t", self.emp_name, "\t", self.emp_address)


# --- PICKLING ---
e = Employee(101, "Sita", "HYD")

with open("emp.dat", "wb") as f:
    pickle.dump(e, f)

print("Pickling of Employee object completed")

# --- UNPICKLING ---
with open("emp.dat", "rb") as f:
    obj = pickle.load(f)

print("Employee information after unpickling:")
obj.display()
```

**Output:**
```
Pickling of Employee object completed
Employee information after unpickling:
101     Sita    HYD
```

---

## 6. Understanding Object Type

```python
e = Employee(101, "Sita", "HYD")
print(type(e))    # <class '__main__.Employee'>
```

> When you print the type of an object, Python shows it as a **class type** reference — not a simple type like `int` or `str`. This is what gets serialized into binary format by `pickle.dump()`.

---

## 7. Pickle Flow Diagram

```
Pickling and Unpickling Flow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PICKLING (Storing):
    Python Object (e)
         ↓  pickle.dump(e, f)
    emp.dat (binary file — unreadable format)
    [stores: emp_no=101, emp_name=Sita, emp_address=HYD]

UNPICKLING (Retrieving):
    emp.dat (binary file)
         ↓  obj = pickle.load(f)
    Python Object (obj)
    [restores: obj.emp_no=101, obj.emp_name=Sita, ...]
         ↓  obj.display()
    101     Sita    HYD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 8. Pickling Multiple Objects

You can pickle multiple objects by calling `dump()` multiple times and loading with `load()` multiple times:

```python
import pickle

class Employee:
    def __init__(self, emp_no, emp_name):
        self.emp_no = emp_no
        self.emp_name = emp_name

# Pickle multiple objects
e1 = Employee(101, "Ali")
e2 = Employee(102, "Mohan")
e3 = Employee(103, "Ravi")

with open("employees.dat", "wb") as f:
    pickle.dump(e1, f)
    pickle.dump(e2, f)
    pickle.dump(e3, f)

print("All employees pickled")

# Unpickle multiple objects
with open("employees.dat", "rb") as f:
    while True:
        try:
            obj = pickle.load(f)
            print(obj.emp_no, obj.emp_name)
        except EOFError:    # end of file reached
            break
```

**Output:**
```
All employees pickled
101 Ali
102 Mohan
103 Ravi
```

---

## Student Q&A

> **Student Question:** What is pickling and why do we need it?
> **Answer:** Pickling is the process of writing the complete state of a Python object to a binary file. We need it because without pickling, all object data is lost when the program ends — it's stored only in memory (temporary storage). With pickling, the object's state is saved permanently to a file and can be restored (unpickled) the next time the program runs.

> **Student Question:** What is the difference between pickling and writing to a text file?
> **Answer:** Text files store character data (strings). Pickling stores entire Python objects in binary format — including all attributes and their values. When you pickle an object and unpickle it, you get back the full object with all its methods and properties. With a text file, you'd have to manually parse and reconstruct the object. Pickling is more convenient for storing Python objects.

> **Student Question:** What extension do we use for pickle files?
> **Answer:** The `.dat` extension is most commonly used for pickle files. However, any extension works — `.pkl`, `.pickle`, `.bin`, etc. The extension does not affect functionality; what matters is using `wb`/`rb` binary modes when opening the file.

> **Student Question:** What file mode do we use for pickling?
> **Answer:** `"wb"` (write binary) for pickling (storing). `"rb"` (read binary) for unpickling (retrieving). Never use text modes (`"w"`, `"r"`) for pickle files — the data is binary and will be corrupted if opened in text mode.

---

## Key Differences

| Feature | Pickling | Unpickling |
|---------|---------|-----------|
| Operation | Write/Store | Read/Retrieve |
| Method | `pickle.dump(obj, f)` | `pickle.load(f)` |
| File mode | `wb` (write binary) | `rb` (read binary) |
| Direction | Object → File | File → Object |
| Also called | Serialization | Deserialization |

| Feature | Text File | Pickle File |
|---------|-----------|-------------|
| Stores | String data | Python objects (binary) |
| Readable | Yes (Notepad) | No (binary format) |
| Extension | `.txt` | `.dat` / `.pkl` |
| Module | Built-in `open()` | `import pickle` |
| Write | `f.write(string)` | `pickle.dump(obj, f)` |
| Read | `f.read()` | `pickle.load(f)` |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `UnicodeDecodeError` | Opening a `.dat` file in text mode (`"r"`) | Use `"rb"` for reading pickle files |
| `EOFError` | Calling `pickle.load()` when no more data remains | Use try-except with `EOFError` to stop reading |
| `FileNotFoundError` | Unpickling before pickling (file doesn't exist) | Run the pickling code first to create the file |
| `AttributeError` after unpickling | Class definition changed after pickling | Re-pickle the object with the updated class |

---

## Interview Questions

**Q: What is pickling in Python?**
A: Pickling is the process of converting a Python object into a binary byte stream and writing it to a file. The reverse — reading the binary data and reconstructing the object — is called unpickling. Python's `pickle` module provides `pickle.dump()` for pickling and `pickle.load()` for unpickling.

**Q: What is the `pickle` module?**
A: `pickle` is a built-in Python module for serializing (pickling) and deserializing (unpickling) Python objects. It provides two main methods: `dump(obj, file)` to store an object into a binary file, and `load(file)` to retrieve an object from a binary file.

**Q: What file mode is used for pickling?**
A: `"wb"` (write binary) for pickling — storing an object to a file. `"rb"` (read binary) for unpickling — retrieving an object from a file.

**Q: What is the difference between pickling and serialization?**
A: They are the same concept. Serialization is the general term for converting an object to a format that can be stored or transmitted. In Python, the specific implementation using the `pickle` module is called pickling. The reverse (deserialization) is called unpickling.

**Q: What types of Python objects can be pickled?**
A: Most Python objects can be pickled: instances of user-defined classes, lists, dictionaries, tuples, integers, strings, etc. Functions, lambda expressions, and some special objects (like file handles, database connections) cannot be pickled.

---

## Try It Yourself

**Exercise 1:** Create a `Student` class with `student_id`, `name`, and `marks` attributes and a `display()` method. Pickle one student object to `student.dat`, then unpickle it and call `display()`.

<details><summary>Answer</summary>

```python
import pickle

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}")

# Pickle
s = Student(1, "Alice", 95)
with open("student.dat", "wb") as f:
    pickle.dump(s, f)
print("Student pickled")

# Unpickle
with open("student.dat", "rb") as f:
    obj = pickle.load(f)
print("After unpickling:")
obj.display()
```
</details>

---

**Exercise 2:** Pickle a Python list `[10, 20, 30, 40, 50]` to a file. Unpickle it and print each element.

<details><summary>Answer</summary>

```python
import pickle

data = [10, 20, 30, 40, 50]

with open("list_data.dat", "wb") as f:
    pickle.dump(data, f)
print("List pickled")

with open("list_data.dat", "rb") as f:
    restored = pickle.load(f)

print("Unpickled list:")
for item in restored:
    print(item)
```
</details>

---

**Exercise 3:** Demonstrate that without pickling, object data is lost. Create an Employee object, print it, and show that after the program "restarts" (simulate by not saving to file), the data is gone. Then use pickling to preserve it.

<details><summary>Answer</summary>

```python
import pickle

class Employee:
    def __init__(self, emp_no, name):
        self.emp_no = emp_no
        self.name = name
    def display(self):
        print(f"Emp: {self.emp_no} - {self.name}")

# Without pickling — data lost after program ends
e = Employee(101, "Bob")
e.display()
# After program ends: data gone

# With pickling — data preserved
with open("emp.dat", "wb") as f:
    pickle.dump(e, f)
print("Data saved permanently")

# Later retrieval
with open("emp.dat", "rb") as f:
    restored = pickle.load(f)
restored.display()    # data still available
```
</details>
