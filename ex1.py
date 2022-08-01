from functools import reduce
from math import log

def convert(position):
    rates = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3}
    name, ext, size, unit = position
    return int(size) * 1024 ** rates[unit]

def calc_size(cats):
    rates = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}
    total = reduce(lambda x, y: x + y, map(lambda x: convert(x), cats), 0)
    unit = rates[int(log(total, 1024))]
    total = round(total / 1024 ** int(log(total, 1024)))
    return (total, unit)

def main(input_file):
    with open(input_file) as file:
        file_lines = file.readlines()

        extensions = set()
        temp_files = []
        for line in file_lines:
            name, size, unit = line.split()
            name, ext = name.split('.')
            extensions.add(ext)
            temp_files.append([name, ext, size, unit])

        extensions = {ext: num for num, ext in enumerate(extensions)}

        sorted_files = [[] for _ in range(len(extensions))]
        for position in temp_files:
            ext = position[1]
            sorted_files[extensions[ext]].append(position)

        for cat in sorted(sorted_files, key=lambda x: x[0][1]):
            print(*map(lambda x: '.'.join(x[:2]), sorted(cat)), sep='\n')
            print('----------')
            total, unit = calc_size(cat)
            print(f'Summary: {total} {unit}')
            print()

main('files.txt')