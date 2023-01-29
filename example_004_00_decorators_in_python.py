from time import time

# 1. Decorator in python 
# 2. Decorator Pattern in OOP 

def add_numbers(a , b):
    return a + b

def multi(a, b):
    return a * b 

def main():
    a = 12
    b = 20 

# Time it! 
    before = time()
    
    c = add_numbers(a , b)
    
    after = time() 

    elapsed_time = after - before 
    print("Elapsed time is: " ,  f'{elapsed_time:.10f}' , "Miliseconds")

    # Another computation  
    before = time()
    
    c = multi(a, b)

    after = time()
    elapsed_time = after - before 

    print("Elapsed time is: " ,  f'{elapsed_time:.10f}' , "Miliseconds")


if __name__ == "__main__":
    main()