def cycleInGraph(edges):
    noOfNodes = len(edges)
    visited = [False for value in range(noOfNodes)]
    nodesInStack = [False for value in range(noOfNodes)]
    for node in range(noOfNodes):
        if visited[node]:
            continue
        containsCycle = isNodeInCycle(node, visited, nodesInStack, edges)
        if containsCycle:
            return True
    return False


def isNodeInCycle(node, visited, verticesInStack, edges):
    visited[node] = True
    verticesInStack[node] = True

    for neighbour in edges[node]:
        if not visited[neighbour]:
            containsCycle = isNodeInCycle(neighbour, visited, verticesInStack, edges)
            if containsCycle:
                return True
        elif verticesInStack[neighbour]:
            return True
    verticesInStack[node] = False
    return False


edges = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]

cycle = cycleInGraph(edges)
print(cycle)
