# ============================================================
# PRACTICE — Day 43: Pandas and Matplotlib (Part 1)
# ============================================================
# Instructions:
#   - Requires: pip install pandas matplotlib numpy
#   - Predict the output BEFORE running each code block
# ============================================================

import warnings
warnings.filterwarnings("ignore")


# --------------------------------------------------
# SECTION 1: Pandas — Series
# --------------------------------------------------

# Q1. Predict the output — Series from a list:

import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
print(s)             # prediction (with index):
print(type(s))       # prediction:
print(s.dtype)       # prediction:


# Q2. Series with custom index — predict:

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)             # prediction:
print(s['b'])        # prediction:
print(s[1])          # prediction (positional still works):


# Q3. Series from NumPy array — predict:

import numpy as np

arr = np.array([100, 200, 300, 400])
s = pd.Series(arr)

print(s)              # prediction:
print(s[2])           # prediction:


# Q4. Series from dictionary — predict:

data = {'Math': 90, 'Science': 85, 'English': 78}
s = pd.Series(data)

print(s)              # prediction (keys become index):
print(s['Science'])   # prediction:
print(s.sum())        # prediction:
print(s.mean())       # prediction (approximate):


# Q5. NaN for missing keys — predict:

data = {'a': 10, 'c': 30}
s = pd.Series(data, index=['a', 'b', 'c'])
print(s)    # prediction ('b' not in dict → ?):


# Q6. Series slicing — predict:

s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s[1:4])    # prediction (positional slice):
print(s['b':'d'])  # prediction (label slice — inclusive!):


# --------------------------------------------------
# SECTION 2: Pandas — DataFrame
# --------------------------------------------------

# Q7. DataFrame from nested list — predict:

data = [
    ['Alice', 25, 'HYD'],
    ['Bob', 30, 'Delhi'],
    ['Charlie', 22, 'Pune']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)         # prediction:
print(df.shape)   # prediction (rows, cols):


# Q8. DataFrame from dictionary — predict:

data = {
    'Name':   ['Sita', 'Ravi', 'Ali'],
    'Salary': [50000, 45000, 60000],
    'City':   ['HYD', 'Delhi', 'Mumbai']
}

df = pd.DataFrame(data)
print(df)             # prediction:
print(df.columns)     # prediction (column names):
print(df['Name'])     # prediction (single column — a Series):


# Q9. head() and tail() — predict:

data = {'x': range(10), 'y': range(10, 20)}
df = pd.DataFrame(data)

print(df.head(3))    # prediction (first 3 rows):
print(df.tail(2))    # prediction (last 2 rows):


# Q10. DataFrame indexing — predict:

df = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Val':  [10, 20, 30, 40]
})

print(df.iloc[0])    # prediction (first row by position):
print(df.iloc[2])    # prediction:
print(df['Val'][1])  # prediction (column 'Val', row index 1):


# --------------------------------------------------
# SECTION 3: DataFrame Operations
# --------------------------------------------------

# Q11. Concatenation — predict:

df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
df2 = pd.DataFrame({'Name': ['Charlie', 'Dave'], 'Age': [22, 28]})

df3 = pd.concat([df1, df2])
print(df3)             # prediction:
print(len(df3))        # prediction:
print(df3.shape)       # prediction:


# --------------------------------------------------
# SECTION 4: Matplotlib — Line Graph
# --------------------------------------------------

# Q12. Basic line plot — run and observe (no prediction for visual output):

import matplotlib
matplotlib.use('Agg')    # non-interactive backend for practice
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 6]

plt.figure()
plt.plot(x, y)
plt.title("My First Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig("practice_plot_43_q12.png")
plt.close()
print("Line graph saved")    # prediction:


# Q13. Bar chart — predict what it visualizes:

categories = ['A', 'B', 'C', 'D']
values = [15, 8, 22, 11]

plt.figure()
plt.bar(categories, values, color='blue')
plt.title("Bar Chart")
plt.savefig("practice_plot_43_q13.png")
plt.close()
print("Bar chart saved")


# Q14. Scatter plot — predict:

x = [1, 3, 5, 7, 9]
y = [2, 8, 4, 9, 3]

plt.figure()
plt.scatter(x, y, color='red', s=100, marker='o')
plt.title("Scatter Plot")
plt.savefig("practice_plot_43_q14.png")
plt.close()
print("Scatter plot saved")


# --------------------------------------------------
# SECTION 5: Write Code
# --------------------------------------------------

# Q15. Create a DataFrame for 4 students:
#   Columns: Name, Marks (out of 100), Grade (A/B/C)
#   a) Print the DataFrame
#   b) Print the average marks
#   c) Print the student(s) with Grade 'A'

# YOUR CODE HERE:


# Q16. Create a line graph of y = x^2 for x from -5 to 5.
#   Add title "Square Function" and axis labels.
#   Save as "square_plot.png"

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — what is the difference?

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(df['A'])       # prediction (Series or DataFrame?):
print(type(df['A'])) # prediction:

print(df[['A']])     # prediction (single-column DataFrame!):
print(type(df[['A']])) # prediction:


# BONUS 2: Predict — concat with ignore_index:

df1 = pd.DataFrame({'val': [1, 2]})
df2 = pd.DataFrame({'val': [3, 4]})

# Without ignore_index — what are the row indices?
result = pd.concat([df1, df2])
print(result.index.tolist())    # prediction:

# With ignore_index — resets indices
result2 = pd.concat([df1, df2], ignore_index=True)
print(result2.index.tolist())   # prediction:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: Series with 0-4 index, dtype int64; <class 'pandas.core.series.Series'>

# Q2: a=10, b=20, c=30 with custom index; s['b']=20; s[1]=20

# Q3: 0=100, 1=200, 2=300, 3=400; s[2]=300

# Q4: Math=90, Science=85, English=78; s['Science']=85; sum=253; mean≈84.3

# Q5: a=10.0, b=NaN, c=30.0 (NaN for missing key 'b')

# Q6: s[1:4] → b=20, c=30, d=40 (positional, exclusive end)
#     s['b':'d'] → b=20, c=30, d=40 (label, INCLUSIVE end)

# Q7: 3 rows, 3 cols table; shape=(3, 3)

# Q8: 3 rows with Name/Salary/City; columns=Index(['Name','Salary','City']); Name is a Series

# Q9: head(3)=rows 0,1,2; tail(2)=rows 8,9

# Q10: first row (index 0); third row (index 2); 20

# Q11: 4 rows with original indices [0,1,0,1]; length=4; shape=(4,2)

# Q12-Q14: "saved" messages (visual output in PNG files)

# BONUS 1: df['A'] → Series; df[['A']] → DataFrame (extra brackets = DataFrame)

# BONUS 2: [0, 1, 0, 1] (original indices preserved), [0, 1, 2, 3] (reset)
