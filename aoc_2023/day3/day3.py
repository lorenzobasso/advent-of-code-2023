import re

from aoc_2023.common.utils import parse_lines


def get_adjacent_cells(text, y, x_start, x_end):
    lines = parse_lines(text)
    start = max(x_start - 1, 0)
    end = min(x_end + 1, len(lines[0]))

    adjacent = []

    if y:
        adjacent.extend(lines[y - 1][start:end])

    if y + 1 < len(lines):
        adjacent.extend(lines[y + 1][start:end])

    if x_start - 1 >= 0:
        adjacent.append(lines[y][x_start - 1])

    if x_end < len(lines[0]):
        adjacent.append(lines[y][x_end])

    return {c for c in adjacent if c != "."}


def get_numbers_and_adjacent(text):
    lines = parse_lines(text)
    coordinates = []

    for y, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            coordinates.append((int(m.group()), get_adjacent_cells(text, y, *m.span())))

    return [num for num, adj in coordinates if adj]


def get_gears(text):
    gears = []
    lines = parse_lines(text)

    def _adjacent_numbers(pos, x):
        return [
            int(num.group())
            for num in re.finditer(r"\d+", lines[pos])
            if x in range(num.span()[0] - 1, num.span()[1] + 1)
        ]

    for y, line in enumerate(lines):
        for m in re.finditer(r"[*]", line):
            x, _ = m.span()
            ratios = set(_adjacent_numbers(y, x))

            if y:
                ratios.update(_adjacent_numbers(y - 1, x))

            if y + 1 < len(lines):
                ratios.update(_adjacent_numbers(y + 1, x))

            if len(ratios) > 1:
                gears.append(ratios)

    return gears


def solution_day_3_part_1(text: str):
    return sum(get_numbers_and_adjacent(text))


def solution_day_3_part_2(text: str):
    ratio_sum = 0
    gears = get_gears(text)

    for gear in gears:
        ratio = 1
        for number in gear:
            ratio *= number
        ratio_sum += ratio

    return ratio_sum
