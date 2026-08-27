import unittest
from .exam import *

class TestExam(unittest.TestCase):

    def test_assertEqual(self):
        self.assertEqual(add(1, 2), 3)

    def test_assertNotEqual(self):
        self.assertNotEqual(subtract(1, 2), 0)

    def test_assertTrue(self):
        self.assertTrue(is_even(4))

    def test_assertFalse(self):
        self.assertFalse(is_even(7))

    def test_assertNotIn(self):
        self.assertNotIn(4, [1,2,3,4])

    def test_assertIn(self):
        self.assertIn(4, [1,2,3,4])

    def test_asserRaises(self):
        with self.assertRaises(ValueError):
            divide(10 , 0)

    def test_assertIs(self):
        x = None
        self.assertIs(x, None)

    def test_assertIsNot(self):
        x = 'hello'
        y = 'helloo'
        self.assertIsNot(x, y)

    def test_assertIsInstance(self):
        self.assertIsInstance(4 , int)

    def test_assertNotIsInstance(self):
        self.assertNotIsInstance(4, str)

    def test_assertGreater(self):
        self.assertGreater(8, 5)

    def test_assertGraterEqual(self):
        self.assertGreaterEqual(8, 5)

    def test_assertLess(self):
        self.assertGreaterEqual(5 , 5)

    def test_assertLess(self):
        self.assertLess(2 , 7)

    def test_asserLessEqual(self):
        self.assertLessEqual(9 , 9)

    def test_assertRegex(self):
        self.assertRegex('hello world', 'hello')

    def test_assertNotRegex(self):
        self.assertNotRegex('hello world', 'hi')

    def test_assertAlmostEqual(self):
        self.assertAlmostEqual(6.258 , 6.257 , places=2)

    def test_assertNotAlmostEqual(self):
        self.assertNotAlmostEqual(6.258 , 8.257 , places=2)

    


