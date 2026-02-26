def min_swaps(arr, k):
    n = len(arr)

    # Count elements <= k
    count = 0
    for x in arr:
        if x <= k:
            count += 1

    # Count bad elements in first window
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1

    ans = bad

    # Sliding window
    for i in range(0, n - count):
        if arr[i] > k:
            bad -= 1
        if arr[i + count] > k:
            bad += 1
        ans = min(ans, bad)

    return ans


# Example 
print(min_swaps([2, 1, 5, 6, 3], 3))        
print(min_swaps([2, 7, 9, 5, 8, 7, 4], 6))  
print(min_swaps([2, 4, 5, 3, 6, 1, 8], 6)) 