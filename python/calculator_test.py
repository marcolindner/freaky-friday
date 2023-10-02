from calculator import Calculator
import unittest

class ClaculatorTests(unittest.TestCase):

    def test_add(self):
        calc = Calculator
        self.assertEqual(10, calc.add(5,5))

    def test_subtract(self):
        calc = Calculator
        self.assertEqual(18, calc.subtract(25,7))

if __name__ == '__main__':
    unittest.main()