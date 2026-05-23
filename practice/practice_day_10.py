# ============================================================
# PRACTICE — Day 10: String Operations and Functions
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: INDEXING
# --------------------------------------------------

# Q1. Write the positive AND negative index for each character:
#
# String: "Python"
#
# Character | Positive index | Negative index
# --------- | -------------- | --------------
#    P       |       0        |     -6
#    y       |       ?        |      ?
#    t       |       ?        |      ?
#    h       |       ?        |      ?
#    o       |       ?        |      ?
#    n       |       ?        |      ?


# Q2. Predict the output:

s = "Python"

# print(s[0])     # prediction:
# print(s[5])     # prediction:
# print(s[-1])    # prediction:
# print(s[-6])    # prediction:
# print(s[2])     # prediction:
# print(s[-3])    # prediction:


# Q3. What is the output — and what error would s[6] give?

s = "Python"
print(s[-1])       # should print: ?
# print(s[6])      # uncomment to see error — predict the error message first:
# Error prediction:


# --------------------------------------------------
# SECTION 2: SLICING
# --------------------------------------------------

# Q4. Predict the output:

s = "abcdefgh"

# print(s[0:4])     # prediction:
# print(s[2:6])     # prediction:
# print(s[:3])      # prediction:   ← start defaults to 0
# print(s[5:])      # prediction:   ← stop defaults to end
# print(s[:])       # prediction:   ← full string
# print(s[1:7:2])   # prediction:   ← step 2
# print(s[::-1])    # prediction:   ← reverse


# Q5. Given s = "Hello, World!" — predict:

s = "Hello, World!"

# print(s[0:5])      # prediction:
# print(s[7:12])     # prediction:
# print(s[-6:-1])    # prediction:
# print(s[::-1])     # prediction:


# Q6. Write slicing to extract:
#     From "Python Programming"
#     a) "Python"   (first 6 chars)
#     b) "Program"  (chars 7 to 13)
#     c) "Porm"     (every 4th char using step)

s = "Python Programming"
# a)
# b)
# c)


# --------------------------------------------------
# SECTION 3: CONCATENATION AND REPETITION
# --------------------------------------------------

# Q7. Predict the output:

# print("Hello" + " " + "World")   # prediction:
# print("Ha" * 4)                   # prediction:
# print("-" * 20)                   # prediction:


# Q8. FIX THE BUG:
#
# name = "Snehith"
# age = 22
# print("Name: " + name + " Age: " + age)   ← crashes!
#
# WHY does it crash?
# YOUR FIX:


# --------------------------------------------------
# SECTION 4: split()
# --------------------------------------------------

# Q9. Predict the output:

sentence = "Python is easy to learn"
words = sentence.split()

# print(words)        # prediction:
# print(type(words))  # prediction:
# print(len(words))   # prediction:
# print(words[0])     # prediction:
# print(words[-1])    # prediction:


# Q10. Split with a custom separator:

data = "10,20,30,40,50"
nums = data.split(",")
# print(nums)     # prediction:
# print(nums[2])  # prediction:


# Q11. Write code to:
#      - Take the string "Alice:85:Python"
#      - Split by ":"
#      - Print name, score, subject separately

s = "Alice:85:Python"
# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 5: STRING FUNCTIONS
# --------------------------------------------------

# Q12. Predict the output:

s = "python programming is fun"

# print(s.capitalize())   # prediction:
# print(s.title())        # prediction:
# print(s.upper())        # prediction:


# Q13. Predict:

s = "Hello World"
# print(s.lower())        # prediction:
# print(s.swapcase())     # prediction:
# print(s.upper())        # prediction:


# Q14. count() — predict:

s = "banana"
# print(s.count("a"))    # prediction:
# print(s.count("an"))   # prediction:
# print(s.count("na"))   # prediction:
# print(s.count("x"))    # prediction:


# Q15. replace() — predict:

s = "I love Java and Java is great"
# print(s.replace("Java", "Python"))   # prediction:

s2 = "aabbccaa"
# print(s2.replace("a", "x"))          # prediction:


# Q16. join() — predict:

words = ["Python", "is", "awesome"]
# print(" ".join(words))    # prediction:
# print("-".join(words))    # prediction:
# print("".join(words))     # prediction:


# --------------------------------------------------
# SECTION 6: SORT STRINGS
# --------------------------------------------------

# Q17. Sort the words in this sentence alphabetically:

sentence = "zebra apple mango banana cherry"
# Step 1: split
# Step 2: sort
# Step 3: join back with space
# YOUR CODE:


# Q18. Sort this sentence in REVERSE alphabetical order:

sentence = "zebra apple mango banana cherry"
# Hint: list.sort(reverse=True)
# YOUR CODE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Given: s = "Hello, World!"
# Using only slicing and string methods:
# a) Print it reversed
# b) Print every other character
# c) Print it in ALL CAPS with all spaces replaced by "_"

s = "Hello, World!"
# a)
# b)
# c)


# BONUS 2:
# Count vowels in a string using a for loop:
# Given: "Python Programming"
# Expected: 5 vowels (y doesn't count)

text = "Python Programming"
# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

s = "DataScience"
print(s[0])
print(s[-1])
print(s[4:7])
print(s[::-1])
print(s.upper())
print(s.lower())
print(s.count("a"))
print(s.replace("a", "@"))
words = s.split("S")
print(words)
print(len(s))

# Your full prediction:


