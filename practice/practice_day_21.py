# ============================================================
# PRACTICE — Day 21: Arrays and NumPy
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: array MODULE (built-in)
# --------------------------------------------------

# Q1. Predict the output:

from array import array

a = array('i', [10, 20, 30, 40, 50])

print(type(a))        # prediction:
print(len(a))         # prediction:
print(a[0])           # prediction:
print(a[-1])          # prediction:
print(a[1:4])         # prediction (what type is the slice?):


# Q2. Predict the output of array operations:

a.insert(2, 99)
print(a)              # prediction: where is 99?

a.remove(99)
print(a)              # prediction:

a.reverse()
print(a)              # prediction:


# Q3. Type code matters — predict the error:

# a2 = array('i', [1.5, 2.5, 3.5])   # 'i' is integer type code
# uncomment → prediction (error type?):


# Q4. Write code:
# Create an array of floats ('f') with values [1.1, 2.2, 3.3, 4.4].
# Print each element using a for loop.

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 2: NumPy — 1D Arrays
# --------------------------------------------------

# Q5. Predict the output:

import numpy as np

a1 = np.array([1, 2, 3, 4, 5])

print(type(a1))       # prediction:
print(a1)             # prediction:
print(a1.dtype)       # prediction (data type):
print(a1.size)        # prediction:
print(a1.ndim)        # prediction (dimensions):
print(a1.shape)       # prediction (format):


# Q6. NumPy arithmetic — predict each line:

a = np.array([10, 20, 30, 40])

print(a + 5)          # prediction:
print(a * 2)          # prediction:
print(a ** 2)         # prediction:
print(a / 10)         # prediction:


# Q7. arange and linspace — predict:

print(np.arange(0, 10, 2))     # prediction (step=2):
print(np.linspace(0, 1, 5))    # prediction (5 evenly spaced between 0 and 1):
print(np.zeros(4))             # prediction:
print(np.ones(3))              # prediction:


# --------------------------------------------------
# SECTION 3: NumPy — 2D Arrays
# --------------------------------------------------

# Q8. Predict the output:

a2 = np.array([[1, 2, 3],
               [4, 5, 6]])

print(a2)             # prediction:
print(a2.shape)       # prediction: (rows, columns)?
print(a2.ndim)        # prediction:
print(a2.size)        # prediction (total elements):


# Q9. Indexing and slicing 2D arrays — predict:

print(a2[0])          # prediction: first row
print(a2[1])          # prediction: second row
print(a2[0][1])       # prediction: element at row 0, col 1
print(a2[1][2])       # prediction: element at row 1, col 2


# Q10. Operations on 2D — predict:

print(a2 + 10)        # prediction: element-wise
print(a2 * 2)         # prediction:


# Q11. flatten() — predict:

print(a2.flatten())   # prediction (converts 2D to 1D):


# Q12. axis operations — predict:

print(a2.sum(axis=0))    # prediction: sum each COLUMN
print(a2.sum(axis=1))    # prediction: sum each ROW
print(a2.max(axis=0))    # prediction: max of each column
print(a2.max(axis=1))    # prediction: max of each row


# --------------------------------------------------
# SECTION 4: array vs NumPy Comparison
# --------------------------------------------------

# Q13. Fill in the blanks — predict:

# from array import array
# a = array('i', [1, 2, 3])
# print(a + a)       # prediction: works or error?

import numpy as np
n = np.array([1, 2, 3])
# print(n + n)       # prediction: works or error? what output?


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Create a 3x3 identity matrix using NumPy (np.eye(3)).
# Print it and predict the output.

# YOUR CODE HERE:


# BONUS 2:
# Create a NumPy array of 10 elements from 1 to 100 evenly spaced.
# Print the array, its mean, and its sum.

# YOUR CODE HERE:


# BONUS 3: Predict ALL output before running:

import numpy as np

a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(a.max())     # prediction:
print(a.min())     # prediction:
print(a.mean())    # prediction:
print(a.sum())     # prediction:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. The main difference between a Python list and an array (array module):
#    A) List can have one type; array can have multiple
#    B) Array stores one data type; list can store any types
#    C) Array is faster for string operations
#    D) They are identical in every way
# Answer: ___

# Q_MCQ_2. np.zeros((2, 3))  creates:
#    A) A 2D array with 2 rows and 3 columns of zeros
#    B) A 1D array of 6 zeros
#    C) An array from 0 to 2 with step 3
#    D) Error — zeros() takes only one argument
# Answer: ___

# Q_MCQ_3. np.arange(1, 10, 2)  produces:
#    A) [1,3,5,7,9]    B) [1,2,...,10]    C) [2,4,6,8,10]    D) [1,10,2]
# Answer: ___

# Q_MCQ_4. arr = np.array([[1,2],[3,4]]); arr.shape  returns:
#    A) 4    B) (2, 2)    C) [2, 2]    D) (4,)
# Answer: ___

