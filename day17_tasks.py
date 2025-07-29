# calculator_with_tests.py

import logging
import unittest

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Main calculator logic
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero")
        raise

def multiply(x, y):
    return x * y

# Custom Exception (optional)
class NegativeInputError(Exception):
    pass

def square_root(x):
    if x < 0:
        logging.error("Negative input not allowed in square_root")
        raise NegativeInputError("Negative input not allowed")
    return x ** 0.5

# Unit tests
class TestCalculator(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_square_root(self):
        self.assertEqual(square_root(16), 4)

    def test_square_root_negative(self):
        with self.assertRaises(NegativeInputError):
            square_root(-1)

# Run tests if executed directly
if __name__ == '__main__':
    unittest.main()
