class MinHeightTree:
    def __init__(self, values) -> None:
        self.values = values

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def invertBinaryTree(tree):
    if tree is None:
        return None
    left =  invertBinaryTree(tree.left)
    right = invertBinaryTree(tree.right)
    if left is None and  right is  None:
        return tree
    temp = left
    tree.left = right
    tree.right = temp
    return tree

def invertBinaryTreeIterative(tree):
    while tree.left is not None or tree.right is not None:
        temp = tree.left
        tree.left = tree.right
        tree.right = temp
    return tree
    


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.right.left = BinaryTree(6)
root.right.right =  BinaryTree(7)

invertBinaryTreeIterative(root)