# Q_MCQ_5. np.array([1,2,3]) * 2  returns:
#    A) [1,2,3,1,2,3]    B) [2,4,6]    C) 12    D) Error
# Answer: ___

# Q_MCQ_6. arr[1, 2]  in a 2D NumPy array accesses:
#    A) Row 2, Column 3    B) Row 1, Column 2
#    C) Row 2, Column 1    D) Element at flat index 5
# Answer: ___

# Q_MCQ_7. np.array([1, 2, 3]).dtype  for integer input returns:
#    A) 'int'    B) 'int64' (or int32 depending on system)
#    C) 'float64'    D) 'object'
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. np.arange(0, 10, 3) = _______.

# FIB_2. np.zeros((3,4)).shape = _______  and .size = _______.

# FIB_3. arr.ndim  for a 2D array returns _______.

# FIB_4. arr.sum(axis=0) computes sum _______, axis=1 computes sum _______.

# FIB_5. array('d', [1.5, 2.5]) stores _______ floats (type code 'd' = double).

# FIB_6. arr.reshape(2, 6)  changes a (3,4) array to _______ — total elements must be _______.

# FIB_7. arr[arr > 5]  is called _______ indexing in NumPy.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Student Marks Analyzer using NumPy — batch statistics.
#
# Requirements:
#   1. Create a 5×4 array (5 students, 4 subjects) using:
#      np.random.seed(42); marks = np.random.randint(40, 100, (5, 4))
#   2. Print: shape, size, ndim, dtype
#   3. Row-wise total (sum per student) using axis=1
#   4. Column-wise average (avg per subject) using axis=0  
#   5. Overall highest and lowest mark
#   6. Boolean indexing: find all marks ≥ 80 (print as a flat array)
#   7. Count how many marks are below 60 (failing)
#   8. Reshape the 5×4 array to 4×5 — print new shape
#   9. Print a nicely formatted report table
#      Subjects: Math, Science, English, History
#
# Expected output (partial, values depend on seed):
#   Marks Array (5 students × 4 subjects):
#   [[...]]
#   Shape: (5,4)  Size: 20  Dimensions: 2
#   Student totals: [...]
#   Subject averages: [...]
#   Highest: 99  Lowest: 41
#   Marks ≥ 80: [...]
#   Failing (<60): X students
#   Reshaped to (4,5): shape = (4, 5)

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: <class 'array.array'>, 5, 10, 50, array('i', [20, 30, 40])

# Q2: array('i', [10, 20, 99, 30, 40, 50]) — inserted at index 2
#     array('i', [10, 20, 30, 40, 50]) — removed 99
#     array('i', [50, 40, 30, 20, 10]) — reversed

# Q3: OverflowError — 'i' type code only accepts integers

# Q5: <class 'numpy.ndarray'>, [1 2 3 4 5], int64, 5, 1, (5,)

# Q6: [15 25 35 45], [20 40 60 80], [100 400 900 1600], [1. 2. 3. 4.]

# Q7: [0 2 4 6 8], [0. 0.25 0.5 0.75 1.], [0. 0. 0. 0.], [1. 1. 1.]

# Q8: [[1 2 3][4 5 6]], (2, 3), 2, 6

# Q9: [1 2 3], [4 5 6], 2, 6

# Q10: [[11 12 13][14 15 16]], [[2 4 6][8 10 12]]

# Q11: [1 2 3 4 5 6]

# Q12: sum axis=0: [5 7 9] (column sums), sum axis=1: [6 15] (row sums)
#       max axis=0: [4 5 6], max axis=1: [3 6]

# Q13: array + array → ERROR (array module doesn't support +)
#       np array + np array → [2 4 6] (element-wise)

# BONUS 3: 9, 1, 3.875, 31


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: A   Q_MCQ_3: A   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: [0, 3, 6, 9]
# FIB_2: (3,4);  12
# FIB_3: 2
# FIB_4: column-wise (for each column);  row-wise (for each row)
# FIB_5: double-precision (64-bit)
# FIB_6: (2,6);  equal (12 in both)
# FIB_7: boolean

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import numpy as np
# np.random.seed(42)
# marks = np.random.randint(40, 100, (5, 4))
# subjects = ["Math","Science","English","History"]
# names    = ["Alice","Bob","Priya","Raj","Meena"]
# print("Marks Array (5 students × 4 subjects):")
# print(marks)
# print(f"Shape: {marks.shape}  Size: {marks.size}  Dimensions: {marks.ndim}  Dtype: {marks.dtype}")
# totals  = marks.sum(axis=1)
# avgs    = marks.mean(axis=0)
# print(f"Student totals: {totals}")
# print(f"Subject averages: {avgs.round(1)}")
# print(f"Highest: {marks.max()}  Lowest: {marks.min()}")
# print(f"Marks ≥ 80: {marks[marks >= 80]}")
# failing = (marks < 60).sum()
# print(f"Failing (<60): {failing} marks")
# print(f"Reshaped to (4,5): shape = {marks.reshape(4,5).shape}")

