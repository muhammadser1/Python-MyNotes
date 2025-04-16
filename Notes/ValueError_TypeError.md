# ⚖️ Difference Between `ValueError` and `TypeError` in Python

---

## ✅ What is a `ValueError`?

A `ValueError` happens when:
> **The type is correct, but the value is not acceptable**.

### 📌 Example:
```python
int("123abc")  
# ❌ ValueError: invalid literal for int() with base 10

* "123abc" is a string, and int() can accept strings.

* But this string doesn't represent a valid integer → causes ValueError.

---

## ✅ What is a `TypeError`?
You use a value of the wrong type for the operation.


"123" + 456  
# ❌ TypeError: can only concatenate str (not "int") to str

Another example:
len(42)  
# ❌ TypeError: object of type 'int' has no len()
