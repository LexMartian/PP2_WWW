def is_palindrome(s):
    if s == s[::-1]:
        print("Yes")
    else:
        print("Not palindrome")

s = str(input())
is_palindrome(s)