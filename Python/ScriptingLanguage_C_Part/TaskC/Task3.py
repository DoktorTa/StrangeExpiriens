import copy


def minor(a, i, j):
    b = copy.deepcopy(a)  # копирование!
    del b[i]

    for i in range(len(a[0]) - 1):
        del b[i][j]

    return b


def det(a: list):
    m = len(a)
    n = len(a[0])

    if m != n:
        return None

    if n == 1:
        return a[0][0]

    signum = 1
    determinant = 0
    # разложение по первой строке

    for j in range(n):
        determinant += a[0][j] * signum * det(minor(a, 0, j))
        signum *= -1

    return determinant


def main():
    answer = det([[1, 2], [3, 4]])
    print(answer)


if __name__ == '__main__':
    main()