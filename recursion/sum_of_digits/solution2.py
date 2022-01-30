
def sum_of_digits(x):
    
    assert int(x) == x and x >= 0, "error, bad input"
    if x == 0:
        return x

    return int(x % 10) + sum_of_digits(int(x / 10))

print(sum_of_digits(1231111523))