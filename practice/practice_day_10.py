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
