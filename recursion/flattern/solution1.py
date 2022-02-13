def flatten(arr):
    current = arr.pop()
    append = True

    if type(current) == list:
        arr.extend(current)
        flatten(arr)
        append = False
    elif len(arr):
        flatten(arr)
    if append:
        arr.append(current)

    return arr


assert flatten([1, 2, 3, [4, 5]]) == [1, 2, 3, 4, 5]
assert flatten([1, [2, [3, 4], [[5]]]]) == [1, 2, 3, 4, 5]
assert flatten([[1], [2], [3]]) == [1, 2, 3]
assert flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) == [1, 2, 3]
