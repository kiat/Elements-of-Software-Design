class Node(object):
    '''This class represents a single Node.'''
    def __init__ (self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):
        
        if self.rChild != None:
            self.rChild.print_node(level + 1)
        
        print(' ' * 4 * level + '->',  self.data)
        
        if self.lChild != None:
            self.lChild.print_node(level + 1)



class BST(object):
    '''This class representa a Binary Search Tree.'''

    def __init__ (self):
        self.root = None
    
    def print(self, level):
        if not self.root == None:
            self.root.print_node(level)

    # Search for a node with the key
    def search(self, key):
        current = self.root
        while ((current != None) and (current.data != key)):
            if (key < current.data):
                current = current.lChild
            else:
                current = current.rChild
            return current

    # Insert a node in the tree
    def insert(self, val):
        newNode = Node(val)
        
        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
        
            while (current != None):
                parent = current
                if (val < current.data):
                    current = current.lChild
                else:
                    current = current.rChild

            if (val < parent.data):
                    parent.lChild = newNode
            else:
                    parent.rChild = newNode

    # In order traversal - left, center, right
    def inOrder(self, aNode):
        if (aNode != None):
            self.inOrder (aNode.lChild)
            print(aNode.data)
            self.inOrder (aNode.rChild)

    # Pre order traversal - center, left, right
    def preOrder(self, aNode):
        if (aNode != None):
            print(aNode.data)
            self.preOrder(aNode.lChild)
            self.preOrder(aNode.rChild)

    # Post order traversal - left, right, center
    def postOrder(self, aNode):
        if (aNode != None):
            self.postOrder (aNode.lChild)
            self.postOrder (aNode.rChild)
            print(aNode.data)

    # Find the node with the smallest value
    def minimum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.lChild
        return parent

    # Find the node with the largest value
    def maximum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.rChild
        return parent

    # Delete a node with a given key
    def delete(self, key):
        deleteNode = self.root
        parent = self.root
        isLeft = False

        # If empty tree
        if (deleteNode == None):
            return False

        # Find the delete node
        while ((deleteNode != None ) and (deleteNode.data != key)):
            parent = deleteNode
            if (key < deleteNode.data):
                deleteNode = deleteNode.lChild
                isLeft = True
            else:
                deleteNode = deleteNode.rChild
                isLeft = False
            
        # If node not found
        if (deleteNode == None):
            return False

        # Delete node is a leaf node
        if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
            if (deleteNode == self.root):
                self.root = None
            elif (isLeft):
                parent.lChild = None
            else:
                parent.rChild = None

        # Delete node is a node with only left child
        elif (deleteNode.rChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.lChild
            elif (isLeft):
                parent.lChild = deleteNode.lChild
            else:
                parent.rChild = deleteNode.lChild

        # Delete node is a node with only right child
        elif (deleteNode.lChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.rChild
            elif (isLeft):
                parent.lChild = deleteNode.rChild
            else:
                parent.rChild = deleteNode.rChild

        # Delete node is a node with both left and right child
        else:
            # Find delete node's successor and successor's parent nodes
            successor = deleteNode.rChild
            successorParent = deleteNode

            while (successor.lChild != None):
                successorParent = successor
                successor = successor.lChild

            # Successor node right child of delete node
            if(deleteNode == self.root):
                self.root = successor
            elif (isLeft):
                parent.lChild = successor
            else:
                parent.rChild = successor

            # Connect delete node's left child to be successor's left child
            successor.lChild = deleteNode.lChild

            # Successor node left descendant of delete node
            if(successor != deleteNode.rChild):
                successorParent.lChild = successor.rChild
                successor.rChild = deleteNode.rChild

        return True
    




###############################
#                             #
#   Example run of a BST run  #
#                             #
###############################

def main():

    bst = BST()

    bst.insert(10)
    bst.insert(20)
    bst.insert(30)
    bst.insert(5)
    bst.insert(12)
    bst.insert(4)
    bst.insert(7)
    bst.insert(18)
    
    bst.print(2)
    
    print("In-order traversal:")
    bst.inOrder(bst.root)
    print("Post-order traversal")
    bst.postOrder(bst.root)
    print("Pre-order traversal")
    bst.preOrder(bst.root)

    # test deleting a node with two children and whose successor
    # had a right child 
    bst.delete(10)
    bst.print(2)

    print()
    print()

    # delete a leaf node (no children)
    bst.delete(4)
    bst.print(2)

    print()
    print()
    
    # delete a node with only a right child
    bst.delete(5)
    bst.print(2)

    print()
    print()
    
    bst.delete(30)
    bst.print(2)

    print()
    print()
    
    # test deleting a non-existing object
    bst.delete(5)
    bst.print(2)

    print()
    print()
    # delete a node with only a left child
    bst.delete(20)
    bst.print(2)

    print()
    print()
    # delete all nodes and try one extra delete
    bst.delete(12)
    bst.delete(18)
    bst.delete(7)
    bst.delete(7)
    bst.print(2)
    

if __name__ == "__main__":
    main()

