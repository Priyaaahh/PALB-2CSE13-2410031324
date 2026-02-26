def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2


        row = mid // n
        col = mid % n

        mid_value = matrix[row][col]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


#Example

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target1 = 3
target2 = 13

print("Searching for", target1, ":", searchMatrix(matrix, target1))
print("Searching for", target2, ":", searchMatrix(matrix, target2))