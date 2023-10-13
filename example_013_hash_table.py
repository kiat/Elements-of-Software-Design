class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return
        raise KeyError(key)

    def __str__(self):
        return str(self.table)

# Example usage
if __name__ == '__main__':
    ht = HashTable(10)

    ht.insert("apple", 5)
    ht.insert("banana", 3)
    ht.insert("cherry", 7)

    print(ht)  # Print the hash table

    print("Value for 'apple':", ht.get("apple"))
    print("Value for 'banana':", ht.get("banana"))
    print("Value for 'cherry':", ht.get("cherry"))

    ht.remove("banana")
    print("After removing 'banana':", ht)