import re

from aoc_2023.common.utils import parse_lines


def get_winning_numbers(line: str):
    ((winning_text, my_numbers_text),) = re.findall(
        r"Card\s+\d+:([\d\s]+)\|([\d\s]+)", line
    )

    winning = {int(n.group()) for n in re.finditer(r"\d+", winning_text)}
    my_numbers = {int(n.group()) for n in re.finditer(r"\d+", my_numbers_text)}

    return winning.intersection(my_numbers)


def get_card_score(line: str):
    winning = get_winning_numbers(line)

    return 2 ** (len(winning) - 1) if winning else 0


def get_better_card_scores(text: str):
    lines = parse_lines(text)
    winnings = [len(get_winning_numbers(line)) for line in lines]

    total = [1 for _ in lines]
    for i, count in enumerate(winnings):
        for j in range(i + 1, i + count + 1):
            total[j] += 1

    return total


def solution_day_4_part_1(text: str):
    lines = parse_lines(text)

    return sum(map(get_card_score, lines))


def solution_day_4_part_2(text: str):
    return 0
