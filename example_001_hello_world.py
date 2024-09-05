import sys

def main():
    d = sys.stdin.read()
    print(d)
    print(type(d))
    data_list = d.split("\n")
    print(data_list[0])

    for value in data_list:
        print(value)

    print("HelloWorld")
if __name__ == "__main__":
    main()
