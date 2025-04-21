
# 🧠 Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a way to structure and design code using **classes** and **objects**. It helps organize complex programs, reuse code, and model real-world systems.

---

## 🔷 What is a Class?

A **class** is a blueprint for creating **objects**. Objects combine **data** (attributes) and **behavior** (methods).

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")
```

---

# 🔑 The 4 Pillars of OOP

---

## 1. 🧱 Encapsulation

**Definition**: Wrapping data and related methods together. It hides the internal state and requires all interaction to be performed through an object’s methods.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

**✔️ Benefit**: Protects internal data from unauthorized access.

---

## 2. 🎯 Abstraction

**Definition**: Hiding the complex implementation details and exposing only the necessary parts.

```python
class Car:
    def start_engine(self):
        print("Engine started")

# Usage
my_car = Car()
my_car.start_engine()
```

**✔️ Benefit**: The user doesn’t need to know how the engine works — only how to start it.

---

## 3. 🧬 Inheritance

**Definition**: A class can inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()
```

**✔️ Benefit**: Promotes code reuse and logical hierarchy.

---

## 4. 🎭 Polymorphism

**Definition**: Different objects can respond to the same method in different ways.

```python
class Cat:
    def speak(self):
        print("Meow")

class Bird:
    def speak(self):
        print("Tweet")

animals = [Cat(), Bird()]
for animal in animals:
    animal.speak()
```

**✔️ Benefit**: Write flexible code that works with multiple object types.

---

## ✅ Summary Table

| Concept        | Description                               | Purpose                      |
|----------------|-------------------------------------------|------------------------------|
| Encapsulation  | Hide and group data + methods             | Protect and organize data    |
| Abstraction    | Hide internal complexity                  | Simplify usage               |
| Inheritance    | Use code from a parent class              | Reuse and extend behavior    |
| Polymorphism   | One interface, different implementations  | Write flexible, reusable code|

---

💡 **Tip**: Use classes when you want to model real-world entities, reuse logic, or organize your code better.
