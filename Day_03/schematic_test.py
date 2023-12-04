import unittest
import os

from schematic import Line


class Test_game(unittest.TestCase):

    def get_test_line_1(self):
        return '467..114..'

    def get_test_line_2(self):
        return '...*....!.'

    def get_test_line_3(self):
        return '..10....!.'

    def test_can_find_numbers(self):
        line = self.get_test_line_1()
        numbers = Line.find_numbers(line)
        self.assertEqual(numbers[0], (range(0, 3), '467'))
        self.assertEqual(numbers[1], (range(5, 8), '114'))

    def test_can_lookup_no_number(self):
        line = Line(self.get_test_line_1())
        self.assertEqual(line.get_numbers_in_position(3), 0)

    def test_can_lookup_number(self):
        line = Line(self.get_test_line_1())
        self.assertEqual(line.get_numbers_in_position(1), 467)

    def test_can_find_special_chars_in_line(self):
        line = self.get_test_line_2()
        self.assertEqual(Line.find_special_chars(line), [3, 8])

    def test_can_find_value_of_lines(self):
        adjacent_lines = [Line(self.get_test_line_1())]
        line = Line(self.get_test_line_2())
        self.assertEqual(line.value_of_line(adjacent_lines), 467 + 114)

    def test_can_solve_puzzle_1(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_1.txt')
        with open(input_path) as f:
            document = f.read()
        lines = [Line(line) for line in document.split('\n')]
        self.assertEqual(Line.add_up_schematic(lines), 559667)

    def test_can_find_gears(self):
        line = self.get_test_line_2()
        self.assertEqual(Line.find_gears(line), [3])

    def test_can_calculate_gear_ratio(self):
        adjacent_lines = [Line(self.get_test_line_1()),
                          Line(self.get_test_line_3())]
        current = Line(self.get_test_line_2())
        self.assertEqual(current.gear_ratios(adjacent_lines), 467 * 10)

    def test_can_solve_puzzle_2(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_1.txt')
        with open(input_path) as f:
            document = f.read()
        lines = [Line(line) for line in document.split('\n')]
        self.assertEqual(Line.add_up_gears(lines), 86841457)


if __name__ == '__main__':
    unittest.main()
