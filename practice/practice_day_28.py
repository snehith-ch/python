# ============================================================
# PRACTICE — Day 28: Inheritance
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Single Inheritance
# --------------------------------------------------

# Q1. Predict — child inherits parent methods:

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} breathes")

    def eat(self):
        print(f"{self.name} eats")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

d = Dog("Rex")
d.breathe()       # prediction (from parent):
d.eat()           # prediction (from parent):
d.bark()          # prediction (own method):
print(d.name)     # prediction:


# Q2. Child constructor vs parent — predict:

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle: {brand}")

    def start(self):
        print(f"{self.brand} started")

class Car(Vehicle):
    def __init__(self, brand, seats):
        Vehicle.__init__(self, brand)    # call parent constructor
        self.seats = seats
        print(f"Car with {seats} seats")

    def honk(self):
        print("Beep!")

c = Car("Toyota", 5)    # prediction (2 lines):
c.start()               # prediction:
c.honk()                # prediction:


# Q3. isinstance() and issubclass() — predict:

class Shape:
    pass

class Circle(Shape):
    pass

class Square(Shape):
    pass

c = Circle()

print(isinstance(c, Circle))    # prediction:
print(isinstance(c, Shape))     # prediction (parent class?):
print(isinstance(c, Square))    # prediction (sibling class?):

print(issubclass(Circle, Shape))   # prediction:
print(issubclass(Shape, Circle))   # prediction (reverse?):


# --------------------------------------------------
# SECTION 2: Multilevel Inheritance
# --------------------------------------------------

# Q4. Predict — chain of inheritance:

class Grandparent:
    def g_method(self):
        print("Grandparent method")

class Parent(Grandparent):
    def p_method(self):
        print("Parent method")

class Child(Parent):
    def c_method(self):
        print("Child method")

obj = Child()
obj.c_method()     # prediction:
obj.p_method()     # prediction (from parent):
obj.g_method()     # prediction (from grandparent):


# Q5. Multilevel with data — predict:

class A:
    def __init__(self):
        self.a = "A"

class B(A):
    def __init__(self):
        A.__init__(self)
        self.b = "B"

class C(B):
    def __init__(self):
        B.__init__(self)
        self.c = "C"

obj = C()
print(obj.a)    # prediction:
print(obj.b)    # prediction:
print(obj.c)    # prediction:
print(obj.__dict__)   # prediction:


# --------------------------------------------------
# SECTION 3: Hierarchical Inheritance
# --------------------------------------------------

# Q6. Predict — one parent, multiple children:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        Employee.__init__(self, name, salary)
        self.team_size = team_size

    def info(self):
        self.display()
        print(f"Team size: {self.team_size}")

class Intern(Employee):
    def __init__(self, name, salary, duration):
        Employee.__init__(self, name, salary)
        self.duration = duration

    def info(self):
        self.display()
        print(f"Internship duration: {self.duration} months")

m = Manager("Alice", 80000, 10)
i = Intern("Bob", 15000, 6)

m.info()    # prediction (2 lines):
i.info()    # prediction (2 lines):

print(isinstance(m, Employee))    # prediction:
print(isinstance(i, Manager))     # prediction:


# --------------------------------------------------
# SECTION 4: Write Code
# --------------------------------------------------

# Q7. Build a class hierarchy:
#   - Animal: name, sound (instance vars), speak() prints "{name} says {sound}"
#   - Cat(Animal): constructor adds color; purr() prints "{name} purrs"
#   - Kitten(Cat): constructor adds weight; tiny() prints "{name} is a tiny {weight}kg kitten"
# Create a Kitten and call speak(), purr(), and tiny().

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict ALL output:

class X:
    def hello(self):
        print("X.hello")

class Y(X):
    def hello(self):
        print("Y.hello")    # overrides X.hello

class Z(Y):
    pass    # no hello — inherits from Y

z = Z()
z.hello()               # prediction (X or Y?):
print(isinstance(z, X)) # prediction:
print(isinstance(z, Y)) # prediction:


# BONUS 2:
# Use issubclass() to check a 3-level hierarchy:
# class A → class B(A) → class C(B)
# Predict: issubclass(C, A), issubclass(A, C), issubclass(C, B)

class A: pass
class B(A): pass
class C(B): pass

print(issubclass(C, A))    # prediction:
print(issubclass(A, C))    # prediction:
print(issubclass(C, B))    # prediction:
print(issubclass(B, A))    # prediction:




# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. In single inheritance,  class Dog(Animal):  means:
#    A) Dog is a parent of Animal    B) Dog inherits from Animal
#    C) Dog and Animal are the same    D) Animal uses Dog's methods
# Answer: ___

# Q_MCQ_2. super().__init__()  inside a child class calls:
#    A) The child's own __init__    B) The parent class's __init__
#    C) The grandparent's __init__   D) Python's built-in init
# Answer: ___

# Q_MCQ_3. In multilevel inheritance A → B → C:
#    A) C inherits from B only    B) C inherits from both A and B
#    C) B and C are siblings      D) A inherits from C
# Answer: ___

# Q_MCQ_4. isinstance(dog_obj, Animal)  returns True if:
#    A) dog_obj is exactly an Animal instance
#    B) Dog is a subclass of Animal (inherited)
#    C) Both A and B
#    D) Only if Dog doesn't override any Animal methods
# Answer: ___

