from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    order = {letter: num for num, letter in enumerate(ordered_dict.keys())}
    list_copy = list(ordered_dict.items())
    ordered_dict.clear()
    for _ in range(len(list_copy)):
        min_item = min(list_copy, key=lambda x: (x, (x[1], order[x[0]]))[by_values])
        key, value = list_copy.pop(list_copy.index(min_item))
        ordered_dict[key] = value

data1 = OrderedDict(e=11, b=22, a=99, g=33, c=33, d=33, h=99, f=77, i=88, k=44)
custom_sort(data1, by_values=True)

print(*data1.items())


