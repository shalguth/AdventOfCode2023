def is_int(possible_int):
    int_found = 1
    try:
        int(possible_int)
    except ValueError:
        int_found = 0
    return int_found


def day_3_part1(sample_file_path, full_file_path):
    schematic = []
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    possible_nums = []
    total_sum = 0
    num_to_ignore = 0
    with open(full_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()
            # '467..114..' -> 467, ., ., 114, ., .
            # print("line")
            # print(line)
            broken_line = list(line)
            # print(broken_line)
            fixed_line = []
            big_num = ""
            # print(broken_line)
            for i in range(len(broken_line)):
                if broken_line[i] in nums:
                    big_num += broken_line[i]
                    # print(big_num)
                else:
                    if big_num != "":
                        fixed_line.extend([big_num]*len(big_num))
                        possible_nums.append(big_num)
                        # print("if")
                        # print(fixed_line)
                        fixed_line.append(broken_line[i])
                        big_num = ""
                    else:
                        fixed_line.append(broken_line[i])
                        # print("else")
                        # print(fixed_line)
                if i == len(broken_line) - 1:
                    # print("last")
                    # last in line, gotta get it on the roster
                    if big_num != "":
                        fixed_line.extend([big_num]*len(big_num))
                        possible_nums.append(big_num)
                        # print("if if")
                        # print(fixed_line)
                        # fixed_line.append(broken_line[i])
                        # print(fixed_line)
                        big_num = ""
                    # else:
                    #     fixed_line.append(broken_line[i])
                    #     print("if else")
                    #     print(fixed_line)
            # print("final")
            # print(fixed_line)
            schematic.append(fixed_line)
            # print(schematic)

        print(schematic)

        for i in range(len(schematic)):  # Row
            for j in range(len(schematic[i])):  # Column
                # print(f"location: {i},{j}")
                if num_to_ignore == 0:
                    try:
                        current_int = int(schematic[i][j])  #114
                        # print(current_int)
                        if current_int != 0:  # We care about checking to see if we can add this or not
                            # print(current_int)
                            # print("ignore: ", num_to_ignore)
                            num_len = len(schematic[i][j])
                            symbols_found = False
                            for k in range(num_len):
                                # print(current_int, k)
                                print(f"{i}, {j}, {k}, {len(schematic[i])}")
                                # Check if symbol is surrounding number
                                if i == 0:
                                    if j == 0:
                                        if not((is_int(schematic[i][j+1+k]) or schematic[i][j+1+k] == '.') and
                                               (is_int(schematic[i+1][j+k]) or schematic[i+1][j+k] == '.') and
                                               (is_int(schematic[i+1][j+1+k]) or schematic[i+1][j+1+k] == '.')):
                                            # Symbols found for this round of K
                                            print("found symbols: 1")
                                            symbols_found = True
                                    elif j >= len(schematic[i])-num_len:
                                        if not((is_int(schematic[i][j-1+k]) or schematic[i][j-1+k] == '.') and
                                                (is_int(schematic[i+1][j-1+k]) or schematic[i+1][j-1+k] == '.') and
                                                (is_int(schematic[i+1][j+k]) or schematic[i+1][j+k] == '.')):
                                            # Symbols found for this round of K
                                            print("found symbols: 2")
                                            symbols_found = True
                                    else:
                                        # print(f"{i}, {j}, {k}")
                                        # print('"'+schematic[i][j-1+k]+'"')
                                        # print(schematic[i][j-1+k] != '.')
                                        # print((is_int(schematic[i][j-1+k]) or schematic[i][j-1+k] != '.'))
                                        # print((is_int(schematic[i][j+1+k]) or schematic[i][j+1+k] != '.'))
                                        # print((is_int(schematic[i+1][j-1+k]) or schematic[i+1][j-1+k] != '.'))
                                        # print((is_int(schematic[i+1][j+k]) or schematic[i+1][j+k] != '.'))
                                        # print((is_int(schematic[i+1][j+1+k]) or schematic[i+1][j+1+k] != '.'))
                                        if not((is_int(schematic[i][j-1+k]) or schematic[i][j-1+k] == '.') and
                                                (is_int(schematic[i][j+1+k]) or schematic[i][j+1+k] == '.') and
                                                (is_int(schematic[i+1][j-1+k]) or schematic[i+1][j-1+k] == '.') and
                                                (is_int(schematic[i+1][j+k]) or schematic[i+1][j+k] == '.') and
                                                (is_int(schematic[i+1][j+1+k]) or schematic[i+1][j+1+k] == '.')):
                                            # Symbols found for this round of K
                                            # print(is_int(schematic[i][j-1+k]))
                                            # print(is_int(schematic[i][j+1+k]))
                                            # print(is_int(schematic[i+1][j-1+k]))
                                            # print(is_int(schematic[i+1][j+k]))
                                            # print(is_int(schematic[i+1][j+1+k]))
                                            print("found symbols: 3")
                                            symbols_found = True

                                elif i == len(schematic)-1:
                                    if j == 0:
                                        if not((is_int(schematic[i-1][j+k]) or schematic[i-1][j+k] == '.') and
                                                (is_int(schematic[i-1][j+1+k]) or schematic[i-1][j+1+k] == '.') and
                                                (is_int(schematic[i][j+1+k]) or schematic[i][j+1+k] == '.')):
                                            # No symbols found for this round of K
                                            print("found symbols: 4")
                                            symbols_found = True

                                    elif j >= len(schematic[i])-num_len:
                                        if not((is_int(schematic[i-1][j-1+k]) or schematic[i-1][j-1+k] == '.') and
                                                (is_int(schematic[i-1][j+k]) or schematic[i-1][j+k] == '.') and
                                                (is_int(schematic[i][j-1+k]) or schematic[i][j-1+k] == '.')):
                                            # No symbols found for this round of K
                                            print("found symbols: 5")
                                            symbols_found = True
                                    else:
                                        if not((is_int(schematic[i-1][j-1+k]) or schematic[i-1][j-1+k] == '.') and
                                                (is_int(schematic[i-1][j+k]) or schematic[i-1][j+k] == '.') and
                                                (is_int(schematic[i-1][j+1+k]) or schematic[i-1][j+1+k] == '.') and
                                                (is_int(schematic[i][j-1+k]) or schematic[i][j-1+k] == '.') and
                                                (is_int(schematic[i][j+1+k]) or schematic[i][j+1+k] == '.')):
                                            # No symbols found for this round of K
                                            print("found symbols: 6")
                                            symbols_found = True
                                else:
                                    if j == 0:
                                        if not((is_int(schematic[i-1][j+k]) or schematic[i-1][j+k] == '.') and
                                                (is_int(schematic[i-1][j+1+k]) or schematic[i-1][j+1+k] == '.') and
                                                (is_int(schematic[i][j+1+k]) or schematic[i][j+1+k] == '.') and
                                                (is_int(schematic[i+1][j+k]) or schematic[i+1][j+k] == '.') and
                                                (is_int(schematic[i+1][j+1+k]) or schematic[i+1][j+1+k] == '.')):
                                            # Symbols found for this round of K
                                            print("found symbols: 7")
                                            symbols_found = True
                                    elif j >= len(schematic[i])-num_len:
                                        if not((is_int(schematic[i-1][j-1+k]) or schematic[i-1][j-1+k] == '.') and
                                                (is_int(schematic[i-1][j+k]) or schematic[i-1][j+k] == '.') and
                                                (is_int(schematic[i][j-1+k]) or schematic[i][j-1+k] == '.') and
                                                (is_int(schematic[i+1][j-1+k]) or schematic[i+1][j-1+k] == '.') and
                                                (is_int(schematic[i+1][j+k]) or schematic[i+1][j+k] == '.')):
                                            # Symbols found for this round of K
                                            print("found symbols: 8")
                                            symbols_found = True
                                    else:
                                        # print(schematic[i][j])
                                        if not((is_int(schematic[i-1][j-1+k]) or schematic[i-1][j-1+k] == '.') and
                                                (is_int(schematic[i-1][j+k]) or schematic[i-1][j+k] == '.') and
                                                (is_int(schematic[i-1][j+1+k]) or schematic[i-1][j+1+k] == '.') and
                                                (is_int(schematic[i][j-1+k]) or schematic[i][j-1+k] == '.') and
                                                (is_int(schematic[i][j+1+k]) or schematic[i][j+1+k] == '.') and
                                                (is_int(schematic[i+1][j-1+k]) or schematic[i+1][j-1+k] == '.') and
                                                (is_int(schematic[i+1][j+k]) or schematic[i+1][j+k] == '.') and
                                                (is_int(schematic[i+1][j+1+k]) or schematic[i+1][j+1+k] == '.')):
                                            # Symbols found for this round of K
                                            print(f"found symbols: 9")
                                            symbols_found = True
                            # print(symbols_found)
                            if symbols_found:
                                # print("HERE")
                                print(current_int)
                                total_sum += current_int
                                # print(total_sum)
                            num_to_ignore = num_len-1
                            # print(f"ignore:{num_to_ignore}")
                    except ValueError:
                        # print(f"value seeen: {schematic[i][j]}")
                        pass

                else:
                    num_to_ignore -= 1
                    # print(f"IGNORE: {num_to_ignore}")
    return total_sum


def day_3_part2(sample_file_path, full_file_path):
    schematic = []
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    total_sum = 0
    with open(full_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()
            broken_line = list(line)
            fixed_line = []
            big_num = ""
            for i in range(len(broken_line)):
                if broken_line[i] in nums:
                    big_num += broken_line[i]
                else:
                    if big_num != "":
                        fixed_line.extend([big_num]*len(big_num))
                        fixed_line.append(broken_line[i])
                        big_num = ""
                    else:
                        fixed_line.append(broken_line[i])
                if i == len(broken_line) - 1:
                    # last in line, gotta get it on the roster
                    if big_num != "":
                        fixed_line.extend([big_num]*len(big_num))
                        big_num = ""
            schematic.append(fixed_line)

        print(schematic)

        for i in range(len(schematic)):  # Row
            for j in range(len(schematic[i])):  # Column
                if schematic[i][j] == '*':  # Found a gear
                    nums_around_gear = set()
                    for row_num in range(max(i-1, 0), min(len(schematic), i+2)):
                        for col_num in range(max(j-1, 0), min(len(schematic[i]), j+2)):
                            # go through surrounding places
                            if is_int(schematic[row_num][col_num]):
                                nums_around_gear.add(int(schematic[row_num][col_num]))
                    if len(nums_around_gear) == 2:
                        total_sum += (nums_around_gear.pop() * nums_around_gear.pop())
    return total_sum
