matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def sum_diagonal(matrix: list) -> int:
    rows = len(matrix)
    sum = 0

    for row in range(0, rows):
        sum += matrix[row][row]

    return sum

assert sum_diagonal(matrix) == 15