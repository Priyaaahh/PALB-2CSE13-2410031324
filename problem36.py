def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])
            
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


# Example1
nums1 = [1, 2, 3]
print("Subsets of", nums1, ":")
print(subsets(nums1))

# Example2
nums2 = [0]
print("\nSubsets of", nums2, ":")
print(subsets(nums2))
