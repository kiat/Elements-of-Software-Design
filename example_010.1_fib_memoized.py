
# Recursive Top-Down implementation
def fib(n):
  if(n <= 1):
    return n 
  else:
    return fib(n-1) + fib(n-2)
      



# Recursive, Top-Down, Memoized
mem={}

def fib_memoized(n):
  if(n in mem):
      return mem.get(n)
    
  if( n <= 1):
    mem[n] = n
    return n 
  else:
    if(n-1 not in mem):
      tmp_n_1=fib_memoized(n-1)
      mem[n-1] = tmp_n_1
    if(n-2 not in mem):
      tmp_n_2=fib_memoized(n-2)
      mem[n-2] = tmp_n_2
    return tmp_n_1 + tmp_n_2
          

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
