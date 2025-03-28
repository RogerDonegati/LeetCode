# TODO there is clearly room for improvement here....

def trap(height: list[int]) -> int:
    result = 0
    left = {
        "value": height[0],
        "index": 0,
        "sum": 0,
    }

    for i in range(1,len(height)):
        if left['value'] <= height[i]:
            result += (i - left['index'] - 1) * left['value'] - left['sum']
            left['value'] = height[i]
            left['sum'] = 0
            left['index'] = i
        else:
            left['sum'] += height[i]

    right = {
        "value": height[len(height)-1],
        "index": len(height)-1,
        "sum": 0,
    }
    for i in range(len(height) -2, -1, -1):
        if right['value'] <= height[i]:
            result += (right['index'] - i -1) * right['value'] - right['sum']
            right['value'] = height[i]
            right['sum'] = 0
            right['index'] = i
        else:
            right['sum'] += height[i]
        if (height[i] == left['value'] or right['value'] == left['value'] ) and result >0:
            break
    return result

print(trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])) # 81
print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,4,3,4])) # 10
print(trap([4,2,0,3,2,5])) # 9
print(trap([4,2,3])) # 1
print(trap([2,0,2])) # 2