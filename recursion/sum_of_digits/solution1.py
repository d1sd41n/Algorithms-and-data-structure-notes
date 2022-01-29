
def sum_(x):
    
    assert int(x) == x and x > 0, "error, bad input"
    if x < 10:
        return x

    last_digit = x % 10
    cut_number = (x/10) - (last_digit/10)

    return last_digit + sum_(cut_number)

print(sum_(1234))