'''Example of a Queue implementation.'''

class Queue():
    '''Queue implements the FIFO principle.'''  
    def __init__ (self):
        self.queue = []

    def enqueue(self, item):
        '''Takes in an item and adds it to the end of the queue.'''
        self.queue.append(item)

    def dequeue(self):
        '''Removes an item from the end of the queue.'''
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        '''Checks if the queue is empty.'''
        return len (self.queue) == 0

    def size(self):
        '''Returns the number of elements in the queue.'''
        return len(self.queue)

    def __str__(self):
        '''Returns a string representation of the queue.'''
        return str(self.queue)


###############################
#                             #
#   Example run of a Queue    #
#                             #
###############################

def main():
    '''A main function to demonstrate the queue functions.'''

    my_queue = Queue()

    # Enqueue 10
    my_queue.enqueue(10)
    print(my_queue)

    # Enqueue 18
    my_queue.enqueue(18)
    print(my_queue)


    # Enqueue 1024
    my_queue.enqueue(1024)
    print(my_queue)


    # dequeue()
    print('Dequeue ', my_queue.dequeue())
    print('Dequeue ', my_queue.dequeue())
    print('Dequeue ', my_queue.dequeue())
    print('Dequeue ', my_queue.dequeue())


if __name__ == '__main__':
    main()
