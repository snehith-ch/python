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
