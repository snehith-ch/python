# ============================================================
# PRACTICE — Day 18: Lambda, filter(), map(), reduce()
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: LAMBDA BASICS
# --------------------------------------------------

# Q1. Predict the output — trace the lambda:

square = lambda n: n * n

print(square(5))    # prediction:
print(square(0))    # prediction:
print(square(-3))   # prediction:


# Q2. Lambda with two arguments — predict:

add = lambda a, b: a + b
mul = lambda a, b: a * b

print(add(10, 20))   # prediction:
print(mul(4, 5))     # prediction:
print(add(add(1, 2), mul(3, 4)))   # prediction — trace carefully:


# Q3. Lambda with a condition — predict:

is_even = lambda n: n % 2 == 0

print(is_even(4))    # prediction:
print(is_even(7))    # prediction:
print(is_even(0))    # prediction:


# Q4. Predict what is returned — does lambda use 'return'?

result = (lambda x: x + 10)(5)   # immediately invoked
print(result)   # prediction:


# Q5. Write lambdas for each of these — then test:
# a) double(n): returns n * 2
# b) greeting(name): returns "Hello, " + name
# c) absolute(n): returns n if n >= 0, else -n (hint: use a ternary: x if cond else y)

# YOUR CODE HERE:


# --------------------------------------------------
# SECTION 2: filter()
# --------------------------------------------------

# Q6. Predict the output — what gets filtered?

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda n: n % 2 == 0, nums))
odds  = list(filter(lambda n: n % 2 != 0, nums))

print(evens)   # prediction:
print(odds)    # prediction:


# Q7. Predict the output — filter strings by length:

words = ["hi", "python", "ok", "programming", "code", "ai"]
long_words = list(filter(lambda w: len(w) > 4, words))

print(long_words)   # prediction:


# Q8. Predict the output — filter out negatives:

numbers = [-5, -3, 0, 2, 4, -1, 8]
positives = list(filter(lambda n: n > 0, numbers))

print(positives)   # prediction:


# Q9. What is the type returned by filter() BEFORE wrapping in list()?

nums = [1, 2, 3]
result = filter(lambda n: n > 1, nums)

print(type(result))   # prediction: int? list? filter object?
print(result)         # prediction: shows values or object?
print(list(result))   # prediction:


# --------------------------------------------------
# SECTION 3: map()
# --------------------------------------------------

# Q10. Predict the output — map applies to ALL elements:

nums = [1, 2, 3, 4, 5]

squares  = list(map(lambda n: n ** 2, nums))
doubled  = list(map(lambda n: n * 2, nums))

print(squares)    # prediction:
print(doubled)    # prediction:
print(len(squares) == len(nums))   # prediction: True or False?


# Q11. Compare filter vs map — predict:

nums = [1, 2, 3, 4, 5, 6]

filtered = list(filter(lambda n: n > 3, nums))   # keeps only some
mapped   = list(map(lambda n: n + 10, nums))     # transforms all

print(filtered)    # prediction:
print(mapped)      # prediction:
print(len(filtered), len(mapped))   # prediction — same length?


# Q12. map() with strings — predict:

words = ["hello", "python", "world"]
upper = list(map(lambda w: w.upper(), words))
lens  = list(map(lambda w: len(w), words))

print(upper)   # prediction:
print(lens)    # prediction:


# Q13. Write your own map equivalent:
# Without using map(), apply a function to every element in a list.
# double_all(nums): returns a new list where every element is doubled.

# YOUR CODE HERE:
# Then compare with: list(map(lambda n: n*2, nums))


# --------------------------------------------------
# SECTION 4: reduce()
# --------------------------------------------------

# Q14. Predict the output — trace reduce step by step:

from functools import reduce

nums = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, nums)
print(total)   # prediction — show your trace:
# Step 1: 1 + 2 = 3
# Step 2: 3 + 3 = ???
# ...

product = reduce(lambda a, b: a * b, nums)
print(product)   # prediction:


# Q15. Predict the output — reduce for max:

nums = [3, 7, 2, 9, 1, 6]
maximum = reduce(lambda a, b: a if a > b else b, nums)
print(maximum)   # prediction:


# Q16. Predict the output — reduce concatenates strings:

words = ["Python", " is", " awesome"]
sentence = reduce(lambda a, b: a + b, words)
print(sentence)   # prediction:


# --------------------------------------------------
# SECTION 5: COMBINING ALL THREE
# --------------------------------------------------

# Q17. Predict the output of this pipeline:

from functools import reduce

nums = list(range(1, 11))   # [1, 2, 3, ... 10]

# Step 1: filter out odds (keep evens)
evens = list(filter(lambda n: n % 2 == 0, nums))
print("Evens:", evens)   # prediction:

# Step 2: square all evens
squared = list(map(lambda n: n ** 2, evens))
print("Squared:", squared)   # prediction:

# Step 3: sum all squared evens
total = reduce(lambda a, b: a + b, squared)
print("Total:", total)   # prediction:


# Q18. Rewrite Q17 as a single chained expression (no intermediate variables):
# YOUR CODE HERE (one line):


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1:
# Use filter() and a lambda to find all prime numbers between 1 and 50.
# A prime has no divisors other than 1 and itself.
# Hint: use all(n % i != 0 for i in range(2, n)) as the condition.

# YOUR CODE HERE:


# BONUS 2:
# Given temperatures in Celsius: [-10, 0, 20, 37, 100]
# Use map() to convert to Fahrenheit (F = C * 9/5 + 32).
# Then use filter() to keep only those above 80°F.
# Print both results.

# YOUR CODE HERE:


# BONUS 3:
# Predict ALL output before running:

from functools import reduce

data = [3, 1, 4, 1, 5, 9, 2, 6, 5]

a = list(filter(lambda x: x > 3, data))
b = list(map(lambda x: x * 2, data))
c = reduce(lambda x, y: x + y, data)
d = reduce(lambda x, y: x if x > y else y, data)

print(a)
print(b)
print(c)
print(d)

# Your full prediction:


# BONUS 4:
# Without using map(), filter(), or reduce(), implement:
# - my_filter(func, seq): returns list of elements where func returns True
# - my_map(func, seq): returns list with func applied to every element
# - my_reduce(func, seq): reduces seq to one value using func
# Test each with a lambda and a list.

# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: 25, 0, 9

# Q2: 30, 20, add(3, 12) = 15

# Q3: True, False, True

# Q4: 15

# Q6: [2,4,6,8,10], [1,3,5,7,9]

# Q7: ['python', 'programming', 'code']

# Q8: [2, 4, 8]

# Q9: <class 'filter'>, filter object (not values), [2, 3]

# Q10: [1,4,9,16,25], [2,4,6,8,10], True

# Q11: [4,5,6], [11,12,13,14,15,16]; len 3, len 6 — NOT same length

# Q12: ['HELLO','PYTHON','WORLD'], [5, 6, 5]

# Q14: total=15 (1+2+3+4+5); product=120

# Q15: 9

# Q16: "Python is awesome"

# Q17: Evens:[2,4,6,8,10], Squared:[4,16,36,64,100], Total:220

# BONUS 3:
# [4, 5, 9, 6, 5]
# [6, 2, 8, 2, 10, 18, 4, 12, 10]
# 36
# 9
