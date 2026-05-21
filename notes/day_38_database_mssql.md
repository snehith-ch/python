# Day 38 — Database Connectivity: Microsoft SQL Server (CRUD Operations)

← [Day 37](day_37_packages.md) | [Index](00_INDEX.md) | [Day 39](day_39_database_mysql.md) →

---

## Quick Revision — Day 38

| # | Key Point |
|---|-----------|
| 1 | Database = permanent storage, centralized, unlimited capacity, SQL query support |
| 2 | `pyodbc` module for MS SQL connectivity; install via File → Settings → Python Interpreter |
| 3 | Connection string: `pyodbc.connect("Driver={SQL Server};Server=.;Database=YourDB;")` |
| 4 | CRUD = **C**reate (INSERT), **R**ead (SELECT), **U**pdate (UPDATE), **D**elete (DELETE) |
| 5 | `con.cursor()` creates cursor — memory location holding query results |
| 6 | `cursor.execute(sql)` executes any SQL statement |
| 7 | `connection.commit()` saves the transaction — **mandatory** after INSERT/UPDATE/DELETE |
| 8 | Iterate cursor with `for row in cursor:` to read each record |
| 9 | MS SQL editor: **SQL Server Management Studio (SSMS)**; server name: `.` or `dot` |
| 10 | Suppress deprecation warnings: `import warnings; warnings.filterwarnings("ignore", category=DeprecationWarning)` |

---

## Navigation

- **Pre-requisite:** [Day 37](day_37_packages.md) — Packages; [Day 32](day_32_exception_advanced_custom.md) — try-except for error handling
- **Next:** [Day 39](day_39_database_mysql.md) — Same CRUD operations using MySQL
- **Related:** [Day 33](day_33_file_handling_basics.md) — File handling (alternative permanent storage)

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| Module | `pyodbc` | MS SQL connectivity library |
| Program | `database_program.py` | All CRUD operations in MS SQL |
| Function | `read(con)` | SELECT all records |
| Function | `create(con)` | INSERT a new record |
| Function | `update(con)` | UPDATE an existing record |
| Function | `delete(con)` | DELETE a record by ID |
| Object | `con` (connection) | Database connection object |
| Object | `cursor` | Holds SQL query results |
| SQL | `SELECT * FROM emp` | Read all records |
| SQL | `INSERT INTO emp VALUES(?, ?, ?, ?)` | Insert one record |
| SQL | `UPDATE emp SET ... WHERE id=?` | Modify a record |
| SQL | `DELETE FROM emp WHERE id=?` | Remove a record |
| Method | `connection.commit()` | Save transaction to database |

---

## 1. Storage Areas Recap

```
Storage Areas
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Temporary:  Python objects (lists, vars) → lost when program ends

Permanent:
    A) File System  → limited, OS-level, no centralized access
    B) Database     → unlimited, centralized, SQL support, many
                       clients can connect simultaneously
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Advantages of Database over File System:**
- Supports huge amounts of data (unlimited)
- Centralized — many clients can access at once
- Supports SQL queries (INSERT, SELECT, UPDATE, DELETE)
- Better security and transaction management

---

## 2. MS SQL Server Setup

### 2.1 Tools Required

| Tool | Purpose |
|------|---------|
| SQL Server 2019 (Developer/Express) | Database engine |
| SQL Server Management Studio (SSMS) | GUI editor (like PyCharm for SQL) |

> Download from Microsoft's website if not installed. See YouTube for installation steps.

### 2.2 Connecting to SSMS

- Server type: **Database Engine**
- Server name: `.` (dot) — universal local server name
- Authentication: **Windows Authentication** (no login/password needed)
- Click **Connect**

### 2.3 Creating Database and Table in SSMS

```
In SSMS (done manually before Python program):
1. Right-click "Databases" → New Database → name: "Python7am"
2. Expand Python7am → right-click "Tables" → New → Table
3. Add columns: id (int), name (varchar), address (varchar), salary (int)
4. Save table as: emp
5. Right-click emp → Edit Top 200 Rows → insert 2 sample records
```

---

## 3. Installing `pyodbc`

```
PyCharm:
  File → Settings → Project: [your project] → Python Interpreter
  Click + → Search "pyodbc" → Install Package
```

> `pyodbc` = Python Open Database Connectivity. This module bridges Python to any ODBC-compatible database (SQL Server, MySQL, Oracle, etc.).

---

## 4. Connection String

```python
import pyodbc

