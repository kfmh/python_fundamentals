# import module you want to test
import unittest
from myaddmodule import add

class TestAddFunction(unittest.TestCase):
    
    def test_add_postiive_numbers(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

if __name__ == "__main__":
    unittest.main()