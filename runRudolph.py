import sys
from Solutions.day1_solution import day_1

day_map = {
    "1": day_1
}


def run_aoc_day():
    day_to_run = sys.argv[1]
    sample = f"Resources/day_{day_to_run}/sample_part2.txt"
    full = f"Resources/day_{day_to_run}/full.txt"

    try:
        result = day_map[day_to_run](sample, full)
        print(result)
    except KeyError:
        print("check your day contains a valid solution and try again. :(")


if __name__ == "__main__":
    run_aoc_day()
