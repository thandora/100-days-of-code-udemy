""" Printing out the speed it takes to run the fast_function() vs the
slow_function(). You will need to complete the speed_calc_decorator()
function.
"""


import time


def speed_calc_decorator(func):
    def wrapper():
        time_start = time.time()
        func()
        run_time = time.time() - time_start
        print(f"{func.__name__} run speed: {round(run_time, 3)}s")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
