"""
# This is an example to read from standard input.
# Run this python script as following
# python3  Python-Scripts/example002_hello_world.py < Python-Scripts/example_data.in
"""


import sys

def main():
    """This is a main function"""
    data = sys.stdin.read()
  
    print(data)
    print(type(data))

    data_list = data.split("\n")

    print(data_list[0])

    for value in data_list:
        print(value)

    print("HelloWorld")

if __name__ == "__main__":
    main()
