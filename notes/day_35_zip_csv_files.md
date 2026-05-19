# Day 35 — ZIP/UNZIP Operations and CSV Files

← [Day 34](day_34_file_handling_advanced.md) | [Index](00_INDEX.md) | [Day 36](day_36_binary_files_pickling.md) →

---

## Quick Revision — Day 35

| # | Key Point |
|---|-----------|
| 1 | ZIP = compress multiple files into one `.zip` folder (also called RAR folder) |
| 2 | UNZIP = extract files from a `.zip` folder |
| 3 | `zipfile` module (built-in): class is `ZipFile` (capital Z, capital F) |
| 4 | `from zipfile import *` allows using `ZipFile` and constants without prefix |
| 5 | `ZIP_DEFLATED` constant → used when writing (zipping) files |
| 6 | `ZIP_STORED` constant → used when reading (unzipping) files |
| 7 | `f.write(filename)` writes a file into the ZIP archive |
| 8 | `f.namelist()` returns a list of all filenames stored in the ZIP |
| 9 | CSV = Comma Separated Values; used to work with Excel-like data |
| 10 | `csv.writer(f)` → writer object; `csv.reader(f)` → reader object |
| 11 | `writer.writerow([list])` writes one row to CSV |
| 12 | CSV file extension is `.csv`; opens in Excel as a spreadsheet |

---

## Navigation

- **Pre-requisite:** [Day 34](day_34_file_handling_advanced.md) — with statement, file operations
- **Next:** Day 36 — Binary files, pickling and unpickling
- **Related:** [Day 33](day_33_file_handling_basics.md) — Text file basics, file modes

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| `.py` file | `file11.py` | Create ZIP file, write files into it |
| `.py` file | `file12.py` | Extract (UNZIP) files and print content |
| `.py` file | `file13.py` | Write employee data into CSV file |
| `.py` file | `file14.py` | Read employee data from CSV file |
| Module | `zipfile` | Built-in ZIP/UNZIP operations |
| Module | `csv` | Built-in CSV read/write operations |
| Class | `ZipFile` | From `zipfile` module |
| Constant | `ZIP_DEFLATED` | For zip write mode |
| Constant | `ZIP_STORED` | For zip read/extract mode |
| Method | `f.namelist()` | List of filenames in ZIP archive |
| Method | `writer.writerow([...])` | Write one row to CSV |
| File created | `files.zip` | ZIP archive containing text files |
| File created | `emp.csv` | CSV file with employee data |

---

## 1. ZIP and UNZIP Operations

### 1.1 What is ZIP?

```
ZIP / RAR Concept
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ZIP:   Compress multiple files into one .zip folder
       ZIP stands for: Zonal Information Protocol
       RAR stands for: Roshal ARchive (named after inventor)
       TAR stands for: Tape ARchive (more secure, needs credentials)

UNZIP: Extract files from a .zip folder one by one

Use case: Sending or storing multiple files as one compact archive
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 1.2 The `zipfile` Module

```
zipfile module
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Module name (lowercase): zipfile
Class name (CamelCase):  ZipFile

Constants:
    ZIP_DEFLATED → indicates writing files INTO zip
    ZIP_STORED   → indicates extracting files FROM zip

Both constants are optional — but used for clarity
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> **Important naming:** `zipfile` (lowercase) is the module name. `ZipFile` (capital Z, capital F) is the class inside the module.

---

## 2. Creating a ZIP File (Zipping)

### 2.1 Syntax

```python
from zipfile import *    # import everything from zipfile module

f = ZipFile("archive_name.zip", "w", ZIP_DEFLATED)
f.write("file1.txt")
f.write("file2.txt")
f.write("file3.txt")
f.close()
```

### 2.2 Full Example — Creating ZIP

```python
from zipfile import *

f = ZipFile("files.zip", "w", ZIP_DEFLATED)

# Write all desired text files into the ZIP archive
f.write("abc.txt")
f.write("abcd.txt")
f.write("sample.txt")

f.close()
print("ZIP file created successfully")
```

**Output:** `ZIP file created successfully`

The `files.zip` file appears in your project. If you go to the physical location on your drive (`D:/Python project/`) and extract manually, you will see all files inside with their data.

> **Why `from zipfile import *`?** Without it, you'd have to write `zipfile.ZipFile` and `zipfile.ZIP_DEFLATED`. With `from zipfile import *`, you can use `ZipFile` and `ZIP_DEFLATED` directly.

---

## 3. Extracting from ZIP (Unzipping)

### 3.1 Syntax

```python
from zipfile import *

f = ZipFile("archive_name.zip", "r", ZIP_STORED)
names = f.namelist()     # list of all files in the ZIP

for name in names:
    f1 = open(name, "r")
    print(f1.read())
    f1.close()

f.close()
```

### 3.2 `namelist()` Method

