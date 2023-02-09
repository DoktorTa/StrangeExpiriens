"""
06. Написать менеджер контекста, который принимает callback и reraise,
    если reraise True прокидывать исключения по стеку вверх,
    иначе вызывать callback, передавая ему ошибку и стек вызовов
    (и ещё что-то) (40 баллов)
"""
from contextlib import contextmanager


class back:
    reraise: bool
    callback: object

    def __init__(self, callback, reraise=False):
        self.callback = callback
        self.reraise = reraise

    def __enter__(self):
        return self.reraise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.reraise is True:
            return False
        self.callback(exc_type, exc_val, exc_tb)
        return True


def callback1(x, y, z):
    print(x, y, z)


def main():
    with back(callback1) as f:
        f = True
        raise ZeroDivisionError


if __name__ == '__main__':
    main()


"""
    from contextlib import ExitStack

    class Callback(ExitStack):
        def __init__(self, callback, /, *args, **kwds):
            super(Callback, self).__init__()
            self.callback(callback, *args, **kwds)
    
        def cancel(self):
            self.pop_all()
    
    with Callback(cleanup_resources) as cb:
        result = perform_operation()
        if result:
            cb.cancel()
"""