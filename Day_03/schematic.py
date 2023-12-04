import re


class Line:

    def __init__(self, line) -> None:
        self.text = line
        self.numbers = Line.find_numbers(line)
        self.special_chars = Line.find_special_chars(line)
        self.gears = Line.find_gears(line)

    @classmethod
    def find_special_chars(cls, line):
        pattern = r'[^\d.]'
        return [match.span()[0] for match in re.finditer(pattern, line)]

    @classmethod
    def find_numbers(cls, line):
        pattern = r'\d+'
        return [(range(*match.span()), match.group())
                for match in re.finditer(pattern, line)]

    @classmethod
    def add_up(cls, lines, extraction_method):
        sum = 0
        adj = [Line(''), Line('')]
        for line in lines:
            sum += extraction_method(adj[1], [adj[0], line])
            adj.append(line)
            adj.pop(0)
        return sum

    @classmethod
    def add_up_schematic(cls, lines):
        return cls.add_up(lines, Line.value_of_line)

    @classmethod
    def add_up_gears(cls, lines):
        return cls.add_up(lines, Line.gear_ratios)

    @classmethod
    def find_gears(cls, line):
        return [match.span()[0] for match in re.finditer(r'\*', line)]

    def gear_ratios(self, adjacent_lines):
        sum = 0
        for gear in self.gears:
            numbers = []
            for line in [adjacent_lines[0], self, adjacent_lines[1]]:
                for idx in [gear - 1, gear, gear + 1]:
                    number = line.get_numbers_in_position(idx)
                    if number != 0:
                        numbers.append(number)
            if len(numbers) == 2:
                sum += numbers[0] * numbers[1]
        return sum

    def value_of_line(self, adjacent_lines):
        value = 0
        for special_char in self.special_chars:
            for line in [*adjacent_lines, self]:
                value += sum([line.get_numbers_in_position(pos) for pos
                              in [special_char - 1, special_char,
                                  special_char + 1]])
        return value

    def fetch_numbers_in_position(self, pos):
        for span, number in self.numbers:
            if pos in span:
                return int(number)
        return 0

    def get_numbers_in_position(self, pos):
        for span, number in self.numbers:
            if pos in span:
                self.numbers.remove((span, number))
                return int(number)
        return 0

    def get_numbers_in_positions(self, positions):
        return 
