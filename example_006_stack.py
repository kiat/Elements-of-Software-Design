"""Example of a Stack implementation."""

class Stack ():
    """This class defines a Stack."""

    def __init__ (self):
        self.stack = []

    def push (self, item):
        """Takes in an item and adds to to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Removes an item from the top of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        """Checks what item is on top of the stack without removing it."""
        return self.stack[len(self.stack) - 1]

    def is_empty (self):
        """Checks if a stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.stack)

    def __str__(self):
        """A string representation of this stack."""
        return str(self.stack)

###############################
#                             #
#   Example run of a stack    #
#                             #
###############################

def main():
    """A main function to demonstrate the Stack functions."""

    my_stack = Stack()

    # Push 10
    my_stack.push(10)
    print(my_stack)

    # Push 18
    my_stack.push(18)
    print(my_stack)

    # Push 1024
    my_stack.push(1024)
    print(my_stack)

    # pop()
    print("pop()  ", my_stack.pop())

    # peek()
    print("peak()  ", my_stack.peek())

    # isEmpty()
    print("isEmpty()   ", my_stack.is_empty())

    print("pop()  ", my_stack.pop())
    print("pop()  ", my_stack.pop())
    print("pop()  ", my_stack.pop())
    print("isEmpty()   ", my_stack.is_empty())

if __name__ == '__main__':
    main()
