import unittest
import fractions as frac

class TestFractions(unittest.TestCase):
    def test_GCD_with_numbers_whose_greatest_common_divisor_is_not_one(self):
        num1 = 4
        num2 = 8
        expected_result = 4
        self.assertEqual(frac.GCD(num1, num2), expected_result)

    def test_GCD_with_numbers_whose_greatest_common_divisor_is_one(self):
        num1 = 3
        num2 = 2
        expected_result = 1
        self.assertEqual(frac.GCD(num1, num2), expected_result)

    def test_if_nominator_is_not_integer_raise_value_error(self):
        nom = 1.5
        denom = 2
        self.assertRaises(ValueError, frac.build_fraction, nom, denom)

    def test_if_denominator_is_not_integer_raise_value_error(self):
        nom = 1
        denom = 2.5
        self.assertRaises(ValueError, frac.build_fraction, nom, denom)


    def test_if_nominator_and_denominator_are_equal_then_return_tuple_of_two_ones(self):
        nom = 2
        denom = 2
        expected_result = (1, 1)
        self.assertEqual(frac.build_fraction(nom, denom), expected_result)

    def test_if_denominator_is_zero_raise_then_exception(self):
        nom = 2
        denom = 0
        self.assertRaises(ZeroDivisionError, frac.build_fraction, nom, denom)
    
    def test_simplify_tractions_if_nominator_and_denominator_have_a_gcd(self):
        input_fraction = (3, 9)
        expected_result = (1, 3)
        self.assertEqual(frac.simplify_fraction(input_fraction), expected_result)

    def test_simplify_tractions_if_nominator_and_denominator_do_not_have_gcd(self):
        input_fraction = (1, 7)
        expected_result = (1, 7)
        self.assertEqual(frac.simplify_fraction(input_fraction), expected_result)

    def test_collect_fractions_with_two_fractions_return_their_sum(self):
        input_fractions = [(1, 4), (1, 2)]
        expected_result = (3, 4)
        self.assertEqual(frac.collect_fractions(input_fractions), expected_result)

    def test_collect_fractions_with_three_fractions_return_their_sum(self):
        input_fractions = [(1, 4), (1, 2), (1, 2)]
        expected_result = (5, 4)
        self.assertEqual(frac.collect_fractions(input_fractions), expected_result)

    def test_sort_fractions_with_two_fractions(self):
        input_fractions = [(2, 3), (1, 2)]
        expected_result = [(1, 2), (2, 3)]
        self.assertEqual(frac.sort_fractions(input_fractions), expected_result)
    
    def test_sort_fractions_with_three_fractions(self):
        input_fractions = ([(2, 3), (1, 2), (1, 3)])
        expected_result = [(1, 3), (1, 2), (2, 3)]
        self.assertEqual(frac.sort_fractions(input_fractions), expected_result)

    def test_sort_fractions_with_more_fractions(self):
        input_fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        expected_result = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
        self.assertEqual(frac.sort_fractions(input_fractions), expected_result)


if __name__ == '__main__':
    unittest.main()
