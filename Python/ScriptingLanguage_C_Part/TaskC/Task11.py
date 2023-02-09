import collections
"""
    Дана строка из символов, вывести список в формате символ, число повторений,
    отсортированный по убыванию частоты вхождения символа в строку.
    Если частота одинаковая, первым выводить лексикографически меньший символ. 
    Считать регистронезависимо (т.е строку привести в нижний регистр)
"""


def main(string):
    string_lower = string.lower()
    string = collections.Counter(string_lower)
    string2_sorted_lexi = sorted(string.elements())
    string = collections.Counter(string2_sorted_lexi)
    string_sorted_up = string.most_common(len(string))
    return string_sorted_up


if __name__ == '__main__':
    z = main("ssssssssddhhsfaa")
    print(z)
