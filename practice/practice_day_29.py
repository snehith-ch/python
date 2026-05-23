# ============================================================
# PRACTICE — Day 29: Multiple Inheritance and Polymorphism
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Multiple Inheritance
# --------------------------------------------------

# Q1. Predict — child inherits from two parents:

class Father:
    def skills(self):
        print("Father: Coding, Cooking")

class Mother:
    def skills(self):
        print("Mother: Teaching, Painting")

class Child(Father, Mother):
    pass

c = Child()
c.skills()    # prediction (Father or Mother? left-to-right MRO):


# Q2. MRO — Method Resolution Order — predict:

class A:
    def hello(self):
        print("A.hello")

class B(A):
    def hello(self):
        print("B.hello")

class C(A):
    def hello(self):
        print("C.hello")

class D(B, C):
    pass

d = D()
d.hello()                # prediction:
print(D.__mro__)         # prediction (order): D → ? → ? → ? → object


# Q3. Multiple inheritance constructor — predict:

class P:
    def __init__(self):
        print("P init")

class Q:
    def __init__(self):
        print("Q init")

class R(P, Q):
    pass    # no own __init__ → which parent's __init__ runs?

r = R()    # prediction:


# Q4. Multiple inheritance with own constructor — predict:

class Fly:
    def __init__(self):
        self.can_fly = True

class Swim:
    def __init__(self):
        self.can_swim = True

class Duck(Fly, Swim):
    def __init__(self):
        Fly.__init__(self)
        Swim.__init__(self)

    def abilities(self):
        print(f"Fly: {self.can_fly}, Swim: {self.can_swim}")

d = Duck()
d.abilities()    # prediction:


# --------------------------------------------------
# SECTION 2: Operator Overloading (Polymorphism)
# --------------------------------------------------

# Q5. + operator — predict:

print(10 + 20)           # prediction:
print("Hello" + " World")  # prediction:
print([1, 2] + [3, 4])  # prediction:


# Q6. __add__ magic method — predict:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2    # calls __add__
print(v3)       # prediction (calls __str__):


# Q7. Other magic methods — predict:

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Rs.{self.amount}"

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __mul__(self, factor):
        return Money(self.amount * factor)

    def __gt__(self, other):
        return self.amount > other.amount

m1 = Money(500)
m2 = Money(300)

print(m1 + m2)    # prediction:
print(m1 - m2)    # prediction:
print(m1 * 3)     # prediction:
print(m1 > m2)    # prediction:
print(str(m1))    # prediction:


# Q8. __len__ and __eq__ — predict:

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return self.items == other.items

a = MyList([1, 2, 3])
b = MyList([1, 2, 3])
c = MyList([4, 5])

print(len(a))        # prediction:
print(len(c))        # prediction:
print(a == b)        # prediction:
print(a == c)        # prediction:


# --------------------------------------------------
# SECTION 3: Write Code
# --------------------------------------------------

# Q9. Create a class Temperature:
#   - Constructor: value (in celsius)
#   - __str__: returns "{value}°C"
#   - __add__: returns new Temperature with sum of values
#   - __gt__: returns True if self.value > other.value
# Test with Temperature(20) + Temperature(15) and Temperature(30) > Temperature(25).

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict the full MRO — trace carefully:

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print([cls.__name__ for cls in D.__mro__])  # prediction (names only):


# BONUS 2: Predict — overloading * for repetition:

class Sentence:
    def __init__(self, text):
        self.text = text

    def __mul__(self, n):
        return Sentence(self.text * n)

    def __str__(self):
        return self.text

s = Sentence("ha")
print(s * 3)       # prediction:


# BONUS 3: What magic methods correspond to these operators?
# Fill in the blanks:
# +   → __add__
# -   → ?
# *   → ?
# /   → ?
# ==  → ?
# <   → ?
# len()→ ?
# str()→ ?

# YOUR ANSWERS:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. class C(A, B) — Python looks up a method in order:
#    A) B → A → C    B) C → A → B    C) C → B → A    D) A → B → C
# Answer: ___

# Q_MCQ_2. Which dunder method overloads the  +  operator?
#    A) __plus__    B) __add__    C) __sum__    D) __append__
# Answer: ___

# Q_MCQ_3. len(obj)  calls which method?
#    A) __size__    B) __length__    C) __len__    D) obj.length()
# Answer: ___

# Q_MCQ_4. __str__(self)  is called when you use:
#    A) repr(obj)    B) str(obj) or print(obj)    C) hash(obj)    D) id(obj)
# Answer: ___

# Q_MCQ_5. The diamond problem in multiple inheritance occurs when:
#    A) Two classes have the same variable name
#    B) A class inherits from two classes that share a common ancestor
#    C) A class has more than 4 levels of inheritance
#    D) super() is used in multiple inheritance
# Answer: ___

