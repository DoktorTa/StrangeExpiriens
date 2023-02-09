"""
22. На вход подается строка, в которой встречается дата в формате dd.mm.yyyy,
    ее надо заменить в этой строке на формат yyyy-mm-dd На самом деле меня
    вообще напрягают бесполезные и бесячие по моему мнению вещи.
    Это просто так сильно меня выматывает Примерно на 20 баллов
"""
import re


def replace_time(text:str) -> str:
    pattern = re.compile(r"([0][1-9]|[1-2][0-9]|[3][0-1])"
                         r".([0-1][1-9]|[1][0-2])"
                         r".([0-9]{4})")
    text_mod = re.sub(pattern, r'\3-\2-\1', text)
    return text_mod


def main():
    text_good = "hello piter 0001-01-01 helo pider 9999-12-31"
    text = "hello piter 01.01.0001 helo pider 31.12.9999"
    text_mod = replace_time(text)
    print(text_mod == text_good, text_mod)


if __name__ == '__main__':
    main()
