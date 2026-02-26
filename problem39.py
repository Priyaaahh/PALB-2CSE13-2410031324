def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Example1
nums1 = [4,5,6,7,0,1,2]
target1 = 0
print("Example 1:", search(nums1, target1))  

# Example2
nums2 = [4,5,6,7,0,1,2]
target2 = 3
print("Example 2:", search(nums2, target2))  

#Example3
nums3 = [1]
target3 = 0
print("Example 3:", search(nums3, target3))  