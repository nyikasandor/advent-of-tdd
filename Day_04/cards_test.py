import unittest
import os

from cards import Card


class Test_game(unittest.TestCase):

    def get_card_1_input(self):
        return 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'

    def get_card_1(self):
        return Card(self.get_card_1_input())

    def test_can_read_card(self):
        card = Card(self.get_card_1_input())
        self.assertEqual(card.left, {41, 48, 83, 86, 17})
        self.assertEqual(card.right, {83, 86,  6, 31, 17, 9, 48, 53})

    def test_can_count_hits(self):
        card = self.get_card_1()
        self.assertEqual(card.get_hits(), 4)

    def test_can_count_point(self):
        card = self.get_card_1()
        self.assertEqual(card.get_points(), 8)

    def test_can_solve_puzzle_1(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_1.txt')
        with open(input_path) as f:
            lines = f.read().splitlines()
        pile_worth = sum((Card(line).get_points() for line in lines))
        self.assertEqual(pile_worth, 22674)

    def get_first_6_cards(self):
        return [
            Card('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'),
            Card('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'),
            Card('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'),
            Card('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'),
            Card('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'),
            Card('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'),]

    def test_can_store_multiple_cards(self):
        card = self.get_card_1()
        card.add_copies(3)
        self.assertEqual(card.copies, 4)

    def test_can_win_copies(self):
        cards = self.get_first_6_cards()
        Card.win_copies(cards)
        for card, solution in zip(cards, [1, 2, 4, 8, 14, 1]):
            self.assertEqual(card.copies, solution)

    def test_can_solve_puzzle_2(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_1.txt')
        with open(input_path) as f:
            lines = f.read().splitlines()
        cards = [Card(line) for line in lines]
        Card.win_copies(cards)
        total_scratchcards = sum((card.copies for card in cards))
        self.assertEqual(total_scratchcards, 5747443)


if __name__ == '__main__':
    unittest.main()
