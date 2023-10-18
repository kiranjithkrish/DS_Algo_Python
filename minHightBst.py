def minHeightBst(array):
    bst = minHeightBstHelperMethodTwo(array,None, 0, len(array)-1)
    return bst
    
def minHeightBstHelperNethodOne(array, root, start, end):
    if start > end:
        return
    mid = (start+end)//2
    if root == None:
        root = BST(array[mid])
    else:
        root.insert(array[mid])
    minHeightBstHelperNethodOne(array, root, mid+1, end)
    minHeightBstHelperNethodOne(array, root,  start, mid-1)
    return root


def minHeightBstHelperMethodTwo(array, root, start, end):
    if start > end:
        return
    else:
        mid = (start+end)//2
        bst = BST(array[mid])
        if root == None:
            root = bst
        else:
            if bst.value<root.value:
                root.left = bst
                root = root.left
            else:
                root.right = bst
                root = root.right
        minHeightBstHelperMethodTwo(array, root,  start, mid-1)
        minHeightBstHelperMethodTwo(array, root, mid+1, end)
        return root
# [1, 2, 5, 7, 10, 13, 14, 15, 22]


def findKthLargestValueInBstOrderN(tree, k):
    sortedValues = []
    inorderTraversal(tree, sortedValues)
    return sortedValues[len(sortedValues)-k]

def inorderTraversal(tree, array):
    if tree is None:
        return
    inorderTraversal(tree.left, array)
    array.append(tree.value)
    inorderTraversal(tree.right, array)

class TreeInfo:
    def __init__(self, noOfNodesVisited, lastVisitedNode) -> None:
        self.noOfNodesVisited = noOfNodesVisited
        self.lastVisitedNode = lastVisitedNode
    
def findKthLargestValueInBstOrderHplusK(tree, k):
    treeInfo = TreeInfo(0,-1)
    reverseInorderTraversal(tree, k, treeInfo)
    return treeInfo.lastVisitedNode

def findKthLargestValueInBst_(tree, k):
    info = Info(k)
    value = -1
    reverseInorderTraversal_(tree, info, value)
    return value

def reverseInorderTraversal(tree, k, treeInfo):
    if tree is None or treeInfo.noOfNodesVisited>k:
        return
    reverseInorderTraversal(tree.right, k, treeInfo)
    if treeInfo.noOfNodesVisited < k:
        treeInfo.noOfNodesVisited += 1
        treeInfo.lastVisitedNode = tree.value
        reverseInorderTraversal(tree.left, k, treeInfo)

class Info:
    def __init__(self,value) -> None:
        self.value = value

def reverseInorderTraversal_(tree, info, value):
    if tree is None or info.value < 0:
        return
    reverseInorderTraversal_(tree.right, info, value)
    if info.value>0:
        info.value -= 1
        value = tree.value
        reverseInorderTraversal_(tree.left, info, value)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)



def reconstructBst(preOrderTraversalValues):
    return reconstructBSTHelper(preOrderTraversalValues, None, 0)

def reconstructBSTHelper(preOrderTraversalArray, root, start):
    if start == len(preOrderTraversalArray):
        return
    else:
        if root is None:
            root = BST(preOrderTraversalArray[start])
        else:
            root.insert(preOrderTraversalArray[start])
        reconstructBSTHelper(preOrderTraversalArray, root, start+1)
        return root



root = minHeightBst([1, 2, 5, 7, 10, 13, 14, 15, 22])
tree = reconstructBst([10, 4, 2, 1, 5, 17, 19, 18])
print(tree)