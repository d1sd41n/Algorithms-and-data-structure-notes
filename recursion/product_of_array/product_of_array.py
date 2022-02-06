
def product_of_array(arr):
    if len(arr) == 1:
        return arr[0]

    return arr[-1] * product_of_array(arr[:-1])


assert product_of_array([1, 2, 3]) == 6
assert product_of_array([1, 2, 3, 10]) == 60
assert product_of_array([20, 300, 1, 50]) == 300000