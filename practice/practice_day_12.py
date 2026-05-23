# ============================================================
# PRACTICE — Day 12: Lists (Complete) & Tuple
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: sort()
# --------------------------------------------------

# Q1. Predict the output:

L = [5, 3, 8, 1, 9, 2, 7, 4, 6]

L.sort()
print(L)

L.sort(reverse=True)
print(L)

# Prediction after sort():
# Prediction after sort(reverse=True):


# Q2. FIX THE BUG — what is wrong here?

# L = [3, 1, 4]
# L = L.sort()    # bug!
# print(L)        # what is printed? why?

# YOUR EXPLANATION:
# YOUR FIX:


# Q3. Sort the list WITHOUT modifying the original:
#     (Hint: make a copy first, then sort the copy)

original = [5, 3, 8, 1, 9]
# YOUR CODE HERE — print both original and sorted version:


# --------------------------------------------------
# SECTION 2: Shallow vs Deep Copy
# --------------------------------------------------

# Q4. Predict the output — trace carefully:

L  = [1, 2, 3, 4, 5]
L1 = L           # shallow copy

L.remove(3)
print(L)         # prediction:
print(L1)        # prediction:

L1.append(99)
print(L)         # prediction:
print(L1)        # prediction:


# Q5. Now use deep copy — predict again:

L  = [1, 2, 3, 4, 5]
L1 = L.copy()    # deep copy

L.remove(3)
print(L)         # prediction:
print(L1)        # prediction:

L1.append(99)
print(L)         # prediction:
print(L1)        # prediction:


# Q6. Explain in 1 sentence each:
# What is a shallow copy?
# YOUR ANSWER:

# What is a deep copy?
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 3: count() and index()
# --------------------------------------------------

# Q7. Predict the output:

L = [10, 20, 30, 10, 40, 10, 20]

# print(L.count(10))   # prediction:
# print(L.count(20))   # prediction:
# print(L.count(99))   # prediction:   ← not present
# print(L.index(20))   # prediction:   ← first occurrence only
# print(L.index(30))   # prediction:


# Q8. What error does this cause?

# L = [10, 20, 30]
# print(L.index(99))   # prediction (what error?):


# --------------------------------------------------
# SECTION 4: Create List from User Input
# --------------------------------------------------

# Q9. Write a program that:
#     - Asks user how many items they want
#     - Accepts that many items in a loop
#     - Prints the final list (OUTSIDE the loop)

# YOUR CODE HERE:


# Q10. Predict the output difference when print is INSIDE vs OUTSIDE the loop:
#      (Trace manually for n=3, items = 10, 20, 30)
#
# # Version A — print INSIDE loop:
# L = []
# for i in range(3):
#     x = input("Value: ")
#     L.append(x)
#     print(L)       ← inside!
#
# # Version B — print OUTSIDE loop:
# L = []
# for i in range(3):
#     x = input("Value: ")
#     L.append(x)
# print(L)            ← outside!

# Version A output (per iteration):
# Version B output:


# --------------------------------------------------
# SECTION 5: Create List from range()
# --------------------------------------------------

# Q11. Predict the output:

# print(list(range(10)))          # prediction:
# print(list(range(5, 15)))       # prediction:
# print(list(range(0, 20, 4)))    # prediction:
# print(list(range(10, 0, -2)))   # prediction:


# --------------------------------------------------
# SECTION 6: TUPLE
# --------------------------------------------------

# Q12. Predict the type of each:

a = (10)
b = (10,)
c = ()
d = 10, 20, 30
e = (10, 20)

# print(type(a))   # prediction:
# print(type(b))   # prediction:
# print(type(c))   # prediction:
# print(type(d))   # prediction:
# print(type(e))   # prediction:


# Q13. Predict the output:

t = ("a", 10, True, 3.14, "b", None, 20)

# print(t[0])      # prediction:
# print(t[-1])     # prediction:
# print(t[2:5])    # prediction:
# print(t[::-1])   # prediction:


# Q14. FIX THE BUG:

# t = (1, 2, 3)
# t[0] = 99   # what error?
# print(t)

# YOUR EXPLANATION:
# Can you delete the whole tuple? Write the code:


# Q15. Predict the output:

t1 = (10, 20)
t2 = ("a", "b")

# print(t1 + t2)    # prediction:
# print(t1 * 3)     # prediction:
# print(len(t1))    # prediction:


# Q16. Tuple packing and unpacking — predict:

a = 100
b = 200
c = 300
t = a, b, c

print(t)          # prediction:
print(type(t))    # prediction:

x, y, z = t
print(x, y, z)    # prediction:


# Q17. Convert between types — predict:

# print(tuple("Python"))         # prediction:
# print(tuple([1, 2, 3, 4]))     # prediction:
# print(list((10, 20, 30)))      # prediction:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Demonstrate the difference between shallow and deep copy with a clear example.
# Modify original list and show which copy is affected and which is not.

# YOUR CODE HERE:


# BONUS 2:
# t = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)
# Without converting to list, find:
# a) How many times does 1 appear?
# b) At what index is the first 9?
# c) What is the length?
# d) What is the sum?

t = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)
# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

L = [3, 1, 4, 1, 5, 9, 2, 6]
L1 = L
L2 = L.copy()

L.sort()
print(L)
print(L1)   # shallow — affected?
print(L2)   # deep — affected?

# Your full prediction:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. What does  [3,1,2].sort()  return?
#    A) [1,2,3]    B) None (sorts in-place)    C) [3,1,2]    D) Error
# Answer: ___

# Q_MCQ_2. How do you sort a list in DESCENDING order?
#    A) list.sort()               B) list.sort(reverse=True)
#    C) sorted(list, asc=False)   D) list.reverse()
# Answer: ___

