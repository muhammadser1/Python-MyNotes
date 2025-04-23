
# ⚖️ Difference Between `ValueError`, `TypeError`, and Common Exception Handling in Python

---

## ✅ What is a `ValueError`?

A `ValueError` happens when:
> **The type is correct, but the value is not acceptable**.

### 📌 Example:

```python
int("123abc")
# ❌ ValueError: invalid literal for int() with base 10
```

- `"123abc"` is a `str` (which `int()` accepts),
- But its **value** doesn't represent a valid number → causes `ValueError`.

---

## ✅ What is a `TypeError`?

A `TypeError` occurs when:
> **You use the wrong data type for the operation.**

### 📌 Example 1:

```python
"123" + 456
# ❌ TypeError: can only concatenate str (not "int") to str
```

You can't add a string and an integer together without conversion.

### 📌 Example 2:

```python
len(42)
# ❌ TypeError: object of type 'int' has no len()
```

`len()` expects a sequence (like a list or string), not an integer.

---

## ✅ What is an `IndexError`?

An `IndexError` happens when:
> **You try to access an index that doesn't exist in a sequence.**

### 📌 Example:

```python
my_list = [10, 20, 30]
print(my_list[5])
# ❌ IndexError: list index out of range
```

---

## 🛠️ Catching Exceptions in General

Python allows you to **gracefully handle** errors using `try`/`except`.

### ✅ Example: Catch specific error

```python
try:
    num = int("abc")
except ValueError:
    print("That was not a valid number!")
```

### ✅ Catch multiple error types

```python
try:
    value = "123" + 456
except TypeError:
    print("You mixed incompatible types!")
```

### ✅ Catch multiple at once

```python
try:
    my_list = [1, 2]
    print(my_list[10])
except (IndexError, ValueError) as e:
    print("Caught an error:", e)
```

---

## ✅ Best Practice:

- Catch specific exceptions instead of using `except:` alone.
- Use `as e` to inspect the error message if needed.
- Always test for edge cases that might raise `ValueError`, `TypeError`, or `IndexError`.

---

## 🧱 Full Structure: `try` / `except` / `else` / `finally`

Python allows you to write robust error-handling logic using all four parts of the `try` block.

```python
try:
    # Code that might raise an exception
except SomeError:
    # Code that runs if an exception happens
else:
    # Code that runs if no exception occurs in try
finally:
    # Code that always runs no matter what
```

---

### 🧪 Example:

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("❌ That's not a valid number!")
else:
    print(f"✅ Success! You entered {num}")
finally:
    print("🔁 This runs no matter what (cleanup, closing files, etc.)")
```

---

### 🔍 Purpose of Each Block

| Block     | When It Runs                                        |
|-----------|-----------------------------------------------------|
| `try`     | Always runs first                                   |
| `except`  | Runs **only if** an error occurs in `try`           |
| `else`    | Runs **only if no error** occurred in `try`         |
| `finally` | Runs **no matter what** (error or no error)         |

---

### ✅ Real-world Use Case: File Handling

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("❌ File not found!")
else:
    print("✅ File read successfully")
finally:
    print("🔁 Closing file...")
    if 'file' in locals():
        file.close()
```

- `finally` is used to guarantee file cleanup even if an error happens.

---


---

## 🚨 Raising Exceptions with `raise`

Sometimes you want to manually trigger an exception to enforce rules or handle errors explicitly. This is done using the `raise` keyword.

---

### ✅ Basic Syntax

```python
raise ExceptionType("Custom error message")
```

---

### 🧪 Example: Raise a `ValueError`

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return f"Age set to {age}"
```

```python
print(set_age(25))   # ✅ OK
print(set_age(-5))   # ❌ Raises ValueError
```

---

### 🧪 Raise in Your Own Checks

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero.")
    return a / b
```

---

### 🧱 Raising Custom Exceptions

You can define your own exception type and raise it:

```python
class TooMuchCoffeeError(Exception):
    pass

def drink(coffee_cups):
    if coffee_cups > 5:
        raise TooMuchCoffeeError("☕ Too much coffee!")
    return "You're good!"
```

---

### 🧠 Why Use `raise`?

- Enforce validations and logic rules.
- Exit a function early when something is wrong.
- Raise your own custom errors in APIs and libraries.
- Re-raise errors inside `except` blocks.

---

### 🔁 Re-raising Exceptions

```python
try:
    x = int("abc")
except ValueError:
    raise ValueError("Custom error: invalid number format")
```

---
```python

def inner():
    raise ValueError("Something went wrong")

def middle():
    inner()

def outer():
    try:
        middle()
    except ValueError as e:
        print("Caught error:", e)
outer()
# Output: Caught error: Something went wrong

```
