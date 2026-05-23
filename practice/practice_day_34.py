# ============================================================
# PRACTICE — Day 34: File Handling Advanced
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: x Mode and os.path.isfile()
# --------------------------------------------------

# Q1. 'x' mode — exclusive create — predict:

import os

# a) Create a new file with 'x' mode
if os.path.isfile("exclusive.txt"):
    os.remove("exclusive.txt")    # clean up first

with open("exclusive.txt", "x") as f:
    f.write("Created with x mode")
print("File created successfully")   # prediction:

# b) Try creating the same file again
# with open("exclusive.txt", "x") as f:   # uncomment → prediction (error?):
#     f.write("Second time")


# Q2. os.path.isfile() — predict:

print(os.path.isfile("exclusive.txt"))   # prediction:
print(os.path.isfile("no_file.txt"))     # prediction:
print(os.path.isfile("."))               # prediction (. is a directory):


# --------------------------------------------------
# SECTION 2: tell() and seek()
# --------------------------------------------------

# Q3. tell() — cursor position — predict:

with open("tell_test.txt", "w") as f:
    f.write("Hello World")

with open("tell_test.txt", "r") as f:
    print(f.tell())           # prediction (start position):
    ch = f.read(1)
    print(ch)                 # prediction (first character):
    print(f.tell())           # prediction (after reading 1 char):
    content = f.read(5)
    print(content)            # prediction (next 5 chars):
    print(f.tell())           # prediction:


# Q4. seek() — move cursor — predict:

with open("tell_test.txt", "r") as f:
    f.seek(6)                 # move to position 6
    print(f.tell())           # prediction:
    print(f.read())           # prediction (reads from position 6):

    f.seek(0)                 # move back to start
    print(f.read(5))          # prediction:


# --------------------------------------------------
# SECTION 3: File Modification with r+ Mode
# --------------------------------------------------

# Q5. r+ mode — read AND write — predict:

# Setup: write a file with names
with open("names.txt", "w") as f:
    f.write("Sita Ravi Mohan")

# Now modify: replace "Ravi" with "XXXX"
with open("names.txt", "r+") as f:
    text = f.read()
    print(f"Before: {text}")    # prediction:

    f.seek(5)                   # "Sita " is 5 chars, so position 5 = 'R'
    f.write("XXXX")             # overwrites next 4 chars

    f.seek(0)
    print(f"After:  {f.read()}")  # prediction:


# Q6. tell() and seek() for specific replacement — predict:

with open("greet.txt", "w") as f:
    f.write("Hello Alice")

with open("greet.txt", "r+") as f:
    print(f.tell())    # prediction:
    f.seek(6)          # jump to position 6 (start of "Alice")
    f.write("Bob  ")   # "Bob  " — 5 chars to match "Alice"
    f.seek(0)
    print(f.read())    # prediction:


# --------------------------------------------------
# SECTION 4: Counting Lines, Words, Characters
# --------------------------------------------------

# Q7. Predict the count values:

with open("count_test.txt", "w") as f:
    f.write("Python is fun\nI love coding\nKeep practicing\n")

line_count = 0
word_count = 0
char_count = 0

with open("count_test.txt", "r") as f:
    for line in f:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

print(f"Lines: {line_count}")   # prediction:
print(f"Words: {word_count}")   # prediction:
print(f"Chars: {char_count}")   # prediction (includes \n):


# --------------------------------------------------
# SECTION 5: Write Code
# --------------------------------------------------

# Q8. Write a function that:
#   - Takes a filename and a word to find
#   - Opens the file and checks if the word appears
#   - Prints "Found" or "Not found"

# YOUR CODE HERE:


# Q9. Write code that:
#   - Creates "data.txt" with 5 lines: "Item 1", "Item 2", ..., "Item 5"
#   - Reads the file, counts lines and words
#   - Prints a summary

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — seek(0, 2) moves to end:

with open("tell_test.txt", "r") as f:
    f.seek(0, 2)          # 0 bytes from end (2 = SEEK_END)
    print(f.tell())       # prediction (file size = length of "Hello World"):
    print(repr(f.read())) # prediction (at EOF):


# BONUS 2: Write a program that reads a file and reverses the order of lines:
# Example: ["Line 1\n", "Line 2\n", "Line 3\n"] → writes "Line 3\nLine 2\nLine 1\n"

# YOUR CODE HERE:


# BONUS 3: Predict — multiple seek() calls:

with open("tell_test.txt", "r") as f:
    f.seek(6)
    a = f.read(1)    # prediction:
    f.seek(0)
    b = f.read(1)    # prediction:
    f.seek(4)
    c = f.read(1)    # prediction ("Hello World"[4] = ?):

print(a, b, c)       # prediction:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Mode "x" opens a file for:
#    A) Exclusive read    B) XML parsing
#    C) Create-only (fails if file exists)    D) Execute mode
# Answer: ___

