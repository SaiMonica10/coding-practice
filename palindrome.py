######## check if a string is palindrome or not #########

# def is_palindrome(s):
#     return s == s[::-1]

s = input()
# if is_palindrome(s):
#     print(s, "is a palindrome")
# else:
#     print(s, "is not a palindrome")

def is_palindrome(s):
    left = 0
    right = len(s) - 1 
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

if is_palindrome(s):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
    