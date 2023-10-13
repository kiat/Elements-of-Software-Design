class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def _hash2(self, key):
        return 7 - (hash(key) % 7)  # A second hash function (can be customized)

    def _probe_interval(self, key):
        return self._hash2(key)

    def insert(self, key, value):
        index = self._hash(key)
        interval = self._probe_interval(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Key already exists, update the value
                self.values[index] = value
                return

            # Double hashing to find the next available slot
            index = (index + interval) % self.size

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._hash(key)
        interval = self._probe_interval(key)
        start_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            # Double hashing to search for the key
            index = (index + interval) % self.size

            if index == start_index:
                break  # Reached the starting point, key not found

        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        interval = self._probe_interval(key)
        start_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                # Rehash to fill gaps left by removed keys
                self._rehash()
                return

            # Double hashing to search for the key
            index = (index + interval) % self.size

            if index == start_index:
                break  # Reached the starting point, key not found

        raise KeyError(key)

    def _rehash(self):
        new_keys = [None] * self.size
        new_values = [None] * self.size

        for key, value in zip(self.keys, self.values):
            if key is not None:
                index = self._hash(key)
                interval = self._probe_interval(key)

                while new_keys[index] is not None:
                    index = (index + interval) % self.size

                new_keys[index] = key
                new_values[index] = value

        self.keys = new_keys
        self.values = new_values

    def __str__(self):
        return str(list(zip(self.keys, self.values)))

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