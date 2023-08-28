"""Now we want to run the timer n times."""

from time import time

def timer(func):
    """A decorator to time a given function."""
    def time_func(*args, **kwargs):
        before = time()
        ret_val = func(*args, **kwargs)
        after = time()

        print("Elapsed Time is: ", after - before)
        return ret_val
    return time_func


@timer
def add(num1, num2=1):
    """A simple function to add two numbers. """
    return num1 + num2


@timer
def mult(num1, num2=1):
    """A simple function to multiply. """
    return num1 * num2


print("add(1,2) = ", add(1, 2))

print("mult(2,3) = ", mult(2, 3))
