"""
    27. Написать функцию, дается на вход две строки,
    вернуть сдвиг если вторая строка это циклический сдвиг первой,
    если хотя бы один аргумент не строка выкинуть TypeError(30 баллов):
"""


def f(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError()
    s = s1 * 2
    return len(s1) - s.find(s2)


def main():
    print(f("abbab", "babba"))
# abbababbab


if __name__ == '__main__':
    main()
