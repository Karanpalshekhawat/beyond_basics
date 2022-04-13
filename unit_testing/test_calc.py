import unittest
from unit_testing import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(5, 4)
        self.assertEqual(result, 9)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-10, -15), -25)

    def test_subtract(self):
        self.assertEqual(calc.subtract(100, 50), 50)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        """dividing by 0 raised correct zero"""
        self.assertRaises(ValueError, calc.divide, 10, 0)

        """another way, better way to catch exception using context manager"""
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
