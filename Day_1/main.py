# 🔄 Mutable vs Immutable Types

# ✅ Mutable types:
# list, dict, set → Can be changed in-place

# ❌ Immutable types:
# int, float, str, tuple → Cannot be changed after creation
# -------------------------------

# 🔤 String Concatenation & Immutability
print("hello" + " " + "World!")

# 💡 Strings are immutable in Python.
# Every time you use +, Python creates a new string.
# It must copy all characters from word1, the space (" "), and word2 into a new memory block.

# -------------------------------
# 🧠 Variable Reassignment with Immutables

x = 10      # Python creates an int object with value 10
x = 4       # Python creates a new int object with value 4

# 🔍 What really happens?
# Now, x points to the new object (4)
# The original 10 is no longer referenced (can be garbage collected)

# ✅ Python doesn't "change" 10 to 4
# It just binds x to a new object

# 🗑️ What Does "Garbage Collected" Mean?
# In Python, when a variable (like x) is no longer being used or referenced, Python automatically removes it from memory.
# This process is called:
# -------------------------------
# 🔁 Example: Mutable List

my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)

# 🔍 What happens here?
# - Python creates a list object: [1, 2, 3]
# - my_list points to that list
# - Then we modify the first element
# ✅ Since lists are mutable, the change happens in-place — no new object is created

# 📤 Output:
# [10, 2, 3]

# Option 1
name = input("What is your name?\n") # This is the prompt. input() returns a str
print("Hello " + name)
print("Nice to meet you, " + name)

# Option 2
print("Hello " + input("What is your name?\n"))
print("Nice to meet you!")  # Can't reuse the name


# Swapping

glass1 = "milk"
glass2 = "juice"
glass1, glass2 = glass2, glass1


x = 5
print(id(x))  # output: 2359685546352

x = 6
print(id(x)) # output: 2359685546384

my_list = [1, 2, 3]
print(id(my_list))

my_list[0] = 10 # output: 1614968025408
print(id(my_list))  # output: 1614968025408
