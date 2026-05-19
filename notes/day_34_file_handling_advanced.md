# Day 34 — File Handling: with Statement, tell/seek, File Modification, os.path

← [Day 33](day_33_file_handling_basics.md) | [Index](00_INDEX.md) | [Day 35](day_35_zip_csv_files.md) →

---

## Quick Revision — Day 34

| # | Key Point |
|---|-----------|
| 1 | `x` mode (exclusive creation): file must NOT exist → `FileExistsError` if it does |
| 2 | `with` statement: groups file operations in a block; **auto-closes file** on exit |
| 3 | Inside `with` block: `f.closed` → `False`; after exiting: `f.closed` → `True` |
| 4 | `tell()` method: returns **current cursor position** (index) |
| 5 | `seek(n)` method: **moves cursor** to position `n` |
| 6 | File modification uses `r+` mode (read and write) |
| 7 | After reading, cursor is at end — use `seek(0)` to go back to beginning |
| 8 | `import os` → `os.path.isfile("filename")` → `True` if file exists, `False` if not |
| 9 | `os._exit(0)` stops program immediately (PVM shutdown) |
| 10 | Count lines, words, characters by reading file line-by-line with a for loop |

---

## Navigation

- **Pre-requisite:** [Day 33](day_33_file_handling_basics.md) — File modes, write/read methods
- **Next:** [Day 35](day_35_zip_csv_files.md) — ZIP/UNZIP operations and CSV files
- **Related:** [Day 32](day_32_exception_advanced_custom.md) — Exception handling (FileNotFoundError, FileExistsError)

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `file6.py` | Exclusive creation mode (`x`) demo |
| `.py` file | `file7.py` | `with` statement demo, `f.closed` check |
| `.py` file | `file8.py` | `tell()` and `seek()` demo |
| `.py` file | `file9.py` | File modification with `r+` mode |
| `.py` file | `file10.py` | `os.path.isfile()` to check file existence |
| Program | Line/word/character counter | Count lines, words, chars in a file |
| Method | `f.tell()` | Returns current cursor position |
| Method | `f.seek(n)` | Moves cursor to position n |
| Function | `os.path.isfile(fname)` | Check if file exists |
| Module | `os` | Operating system utilities |
| File created | `xyz.txt` | Created with exclusive creation (x) mode |

---

## 1. Exclusive Creation Mode (`x`)

```
x mode (exclusive creation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Purpose: Create a BRAND NEW file for write operations
Rule:    File name must NOT already exist
If file exists: FileExistsError
If file absent: Creates the new file instantly
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```python
try:
    f = open("abc.txt", "x")    # abc.txt already exists → error
    f.write("hello\n")
    f.write("hydra path\n")
    print("Data written to the file")
    f.close()
except FileExistsError as msg:
    print(msg)
```

**Output (if abc.txt exists):** `[Errno 17] File exists: 'abc.txt'`

```python
try:
    f = open("xyz.txt", "x")    # xyz.txt does NOT exist → created
    f.write("hello\n")
    f.write("hydra path\n")
    print("Data written to the file")
    f.close()
except FileExistsError as msg:
    print(msg)
```

**Output:** `Data written to the file` — and `xyz.txt` is created.

---

## 2. `with` Statement

### 2.1 What Is `with`?

```
with statement
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with keyword: groups ALL file operation statements into a block

Syntax:
    with open("filename.txt", mode) as f:
        statement 1
        statement 2
        statement 3
        ...
        (all these are part of the with block)

Main Advantage:
    Once you EXIT the with block → file closes AUTOMATICALLY
    You do NOT need to call f.close() explicitly
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2.2 Syntax Comparison

```python
# Without with statement — manual close required
f = open("sample.txt", "w")
f.write("hello\n")
f.write("hi\n")
f.close()    # must remember to close

# With 'with' statement — auto-close
with open("sample.txt", "w") as f:
    f.write("hello\n")
    f.write("hi\n")
# file is automatically closed here when block exits
```

### 2.3 Demo — Checking `f.closed`

```python
with open("regard.txt", "w") as f:
    f.write("hello\n")
    f.write("hi\n")
    f.write("this is")
    print("Is file closed?", f.closed)    # False — still in with block

# exited with block
print("Is file closed?", f.closed)        # True — auto-closed
```

**Output:**
```
Is file closed? False
Is file closed? True
```

> Inside the `with` block, the file is still open. Once you exit the block, it is automatically closed — no `f.close()` needed.

### 2.4 Why Use `with`?

When doing file **modification** (open → read → seek → write → read again), you open and close the file multiple times. The `with` block lets you do all operations in one block without repeated close calls.

---

## 3. `tell()` and `seek()` Methods

