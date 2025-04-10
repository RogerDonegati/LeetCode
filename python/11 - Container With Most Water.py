def maxArea(height: int) -> int:
    result = 0
    left = 0
    right = len(height) -1

    while left < right:
        currentWater = min(height[left], height[right]) * (right - left)
        result = max(result, currentWater)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return result

