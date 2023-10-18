def removeIslands(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            columnIsBorder = column == 0 or column == len(matrix[row]) - 1
            isBorder = rowIsBorder or columnIsBorder
            if not isBorder:
                continue
            if matrix[row][column] != 1:
                continue
            changeOnesConnectedToBorderTwo(matrix, row, column)
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 0:
                continue
            if matrix[row][column] == 2:
                matrix[row][column] = 1
            else:
                matrix[row][column] = 0
    return matrix


def changeOnesConnectedToBorderTwo(matrix, row, column):
    stack = [(row, column)]
    while len(stack):
        current = stack.pop()
        currentRow, currentColumnn = current
        alreadyVisited = matrix[currentRow][currentColumnn] == 2
        if alreadyVisited:
            continue
        matrix[currentRow][currentColumnn] = 2
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
