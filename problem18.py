from collections import Counter

def is_subset(a, b):
    count_a = Counter(a)
    count_b = Counter(b)

    for key in count_b:
        if count_b[key] > count_a.get(key, 0):
            return False
    return True


# Example 
print(is_subset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))  
print(is_subset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))           
print(is_subset([10, 5, 2, 23, 19], [19, 5, 3]))           