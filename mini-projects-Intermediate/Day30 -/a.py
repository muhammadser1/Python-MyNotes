def inner():
    raise ValueError("Something went wrong")

def middle():
    inner()

def outer():
    try:
        middle()
    except ValueError as e:
        print("Caught error:", e)
outer()
# Output: Caught error: Something went wrong
