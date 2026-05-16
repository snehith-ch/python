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
