# ============================================================
# PRACTICE — Day 38: Database — MS SQL Server (CRUD)
# ============================================================
# Instructions:
#   - These questions test understanding of pyodbc and MS SQL
#   - Code blocks are templates — fill in the blanks
#   - Some questions are conceptual (no database required)
# ============================================================


# --------------------------------------------------
# SECTION 1: Concepts
# --------------------------------------------------

# Q1. What does CRUD stand for? Fill in:

# C = ________ (SQL: ________)
# R = ________ (SQL: ________)
# U = ________ (SQL: ________)
# D = ________ (SQL: ________)

# YOUR ANSWERS:


# Q2. True or False:

# a) pyodbc is a built-in Python module (no installation needed).      → ?
# b) The connection string Driver should be {SQL Server} for MS SQL.   → ?
# c) Server=. means the local machine's SQL Server.                    → ?
# d) cursor.execute() saves changes to the database immediately.       → ?
# e) connection.commit() is required after SELECT statements.          → ?
# f) A cursor holds query results after cursor.execute(SELECT ...).    → ?

# YOUR ANSWERS:


# Q3. Identify the error in each connection string:

# a) pyodbc.connect("Driver={SQL Server};Server=localhost;Database=MyDB;")
#    Error: ________ (localhost should be ?)

# b) pyodbc.connect("Driver=SQL Server;Server=.;Database=MyDB;")
#    Error: ________ (Driver format issue?)

# c) pyodbc.connect("Driver={SQL Server};Server=.;Database=MyDB")
#    Error: ________ (missing what at the end?)

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 2: Fill in the Blanks — Code Completion
# --------------------------------------------------

# Q4. Complete the connection code:

# import pyodbc
#
# cn = pyodbc.connect(
#     "Driver={________};"      # database driver
#     "Server=________;"        # local server symbol
#     "Database=________;"      # your database name
#     "Trusted_Connection=________;"   # Windows auth value
# )

# YOUR ANSWERS:


# Q5. Complete the READ function:

# def read(con):
#     cursor = con.________()           # create cursor
#     cursor.________("SELECT * FROM emp")   # execute SQL
#     for row in ________:              # iterate cursor
#         print(________)               # print each row

# YOUR ANSWERS:


# Q6. Complete the INSERT function:

# def create(con):
#     cursor = con.cursor()
#     cursor.execute(
#         "INSERT INTO emp VALUES(________, ________, ________, ________)",
#         (3, "Durga", "HYD", 45000)    # 4 values for 4 ? placeholders
#     )
#     con.________()          # mandatory — saves the transaction
#     print("Record inserted")

# YOUR ANSWERS: (fill in the placeholders and method name)


# Q7. Complete the UPDATE function:

# def update(con):
#     cursor = con.cursor()
#     cursor.execute(
#         "UPDATE emp SET name=________, address=________, salary=________ WHERE id=________",
#         ("Ravi", "Amir Peth", 23000, 1)
#     )
#     con.________()    # save the update

# YOUR ANSWERS:


# Q8. Complete the DELETE function:

# def delete(con):
#     cursor = con.cursor()
#     cursor.execute(
#         "DELETE FROM emp WHERE id=________",
#         (2,)    # why is the comma needed here?
#     )
#     con.________()    # save the deletion

# Answer: why is there a trailing comma in (2,)?


# --------------------------------------------------
# SECTION 3: Conceptual Questions
# --------------------------------------------------

# Q9. What is a cursor in database programming?
# Choose the best answer:
# a) A blinking line on the screen
# b) A memory location where query results are stored after execute()
# c) A type of database table
# d) The SQL connection object

# YOUR ANSWER:


# Q10. Order the steps for a complete CRUD operation:

# Unordered steps:
# [ ] cursor.execute(SQL, values)
# [ ] import pyodbc
# [ ] cn = pyodbc.connect(...)
# [ ] cursor = cn.cursor()
# [ ] cn.commit()
# [ ] for row in cursor: print(row)  (only for SELECT)

# Correct order (write the numbers 1-6):

