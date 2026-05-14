# Day 3 — PyCharm Deep Dive: Project Setup, Files, and Running Code

## Quick Revision — Day 3
| # | Key Point |
|---|-----------|
| 1 | Interactive mode: open IDLE → type code → press Enter → instant output; `print()` is optional here |
| 2 | Script mode: write code in Notepad → save as `test.py` → run with `python test.py` or `py test.py` |
| 3 | Every Python file has a `.py` extension — this is mandatory |
| 4 | In Python, every `.py` file is called a **module** |
| 5 | PyCharm Community Edition is free; download from **www.jetbrains.com** |
| 6 | Always create a PyCharm project first; all `.py` files live inside the project |
| 7 | Right-click a file in PyCharm → **Run 'filename'** to execute it |
| 8 | PyCharm shows red underline for errors in real time — this is a major advantage over Notepad |
| 9 | Change font size: File → Settings → Editor → Font → set size to 20 |
| 10 | Upcoming (Day 4): comments, keywords, indentation, identifiers, variables, multiple assignment |

---

**Pre-requisite:** Day 2 — Python installation, application areas, features
**Next:** Day 4 — Fundamental concepts (comments, keywords, indentation, identifiers, variables)
**Related:** Day 2 — PyCharm download and initial setup

---

## Code Created This Day
| Item | Name / Example | Purpose |
|------|----------------|---------|
| .py file | test.py | First script in Notepad → ran via command prompt |
| .py file | test2.py | Second script saved on desktop |
| PyCharm project | Python Project at 7AM | Main project folder |
| .py file in PyCharm | main.py | Auto-created default file |
| .py file in PyCharm | test.py | Custom file added to project |
| .py file in PyCharm | test1.py | Second custom file (addition program) |

---

## 1. Review: Three Ways to Write and Run Python Code

### Option 1: Interactive Mode (IDLE Shell)

Open IDLE: Search → type `idle` → open.

The interactive shell opens — you can type Python code directly:

```python
>>> "hello"
'hello'
>>> a = 10
>>> a
10
>>> type(a)
<class 'int'>
>>> a = 23.45
>>> print(type(a))
<class 'float'>
>>> a = "size"
>>> type(a)
<class 'str'>
```

- `print()` is **optional** in the interactive window — just type a variable name and press Enter
- Press Enter after each line to execute it
- Output appears immediately
- Code is **not saved** — this is for experimentation only

### Option 2: Script Mode (Notepad)

1. Open Notepad
2. Write Python code:
```python
print("Hello, Hydra Boy")
```
3. File → Save As → choose Desktop → set file name: `test.py`
   - **Important:** in the "Save as type" dropdown, select "All Files" so Notepad doesn't add `.txt` automatically
4. Close Notepad

You now have `test.py` on your Desktop.

**Run via Command Prompt:**
```
cd Desktop
python test.py
```
or
```
py test.py
```

Both commands produce the same output: `Hello, Hydra Boy`

**Run via IDLE:**
1. Open IDLE
2. File → **Open** → navigate to Desktop → select `test.py`
3. Run menu → **Run Module**

Output appears in the interactive shell window.

```
python test.py          ← full command form
py test.py              ← short form (both work)
```

> **Key fact:** Every `.py` file is treated as a **module** in Python. That is why the IDLE "Run" menu says "Run Module."

### Option 3: Using IDLE to Create a New File

1. Open IDLE
2. File → **New File**
3. Write code:
```python
a = 10
b = 20
c = a + b
print("Sum is", c)
```
4. Run → **Run Module** → it prompts you to save → save as `test_all.py`

Output: `Sum is 30`

---

## 2. PyCharm: Complete Setup Walkthrough

### 2.1 Download PyCharm

1. Go to **www.jetbrains.com**
2. PyCharm → Download
3. Choose **Community Edition** (free, lifetime)
4. Download the installer

### 2.2 Install PyCharm

1. Double-click the installer → Run
2. Click **Next** → **Next**
3. (Optional but recommended) Check:
   - ✅ Create Desktop Shortcut
   - ✅ Update PATH variable
   - ✅ Update context menu
