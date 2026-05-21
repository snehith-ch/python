# ============================================================
# PRACTICE — Day 32: Exception Handling — Advanced and Custom
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: finally Block
# --------------------------------------------------

# Q1. finally ALWAYS executes — predict all outputs:

def test(x):
    try:
        result = 10 / x
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("finally block runs")

test(2)     # prediction (2 lines):
test(0)     # prediction (2 lines):


# Q2. finally with return — tricky — predict:

def tricky():
    try:
        return "from try"
    finally:
        print("finally runs even with return!")
        # finally runs before the return actually exits

result = tricky()
print(result)    # prediction (what gets returned? does finally block it?):


# Q3. finally as cleanup — predict the flow:

def read_file(filename):
    print(f"Opening {filename}")
    try:
        if filename == "bad.txt":
            raise FileNotFoundError("File not found!")
        print("Reading file content")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        print(f"Closing {filename}")    # always close file

read_file("good.txt")    # prediction (3 lines):
print("---")
read_file("bad.txt")     # prediction (3 lines):


# --------------------------------------------------
# SECTION 2: Nested try-except
# --------------------------------------------------

# Q4. Predict — inner exception doesn't bubble to outer if caught:

try:
    print("Outer try")
    try:
        print("Inner try")
        x = int("abc")    # raises ValueError
        print("After int('abc')")
    except ValueError:
        print("Inner except: ValueError")
    print("After inner try-except")
except Exception:
    print("Outer except")
print("After all")

# prediction (all lines in order):


# Q5. Predict — inner exception NOT caught → bubbles to outer:

try:
    print("Outer try")
    try:
        print("Inner try")
        x = 1 / 0    # ZeroDivisionError — not caught by inner except
    except ValueError:
        print("Inner except: ValueError")
    print("After inner block")
except ZeroDivisionError:
    print("Outer except: ZeroDivisionError")
print("After all")

# prediction:


# --------------------------------------------------
# SECTION 3: User-Defined Exceptions
# --------------------------------------------------

# Q6. Custom exception — predict:

class AgeException(Exception):
    def __init__(self, msg):
        self.msg = msg

def check_age(age):
    if age < 0:
        raise AgeException("Age cannot be negative")
    if age >= 60:
        raise AgeException("Age should not be 60 or more")
    print(f"Valid age: {age}")

try:
    check_age(25)     # prediction:
except AgeException as e:
    print(e.msg)

try:
    check_age(65)     # prediction:
except AgeException as e:
    print(e.msg)

try:
    check_age(-5)     # prediction:
except AgeException as e:
    print(e.msg)


# Q7. Custom exception with multiple fields — predict:

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: have {balance}, need {amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    print(f"Withdrawn {amount}. Remaining: {balance - amount}")

try:
    withdraw(1000, 500)      # prediction:
except InsufficientFundsError as e:
    print(e)

try:
    withdraw(500, 800)       # prediction:
except InsufficientFundsError as e:
    print(e)
    print(f"Short by: {e.amount - e.balance}")    # prediction:


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q8. Create a custom exception NegativeValueError.
#   - Write a function sqrt_safe(n) that:
#     - Raises NegativeValueError if n < 0
#     - Returns math.sqrt(n) otherwise
#   - Handle it with try-except and print an appropriate message.

# YOUR CODE HERE:


# Q9. Write a function with try-except-finally:
#   - Takes a filename and a list of lines to write
#   - Opens file in write mode
#   - Writes all lines
#   - finally: prints "Write operation complete" always
#   - except IOError: prints "Could not write to file"

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict ALL output — finally + exception flow:

def mission():
    try:
        print("Step 1")
        raise ValueError("Oops")
        print("Step 2")    # does this print?
    except ValueError as e:
        print(f"Caught: {e}")
        return "failed"
    finally:
        print("Cleanup")

result = mission()
print(f"Result: {result}")


# BONUS 2: Custom exception hierarchy — predict:

class AppError(Exception):
    pass

class NetworkError(AppError):
    pass

class TimeoutError(NetworkError):
    pass

try:
    raise TimeoutError("Connection timed out")
except NetworkError as e:
    print(f"Network problem: {e}")    # prediction: catches TimeoutError?
except AppError as e:
    print(f"App problem: {e}")


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: Case test(2): "Result: 5.0", "finally block runs"
#     Case test(0): "Cannot divide by zero", "finally block runs"

# Q2: "finally runs even with return!", "from try"
#     (finally runs but doesn't stop return; return still happens)

# Q3: "Opening good.txt", "Reading file content", "Closing good.txt"
#     "Opening bad.txt", "Error: File not found!", "Closing bad.txt"

# Q4: "Outer try", "Inner try", "Inner except: ValueError",
#     "After inner try-except", "After all"
#     (outer except NOT triggered — inner caught the error)

# Q5: "Outer try", "Inner try", "Outer except: ZeroDivisionError", "After all"
#     ("After inner block" NOT printed — exception skipped it)

# Q6: "Valid age: 25", "Age should not be 60 or more", "Age cannot be negative"

# Q7: "Withdrawn 500. Remaining: 500"
#     "Insufficient funds: have 500, need 800", "Short by: 300"

# BONUS 1: "Step 1", "Caught: Oops", "Cleanup", "Result: failed"

# BONUS 2: "Network problem: Connection timed out"
#          — TimeoutError IS a NetworkError (inheritance), so first except catches it
