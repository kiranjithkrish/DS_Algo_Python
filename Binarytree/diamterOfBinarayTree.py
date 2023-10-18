class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return binaryTreeInfo(tree).diameter

def binaryTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0)
    leftTreeInfo = binaryTreeInfo(tree.left)
    rightTreeInfo = binaryTreeInfo(tree.right)
    heightOfTree = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
    maxDiameter = max(leftTreeInfo.diameter, rightTreeInfo.diameter, (leftTreeInfo.height + rightTreeInfo.height))
    return TreeInfo(maxDiameter, heightOfTree)

class TreeInfo:
    def __init__(self, diameter, height) -> None:
        self.diameter = diameter
        self.height = height


root = BinaryTree(1)
root.left = BinaryTree(3)
root.right = BinaryTree(2)
root.left.left = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)
root.left.right = BinaryTree(4)
root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)
diameter = binaryTreeDiameter(root)
print(diameter)


