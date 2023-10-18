
def misssingNumbersXorSolution(nums):
    solutionXor = 0
    for i in range(0,len(nums)+3):
        solutionXor = solutionXor ^ i
        if i<len(nums):
            solutionXor ^= nums[i]
    setBit = solutionXor & - solutionXor    
    print("set bit is", setBit)
    solution = [0,0]
    for i in range(0,len(nums)+3):
        if i & setBit == 0:
            solution[0] ^= i
        else:
            solution[1] ^= i 
        if i<len(nums):
            if nums[i] & setBit == 0:
                 solution[0] ^= nums[i]
            else:
                solution[1] ^= nums[i]
            
    return sorted(solution)










def missingNumbersSumSolution(nums):
    total = sum(range(1,len(nums)+3))
    for num in nums:
        total -= num
    avg = total//2
    sumLess = 0
    sumMore = 0
    for i in nums:
        if i<=avg:
            sumLess += i
        else:
            sumMore += i
    numberOne = sum(range(1,avg+1)) - sumLess
    numberTwo = sum(range(avg+1,len(nums)+3))
    return [numberOne,numberTwo]

nums = misssingNumbersXorSolution([])
print(nums)