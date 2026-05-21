# Day 44 — Pandas and Matplotlib (Part 2)

← [Day 43](day_43_pandas_matplotlib_part1.md) | [Index](00_INDEX.md) →

---

## Quick Revision — Day 44

| # | Key Point |
|---|-----------|
| 1 | Line graph with two lines: call `plt.plot()` twice with different data |
| 2 | Color codes: `'g'`=green, `'b'`=blue, `'r'`=red, `'c'`=cyan, `'k'`=black, `'m'`=magenta, `'y'`=yellow |
| 3 | `linewidth=5` — controls line thickness; `label="name"` — name for legend |
| 4 | `plt.legend()` — displays color-coded legend showing which line is which |
| 5 | `plt.grid(True, color='yellow')` — adds horizontal/vertical grid lines |
| 6 | `plt.bar(x, y, color='g', label='name')` — bar chart |
| 7 | `plt.scatter(x, y, color='r', s=90, marker='*')` — scatter plot with style |
| 8 | `plt.stackplot(x, y1, y2, ..., colors=[], labels=[])` — stacked area chart |
| 9 | `plt.pie(slices, labels=[], colors=[], shadow=True, explode=(), startangle=90, autopct='%1.1f%%')` |
| 10 | `explode=(0.1, 0, 0, 0)` — pulls first slice outward to highlight it |

---

## Navigation

- **Pre-requisite:** [Day 43](day_43_pandas_matplotlib_part1.md) — Pandas and Matplotlib basics
- **This is the final session of the Python batch**
- **Next steps:** Django with REST API (new batch announced)

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| Plot | `plt.plot(x, y, color, linewidth, label)` | Styled line graph |
| Function | `plt.legend()` | Display legend for labeled plots |
| Function | `plt.grid(True, color='yellow')` | Add grid lines to graph |
| Plot | `plt.bar(x, y, color, label)` | Bar chart |
| Plot | `plt.scatter(x, y, color, s, marker)` | Scatter plot with style |
| Plot | `plt.stackplot(x, y1, y2, colors, labels)` | Stacked area chart |
| Plot | `plt.pie(slices, labels, colors, shadow, explode, startangle, autopct)` | Pie chart |
| Param | `explode=(0.1, 0, 0, 0)` | Highlight/pull out one pie slice |
| Param | `autopct='%1.1f%%'` | Show percentage labels on pie slices |

---

## 1. Styled Two-Line Graph

```python
from matplotlib import pyplot as plt

x1 = [5, 8, 10, 9, 10]
y1 = [12, 16, 6, 7, 11]

x2 = [6, 9, 11, 15, 7]
y2 = [2, 3, 4, 5, 7]

# Two lines with color, width, and label
plt.plot(x1, y1, 'g', linewidth=5, label='Line 1')    # green, thick
plt.plot(x2, y2, 'c', linewidth=5, label='Line 2')    # cyan, thick

plt.title("Simple Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()                              # show legend box
plt.grid(True, color='yellow')           # add yellow grid
plt.show()
```

---

## 2. Color Codes Reference

| Code | Color   | Code | Color   |
|------|---------|------|---------|
| `'g'` | Green  | `'b'` | Blue   |
| `'r'` | Red    | `'c'` | Cyan   |
| `'k'` | Black  | `'m'` | Magenta |
| `'y'` | Yellow |      |         |

---

## 3. Bar Graph

```python
from matplotlib import pyplot as plt

# Two bar sets (odd positions and even positions)
plt.bar([1, 3, 5, 7, 9], [5, 7, 8, 2, 3],
        color='b', label='Bar 1')

plt.bar([2, 4, 6, 8], [6, 7, 8, 2],
        color='g', label='Bar 2')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Bar Graph")
plt.legend()
plt.show()
```

> Bar height is determined by the Y values. Changing X positions controls where bars appear on the axis. Multiple `plt.bar()` calls create grouped bars.

---

## 4. Scatter Plot with Style

```python
from matplotlib import pyplot as plt

x = [3, 7, 2, 3, 8, 9]
y = [5, 8, 9, 5, 6, 3]

plt.scatter(x, y,
            color='red',    # point color
            s=90,           # point size
            marker='*')     # point shape: star

plt.title("Scatter Plot")
plt.show()
```

**Scatter plot marker options:**
```
'o' = circle     '*' = star      '^' = triangle up
's' = square     '+' = plus      'D' = diamond
```

---

## 5. Stack Plot

Stack plots show how multiple quantities change together over time, stacked on top of each other.