# Q_MCQ_6. v1 = Vector(1,2); v2 = Vector(3,4); v1 + v2  would call:
#    A) v1.__plus__(v2)    B) v1.__add__(v2)    C) add(v1,v2)    D) Vector.add(v1,v2)
# Answer: ___

# Q_MCQ_7. __eq__(self, other)  overloads:
#    A) >=    B) ==    C) !=    D) <=
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. MRO stands for _______ and determines method lookup order.

# FIB_2. print(C.__mro__)  for class C(A,B) shows: C → _______ → _______ → object.

# FIB_3. v1 * 3  calls v1._______(3).

# FIB_4. __repr__  is meant for _______ representation; __str__ for _______ output.

# FIB_5. a < b  calls a._______(b).

# FIB_6. class C(A, B) — super() in C follows _______ order.

# FIB_7. To overload  -  operator: define _______ method.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Smart Vector Class with full operator overloading.
#
# Requirements:
#   Define  Vector  class:
#   - __init__(x, y)
#   - __add__(other): component-wise add → Vector(x1+x2, y1+y2)
#   - __sub__(other): component-wise subtract
#   - __mul__(scalar): Vector(x*scalar, y*scalar)
#   - __eq__(other): True if x and y both equal
#   - __str__: "Vector(x, y)"
#   - __repr__: "Vector(x={x}, y={y})"
#   - magnitude(): returns sqrt(x²+y²) using math.sqrt
#   - __len__: returns int(magnitude())  [so len() works]
#
# Also create two mixin classes:
#   Printable: has print_info() method that prints type + str(self)
#   Comparable: has is_larger_than(other) → magnitude > other.magnitude
#
#   class SmartVector(Vector, Printable, Comparable): pass
#
# Demonstrate:
#   v1 = SmartVector(3, 4); v2 = SmartVector(1, 2)
#   1. v1 + v2, v1 - v2, v1 * 2
#   2. v1 == SmartVector(3,4) → True
#   3. len(v1) → 5
#   4. v1.magnitude() → 5.0
#   5. v1.print_info()
#   6. v1.is_larger_than(v2)
#   7. Print SmartVector.__mro__

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "Father: Coding, Cooking" — left-to-right MRO, Father comes first

# Q2: "B.hello", MRO: D → B → C → A → object

# Q3: "P init" — only first parent's __init__ runs (MRO: R → P → Q → object)

# Q4: "Fly: True, Swim: True"

# Q5: 30, "Hello World", [1, 2, 3, 4]

# Q6: "Vector(4, 6)"

# Q7: Rs.800, Rs.200, Rs.1500, True, Rs.500

# Q8: 3, 2, True, False

# BONUS 1: ['D', 'B', 'C', 'A', 'object']

# BONUS 2: "hahaha"

# BONUS 3: - → __sub__, * → __mul__, / → __truediv__,
#          == → __eq__, < → __lt__, len() → __len__, str() → __str__


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: C   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: Method Resolution Order
# FIB_2: A;  B
# FIB_3: __mul__
# FIB_4: developer/unambiguous;  user-friendly
# FIB_5: __lt__
# FIB_6: MRO (left-to-right)
# FIB_7: __sub__

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import math
# class Vector:
#     def __init__(self, x, y): self.x, self.y = x, y
#     def __add__(self, o): return Vector(self.x+o.x, self.y+o.y)
#     def __sub__(self, o): return Vector(self.x-o.x, self.y-o.y)
#     def __mul__(self, s): return Vector(self.x*s, self.y*s)
#     def __eq__(self, o): return self.x==o.x and self.y==o.y
#     def __str__(self): return f"Vector({self.x}, {self.y})"
#     def __repr__(self): return f"Vector(x={self.x}, y={self.y})"
#     def magnitude(self): return math.sqrt(self.x**2 + self.y**2)
#     def __len__(self): return int(self.magnitude())
#
# class Printable:
#     def print_info(self): print(f"[{type(self).__name__}] {str(self)}")
#
# class Comparable:
#     def is_larger_than(self, other): return self.magnitude() > other.magnitude()
#
# class SmartVector(Vector, Printable, Comparable): pass
#
# v1, v2 = SmartVector(3,4), SmartVector(1,2)
# print(v1+v2, v1-v2, v1*2)
# print(f"v1==SmartVector(3,4): {v1==SmartVector(3,4)}")
# print(f"len(v1)={len(v1)}  magnitude={v1.magnitude()}")
# v1.print_info()
# print(f"v1 larger than v2: {v1.is_larger_than(v2)}")
# print("MRO:", [c.__name__ for c in SmartVector.__mro__])

