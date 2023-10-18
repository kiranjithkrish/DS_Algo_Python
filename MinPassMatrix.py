def minimumPassesOfMatrix(matrix):
    passes = getNegetives(matrix)
    return passes-1 if not containNegetive(matrix) else -1

def getNegetives(matrix):
    queue = getAllPositiveIndices(matrix)
    passes = 0

    while len(queue)>0:
        passBy = len(queue)
        while passBy>0:
            row,column  = queue.pop(0)
            neighbours = getAllNeighbours(row, column, matrix)
            for neighbour in neighbours:
                row, column = neighbour
                if matrix[row][column]<0:
                    matrix[row][column] = matrix[row][column]*-1
                    queue.append(neighbour)
            passBy -= 1
        passes += 1
    return passes

def getAllPositiveIndices(matrix):
    positiveIndices = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column]>0:
                positiveIndices.append([row,column])
    return positiveIndices

def containNegetive(matrix):
    for row in matrix:
        for value in row:
            if value<0:
                return True
    return False

def getAllNeighbours(row, column, matrix):
    neighbours = []
    if row>0:
        neighbours.append([row-1, column])
    if row<len(matrix)-1:
        neighbours.append([row+1, column])
    if column>0:
        neighbours.append([row, column-1])
    if column<len(matrix[0])-1:
        neighbours.append([row, column+1])
    return neighbours


matrix = [
  [0, -1, -3, 2, 0],
  [1, -2, -5, -1, -3],
  [3, 0, 0, -4, -1]
]

passes = minimumPassesOfMatrix(matrix)
print(passes)