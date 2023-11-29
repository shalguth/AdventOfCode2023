

def day_1(sample_file_path, full_file_path):
    with open(sample_file_path, 'r') as sample_f:
        sample_line = sample_f.readline()
    with open(full_file_path, 'r') as full_f:
        full_line = full_f.readline()

    return int(sample_line) + int(full_line)
