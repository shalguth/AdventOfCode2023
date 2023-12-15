def hash_algo(char, beg_value):
    ascii_char_val = int(ord(char))
    ascii_char_val += beg_value
    return (int(ascii_char_val) * 17) % 256


def calculate_focusing_power(boxes, focal_lengths):
    focusing_power = 0
    for box_key in boxes:
        for lens_index in range(len(boxes[box_key])):
            lens_power = (1+box_key)*(lens_index+1)*focal_lengths[boxes[box_key][lens_index]]
            focusing_power += lens_power
    return focusing_power


def day_15(sample_file_path, full_file_path):
    hash_sum = 0

    with open(full_file_path, 'r') as sample_f:
        data = []
        for line in sample_f:
            line = line.strip()
            data = line.split(',')

    for string in data:
        beg_value = 0
        for char in string:
            beg_value = hash_algo(char, beg_value)
        hash_sum += beg_value

    return hash_sum


def day_15_part2(sample_file_path, full_file_path):
    with open(full_file_path, 'r') as sample_f:
        data = []
        for line in sample_f:
            line = line.strip()
            data = line.split(',')

    boxes = {}
    focal_lengths = {}
    for string in data:
        box_num = 0
        if '-' in string:
            label = string.split('-')[0]
            for char in label:
                box_num = hash_algo(char, box_num)
            if box_num in boxes.keys() and label in boxes[box_num]:
                # only action is taken to remove things if this exists
                boxes[box_num].remove(label)
                del focal_lengths[label]
        elif '=' in string:
            sep_string = string.split('=')
            label = sep_string[0]
            for char in label:
                box_num = hash_algo(char, box_num)
            focal_length = int(sep_string[1])

            if box_num not in boxes.keys():
                boxes[box_num] = []
            if label not in boxes[box_num]:
                boxes[box_num].append(label)
            focal_lengths[label] = focal_length
    return calculate_focusing_power(boxes, focal_lengths)