# Q_MCQ_2. f.tell()  returns:
#    A) Number of lines    B) Current byte position of the cursor
#    C) Total file size    D) Whether file is open
# Answer: ___

# Q_MCQ_3. f.seek(0)  moves the cursor to:
#    A) End of file    B) Beginning of file    C) Line 0    D) Byte 10
# Answer: ___

# Q_MCQ_4. Mode "r+"  is used for:
#    A) Read-only    B) Write-only
#    C) Read + Write (file must exist)    D) Append + Read
# Answer: ___

# Q_MCQ_5. After f.seek(0, 2), f.tell() returns:
#    A) 0    B) 1    C) Total number of lines    D) Total file size in bytes
# Answer: ___

# Q_MCQ_6. What does  f.seek(0, 1)  mean?
#    A) Seek to byte 0 from start    B) Seek 0 bytes from current position
#    C) Seek to end    D) Reset cursor
# Answer: ___

# Q_MCQ_7. To both read AND write an existing file from the beginning:
#    A) "r"    B) "w"    C) "r+"    D) "a"
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. f.seek(0) is equivalent to f.seek(0, _______) where 0 = SEEK_SET.

# FIB_2. To find the file size: open in "rb" mode, seek to end with
#         f.seek(0, _______), then call f.tell().

# FIB_3. Mode "_______" raises FileExistsError if the file already exists.

# FIB_4. f.seek(n, 1) moves  n  bytes from the _______ position.

# FIB_5. To overwrite the first line without deleting the rest, use mode
#         "_______" and  f.seek(0).

# FIB_6. f.readlines() reads _______, while f.readline() reads _______.

# FIB_7. The two WHENCE values for seek:  0 = _______, 1 = _______, 2 = _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Build a Log File Analyzer that reads, parses, and modifies logs.
#
# Requirements:
#   1. Create "app.log" with 5 sample log lines (INFO, WARNING, ERROR levels)
#   2. Read the file and count INFO / WARNING / ERROR occurrences
#   3. Use tell() to record the byte position before each line read
#   4. Use seek() to re-read a specific line by its stored byte position
#   5. Append a new ERROR log entry at the end
#   6. Display the file size in bytes before and after appending
#
# Expected output (example):
#   === Log Summary ===
#   INFO    : 2
#   WARNING : 1
#   ERROR   : 2
#   File size before: 215 bytes
#   File size after:  248 bytes
#   Re-reading first ERROR line: [ERROR] Database connection failed
#
# Hint: Use "r+" to read/seek, "a" to append.
#       Store tell() positions in a list while reading.
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q2: True, False, False (. is a directory, not a file)

# Q3: 0, 'H', 1, 'ello ', 6

# Q4: position 6, "World", "Hello"

# Q5: "Before: Sita Ravi Mohan", "After:  Sita XXXX Mohan"

# Q6: 0, "Hello Bob  "

# Q7: Lines: 3, Words: 9 (3+3+2? actually: "Python is fun"=3, "I love coding"=3, "Keep practicing"=2 = 8)
#     Chars: "Python is fun\n"=15, "I love coding\n"=15, "Keep practicing\n"=17 = 47
#     (count the characters including spaces and \n)

# BONUS 1: 11 (len "Hello World"), '' (at EOF)

# BONUS 3: 'W' (position 6 of "Hello World"), 'H' (position 0), 'o' (position 4)
#          W H o

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: C   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: C
# Q_MCQ_5: D   Q_MCQ_6: B   Q_MCQ_7: C

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: 0
# FIB_2: 2  (SEEK_END)
# FIB_3: x
# FIB_4: current
# FIB_5: r+
# FIB_6: all lines as a list; one line as a string
# FIB_7: start of file; current position; end of file

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# LOG = "app.log"
# sample = [
#     "[INFO] Server started\n",
#     "[INFO] Config loaded\n",
#     "[WARNING] Memory usage high\n",
#     "[ERROR] Database connection failed\n",
#     "[ERROR] Timeout on request /api\n",
# ]
# with open(LOG, "w") as f:
#     f.writelines(sample)
#
# counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
# positions = {}
# with open(LOG, "r") as f:
#     while True:
#         pos = f.tell()
#         line = f.readline()
#         if not line: break
#         for level in counts:
#             if f"[{level}]" in line:
#                 counts[level] += 1
#                 if level not in positions:
#                     positions[level] = pos
#
# print("=== Log Summary ===")
# for level, count in counts.items():
#     print(f"{level:<8}: {count}")
#
# import os
# size_before = os.path.getsize(LOG)
# with open(LOG, "a") as f:
#     f.write("[ERROR] New critical error detected\n")
# size_after = os.path.getsize(LOG)
# print(f"File size before: {size_before} bytes")
# print(f"File size after:  {size_after} bytes")
#
# with open(LOG, "r") as f:
#     f.seek(positions["ERROR"])
#     print(f"Re-reading first ERROR line: {f.readline().strip()}")

