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
