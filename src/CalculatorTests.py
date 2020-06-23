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

    # Testing addition
    def test_addition(self):
        add_test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in add_test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        add_test_data.clear()

    #Testing subtraction
    def test_subtraction(self):
        subtract_test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in subtract_test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        subtract_test_data.clear()

    #Testing multiplication
    def test_multiplication(self):
        multiply_test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in multiply_test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        multiply_test_data.clear()

    #Testing division
    def test_division(self):
        divide_test_data = CsvReader('/src/Unit Test Division.csv').data
        for row in divide_test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), (float(row['Result'])))
            self.assertEqual(round(self.calculator.result, 9), float(row['Result']))
        divide_test_data.clear()

    #Testing squared
    def test_squared(self):
        square_test_data = CsvReader('/src/Unit Test Square.csv').data
        for row in square_test_data:
            self.assertEqual(self.calculator.square (row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        square_test_data.clear()





if __name__ == '__main__':
    unittest.main()
