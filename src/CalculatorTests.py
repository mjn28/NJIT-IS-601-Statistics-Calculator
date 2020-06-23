import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # To test instantiation of calculator class
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # Testing
    def test_addition(self):
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(6,4), 2)
        self.assertEqual(self.calculator.result, 2)
        #self.testData = CsvReader('datafile_subtraction.csv').data




if __name__ == '__main__':
    unittest.main()