# YOUR ANSWER:


# Q11. When is commit() required?
# Mark each SQL operation: commit required (YES) or not (NO):

# SELECT * FROM emp      → ?
# INSERT INTO emp ...    → ?
# UPDATE emp SET ...     → ?
# DELETE FROM emp ...    → ?

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 4: Complete Program
# --------------------------------------------------

# Q12. Write a complete READ function (without database):
# Simulate what it would do by using a list of tuples as mock data:

mock_data = [
    (1, "Sita", "HYD", 90000),
    (2, "Mohan", "HYD", 80000),
    (3, "Durga", "HYD", 45000)
]

def mock_read(data):
    print("\n--- Reading data ---")
    for row in data:
        print(row)

mock_read(mock_data)    # prediction (3 rows):


# Q13. Simulate what cursor.execute() + for row in cursor does:

def simulate_select(table_data, condition=None):
    results = []
    for row in table_data:
        if condition is None or condition(row):
            results.append(row)
    return results

# Simulate: SELECT * FROM emp
all_rows = simulate_select(mock_data)
print(all_rows)    # prediction:

# Simulate: SELECT * FROM emp WHERE salary > 60000
high_earners = simulate_select(mock_data, lambda row: row[3] > 60000)
print(high_earners)    # prediction:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Write the complete pyodbc template for all CRUD operations:
# (Fill in all blanks — this is a template, not meant to run)

# import pyodbc
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)
#
# cn = pyodbc.connect(
#     "Driver={_____};Server=____;Database=_____;Trusted_Connection=_____;"
# )
#
# def read(con):
#     cursor = con._____()
#     cursor._____("SELECT * FROM emp")
#     for row in _____:
#         print(row)
#
# def create(con, id, name, addr, sal):
#     cursor = con.cursor()
#     cursor._____("INSERT INTO emp VALUES(?,?,?,?)", (id, name, addr, sal))
#     con._____()
#
# def update(con, id, name, addr, sal):
#     cursor = con.cursor()
#     cursor._____("UPDATE emp SET name=?, address=?, salary=? WHERE id=?",
#                  (name, addr, sal, id))
#     con._____()
#
# def delete(con, id):
#     cursor = con.cursor()
#     cursor._____("DELETE FROM emp WHERE id=?", (id,))
#     con._____()
#
# read(cn)
# create(cn, 4, "Ali", "Mumbai", 35000)
# update(cn, 1, "Ravi", "Delhi", 55000)
# delete(cn, 2)

# YOUR COMPLETED TEMPLATE:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Which Python library is used to connect to SQL Server (MSSQL)?
#    A) sqlite3    B) pymysql    C) pyodbc    D) psycopg2
# Answer: ___

# Q_MCQ_2. What does cursor.execute(sql) do?
#    A) Fetches rows    B) Sends a SQL statement to the database
#    C) Opens the connection    D) Closes the cursor
# Answer: ___

# Q_MCQ_3. cursor.fetchall()  returns:
#    A) One row as a tuple    B) All rows as a list of tuples
#    C) Column names only    D) The row count
# Answer: ___

# Q_MCQ_4. conn.commit()  is required after:
#    A) SELECT queries    B) INSERT / UPDATE / DELETE queries
#    C) Every execute()    D) Opening the connection
# Answer: ___

# Q_MCQ_5. Which function creates a database connection?
#    A) cursor.connect()    B) pyodbc.connect()
#    C) db.open()           D) sql.connect()
# Answer: ___

# Q_MCQ_6. cursor.fetchone()  returns:
#    A) All rows    B) The first row only    C) Column headers    D) None always
# Answer: ___

# Q_MCQ_7. To use parameterized queries (avoid SQL injection), use:
#    A) f-strings inside SQL    B) ? placeholders with a tuple of values
#    C) String format()         D) Hardcoded values
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. import _______ to connect to SQL Server from Python.

# FIB_2. conn = pyodbc.connect(_______) — the argument is a _______ string.

