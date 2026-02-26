def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else: 
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


#Example1
nums1 = [2,0,2,1,1,0]
sortColors(nums1)
print("Sorted array 1:", nums1)

#Example2
nums2 = [2,0,1]
sortColors(nums2)
print("Sorted array 2:", nums2)