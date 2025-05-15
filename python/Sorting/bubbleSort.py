def bubbleSort(my_array):
    n = len(my_array)
    interactions = 0
    for i in range(n):
        interactions +=  1
        is_sorted = True # handle early return in case the array is already sorted
        for j in range(0, n - i - 1):
            if my_array[j] > my_array[j + 1]:
                my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
                is_sorted = False
        if is_sorted:
            print(f'array sorted after {interactions} interactions')
            return my_array
        
    print(f'array sorted after {interactions} interactions')
    return my_array

print(bubbleSort([1,2,3,4,5]))
print(bubbleSort([5,4,3,2,1]))
print(bubbleSort([5,2,1,4,3,7]))