class Queue(object):
  '''Queue implements the FIFO principle.'''
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    if(not self.isEmpty()):
      return self.queue.pop(0)
    else:
      return None
    
  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)
  
  # a string representation of this stack.
  def __str__(self):
    return str(self.queue)


###############################
#                             #
#   Example run of a Queue    #
#                             #
###############################

my_queue = Queue()

# enqueue 10
my_queue.enqueue(10)
print(my_queue)

# enqueue 18
my_queue.enqueue(18)
print(my_queue)


# enqueue 1024
my_queue.enqueue(1024)
print(my_queue)


# dequeue()
print("Dequeue ", my_queue.dequeue())
print("Dequeue ", my_queue.dequeue())
print("Dequeue ", my_queue.dequeue())
print("Dequeue ", my_queue.dequeue())
