import copy


def main(matrix: list):
    if not ((isinstance(matrix, list)) and (isinstance(matrix[0], list))):
        raise ValueError

    m = len(matrix)
    n = len(matrix[0])
    matrix_g = copy.deepcopy(matrix)

    matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]) - 1, -1, -1)]
    return matrix


if __name__ == '__main__':
    x = [[1, 2, 3], [4, 5, 6]]
    print(main(x))
    print(x)