"""
31. Реализовать декоратор `with_retries`, принимающий в качестве параметра
    натуральное число `n`. При вызове функции, к которой применён декоратор,
    необходимо сделать не более `n` попыток вызова, пока функция не отработает
    без исключения (исключениями считать классы Exception и его предков);
    в противном случае пробросить крайнее исключение. (40 баллов)
"""


def with_retries(n: int):
    n = n

    def decor(func):

        def wrapper(*args, **kwargs):
            e = 0
            for i in range(n):
                try:
                    answer = func(*args, **kwargs)
                except Exception as a:
                    e = a
                    continue
                else:
                    return answer
            raise e

        return wrapper

    return decor


@with_retries(n=5)
def a():
    x = 0
    z = 1 / x
    return 1


def main():
    print(a())


if __name__ == '__main__':
    main()