These two methods control the **cursor position** (file pointer) inside a file.

```
File Cursor Concept
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Imagine the file as a long text:
    h  e  l  l  o     h  i     w  e  l  c  o  m  e
    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15

Cursor starts at position 0 (beginning of file in r mode)
As you read characters, cursor moves forward automatically.

tell()  → "Where is the cursor right now?"
seek(n) → "Move the cursor to position n"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3.1 `tell()` Method

```python
f = open("abc.txt", "r")
print("Cursor position:", f.tell())    # 0 — start of file

data = f.read(3)                       # read 3 chars: "hel"
print("Read:", data)
print("Cursor position:", f.tell())    # 3

data = f.read(4)                       # read 4 more chars: "lo\nh"
print("Read:", data)
print("Cursor position:", f.tell())    # 7 (3+4, including \n)

f.close()
```

**Output:**
```
Cursor position: 0
Read: hel
Cursor position: 3
Read: lo
h
Cursor position: 7
```

### 3.2 `seek()` Method

```python
f = open("abc.txt", "r")

print("Position:", f.tell())    # 0
f.read(5)                       # move cursor forward 5
print("Position:", f.tell())    # 5

f.seek(0)                       # move cursor back to beginning
print("Position:", f.tell())    # 0

f.seek(13)                      # jump to position 13
print("Position:", f.tell())    # 13

f.close()
```

> `seek(0)` resets the cursor to the beginning. This is essential for reading a file again after already reading it once.

---

## 4. File Modification

To modify a file:
1. Open in `r+` mode (read and write)
2. Read the content (cursor moves to end)
3. Use `seek(n)` to move cursor to modification point
4. Write the new data
5. Use `seek(0)` to go back to start
6. Read again to verify the change

### 4.1 Complete File Modification Example

```python
# Step 1: Create the file with initial data
data = "My name is Durga"
f = open("triple.txt", "w")
f.write(data)
f.close()

# Step 2: Read, modify, and verify using with block
with open("triple.txt", "r+") as f:
    print("Cursor before reading:", f.tell())    # 0

    text = f.read()
    print("Content:", text)                       # My name is Durga

    print("Cursor after reading:", f.tell())      # 16 (length of string)

    f.seek(11)                                    # move to position 11 (where 'D' in 'Durga' is)
    print("Cursor after seek:", f.tell())         # 11

    f.write("Mohan")                              # overwrite 'Durga' with 'Mohan'

    f.seek(0)                                     # move cursor back to start
    print("Data after modification:", f.read())   # My name is Mohan
```

**Output:**
```
Cursor before reading: 0
Content: My name is Durga
Cursor after reading: 16
Cursor after seek: 11
Data after modification: My name is Mohan
```

> **Why `seek(0)` before final read?** After writing "Mohan", cursor is at position 16 (end). Reading from position 16 gives nothing. Move cursor to 0 first, then read from the beginning to see the full updated content.

### 4.2 Modification Flow Diagram

```
File Modification Flow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 1: Open file in r+ mode
Step 2: tell() → cursor at 0 (beginning)
Step 3: read() → reads all content; cursor moves to end (16)
Step 4: seek(11) → move cursor to position 11 (modification point)
Step 5: write("Mohan") → overwrites 5 chars from position 11
Step 6: seek(0) → move cursor back to beginning
Step 7: read() → read full file from 0 to see updated content
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 5. Checking File Existence — `os.path.isfile()`

```
os module (operating system module)
    ↓
os.path (sub-module with file/directory path utilities)
    ↓
os.path.isfile(filename) — function to check if file exists
    Returns: True  (if file exists)
             False (if file does not exist)
```

### 5.1 Syntax

```python
import os
os.path.isfile("filename.txt")    # True or False
```

### 5.2 Example — Check and Read

```python
import os

fname = input("Enter file name to check: ")

if os.path.isfile(fname):
    print(fname, "file exists")
    f = open(fname, "r")
    print("Content of the file:")
    print(f.read())
    f.close()
else:
    print(fname, "file does not exist")
```

**Input: abc.txt (exists)** → Prints content
**Input: mohan.txt (does not exist)** → `mohan.txt file does not exist`

---

## 6. Counting Lines, Words, and Characters

```python
import os

fname = input("Enter file name to check: ")

if os.path.isfile(fname):
    f = open(fname, "r")
    print(fname, "file exists")

    l_count = w_count = c_count = 0    # line, word, character counts

    for line in f:                     # iterate through each line
        l_count += 1                   # count lines
        c_count += len(line)           # count characters (including \n)
        words = line.split()           # split line into words
        w_count += len(words)          # count words

    f.close()

    print("Number of lines:", l_count)
    print("Number of words:", w_count)
    print("Number of characters:", c_count)
else:
    print(fname, "file does not exist")
    import os
    os._exit(0)                        # stop program if file not found
```

