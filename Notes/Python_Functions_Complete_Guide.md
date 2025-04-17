
# 🧠 Python Functions – Full Guide for Beginners

---

## ✅ What is a Function?

A **function** is a reusable block of code that performs a specific task.

### 🔹 Syntax:
```python
def greet(name):
    return f"Hello, {name}!"
```

### 🔹 Use:
- To organize code
- Avoid repetition
- Improve readability and reusability

---

## 📥 Parameters and Arguments

### 🔹 Parameters
Variables listed inside the function definition.

### 🔹 Arguments
Actual values passed to the function when calling it.


---

## 🌟 Default Arguments

You can assign default values to parameters.

```python
def greet(name="friend"):
    print(f"Hello, {name}!")

greet()         # Hello, friend!
greet("Sara")   # Hello, Sara
```

---

## ⚠️ Mutable Default Argument Pitfall

Avoid using mutable types (like lists or dicts) as default values.

```python
def add_item(item, my_list=[]):  # ⚠️ shared between calls!
    my_list.append(item)
    return my_list

print(add_item("A"))  # ['A']
print(add_item("B"))  # ['A', 'B'] ← unexpected!
```

### ✅ Correct way:
```python
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

---

## 🌐 *args and **kwargs

### 🔹 *args: any number of positional arguments (type of args is tuple)
```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3)  # 6
```

### 🔹 **kwargs: any number of named keyword arguments (type of kwargs is dict)
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Ali", age=25)
```

---

## 🧠 Functions as First-Class Citizens

You can:
- Pass functions as arguments
- Return functions from other functions
- Store them in variables

---

## 🧲 Higher-Order Functions

A **higher-order function** accepts a function as a parameter or returns a function.

```python
def apply_twice(func, value):
    return func(func(value))

def double(x):
    return x * 2

apply_twice(double, 3)  # 12
```

---

## 🔁 Function Returning Function (Closure)

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
print(double(5))  # 10
```

---

## 🔒 Closures

A closure "remembers" the values from its enclosing scope even if the outer function is done.

Used for:
- Customizing functions
- Keeping state (like counters)

---

## 🎁 Decorators

A decorator is a function that **wraps another function** to add extra behavior.

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()
```

### 📦 Output:
```
Before
Hi!
After
```

---

## 💡 Why Use Decorators?

- Logging
- Access control
- Memoization
- Timing function execution

---

## ✅ Summary

| Concept               | When to Use                                      |
|-----------------------|--------------------------------------------------|
| Regular Function      | Reuse logic                                      |
| Default Arguments     | Set default values (avoid mutable types)         |
| *args, **kwargs       | Accept variable # of args or key-value pairs     |
| Higher-Order Function | Pass/return functions                            |
| Closures              | Remember state from outer functions              |
| Decorators            | Add behavior to functions (logging, timing etc.)|

---

