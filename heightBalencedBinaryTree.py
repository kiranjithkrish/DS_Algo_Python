# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, height, balenced) -> None:
        self.height = height
        self.balenced = balenced

def heightBalancedBinaryTreeHelper(tree, info):
    if tree is None :
        return TreeInfo(1, True)
    leftInfo = heightBalancedBinaryTreeHelper(tree.left)
    rightInfo = heightBalancedBinaryTreeHelper(tree.right)
    height = 1 + max(leftInfo.height, rightInfo.height)
    diff = abs(leftInfo.height-rightInfo.height)
    isBalenced = diff<2 and leftInfo.balenced and rightInfo.balenced
    return TreeInfo(height, isBalenced)

def heightBalancedBinaryTree(tree):
    # if tree is  None:
    #     return 0
    # lH = heightBalancedBinaryTree(tree.left)
    # rH = heightBalancedBinaryTree(tree.right)
    # diff = lH-rH
    # H = 1+lH+rH
    return heightBalancedBinaryTreeHelper(tree)

    

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.left.right.left = BinaryTree(7)
root.left.right.right = BinaryTree(8)
root.right.right =  BinaryTree(6)
root.right.right.left =  BinaryTree(9)
root.right.right.right =  BinaryTree(10)

height = heightBalancedBinaryTree(root)
print(height)