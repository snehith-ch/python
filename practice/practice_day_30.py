# ============================================================
# PRACTICE — Day 30: Method Overriding and Abstraction
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Method Overriding
# --------------------------------------------------

# Q1. Predict — child redefines parent method:

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):        # overrides Animal.speak
        print("Dog barks")

class Cat(Animal):
    def speak(self):        # overrides Animal.speak
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.speak()    # prediction:
d.speak()    # prediction:
c.speak()    # prediction:


# Q2. Polymorphism via overriding — same call, different behavior:

animals = [Animal(), Dog(), Cat(), Dog()]
for animal in animals:
    animal.speak()    # prediction (4 lines):


# Q3. Calling parent method with super() — predict:

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle init: {brand}")

    def info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)    # call parent __init__
        self.model = model
        print(f"Car init: {model}")

    def info(self):
        super().info()             # call parent info()
        print(f"Model: {self.model}")

c = Car("Toyota", "Corolla")    # prediction (2 lines):
c.info()                        # prediction (2 lines):


# Q4. Override and extend — predict:

class Shape:
    def area(self):
        return 0

    def describe(self):
        print(f"Area: {self.area()}")    # calls overridden area()!

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s ** 2

for shape in [Circle(5), Square(4)]:
    shape.describe()    # prediction (2 iterations):


# --------------------------------------------------
# SECTION 2: Abstract Classes
# --------------------------------------------------

# Q5. Abstract class — cannot instantiate — predict:

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    def receipt(self):
        print("Receipt generated")    # concrete method in abstract class

# p = Payment()    # uncomment → prediction (error?):


# Q6. Must implement all abstract methods — predict:

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} in cash")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} by card")

c = CashPayment()
c.pay(500)        # prediction:
c.receipt()       # prediction (inherited from abstract class):

k = CardPayment()
k.pay(1200)       # prediction:


# Q7. Partial implementation — predict the error:

class Incomplete(Payment):
    pass    # did NOT implement pay()

# obj = Incomplete()    # uncomment → prediction (error?):


# Q8. Abstract class with data — predict:

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def introduce(self):
        print(f"I am {self.name}")
        self.speak()    # calls child's speak()!

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

d = Dog("Rex")
d.introduce()    # prediction (2 lines):

c = Cat("Whiskers")
c.introduce()    # prediction (2 lines):


# --------------------------------------------------
# SECTION 3: Write Code
# --------------------------------------------------

# Q9. Create an abstract class Appliance:
#   - Abstract method: turn_on()
#   - Abstract method: turn_off()
#   - Concrete method: status() prints "Appliance is ready"
# Create Fan and AC subclasses. Both implement turn_on/turn_off.
# Test all methods.

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict ALL output — mix of override and super():

class Base:
    def greet(self):
        print("Hello from Base")
        return "Base"

class Mid(Base):
    def greet(self):
        result = super().greet()     # calls Base.greet
        print(f"Mid received: {result}")
        return "Mid"

class Top(Mid):
    def greet(self):
        result = super().greet()     # calls Mid.greet (which calls Base.greet)
        print(f"Top received: {result}")

t = Top()
t.greet()    # prediction (3 lines in what order?):


# BONUS 2: Can an abstract method have a body? Predict:

from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def process(self):
        print("Base process — can still have body!")

class Child(Base):
    def process(self):
        super().process()    # can call abstract method's body!
        print("Child process")

c = Child()
c.process()    # prediction:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Method overriding occurs when:
#    A) Parent calls child's method    B) Child redefines a method from parent
#    C) Two classes have the same name    D) A method has two implementations
# Answer: ___

# Q_MCQ_2. Abstract classes CANNOT be:
#    A) Inherited    B) Instantiated (cannot create objects directly)
#    C) Used as parents    D) Extended
# Answer: ___

# Q_MCQ_3. @abstractmethod makes a method:
#    A) Private    B) Compulsory to override in child classes
#    C) Optional to override    D) A class method
# Answer: ___

# Q_MCQ_4. To create an abstract class, inherit from:
#    A) object    B) Abstract    C) ABC    D) AbstractBase
# Answer: ___

# Q_MCQ_5. super().speak()  in a child class calls:
#    A) The child's speak()    B) The parent class's speak()
#    C) The grandparent's speak()    D) Python's built-in speak()
# Answer: ___

# Q_MCQ_6. If a child class does NOT implement all abstract methods:
#    A) It inherits the abstract methods as-is    B) TypeError when instantiating
#    C) SyntaxError    D) The methods become optional
# Answer: ___

# Q_MCQ_7. Python DOES NOT support method overloading (same name, different params)
#           natively. The Pythonic alternative is:
#    A) Create multiple classes    B) Use *args/**kwargs with conditions
#    C) Use C++ extensions         D) Use decorator @overload only
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. from abc import _______ to create abstract base classes.

# FIB_2. @_______ decorator marks a method as abstract.

