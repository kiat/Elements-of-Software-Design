""""
The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...
"""


def fib(n):
  """Fibonacci Sequence Iterative"""
  a = 0
  b = 1
  
  for i in range(0, n):
    tmp = a + b 
    a = b
    b = tmp     
  
  return a

# Let us test it if it generates the Fibonacci sequence
for i in range(10):
    print(fib(i))

print("\n##########\n")

def fib(n):
  """Fibonacci Sequence Iterative without temp variable"""
  a , b = 0, 1
  
  for i in range(0, n):
    a, b = b, a+b
  
  return a

# Let us test it if it generates the Fibonacci sequence
for i in range(10):
    print(fib(i))

print("\n##########\n")


def fib(n):
  """Fibonacci Sequence Recursive"""
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fib(n-2) + fib(n-1)

  
# Let us test it if it generates the Fibonacci sequence
for i in range(10):
    print(fib(i))