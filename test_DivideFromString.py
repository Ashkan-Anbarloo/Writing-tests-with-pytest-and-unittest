import unittest
from divideFromString import SafeDivider

class TestSafeDivide(unittest.TestCase):
    def setUp(self):
        self.divider = SafeDivider()

    def test_vali_division(self):
        result = self.divider.divide_from_string("20", 4)
        self.assertEqual(result, 5.0)

    def test_non_numeric_input(self):
        result = self.divider.divide_from_string("ali", 3)
        self.assertEqual(result, "Input muust be a numric string")

    def test_zero_division(self):
        result = self.divider.divide_from_string("11", 0)
        self.assertEqual(result, "Cannot divide by zero")

    def test_unexpected_type(self):
        result = self.divider.divide_from_string(None, 1)
        self.assertTrue('Unexpected error', result)


if __name__ == '__main__':
    unittest.main()