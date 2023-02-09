"""
    17. Написать кэширующий декоратор,
     для функции f, если f(x) и f(x=) можно считать разными вызовами(40 баллов)
"""


def cache(func):
    data = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key is not data:
            data[key] = func(*args, **kwargs)
            print(data)
        return data[key]

    return wrapper


@cache
def m(a, b=0):
    return a + b


def main():
    m(1)
    m(a=2)
    m(1, b=3)
    m(a=4, b=5)


if __name__ == '__main__':
    main()
