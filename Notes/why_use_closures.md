
# 🧠 Why Use Closures like `make_multiplier` Instead of Just `multiply(x, y)`?

## ❓ The Question

> Why write something like this?

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier
```

> When I can just do:

```python
def multiply(x, y):
    return x * y
```

---

## ✅ Short Answer

Use `multiply(x, y)` for **simple one-time calculations**.

Use `make_multiplier(factor)` when you want to **create a custom, reusable function with built-in behavior** (a closure).

---

## 🎯 Think of it Like a Function Factory

```python
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # ➡️ 20
print(triple(10))  # ➡️ 30
```

Here, `double` and `triple` are **custom multipliers**.

---

## 📦 Real-Life Use Case

Imagine you have a shopping cart app and different buttons apply different discounts:

```python
apply_10 = make_multiplier(0.9)
apply_20 = make_multiplier(0.8)
```

Now you can do:

```python
def make_discount(discount_factor):
    """
    Returns a function that applies a discount factor to a price.
    Example: discount_factor = 0.9 → 10% discount
    """
    def apply_discount(price):
        return price * discount_factor
    return apply_discount

# Create two discount functions using closures
apply_10 = make_discount(0.9)  # 10% off
apply_20 = make_discount(0.8)  # 20% off

# Use them
price = 100
print(apply_10(price))  # ➡️ 90.0
print(apply_20(price))  # ➡️ 80.0

```

You’ve created **tools** that contain their logic inside.

---

## 📊 Comparison Table

| Scenario                                 | Use Regular Function | Use Closure     |
|------------------------------------------|-----------------------|-----------------|
| Just multiply two numbers once           | ✅ Yes                | ❌ Not needed   |
| Create a reusable function like `double` | ❌ Needs wrapper code | ✅ Perfect use  |
| Customize behavior with stored state     | ❌ Hard               | ✅ Easy         |
| UI callbacks / APIs / math pipelines     | ❌ Verbose            | ✅ Elegant      |

---

## 🧠 Key Insight

Closures let you:

- Store **state** (like `factor`)
- Create **custom behaviors**
- Pass functions around with **embedded configuration**

---

## 🧠 Analogy

Using `make_multiplier(3)` is like saying:

> “Give me a tool that always multiplies by 3 — and let me use it whenever I want.”

Instead of writing `multiply(x, 3)` again and again.

---

## ✅ Final Thoughts

Closures may look weird at first, but they:
- Reduce repetition
- Add flexibility
- Make functional programming and GUI design powerful

You don't *need* them for everything, but when you *do* — they're magic ✨
