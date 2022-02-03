
def gcd(x, y):

    assert int(x) == x and int(y) == y, "bad input"

    x, y = abs(x), abs(y)

    if x > y:
        sub = y
        reminder = x % sub
    else:
        sub = x
        reminder = y % sub

    if reminder:
        return gcd(sub, reminder)
    else:
        return sub


assert gcd(8, -12) == 4
assert gcd(48, 18) == 6
assert gcd(16, 12) == 4
assert gcd(225, 300) == 75
assert gcd(380, 420) == 20
assert gcd(10, 10) == 10

