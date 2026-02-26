def min_jumps(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps


# Example 1
nums1 = [2, 3, 1, 1, 4]
print("Minimum jumps:", min_jumps(nums1)) 


# Example2
nums2 = [2, 3, 0, 1, 4]
print("Minimum jumps:", min_jumps(nums2))  