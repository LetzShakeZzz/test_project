from functools import reduce
from math import log

rates = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3}
reversed_rates = {y: x for x, y in rates.items()}


def convert(position):
    full_name, size, unit = position
    return int(size) * 1024 ** rates[unit]


def calc_size(cats):
    total = reduce(lambda x, y: x + y, map(lambda x: convert(x), cats), 0)
    unit = reversed_rates[int(log(total, 1024))]
    total = round(total / 1024 ** int(log(total, 1024)))
    return (total, unit)


with open('files.txt') as file:
    files = {}

    for line in file.readlines():
        full_name, size, unit = line.split()
        base_name, ext = full_name.split('.')
        if ext not in files:
            files[ext] = []
        files[ext].append([full_name, size, unit])

    for ext in sorted(files.keys()):
        cat = files[ext]
        print(*map(lambda x: '.'.join(x[:1]), sorted(cat)), sep='\n')
        print('----------')
        total, unit = calc_size(cat)
        print(f'Summary: {total} {unit}')
        print()