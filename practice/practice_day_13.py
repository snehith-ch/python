# ============================================================
# PRACTICE — Day 13: Sets & Dictionaries (Complete)
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: SET BASICS
# --------------------------------------------------

# Q1. Predict the type and content:

a = {}
b = set()
c = {1, 2, 3, 2, 1}
d = {3, 1, 4, 1, 5}

# print(type(a))   # prediction:
# print(type(b))   # prediction:
# print(c)         # prediction:   ← duplicates?
# print(d)         # prediction:   ← order?


# Q2. Can you predict the exact output of this set?
#     (Hint: sets are unordered — order may vary)

s = {5, 3, 8, 1, 9, 2}
# print(s)   # prediction (approximate — list unique elements):


# --------------------------------------------------
# SECTION 2: add() and update()
# --------------------------------------------------

# Q3. Predict the content of the set after each operation:

s = {10, 20, 30}
print("Start:", s)

s.add(40)
print("After add(40):", s)

s.update([50, 60, 70])
print("After update([50,60,70]):", s)

s.add(20)         # 20 is already there
print("After add(20) again:", s)


# --------------------------------------------------
# SECTION 3: discard() vs remove()
# --------------------------------------------------

# Q4. Predict the output — which line causes an error?

s = {10, 20, 30, 40}

s.discard(10)
print(s)             # prediction:

s.discard(100)       # 100 not in set
print(s)             # prediction:   ← error or silent?

s.remove(20)
print(s)             # prediction:

# s.remove(100)      # uncomment to see the error — predict first:
# prediction:


# Q5. What is the difference between discard() and remove()?
# YOUR ANSWER (one sentence each):
# discard():
# remove():


# --------------------------------------------------
# SECTION 4: SET OPERATIONS
# --------------------------------------------------

# Q6. Predict the output of all set operations:

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# print(A | B)    # union — prediction:
# print(A & B)    # intersection — prediction:
# print(A - B)    # difference A minus B — prediction:
# print(B - A)    # difference B minus A — prediction:
# print(A ^ B)    # symmetric difference — prediction:


# Q7. FIX THE BUG — predict what is wrong:

# A = {1, 2, 3}
# B = {3, 4, 5}
# result = A.union(B)
# print(A)        # has union changed A? prediction:
# print(result)   # prediction:


# Q8. What is the difference between union (|) and symmetric difference (^)?
# Use sets A={1,2,3,4,5} and B={4,5,6,7,8} to explain.
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 5: DICTIONARY BASICS
# --------------------------------------------------

# Q9. Create a dictionary for a person with:
#     name, age, city, job
#     Then access each value in TWO ways:
#     a) square bracket access
#     b) get() method

# YOUR CODE HERE:


# Q10. Predict the output — which access causes an error?

d = {"name": "Snehith", "age": 22}

# print(d["name"])          # prediction:
# print(d.get("name"))      # prediction:
# print(d["city"])          # prediction:   ← key not present
# print(d.get("city"))      # prediction:
# print(d.get("city", "N/A"))  # prediction:


# Q11. Add and update values — predict after each step:

d = {"name": "Alice", "marks": 80}
print("Start:", d)

d["marks"] = 95        # update existing
print("After update:", d)

d["grade"] = "A"       # add new key
print("After add:", d)

d["name"] = "Bob"
print("Final:", d)


# --------------------------------------------------
# SECTION 6: DICTIONARY KEYS
# --------------------------------------------------

# Q12. Which keys are valid? Predict VALID or INVALID and why:

# d1 = {1: "int key"}               # prediction:
# d2 = {1.5: "float key"}           # prediction:
# d3 = {"name": "str key"}          # prediction:
# d4 = {(1, 2): "tuple key"}        # prediction:
# d5 = {[1, 2]: "list key"}         # prediction:   ← mutable!
# d6 = {True: "bool key"}           # prediction:


# Q13. FIX THE BUG:

# d = {[1, 2, 3]: "values"}   # crash!
# print(d)

# WHY does it crash?
# HOW do you fix it?
# YOUR FIX:


# --------------------------------------------------
# SECTION 7: DELETE, COPY, METHODS
# --------------------------------------------------

# Q14. Predict the output:

d = {"a": 1, "b": 2, "c": 3, "d": 4}

val = d.pop("b")
print(val)       # prediction:
print(d)         # prediction:

last = d.popitem()
print(last)      # prediction:   ← last inserted
print(d)         # prediction:


# Q15. Dictionary membership test — predict:

d = {"id": 1234, "name": "Snehith", "age": 22}

# print("id" in d)      # prediction:
# print(1234 in d)      # prediction:   ← value, not key!
# print("city" in d)    # prediction:
# print("age" not in d) # prediction:


# Q16. Predict the output of each method:

d = {"id": 1234, "name": "Snehith", "age": 22}

# print(d.keys())    # prediction:
# print(d.values())  # prediction:
# print(d.items())   # prediction:
# print(len(d))      # prediction:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Given two lists: names = ["Alice", "Bob", "Charlie"]
#                  scores = [85, 92, 78]
# Create a dictionary mapping name → score.
# Then print: each name and their score on a separate line.

# YOUR CODE HERE:


# BONUS 2:
# Deduplicate a list WITHOUT using set() directly:
# Use a loop to build a new list with no duplicates.
# nums = [1, 2, 3, 2, 4, 3, 5, 1, 6, 5]

nums = [1, 2, 3, 2, 4, 3, 5, 1, 6, 5]
# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

A = {1, 2, 3}
B = {2, 3, 4}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)

d = {"x": 10, "y": 20}
d["z"] = 30
print(len(d))
print(d.get("w", 0))
print("x" in d)
print(10 in d)

# Your full prediction:


# BONUS 4:
# Using a dictionary, count how many times each character appears
# in the string "mississippi"
# Expected: {'m': 1, 'i': 4, 's': 4, 'p': 2}

word = "mississippi"
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: dict, set, {1,2,3} (dups removed), {1,3,4,5} (unordered, dups removed)

# Q4:
# After discard(10): {20, 30, 40}
# After discard(100): {20, 30, 40}  — silent, no error
# After remove(20): {30, 40}
# remove(100) → KeyError: 100

# Q6:
# A | B = {1,2,3,4,5,6,7,8}
# A & B = {4,5}
# A - B = {1,2,3}
# B - A = {6,7,8}
# A ^ B = {1,2,3,6,7,8}

# Q7: union() does NOT change A. result has all unique values. A is unchanged.

# Q10: d["city"] → KeyError; d.get("city") → None; d.get("city","N/A") → "N/A"

# Q14: val=2, d={'a':1,'c':3,'d':4}; last=('d',4), d={'a':1,'c':3}

# Q15: True, False (1234 is value not key), False, False

# BONUS 3: {1,2,3,4}, {2,3}, {1}, {1,4}; 3, 0, True, False
