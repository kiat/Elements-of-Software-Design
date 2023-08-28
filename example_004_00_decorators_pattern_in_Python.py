""" A simple Example for a program timing problem with a decorator pattern."""

from time import time


def timer(func):
    """A decorator to time a given function."""
    def time_func(num1, num2=1):
        before = time()
        ret_val = func(num1, num2)
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
