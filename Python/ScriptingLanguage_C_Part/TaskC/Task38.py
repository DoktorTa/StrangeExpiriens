"""
38. Реализовать менеджер контекстов open_files(*filenames, mode, encoding),
    открывающий заданные файлы в указанном режиме и кодировке.
     Пример использования:
        with open_files(‘1.txt’, ‘2.txt’, mode=’r’, encoding=’cp866’) as (f, g):
            print(f.read(), g.read())
"""
import os


class open_files:
    __mode = "r"
    __encoding = "utf8"
    __file = []

    def __init__(self, *args, mode: str, encoding="utf8"):
        self.__mode = mode
        self.__encoding = encoding
        self.__file = []
        for i in args:
            print(i)
            path = os.path.dirname(os.path.abspath(__file__))
            self.__file.append(path + i)

    def __enter__(self):
        while len(self.__file) != 0:
            try:
                self.fp = open(self.__file.pop(), mode=self.__mode, encoding=self.__encoding)
            except IOError:
                self.fp = open(self.__file.pop(), mode=self.__mode, encoding=self.__encoding)
            yield self.fp

    def __exit__(self, exp_type, exp_value, exp_tr):
        if exp_type is IOError:
            self.fp.close()
            return True
        self.fp.close()


def main():
    with open_files(r"/Task7_1.txt", r"/Task7_2.txt", mode="r") as (f, g):
        print(f.read(), g.read())


if __name__ == '__main__':
    main()
