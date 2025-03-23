def threeSum(nums: list[int], searched: int) -> list[list[int]]:
    results = []
    nums = sorted(nums)
    i=0
    for i in range(len(nums)):
        if i >= 1 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = len(nums) -1
        while  j < k:
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                results.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1
    return sorted(results)


# HashMapSolution
# def threeSum(nums: list[int], searched: int) -> list[list[int]]:
#     nums = sorted(nums)
#     results = []
#     cache = []

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             missingValue = searched - (nums[i] + nums[j])
#             if missingValue in cache and sorted([nums[i], nums[j], missingValue]) not in results:
#                 results.append(sorted([nums[i], nums[j], missingValue]))
#         cache.append(nums[i])
            
#     return sorted(results)
    

print(threeSum([-1,0,1,2,-1,-4], 0))
print(threeSum([0,1,1], 0))
print(threeSum([0,0,0,0], 0))
print(threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10],0))