4. Click **Install**
5. Click **Finish**

> After installation, PyCharm may ask to **Reboot Now**. Select "I want to manually reboot later" to continue immediately.

### 2.3 Create a New Project

1. Open PyCharm → **New Project**
2. Click the folder icon next to "Location"
3. Choose your drive (e.g., D drive)
4. Name your project: `Python Project at 7AM`
5. Click **OK**
6. Click **Create**

PyCharm automatically:
- Creates the project folder
- Sets up a **virtual environment** (isolated Python environment)

```
D:\Python Project at 7AM\
├── venv\               ← virtual environment (auto-created)
└── main.py             ← default file (auto-created)
```

### 2.4 The Default main.py

PyCharm creates a `main.py` with sample code:
```python
def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
```

Run it: Run → Run 'main' → Output: `Hi, PyCharm`

> Don't worry about the `f'Hi, {name}'` syntax yet — this is a **formatted string** (f-string). It will be explained when string topics are covered.

### 2.5 Change the Theme and Font Size

**Change theme to light (recommended for visibility):**
- File → **Settings** → Appearance & Behavior → Appearance
- Theme dropdown → select **Windows** or **Light**

**Change font size:**
- File → **Settings** → Editor → **Font**
- Set font size to **20**

---

## 3. Creating and Running Files in PyCharm

### Create a New Python File

**Method:** Right-click on the project name in the left panel → **New** → **Python File**

- Type the file name (e.g., `test`) — **no need to add .py**, PyCharm adds it automatically
- Press Enter

The new file opens in the editor.

> Difference between two "New file" options:
> - **New → File** — creates a blank file, you must type `.py` manually
> - **New → Python File** — creates a `.py` file automatically, just give the name

### Write Code in the New File

```python
# test.py
print("Hello from PyCharm!")
```

### Run the File

**Option 1:** Right-click on the file tab → **Run 'test'**
**Option 2:** Run menu → select the file to run

Output appears in the **Run / Console panel** at the bottom.

### Running Multiple Files

If your project has multiple files (`test.py`, `test1.py`, `main.py`), PyCharm's "Run" button runs the **last run file** by default. To run a specific file:
- Right-click on the file tab → Run 'filename'

---

## 4. PyCharm's IntelliSense: Why It's Better Than Notepad

```python
# As you type 'print', PyCharm shows suggestions:
pri→ [IntelliSense shows: print, print_hi, ...]

# If you make an error, PyCharm underlines it in RED immediately:
print("hello"    ← missing closing bracket — red underline appears instantly
```

In Notepad, you see errors only when you run the code.
In PyCharm, errors appear **as you type** — much better for beginners.

```
Notepad:        write code → save → run → see error → go back to fix
PyCharm:        write code → see error immediately → fix before even running
```

---

## 5. Demonstration: Addition Program

```python
# test1.py
a = 10
b = 20
c = a + b
print("Some keys:", a + b)
```

Run output: `Some keys: 30`

**Intentional Error Demonstration:**
```python
# Missing closing bracket:
print("Some keys", a + b   # ← red underline in PyCharm
```

Error when running:
```
File "test1.py", line 3
    print("Some keys", a + b
                              ^
SyntaxError: unexpected EOF while parsing
```

PyCharm shows: `File directory...test1.py line number 3... never closed bracket`

---

## 6. Installing External Libraries from PyCharm

(Demonstrated with pandas)

1. File → **Settings** → Project: Python Project at 7AM → **Python Interpreter**
2. Click **+** (plus button)
3. In the search box, type: `pandas`
4. Select `pandas` from the results
5. Click **Install Package**
6. Wait for: "Package 'pandas' installed successfully"

Now this works without error:
```python
import pandas
print("pandas imported successfully")
```

Before installation, `import pandas` showed a red underline ("No module named 'pandas'").
After installation, the red underline disappears.

> **Tip:** The same process works for any library — numpy, matplotlib, requests, etc. In upcoming sessions, when a new library is needed, install it this way.

---

