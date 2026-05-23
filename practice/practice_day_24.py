# ============================================================
# PRACTICE — Day 24: Types of Variables
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Instance Variables
# --------------------------------------------------

# Q1. Predict — each object gets its OWN copy:

class Student:
    def __init__(self, name, marks):
        self.name = name       # instance variable
        self.marks = marks     # instance variable

s1 = Student("Alice", 90)
s2 = Student("Bob", 75)

print(s1.name)     # prediction:
print(s2.name)     # prediction:
print(s1.marks)    # prediction:
print(s2.marks)    # prediction:


# Q2. Modifying one object's instance variable — predict:

s1.marks = 95
print(s1.marks)    # prediction:
print(s2.marks)    # prediction (should s2 change?):


# Q3. Instance variables can be added outside __init__ — predict:

class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Rex")
d.age = 3          # adding instance variable outside __init__

print(d.name)      # prediction:
print(d.age)       # prediction:

d2 = Dog("Max")
# print(d2.age)    # uncomment → prediction (error?):


# --------------------------------------------------
# SECTION 2: Static (Class) Variables
# --------------------------------------------------

# Q4. Predict — static variable is SHARED across all objects:

class Circle:
    pi = 3.14159    # static variable — belongs to class

    def __init__(self, radius):
        self.radius = radius    # instance variable

    def area(self):
        return Circle.pi * self.radius ** 2

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi)   # prediction: access via class name
print(c1.pi)       # prediction: access via object (also works)
print(c1.area())   # prediction (approx):
print(c2.area())   # prediction (approx):


# Q5. Changing static variable — predict who is affected:

class Counter:
    count = 0    # static variable

    def __init__(self):
        Counter.count += 1

c1 = Counter()
print(Counter.count)    # prediction:
c2 = Counter()
print(Counter.count)    # prediction:
c3 = Counter()
print(Counter.count)    # prediction:


# Q6. Tricky: instance variable shadows static variable — predict:

class Foo:
    x = 10    # static

    def change(self):
        self.x = 99    # creates instance variable! doesn't change static

f1 = Foo()
f2 = Foo()

print(f1.x)       # prediction: reads static
f1.change()
print(f1.x)       # prediction: now reads instance variable
print(f2.x)       # prediction: f2 unchanged, still reads static
print(Foo.x)      # prediction: class variable unchanged


# --------------------------------------------------
# SECTION 3: Local Variables
# --------------------------------------------------

# Q7. Local variables — predict the error:

class Calculator:
    def add(self, a, b):
        result = a + b    # local variable — exists only inside add()
        return result

calc = Calculator()
print(calc.add(3, 4))    # prediction:
# print(result)           # uncomment → prediction (error?):


# Q8. Predict — local vs instance:

class Temp:
    def __init__(self):
        self.x = 100    # instance variable

    def process(self):
        x = 200         # local variable (shadows self.x inside method)
        print(x)        # prediction:
        print(self.x)   # prediction:

t = Temp()
t.process()


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q9. Define a class Employee:
#   - Static variable: company = "TechCorp"
#   - Instance variables: name, salary
#   - Method display(): prints company, name, salary
# Create 2 employees. Change the company name via class name.
# Verify both employees see the new company name.

# YOUR CODE HERE:


# Q10. Predict then verify — delete a static variable:

class Config:
    debug = True
    version = "1.0"

print(Config.debug)        # prediction:
del Config.debug
# print(Config.debug)       # uncomment → prediction (error?):
print(Config.version)      # prediction (still accessible?):


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict ALL output:

class Example:
    val = "class_val"

    def __init__(self):
        self.val = "instance_val"

    def show(self):
        val = "local_val"
        print(val)          # prediction:
        print(self.val)     # prediction:
        print(Example.val)  # prediction:

e = Example()
e.show()


# BONUS 2:
# Create a class BankAccount with:
#   - Static: bank_name = "National Bank", interest_rate = 0.05
#   - Instance: owner, balance
#   - Method annual_interest(): returns balance * interest_rate
# Change interest_rate to 0.07 via class name.
# Create 2 accounts and verify both use the new rate.

# YOUR CODE HERE:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. An instance variable is:
#    A) Shared by all objects    B) Belongs to a specific object (self.x)
#    C) Defined outside the class    D) A constant value
# Answer: ___

# Q_MCQ_2. A class (static) variable is:
#    A) Defined inside __init__ with self    B) Local to each method
#    C) Defined in class body, shared by all objects    D) Always uppercase
# Answer: ___

# Q_MCQ_3. If you do  obj.class_var = 99  on an object, what happens?
#    A) All objects' class_var becomes 99
#    B) A new instance variable named class_var is created for obj only
#    C) SyntaxError    D) The class variable is permanently changed
# Answer: ___

