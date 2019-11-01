import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data_addition = CsvReader('/src/Unit_Test_Addition.csv').data
        pprint(test_data_addition)
        for row in test_data_addition:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data_subtraction = CsvReader('/src/Unit_Test_Subtraction.csv').data
        pprint(test_data_subtraction)
        for row in test_data_subtraction:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data_multiplication = CsvReader('/src/Unit_Test_Multiplication.csv').data
        for row in test_data_multiplication:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data_division = CsvReader('/src/Unit_Test_Division.csv').data
        for row in test_data_division:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        test_data_square = CsvReader('/src/Unit_Test_Square.csv').data
        for row in test_data_square:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt(self):
        test_data_sqrt = CsvReader('/src/Unit_Test_Square Root.csv').data
        for row in test_data_sqrt:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqrt(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
