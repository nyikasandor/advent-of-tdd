import unittest
import os

from schematic import Line


class Test_game(unittest.TestCase):

    def get_test_line_1(self):
        return '467..114..'

    def get_test_line_2(self):
        return '...*....!.'

    def test_can_find_numbers(self):
        line = self.get_test_line_1()
        numbers = Line.find_numbers(line)
        self.assertEqual(numbers[0], (range(0, 3), '467'))
        self.assertEqual(numbers[1], (range(5, 8), '114'))

    def test_can_lookup_no_number(self):
        line = Line(self.get_test_line_1())
        self.assertEqual(line.get_number_in_pos(3), 0)

    def test_can_lookup_number(self):
        line = Line(self.get_test_line_1())
        self.assertEqual(line.get_number_in_pos(1), 467)

    def test_can_find_special_chars_in_line(self):
        line = self.get_test_line_2()
        self.assertEqual(Line.find_special_chars(line), [3, 8])

    def test_can_lookup_multiple_numbers(self):
        line = Line(self.get_test_line_1())
        self.assertEqual(line.get_numbers_in_positions([1, 6, 5]), 467 + 114)


if __name__ == '__main__':
    unittest.main()
