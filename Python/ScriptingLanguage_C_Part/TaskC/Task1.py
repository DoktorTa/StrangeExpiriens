# 01. Написать класс "вектор" с операциями:
# +(сложение), -(вычитание), *(умножение на число), [ ](доступ к координатам)

class InvalidVectorsDimension(Exception):
    pass


class MyVector:
    __vector_cord: list

    def __init__(self, cords: list):
        self.__vector_cord = []

        for cord in cords:

            if cord is not int:
                self.__vector_cord.append(cord)
            else:
                raise TypeError

    def check_dimension(self, vector_1_cord: list):
        return len(self.get_vector_cord) == len(vector_1_cord)

    @property
    def get_vector_cord(self) -> list:
        return self.__vector_cord


class VectorOperation:

    @staticmethod
    def add(vector_1: MyVector, vector_2: MyVector) -> MyVector:
        vector_1_cord = vector_1.get_vector_cord
        vector_2_cord = vector_2.get_vector_cord

        if vector_1.check_dimension(vector_2_cord):
            vector_answer_cord = []

            for inc in range(len(vector_2_cord)):
                vector_answer_cord.append(
                    vector_1_cord[inc] + vector_2_cord[inc])

            vector_answer = MyVector(vector_answer_cord)
            return vector_answer

        raise InvalidVectorsDimension

    @staticmethod
    def sub(vector_1: MyVector, vector_2: MyVector):
        vector_1_cord = vector_1.get_vector_cord
        vector_2_cord = vector_2.get_vector_cord

        if vector_1.check_dimension(vector_2_cord):
            vector_answer_cord = []

            for inc in range(len(vector_2_cord)):
                vector_answer_cord.append(
                    vector_1_cord[inc] - vector_2_cord[inc])

            vector_answer = MyVector(vector_answer_cord)
            return vector_answer

        raise InvalidVectorsDimension

    @staticmethod
    def mul_to_const(vector_1: MyVector, const: int):
        vector_1_cord = vector_1.get_vector_cord

        vector_answer_cord = []

        for inc in range(len(vector_1_cord)):
            vector_answer_cord.append(vector_1_cord[inc] * const)

        vector_answer = MyVector(vector_answer_cord)
        return vector_answer