# Q_MCQ_3. What is the difference between shallow copy and deep copy?
#    A) No difference — both copy everything
#    B) Shallow copies nested objects by reference; deep copy creates
#       completely independent copies including nested objects
#    C) Deep copy is slower but both behave the same
#    D) Shallow copy is for lists; deep copy is for dicts
# Answer: ___

# Q_MCQ_4. Which creates a list of squares: [0,1,4,9,16]?
#    A) [x**2 in range(5)]        B) [x**2 for x in range(5)]
#    C) list(x**2 for x in 5)     D) [x*x, range(5)]
# Answer: ___

# Q_MCQ_5. What does  tuple("abc")  produce?
#    A) ("abc",)    B) ('a','b','c')    C) Error    D) ["a","b","c"]
# Answer: ___

# Q_MCQ_6. Can you sort a tuple directly?
#    A) Yes, tuple.sort() works       B) No — tuples are immutable;
#       use sorted() which returns a new list
#    C) Yes with tuple.sorted()       D) No, you can never sort a tuple's content
# Answer: ___

# Q_MCQ_7. import copy; b = copy.copy(a)  — if  a = [[1,2],[3,4]]:
#           b[0][0] = 99.  What happens to  a[0][0]?
#    A) Stays 1          B) Becomes 99 — shallow copy shares inner lists
#    C) Raises TypeError D) a becomes None
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. sorted([5,2,8,1]) returns _______ and the original list is _______.

# FIB_2. list.sort() returns _______ (it modifies the list _______ ).

# FIB_3. To sort by length:  sorted(words, key=_______).

# FIB_4. copy.deepcopy() is imported from the _______ module.

# FIB_5. [x*2 for x in [1,2,3] if x > 1]  = _______.

# FIB_6. A tuple with ONE element looks like: (42,)  — the _______ is required.

# FIB_7. list(range(5)) = _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Student Grade Manager for a school system.
#
# Requirements:
#   1. Start with a list of (student_name, score) tuples (5 students)
#   2. Sort by score DESCENDING using sorted() with key=lambda — do NOT
#      modify the original list
#   3. Print the leaderboard (rank, name, score)
#   4. List comprehension: extract names of students who passed (score >= 50)
#   5. List comprehension: create "grade letter" list
#      (A≥90, B≥75, C≥60, else F)
#   6. Deep copy the sorted list; modify the copy's first student's score
#      to 0. Prove the original is unchanged.
#   7. Calculate and print: class average, highest, lowest
#
# Expected output:
#   === Leaderboard ===
#   1. Priya    : 95
#   2. Snehith  : 88
#   3. Aarav    : 74
#   4. Meena    : 61
#   5. Rohan    : 43
#   Passed: ['Priya', 'Snehith', 'Aarav', 'Meena']
#   Grades: ['A', 'B', 'C', 'C', 'F']
#   Average: 72.2 | Highest: 95 | Lowest: 43
#   (Deep copy modified — original first score still: 95)
#
# Hint: key=lambda x: x[1] extracts the score from each (name,score) tuple.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: [1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1]

# Q2: L.sort() returns None — don't assign. Fix: L.sort() on its own line.

# Q4:
# After L.remove(3): L = [1,2,4,5], L1 = [1,2,4,5]   (same object)
# After L1.append(99): L = [1,2,4,5,99], L1 = [1,2,4,5,99]

# Q5:
# After L.remove(3): L = [1,2,4,5], L1 = [1,2,3,4,5]  (independent)
# After L1.append(99): L = [1,2,4,5], L1 = [1,2,3,4,5,99]

# Q7: 3, 2, 0, 1, 2

# Q8: ValueError: 99 is not in list

# Q11:
# [0,1,2,3,4,5,6,7,8,9]
# [5,6,7,8,9,10,11,12,13,14]
# [0,4,8,12,16]
# [10,8,6,4,2]

# Q12: int, tuple, tuple, tuple, tuple

# Q13: 'a', 20, (True, 3.14, 'b'), (20, None, 'b', 3.14, True, 10, 'a')

# Q15: (10, 20, 'a', 'b'), (10,20,10,20,10,20), 2

# Q16: (100, 200, 300), tuple, 100 200 300

# Q17: ('P','y','t','h','o','n'), (1,2,3,4), [10,20,30]

# BONUS 3: L=[1,2,3,4,5,6,9]; L1=[1,2,3,4,5,6,9] (shallow, same object); L2=[3,1,4,1,5,9,2,6] (deep, unaffected)


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: [1,2,5,8];  unchanged
# FIB_2: None;  in-place
# FIB_3: key=len
# FIB_4: copy
# FIB_5: [4, 6]
# FIB_6: trailing comma
# FIB_7: [0, 1, 2, 3, 4]

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import copy
# students = [("Priya",95),("Snehith",88),("Aarav",74),("Meena",61),("Rohan",43)]
# ranked = sorted(students, key=lambda x: x[1], reverse=True)
# print("=== Leaderboard ===")
# for i,(name,score) in enumerate(ranked,1):
#     print(f"{i}. {name:<8}: {score}")
# passed = [n for n,s in ranked if s >= 50]
# print(f"Passed: {passed}")
# grade = lambda s: 'A' if s>=90 else 'B' if s>=75 else 'C' if s>=60 else 'F'
# grades = [grade(s) for _,s in ranked]
# print(f"Grades: {grades}")
# scores = [s for _,s in students]
# print(f"Average: {sum(scores)/len(scores):.1f} | Highest: {max(scores)} | Lowest: {min(scores)}")
# ranked_copy = copy.deepcopy(ranked)
# ranked_copy[0] = (ranked_copy[0][0], 0)
# print(f"(Deep copy modified — original first score still: {ranked[0][1]})")

