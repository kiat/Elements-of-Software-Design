"""Example Multiple Inheritance."""
import math


class MyA:
    """A simple example class A"""

    def __init__(self, my_x, my_y):
        self.my_x = my_x
        self.my_y = my_y

    def calculate(self):
        """A simple root square calculation."""
        return math.sqrt(self.my_x**2 + self.my_y**2)

    def do_it(self, *args):
        """A simple method to demonstrate the call of this function. """
        print("method of Class A is called")
        print(self.calculate())
        if len(args)>0:
            print("Arguments given.")


class MyC(MyA):
    """A simple example class C inheriting from class A"""

    def __init__(self, my_x, my_y, my_z):
        # Call the constructor of the base class (MyA) using super()
        super().__init__(my_x, my_y)
        self.my_z = my_z

    def calculate(self):
        """A simple root cube calculation."""
        return math.sqrt(self.my_x**2 + self.my_y**2 + self.my_z**2)

    def do_it(self, *args):
        """Another method of do_it in the subclass MyC"""
        print(f"method of Class C with argument {args[0]} is called")
        print(self.calculate() + args[0])


def main():
    """A main function to create objects of the above classes."""
    # Usage:
    obj_a = MyA(3, 4)
    obj_a.do_it()

    obj_c = MyC(3, 4, 5)
    obj_c.do_it(10)

    # obj_c.do_it()
    # You can not have another obj_c.do_it()
    # You will get
    # TypeError: MyC.do_it() missing 1 required positional argument: 'x_val'

    # Solution: use  *args and **kwargs arguments;

    # Multiple inheritance with old-style classes is governed
    # by two rules: depth-first and then left-to-right.
    # more info here https://www.geeksforgeeks.org/multiple-inheritance-in-python/


if __name__ == "__main__":
    main()
