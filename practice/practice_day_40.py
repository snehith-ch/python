# ============================================================
# PRACTICE — Day 40: Multithreading
# ============================================================
# Instructions:
#   - Predict the output BEFORE running each code block
#   - Write your prediction as a comment, then run to verify
# ============================================================


# --------------------------------------------------
# SECTION 1: Main Thread
# --------------------------------------------------

# Q1. Predict — every Python program has a main thread:

import threading

print(threading.current_thread().name)   # prediction:


# Q2. Rename the main thread — predict:

threading.current_thread().name = "MyMainThread"
print(threading.current_thread().name)   # prediction:


# Q3. from threading import * — predict:

from threading import *

print(current_thread().name)    # prediction:


# --------------------------------------------------
# SECTION 2: Thread Basics
# --------------------------------------------------

# Q4. Create a thread — predict the output and note it's unpredictable:

from threading import *
import time

def greet(name, times):
    for _ in range(times):
        print(f"Hello, {name}!")
        time.sleep(0.1)

t = Thread(target=greet, args=("Alice", 3))
t.start()
t.join()    # wait for thread to finish
print("Done")

# prediction (in order? or could vary?):


# Q5. Two threads running simultaneously — predict approximate timing:

import time
from threading import *

def count_up(n):
    for i in range(1, n+1):
        time.sleep(0.1)
        print(f"Up: {i}")

def count_down(n):
    for i in range(n, 0, -1):
        time.sleep(0.1)
        print(f"Down: {i}")

start = time.time()
T1 = Thread(target=count_up, args=(3,))
T2 = Thread(target=count_down, args=(3,))
T1.start()
T2.start()
T1.join()
T2.join()
print(f"Time: {time.time() - start:.1f}s")

# prediction: time ≈ ? (sequential would take 0.6s)
# prediction: is Up/Down output in fixed order?


# Q6. Predict — what happens WITHOUT join():

from threading import *
import time

def slow_task():
    time.sleep(0.5)
    print("Task finished")

t = Thread(target=slow_task)
t.start()
# t.join()   # join is commented out
print("Main continues immediately")
# prediction: what order do the two print statements appear?


# --------------------------------------------------
# SECTION 3: Thread with Arguments
# --------------------------------------------------

# Q7. Predict — args must be a tuple:

from threading import *
import time

def square(numbers):
    for n in numbers:
        time.sleep(0.05)
        print(f"Square: {n*n}")

def cube(numbers):
    for n in numbers:
        time.sleep(0.05)
        print(f"Cube: {n*n*n}")

nums = [2, 3, 4]

T1 = Thread(target=square, args=(nums,))   # (nums,) is a tuple
T2 = Thread(target=cube,   args=(nums,))

t = time.time()
T1.start()
T2.start()
T1.join()
T2.join()
print(f"Done in {time.time()-t:.2f}s")

# prediction: output order? time vs sequential?


# Q8. Single-element tuple syntax — predict:

# These are DIFFERENT:
x = (5)     # just an integer 5
y = (5,)    # a tuple with one element

print(type(x))    # prediction:
print(type(y))    # prediction:

# Why does Thread(target=func, args=(nums,)) need the comma?
# YOUR ANSWER:


# --------------------------------------------------
# SECTION 4: Three Ways to Create Threads
# --------------------------------------------------

# Q9. Way 1: Without any class — predict:

from threading import *

def task():
    for i in range(3):
        print(f"Task: {i}")

t = Thread(target=task)    # no class keyword used
t.start()
t.join()
print("Way 1 complete")

# prediction (4 lines total):


# Q10. Way 2: By extending Thread class — predict:

from threading import *

class MyThread(Thread):
    def run(self):            # override run()
        for i in range(3):
            print(f"MyThread: {i}")

t = MyThread()
t.start()
t.join()
print("Way 2 complete")

# prediction:


# Q11. Way 3: Without extending Thread class — predict:

