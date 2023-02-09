import unittest
from Task34 import Rational


class TestTask34(unittest.TestCase):
    def test_init(self):
        r = Rational(1, 3)
        self.assertEqual(str(r), r"1 / 3")
        self.assertEqual(r.get_numerator, 1)
        self.assertEqual(r.get_denominator, 3)

    def test_add(self):
        self.assertEqual(Rational(1, 2) + Rational(1, 2), 1)
        self.assertEqual(Rational(1, 2) + Rational(1, 3), Rational(5, 6))
        self.assertEqual(Rational(1, 2) + Rational(2, 2), Rational(6, 4))
        self.assertEqual(Rational(1, 2) + 1, Rational(3, 2))
        self.assertEqual(Rational(2, 2) + 2, 3)
        self.assertEqual(Rational(-2, 2) + Rational(2, 2), 0)
        self.assertEqual(Rational(-2, 2) + Rational(3, 2), Rational(2, 4))

    def test_sub(self):
        self.assertEqual(Rational(1, 2) - Rational(1, 2), 0)
        self.assertEqual(Rational(3, 2) - Rational(1, 2), 1)
        self.assertEqual(Rational(1, 2) - Rational(1, 3), Rational(1, 6))
        self.assertEqual(Rational(3, 2) - 1, Rational(1, 2))
        self.assertEqual(Rational(1, 2) - 1, Rational(-1, 2))

    def test_mul(self):
        self.assertEqual(Rational(2, 1) * Rational(1, 2), 1)
        self.assertEqual(Rational(1, 2) * Rational(1, 2), Rational(1, 4))
        self.assertEqual(Rational(3, 1) * Rational(1, 2), Rational(3, 2))
        self.assertEqual(Rational(2, 1) * Rational(0, 2), 0)
        self.assertEqual(Rational(2, 1) * Rational(-1, 2), -1)
        self.assertEqual(Rational(2, 1) * 1, 2)
        self.assertEqual(Rational(2, 1) * 0, 0)
        self.assertEqual(Rational(2, 1) * -1, -2)
        self.assertEqual(Rational(1, 3) * 2, Rational(2, 3))

    def test_div(self):
        self.assertEqual(Rational(1, 2) / Rational(1, 2), 1)
        self.assertEqual(Rational(1, 2) / Rational(2, 1), Rational(1, 4))
        self.assertEqual(Rational(4, 2) / 2, 1)
        self.assertEqual(Rational(1, -2) / Rational(1, 2), -1)
        self.assertEqual(Rational(1, 2) / Rational(-1, 2), -1)


    def test_last(self):
        self.assertEqual((4 - (Rational(1, 3) * 3 + 1)), 2)
        self.assertEqual((4 - (Rational(1, 3) * 3 + 1) / Rational(2)), 2)


if __name__ == '__main__':
    unittest.main()
