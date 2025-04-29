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
