

class A:
    def do_it(self):
        print("method of A called")
    
class C(A):
    def do_it(self, *args) :
        print("method of C called n=" + str(n))



x = C()
x.do_it()
x.do_it(2)
# Multiple inheritance with old-style classes is governed by two rules: depth-first and then left-to-right.
# more info here https://www.geeksforgeeks.org/multiple-inheritance-in-python/
