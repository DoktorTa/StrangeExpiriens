from functools import wraps


import functools
import time


def debug(file_obj):
    def inner(func):
        @wraps(func)
        def _wrap(*args, **kwargs):
            start = time.time()

            result = func(*args, **kwargs)

            end = time.time()
            time_elapsed = end - start

            file_obj.write(f'{time_elapsed} {func.__name__}({", ".join(map(str, args))}, '
                           f'{", ".join(map(lambda tup: f"{tup[0]}={tup[1]}", kwargs.items()))}) -> {result}\n')
            return result
        return _wrap
    return inner


@debug("file", "a")
def func():
    inc = 0
    while inc != 100:
        inc += 1
    return inc


if __name__ == '__main__':
    func()

