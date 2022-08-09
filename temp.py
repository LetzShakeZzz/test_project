import time


def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


t = time.perf_counter()
for_and_append()
print(f"for_and_append     = {time.perf_counter() - t} с.")

t = time.perf_counter()
list_comprehension()
print(f"list_comprehension = {time.perf_counter() - t} с.")