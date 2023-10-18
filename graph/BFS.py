class Node:
    def __init__(self, name) -> None:
        self.children = []
        self.name = name

    def addChild(self, name):
        newNodee = Node(name)
        self.children.append(Node(name))
        return newNodee

    def breadthFirstSearch(self, array):
        pass


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
