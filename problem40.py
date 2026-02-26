def searchRange(nums, target):
    
    def findFirst():
        left, right = 0, len(nums) - 1
        first = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                first = mid
                right = mid - 1 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return first

    def findLast():
        left, right = 0, len(nums) - 1
        last = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                last = mid
                left = mid + 1   
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return last

    return [findFirst(), findLast()]


# Example1
nums1 = [5,7,7,8,8,10]
target1 = 8
print("Example 1:", searchRange(nums1, target1)) 

#Example2
nums2 = [5,7,7,8,8,10]
target2 = 6
print("Example 2:", searchRange(nums2, target2))  

#Example3
nums3 = []
target3 = 0
print("Example 3:", searchRange(nums3, target3))  