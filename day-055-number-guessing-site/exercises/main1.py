"""Coding exercise: 
Create a program that will log the name of a function,
its arguments, and its return value. Do this using decorators.
"""


# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args):
        func_name = func.__name__
        message = f"You called {func_name}{args}"
        message = message + f"\nIt returned: {func(*args)}"
        print(message)

    return wrapper


# Use the decorator 👇
@logging_decorator
def multiplier(*args):
    product = 1
    for n in args:
        product *= n

    return product


multiplier(2, 3)
