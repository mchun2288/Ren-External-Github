import unittest

import calc


class CalcTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 4), 2.5)

    def test_power(self):
        self.assertEqual(calc.power(2, 3), 8)

    def test_percent(self):
        self.assertEqual(calc.percent(200, 10), 20)

    def test_factorial(self):
        self.assertEqual(calc.factorial(5), 120)

    def test_average(self):
        self.assertEqual(calc.average([1, 2, 3]), 2)

    def test_evaluate(self):
        calc.evaluate("2 + 3 * 4")

    def test_history_isolated(self):
        self.assertEqual(calc.record("a"), ["a"])
        self.assertEqual(calc.record("b"), ["b"])


if __name__ == "__main__":
    unittest.main()