```
f.namelist()
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Returns: A list of all filenames stored in the ZIP
Example: ['abc.txt', 'abcd.txt', 'sample.txt']
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3.3 Full Example — Extracting ZIP

```python
from zipfile import *

f = ZipFile("files.zip", "r", ZIP_STORED)
names = f.namelist()

for name in names:
    print("File name:", name)
    f1 = open(name, "r")
    print("Content:")
    print(f1.read())
    print()                   # blank line between files
    f1.close()

f.close()
```

**Output:**
```
File name: abc.txt
Content:
hello
hi
welcome

File name: abcd.txt
Content:
Durga
Mohan
Ravi
...
```

---

## 4. ZIP Operations — Summary Diagram

```
ZIP and UNZIP Flow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ZIPPING (Creating):
    abc.txt   ─┐
    abcd.txt  ─┼→  f.write() →  files.zip
    sample.txt ─┘

UNZIPPING (Extracting):
    files.zip  →  f.namelist()  →  ['abc.txt', 'abcd.txt', ...]
                                         ↓
                                   for name in names:
                                     open(name, "r").read()
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 5. CSV Files

### 5.1 What is CSV?

```
CSV — Comma Separated Values
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extension: .csv
Purpose:   Store tabular data (like Excel spreadsheet)
Format:    Each row is a line; values separated by commas

When you open a .csv file in Excel, it displays as a table:
    emp_no | emp_name | salary | address
    -------|----------|--------|--------
    101    | Ali      | 5000   | HYD
    102    | She      | 4000   | HYD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.2 The `csv` Module

```python
import csv
```

| Object | Created with | Purpose |
|--------|-------------|---------|
| Writer object | `csv.writer(f)` | Write rows to CSV |
| Reader object | `csv.reader(f)` | Read rows from CSV |

---

## 6. Writing Data to CSV

### 6.1 `writerow()` Method

```
writer.writerow([list])
→ Writes one row (a list) to the CSV file
→ Each element in the list becomes one column
```

### 6.2 Full Example — Writing CSV (file13.py)

```python
import csv

with open("emp.csv", "w", newline="") as f:
    w = csv.writer(f)

    # Write header row
    w.writerow(["Emp_No", "Emp_Name", "Emp_Salary", "Emp_Address"])

    # Accept employee data from user
    n = int(input("Enter number of employees: "))
    for i in range(n):
        emp_no = input("Enter employee number: ")
        emp_name = input("Enter employee name: ")
        emp_salary = input("Enter employee salary: ")
        emp_address = input("Enter employee address: ")
        w.writerow([emp_no, emp_name, emp_salary, emp_address])

print("Employee data written to CSV file successfully")
```

**Sample Interaction:**
```
Enter number of employees: 2
Enter employee number: 101
Enter employee name: Ali
Enter employee salary: 5000
Enter employee address: HYD
Enter employee number: 102
Enter employee name: She
Enter employee salary: 4000
Enter employee address: HYD
Employee data written to CSV file successfully
```

**Generated `emp.csv` (viewed in Excel):**

| Emp_No | Emp_Name | Emp_Salary | Emp_Address |
|--------|----------|------------|-------------|
| 101    | Ali      | 5000       | HYD         |
| 102    | She      | 4000       | HYD         |

> **Why `newline=""`?** Without this attribute, CSV files include blank lines between each row. Adding `newline=""` prevents those blank lines and keeps the format clean.

---

## 7. Reading Data from CSV

### 7.1 Reading Process

```python
import csv

f = open("emp.csv", "r")
r = csv.reader(f)           # reader object
data = list(r)              # convert reader to list of rows
f.close()
```

### 7.2 Printing CSV in Table Format

```python
import csv

f = open("emp.csv", "r")
r = csv.reader(f)
data = list(r)
f.close()

for line in data:
    for word in line:
        print(word, end="\t")    # tab between columns
    print()                       # new line after each row
```

**Output:**
```
Emp_No    Emp_Name    Emp_Salary    Emp_Address
101       Ali         5000          HYD
102       She         4000          HYD
```

### 7.3 Full Example — Reading CSV (file14.py)

```python
import csv

f = open("emp.csv", "r")
r = csv.reader(f)
data = list(r)
f.close()

print("Employee Data:")
for line in data:
    for word in line:
        print(word, end="\t")
    print()
```

---

## 8. CSV — Understanding the Reader Object

When you print `r` (the reader object) directly, you get a memory reference:
```
<_csv.reader object at 0x000001F2...>
```

To access data, convert it to a list:
```python
data = list(r)    # list of lists — each inner list is one row
print(data)
# [['Emp_No', 'Emp_Name', 'Emp_Salary', 'Emp_Address'],
#  ['101', 'Ali', '5000', 'HYD'],
#  ['102', 'She', '4000', 'HYD']]
```

Each row in data is a **list**. The entire dataset is a **list of lists** (nested list).

---

## 9. Complete Class Walkthrough

### Step 1: Create ZIP File (file11.py)

```python
from zipfile import *

