class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# def findSuccessor(tree, node):
#     # Write your code here.
#     return findSuccessorHelper(tree, node, None)

def findSuccessor(tree, node):
    if node is None:
        return None
    if node.right:
        return leftMostNode(node.right)
    current = node
    while current.parent != None and current.parent.right == node:
        current = current.parent
    return current.parent

    
def leftMostNode(rightNode):
    if rightNode.left:
        current = rightNode
        while(current.left != None):
            current = current.left
        return current
    return rightNode
    


def findSuccessorHelper(tree, node, successor):
    if tree is None:
        successor = None
        return None
    elif tree.value == node.value:
        successor = tree.left if tree.left is not None else tree.right
    findSuccessorHelper(tree.left, node, None)
    print(tree.value)
    findSuccessorHelper(tree.right, node, None)
    return successor

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.parent = root
root.right.parent = root
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.left.left.parent = root.left
root.left.right.parent = root.left
root.left.left.left = BinaryTree(6)
root.left.left.left.parent = root.left.left

node = findSuccessor(root, root.right )
print(node)