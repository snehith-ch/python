# Day 39 — Database Connectivity: MySQL (CRUD Operations)

← [Day 38](day_38_database_mssql.md) | [Index](00_INDEX.md) | [Day 40](day_40_multithreading.md) →

---

## Quick Revision — Day 39

| # | Key Point |
|---|-----------|
| 1 | MySQL module: `mysql.connector` — install via PyCharm Settings → Python Interpreter |
| 2 | Connection: `mysql.connector.connect(host="localhost", user="root", password="...", database="...")` |
| 3 | `con.is_connected()` — returns True if connection succeeded |
| 4 | MySQL placeholders: `%s` (not `?` like MS SQL) |
| 5 | `cursor.executemany(sql, records)` — insert multiple records at once |
| 6 | `cursor.fetchall()` — retrieves ALL rows from SELECT result as a list of tuples |
| 7 | `con.commit()` — mandatory after INSERT/UPDATE/DELETE to save changes |
| 8 | `con.rollback()` — undo uncommitted changes on error |
| 9 | try-except-finally pattern: operations in try, `rollback()` in except, `cursor.close()`/`con.close()` in finally |
| 10 | MySQL editor: **MySQL Workbench**; server: `localhost`; port: 3306 |

---

## Navigation

- **Pre-requisite:** [Day 38](day_38_database_mssql.md) — MS SQL CRUD operations
- **Next:** [Day 40](day_40_multithreading.md) — Multithreading
- **Related:** [Day 32](day_32_exception_advanced_custom.md) — try-except-finally for error handling

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| Module | `mysql.connector` | MySQL connectivity library |
| Program | `mysql_program.py` | All CRUD operations in MySQL |
| Method | `con.is_connected()` | Check if connection is active |
| Method | `cursor.executemany(sql, data)` | Insert multiple records at once |
| Method | `cursor.fetchall()` | Retrieve all rows as list of tuples |
| Method | `con.rollback()` | Undo uncommitted changes |
| Object | `con` (connection) | MySQL connection object |
| Object | `cursor` | Holds query results |
| SQL | `SELECT * FROM emp` | Read all records |
| SQL | `INSERT INTO emp VALUES (%s, %s, %s)` | Insert one record |
| SQL | `UPDATE emp SET name=%s WHERE id=%s` | Modify a record |
| SQL | `DELETE FROM emp WHERE id=%s` | Remove a record |
| Pattern | try-except-finally | Safe database operations with cleanup |

---

## 1. MySQL vs MS SQL — Overview

```
MySQL                          MS SQL Server
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Free (Community Edition)       Paid (Developer/Express free)
mysql.connector module         pyodbc module
localhost                      . (dot)
%s placeholders                ? placeholders
MySQL Workbench (editor)       SQL Server Management Studio
fetchall() to read results     iterate cursor directly
Commonly used in web apps      Windows/.NET environments
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> **Key insight:** The SQL statements (INSERT, SELECT, UPDATE, DELETE) are identical in both databases. Only the connection string, module name, and placeholder symbol (`?` vs `%s`) change.

---

## 2. Setup — MySQL and mysql.connector

### 2.1 Tools Required

| Tool | Purpose |
|------|---------|
| MySQL Community Server | Database engine |
| MySQL Workbench | GUI editor |
| `mysql.connector` | Python module for MySQL |

### 2.2 Installing mysql.connector

```
PyCharm:
  File → Settings → Project: [your project] → Python Interpreter
  Click + → Search "mysql-connector-python" → Install Package
```

### 2.3 Creating Database and Table in MySQL Workbench

```sql
-- Create database
CREATE DATABASE python7am;

-- Use the database
USE python7am;

-- Create table
CREATE TABLE emp (
    id INT,
    name VARCHAR(50),
    address VARCHAR(50)
);
```

---

## 3. Connection

```python
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="python7am"
)

if con.is_connected():
    print("Connected to MySQL successfully")
