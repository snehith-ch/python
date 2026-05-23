# ============================================================
# PRACTICE — Day 35: ZIP Files and CSV Files
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: ZIP Files — zipfile Module
# --------------------------------------------------

# Q1. Predict the ZIP constants — fill in:

from zipfile import *

print(ZIP_DEFLATED)    # prediction (numeric value):
print(ZIP_STORED)      # prediction (numeric value):
# Which one compresses? Which one doesn't?


# Q2. Create and inspect a ZIP file — predict:

# First create files to zip
with open("file_a.txt", "w") as f:
    f.write("Content of file A")
with open("file_b.txt", "w") as f:
    f.write("Content of file B")

# Create ZIP
z = ZipFile("archive.zip", "w", ZIP_DEFLATED)
z.write("file_a.txt")
z.write("file_b.txt")
z.close()

# Inspect the ZIP
z2 = ZipFile("archive.zip", "r")
names = z2.namelist()
print(names)      # prediction (list of filenames):
print(type(names))   # prediction:
z2.close()


# Q3. Extract ZIP — predict what happens:

z = ZipFile("archive.zip", "r")
z.extractall("extracted_folder")    # extracts to subfolder
z.close()

import os
print(os.listdir("extracted_folder"))   # prediction:


# Q4. ZIP_STORED vs ZIP_DEFLATED — fill in blanks:

# ZIP_STORED (0)    → stores files __________ (compressed / uncompressed?)
# ZIP_DEFLATED (8)  → stores files __________ (uses __________ algorithm)

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 2: CSV Files — csv Module
# --------------------------------------------------

# Q5. Write a CSV file — predict the file content:

import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Grade"])     # header
    writer.writerow([1, "Alice", "A"])
    writer.writerow([2, "Bob", "B"])
    writer.writerow([3, "Charlie", "A+"])

# prediction: open students.csv — what do the first 4 rows look like?


# Q6. Read a CSV file — predict the output:

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)    # prediction (each row is a list):


# Q7. Why newline="" in open for CSV? — fill in the blank:
# Without newline="", on Windows, each row would have an extra __________ line between rows.
# The newline="" parameter tells Python not to add an extra __________.

# YOUR ANSWERS:


# Q8. CSV with employee data — predict the file and output:

import csv

# Write
with open("emp.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Emp_No", "Emp_Name", "Emp_Salary"])
    writer.writerow([101, "Sita", 50000])
    writer.writerow([102, "Ravi", 45000])
    writer.writerow([103, "Ali", 55000])

