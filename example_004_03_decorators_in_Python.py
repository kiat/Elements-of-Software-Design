"""Now we want to run the timer n times."""

from time import time

# def timer(func):
#     def f(*args, **kwargs):
#         before = time()
#         rv = func(*args, **kwargs)
#         after = time()
#         print("Elapsed Time is: ", after - before)
#         return rv
#     return f

N = 4


def ntimes(func):
    """A decorator to time a function n times."""
    def wrapper(*args, **kwargs):
        for _ in range(N):
            before = time()
            ret_val = func(*args, **kwargs)
            after = time()
            print("Elapsed Time is: ", after - before)
        return ret_val
    return wrapper


@ntimes
def add(num1, num2=1):
    """A simple function to add two numbers. """
    return num1 + num2


@ntimes
def mult(num1, num2=1):
    """A simple function to multiply. """
    return num1 * num2


print("add(1,2) = ", add(1, 2))

print("mult(2,3) = ", mult(2, 3))
