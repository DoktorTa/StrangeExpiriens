import unittest
import os
from FirstTask import JarikPrimDecstra


class TestJarikPrimDecstra(unittest.TestCase):

    def test_file_read(self):
        j = JarikPrimDecstra()
        path = os.path.dirname(os.path.abspath(__file__))

        file_data = "4\n" \
                    "32767 25 4 32767\n" \
                    "25 32767 0 32767\n" \
                    "4 0 32767 7\n" \
                    "32767 32767 7 32767"

        self.assertEqual(j.file_read(path + r"/in.txt"), file_data)

    def test_create_matrix_graph(self):
        j = JarikPrimDecstra()
        path = path = os.path.dirname(os.path.abspath(__file__))

        matrix_graf = [[32767, 25, 4, 32767],
                       [25, 32767, 0, 32767],
                       [4, 0, 32767, 7],
                       [32767, 32767, 7, 32767]]

        file_data = j.file_read(path + r"/in.txt")

        self.assertEqual(j.create_matrix_graph(file_data), matrix_graf)

    def test_min_len(self):
        j = JarikPrimDecstra()
        inc = 0

        matrix_graf = [[32767, 25, 4, 32767],
                       [25, 32767, 0, 32767],
                       [4, 0, 32767, 7],
                       [32767, 32767, 7, 32767]]

        answer = [4, 0, 0, 7]

        for ver in matrix_graf:
            self.assertEqual(j.min_len(ver), answer[inc])
            inc += 1


if __name__ == '__main__':
    unittest.main()