```

| Parameter | Description |
|-----------|-------------|
| `host` | Server address — `"localhost"` for local MySQL |
| `user` | MySQL username — typically `"root"` |
| `password` | Your MySQL root password |
| `database` | Which database to connect to |

> **Important:** The `database=` parameter is required when you want to work with a specific database. Without it, connection succeeds but you can't execute table operations.

---

## 4. CRUD Operations

### 4.1 CREATE — INSERT Single Record

```python
def create(con):
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO emp VALUES (%s, %s, %s)",
        (101, "Sita", "HYD")    # %s placeholders for values
    )
    con.commit()    # MANDATORY — saves the transaction
    print("Record inserted")


create(con)
```

> **`%s` placeholders** are used in MySQL (unlike `?` in MS SQL). The number of `%s` must match the number of values in the tuple.

### 4.2 CREATE — INSERT Multiple Records with executemany()

```python
def create_many(con):
    cursor = con.cursor()
    records = [
        (101, "Sita", "HYD"),
        (102, "Mohan", "Delhi"),
        (103, "Durga", "Pune")
    ]
    cursor.executemany(
        "INSERT INTO emp VALUES (%s, %s, %s)",
        records
    )
    con.commit()
    print(f"{cursor.rowcount} records inserted")


create_many(con)
```

> `cursor.executemany(sql, list_of_tuples)` — runs the SQL statement once for each tuple in the list. More efficient than calling `execute()` in a loop.

### 4.3 READ — SELECT Records with fetchall()

```python
def read(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM emp")
    emp_details = cursor.fetchall()    # returns list of tuples
    print("\n--- Reading data from database ---")
    for row in emp_details:
        print(row[0], row[1], row[2])


read(con)
```

**Output:**
```
--- Reading data from database ---
101 Sita HYD
102 Mohan Delhi
103 Durga Pune
```

> `cursor.fetchall()` returns all rows as a **list of tuples**. Access individual columns by index: `row[0]`, `row[1]`, etc.

### 4.4 UPDATE — Modify Record

```python
def update(con):
    cursor = con.cursor()
    cursor.execute(
        "UPDATE emp SET name=%s, address=%s WHERE id=%s",
        ("Ravi", "Amir Peth", 101)    # update record with id=101
    )
    con.commit()
    print("Record updated")
    read(con)    # verify


update(con)
```

### 4.5 DELETE — Remove Record

```python
def delete(con):
    cursor = con.cursor()
    cursor.execute(
        "DELETE FROM emp WHERE id=%s",
        (102,)    # delete record with id=102
    )
    con.commit()
    print("Record deleted")
    read(con)    # verify


delete(con)
```

---

## 5. Safe Pattern — try-except-finally

```python
import mysql.connector

con = None
cursor = None

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="python7am"
    )

    if con.is_connected():
        print("Connected successfully")

    cursor = con.cursor()
    cursor.execute("INSERT INTO emp VALUES (%s, %s, %s)", (104, "Ali", "Mumbai"))
    con.commit()
    print("Record inserted")

except mysql.connector.Error as e:
    print(f"Database error: {e}")
    if con:
        con.rollback()    # undo any uncommitted changes

finally:
    if cursor:
        cursor.close()    # always close cursor
    if con and con.is_connected():
        con.close()       # always close connection
        print("Connection closed")
```

> `con.rollback()` — if an error occurs after some changes, rollback reverts them so the database stays consistent.

---

## 6. Complete CRUD Program

```python
import mysql.connector

# Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="python7am"
)


