def removeDuplicates( nums: list[int]) -> int:
    result = 1
    previous_val = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != previous_val:
            nums[result] = nums[i]
            result += 1
        previous_val = nums[i]

    return result

