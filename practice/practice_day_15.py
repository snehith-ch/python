# ============================================================
# PRACTICE — Day 15: Functions — Return Values, Local & Global
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: RETURN MULTIPLE VALUES
# --------------------------------------------------

# Q1. Predict the output:

def stats(a, b):
    total = a + b
    diff  = a - b
    return total, diff

x, y = stats(30, 10)
print(x)   # prediction:
print(y)   # prediction:


# Q2. What type does a multi-value return actually produce?

def multi():
    return 1, 2, 3

result = multi()
print(result)         # prediction:
print(type(result))   # prediction:


# Q3. Return multiple values — the "bad practice" discussion:
#
# Function below does addition, subtraction, AND multiplication:
#
# def all_ops(a, b):
#     return a+b, a-b, a*b
#
# Q3a. If you only need the sum, can you stop subtract/multiply from running?
# YOUR ANSWER:
#
# Q3b. Write the BETTER approach: 3 separate functions, each doing ONE task.

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 2: LOCAL VARIABLES
# --------------------------------------------------

# Q4. Predict the output — which line causes an error?

def f1():
    a = 10
    print(a)

def f2():
    b = 20
    print(b)

f1()   # prediction:
f2()   # prediction:


# Q5. Access a local variable from another function — predict the error:

def f1():
    secret = 42
    print("Inside f1:", secret)

def f2():
    print("Inside f2:", secret)   # can f2 see f1's variable?

f1()
# f2()   # uncomment to see error — predict:
# YOUR PREDICTION:


# Q6. What happens inside f1 stays in f1:

def f1():
    x = 100
    print("f1:", x)

def f2():
    x = 999          # different x — local to f2
    print("f2:", x)

f1()
f2()
# Are these the same x? YOUR ANSWER:


# --------------------------------------------------
# SECTION 3: GLOBAL VARIABLES
# --------------------------------------------------

# Q7. Predict the output:

n = 50   # global

def f1():
    print("f1:", n)

def f2():
    print("f2:", n)

f1()   # prediction:
f2()   # prediction:


# Q8. Global variable — read vs write WITHOUT global keyword:

count = 0   # global

def increment():
    count = count + 1   # does this modify the global?
    print(count)

# increment()   # uncomment to see error — predict:
# YOUR PREDICTION (what error and why):


# Q9. FIX Q8 using the global keyword:

count = 0

def increment():
    global count
    count = count + 1
    print(count)

increment()
increment()
increment()
# Prediction (3 calls):


# Q10. Call ORDER matters with global:

val = 10   # global

def change_val():
    global val
    val = 99

def read_val():
    print(val)

read_val()      # prediction:
change_val()    # prediction (output?):
read_val()      # prediction:


# --------------------------------------------------
# SECTION 4: global KEYWORD — DECLARE INSIDE FUNCTION
# --------------------------------------------------

# Q11. Create a global variable INSIDE a function:

def create_global():
    global message
    message = "Hello from inside!"

def read_message():
    print(message)

create_global()
read_message()   # prediction:


# Q12. What happens if you call read_message BEFORE create_global?

# read_message()    # uncomment to see — prediction (what error?):


# --------------------------------------------------
# SECTION 5: NAME CONFLICT — local vs global
# --------------------------------------------------

# Q13. Predict the output carefully:

x = "global"

def f1():
    x = "local"     # shadows the global
    print(x)

def f2():
    print(x)        # no local x here

f1()   # prediction:
f2()   # prediction:


# Q14. Predict the output:

score = 100   # global

def game():
    global score
    score = 50   # modifies global

def show():
    print(score)

show()    # prediction:
game()
show()    # prediction:


# Q15. Access BOTH local and global when names conflict:

n = 10   # global

def f1():
    n = 99               # local
    print("local n:", n)
    print("global n:", globals()["n"])

f1()
# Prediction (2 lines):


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Write a function counter() using the global keyword.
# Every time it is called, it increments a global variable 'total' by 1
# and prints the current total.
# Call it 5 times.

total = 0
# YOUR CODE HERE:


# BONUS 2:
# Predict ALL output before running:

a = 5   # global

def outer():
    a = 10              # local to outer
    print("outer:", a)

def show_global():
    print("global:", a)

outer()
show_global()

# Your prediction:


# BONUS 3:
# Write two functions:
#   area(length, width): returns length * width
#   perimeter(length, width): returns 2 * (length + width)
# Use return (not print) in both.
# Accept length and width from the user, call both, print results.

# YOUR CODE HERE:


# BONUS 4:
# Predict the output — trace very carefully:

x = 1   # global

def f1():
    global x
    x = x + 1
    print("f1:", x)

def f2():
    x = 100           # local
    print("f2:", x)

def f3():
    print("f3:", x)   # which x — local or global?

f3()   # prediction:
f1()   # prediction:
f2()   # prediction:
f3()   # prediction:
f1()   # prediction:

# Your step-by-step trace:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. A function with no  return  statement returns:
#    A) 0    B) ""    C) None    D) Error
# Answer: ___

# Q_MCQ_2. What does  return x, y  actually return?
#    A) Two separate values    B) A tuple (x, y)
#    C) A list [x, y]          D) Error — only one value can be returned
# Answer: ___

# Q_MCQ_3. Which letter in LEGB stands for "Enclosing"?
#    A) L    B) E    C) G    D) B
# Answer: ___

