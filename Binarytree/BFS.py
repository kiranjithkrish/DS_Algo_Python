class Node:
    def __init__(self, name) -> None:
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue)>0:
            current = queue.pop(0)
            array.append(current.name)
            for edge in current.children:
                queue.append(edge)
        return array
root = Node("A")
nodeB = root.addChild("B")
nodeB.addChild("E")
nodeF = nodeB.addChild("F")
nodeF.addChild("I")
nodeF.addChild("J")
root.addChild("C")
nodeD = root.addChild("D")
nodeG = nodeD.addChild("G")
nodeG.addChild("K")
nodeD.addChild("H")
