



def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    res = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            res[i][j] = matrix[i][j]

    return res
