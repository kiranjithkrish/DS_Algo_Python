class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None    

def InOrderTraversal(tree):
    stack = []
    current = tree
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.value)
            current = current.right
        else:
            break







root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
out = InOrderTraversal(root)
print(out)