
# 🧠 What is `global` in Python?

In Python, variables defined **inside a function** are **local** by default — they exist only within that function's scope.

But sometimes you want to **modify a variable defined outside the function** (in the global scope).  
That’s where the `global` keyword comes in.

---

## ⚠️ Without `global`

```python
counter = 0

def increment():
    counter += 1  # ❌ Error! UnboundLocalError

increment()
```

### ❓ Why error?
Python sees `counter += 1` and assumes `counter` is a local variable.  
But we never declared it in the function, and Python doesn’t automatically use the outer one if you're **modifying** it.

---

## ✅ With `global`

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # ➡️ 1
```

Now it works — we told Python to use the global `counter`, not create a new local one.

---

## 💡 When to Use `global`?

Use it **only when**:
- You truly need to **modify a global variable inside a function**.
- You are managing shared state in a **simple script or small program**.

---

## ❌ When NOT to Use It

In large projects or real-world software, using `global` can lead to:
- Bugs
- Unpredictable state
- Hard-to-track behavior

### Instead, use:
- Return values from functions
- Classes to encapsulate state
- Mutable objects (like lists or dicts) if you must share data

---

## 🧪 Another Example: List vs Int

```python
x = 5

def change():
    global x
    x = 10

change()
print(x)  # ➡️ 10
```

But for **mutable objects** like lists:

```python
nums = [1, 2, 3]

def modify():
    nums.append(4)  # Works! No need for `global` since we're not reassigning

modify()
print(nums)  # ➡️ [1, 2, 3, 4]
```

You only need `global` if you’re **reassigning** the variable — not if you’re modifying a mutable one.

---

## 🧾 Summary

| Operation         | Type      | Needs `global`? |
|------------------|-----------|------------------|
| `x = 5`          | int       | ✅ if modified   |
| `x += 1`         | int       | ✅               |
| `list.append()`  | list      | ❌               |
| `list = []`      | list      | ✅ (reassignment) |
