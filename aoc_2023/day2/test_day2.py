import pytest
from pathlib import Path

from aoc_2023.day2.day2 import (
    parse_game,
    is_game_possible,
    get_cube_minimum,
    get_set_power,
    solution_day_2_part_1,
    solution_day_2_part_2,
)


@pytest.mark.parametrize(
    "input,game_number,sets",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            1,
            [(4, 0, 3), (1, 2, 6), (0, 2, 0)],
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            2,
            [(0, 2, 1), (1, 3, 4), (0, 1, 1)],
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            3,
            [(20, 8, 6), (4, 13, 5), (1, 5, 0)],
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            4,
            [(3, 1, 6), (6, 3, 0), (14, 3, 15)],
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            5,
            [(6, 3, 1), (1, 2, 2)],
        ),
    ],
)
def test__parse_game(input, game_number, sets):
    assert parse_game(input) == (game_number, sets)


@pytest.mark.parametrize(
    "input,expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            False,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            False,
        ),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True),
    ],
)
def test__is_game_possible(input, expected):
    assert is_game_possible(input, 12, 13, 14) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (4, 2, 6)),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (1, 3, 4)),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            (20, 13, 6),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            (14, 3, 15),
        ),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", (6, 3, 2)),
    ],
)
def test__get_cube_minimum(input, expected):
    assert get_cube_minimum(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            1560,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            630,
        ),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36),
    ],
)
def test__get_set_power(input, expected):
    assert get_set_power(get_cube_minimum(input)) == expected


def test__solution_day_2_part_1():
    input_string = """
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """
    assert solution_day_2_part_1(input_string) == 8


def test__solution_day_2_part_2():
    input_string = """
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """
    assert solution_day_2_part_2(input_string) == 2286


def test__regression():
    filename = Path(__file__).parent / "input"
    assert solution_day_2_part_1(open(filename).read()) == 1734
    assert solution_day_2_part_2(open(filename).read()) == 70387
