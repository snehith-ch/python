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



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. How do you create a custom exception in Python?
#    A) class MyError:  pass
#    B) class MyError(Exception):  pass
#    C) def MyError(Exception):  pass
#    D) exception MyError:  pass
# Answer: ___

# Q_MCQ_2. What keyword is used to raise an exception manually?
#    A) throw    B) raise    C) error    D) except
# Answer: ___

# Q_MCQ_3. When does the  finally  block execute?
#    A) Only on success    B) Only on error
#    C) Always — success or failure    D) Only when re-raising
# Answer: ___

# Q_MCQ_4. To pass a custom message with a raised exception:
#    A) raise ValueError    B) raise ValueError("message")
#    C) error("message")    D) except ValueError("message")
# Answer: ___

# Q_MCQ_5. What is the base class for ALL built-in exceptions?
#    A) Error    B) BaseException    C) Exception    D) RuntimeError
# Answer: ___

# Q_MCQ_6. Which is the correct way to re-raise a caught exception?
#    A) re-raise    B) raise e    C) raise    D) throw e
# Answer: ___

# Q_MCQ_7. Custom exceptions should inherit from  Exception  because:
#    A) It is required by Python syntax
#    B) It lets them be caught by  except Exception
#    C) It makes them print automatically
#    D) All of the above
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. class InvalidAgeError(_______):  pass  — inherits from built-in base.

# FIB_2. To trigger a custom exception:  _______ InvalidAgeError("Too young")

# FIB_3. The  _______  block ALWAYS runs, even if  return  is hit in try.

# FIB_4. You can add a custom message by overriding  _______(self, msg)  in
#         the exception class.

# FIB_5. Catching  Exception  in an except block catches _______
#         (all / only user-defined) exceptions.

# FIB_6. If no  except  block matches, the exception _______  up the call stack.

# FIB_7. A finally block is typically used to _______ resources
#         (e.g., close files, DB connections).


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: User Registration System with custom validation exceptions.
#
# Requirements:
#   1. Define three custom exceptions:
#      - InvalidAgeError    (age < 18 or > 120)
#      - InvalidEmailError  (no "@" or no ".")
#      - WeakPasswordError  (length < 8)
#   2. Write a  register_user(name, age, email, password)  function that
#      raises the appropriate custom exception
#   3. In main code, call register_user inside try/except/finally
#   4. finally should print "Registration attempt complete."
#   5. Test with at least 3 cases: one success, two failures
#
# Expected output (example):
#   Registering Alice (17)...
#   InvalidAgeError: Age must be between 18 and 120. Got: 17
#   Registration attempt complete.
#   Registering Bob (25)...
#   InvalidEmailError: Invalid email: no-at-sign
#   Registration attempt complete.
#   Registering Carol (30, carol@mail.com, Str0ngPass)...
#   User Carol registered successfully!
#   Registration attempt complete.
#
# YOUR CODE HERE:


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

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: C   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: C   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: Exception
# FIB_2: raise
# FIB_3: finally
# FIB_4: __init__
# FIB_5: all  (all exceptions that inherit from Exception)
# FIB_6: propagates
# FIB_7: release / close / clean up

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# class InvalidAgeError(Exception): pass
# class InvalidEmailError(Exception): pass
# class WeakPasswordError(Exception): pass
#
# def register_user(name, age, email, password):
#     if not (18 <= age <= 120):
#         raise InvalidAgeError(f"Age must be between 18 and 120. Got: {age}")
#     if "@" not in email or "." not in email:
#         raise InvalidEmailError(f"Invalid email: {email}")
#     if len(password) < 8:
#         raise WeakPasswordError(f"Password too short: {len(password)} chars")
#     print(f"User {name} registered successfully!")
#
# tests = [
#     ("Alice", 17, "alice@mail.com", "P@ssword1"),
#     ("Bob", 25, "no-at-sign", "P@ssword1"),
#     ("Carol", 30, "carol@mail.com", "Str0ngPass"),
# ]
# for args in tests:
#     name = args[0]
#     print(f"Registering {name}...")
#     try:
#         register_user(*args)
#     except (InvalidAgeError, InvalidEmailError, WeakPasswordError) as e:
#         print(f"{type(e).__name__}: {e}")
#     finally:
#         print("Registration attempt complete.")

