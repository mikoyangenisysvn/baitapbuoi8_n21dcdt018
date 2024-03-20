class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

# Test the implementation
if __name__ == "__main__":
    # Create an instance of BinarySearchTree
    bst = BinarySearchTree()
    
    # Test if root is initialized as None
    assert bst.root == None
    
    print("BinarySearchTree class and constructor are implemented successfully!")
