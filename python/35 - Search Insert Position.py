
def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) -1

    while left < right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return left



            
print(searchInsert([1,3,5,6], 7)) # 2