# FIB_3. After executing INSERT/UPDATE/DELETE you must call conn._______()
#         to save changes.

# FIB_4. cursor.execute("SELECT * FROM students WHERE id=?", (_______,))
#         uses parameterized query to avoid SQL injection.

# FIB_5. To get the column names from a cursor: [col[0] for col in
#         cursor._______].

# FIB_6. cursor.rowcount  gives the number of rows _______ by the last query.

# FIB_7. Always close the connection with conn._______() when done.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Student Management System using a database.
# (Use sqlite3 if MSSQL/pyodbc is not available — same CRUD concepts)
#
# Requirements:
#   1. Connect to a SQLite database "students.db"
#   2. Create table: Students(id INT PK, name TEXT, age INT, grade TEXT)
#   3. INSERT 5 student records using parameterized queries
#   4. SELECT and display all students
#   5. UPDATE a student's grade by id
#   6. DELETE a student by id
#   7. SELECT again to verify the changes
#   8. Close the connection properly
#
# Expected output:
#   Table created.
#   Inserted 5 students.
#   === All Students ===
#   1  Alice   20  A
#   2  Bob     21  B
#   ...
#   Updated Bob's grade to A.
#   Deleted student id=5.
#   === After Changes ===
#   1  Alice   20  A
#   2  Bob     21  A
#   ...
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: C=Create/INSERT, R=Read/SELECT, U=Update/UPDATE, D=Delete/DELETE

# Q2: a)False, b)True, c)True, d)False (only stages in memory), e)False, f)True

# Q3: a) localhost should be . (dot) for local SQL Server
#     b) Driver must be in curly braces: {SQL Server}
#     c) Missing semicolon at the very end (Trusted_Connection not shown, but string needs consistent format)

# Q4: SQL Server, ., your_database_name, yes

# Q5: cursor(), execute, cursor, row

# Q6: ?, ?, ?, ?  (four question marks for four values), commit

# Q7: ?, ?, ?, ? (four placeholders), commit

# Q8: ? (one placeholder for one value), commit
#     Trailing comma in (2,) makes it a tuple — without comma, (2) is just the integer 2

# Q9: b) A memory location where query results are stored after execute()

# Q10: 1=import pyodbc, 2=connect, 3=cursor(), 4=execute(), 5=commit (or for row in cursor), 6=close

# Q11: SELECT→NO, INSERT→YES, UPDATE→YES, DELETE→YES

# Q12: 3 rows printed: (1,'Sita','HYD',90000), (2,'Mohan','HYD',80000), (3,'Durga','HYD',45000)

# Q13: All 3 rows; only rows with salary > 60000: [(1,'Sita','HYD',90000), (2,'Mohan','HYD',80000)]

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: C   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: pyodbc
# FIB_2: connection string (DSN / driver info)
# FIB_3: commit
# FIB_4: the id value (e.g. 1)
# FIB_5: description
# FIB_6: affected
# FIB_7: close

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import sqlite3
# conn = sqlite3.connect("students.db")
# cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS Students")
# cur.execute("CREATE TABLE Students(id INT PRIMARY KEY, name TEXT, age INT, grade TEXT)")
# conn.commit(); print("Table created.")
#
# students = [(1,"Alice",20,"A"),(2,"Bob",21,"B"),(3,"Carol",22,"A"),
#             (4,"David",20,"C"),(5,"Eve",21,"B")]
# cur.executemany("INSERT INTO Students VALUES (?,?,?,?)", students)
# conn.commit(); print("Inserted 5 students.")
#
# print("=== All Students ===")
# for row in cur.execute("SELECT * FROM Students"):
#     print(*row)
#
# cur.execute("UPDATE Students SET grade=? WHERE id=?", ("A", 2))
# conn.commit(); print("Updated Bob's grade to A.")
#
# cur.execute("DELETE FROM Students WHERE id=?", (5,))
# conn.commit(); print("Deleted student id=5.")
#
# print("=== After Changes ===")
# for row in cur.execute("SELECT * FROM Students"):
#     print(*row)
# conn.close()

