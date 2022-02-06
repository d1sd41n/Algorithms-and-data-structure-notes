def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(4) == 24
assert factorial(7) == 5040
