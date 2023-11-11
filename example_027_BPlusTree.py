class BPlusTree:
    def __init__(self, order):
        """
        Initializes a B+Tree with a specified order.

        Args:
        order (int): The maximum number of children for internal nodes.
        """
        self.root = BPlusNode(order)  # Initialize the root node of the B+Tree.

    def search(self, key):
        """
        Searches for a key in the B+Tree.

        Args:
        key: The key to search for in the tree.

        Returns:
        Value associated with the key if found, else None.
        """
        return self.root.search(key)  # Initiates the search from the root node.

    def insert(self, key, value):
        """
        Inserts a key-value pair into the B+Tree.

        Args:
        key: The key to insert.
        value: The value associated with the key.
        """
        self.root.insert(key, value)  # Initiates the insertion from the root node.


class BPlusNode:
    def __init__(self, order):
        """
        Initializes a B+Tree node with a specified order.
        
        Args:
        order (int): The maximum number of children for internal nodes.
        """
        self.order = order  # Maximum number of children for this node.
        self.keys = list()  # List to hold keys.
        self.values = list()  # List to hold values.
        self.children = list() # List to hold child nodes.

    def search(self, key):
        """
        Searches for a key in the current node or its children.
        
        Args:
        key: The key to search for in the node or its children.
        
        Returns:
        Value associated with the key if found, else None.
        """
        if self.is_leaf():  # If it's a leaf node, search directly in this node.
            for i in range(len(self.keys)):
                if key == self.keys[i]:
                    return self.values[i]
            return None
        else:  # If it's an internal node, find the appropriate child to continue the search.
            child_index = self.get_child_index(key)
            return self.children[child_index].search(key)

    def insert(self, key, value):
        """
        Inserts a key-value pair into the current node or its children.
        
        Args:
        key: The key to insert.
        value: The value associated with the key.
        """
        if not self.is_leaf():  # If it's an internal node, find the appropriate child to insert the key-value pair.
            child_index = self.get_child_index(key)
            self.children[child_index].insert(key, value)
        else:  # If it's a leaf node, directly insert the key-value pair.
            self.keys.append(key)
            self.values.append(value)
            self.sort_node()  # Sort the node after insertion.

    def is_leaf(self):
        """
        Checks if the node is a leaf node.

        Returns:
        True if the node is a leaf, False otherwise.
        """
        return len(self.children) == 0

    def get_child_index(self, key):
        """
        Determines the appropriate child index for the given key.
        
        Args:
        key: The key to find the child index for.
        
        Returns:
        The index of the child node for the given key.
        """
        for i in range(len(self.keys)):
            if key < self.keys[i]:
                return i
        return len(self.keys)  # If key is greater than all keys, return the last child index.

    def sort_node(self):
        """
        Sorts the keys and values in the node.
        """
        combined = list(zip(self.keys, self.values))  # Convert to a list to maintain lists for keys and values
        combined.sort(key=lambda x: x[0])  # Sort based on keys
        self.keys, self.values = zip(*combined)  # Unzip the sorted keys and values
        self.keys = list(self.keys)
        self.values = list(self.values)



def main():
    b_plus_tree = BPlusTree(order=3)  # Create a B+Tree with order 3.

    # Insert some key-value pairs
    b_plus_tree.insert(10, "A")
    b_plus_tree.insert(5, "B")
    b_plus_tree.insert(20, "C")
    b_plus_tree.insert(30, "D")

    # # Search for a key
    result = b_plus_tree.search(5)
    print("Value for key 5:", result)  # Output: Value for key 5: B


if __name__ == "__main__":
    main()