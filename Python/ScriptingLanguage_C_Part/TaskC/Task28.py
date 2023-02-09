"""
    28. Написать генераторную функцию, возвращающую подмножества множества.
     itertools.combinations использовать нельзя: (30 баллов)
"""


def power_set(s):
    elements = list(s)
    if len(elements) > 0:
        head = elements[0]
        for tail in power_set(elements[1:]):
            yield [head] + tail
            yield tail
    else:
        yield []


def main():
    x = power_set([1, 2, 3])
    print(list(x))


if __name__ == '__main__':
    main()
