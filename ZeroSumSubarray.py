def zeroSumSubarray(nums):
        allSubarrays(nums, 0, 0)
        return 

def allSubarrays(nums, start, end):
    if start<=end:
        if end > len(nums)-1 :
            return 
        else:
            print(nums[end])
            allSubarrays(nums, start, end+1)
        end = start
        print("\n")
        allSubarrays(nums, start+1, end+1)
    else:
        return
nums = [1,2,3]
zeroSumSubarray(nums)
