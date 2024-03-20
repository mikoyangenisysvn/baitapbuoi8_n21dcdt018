class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def contains(self, target):
        temp = self.root
        while temp is not None:
            if target == temp.value:
                return True
            elif target < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

# Example usage:
# Create a Binary Search Tree
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(9)

# Check if a value exists in the tree
print(bst.contains(4))  # Output: True
print(bst.contains(8))  # Output: False
