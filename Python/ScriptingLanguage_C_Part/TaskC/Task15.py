"""
    Написать, функцию, которая принимает два итератора и возвращает расстояние
    Хэминга между этими итераторами.
"""


def hamming(iter_1, iter_2):
    hamming_distance = 0

    if len(iter_1.__reduce__()[1][0]) < len(iter_2.__reduce__()[1][0]):
        iter_1, iter_2 = iter_2, iter_1

    for item in iter_1:
        try:
            if item != iter_2.__next__():
                hamming_distance += 1
        except StopIteration:
            hamming_distance += 1

    return hamming_distance


def main():
    items_1 = "123321222"
    items_2 = "123331"
    items_3 = [1, 2, 3, 4]
    items_4 = [1, 2, 3, 5]
    print(hamming(iter(items_3), iter(items_4)))


if __name__ == '__main__':
    main()
