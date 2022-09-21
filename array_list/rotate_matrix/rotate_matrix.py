import numpy as np

matrix_sample = np.array([[1, 2, 3],  # 7, 4, 1
                          [4, 5, 6],  # 8, 5, 2
                          [7, 8, 9]])  # 9, 6, 3


def rotate_matrix(matrix):
    len_rows = len(matrix)

    for row in range(len_rows // 2):

        first_row = row
        last_row = len_rows - row - 1

        for col in range(first_row, last_row):
            temp = matrix[row][col]
            matrix[row][col] = matrix[-col-1][row]
            matrix[-col-1][row] = matrix[-row-1][-col-1]
            matrix[-row-1][-col-1] = matrix[col][-row-1]
            matrix[col][-row-1] = temp

    return matrix


res = rotate_matrix(matrix_sample)
res_test = np.array([[7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]])
assert (res == res_test).all() == True
