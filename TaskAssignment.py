def taskAssignment(k, tasks):
    sortedDuration = sorted(tasks)
    indicesOfTasks = []
    indicesForDuration = saveIndicesOfDuration(tasks)
    start = 0
    end = len(tasks)-1
    while start<end:
        indexOfTaskOne = indicesForDuration[sortedDuration[start]].pop()
        IndexOfTaskTwo = indicesForDuration[sortedDuration[end]].pop()
        result = [indexOfTaskOne, IndexOfTaskTwo]
        indicesOfTasks.append(result)
        start += 1
        end -= 1

    # for leftIdx in range(k):
    #     indexOfTaskOne = indicesForDuration[sortedDuration[leftIdx]].pop()
    #     rightIdx = len(sortedDuration)-1-leftIdx
    #     IndexOfTaskTwo = indicesForDuration[sortedDuration[rightIdx]].pop()
    #     result = [indexOfTaskOne, IndexOfTaskTwo]
    #     indicesOfTasks.append(result)
    return indicesOfTasks

def saveIndicesOfDuration(tasks):
    indicesForDuration = {}
    for idx,duration in enumerate(tasks):
        if duration in indicesForDuration:
            indicesForDuration[duration].append(idx)
        else:
            indicesForDuration[duration] = [idx]
    return indicesForDuration

pair = taskAssignment(3, [1, 3, 5, 3, 1, 4])
print(pair)
