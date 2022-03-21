
def capitalizeWords(arr):
    if not len(arr):
        return []

    current = arr.pop()

    capitalizeWords(arr)
    current_cap = current.upper()
    arr.append(current_cap)

    return arr


words = ['i', 'am', 'learning', 'recursion']
assert capitalizeWords(words) == ['I', 'AM', 'LEARNING', 'RECURSION']