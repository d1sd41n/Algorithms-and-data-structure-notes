
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

assert power(3, 2) == 3 ** 2
assert power(5, 5) == 5 ** 5
assert power(4, 19) == 4 ** 19
assert power(410, 100) == 410 ** 100
assert power(3, 0) == 3 ** 0
assert power(410, 1) == 410 ** 1