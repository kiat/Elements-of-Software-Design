#  File: HelloWorld.py

# run this python script as following
# python3  Example-Script-001-HelloWorld.py  < example_data.in 


import sys

def main():
  x = sys.stdin.read()
  
  print(x)
  print(type(x))

  a = x.split("\n")

  print(a[0])

  for value in a:
    print(value)



  print(sys.stdin.read())
  print("HelloWorld")


if __name__ == "__main__":
  main()
