import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # To test instantiation of calculator class
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # Testing
    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(6,4), 10)




if __name__ == '__main__':
    unittest.main()
