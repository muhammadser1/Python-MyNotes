
# 📚 What is `if __name__ == "__main__"` in Python?

When Python runs a file,  
**each file** gets a special built-in variable called `__name__`.

| Situation | Value of `__name__` |
|:---|:---|
| If you **run the file directly** (`python app.py`) | `__name__` is `"__main__"` |
| If you **import the file** into another file | `__name__` is the **name of the file** (like `"app"` or `"module"`) |

---

# 🧠 What does `if __name__ == "__main__":` mean?

It means:

> "Only run this part of the code if this file is being **run directly** (not imported as a module)."

In Flask, it usually looks like:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

- If you run `python app.py`, this block will start the web server.
- If you import `app` from another file (e.g., `from app import app`), this block **will not run automatically**.

---

# 🎯 In simple words:

✅ **`__main__` is a way to control when the file should actually "do" something.**  
✅ It helps your code be clean when you **reuse** files.

---

# 📋 Very simple example:

**File: `hello.py`**

```python
print("This will always run.")

if __name__ == "__main__":
    print("This will only run if you run hello.py directly.")
```

| You do | What happens |
|:---|:---|
| `python hello.py` | Output:<br>✅ This will always run.<br>✅ This will only run if you run hello.py directly. |
| `import hello` in another file | Output:<br>✅ This will always run.<br>❌ "This will only run if you run directly" does not print. |

---

# 🚀 Why is it important in Flask?

In Flask apps,  
you often want to **define the app** (`app = Flask(__name__)`)  
and then **control when the server runs**.

```python
# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello!"

if __name__ == '__main__':
    app.run(debug=True)
```

✅ Now you can **import `app`** into other files (for example: to connect it to a bigger system) without starting the server by accident.

---

# 🔥 Final summary:

| Concept | Meaning |
|:---|:---|
| `__name__` | Built-in variable in every Python file |
| `"__main__"` | Means "I am running this file directly" |
| `if __name__ == "__main__"` | Protects code from running when imported elsewhere |
