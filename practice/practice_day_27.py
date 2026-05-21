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