from threading import *

class Worker:               # NO inheritance from Thread
    def do_work(self):
        for i in range(3):
            print(f"Worker: {i}")

w = Worker()
t = Thread(target=w.do_work)   # pass method as target
t.start()
t.join()
print("Way 3 complete")

# prediction:


# --------------------------------------------------
# SECTION 5: Write Code
# --------------------------------------------------

# Q12. Write a multithreaded program with two functions:
#   - print_evens(): prints 0, 2, 4, 6, 8 (0.1s delay each)
#   - print_odds():  prints 1, 3, 5, 7, 9 (0.1s delay each)
# Run them as threads and measure total time.
# Sequential would take ~1s — multithreaded should take ~0.5s.

import time
from threading import *

# YOUR CODE HERE:


# --------------------------------------------------
# BONUS CHALLENGES
# --------------------------------------------------

# BONUS 1: Predict — main thread and child thread interleave:

from threading import *
import time

def child():
    for i in range(3):
        print(f"Child: {i}")
        time.sleep(0.05)

t = Thread(target=child)
t.start()
for i in range(3):
    print(f"Main: {i}")
    time.sleep(0.05)
t.join()

# prediction: fixed order or varies? Why?


# BONUS 2: What is wrong with this code? Fix it:

# from threading import *
# def work(n):
#     print(f"Working on {n}")
#
# T = Thread(target=work, args=5)    # error!
# T.start()

# Error: ?
# Fix: ?


# BONUS 3: Conceptual — answer these:
# a) Why is multithreading output "unpredictable"?
# b) What is the main thread?
# c) What is the difference between start() and join()?
# d) What are the 3 ways to create a thread in Python?

# YOUR ANSWERS:



# --------------------------------------------------
# SECTION: MULTIPLE CHOICE QUESTIONS (MCQ)
# --------------------------------------------------

# Q_MCQ_1. Which module provides threading in Python?
#    A) multiprocessing    B) concurrent    C) threading    D) asyncio
# Answer: ___

# Q_MCQ_2. To start a thread, you call:
#    A) thread.run()    B) thread.start()    C) thread.begin()    D) thread.execute()
# Answer: ___

# Q_MCQ_3. thread.join()  makes the main program:
#    A) Terminate immediately    B) Wait until the thread finishes
#    C) Pause for 1 second    D) Kill the thread
# Answer: ___

# Q_MCQ_4. What is a Race Condition?
#    A) Two threads competing in a performance benchmark
#    B) Multiple threads accessing/modifying shared data simultaneously
#    C) A thread running faster than expected
#    D) A deadlock situation
# Answer: ___

# Q_MCQ_5. threading.Lock() is used to:
#    A) Stop a thread permanently
#    B) Prevent simultaneous access to shared resources
#    C) Create a new thread
#    D) Set thread priority
# Answer: ___

# Q_MCQ_6. The GIL (Global Interpreter Lock) means:
#    A) Python threads run truly in parallel on multiple CPUs
#    B) Only one thread executes Python bytecode at a time
#    C) Threads cannot share variables
#    D) Threading is disabled in Python 3
# Answer: ___

# Q_MCQ_7. threading.Thread(target=func, args=(x,)) passes  x  to  func  via:
#    A) A global variable    B) The args parameter as a tuple
#    C) A shared queue    D) Return value of func
# Answer: ___


# --------------------------------------------------
# SECTION: FILL IN THE BLANKS
# --------------------------------------------------

# FIB_1. import _______ to use threads in Python.

# FIB_2. t = threading.Thread(target=_______, args=(arg1,)) creates a thread
#         that calls the given function.

# FIB_3. Calling t._______() starts the thread's execution.

# FIB_4. Calling t._______() blocks the caller until the thread finishes.

# FIB_5. A threading._______ prevents race conditions on shared data.

# FIB_6. lock.acquire() and lock.release() can also be written as
#         with lock: _______ (using the context manager).

