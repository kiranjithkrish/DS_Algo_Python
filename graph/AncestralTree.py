# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = depthOfNode(descendantOne)
    depthTwo = depthOfNode(descendantTwo)
    # top = descendantOne if depthOne < depthTwo else descendantTwo
    # bottom = descendantOne if depthOne > depthTwo else descendantTwo
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne-depthTwo)
    else:
        return backtrackAncestralTree(descendantOne, descendantOne, depthTwo-depthOne)


def backtrackAncestralTree(bottom, top, diff):
    while diff > 0:
        diff -= 1
        bottom = bottom.ancestor
    while bottom != top:
        bottom = bottom.ancestor
        top = top.ancestor
    return bottom


def depthOfNode(descendant):
    height = 0
    while descendant.ancestor is not None:
        height += 1
        descendant = descendant.ancestor
    return height


root = AncestralTree("A")
b = AncestralTree("B")
b.ancestor = root
c = AncestralTree("C")
c.ancestor = root
d = AncestralTree("D")
e = AncestralTree("E")
d.ancestor = b
e.ancestor = b
f = AncestralTree("F")
g = AncestralTree("G")
f.ancestor = c
g.ancestor = c
h = AncestralTree("H")
i = AncestralTree("I")
h.ancestor = d
i.ancestor = d

result = getYoungestCommonAncestor(root, b, f)
print(result.name)
