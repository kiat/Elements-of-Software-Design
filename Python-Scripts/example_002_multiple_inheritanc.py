
# run this script with python3 and pytho2.7 to see the difference. 

# change to 
# class A(object):
# to see the difference. 

class A:
    def do_it(self):
        print("method of A called")

class B(A):
    pass
    
class C(A):
    def do_it(self):
        print("method of C called")

class D(B,C):
    pass

x = D()
x.do_it()

# Multiple inheritance with old-style classes is governed by two rules: depth-first and then left-to-right.

# for more details look here https://www.geeksforgeeks.org/multiple-inheritance-in-python/