```python
from matplotlib import pyplot as plt

# X axis: 5 days
days = [1, 2, 3, 4, 5]

# Activities per day (in hours — should total 24 each day)
sleeping = [7, 8, 6, 7, 8]    # hours sleeping
eating   = [2, 3, 2, 3, 2]    # hours eating
working  = [7, 8, 9, 7, 8]    # hours working
playing  = [8, 5, 7, 7, 6]    # hours playing

colors = ['m', 'c', 'r', 'k']    # magenta, cyan, red, black
labels = ['sleeping', 'eating', 'working', 'playing']

plt.stackplot(days, sleeping, eating, working, playing,
              colors=colors, labels=labels)

plt.xlabel("Days")
plt.ylabel("Hours")
plt.title("Daily Activity Stack Plot")
plt.legend(loc='upper left')
plt.show()
```

**Each day's activities should sum to 24 hours:**
```
Day 1: 7+2+7+8 = 24  ✓
Day 2: 8+3+8+5 = 24  ✓
```

---

## 6. Pie Chart

Pie charts show proportional data — each slice represents a percentage of the whole.

### 6.1 Basic Pie Chart

```python
from matplotlib import pyplot as plt

slices  = [7, 2, 2, 13]                         # values (hours)
labels  = ['sleeping', 'eating', 'working', 'playing']
colors  = ['c', 'm', 'r', 'b']

plt.pie(slices, labels=labels, colors=colors,
        shadow=True, startangle=90,
        autopct='%1.1f%%')                       # show % on each slice

plt.title("Daily Activities")
plt.show()
```

**Output:** Pie divided into 4 slices with labels and percentage values.

### 6.2 explode — Highlighting a Slice

```python
from matplotlib import pyplot as plt

slices  = [7, 2, 2, 13]
labels  = ['sleeping', 'eating', 'working', 'playing']
colors  = ['c', 'm', 'r', 'b']
explode = (0, 0.1, 0, 0)    # pull out 2nd slice (eating) by 0.1

plt.pie(slices, labels=labels, colors=colors,
        shadow=True, startangle=90,
        autopct='%1.1f%%',
        explode=explode)

plt.show()
```

> `explode=(0, 0.1, 0, 0)` — pulls the second slice (eating) outward by 0.1 units, drawing audience attention to it. `0` means no separation.

### 6.3 Pie Chart Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `slices` | List of values (any numbers, will be % of total) | `[7, 2, 2, 13]` |
| `labels` | List of slice labels | `['A', 'B', 'C']` |
| `colors` | List of color codes | `['r', 'g', 'b']` |
| `shadow` | Add shadow behind pie | `True` |
| `startangle` | Rotate starting point of first slice | `90` |
| `autopct` | Show percentage inside each slice | `'%1.1f%%'` |
| `explode` | Offset for each slice (0=none) | `(0.1, 0, 0, 0)` |

---

## 7. Pandas — Additional Examples

### 7.1 Series from Nested Data with NaN

```python
import pandas as pd

data = {'a': 10, 'c': 20, 'd': 30}

# Custom index includes 'b' which is NOT in the dict
s = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(s)
```

**Output:**
```
a    10.0
b     NaN    ← 'b' not in dict → NaN (Not a Number)
c    20.0
d    30.0
dtype: float64
```

### 7.2 DataFrame with Multiple Operations

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

# Concatenate
df3 = pd.concat([df1, df2])
print(df3)
print(df3.head(2))    # first 2 rows
print(df3.tail(2))    # last 2 rows
```

---

## 8. All Matplotlib Plot Types — Summary

| Plot Type | Function | Use Case |
|-----------|----------|----------|
| Line graph | `plt.plot(x, y)` | Trends over time |
| Bar chart | `plt.bar(x, y)` | Compare categories |
| Scatter plot | `plt.scatter(x, y)` | Relationships between variables |
| Stack plot | `plt.stackplot(x, y1, y2, ...)` | Parts of a whole over time |
| Pie chart | `plt.pie(slices)` | Proportions/percentages |

---

## 9. Complete Graph Options Reference

```python
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 5, 6]

plt.plot(x, y,
         color='g',         # line color
         linewidth=3,       # line thickness
         linestyle='--',    # line style: '-', '--', '-.', ':'
         marker='o',        # marker at each point
         label='My Line')   # label for legend

