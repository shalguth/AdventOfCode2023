import re
from itertools import cycle


def day_8(sample_file_path, full_file_path):
    steps = 0
    cur_node = "AAA"
    nodes = {}
    with open(full_file_path, 'r') as sample_f:
        directions_string = sample_f.readline().strip()
        directions_string_conv = directions_string.replace('L', '0').replace('R', '1')
        directions = list(directions_string_conv)
        directions_ints = [int(direction) for direction in directions]
        directions_ints_circle = cycle(directions_ints)

        sample_f.readline()  # Blank line

        for line in sample_f:
            line = re.split(r' = \(|, ', line.strip()[:-1])
            nodes[line[0]] = (line[1], line[2])

    for direction in directions_ints_circle:
        if cur_node != 'ZZZ':
            steps += 1
            cur_node = nodes[cur_node][direction]
        else:
            return steps


def day_8_part2(sample_file_path, full_file_path):
    steps = 0
    cur_nodes = []
    nodes = {}
    with open(full_file_path, 'r') as sample_f:
        directions_string = sample_f.readline().strip()
        directions_string_conv = directions_string.replace('L', '0').replace('R', '1')
        directions = list(directions_string_conv)
        directions_ints = [int(direction) for direction in directions]
        directions_ints_circle = cycle(directions_ints)

        sample_f.readline()  # Blank line

        for line in sample_f:
            line = re.split(r' = \(|, ', line.strip()[:-1])
            nodes[line[0]] = (line[1], line[2])
    for key in nodes.keys():
        if key[2] == 'A':
            cur_nodes.append(key)
    for direction in directions_ints_circle:
        if all(map(lambda x: x[2] == 'Z', cur_nodes)):
            print("BOOM")
            return steps
        else:
            # print(steps)
            steps += 1
            for index, node in enumerate(cur_nodes):
                # print(node, index)
                # print(nodes[node])
                cur_nodes[index] = nodes[node][direction]
            # cur_nodes = [nodes[node][direction] for index, node in enumerate(cur_nodes)]
    # return 0


def day_8_part2_take2(sample_file_path, full_file_path):
    steps = 0
    cur_nodes = []
    nodes = {}
    with open(sample_file_path, 'r') as sample_f:
        directions_string = sample_f.readline().strip()
        directions_string_conv = directions_string.replace('L', '0').replace('R', '1')
        directions = list(directions_string_conv)
        directions_ints = [int(direction) for direction in directions]
        directions_ints_circle = cycle(directions_ints)

        sample_f.readline()  # Blank line

        for line in sample_f:
            line = re.split(r' = \(|, ', line.strip()[:-1])
            nodes[line[0]] = (line[1], line[2])
    for key in nodes.keys():
        if key[2] == 'A':
            cur_nodes.append(key)
    for direction in directions_ints_circle:
        if all(map(lambda x: x[2] == 'Z', cur_nodes)):
            print("BOOM")
            return steps
        else:
            # print(steps)
            steps += 1
            for index, node in enumerate(cur_nodes):
                # print(node, index)
                # print(nodes[node])
                cur_nodes[index] = nodes[node][direction]
            # cur_nodes = [nodes[node][direction] for index, node in enumerate(cur_nodes)]
    # return 0
