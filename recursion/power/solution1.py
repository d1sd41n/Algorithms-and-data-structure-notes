

# only positive and int exp
def power(base, exp):
    assert exp == int(exp) or exp > 0, "bad input"

    if exp == 1:
        return base
    elif exp == 0:
        return 1

    return base * power(base, exp - 1)


assert power(3, 2) == 3 ** 2
assert power(5, 5) == 5 ** 5
assert power(4, 19) == 4 ** 19
assert power(410, 100) == 410 ** 100
assert power(3, 0) == 3 ** 0
assert power(410, 1) == 410 ** 1