plt.title("Graph Title")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.legend()               # show legend
plt.grid(True)             # show grid
plt.show()
```

---

## Student Q&A

> **Student Question:** What is `plt.legend()` and when do we use it?
> **Answer:** `plt.legend()` displays a legend box on the graph that shows which color/line corresponds to which label. You set labels using the `label="name"` parameter in `plt.plot()` or `plt.bar()`, and then call `plt.legend()` to display them. Without legend, when you have multiple lines or bars, you cannot identify which is which. It's especially important when two or more plots are drawn on the same axes.

> **Student Question:** What is the difference between a stack plot and a line graph?
> **Answer:** A line graph shows individual lines for each data series — you can see each line's value separately. A stack plot shows the same data stacked on top of each other, forming filled areas — you can see each component's contribution and the total at a glance. Stack plots are best for showing how parts of a whole change over time (like daily hours for different activities).

> **Student Question:** What does `explode` do in a pie chart?
> **Answer:** The `explode` parameter is a tuple with one value per pie slice. A value of `0` means the slice stays in the pie normally. A positive value (like `0.1`) pulls that slice outward from the center by that amount — visually separating it to draw attention to it. This is used to highlight a specific category in data presentations.

> **Student Question:** What is `autopct` in a pie chart?
> **Answer:** `autopct='%1.1f%%'` automatically calculates and displays the percentage value of each pie slice on the slice itself. The format `'%1.1f%%'` means: one decimal place percentage. For example, `29.2%` or `8.3%`. Without `autopct`, pie slices have no numbers — only labels.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ValueError: x and y must have same first dimension` | X and Y have different lengths | Make sure X and Y lists have the same number of elements |
| Legend not showing | Labels set but `plt.legend()` not called | Call `plt.legend()` before `plt.show()` |
| Pie chart slices don't match | `explode` tuple length doesn't match `slices` length | `explode` must have same number of elements as `slices` |
| Stack plot missing colors | `colors` list shorter than number of Y series | Provide one color per Y series in `colors` list |

---

## Interview Questions

**Q: What is Matplotlib in Python?**
A: Matplotlib (Mathematical Plot Library) is a Python library for data visualization — creating diagrams from data. It provides functions for line graphs (`plt.plot()`), bar charts (`plt.bar()`), scatter plots (`plt.scatter()`), pie charts (`plt.pie()`), and stack plots (`plt.stackplot()`). It is built on NumPy. You supply X and Y coordinate values (or just values for pie/bar), and Matplotlib renders the visual diagram.

**Q: What is a scatter plot and when is it used?**
A: A scatter plot displays individual data points as dots (or other markers) at their (X, Y) coordinate positions without connecting them with lines. It is used to visualize relationships between two variables — e.g., do sales increase with advertising spend? Parameters include `color`, `s` (size), and `marker` (shape). Use `plt.scatter(x, y)`.

**Q: What is a pie chart and how do you highlight a slice?**
A: A pie chart shows proportional data — each slice represents what percentage of the total it comprises. Created with `plt.pie(slices, labels, colors, shadow, startangle, autopct)`. To highlight a specific slice, use the `explode` parameter: a tuple of the same length as `slices` where a positive value (like 0.1) pulls that slice outward from the center.

**Q: How do you add a legend to a Matplotlib graph?**
A: Add `label="name"` parameter to each `plt.plot()` or `plt.bar()` call, then call `plt.legend()` before `plt.show()`. This creates a legend box showing which color/line/bar corresponds to which label. `plt.legend(loc='upper left')` positions the legend.

---

## Try It Yourself

**Exercise 1:** Create a pie chart showing the market share of 4 programming languages: Python=40%, Java=30%, JavaScript=20%, Others=10%. Use shadow and autopct. Highlight Python's slice.

<details><summary>Answer</summary>

```python
from matplotlib import pyplot as plt

slices  = [40, 30, 20, 10]
labels  = ['Python', 'Java', 'JavaScript', 'Others']
colors  = ['g', 'b', 'y', 'r']
explode = (0.1, 0, 0, 0)    # highlight Python

plt.pie(slices, labels=labels, colors=colors,
        shadow=True, startangle=90,
        autopct='%1.1f%%', explode=explode)

plt.title("Programming Language Market Share")
plt.show()
```
</details>

---

**Exercise 2:** Create a stacked area plot for 3 days showing hours spent on: work (8, 9, 7), study (3, 2, 4), leisure (5, 4, 6). Days are 1, 2, 3.

<details><summary>Answer</summary>

```python
from matplotlib import pyplot as plt

days    = [1, 2, 3]
work    = [8, 9, 7]
study   = [3, 2, 4]
leisure = [5, 4, 6]

plt.stackplot(days, work, study, leisure,
              colors=['b', 'g', 'r'],
              labels=['Work', 'Study', 'Leisure'])

plt.xlabel("Day")
plt.ylabel("Hours")
plt.title("Daily Time Allocation")
plt.legend(loc='upper left')
plt.show()
```
</details>

---

**Exercise 3:** Plot two bar charts side by side comparing Q1 and Q2 sales for 3 products at positions [1, 3, 5] and [2, 4, 6]. Add labels, legend, and title.

<details><summary>Answer</summary>

```python
from matplotlib import pyplot as plt

plt.bar([1, 3, 5], [15000, 12000, 18000], color='b', label='Q1 Sales')
plt.bar([2, 4, 6], [17000, 13500, 16000], color='g', label='Q2 Sales')

plt.xlabel("Products")
plt.ylabel("Sales (Rs)")
plt.title("Q1 vs Q2 Sales Comparison")
plt.legend()
plt.show()
```
</details>
