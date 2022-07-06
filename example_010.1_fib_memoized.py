
# Recursive Top-Down implementation
def fib(n):
  if(n <= 1):
    return n 
  else:
    return fib(n-1) + fib(n-2)
      



# Recursive, Top-Down, Memoized
mem={}

def fib_memoized(n):
  if( n <= 1):
    return n 
  else:
    if(n-1 in mem):
      tmp_n1=mem.get(n-1)
    else:
      tmp_n1=fib(n-1)
      
    if(n-2 in mem):
      tmp_n2=mem.get(n-2)
    else:
      tmp_n2=fib(n-2)
          
    return tmp_n1 + tmp_n2

# Iterative Buttom-up Method. 
def fib_iter(n):
  a = 0 
  b = 1 
  
  if n<=1:
    return n
  else:
    for i in range(2, n+1):
      c = a + b
      a = b 
      b = c
    return b    


def main():
  print(fib(10))
  
  print(fib_memoized(10))
  print(fib_iter(10))
  



# Call the main function. 
if __name__ == "__main__":
  main()
