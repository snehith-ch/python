# ============================================================
# PRACTICE — Day 39: Database — MySQL (CRUD)
# ============================================================
# Instructions:
#   - Conceptual questions and code-completion exercises
#   - Runnable simulation sections use mock data (no MySQL needed)
# ============================================================


# --------------------------------------------------
# SECTION 1: MySQL vs MS SQL Concepts
# --------------------------------------------------

# Q1. Fill in the differences:

# Feature          | MS SQL (pyodbc)         | MySQL (mysql.connector)
# Module           | ?                       | ?
# Connection func  | pyodbc.connect(string)  | mysql.connector.connect(?)
# Server address   | . (dot)                 | ?
# Check connection | —                       | ?
# Placeholders     | ?                       | ?
# Read results     | for row in cursor       | ?
# Bulk insert      | multiple execute()      | ?

# YOUR ANSWERS:


# Q2. True or False:

# a) mysql.connector is a built-in Python module.                    → ?
# b) MySQL uses %s placeholders (not ? like MS SQL).                → ?
# c) fetchall() returns a list of tuples.                           → ?
# d) executemany() requires connection.commit() afterward.          → ?
# e) rollback() saves changes permanently.                          → ?
# f) try-except-finally is the recommended pattern for MySQL CRUD.  → ?

# YOUR ANSWERS:


# Q3. What does each method do? Match:

# a) cursor.execute(sql, values)    → ?
# b) cursor.executemany(sql, list)  → ?
# c) cursor.fetchall()              → ?
# d) con.commit()                   → ?
# e) con.rollback()                 → ?
# f) cursor.close()                 → ?
# g) con.is_connected()             → ?

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 2: Code Completion
# --------------------------------------------------

# Q4. Complete the connection code:

# import mysql.connector
#
# con = mysql.connector.connect(
#     host="________",       # server address for local MySQL
#     user="________",       # default MySQL username
#     password="________",   # your MySQL password
#     database="________"    # your database name
# )
#
# if con.________():
#     print("Connected successfully")

# YOUR ANSWERS:


# Q5. Complete the INSERT single record:

# def create(con):
#     cursor = con.cursor()
#     cursor.execute(
#         "INSERT INTO emp VALUES (________, ________, ________)",
#         (101, "Sita", "HYD")
#     )
#     con.________()    # mandatory
#     print("Record inserted")

# YOUR ANSWERS:


# Q6. Complete executemany():

# def create_many(con):
#     cursor = con.cursor()
#     records = [
#         (101, "Sita", "HYD"),
#         (102, "Mohan", "Delhi"),
#         (103, "Durga", "Pune")
#     ]
#     cursor.________("INSERT INTO emp VALUES (________, ________, ________)", ________)
#     con.commit()

# YOUR ANSWERS:


# Q7. Complete the READ function:

# def read(con):
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM emp")
#     emp_details = cursor.________()    # get all rows as list of tuples
#     for row in emp_details:
#         print(row[________], row[________], row[________])   # id, name, address

# YOUR ANSWERS:


# Q8. Complete the try-except-finally template:

# import mysql.connector
# con = None
# cursor = None
#
# try:
#     con = mysql.connector.connect(host="localhost", user="root",
#                                   password="pwd", database="mydb")
#     cursor = con.cursor()
#     cursor.execute("INSERT INTO emp VALUES (%s, %s, %s)", (104, "Ali", "Mumbai"))
#     con.________()      # save
#
# except mysql.connector.Error as e:
#     print(f"Error: {e}")
#     if con:
#         con.________()  # undo changes
#
# finally:
#     if cursor:
#         cursor.________()    # always close cursor
#     if con and con.________():
#         con.________()       # always close connection

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 3: Simulation (Runnable)
# --------------------------------------------------

# Q9. Simulate fetchall() behavior using a plain list:

mock_emp = [
    (101, "Sita", "HYD"),
    (102, "Mohan", "Delhi"),
    (103, "Ali", "Pune")
]

# Simulate: cursor.execute("SELECT * FROM emp") + cursor.fetchall()
def mock_read(data):
    for row in data:
        print(row[0], row[1], row[2])

