def factorial_digits(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return [int(d) for d in str(fact)]


# Example
print(factorial_digits(5))    # [1, 2, 0]
print(factorial_digits(10))   # [3, 6, 2, 8, 8, 0, 0]
print(factorial_digits(1))    # [1]