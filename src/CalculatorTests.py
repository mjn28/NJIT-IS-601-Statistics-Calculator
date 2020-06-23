import unittest
from Calculator import Calculator
#from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # To test instantiation of calculator class
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # Testing
    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(6,4), 10)
        self.assertEqual(self.calculator.result, 10)
        #self.testData = CsvReader('datafile_addition.csv').data


    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(6,4), 2)
        self.assertEqual(self.calculator.result, 2)
        #self.testData = CsvReader('datafile_subtraction.csv').data




if __name__ == '__main__':
    unittest.main()
