import os
import unittest

from calibration import (find_first_digit,
                         find_last_digit,
                         form_two_digit,
                         add_up_multiple_line,

                         find_first_digit_allow_spelled,
                         find_last_digit_allow_spelled,
                         form_two_digit_allow_spelled,
                         add_up_multiple_line_allow_spelled)


class Test_calibration(unittest.TestCase):

    def test_can_find_first_digit(self):
        self.assertEqual(find_first_digit('abc0xxx9'), '0')

    def test_can_find_last_digit(self):
        self.assertEqual(find_last_digit('0a1abc'), '1')

    def test_can_form_two_digit(self):
        self.assertEqual(form_two_digit('0a1abc9'), '09')

    def test_can_add_up_multiple_line(self):
        document = 'ab11\n 412a3'
        self.assertEqual(add_up_multiple_line(document), 11 + 43)

    def test_can_solve_puzzle_1_input(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_1')
        with open(input_path) as f:
            document = f.read()
        self.assertEqual(add_up_multiple_line(document), 55130)

# ==== Part 2

    def test_can_find_first_spelled_digits(self):
        self.assertEqual(find_first_digit_allow_spelled('one3abc'), 1)

    def test_can_find_last_spelled_digits(self):
        self.assertEqual(find_last_digit_allow_spelled('one3abc'), 3)

    def test_form_two_digit_allow_spelled(self):
        self.assertEqual(form_two_digit_allow_spelled('one3abc'), 13)

    def test_can_solve_puzzle_2_input(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_2')
        with open(input_path) as f:
            document = f.read()
        self.assertEqual(add_up_multiple_line_allow_spelled(document), 54985)


if __name__ == '__main__':
    unittest.main()
