from unittest import TestCase
from function import divide
from function import multiply


class TestFunction(TestCase):
    # def test_divide_result(self):
    #     dividend = 15
    #     divisor = 3
    #     expected_result = 5
    #     self.assertEqual(divide(dividend, divisor), expected_result)

    # def test_divide_negative(self):
    #     dividend = 15
    #     divisor = -3
    #     expected_result = -5.0001
    #     self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.001)

    # def test_divide_zerodividend(self):
    #     dividend = 0
    #     divisor = 30
    #     expected_result = 0
    #     self.assertEqual(divide(dividend, divisor), expected_result)

    # def test_divide_zerodivisor(self):
    #     with self.assertRaises(ValueError):
    #         divide(25, 0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single(self):
        expected_result = 15
        self.assertEqual(multiply(expected_result), expected_result)

    def test_multiply_zero(self):
        expected_result = 0
        self.assertEqual(multiply(expected_result), expected_result)

    def test_multiply_result_zero(self):
        args = (2, 2, 2, 2, 0)
        expected_result = 0
        self.assertEqual(multiply(*args), expected_result)

    def test_multiply_result(self):
        args = (2, 2, 2, 2, 2)
        expected_result = 32
        self.assertEqual(multiply(*args), expected_result)

    def test_multiply_resultnegative(self):
        args = (2, 2, -2, 2, 2)
        expected_result = -32
        self.assertEqual(multiply(*args), expected_result)

    def test_multiply_floats(self):
        args = (2, 2, 2.0000, 2, 2)
        expected_result = 32
        self.assertEqual(multiply(*args), expected_result)
