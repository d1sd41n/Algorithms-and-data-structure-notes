"""Given a list, write a function to get first, second best 
scores from the list.

List may contain duplicates."""

array = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

def firstSecond(array):
    temp = [0, 0]

    for x in array:
        if x > temp[0] and x > temp[1]:
            temp[1] = temp[0]
            temp[0] = x
            continue

        elif x < temp[0] and x > temp[1]:
            temp[1] = x

    return temp[0], temp[1]

assert firstSecond(array) == (90, 87)
