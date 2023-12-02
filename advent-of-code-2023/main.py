from day1.day1 import solution_day_1_part_1, solution_day_1_part_2

solution_table = {1: [solution_day_1_part_1, solution_day_1_part_2]}


def print_day_solution(day):
    print(f"--- Day {day} ---")

    for i, solution in enumerate(solution_table[day]):
        print(
            f"  Part {i+1}:",
            solution(open(f"advent-of-code-2023/day{day}/input").read()),
        )

    print("\n")


for day in solution_table:
    print_day_solution(day)
