""" Multiple Inheritance Example in Python 3. """

class MY_A:
    """A simple example class A"""

    def do_it(self):
        print("method of Class A is called")

class MY_B(MY_A):
    "A class B that inherits Class A. "
    # pass


class MY_C(MY_A):
    "A class C that also inherits Class A. "

    def do_it(self):
        print("method of Class C is called")


class MY_D(MY_B, MY_C):
    "A class D that inherits both Classes B and C. Multiple Inheritance. "
    # pass


def main():
    myobject = MY_D()
    myobject.do_it()

    # Multiple inheritance with old-style classes is governed by two rules:
    # depth-first and then left-to-right.
    # The order is driven using a set of rules called Method Resolution Order (MRO).
    print(MY_D.mro())


if __name__ == "__main__":
    main()
