"""
    Пусть панграмма это такая строка в которой содержатся все буквы алфавита.
    Пример такой фразы: The quick brown fox jumps over the lazy dog.
    Написать такую функцию определяющую является ли строка панграммой.
    На вход функции подается сама строка и алфавит.
    (30 баллов)
    (превратить строку в set и проверить вложенность алфавита в set от строки)
"""


def main(string: str) -> bool:
    string_lower = string.lower()
    string_alphabet = set(string_lower)
    alphabet = set(''.join([chr(i) for i in range(ord("a"), ord("a") + 26)]))
    return alphabet.issubset(string_alphabet)


if __name__ == '__main__':
    x = main("The quick brown fox jumps over the lazy dog")
    print(x)
    x = main("the lazy dog")
    print(x)
    x = main("The quick brown fox jumps oer the lazy dog aaaaaav")
    print(x)