# Read
with open("emp.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)    # convert to list

print(data[0])      # prediction (header row):
print(data[1])      # prediction (first data row):
print(len(data))    # prediction (total rows including header):


# --------------------------------------------------
# SECTION 3: Write Code
# --------------------------------------------------

# Q9. Write a program that:
#   a) Creates a CSV file "marks.csv" with columns: Name, Math, Science, English
#   b) Adds 3 student records
#   c) Reads the file and prints each student's total marks (Math + Science + English)
#   Note: all values read from CSV are STRINGS — convert to int first!

# YOUR CODE HERE:


# Q10. ZIP multiple text files:
#   a) Create 3 text files: "note1.txt", "note2.txt", "note3.txt"
#   b) Add all 3 to a ZIP file "notes.zip" using ZIP_DEFLATED
#   c) Open the ZIP and print the list of files inside

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — reading CSV data and doing calculations:

import csv
from io import StringIO

# Simulate a CSV in memory
csv_data = "item,price,qty\nApple,50,10\nBanana,20,25\nMango,80,5"
reader = csv.reader(StringIO(csv_data))
next(reader)    # skip header

total_value = 0
for row in reader:
    value = float(row[1]) * int(row[2])
    total_value += value
    print(f"{row[0]}: {value}")    # prediction (3 lines):

print(f"Total: {total_value}")     # prediction:


# BONUS 2: What happens if you open a CSV without newline="" on Windows?
# a) The file still writes correctly → True or False?
# b) Extra blank lines appear between rows → True or False?
# c) It raises an error → True or False?

# YOUR ANSWERS:


# BONUS 3: Write code to:
# - Read "emp.csv" (created in Q8)
# - Find the employee with the highest salary
# - Print their name and salary

# YOUR CODE HERE:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Which module handles CSV files?
#    A) json    B) csv    C) file    D) tabulate
# Answer: ___

# Q_MCQ_2. csv.reader() returns rows as:
#    A) Dicts    B) Strings    C) Lists    D) Tuples
# Answer: ___

# Q_MCQ_3. csv.DictReader() returns each row as:
#    A) A list    B) An OrderedDict / dict (keys from header row)
#    C) A tuple    D) A string
# Answer: ___

# Q_MCQ_4. To add a new file to a ZIP without deleting existing files:
#    A) zipfile.ZipFile("f.zip", "w")    B) zipfile.ZipFile("f.zip", "a")
#    C) zipfile.ZipFile("f.zip", "r")    D) zipfile.ZipFile("f.zip", "x")
# Answer: ___

# Q_MCQ_5. zipfile.ZipFile.namelist()  returns:
#    A) Number of files    B) List of file names in the archive
#    C) File sizes    D) Compression method
# Answer: ___

# Q_MCQ_6. To write a CSV with a custom delimiter (e.g., |):
#    A) csv.writer(f, delimiter="|")    B) csv.writer(f, sep="|")
#    C) csv.writer(f, char="|")         D) Not possible
# Answer: ___

# Q_MCQ_7. zipfile.ZipFile(path, "r").extractall("dest_dir") extracts to:
#    A) Current directory always    B) dest_dir
#    C) A temp folder    D) The same folder as the zip
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. import _______ to work with CSV files.

# FIB_2. csv.writer(f).writerow([...]) writes a _______ to the CSV.

# FIB_3. To read a CSV with headers as dict keys, use csv._______(f).

# FIB_4. zipfile.ZipFile("data.zip", "_______") creates a new zip or
#         overwrites existing.

# FIB_5. zf.extractall("output/")  extracts _______ files from the archive.

# FIB_6. The default delimiter in Python's csv module is _______.

# FIB_7. To list all files inside a zip without extracting: zf._______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Student Records Manager — CSV + ZIP backup system.
#
# Requirements:
#   1. Create "students.csv" with columns: Name, Age, Grade, Score
#      Add at least 5 student rows
#   2. Read the CSV using DictReader and calculate the average score
#   3. Filter students with Score >= 75 and write them to "toppers.csv"
#   4. Compress both CSV files into "records.zip" using zipfile
#   5. List the contents of records.zip
#   6. Extract records.zip into an "extracted/" folder
#
# Expected output:
#   Created students.csv with 5 students.
#   Average score: 78.4
#   Toppers (score >= 75): 3 students → saved to toppers.csv
#   records.zip contains: ['students.csv', 'toppers.csv']
#   Extracted to extracted/
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: ZIP_DEFLATED=8, ZIP_STORED=0
#     ZIP_DEFLATED compresses; ZIP_STORED just packages without compression

# Q2: ['file_a.txt', 'file_b.txt'], <class 'list'>

# Q3: ['file_a.txt', 'file_b.txt'] (extracted files)

# Q4: ZIP_STORED → uncompressed; ZIP_DEFLATED → compressed (deflate algorithm)

# Q6: ['ID', 'Name', 'Grade'], ['1', 'Alice', 'A'], ['2', 'Bob', 'B'], ['3', 'Charlie', 'A+']
#     (all values are strings, even numbers)

# Q7: blank line; newline character

# Q8: ['Emp_No', 'Emp_Name', 'Emp_Salary'], ['101', 'Sita', '50000'], 4

# BONUS 1: "Apple: 500.0", "Banana: 500.0", "Mango: 400.0", "Total: 1400.0"

# BONUS 2: a) True (file writes), b) True (extra blank lines), c) False (no error)

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: A   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: csv
# FIB_2: single row (as a list)
# FIB_3: DictReader
# FIB_4: "w"
# FIB_5: all
# FIB_6: comma (,)
# FIB_7: namelist()

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import csv, zipfile, os
#
# students = [
#     ["Name","Age","Grade","Score"],
#     ["Alice","20","A","92"],
#     ["Bob","21","B","78"],
#     ["Carol","22","C","65"],
#     ["David","20","A","88"],
#     ["Eve","21","B","69"],
# ]
# with open("students.csv","w",newline="") as f:
#     csv.writer(f).writerows(students)
# print("Created students.csv with 5 students.")
#
# with open("students.csv","r") as f:
#     rows = list(csv.DictReader(f))
#
# scores = [int(r["Score"]) for r in rows]
# print(f"Average score: {sum(scores)/len(scores):.1f}")
#
# toppers = [r for r in rows if int(r["Score"]) >= 75]
# with open("toppers.csv","w",newline="") as f:
#     w = csv.DictWriter(f, fieldnames=rows[0].keys())
#     w.writeheader(); w.writerows(toppers)
# print(f"Toppers (score >= 75): {len(toppers)} students -> saved to toppers.csv")
#
# with zipfile.ZipFile("records.zip","w") as zf:
#     zf.write("students.csv"); zf.write("toppers.csv")
# with zipfile.ZipFile("records.zip","r") as zf:
#     print(f"records.zip contains: {zf.namelist()}")
#     zf.extractall("extracted/")
# print("Extracted to extracted/")

