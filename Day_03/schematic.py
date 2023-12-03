import re


class Line:

    def __init__(self, line) -> None:
        self.numbers = Line.find_numbers(line)

    @classmethod
    def find_special_chars(cls, line):
        pattern = r'[^\d.]'
        return [match.span()[0] for match in re.finditer(pattern, line)]

    @classmethod
    def find_numbers(cls, line):
        pattern = r'\d+'
        return [(range(*match.span()), match.group())
                for match in re.finditer(pattern, line)]

    def get_number_in_pos(self, pos):
        for span, number in self.numbers:
            if pos in span:
                self.numbers.remove((span, number))
                return int(number)
        return 0

    def get_numbers_in_positions(self, positions):
        return sum(self.get_number_in_pos(pos) for pos in positions)
