# Day 43 — Pandas and Matplotlib (Part 1)

← [Day 42](day_42_assertion_logging.md) | [Index](00_INDEX.md) | [Day 44](day_44_pandas_matplotlib_part2.md) →

---

## Quick Revision — Day 43

| # | Key Point |
|---|-----------|
| 1 | **Pandas** = Python Data Analysis (originally "Panel Data") |
| 2 | **Matplotlib** = Mathematical Plot Library — for data visualization |
| 3 | Both modules are built on top of **NumPy** (Numerical Python) |
| 4 | Install: PyCharm → File → Settings → Python Interpreter → `+` → search pandas/matplotlib |
| 5 | `import pandas as pd` — `pd` is the standard alias |
| 6 | **Series** = single dimension array representation — `pd.Series()` |
| 7 | **DataFrame** = two dimension array (rows and columns) — `pd.DataFrame()` |
| 8 | Data input can be in ANY format: list, tuple, dict, NumPy array |
| 9 | `df.head(n)` — first n records; `df.tail(n)` — last n records |
| 10 | `pd.read_csv("file.csv")` reads CSV; `.to_html("file.html")` converts to HTML |

---

## Navigation

- **Pre-requisite:** [Day 42](day_42_assertion_logging.md) — Assertion and Logging; [Day 35](day_35_zip_csv_files.md) — CSV files
- **Next:** [Day 44](day_44_pandas_matplotlib_part2.md) — Matplotlib graphs continuation
- **Related:** [Day 38](day_38_database_mssql.md) — Database (Pandas also reads database data)

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| Module | `pandas` | Python Data Analysis module |
| Module | `matplotlib` | Mathematical Plot Library |
| Alias | `import pandas as pd` | Standard alias for pandas |
| Function | `pd.Series()` | Create single-dimension array (Series) |
| Function | `pd.DataFrame()` | Create two-dimension array (DataFrame) |
| Method | `df.head(n)` | Get first n rows |
| Method | `df.tail(n)` | Get last n rows |
| Function | `pd.concat([df1, df2])` | Concatenate (join) two DataFrames |
| Method | `pd.read_csv("file.csv")` | Read CSV file into DataFrame |
| Method | `df.to_html("file.html")` | Convert DataFrame to HTML file |
| Import | `from matplotlib import pyplot as plt` | Import plotting module |
| Function | `plt.plot(x, y)` | Create a line plot |
| Function | `plt.show()` | Display the plot |

---

## 1. Overview — Pandas and Matplotlib

```
Pandas                          Matplotlib
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Python Data Analysis            Mathematical Plot Library
(Panel Data)                    Data Visualization

Creates:                        Creates:
  Series (1D array)               Line graphs
  DataFrame (2D array)            Bar charts
                                  Pie charts
Analyzes data in structured       Scatter plots
table format                      Stack plots

Both modules designed and developed on top of NUMPY
NumPy = Numerical Python (multi-dimensional array support)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> **Key rule:** You MUST pass your data as input (in list/tuple/dict/array format). Without data, neither Pandas nor Matplotlib can analyze or visualize anything.

---

## 2. Installation

```
PyCharm:
  File → Settings → Project → Python Interpreter → click + 
  → Search "pandas"      → Install Package
  → Search "matplotlib"  → Install Package
```

---

## 3. Pandas — Series (1D Array)

### 3.1 Empty Series

```python
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import pandas as pd

s = pd.Series()    # empty series
print(s)           # Empty, dtype: object
```

### 3.2 Series from NumPy Array

```python
import numpy as np
import pandas as pd

a = np.array(['a', 'b', 'c', 'd'])    # character array

s = pd.Series(a)    # pass array to Series
print(s)
```

**Output:**
```
0    a
1    b
2    c
3    d
dtype: object
```

Default index starts from 0. Provide custom index with `index=`:

```python
s = pd.Series(a, index=[1, 2, 3, 4])    # custom index: 1-based
print(s)
```

### 3.3 Series from List

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
print(s)           # index 0-4

# Custom index
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# Access by index
print(s['a'])      # 10
print(s['c'])      # 30

# Slicing
print(s[1:4])      # index 1, 2, 3
```

### 3.4 Series from Dictionary

```python
import pandas as pd

data = {
    'emp_id':      [1, 2, 3, 4],
    'emp_name':    ['Sita', 'Ravi', 'Ali', 'Mohan'],
    'emp_address': ['HYD', 'Delhi', 'Mumbai', 'Pune']
}

s = pd.Series(data)
print(s)
```

**Output:**
```
emp_id          [1, 2, 3, 4]
emp_name      [Sita, Ravi, Ali, Mohan]
emp_address   [HYD, Delhi, Mumbai, Pune]
dtype: object
```