f = ZipFile("files.zip", "w", ZIP_DEFLATED)
f.write("abc.txt")
f.write("abcd.txt")
f.write("sample.txt")
f.close()
print("ZIP file created successfully")
```

### Step 2: Extract ZIP File (file12.py)

```python
from zipfile import *

f = ZipFile("files.zip", "r", ZIP_STORED)
names = f.namelist()

for name in names:
    print("File name:", name)
    f1 = open(name, "r")
    print(f1.read())
    print()
    f1.close()

f.close()
```

### Step 3: Write CSV (file13.py)

```python
import csv

with open("emp.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Emp_No", "Emp_Name", "Emp_Salary", "Emp_Address"])
    n = int(input("Enter number of employees: "))
    for i in range(n):
        emp_no = input("Enter employee number: ")
        emp_name = input("Enter employee name: ")
        emp_salary = input("Enter employee salary: ")
        emp_address = input("Enter employee address: ")
        w.writerow([emp_no, emp_name, emp_salary, emp_address])

print("Employee data written to CSV file successfully")
```

### Step 4: Read CSV (file14.py)

```python
import csv

f = open("emp.csv", "r")
r = csv.reader(f)
data = list(r)
f.close()

for line in data:
    for word in line:
        print(word, end="\t")
    print()
```

---

## Student Q&A

> **Student Question:** What is the difference between a ZIP file and a RAR file?
> **Answer:** Both are compressed archive formats. ZIP (Zonal Information Protocol) is the most common format and is cross-platform. RAR (Roshal ARchive, named after inventor Eugene Roshal) is another format. In Python, we work with ZIP files using the `zipfile` module. TAR is another archive format commonly used in Linux for highly secure file transfers (requires credentials/password for extraction).

> **Student Question:** What is the difference between `zipfile` (module) and `ZipFile` (class)?
> **Answer:** `zipfile` is the module name (lowercase). `ZipFile` is the class inside the module (capital Z, capital F). When you write `from zipfile import *`, you can then use `ZipFile` directly. Without the import, you'd need `zipfile.ZipFile`. The naming difference (case) distinguishes the module from the class.

> **Student Question:** What does `ZIP_DEFLATED` mean?
> **Answer:** `ZIP_DEFLATED` is a constant that indicates you are writing (compressing) files into the ZIP archive. `ZIP_STORED` indicates you are reading (extracting) files from the ZIP archive. Both constants are optional — the program still works without them — but including them makes the intent clear.

> **Student Question:** Why do we need `newline=""` when writing CSV?
> **Answer:** Without `newline=""`, the CSV writer adds extra blank lines between each row. The `newline=""` attribute prevents those blank lines, keeping the CSV data in a clean, proper format. This is a specific requirement for CSV file writing in Python.

> **Student Question:** What is the difference between `write()` (text file) and `writerow()` (CSV)?
> **Answer:** `write(string)` writes a plain string to a text file. `writerow([list])` writes a list of values as one row in a CSV file, with values automatically separated by commas. For CSV, always use `csv.writer` and `writerow()` — not plain `write()`.

---

## Key Differences

| Feature | ZIP File | Text File | CSV File |
|---------|----------|-----------|----------|
| Extension | `.zip` | `.txt` | `.csv` |
| Module | `zipfile` | Built-in `open()` | `csv` |
| Purpose | Archive/compress files | Store text | Store tabular data |
| View in | WinRAR, 7-Zip | Notepad | Excel |
| Write method | `f.write(filename)` | `f.write(string)` | `writer.writerow([...])` |
| Read method | `f.namelist()` + open | `f.read()` | `csv.reader(f)` |

| Feature | `ZIP_DEFLATED` | `ZIP_STORED` |
|---------|---------------|-------------|
| Used for | Creating/writing ZIP | Extracting/reading ZIP |
| Mode paired with | `"w"` | `"r"` |
| Optional? | Yes | Yes |

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `FileNotFoundError` in UNZIP | `files.zip` doesn't exist | Create the ZIP file first (run file11 before file12) |
| `NameError: ZipFile is not defined` | Forgot `from zipfile import *` | Add `from zipfile import *` or `import zipfile` |
| Blank lines between CSV rows | Missing `newline=""` in CSV `open()` | Use `open("emp.csv", "w", newline="")` |
| CSV reader shows object reference | Printing `r` directly | Convert to list: `data = list(r)` and print `data` |
| File added to ZIP not found | File doesn't exist in project directory | Ensure the file exists before calling `f.write(filename)` |

---

## Interview Questions

**Q: What is the `zipfile` module in Python?**
A: The `zipfile` module is a built-in Python module for working with ZIP archive files. It provides the `ZipFile` class to create, read, and extract ZIP files. Use `from zipfile import *` to import all contents. The `ZIP_DEFLATED` constant is used for compression (writing), and `ZIP_STORED` for extraction (reading).

**Q: How do you create a ZIP file in Python?**
A: Use `from zipfile import *`, create a `ZipFile` object in write mode: `f = ZipFile("archive.zip", "w", ZIP_DEFLATED)`, then call `f.write("filename.txt")` for each file to add. Close with `f.close()`.

**Q: How do you extract files from a ZIP archive?**
A: Open the ZIP in read mode: `f = ZipFile("archive.zip", "r", ZIP_STORED)`. Use `f.namelist()` to get a list of all file names inside. Then loop through the names, open each file with `open(name, "r")`, and read its content.

**Q: What is CSV in Python?**
A: CSV stands for Comma Separated Values. It is a file format (`.csv`) for storing tabular data — each row is one record, and values are separated by commas. When opened in Excel, CSV displays as a spreadsheet. Python's built-in `csv` module provides `csv.writer` for writing and `csv.reader` for reading CSV data.

**Q: What is the difference between `csv.writer` and `csv.reader`?**
A: `csv.writer(f)` creates a writer object that can write rows to a CSV file using `writerow([list])`. `csv.reader(f)` creates a reader object that reads rows from a CSV file — convert it to a list with `list(reader)` to get all rows as a nested list.

**Q: Why do we use `newline=""` when opening a CSV file for writing?**
A: Without `newline=""`, the `csv.writer` adds extra blank lines between rows on Windows systems. The `newline=""` parameter prevents those empty lines, keeping the CSV data clean and properly formatted.

**Q: What does `f.namelist()` return in zipfile operations?**
A: `f.namelist()` returns a Python list containing the names of all files stored inside the ZIP archive. For example: `['abc.txt', 'abcd.txt', 'sample.txt']`. You can then iterate over this list to access each file.

---

## Try It Yourself

**Exercise 1:** Create 3 text files with any content. Write a program to zip all 3 into a single `archive.zip` file. Then write another program to unzip and print each file's name and content.

<details><summary>Answer</summary>

```python
# Step 1: Create files
for i in range(1, 4):
    with open(f"file{i}.txt", "w") as f:
        f.write(f"This is file {i}\n")

