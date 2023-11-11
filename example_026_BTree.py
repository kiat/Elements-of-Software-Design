class BTreeNode:
    
    def __init__(self, leaf=True):
        # Constructor to initialize a B-Tree node
        self.leaf = leaf  # Indicates if the node is a leaf
        self.keys = []  # List to store keys
        self.children = []  # List to store child nodes


class BTree:
    def __init__(self, t):
        """
        B-Tree constructor.

        Args:
        - t: Order of the B-Tree
        """
        self.root = BTreeNode(True)  # Initializing the root node
        self.t = t  # Order of the B-Tree

        self.root = BTreeNode(True)
        self.t = t

    def insert(self, k):
        """
        Insert a key into the B-Tree.

        Args:
        - k: Key to insert
        """
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode()
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, k)
            self.root = new_root
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, node, k):
        """
        Insert into a non-full node.

        Args:
        - node: Current node in the B-Tree
        - k: Key to insert
        """
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def _split_child(self, parent, i):
        """
        Split child node of a parent node.

        Args:
        - parent: Parent node
        - i: Index of child node to split
        """
        t = self.t
        child = parent.children[i]
        new_child = BTreeNode(child.leaf)
        parent.children.insert(i + 1, new_child)
        parent.keys.insert(i, child.keys[t - 1])
        new_child.keys = child.keys[t: (2 * t) - 1]
        child.keys = child.keys[0: t - 1]
        if not child.leaf:
            new_child.children = child.children[t: 2 * t]
            child.children = child.children[0: t - 1]

    def search(self, k, node=None):
        """
        Search for a key in the B-Tree.

        Args:
        - k: Key to search
        - node: Starting node for the search
        """

        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and k == node.keys[i]:
            return True
        elif node.leaf:
            return False
        else:
            return self.search(k, node.children[i])

    def display(self, node=None, level=0):
        """
        Display the B-Tree structure.

        Args:
        - node: Node to start the display from (default is the root)
        - level: Level of the node in the B-Tree (default is 0)
        """

        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if not node.leaf:
                self.display(node.children[i], level + 1)
            print("Level", level, "Key", node.keys[i])

        if not node.leaf:
            self.display(node.children[len(node.keys)], level + 1)

def main():
    # Create a B-Tree of order 3
    b_tree = BTree(3)

    # Keys to insert into the B-Tree
    keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]

    # Insert keys into the B-Tree
    for key in keys_to_insert:
        b_tree.insert(key)

    # Display the B-Tree structure
    print("B-Tree structure:")
    b_tree.display()

    # Key to search in the B-Tree
    search_key = 6
    if b_tree.search(search_key):
        print(f"Key {search_key} found in the B-Tree")
    else:
        print(f"Key {search_key} not found in the B-Tree")


if __name__ == "__main__":
    main()