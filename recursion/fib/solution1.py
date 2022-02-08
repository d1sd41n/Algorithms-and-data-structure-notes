def fib(num):
    if num <= 2:
        return 1
    return fib(num - 2) + fib(num - 1)


assert fib(4) == 3
assert fib(10) == 55
assert fib(28) == 317811
assert fib(35) == 9227465
