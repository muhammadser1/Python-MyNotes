
# 📘 Python List Comprehension

## ✨ What is List Comprehension?

List comprehension is a concise way to create lists in Python using a **single line of code**.  
It replaces longer `for` loops with a cleaner syntax.

---

## 🔍 Why Use List Comprehension?

- ✅ Cleaner and more readable code
- ✅ Fewer lines of code
- ✅ Often faster than regular `for` loops
- ✅ Pythonic (preferred by experienced developers)

---

## 🧱 Basic Syntax

```python
[expression for item in iterable]
```

Or with a condition:

```python
[expression for item in iterable if condition]
```

---

## ✅ Examples

### 1. Square Numbers
```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

### 2. Filter Even Numbers
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

---

### 3. Convert Strings to Uppercase
```python
words = ["hello", "world"]
upper_words = [w.upper() for w in words]
print(upper_words)  # ['HELLO', 'WORLD']
```

---

### 4. Nested Loop (flatten a list)
```python
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4]

# 🧵 How to Read It (step by step):
# “Go through each row in the matrix,
# and then for each num in that row,
# put num into the new list.”.


[new_value for value in list]
[<new_value_if_true> if <condition> else <new_value_if_false> for <value> in <list>]
```

---

## ⚠️ When **Not** to Use List Comprehensions

- If the logic is too complex and hard to read
- If you're doing multiple steps that need clarity

---

## 🧠 Tip:
You can also use **set comprehension** and **dictionary comprehension** in the same way:

```python
# new_dict = {new_key : new_value for item in list}

# Set
unique = {x for x in [1, 2, 2, 3]}
# Dictionary
squares = {x: x**2 for x in range(5)}
# new_dict = {new_key : new_value for (key,value) in dict}
original = {'a': 1, 'b': 2, 'c': 3}
new_dict = {k: v * 2 for (k, v) in original.items()}
print(new_dict)  # {'a': 2, 'b': 4, 'c': 6}
```

---

## 📚 Summary

| Traditional Loop | List Comprehension         |
|------------------|----------------------------|
| More lines       | One-liner                  |
| Easier to debug  | Easier to read (if simple) |
| Slower sometimes | Faster & Pythonic          |

---

Keep your code **clean, fast, and elegant** with list comprehensions! 🚀
