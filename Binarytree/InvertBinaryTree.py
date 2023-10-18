def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapChildrenFor(current)
        queue.append(current.left)
        queue.append(current.right)


def swapChildrenFor(current):
    current.left, current.right = current.right, current.left


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)


invertBinaryTree(root)
