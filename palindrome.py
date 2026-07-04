######## check if a string is palindrome or not #########

def is_palindrome(s):
    return s == s[::-1]

s = input()
if is_palindrome(s):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")