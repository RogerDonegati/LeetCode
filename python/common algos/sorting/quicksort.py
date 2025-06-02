# time complexity
# (n log n)
# worst: n^2

def quicksort(my_array):
    def partition(left, right):
        pivot = my_array[right]
        i = left - 1 # aux minimal index to move smaller values from left to right

        for j in range(left, right):
            if my_array[j] <= pivot:
                i += 1
                my_array[i], my_array[j] = my_array[j], my_array[i]
        my_array[i + 1], my_array[right] = my_array[right], my_array[i + 1]
        return i + 1

    def recursive_handler(left, right):
        if left < right:
            aux = partition(left, right)
            recursive_handler(left, aux - 1)
            recursive_handler(aux + 1, right)

    recursive_handler(0, len(my_array) - 1)
    return my_array

print(quicksort([1,2,4,5,6,7,3,4,2,64,3]))
print(quicksort([1,9,2,8,3,7,4,6,5]))
print(quicksort([0,1,2,3,9,8,7,6,12,98,15,76,42]))
