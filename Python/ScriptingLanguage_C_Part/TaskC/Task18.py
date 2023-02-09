"""
    18. Написать генератор возвращающий пары простых чисел-близнецов
    (отличающихся на 2)(30 баллов)
"""
# (m, m + 2)
# 4((m-1)! + 1) + m % m(m - 2) == 0
# https://coderoad.ru/36191209/%D0%92%D1%8B%D0%B2%D0%B5%D0%B4%D0%B8%D1%82%D0%B5-%D0%B2%D1%81%D0%B5-%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D1%8B-%D0%B1%D0%BB%D0%B8%D0%B7%D0%BD%D0%B5%D1%86%D0%BE%D0%B2-%D0%BD%D0%B8%D0%B6%D0%B5-100-%D0%B2-Python
# https://www.cyberforum.ru/python-beginners/thread2622800.html
import math


def primes(n=2): # don't provide a different n value, or you will get odd results
    yield from filter(lambda x: x % n, primes(n + 1))


def gen_prims():
    for m in range(2, 1000):
        if m > 100:
            break
        z = (m * (m + 2))
        if z == 0:
            continue
        v = (4 * (math.factorial(m-1) + 1) + m)
        answer_vilson = v % z
        if answer_vilson == 0:
            answer = (m, m + 2)
            yield answer


def main():
    z = gen_prims()
    # z = gen_prims()
    for x in z:
        print(x)
        if x[0] > 100:
            break


if __name__ == '__main__':
    main()
