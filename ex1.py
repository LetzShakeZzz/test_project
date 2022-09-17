import timeit

code_to_test = """
from collections import OrderedDict

def custom_sort(data, by_values=False):
    if by_values:
        for key in sorted(data, key=lambda k: data[k]):
            data.move_to_end(key)
    else:
        for key in sorted(data):
            data.move_to_end(key)

data1 = OrderedDict({str(i): i for i in range(10000)})
custom_sort(data1, by_values=True)
"""

elapsed_time = timeit.timeit(code_to_test, number=1)/1
print(elapsed_time)