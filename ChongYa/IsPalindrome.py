def isPalindrome(x):
    string = str(x)
    reverse = string[::-1]
    if reverse == string:  # 直接简化为 return string == reverse
        print(True)
    else:
        print(False)


isPalindrome(123821)