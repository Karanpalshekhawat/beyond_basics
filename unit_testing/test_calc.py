import unittest
from unit_testing import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(5, 4)
        self.assertEqual(result, 9)


if __name__=='__main__':
    unittest.main()