mock_read(mock_emp)    # prediction (3 lines):


# Q10. Simulate executemany():

new_records = [
    (104, "Ravi", "Mumbai"),
    (105, "Priya", "Chennai")
]

# Simulate: cursor.executemany() → add all records to table
for record in new_records:
    mock_emp.append(record)

mock_read(mock_emp)    # prediction (5 lines now):


# Q11. Simulate rollback() — if error, don't save:

def simulate_insert(data, record, should_fail=False):
    temp = data.copy()
    temp.append(record)
    if should_fail:
        print("Error occurred — rollback!")
        return data     # return original unchanged data
    print("Committed successfully")
    return temp

result = simulate_insert(mock_emp, (106, "Dev", "Delhi"), should_fail=False)
print(f"Rows: {len(result)}")    # prediction:

result2 = simulate_insert(mock_emp, (107, "Bad", "?"), should_fail=True)
print(f"Rows: {len(result2)}")   # prediction (rollback → no change):


# --------------------------------------------------
# SECTION 4: Interview Prep
# --------------------------------------------------

# Q12. Answer these common interview questions briefly:

# a) What is the difference between execute() and executemany()?
# YOUR ANSWER:

# b) What does cursor.fetchall() return?
# YOUR ANSWER:

# c) Why use %s instead of embedding values in SQL strings directly?
# YOUR ANSWER:

# d) When would you call rollback() instead of commit()?
# YOUR ANSWER:

# e) What does con.is_connected() return?
# YOUR ANSWER:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: What is wrong with this code? Fix it:

# import mysql.connector
# con = mysql.connector.connect(host="localhost", user="root", password="pwd")
# cursor = con.cursor()
# cursor.execute("INSERT INTO emp VALUES (%s, %s, %s)", 101, "Ali", "HYD")
# con.commit()

# Errors (there are 2):
# Error 1: ?
# Error 2: ?

# YOUR ANSWERS:


# BONUS 2: Write the difference — predict what each returns:

mock_single = [(101, "Sita", "HYD")]
mock_all = [(101, "Sita", "HYD"), (102, "Ravi", "Delhi")]

# cursor.fetchone() → returns first row only:
print(mock_single[0])     # simulates fetchone()

# cursor.fetchall() → returns list of all rows:
print(mock_all)           # simulates fetchall()

# prediction for each:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Which library connects Python to MySQL?
#    A) pyodbc    B) sqlite3    C) mysql.connector    D) psycopg2
# Answer: ___

# Q_MCQ_2. To install mysql-connector-python:
#    A) import mysql    B) pip install mysql-connector-python
#    C) pip install mysql    D) conda install mysql
# Answer: ___

# Q_MCQ_3. mysql.connector.connect() requires which parameters?
#    A) host, user, password, database    B) dsn, driver
#    C) server, port only    D) user, schema
# Answer: ___

# Q_MCQ_4. cursor.executemany(sql, list_of_tuples) is used to:
#    A) Run the same query multiple times with different data
#    B) Fetch multiple rows
#    C) Create multiple cursors
#    D) Run multiple different SQL statements
# Answer: ___

# Q_MCQ_5. In MySQL Python connector, the placeholder for parameterized
#           queries is:
#    A) ?    B) %s    C) $    D) {}
# Answer: ___

# Q_MCQ_6. conn.autocommit = True  means:
#    A) Every execute() auto-commits to the database
#    B) Transactions are disabled
#    C) Only SELECT is auto-committed
#    D) Rollback is always triggered
# Answer: ___

# Q_MCQ_7. cursor.description  after a SELECT gives:
#    A) Row data    B) Column metadata (names, types)
#    C) Table schema    D) Row count
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. import _______.connector to work with MySQL in Python.

# FIB_2. In mysql-connector, parameterized query placeholder is _______.

# FIB_3. conn = mysql.connector.connect(host="localhost", user="root",
#         password=_______, database="mydb")

# FIB_4. After INSERT/UPDATE/DELETE call conn._______() to persist changes.

# FIB_5. cursor.fetchall() returns a _______ of _______.

