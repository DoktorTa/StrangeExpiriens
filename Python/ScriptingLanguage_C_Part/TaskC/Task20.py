"""
Функция, принимающая итератор строк, которая возвращает только те строки,
 которые отсортированы лексикографически(30)
"""
import collections


def check_lecks(iter_str):
    string_lecks = []
    for string in iter_str:
        if list(string) == list(sorted(sorted(string), key=str.upper)):
            string_lecks.append(string)
    return string_lecks


def main():
    x = check_lecks(iter(["ba", "ab", "aAb", "Ba", "AbB", "aBAb", "AaBb"]))
    print(x)


if __name__ == '__main__':
    main()
