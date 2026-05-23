# ============================================================
# PRACTICE — Day 11: Advanced String Functions & List Intro
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: STRIP FUNCTIONS
# --------------------------------------------------

# Q1. Predict the output of each:

s = "   Hello, Python!   "

# print(s.strip())    # prediction:
# print(s.lstrip())   # prediction:
# print(s.rstrip())   # prediction:


# Q2. Custom character stripping — predict:

s = "aaaDurgaSoftaaa"

# print(s.strip("a"))    # prediction:
# print(s.lstrip("a"))   # prediction:
# print(s.rstrip("a"))   # prediction:


# Q3. What would happen here? Predict:

s = "xxHello Worldxx"
# print(s.strip("x"))    # prediction:
# print(s.strip("xo"))   # prediction:   ← strips ALL x and o from both ends


# --------------------------------------------------
# SECTION 2: find() and index()
# --------------------------------------------------

# Q4. Predict the output:

s = "python is easy and python is fun"

# print(s.find("python"))    # prediction:
# print(s.find("java"))      # prediction:   ← not found
# print(s.index("easy"))     # prediction:
# print(s.rindex("python"))  # prediction:   ← last occurrence


# Q5. Predict the output — and which line causes an error?

s = "hello world"
print(s.find("xyz"))      # prediction:
# print(s.index("xyz"))   # prediction: (what error?)


# Q6. USE find() to safely check and report:
#     Check if "Python" is in the string "I love Python programming"
#     If yes — print "Found at index X"
#     If no  — print "Not found"

sentence = "I love Python programming"
# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 3: max(), min(), ord()
# --------------------------------------------------

# Q7. Predict which character is returned:

s = "Python"
# print(max(s))   # prediction:   ← remember ASCII ordering
# print(min(s))   # prediction:


# Q8. Predict the ord() values:

# print(ord("A"))   # prediction:
# print(ord("a"))   # prediction:
# print(ord("z"))   # prediction:
# print(ord("Z"))   # prediction:
# Ordering: uppercase (65-90) or lowercase (97-122) comes first in ASCII?


# --------------------------------------------------
# SECTION 4: partition()
# --------------------------------------------------

# Q9. Predict the output and type:

s = "python is easy and it is fun"
result = s.partition("is")

# print(result)        # prediction:
# print(type(result))  # prediction:
# print(result[0])     # prediction:
# print(result[1])     # prediction:
# print(result[2])     # prediction:


# Q10. Compare partition() vs split():

s = "a-b-c-d"
# print(s.partition("-"))   # prediction:
# print(s.split("-"))       # prediction:
# Differences (write as comment):
# 1.
# 2.


# --------------------------------------------------
# SECTION 5: startswith() and endswith()
# --------------------------------------------------

# Q11. Predict True or False:

s = "Hello, World!"

# print(s.startswith("Hello"))    # prediction:
# print(s.startswith("hello"))    # prediction:   ← case-sensitive!
# print(s.endswith("!"))          # prediction:
# print(s.endswith("World!"))     # prediction:
# print(s.endswith("world!"))     # prediction:


# --------------------------------------------------
# SECTION 6: isdigit, isalpha, isalnum
# --------------------------------------------------

# Q12. Predict True or False for each — justify your answer:

tests = ["12345", "12.5", "hello", "hello1", "hello 1", "Hello", "abc!", ""]

for t in tests:
    # print(f"{t!r:15} isdigit={t.isdigit()}, isalpha={t.isalpha()}, isalnum={t.isalnum()}")
    pass

# Uncomment the print line and run — then explain any surprising results:


# --------------------------------------------------
# SECTION 7: LIST — Intro
# --------------------------------------------------

# Q13. Create a list of 5 fruits and access:
#      - First fruit (positive index)
#      - Last fruit (negative index)
#      - Middle fruit

# YOUR CODE HERE:


# Q14. Nested list — predict the output:

L = [10, 20, ["Python", "Java", "C++"], 40, 50]

# print(L[2])        # prediction:
# print(L[2][0])     # prediction:
# print(L[2][-1])    # prediction:
# print(L[-3][1])    # prediction:


# Q15. Predict the output — show the list at each step:

L = [1, 2, 3, 4, 5]
print("Original:", L)

L.append(6)
print("After append(6):", L)

L.insert(0, 99)
print("After insert(0,99):", L)

L.extend([10, 20])
print("After extend([10,20]):", L)

L.remove(3)
print("After remove(3):", L)

L.pop(1)
print("After pop(1):", L)


# Q16. FIX THE BUG — predict the error:

# L = [1, 2, 3]
# L.remove(10)   # what error? prediction:
# L.pop(10)      # what error? prediction:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Take a string at runtime. Check:
# a) Does it start and end with a letter?
# b) Is it all digits? All letters? Alphanumeric?
# c) Print result of strip() — remove any whitespace

# YOUR CODE HERE:


# BONUS 2:
# Create a list of 5 numbers from user input using a for loop.
# Then print:
# - List in original order
# - List reversed (hint: slicing [::-1])
# - First and last element

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

s = "  Python Programming  "
print(len(s))
print(s.strip())
print(len(s.strip()))
print(s.find("Prog"))
print(s.partition("P"))
print("Python".startswith("Py"))
print("Python123".isalnum())
print("Python 123".isalnum())

