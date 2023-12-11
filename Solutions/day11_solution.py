import pandas as pd


def perform_universe_expansion(df):
    # Get column numbers with unique values, aka empty space
    cols = df.columns[df.nunique() == 1]
    # Expand each of those columns into two
    inserted_cols = 0
    for col in cols:
        df.insert(col+inserted_cols, col, df[col], allow_duplicates=True)
        inserted_cols += 1
    df.columns = range(len(df.columns))
    # Get row numbers with unique values, aka empty space
    rows = df[df.nunique(axis=1) == 1].index.tolist()
    for row in rows:
        df.loc[row+.5] = df.iloc[[row]].values[0]
    df = df.sort_index().reset_index(drop=True)
    return df


def understand_universe_expansion(df):
    # Get column numbers with unique values, aka empty space
    cols = df.columns[df.nunique() == 1].tolist()
    print(cols)

    # Get row numbers with unique values, aka empty space
    rows = df[df.nunique(axis=1) == 1].index.tolist()
    print(rows)

    return rows, cols


def day_11(sample_file_path, full_file_path):
    smallest_paths_sum = 0

    with open(full_file_path, 'r') as sample_f:
        data = []
        for line in sample_f:
            line = line.strip()
            line_data = list(line)
            data.append(line_data)
    universe = pd.DataFrame(data)
    universe = perform_universe_expansion(universe)

    galaxies = universe[universe.isin(['#'])].stack().index.values

    for galaxy_index in range(len(galaxies) - 1):
        for neighbor_galaxy_index in range(galaxy_index+1, len(galaxies)):
            # print(f"Comparing galaxy {galaxy_index} at {galaxies[galaxy_index]} to neighboring galaxy {neighbor_galaxy_index} at {galaxies[neighbor_galaxy_index]}")
            smallest_path = abs(galaxies[galaxy_index][0]-galaxies[neighbor_galaxy_index][0]) + abs(galaxies[galaxy_index][1]-galaxies[neighbor_galaxy_index][1])
            smallest_paths_sum += smallest_path
    return smallest_paths_sum


def day_11_part2(sample_file_path, full_file_path):
    smallest_paths_sum = 0
    universe_multiplier = 1000000

    with open(full_file_path, 'r') as sample_f:
        data = []
        for line in sample_f:
            line = line.strip()
            line_data = list(line)
            data.append(line_data)
    universe = pd.DataFrame(data)
    rows, cols = understand_universe_expansion(universe)

    galaxies = universe[universe.isin(['#'])].stack().index.values

    for galaxy_index in range(len(galaxies) - 1):
        for neighbor_galaxy_index in range(galaxy_index+1, len(galaxies)):
            smallest_path = abs(galaxies[galaxy_index][0]-galaxies[neighbor_galaxy_index][0]) + abs(galaxies[galaxy_index][1]-galaxies[neighbor_galaxy_index][1])
            num_expanses_crossed = 0
            for row_num in rows:
                if row_num in range(min(galaxies[galaxy_index][0], galaxies[neighbor_galaxy_index][0]), max(galaxies[galaxy_index][0], galaxies[neighbor_galaxy_index][0])):
                    num_expanses_crossed += 1
            for col_num in cols:
                if col_num in range(min(galaxies[galaxy_index][1], galaxies[neighbor_galaxy_index][1]), max(galaxies[galaxy_index][1], galaxies[neighbor_galaxy_index][1])):
                    num_expanses_crossed += 1
            smallest_paths_sum += (smallest_path - num_expanses_crossed + (num_expanses_crossed * universe_multiplier))
    return smallest_paths_sum
