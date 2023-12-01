def day_1_part1(sample_file_path, full_file_path):
    valid_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    total_sum = 0
    with open(full_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()
            temp = list(line)
            for i in range(len(temp)):
                if temp[i] in valid_nums:
                    first = temp[i]
                    break
            for i in reversed(range(len(temp))):
                if temp[i] in valid_nums:
                    last = temp[i]
                    break
            value = int(first+last)
            total_sum += value
    return total_sum


def day_1(sample_file_path, full_file_path):
    valid_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        "5": '5',
        "6": '6',
        "7": '7',
        "8": '8',
        "9": '9'

    }
    place_map_first = {
        'one': None,
        'two': None,
        'three': None,
        'four': None,
        "five": None,
        "six": None,
        "seven": None,
        "eight": None,
        "nine": None,
        '1': None,
        '2': None,
        '3': None,
        '4': None,
        '5': None,
        '6': None,
        '7': None,
        '8': None,
        '9': None
    }

    place_map_last = {
        'one': None,
        'two': None,
        'three': None,
        'four': None,
        "five": None,
        "six": None,
        "seven": None,
        "eight": None,
        "nine": None,
        '1': None,
        '2': None,
        '3': None,
        '4': None,
        '5': None,
        '6': None,
        '7': None,
        '8': None,
        '9': None
    }

    total_sum = 0
    with open(full_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()

            # Figure out where the first of each thing I care about starts
            for key in num_map.keys():
                place_map_first[key] = line.find(key)
            print(line)
            place_map_first_non_neg = dict(filter(lambda k: k[1] >= 0.0, place_map_first.items()))

            # Figure out where the last of each thing I care about starts
            for key in num_map.keys():
                place_map_last[key] = line.rfind(key)
            print(line)
            place_map_last_non_neg = dict(filter(lambda k: k[1] >= 0.0, place_map_last.items()))

            # replace values to get all digits
            if place_map_first_non_neg != {}:
                min_key = min(place_map_first_non_neg, key=place_map_first_non_neg.get)
                line = line.replace(min_key, num_map[min_key], 1)
            if place_map_last_non_neg != {}:
                max_key = max(place_map_last_non_neg, key=place_map_last_non_neg.get)
                line = line.replace(max_key, num_map[max_key], -1)
                print(line)

            temp = list(line)
            # Grab values of first and last valid digits
            for i in range(len(temp)):
                if temp[i] in valid_nums:
                    first = temp[i]
                    break
            for i in reversed(range(len(temp))):
                if temp[i] in valid_nums:
                    last = temp[i]
                    break

            value = int(first+last)
            print(value)
            total_sum += value

    return total_sum
