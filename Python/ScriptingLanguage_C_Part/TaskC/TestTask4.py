import unittest
from Task4 import A


class TestTask4(unittest.TestCase):
    def test_something(self):
        s = {2016, 930, 37506, 420, 6, 2184, 42, 8970, 8364, 1806, 1428, 630, 21114, 120, 10998, 23994, 156}
        a = A()
        self.assertEqual(a.chech(15), s)


if __name__ == '__main__':
    unittest.main()
