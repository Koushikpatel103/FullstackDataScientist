def is_palindrome(str):
    if str[::-1]==str[::1]:
        return True
    else:
        return False
str=input("enter a string")
if is_palindrome(str):
    print("True")
else:
    print("False")