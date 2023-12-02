from aoc_2023.common.utils import parse_lines

word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
    **{str(i): str(i) for i in range(10)},
}


def get_calibration_values(decorated):
    digits = [c for c in decorated if c.isnumeric()]
    return int(digits[0] + digits[-1])


def get_improved_calibration_values(decorated):
    digits = []

    for i in range(len(decorated)):
        options = {d for w, d in word_to_digit.items() if decorated[i:].startswith(w)}
        if options:
            digits.append(options.pop())

    return int(digits[0] + digits[-1])


def solution_day_1_part_1(text: str):
    return sum(get_calibration_values(line) for line in parse_lines(text))


def solution_day_1_part_2(text: str):
    return sum(get_improved_calibration_values(line) for line in parse_lines(text))
