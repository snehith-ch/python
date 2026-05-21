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
