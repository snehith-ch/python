# Day 10 — String Operations and Functions

← [Day 9](day_09_control_flow.md) | [Index](00_INDEX.md) | [Day 11](day_11_strings_advanced_list_intro.md) →

---

## Quick Revision

| # | Question | Answer |
|---|----------|--------|
| 1 | What index does the first character have? | 0 (positive) or `-len(s)` (negative) |
| 2 | What index does the last character have? | `len(s)-1` (positive) or `-1` (negative) |
| 3 | Slicing syntax? | `s[start:stop:step]` — stop is excluded |
| 4 | How to reverse a string? | `s[::-1]` |
| 5 | What does `split()` return? | A **list** of substrings |
| 6 | `capitalize()` vs `title()`? | `capitalize()` — first letter only; `title()` — first letter of every word |
| 7 | What does `swapcase()` do? | Upper becomes lower, lower becomes upper |
| 8 | What does `join()` do? | Joins a list of strings with a separator |
| 9 | Are strings mutable? | No — immutable |
| 10 | What does `replace("a","b")` do? | Returns a NEW string with all `"a"` replaced by `"b"` |

---

## 1. String Indexing

Every character in a string has two indices: **positive** (left to right) and **negative** (right to left).

```
String:   P  y  t  h  o  n
Positive: 0  1  2  3  4  5
Negative:-6 -5 -4 -3 -2 -1
```

```python
s = "Python"

print(s[0])    # P   (first character)
print(s[5])    # n   (last character — index = len-1)
print(s[-1])   # n   (last character, negative index)
print(s[-6])   # P   (first character, negative index)

# IndexError if you go out of range:
# print(s[6])  # IndexError: string index out of range
```

---

## 2. String Slicing

Extract a **substring** using `s[start:stop:step]`.

- `start` — where to begin (included)
- `stop` — where to end (excluded)
- `step` — how many to skip (default = 1)

```python
s = "Python"

print(s[0:3])    # Pyt  (index 0,1,2 — stop 3 excluded)
print(s[2:5])    # tho
print(s[0:6])    # Python
print(s[:])      # Python  (full string)
print(s[:3])     # Pyt  (start defaults to 0)
print(s[3:])     # hon  (stop defaults to end)
```

### Slicing with step

```python
s = "Python"

print(s[0:6:2])    # Pto  (every 2nd character)
print(s[::2])      # Pto
print(s[1::2])     # yhn  (start at 1, every 2nd)
```

### Reverse a string

```python
s = "Python"
print(s[::-1])     # nohtyP  — step of -1 goes right to left
```

---

## 3. String Concatenation and Repetition

```python
# Concatenation — joins strings
first = "Hello"
second = "World"
print(first + " " + second)   # Hello World

# Repetition — repeats a string
print("Ha" * 3)     # HaHaHa
print("-" * 30)     # ────────────────────────────── (separator line)
```

---

## 4. `split()` — string to list

Splits a string into a **list** of substrings. Default separator: whitespace.

```python
sentence = "Python is easy to learn"
words = sentence.split()
print(words)        # ['Python', 'is', 'easy', 'to', 'learn']
print(type(words))  # <class 'list'>

# Custom separator
data = "10,20,30,40"
nums = data.split(",")
print(nums)   # ['10', '20', '30', '40']
```

---

## 5. String Functions

### `capitalize()` — first letter of entire string to uppercase

```python
s = "python programming"
print(s.capitalize())   # Python programming
                        # only the very first letter changes
```

### `title()` — first letter of EVERY word to uppercase

```python
s = "python programming is fun"
print(s.title())   # Python Programming Is Fun
```

### `upper()` and `lower()`

```python
s = "Python"
print(s.upper())   # PYTHON
print(s.lower())   # python
```

### `swapcase()` — flip all cases

```python
s = "Hello World"
print(s.swapcase())   # hELLO wORLD
```

### `count()` — how many times a substring appears

```python
s = "banana"
print(s.count("a"))    # 3
print(s.count("an"))   # 2
print(s.count("na"))   # 2
```

### `replace()` — substitute substrings

Returns a **new string** — original is unchanged.

```python
s = "Hello World"
new_s = s.replace("World", "Python")
print(new_s)   # Hello Python
print(s)       # Hello World  — original unchanged

# Replace all occurrences:
s2 = "aabbaa"
print(s2.replace("a", "x"))   # xxbbxx
```

