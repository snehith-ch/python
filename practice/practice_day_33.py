# ============================================================
# PRACTICE — Day 33: File Handling Basics
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: File Modes and Properties
# --------------------------------------------------

# Q1. Predict the file object properties:

f = open("test_q1.txt", "w")

print(f.name)       # prediction:
print(f.mode)       # prediction:
print(f.writable()) # prediction:
print(f.readable()) # prediction:
print(f.closed)     # prediction (file is open):

f.close()
print(f.closed)     # prediction (after close):


# Q2. Predict — mode 'r' on non-existent file:

# f = open("no_such_file.txt", "r")    # uncomment → prediction (error?):


# Q3. File modes comparison — fill in the blanks:
# Mode | Read | Write | Truncate | Create | Position
# 'r'  |  ?   |   ?   |    ?     |   ?    | beginning
# 'w'  |  ?   |   ?   |    ?     |   ?    | beginning
# 'a'  |  ?   |   ?   |    ?     |   ?    | end
# 'x'  |  ?   |   ?   |    ?     |   ?    | beginning

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 2: Writing to Files
# --------------------------------------------------

# Q4. write() vs writelines() — predict what appears in the file:

with open("test_q4.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

# After this runs, open test_q4.txt — prediction (content):


# Q5. writelines() — predict the file content:

with open("test_q5.txt", "w") as f:
    lines = ["Apple\n", "Banana\n", "Cherry\n"]
    f.writelines(lines)    # no separator added — lines must include \n

# prediction (content of file):


# Q6. append mode — predict:

with open("test_q6.txt", "w") as f:
    f.write("Original content\n")

with open("test_q6.txt", "a") as f:
    f.write("Appended line\n")

with open("test_q6.txt", "r") as f:
    print(f.read())    # prediction:


# Q7. 'w' mode truncates — predict:

with open("test_q7.txt", "w") as f:
    f.write("First write\n")

with open("test_q7.txt", "w") as f:    # 'w' truncates existing content!
    f.write("Second write\n")

with open("test_q7.txt", "r") as f:
    print(f.read())    # prediction (first or second write?):


# --------------------------------------------------
# SECTION 3: Reading from Files
# --------------------------------------------------

# Q8. Set up a file, then predict each read:

with open("test_q8.txt", "w") as f:
    f.write("Line A\nLine B\nLine C\n")

# read() — reads everything
with open("test_q8.txt", "r") as f:
    content = f.read()
    print(repr(content))    # prediction (with \n visible):

# readline() — reads one line at a time
with open("test_q8.txt", "r") as f:
    print(repr(f.readline()))   # prediction:
    print(repr(f.readline()))   # prediction:

# readlines() — reads all lines into a list
with open("test_q8.txt", "r") as f:
    lines = f.readlines()
    print(lines)     # prediction (list of strings):
    print(len(lines))    # prediction:


# Q9. Iterating over file lines — predict:

with open("test_q8.txt", "r") as f:
    for line in f:
        print(line.strip())    # prediction (3 lines, .strip() removes \n):


# --------------------------------------------------
# SECTION 4: with Statement
# --------------------------------------------------

# Q10. with statement auto-closes — predict:

with open("test_q10.txt", "w") as f:
    f.write("Auto-close test")
    print(f.closed)    # prediction (inside with):

print(f.closed)        # prediction (outside with):


# --------------------------------------------------
# SECTION 5: Write Code
# --------------------------------------------------

# Q11. Write a program that:
#   a) Creates a file "fruits.txt" with 5 fruits (one per line)
#   b) Reads the file and prints each fruit in uppercase

# YOUR CODE HERE:


# Q12. Write a program that:
#   a) Creates "log.txt" with "Session 1\n"
#   b) Appends "Session 2\n" and "Session 3\n"
#   c) Reads and prints all content

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — what happens after close():

f = open("bonus.txt", "w")
f.write("data")
f.close()
# f.write("more")    # uncomment → prediction (error?):


# BONUS 2: Predict — reading beyond EOF:

with open("test_q8.txt", "r") as f:
    print(repr(f.read()))         # prediction:
    print(repr(f.read()))         # prediction (read again — EOF):
    print(repr(f.readline()))     # prediction (at EOF):


# BONUS 3:
# Write a function word_count(filename) that:
# - Opens the file
# - Returns a dict with line_count, word_count, char_count
# Test it on test_q8.txt (which has "Line A\nLine B\nLine C\n")

# YOUR CODE HERE:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Which mode opens a file for READING only?
#    A) "w"    B) "r"    C) "a"    D) "x"
# Answer: ___

# Q_MCQ_2. What does  open("file.txt", "w")  do if the file already exists?
#    A) Appends to it    B) Raises FileExistsError
#    C) Truncates (overwrites) it    D) Opens in read mode
# Answer: ___

# Q_MCQ_3. What is the advantage of using  with open(...) as f:  ?
#    A) Faster file I/O    B) Auto-closes the file on exit
#    C) Works on binary files only    D) Avoids ImportError
# Answer: ___

# Q_MCQ_4. f.readlines()  returns:
#    A) A single string    B) A list of lines (with \n)
#    C) A generator    D) The number of lines
# Answer: ___

# Q_MCQ_5. Which mode APPENDS to an existing file (creates if missing)?
#    A) "r"    B) "w"    C) "a"    D) "x"
# Answer: ___

# Q_MCQ_6. To write multiple lines at once use:
#    A) f.write()    B) f.writelines()    C) f.puts()    D) f.dump()
# Answer: ___

# Q_MCQ_7. After reading a file, calling  f.read()  again returns:
#    A) The same content    B) An empty string (cursor at end)
#    C) FileNotFoundError    D) None
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. The default mode for  open()  is _______.

# FIB_2. To read the entire file as one string: f._______.

# FIB_3. with open("data.txt", "a") as f:  opens in _______ mode.

# FIB_4. Each string in the list returned by  readlines()  ends with _______.

# FIB_5. The  with  statement calls  f._______()  automatically on exit.

# FIB_6. To write a string to a file: f._______("Hello\n").

# FIB_7. Opening a file with mode "r" and the file does not exist raises
#         _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Build a Personal Diary App that reads and writes diary entries.
#
# Requirements:
#   1. Append a new diary entry to "diary.txt" (date + text, one per run)
#   2. Read and display ALL past entries from the file
#   3. Count total number of entries
#   4. Use  with  statement for all file operations
#   5. Handle FileNotFoundError gracefully if diary.txt does not exist yet
#   6. Strip trailing whitespace when displaying entries
#
# Expected output (2nd run after first entry):
#   === Your Diary ===
#   Entry 1: 2024-01-15 | Today I learned file handling!
#   Entry 2: 2024-01-16 | Files make data persistent!
#   Total entries: 2
#   New entry saved for 2024-01-16.
#
# Hint: Use datetime.date.today() for the date.
#       Write each entry as: "YYYY-MM-DD | text\n"
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "test_q1.txt", "w", True, False, False (open), True (after close)

# Q2: FileNotFoundError: [Errno 2] No such file or directory

# Q3: 'r': read=YES, write=NO, truncate=NO, create=NO
#     'w': read=NO, write=YES, truncate=YES, create=YES
#     'a': read=NO, write=YES, truncate=NO, create=YES
#     'x': read=NO, write=YES, truncate=NO, create=YES (fails if exists)

# Q4: File contains: "Line 1\nLine 2\nLine 3\n" (3 lines)

# Q6: "Original content\nAppended line\n" (both lines)

# Q7: "Second write\n" only (w mode erased first write)

# Q8: 'Line A\nLine B\nLine C\n', 'Line A\n', 'Line B\n',
#     ['Line A\n', 'Line B\n', 'Line C\n'], 3

# Q9: Line A, Line B, Line C (each on its own line, \n stripped)

# Q10: False (inside with — still open), True (outside with — auto-closed)

# BONUS 1: ValueError: I/O operation on closed file

# BONUS 2: 'Line A\nLine B\nLine C\n', '' (empty string at EOF), '' (at EOF)

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: "r"  (read mode)
# FIB_2: read()
# FIB_3: append
# FIB_4: \n  (newline character)
# FIB_5: close
# FIB_6: write
# FIB_7: FileNotFoundError

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# from datetime import date
# DIARY = "diary.txt"
#
# def read_diary():
#     try:
#         with open(DIARY, "r") as f:
#             lines = [l.rstrip() for l in f.readlines()]
#         print("=== Your Diary ===")
#         for i, line in enumerate(lines, 1):
#             print(f"Entry {i}: {line}")
#         print(f"Total entries: {len(lines)}")
#         return len(lines)
#     except FileNotFoundError:
#         print("No diary found. Starting fresh!")
#         return 0
#
# def write_entry(text):
#     entry = f"{date.today()} | {text}"
#     with open(DIARY, "a") as f:
#         f.write(entry + "\n")
#     print(f"New entry saved for {date.today()}.")
#
# read_diary()
# write_entry("Today I practiced file handling!")

