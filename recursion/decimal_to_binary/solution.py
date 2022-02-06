

from multiprocessing.context import assert_spawning


def decimal_to_binary(num):
    assert int(num) == num, "bad input"

    if not num//2:
        return str(num % 2)

    return decimal_to_binary(num//2) + str(num % 2)


assert "1101" == decimal_to_binary(13)
assert "10" == decimal_to_binary(2)
assert "1010" == decimal_to_binary(10)
assert "1111" == decimal_to_binary(15)
assert "1100100" == decimal_to_binary(100)
assert "1001110" == decimal_to_binary(78)
