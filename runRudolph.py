import sys
from Solutions.day1_solution import day_1
from Solutions.day2_solution import day_2

day_map = {
    "1": day_1,
    "2": day_2
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
