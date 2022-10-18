import sys
class Max_heap:
    '''
    Max Heap Implementation in Python
    '''
    def __init__(self):
        '''
        On this implementation the heap list is initialized with a value
        '''
        # We do not use the index 0 
        # Index zero is always a very large number as placeholder. 
        self.heap_list = [sys.maxsize]

    @property
    def size(self):
        '''Returns the size of this heap'''
        return len(self.heap_list) - 1 
 

    def parent(self, index):
        ''' Return the parent of a node at index'''
        return index // 2


    def l_child(self, index):
        '''Return the position of the left child node of a given index'''
        return 2 * index

    def r_child(self, index):
        '''Return the position of the right child node of a given index'''
        return (2 * index) + 1

    def is_leaf(self, index):
        ''' Returns true if the given index is a leaf node'''
        return index * 2 > self.size 


    def swap(self, from_pos, to_pos):
        '''A helper function to swap two nodes of the heap'''
        self.heap_list[from_pos], self.heap_list[to_pos] = self.heap_list[to_pos], self.heap_list[from_pos]
        

    def insert(self, element):
        '''
        It inserts an element to the heap structure and maintain the heap property. 
        '''
        self.heap_list.append(element)

        current = self.size

        while (self.heap_list[current] > self.heap_list[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)


 
    def __str__(self):
        '''A simple str function to print the contents of the heap'''
        return str(self.heap_list)

    def max_heapify(self, i):
        '''
        # Function to heapify the node at index
        '''
        l = self.l_child(i)
        r = self.r_child(i)

        if l <= self.size and self.heap_list[l] > self.heap_list[i]:
            largest = l
        else:
            largest = i

        if r <= self.size and self.heap_list[r] > self.heap_list[largest]:
            largest = r 

        if largest != i :
            self.swap(i, largest)
            self.max_heapify(largest)


    def build_max_heap(self, unsorted_list):

        # Set the max possible number to the begining of the list 
        unsorted_list.insert(0, sys.maxsize)

        self.heap_list = unsorted_list

        for i in range(len(unsorted_list) // 2 , 1, -1):
            self.max_heapify(i)
            




    def extract_max(self):
        '''Extracts the max of this heap'''

        # 1. pop the root of the tree which is on the index 1 of the list 
        popped = self.heap_list.pop(1)
        
        # 2. Insert the last element of the heap list which is a leaf node and insert it to the root
        if(self.size > 1):
            self.insert(self.heap_list.pop())
        # 3. Call heapify() on the root to fix the error it may have caused. 
            self.max_heapify(1)
    
        return popped

####################################
#                                  #
#   Example run of a MIN HEAP run  #
#                                  #
####################################

def main():

    # Same tree as above example.
    my_heap = Max_heap()
    my_heap.insert(1)
    print(my_heap)
    my_heap.insert(4)
    print(my_heap)
    my_heap.insert(10)
    print(my_heap)
    my_heap.insert(13)
    print(my_heap)
    my_heap.insert(17)
    print(my_heap)

    my_heap.insert(9)
    print(my_heap)
    
    my_heap.insert(22)
    print(my_heap)
    

    print("\nSorted Output")
    for i in range(my_heap.size):
        print(my_heap.extract_max())

# 2. Second test 
# Given an list of integers 

    my_heap.build_max_heap([4,12,45,23,11])
    print(my_heap)





if __name__ == '__main__':
    main()