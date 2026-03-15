# test_my_math.py

import unittest
from my_math import add, divide

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)   # Expected 5
        self.assertEqual(add(-1, 1), 0)  # Expected 0

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)  # Expected 5
        self.assertRaises(ValueError, divide, 10, 0)  # Division by zero check

# Run tests
if __name__ == "__main__":
    unittest.main()
