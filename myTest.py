import unittest

#--------class1----------
# class MyTest(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(1 , 1)
#
#     def test_something_else(self):
#         self.assertTrue(8 > 4)
#
# if __name__ == '__main__':
#     unittest.main()

#--------class2----------
def add(a , b):
    return a+b

class TestMathFunction(unittest.TestCase):
    def test_add_positive_number(self):
        self.assertEqual(add(1,2), 3)

    def test_add_negetive_number(self):
        self.assertEqual(add(1,-2), -1)

    def test_add_mixed_number(self):
        self.assertEqual(add(2,7), 9)


if __name__ == '__main__':
    unittest.main()