# Q_MCQ_5. Method overriding means:
#    A) Adding a new method in child    B) Child redefines a method from parent
#    C) Parent calls child's method     D) Removing a parent method
# Answer: ___

# Q_MCQ_6. Hierarchical inheritance means:
#    A) One child, multiple parents    B) Multiple children inherit from one parent
#    C) Children in a chain            D) All classes are siblings
# Answer: ___

# Q_MCQ_7. print(ClassName.__mro__)  shows:
#    A) All attributes of the class    B) The Method Resolution Order (inheritance chain)
#    C) All methods of the class       D) The class's module
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. class Child(Parent): — Child _______ all non-private methods from Parent.

# FIB_2. super() refers to the _______ class in the MRO.

# FIB_3. A → B → C (multilevel): C can access methods from _______ and _______.

# FIB_4. If Dog overrides speak() from Animal, calling dog.speak() runs
#         _______ speak() method.

# FIB_5. issubclass(Dog, Animal)  returns _______ if Dog inherits Animal.

# FIB_6. Hierarchical: Cat(Animal), Dog(Animal), Cow(Animal) — all three
#         share _______ parent class.

# FIB_7. To call the overridden parent method from child: use _______.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Animal Kingdom hierarchy with 3 inheritance types.
#
# Requirements:
# Single:    Dog(Animal)
# Multilevel: GoldenRetriever(Dog)
# Hierarchical: Cat(Animal), Dog(Animal) — both inherit Animal
#
#   Animal: __init__(name, sound), speak(), __str__
#   Dog(Animal): fetch(ball_name), override speak() → "Dog barks: {sound}"
#   Cat(Animal): purr(), override speak() → "Cat meows: {sound}"
#   GoldenRetriever(Dog): add color attribute, override fetch() with detail
#
# Demonstrate:
#   1. Create one of each: Animal, Dog, Cat, GoldenRetriever
#   2. Call speak() on all — show polymorphism
#   3. GoldenRetriever can call both fetch() (from Dog) AND speak()
#   4. isinstance(golden, Dog) → True, isinstance(golden, Animal) → True
#   5. issubclass(GoldenRetriever, Animal) → True
#   6. print(GoldenRetriever.__mro__)
#
# Expected output:
#   Animal Crow: Crow says caw caw
#   Dog Rex: Dog barks: woof
#   Cat Whiskers: Cat meows: meow
#   GoldenRetriever Buddy: Dog barks: woof (color: Golden)
#   Buddy fetching tennis ball with enthusiasm!
#   isinstance(buddy, Animal): True
#   GoldenRetriever MRO: (<class GoldenRetriever>, <class Dog>, <class Animal>, ...)

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: "{Rex} breathes", "{Rex} eats", "{Rex} barks", "Rex"

# Q2: "Vehicle: Toyota", "Car with 5 seats", "{Toyota} started", "Beep!"

# Q3: True, True, False, True, False

# Q4: "Child method", "Parent method", "Grandparent method"

# Q5: "A", "B", "C", {'a': 'A', 'b': 'B', 'c': 'C'}

# Q6: "Name: Alice, Salary: 80000", "Team size: 10",
#     "Name: Bob, Salary: 15000", "Internship duration: 6 months"
#     True, False (i is Intern, not Manager)

# BONUS 1: "Y.hello" (Y overrides X; Z inherits from Y), True, True

# BONUS 2: True, False, True, True


# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: B   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: C
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: inherits
# FIB_2: next (immediate parent)
# FIB_3: B and A (all ancestors)
# FIB_4: Dog's (child's overridden)
# FIB_5: True
# FIB_6: one (Animal)
# FIB_7: super().method_name()

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# class Animal:
#     def __init__(self, name, sound):
#         self.name = name; self.sound = sound
#     def speak(self): print(f"{self.name}: {self.sound}")
#     def __str__(self): return f"Animal({self.name})"
#
# class Dog(Animal):
#     def speak(self): print(f"Dog {self.name}: Dog barks: {self.sound}")
#     def fetch(self, ball): print(f"{self.name} fetches {ball}!")
#
# class Cat(Animal):
#     def speak(self): print(f"Cat {self.name}: Cat meows: {self.sound}")
#     def purr(self): print(f"{self.name} purrs... 😺")
#
# class GoldenRetriever(Dog):
#     def __init__(self, name, sound, color):
#         super().__init__(name, sound)
#         self.color = color
#     def speak(self): print(f"GoldenRetriever {self.name}: Dog barks: {self.sound} (color: {self.color})")
#     def fetch(self, ball): print(f"{self.name} fetches {ball} with enthusiasm!")
#
# a = Animal("Crow","caw caw"); d = Dog("Rex","woof")
# c = Cat("Whiskers","meow"); g = GoldenRetriever("Buddy","woof","Golden")
# for animal in [a,d,c,g]: animal.speak()
# g.fetch("tennis ball")
# print(f"isinstance(g, Animal): {isinstance(g, Animal)}")
# print(f"issubclass(GoldenRetriever, Animal): {issubclass(GoldenRetriever, Animal)}")
# print("MRO:", [cls.__name__ for cls in GoldenRetriever.__mro__])

