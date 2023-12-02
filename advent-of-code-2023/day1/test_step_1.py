import pytest
from .day1 import (
    get_calibration_values,
    get_improved_calibration_values,
    solution_day_1_part_1,
    solution_day_1_part_2,
)


@pytest.mark.parametrize(
    "input,expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test__get_calibration_values(input, expected):
    assert get_calibration_values(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test__get_improved_calibration_values(input, expected):
    assert get_improved_calibration_values(input) == expected


def test__solution_day_1_part_1():
    input_string = """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """
    assert solution_day_1_part_1(input_string) == 142


def test__solution_day_1_part_2():
    input_string = """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
    """
    assert solution_day_1_part_2(input_string) == 281
