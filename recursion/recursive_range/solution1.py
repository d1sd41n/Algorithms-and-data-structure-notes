def recursive_range(num):
    if num < 1:
        return 0
    
    return num + recursive_range(num-1)

assert recursive_range(6) == 21
assert recursive_range(10) == 55
assert recursive_range(3) == 6
assert recursive_range(4) == 10
assert recursive_range(7) == 28



