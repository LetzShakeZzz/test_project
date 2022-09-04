from zipfile import ZipFile
from math import log

def calc_size(size):
    total = round(size / 1024 ** int(log(size, 1024)))
    unit = ('B', 'KB', 'MB', 'GB')[int(log(size, 1024))]
    return f' {total} {unit}'

with ZipFile('desktop.zip') as zip_file:
    for entry in zip_file.infolist():
        name = entry.filename.rstrip('/')
        spaces = len(name.split('/')) - 1
        size = calc_size(entry.file_size) if entry.file_size else ''
        print(f"{'  ' * spaces}{name.split('/')[-1]}{size}")