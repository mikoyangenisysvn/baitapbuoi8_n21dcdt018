class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while temp:
            if value == temp.value:
                return False
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

# Test the implementation
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Test insert method
    assert bst.insert(10) == True
    assert bst.insert(5) == True
    assert bst.insert(15) == True
    assert bst.insert(10) == False # Duplicate value
    
    print("Insert method for BinarySearchTree class is implemented successfully!")
