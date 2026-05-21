# ============================================================
# PRACTICE — Day 44: Pandas and Matplotlib (Part 2)
# ============================================================
# Instructions:
#   - Requires: pip install pandas matplotlib
#   - Plots are saved as PNG files for review
# ============================================================

import warnings
warnings.filterwarnings("ignore")

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


# --------------------------------------------------
# SECTION 1: Styled Line Graphs
# --------------------------------------------------

# Q1. Predict — color codes:
# 'g' = ?      'b' = ?      'r' = ?
# 'c' = ?      'k' = ?      'm' = ?      'y' = ?

# YOUR ANSWERS:


# Q2. Two-line graph with styling — predict what you'd see if you ran this:

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 3, 5, 6]

x2 = [1, 2, 3, 4, 5]
y2 = [5, 3, 6, 2, 4]

plt.figure()
plt.plot(x1, y1, 'g', linewidth=3, label='Line 1')
plt.plot(x2, y2, 'r', linewidth=3, label='Line 2')
plt.title("Two Lines")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, color='grey')
plt.savefig("practice_plot_44_q2.png")
plt.close()
print("Q2 saved")


# Q3. Legend and labels — fill in blanks:

# plt.plot(x, y, '____', linewidth=____, label='____')   # color, thickness, name
# plt.legend()    # call this to show the legend box

# Without legend(), what happens to labels?
# YOUR ANSWER:


# Q4. grid() parameters — predict:

# plt.grid(True)                      → shows grid in __________ color
# plt.grid(True, color='yellow')      → shows grid in __________ color
# plt.grid(False)                     → __________
# plt.grid(True, linestyle='--')      → dashed __________ lines

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 2: Bar Graph
# --------------------------------------------------

# Q5. Basic bar chart:

categories = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
sales = [120, 85, 160, 90, 200]

plt.figure()
plt.bar(categories, sales, color='b', label='Sales')
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Weekly Sales")
plt.legend()
plt.savefig("practice_plot_44_q5.png")
plt.close()
print("Q5 saved")


# Q6. Two-group bar chart — predict positions:

plt.figure()
plt.bar([1, 3, 5, 7], [10, 15, 8, 12], color='g', label='Group A')
plt.bar([2, 4, 6, 8], [8, 12, 14, 9], color='r', label='Group B')
plt.title("Two Groups")
plt.legend()
plt.savefig("practice_plot_44_q6.png")
plt.close()

# Q: Why use [1,3,5,7] and [2,4,6,8] instead of both using [1,2,3,4]?
# YOUR ANSWER:


# Q7. Bar chart — what does bar height represent?
# a) The X coordinate value
# b) The Y value — the magnitude of each category
# c) The index position of the bar

# YOUR ANSWER:


# --------------------------------------------------
# SECTION 3: Scatter Plot
# --------------------------------------------------

# Q8. Scatter plot with custom markers — run and observe:

x = [2, 4, 6, 8, 10, 12]
y = [3, 7, 5, 9, 4, 8]

plt.figure()
plt.scatter(x, y, color='m', s=150, marker='*')
plt.title("Scatter Plot with Stars")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("practice_plot_44_q8.png")
plt.close()
print("Q8 saved")


# Q9. Match scatter markers to their names:

# 'o' → ?      '*' → ?      '^' → ?
# 's' → ?      '+' → ?      'D' → ?

# YOUR ANSWERS:


# Q10. Scatter vs Line — when to use each?
# Scatter: use when data points __________ (no meaningful connection between points)
# Line: use when data shows __________ (connected trend or time series)

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 4: Stack Plot
# --------------------------------------------------

# Q11. Stack plot — create one:

days = [1, 2, 3, 4, 5]
work  = [8, 9, 7, 8, 6]
study = [2, 3, 4, 3, 4]
play  = [6, 4, 5, 5, 6]
sleep = [8, 8, 8, 8, 8]

# Verify: do they sum to 24 each day?
for i, d in enumerate(days):
    total = work[i] + study[i] + play[i] + sleep[i]
    print(f"Day {d}: {total} hours")    # prediction (should all be 24):

plt.figure()
plt.stackplot(days, work, study, play, sleep,
              colors=['b', 'g', 'r', 'grey'],
              labels=['Work', 'Study', 'Play', 'Sleep'])
plt.xlabel("Day")
plt.ylabel("Hours")
plt.title("Daily Activities")
plt.legend(loc='upper left')
plt.savefig("practice_plot_44_q11.png")
plt.close()
print("Q11 saved")


# Q12. Stack plot concept — fill in blanks:

# In a stack plot, each series is __________ on top of the previous one.
# The total height at any X point represents __________ of all series.
# Labels appear via plt.________() function.

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 5: Pie Chart
# --------------------------------------------------

# Q13. Basic pie chart:

