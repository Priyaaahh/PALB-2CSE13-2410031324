def row_with_max_ones(arr):
    max_ones = 0
    row_index = -1

    for i in range(len(arr)):
        count_ones = arr[i].count(1)
        if count_ones > max_ones:
            max_ones = count_ones
            row_index = i

    return row_index


#  Example 1
arr1 = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]
print("Output:", row_with_max_ones(arr1)) 


# Example 2
arr2 = [
    [0, 0],
    [1, 1]
]
print("Output:", row_with_max_ones(arr2))  


# Example 3
arr3 = [
    [0, 0],
    [0, 0]
]
print("Output:", row_with_max_ones(arr3)) 