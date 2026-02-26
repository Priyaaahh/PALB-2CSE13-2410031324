def is_palindrome_array(arr):
    for num in arr:
        s = str(num)
        if s != s[::-1]:
            return False
    return True


# Example
print(is_palindrome_array([111, 222, 333, 444, 555]))  
print(is_palindrome_array([121, 131, 20]))            