> When a key from the custom index is **not found** in the dictionary, Pandas shows `NaN` (Not a Number).

---

## 4. Pandas — DataFrame (2D Array)

### 4.1 Empty DataFrame

```python
import pandas as pd

df = pd.DataFrame()    # empty DataFrame
print(df)              # Empty DataFrame, Columns: [], Index: []
```

### 4.2 DataFrame from Nested List

```python
import pandas as pd

data = [
    ['Sita', 45],
    ['Durga', 32],
    ['Mohan', 30],
    ['Ravi', 46]
]

df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
```

**Output:**
```
    Name  Age
0   Sita   45
1  Durga   32
2  Mohan   30
3   Ravi   46
```

With custom row indexes:

```python
df = pd.DataFrame(data, columns=['Name', 'Age'],
                  index=['row1', 'row2', 'row3', 'row4'])
```

### 4.3 DataFrame from Dictionary

```python
import pandas as pd

data = {
    'Name':    ['Sita', 'Mohan', 'Ravi', 'Ali'],
    'Age':     [22, 38, 34, 43],
    'Address': ['HYD', 'Delhi', 'Pune', 'Mumbai']
}

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
    Name  Age Address
0   Sita   22     HYD
1  Mohan   38   Delhi
2   Ravi   34    Pune
3    Ali   43  Mumbai
```

> Dictionary keys become column names automatically. All value lists must have the **same length**, otherwise ValueError is raised.

### 4.4 head() and tail()

```python
print(df.head(2))     # first 2 records
print(df.tail(1))     # last 1 record
print(df.head())      # default: first 5 records
print(df.tail())      # default: last 5 records
```

---

## 5. Concatenating DataFrames

```python
import pandas as pd

df1 = pd.DataFrame(
    {'Name': ['Sita', 'Mohan', 'Durga'], 'Age': [22, 38, 45]},
    index=[0, 1, 2]
)

df2 = pd.DataFrame(
    {'Name': ['Ravi', 'Ali'], 'Age': [34, 43]},
    index=[3, 4]
)

# Combine two DataFrames into one
df3 = pd.concat([df1, df2])
print(df3)
```

**Output:**
```
    Name  Age
0   Sita   22
1  Mohan   38
2  Durga   45
3   Ravi   34
4    Ali   43
```

---

## 6. Reading CSV and Converting to HTML

```python
import pandas as pd

# Read CSV file into DataFrame
f = pd.read_csv("D:/Python project at 7AM/emp.csv")

# Convert to HTML file
f.to_html("emp.html")
print("CSV converted to HTML successfully")
```

> After running, open `emp.html` in a browser — the CSV data appears as a styled HTML table. Pandas also supports `.to_excel()`, `.to_json()`, `.to_csv()` and many other conversions.

---

## 7. Matplotlib — Basic Line Plot

```python
from matplotlib import pyplot as plt

# Input data
x = [5, 1, 3, 4, 7]
y = [10, 5, 7, 6, 9]

# Create and display plot
plt.plot(x, y)
plt.show()
```

### 7.1 With Labels and Title

```python
from matplotlib import pyplot as plt

x = [5, 1, 3, 4, 7]
y = [10, 5, 7, 6, 9]

plt.plot(x, y)
plt.title("Simple Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
```

### 7.2 With Marker

```python
plt.plot(x, y, marker='o')    # 'o' = circle marker at each data point
plt.show()
```

> Adding `marker='o'` puts a visible dot at each coordinate — makes it easy to identify exact data points on the graph.

---

## 8. Matplotlib — Two Line Graphs

```python
from matplotlib import pyplot as plt

x1 = [5, 8, 10, 9, 10]
y1 = [12, 16, 6, 7, 11]

x2 = [6, 9, 11, 15, 7]
y2 = [2, 3, 4, 5, 7]

plt.plot(x1, y1)    # first line
plt.plot(x2, y2)    # second line

plt.title("Simple Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
```

Default colors: first line = blue, second line = orange.

---

## 9. Bar Graph

```python
from matplotlib import pyplot as plt

plt.bar([1, 3, 5, 7, 9], [5, 7, 8, 2, 3], label="Bar 1")
plt.bar([2, 4, 6, 8],    [6, 7, 8, 2],    label="Bar 2")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Bar Graph")
plt.legend()
plt.show()
```

---

## 10. Scatter Plot

```python
from matplotlib import pyplot as plt

x = [3, 7, 2, 3, 8, 9]
y = [5, 8, 9, 5, 6, 3]

plt.scatter(x, y,
            color='red',
            s=90,           # size of scatter points
            marker='*')     # marker style: star

plt.title("Scatter Plot")
plt.show()
```

---

## 11. Series vs DataFrame — Key Differences

