def numberOfWaysToTraverseGraphOne(width, height):
    if width == 1 or height == 1:
        return 1
    return numberOfWaysToTraverseGraphOne(width-1, height) + numberOfWaysToTraverseGraphOne(width, height-1)
    


# n = numberOfWaysToTraverseGraphOne(4,3)
# print(n)


def numberOfWaysToTraverseGraphDP(width, height):
    grid = [[0 for x in range(width)] for y in range(height)]
    # for column in range(width):
    #     grid[0][column] = 1
    # for row in range(height):
    #     grid[row][0] = 1
    for i in range(0, height):
        for j in range(0, width):
            if i == 0 or j ==0:
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i-1][j]+grid[i][j-1]
    return grid



def numberOfWaysToTraverseGraph(width, height):
    xDistanceToCorner = width - 1
    yDistanceToCorner = height - 1
    numerator = factorial(xDistanceToCorner + yDistanceToCorner)
    denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner)
    return numerator//denominator

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number*factorial(number-1)

n = numberOfWaysToTraverseGraph(4,3)
print(n)