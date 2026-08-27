import unittest
from exceptions import Divider

class TestDivider(unittest.TestCase):

    def setUp(self):
        self.divider = Divider()

    def test_divider_normal(self):
        result = self.divider.divide(10 , 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.divider.divide(10, 0)

    def test_divide_with_string_input(self):
        with self.assertRaises(TypeError):
            self.divider.divide('10', 2)

    def test_divide_with_none_input(self):
        with self.assertRaises(TypeError):
            self.divider.divide(None, 7)

    def test_divide_with_list_input(self):
        with self.assertRaises(TypeError):
            self.divider.divide([10, 20], 2)

if __name__ == '__main__':
    unittest.main()
