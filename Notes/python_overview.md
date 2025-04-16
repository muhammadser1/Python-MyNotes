## 🐍 **Python Overview**

### 🧪 Interpreted
- The code is **run line by line** by a program called the **interpreter**.
- You **don’t compile** the code into machine language (like C or C++) before running it.
- The interpreter reads your `.py` file and **executes each line directly**.

### 🔣 Dynamically Typed
- No need to declare variable types.
- Easy to write, but may be slower since types are checked at **runtime**.

---

## 🔒 Global Interpreter Lock (GIL)

- Python’s **GIL** allows **only one thread** to execute Python bytecode at a time.
- Useful for **I/O-bound tasks** but **limits multi-core CPU usage** for **CPU-bound tasks**.

### 🔄 Where GIL Matters

#### ✅ Multithreading (Good for I/O-bound)
```python
import threading
import time

def download():
    print("Start downloading...")
    time.sleep(2)
    print("Done!")

thread1 = threading.Thread(target=download)
thread2 = threading.Thread(target=download)
thread1.start()
thread2.start()
```

**Why this works well:**
- The program **spends most time waiting** (e.g., for network or disk).
- While one thread waits, the **GIL is released**, allowing others to proceed.

---

#### ❌ CPU-Bound Task (Bad with GIL)

```python
import threading

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def count_primes(limit):
    count = 0
    for num in range(2, limit):
        if is_prime(num):
            count += 1
    print(f"Found {count} primes up to {limit}")

thread1 = threading.Thread(target=count_primes, args=(100_000,))
thread2 = threading.Thread(target=count_primes, args=(100_000,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
```

**Why this is slow:**
- Threads **compete for the GIL**.
- No real parallelism — only one thread runs at a time.
- Doesn’t utilize multiple CPU cores.

---

### ✅ Multiprocessing (Bypasses GIL)

```python
from multiprocessing import Process

# Same function from above
process1 = Process(target=count_primes, args=(100_000,))
process2 = Process(target=count_primes, args=(100_000,))

process1.start()
process2.start()
process1.join()
process2.join()
```

**Why this works:**
- Each process has its **own Python interpreter and GIL**.
- True parallel execution across **multiple CPU cores**.

---

## 🐢 Why is Python Slower Than C++/Java?

- 🧪 Interpreted – Not compiled to native code.
- 🔣 Dynamically typed – Type checks are done during runtime.
- 🗑️ Uses **garbage collection** and **reference counting**.
- 🔒 GIL limits multi-threaded performance for CPU-bound tasks.
