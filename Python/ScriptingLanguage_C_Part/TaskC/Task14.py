"""
    14. Написать декоратор, который будет считать кол-во вызовов функции,
     сохраняя это кол-во в атрибут calls
"""


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    func.calls = 0

    def wrapper(*args, **kwargs):
        func.calls += 1
        res = func(*args, **kwargs)
        return res

    return wrapper


@counter
def b():
    print(2)


def main():
    b()
    b()
    b()


if __name__ == '__main__':
    main()
