import unittest
import os

from hand import Hand


class Test_hand(unittest.TestCase):

    def get_hand_pair(self):
        return '42T4K 765'

    def get_hand_two_pair(self):
        return '3KT3K 765'

    def get_hand_three_of_a_kind(self):
        return '3233K 765'

    def get_hand_full_house(self):
        return '32233 765'

    def get_hand_four_of_a_kind(self):
        return '55455 765'

    def get_hand_five_of_a_kind(self):
        return '55555 765'

    def get_hand_hight_cards(self):
        return '23456 765'

    def test_can_create_hand(self):
        hand = Hand(self.get_hand_pair())
        self.assertEqual(hand.bid, 765)
        self.assertEqual(hand.cards, '42T4K')

    def test_can_detect_one_pair(self):
        hand = Hand(self.get_hand_pair())
        self.assertEqual(hand.type, 'one pair')

    def test_can_detect_two_pair(self):
        hand = Hand(self.get_hand_two_pair())
        self.assertEqual(hand.type, 'two pair')

    def test_can_detect_three_of_a_kind(self):
        hand = Hand(self.get_hand_three_of_a_kind())
        self.assertEqual(hand.type, 'three of a kind')

    def test_can_detect_full_house(self):
        hand = Hand(self.get_hand_full_house())
        self.assertEqual(hand.type, 'full house')

    def test_can_detect_four_of_a_kind(self):
        hand = Hand(self.get_hand_four_of_a_kind())
        self.assertEqual(hand.type, 'four of a kind')

    def test_can_detect_five_of_a_kind(self):
        hand = Hand(self.get_hand_five_of_a_kind())
        self.assertEqual(hand.type, 'five of a kind')

    def test_can_detect_high(self):
        hand = Hand(self.get_hand_hight_cards())
        self.assertEqual(hand.type, 'high')

    def test_can_detect_four_joker(self):
        hand = Hand('JJJ6Q 1')
        self.assertEqual(hand.joker_power, 5)

    def test_can_detect_pair_joker(self):
        hand = Hand('J236Q 1')
        self.assertEqual(hand.joker_power, 1)

    def test_can_detect_drill_joker(self):
        hand = Hand('J2J6Q 1')
        self.assertEqual(hand.joker_power, 3)

    def test_can_detect_four_joker_pair(self):
        hand = Hand('J2J66 1')
        self.assertEqual(hand.joker_power, 5)

    def test_can_detect_five_joker_only(self):
        hand = Hand('JJJJJ 1')
        self.assertEqual(hand.joker_power, 6)

    def test_can_detect_drill_one_joker(self):
        hand = Hand('A33J8 1')
        self.assertEqual(hand.joker_power, 3)

    def test_can_detect_full_house_joker(self):
        hand = Hand('TJ99T 1')
        self.assertEqual(hand.joker_power, 4)

    def test_can_detect_five_joker(self):
        hand = Hand('J2J2J 1')
        self.assertEqual(hand.joker_power, 6)

    def test_can_label_strength(self):
        hands = [Hand('KK677 1'),
                 Hand('KTJ2T 2'),]
        Hand.sort_hands(hands)
        self.assertEqual(hands[0].cards, 'KTJ2T')
        self.assertEqual(hands[1].cards, 'KK677')

    def test_can_sort(self):
        hands = [Hand(self.get_hand_hight_cards()),
                 Hand(self.get_hand_five_of_a_kind()),
                 Hand(self.get_hand_three_of_a_kind()),
                 Hand(self.get_hand_four_of_a_kind()),
                 Hand(self.get_hand_full_house()),
                 Hand(self.get_hand_two_pair()),
                 Hand(self.get_hand_pair()),]
        Hand.sort_hands(hands)
        self.assertEqual(hands[0].type, 'high')
        self.assertEqual(hands[6].type, 'five of a kind')

    def test_can_solve_puzzle_1(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_1.txt')
        with open(input_path) as f:
            lines = f.read().splitlines()
        hands = [Hand(line) for line in lines]
        self.assertEqual(Hand.calculate_winnings(hands), 247823654)

    def test_can_solve_puzzle_2(self):
        input_path = os.path.join(os.path.dirname(__file__), 'input_1.txt')
        with open(input_path) as f:
            lines = f.read().splitlines()
        hands = [Hand(line) for line in lines]
        self.assertEqual(Hand.calculate_joker_winnings(hands), 245461700)


if __name__ == '__main__':
    unittest.main()
