import numpy as np


def get_minmax(matrix):
    transpose_matrix = matrix.T

    cols_min_values = []

    for col in transpose_matrix:
        cols_min_values.append(np.max(col))

    cols_min_values.append(get_maxmin(matrix))

    return np.min(cols_min_values)


def get_maxmin(matrix):
    rows_min_values = []

    for row in matrix:
        rows_min_values.append(np.min(row))

    return np.max(rows_min_values)


def main():
    matrix = np.array([
        [-1, 9, 6, 8],
        [-2, 10, 4, 6],
        [5, 3, 0, 7],
        [7, -2, 8, 4]
    ])

    print(get_minmax(matrix))
    print(get_maxmin(matrix))


if __name__ == '__main__':
    main()