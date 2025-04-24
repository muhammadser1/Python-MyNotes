
# 🌐 HTTP Basics Cheat Sheet

A fun and practical overview of HTTP Request components and Status Codes.

---

## 📬 HTTP Request: What’s Inside?

An **HTTP request** is what a client (e.g. browser or frontend app) sends to a server. It has several parts:

### 1. 🔗 Method
Tells the server **what action** you want to perform.

| Method | Action              | Use Case                           |
|--------|---------------------|------------------------------------|
| GET    | Retrieve data       | Get a list, view a profile         |
| POST   | Create new data     | Register a user, submit a form     |
| PUT    | Replace data        | Update all fields of a resource    |
| PATCH  | Modify data         | Update specific fields             |
| DELETE | Remove data         | Delete a record                    |

---

### 2. 🌍 URL / Endpoint
The **address** of the resource, e.g.:
```
GET /api/users/123
```

---

### 3. 🧾 Headers
Key-value pairs with extra info about the request.
Examples:
- `Authorization: Bearer <token>`
- `Content-Type: application/json`

---

### 4. 📦 Body (Payload)
Used with POST/PUT/PATCH to **send data** to the server.
Usually in **JSON** format:
```json
{
  "username": "mohammad",
  "email": "test@example.com"
}
```

---

## 📡 HTTP Status Codes — Fun Summary

### 🟦 1xx — Hold On...
> 🔄 **Informational**  
The request was received and is still processing.

- `100 Continue`
- `101 Switching Protocols`

---

### 🟩 2xx — Here You Go ✔️
> ✅ **Success**  
The request was successful!

- `200 OK`: Everything worked
- `201 Created`: New resource created
- `204 No Content`: Success but no content to show

---

### 🟨 3xx — Go Away ➡️
> 🔁 **Redirection**  
You’re being sent elsewhere.

- `301 Moved Permanently`
- `302 Found`
- `304 Not Modified`

---

### 🟥 4xx — You Screwed Up 🚫
> ❌ **Client Error**  
You sent something wrong.

- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`
- `429 Too Many Requests`

---

### ⛔ 5xx — I Screwed Up 💥
> 🧯 **Server Error**  
Server failed to process a valid request.

- `500 Internal Server Error`
- `502 Bad Gateway`
- `503 Service Unavailable`
- `504 Gateway Timeout`

---

## 🧠 Final Tip

> `4xx` → Your mistake.  
> `5xx` → Server mistake.  
> Always check the status code before debugging!

---


response.raise_for_status() — What does it do?
In Python's requests library, calling:

python
Copy
Edit
response.raise_for_status()
means:

🚨 "If the response was an error (4xx or 5xx), raise an exception."

🔍 What happens behind the scenes?
If the response status code is 200–299 → ✅ Does nothing.

If the response status code is 400–599 → ❌ Raises an exception.

https://api.sunrise-sunset.org/json
This is the base URL for the API.

Everything after ? are query parameters.

📬 Query Parameters

Parameter	Required	Description
lat	✅ Yes	Latitude of the location
lng	✅ Yes	Longitude of the location
date	❌ Optional	Date in YYYY-MM-DD format (default: today)
formatted	❌ Optional	0 to get 24-hour ISO 8601 time, 1 (default) for AM/PM format
🧪 Example Request:
url
Copy
Edit
https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400