| Feature | Series | DataFrame |
|---------|--------|-----------|
| Dimensions | 1D (single column) | 2D (rows + columns) |
| Function | `pd.Series()` | `pd.DataFrame()` |
| Index | Auto 0, 1, 2... | Auto 0, 1, 2... (row index) |
| Columns | None (single column) | Multiple named columns |
| Analogy | Single array | Table / spreadsheet |

---

## Student Q&A

> **Student Question:** What is Pandas and what is it used for?
> **Answer:** Pandas stands for Python Data Analysis (originally "Panel Data"). It is a Python library used for analyzing and representing data in structured formats. It provides two main data structures: Series (single-dimension array) and DataFrame (two-dimension array — rows and columns). You pass your data in any format (list, dict, array), and Pandas arranges it in structured form. Both Pandas and Matplotlib are built on NumPy (Numerical Python).

> **Student Question:** What is the difference between Series and DataFrame?
> **Answer:** A Series is a single-dimension array — like one column of data with an index. A DataFrame is a two-dimension structure — like a table with rows and columns. Use `pd.Series()` for Series and `pd.DataFrame()` for DataFrames. DataFrames are more commonly used as they can hold multiple columns (like a CSV or database table).

> **Student Question:** Does it matter what format the data is in when passing to Pandas?
> **Answer:** No — you can pass data in any Python data structure: list, tuple, dictionary, NumPy array, set, or any format. Pandas will arrange it into the appropriate Series or DataFrame structure. The most common format is dictionary for DataFrames (keys become column names) and list/array for Series.

> **Student Question:** What is Matplotlib used for?
> **Answer:** Matplotlib (Mathematical Plot Library) is used for data visualization. When you have large amounts of data in table format, it can be hard to analyze just by reading. Matplotlib lets you represent the same data as line graphs, bar charts, scatter plots, pie charts, and stack plots — making patterns and trends immediately visible. You must supply coordinate values (X and Y) as input, and Matplotlib creates the visual diagram.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: No module named 'pandas'` | Pandas not installed | PyCharm: Settings → Python Interpreter → + → install pandas |
| `ValueError: arrays must all be same length` | DataFrame columns have different lengths | Make sure all list values in the dict have the same number of elements |
| `KeyError: 'column_name'` | Accessing a non-existent column | Check column names with `df.columns` |
| FutureWarning on empty Series | Default dtype changed in future versions | Add `import warnings; warnings.filterwarnings("ignore", category=FutureWarning)` |
| Graph not displaying | Forgot `plt.show()` | Always call `plt.show()` at the end |

---

## Interview Questions

**Q: What is Pandas in Python?**
A: Pandas (Python Data Analysis) is a third-party library used for data analysis and data manipulation. It provides two main data structures: Series (single-dimension) and DataFrame (two-dimension, like a table). Data can be input in any Python format (list, dict, array). Pandas is commonly used in data science and data analysis workflows. It is built on top of NumPy.

**Q: What is the difference between a Series and a DataFrame in Pandas?**
A: A Series is a single-dimensional array-like structure with an index — like one column of data. A DataFrame is a two-dimensional structure with rows and columns — like a spreadsheet or database table. `pd.Series()` creates a Series; `pd.DataFrame()` creates a DataFrame. DataFrames support multiple columns, head/tail functions, concatenation, and direct CSV/Excel I/O.

**Q: What is Matplotlib and what types of plots can it create?**
A: Matplotlib (Mathematical Plot Library) is a Python library for data visualization. It can create: line graphs (`plt.plot()`), bar charts (`plt.bar()`), scatter plots (`plt.scatter()`), pie charts (`plt.pie()`), stack plots (`plt.stackplot()`), and histograms. You supply X and Y coordinate values and call `plt.show()` to display the diagram. It is built on NumPy.

---

## Try It Yourself

**Exercise 1:** Create a Pandas DataFrame from a dictionary with three columns: `Student`, `Subject`, `Marks`. Add 4 records and print the first 2 and last 1 records using `head()` and `tail()`.

<details><summary>Answer</summary>

```python
import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Subject': ['Math', 'Science', 'English', 'Math'],
    'Marks':   [90, 85, 78, 92]
}

df = pd.DataFrame(data)
print(df.head(2))    # first 2
print(df.tail(1))    # last 1
```
</details>

---

**Exercise 2:** Create a Matplotlib line graph showing monthly sales data. X axis = months (1–6), Y axis = sales values. Add title, X label, Y label.

<details><summary>Answer</summary>

```python
from matplotlib import pyplot as plt

months = [1, 2, 3, 4, 5, 6]
sales  = [4000, 4500, 3800, 5200, 4900, 5600]

plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales (Rs)")
plt.show()
```
</details>