cn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=.;"
    "Database=Python7am;"
    "Trusted_Connection=yes;"
)
```

| Part | Description |
|------|-------------|
| `Driver={SQL Server}` | Which database driver to use |
| `Server=.` | Dot = local server (your computer) |
| `Database=Python7am` | Name of the database to connect |
| `Trusted_Connection=yes` | Use Windows authentication |

> **Only the database name changes** when switching databases. Driver and server stay the same for MS SQL.

---

## 5. CRUD Operations

### 5.1 Cursor Concept

```
Cursor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
cursor = con.cursor()
→ Memory location where all retrieved records are stored
→ After cursor.execute(SQL), records are in the cursor object
→ Iterate with: for row in cursor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.2 READ — SELECT Records

```python
def read(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM emp")
    print("Reading data from database:")
    for row in cursor:
        print(row)
        print()    # empty line between records
    con.close()


read(cn)
```

**Output:**
```
Reading data from database:
(1, 'Sita', 'HYD', 90000)

(2, 'Mohan', 'HYD', 80000)
```

### 5.3 CREATE — INSERT Record

```python
def create(con):
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO emp VALUES(?, ?, ?, ?)",
        (3, "Durga", "HYD", 45000)    # ? placeholders for values
    )
    con.commit()    # MANDATORY — saves the transaction
    print("Record inserted")
    read(con)       # verify by reading again


create(cn)
```

> **`commit()` is mandatory** after INSERT, UPDATE, DELETE. Without it, the change is NOT saved to the database.

> **`?` placeholders** are used to pass values separately from the SQL string — safer (avoids SQL injection) and cleaner.

### 5.4 UPDATE — Modify Record

```python
def update(con):
    cursor = con.cursor()
    cursor.execute(
        "UPDATE emp SET name=?, address=?, salary=? WHERE id=?",
        ("Ravi", "Amir Peth", 23000, 1)    # update record with id=1
    )
    con.commit()    # save the update
    print("Record updated")
    read(con)       # verify


update(cn)
```

### 5.5 DELETE — Remove Record

```python
def delete(con):
    cursor = con.cursor()
    cursor.execute(
        "DELETE FROM emp WHERE id=?",
        (2,)    # delete record with id=2
    )
    con.commit()    # save the deletion
    print("Record deleted")
    read(con)       # verify


delete(cn)
```

---

## 6. Complete CRUD Program

```python
import pyodbc
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Connection
cn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=.;"
    "Database=Python7am;"
    "Trusted_Connection=yes;"
)


def read(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM emp")
    print("\n--- Reading data from database ---")
    for row in cursor:
        print(row)
    # Note: do not close con here if calling read() from other functions


def create(con):
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO emp VALUES(?, ?, ?, ?)",
        (3, "Durga", "HYD", 45000)
    )
    con.commit()
    print("Record inserted")
    read(con)


def update(con):
    cursor = con.cursor()
    cursor.execute(
        "UPDATE emp SET name=?, address=?, salary=? WHERE id=?",
        ("Ravi", "Amir Peth", 23000, 1)
    )
    con.commit()
    print("Record updated")
    read(con)


def delete(con):
    cursor = con.cursor()
    cursor.execute(
        "DELETE FROM emp WHERE id=?",
        (2,)
    )
    con.commit()
    print("Record deleted")
    read(con)


# Execute all CRUD operations
read(cn)       # initial read — 2 records
create(cn)     # insert record 3 → now 3 records
update(cn)     # update record 1 → name changed
delete(cn)     # delete record 2 → now 2 records (1 and 3)
```

**Execution flow:**
```
Initial read:  (1, Sita, HYD, 90000), (2, Mohan, HYD, 80000)
After insert:  +record 3 Durga
After update:  record 1 becomes Ravi/APS/23000
After delete:  record 2 removed → records 1 and 3 remain
```

---

## 7. Suppressing Deprecation Warnings

```python
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
```

> Deprecation warnings appear when certain functions are marked for removal in future Python versions. They are **not errors** — your program still works. Adding the filter above cleans up the console output.

---

## 8. MS SQL vs MySQL Comparison

| Feature | MS SQL | MySQL |
|---------|--------|-------|
| Software | SQL Server 2019 | MySQL Community Server |
| Editor | SQL Server Management Studio | MySQL Workbench |
| Python module | `pyodbc` | `mysql.connector` |
| Server name | `.` (dot) | `localhost` |
| Used in Django | Rarely | Commonly used |
| Best for | Windows/.NET environments | Web apps (LAMP stack) |

> Only the connection string changes when switching from MS SQL to MySQL. SQL statements (INSERT, SELECT, UPDATE, DELETE) are the same.

---

## Student Q&A

> **Student Question:** What is the difference between file system and database storage?
> **Answer:** File system stores data in files on one computer (OS level), has limited capacity, and does not support centralized access. Database storage supports huge data, centralized access (many clients, one database), SQL query support for inserting/reading/updating/deleting data. For large applications, always use databases.

