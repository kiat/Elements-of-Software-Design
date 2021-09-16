from time import time 

# Now we want to run the timer n times. 

# def timer(func):
#     def f(*args, **kwargs):
#         before = time()
#         rv = func(*args, **kwargs)
#         after = time()
#         print("Elapsed Time is: ", after - before)
#         return rv
#     return f 

def ntimes(n):
    def inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                before = time()
                rv = func(*args, **kwargs)
                after = time()
                print("Elapsed Time is: ", after - before)
            return rv
        return wrapper
    return inner




@ntimes(2)
def add(x, y=1):
    return x + y


@ntimes(3)
def mult(x, y=1):
    return x * y


print("add(1,2) = ", add(1,2))

print("mult(2,3) = ", mult(2,3))




# More about the Wrappers 
# https://stackoverflow.com/questions/63512189/can-i-run-a-decorated-function-without-a-decorator-functionality







