def plus_one(digits):
    n = len(digits)


    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0


    return [1] + digits


# Example 1
digits1 = [1, 2, 3]
print(plus_one(digits1))


# Example 2
digits2 = [4, 3, 2, 1]
print(plus_one(digits2))

#Example 3
digits3 = [9]
print(plus_one(digits3))

# Example 4
digits4 = [9, 9, 9]
print(plus_one(digits4))