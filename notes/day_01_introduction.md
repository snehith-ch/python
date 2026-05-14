# Day 1 — Introduction to Python

## Quick Revision — Day 1
| # | Key Point |
|---|-----------|
| 1 | Python is a **general purpose, high level, interpreted, dynamically typed, case-sensitive** programming language |
| 2 | **General purpose** — can build any type of application (web, data science, AI, gaming, embedded, etc.) |
| 3 | **High level** — no need to write code for memory management or security; Python handles it internally via garbage collector |
| 4 | **Interpreted** — code runs line by line; stops at the first error (unlike compilers that check all at once) |
| 5 | **Dynamically typed** — no need to declare data types; Python assigns them at runtime based on the value |
| 6 | **Case sensitive** — `a` and `A` are different variables |
| 7 | Python was designed by **Guido van Rossum**; first version released in **1991** (version 0.9.0); named after **Monty Python's Flying Circus** |
| 8 | Current stable version used in this course: **Python 3.10.4** |
| 9 | Python programs are **platform independent** — same code runs on Windows, macOS, Linux |
| 10 | Editor used in this course: **PyCharm Community Edition** (also VS Code is recommended) |

---

**Pre-requisite:** None — this is the first session.
**Next:** Day 2 — Installation, application areas, features of Python, PyCharm setup
**Related:** Day 3 — PyCharm project setup and running Python code

---

## Code Created This Day
| Item | Name / Example | Purpose |
|------|----------------|---------|
| No code files | Theory session only | Introduction and concepts |

---

## 1. What Is Python?

Python is a **programming language** used to write code for application development.

```python
# This is how simple Python is — just one line to print output:
print("Welcome")
```

Compare that to Java:
```java
// Java needs this entire structure just to print "Welcome":
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Welcome");
    }
}
```

And C:
```c
#include <stdio.h>
void main() {
    printf("Welcome");
}
```

Python: **one line**. Java: **five lines**. This simplicity is a core reason Python is so popular.

---

## 2. What Type of Programming Language Is Python?

Python is a **general purpose, high level, interpreted, dynamically typed, case-sensitive** programming language.

### 2.1 General Purpose

**General purpose** means Python is not designed for one specific kind of application. You can use it for:
- Web application development (Django, Flask)
- Data science and data analysis
- Artificial intelligence and machine learning
- Network programming
- Gaming applications
- Audio/video processing
- Business applications
- Embedded systems, MATLAB, VLSI
- Automation and scripting

> **Interview Question:** What does "general purpose" mean in the context of Python?
> **Answer:** It means Python is not designed for a specific domain. It can be used to develop any type of application — web apps, data science, AI, gaming, network programming, and more.

### 2.2 High Level

**High level** means you (the programmer) do not need to write any code for low-level activities like:
- **Memory management** — handled automatically by Python's garbage collector
- **Security** — handled internally by Python

This makes Python a programmer-friendly language. You focus only on solving the problem, not managing system resources.

> **Interview Question:** What is a high-level programming language?
> **Answer:** A programming language where the programmer does not need to handle low-level activities like memory management and security. Python manages these internally through its garbage collector and other built-in tools.

### 2.3 Interpreted

**Interpreted** means Python code is executed **line by line**, one line at a time.

| Compiler-based languages | Interpreter-based languages |
|--------------------------|------------------------------|
| Java, C, C++, C#.Net | Python, JavaScript |
| Entire program is checked at once | Code is checked and executed line by line |
| Shows all errors at the end (e.g., "3 errors found") | Stops at the first error and shows only that line |
| Creates a compiled file (.class, .exe) | No compiled file — runs directly |

```
How Python's interpreter works:

Line 1 → check → OK → execute
Line 2 → check → OK → execute
Line 3 → check → ERROR → stop → show error message
(Lines 4, 5, 6... never reached)
```

> **Common Mistake:** Thinking Python has no compiler. Python does compile internally, but as a programmer you never do it explicitly. The interpreter takes care of compilation automatically.