# Your full prediction:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What does  "  hello  ".strip()  return?
#    A) "  hello  "    B) "hello"    C) "hello  "    D) "  hello"
# Answer: ___

# Q_MCQ_2. What does  list.append(x)  return?
#    A) The updated list    B) x    C) None    D) The index of x
# Answer: ___

# Q_MCQ_3. What is the difference between  find()  and  index()?
#    A) No difference
#    B) find() raises ValueError if not found; index() returns -1
#    C) index() raises ValueError if not found; find() returns -1
#    D) find() is for lists; index() is for strings
# Answer: ___

# Q_MCQ_4. list.pop()  with no argument removes:
#    A) The first element    B) The last element
#    C) All elements         D) A random element
# Answer: ___

# Q_MCQ_5. "hello world".split("o")  returns:
#    A) ['hello', 'world']    B) ['hell', ' w', 'rld']
#    C) ['helloworld']        D) Error
# Answer: ___

# Q_MCQ_6. list.sort()  vs  sorted(list):
#    A) Both return a new sorted list
#    B) sort() modifies in-place (returns None); sorted() returns new list
#    C) sorted() modifies in-place; sort() returns new list
#    D) They are identical in every way
# Answer: ___

# Q_MCQ_7. "racecar".lstrip("r")  returns:
#    A) "acecar"    B) "aceca"    C) "racecar"    D) "acecar" — strips all 'r's from left
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. "***hello***".strip("*") = _______.

# FIB_2. "hello world".find("world") returns _______ (the start index).

# FIB_3. [1, 2, 3].insert(1, 99) makes the list _______.

# FIB_4. [10, 20, 30].pop(0) returns _______ and leaves _______.

# FIB_5. "hello".replace("l", "r") = _______.

# FIB_6. "a,b,c".split(",") = _______.

# FIB_7. lstrip() strips from the _______ side; rstrip() from the _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Text Message Cleaner & Analyzer for a chat application.
# The app receives messy user messages that need cleaning and analysis.
#
# Raw message (copy this exactly):
#   raw = "  *** Hello   Python   World!  I love python.  ***   "
#
# Requirements:
#   1. Strip leading/trailing spaces AND * characters
#   2. Squeeze multiple spaces into one (hint: split() then join)
#   3. Convert to title case
#   4. Count how many times "python" appears (case-insensitive)
#   5. Replace "python" (any case) with "Python 🐍"
#   6. Split into individual words; print word count
#   7. Check if message starts with "Hello" and ends with "."
#   8. Find the index of "World" in the cleaned message
#
# Expected output (approximate):
#   Raw      : "  *** Hello   Python   World!  I love python.  ***   "
#   Stripped : "Hello   Python   World!  I love python."
#   Cleaned  : "Hello Python World! I Love Python."
#   "python" count (original, case-insensitive): 2
#   After replace: "Hello Python 🐍 World! I Love Python 🐍."
#   Word count : 8
#   Starts with 'Hello': True
#   Index of 'World': 14
#
# Hint: strip("* ") strips both spaces AND asterisks in one call.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "Hello, Python!", "Hello, Python!   ", "   Hello, Python!"

# Q2: "DurgaSoft", "DurgaSoftaaa", "aaaDurgaSoft"

# Q4:
# find("python") = 0  (first occurrence at index 0)
# find("java")   = -1 (not found)
# index("easy")  = 10
# rindex("python") = 18  (last occurrence)

# Q5: find("xyz") = -1; index("xyz") raises ValueError

# Q7: max = y (ord 121), min = P (ord 80) — uppercase < lowercase in ASCII

# Q8: A=65, a=97, z=122, Z=90  — uppercase FIRST (65-90), then lowercase (97-122)

# Q9: ('python ', 'is', ' easy and it is fun'), tuple, 'python ', 'is', ' easy and...'

# Q10:
# partition: ('a', '-', 'b-c-d')  — first occurrence only, 3-tuple, sep included
# split:     ['a', 'b', 'c', 'd'] — all occurrences, list, sep not included

# Q11: True, False, True, True, False

# Q14:
# ['Python', 'Java', 'C++']
# Python
# C++
# Java

# BONUS 3:
# 22 (with spaces), "Python Programming", 20, 9, ('  ', 'P', 'ython Programming  ')
# True, True, False (space makes it fail isalnum)


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: C   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: A

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: "hello"
# FIB_2: 6
# FIB_3: [1, 99, 2, 3]
# FIB_4: 10;  [20, 30]
# FIB_5: "herro"
# FIB_6: ['a', 'b', 'c']
# FIB_7: left;  right

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# raw = "  *** Hello   Python   World!  I love python.  ***   "
# print(f'Raw      : "{raw}"')
# stripped = raw.strip("* ").strip()
# print(f'Stripped : "{stripped}"')
# cleaned = " ".join(stripped.split()).title()
# print(f'Cleaned  : "{cleaned}"')
# count = stripped.lower().count("python")
# print(f'"python" count (original, case-insensitive): {count}')
# import re
# replaced = re.sub(r'python', 'Python 🐍', cleaned, flags=re.IGNORECASE)
# print(f'After replace: "{replaced}"')
# words = cleaned.split()
# print(f'Word count : {len(words)}')
# print(f"Starts with 'Hello': {cleaned.startswith('Hello')}")
# idx = cleaned.find("World")
# print(f"Index of 'World': {idx}")

