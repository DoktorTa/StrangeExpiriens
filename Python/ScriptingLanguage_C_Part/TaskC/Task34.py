"""
34. Реализовать класс Rational рациональных чисел с арифметическими операциями
    +, -, *, /. Арифметика также должна работать с аргументами типа целых чисел
    Пример использования: 4 - (Rational(1, 3)*3 + 1)/Rational(2)
"""


class Rational:
    __numerator: int
    __denominator: int

    def __init__(self, numerator: int, denominator=1):
        self.__numerator = numerator
        if denominator != 0:
            self.__denominator = denominator
        else:
            raise ZeroDivisionError

    def __reduction(self):
        if self.__numerator % self.__denominator == 0:
            return int(self.__numerator // self.__denominator)
        return self

    def __add__(self, other):
        if isinstance(other, Rational):
            answer = Rational(self.__numerator * other.get_denominator
                              + other.get_numerator * self.get_denominator,
                              other.get_denominator * self.get_denominator)
            answer = answer.__reduction()
            return answer

        elif isinstance(other, int):
            return self.__add__(Rational(other, 1))

    def __sub__(self, other):
        if isinstance(other, Rational):
            answer = Rational(self.__numerator * other.get_denominator
                              - other.get_numerator * self.get_denominator,
                              other.get_denominator * self.get_denominator)

            if answer.get_numerator != 0:
                answer = answer.__reduction()
            else:
                answer = 0
            return answer

        elif isinstance(other, int):
            return self.__sub__(Rational(other, 1))

    def __mul__(self, other):
        if isinstance(other, Rational):
            answer = Rational(self.__numerator * other.get_numerator,
                              other.get_denominator * self.get_denominator)

            if answer.get_numerator != 0:
                answer = answer.__reduction()
            else:
                answer = 0
            return answer

        elif isinstance(other, int):
            return self.__mul__(Rational(other, 1))

    def __truediv__(self, other):
        if isinstance(other, Rational):
            answer = Rational(self.__numerator * other.get_denominator,
                              self.get_denominator * other.__numerator)

            if answer.get_numerator != 0:
                answer = answer.__reduction()
            else:
                answer = 0
            return answer

        elif isinstance(other, int):
            return self.__truediv__(Rational(other, 1))

    def __str__(self):
        return rf"{self.__numerator} / {self.__denominator}"

    def __radd__(self, other):
        return Rational(self.__numerator * 1 + other * self.__denominator, self.__denominator * 1)

    @property
    def get_numerator(self) -> int:
        return self.__numerator

    @property
    def get_denominator(self) -> int:
        return self.__denominator

    def __eq__(self, other):
        if isinstance(other, Rational):
            if ((self.__numerator == other.get_numerator)
                    and (self.__denominator == other.get_denominator)):
                return True
        return False

    def __int__(self):
        return self.__reduction()


if __name__ == '__main__':
    print(4 - (Rational(1, 3) * 3 + 1) / Rational(2))
