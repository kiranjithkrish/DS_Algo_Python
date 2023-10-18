def printSubArrays(arr, start, end):
    if end == len(arr):
        return
    elif start>end:
        printSubArrays(arr, 0 , end+1)    
    else:
        print(arr[start:end+1])
        print("start is", start)
        print("end is", end)
        printSubArrays(arr, start+1, end)


printSubArrays([1,2,3], 0 ,0)