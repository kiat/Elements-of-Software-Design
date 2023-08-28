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

# this video describes this code very well https://www.youtube.com/watch?v=r7Dtus7N4pI


def ntimes(num):
    """A decorator to time a function n times."""
    def inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                before = time()
                ret_val = func(*args, **kwargs)
                after = time()
                print("Elapsed Time is: ", after - before)
            return ret_val
        return wrapper
    return inner


@ntimes(2)
def add(num1, num2=1):
    """A simple function to add two numbers. """
    return num1 + num2


@ntimes(3)
def mult(num1, num2=1):
    """A simple function to multiply. """
    return num1 * num2


print("add(1,2) = ", add(1, 2))

print("mult(2,3) = ", mult(2, 3))


# More about the Wrappers
# https://stackoverflow.com/questions/63512189/can-i-run-a-decorated-function-without-a-decorator-functionality
