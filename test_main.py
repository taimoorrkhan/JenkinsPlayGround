import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):
    # Test the add() function and ensure that it returns the correct result
    def test_add(self):
        self.assertEqual(Calculator.add(10, 5), 15)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(-1, -1), -2)
        self.assertEqual(Calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 5), 5)
        self.assertEqual(Calculator.subtract(-1, 1), -2)
        self.assertEqual(Calculator.subtract(-1, -1), 0)
        # Test for floating point equality
    def test_multiply(self):
        self.assertEqual(Calculator.multiply(10, 5), 50)
        self.assertEqual(Calculator.multiply(-1, 1), -1)
        self.assertEqual(Calculator.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 5), 2)
        self.assertEqual(Calculator.divide(-1, 1), -1)
        self.assertEqual(Calculator.divide(-1, -1), 1)
        self.assertRaises(ValueError, Calculator.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