# FIB_7. The GIL limits CPU-bound parallelism; for CPU-heavy work use
#         _______ instead of threading.


# --------------------------------------------------
# REAL-WORLD TASK 🌍
# --------------------------------------------------
# Scenario: Parallel File Download Simulator using threads.
#
# Requirements:
#   1. Simulate downloading 5 files with different sizes (use time.sleep)
#   2. Run all downloads in PARALLEL using threading.Thread
#   3. Print "[filename] download started" and "[filename] done (X.Xs)"
#   4. Use thread.join() for all threads before printing the summary
#   5. Track total time using time.time()
#   6. Use a Lock to safely print from multiple threads without overlap
#
# Expected output (order may vary):
#   file1.zip  download started
#   file3.pdf  download started
#   file2.mp4  download started
#   ...
#   file1.zip  done (1.0s)
#   file3.pdf  done (1.5s)
#   ...
#   All 5 downloads complete. Total time: 2.5s
#
# Hint: sizes = [1.0, 2.5, 1.5, 0.8, 2.0] seconds of "download time"
#
# YOUR CODE HERE:


# ============================================================
# SOLUTIONS
# ============================================================

# Q1: MainThread (default name)

# Q2: MyMainThread

# Q3: MyMainThread (name was changed in Q2 — same thread)

# Q4: "Hello, Alice!" × 3, then "Done" (join ensures t finishes first)

# Q5: Time ≈ 0.3s (vs 0.6s sequential — parallel halves time)
#     Up/Down order NOT fixed — varies per run

# Q6: "Main continues immediately" prints FIRST (before task finishes)
#     then "Task finished" after 0.5s — without join(), main doesn't wait

# Q7: Output interleaves (squares and cubes mixed); time ≈ 0.15s

# Q8: int, tuple; single-element tuple needs comma to distinguish from (5)=int
#     Without comma, args=(nums) is just nums (a list), not a tuple

# Q9: Task: 0, Task: 1, Task: 2, Way 1 complete

# Q10: MyThread: 0, MyThread: 1, MyThread: 2, Way 2 complete

# Q11: Worker: 0, Worker: 1, Worker: 2, Way 3 complete

# BONUS 1: Order varies — threads interleave unpredictably

# BONUS 2: args=5 is wrong (not a tuple); Fix: args=(5,)

# BONUS 3: a) Multiple threads run in parallel — OS decides scheduling
#          b) Default thread every Python program starts with
#          c) start() begins execution; join() waits for thread to finish
#          d) Without class, extending Thread, without extending Thread

# ── MCQ ANSWERS ──────────────────────────────────────────────────────────────
# Q_MCQ_1: C   Q_MCQ_2: B   Q_MCQ_3: B   Q_MCQ_4: B
# Q_MCQ_5: B   Q_MCQ_6: B   Q_MCQ_7: B

# ── FILL IN THE BLANKS ANSWERS ───────────────────────────────────────────────
# FIB_1: threading
# FIB_2: the function name (e.g. my_func)
# FIB_3: start
# FIB_4: join
# FIB_5: Lock
# FIB_6: the code block inside the with statement
# FIB_7: multiprocessing

# ── REAL-WORLD TASK SOLUTION ─────────────────────────────────────────────────
# import threading, time
#
# lock = threading.Lock()
# files = [("file1.zip",1.0),("file2.mp4",2.5),("file3.pdf",1.5),
#          ("file4.docx",0.8),("file5.iso",2.0)]
#
# def download(name, duration):
#     with lock: print(f"{name:12} download started")
#     time.sleep(duration)
#     with lock: print(f"{name:12} done ({duration}s)")
#
# start = time.time()
# threads = [threading.Thread(target=download, args=(n,d)) for n,d in files]
# for t in threads: t.start()
# for t in threads: t.join()
# print(f"All {len(files)} downloads complete. Total time: {time.time()-start:.1f}s")

