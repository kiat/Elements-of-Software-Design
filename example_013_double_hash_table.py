class hash_table_with_double_hashing:
    '''
    A Hash Table with Double Hashing
    '''
    # initialize hash Table

    def __init__(self, size):
        
        self.size = size
        
        # initialize table with all elements 0
        self.table = list(None for i in range(self.size))
        
        self.elementCount = 0
        self.comparisons = 0

    def __str__(self):
        ''' Print the hash table '''
        tmp = ''
        for i in range(self.size):
            tmp = tmp + "[ " + str(i) + " , " + str(self.table[i]) + " ] \n"
        
        return tmp
    

    def is_full(self):
        '''  Checks if the hash table is full or not '''
        if self.elementCount == self.size:
            return True
        else:
            return False

    # First hash function
    def h1(self, element):
        return element % self.size

    # Second hash function
    def h2(self, element):
        return 7 - (element % 7)

    

    def double_hashing(self, key):
        '''
        resolve collision by double hashing method
        '''
        pos_found = False   
        i = 1

        # loop to find the slot
        while i <= self.size:
            # find a new slot by probing
            new_slot = (self.h1(key) + i * self.h2(key)) % self.size
            
            # if new slot is empty then break out of loop and return new slot
            if self.table[new_slot] == None:
                pos_found = True
                break
            else:
                # If the slot is not empty increment the attempt counter i 
                i += 1
        return pos_found, new_slot




    def insert(self, key):
        ''' inserts a data item into the hash table '''

        # checking if the table is full
        if self.is_full():
            print("Hash Table Full")
            return False

        pos_found = False

        position = self.h1(key)

        # checking if the position is empty
        if self.table[position] == None:
            # We found an empty slot, store the element there
            self.table[position] = key
            self.elementCount += 1

        # If collision occured
        else:
            while not pos_found:
                pos_found, position = self.double_hashing(key)
                if pos_found:
                    self.table[position] = key
                    self.elementCount += 1

        return pos_found


if __name__ == '__main__':
    
    table_size = 7
    hash_table = hash_table_with_double_hashing(table_size)
    print(hash_table)

    hash_table.insert(3)
    print(hash_table)

    hash_table.insert(10)
    print(hash_table)

    hash_table.insert(17)
    print(hash_table)