> **Important cursor note:** If you use `f.read()` first to print the content, the cursor moves to the end. Then the `for line in f` loop reads nothing (cursor already at end). Either:
> - Do the content print AFTER the loop, OR
> - Use `f.seek(0)` to reset cursor before the loop

**Corrected version with content + count:**

```python
import os

fname = input("Enter file name: ")

if os.path.isfile(fname):
    f = open(fname, "r")

    l_count = w_count = c_count = 0

    for line in f:
        l_count += 1
        c_count += len(line)
        words = line.split()
        w_count += len(words)

    f.seek(0)                    # reset cursor to read content
    print("Content:", f.read())  # print content after counting
    f.close()

    print("Lines:", l_count)
    print("Words:", w_count)
    print("Characters:", c_count)
else:
    print("File does not exist:", fname)
    os._exit(0)
```

---

## 7. Complete Class Walkthrough

### Step 1: x mode — Exclusive Creation (file6.py)

```python
try:
    f = open("abc.txt", "x")
    f.write("hello\n")
    f.write("hydra path\n")
    print("Data written to the file")
    f.close()
except FileExistsError as msg:
    print(msg)
```

### Step 2: with Statement (file7.py)

```python
with open("regard.txt", "w") as f:
    f.write("hello\n")
    f.write("hi\n")
    f.write("this is")
    print("Is file closed?", f.closed)    # False

print("Is file closed?", f.closed)        # True
```

### Step 3: tell() and seek() (file8.py)

```python
f = open("abc.txt", "r")
print("Position:", f.tell())     # 0
print(f.read(3))                 # hel
print("Position:", f.tell())     # 3
f.seek(0)
print("Position:", f.tell())     # 0 again
f.close()
```

### Step 4: File Modification (file9.py)

```python
data = "My name is Durga"
f = open("triple.txt", "w")
f.write(data)
f.close()

with open("triple.txt", "r+") as f:
    print("Cursor before reading:", f.tell())
    text = f.read()
    print("Content:", text)
    print("Cursor after reading:", f.tell())
    f.seek(11)
    f.write("Mohan")
    f.seek(0)
    print("Data after modification:", f.read())
```

### Step 5: Check File Existence (file10.py)

```python
import os

fname = input("Enter file name to check: ")
if os.path.isfile(fname):
    print(fname, "file exists")
    f = open(fname, "r")
    print(f.read())
    f.close()
else:
    print(fname, "file does not exist")
```

### Step 6: Line/Word/Character Counter

```python
import os

fname = input("Enter file name: ")
if os.path.isfile(fname):
    f = open(fname, "r")
    l_count = w_count = c_count = 0
    for line in f:
        l_count += 1
        c_count += len(line)
        words = line.split()
        w_count += len(words)
    f.seek(0)
    print("Content:", f.read())
    f.close()
    print("Lines:", l_count)
    print("Words:", w_count)
    print("Characters:", c_count)
else:
    print("File does not exist:", fname)
    os._exit(0)
```

---

## Student Q&A

> **Student Question:** What is the main advantage of the `with` statement?
> **Answer:** The main advantage is automatic file closing. Once you exit the `with` block, Python automatically calls `f.close()` for you. This is especially useful during file modification when you perform many operations — you don't need to open and close the file repeatedly. Everything within the `with` block is treated as one group of operations.

> **Student Question:** What is the difference between `tell()` and `seek()`?
> **Answer:** `tell()` returns the current cursor position (the index where the cursor is right now). `seek(n)` moves the cursor to position `n`. Think of the cursor as a blinking text cursor in a word processor — `tell()` tells you where it is, and `seek()` lets you jump to any position.

> **Student Question:** Why do we need `seek(0)` after reading before reading again?
> **Answer:** When you read a file using `read()`, the cursor moves to the end of the file. If you try to read again without resetting, you start from the end — and there's nothing to read. `seek(0)` moves the cursor back to position 0 (beginning), so the next read starts from the beginning of the file.

> **Student Question:** What mode should we use for file modification?
> **Answer:** Use `r+` mode (read and write). This allows you to read the existing content and then write (overwrite) specific parts. Using `r+` does not delete existing content — it places the cursor at the beginning and lets you read and write selectively.

> **Student Question:** What is `os.path.isfile()`?
> **Answer:** It is a function from the `os` module (operating system module) that checks whether a file exists. `os.path` is a sub-module, and `isfile()` is the function. It accepts a filename as input and returns `True` if the file exists, `False` if not. This is useful before opening a file in read mode to avoid `FileNotFoundError`.

---