### `join()` — list to string

Joins elements of a list (or any iterable) with a separator.

```python
words = ["Python", "is", "great"]
result = " ".join(words)
print(result)   # Python is great

# With comma separator:
items = ["apple", "banana", "cherry"]
print(", ".join(items))   # apple, banana, cherry

# No separator:
chars = ["P", "y", "t", "h", "o", "n"]
print("".join(chars))   # Python
```

---

## 6. Sorting a String

Strings are immutable, so you cannot sort in place. Use the split → sort → join pattern.

```python
sentence = "banana apple cherry date"

# Step 1: split into list
words = sentence.split()
# ['banana', 'apple', 'cherry', 'date']

# Step 2: sort the list
words.sort()
# ['apple', 'banana', 'cherry', 'date']

# Step 3: join back to string
sorted_sentence = " ".join(words)
print(sorted_sentence)   # apple banana cherry date
```

---

## 7. Complete Function Reference

| Function | What it does | Example | Output |
|----------|-------------|---------|--------|
| `len(s)` | Length (number of characters) | `len("Python")` | `6` |
| `s[i]` | Single character at index | `"Python"[0]` | `"P"` |
| `s[a:b]` | Slice from a to b-1 | `"Python"[1:4]` | `"yth"` |
| `s[::-1]` | Reverse the string | `"Python"[::-1]` | `"nohtyP"` |
| `s + t` | Concatenate | `"Hi"+"!"` | `"Hi!"` |
| `s * n` | Repeat n times | `"ha"*3` | `"hahaha"` |
| `s.split()` | Split into list | `"a b c".split()` | `["a","b","c"]` |
| `s.capitalize()` | First letter upper | `"hello".capitalize()` | `"Hello"` |
| `s.title()` | Each word capitalized | `"hello world".title()` | `"Hello World"` |
| `s.upper()` | All uppercase | `"hi".upper()` | `"HI"` |
| `s.lower()` | All lowercase | `"HI".lower()` | `"hi"` |
| `s.swapcase()` | Swap all cases | `"Hi".swapcase()` | `"hI"` |
| `s.count(x)` | Count occurrences | `"banana".count("a")` | `3` |
| `s.replace(a,b)` | Replace all a with b | `"cat".replace("c","b")` | `"bat"` |
| `sep.join(list)` | List to string | `",".join(["a","b"])` | `"a,b"` |

---

## 8. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `IndexError: string index out of range` | Index >= len(s) | Use `len(s)-1` as max index |
| `TypeError: 'str' object does not support item assignment` | Trying to change a character | Strings are immutable — use `replace()` instead |
| `join()` error: `sequence item 0: expected str instance, int found` | Trying to join a list with non-strings | Convert to str first: `str(x)` |
| `split()` on comma but forgot the argument | `"a,b".split()` → `['a,b']` | `"a,b".split(",")` |

---

## 9. Interview Questions

1. What is the difference between positive and negative indexing?
2. What does `s[::−1]` do?
3. What does `split()` return?
4. What is the difference between `capitalize()` and `title()`?
5. Are strings mutable or immutable in Python?
6. What does `replace()` return?
7. How do you sort a string alphabetically in Python?
8. What does `join()` do, and what does it take as input?

---

## 10. Try It Yourself

```python
# 1. s = "Hello, World!"
#    Print: first char, last char, reverse, characters 7-11

# 2. Print every other character of "abcdefghij"

# 3. Count how many times "o" appears in "chocolate coconut cookie"

# 4. Replace all spaces with underscores in "Python is fun"

# 5. Split "Monday,Tuesday,Wednesday,Thursday,Friday" by comma,
#    sort alphabetically, join back with " - "

# 6. Given a full name "snehith kumar", print it in Title Case
#    and count how many characters it has (excluding spaces)
```

---

## Code Created in Class

| Code | Purpose |
|------|---------|
| `s[0]`, `s[-1]` | First and last character |
| `s[1:4]` | Slice characters at index 1,2,3 |
| `s[::-1]` | Reverse a string |
| `s.split()` | Split sentence into list of words |
| `s.capitalize()` | Only first letter capitalized |
| `s.title()` | Every word capitalized |
| `s.count("a")` | Count "a" occurrences |
| `s.replace("old","new")` | Substitute substring |
| `" ".join(word_list)` | List of words → single string |
| `split → sort → join` | Sort words in a sentence |
