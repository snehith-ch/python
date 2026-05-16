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
