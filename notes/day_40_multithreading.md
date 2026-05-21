# Day 40 — Multithreading

← [Day 39](day_39_database_mysql.md) | [Index](00_INDEX.md) | [Day 41](day_41_decorators_generators.md) →

---

## Quick Revision — Day 40

| # | Key Point |
|---|-----------|
| 1 | Multitasking = executing several tasks simultaneously |
| 2 | Two types: **process-based** (multi-processing, OS level) and **thread-based** (multi-threading, programmatic level) |
| 3 | Each independent part of a program is called one **thread** |
| 4 | Every Python program by default has one thread: the **main thread** |
| 5 | Python module for multithreading: `import threading` (or `from threading import *`) |
| 6 | `Thread(target=func, args=(...))` — create a thread targeting a function |
| 7 | `t.start()` — start thread execution; `t.join()` — wait for thread to finish |
| 8 | Single-thread program: 14 seconds; Multi-thread program: **7 seconds** (50% time reduction) |
| 9 | Output of multi-threaded programs is **unpredictable** — threads run in parallel |
| 10 | 3 ways to create threads: without class, by extending Thread class, without extending Thread class |

---

## Navigation

- **Pre-requisite:** [Day 39](day_39_database_mysql.md) — MySQL database connectivity
- **Next:** [Day 41](day_41_decorators_generators.md) — Decorators and Generators
- **Related:** [Day 32](day_32_exception_advanced_custom.md) — try-except for error handling in threads

---

## Code Created This Day

| Item | Name / Example | Purpose |
|------|----------------|---------|
| Module | `threading` | Built-in multithreading module |
| Program | `thread1.py` | Main thread demo, get/set thread name |
| Program | `thread2.py` | Single-thread vs multi-thread time comparison |
| Class | `Thread` | Built-in class to create thread objects |
| Attribute | `target` | Which function the thread should execute |
| Attribute | `args` | Arguments tuple to pass to the target function |
| Method | `t.start()` | Start a thread |
| Method | `t.join()` | Wait for a thread to complete |
| Method | `threading.current_thread()` | Get the currently executing thread |
| Module | `time` | Used to measure execution time (`time.time()`) |

---

## 1. Multitasking — Core Concept

```
Multitasking
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Executing several tasks simultaneously
Main advantage: improve performance by reducing response time

Type 1: Process-Based Multitasking (Multi-Processing)
  → Each task is a separate independent process
  → Managed by the OS (Operating System level)
  → Memory NOT shared between processes
  → Example: PyCharm open + file downloading + recording meeting

Type 2: Thread-Based Multitasking (Multi-Threading)
  → Each task is a separate independent part of the SAME program
  → Each independent part = one thread
  → Memory CAN BE shared between threads
  → Best suitable for PROGRAMMATIC level (Python programs)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> **We use thread-based multitasking in Python** — executing functions of the same program in parallel. Process-based multitasking is for OS-level tasks like running separate applications.

### 1.1 Application Areas of Multithreading

- Multimedia and graphics / animations
- Video games
- Web application services

---

## 2. Main Thread

```python
import threading

# Every Python program has one default thread: main thread
print("Current executing thread:", threading.current_thread().name)
# Output: main

# Change the thread name
threading.current_thread().name = "my_thread"
print("Current executing thread:", threading.current_thread().name)
# Output: my_thread
```

> Every Python program by default contains **one thread** called the **main thread**. Even without any threading code, the program runs under the main thread.

---

## 3. Single Thread vs Multi-Thread — Time Comparison

### 3.1 Single Thread Program (14 seconds)

```python
import time

def square(numbers):
    for n in numbers:
        time.sleep(1)    # 1 second delay per number
        print(f"Square: {n*n}")

def cube(numbers):
    for n in numbers:
        time.sleep(1)
        print(f"Cube: {n*n*n}")


numbers = [2, 3, 4, 5, 6, 7]

t = time.time()

square(numbers)    # executes first — takes ~6 seconds
cube(numbers)      # executes after — takes another ~6 seconds

print(f"Done in {time.time() - t:.2f} seconds")
# Output: Done in ~14 seconds
```

**Flow:** `square()` runs completely → then `cube()` starts. Total = 14 seconds.

### 3.2 Multi-Thread Program (7 seconds)

```python
from threading import *
import time

def square(numbers):
    for n in numbers:
        time.sleep(1)
        print(f"Square: {n*n}")

def cube(numbers):
    for n in numbers:
        time.sleep(1)
        print(f"Cube: {n*n*n}")


numbers = [2, 3, 4, 5, 6, 7]

t = time.time()

# Create threads
T1 = Thread(target=square, args=(numbers,))    # thread for square
T2 = Thread(target=cube,   args=(numbers,))    # thread for cube

# Start both threads
T1.start()
T2.start()

# Wait for both to finish
T1.join()
T2.join()

print(f"Done in {time.time() - t:.2f} seconds")
# Output: Done in ~7 seconds (50% time reduction!)
```

**Flow:** `square()` and `cube()` run **at the same time**. Total = 7 seconds.

```
Time Comparison
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Single-thread:  square → cube (sequential)  = 14 sec
Multi-thread:   square + cube (parallel)    =  7 sec
                                  ↑ 50% faster
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> **Output of multithreading programs is unpredictable.** Since multiple threads run in parallel, you cannot expect a fixed order. Output varies from run to run. This can be fixed with synchronization techniques (covered later).

---

## 4. Three Ways to Create Threads

### Way 1: Without Using Any Class

```python
from threading import *

def f1():
    for i in range(10):
        print("Thread executing f1:", i)

# Create thread without any class (no `class` keyword used)
t = Thread(target=f1)    # no args needed since f1 has no parameters
t.start()

# Main thread executes this while t executes f1
print("Main thread executing")
```

