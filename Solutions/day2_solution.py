def day_2(sample_file_path, full_file_path):
    game_dict = {}
    possible_red = 12
    possible_green = 13
    possible_blue = 14

    total_sum = 0
    power_total = 0
    with open(full_file_path, 'r') as sample_f:
        for line in sample_f:
            line = line.strip()
            line_pieces = line.split(": ")
            # Set up tracking dict
            game_number = line_pieces[0].split(" ")[1]
            game_dict[game_number] = {
                "red": 0,
                "blue": 0,
                "green": 0
            }
            bag_contents = line_pieces[1]

            print(f"game number {game_number}")

            bag_contents_list = bag_contents.split("; ")
            for hand in bag_contents_list:
                hand_contents = hand.split(", ")

                # Grab most amount of blues seen across hands, hold onto it
                if any("blue" in item for item in hand_contents):
                    blue_item = [blue_thing for blue_thing in hand_contents if "blue" in blue_thing]
                    blue_count = int(blue_item[0].split(" ")[0])
                    if blue_count > game_dict[game_number]["blue"]:
                        game_dict[game_number]["blue"] = blue_count

                # Grab most amount of greens seen across hands, hold onto it
                if any("green" in item for item in hand_contents):
                    green_item = [green_thing for green_thing in hand_contents if "green" in green_thing]
                    green_count = int(green_item[0].split(" ")[0])
                    if green_count > game_dict[game_number]["green"]:
                        game_dict[game_number]["green"] = green_count

                # Grab most amount of reds seen across hands, hold onto it
                if any("red" in item for item in hand_contents):
                    red_item = [red_thing for red_thing in hand_contents if "red" in red_thing]
                    red_count = int(red_item[0].split(" ")[0])
                    if red_count > game_dict[game_number]["red"]:
                        game_dict[game_number]["red"] = red_count

        for item in game_dict.keys():
            # Check if game works with possible blocks
            if (game_dict[item]["blue"] <= possible_blue and
                    game_dict[item]["red"] <= possible_red and
                    game_dict[item]["green"] <= possible_green):
                total_sum += int(item)

            # Calculate power of each game
            power_total += (game_dict[item]["blue"] * game_dict[item]["red"] * game_dict[item]["green"])

    return total_sum, power_total