# FIB_6. To create a new MySQL database from Python:
#         cursor.execute("CREATE DATABASE IF NOT EXISTS _______")

# FIB_7. cursor.close() and conn.close() should be called to _______ resources.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Product Inventory System (use sqlite3 if MySQL unavailable).
#
# Requirements:
#   1. Connect to database "inventory.db" (sqlite3)
#   2. Create table: Products(id, name, price REAL, quantity INT)
#   3. Insert 5 products using executemany with parameterized queries
#   4. Display all products sorted by price
#   5. Update the price of one product by name
#   6. Delete products where quantity = 0
#   7. Show total inventory value: SUM(price * quantity)
#   8. Display remaining products
#
# Expected output:
#   5 products inserted.
#   === Products by Price ===
#   1  Pen      10.0   100
#   3  Eraser   15.0   50
#   ...
#   Updated Pen price to 12.0
#   Deleted 1 out-of-stock product(s).
#   Total inventory value: Rs. 4850.00
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: Module: pyodbc | mysql.connector
#     Connection: connect(str) | connect(host, user, password, database)
#     Server: . | localhost
#     Check: — | con.is_connected()
#     Placeholders: ? | %s
#     Read: for row in cursor | cursor.fetchall()
#     Bulk insert: multiple execute() | cursor.executemany()

# Q2: a)False, b)True, c)True, d)True, e)False (rollback UNDOES), f)True

# Q3: a)run one SQL statement  b)run SQL for each tuple in list
#     c)get all rows as list of tuples  d)save changes permanently
#     e)undo uncommitted changes  f)close cursor  g)check if connected

# Q4: localhost, root, your_password, your_database, is_connected

# Q5: %s, %s, %s  (three placeholders); commit

# Q6: executemany, %s, %s, %s, records

# Q7: fetchall(), 0, 1, 2

# Q8: commit, rollback, close, is_connected, close

# Q9: 101 Sita HYD, 102 Mohan Delhi, 103 Ali Pune

# Q10: 101 Sita HYD, 102 Mohan Delhi, 103 Ali Pune, 104 Ravi Mumbai, 105 Priya Chennai

# Q11: "Committed successfully", Rows: 6; "Error occurred — rollback!", Rows: 5

# BONUS 1: Error 1: database= parameter missing in connect()
#          Error 2: values must be a tuple: (%s, %s, %s), (101, "Ali", "HYD")

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: C   Q_MCQ_2: B   Q_MCQ_3: A   Q_MCQ_4: A
# Q_MCQ_5: B   Q_MCQ_6: A   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: mysql
# FIB_2: %s
# FIB_3: "your_password"
# FIB_4: commit
# FIB_5: list of tuples
# FIB_6: the database name (e.g., mydb)
# FIB_7: release / free

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import sqlite3
# conn = sqlite3.connect("inventory.db")
# cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS Products")
# cur.execute("CREATE TABLE Products(id INT, name TEXT, price REAL, quantity INT)")
# products = [(1,"Pen",10.0,100),(2,"Notebook",45.0,30),(3,"Eraser",15.0,50),
#             (4,"Scale",20.0,0),(5,"Sharpener",25.0,60)]
# cur.executemany("INSERT INTO Products VALUES(?,?,?,?)", products)
# conn.commit(); print("5 products inserted.")
#
# print("=== Products by Price ===")
# for r in cur.execute("SELECT * FROM Products ORDER BY price"):
#     print(*r)
#
# cur.execute("UPDATE Products SET price=? WHERE name=?", (12.0, "Pen"))
# conn.commit(); print("Updated Pen price to 12.0")
#
# cur.execute("DELETE FROM Products WHERE quantity=0")
# conn.commit(); print(f"Deleted {cur.rowcount} out-of-stock product(s).")
#
# cur.execute("SELECT SUM(price*quantity) FROM Products")
# total = cur.fetchone()[0]
# print(f"Total inventory value: Rs. {total:.2f}")
# print("=== Remaining Products ===")
# for r in cur.execute("SELECT * FROM Products"):
#     print(*r)
# conn.close()

