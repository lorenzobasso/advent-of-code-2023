from pathlib import Path
from aoc_2023.day1.day1 import solution_day_1_part_1, solution_day_1_part_2
from aoc_2023.day2.day2 import solution_day_2_part_1

solution_table = {
    1: [solution_day_1_part_1, solution_day_1_part_2],
    2: [solution_day_2_part_1],
}


def print_day_solution(day):
    print(f"--- Day {day} ---")

    for i, solution in enumerate(solution_table[day]):
        print(
            f"  Part {i+1}:",
            solution(open(Path(__file__).parent / f"aoc_2023/day{day}/input").read()),
        )

    print("\n")


for day in solution_table:
    print_day_solution(day)