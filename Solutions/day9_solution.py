import re
from anytree import Node

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild=None

def day_9(sample_file_path, full_file_path):
    histories_sum = 0
    node_lists = []
    with open(sample_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()
            first_round = line.split(" ")
            first_round_ints = [int(i) for i in first_round]

            for index, value in enumerate(first_round_ints):
                cur_node = BinaryTreeNode(value)
                child_node = BinaryTreeNode(cur_node.data - prev_node.data)
                if index == 0:
                    cur_node = BinaryTreeNode(first_round_ints[0])
                    node_lists.append([cur_node])
                elif index == 1:
                    # first item, only right child
                    prev_node.rightChild = child_node
                    cur_node.leftChild = child_node
                    node_lists[0].append(cur_node)
                    node_lists.append([child_node])
                elif index == len(first_round)-1:
                    # last round, only left child
                    prev_node.rightChild = child_node
                    node_lists[0].append(cur_node)
                    node_lists[1].append(child_node)
                else:
                    prev_node.rightChild = child_node
                    cur_node.leftChild = child_node
                    node_lists[0].append(cur_node)
                    node_lists[1].append(child_node)
                prev_node = cur_node


    # for index in range(1, len(times)):
    #     dist_to_beat = int(distances[index])
    #     option_count = 0
    #     race_time = int(times[index])
    #     # check scenarios giving higher than best distance
    #     for ms_hold in range(int(times[index])+1):
    #         if (ms_hold * race_time) > dist_to_beat:
    #             option_count += 1
    #         race_time -= 1
    #     number_of_ways *= option_count
    return histories_sum


# def day_6_part2(sample_file_path, full_file_path):
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
