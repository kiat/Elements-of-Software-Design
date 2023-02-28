class Stack (object):

  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop(self):
    if(not self.isEmpty()):
      return self.stack.pop()
    else:
      return None

  # check what item is on top of the stack without removing it
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size(self):
    return (len(self.stack))

  # a string representation of this stack. 
  def __str__(self):
    return str(self.stack)



###############################
#                             #
#   Example run of a stack    #
#                             #
###############################

def main():

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
  print("isEmpty()   ", my_stack.isEmpty())


  print("pop()  ", my_stack.pop())
  print("pop()  ", my_stack.pop())
  print("pop()  ", my_stack.pop())
  print("isEmpty()   ", my_stack.isEmpty())


if __name__ == '__main__':
    main()
