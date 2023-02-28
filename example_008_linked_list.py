class Link():
  ''' This class represents a link between data items only'''
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data) + " --> " + str(self.next)



class LinkedList():
  ''' This class implements the operations of a simple linked list'''
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    '''inset data at begining of a linked list'''
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    ''' Inset the data at the end of a linked list '''
    newLink = Link(data)
    current = self.first

    if (current == None):
      self.first = newLink
      return
    # find the last and insert it there. 
    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink(self, data):
    ''' find to which data is the link of a given data inside this linked list'''
    current = self.first
    if (current == None):
      return None

    # searcg and find the position of the given data, the get the link if. 
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink(self, data):
    ''' Removes the data from the list if exist and fix the link problems.'''

    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
    
      current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  def __str__(self):
    return str(self.first)

#####################################
#                                   #
#   Example run of a Linked List    #
#                                   #
#####################################
def main():


  my_list = LinkedList()


  my_list.insertFirst(10)
  print(my_list)


  my_list.insertFirst(20)
  print(my_list)


  my_list.insertFirst(30)
  print(my_list)


  my_list.insertLast(1)
  print(my_list)


  print("Find Link of 10 : It is  ", my_list.findLink(10))


  my_list.deleteLink(20)
  print(my_list)


if __name__ == '__main__':
    main()
