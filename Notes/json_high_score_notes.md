
# 🧠 Using JSON for High Scores in Python Games

---

## 📌 What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight data-interchange format used to store structured data.

**Example:**
```json
{
  "high_score": 42,
  "player_name": "Mohammad"
}
```

---

## ✅ When Should You Use JSON?

| Use Case                                       | Use JSON? | Why? |
|------------------------------------------------|-----------|------|
| Saving just one number (like a score)          | ❌        | Better to use a `.txt` file for simplicity |
| Saving multiple values (like name + score)     | ✅        | JSON handles structured data like dictionaries |
| Saving game state or configuration             | ✅        | JSON supports nested and complex data |
| Storing multiple players' scores               | ✅        | JSON can hold lists of dictionaries |

---

## 🧪 Python Example: Using JSON for High Score

### 🧾 Sample `score_data.json` file:
```json
{
  "high_score": 42,
  "player_name": "Mohammad"
}
```

### 🐍 Load and Save Code:
```python
import json

# Load high score
def load_high_score():
    try:
        with open("score_data.json") as file:
            data = json.load(file)
            return data["high_score"], data["player_name"]
    except FileNotFoundError:
        return 0, "Anonymous"

# Save high score
def save_high_score(score, name):
    data = {
        "high_score": score,
        "player_name": name
    }
    with open("score_data.json", "w") as file:
        json.dump(data, file)
```

---

## 🔁 Performance: Is JSON O(1)?

### ❌ No — JSON loading/saving is **not O(1)**.

| Operation           | Complexity | Why? |
|---------------------|------------|------|
| `json.load(file)`   | O(n)       | Reads the entire file |
| `json.dump(data)`   | O(n)       | Writes the entire data object |
| `dict["key"]`       | ✅ O(1)    | Accessing a key from a Python dictionary in memory |

---

## ✅ Summary

- Use `.txt` for a **single value** (like just a number).
- Use **JSON** when:
  - You need to store more than one value (like name + score).
  - You want the flexibility of structured data.
- Once JSON is loaded into a dictionary, key lookups are O(1).

---

## 💡 Bonus Tip

For larger games, you can also consider:
- `pickle`: For saving Python objects (not human-readable)
- `sqlite3`: For saving high scores in a lightweight embedded database
