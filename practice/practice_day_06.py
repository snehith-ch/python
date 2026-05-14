# ============================================================
# PRACTICE — Day 6: List, Tuple, Set, Dictionary, Range
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: MUTABLE vs IMMUTABLE
# --------------------------------------------------

# Q1. Which of these are mutable and which are immutable?
#     Write M (mutable) or I (immutable) next to each:

# a) int          →  ___
# b) list         →  ___
# c) str          →  ___
# d) tuple        →  ___
# e) set          →  ___
# f) dict         →  ___
# g) float        →  ___
# h) bool         →  ___


# Q2. Predict the output — does id() change?

x = 10
print(id(x))
x = 20
print(id(x))

# Are the two IDs the same or different? Why?
# Your answer:


# --------------------------------------------------
# SECTION 2: LIST
# --------------------------------------------------

# Q3. Create a list of 5 cities. Print:
#     - The 1st city
#     - The last city (using negative index)
#     - The 3rd city

# YOUR CODE HERE:


# Q4. Change the 2nd element of your list to "Bangalore"
#     and print the list again.

# YOUR CODE HERE:


# Q5. Predict the output:

nums = [10, 20, 30, 40, 50]
nums.append(60)
nums.remove(30)
print(nums)
print(len(nums))

# Prediction:
# Line 1:
# Line 2:


# Q6. FIX THE BUG — this crashes with a TypeError:
#
# t = (1, 2, 3)
# t[0] = 99
# print(t)
#
# WHY does it crash? What would you use instead?
# YOUR EXPLANATION:


# --------------------------------------------------
# SECTION 3: TUPLE
# --------------------------------------------------

# Q7. Predict the type of each:

a = (10)
b = (10,)
c = ()
d = (10, 20, 30)

# print(type(a))   # prediction:
# print(type(b))   # prediction:
# print(type(c))   # prediction:
# print(type(d))   # prediction:


# Q8. Create a tuple holding: your name, age, city
#     Access each element using both positive and negative indexing.

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 4: SET
# --------------------------------------------------

# Q9. CRITICAL — What type is each?

x = {}
y = set()
z = {1, 2, 3}

# print(type(x))   # prediction:
# print(type(y))   # prediction:
# print(type(z))   # prediction:


# Q10. Create a set with duplicates and verify duplicates are removed:

data = {3, 1, 4, 1, 5, 9, 2, 6, 5, 5}
print(data)

# Prediction: ___________
# Does order match what you wrote? (Sets are unordered)


# Q11. Write code to:
#      - Create an empty set
#      - Add 10, 20, 30
#      - Remove 20
#      - Print the set

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 5: DICTIONARY
# --------------------------------------------------

# Q12. Create a dictionary for a student with:
#      keys: "name", "age", "marks"
#      values: your choice
#      Then:
#      - Print the value for "name"
#      - Update "marks" to a new value
#      - Add a new key "city"
#      - Print all keys and all values

# YOUR CODE HERE:


# Q13. Predict the output:

d = {"a": 1, "b": 2, "c": 3}
d["b"] = 99
d["d"] = 4
print(d)
print(len(d))

# Prediction:
# Line 1:
# Line 2:


# Q14. FIX THE BUG — what's wrong with using a list as a key?
#
# d = {[1, 2]: "value"}
# print(d)
#
# WHY does it crash?
# YOUR EXPLANATION:


# --------------------------------------------------
# SECTION 6: RANGE
# --------------------------------------------------

# Q15. Convert each range to a list and predict the output:

# print(list(range(5)))            # prediction:
# print(list(range(1, 6)))         # prediction:
# print(list(range(1, 10, 2)))     # prediction:
# print(list(range(10, 0, -1)))    # prediction:
# print(list(range(0, 20, 5)))     # prediction:


# Q16. What is wrong with this? Predict without running:
#
# print(range(1, 10))
#
# What does it print?
# How do you see all values?
# YOUR ANSWER:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Create a list of 5 numbers.
# Print: sum, minimum, maximum (use Python built-ins: sum(), min(), max())

# YOUR CODE HERE:


# BONUS 2:
# Create a shopping cart as a list: ["milk", "bread", "eggs"]
# - User wants to add "butter" → add to end
# - User changed mind about "bread" → remove it
# - Print final cart and number of items

# YOUR CODE HERE:


# BONUS 3:
# Create a dictionary of 3 students and their marks:
# {"Alice": 85, "Bob": 92, "Charlie": 78}
# Find and print:
# - The student with the highest marks (you can use max())
# - The average marks

# YOUR CODE HERE:


# BONUS 4:
# Using only a set — deduplicate this list without using any loop:
numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6, 5]
# Hint: convert to set, then convert back to list

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1:
# a) int    → I
# b) list   → M
# c) str    → I
# d) tuple  → I
# e) set    → M
# f) dict   → M
# g) float  → I
# h) bool   → I

# Q2: Different IDs — x = 20 creates a new int object in memory

# Q5:
# [10, 20, 40, 50, 60]  (30 removed, 60 added)
# 5

# Q6: Tuples are immutable — use a list instead

# Q7:
# a) int    (10 without comma is just int, parentheses are just grouping)
# b) tuple  (trailing comma makes it a tuple)
# c) tuple  (empty tuple)
# d) tuple

# Q9:
# x: dict   ({} with no elements = empty dict)
# y: set    (set() = empty set)
# z: set    ({elements} without key:value = set)

# Q13:
# {'a': 1, 'b': 99, 'c': 3, 'd': 4}
# 4

# Q14: Lists are mutable and therefore unhashable — dict keys must be immutable
# Use a tuple instead: {(1, 2): "value"}

# Q15:
# [0, 1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [1, 3, 5, 7, 9]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# [0, 5, 10, 15]

# Q16: print(range(1, 10)) prints "range(1, 10)" not the values
# Use: print(list(range(1, 10)))
