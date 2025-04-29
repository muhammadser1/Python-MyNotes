## ********Day 55 Start - 100 Days of Code **********
## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(*args, **kwargs)
        else:
            print("Access denied. User not logged in.")
    return wrapper



@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)

new_user = User("mo")
create_blog_post(new_user)




# def logging_decorator(function):
#     def wrapper(*args):
#         print(f"You called {function.__name__}{args}")
#         res = function(*args)
#         print(f"It returned: {res}")
#         return res
#
#     return wrapper
#
#
# @logging_decorator
# def a_function(*args):
#     print("Executing the main function logic...")
#     return sum(args)
#
#
# print("Starting the program...")
# a_function(1, 2, 3)
