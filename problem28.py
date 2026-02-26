def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        r = mid // cols
        c = mid % cols

        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Example1
matrix1 = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target1 = 3
print("Output:", search_matrix(matrix1, target1))  


# Example2
matrix2 = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target2 = 13
print("Output:", search_matrix(matrix2, target2)) 