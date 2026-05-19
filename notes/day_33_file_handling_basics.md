# Day 33 — File Handling Basics

← [Day 32](day_32_exception_advanced_custom.md) | [Index](00_INDEX.md) | [Day 34](day_34_file_handling_advanced.md) →

---

## Quick Revision — Day 33

| # | Key Point |
|---|-----------|
| 1 | Two permanent storage areas: **file system** (OS level) and **database** (centralized) |
| 2 | Two file types: **text files** (`.txt`, character data) and **binary files** (images, audio, video) |
| 3 | Open file: `f = open("filename.txt", mode)` |
| 4 | File modes: `w` (write), `r` (read), `a` (append), `x` (exclusive create), `r+`, `w+`, `a+` |
| 5 | Close file: `f.close()` — always close after operations |
| 6 | File properties: `f.name`, `f.mode`, `f.writable()`, `f.readable()`, `f.closed` |
| 7 | Write methods: `write(string)` — single string; `writelines(list)` — list of lines |
| 8 | `w` mode overwrites existing data; `a` mode appends (keeps existing data) |
| 9 | Read methods: `read()`, `read(n)`, `readline()`, `readlines()` |
| 10 | In read mode, if file does not exist → `FileNotFoundError` |

---

## Navigation

- **Pre-requisite:** [Day 32](day_32_exception_advanced_custom.md) — Exception handling (used for FileNotFoundError)
- **Next:** [Day 34](day_34_file_handling_advanced.md) — with statement, tell/seek, file modification, os.path.isfile()
- **Related:** [Day 35](day_35_zip_csv_files.md) — ZIP files and CSV files

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `file1.py` | File properties demo (`name`, `mode`, `writable()`, `readable()`, `closed`) |
| `.py` file | `file2.py` | `write()` method — store string data |
| `.py` file | `file3.py` | `a` (append) mode demo |
| `.py` file | `file4.py` | `writelines()` — store list of lines |
| `.py` file | file read demos | `read()`, `read(n)`, `readline()`, `readlines()` |
| File created | `sample.txt` | Text file created with W mode |
| File created | `abc.txt` | Text file with hello, hi, welcome |
| File created | `abcd.txt` | Text file with list of names |

---

## 1. Storage Areas

Before file handling, understand where data can be stored:

```
Storage Areas in Python
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type 1: TEMPORARY STORAGE AREA
    → Python objects: list, set, tuple, dict, variables
    → Data exists ONLY during program execution
    → Once program ends, data is DESTROYED
    → Example: a = [1, 2, 3] — lost after program exits

Type 2: PERMANENT STORAGE AREA
    Two sub-types:
    A) File System (File handling)
       → Data stored in files on the computer
       → Managed at OS level (one computer)
       → Limited capacity
       → Does NOT support centralized access

    B) Database Storage
       → Data stored in a database (MySQL, Oracle, etc.)
       → Managed at database level
       → Unlimited capacity
       → Supports CENTRALIZED access (many clients, one DB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

| Feature | File System | Database |
|---------|-------------|----------|
| Capacity | Limited | Unlimited |
| Access | One computer (OS level) | Centralized (many clients) |
| Shared access | No | Yes |
| Suitable for | Small local data | Large enterprise data |

---

## 2. Types of Files

```
File Types
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type 1: TEXT FILES
    Extension:   .txt
    Stores:      Character data (strings, text)
    Example:     hello.txt, sample.txt

Type 2: BINARY FILES
    Extension:   Various (.jpg, .mp3, .mp4, .py, etc.)
    Stores:      Binary data
    Includes:    Images, audio, video, object data
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

This session covers **text files** only. Binary files (pickling/unpickling) will be covered later.

---

## 3. Opening and Closing a File

### 3.1 Syntax

```python
# Opening a file
file_object = open("filename.txt", mode)

# Closing a file
file_object.close()
```

```python
# Example
f = open("sample.txt", "w")    # f is the file object
# ... do operations ...
f.close()                       # always close the file
```

> **After all operations, always close the file** with `file_object.close()`. Not closing can lead to data loss or file corruption.

### 3.2 File Object

The file object (`f`) is your handle to the file. It provides access to all file properties and methods.

---

## 4. File Modes

### 4.1 Text File Modes

