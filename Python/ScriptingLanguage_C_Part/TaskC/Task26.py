"""
    26. Реализовать генераторную функцию, принимающую итератор произвольных
    объектов и возвращающую их без повторений. Порядок следования объектов
    должен сохраниться.
"""


def get_no_repetitions_gen(arbitrary_obj_iter):
    no_rep_collection = set()
    for item in arbitrary_obj_iter:
        try:
            if tuple(item) not in no_rep_collection:
                no_rep_collection.add(tuple(item))
                yield item
        except TypeError:
            if item not in no_rep_collection:
                no_rep_collection.add(item)
                yield item


def f():
    pass


def main():
    col = [[1], [2], [1], 2, 3, 'qq', 'x']
    col = ["", [], [], 1, 1, 1, 2, 3, [], f(), f()]
    # for i in col:
    #     print(i)
    # iter_col = col.__iter__()
    x = get_no_repetitions_gen(iter(col))
    print(list(x))


if __name__ == '__main__':
    main()
