
def capitalizeFirst(arr):

    if not len(arr):
        return []

    current = arr.pop()


    return capitalizeFirst(arr) + [current.capitalize()]

print(capitalizeFirst(["car", "taco", "banana"]))

assert capitalizeFirst(["car", "taco", "banana"]) == ["Car", "Taco", "Banana"]
assert capitalizeFirst(["rice", "papa", "mama"]) == ["Rice", "Papa", "Mama"]
assert capitalizeFirst(["olakaze", "hola", "mmmm"]) == [
    "Olakaze", "Hola", "Mmmm"]
