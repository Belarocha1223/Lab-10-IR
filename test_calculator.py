# https://github.com/Belarocha1223/Lab-10-IR
# Partner 1: Isabela Rocha
# Partner 2: none

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(5, 5), 0)
        self.assertEqual(calculator.subtract(2, 10), -8)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(8, 2), 3.0)
        self.assertAlmostEqual(calculator.logarithm(100, 10), 2.0)
        self.assertAlmostEqual(calculator.logarithm(16, 4), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 1)

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(1, 5), 5)
        self.assertEqual(calculator.div(5, 25), 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 2)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(8, 15), 17.0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(0), 0.0)

if __name__ == '__main__':
    unittest.main()
