"""
08. Написать функцию-декоратор, который принимает типы или списки типов и
 проверяет что параметры, передаваемые в функцию, соответствуют указанным типам
  Если один из переданных параметров не соответствует ни одному из типов,
    выкинуть исключение TypeError. (40 баллов) Пример:
        @check_types((int, str), list)
        def some_func(a, b):
            pass
"""


def check_types(*args, **kwargs):

    def actual_dec(func):

        func.argstypes = args

        def wrapper(*args, **kwargs):
            check_t(args, func.argstypes)
            res = func(*args, **kwargs)
            return res

        def check_t(args, argstypes):
            print(args, argstypes)

            inc = 0
            for argstype in argstypes:

                if (type(argstype) == list) or (type(argstype) == tuple):
                    check_t(args[inc], argstype)
                else:
                    if isinstance(args[inc], argstype):
                        pass
                    else:
                        raise TypeError

                inc += 1

        return wrapper

    return actual_dec


@check_types(int, str)
def some_func_too(a, b):
    print("Good")


@check_types((int, str), list)
def some_func(a, b):
    pass


def main():
    # some_func_too(1, "")
    some_func((1, ""), [])


if __name__ == '__main__':
    main()
