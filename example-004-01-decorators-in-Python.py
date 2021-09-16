from time import time 

# Removed the hard coded variables now. 
# This function now can time any kind of function runs . 
def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
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












