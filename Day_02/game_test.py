import unittest
import os

from game import (parse_game,
                  min_cubes,
                  is_game_possible,
                  sum_of_possible_game_ids,

                  power_of_set,
                  sum_of_power_of_sets)


class Test_game(unittest.TestCase):

    def get_game_1_input(self):
        return 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

    def get_game_1(self):
        return (1, [{'blue': 3, 'red': 4},
                    {'red': 1, 'green': 2, 'blue': 6},
                    {'green': 2}])

    def test_can_parse_game(self):
        line = self.get_game_1_input()
        self.assertEqual(parse_game(line), self.get_game_1())

    def test_can_find_min_cubes(self):
        _, turns = self.get_game_1()
        self.assertEqual(min_cubes(turns),
                         {'red': 4, 'green': 2, 'blue': 6})

    def test_can_detect_possible_game(self):
        cubes = {'red': 4, 'green': 2, 'blue': 9}
        _, turns = self.get_game_1()
        self.assertTrue(is_game_possible(turns, cubes))

    def test_can_detect_impossible_game(self):
        cubes = {'red': 4, 'green': 2}
        _, turns = self.get_game_1()
        self.assertFalse(is_game_possible(turns, cubes))

    def test_can_solve_puzzle_1(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_1')
        with open(input_path) as f:
            document = f.read()
        inventory = {'red': 12, 'green': 13, 'blue': 14}
        self.assertEqual(sum_of_possible_game_ids(document, inventory), 2683)

# === Part 2

    def test_can_calculate_zero_power_of_game(self):
        turns = [{'blue': 3, 'red': 4},
                 {'red': 1, 'blue': 6}]
        self.assertEqual(power_of_set(turns), 0)

    def test_can_calculate_non_zero_power_of_game(self):
        _, turns = self.get_game_1()
        self.assertEqual(power_of_set(turns), 48)

    def test_can_solve_puzzle_2(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_1')
        with open(input_path) as f:
            document = f.read()
        self.assertEqual(sum_of_power_of_sets(document), 49710)


if __name__ == '__main__':
    unittest.main()
