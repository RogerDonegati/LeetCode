def longestConsecutive(nums: list[int]) -> int:
    nums = set(nums)
    result = 0

    for num in nums:
        if num - 1 not in nums:
            currentMax = 1
            while num + currentMax in nums:
                currentMax += 1
            result = max(result, currentMax)

    return result
    

print(longestConsecutive([100,4,200,1,3,2])) # 4
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(longestConsecutive([0,-1])) # 2