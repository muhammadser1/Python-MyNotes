def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        res = function(*args)
        print(f"It returned: {res}")
        return res

    return wrapper


@logging_decorator
def a_function(*args):
    print("Executing the main function logic...")
    return sum(args)


print("Starting the program...")
a_function(1, 2, 3)