# BONUS 4:
# Palindrome checker:
# A word is a palindrome if it reads the same forwards and backwards.
# Check if "racecar", "python", "level" are palindromes.
# Use slicing [::-1] to reverse, then compare.

# YOUR CODE HERE:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What is  "Python"[-1]?
#    A) 'P'    B) 'n'    C) 'o'    D) 'y'
# Answer: ___

# Q_MCQ_2. What does  "Hello World"[2:7]  return?
#    A) "ello "    B) "Hello"    C) "llo W"    D) "llo"
# Answer: ___

# Q_MCQ_3. Which method converts "hello world" to "Hello World"?
#    A) .upper()    B) .capitalize()    C) .title()    D) .swapcase()
# Answer: ___

# Q_MCQ_4. "banana".count("a")  returns:
#    A) 1    B) 2    C) 3    D) 0
# Answer: ___

# Q_MCQ_5. "Hello".find("z")  returns:
#    A) 0    B) -1    C) None    D) Error
# Answer: ___

# Q_MCQ_6. " ".join(["a", "b", "c"])  returns:
#    A) "abc"    B) "a b c"    C) ["a","b","c"]    D) "a,b,c"
# Answer: ___

# Q_MCQ_7. "Python"[::−1]  returns:
#    A) "Python"    B) "nohtyP"    C) "P"    D) "n"
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. Negative index -1 refers to the _______ character of a string.

# FIB_2. s[1:4]  extracts characters at indices _______, _______, _______.
#         (start is _______, stop is _______.)

# FIB_3. "hello".upper() = _______,   "WORLD".lower() = _______.

# FIB_4. "apple mango".split()  returns _______.

# FIB_5. "Python".replace("P", "J") = _______.

# FIB_6. "hello".index("z") raises _______, but
#         "hello".find("z") returns _______.

# FIB_7. "  spacious  ".strip() = _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Username Validator & Formatter for a web app signup.
#
# Requirements:
#   1. Take a username as input()
#   2. Validate:  a) Length 5-15 chars
#                 b) Starts with a letter (use isalpha on [0])
#                 c) No spaces (check ' ' not in username)
#                 d) Only letters, digits, underscores
#                    (all chars: c.isalnum() or c == '_')
#   3. If any check fails, print the specific rule that was violated
#   4. If valid, print:
#      - Original, UPPERCASE, title case, reversed
#      - Count of vowels (a,e,i,o,u) using .count() for each
#      - Check if username starts/ends with specific letters
#
# Expected output (input: "snehith"):
#   ✓ Username is VALID
#   Original  : snehith
#   Uppercase : SNEHITH
#   Title     : Snehith
#   Reversed  : htihens
#   Vowels    : 2  (e, i)
#   Starts with 's': True
#   Ends with 'h'  : True
#
# Hint: Use a list of (condition, error_message) tuples to validate cleanly.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1:
# y: +1, -5 | t: +2, -4 | h: +3, -3 | o: +4, -2 | n: +5, -1

# Q2: P, n, n, P, t, h

# Q4:
# s[0:4]   = "abcd"
# s[2:6]   = "cdef"
# s[:3]    = "abc"
# s[5:]    = "fgh"
# s[:]     = "abcdefgh"
# s[1:7:2] = "bdf"
# s[::-1]  = "hgfedcba"

# Q5:
# s[0:5]   = "Hello"
# s[7:12]  = "World"
# s[-6:-1] = "World"
# s[::-1]  = "!dlroW ,olleH"

# Q7: "Hello World", "HaHaHaHa", "--------------------"

# Q8: Can't concatenate str and int; fix: str(age) or use f-string or comma in print

# Q9: ['Python', 'is', 'easy', 'to', 'learn'], <class 'list'>, 5, 'Python', 'learn'

# Q12:
# "Python programming is fun"  (only first letter capitalized)
# "Python Programming Is Fun"  (every word)
# "PYTHON PROGRAMMING IS FUN"

# Q14: 3, 2, 2, 0

# Q15:
# "I love Python and Python is great"
# "xxbbccxx"

# Q16:
# "Python is awesome"
# "Python-is-awesome"
# "Pythonisawesome"

# BONUS 3:
# D, e, Sci, ecneicSataD, DATASCIENCE, datascience, 2, D@t@Science, ['Data', 'cience'], 11


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: C   Q_MCQ_4: C
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: last
# FIB_2: 1, 2, 3;  inclusive;  exclusive
# FIB_3: "HELLO";  "world"
# FIB_4: ['apple', 'mango']
# FIB_5: "Jython"
# FIB_6: ValueError;  -1
# FIB_7: "spacious"

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# username = input("Enter username: ")
# errors = []
# if not (5 <= len(username) <= 15):
#     errors.append("Length must be 5-15 characters")
# if not username[0].isalpha():
#     errors.append("Must start with a letter")
# if ' ' in username:
#     errors.append("No spaces allowed")
# if not all(c.isalnum() or c == '_' for c in username):
#     errors.append("Only letters, digits, and underscores allowed")
# if errors:
#     print("✗ Invalid username:")
#     for e in errors: print(f"  - {e}")
# else:
#     print("✓ Username is VALID")
#     print(f"Original  : {username}")
#     print(f"Uppercase : {username.upper()}")
#     print(f"Title     : {username.title()}")
#     print(f"Reversed  : {username[::-1]}")
#     vowels = sum(username.lower().count(v) for v in 'aeiou')
#     print(f"Vowels    : {vowels}")
#     print(f"Starts with '{username[0]}': True")
#     print(f"Ends with '{username[-1]}'  : True")

