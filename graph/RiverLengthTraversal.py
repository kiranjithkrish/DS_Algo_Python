def riverSizes(matrix):
    riverSizes = []
    visited = [[False for value in row] for row in matrix]
    print(range(len(matrix)))
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if visited[row][column] == True:
                continue
            traverseNode(row, column, matrix, visited, riverSizes)
    return riverSizes


def traverseNode(row, column, matrix, visited, riverSizes):
    currentRiverSize = 0
    nodesToExplore = [[row, column]]
    while (len(nodesToExplore)):
        currentNode = nodesToExplore.pop()
        row = currentNode[0]
        column = currentNode[1]
        if visited[row][column]:
            continue
        visited[row][column] = True
        if matrix[row][column] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbours = getUnvisitedNeighbours(
            row, column, matrix, visited)
        for neighbour in unvisitedNeighbours:
            nodesToExplore.append(neighbour)
    if currentRiverSize > 0:
        riverSizes.append(currentRiverSize)


def getUnvisitedNeighbours(row, column, matrix, visited):
    unvisitedNeighbours = []
    if row > 0 and not visited[row-1][column]:
        unvisitedNeighbours.append([row-1, column])
    if row < len(matrix)-1 and not visited[row+1][column]:
        unvisitedNeighbours.append([row+1, column])
    if column > 0 and not visited[row][column-1]:
        unvisitedNeighbours.append([row, column-1])
    print(column < len(matrix)-1 and not visited[row][column+1])
    if column < len(matrix[0])-1 and not visited[row][column+1]:
        unvisitedNeighbours.append([row, column+1])
    return unvisitedNeighbours


riverAndLand = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]


sizes = riverSizes(riverAndLand)
print(sizes)
