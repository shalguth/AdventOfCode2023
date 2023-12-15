import pandas as pd


def day_12(sample_file_path, full_file_path):
    smallest_paths_sum = 0

    with open(sample_file_path, 'r') as sample_f:
        data = []
        for line in sample_f:
            line = line.strip()
            line_data = list(line)
            data.append(line_data)
    universe = pd.DataFrame(data)
    # universe = perform_universe_expansion(universe)

    galaxies = universe[universe.isin(['#'])].stack().index.values

    for galaxy_index in range(len(galaxies) - 1):
        for neighbor_galaxy_index in range(galaxy_index+1, len(galaxies)):
            # print(f"Comparing galaxy {galaxy_index} at {galaxies[galaxy_index]} to neighboring galaxy {neighbor_galaxy_index} at {galaxies[neighbor_galaxy_index]}")
            smallest_path = abs(galaxies[galaxy_index][0]-galaxies[neighbor_galaxy_index][0]) + abs(galaxies[galaxy_index][1]-galaxies[neighbor_galaxy_index][1])
            smallest_paths_sum += smallest_path
    return smallest_paths_sum


# def day_12_part2(sample_file_path, full_file_path):
#     smallest_paths_sum = 0
#     universe_multiplier = 1000000
#
#     with open(full_file_path, 'r') as sample_f:
#         data = []
#         for line in sample_f:
#             line = line.strip()
#             line_data = list(line)
#             data.append(line_data)
#     universe = pd.DataFrame(data)
#     rows, cols = understand_universe_expansion(universe)
#
#     galaxies = universe[universe.isin(['#'])].stack().index.values
#
#     for galaxy_index in range(len(galaxies) - 1):
#         for neighbor_galaxy_index in range(galaxy_index+1, len(galaxies)):
#             smallest_path = abs(galaxies[galaxy_index][0]-galaxies[neighbor_galaxy_index][0]) + abs(galaxies[galaxy_index][1]-galaxies[neighbor_galaxy_index][1])
#             num_expanses_crossed = 0
#             for row_num in rows:
#                 if row_num in range(min(galaxies[galaxy_index][0], galaxies[neighbor_galaxy_index][0]), max(galaxies[galaxy_index][0], galaxies[neighbor_galaxy_index][0])):
#                     num_expanses_crossed += 1
#             for col_num in cols:
#                 if col_num in range(min(galaxies[galaxy_index][1], galaxies[neighbor_galaxy_index][1]), max(galaxies[galaxy_index][1], galaxies[neighbor_galaxy_index][1])):
#                     num_expanses_crossed += 1
#             smallest_paths_sum += (smallest_path - num_expanses_crossed + (num_expanses_crossed * universe_multiplier))
#     return smallest_paths_sum
