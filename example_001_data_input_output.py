"""
  Run this python script as following
  python3  example_001_data_input_output.py  < example_data.in
"""
import sys


def main():
    """This function simulates how we read data from standard input, and write to it."""
    # 1. Using sys and stdin .
    # You can do a normal print to write.
    string_values = sys.stdin.read()
    print(string_values)
    print(type(string_values))

    lines = string_values.split("\n")

    print(lines[0])

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
    