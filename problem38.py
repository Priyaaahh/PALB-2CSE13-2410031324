def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        for j in range(i + 1, n):

            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    quad = [nums[i], nums[j], nums[left], nums[right]]
                    
                    if quad not in result:  
                        result.append(quad)

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


# Example 1
nums1 = [1,0,-1,0,-2,2]
target1 = 0
print(fourSum(nums1, target1))

# Example 2
nums2 = [2,2,2,2,2]
target2 = 8
print(fourSum(nums2, target2))