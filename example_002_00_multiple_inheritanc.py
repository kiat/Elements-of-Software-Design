""" Multiple Inheritance Example in Python 3. """
import math

class MyA:
    """A simple example class A"""
    def __init__(self, my_x, my_y):
        self.my_x = my_x
        self.my_y = my_y

    def calculate(self):
        """A simple root square calculation."""
        return math.sqrt(self.my_x**2 + self.my_y**2)

    def do_it(self):
        """A simple method do demonstrate the call of this function. """
        print("method of Class A is called")
        print(self.calculate())

class MyB(MyA):
    "A class B that inherits Class A. "
    # pass


class MyC(MyA):
    "A class C that also inherits Class A. "

    def do_it(self):
        """A simple method do demonstrate the call of this function. """
        print("method of Class C is called")


class MyD(MyB, MyC):
    "A class D that inherits both Classes B and C. Multiple Inheritance. "
    # pass


def main():
    """A main function to create objects of the above classes."""
    myobject = MyD(2,2)
    myobject.do_it()

    # Multiple inheritance with old-style classes is governed by two rules:
    # depth-first and then left-to-right.
    # The order is driven using a set of rules called Method Resolution Order (MRO).
    print(MyD.mro())


if __name__ == "__main__":
    main()
