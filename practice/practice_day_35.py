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
