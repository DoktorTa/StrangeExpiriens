"""
Написать функцию, которая принимает на вход вектор (список),
в котором в порядке убывания степеней записаны коэффициенты
многочлена над полем Z. Вернуть все его корни в порядке убывания.
"""
import numpy


def main(index: list):
    r = numpy.roots(index)
    r = sorted(r, reverse=True)
    return r


if __name__ == '__main__':
    roots = main([1, 2, 3, 4, 5, 6, 7])
    print(roots)
