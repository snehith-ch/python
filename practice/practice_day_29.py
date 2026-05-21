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