| Mode | Name | Description |
|------|------|-------------|
| `r` | Read | Open existing file for reading. `FileNotFoundError` if file doesn't exist. Default mode. |
| `w` | Write | Open for writing. **Overwrites** existing data. Creates file if it doesn't exist. |
| `a` | Append | Open for appending. **Adds** to existing data (no overwrite). Creates file if it doesn't exist. |
| `x` | Exclusive Create | Creates a NEW file. `FileExistsError` if file already exists. |
| `r+` | Read and Write | Read first, then write. File must exist. Does not overwrite — pointer at beginning. |
| `w+` | Write and Read | Write first, then read. **Overwrites** existing data. |
| `a+` | Append and Read | Append and read. Does not overwrite existing data. |

### 4.2 Binary File Modes

Add `b` suffix to any text mode for binary operations:

| Binary Mode | Description |
|-------------|-------------|
| `rb` | Read binary |
| `wb` | Write binary |
| `ab` | Append binary |
| `r+b` | Read and write binary |
| `w+b` | Write and read binary |
| `a+b` | Append and read binary |
| `xb` | Exclusive create binary |

```
Key Differences Between Modes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
r mode:  File MUST exist  → FileNotFoundError if not
w mode:  File may or may not exist → creates if absent
a mode:  File may or may not exist → creates if absent
x mode:  File must NOT exist → FileExistsError if present
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 5. File Properties and Methods

### 5.1 Properties

| Property/Method | Type | Description | Returns |
|----------------|------|-------------|---------|
| `f.name` | Property | Name of the open file | String (filename) |
| `f.mode` | Property | Mode in which file is open | String (`'w'`, `'r'`, etc.) |
| `f.closed` | Property | Check if file is closed | `True` or `False` |
| `f.writable()` | Method | Is file open in write mode? | `True` or `False` |
| `f.readable()` | Method | Is file open in read mode? | `True` or `False` |

### 5.2 Demo Program

```python
f = open("sample.txt", "w")

print("File name:", f.name)           # sample.txt
print("File mode:", f.mode)           # w
print("Is file readable?", f.readable())   # False (w mode)
print("Is file writable?", f.writable())   # True  (w mode)
print("Is file closed?", f.closed)    # False (not closed yet)

f.close()

print("Is file closed?", f.closed)    # True (now closed)
```

**Output:**
```
File name: sample.txt
File mode: w
Is file readable? False
Is file writable? True
Is file closed? False
Is file closed? True
```

---

## 6. Writing Data to Files

### 6.1 Two Write Methods

| Method | Stores | Input |
|--------|--------|-------|
| `f.write(string)` | String data | A single string |
| `f.writelines(list)` | List of lines | A list of strings |

### 6.2 `write()` Method

```python
f = open("abc.txt", "w")

f.write("hello\n")
f.write("hi\n")
f.write("welcome")

print("Data written to the file")
f.close()
```

**File content of `abc.txt`:**
```
hello
hi
welcome
```

> **`\n` adds a new line.** Without `\n`, all text is written on one continuous line.

### 6.3 `writelines()` Method

```python
f = open("abcd.txt", "w")

L = ["Durga\n", "Mohan\n", "Ravi\n", "Rahim\n", "Robert\n"]
f.writelines(L)

print("List data written to the file")
f.close()
```

**File content of `abcd.txt`:**
```
Durga
Mohan
Ravi
Rahim
Robert
```

> `writelines()` does NOT add newlines automatically — include `\n` in each list element.

---

## 7. Append Mode vs Write Mode

```
w mode (Write):     Each time you run, existing data is OVERWRITTEN
a mode (Append):    Each time you run, new data is ADDED to existing data
```

### 7.1 Append Demo

```python
f = open("sample.txt", "a")
f.write("Welcome to Durga's\n")
print("Data written to the file")
f.close()
```

**Run 1:** File contains: `Welcome to Durga's`
**Run 2:** File contains: `Welcome to Durga's\nWelcome to Durga's`
**Run 3:** File contains: three lines...

Every execution adds one more line — data is never overwritten.

---

## 8. Reading Data from Files

### 8.1 Four Read Methods

| Method | Reads | Returns |
|--------|-------|---------|
| `f.read()` | Complete file content | Single string |
| `f.read(n)` | First `n` characters | String of `n` chars |
| `f.readline()` | First line only | String |
| `f.readlines()` | All lines | List of strings |

> **Important:** In read mode (`r`), the file **must already exist**. If not → `FileNotFoundError`.

### 8.2 `read()` — Complete File

```python
f = open("abc.txt", "r")
data = f.read()
print(data)
f.close()
```

**Output:**
```
hello
hi
welcome
```

### 8.3 `read(n)` — Read n Characters

