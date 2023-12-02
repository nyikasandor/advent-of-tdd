import string


def find_first_digit(line):
    return next((char for char in line if char.isdecimal()))


def find_last_digit(line):
    return find_first_digit(line[::-1])


def form_two_digit(line):
    return find_first_digit(line) + find_last_digit(line)


def add_up_multiple_line(lines):
    return sum(int(form_two_digit(line)) for line in lines.splitlines())

# === Part 2


digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
          'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
          **dict(zip(string.digits, range(len(string.digits))))}


def find_first_digit_allow_spelled(line):
    for start_at in range(len(line)):
        for digit, value in digits.items():
            if line[start_at:].startswith(digit):
                return value


def find_last_digit_allow_spelled(line):
    for end_at in range(len(line), 0, -1):
        for digit, value in digits.items():
            if line[0: end_at].endswith(digit):
                return value


def form_two_digit_allow_spelled(line):
    return (find_first_digit_allow_spelled(line) * 10
            + find_last_digit_allow_spelled(line))


def add_up_multiple_line_allow_spelled(lines):
    return sum(form_two_digit_allow_spelled(line)
               for line in lines.splitlines())
