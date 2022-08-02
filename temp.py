from functools import reduce
from math import log

FILE_NAME = 'files.txt'
RATES = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3}
reverse_rates = {y: x for x, y in RATES.items()}


def convert(position):
    name, size, unit = position
    return int(size) * 1024 ** RATES[unit]


def calc_size(categories):
    total_bytes = reduce(lambda x, y: x + y, map(lambda x: convert(x), categories), 0)
    unit = reverse_rates[int(log(total_bytes, 1024))]
    total = round(total_bytes / 1024 ** int(log(total_bytes, 1024)))
    return (total, unit)


def parse_input(fh):
    parsed_files = {}
    lines = fh.readlines()
    for line in lines:
        full_name, size, unit = line.split()
        base_name, ext = full_name.split('.')

        if ext not in parsed_files:
            parsed_files[ext] = []

        parsed_files[ext].append([full_name, size, unit])

    return parsed_files


def print_stats(parsed_files):
    for ext in sorted(parsed_files.keys()):
        cat = parsed_files[ext]
        print(*map(lambda x: x[0], sorted(cat)), sep='\n')
        print('----------')
        total, unit = calc_size(cat)
        print(f'Summary: {total} {unit}')
        print()


def main():
    parsed_files = parse_input(open(FILE_NAME))
    print_stats(parsed_files)


if __name__ == "__main__":
    main()