> "Without using any class" means you don't define a `class` with the `class` keyword. You use the built-in `Thread` class directly.

**Two threads running:**
- `t` → executes `f1()`
- `main thread` → executes the `print` statement

Output is unpredictable — main and thread output interleave differently each run.

### Way 2: By Extending Thread Class

```python
from threading import *

class MyThread(Thread):    # extend (inherit from) Thread class
    def run(self):         # override run() method
        for i in range(10):
            print("MyThread:", i)

t = MyThread()
t.start()
print("Main thread")
```

### Way 3: Without Extending Thread Class

```python
from threading import *

class MyTask:              # NOT extending Thread class
    def task(self):
        for i in range(10):
            print("Task thread:", i)

obj = MyTask()
t = Thread(target=obj.task)    # pass method as target
t.start()
print("Main thread")
```

---

## 5. Thread Attributes — Quick Reference

| Attribute / Method | Description |
|---------------------|-------------|
| `Thread(target=func, args=(val,))` | Create a thread targeting `func` with arguments |
| `t.start()` | Begin thread execution |
| `t.join()` | Wait (block) until this thread finishes |
| `threading.current_thread().name` | Get name of currently running thread |
| `threading.current_thread().name = "name"` | Set a custom name for the thread |

---

## 6. Process-Based vs Thread-Based Multitasking

```
Feature              Process-Based         Thread-Based
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Also called          Multi-processing      Multi-threading
Level                OS level              Programmatic level
Memory sharing       No (separate memory)  Yes (shared memory)
If one fails         Others unaffected     May affect others
Who manages          Operating system      Python threading module
Python use           Rarely needed         Commonly used
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Student Q&A

> **Student Question:** What is multitasking and what are its types?
> **Answer:** Multitasking means executing several tasks simultaneously. There are two types: (1) Process-based multitasking — each task is a separate independent process managed by the OS, suitable for OS-level operations. (2) Thread-based multitasking — each task is a separate independent part of the same program, suitable for programmatic level. In Python, we use thread-based multitasking using the `threading` module.

> **Student Question:** What is the main thread?
> **Answer:** Every Python program, by default, contains exactly one thread called the main thread. All Python code runs under this main thread unless you explicitly create additional threads. You can access it with `threading.current_thread()` and check its name (default: `"MainThread"`).

> **Student Question:** What is the difference between `start()` and `join()`?
> **Answer:** `t.start()` begins executing the thread — it starts the thread and immediately returns, allowing other code (main thread or other threads) to continue. `t.join()` makes the calling thread wait until thread `t` has finished. Typically you call `start()` on all threads first, then `join()` on all threads to wait for them to complete.

> **Student Question:** Why is multithreading output unpredictable?
> **Answer:** In a multithreaded program, multiple threads execute in parallel and share CPU time. The OS scheduler decides which thread runs at any given moment, and this varies between runs. So the interleaving of output from different threads is not fixed. You can control this with synchronization techniques (locks/semaphores) to get a predictable order.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TypeError: target must be callable` | Passed function result instead of function name | Use `target=func` not `target=func()` |
| `TypeError: args must be a tuple` | Passed a non-tuple as `args` | Use `args=(val,)` — note the comma for single-element tuple |
| Thread never starts | Forgot to call `t.start()` | Always call `t.start()` after creating the thread |
| Program ends before thread finishes | No `t.join()` call | Add `t.join()` to wait for threads to complete |

---

## Interview Questions

**Q: What is multithreading in Python?**
A: Multithreading is a form of thread-based multitasking where multiple threads of the same program execute simultaneously. Python provides the built-in `threading` module with a `Thread` class. Each thread targets a function (via `target=`) and runs it independently. This improves performance by reducing execution time — tasks that run sequentially in 14 seconds can run in 7 seconds with two threads.

**Q: What is the difference between process-based and thread-based multitasking?**
A: Process-based multitasking (multi-processing) runs each task as a separate independent process managed by the OS. Memory is not shared between processes. Thread-based multitasking (multi-threading) runs multiple independent parts of the same program as threads. Memory can be shared between threads. Thread-based is best for Python programming; process-based is for OS-level tasks.

**Q: What are the three ways to create threads in Python?**
A: (1) Without using any class — directly use `Thread(target=func)` with no class definition. (2) By extending Thread class — create a class that inherits from `Thread` and override the `run()` method. (3) Without extending Thread class — create any class with a method, then pass that method as `Thread(target=obj.method)`.

**Q: What does `t.join()` do?**
A: `t.join()` makes the current thread (typically main thread) wait until thread `t` finishes executing. Without `join()`, the main thread may end before other threads complete. `join()` ensures the program waits for all threads to finish before moving on.

---

## Try It Yourself

**Exercise 1:** Create a multithreaded program with two functions: one prints even numbers (0–8) and another prints odd numbers (1–9). Each number has a 0.5 second delay. Run them in separate threads and compare with sequential execution.

<details><summary>Answer</summary>

```python
from threading import *
import time

def print_even():
    for i in range(0, 10, 2):
        time.sleep(0.5)
        print(f"Even: {i}")

def print_odd():
    for i in range(1, 10, 2):
        time.sleep(0.5)
        print(f"Odd: {i}")

t = time.time()
T1 = Thread(target=print_even)
T2 = Thread(target=print_odd)
T1.start()
T2.start()
T1.join()
T2.join()
print(f"Done in {time.time() - t:.2f}s")
```
</details>

---

**Exercise 2:** Create a thread by extending the Thread class. Override the `run()` method to print "Hello from custom thread" 5 times.

<details><summary>Answer</summary>

```python
from threading import *

class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("Hello from custom thread", i)

t = MyThread()
t.start()
t.join()
```
</details>