> **Student Question:** Why is `commit()` mandatory after INSERT/UPDATE/DELETE?
> **Answer:** SQL operations run in transactions. `cursor.execute()` only prepares the change in memory — it does NOT save it to the actual database. `connection.commit()` saves (commits) the transaction permanently. If you skip `commit()`, the changes will be lost when the connection closes.

> **Student Question:** What are `?` placeholders in the SQL statement?
> **Answer:** `?` is a placeholder (parameter marker) used in `cursor.execute()`. Instead of embedding values directly in the SQL string (which is a security risk — SQL injection), you pass values as a separate tuple. This is safer and also makes the code cleaner. The number of `?` must match the number of values in the tuple.

> **Student Question:** What is a cursor?
> **Answer:** A cursor is an object returned by `con.cursor()`. It represents a memory location where records from the database are stored after executing a query. After `cursor.execute("SELECT * FROM emp")`, the cursor holds all the rows returned. You iterate over them with `for row in cursor`.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: No module named 'pyodbc'` | pyodbc not installed | File → Settings → Python Interpreter → install pyodbc |
| `pyodbc.OperationalError: Can't connect` | Wrong server name or authentication | Check server name (use `.`) and Windows Authentication |
| Records not saved to database | `commit()` not called | Add `connection.commit()` after INSERT/UPDATE/DELETE |
| `pyodbc.ProgrammingError: Invalid column name` | Column name typo in SQL | Check table column names in SSMS |
| Deprecation warnings flooding console | pyodbc warning for older functions | Add `warnings.filterwarnings("ignore", category=DeprecationWarning)` |

---

## Interview Questions

**Q: What is `pyodbc`?**
A: `pyodbc` is a Python module (open-source) for connecting Python programs to ODBC-compatible databases like Microsoft SQL Server. ODBC stands for Open Database Connectivity. It provides a standard API to interact with databases using SQL statements.

**Q: What are CRUD operations?**
A: CRUD stands for Create (INSERT), Read (SELECT), Update (UPDATE), and Delete (DELETE). These four operations cover all basic database interactions. In Python with `pyodbc`, each operation uses `cursor.execute(sql)` with the appropriate SQL statement, and INSERT/UPDATE/DELETE require `connection.commit()` to save changes.

**Q: What is a cursor in database programming?**
A: A cursor is an object created by `con.cursor()` that represents a database cursor — a pointer to the result set of a SQL query. After executing a SELECT query with `cursor.execute(sql)`, the cursor holds all returned records. You iterate over them with `for row in cursor`.

**Q: Why do we need `connection.commit()` after INSERT/UPDATE/DELETE?**
A: Database operations run inside transactions. `cursor.execute()` stages the change in memory but does not write it to the database. `connection.commit()` finalizes the transaction and permanently writes the change to the database. Without `commit()`, the change is lost when the connection is closed.

**Q: What is the connection string for MS SQL Server?**
A: `"Driver={SQL Server};Server=.;Database=DatabaseName;Trusted_Connection=yes;"` — Driver specifies the ODBC driver, Server=. means local server (your computer), Database is the database name, and Trusted_Connection=yes uses Windows authentication.

---

## Try It Yourself

**Exercise 1:** Set up a database named `school` with a table `students (id INT, name VARCHAR(50), grade INT)`. Write a Python program using `pyodbc` to insert 3 records into the students table.

<details><summary>Answer</summary>

```python
import pyodbc

cn = pyodbc.connect(
    "Driver={SQL Server};Server=.;Database=school;Trusted_Connection=yes;"
)

cursor = cn.cursor()
cursor.execute("INSERT INTO students VALUES(?, ?, ?)", (1, "Alice", 90))
cursor.execute("INSERT INTO students VALUES(?, ?, ?)", (2, "Bob", 85))
cursor.execute("INSERT INTO students VALUES(?, ?, ?)", (3, "Charlie", 92))
cn.commit()
print("3 records inserted")
cn.close()
```
</details>

---

**Exercise 2:** Write a `read()` function that reads all records from the `students` table and prints each record on a separate line.

<details><summary>Answer</summary>

```python
import pyodbc

cn = pyodbc.connect(
    "Driver={SQL Server};Server=.;Database=school;Trusted_Connection=yes;"
)

def read(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor:
        print(row)

read(cn)
cn.close()
```
</details>

---

**Exercise 3:** Write a function to update the grade of a student by ID. Then call `read()` to verify the change.

<details><summary>Answer</summary>

```python
def update_grade(con, student_id, new_grade):
    cursor = con.cursor()
    cursor.execute(
        "UPDATE students SET grade=? WHERE id=?",
        (new_grade, student_id)
    )
    con.commit()
    print(f"Updated student {student_id}'s grade to {new_grade}")
```
</details>
