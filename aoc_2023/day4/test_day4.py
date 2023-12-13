import pytest
from pathlib import Path

from aoc_2023.day4.day4 import (
    get_winning_numbers,
    get_card_score,
    get_better_card_scores,
    solution_day_4_part_1,
    solution_day_4_part_2,
)


example1 = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", {48, 83, 86, 17}),
        ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", {32, 61}),
        ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", {1, 21}),
        ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", {84}),
        ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", set()),
        ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", set()),
    ],
)
def test__get_winning_numbers(text, expected):
    assert get_winning_numbers(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 8),
        ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2),
        ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 2),
        ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1),
        ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0),
        ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0),
    ],
)
def test__get_card_score(text, expected):
    assert get_card_score(text) == expected


def test__better_card_score():
    assert get_better_card_scores(example1) == [1, 2, 4, 8, 14, 1]


def test__solution_day_4_part_1():
    assert solution_day_4_part_1(example1) == 13


# def test__solution_day_4_part_2():
#     assert solution_day_4_part_2(example1) == 467835


def test__regression():
    filename = Path(__file__).parent / "input"
    assert solution_day_4_part_1(open(filename).read()) == 17803
    # assert solution_day_4_part_2(open(filename).read()) == 73201705
