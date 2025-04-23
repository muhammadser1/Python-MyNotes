
  

# Python Functions: `*args` and `**kwargs` Explained

  

In Python, you can use `*args` and `**kwargs` to make your functions more flexible and able to accept a variable number of arguments.

  

---

  

## 1. Basic Function with Default Arguments

  

```python

def  fun(a=1, b=2, c=3):
	print("a", a)

	print("b", b)

	print("c", c)

```

  

### Examples:

  

```python

fun(a=2, b=3)

# Output:

# a 2

# b 3

# c 3 <- default value used

  

fun()

# Output:

# a 1

# b 2

# c 3 <- all default values used

  

fun(b=10)

# Output:

# a 1 <- default

# b 10

# c 3 <- default

```

  

---
## 1.2 Default Argument Values – Mutable vs Immutable

  

Python evaluates default argument values only **once**, when the function is defined — not each time it’s called.

  

### ✅ Immutable default values (safe):

  

```python

def  greet(name="Guest"):

print("Hello", name)

  

greet() # Hello Guest

greet("Alice") # Hello Alice

```

  

Immutable types like `int`, `str`, `float`, `tuple`, `None` are **safe** to use as default values.

  

---

  

### ⚠️ Mutable default values (dangerous):

  

```python

def  add_item(item, my_list=[]):

my_list.append(item)

return my_list

  

print(add_item(1)) # [1]

print(add_item(2)) # [1, 2] ← not a fresh list!

```

  

Here, the same list is reused across function calls.

  

---

  

### ✅ Safe alternative using `None`:

  

```python

def  add_item(item, my_list=None):

if my_list is  None:

my_list = []

my_list.append(item)

return my_list

  

print(add_item(1)) # [1]

print(add_item(2)) # [2] ← fresh list each time

```

  

This is the recommended way to use mutable default values like lists or dicts.
  

## 2. `*args` – Non-keyworded Variable-Length Arguments

  

Use `*args` to pass a variable number of **positional** arguments.

  

```python

def  example_args(*args):

for i, val in  enumerate(args):

print(f"Argument {i}: {val}")

```

  

### Example:

  

```python

example_args(1, 2, 3)

# Output:

# Argument 0: 1

# Argument 1: 2

# Argument 2: 3

```

  

`args` is a tuple containing all extra positional arguments.

  

---
### 💡 When to Use `*args`

You should use `*args` when you want your function to accept a **flexible number of positional arguments**, and you don’t know in advance how many inputs there will be.
  `*args` Use Cases
  ### 2.1 ✅ Utility Function – `sum_all`

Use `*args` to collect any number of numbers and compute a result:
```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))   # Output: 6
print(sum_all(10, 20))    # Output: 30
print(sum_all())          # Output: 0

```

### 2.2 ✅ Looping Over Inputs

Use `*args` when you want to loop over many values passed to a function:
```python
def print_uppercase(*words):
    for word in words:
        print(word.upper())

print_uppercase("hello", "world", "python")
# Output:
# HELLO
# WORLD
# PYTHON
```
### 2.3 ✅ Wrappers / Decorators That Forward Arguments

Decorators often use `*args` and `**kwargs` so they can wrap **any** function without knowing its exact parameters:
```python
def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments passed:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@debug_decorator
def greet(name, age):
    print(f"Hello {name}, age {age}")

greet("Alice", age=30)
# Output:
# Arguments passed: ('Alice',) {'age': 30}
# Hello Alice, age 30

```
## 3. *kwargs` – Keyworded Variable-Length Arguments

  

Use `**kwargs` to accept any number of **keyword** arguments.

  

```python

def  example_kwargs(**kwargs):

for key, value in kwargs.items():

print(f"{key} = {value}")

```

  

### Example:

  

```python

example_kwargs(name="Alice", age=30)

# Output:

# name = Alice

# age = 30

```

  

`kwargs` is a dictionary containing all extra keyword arguments.

  ## 💡 When to Use `**kwargs`

Use `**kwargs` when your function needs to accept an **unknown number of keyword (named) arguments**.

It allows you to write flexible and dynamic functions that don’t require a fixed set of named parameters.

### ✅ Use Case 3.1: Optional configuration/settings
```python
def connect_to_db(**config):
    host = config.get("host", "localhost")
    port = config.get("port", 5432)
    print(f"Connecting to {host}:{port}")

connect_to_db(host="127.0.0.1", port=3306)
```
Use `**kwargs` when you want to accept a set of optional settings.
### ✅ Use Case 3.2: Pass named arguments dynamically


```python
	def print_profile(name, age, **details):
	    print(f"Name: {name}, Age: {age}")
	    for key, value in details.items():
	        print(f"{key}: {value}")

	print_profile("Alice", 30, country="USA", hobby="Reading")
	# Output:
	# Name: Alice, Age: 30
	# country: USA
	# hobby: Reading
```
Use this when you want to allow flexible metadata to be passed in.
### ✅ Use Case 3: Forwarding keyword arguments (e.g. decorators, wrappers)

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def create_user(name, age, admin=False):
    print(f"User {name}, age {age}, admin: {admin}")

create_user(name="Bob", age=25, admin=True)
# Output:
# Calling create_user with {'name': 'Bob', 'age': 25, 'admin': True}
# User Bob, age 25, admin: True

```


## 4. Using All Together

  

```python

def  combined_example(a, *args, **kwargs):

print("a:", a)

print("args:", args)

print("kwargs:", kwargs)

```

  

### Example:

  

```python

combined_example(5, 10, 20, x=1, y=2)

# Output:

# a: 5

# args: (10, 20)

# kwargs: {'x': 1, 'y': 2}

```

  

---

  

## Summary

  

| Type | Symbol | What It Captures | Type |

|----------|----------|----------------------------------|-----------|

| Positional | `*args` | Extra non-keyworded args | `tuple` |

| Keyword | `**kwargs`| Extra keyworded args | `dict` |

  

You can use them together to create powerful, flexible function definitions.