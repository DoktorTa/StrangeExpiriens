"""
09. Написать функцию которая принимает на вход строку и возвращает строку,
    из которой удалены все слова, повторяющиеся подряд.
    Сделать это с помощью регулярных выражений. (30 баллов)
"""

# (?<word>\w+) +(?=\k<word>)
# \b(\w+)\s+\1\b
# (\b\w+\b)(\s+\1)+
import re


def main(string: str):
    p = re.compile(r"(\b\w+\b)(?=(\s+\1)) ")
    print(re.sub(p, "", string))


if __name__ == '__main__':
    main("hello hello hello gun my bitch bitch oo")