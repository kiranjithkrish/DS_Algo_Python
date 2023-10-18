def majorityElement(array):
    answer = None
    count = 0
    for value in array:
        if count == 0:
            answer = value
        if answer == value:
            count += 1
        else:
            count -= 1
    return answer


def majorityElementBitwise(array):
    answer = 0
    for currentBit in range(32):
        currentBitValue = 1 << currentBit
        onesCount = 0
        for num in array:
            if (num & currentBitValue) != 0:
                onesCount += 1
        if onesCount > len(array)/2:
            answer += currentBitValue
    return answer


majority = majorityElementBitwise([1, 22, 3, 22, 22, 1, 22])
print(majority)
