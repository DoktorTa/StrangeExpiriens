import math


def get_roots(poly):
    numerators = list(get_divisors(poly[0]))
    roots = set()
    for numerator in numerators:
        if abs(get_value(poly, numerator)) < 1e-4:
            roots.add(numerator)
    return sorted(list(roots))[::-1]


def get_value(poly, x):
    a = 1
    value = 0
    for coeff in poly[::-1]:
        value += a * coeff
        a *= x
    return value


def get_divisors(number):
    number = abs(number)
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            yield i
            yield -i
    yield number