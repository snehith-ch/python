# ============================================================
# PRACTICE — Day 27: Inner Class and Encapsulation
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Inner Classes
# --------------------------------------------------

# Q1. Predict — accessing inner class through outer:

class Outer:
    def __init__(self):
        self.message = "I am Outer"
        self.inner = self.Inner()    # create Inner object inside Outer

    class Inner:
        def __init__(self):
            self.message = "I am Inner"

        def show(self):
            print(self.message)

    def display(self):
        print(self.message)
        self.inner.show()

o = Outer()
o.display()        # prediction (two lines):


# Q2. Accessing inner class — 3 styles — predict:

class Engine:
    def __init__(self):
        self.type = "V8"
        self.transmission = self.Transmission()

    class Transmission:
        def __init__(self):
            self.gear = "Automatic"

        def info(self):
            print(f"Transmission: {self.gear}")

    def start(self):
        print(f"Engine type: {self.type}")
        self.transmission.info()

# Style 1: separate references
e = Engine()
t = e.transmission
t.info()            # prediction:

# Style 2: chained access
e.transmission.info()   # prediction:

# Style 3: via the start method
e.start()               # prediction (2 lines):


# Q3. Inner class without outer object first — predict:

class Library:
    class Book:
        def __init__(self, title):
            self.title = title

        def show(self):
            print(f"Book: {self.title}")

# Can we create a Book without creating Library first?
b = Library.Book("Python 101")   # prediction (works or error?):
b.show()                         # prediction:


# --------------------------------------------------
# SECTION 2: Encapsulation — Access Modifiers
# --------------------------------------------------

# Q4. Public variables — predict:

class Person:
    def __init__(self, name, age):
        self.name = name    # public
        self.age = age      # public

p = Person("Alice", 30)
print(p.name)       # prediction:
print(p.age)        # prediction:
p.name = "Bob"      # public — can modify directly
print(p.name)       # prediction:


# Q5. Protected (_) variables — predict:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance    # protected (convention only)

    def show(self):
        print(f"{self.owner}: {self._balance}")

b = BankAccount("Sita", 10000)
b.show()               # prediction:
print(b._balance)      # prediction (accessible but discouraged):
b._balance = 99999     # prediction: works or error?
print(b._balance)      # prediction:


# Q6. Private (__) variables — name mangling — predict:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary    # private — name mangled to _Employee__salary

    def get_salary(self):
        return self.__salary      # works inside class

e = Employee("Ravi", 50000)
print(e.name)           # prediction:
print(e.get_salary())   # prediction:

# print(e.__salary)     # uncomment → prediction (error?):
print(e._Employee__salary)   # prediction (name mangling trick):


# Q7. Private METHOD — predict:

class Secure:
    def __init__(self, pin):
        self.__pin = pin

    def __validate(self):              # private method
        return self.__pin == "1234"    # only works inside class

    def login(self, attempt):
        if attempt == self.__pin:
            print("Login successful")
        else:
            print("Wrong PIN")

s = Secure("1234")
s.login("1234")     # prediction:
s.login("9999")     # prediction:
# s.__validate()    # uncomment → prediction (error?):


# --------------------------------------------------
# SECTION 3: Write Code
# --------------------------------------------------

# Q8. Create a class CreditCard:
#   - Private: __card_number, __cvv, __balance
#   - Public: owner
#   - Method show_info(): prints owner and last 4 digits of card only
#   - Method charge(amount): deducts from balance if sufficient
# Create one card and test both methods.

# YOUR CODE HERE:


# Q9. Create an outer class Computer with an inner class CPU:
#   - Computer: brand (instance var)
#   - CPU: cores, speed (instance vars), info() method
#   - Computer: start() method that prints brand and calls cpu.info()
# Create a Computer object and call start().

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — can you change a private var from outside using mangling?

class Secret:
    def __init__(self):
        self.__code = 42

    def reveal(self):
        print(self.__code)

s = Secret()
s.reveal()                    # prediction:
s._Secret__code = 999         # name mangling — modifying private var
s.reveal()                    # prediction: changes or not?


# BONUS 2: Predict the error — and explain WHY:

class Wallet:
    def __init__(self):
        self.__amount = 100

w = Wallet()
# w.__amount = 500      # is this modifying the private variable?
# w._Wallet__amount     # what does this access?

# Tricky: if you do w.__amount = 500, you are NOT modifying _Wallet__amount
# You are CREATING a new attribute called __amount
# They are DIFFERENT attributes!

# Try this:
w.__amount = 500             # creates NEW attribute (not private one)
print(w.__amount)            # prediction:
print(w._Wallet__amount)     # prediction (original private — still 100?):




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. How do you access an inner class from outside the outer class?
#    A) InnerClass()         B) Outer.Inner()
#    C) outer_obj.Inner()    D) Both B and C work
# Answer: ___

# Q_MCQ_2. Name mangling (__name) transforms the attribute to:
#    A) __name    B) _name    C) _ClassName__name    D) ClassName__name
# Answer: ___

# Q_MCQ_3. A single underscore prefix (e.g., _balance) means:
#    A) Completely private — cannot be accessed outside
#    B) Protected by convention — not enforced by Python
#    C) Class variable    D) Abstract attribute
# Answer: ___

# Q_MCQ_4. The purpose of encapsulation is to:
#    A) Speed up execution    B) Bundle data and methods, restrict direct access
#    C) Allow multiple inheritance    D) Create abstract classes
# Answer: ___

