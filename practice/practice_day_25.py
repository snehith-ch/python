# ============================================================
# PRACTICE — Day 25: Types of Methods
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Instance Methods
# --------------------------------------------------

# Q1. Instance methods use self — predict:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):               # instance method
        return self.width * self.height

    def scale(self, factor):      # instance method with extra param
        self.width *= factor
        self.height *= factor

r = Rectangle(4, 5)
print(r.area())       # prediction:
r.scale(2)
print(r.width)        # prediction:
print(r.height)       # prediction:
print(r.area())       # prediction:


# Q2. Calling instance method on class (not object) — predict:

# Rectangle.area()     # uncomment → prediction (error?):
# Rectangle.area(r)    # uncomment → prediction (works or error?):


# --------------------------------------------------
# SECTION 2: Class Methods
# --------------------------------------------------

# Q3. Class methods use cls — predict:

class Product:
    discount_rate = 0.10    # static variable

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):    # instance method
        return self.price * (1 - Product.discount_rate)

    @classmethod
    def set_discount(cls, rate):   # class method — modifies class variable
        cls.discount_rate = rate

    @classmethod
    def info(cls):
        print(f"Current discount: {cls.discount_rate * 100}%")

p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)

Product.info()             # prediction:
print(p1.final_price())    # prediction:

Product.set_discount(0.20)
Product.info()             # prediction:
print(p1.final_price())    # prediction (rate changed):
print(p2.final_price())    # prediction:


# Q4. Call class method via object — works or error? Predict:

p1.info()    # prediction (called via object, not class name):


# --------------------------------------------------
# SECTION 3: Static Methods
# --------------------------------------------------

# Q5. Static methods — no self, no cls — predict:

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def square(n):
        return n ** 2

# Call via class name
print(MathUtils.add(3, 4))      # prediction:
print(MathUtils.is_even(7))     # prediction:
print(MathUtils.square(5))      # prediction:

# Call via object — also works
m = MathUtils()
print(m.add(10, 20))            # prediction:


# Q6. Static method does NOT access instance or class variables — predict:

class Converter:
    factor = 1.6    # class variable — static method CANNOT access this!

    @staticmethod
    def km_to_miles(km):
        return km * 0.621    # uses direct value, not class variable

    @classmethod
    def km_to_miles_cls(cls, km):
        return km * cls.factor   # class method CAN access class variable

print(Converter.km_to_miles(10))       # prediction:
print(Converter.km_to_miles_cls(10))   # prediction:


# --------------------------------------------------
# SECTION 4: Recognizing Method Types
# --------------------------------------------------

# Q7. Identify the type of each method:

class Demo:
    class_var = 0

    def __init__(self):
        self.inst_var = 1

    def method_a(self):          # type: ?
        return self.inst_var

    @classmethod
    def method_b(cls):           # type: ?
        return cls.class_var

    @staticmethod
    def method_c(x, y):          # type: ?
        return x + y

d = Demo()
print(d.method_a())              # prediction:
print(Demo.method_b())           # prediction:
print(Demo.method_c(3, 7))       # prediction:


# --------------------------------------------------
# SECTION 5: Write Code
# --------------------------------------------------

# Q8. Create a class Temperature:
#   - Instance variable: celsius
#   - Instance method to_fahrenheit(): returns celsius * 9/5 + 32
#   - Class method set_offset(cls, offset): sets class-level offset variable
#   - Static method is_freezing(celsius): returns True if celsius <= 0

# YOUR CODE HERE:


# Q9. Create a class StringUtils with only static methods:
#   - reverse(s): returns reversed string
#   - is_palindrome(s): returns True if s == s reversed
#   - count_vowels(s): returns count of vowels
# Test with "racecar" and "hello".

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict ALL output:

class Vault:
    total = 0

    def __init__(self, amount):
        self.amount = amount
        Vault.total += amount

    def show(self):
        print(f"Vault: {self.amount}, Total: {Vault.total}")

    @classmethod
    def reset(cls):
        cls.total = 0

v1 = Vault(100)
v2 = Vault(200)
v1.show()          # prediction:
v2.show()          # prediction:
Vault.reset()
v1.show()          # prediction (total after reset):


# BONUS 2: What is wrong with this code? Fix it:

class Circle:
    pi = 3.14

    def area(radius):    # missing something?
        return Circle.pi * radius ** 2

# Circle().area(5)   # uncomment — what error? fix it.


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: 20, 8, 10, 80

# Q2: TypeError (area() missing self), Rectangle.area(r) → works, returns 20

# Q3: "Current discount: 10.0%", 45000.0, "Current discount: 20.0%", 40000.0, 16000.0

# Q4: "Current discount: 20.0%" — calling via object works, cls is still Product

# Q5: 7, False, 25, 30

# Q6: 6.21, 16.0

# Q7: method_a=instance, method_b=class, method_c=static; outputs: 1, 0, 10

# BONUS 1: "Vault: 100, Total: 300", "Vault: 200, Total: 300", "Vault: 100, Total: 0"

# BONUS 2: Missing @staticmethod decorator (or add self parameter)
#           Fix: add @staticmethod above def area(radius):
