def get_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]

    return [min_val, max_val]

# Example usage
arr = [1, 4, 3, 5, 8, 6]
print(get_min_max(arr))