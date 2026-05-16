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
