def largest_element(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


# Example usage
arr = [1, 8, 7, 56, 90]
print(largest_element(arr))
