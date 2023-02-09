"""
24. Пусть дано натуральное число k. Обозначим S(k) сумму цифр числа k.
    Реализовать функцию, принимающую натуральное число k и возвращающую
    (S(...S(k)...)). S применяются для тех пор, пока не останется одна цифра.
    При реализации ЗАПРЕЩЕНО использовать циклы for, while а также if
"""
import math


def S(k: int):
    try:
        k = list(str(k))
        k = [int(digit) for digit in k]
        summa = sum(k)
        math.sqrt(summa - 10)
        summa = S(summa)
    except ValueError:
        pass
    return summa


def main():
    print(S(999999999999))


if __name__ == '__main__':
    main()
