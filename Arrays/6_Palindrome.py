''' 
Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

Input:
5
111 222 333 444 555

Output:
1'''

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def PalinArray(arr, n):
    for num in arr:
        if not is_palindrome(num):
            return 0
    return 1

# Example usage
print(PalinArray([111, 222, 333, 444, 555], 5))  # Output: 1
print(PalinArray([121, 131, 20], 3))            # Output: 0
