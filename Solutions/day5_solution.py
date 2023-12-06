import re


def item_in_list(item, list):
    try:
        list[item]
        return True
    except Exception as E:
        return False


def day_5(sample_file_path, full_file_path):
    seeds = []
    soils = []
    ferts = []
    waters = []
    lights = []
    temps = []
    humidity = []
    locations = []

    map_map = {
        1: seeds,
        2: soils,
        3: ferts,
        4: waters,
        5: lights,
        6: temps,
        7: humidity,
        8: locations
    }
    seed_locations = []
    with open(sample_file_path, 'r') as sample_f:
        seeds_line = sample_f.readline().strip()
        seeds_list = re.split(r': | ', seeds_line)[1:]
        seeds_list = [int(i) for i in seeds_list]  # turn into ints
        map_count = 0
        for line in sample_f:
            if line != "\n":
                if ":" not in line:
                    # We need to do something with these map numbers
                    line_items = line.strip().split(" ")
                    for i in range(int(line_items[1]), int(line_items[1])+int(line_items[2])):
                        map_map[map_count].append(i)
                    for i in range(int(line_items[0]), int(line_items[0])+int(line_items[2])):
                        map_map[map_count+1].append(i)
                    # print(map_map[map_count])
                    # print(map_map[map_count+1])
                # else:
                    # Name of map, can pass
                    # pass
            else:
                # empty line found, increase map count
                map_count += 1
        print(seeds_list)
        # for line in sample_f:
        #     line = line.strip()
        #     split_line = re.split(r': | \| ', line)

    for seed in seeds_list:
        next_num = seed
        for i in range(1, 8):
            # try:
                # print(map_count[i])
            print(f"next_num: {next_num}")
            print(f"cur map: {map_map[i]}")
            print(f"cur map index of next_num: {map_map[i].index(next_num)}")
            next_num_index = map_map[i].index(next_num)
            print(f"next map: {map_map[i+1]}")
            print(f"next map value: {map_map[i+1][next_num_index]}")
            if item_in_list(map_map[i+1][next_num_index], map_map[i+1]):
                next_num = map_map[i+1][next_num_index]
            print(f"next_num: {next_num}")
            # except Exception as E:
                # item isn't found, maps to itself
                # print(E)

        # 79
        seed_locations.append(next_num)
        print(seed_locations)

    return min(seed_locations)