```python
f = open("abc.txt", "r")
print(f.read(3))    # reads first 3 chars: 'hel'
print(f.read(4))    # reads next 4 chars: 'lo\nh'
f.close()
```

### 8.4 `readline()` — First Line Only

```python
f = open("abc.txt", "r")
line = f.readline()
print(line)    # prints: hello
f.close()
```

### 8.5 `readlines()` — All Lines as List

```python
f = open("abc.txt", "r")
lines = f.readlines()
print(lines)    # ['hello\n', 'hi\n', 'welcome']
f.close()
```

---

## 9. FileNotFoundError — Read Mode Requirement

```python
f = open("mohan.txt", "r")    # mohan.txt does not exist
data = f.read()
print(data)
f.close()
```

**Output:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'mohan.txt'
```

**Fix with try-except:**

```python
try:
    f = open("mohan.txt", "r")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError as msg:
    print(msg)
```

---

## 10. Complete Class Walkthrough

### Step 1: File Properties (file1.py)

```python
f = open("sample.txt", "w")
print("File name:", f.name)
print("File mode:", f.mode)
print("Is readable?", f.readable())
print("Is writable?", f.writable())
print("Is closed?", f.closed)
f.close()
print("Is closed?", f.closed)
```

### Step 2: Write with write() (file2.py)

```python
f = open("abc.txt", "w")
f.write("hello\n")
f.write("hi\n")
f.write("welcome")
print("Data written to the file")
f.close()
```

### Step 3: Append Mode (file3.py)

```python
f = open("sample.txt", "a")
f.write("Welcome to Durga's\n")
print("Data written to the file")
f.close()
```

### Step 4: writelines() (file4.py)

```python
f = open("abcd.txt", "w")
L = ["Durga\n", "Mohan\n", "Ravi\n", "Rahim\n", "Robert\n"]
f.writelines(L)
print("List data written to the file")
f.close()
```

### Step 5: All Read Methods

```python
# read() — complete content
f = open("abc.txt", "r")
print(f.read())
f.close()

# read(n) — n characters
f = open("abc.txt", "r")
print(f.read(3))    # 'hel'
f.close()

# readline() — first line
f = open("abc.txt", "r")
print(f.readline())
f.close()

# readlines() — all lines as list
f = open("abc.txt", "r")
print(f.readlines())
f.close()
```

### Step 6: FileNotFoundError Handling

```python
try:
    f = open("mohan.txt", "r")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError as msg:
    print(msg)
