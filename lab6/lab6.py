import numpy as np
from scipy.optimize import linear_sum_assignment


def main():

    matrix = np.array([[2.3, 1.9, 2.2, 2.7],
                       [1.8, 2.2, 2.0, 1.8],
                       [2.5, 2.0, 2.2, 3.0],
                       [2.0, 2.4, 2.4, 2.8]])

    row_ind, col_ind = linear_sum_assignment(matrix)
    print(col_ind)

    result = []

    for i in range(len(matrix[0])):
        result.append(matrix[i][col_ind[i]])

    print(result)


if __name__ == '__main__':
    main()
