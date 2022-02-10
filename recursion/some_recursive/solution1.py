def isOdd(num):
    if num%2==0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    
    if len(arr) == 1:
        return cb(arr.pop())
    
    if not(cb(arr.pop())):
        return someRecursive(arr, cb)

    return True

assert someRecursive([1, 2, 3, 4], isOdd) == True
assert someRecursive([4, 6, 8, 9], isOdd) == True
assert someRecursive([4, 6, 8], isOdd) == False
