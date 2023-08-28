'''Example of a double linked list implementation.'''

class Link():
    '''This class represents a link between data items only.'''

    def __init__(self, data, next_link = None, previous_link=None):
        self.data = data
        self.next = next_link
        self.previous = previous_link

    def print_data(self):
        ''' Print the data contained in this link.'''
        print(self.data)

    def print_previous(self):
        ''' Print the previous link.'''
        if self.previous is not None:
            print(self.previous.data)
        else:
            print("None")

    def print_next(self):
        ''' Print the next link.'''
        if self.next is not None:
            print(self.next.data)
        else:
            print("None")

class DoublyLinkedList():
    '''This class represents a doubly linked list.'''

    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        '''Inserts data at the beginning of the linked list.'''
        if self.head is None:
            new_node = Link(data)
            self.head = new_node
        else:
            new_node = Link(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        '''Inserts data at the end of the linked list.'''
        new_node = Link(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.previous = temp

    def delete(self, data):
        '''Deletes the Link containing data from the linked list.'''
        temp = self.head
        if temp.next is not None:

            # If head node is to be deleted.
            if temp.data == data:
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            while temp.next is not None:
                if temp.data == data:
                    break
                temp = temp.next

                if temp.next:
                    # If element to be deleted is in between.
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    # If element to be deleted is the last element.
                    temp.previous.next = None
                    temp.previous = None
                return

        if temp is None:
            return

    def __str__(self):
        m_string = ''
        temp = self.head
        while temp is not None:
            m_string += str(temp.data) + ' <-> '
            temp = temp.next
        return m_string


############################################
#                                          #
#   Example run of a Doubly Linked List    #
#                                          #
############################################

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_start(1)
    dll.insert_at_start(2)

    print(dll)

    print("\nInsert at End! \n ")
    dll.insert_at_end(3)
    print(dll)

    print("\nInsert at Start! \n")

    dll.insert_at_start(4)
    print(dll)

    print("\nDelete 2 !\n")
    dll.delete(2)
    print(dll)
