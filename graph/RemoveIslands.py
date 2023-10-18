def removeIslands(matrix):
    onesConnected = [[False for row in matrix[0]] for row in matrix]
    visited = [[False for value in row] for row in matrix]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            columnIsBorder = column == 0 or column == len(matrix[row]) - 1
            isBorder = rowIsBorder or columnIsBorder
            if not isBorder:
                continue
            if matrix[row][column] == 0:
                continue
            findOnesConnectedToBorder(matrix, row, column, onesConnected)
    for row in range(1, len(matrix) - 1):
        for column in range(1, len(matrix[row]) - 1):
            if matrix[row][column] == 0:
                continue
            if onesConnected[row][column] == True:
                continue
            else:
                matrix[row][column] = 0
    return matrix


def findOnesConnectedToBorder(matrix, row, column, onesConnected):
    stack = [(row, column)]
    while len(stack):
        current = stack.pop()
        currentRow, currentColumnn = current
        alreadyVisited = onesConnected[currentRow][currentColumnn]
        if alreadyVisited:
            continue
        onesConnected[currentRow][currentColumnn] = True
        neighbours = getNeighboursForCurrent(currentRow, currentColumnn, matrix)
        for neighbour in neighbours:
            row, column = neighbour
            if matrix[row][column] == 0:
                continue
            stack.append(neighbour)


def getNeighboursForCurrent(row, column, matrix):
    neighbours = []
    numRows = len(matrix)
    numCols = len(matrix[row])

    if row - 1 >= 0:
        neighbours.append((row - 1, column))
    if row + 1 < numRows:
        neighbours.append((row + 1, column))
    if column - 1 >= 0:
        neighbours.append((row, column - 1))
    if column + 1 < numCols:
        neighbours.append((row, column + 1))
    return neighbours


riverAndLand = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]


sizes = removeIslands(riverAndLand)
print(sizes)
