import re


def day_6(sample_file_path, full_file_path):
    number_of_ways = 1
    with open(full_file_path, 'r') as sample_f:
        time_line = sample_f.readline().strip()
        times = re.split(r': +| +', time_line)

        dist_line = sample_f.readline().strip()
        distances = re.split(r': +| +', dist_line)

    for index in range(1, len(times)):
        dist_to_beat = int(distances[index])
        option_count = 0
        race_time = int(times[index])
        # check scenarios giving higher than best distance
        for ms_hold in range(int(times[index])+1):
            if (ms_hold * race_time) > dist_to_beat:
                option_count += 1
            race_time -= 1
        number_of_ways *= option_count
    return number_of_ways


def day_6_part2(sample_file_path, full_file_path):
    number_of_ways = 1
    race_time = ""
    dist_to_beat = ""
    with open(full_file_path, 'r') as sample_f:
        time_line = sample_f.readline().strip()
        times = re.split(r': +| +', time_line)

        dist_line = sample_f.readline().strip()
        distances = re.split(r': +| +', dist_line)

    for index in range(1, len(times)):
        race_time += times[index]
        dist_to_beat += distances[index]

    race_time = int(race_time)
    dist_to_beat = int(dist_to_beat)
    option_count = 0

    # check scenarios giving higher than best distance
    for ms_hold in range(race_time+1):
        if (ms_hold * race_time) > dist_to_beat:
            option_count += 1
        race_time -= 1
    number_of_ways *= option_count
    return number_of_ways