> **Interview Question:** What is the difference between a compiler and an interpreter?
> **Answer:** A compiler checks the entire program at once before execution. An interpreter checks and executes line by line. Python is interpreter-based, so it stops at the first error it finds.

### 2.4 Dynamically Typed

**Dynamically typed** means you do NOT declare the data type of a variable. Python figures it out at runtime based on the value you assign.

```python
# Statically typed (Java, C) — you must specify the type:
# int a = 10;   ← this syntax is INVALID in Python

# Python — dynamically typed:
a = 10          # Python internally assigns: integer type
a = 10.5        # Python internally reassigns: float type
a = "Durga"     # Python internally reassigns: string type

# To check the data type:
print(type(a))  # Output: <class 'str'>
```

> **Exam Tip:** Dynamically typed does NOT mean Python has no data types. Python has many data types — it just assigns them automatically at runtime.

> **Interview Question:** What is dynamic typing in Python?
> **Answer:** In Python, you do not need to declare the data type of a variable. At runtime, based on the value assigned, Python automatically determines and assigns the data type. This is called dynamic typing.

### 2.5 Case Sensitive

**Case sensitive** means Python treats `a` and `A` as completely different names.

```python
a = 10
print(a)   # Output: 10
print(A)   # ERROR: NameError: name 'A' is not defined
```

You must access a variable with the exact same case you used to declare it.

---

## 3. Why Python? (Why Not Java or C++?)

The main reasons Python became the most popular programming language:

1. **Simple syntax** — reads almost like English; very beginner-friendly
2. **Less code** — write the same logic in fewer lines than Java or C++
3. **Huge standard libraries** — ready-made libraries for every domain (pandas, numpy, matplotlib, etc.)
4. **Free and open source** — no license required
5. **Platform independent** — runs on Windows, macOS, Linux, Unix
6. **General purpose** — useful in every field of software development

---

## 4. History of Python

| Fact | Detail |
|------|--------|
| **Creator** | Guido van Rossum |
| **First version** | 0.9.0 — released in **1991** |
| **Name origin** | Named after **Monty Python's Flying Circus** (a BBC TV show the author was watching while writing Python) |
| **Current version** | 3.10.4 (used in this course) |
| **Official website** | www.python.org |

Python was built by taking features from multiple languages:
- Functional programming features → from C
- Object-oriented programming features → from C++
- Scripting language features → from Perl and shell script

---

## 5. Platform Independence

Python is **platform independent** (also called cross-platform). A Python program written on Windows can run on Linux, macOS, or Unix **without any changes**.

```
Your Python Code
      │
      ▼
Python Virtual Machine (PVM)
      │  converts to machine-understandable form
      ▼
Runs on Windows / macOS / Linux / Unix
```

This is different from, say, a compiled C program which produces a platform-specific executable.

---

## 6. Python Editors

The instructor covers this course using **PyCharm Community Edition**.

| Editor | Notes |
|--------|-------|
| **PyCharm Community** | Best for beginners; intelligent code suggestions; free |
| **VS Code** | Also recommended; lightweight; very popular in industry |
| IDLE | Default editor bundled with Python; basic |
| Jupyter Notebook | Popular for data science |
| Spyder | Common in Anaconda/data science |
| Notepad | Can write Python, but not recommended for beginners |

> **Instructor's Recommendation:** Use PyCharm Community Edition or VS Code. Avoid Notepad in the early stages because there are no syntax hints or error indicators.

---

## 7. This Course Structure

| Subject | Duration |
|---------|----------|
| Python Core + Advanced | ~45 days |
| Django + HTML/CSS/JavaScript/jQuery/Bootstrap | ~45 days |
| Django REST Framework (REST API) | ~25–30 days |
| **Total** | **~3.5 to 4 months** |

### Prerequisite chain:
```
Python Core & Advanced
        ↓  (required before)
Django (web framework)
        ↓  (required before)
Django REST Framework (REST API)
```

---

## 8. Student Q&A from Class