# Q_MCQ_4. Can you READ a global variable inside a function without
#           using the  global  keyword?
#    A) No — you always need global keyword
#    B) Yes — reading works; only MODIFYING needs global
#    C) Only if the variable is an integer
#    D) Only inside a class
# Answer: ___

# Q_MCQ_5. What does  global x  do inside a function?
#    A) Creates a new local variable
#    B) Tells Python to use and modify the global x, not create a local one
#    C) Deletes the global x
#    D) Makes x read-only
# Answer: ___

# Q_MCQ_6. Which is the correct LEGB lookup order?
#    A) Global → Local → Built-in → Enclosing
#    B) Local → Enclosing → Global → Built-in
#    C) Built-in → Global → Enclosing → Local
#    D) Local → Global → Enclosing → Built-in
# Answer: ___

# Q_MCQ_7. def f(): x = 10  → After calling f(), is x accessible outside?
#    A) Yes — x is now global    B) No — x is local to f()
#    C) Only if returned          D) Yes if f() is called twice
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. A function that returns nothing implicitly returns _______.

# FIB_2. a, b = get_min_max(lst)  works when get_min_max returns _______.

# FIB_3. To modify a global variable inside a function, use the
#         _______ keyword before assignment.

# FIB_4. LEGB stands for: L=_______, E=_______, G=_______, B=_______.

# FIB_5. A variable created inside a function is called a _______ variable
#         and only exists while the function is _______.

# FIB_6. Built-in names like  print, len, range  are in the _______ scope.

# FIB_7. def calc(a, b): return a+b, a-b, a*b  — calling this returns
#         a _______ with _______ elements.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: BMI Health Calculator using proper function design.
#
# Requirements:
#   1. Global constant: CATEGORIES = {(0,18.5):"Underweight",
#      (18.5,25):"Normal", (25,30):"Overweight", (30,100):"Obese"}
#   2. Function: calculate_bmi(weight_kg, height_m) → returns BMI (float)
#      Formula: weight / (height ** 2)
#   3. Function: get_category(bmi) → returns category string
#      (loop through CATEGORIES dict)
#   4. Function: get_advice(category) → returns advice string
#      (use a local dict inside the function — show local scope)
#   5. Function: full_report(name, weight, height) → calls all 3 functions,
#      prints formatted report, returns (bmi, category)
#   6. Main code: call full_report for 2 people
#   7. Show that the local advice dict inside get_advice() is NOT
#      accessible outside the function (use try/except NameError)
#
# Expected output:
#   === BMI Report: Snehith ===
#   Weight: 70 kg | Height: 1.75 m
#   BMI      : 22.9
#   Category : Normal
#   Advice   : Maintain your diet and stay active!
#
# Hint: For get_category, iterate CATEGORIES.items() and check
#       lower <= bmi < upper.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: x=40, y=20

# Q2: (1, 2, 3), <class 'tuple'>

# Q3a: No — the function does all tasks, you can ignore results but cannot stop execution

# Q4: f1→10, f2→20

# Q5: NameError: name 'secret' is not defined

# Q6: They are DIFFERENT variables — each local to its own function

# Q7: f1→50, f2→50

# Q8: UnboundLocalError: local variable 'count' referenced before assignment
#     Python sees 'count = count + 1' as local (there's an assignment in the function)
#     but tries to read it before assigning

# Q9: 1, 2, 3

# Q10: 10 (global), (no output), 99 (changed global)

# Q11: "Hello from inside!"

# Q12: NameError: name 'message' is not defined

# Q13: f1→"local", f2→"global"

# Q14: 100, (no output), 50

# Q15: local n: 99, global n: 10

# BONUS 2: outer→10, global→5

# BONUS 4: f3→1, f1→2, f2→100, f3→2, f1→3


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: C   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: None
# FIB_2: a tuple of 2 values (or two separate values separated by comma)
# FIB_3: global
# FIB_4: Local, Enclosing, Global, Built-in
# FIB_5: local;  executing (running)
# FIB_6: built-in (B in LEGB)
# FIB_7: tuple;  3

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# CATEGORIES = [(0,18.5,"Underweight"),(18.5,25,"Normal"),
#               (25,30,"Overweight"),(30,100,"Obese")]
#
# def calculate_bmi(weight, height):
#     return weight / (height ** 2)
#
# def get_category(bmi):
#     for low, high, cat in CATEGORIES:
#         if low <= bmi < high:
#             return cat
#     return "Unknown"
#
# def get_advice(category):
#     advice = {"Underweight": "Eat more nutritious food.",
#               "Normal":      "Maintain your diet and stay active!",
#               "Overweight":  "Consider more exercise and less sugar.",
#               "Obese":       "Consult a doctor for a diet plan."}
#     return advice.get(category, "No advice available.")
#
# def full_report(name, weight, height):
#     bmi = calculate_bmi(weight, height)
#     cat = get_category(bmi)
#     adv = get_advice(cat)
#     print(f"=== BMI Report: {name} ===")
#     print(f"Weight: {weight} kg | Height: {height} m")
#     print(f"BMI      : {bmi:.1f}")
#     print(f"Category : {cat}")
#     print(f"Advice   : {adv}")
#     return bmi, cat
#
# full_report("Snehith", 70, 1.75)
# full_report("Priya",   55, 1.60)