```

---

## Student Q&A

> **Student Question:** What is the difference between file system and database storage?
> **Answer:** Both are permanent storage areas, but they differ in capacity and access. File system stores data in files on a single computer (OS level), has limited capacity, and does not support centralized access. Database storage is managed at database level, has unlimited capacity, and supports centralized access — meaning many clients can access one database. For small local data, files are fine; for enterprise applications, use databases.

> **Student Question:** What is the difference between `write()` and `writelines()`?
> **Answer:** `write()` stores a single string. `writelines()` stores a list of strings (list of lines). Both write to the file in write mode. With `writelines()`, you need to include `\n` in each list element yourself — the method does not add newlines automatically.

> **Student Question:** What is the difference between `w` mode and `a` mode?
> **Answer:** `w` mode (write) overwrites the file every time — if the file already has data, it is replaced completely. `a` mode (append) keeps the existing data and adds new data to the end. If you run an append-mode program 5 times, the file will have 5 copies of the data. Both modes create a new file if it doesn't exist.

> **Student Question:** In read mode, what happens if the file does not exist?
> **Answer:** Python raises `FileNotFoundError`. In read mode, the file must already exist — unlike write and append modes that create the file if absent. Always handle this with try-except when reading files whose existence is uncertain.

> **Student Question:** What is the default file mode?
> **Answer:** The default mode is `r` (read mode). If you open a file without specifying a mode, Python uses read mode. So `open("sample.txt")` is the same as `open("sample.txt", "r")`.

---

## Key Differences

| Feature | `write()` | `writelines()` |
|---------|-----------|----------------|
| Input | Single string | List of strings |
| Newlines | Must add `\n` manually | Must add `\n` in list elements |
| Use case | Store one piece of text | Store multiple lines from a list |

| Feature | `read()` | `read(n)` | `readline()` | `readlines()` |
|---------|---------|---------|------------|-------------|
| Reads | Complete file | n characters | First line | All lines |
| Returns | String | String | String | List of strings |
| Use case | Read all at once | Read chunks | First line only | Process line by line |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `FileNotFoundError: No such file or directory` | File does not exist in read mode | Use try-except or ensure file exists before opening |
| Data overwritten unexpectedly | Using `w` mode on existing file | Switch to `a` (append) mode |
| No newlines between written items | Missing `\n` in `write()` calls | Add `\n`: `f.write("text\n")` |
| `ValueError: read of closed file` | Trying to read after `f.close()` | Open file again before reading |
| `FileExistsError` | Using `x` mode on existing file | Use a different file name or `w` mode |

---

## Interview Questions

**Q: What is file handling in Python?**
A: File handling is the process of storing data permanently into files (text or binary) and retrieving it when needed. Python provides built-in functions and methods to create, read, write, append, and close files. The main function is `open()`, which returns a file object.

**Q: What are the different file modes in Python?**
A: `r` (read), `w` (write/overwrite), `a` (append), `x` (exclusive create), `r+` (read and write), `w+` (write and read), `a+` (append and read). Adding `b` suffix makes them binary modes: `rb`, `wb`, `ab`, etc.

**Q: What is the difference between `w` and `a` mode?**
A: `w` (write) mode overwrites all existing content each time the file is opened. `a` (append) mode adds new data to the end of existing content without deleting it. Both modes create the file if it doesn't exist.

**Q: What happens in `r` mode if the file does not exist?**
A: Python raises `FileNotFoundError`. The `r` mode requires the file to already exist. Unlike `w` and `a` modes, read mode does not create the file automatically.

**Q: What are `write()` and `writelines()` methods?**
A: `write(string)` stores a single string to the file. `writelines(list)` stores a list of strings to the file. Neither method adds newlines automatically — you must include `\n` in your strings.

**Q: What are the different read methods in Python file handling?**
A: `read()` reads the complete file and returns a single string. `read(n)` reads the first `n` characters. `readline()` reads the first line. `readlines()` reads all lines and returns them as a list.

**Q: Why should we close a file after operations?**
A: Not closing a file can cause data loss (buffered data may not be written to disk), file corruption, and resource leaks (file handles are limited OS resources). Always call `f.close()` after operations, or use the `with` statement which closes automatically.

---

## Try It Yourself

**Exercise 1:** Create a text file called `my_info.txt` and write your name, age, and city on separate lines using the `write()` method. Then read the file and print its content.

<details><summary>Answer</summary>

```python
# Write
f = open("my_info.txt", "w")
f.write("Name: Alice\n")
f.write("Age: 25\n")
f.write("City: Hyderabad\n")
f.close()

# Read
f = open("my_info.txt", "r")
print(f.read())
f.close()
```
</details>

---

**Exercise 2:** Use `writelines()` to store a list of 5 fruits in a file called `fruits.txt`. Then use `readlines()` to read them back and print each fruit on a separate line.

<details><summary>Answer</summary>

```python
fruits = ["Apple\n", "Banana\n", "Cherry\n", "Mango\n", "Orange\n"]

f = open("fruits.txt", "w")
f.writelines(fruits)
f.close()

f = open("fruits.txt", "r")
lines = f.readlines()
for line in lines:
    print(line.strip())    # strip() removes \n
f.close()
```
</details>

---

**Exercise 3:** Open a file in append mode and add a new line each time the program runs. Run the program 3 times and open the file to see all 3 lines.

<details><summary>Answer</summary>

```python
f = open("log.txt", "a")
f.write("Program executed\n")
f.close()

# Read to verify
f = open("log.txt", "r")
print(f.read())
f.close()
```
</details>

---

**Exercise 4:** Write a program that accepts a filename from the user and prints its content. Handle `FileNotFoundError` using try-except.

<details><summary>Answer</summary>

```python
filename = input("Enter filename to read: ")
try:
    f = open(filename, "r")
    print(f.read())
    f.close()
except FileNotFoundError as msg:
    print("File not found:", msg)
```
</details>

---

**Exercise 5:** Demonstrate the difference between `w` and `a` modes. Run a `w` mode program twice and show the file content each time. Then switch to `a` mode and run twice. Compare results.

<details><summary>Answer</summary>

```python
# w mode — run this twice, file always has only one line
f = open("test_w.txt", "w")
f.write("Hello from w mode\n")
f.close()

f = open("test_w.txt", "r")
print("After w mode:", f.read())
f.close()

# a mode — run this twice, file accumulates lines
f = open("test_a.txt", "a")
f.write("Hello from a mode\n")
f.close()

f = open("test_a.txt", "r")
print("After a mode:", f.read())
f.close()
```
</details>