> **Student Question (Vishnu):** Does this Python course cover embedded-related programming?
> **Answer:** The course covers Python core and advanced concepts including OOP, exception handling, and more. Embedded developers can learn Python here and then map the knowledge to their domain. The instructor is not an embedded specialist but covers all Python fundamentals and advanced topics.

> **Student Question:** Is Python training helpful for data science?
> **Answer:** Absolutely — Python is a prerequisite for data science. In this course, data science modules like numpy, pandas, and matplotlib basics are covered. Without Python, you cannot move to data science.

> **Student Question:** After finishing Python core and advanced, will we be able to write scripts?
> **Answer:** Yes, undoubtedly. Once the Python core and advanced sessions are complete, you will be writing full scripts for all topics covered.

---

## 9. Key Differences: Compiler vs Interpreter

| Feature | Compiler (Java, C, C++) | Interpreter (Python, JavaScript) |
|---------|-------------------------|----------------------------------|
| Execution | Whole program at once | Line by line |
| Error reporting | All errors shown at end | Stops at first error |
| Output file | Produces .class/.exe file | No compiled output file |
| Speed of finding errors | Slower (must finish compiling) | Faster (stops immediately) |
| Example languages | Java, C, C++, C#.Net | Python, JavaScript |

---

## Common Errors — Day 1 (Conceptual)

| Mistake | What Goes Wrong | Correct Approach |
|---------|-----------------|------------------|
| Declaring variable with a data type like `int a = 10` | SyntaxError — this is Java/C syntax, not Python | Just write `a = 10` |
| Accessing `A` when you declared `a` | NameError: name 'A' is not defined | Match the case exactly: `a` |
| Expecting Python to show all errors at once | Python stops at the first error | Fix errors one at a time |

---

## Interview Questions — Day 1

**Q: What is Python?**
A: Python is a general purpose, high level, interpreted, dynamically typed, and case-sensitive programming language used for writing code for application development.

**Q: Who created Python and when?**
A: Python was created by Guido van Rossum. The first version (0.9.0) was released in 1991. The name was taken from the BBC TV show "Monty Python's Flying Circus."

**Q: What does "dynamically typed" mean?**
A: In Python, you do not specify data types when declaring variables. Python automatically determines the data type at runtime based on the value assigned to the variable.

**Q: What is the difference between a compiler and an interpreter?**
A: A compiler processes the entire source code at once and produces an executable. An interpreter processes code line by line, stopping at the first error. Python uses an interpreter.

**Q: Is Python platform independent?**
A: Yes. Python programs can run on any operating system (Windows, macOS, Linux, Unix) without modification, because Python's virtual machine converts the code to platform-specific machine code internally.

**Q: Why is Python so popular compared to Java and C++?**
A: Python has simple syntax (less code), huge built-in libraries, is free and open source, is platform independent, and can be used in any domain from web development to AI to data science.

**Q: What is a high-level programming language?**
A: A language that abstracts away low-level details like memory management and security. Programmers focus on logic, not system resources. Python is high-level because garbage collection and memory management are handled automatically.

**Q: What is "general purpose" in programming languages?**
A: A general purpose language is not designed for one specific type of application. Python can be used for web apps, data science, AI, gaming, network programming, testing, automation, and more.

---

## Try It Yourself — Day 1

**Exercise 1:** Open Python's interactive shell (IDLE) and type the following. Observe the output:
```python
print("Hello, World!")
a = 10
print(type(a))
a = 3.14
print(type(a))
a = "Python"
print(type(a))
```
*Expected: int, float, str*

**Exercise 2:** Try this in the interactive shell and observe what happens:
```python
x = 100
print(X)   # Note: capital X
```
*Expected: NameError — Python is case sensitive*

**Exercise 3:** Go to www.python.org and find the current stable version. Compare it to 3.10.4 used in class.

**Exercise 4:** In the interactive shell, check the type of these values:
```python
print(type(True))
print(type(None))
print(type(3+4j))
```
*Think: what do you expect before running?*

**Exercise 5:** Write the equivalent of this Python line in Java/C (mentally or on paper):
```python
print("Welcome to Python")
```
*Notice how many more lines Java requires — this shows Python's simplicity.*
