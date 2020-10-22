import unittest

from decimal_number_to_roman import divide_to_parts,\
    to_full_list_sequence, roman, make_roman_numbers


class TestNumberToRoman(unittest.TestCase):
    
    def test_divide_to_parts(self):
        case_1, case_2 = 1984, 1
        result_1 = [
            [1000], [500], [100, 100, 100, 100],
            [50], [10, 10, 10], [1, 1, 1, 1]
        ]
        result_2 = [[1]]
        self.assertEqual(divide_to_parts(case_1), result_1)
        self.assertEqual(divide_to_parts(case_2), result_2)

    def test_to_full_list_sequence(self):
        case_1 = [[1], 2, [3, 4], 5]
        result_1 = [[1], [2], [3, 4], [5]]
        self.assertEqual(to_full_list_sequence(case_1), result_1)

    def test_roman(self):
        case_1 = 1984
        result_1 = 'MCMLXXXIV'
        self.assertEqual(roman(case_1), result_1)

    def test_make_roman_numbers(self):
        case_1 = [
            [1000], [500], [100, 100, 100, 100],
            [50], [10, 10, 10], [1, 1, 1, 1]
        ]
        result_1 = [
            [1000], [900], [50], [10, 10, 10], [4]
        ]
        self.assertEqual(make_roman_numbers(case_1), result_1)


if __name__ == "__main__":
    unittest.main()