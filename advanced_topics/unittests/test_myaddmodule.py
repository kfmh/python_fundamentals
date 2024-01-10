# import module you want to test
import unittest
from myaddmodule import add

class TestAddFunction(unittest.TestCase):
    """
    Test suite for the add function in myaddmodule.

    Methods
    -------
    test_add_positive_numbers():
        Tests the add function with positive integer inputs.
    
    test_add_negative_numbers():
        Tests the add function with negative integer inputs.
    """
    
    def test_add_postiive_numbers(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

if __name__ == "__main__":
    unittest.main()