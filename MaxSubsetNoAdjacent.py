def maxSubsetSumNoAdjacentNotWorking(array):
    for i in range(1, len(array)):
        if i == 1:
            array[i] = max(array[i], array[i-1])
        else:
            array[i] = max(array[i-1], array[i]+array[i-2])
    return array[len(array)-1]

        
    return max + leftSum + rightSum
def maxSubsetSumNoAdjacent(array):
    return maxSubsetSumNoAdjacentHelper(array, 0, len(array)-1)

def maxSubsetSumNoAdjacentHelper(array, start, end):
    if start>end:
        return 0
    if start == end:
        return array[start] 
    maxIndex = findMaxIndex(array, start, end)
    if maxIndex < end and maxIndex > start and array[maxIndex] < (array[maxIndex-1] + array[maxIndex+1]):
        maxLeft = maxSubsetSumNoAdjacentHelper(array, start, maxIndex-1)
        maxRight = maxSubsetSumNoAdjacentHelper(array, maxIndex+1, end)
        return maxLeft + maxRight
    else:
        maxLeft = maxSubsetSumNoAdjacentHelper(array, start, maxIndex-2)
        maxRight = maxSubsetSumNoAdjacentHelper(array, maxIndex+2, end)
        return array[maxIndex] + maxLeft + maxRight

    
def findMaxIndex(array, start, end):
    maxIndex = 0
    for i in range(start, end+1):
        if array[i]>array[maxIndex]:
            maxIndex = i
    return maxIndex

sum = maxSubsetSumNoAdjacentNotWorking([75, 105, 120, 75, 90, 135])
print(sum)