# Q_MCQ_4. Where is a local variable accessible?
#    A) Across all methods    B) Only inside the method where it's defined
#    C) In the class and its subclasses    D) In any function in the module
# Answer: ___

# Q_MCQ_5. Company.employee_count  vs  emp1.employee_count — which is correct
#           to access a class variable?
#    A) Only Company.employee_count    B) Only emp1.employee_count
#    C) Both work; Company. is preferred for class variables    D) Neither
# Answer: ___

# Q_MCQ_6. What is the value of Dog.legs  after this?
#           class Dog: legs = 4
#           d = Dog(); d.legs = 3
#    A) 3    B) 4    C) Error    D) None
# Answer: ___

# Q_MCQ_7. A local variable inside __init__ (without self.) is:
#    A) The same as an instance variable    B) NOT stored in the object
#    C) A class variable                    D) Accessible from outside
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. self.name = name  creates an _______ variable.
#         Employee.count = 0  creates a _______ variable.

# FIB_2. A local variable defined inside a method (without self)
#         is destroyed when the method _______.

# FIB_3. All objects of a class share the same _______ variables.

# FIB_4. ClassName.class_var += 1  modifies the class variable for
#         _______ objects.

# FIB_5. obj.__dict__  shows all _______ variables of the object.

# FIB_6. temp = self.salary * 0.1  inside a method — temp is a _______ variable.

# FIB_7. Class variables are defined _______ the __init__ method,
#         directly in the class body.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Bank Branch System showing instance vs class variables.
#
# Requirements:
#   Define  BankAccount  class:
#   - Class variable: bank_name = "PythonBank", total_accounts = 0
#   - __init__(holder, balance=0): increment total_accounts, store holder & balance
#   - deposit(amount): add to balance, print receipt
#   - withdraw(amount): check balance first; print receipt or "Insufficient funds"
#   - display(): show holder, balance, bank_name
#   - classmethod get_total(): returns total_accounts
#   - __str__: returns "Account[{holder}]: ₹{balance:,}"
#
# Then:
#   1. Create 3 accounts (different holders, different balances)
#   2. Deposit to account 1; withdraw from account 2 (valid)
#   3. Try to overdraw account 3
#   4. Print total_accounts via BOTH Bank.get_total() AND each obj
#   5. Print all accounts using str()
#   6. Show bank_name is shared: change BankAccount.bank_name = "NewBank"
#      → verify all objects show "NewBank" in display()
#
# Expected output (partial):
#   Total accounts created: 3
#   Snehith: ₹15,000 → deposited ₹5,000 → balance: ₹20,000
#   Priya  : withdrew ₹2,000 → balance: ₹8,000
#   Raj    : Insufficient funds (balance: ₹500)
#   All now show bank: NewBank

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: Alice, Bob, 90, 75

# Q2: 95, 75 (s2 is not affected — each has its own copy)

# Q3: Rex, 3
#     AttributeError: 'Dog' object has no attribute 'age' (d2 has no .age)

# Q4: 3.14159, 3.14159, 78.53975, 314.159

# Q5: 1, 2, 3

# Q6: 10 (reads static), 99 (reads instance — shadowed), 10 (f2 still reads static), 10 (class unchanged)

# Q7: 7
#     NameError: name 'result' is not defined (local variable gone after method ends)

# Q8: 200 (local), 100 (instance — self.x unchanged)

# Q10: True, AttributeError after del Config.debug, "1.0"

# BONUS 1: local_val, instance_val, class_val


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: C   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: instance;  class (static)
# FIB_2: returns (finishes)
# FIB_3: class
# FIB_4: all
# FIB_5: instance
# FIB_6: local
# FIB_7: outside

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# class BankAccount:
#     bank_name      = "PythonBank"
#     total_accounts = 0
#
#     def __init__(self, holder, balance=0):
#         BankAccount.total_accounts += 1
#         self.holder  = holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited ₹{amount:,} → {self.holder}'s balance: ₹{self.balance:,}")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print(f"Insufficient funds (balance: ₹{self.balance:,})")
#         else:
#             self.balance -= amount
#             print(f"Withdrew ₹{amount:,} → {self.holder}'s balance: ₹{self.balance:,}")
#
#     def display(self):
#         print(f"{self.holder} | ₹{self.balance:,} | Bank: {BankAccount.bank_name}")
#
#     @classmethod
#     def get_total(cls): return cls.total_accounts
#
#     def __str__(self): return f"Account[{self.holder}]: ₹{self.balance:,}"
#
# a1 = BankAccount("Snehith", 15000)
# a2 = BankAccount("Priya", 10000)
# a3 = BankAccount("Raj", 500)
# a1.deposit(5000); a2.withdraw(2000); a3.withdraw(1000)
# print(f"Total accounts: {BankAccount.get_total()}")
# BankAccount.bank_name = "NewBank"
# for a in [a1,a2,a3]: a.display()

