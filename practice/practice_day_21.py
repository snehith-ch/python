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
