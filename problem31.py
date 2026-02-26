def combination_sum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
        
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            if candidates[i] > remaining:
                break
            
            backtrack(i + 1, remaining - candidates[i], path + [candidates[i]])

    backtrack(0, target, [])
    return result


# Example 1
candidates1 = [10, 1, 2, 7, 6, 1, 5]
target1 = 8
print("Output:", combination_sum2(candidates1, target1))


# Example 2 
candidates2 = [2, 5, 2, 1, 2]
target2 = 5
print("Output:", combination_sum2(candidates2, target2))