# Q_MCQ_5. A getter method:
#    A) Sets a private attribute value    B) Returns a private attribute value
#    C) Deletes an attribute             D) Validates input
# Answer: ___

# Q_MCQ_6. A setter method should:
#    A) Return the value    B) Validate input before setting the private attribute
#    C) Always raise an error    D) Access class variables only
# Answer: ___

# Q_MCQ_7. Trying to access obj.__private_var from outside the class:
#    A) Works normally    B) Returns None
#    C) Raises AttributeError (due to name mangling)    D) Prints a warning
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. __balance in a class becomes _______ (name mangling).

# FIB_2. One underscore (_name) is _______ by convention; double underscore
#         (__name) is enforced through _______.

# FIB_3. Inner class is defined _______ the outer class body.

# FIB_4. A setter validates before setting; a getter _______ the value.

# FIB_5. obj.__dict__  shows all _______ attributes of an object.

# FIB_6. To still access a name-mangled attribute from outside:
#         obj._ClassName________.

# FIB_7. Encapsulation in Python is achieved through _______ and _______ methods.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: ATM Machine Simulation with encapsulation + inner class.
#
# Requirements:
#   Define  ATM  class:
#   - Private: __balance, __pin
#   - Protected: _bank_name
#   - Inner class  Transaction: __init__(type, amount), display() prints receipt
#   - check_balance(entered_pin): verify pin; if correct, return balance
#   - deposit(amount): validate positive; update balance; create Transaction
#   - withdraw(amount, entered_pin): verify pin; check funds; update; Transaction
#   - change_pin(old_pin, new_pin): verify old pin; set new pin
#   - Getter get_balance() and get_bank() methods
#
# Simulate:
#   1. Create ATM(balance=5000, pin=1234, bank="PythonBank")
#   2. check_balance with WRONG pin → "Invalid PIN"
#   3. check_balance with correct pin → shows balance
#   4. deposit(2000) → balance becomes 7000
#   5. withdraw(3000, correct pin) → balance becomes 4000
#   6. withdraw(10000, correct pin) → "Insufficient funds"
#   7. change_pin(1234, 9999)
#   8. Try to access atm.__balance directly → AttributeError
#
# Expected output (partial):
#   Invalid PIN!
#   Balance: ₹5,000
#   ✅ Deposited ₹2,000 | New balance: ₹7,000
#   ✅ Withdrew ₹3,000  | New balance: ₹4,000
#   ❌ Insufficient funds
#   PIN changed successfully!
#   AttributeError: 'ATM' object has no attribute '__balance'

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "I am Outer", "I am Inner"

# Q2: "Transmission: Automatic", "Transmission: Automatic",
#     "Engine type: V8", "Transmission: Automatic"

# Q3: Works — b = Library.Book("Python 101"), "Book: Python 101"

# Q4: Alice, 30, Bob

# Q5: "Sita: 10000", 10000, works (only a convention), 99999

# Q6: Ravi, 50000
#     AttributeError: 'Employee' object has no attribute '__salary'
#     50000 (name mangling allows this)

# Q7: "Login successful", "Wrong PIN"
#     AttributeError: __validate is name-mangled to _Secure__validate

# BONUS 1: 42, 999 — yes, name mangling allows external modification

# BONUS 2: 500, 100 — they are DIFFERENT attributes!
#          w.__amount creates a new public-ish attr; _Wallet__amount is unchanged


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: D   Q_MCQ_2: C   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: C

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: _ATM__balance (or _ClassName__balance)
# FIB_2: protected;  name mangling
# FIB_3: inside
# FIB_4: returns
# FIB_5: instance
# FIB_6: __attribute_name
# FIB_7: getter;  setter

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# class ATM:
#     class Transaction:
#         def __init__(self, type_, amount):
#             self.type_  = type_
#             self.amount = amount
#         def display(self):
#             print(f"  📄 Transaction: {self.type_} | Amount: ₹{self.amount:,}")
#
#     def __init__(self, balance, pin, bank):
#         self.__balance  = balance
#         self.__pin      = pin
#         self._bank_name = bank
#
#     def check_balance(self, entered_pin):
#         if entered_pin != self.__pin: return print("Invalid PIN!")
#         print(f"Balance: ₹{self.__balance:,}")
#
#     def deposit(self, amount):
#         if amount <= 0: return print("Invalid amount.")
#         self.__balance += amount
#         print(f"✅ Deposited ₹{amount:,} | New balance: ₹{self.__balance:,}")
#         self.Transaction("Deposit", amount).display()
#
#     def withdraw(self, amount, entered_pin):
#         if entered_pin != self.__pin: return print("Invalid PIN!")
#         if amount > self.__balance: return print("❌ Insufficient funds")
#         self.__balance -= amount
#         print(f"✅ Withdrew ₹{amount:,}  | New balance: ₹{self.__balance:,}")
#         self.Transaction("Withdrawal", amount).display()
#
#     def change_pin(self, old, new):
#         if old != self.__pin: return print("Wrong old PIN!")
#         self.__pin = new; print("PIN changed successfully!")
#
# atm = ATM(5000, 1234, "PythonBank")
# atm.check_balance(9999)
# atm.check_balance(1234)
# atm.deposit(2000)
# atm.withdraw(3000, 1234)
# atm.withdraw(10000, 1234)
# atm.change_pin(1234, 9999)
# try: print(atm.__balance)
# except AttributeError as e: print(f"AttributeError: {e}")

