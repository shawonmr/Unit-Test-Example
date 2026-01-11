# test_calculator_unittest.py
import unittest
from calculator import add, subtract


class TestCalculatorFunctions(unittest.TestCase):
    # 1. Setup/Teardown methods can be added here (e.g., setUp/tearDown)

    def test_add_positive_numbers(self):
        """Tests standard addition of positive integers."""
        # Use an assertion method to check the expected result
        self.assertEqual(add(5, 7), 12)

    def test_add_negative_and_positive(self):
        """Tests addition resulting in zero."""
        self.assertEqual(add(-10, 10), 0)

    def test_subtract_numbers(self):
        """Tests subtraction of two numbers."""
        self.assertEqual(subtract(15, 8), 7)

    def test_subtract_to_negative(self):
        """Tests subtraction that results in a negative number."""
        self.assertEqual(subtract(5, 10), -5)


# This allows the script to be executed directly from the command line
if __name__ == '__main__':
    unittest.main()