## Key Differences

| Feature | `tell()` | `seek()` |
|---------|---------|---------|
| Purpose | Get cursor position | Move cursor position |
| Returns | Current index (int) | Nothing |
| Syntax | `f.tell()` | `f.seek(n)` |

| Feature | With `with` statement | Without `with` statement |
|---------|----------------------|--------------------------|
| Close file | Automatic on block exit | Must call `f.close()` manually |
| Risk | No leak risk | Might forget to close |
| Code length | Slightly more concise | Slightly verbose |
| Recommended? | Yes (preferred) | Acceptable for simple cases |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `FileExistsError` | Opening existing file in `x` mode | Use `w` mode or try-except |
| Empty output after `f.read()` then loop | Cursor at end after `read()` | Use `f.seek(0)` before the loop |
| Modified file still shows old data | Read after write without `seek(0)` | Call `f.seek(0)` after writing, before reading |
| `FileNotFoundError` in `r+` mode | File does not exist | Create file with `w` mode first, or use try-except |
| `AttributeError: 'str' object has no attribute 'read'` | Used string variable name instead of file object | Check that `f` is the file object from `open()`, not a string |

---

## Interview Questions

**Q: What is the `with` statement in Python file handling?**
A: The `with` statement groups all file operation statements into a block. Its main advantage is automatic file closing — once execution exits the `with` block, the file is closed automatically without needing `f.close()`. It uses Python's context manager protocol.

**Q: What is the difference between `tell()` and `seek()` methods?**
A: `tell()` returns the current cursor (file pointer) position as an integer. `seek(n)` moves the cursor to position `n`. They are used together for file navigation — especially during file modification, where you need to find your position, jump to a specific index, write data, then reset the cursor to read the updated content.

**Q: How do you check if a file exists in Python?**
A: Use `os.path.isfile("filename.txt")` from the `os` module. It returns `True` if the file exists and `False` if it doesn't. This is useful before opening a file in read mode to avoid `FileNotFoundError`.

**Q: What is `r+` mode in Python?**
A: `r+` mode opens an existing file for both reading and writing. Unlike `w+`, it does not overwrite existing data — the cursor starts at the beginning, and you can read and selectively write/overwrite portions of the file. Used primarily for file modification.

**Q: How do you count lines, words, and characters in a file?**
A: Open the file in read mode and iterate using a `for` loop (which reads one line at a time). Increment `l_count` for each line, add `len(line)` to `c_count` for characters, and use `line.split()` to get a list of words (add its length to `w_count`).

---

## Try It Yourself

**Exercise 1:** Create a file and write "Python is awesome" to it. Use `tell()` to find the cursor position before and after reading the file.

<details><summary>Answer</summary>

```python
f = open("demo.txt", "w")
f.write("Python is awesome")
f.close()

f = open("demo.txt", "r")
print("Position before read:", f.tell())    # 0
data = f.read()
print("Position after read:", f.tell())     # 17
print("Content:", data)
f.close()
```
</details>

---

**Exercise 2:** Create a file with "Hello World" and use `seek()` to move the cursor to position 6 and read the remaining content.

<details><summary>Answer</summary>

```python
f = open("hw.txt", "w")
f.write("Hello World")
f.close()

f = open("hw.txt", "r")
f.seek(6)                   # move to position 6 (W in World)
print(f.read())             # prints: World
f.close()
```
</details>

---

**Exercise 3:** Use the `with` statement to write three lines to a file and verify it auto-closes by printing `f.closed` inside and outside the block.

<details><summary>Answer</summary>

```python
with open("test_with.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    print("Inside with block - closed:", f.closed)    # False

print("Outside with block - closed:", f.closed)       # True
```
</details>

---

**Exercise 4:** Use `os.path.isfile()` to check if a user-specified file exists. If it exists, print the number of lines. If not, print an error message.

<details><summary>Answer</summary>

```python
import os

fname = input("Enter filename: ")
if os.path.isfile(fname):
    f = open(fname, "r")
    count = sum(1 for line in f)
    f.close()
    print(f"{fname} has {count} lines")
else:
    print(f"{fname} does not exist")
```
</details>

---

**Exercise 5:** Create a file with "My name is Alice". Use `r+` mode to change "Alice" to "Bob". Print the file content before and after the change.

<details><summary>Answer</summary>

```python
f = open("name.txt", "w")
f.write("My name is Alice")
f.close()

with open("name.txt", "r+") as f:
    print("Before:", f.read())     # My name is Alice
    f.seek(11)                     # position of 'A' in Alice
    f.write("Bob  ")               # overwrite Alice with Bob + spaces
    f.seek(0)
    print("After: ", f.read())     # My name is Bob
```
</details>
