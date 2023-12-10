class Hand:

    __power = {
        'high': 0,
        'one pair': 1,
        'two pair': 2,
        'three of a kind': 3,
        'full house': 4,
        'four of a kind': 5,
        'five of a kind': 6,
    }

    __cards_joker = list(reversed(
            ['A', 'K', 'Q', 'T',
             '9', '8', '7', '6', '5',
             '4', '3', '2', 'J']))

    __cards = list(reversed(
                ['A', 'K', 'Q', 'J', 'T',
                 '9', '8', '7', '6', '5',
                 '4', '3', '2']))

    __card_value = dict(zip(__cards,
                            range(len(__cards))))

    __card_joker_value = dict(zip(__cards_joker,
                                  range(len(__cards_joker))))

    def __init__(self, input_line) -> None:
        self.cards, bid_ = input_line.split()
        self.bid = int(bid_)
        self.type = self.calculate_type()
        self.power = Hand.__power[self.type]
        self.decoded_cards = self.decode_cards()
        self.joker_power = self.calculate_joker_power()
        self.decoded_joker_cards = self.decode_joker_cards()

    def __repr__(self) -> str:
        return f'{self.cards}, {self.joker_power}'

    def calculate_joker_power(self):
        joker_count = self.cards.count('J')
        joker_gain = joker_count
        if self.power < 4 and joker_count + self.power > 3:
            # skip full house score
            joker_gain += 1
        if joker_count > 2 and self.power < 4:
            return 5
        if joker_count == 1 and self.power == 1:
            # skip two pair
            return 3
        if joker_count == 1 and self.power == 2:
            # full house with joker
            return 4
        return min(self.power + joker_gain, 6)

    def calculate_type(self):
        unique_cards = len(set(self.cards))
        if 5 == unique_cards:
            return 'high'
        if 4 == unique_cards:
            return 'one pair'
        if (3 == unique_cards and
            (self.cards.count(self.cards[0]) == 3 or
             self.cards.count(self.cards[1]) == 3 or
             self.cards.count(self.cards[2]) == 3)):
            return 'three of a kind'
        if 3 == unique_cards:
            return 'two pair'
        if (2 == unique_cards and (
             self.cards.count(self.cards[1]) == 4 or
             self.cards.count(self.cards[2]) == 4)):
            return 'four of a kind'
        if 2 == unique_cards:
            return 'full house'
        if 1 == unique_cards:
            return 'five of a kind'

    def decode_cards(self):
        return [Hand.__card_value[card] for card in self.cards]

    def decode_joker_cards(self):
        return [Hand.__card_joker_value[card] for card in self.cards]

    @classmethod
    def sort_hands(cls, hands):
        hands.sort(key=lambda hand: (hand.power,
                                     *hand.decoded_cards))

    @classmethod
    def sort_joker_hands(cls, hands):
        hands.sort(key=lambda hand: (hand.joker_power,
                                     *hand.decoded_joker_cards))

    @classmethod
    def calculate_winnings(cls, hands):
        Hand.sort_hands(hands)
        return sum(rank * hand.bid
                   for rank, hand in enumerate(hands, 1))

    @classmethod
    def calculate_joker_winnings(cls, hands):
        Hand.sort_joker_hands(hands)
        return sum(rank * hand.bid
                   for rank, hand in enumerate(hands, 1))