# Step 2: ZIP them
from zipfile import *

with ZipFile("archive.zip", "w", ZIP_DEFLATED) as zf:
    for i in range(1, 4):
        zf.write(f"file{i}.txt")

print("ZIP created")

# Step 3: UNZIP and print
with ZipFile("archive.zip", "r", ZIP_STORED) as zf:
    for name in zf.namelist():
        print("File:", name)
        with open(name, "r") as f:
            print(f.read())
```
</details>

---

**Exercise 2:** Write a program to create a CSV file of student records (student ID, name, marks). Accept 3 student records from the user, write to `students.csv`, then read it back and print in tabular format.

<details><summary>Answer</summary>

```python
import csv

# Write
with open("students.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Student_ID", "Name", "Marks"])
    for i in range(3):
        sid = input("Student ID: ")
        name = input("Name: ")
        marks = input("Marks: ")
        w.writerow([sid, name, marks])

print("Data written to students.csv")

# Read
with open("students.csv", "r") as f:
    data = list(csv.reader(f))

for row in data:
    for val in row:
        print(val, end="\t")
    print()
```
</details>

---

**Exercise 3:** Use `zipfile.namelist()` to print just the list of filenames inside a ZIP archive without extracting the content.

<details><summary>Answer</summary>

```python
from zipfile import *

with ZipFile("archive.zip", "r") as zf:
    files = zf.namelist()
    print("Files in archive:")
    for name in files:
        print("-", name)
```
</details>

---

**Exercise 4:** Read a CSV file and find the student with the highest marks (skip the header row).

<details><summary>Answer</summary>

```python
import csv

with open("students.csv", "r") as f:
    data = list(csv.reader(f))

data = data[1:]    # skip header row

max_marks = -1
top_student = ""

for row in data:
    marks = int(row[2])
    if marks > max_marks:
        max_marks = marks
        top_student = row[1]

print(f"Top student: {top_student} with {max_marks} marks")
```
</details>

---

**Exercise 5:** Write a program that lists all `.txt` files in the current directory (use `os.listdir()`) and creates a ZIP archive containing all of them.

<details><summary>Answer</summary>

```python
import os
from zipfile import *

txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print("Files to zip:", txt_files)

with ZipFile("all_texts.zip", "w", ZIP_DEFLATED) as zf:
    for fname in txt_files:
        zf.write(fname)

print("ZIP created with", len(txt_files), "files")
```
</details>
