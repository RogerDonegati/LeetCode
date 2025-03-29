
def trap(height: list[int]) -> int:
    result = 0
    left = {
        "value": height[0],
        "index": 0,
        "heightArea": 0,
    }
    right = {
        "value": height[len(height)-1],
        "index": 0,
        "heightArea": 0,
    }

    for i in range(1,len(height)):
        if left['value'] <= height[i]:
            result += (i - left['index'] - 1) * left['value'] - left['heightArea']
            left['value'] = height[i]
            left['heightArea'] = 0
            left['index'] = i
        else:
            left['heightArea'] += height[i]

    newHeight = height[left['index']-len(height):][::-1]
    for i in range(1, len(newHeight)):
        if right['value'] <= newHeight[i]:
            result += (i - right['index'] - 1) * right['value'] - right['heightArea']
            right['value'] = newHeight[i]
            right['heightArea'] = 0
            right['index'] = i
        else:
            right['heightArea'] += newHeight[i]
        if (newHeight[i] == left['value'] or right['value'] == left['value'] ) and result >0:
            break
    return result

def optimzedTrap(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            # this means that there is a wall in right higher than any wall in the left
            # so we just need to calcula max left - current height
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            # this means that there is a wall in left higher than any wall in the right
            # so we just need to calcula max right - current height
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    return water



print(optimzedTrap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])) # 83
print(optimzedTrap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(optimzedTrap([4,2,0,3,2,4,3,4])) # 10
print(optimzedTrap([4,2,0,3,2,5])) # 9
print(optimzedTrap([4,2,3])) # 1
print(optimzedTrap([2,0,2])) # 2