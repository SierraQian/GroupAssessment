# problem_tests.py
import unittest
from problem1_func import find_gcd

class TestFindGCD(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(find_gcd(15, 25), 5)
        self.assertEqual(find_gcd(50, 20), 10)
        self.assertEqual(find_gcd(36, 48), 12)

    def test_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            find_gcd(-15, 25)
        self.assertEqual(str(context.exception), "Both inputs must be positive integers.")

        with self.assertRaises(Exception) as context:
            find_gcd(-50, -20)
        self.assertEqual(str(context.exception), "Both inputs must be positive integers.")

        with self.assertRaises(Exception) as context:
            find_gcd(-36, 48)
        self.assertEqual(str(context.exception), "Both inputs must be positive integers.")

    def test_one_zero_input(self):
        self.assertEqual(find_gcd(0, 10), 10)
        with self.assertRaises(Exception) as context:
            find_gcd(-10, 0)
        self.assertEqual(str(context.exception), "Both inputs must be positive integers.")

        with self.assertRaises(Exception) as context:
            find_gcd(0, 0)
        self.assertEqual(str(context.exception), "Both inputs must be positive integers.")

    def test_non_integer_input(self):
        with self.assertRaises(Exception) as context:
            find_gcd(15, 3.5)
        self.assertEqual(str(context.exception), "Both inputs must be positive integers.")

        with self.assertRaises(Exception) as context:
            find_gcd(50, "hello")
        self.assertEqual(str(context.exception), "Both inputs must be positive integers.")

if __name__ == '__main__':
    unittest.main()
