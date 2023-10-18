# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def mergeBinaryTreeIterative(tree1, tree2):
    if tree1 is None:
        return tree2
    stack1 = [tree1]
    stack2 = [tree2]
    while  stack1:
        current1 = stack1.pop()
        current2 = stack2.pop()

        if current2 is None:
            continue
        current1.value += current2.value
        if current1.left is None:
            current1.left = current2.left
        else:
            stack1.append(current1.left)
            stack2.append(current2.left)

        if current1.right is None:
            current1.right = current2.right
        else:
            stack1.append(current1.right)
            stack2.append(current2.right)
    return tree1
        
            



def mergeBinaryTrees(tree1, tree2):
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1
    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree1

def mergeBinaryTreesSolutionOne(tree1, tree2):
    if tree1 is None and tree2 is None:
        return None
    if tree1 is None:
        tree3 = BinaryTree(tree2.value)
        tree3.left = mergeBinaryTrees(None, tree2.left)
        tree3.right = mergeBinaryTrees(None, tree2.right)
        return tree3
    if tree2 is None:
        tree3 = BinaryTree(tree1.value)
        tree3.left = mergeBinaryTrees(tree1.left, None)
        tree3.right = mergeBinaryTrees(tree1.right, None)
        return tree3
    else:
        tree3 = BinaryTree(tree2.value + tree1.value)
        tree3.left = mergeBinaryTrees(tree1.left, tree2.left)
        tree3.right = mergeBinaryTrees(tree1.right, tree2.right)
        return tree3


tree1 = BinaryTree(1)
tree1.left = BinaryTree(3)
tree1.right = BinaryTree(2)
tree1.left.left = BinaryTree(7)
tree1.left.right = BinaryTree(4)

tree2 = BinaryTree(1)
tree2.left = BinaryTree(5)
tree2.right = BinaryTree(9)
tree2.left.left = BinaryTree(2)
tree2.right.left = BinaryTree(7)
tree2.right.right = BinaryTree(6)

mergeBinaryTreeIterative(tree1, tree2)