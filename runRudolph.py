import sys
from Solutions.day1_solution import day_1_part1, day_1
from Solutions.day2_solution import day_2
from Solutions.day3_solution import day_3_part1, day_3_part2
from Solutions.day4_solution import day_4_part1, day_4_part2
from Solutions.day6_solution import day_6, day_6_part2
from Solutions.day8_solution import day_8, day_8_part2

day_map = {
    "1": day_1,
    "2": day_2,
    "3": day_3_part2,
    "4": day_4_part2,
    "6": day_6_part2,
    "8": day_8_part2
}


def run_aoc_day():
    day_to_run = sys.argv[1]
    sample = f"Resources/day_{day_to_run}/sample.txt"
    full = f"Resources/day_{day_to_run}/full.txt"

    try:
        result = day_map[day_to_run](sample, full)
        print(result)
    except KeyError:
        print("check your day contains a valid solution and try again. :(")


if __name__ == "__main__":
    run_aoc_day()
