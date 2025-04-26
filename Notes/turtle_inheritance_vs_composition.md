
# 🐢 Inheritance vs Composition in Turtle Games

## ✅ Current Approach: Inheritance

```python
class Player(Turtle):
    ...
```

This means: **“A `Player` _is a_ Turtle.”**

### Advantages:
- Inherits all methods from `Turtle` like `.goto()`, `.ycor()`, `.forward()`.
- No need to create a separate `Turtle` instance.
- Cleaner and shorter code for visual elements.
- Ideal when your class **behaves like** a turtle.

---

## 🤔 Alternative Approach: Composition

```python
class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        ...

    def up(self):
        self.turtle.goto(self.turtle.xcor(), self.turtle.ycor() + 10)
```

This means: **“A `Player` _has a_ Turtle.”**

### Advantages:
- Better separation of logic and visuals.
- More flexibility in large applications.
- Useful if the class includes **multiple objects** (not just a turtle).

---

## 🎯 Why Inheritance Works Well Here

- The `Player` object **is** the turtle that moves on screen.
- Keeps your class **simple and direct**.
- Common practice in turtle-based games like Snake, Crossy Road, etc.

---

## 🔑 Summary Rule of Thumb

| Use | When |
|-----|------|
| **Inheritance** | When your class _is a_ special type of another (e.g., `Player` _is a_ `Turtle`) |
| **Composition** | When your class _has_ other parts (e.g., `Player` _has a_ `Turtle`) |

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz  # ✅ has-a relationship
