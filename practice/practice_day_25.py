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




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. An instance method's first parameter is always:
#    A) cls    B) self    C) obj    D) No required first parameter
# Answer: ___

# Q_MCQ_2. A class method is decorated with:
#    A) @instance    B) @staticmethod    C) @classmethod    D) @method
# Answer: ___

# Q_MCQ_3. A static method:
#    A) Has access to self    B) Has access to cls
#    C) Has access to neither self nor cls    D) Can only be called on instances
# Answer: ___

# Q_MCQ_4. Which is a common use case for a CLASS method?
#    A) Accessing instance attributes    B) Alternative constructor (factory method)
#    C) Utility/helper function          D) Modifying global state
# Answer: ___

# Q_MCQ_5. Temperature.from_fahrenheit(212)  is likely a:
#    A) Instance method    B) Static method    C) Class method    D) Property
# Answer: ___

# Q_MCQ_6. A static method can be called using:
#    A) Only instance: obj.method()    B) Only class: ClassName.method()
#    C) Both class and instance        D) Only via super()
# Answer: ___

# Q_MCQ_7. Which method type would you use for a utility like  is_valid_email(email)?
#    A) Instance method    B) Class method    C) Static method    D) Abstract method
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. @classmethod decorator changes the first parameter from self to _______.

# FIB_2. cls refers to the _______ (not an instance).

# FIB_3. A @staticmethod cannot access _______ or _______.

# FIB_4. A class method used to create an object from different input format
#         is called a _______ method.

# FIB_5. Instance methods are called on _______.
#         Class methods can be called on _______ OR _______.

# FIB_6. @staticmethod with no self/cls — this makes the method a pure
#         _______ function that belongs to the class namespace.

# FIB_7. To call a class method from within an instance method:
#         self._______ or ClassName._______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Temperature Converter utility class.
#
# Requirements:
#   Define  Temperature  class:
#   - Class variable: unit_system = "Metric"
#   - __init__(self, celsius): store celsius
#   - to_fahrenheit(self): instance method → returns C*(9/5)+32
#   - to_kelvin(self): instance method → returns C+273.15
#   - from_fahrenheit(cls, f): @classmethod factory → Temperature((f-32)*5/9)
#   - from_kelvin(cls, k): @classmethod factory → Temperature(k-273.15)
#   - is_valid(c): @staticmethod → True if -273.15 <= c <= 5778
#   - __str__(self): "{celsius:.2f}°C = {F:.2f}°F = {K:.2f}K"
#
# Then:
#   1. Create t1 from Celsius directly: Temperature(100)
#   2. Create t2 from Fahrenheit: Temperature.from_fahrenheit(32)
#   3. Create t3 from Kelvin: Temperature.from_kelvin(373.15)
#   4. Print str() for all three
#   5. Check validity: is_valid(-300) → False, is_valid(25) → True
#   6. Show unit_system class variable
#
# Expected output:
#   100.00°C = 212.00°F = 373.15K
#   0.00°C = 32.00°F = 273.15K
#   100.00°C = 212.00°F = 373.15K
#   is_valid(-300): False
#   is_valid(25)  : True
#   Unit system: Metric

# YOUR CODE HERE:


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


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: C   Q_MCQ_3: C   Q_MCQ_4: B
# Q_MCQ_5: C   Q_MCQ_6: C   Q_MCQ_7: C

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: cls
# FIB_2: class itself
# FIB_3: self;  cls
# FIB_4: factory (alternative constructor)
# FIB_5: objects (instances);  the class;  instances
# FIB_6: utility / helper
# FIB_7: class_method_name

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# class Temperature:
#     unit_system = "Metric"
#     def __init__(self, celsius):
#         self.celsius = celsius
#     def to_fahrenheit(self): return self.celsius * 9/5 + 32
#     def to_kelvin(self):     return self.celsius + 273.15
#     @classmethod
#     def from_fahrenheit(cls, f): return cls((f - 32) * 5/9)
#     @classmethod
#     def from_kelvin(cls, k):     return cls(k - 273.15)
#     @staticmethod
#     def is_valid(c): return -273.15 <= c <= 5778
#     def __str__(self):
#         return f"{self.celsius:.2f}°C = {self.to_fahrenheit():.2f}°F = {self.to_kelvin():.2f}K"
#
# t1 = Temperature(100)
# t2 = Temperature.from_fahrenheit(32)
# t3 = Temperature.from_kelvin(373.15)
# for t in [t1, t2, t3]: print(t)
# print(f"is_valid(-300): {Temperature.is_valid(-300)}")
# print(f"is_valid(25)  : {Temperature.is_valid(25)}")
# print(f"Unit system: {Temperature.unit_system}")

