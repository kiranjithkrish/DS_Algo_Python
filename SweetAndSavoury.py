def sweetAndSavory(dishes, target):
    sweet = sorted([dish for dish in dishes if dish<0], key=abs)
    savoury = sorted([dish for dish in dishes if dish>0])
    bestIndex = [0,0]
    bestDiff = float('inf')
    sweetIndex, savIndex = 0, 0
    while sweetIndex<len(sweet) and savIndex<len(savoury):
        sum = sweet[sweetIndex] + savoury[savIndex]
        if sum<=target:
            currentDiff = target - sum  
            if currentDiff<bestDiff:
                bestDiff = currentDiff
                bestIndex = [sweet[sweetIndex], savoury[savIndex]]
            savIndex += 1
        else:
            sweetIndex += 1
    return bestIndex

print(sweetAndSavory([-5,10], 5))