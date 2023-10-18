# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def reconstructBst(preOrderTraversalValues):
#     if len(preOrderTraversalValues) == 0:
#         return None
#     currentValue = preOrderTraversalValues[0]
#     rightSubtreeRootIdx = len(preOrderTraversalValues)

#     for idx, value in enumerate(preOrderTraversalValues):
#         if value>currentValue:
#             rightSubtreeRootIdx = idx
#             break
    
#     leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
#     rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])
#     return BST(currentValue, leftSubtree, rightSubtree)

class TreeNodeInfo:
    def __init__(self,rootIdx) -> None:
        self.rootIdx = rootIdx


def reconstructBst(preOrderTraversalValues):
     treeInfo = TreeNodeInfo(0)
     return reconstructBstFromRange(float('-inf'), float('inf'), treeInfo, preOrderTraversalValues)
     

def reconstructBstFromRange(lowerBound, upperBound, treeInfo, preOrderTraversalValues):
    if treeInfo.rootIdx == len(preOrderTraversalValues):
        return None
    rootValue = preOrderTraversalValues[treeInfo.rootIdx]
    if rootValue<lowerBound or rootValue>upperBound:
        return None
    treeInfo.rootIdx += 1
    letSubree = reconstructBstFromRange(lowerBound, rootValue, treeInfo, preOrderTraversalValues)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, treeInfo, preOrderTraversalValues)
    return BST(rootValue, letSubree, rightSubtree)

root = reconstructBst([2, 0, 1, 4, 3, 3])