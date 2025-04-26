
# HTTP Request Methods (Simple Guide)

HTTP (HyperText Transfer Protocol) defines several **methods** that clients (like browsers or Python programs) use to communicate with servers.

Each method means a different **action**.

---

## The 4 Most Important Methods You Must Know

| Method | Meaning | Common Use | Example |
|:-------|:--------|:-----------|:--------|
| **GET** | 🔎 Fetch data from the server | Read data | Get user info, weather data, articles |
| **POST** | ✏️ Send **new** data to the server | Create something new | Register new user, upload file |
| **PUT** | 🔄 Update **existing** data completely | Replace existing resource | Update user profile, replace a document |
| **DELETE** | ❌ Delete existing data | Remove resource | Delete a user account |

---

## Easy Way to Remember

| Method | Think About It Like... |
|:-------|:----------------------|
| GET | "Give me information" |
| POST | "Here is **new** data, please create it" |
| PUT | "Here is an **updated version** of existing data, replace it" |
| DELETE | "Remove this thing completely" |

---

## More Detailed Behavior

| Method | More Detailed Behavior |
|:-------|:-----------------------|
| **GET** | No body usually; just URL + maybe parameters (query string) |
| **POST** | Sends a **body** (JSON, form data) to **create** a resource |
| **PUT** | Sends a **full body** to **replace** an existing resource (must exist first) |
| **PATCH** (extra) | Only update **part** of a resource (not all) |
| **DELETE** | Tells server to delete a resource |

---

## Example (Real Life)

Imagine a **website that manages users**:

| Action | HTTP Method | What Happens |
|:-------|:------------|:-------------|
| Show a user profile | GET `/user/123` | Fetch data about user 123 |
| Create a new user | POST `/user/` with body `{name: "John", email: "..."}` | Add a new user |
| Update a user profile | PUT `/user/123` with body `{name: "Johnny", email: "new@email.com"}` | Replace user 123's info |
| Delete a user | DELETE `/user/123` | Remove user 123 from database |

---

## How to Send in Python (with `requests`)

```python
import requests

# GET
response = requests.get('https://api.example.com/users')

# POST
data = {"name": "John", "email": "john@example.com"}
response = requests.post('https://api.example.com/users', json=data)

# PUT
update_data = {"name": "Johnny", "email": "new@email.com"}
response = requests.put('https://api.example.com/users/123', json=update_data)

# DELETE
response = requests.delete('https://api.example.com/users/123')
```

✅ Always check if you need to send **headers**, **authorization tokens**, or **special formats** like JSON.

---

## Super Quick Summary Table

| Method | Used To... | Sends Body? |
|:-------|:-----------|:------------|
| GET | Read data | ❌ No |
| POST | Create new data | ✅ Yes |
| PUT | Replace existing data | ✅ Yes |
| DELETE | Delete data | ❌ No |

---

## Final Simple Sentence to Remember

> **GET** = Read, **POST** = Create, **PUT** = Update/Replace, **DELETE** = Remove.

---
