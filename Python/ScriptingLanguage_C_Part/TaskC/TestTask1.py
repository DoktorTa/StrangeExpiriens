import unittest

from Task1 import MyVector, VectorOperation, InvalidVectorsDimension


class TestTask1(unittest.TestCase):
    def test_get_vector_cord(self):
        v_1 = MyVector([1, 2, 3, 4, 5])
        self.assertEqual(v_1.get_vector_cord, [1, 2, 3, 4, 5])

    def test_check_dimension(self):
        v_1 = MyVector([1, 2, 3])
        v_2 = MyVector([3, 4, 5])
        v_3 = MyVector([1, 2])

        self.assertTrue(v_1.check_dimension(v_2.get_vector_cord))
        self.assertFalse(v_1.check_dimension(v_3.get_vector_cord))

    def test_add(self):
        v_1 = MyVector([1, 2, 3])
        v_2 = MyVector([3, 4, 5])
        v_3 = MyVector([4, 6, 8])
        v_4 = MyVector([1])

        self.assertEqual(
            VectorOperation.add(v_1, v_2).get_vector_cord, v_3.get_vector_cord)

        self.assertRaises(
            InvalidVectorsDimension, lambda: VectorOperation.add(v_1, v_4))

    def test_sub(self):
        v_1 = MyVector([1, 2, 3])
        v_2 = MyVector([3, 4, 5])
        v_3 = MyVector([-2, -2, -2])
        v_4 = MyVector([1])

        self.assertEqual(
            VectorOperation.sub(v_1, v_2).get_vector_cord, v_3.get_vector_cord)

        self.assertRaises(
            InvalidVectorsDimension, lambda: VectorOperation.sub(v_1, v_4))

    def test_mul_to_const(self):
        v_1 = MyVector([1, 2, 3])
        const = 2
        v_3 = MyVector([2, 4, 6])

        self.assertEqual(
            VectorOperation.mul_to_const(v_1, const).get_vector_cord, v_3.get_vector_cord)

if __name__ == '__main__':
    unittest.main()