# FIB_3. Abstract class cannot be _______ directly.

# FIB_4. A child must _______ all abstract methods; otherwise it too
#         becomes _______.

# FIB_5. super().method() lets the child call the _______ version of a method.

# FIB_6. Polymorphism allows different classes to be used _______ through
#         a common interface.

# FIB_7. ABCMeta is the _______ that makes a class abstract.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Payment Gateway System with abstract interface.
#
# Requirements:
#   Abstract  PaymentMethod(ABC):
#   - @abstractmethod process_payment(amount)
#   - @abstractmethod validate()
#   - @abstractmethod get_fee(amount) → float
#   - Concrete method: complete_payment(amount):
#       if self.validate(): show fee, call process_payment, print "✅ Complete"
#       else: print "❌ Validation failed"
#
#   Implement 3 concrete classes:
#   CreditCard(PaymentMethod):
#     - __init__(card_number): store card (must be 16 digits)
#     - validate(): card_number is 16-digit string
#     - get_fee(amount): 2% of amount
#     - process_payment(amount): print "💳 Charged ₹{amount} to card ...{last4}"
#
#   UPI(PaymentMethod):
#     - __init__(upi_id): e.g. "user@okicici"
#     - validate(): upi_id contains @
#     - get_fee(amount): 0
#     - process_payment(amount): print "📱 Sent ₹{amount} via {upi_id}"
#
#   Crypto(PaymentMethod):
#     - __init__(wallet): wallet address string
#     - validate(): len(wallet) >= 26
#     - get_fee(amount): 0.5%
#     - process_payment(amount): print "₿ Transferred {amount} BTC equivalent"
#
# Demonstrate:
#   1. Try to instantiate PaymentMethod() → TypeError
#   2. Create all 3, call complete_payment(1000) on each
#   3. Test an INVALID CreditCard (wrong length) — show validation fail

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "Animal makes a sound", "Dog barks", "Cat meows"

# Q2: "Animal makes a sound", "Dog barks", "Cat meows", "Dog barks"

# Q3: "Vehicle init: Toyota", "Car init: Corolla"
#     "Brand: Toyota", "Model: Corolla"

# Q4: "Area: 78.5", "Area: 16"

# Q5: TypeError: Can't instantiate abstract class Payment with abstract method pay

# Q6: "Paid Rs.500 in cash", "Receipt generated", "Paid Rs.1200 by card"

# Q7: TypeError: Can't instantiate abstract class Incomplete with abstract method pay

# Q8: "I am Rex", "Woof!", "I am Whiskers", "Meow!"

# BONUS 1: "Hello from Base", "Mid received: Base", "Top received: Mid"

# BONUS 2: "Base process — can still have body!", "Child process"
#          Yes — abstract methods CAN have a body, accessible via super()


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: C
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: ABC
# FIB_2: abstractmethod
# FIB_3: instantiated
# FIB_4: override;  abstract
# FIB_5: parent's
# FIB_6: interchangeably
# FIB_7: metaclass

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# from abc import ABC, abstractmethod
# class PaymentMethod(ABC):
#     @abstractmethod
#     def process_payment(self, amount): pass
#     @abstractmethod
#     def validate(self): pass
#     @abstractmethod
#     def get_fee(self, amount): pass
#     def complete_payment(self, amount):
#         if self.validate():
#             fee = self.get_fee(amount)
#             print(f"  Fee: ₹{fee:.2f}")
#             self.process_payment(amount)
#             print(f"  ✅ Payment of ₹{amount} complete!")
#         else:
#             print("  ❌ Validation failed — payment cancelled.")
#
# class CreditCard(PaymentMethod):
#     def __init__(self, card): self.card = card
#     def validate(self): return len(str(self.card)) == 16 and str(self.card).isdigit()
#     def get_fee(self, amt): return amt * 0.02
#     def process_payment(self, amt): print(f"  💳 Charged ₹{amt} to card ...{str(self.card)[-4:]}")
#
# class UPI(PaymentMethod):
#     def __init__(self, uid): self.uid = uid
#     def validate(self): return '@' in self.uid
#     def get_fee(self, amt): return 0
#     def process_payment(self, amt): print(f"  📱 Sent ₹{amt} via {self.uid}")
#
# class Crypto(PaymentMethod):
#     def __init__(self, wallet): self.wallet = wallet
#     def validate(self): return len(self.wallet) >= 26
#     def get_fee(self, amt): return amt * 0.005
#     def process_payment(self, amt): print(f"  ₿ Transferred ₹{amt} equivalent in crypto")
#
# try: PaymentMethod()
# except TypeError as e: print(f"TypeError: {e}")
# for p in [CreditCard("1234567890123456"), UPI("snehith@okicici"), Crypto("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")]:
#     print(type(p).__name__ + ":")
#     p.complete_payment(1000)
# print("Invalid card:"); CreditCard("123").complete_payment(1000)

