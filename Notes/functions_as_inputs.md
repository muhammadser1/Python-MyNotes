
# 🧠 Python: Functions as Inputs – Reusability & Composability

## 🔍 What Does "Function as Input" Mean?
In Python, functions are **first-class citizens**, meaning:
- You can assign them to variables
- You can **pass them as arguments** to other functions
- You can **return** them from other functions

This allows your code to be more **modular**, **flexible**, and **reusable**.

---

## 🔁 Basic Example
```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(name):
    return f"Hello, {name}!"

def speak(style_function, name):
    text = greet(name)
    return style_function(text)

print(speak(shout, "Mohammad"))   # HELLO, MOHAMMAD!
print(speak(whisper, "Sara"))     # hello, sara
```

Instead of hardcoding behavior inside `speak`, we allow it to take a function and apply it — reusable & flexible.

---

## 🎯 Calculator Example with Function Inputs

### ✅ Step 1: Define operations
```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y
```

### ✅ Step 2: Reusable calculator function
```python
def calculate(x, y, operation):
    return operation(x, y)
```

### ✅ Step 3: Use it
```python
print(calculate(5, 3, add))        # ➡️ 8
print(calculate(5, 3, subtract))   # ➡️ 2
print(calculate(5, 3, multiply))   # ➡️ 15
print(calculate(5, 3, divide))     # ➡️ 1.666...
```

### 🧠 But why not just call multiply(x, y)?
> You **can** — but what if you're building something generic (e.g., a UI calculator, API endpoint, math pipeline)?

You might:
- Pass the function as a parameter
- Choose it from a user input
- Store it in a dictionary for later use

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

op = input("Choose operation: ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if op in operations:
    result = calculate(x, y, operations[op])
    print("Result:", result)
```
This wouldn't be possible if you hardcoded each function.

---

## 🧱 Composable Functions

### Compose = Combine simple functions into more powerful ones.
```python
def compose(f, g):
    return lambda x: f(g(x))

double = lambda x: x * 2
square = lambda x: x ** 2

combined = compose(square, double)  # square(double(x))
print(combined(3))  # ➡️ 36
```
You can plug this into any system later, like data pipelines or games.

---

## 🔄 Reusable List Processor
Instead of repeating logic, make a generic processor:

```python
def process_list(lst, operation):
    return [operation(x) for x in lst]

print(process_list([1, 2, 3], lambda x: x * 2))    # [2, 4, 6]
print(process_list([1, 2, 3], lambda x: x ** 2))   # [1, 4, 9]
print(process_list([1, 2, 3], lambda x: -x))       # [-1, -2, -3]
```

You can even define:
```python
def plus_five(x):
    return x + 5

print(process_list([1, 2, 3], plus_five))  # ➡️ [6, 7, 8]
```

---

## 🐢 Real-Life: Turtle Key Binding

```python
def move_up():
    turtle.setheading(90)
    turtle.forward(50)

screen.onkey(move_up, "Up")
```
Here, `move_up` is passed as a **function**, not called. The turtle will call it **when the user presses the key**.

This is what makes games and UIs work reactively.

---

## ✅ Summary Table
| Situation                        | Use function input? |
|----------------------------------|---------------------|
| Apply different behaviors        | ✅ Yes              |
| React to user input              | ✅ Yes              |
| Avoid code duplication           | ✅ Yes              |
| Write simpler modular code       | ✅ Yes              |
| Just calling one fixed function  | ❌ No               |

---

## 💬 Final Thoughts
Using functions as inputs may seem strange at first, but it unlocks powerful patterns:
- Dynamic behavior
- Clean architecture
- Plugin systems
- Event-driven logic

Once you get comfortable with it, it becomes one of your strongest tools in Python!
import time


def delay_decorator(original_function):
    def wrapper_function():
        print("Waiting 2 seconds...")
        time.sleep(2)
        original_function()
        print("Finished running the function.")

    return wrapper_function


# Using the @ syntax
@delay_decorator
def say_hello():
    print("Hello!")


@delay_decorator
def say_bye():
    print("Goodbye!")


# Without @ syntax
def say_greeting():
    print("How are you?")


decorated_greeting = delay_decorator(say_greeting)

# Running
say_hello()
say_bye()
decorated_greeting()
