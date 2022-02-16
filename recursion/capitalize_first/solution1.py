def capitalizeFirst(arr):

    if not len(arr):
        return []

    current = arr.pop()

    capitalizeFirst(arr)
    current_cap = current.capitalize()
    arr.append(current_cap)

    return arr


assert capitalizeFirst(["car", "taco", "banana"]) == ["Car", "Taco", "Banana"]
assert capitalizeFirst(["rice", "papa", "mama"]) == ["Rice", "Papa", "Mama"]
assert capitalizeFirst(["olakaze", "hola", "mmmm"]) == [
    "Olakaze", "Hola", "Mmmm"]
