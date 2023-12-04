import re


def day_4_part1(sample_file_path, full_file_path):
    winning_nums = {}
    my_nums = {}
    total_winning_points = 0
    with open(full_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()
            split_line = re.split(r': | \| ', line)
            winning_nums[split_line[0]] = re.split(r' +', split_line[1])
            my_nums[split_line[0]] = re.split(r' +', split_line[2])
            print(winning_nums)
            print(my_nums)

        for key in my_nums.keys():
            winning_count = 0
            print(f"KEY: {key}")
            for num in my_nums[key]:
                if num in winning_nums[key]:
                    winning_count += 1
            if winning_count > 0:
                total_winning_points += (2**(winning_count-1))

    return total_winning_points


def day_4_part2(sample_file_path, full_file_path):
    winning_nums = {}
    my_nums = {}
    scratcher_count = {}
    total_scratchers = 0
    count = 1
    with open(full_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()
            split_line = re.split(r': | \| ', line)
            print(split_line)
            winning_nums[f"Card {count}"] = re.split(r' +', split_line[1])
            my_nums[f"Card {count}"] = re.split(r' +', split_line[2])
            scratcher_count[f"Card {count}"] = 0
            count += 1

        total_original_cards = len(my_nums)
        for card_id_count in range(total_original_cards):
            key = f"Card {card_id_count+1}"
            scratcher_count[key] += 1
            winning_count = 0
            for num in my_nums[key]:
                if num in winning_nums[key]:
                    winning_count += 1
            if winning_count > 0:
                for winning_id_count in range(winning_count):
                    count_key = f"Card {card_id_count+1+winning_id_count+1}"
                    scratcher_count[count_key] += (1*scratcher_count[key])
                    print(scratcher_count)

        for key in scratcher_count.keys():
            total_scratchers += scratcher_count[key]

    return total_scratchers
