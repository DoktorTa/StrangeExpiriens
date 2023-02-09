"""
16. Написать функцию, принимающую СЛАУ в виде списка уравнений, представленных
    в виде (список_коэффициентов, свободный член), а на выход предоставляющую
    None, если решений нет, иначе одно решение в виде списка. (40 баллов)
"""

#
# def solve(a, b):
#     a, _ = _makearray(a)
#     _assert_stacked_2d(a)
#     _assert_stacked_square(a)
#     b, wrap = _makearray(b)
#     t, result_t = _commonType(a, b)
#
#     # We use the b = (..., M,) logic, only if the number of extra dimensions
#     # match exactly
#     if b.ndim == a.ndim - 1:
#         gufunc = _umath_linalg.solve1
#     else:
#         gufunc = _umath_linalg.solve
#
#     signature = 'DD->D' if isComplexType(t) else 'dd->d'
#     extobj = get_linalg_error_extobj(_raise_linalgerror_singular)
#     r = gufunc(a, b, signature=signature, extobj=extobj)
#
#     return wrap(r.astype(result_t, copy=False))


# zero_arr = lambda n: map(lambda a: 0, range(0, n))
sub = lambda x, y: map(lambda a, b: a - b, x, y)
mulbyn = lambda x, n: map(lambda a, b=n: a * b, x)

def sub(x, y):
    for i in x:

    return

def zero_arr(n):
    arr = [0 for i in range(n)]
    return arr


def choose(x):
    i = 0
    while (x[i] == 0) and (i < len(x)):
        i += 1
    if i < len(x):
        return i
    else:
        return -1


def gauss_sol(A, b):
    if (len(A) != len(A[0])) or (len(A) != len(b)):
        return None
    M = A[:]
    c = b[:]
    n = len(M)
    indices = zero_arr(n)
    for i in range(0, n):
        print(M[i])
        k = choose(M[i])
        for j in filter(lambda a, b = i: a != b, range(0, n)):
            c[j] -= float(c[i]) * M[j][k] / M[i][k]
            M[j] = sub(M[j], mulbyn(M[i], float(M[j][k]) / M[i][k]))
        indices[i] = k
    x = zero_arr(n)
    for i in range(0, n):
        x[i] = c[indices[i]]
    return x


def main():
    a = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b = [8, -11, -3]
    print(gauss_sol(a, b))


if __name__ == '__main__':
    main()