slices  = [35, 25, 20, 20]
labels  = ['Python', 'Java', 'JavaScript', 'Other']
colors  = ['g', 'b', 'y', 'grey']

plt.figure()
plt.pie(slices, labels=labels, colors=colors,
        shadow=True, startangle=90, autopct='%1.1f%%')
plt.title("Language Popularity")
plt.savefig("practice_plot_44_q13.png")
plt.close()
print("Q13 saved")


# Q14. autopct='%1.1f%%' — what does each part mean?
# %1.1f → ?
# %% → ?
# Together: what does it show on each slice?

# YOUR ANSWERS:


# Q15. explode — predict the visual effect:

slices  = [40, 30, 20, 10]
labels  = ['A', 'B', 'C', 'D']
explode = (0.1, 0, 0, 0)    # pull out first slice

plt.figure()
plt.pie(slices, labels=labels, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Explode Demo")
plt.savefig("practice_plot_44_q15.png")
plt.close()

# prediction: which slice is pulled out?
# prediction: what does explode=(0,0,0.2,0) do?

# YOUR ANSWERS:


# Q16. Pie chart parameters — match each to its purpose:

# shadow=True          → ?
# startangle=90        → ?
# autopct='%1.1f%%'    → ?
# explode=(0.1,0,0,0)  → ?

# YOUR ANSWERS:


# --------------------------------------------------
# SECTION 6: Write Code
# --------------------------------------------------

# Q17. Create a complete pie chart for monthly budget:
#   - Categories: Rent(4000), Food(2000), Transport(1000), Entertainment(500), Savings(2500)
#   - Highlight Savings slice (explode by 0.1)
#   - Show percentages with autopct
#   - Add shadow and title "Monthly Budget"
#   - Save as "budget_pie.png"

# YOUR CODE HERE:


# Q18. Create a stack plot showing 4 weeks of time spent (hours per day):
#   Week 1: Work=8, Study=2, Rest=14
#   Week 2: Work=9, Study=3, Rest=12
#   Week 3: Work=7, Study=4, Rest=13
#   Week 4: Work=8, Study=3, Rest=13
# (Verify they sum to 24 each)
# Save as "weekly_stack.png"

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — two subplots in one figure:

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)    # 1 row, 2 cols, plot 1
x = [1, 2, 3, 4, 5]
plt.plot(x, [v**2 for v in x], 'b')
plt.title("Square")

plt.subplot(1, 2, 2)    # 1 row, 2 cols, plot 2
plt.plot(x, [v**3 for v in x], 'r')
plt.title("Cube")

plt.tight_layout()
plt.savefig("practice_plot_44_bonus1.png")
plt.close()
print("Bonus 1 saved")    # prediction:


# BONUS 2: Answer conceptual questions:

# a) What is the difference between a line graph and a scatter plot?
# b) When would a stack plot be more informative than a regular line graph?
# c) What does the total height of a stacked bar at any X represent?
# d) If autopct='%1.0f%%' instead of '%1.1f%%', what changes?

# YOUR ANSWERS:


# BONUS 3: Create a 4-in-1 figure with:
#   - Subplot 1: Line graph (x vs x^2)
#   - Subplot 2: Bar chart (weekday sales)
#   - Subplot 3: Scatter plot (random-ish points)
#   - Subplot 4: Pie chart (4 categories)
# Use plt.subplot(2, 2, n) for each.
# Save as "dashboard.png"

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: g=green, b=blue, r=red, c=cyan, k=black, m=magenta, y=yellow

# Q3: Without legend(), labels are set but never displayed — no legend box appears

# Q4: default (blue-grey), yellow, no grid, dashed lines

# Q6: Using different X positions (odd vs even) places bars SIDE BY SIDE
#     Using same positions would overlap (one would hide the other)

# Q7: b) The Y value — magnitude of each category

# Q9: o=circle, *=star, ^=triangle, s=square, +=plus, D=diamond

# Q10: Scatter: no meaningful connection; Line: connected trend or time series

# Q11: Day 1: 24, Day 2: 24, Day 3: 24, Day 4: 24, Day 5: 24

# Q12: stacked, the sum, legend

# Q14: %1.1f = one decimal float, %% = literal % sign
#      Together: shows percentage like "29.2%"

# Q15: Slice A (first) is pulled out; explode=(0,0,0.2,0) pulls out slice C (third)

# Q16: shadow=True=adds shadow behind pie, startangle=90=rotates starting position,
#      autopct=shows % on slices, explode=separates one slice

# BONUS 1: "Bonus 1 saved"

# BONUS 2: a) Line connects points showing trend; scatter shows individual points with no connection
#          b) Stack shows composition (parts of a whole over time)
#          c) The total/sum of all series at that X point
#          d) %1.0f shows whole numbers (no decimal): "29%" instead of "29.2%"
