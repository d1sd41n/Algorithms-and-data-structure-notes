# Write a function to find the missing number in a given integer array of 1 to 100.


def missin_number(array, total_count):
    theoric_sum = total_count * (total_count + 1) / 2

    total_sum = 0

    for x in array:
        total_sum += x
    
    return theoric_sum - total_sum

assert missin_number([1, 2, 3, 4, 6], 6) == 5