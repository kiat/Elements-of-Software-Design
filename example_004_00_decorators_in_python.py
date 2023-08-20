""" A simple Example for a program timing problem."""

from time import time

# 1. Decorator in python
# 2. Decorator Pattern in OOP

def add_numbers(my_a, my_b):
    """A simple function to add two numbers. """
    return my_a + my_b


def multi(my_a, my_b):
    """A simple function to multiply. """
    return my_a * my_b


def main():
    """A main function to demonstrate it."""
    my_a = 12
    my_b = 20

    # Start of timing.
    before = time()

    my_c = add_numbers(my_a, my_b)

    after = time()

    elapsed_time = after - before
    print("Elapsed time is: ",  f'{elapsed_time:.10f}', "Milliseconds")

    # Another computation
    before = time()

    my_c = multi(my_a, my_b)

    after = time()
    elapsed_time = after - before

    print("Elapsed time is: ",  f'{elapsed_time:.10f}', "Milliseconds")
    print(my_c)


if __name__ == "__main__":
    main()
