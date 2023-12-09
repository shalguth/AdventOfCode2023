def find_next_number(listed_numbers):
    differences = []
    for index in range(1, len(listed_numbers)):
        differences.append(listed_numbers[index] - listed_numbers[index-1])
    if differences.count(differences[0]) == len(differences):
        # Found end / base case
        return differences[-1]
    return differences[-1] + find_next_number(differences)


def find_previous_number(listed_numbers):
    differences = []
    for index in reversed(range(1, len(listed_numbers))):
        differences.insert(0, listed_numbers[index] - listed_numbers[index-1])
    if differences.count(differences[0]) == len(differences):
        # Found end / base case
        return differences[0]
    return differences[0] - find_previous_number(differences)


def day_9(sample_file_path, full_file_path):
    histories_sum = 0
    with open(full_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()
            first_round = line.split(" ")
            first_round_ints = [int(i) for i in first_round]
            next_number_difference = find_next_number(first_round_ints)
            histories_sum += (next_number_difference + first_round_ints[-1])
    return histories_sum


def day_9_part2(sample_file_path, full_file_path):
    histories_sum = 0
    with open(full_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()
            first_round = line.split(" ")
            first_round_ints = [int(i) for i in first_round]
            prev_number_difference = find_previous_number(first_round_ints)
            histories_sum += (first_round_ints[0] - prev_number_difference)
    return histories_sum
