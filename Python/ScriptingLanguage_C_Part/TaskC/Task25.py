"""
25. Реализовать функцию принимающую натуральное число и возвращающую количество
    простых множителей в разложении числа. Если передано не число выбросить
    typeerror. Если передано не натуральное число то valueerror.
"""


def factor(n: int):

    if not isinstance(n, int) and not (isinstance(n, float)):
        raise TypeError
    if (n <= 0) or n % 1 != 0:
        raise ValueError

    Ans = []
    ans = {}
    d = 2

    while d * d <= n:
        if n % d == 0:
            Ans.append(d)

            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return len(Ans)


def main():
    print(factor(225))


if __name__ == '__main__':
    main()
