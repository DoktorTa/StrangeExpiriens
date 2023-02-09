"""
21. На вход подаются два итератора написать генераторную функцию,
    которая возвращает декартово произведение по схеме
    = a  b  c  d...    1 2 3
    A 01 04 09 16... 4 4
    B 02 03 08 15... 5 5
    C 05 06 07 14... 6
    D 10 11 12 13
    . . . .
    . . . .
"""


def dekart_mul(iter_1, iter_2):
    for i in range(len(iter_1)):
        j = 0
        z = i
        for k in range(2 * i + 1):
            try:
                if z > j:
                    yield iter_1[j] * iter_2[z]
                    j += 1
                else:
                    yield iter_1[j] * iter_2[z]
                    z -= 1
            except:
                pass
        # yield iter_1[0] * iter_2[0]
        #
        # yield iter_1[0] * iter_2[1]
        # yield iter_1[1] * iter_2[1]
        # yield iter_1[1] * iter_2[0]
        #
        # yield iter_1[0] * iter_2[2]
        # yield iter_1[1] * iter_2[2]
        # yield iter_1[2] * iter_2[2]
        # yield iter_1[2] * iter_2[1]
        # yield iter_1[2] * iter_2[0]
        #
        # yield iter_1[0] * iter_2[3]
        # yield iter_1[1] * iter_2[3]
        # yield iter_1[2] * iter_2[3]
        # yield iter_1[3] * iter_2[3]
        # yield iter_1[3] * iter_2[2]
        # yield iter_1[3] * iter_2[1]
        # yield iter_1[3] * iter_2[0]


def main():
    print(list(dekart_mul([1, 2, 3], [4, 5])))


if __name__ == '__main__':
    main()
