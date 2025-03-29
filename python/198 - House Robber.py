def rob(nums: list[int]) -> int:
    x, y = 0, 0
    for num in nums:
        if num + y > x:
            x, y = num + y, x
        else:
            x, y = x, x
    
    return x


print(rob([1,2,3,1]))   # 4
print(rob([2,7,9,3,1])) # 12