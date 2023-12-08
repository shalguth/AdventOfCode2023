import re


def calculate_score(hand_level, counter, all_hands, start_index=0):
    # print(hand_level.items())
    # max_dict_value_tuple = max(hand_level.items(), key=lambda item: max(item[1][start_index]))
    values = list(hand_level.values())
    single_values = [item[start_index] for item in hand_level.values()]
    # print("VAL")
    # print(values)
    keys = list(hand_level.keys())
    single_value_index = values[single_values.index(max(single_values))]
    # print("WOW")
    # print(values[single_value_index])
    max_dict_value_tuple = (keys[values.index(single_value_index)], hand_level[keys[values.index(single_value_index)]])
    # max_dict_value_tuple = max(hand_level, key=lambda k: max(hand_level[k][start_index]))
    # print("TUP")
    # print(max_dict_value_tuple)
    max_keys = list(filter(lambda k: hand_level[k][start_index] == max_dict_value_tuple[1][start_index], hand_level))
    # print(max_keys)
    # print(hand_level)
    if len(max_keys) == 1:
        # Remove highest order from dictionary
        del hand_level[max_dict_value_tuple[0]]
        # print(max_dict_value_tuple[0], counter)
        all_hands[max_dict_value_tuple[0]] = all_hands[max_dict_value_tuple[0]] * counter
        # print(all_hands)
        counter -= 1
        if len(hand_level) == 0:
            return 1
        else:
            return counter - calculate_score(hand_level, counter, all_hands, start_index-1)
    else:
        work_with_subset = {k: hand_level[k] for k in max_keys}
        return counter - calculate_score(work_with_subset, counter, all_hands, start_index+1)

# Assuming each hand is unique


def day_7(sample_file_path, full_file_path):
    counter = 0
    scoring_map = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    five_of_kind = {}
    four_of_kind = {}
    full_house = {}
    three_of_kind = {}
    two_pair = {}
    one_pair = {}
    high_card = {}
    all_hands = {}

    with open(full_file_path, 'r') as sample_f:
        for line in sample_f.readlines():
            line = line.strip()
            split_line = line.split(' ')

            hand_count = {}
            counter += 1
            for char in split_line[0]:
                if char in hand_count:
                    hand_count[char] += 1
                else:
                    hand_count[char] = 1
            max_count = max(hand_count.values())
            all_hands[split_line[0]] = int(split_line[1])
            if max_count == 5:
                five_of_kind[split_line[0]] = [scoring_map[split_line[0][0]], scoring_map[split_line[0][1]], scoring_map[split_line[0][2]], scoring_map[split_line[0][3]], scoring_map[split_line[0][4]]]
            elif max_count == 4:
                four_of_kind[split_line[0]] = [scoring_map[split_line[0][0]], scoring_map[split_line[0][1]], scoring_map[split_line[0][2]], scoring_map[split_line[0][3]], scoring_map[split_line[0][4]]]
            elif max_count == 3:
                if len(hand_count) == 2:
                    # found a full house
                    full_house[split_line[0]] = [scoring_map[split_line[0][0]], scoring_map[split_line[0][1]], scoring_map[split_line[0][2]], scoring_map[split_line[0][3]], scoring_map[split_line[0][4]]]
                else:
                    # found three of a kind
                    three_of_kind[split_line[0]] = [scoring_map[split_line[0][0]], scoring_map[split_line[0][1]], scoring_map[split_line[0][2]], scoring_map[split_line[0][3]], scoring_map[split_line[0][4]]]
            elif max_count == 2:
                if len(hand_count) == 3:
                    # found two pair
                    two_pair[split_line[0]] = [scoring_map[split_line[0][0]], scoring_map[split_line[0][1]], scoring_map[split_line[0][2]], scoring_map[split_line[0][3]], scoring_map[split_line[0][4]]]
                else:
                    # found one pair
                    one_pair[split_line[0]] = [scoring_map[split_line[0][0]], scoring_map[split_line[0][1]], scoring_map[split_line[0][2]], scoring_map[split_line[0][3]], scoring_map[split_line[0][4]]]
            elif max_count == 1:
                high_card[split_line[0]] = [scoring_map[split_line[0][0]], scoring_map[split_line[0][1]], scoring_map[split_line[0][2]], scoring_map[split_line[0][3]], scoring_map[split_line[0][4]]]

    print(all_hands)
    print(counter)
    if len(five_of_kind) > 0:
        counter = calculate_score(five_of_kind, counter, all_hands)
        print(counter)
    if len(four_of_kind) > 0:
        counter = calculate_score(four_of_kind, counter, all_hands)
        print(counter)
    if len(full_house) > 0:
        counter = calculate_score(full_house, counter, all_hands)
        print(counter)
    if len(three_of_kind) > 0:
        counter = calculate_score(three_of_kind, counter, all_hands)
        print(counter)
    if len(two_pair) > 0:
        counter = calculate_score(two_pair, counter, all_hands)
        print(counter)
    if len(one_pair) > 0:
        counter = calculate_score(one_pair, counter, all_hands)
        print(counter)
    if len(high_card) > 0:
        counter = calculate_score(high_card, counter, all_hands)

    return sum(all_hands.values())


# def day_7_part2(sample_file_path, full_file_path):
#     number_of_ways = 1
#     race_time = ""
#     dist_to_beat = ""
#     with open(full_file_path, 'r') as sample_f:
#         time_line = sample_f.readline().strip()
#         times = re.split(r': +| +', time_line)
#
#         dist_line = sample_f.readline().strip()
#         distances = re.split(r': +| +', dist_line)
#
#     for index in range(1, len(times)):
#         race_time += times[index]
#         dist_to_beat += distances[index]
#
#     race_time = int(race_time)
#     dist_to_beat = int(dist_to_beat)
#     option_count = 0
#
#     # check scenarios giving higher than best distance
#     for ms_hold in range(race_time+1):
#         if (ms_hold * race_time) > dist_to_beat:
#             option_count += 1
#         race_time -= 1
#     number_of_ways *= option_count
#     return number_of_ways