## 7. Preview: Fundamental Concepts (Coming in Day 4)

The instructor announced that Day 4 covers these fundamental concepts:

| Concept | Brief Description |
|---------|-------------------|
| **Comments** | Lines excluded from execution; used for description |
| **Keywords / Reserved Words** | Special words Python reserves for specific purposes |
| **Indentation** | Spaces used to define code blocks (replaces `{}` from other languages) |
| **Identifiers** | Names of variables, functions, and classes |
| **Variables** | Named memory locations to store values |
| **Multiple Assignment** | Assigning multiple values to multiple variables at once |

---

## 8. Student Q&A from Class

> **Student Question:** When opening IDLE and the session link says "session is over," what does that mean?
> **Answer:** That means you joined after the session already ended. You need to join at the scheduled start time (7 AM in this batch). The session link only becomes active once the organizer starts it.

> **Student Question:** Can I install PyCharm before Python?
> **Answer:** No — always install Python first. PyCharm is just an editor; it needs Python to run code. If you install PyCharm without Python, it won't be able to execute any programs.

> **Student Question:** What is the difference between "Run" and "Run Module" in IDLE?
> **Answer:** In IDLE's file editor, "Run Module" (F5) executes the currently open file. The output appears in the interactive shell. "Run" in PyCharm executes the last run configuration. Right-clicking a file → "Run 'filename'" is the most reliable way to run a specific file.

---

## Common Errors — Day 3

| Error | Cause | Fix |
|-------|-------|-----|
| File saved as `test.py.txt` | Notepad added `.txt` automatically | In Save As dialog, set "Save as type" to "All Files" |
| `python test.py` gives "python not found" | Python not added to PATH | Reinstall Python and check "Add Python to PATH" |
| PyCharm "Run" executes wrong file | PyCharm remembers last run file | Right-click the desired file → Run 'filename' |
| `SyntaxError: unexpected EOF` | Missing closing bracket or quote | Check for missing `)`, `"`, or `'` |
| Red underline on `import pandas` | pandas not installed | File → Settings → Python Interpreter → + → install pandas |

---

## Interview Questions — Day 3

**Q: What is the difference between interactive mode and script mode in Python?**
A: Interactive mode (IDLE shell) executes code line by line immediately — useful for quick tests, but code is not saved. Script mode writes code to a `.py` file and runs it all at once — suitable for real programs.

**Q: What is a Python module?**
A: Every `.py` file in Python is a module. A module is a file containing Python code (functions, classes, variables) that can be executed directly or imported into other programs.

**Q: Why is PyCharm recommended for Python beginners?**
A: PyCharm provides real-time error detection (red underline), IntelliSense (code suggestions), automatic indentation, and easy library installation. Beginners make fewer mistakes because errors are shown as they type, not just at runtime.

**Q: How do you run a Python file from the command line?**
A: Navigate to the file's directory using `cd foldername`, then type `python filename.py` or `py filename.py`.

**Q: What is a virtual environment in PyCharm?**
A: A virtual environment is an isolated Python environment created per project. It keeps each project's libraries separate so different projects can use different library versions without conflicts.

---

## Try It Yourself — Day 3

**Exercise 1:** Open IDLE interactive shell and run each line one by one. Observe the output:
```python
"hello"
10 + 5
a = "Python"
a
type(a)
```

**Exercise 2:** Write a script in Notepad, save as `greet.py` on your Desktop, run via Command Prompt:
```python
name = "Student"
print("Hello,", name)
print("Welcome to Python programming!")
```

**Exercise 3:** In PyCharm, create a new file called `calculator.py` and write:
```python
a = 50
b = 30
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
```
Run it and verify all four results.

**Exercise 4:** Intentionally introduce a syntax error in `calculator.py` (e.g., remove a closing bracket from one print statement). Observe the red underline in PyCharm. Then run it — compare the error message to what PyCharm showed in real time.

**Exercise 5:** Create two files in your PyCharm project: `program_a.py` and `program_b.py`. Add a print statement to each. Practice switching between them using right-click → Run to confirm you can run either file independently.
