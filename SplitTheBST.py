# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, split , sum) -> None:
        self.split = split
        self.sum = sum

# def splitBinaryTree(tree):
#     info =  splitBinaryTreeH(tree, TreeInfo(False, 0))
#     return info.sum if info.split else 0
def splitBinaryTree2(tree):
    total = getTreeSum(tree)
    desiredSum = total/2
    info =  splitBinaryTreeH(tree, TreeInfo(False, 0), desiredSum)
    return info.sum if info.split else 0

def splitBinaryTreeH(tree, treeInfo, desiredSum):
    if tree is None:
        return TreeInfo(False, 0)
    leftSum = splitBinaryTreeH(tree.left, treeInfo, desiredSum)
    rightSum = splitBinaryTreeH(tree.right, treeInfo, desiredSum)
    total =  tree.value + leftSum.sum + rightSum.sum
    if total == desiredSum or leftSum.split is True and rightSum.split is True:
        return TreeInfo(True, total)
    else:
        return TreeInfo(False, total)

def splitBinaryTree(tree):
    desiredSubtreeSum = getTreeSum(tree)/2
    canBeSplit = trySubtrees(tree, desiredSubtreeSum)[1]
    return desiredSubtreeSum if canBeSplit else 0


def trySubtrees(tree, desiredSum):
    if tree is None:
        return (0, False)
    leftSum, leftCanSplit = trySubtrees(tree.left, desiredSum)
    rightSum, rightCanSplit = trySubtrees(tree.right, desiredSum)
    currentTreeSum = tree.value + leftSum + rightSum
    canBeSplit = currentTreeSum == desiredSum or leftCanSplit or rightCanSplit
    return (currentTreeSum, canBeSplit)
    


def getTreeSum(tree):
    if tree is None:
        return 0
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)




root = BinaryTree(1)
#root.left = BinaryTree(2)
#root.right = BinaryTree(2)
# root.left.left = BinaryTree(6)
# root.left.right = BinaryTree(-5)
# root.left.left.left = BinaryTree(2)
# root.right.left = BinaryTree(5)
#root.right.right =  BinaryTree(4)

sum = splitBinaryTree2(root)
print(sum)