import re

from aoc_2023.common.utils import parse_lines


def parse_game(game):
    def match(string, color):
        (value,) = re.findall(rf"(\d+) {color}", string) or [0]
        return int(value)

    (game_number,) = re.findall(r"^Game (\d+): .*", game)

    sets = []
    for set in game.split(";"):
        sets.append(
            (
                match(set, "red"),
                match(set, "green"),
                match(set, "blue"),
            )
        )

    return int(game_number), sets


def is_game_possible(game, total_red, total_green, total_blue):
    _, sets = parse_game(game)

    for red, green, blue in sets:
        if red > total_red or green > total_green or blue > total_blue:
            return False

    return True


def get_cube_minimum(game):
    _, sets = parse_game(game)

    return (
        max(red for red, _, _ in sets),
        max(green for _, green, _ in sets),
        max(blue for _, _, blue in sets),
    )


def get_set_power(set):
    red, green, blue = set
    return red * green * blue


def solution_day_2_part_1(text: str):
    return sum(
        parse_game(game)[0]
        for game in parse_lines(text)
        if is_game_possible(game, 12, 13, 14)
    )


def solution_day_2_part_2(text: str):
    return sum(get_set_power(get_cube_minimum(game)) for game in parse_lines(text))
