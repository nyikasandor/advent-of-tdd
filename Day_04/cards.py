class Card:

    def __init__(self, input_line) -> None:
        self.card_id, numbers = input_line.split(':')
        left, right = numbers.split('|')
        self.left = {int(number) for number in left.split()}
        self.right = {int(number) for number in right.split()}
        self.copies = 1

    def get_hits(self):
        return len(self.left & self.right)

    def get_points(self):
        return int(2 ** (self.get_hits()-1))

    def add_copies(self, count):
        self.copies += count

    @classmethod
    def win_copies(cls, cards):
        for idx, current_card in enumerate(cards):
            for win in range(idx + 1, current_card.get_hits() + idx + 1):
                cards[win].add_copies(current_card.copies)
