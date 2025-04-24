def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    hash_map = {}
    for i, num in enumerate(nums):
        if num in hash_map and abs(i - hash_map[num]) <= k:
            return True
        hash_map[num] = i
    return False

# classical slide window (expanding and collapsing)
def containsNearbyDuplicate2(nums: list[int], k: int) -> bool:
    slow = 0
    fast = 1
    hash_map = {nums[0]: 0}
    while fast < len(nums):
        while abs(slow - fast) > k:
            del(hash_map[nums[slow]])
            slow += 1

        if nums[fast] not in hash_map:
            hash_map[nums[fast]] = fast
        elif abs(hash_map[nums[fast]] - fast) <= k:
            return True

        fast +=1
    return False

containsNearbyDuplicate([1,0,1,1], 1)