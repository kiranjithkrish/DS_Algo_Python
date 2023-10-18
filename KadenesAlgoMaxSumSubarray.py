def kadanesAlgorithm(array):
    maxSumHere = array[0]
    maxSumSoFar = maxSumHere
    for i in range(1, len(array)):
        maxSumHere = max(array[i], (maxSumHere+array[i]))
        maxSumSoFar = max(maxSumSoFar, maxSumHere)
    return maxSumSoFar


kadanesAlgorithm( [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])