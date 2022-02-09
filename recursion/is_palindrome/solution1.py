def isPalindrome(strng):

    if len(strng) < 2:
        return True

    if strng[0] != strng[-1]:
        return False

    return True and isPalindrome(strng[1:-1])


assert isPalindrome("awesome") == False
assert isPalindrome("holaaa") == False
assert isPalindrome("me la suda") == False
assert isPalindrome("D-E-I-F-I-E-D") == True
assert isPalindrome("radar") == True
assert isPalindrome("rotator") == True
assert isPalindrome("radarrotatorradar") == True
assert isPalindrome("pip") == True
