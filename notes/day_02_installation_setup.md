# Day 2 — Application Areas, Features, Python Installation & PyCharm Setup

## Quick Revision — Day 2
| # | Key Point |
|---|-----------|
| 1 | Application areas of Python: web, desktop, database, gaming, data science, AI/ML, testing, DevOps, IoT, embedded |
| 2 | Key features: simple, free & open source, high level, platform independent, portable, dynamically typed, OOP + procedural, extensible, huge libraries |
| 3 | Install Python from **www.python.org** → Download → Python 3.10.4 |
| 4 | During installation: **check "Add Python to PATH"** — this is critical |
| 5 | Verify installation: open Command Prompt → type `python --version` |
| 6 | IDLE = **Integrated Development Learning and Running** (Environment) — default editor |
| 7 | PyCharm download: **www.jetbrains.com** → Community Edition (free, recommended for beginners) |
| 8 | Install Python software **before** PyCharm — core libraries come with Python |
| 9 | 3 ways to run Python code: interactive mode (IDLE shell), script mode (notepad + .py), PyCharm editor |
| 10 | PyCharm: install external libraries via File → Settings → Project → Python Interpreter → + |

---

**Pre-requisite:** Day 1 — Introduction to Python (what Python is, why it's used)
**Next:** Day 3 — PyCharm project creation, interactive window, running Python files
**Related:** Day 4 — Writing first programs (comments, variables, indentation)

---

## Code Created This Day
| Item | Name / Example | Purpose |
|------|----------------|---------|
| Interactive shell | IDLE shell | Testing basic Python statements |
| Script file | test.py | First Python script in notepad |
| PyCharm project | Python Project at 7AM | Main project for entire course |

---

## 1. Application Areas of Python

Python can be used in virtually every type of software development:

```
Application Areas of Python
├── Standalone / Desktop Applications
│   ├── Console Applications (CUI — command user interface)
│   └── Desktop GUI Applications (graphical user interface)
├── Web Applications (requires Django or Flask framework)
├── Database Applications
├── Gaming Applications
├── Data Science / Data Analysis
├── Statistical Analysis
├── Machine Learning / Artificial Intelligence
├── Testing (Selenium with Python)
├── DevOps
├── IoT (Internet of Things)
├── Network Programming
├── Embedded / VLSI / MATLAB programming
└── Business Applications
```

> **Important:** Django and REST API are web frameworks **written in Python**. To use them, you must know Python first. This is why the course starts with Python Core & Advanced.

---

## 2. Features of Python

### 2.1 Simple and Easy to Learn
Python syntax is straightforward — it reads almost like English. Programs can be written with very few lines of code compared to other languages. Even beginners with no prior programming experience can understand it.

### 2.2 Free and Open Source
Python is completely free. No license is required. The source code is open, meaning you can customize it according to your needs.

### 2.3 High Level Programming Language
As a programmer, you do not write any code for memory management or security. Python handles these internally. The garbage collector manages memory automatically.

### 2.4 Platform Independent (Cross-Platform)
Python programs run on **any operating system** — Windows, macOS, Linux, Unix — without rewriting. Python's Virtual Machine (PVM) converts code to machine-readable form for each platform.

```
Python Code (.py)
      │
      ▼
Python Virtual Machine (PVM)
      │
      ├──→ Windows machine code
      ├──→ Linux machine code
      └──→ macOS machine code
```

### 2.5 Portable
Portability means you can **migrate Python programs from one platform to another** easily. The result is always the same regardless of platform. You do not need to rewrite code when switching operating systems.

| | Platform Independence | Portability |
|-|----------------------|-------------|
| **Meaning** | Runs on any OS | Can be moved to any OS easily |
| **Key point** | No change required | Same result on every platform |

### 2.6 Dynamically Typed
No need to declare data types for variables. Python assigns data types at runtime based on the value. (Covered in detail in Day 1.)

### 2.7 Both Procedure-Oriented and Object-Oriented
Python supports **both** paradigms:
- **Procedure-oriented** (like C) — writing functions and calling them
- **Object-oriented** (like C++, Java) — writing classes and objects with OOP concepts (inheritance, encapsulation, polymorphism, abstraction)

### 2.8 Extensible
You can use code written in other languages (like C or C++) inside a Python program. This lets you leverage existing legacy code and improve performance where needed.

### 2.9 Huge Standard Libraries
Once Python is installed, you get a large collection of **built-in libraries** — ready-made code for different tasks. You do not write from scratch; you use existing tools.

Examples:
| Domain | Library |
|--------|---------|
| Data analysis | pandas, numpy |
| Data visualization | matplotlib, seaborn, bokeh |
| Web development | django, flask |
| Machine learning | scikit-learn, tensorflow |
| Network programming | socket, requests |
| Testing | unittest, selenium |

> **Interview Question:** Why did Python become the most popular programming language?
> **Answer:** Python has simple and readable syntax, supports huge standard libraries for every domain, is platform independent, free and open source, and can be used for any type of application — from web development to AI to data science.

---

## 3. Python Versions

| Version | Notes |
|---------|-------|
| 0.9.0 | First ever version — released 1991 |
| 1.x | Early major version |
| 2.x | Second major version (2.7 still used in some legacy systems) |
| **3.10.4** | **Current stable version used in this course** |

To check which version you have installed:
```
# In Command Prompt or Terminal:
python --version
# Output: Python 3.10.4
```

> **Note:** Python 2.x and Python 3.x have some syntax differences. Always use Python 3.x for new projects.

---

## 4. Installing Python

### Step-by-Step Installation

1. Go to **www.python.org**
2. Click on **Downloads**
3. Click **Download Python 3.10.4**
4. Double-click the downloaded `.exe` file
5. Click **Run** when prompted

> **CRITICAL STEP — Do NOT skip this:**
> Before clicking "Install Now", check the checkbox:
> ✅ **Add Python 3.10 to PATH**

6. Click **Install Now**
7. Wait for installation to complete (less than 1 minute)
8. Click **Close**

### Verify Installation
Open **Command Prompt** and type:
```
python --version
```
You should see: `Python 3.10.4`

If you see an error, the PATH was not set. You can add it manually through System Environment Variables.

> **Common Mistake:** Forgetting to check "Add Python to PATH" during installation. If skipped, `python` command won't work in Command Prompt.

---

## 5. Different Ways to Write and Run Python Code

### Option 1: Interactive Mode (IDLE Interactive Shell)

After installing Python, IDLE is available. Open it via Search → "IDLE".

```
Python 3.10.4 (default, Mar 23 2022, 23:44:11)
>>>                     ← type code here and press Enter
```

- Type code → press Enter → see output immediately
- `print()` is **optional** in interactive mode — just type a value and press Enter
- Best for quick experiments

```python
>>> "hello"
'hello'
>>> a = 10
>>> a
10
>>> type(a)
<class 'int'>
>>> a = 12.34
>>> type(a)
<class 'float'>
```

> **Note:** Interactive mode is useful for testing small code snippets. It does NOT save your code.

### Option 2: Script Mode (Notepad + Command Prompt)

1. Open **Notepad** (or any text editor)
2. Write your Python code
3. Save the file with **.py extension** (e.g., `test.py`)
4. Open **Command Prompt**
5. Navigate to the folder: `cd Desktop`
6. Run the file:
```
python test.py
```
or
```
py test.py
```

Example:
```python
# test.py
print("Welcome to Durga Soft")
```

```
C:\Users\user\Desktop> python test.py
Welcome to Durga Soft
```

> **Note:** Both `python filename.py` and `py filename.py` work to run a Python file.

### Option 3: Python IDLE Editor (New File)

1. Open IDLE
2. File → **New File**
3. Write your Python code
4. File → **Save** (with .py extension)
5. Run → **Run Module**

Output appears in the interactive window.

### Option 4: PyCharm Editor (Used Throughout This Course)

The most powerful and recommended option for beginners and professionals.

---

## 6. PyCharm Editor — Download and Install

### What is PyCharm?

PyCharm is a professional IDE (Integrated Development Environment) built specifically for Python by **JetBrains**. It provides:
- Intelligent code completion (IntelliSense)
- Real-time error detection (red underline)
- Automatic indentation
- Easy library management
- Project organization

### Two Editions

| Feature | Community Edition | Professional Edition |
|---------|------------------|---------------------|
| Cost | **Free (lifetime)** | 30-day trial, then paid |
| Python support | Full | Full |
| Django/web support | Limited | Full |
| Data science tools | Limited | Full |
| **Recommendation** | ✅ Use this for Python Core & Advanced | Use this when starting Django |

> **Student tip:** For Python core and advanced (this phase), Community Edition is sufficient. The instructor will switch to Professional Edition when Django sessions start.

### Installation Steps

1. Go to **www.jetbrains.com**
2. Navigate to PyCharm → Download
3. Select **Community Edition** → Download
4. Double-click the downloaded installer → Run
5. Options to select:
   - ✅ Create Desktop Shortcut
   - ✅ Update PATH variable (restart may be needed)
   - ✅ Update context menu
6. Click **Install**
7. Click **Finish** (choose to reboot later if needed)

### First-Time Setup

Open PyCharm → Create New Project:
- Choose **location** carefully (e.g., `D:\Python Project at 7AM`)
- PyCharm automatically creates a **virtual environment** for your project
- Click **Create**

> **What is a virtual environment?**
> An isolated environment where your project's Python and libraries run separately from other projects. Keeps dependencies clean.

---

## 7. PyCharm: Creating Projects and Files

```
PyCharm Project Structure:
Python Project at 7AM/
├── venv/                  ← virtual environment (auto-created)
└── main.py                ← default file created by PyCharm
```

### Creating a New Python File
Right-click on the project name → New → **Python File** → enter file name (no need to type .py — PyCharm adds it automatically)

### Running a Program
- Right-click on the file tab → **Run 'filename'**
- Or: Run menu → Run

Output appears in the **Console/Run window** at the bottom.

---

## 8. Installing External Libraries in PyCharm

Some libraries are not included by default (e.g., pandas). To install:

1. File → **Settings**
2. Left panel → Project: [your project name] → **Python Interpreter**
3. Click the **+** button
4. Search for the library (e.g., `pandas`)
5. Click **Install Package**

```
Settings → Python Interpreter → + → Search "pandas" → Install Package
```

Once installed, you can import it in your code:
```python
import pandas
```

> **Important:** Install Python software **before** PyCharm. PyCharm needs Python installed to function properly.

---

## 9. IDLE Explained

**IDLE** = **Integrated Development Learning and Running** (Environment)

IDLE is Python's built-in default editor. It comes automatically when you install Python. While it works, it lacks the advanced features of PyCharm (no IntelliSense, no real-time error highlighting).

```
IDLE provides:
├── Interactive Shell (type code, see instant output)
└── File Editor (create .py files, run them)

PyCharm provides:
├── Project management
├── IntelliSense (code suggestions)
├── Real-time error detection
├── Easy library installation
└── Professional debugging tools
```

---

## 10. Comparison: Ways to Run Python Code

| Method | Best For | Saves Code? | Error Hints? |
|--------|----------|-------------|--------------|
| Interactive shell (IDLE) | Quick tests | No | No |
| Script mode (Notepad + cmd) | Simple scripts | Yes (.py file) | No |
| IDLE file editor | Small programs | Yes | Minimal |
| PyCharm | Full development | Yes | Yes (real-time) |

> **Instructor Recommendation:** Use PyCharm for all coding sessions in this course. For beginners, PyCharm's real-time error hints and auto-indentation prevent many common mistakes.

---

## 11. Student Q&A from Class

> **Student Question:** How is this Python course helpful for DevOps engineers?
> **Answer:** Python is widely used in DevOps for scripting, automation, and infrastructure management. This course teaches complete Python — once you have strong Python knowledge, applying it in a DevOps context becomes straightforward. The course does not cover DevOps-specific tooling, but Python fundamentals transfer directly.

> **Student Question:** Will we have lifetime access to session recordings?
> **Answer:** Yes. Every session is recorded. Once enrolled, all recordings are shared to your Google Drive with lifetime access. Course material (PDF/docs) is also shared along with recordings.

> **Student Question (student):** Is `python` or `py` command used to run files?
> **Answer:** Both work. `python test.py` and `py test.py` both execute a Python file from the Command Prompt.

---

## Common Errors — Day 2

| Error | Cause | Fix |
|-------|-------|-----|
| `python` not recognized in Command Prompt | "Add Python to PATH" was not checked during installation | Re-run installer and check the PATH checkbox, or manually add Python to system environment variables |
| PyCharm doesn't recognize Python | Python not installed before PyCharm | Install Python first, then create a new PyCharm project pointing to the correct Python interpreter |
| `No module named 'pandas'` | pandas not installed in your environment | File → Settings → Python Interpreter → + → Install pandas |
| Script runs but shows wrong output | Editing the wrong file | Check which tab is active in PyCharm; right-click the correct file and run it |

---

## Interview Questions — Day 2

**Q: What are the main features of Python?**
A: Simple and easy to learn, free and open source, high level, platform independent, portable, dynamically typed, supports both procedural and OOP, extensible, and has huge standard libraries.

**Q: What types of applications can you build with Python?**
A: Web applications (with Django/Flask), desktop applications, database applications, data science and analysis apps, AI/ML applications, gaming, network programming, testing (Selenium), DevOps automation, IoT, and embedded systems.

**Q: What is the difference between Community and Professional editions of PyCharm?**
A: Community Edition is free and supports Python development fully. Professional Edition is paid (30-day trial) and adds support for Django web development, databases, and scientific tools. For Python Core and Advanced, Community Edition is sufficient.

**Q: Why should you install Python before PyCharm?**
A: Python's core libraries and the Python interpreter are installed with the Python software. PyCharm is just an editor — it needs a Python interpreter to run code. Without Python installed first, PyCharm cannot execute any programs.

**Q: What is a virtual environment in Python?**
A: A virtual environment is an isolated Python environment for a specific project. It keeps that project's libraries and Python version separate from other projects, preventing version conflicts.

**Q: What does "Add Python to PATH" mean during installation?**
A: Adding Python to the system PATH means the operating system knows where to find the Python executable. Without it, running `python` in Command Prompt gives a "not recognized" error. Always check this box during installation.

**Q: What are the different ways to run Python code?**
A: Four ways: (1) Interactive mode in IDLE shell, (2) Script mode — write code in Notepad, save as .py, run via `python filename.py` in Command Prompt, (3) IDLE file editor, (4) PyCharm editor (recommended).

---

## Try It Yourself — Day 2

**Exercise 1:** Install Python 3.10.4 (if not already installed). Open Command Prompt and verify:
```
python --version
```

**Exercise 2:** Open IDLE's interactive shell and try these one by one — observe how Python responds instantly:
```python
10 + 20
"Durga" + " Soft"
type(3.14)
type(True)
```

**Exercise 3:** Open Notepad, write the following, save as `hello.py` on your Desktop, then run it from Command Prompt:
```python
print("Hello from script mode!")
print("My name is Python")
```
Command: `cd Desktop` then `python hello.py`

**Exercise 4:** Install PyCharm Community Edition. Create a new project called `PythonCourse`. Add a file called `day2.py` and write:
```python
print("PyCharm is working!")
a = 100
print(type(a))
```
Right-click → Run. Confirm output appears in the console.

**Exercise 5:** In PyCharm, try to install the `requests` library via Settings → Python Interpreter → +. After installation, write:
```python
import requests
print("requests library installed successfully")
```