def read(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM emp")
    emp_details = cursor.fetchall()
    print("\n--- Records ---")
    for row in emp_details:
        print(row[0], row[1], row[2])


def create(con):
    cursor = con.cursor()
    records = [
        (101, "Sita", "HYD"),
        (102, "Mohan", "Delhi"),
        (103, "Durga", "Pune")
    ]
    cursor.executemany("INSERT INTO emp VALUES (%s, %s, %s)", records)
    con.commit()
    print("Records inserted")
    read(con)


def update(con):
    cursor = con.cursor()
    cursor.execute(
        "UPDATE emp SET name=%s, address=%s WHERE id=%s",
        ("Ravi", "Amir Peth", 101)
    )
    con.commit()
    print("Record updated")
    read(con)


def delete(con):
    cursor = con.cursor()
    cursor.execute("DELETE FROM emp WHERE id=%s", (102,))
    con.commit()
    print("Record deleted")
    read(con)


# Execute all CRUD operations
read(con)      # initial read — empty table
create(con)    # insert 3 records
update(con)    # update record 101
delete(con)    # delete record 102
con.close()
```

**Execution flow:**
```
Initial read:  (empty table)
After insert:  records 101, 102, 103
After update:  record 101 name → Ravi, address → Amir Peth
After delete:  record 102 removed → records 101 and 103 remain
```

---

## 7. fetchall() vs Iterating Cursor Directly

```
MS SQL (pyodbc)              MySQL (mysql.connector)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
for row in cursor:           emp_details = cursor.fetchall()
    print(row)               for row in emp_details:
                                 print(row[0], row[1])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Iterate cursor directly      fetchall() returns list of tuples
row is a Row object          row is a plain tuple → use index
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 8. MS SQL vs MySQL — Full Comparison

| Feature | MS SQL (pyodbc) | MySQL (mysql.connector) |
|---------|----------------|------------------------|
| Module | `pyodbc` | `mysql.connector` |
| Connection function | `pyodbc.connect(string)` | `mysql.connector.connect(params)` |
| Server | `.` (dot) | `localhost` |
| Check connection | — | `con.is_connected()` |
| Placeholders | `?` | `%s` |
| Read results | `for row in cursor` | `cursor.fetchall()` |
| Multiple insert | multiple `execute()` calls | `cursor.executemany()` |
| Rollback | — | `con.rollback()` |
| Editor | SSMS | MySQL Workbench |
| OS | Windows | Cross-platform |

---

## Student Q&A

> **Student Question:** What is the difference between `execute()` and `executemany()`?
> **Answer:** `cursor.execute(sql, values)` runs a SQL statement once with one set of values. `cursor.executemany(sql, list_of_tuples)` runs the SQL statement once for each tuple in the list — useful for batch insertions. Both require `con.commit()` afterward to save.

> **Student Question:** What does `cursor.fetchall()` return?
> **Answer:** `fetchall()` returns a list of tuples, where each tuple represents one row. For example, for a table with columns id, name, address: `[(101, 'Sita', 'HYD'), (102, 'Mohan', 'Delhi')]`. Access values by index: `row[0]` for id, `row[1]` for name, `row[2]` for address.

> **Student Question:** Why do we use `%s` instead of `?` in MySQL?
> **Answer:** Each database driver has its own placeholder syntax. `pyodbc` (for MS SQL) uses `?`. `mysql.connector` (for MySQL) uses `%s`. The purpose is the same — pass values separately from the SQL string to avoid SQL injection. The number of `%s` must match the values provided.

> **Student Question:** What is `con.rollback()` and when do we need it?
> **Answer:** `rollback()` undoes all uncommitted changes to the database. If an error occurs in the middle of multiple database operations — say, two out of three inserts succeeded — `rollback()` reverts all of them so the database stays in a consistent state. Always call `rollback()` in the `except` block of a try-except-finally pattern.

> **Student Question:** Why does connection fail even when `database=` is not given?
> **Answer:** `mysql.connector.connect()` without `database=` connects to the MySQL server, not to a specific database. When you then try to execute `INSERT INTO emp ...`, MySQL doesn't know which database's `emp` table to use, so it throws an error. Always include `database=` in the connection to specify which database to use.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: No module named 'mysql'` | mysql-connector-python not installed | PyCharm: Settings → Interpreter → install `mysql-connector-python` |
| `mysql.connector.errors.DatabaseError: 1049 Unknown database` | Database name doesn't exist | Create the database in MySQL Workbench first |
| `mysql.connector.errors.ProgrammingError: Table doesn't exist` | Table not created | Create the table in MySQL Workbench or via `cursor.execute("CREATE TABLE ...")` |
| Records not saved | `commit()` not called | Add `con.commit()` after INSERT/UPDATE/DELETE |
| `Access denied for user 'root'` | Wrong password | Check MySQL root password |
| `Can't connect to MySQL server` | MySQL server not running | Start MySQL service from System Services |

---

## Interview Questions

**Q: What module is used for MySQL connectivity in Python?**
A: `mysql.connector` (from the `mysql-connector-python` package). Import with `import mysql.connector`. It provides `mysql.connector.connect()` to create a connection and returns a connection object with methods like `cursor()`, `commit()`, `rollback()`, and `is_connected()`.

**Q: What is the difference between `execute()` and `executemany()` in mysql.connector?**
A: `cursor.execute(sql, values)` runs a SQL statement once with a single set of values. `cursor.executemany(sql, list_of_tuples)` runs the same SQL statement for each tuple in the list — useful for batch inserts. Both require `con.commit()` to save changes.

**Q: What does `cursor.fetchall()` do?**
A: `fetchall()` retrieves all rows returned by a SELECT query as a list of tuples. Each tuple represents one row; columns are accessed by index (`row[0]`, `row[1]`, etc.). Unlike MS SQL's pyodbc (which lets you iterate cursor directly), `mysql.connector` typically uses `fetchall()` to get results.

**Q: Why do we use `%s` placeholders in MySQL instead of `?`?**
A: Each database driver defines its own parameter placeholder. `mysql.connector` uses `%s`; `pyodbc` uses `?`. Both serve the same purpose: passing values separately from the SQL string to prevent SQL injection and keep code clean. The number of `%s` must match the number of values.

**Q: What is `con.rollback()` and when is it used?**
A: `rollback()` undoes all uncommitted changes to the database. It is used in the `except` block of a try-except-finally pattern when a database error occurs mid-transaction, ensuring the database remains in a consistent state. `commit()` saves changes; `rollback()` reverses them.

---

## Try It Yourself

**Exercise 1:** Connect to a MySQL database and insert 3 student records (id, name, marks) into a `students` table using `executemany()`.

<details><summary>Answer</summary>

```python
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="school"
)

cursor = con.cursor()
students = [
    (1, "Alice", 90),
    (2, "Bob", 85),
    (3, "Charlie", 92)
]
cursor.executemany("INSERT INTO students VALUES (%s, %s, %s)", students)
con.commit()
print(f"{cursor.rowcount} records inserted")
con.close()
```
</details>

---

**Exercise 2:** Write a `read()` function that uses `fetchall()` to retrieve and print all records from the `students` table.

<details><summary>Answer</summary>

```python
import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root",
    password="your_password", database="school"
)

def read(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1], row[2])

read(con)
con.close()
```
</details>

---

**Exercise 3:** Write a complete CRUD program for a `products` table (id, name, price) using try-except-finally with `rollback()` on error.

<details><summary>Answer</summary>

```python
import mysql.connector

con = None
cursor = None

try:
    con = mysql.connector.connect(
        host="localhost", user="root",
        password="your_password", database="store"
    )
    cursor = con.cursor()

    # INSERT
    records = [(1, "Laptop", 50000), (2, "Mouse", 500), (3, "Keyboard", 1200)]
    cursor.executemany("INSERT INTO products VALUES (%s, %s, %s)", records)
    con.commit()

    # READ
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row[0], row[1], row[2])

    # UPDATE
    cursor.execute("UPDATE products SET price=%s WHERE id=%s", (55000, 1))
    con.commit()

    # DELETE
    cursor.execute("DELETE FROM products WHERE id=%s", (3,))
    con.commit()

except mysql.connector.Error as e:
    print(f"Error: {e}")
    if con:
        con.rollback()

finally:
    if cursor:
        cursor.close()
    if con and con.is_connected():
        con.close()
```
</details>
