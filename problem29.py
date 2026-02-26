def matrix_median(mat):
    elements = []


    for row in mat:
        elements.extend(row)

    elements.sort()

    mid = len(elements) // 2
    return elements[mid]


#Example1
mat1 = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print("Output:", matrix_median(mat1))  


# Example2
mat2 = [
    [2, 4, 9],
    [3, 6, 7],
    [4, 7, 10]
]
print("Output:", matrix_median(mat2))  


#Example3
mat3 = [
    [3],
    [4],
    [8]
]
print("Output:", matrix_median(mat3))  