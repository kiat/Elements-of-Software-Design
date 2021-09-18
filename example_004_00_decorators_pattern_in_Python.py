from time import time 


def timer(func):
    def f(x, y=1):
        before = time()
        rv = func(x, y)
        after = time()

        print("Elapsed Time is: ", after - before)
        return rv
    return f 


@timer
def add(x, y=1):
    return x + y


@timer
def mult(x, y=1):
    return x * y


print("add(1,2) = ", add(1,2))

print("mult(2,3) = ", mult(2,3))












