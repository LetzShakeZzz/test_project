import timeit

code_to_test = """
from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    order = {letter: num for num, letter in enumerate(ordered_dict.keys())}
    list_copy = list(ordered_dict.items())
    ordered_dict.clear()
    for _ in range(len(list_copy)):
        min_item = min(list_copy, key=lambda x: (x, (x[1], order[x[0]]))[by_values])
        key, value = list_copy.pop(list_copy.index(min_item))
        ordered_dict[key] = value

data1 = OrderedDict({str(i): i for i in range(10000)})
custom_sort(data1, by_values=True)
"""

elapsed_time = timeit.timeit(code_to_test, number=1)
print(elapsed_time)